"""Membuat src/js/traces.js: rekaman "jalankan baris per baris" untuk contoh kode pelajaran.

Setiap contoh kode Python, Java, JavaScript, dan TypeScript di jalur pemrograman dijalankan
dengan pelacak (tools/gen/trace/): baris yang akan dijalankan, isi variabel, dan keluaran
dicatat langkah demi langkah. Hasilnya dipakai tombol "Jalankan langkah demi langkah".
Butuh Python 3, JDK 21, dan Node 22. Jalankan dari akar repo: python3 tools/gen/traces.py
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bugs import lessons, CONST_LANG, CONST_KEY  # noqa: E402
from tips import ROOT, HERE  # noqa: E402

TR = HERE / "trace"
TRACKS = {"PY_MODULES", "JAVA_MODULES", "TS_MODULES", "FE0_MODULES", "FE_MODULES"}


def trace_py(code):
    with tempfile.TemporaryDirectory() as d:  # program contoh boleh menulis berkas; jangan di akar repo
        r = subprocess.run(["python3", "-I", str(TR / "trace_py.py")], input=code, capture_output=True, text=True, timeout=60, cwd=d)
    return json.loads(r.stdout) if r.returncode == 0 else None


def trace_js(code, ext):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d, "main" + ext)
        f.write_text(code)
        r = subprocess.run(["node", str(TR / "trace_js.js"), str(f)], capture_output=True, text=True, timeout=60, cwd=d)
        return json.loads(r.stdout) if r.stdout.strip() else None


JT = None


def trace_java(code):
    global JT
    if JT is None:
        JT = tempfile.mkdtemp()
        subprocess.run(["javac", "-d", JT, str(TR / "JTrace.java")], check=True, capture_output=True)
    m = re.search(r"public\s+class\s+(\w+)", code)
    if not m:
        return None
    with tempfile.TemporaryDirectory() as d:
        Path(d, m.group(1) + ".java").write_text(code)
        c = subprocess.run(["javac", "-g", m.group(1) + ".java"], cwd=d, capture_output=True, text=True)
        if c.returncode:
            return None
        r = subprocess.run(["java", "-cp", JT, "JTrace", d, m.group(1)], capture_output=True, text=True, timeout=60, cwd=d)
        line = next((x for x in r.stdout.splitlines() if x.startswith("{")), None)
        return json.loads(line) if line else None


def compact(t, code):
    """Buang langkah ganda dan baris di luar kode, lalu simpan variabel sebagai perubahan saja."""
    n = len(code.split("\n"))
    steps, prev = [], None
    for ln, fn, vs, o in t["steps"]:
        if ln > n:
            continue
        cur = (ln, fn, json.dumps(vs, sort_keys=True), o)
        if cur == prev:
            continue
        prev = cur
        steps.append([ln, fn, vs, o])
    out, pf, pv = [], None, {}
    for ln, fn, vs, o in steps:
        if fn != pf:
            out.append([ln, fn, vs, o, 1])
        else:
            diff = {k: v for k, v in vs.items() if pv.get(k) != v}
            gone = [k for k in pv if k not in vs]
            if gone:
                diff["-"] = gone
            out.append([ln, fn, diff, o])
        pf, pv = fn, vs
    return {"s": out, "o": t["out"], "cut": t["cut"]}


def main():
    res = {}
    for L in lessons():
        if L["c"] not in TRACKS:
            continue
        lang = L["lang"] or CONST_LANG[L["c"]]
        code = L["code"]
        try:
            t = {"python": lambda: trace_py(code), "java": lambda: trace_java(code),
                 "js": lambda: trace_js(code, ".js"), "ts": lambda: trace_js(code, ".ts")}.get(lang, lambda: None)()
        except subprocess.TimeoutExpired:
            t = None
        key = CONST_KEY[L["c"]] + ":" + L["t"]
        ok = t and not t.get("err") and len(t["steps"]) >= 3
        print("✓" if ok else "·", key, len(t["steps"]) if t else "-", (t or {}).get("err") or "")
        if ok:
            res[key] = compact(t, code)
    tpl = (HERE / "traces.tpl.js").read_text()
    (ROOT / "src/js/traces.js").write_text(tpl.replace("%TRACES%", json.dumps(res, ensure_ascii=False, separators=(",", ":"))))
    print(len(res), "rekaman ditulis ke src/js/traces.js")


if __name__ == "__main__":
    main()
