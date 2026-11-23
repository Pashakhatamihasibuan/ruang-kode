"""Lapisan contoh bertahap: src/contoh/<jalur>.json (atau <jalur>.<bagian>.json) ditimpakan ke isi pelajaran hasil ekspor.

Format (dikunci dengan id pelajaran, misalnya "python-1-3"):
{
  "<id>": {
    "code": "...", "out": "...",          # opsional: ganti contoh utama yang melompat materi
    "trs": [["kalimat", "baris kode"]],   # opsional: tabel "Dari kalimat ke kode" untuk contoh utama baru
    "exs": [{"t": "Judul kasus", "d": "penjelasan singkat (opsional)", "code": "...", "out": "..."}],
    "cx":  [{"t": "Judul kasus nyata", "b": "penjelasan", "code": "...", "out": "..."}]  # ganti seluruh Pendalaman
  }
}
Semua contoh hanya boleh memakai konsep yang sudah diajarkan sampai pelajaran itu (dicek tools/cek/urutan.py)."""
import json
from pathlib import Path

KUNCI = {"code", "out", "trs", "exs", "cx"}


def muat(root, track):
    """Gabungkan src/contoh/<jalur>.json dan src/contoh/<jalur>.<bagian>.json (jalur besar dipecah per bagian)."""
    d = Path(root) / "src" / "contoh"
    files = ([d / f"{track}.json"] if (d / f"{track}.json").exists() else []) + sorted(d.glob(f"{track}.*.json"))
    data = {}
    for f in files:
        for lid, c in json.loads(f.read_text()).items():
            if lid in data:
                raise SystemExit(f"{f.name}: id {lid} sudah ada di berkas contoh lain")
            data[lid] = c
    return data


def terapkan(data, bodies, nama="contoh"):
    byid = {b["id"]: b for b in bodies.values()}
    for lid, c in data.items():
        b = byid.get(lid)
        if not b:
            raise SystemExit(f"{nama}: id pelajaran tidak dikenal: {lid}")
        asing = set(c) - KUNCI
        if asing:
            raise SystemExit(f"{nama}: {lid}: kunci tidak dikenal {sorted(asing)}")
        if c.get("code"):
            b["code"] = c["code"]
            b["out"] = c.get("out")
            b.pop("trc", None)  # jejak langkah lama tidak cocok lagi dengan kode baru
            b.pop("fig", None)
            if c.get("trs"):
                b["trs"] = c["trs"]
            else:
                b.pop("trs", None)
        for e in c.get("exs") or []:
            if not e.get("t") or not e.get("code"):
                raise SystemExit(f"{nama}: {lid}: setiap exs butuh t dan code")
        if c.get("exs"):
            b["exs"] = [{"t": e["t"], "code": e["code"], "out": e.get("out"), "d": e.get("d")} for e in c["exs"]]
        if "cx" in c:
            deep = b.setdefault("deep", {"ist": [], "cx": []})
            deep["cx"] = [{"t": x["t"], "b": x.get("b", ""), "code": x["code"], "lang": x.get("lang", b.get("lang")), "out": x.get("out")}
                          for x in c["cx"]]
