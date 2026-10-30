"""Menyusun src/ menjadi satu file HTML.

Keluaran:
  index.html            halaman lengkap untuk GitHub/Vercel
  dist/artifact.html    isi halaman tanpa doctype (untuk Artifact claude.ai)
Jalankan: python3 build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
CSS = ["base.css", "lms.css", "v4.css"]
JS = ["data.js", "util.js", "viz.js", "sqlengine.js", "sqldata.js", "sqldata-bi.js",
      "track-java.js", "track-python.js", "track-sql.js", "track-sql-extra.js",
      "track-html.js", "track-css.js", "track-fe0.js", "track-fe.js", "track-react.js",
      "track-ts.js", "track-git.js", "track-pda.js", "track-da.js", "track-bi.js",
      "track-de.js", "track-ux.js", "track-ds.js",
      "viz2.js", "viz3.js", "app.js", "app-pages.js", "app-lesson.js", "app-javapy.js",
      "app-extra.js", "app-nav.js"]

HEAD = """<title>Ruang Kode</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="author" content="Pasha Khatami Hasibuan">
<meta name="description" content="Akademi coding, data, dan desain berbahasa Indonesia: 16 jalur mengikuti roadmap.sh, visual interaktif, editor langsung jalan, konsol SQL, ujian, dan sertifikat. Dikembangkan oleh Pasha Khatami Hasibuan.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@500;600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
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
  <main class="main"><div class="wrap" id="view"></div></main>
</div>
<aside class="drawer" id="drawer" aria-label="Menu" hidden></aside>
<div class="palette" id="palette" role="dialog" aria-modal="true" aria-label="Pencarian" hidden>
  <div class="pl-box"><input id="sQ" type="search" role="combobox" aria-expanded="true" aria-controls="sList" placeholder="Cari jalur, modul, pelajaran, atau istilah…" autocomplete="off">
  <ul id="sList" role="listbox"></ul><div class="pl-foot"><span><kbd>↑</kbd><kbd>↓</kbd> pilih</span><span><kbd>Enter</kbd> buka</span><span><kbd>Esc</kbd> tutup</span></div></div>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<footer class="sfoot"><div><span>Ruang Kode · dikembangkan oleh <b>Pasha Khatami Hasibuan</b></span><span>Kurikulum mengikuti <a href="https://roadmap.sh" target="_blank" rel="noopener">roadmap.sh</a> · progres tersimpan di browser ini</span></div></footer>
"""


def build():
    css = "\n".join((SRC / "css" / f).read_text() for f in CSS)
    js = "\n".join((SRC / "js" / f).read_text() for f in JS)
    # isi pelajaran memuat contoh </script>; samarkan agar tidak menutup tag script halaman
    js = re.sub(r"</(script)", r"<\\/\1", js, flags=re.I)
    page = f"{HEAD}<style>\n{css}\n</style>\n{BODY}\n<script>\n{js}\n</script>\n"
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "artifact.html").write_text(page)
    full = ('<!doctype html>\n<html lang="id">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + page.replace(BODY, "</head>\n<body>" + BODY, 1) + "</body>\n</html>\n")
    (ROOT / "index.html").write_text(full)
    print(f"index.html {len(full):,} byte")


if __name__ == "__main__":
    build()
