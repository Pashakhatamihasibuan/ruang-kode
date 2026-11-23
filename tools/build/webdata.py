"""Ekspor kurikulum ke JSON untuk aplikasi Next.js di web/.

Keluaran (web/src/data/):
  catalog.json   daftar jalur, modul, dan pelajaran (tanpa isi), jalur karier, grup
  t/<jalur>.json isi lengkap setiap pelajaran milik jalur itu, dikunci dengan slug
  glossary.json  istilah glosarium
Semua jenis pelajaran dinormalkan: bab Java/Python (lab) dan topik diubah menjadi bentuk yang sama
dengan pelajaran konsep, sehingga satu komponen React bisa merender semuanya."""
import json
import re
import subprocess
from pathlib import Path

from . import site
from .contoh import muat, terapkan

KIND = site.KIND


def _quiz(items):
    """Soal menjadi bentuk seragam {q,o,a,w} dengan HTML aman (teks biasa di-escape)."""
    out = []
    for it in items or []:
        if isinstance(it, list):
            q, o, a, w = it
            out.append({"q": q, "o": o, "a": a, "w": w, "html": False})
        else:
            out.append({"q": it["q"], "o": it["o"], "a": it["a"], "w": it["w"], "html": True})
    return out


def _normal(t, l, book):
    """Isi satu pelajaran dalam bentuk seragam untuk React."""
    lang = l.get("lang") or t["lang"]
    k = l["k"]
    keep = {kk: v for kk, v in l.items() if kk not in ("src", "src_tk", "ref", "_t", "t", "n", "qn", "q")}
    keep["lang"] = lang
    if k == "lab":
        c = book[{"java": "CHJ", "python": "CHP"}.get(t["k"], "CH")][l["n"] - 1]
        lg = "java" if t["k"] == "java" else "python"
        o = c.get("out")
        o = o.get(lg) if isinstance(o, dict) else o
        keep.update({"b": c["body"], "code": c[lg], "lang": lg, "out": o, "pts": c.get("points") or [], "q": _quiz(c["quiz"])})
    elif k == "topic":
        n, i = map(int, l["ref"].split("."))
        tp = book["TOPICS"][str(n)][i]
        java = t["k"] == "java"
        lg = "java" if java else "python"
        keep.update({"lang": lg, "code": tp[lg], "trs": [[r[0], r[1 if java else 2]] for r in (tp["tr"] if java else tp["trp"])],
                     "b": [f"Topik ini melatih cara menerjemahkan kalimat sehari-hari menjadi kode {'Java' if java else 'Python'}, langkah demi langkah."]})
    else:
        keep["q"] = _quiz(l.get("q"))
    return keep


def _eval_js(src, expr):
    js = src + f"\n;process.stdout.write(JSON.stringify({expr}));"
    r = subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def _colors(css):
    """Warna aksen per jalur dari tema-jalur.css (terang dan gelap)."""
    blocks = re.findall(r"(:root[^{]*)\{([^}]*)\}", css)
    light, dark = {}, {}
    for sel, body in blocks:
        vals = dict(re.findall(r"--c-([a-z0-9]+):(#[0-9A-Fa-f]{6})", body))
        (dark if "dark" in sel else light).update(vals)
    return light, dark


def export(root, app_js, data, keys, deep):
    out = root / "web" / "src" / "data"
    (out / "t").mkdir(parents=True, exist_ok=True)
    tracks = site.tracks_meta(app_js, data, keys)
    book = data["book"]
    marks = dict(re.findall(r"\{k:'(\w+)'[^}]*?mark:'((?:[^'\\]|\\.)*)'", app_js))
    light, dark = _colors((root / "src" / "css" / "tema-jalur.css").read_text())
    byk = {t["k"]: t for t in tracks}

    catalog = []
    for t in tracks:
        dk = deep.get(t["k"], {})
        mods_meta, bodies = [], {}
        for mi, m in enumerate(t["mods"]):
            ls = []
            for li, l in enumerate(m["lessons"]):
                if l["k"] == "see":
                    src = l.get("src")
                    if not src:
                        continue
                    ls.append({"id": l["id"], "k": "see", "title": l["title"], "src": l["src_tk"], "slug": src["slug"],
                               "srcId": src["id"], "kind": KIND.get(src["k"], "Konsep & kode"),
                               "srcName": byk[l["src_tk"]]["name"]})
                    continue
                qn = len(l.get("q") or []) if l["k"] != "lab" else len(book["CH"][l["n"] - 1]["quiz"])
                ls.append({"id": l["id"], "k": l["k"], "title": l["title"], "slug": l["slug"], "kind": KIND.get(l["k"], "Konsep & kode"), "qn": qn})
                body = _normal(t, l, book)
                body.update({"id": l["id"], "title": l["title"], "mi": mi, "li": li})
                if dk.get(l["title"]):
                    body["deep"] = dk[l["title"]]
                bodies[l["slug"]] = body
            mods_meta.append({"t": m["t"], "d": m.get("d", ""), "lvl": m.get("lvl", ""), "lessons": ls})
        catalog.append({"k": t["k"], "g": t["g"], "name": t["name"], "lang": t["lang"], "h": site.text(t["h"]), "d": site.text(t["d"]),
                        "mark": marks.get(t["k"], t["k"][:2].upper()).replace("&lt;", "<").replace("&gt;", ">"),
                        "c": light.get(t["k"], "#C9D2F0"), "cd": dark.get(t["k"], "#C9D2F0"), "mods": mods_meta})
        _contoh(root, t, bodies)
        _v3(root, t, bodies)
        (out / "t" / f"{t['k']}.json").write_text(json.dumps(bodies, ensure_ascii=False, separators=(",", ":")))

    paths = _eval_js(re.search(r"const PATHS=\[.*?\}\];", app_js, re.S).group(0), "PATHS")
    (out / "catalog.json").write_text(json.dumps(
        {"groups": [{"k": k, "t": v} for k, v in site.GROUPS], "tracks": catalog, "paths": paths},
        ensure_ascii=False, separators=(",", ":")))

    gl_src = (root / "src" / "js" / "gl.js").read_text()
    gl = _eval_js(gl_src.split("/* ---------- istilah yang bisa disentuh")[0], "{cats:CATS,items:GL}")
    (out / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, separators=(",", ":")))
    _legacy(root)
    kit = _eval_js((root / "src" / "js" / "desain-kit.js").read_text().split("\n/*")[0], "KIT_DESAIN")
    (out / "kit.json").write_text(json.dumps(kit, ensure_ascii=False, separators=(",", ":")))
    n = sum(len(m["lessons"]) for t in catalog for m in t["mods"])
    return len(catalog), n


def _contoh(root, t, bodies):
    """Contoh bertahap dari src/contoh/<jalur>.json (lihat tools/build/contoh.py)."""
    terapkan(muat(root, t["k"]), bodies, f"src/contoh/{t['k']}.json")


def _v3(root, t, bodies):
    """Adegan visual 3D per pelajaran, dipilih dengan aturan yang sama seperti situs lama (viz3d.js):
    v3 di pelajaran menang, selain itu judul pelajaran dicocokkan dengan pola adegan."""
    items = [{"s": slug, "t": b["title"], "v3": b.get("v3", False) if "v3" in b else None, "p": b.get("v3p")} for slug, b in bodies.items()]
    src = (root / "src" / "js" / "viz3d.js").read_text()
    js = ("var window=globalThis;" + src + "\n;const T=" + json.dumps({"k": t["k"], "lang": t["lang"]}) + ";const L=" + json.dumps(items)
          + ";process.stdout.write(JSON.stringify(L.map(x=>{const k=x.v3!==null?x.v3:v3dOf(T,x.t);"
          + "return k&&V3DT(k)?[x.s,k,V3DT(k),x.p||v3dInit(k,x.t)||null]:null}).filter(Boolean)));")
    r = subprocess.run(["node", "-"], input=js, capture_output=True, text=True, check=True)
    for slug, k, title, init in json.loads(r.stdout):
        bodies[slug]["v3"] = {"k": k, "t": title, "p": init}
        bodies[slug].pop("v3p", None)


LAB_CSS = ["base.css", "lms.css", "v4.css", "tema-jalur.css", "v5.css", "nb.css"]
LAB_JS = ["util.js", "viz.js", "sqlengine.js", "sqldata.js", "sqldata-bi.js", "viz2.js", "viz3.js", "viz-msi.js", "viz-var.js", "viz-fc.js", "viz3d.js"]


def _legacy(root):
    """Visual interaktif lama dipakai ulang di dalam iframe terisolasi (web/public/lab),
    dan mesin SQL dijadikan modul ES untuk konsol SQL React."""
    js = root / "src" / "js"
    lab = root / "web" / "public" / "lab"
    lab.mkdir(parents=True, exist_ok=True)
    (lab / "legacy.css").write_text("\n".join((root / "src" / "css" / f).read_text() for f in LAB_CSS))
    (lab / "legacy-viz.js").write_text("\n;".join((js / f).read_text() for f in LAB_JS)
                                       + "\n;window.VIZ2=VIZ2;window.VIZ2T=VIZ2T;\n")
    sq = "\n".join((js / f).read_text() for f in ["sqlengine.js", "sqldata.js", "sqldata-bi.js"])
    sq = sq.replace("if(typeof module!=='undefined')module.exports=SQLE;", "")
    (root / "web" / "src" / "lib" / "sqle.js").write_text("// Dibuat otomatis oleh tools/build/webdata.py dari src/js. Jangan diedit.\n/* eslint-disable */\n" + sq + "\nexport { SQLE, SEED };\n")
