import com.sun.jdi.*;
import com.sun.jdi.connect.*;
import com.sun.jdi.event.*;
import com.sun.jdi.request.*;
import java.io.*;
import java.util.*;

/** Merekam eksekusi program Java baris per baris dengan Java Debug Interface (dipakai tools/gen/traces.py).
 *  Pemakaian: java JTrace.java <folder kelas> <NamaKelasUtama>
 *  Keluaran (stdout): JSON {steps, out, cut, err}. Setiap langkah: [baris, method, {variabel: nilai}, panjang keluaran]. */
public class JTrace {
    static final int MAX = 200;
    static final StringBuffer OUT = new StringBuffer();

    public static void main(String[] a) throws Exception {
        String dir = a[0], main = a[1], file = main + ".java";
        LaunchingConnector lc = Bootstrap.virtualMachineManager().defaultConnector();
        Map<String, Connector.Argument> args = lc.defaultArguments();
        args.get("main").setValue(main);
        args.get("options").setValue("-cp " + dir + " -Xshare:off");
        VirtualMachine vm = lc.launch(args);
        Thread pump = new Thread(() -> {
            try (Reader r = new InputStreamReader(vm.process().getInputStream(), "UTF-8")) {
                int c; while ((c = r.read()) >= 0) OUT.append((char) c);
            } catch (IOException e) { }
        });
        pump.start();
        new Thread(() -> { try { vm.process().getErrorStream().transferTo(OutputStream.nullOutputStream()); } catch (IOException e) { } }).start();
        EventRequestManager erm = vm.eventRequestManager();
        MethodEntryRequest me = erm.createMethodEntryRequest();
        me.addClassFilter(main);
        me.setSuspendPolicy(EventRequest.SUSPEND_EVENT_THREAD);
        me.enable();
        List<String> steps = new ArrayList<>();
        boolean cut = false, err = false;
        StepRequest step = null;
        loop:
        while (true) {
            EventSet set = vm.eventQueue().remove();
            for (Event ev : set) {
                if (ev instanceof MethodEntryEvent mev && step == null) {
                    me.disable();
                    step = erm.createStepRequest(mev.thread(), StepRequest.STEP_LINE, StepRequest.STEP_INTO);
                    for (String p : new String[]{"java.*", "javax.*", "jdk.*", "sun.*", "com.sun.*"}) step.addClassExclusionFilter(p);
                    step.setSuspendPolicy(EventRequest.SUSPEND_EVENT_THREAD);
                    step.enable();
                    Location loc = mev.location();
                    steps.add("[" + loc.lineNumber() + "," + js(loc.method().name()) + "," + vars(mev.thread()) + ",0]");
                } else if (ev instanceof StepEvent se) {
                    Location loc = se.location();
                    String src;
                    try { src = loc.sourceName(); } catch (AbsentInformationException e) { src = ""; }
                    if (src.equals(file)) {
                        if (steps.size() >= MAX) { cut = true; break loop; }
                        Thread.sleep(3);
                        steps.add("[" + loc.lineNumber() + "," + js(loc.method().name()) + "," + vars(se.thread()) + "," + OUT.length() + "]");
                    }
                } else if (ev instanceof ExceptionEvent) {
                    err = true;
                } else if (ev instanceof VMDeathEvent || ev instanceof VMDisconnectEvent) {
                    break loop;
                }
            }
            set.resume();
        }
        if (cut) try { vm.exit(0); } catch (Exception e) { }
        pump.join(3000);
        int code = 0;
        try { code = vm.process().waitFor(); } catch (Exception e) { }
        String last = steps.isEmpty() ? "{}" : lastVars(steps.get(steps.size() - 1));
        steps.add("[0,\"main\"," + last + "," + OUT.length() + "]");
        System.out.println("{\"steps\":[" + String.join(",", steps) + "],\"out\":" + js(OUT.toString()) + ",\"cut\":" + cut + ",\"err\":" + (code != 0 && !cut ? "\"error\"" : "null") + "}");
    }

    static String lastVars(String step) {
        int i = step.indexOf('{'), j = step.lastIndexOf('}');
        return i >= 0 && j > i ? step.substring(i, j + 1) : "{}";
    }

    static String vars(ThreadReference t) throws Exception {
        StackFrame f = t.frame(0);
        StringBuilder sb = new StringBuilder("{");
        try {
            for (LocalVariable v : f.visibleVariables()) {
                if (v.name().equals("args")) continue;
                if (sb.length() > 1) sb.append(',');
                sb.append(js(v.name())).append(':').append(js(cut(fmt(f.getValue(v), 0))));
            }
        } catch (AbsentInformationException e) { }
        return sb.append('}').toString();
    }

    static String cut(String s) { return s.length() <= 48 ? s : s.substring(0, 45) + "…"; }

    static String fmt(Value v, int depth) {
        if (v == null) return "null";
        if (v instanceof StringReference s) return '"' + s.value() + '"';
        if (v instanceof CharValue c) return "'" + c.value() + "'";
        if (v instanceof PrimitiveValue) return v.toString();
        if (v instanceof ArrayReference ar) {
            if (depth > 1) return "[…]";
            List<String> xs = new ArrayList<>();
            int n = Math.min(ar.length(), 8);
            for (int i = 0; i < n; i++) xs.add(fmt(ar.getValue(i), depth + 1));
            return "[" + String.join(", ", xs) + (ar.length() > 8 ? ", …" : "") + "]";
        }
        ObjectReference o = (ObjectReference) v;
        ReferenceType rt = o.referenceType();
        String name = rt.name();
        String simple = name.substring(name.lastIndexOf('.') + 1);
        if (name.startsWith("java.lang.") && rt.fieldByName("value") != null && !name.equals("java.lang.String")) return fmt(o.getValue(rt.fieldByName("value")), depth);
        if ((name.equals("java.util.ArrayList") || name.equals("java.util.LinkedList")) && depth < 2) {
            Field sz = rt.fieldByName("size"), data = rt.fieldByName("elementData");
            int size = ((IntegerValue) o.getValue(sz)).value();
            if (data != null) {
                ArrayReference ar = (ArrayReference) o.getValue(data);
                List<String> xs = new ArrayList<>();
                for (int i = 0; i < Math.min(size, 8); i++) xs.add(fmt(ar.getValue(i), depth + 1));
                return "[" + String.join(", ", xs) + (size > 8 ? ", …" : "") + "]";
            }
            return simple + "(" + size + ")";
        }
        Field sz = rt.fieldByName("size");
        if (sz != null && name.startsWith("java.util.")) {
            Value s = o.getValue(sz);
            if (s instanceof IntegerValue iv) return simple + "(" + iv.value() + " isi)";
        }
        if (depth < 1 && !name.startsWith("java.")) {
            List<String> xs = new ArrayList<>();
            for (Field fl : rt.visibleFields()) {
                if (fl.isStatic()) continue;
                xs.add(fl.name() + "=" + fmt(o.getValue(fl), depth + 1));
                if (xs.size() >= 4) break;
            }
            return simple + "{" + String.join(", ", xs) + "}";
        }
        return simple;
    }

    static String js(String s) {
        StringBuilder sb = new StringBuilder("\"");
        for (char c : s.toCharArray()) {
            switch (c) {
                case '"' -> sb.append("\\\"");
                case '\\' -> sb.append("\\\\");
                case '\n' -> sb.append("\\n");
                case '\r' -> sb.append("\\r");
                case '\t' -> sb.append("\\t");
                default -> { if (c < 0x20) sb.append(String.format("\\u%04x", (int) c)); else sb.append(c); }
            }
        }
        return sb.append('"').toString();
    }
}
