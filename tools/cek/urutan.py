"""Pemeriksa contoh bertahap.

1. Urutan konsep: menandai contoh (contoh utama, contoh lain, dan kasus Pendalaman) yang memakai konsep
   sebelum konsep itu diajarkan di jalurnya.
2. Jumlah contoh: menandai pelajaran berkode yang belum punya minimal 2 contoh lain.

Aturan per jalur ada di tools/cek/aturan/<jalur>.json:
  {"aturan": [["nama konsep", "regex di kode", "regex judul pelajaran yang memperkenalkannya"], ...],
   "abaikan": ["id pelajaran yang tidak dicek jumlah contohnya, misalnya pelajaran instalasi"]}
Konsep dianggap sudah diajarkan mulai pelajaran pertama yang judulnya cocok. Konsep yang judulnya tidak
ditemukan di jalur dianggap tidak pernah diajarkan, jadi setiap pemakaiannya dilaporkan.
Isi src/contoh/<jalur>.json diterapkan dulu, jadi hasil cek sama dengan yang tampil di situs.

Jalankan: python3 tools/cek/urutan.py [jalur ...] [--min N]"""
import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "web" / "src" / "data"
ATURAN = Path(__file__).resolve().parent / "aturan"
sys.path.insert(0, str(ROOT / "tools" / "build"))
from contoh import muat, terapkan  # noqa: E402


def isi(track):
    bodies = copy.deepcopy(json.loads((DATA / "t" / f"{track}.json").read_text()))
    terapkan(muat(ROOT, track), bodies, f"src/contoh/{track}.json")
    return bodies


def cek(track, cfg, minimal=2):
    rules = cfg["aturan"]
    cat = json.loads((DATA / "catalog.json").read_text())
    t = next(x for x in cat["tracks"] if x["k"] == track)
    bodies = isi(track)
    order = [l for m in t["mods"] for l in m["lessons"] if l["k"] != "see"]
    intro = {}
    for i, l in enumerate(order):
        for name, _, title_rx in rules:
            if name not in intro and re.search(title_rx, l["title"], re.I):
                intro[name] = i
    lompat, kurang = [], []
    skip = set(cfg.get("abaikan") or [])
    for i, l in enumerate(order):
        b = bodies.get(l["slug"], {})
        codes = [("contoh 1", b.get("code") or "")]
        codes += [(f"contoh {j + 2}", e.get("code", "")) for j, e in enumerate(b.get("exs") or [])]
        codes += [(f"konsol {j + 1}", e[1]) for j, e in enumerate(b.get("ex") or []) if isinstance(e, list) and len(e) == 2]
        codes += [(f"pendalaman {j + 1}", e.get("code", "")) for j, e in enumerate((b.get("deep") or {}).get("cx") or [])]
        for label, code in codes:
            if not code:
                continue
            hits = [name for name, rx, _ in rules if intro.get(name, 10**9) > i and re.search(rx, code, re.M)]
            if hits:
                lompat.append((i + 1, b.get("id"), l["title"], label, hits))
        if b.get("code") and b.get("k") != "w" and b.get("id") not in skip and len(b.get("exs") or []) < minimal:
            kurang.append((i + 1, b.get("id"), l["title"], len(b.get("exs") or [])))
    return lompat, kurang


if __name__ == "__main__":
    args = sys.argv[1:]
    minimal = 2
    if "--min" in args:
        k = args.index("--min")
        minimal = int(args[k + 1])
        del args[k:k + 2]
    tracks = args or sorted(p.stem for p in ATURAN.glob("*.json"))
    total = 0
    for tk in tracks:
        f = ATURAN / f"{tk}.json"
        if not f.exists():
            print(f"== {tk}: belum ada aturan di {f.relative_to(ROOT)}")
            total += 1
            continue
        lompat, kurang = cek(tk, json.loads(f.read_text()), minimal)
        total += len(lompat) + len(kurang)
        print(f"== {tk}: {len(lompat)} contoh melompat, {len(kurang)} pelajaran dengan contoh lain < {minimal}")
        for n, lid, title, label, hits in lompat:
            print(f"  {n:3}. {lid} {title} [{label}]: {', '.join(hits)}")
        for n, lid, title, k in kurang:
            print(f"  {n:3}. {lid} {title}: baru {k} contoh lain")
    sys.exit(1 if total else 0)
