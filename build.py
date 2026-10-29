"""Menyusun src/ menjadi satu file HTML.

Keluaran:
  index.html            halaman lengkap untuk GitHub/Vercel
  dist/artifact.html    isi halaman tanpa doctype (untuk Artifact claude.ai)
Jalankan: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
CSS = ["base.css", "lms.css"]
JS = ["data.js", "util.js", "viz.js", "sqlengine.js", "sqldata.js",
      "track-java.js", "track-python.js", "track-sql.js", "viz2.js", "app.js"]

HEAD = """<title>Ruang Kode · Akademi Java, Python &amp; SQL</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Belajar Java, Python, dan SQL dalam bahasa Indonesia: tiga jalur terstruktur mengikuti roadmap.sh, visual interaktif, dan konsol SQL di browser.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@500;600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
"""

BODY = """
<header class="gnav">
  <div class="gnav-in">
    <a class="brand" href="#beranda"><span class="brand-mark">RK</span><span><b>Ruang Kode</b><small>Java · Python · SQL</small></span></a>
    <nav class="tracks" id="tracks" aria-label="Jalur belajar">
      <a href="#java" data-tk="java" class="t-java"><i class="dot"></i>Java</a>
      <a href="#python" data-tk="python" class="t-python"><i class="dot"></i>Python</a>
      <a href="#sql" data-tk="sql" class="t-sql"><i class="dot"></i>SQL</a>
      <span class="ind" id="ind" aria-hidden="true"></span>
    </nav>
    <nav class="gx" id="gx" aria-label="Lainnya"><a href="#kuis" data-r="kuis">Kuis</a><a href="#glosarium" data-r="glosarium">Glosarium</a></nav>
  </div>
  <div class="rprog"><i id="rprog"></i></div>
</header>
<div class="shell" id="shell">
  <div class="scrim" id="scrim"></div>
  <aside class="outline" id="outline" aria-label="Daftar materi" hidden></aside>
  <main class="main"><div class="wrap" id="view"></div></main>
</div>
<footer class="sfoot"><div><span>Ruang Kode · belajar Java, Python &amp; SQL dalam bahasa Indonesia</span><span>Kurikulum mengikuti <a href="https://roadmap.sh" target="_blank" rel="noopener">roadmap.sh</a> · progres tersimpan di browser ini</span></div></footer>
"""


def build():
    css = "\n".join((SRC / "css" / f).read_text() for f in CSS)
    js = "\n".join((SRC / "js" / f).read_text() for f in JS)
    assert "</script" not in js.lower(), "kode JS tidak boleh berisi </script"
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
