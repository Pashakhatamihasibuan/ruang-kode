"""Bagian build untuk versi web: PWA (manifest, service worker, ikon) dan halaman statis SEO."""
import html
import json
import re
import shutil
import unicodedata
from datetime import date
from pathlib import Path

GROUPS = [("prog", "Pemrograman"), ("web", "Web & Frontend"), ("data", "Data"), ("des", "Desain"), ("tool", "Alat kerja")]
KIND = {"lab": "Konsep & lab", "topic": "Topik 5 langkah", "c": "Konsep & kode", "s": "Praktik SQL",
        "w": "Praktik langsung", "proj": "Proyek akhir"}
LANG = {"java": "Java", "python": "Python", "sql": "SQL", "ts": "TypeScript", "js": "JavaScript", "jsx": "JSX",
        "html": "HTML", "css": "CSS", "bash": "Terminal", "yaml": "YAML", "json": "JSON", "text": "Contoh"}
e = html.escape


# ---------------------------------------------------------------- data jalur
def tracks_meta(app_js, data, keys):
    """Daftar jalur (urutan TRACKS di app.js) dengan modul dan pelajaran berjudul."""
    out = []
    for line in [x for x in re.findall(r"^\s*\{k:'\w+'.*\}[\],;]*$", app_js, re.M) if 'mods:' in x]:
        f = dict(re.findall(r"(\w+):'((?:[^'\\]|\\.)*)'", line))
        const = re.search(r"mods:(\w+)", line).group(1)
        t = {"k": f["k"], "g": f["g"], "name": f["name"], "lang": f["lang"], "road": f["road"],
             "h": f["h"], "d": f["d"], "const": const}
        v = data["tracks"][const]
        mods, i = [], 0
        for mi, m in enumerate(v["skel"]):
            ls = []
            for li, l in enumerate(m["lessons"]):
                b = v["bodies"][i]
                i += 1
                ls.append({**l, **b, "id": f"{t['k']}-{mi + 1}-{li + 1}", "title": l.get("_t") or l.get("t") or ""})
            mods.append({"t": m["t"], "d": m.get("d", ""), "lvl": m.get("lvl", ""), "lessons": ls})
        t["mods"] = mods
        out.append(t)
    # pelajaran "see" meminjam pelajaran jalur lain
    byk = {t["k"]: t for t in out}
    for t in out:
        for m in t["mods"]:
            for l in m["lessons"]:
                if l["k"] == "see":
                    tk, ti = l["ref"].split(":", 1)
                    src = next((x for mm in byk[tk]["mods"] for x in mm["lessons"] if x["title"] == ti and x["k"] != "see"), None)
                    l["src"], l["src_tk"], l["title"] = src, tk, ti
    for t in out:  # slug unik per jalur, stabil terhadap judul
        used = set()
        for m in t["mods"]:
            for l in m["lessons"]:
                if l["k"] == "see":
                    continue
                s = slug(l["title"]) or l["id"]
                while s in used:
                    s += "-2"
                used.add(s)
                l["slug"] = s
    return out


def slug(s):
    s = unicodedata.normalize("NFKD", re.sub(r"<[^>]+>", "", s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:70]


def text(s, n=None):
    s = html.unescape(re.sub(r"<[^>]+>", "", s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    if n and len(s) > n:
        s = s[: n - 1].rsplit(" ", 1)[0] + "…"
    return s


def lesson_url(t, l):
    if l["k"] == "see":
        return f"/belajar/{l['src_tk']}/{l['src']['slug']}" if l.get("src") else None
    return f"/belajar/{t['k']}/{l['slug']}"


# ---------------------------------------------------------------- beranda
def noscript(tracks):
    """Isi awal #view: daftar jalur yang bisa dibaca mesin pencari; diganti aplikasi saat JS berjalan."""
    rows = "".join(f'<li><a href="/belajar/{t["k"]}">{e(t["name"])}</a>: {e(t["h"])}</li>' for t in tracks)
    return (f'<section class="section"><h1>Ruang Kode</h1><p>Akademi coding, data, dan desain berbahasa Indonesia. '
            f'Pilih jalur belajar:</p><ul>{rows}</ul><p><a href="/belajar">Lihat semua materi</a></p></section>')


def jsonld_home(url, tracks, desc):
    d = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "name": "Ruang Kode", "url": url + "/", "inLanguage": "id", "description": desc,
         "author": {"@type": "Person", "name": "Pasha Khatami Hasibuan"}},
        {"@type": "ItemList", "name": "Jalur belajar Ruang Kode", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f"{url}/belajar/{t['k']}", "name": t["name"]}
            for i, t in enumerate(tracks)]}]}
    return f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>\n'


# ---------------------------------------------------------------- PWA
def write_pwa(root, version, precache):
    icons = root / "icons"
    if not (icons / "icon-512.png").exists():
        make_icons(icons)
    manifest = {
        "name": "Ruang Kode · Akademi coding, data & desain", "short_name": "Ruang Kode",
        "description": "Belajar coding, data, dan desain berbahasa Indonesia, bisa dipakai offline.",
        "lang": "id", "start_url": "/", "scope": "/", "display": "standalone",
        "background_color": "#F2F4F8", "theme_color": "#152033",
        "icons": [{"src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
                  {"src": "/icons/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
        "shortcuts": [{"name": "Lanjutkan belajar", "url": "/#saya"}, {"name": "Katalog", "url": "/#katalog"}]}
    (root / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    sw = (Path(__file__).parent / "sw.tpl.js").read_text()
    sw = sw.replace("%VERSION%", version).replace("%PRECACHE%", json.dumps(precache + ["/manifest.webmanifest", "/icons/icon-192.png"]))
    (root / "sw.js").write_text(sw)


def make_icons(out):
    from PIL import Image, ImageDraw, ImageFont
    out.mkdir(exist_ok=True)
    font_path = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Bold.ttf"

    def tile(size, pad, radius):
        im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        grad = Image.new("RGBA", (size, size))
        a, b = (176, 68, 27), (37, 93, 162)  # warna Java -> Python di tema terang
        px = grad.load()
        for y in range(size):
            for x in range(size):
                k = min(1, (x + y) / (2 * size) * 1.3)
                px[x, y] = tuple(int(a[i] + (b[i] - a[i]) * k) for i in range(3)) + (255,)
        mask = Image.new("L", (size, size), 0)
        ImageDraw.Draw(mask).rounded_rectangle([pad, pad, size - pad, size - pad], radius=radius, fill=255)
        im.paste(grad, (0, 0), mask)
        d = ImageDraw.Draw(im)
        f = ImageFont.truetype(font_path, int(size * 0.34))
        d.text((size / 2, size / 2), "RK", font=f, fill="white", anchor="mm")
        return im

    tile(512, 0, 110).save(out / "icon-512.png")
    tile(512, 0, 110).resize((192, 192), Image.LANCZOS).save(out / "icon-192.png")
    full = tile(512, 0, 0)  # maskable: latar penuh, huruf di zona aman
    full.save(out / "maskable-512.png")
    tile(512, 0, 0).resize((180, 180), Image.LANCZOS).save(out / "apple-touch-icon.png")
    # gambar pratinjau tautan 1200x630
    og = Image.new("RGB", (1200, 630), (21, 32, 51))
    og.paste(tile(220, 0, 48), (90, 205), tile(220, 0, 48))
    d = ImageDraw.Draw(og)
    d.text((360, 230), "Ruang Kode", font=ImageFont.truetype(font_path, 84), fill="white")
    d.text((364, 340), "coding · data · desain · 16 jalur", font=ImageFont.truetype(font_path, 34), fill=(200, 212, 228))
    og.save(out / "og.png", optimize=True)


# ---------------------------------------------------------------- halaman statis
CSS = """:root{--bg:#F2F4F8;--surface:#fff;--ink:#152033;--muted:#556175;--line:#D6DDE7;--acc:#255DA2;--code:#101A28;--code-fg:#D9E3EF;--ok:#22744A}
@media (prefers-color-scheme:dark){:root{--bg:#0C121B;--surface:#131B27;--ink:#E4EAF2;--muted:#98A5B7;--line:#273347;--acc:#79ACEE;--code:#090F17;--ok:#62C98F;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:400 1.02rem/1.65 Inter,"Segoe UI",system-ui,sans-serif}
a{color:var(--acc)}header,main,footer{max-width:820px;margin:0 auto;padding-inline:max(16px,env(safe-area-inset-left,0px)) max(16px,env(safe-area-inset-right,0px))}
header{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-block:18px;border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;font-weight:600;color:var(--ink);text-decoration:none}.brand i{display:grid;place-items:center;width:34px;height:34px;border-radius:8px;background:linear-gradient(135deg,#B0441B,#255DA2);color:#fff;font:700 .7rem/1 "JetBrains Mono",monospace;font-style:normal}
main{padding-block:24px 48px}h1{font:600 clamp(1.7rem,4vw,2.4rem)/1.15 "Inter Tight",Inter,sans-serif;text-wrap:balance;margin:.2em 0 .4em}
h2{font:600 1.3rem/1.3 "Inter Tight",Inter,sans-serif;margin:2em 0 .6em}.crumb{font-size:.86rem;color:var(--muted)}.crumb a{color:var(--muted)}
.eyebrow{font:600 .72rem "JetBrains Mono",monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
pre{background:var(--code);color:var(--code-fg);padding:14px 16px;border-radius:10px;overflow-x:auto;font:400 .88rem/1.55 "JetBrains Mono",ui-monospace,monospace}
code{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.9em}.lbl{font:600 .7rem "JetBrains Mono",monospace;letter-spacing:.06em;color:var(--muted);margin:14px 0 4px}
.cta{display:inline-block;margin:18px 0;padding:11px 18px;border-radius:10px;background:var(--ink);color:var(--bg);text-decoration:none;font-weight:600}
.mod{border:1px solid var(--line);background:var(--surface);border-radius:12px;padding:6px 18px 12px;margin:14px 0}.mod ol{padding-left:1.2em}.mod small{color:var(--muted)}
details{border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:10px 0;background:var(--surface)}summary{cursor:pointer;font-weight:600}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto}td,th{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
.pro{display:grid;gap:10px}.ok{color:var(--ok);font-weight:600}footer{border-top:1px solid var(--line);padding-block:18px;color:var(--muted);font-size:.88rem}
"""


def page(url, title, desc, crumbs, body, ld, path_css="/belajar/s.css"):
    cr = " / ".join(f'<a href="{h}">{e(n)}</a>' if h else e(n) for n, h in crumbs)
    return f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="Pasha Khatami Hasibuan">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:site_name" content="Ruang Kode">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{url.split('/belajar')[0]}/icons/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/icons/icon-192.png" type="image/png"><link rel="manifest" href="/manifest.webmanifest">
<link rel="stylesheet" href="{path_css}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header><a class="brand" href="/"><i>RK</i>Ruang Kode</a><a href="/belajar">Semua materi</a></header>
<main><nav class="crumb" aria-label="Lokasi">{cr}</nav>
{body}
</main>
<footer>Ruang Kode · dikembangkan oleh Pasha Khatami Hasibuan · kurikulum mengikuti <a href="https://roadmap.sh">roadmap.sh</a></footer>
</body>
</html>
"""


def code(c, lang, label=None):
    return f'<div class="lbl">{e(label or LANG.get(lang, "Kode").upper())}</div><pre><code>{e(c)}</code></pre>'


def quiz(items):
    """Soal: [q,o,a,w] (teks biasa) atau {q,o,a,w} (HTML dari bab Java/Python)."""
    out = []
    for it in items or []:
        if isinstance(it, list):
            q, o, a, w = it
            q, o, w = e(q), [e(x) for x in o], e(w)
        else:
            q, o, a, w = it["q"], it["o"], it["a"], it["w"]
        out.append(f"<details><summary>{q}</summary><p class=\"ok\">Jawaban: {o[a]}</p><p>{w}</p></details>")
    return "<h2>Cek pemahaman</h2>" + "".join(out) if out else ""


def pros(l, lang):
    out = []
    for p in l.get("pro") or []:
        lg = p.get("lang", lang)
        out.append(f"<details><summary>{e(p['t'])}</summary><p>{p['why']}</p>{code(p['a'], lg, 'KODE PEMULA')}"
                   f"{code(p['b'], lg, 'KODE RAPI (BEST PRACTICE)')}{code(p['out'], 'text', 'KELUARAN KEDUANYA') if p.get('out') else ''}</details>")
    return "<h2>Kode pemula vs kode rapi</h2>" + "".join(out) if out else ""


def lesson_body(t, l, book):
    lang = l.get("lang") or t["lang"]
    k, h = l["k"], []
    if k == "lab":
        c = book["CHJ" if t["k"] == "java" else "CH"][l["n"] - 1]  # jalur Java: tanpa perbandingan Python
        h += [f"<p>{p}</p>" for p in c["body"]]
        lg = "java" if t["k"] == "java" else "python"
        h.append(code(c[lg], lg))
        o = c.get("out")
        o = o.get(lg) if isinstance(o, dict) else o
        if o:
            h.append(code(o, "text", "KELUARAN"))
        if c.get("points"):
            h.append("<h2>Poin penting</h2><ul>" + "".join(f"<li>{p}</li>" for p in c["points"]) + "</ul>")
        h.append(quiz(c["quiz"]))
    elif k == "topic":
        n, i = map(int, l["ref"].split("."))
        tp = book["TOPICS"][str(n)][i]
        col = 1 if t["k"] == "java" else 2
        h.append("<h2>Dari kalimat ke kode</h2><table><tr><th>Maksud</th><th>Kode</th></tr>"
                 + "".join(f"<tr><td>{e(r[0])}</td><td><code>{e(r[col])}</code></td></tr>" for r in tp["tr"]) + "</table>")
        lg = "java" if col == 1 else "python"
        h.append(code(tp[lg], lg))
    elif k == "proj":
        h.append(f"<p>{l.get('brief', '')}</p>")
        if l.get("stack"):
            h.append(f"<p><b>Teknologi:</b> {e(l['stack'])}</p>")
        if l.get("feats"):
            h.append("<h2>Fitur yang dibuat</h2><ul>" + "".join(f"<li>{e(f)}</li>" for f in l["feats"]) + "</ul>")
        if l.get("steps"):
            h.append("<h2>Langkah kerja</h2><ol>" + "".join(f"<li>{s}</li>" for s in l["steps"]) + "</ol>")
        for f in l.get("files") or []:
            h.append(code(f[2], f[1], f[0]))
    else:
        h += [f"<p>{p}</p>" for p in l.get("b") or []]
        if l.get("code"):
            h.append(code(l["code"], lang))
            if l.get("out") is not None:
                h.append(code(l["out"], "text", "KELUARAN"))
        for key in ("html", "css", "js"):
            if l.get(key):
                h.append(code(l[key], "jsx" if key == "js" and l.get("react") else key))
        if l.get("sql"):
            h.append(code(l["sql"], "sql"))
        for ex in l.get("ex") or []:
            h.append(code(ex[1], "sql", ex[0]))
        tasks = l.get("tasks") or ([l["task"]] if l.get("task") else [])
        if tasks:
            h.append("<h2>Tantangan</h2><ol>" + "".join(f"<li>{x.get('q', '')}</li>" for x in tasks if isinstance(x, dict)) + "</ol>")
        h.append(pros(l, lang))
        if l.get("pts"):
            h.append("<h2>Poin penting</h2><ul>" + "".join(f"<li>{p}</li>" for p in l["pts"]) + "</ul>")
        h.append(quiz(l.get("q")))
    return "\n".join(x for x in h if x)


def write_static(root, url, tracks, data):
    out = root / "belajar"
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir()
    (out / "s.css").write_text(CSS)
    book, urls, n = data["book"], [url + "/", url + "/belajar"], 0
    org = {"@type": "Organization", "name": "Ruang Kode", "url": url + "/"}

    # katalog
    body = "<h1>Semua materi Ruang Kode</h1><p>16 jalur belajar coding, data, dan desain berbahasa Indonesia. Setiap pelajaran punya versi interaktif di aplikasi.</p>"
    for g, gn in GROUPS:
        body += f"<h2>{e(gn)}</h2><ul>" + "".join(
            f'<li><a href="/belajar/{t["k"]}">{e(t["name"])}</a>: {e(t["h"])}</li>' for t in tracks if t["g"] == g) + "</ul>"
    (out / "index.html").write_text(page(url + "/belajar", "Semua materi · Ruang Kode", "16 jalur belajar coding, data, dan desain berbahasa Indonesia mengikuti roadmap.sh.",
                                         [("Beranda", "/"), ("Materi", None)], body, {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Semua materi", "publisher": org}))

    for t in tracks:
        tdir = out / t["k"]
        tdir.mkdir()
        tu = f"{url}/belajar/{t['k']}"
        nl = sum(len(m["lessons"]) for m in t["mods"])
        body = (f'<div class="eyebrow">Jalur belajar · roadmap.sh/{e(t["road"])}</div><h1>{e(t["name"])}: {e(t["h"])}</h1><p>{e(t["d"])}</p>'
                f'<p>{len(t["mods"])} modul · {nl} pelajaran</p><a class="cta" href="/#{t["k"]}">Mulai belajar di aplikasi</a>')
        for mi, m in enumerate(t["mods"]):
            items = []
            for l in m["lessons"]:
                lu = lesson_url(t, l)
                items.append(f'<li><a href="{lu}">{e(l["title"])}</a></li>' if lu else f"<li>{e(l['title'])}</li>")
            body += f'<section class="mod"><h2>Modul {mi + 1}: {e(m["t"])}</h2><small>{e(m["lvl"])}</small><p>{e(m["d"])}</p><ol>{"".join(items)}</ol></section>'
        ld = {"@context": "https://schema.org", "@type": "Course", "name": f"{t['name']}: {t['h']}", "description": t["d"],
              "inLanguage": "id", "provider": org, "url": tu, "isAccessibleForFree": True,
              "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": f"PT{max(1, nl // 6)}H"},
              "offers": {"@type": "Offer", "price": 0, "priceCurrency": "IDR", "category": "Free"}}
        (out / f"{t['k']}.html").write_text(page(tu, f"Belajar {t['name']}: {t['h']} · Ruang Kode", text(t["d"], 155),
                                                [("Beranda", "/"), ("Materi", "/belajar"), (t["name"], None)], body, ld))
        urls.append(tu)
        n += 1

        flat = [l for m in t["mods"] for l in m["lessons"] if l["k"] != "see"]
        for mi, m in enumerate(t["mods"]):
            for l in m["lessons"]:
                if l["k"] == "see":
                    continue
                lu = f"{url}/belajar/{t['k']}/{l['slug']}"
                content = lesson_body(t, l, book)
                desc = text(re.search(r"<p>(.*?)</p>", content, re.S).group(1) if "<p>" in content else m["d"], 155) or m["d"]
                i = flat.index(l)
                nav = "".join(f'<p>{lab}: <a href="/belajar/{t["k"]}/{x["slug"]}">{e(x["title"])}</a></p>'
                              for lab, x in (("Sebelumnya", flat[i - 1] if i else None), ("Berikutnya", flat[i + 1] if i + 1 < len(flat) else None)) if x)
                body = (f'<div class="eyebrow">{e(t["name"])} · Modul {mi + 1} · {e(KIND.get(l["k"], ""))}</div><h1>{e(text(l["title"]))}</h1>'
                        f'<a class="cta" href="/#{l["id"]}">Buka versi interaktif</a>\n{content}\n<a class="cta" href="/#{l["id"]}">Kerjakan latihannya di aplikasi</a>{nav}')
                ld = {"@context": "https://schema.org", "@graph": [
                    {"@type": "LearningResource", "name": text(l["title"]), "description": desc, "inLanguage": "id", "url": lu,
                     "learningResourceType": KIND.get(l["k"], "Pelajaran"), "isPartOf": {"@type": "Course", "name": t["name"], "url": tu},
                     "provider": org, "isAccessibleForFree": True},
                    {"@type": "BreadcrumbList", "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Materi", "item": url + "/belajar"},
                        {"@type": "ListItem", "position": 2, "name": t["name"], "item": tu},
                        {"@type": "ListItem", "position": 3, "name": text(l["title"]), "item": lu}]}]}
                (tdir / f"{l['slug']}.html").write_text(page(lu, f"{text(l['title'])} · {t['name']} · Ruang Kode", desc,
                                                            [("Materi", "/belajar"), (t["name"], f"/belajar/{t['k']}"), (f"Modul {mi + 1}", None)], body, ld))
                urls.append(lu)
                n += 1

    today = date.today().isoformat()
    (root / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    (root / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {url}/sitemap.xml\n")
    return n
