"""Menjalankan setiap contoh di src/contoh/<jalur>.json dan membandingkan keluarannya dengan "out".

Bahasa yang bisa dijalankan: python, js, ts (node --experimental-strip-types), java (java Berkas.java),
dart dan kotlin (bila SDK ada di /opt/sdk). Bahasa lain (sql, html, ...) dilewati dan dilaporkan sebagai "tidak dijalankan".
Contoh yang memakai input() / Scanner / prompt dilewati karena butuh masukan pengguna.

Jalankan: python3 tools/cek/jalankan.py <jalur> [--bahasa python]"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "build"))
from contoh import muat  # noqa: E402

DART = "/opt/sdk/dart-sdk/bin/dart"  # unduh: storage.googleapis.com/dart-archive (stable, linux-x64)
KT = "/opt/sdk/kt"  # jar kotlin-compiler-embeddable 2.2.0 + dependensinya dari Maven Central
BUTUH_INPUT = ("input(", "Scanner(", "prompt(", "readLine(", "readline")


def jalankan(lang, code):
    with tempfile.TemporaryDirectory() as d:
        if lang == "python":
            f = Path(d) / "contoh.py"; f.write_text(code); cmd = [sys.executable, "-I", str(f)]
        elif lang in ("js", "javascript"):
            f = Path(d) / "contoh.mjs"; f.write_text(code); cmd = ["node", str(f)]
        elif lang == "ts":
            f = Path(d) / "contoh.mts"; f.write_text(code); cmd = ["node", "--experimental-strip-types", "--no-warnings", str(f)]
        elif lang == "java":
            f = Path(d) / "Contoh.java"; f.write_text(code); cmd = ["java", str(f)]
        elif lang == "dart" and Path(DART).exists():
            f = Path(d) / "contoh.dart"; f.write_text(code); cmd = [DART, "run", str(f)]
        elif lang == "kotlin" and Path(KT).exists():
            f = Path(d) / "Contoh.kt"; f.write_text(code)
            std = f"{KT}/kotlin-stdlib-2.2.0.jar"
            r = subprocess.run(["java", "-cp", f"{KT}/*", "org.jetbrains.kotlin.cli.jvm.K2JVMCompiler", "-no-stdlib", "-no-reflect",
                                "-cp", std, str(f), "-d", f"{d}/out"], capture_output=True, text=True, timeout=120, cwd=d)
            if r.returncode:
                return "[gagal kompilasi]\n" + r.stderr
            cmd = ["java", "-cp", f"{d}/out:{std}", "ContohKt"]
        else:
            return None
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=d)
        return r.stdout + (("\n[stderr]\n" + r.stderr) if r.returncode else "")


def main(track, lang_paksa=None):
    cat = json.loads((ROOT / "web" / "src" / "data" / "catalog.json").read_text())
    bodies = json.loads((ROOT / "web" / "src" / "data" / "t" / f"{track}.json").read_text())
    byid = {b["id"]: b for b in bodies.values()}
    data = muat(ROOT, track)
    ok = beda = lewat = 0
    for lid, c in data.items():
        lang = lang_paksa or byid[lid].get("lang")
        items = []
        if c.get("code"):
            items.append(("contoh 1", c["code"], c.get("out"), lang))
        items += [(f"contoh {i + 2}", e["code"], e.get("out"), lang) for i, e in enumerate(c.get("exs") or [])]
        items += [(f"pendalaman {i + 1}", e["code"], e.get("out"), e.get("lang", lang)) for i, e in enumerate(c.get("cx") or [])]
        for label, code, out, lg in items:
            if out is None or any(k in code for k in BUTUH_INPUT):
                lewat += 1
                continue
            got = jalankan(lg, code)
            if got is None:
                lewat += 1
                continue
            if got.rstrip() == out.rstrip():
                ok += 1
            else:
                beda += 1
                print(f"✗ {lid} [{label}]\n--- diharapkan\n{out.rstrip()}\n--- didapat\n{got.rstrip()}\n")
    print(f"{track}: {ok} cocok, {beda} beda, {lewat} tidak dijalankan")
    return beda


if __name__ == "__main__":
    a = sys.argv[1:]
    lp = None
    if "--bahasa" in a:
        k = a.index("--bahasa"); lp = a[k + 1]; del a[k:k + 2]
    sys.exit(1 if sum(main(t, lp) for t in a) else 0)
