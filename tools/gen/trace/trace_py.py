"""Merekam eksekusi program Python baris per baris (dipakai tools/gen/traces.py).

Masukan (stdin): kode program. Keluaran (stdout): JSON {steps, out, cut}.
Setiap langkah: [baris yang akan dijalankan, nama fungsi, variabel lokal {nama: repr}, panjang keluaran sejauh ini].
"""
import io
import json
import sys
import types

MAX = 200
code = sys.stdin.read()
buf = io.StringIO()
steps = []


class Cut(Exception):
    pass


def rep(v):
    try:
        r = repr(v)
    except Exception:
        r = "?"
    return r if len(r) <= 48 else r[:45] + "…"


def snap(frame):
    out = {}
    for k, v in frame.f_locals.items():
        if k.startswith("__") or isinstance(v, (types.ModuleType, types.FunctionType, type, types.BuiltinFunctionType)):
            continue
        out[k] = rep(v)
    return out


def tracer(frame, event, arg):
    if frame.f_code.co_filename != "<main>":
        return None
    if event == "line":
        if len(steps) >= MAX:
            raise Cut()
        steps.append([frame.f_lineno, frame.f_code.co_name, snap(frame), len(buf.getvalue())])
    return tracer


g = {"__name__": "__main__"}
cut = False
err = None
real = sys.stdout
sys.stdout = buf
sys.stdin = io.StringIO("")
try:
    sys.settrace(tracer)
    exec(compile(code, "<main>", "exec"), g)
except Cut:
    cut = True
except BaseException as e:  # program error atau input(): langkahnya tidak dipakai
    err = type(e).__name__
finally:
    sys.settrace(None)
    sys.stdout = real
final = {k: rep(v) for k, v in g.items() if not k.startswith("__") and not isinstance(v, (types.ModuleType, types.FunctionType, type))}
steps.append([0, "<module>", final, len(buf.getvalue())])
json.dump({"steps": steps, "out": buf.getvalue(), "cut": cut, "err": err}, sys.stdout, ensure_ascii=False)
