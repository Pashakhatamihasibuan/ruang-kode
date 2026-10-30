"""Menyusun src/ menjadi situs Ruang Kode.

Keluaran:
  dist/artifact.html    satu file berisi semuanya, tanpa doctype (untuk Artifact claude.ai)
  index.html            versi web: inti aplikasi + kerangka materi; isi pelajaran dimuat per jalur
  c/*.js                bagian materi (nama memuat hash isi, aman di-cache selamanya)
  sw.js, manifest.webmanifest   aplikasi web yang bisa dipasang dan dipakai offline
  belajar/**, sitemap.xml, robots.txt   halaman statis per jalur dan pelajaran untuk mesin pencari
Butuh Python 3 dan Node (untuk membaca berkas kurikulum). Jalankan: python3 build.py
"""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

from tools.build import site

ROOT = Path(__file__).parent
SRC = ROOT / "src"
SITE_URL = "https://ruang-kode-nine.vercel.app"
CSS = ["base.css", "lms.css", "v4.css"]
TRACK_JS = ["track-java.js", "track-python.js", "track-sql.js", "track-sql-extra.js",
            "track-html.js", "track-css.js", "track-fe0.js", "track-fe.js", "track-react.js",
            "track-ts.js", "track-git.js", "track-pda.js", "track-da.js", "track-bi.js",
            "track-de.js", "track-ux.js", "track-ds.js", "track-more.js", "tips.js"]
RT_JS = ["viz.js", "sqlengine.js", "sqldata.js", "sqldata-bi.js", "viz2.js", "viz3.js"]
BOOK_JS = ["data.js", "app-javapy.js", "app-extra.js"]
CORE_JS = ["app.js", "app-pages.js", "app-lesson.js", "app-nav.js"]
# urutan versi satu file (sama dengan urutan sebelum materi dipecah)
ALL_JS = (["data.js", "util.js", "viz.js", "sqlengine.js", "sqldata.js", "sqldata-bi.js"] + TRACK_JS
          + ["viz2.js", "viz3.js", "app.js", "app-pages.js", "app-lesson.js", "app-javapy.js",
             "app-extra.js", "app-nav.js"])

DESC = ("Akademi coding, data, dan desain berbahasa Indonesia: 16 jalur mengikuti roadmap.sh, "
        "visual interaktif, editor langsung jalan, konsol SQL, ujian, dan proyek. "
        "Dikembangkan oleh Pasha Khatami Hasibuan.")
FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@500;600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
"""
HEAD = f"""<title>Ruang Kode</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="author" content="Pasha Khatami Hasibuan">
<meta name="description" content="{DESC}">
{FONTS}"""
WEB_HEAD = f"""<link rel="canonical" href="{SITE_URL}/">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="icon" href="/icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<meta name="theme-color" content="#F2F4F8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0C121B" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ruang Kode">
<meta property="og:title" content="Ruang Kode · Akademi coding, data & desain">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{SITE_URL}/">
<meta property="og:image" content="{SITE_URL}/icons/og.png">
<meta property="og:locale" content="id_ID">
<meta name="twitter:card" content="summary_large_image">
"""

BODY = """
<header class="gnav">
  <div class="gnav-in">
    <a class="brand" href="#beranda"><span class="brand-mark">RK</span><span><b>Ruang Kode</b><small>coding · data · desain</small></span></a>
    <nav class="gmain" id="gmain" aria-label="Utama">
      <button class="gbtn" id="catBtn" aria-expanded="false" aria-controls="mega">Katalog <span aria-hidden="true">▾</span></button>
      <a href="#saya" data-r="saya">Belajar saya</a>
      <a href="#ulang" data-r="ulang">Ulang <span class="badge wrongN" hidden></span></a>
      <a href="#kuis" data-r="kuis">Kuis</a>
      <a href="#glosarium" data-r="glosarium">Glosarium</a>
    </nav>
    <div class="gtools">
      <button class="gsearch" id="srchBtn" aria-label="Cari (Ctrl+K)"><span aria-hidden="true">⌕</span><span class="gs-t">Cari materi…</span><kbd>Ctrl K</kbd></button>
      <button class="icon-btn" id="themeBtn" aria-label="Tema">◐</button>
      <button class="icon-btn menu-btn" id="menuBtn" aria-label="Menu" aria-expanded="false" aria-controls="drawer">☰</button>
    </div>
  </div>
  <div class="mega" id="mega" hidden></div>
  <div class="rprog"><i id="rprog"></i></div>
</header>
<div class="shell" id="shell">
  <div class="scrim" id="scrim"></div>
  <aside class="outline" id="outline" aria-label="Daftar materi" hidden></aside>
  <main class="main"><div class="wrap" id="view">%NOSCRIPT%</div></main>
</div>
<aside class="drawer" id="drawer" aria-label="Menu" hidden></aside>
<div class="palette" id="palette" role="dialog" aria-modal="true" aria-label="Pencarian" hidden>
  <div class="pl-box"><input id="sQ" type="search" role="combobox" aria-expanded="true" aria-controls="sList" placeholder="Cari jalur, modul, pelajaran, atau istilah…" autocomplete="off">
  <ul id="sList" role="listbox"></ul><div class="pl-foot"><span><kbd>↑</kbd><kbd>↓</kbd> pilih</span><span><kbd>Enter</kbd> buka</span><span><kbd>Esc</kbd> tutup</span></div></div>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<footer class="sfoot"><div><span>Ruang Kode · dikembangkan oleh <b>Pasha Khatami Hasibuan</b></span><span>Kurikulum mengikuti <a href="https://roadmap.sh" target="_blank" rel="noopener">roadmap.sh</a> · progres tersimpan di browser ini</span></div></footer>
"""


def read(*parts):
    return (SRC.joinpath(*parts)).read_text()


def js_of(files):
    return "\n".join(read("js", f) for f in files)


def safe_inline(js):
    # isi pelajaran memuat contoh </script>; samarkan agar tidak menutup tag script halaman
    return re.sub(r"</(script)", r"<\\/\1", js, flags=re.I)


def doc(head, body, scripts):
    return ('<!doctype html>\n<html lang="id">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head + "</head>\n<body>" + body + scripts + "</body>\n</html>\n")


def split_tracks():
    """Kurikulum dijalankan di Node lalu dipecah: kerangka (judul, jenis) dan isi per pelajaran."""
    files = [str(SRC / "js" / f) for f in ["data.js"] + TRACK_JS]
    res = subprocess.run(["node", str(ROOT / "tools/build/evaltracks.js"), *files],
                         capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


def track_keys():
    """Nama konstanta kurikulum -> kunci jalur, dibaca dari TRACKS di app.js."""
    return {c: k for k, c in re.findall(r"\{k:'(\w+)'[^}]*?mods:(\w+)", read("js", "app.js"))}


def write_chunk(name, js):
    h = hashlib.sha256(js.encode()).hexdigest()[:10]
    path = f"c/{name}.{h}.js"
    (ROOT / path).write_text(js)
    return path


def build():
    css = "\n".join(read("css", f) for f in CSS)

    # 1. satu file untuk Artifact
    page = f"{HEAD}<style>\n{css}\n</style>\n{BODY.replace('%NOSCRIPT%', '')}\n<script>\n{safe_inline(js_of(ALL_JS))}\n</script>\n"
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "artifact.html").write_text(page)

    # 2. versi web: materi dipecah per jalur
    data = split_tracks()
    keys = track_keys()
    shutil.rmtree(ROOT / "c", ignore_errors=True)
    (ROOT / "c").mkdir()
    chunks = {"rt": write_chunk("rt", js_of(RT_JS)), "book": write_chunk("book", js_of(BOOK_JS))}
    skel = []
    for const, v in data["tracks"].items():
        tk = keys[const]
        skel.append(f"const {const}={json.dumps(v['skel'], ensure_ascii=False, separators=(',', ':'))};")
        chunks["t:" + tk] = write_chunk(
            "t-" + tk, f"RKfill({json.dumps(tk)},{json.dumps(v['bodies'], ensure_ascii=False, separators=(',', ':'))});\n")
    core = "\n".join([read("js", "util.js"), *skel, js_of(CORE_JS)])
    boot = f"window.RK_CHUNKS={json.dumps(chunks)};"
    tracks = site.tracks_meta(read("js", "app.js"), data, keys)
    web = doc(HEAD + WEB_HEAD + site.jsonld_home(SITE_URL, tracks, DESC) + f"<style>\n{css}\n</style>\n",
              BODY.replace("%NOSCRIPT%", site.noscript(tracks)),
              f"\n<script>{boot}</script>\n<script>\n{safe_inline(core)}\n</script>\n")
    (ROOT / "index.html").write_text(web)

    # 3. PWA dan halaman statis
    version = hashlib.sha256((web + "".join(chunks.values())).encode()).hexdigest()[:10]
    site.write_pwa(ROOT, version, ["/", *("/" + c for c in chunks.values())])
    pages = site.write_static(ROOT, SITE_URL, tracks, data)
    print(f"index.html {len(web):,} byte · {len(chunks)} bagian materi · {pages} halaman statis · "
          f"artifact {len(page):,} byte")


if __name__ == "__main__":
    build()
