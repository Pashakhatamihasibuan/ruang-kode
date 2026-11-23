"""Pendalaman jalur Slicing Web: istilah dunia kerja dan contoh HTML/CSS (perhitungan pendukung dijalankan dengan Python)."""
K = 'slw'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def C(t, code, b=None, lang='css'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Apa itu slicing dan alurnya': dict(
  ist=[('Slicing', 'Mengubah desain (Figma) menjadi HTML/CSS yang berfungsi dan responsif.'),
       ('Pixel-perfect', 'Hasil sangat dekat dengan desain; di dunia nyata yang dikejar "design-faithful" di semua lebar layar.'),
       ('Front-end handoff', 'Desain diserahkan dengan token, aset, dan anotasi; slicer menanyakan bagian yang ambigu.'),
       ('Scope of work', 'Daftar halaman, breakpoint, browser yang didukung, dan interaksi yang termasuk pekerjaan.')],
  cx=[P('Estimasi pekerjaan slicing landing page', '''
section = {"navbar": 2, "hero": 3, "fitur (grid 3)": 2, "testimoni (scroll-snap)": 3, "harga (3 paket)": 3,
           "FAQ (accordion)": 2, "footer + newsletter": 2}
tambahan = {"setup token & base CSS": 2, "responsif 3 breakpoint": 4, "QA lintas browser & aksesibilitas": 3, "deploy": 1}
total = sum(section.values()) + sum(tambahan.values())
for k, v in {**section, **tambahan}.items():
    print(f"{k:34} {v:>2} jam")
print(f"{'TOTAL':34} {total:>2} jam  (~{total / 6:.1f} hari kerja efektif)")
''')]),

'Membaca desain di Figma Dev Mode': dict(
  ist=[('Inspect panel', 'Panel yang menampilkan ukuran, jarak, warna, tipografi, dan cuplikan CSS.'),
       ('Variables & styles', 'Nilai yang sudah bernama di Figma; pakai namanya, jangan menyalin angka mentah.'),
       ('Measure (Alt/Option hover)', 'Cara mengukur jarak antar elemen di Figma.'),
       ('Generated CSS', 'CSS dari Dev Mode adalah petunjuk, bukan kode final (sering absolute dan ukuran tetap).')],
  cx=[C('CSS dari Dev Mode vs CSS yang ditulis ulang', '''
/* Dev Mode (mentah) */
.frame-12 { position: absolute; width: 343px; height: 56px; left: 16px; top: 612px;
            background: #0F766E; border-radius: 12px; font-family: 'Plus Jakarta Sans'; font-size: 16px; }

/* Ditulis ulang: mengalir, responsif, memakai token */
.btn-primary {
  display: inline-flex; align-items: center; justify-content: center;
  width: 100%; min-height: 56px; padding-inline: var(--space-5);
  background: var(--color-action-primary); color: var(--color-on-action);
  border-radius: var(--radius-lg); font: var(--type-label-lg);
}
''')]),

'Token desain ke CSS variables': dict(
  ist=[('CSS custom properties', 'Variabel CSS (--nama) yang bisa diubah per tema dan dibaca JavaScript.'),
       ('Token naming parity', 'Nama variabel CSS sama dengan nama variable di Figma.'),
       ('Fallback value', 'var(--x, nilai-cadangan) untuk berjaga jika token belum didefinisikan.'),
       ('Cascade layers', '@layer reset, tokens, base, components, utilities untuk mengatur prioritas CSS.')],
  cx=[C('Struktur CSS dengan @layer dan token', '''
@layer reset, tokens, base, components, utilities;

@layer tokens {
  :root {
    --color-bg: #FFFBF5; --color-text: #2B1D14; --color-accent: #B45309;
    --font-display: "Fraunces", Georgia, serif; --font-body: "Inter", system-ui, sans-serif;
    --space-2: .5rem; --space-4: 1rem; --space-8: 2rem; --radius-md: .75rem;
  }
}
@layer base {
  body { background: var(--color-bg); color: var(--color-text); font: 1rem/1.6 var(--font-body); }
  h1, h2 { font-family: var(--font-display); text-wrap: balance; }
}
@layer utilities { .visually-hidden { position: absolute !important; clip: rect(0 0 0 0); width: 1px; height: 1px; overflow: hidden; } }
''')]),

'HTML semantik dari desain': dict(
  ist=[('Landmark', 'header, nav, main, section, aside, footer yang dipakai pembaca layar untuk melompat.'),
       ('Heading outline', 'Satu h1 per halaman, h2 per section, tanpa melompat tingkat.'),
       ('Div soup', 'HTML yang semuanya div; sulit diakses dan dirawat.'),
       ('Button vs link', 'Link (<a>) untuk pindah halaman; button untuk aksi di halaman.')],
  cx=[C('Kerangka semantik landing page', '''
<body>
  <a class="skip" href="#utama">Lewati ke konten utama</a>
  <header class="situs">
    <a href="/" class="logo" aria-label="Kopi Kita, beranda"><img src="logo.svg" alt="" width="120" height="32"></a>
    <nav aria-label="Utama"><ul><li><a href="#menu">Menu</a></li><li><a href="#lokasi">Lokasi</a></li></ul></nav>
  </header>
  <main id="utama">
    <section aria-labelledby="judul-hero"><h1 id="judul-hero">Kopi Gayo diseduh pelan</h1>…</section>
    <section id="menu" aria-labelledby="judul-menu"><h2 id="judul-menu">Menu favorit</h2>…</section>
  </main>
  <footer>…</footer>
</body>
''', lang='html')]),

'Navbar responsif': dict(
  ist=[('Hamburger menu', 'Tombol untuk membuka navigasi di layar kecil; wajib aria-expanded dan aria-controls.'),
       ('Disclosure pattern', 'Pola tombol yang menampilkan/menyembunyikan konten terkait.'),
       ('Sticky header', 'Header menempel saat scroll; jaga agar tidak menutupi elemen fokus (WCAG 2.4.11).'),
       ('Current page', 'aria-current="page" menandai tautan halaman aktif.')],
  cx=[C('Navbar dengan tombol menu yang aksesibel', '''
<button class="menu-btn" aria-expanded="false" aria-controls="nav-utama">
  <span class="visually-hidden">Buka menu</span>☰
</button>
<nav id="nav-utama" class="nav" data-terbuka="false">
  <a href="/" aria-current="page">Beranda</a> <a href="/menu">Menu</a> <a href="/lokasi">Lokasi</a>
</nav>
<script>
  const b = document.querySelector(".menu-btn"), n = document.getElementById("nav-utama");
  b.addEventListener("click", () => {
    const buka = b.getAttribute("aria-expanded") !== "true";
    b.setAttribute("aria-expanded", buka); n.dataset.terbuka = buka;
    b.querySelector(".visually-hidden").textContent = buka ? "Tutup menu" : "Buka menu";
  });
</script>
<style>
  @media (max-width: 767px) { .nav[data-terbuka="false"] { display: none; } }
  @media (min-width: 768px) { .menu-btn { display: none; } .nav { display: flex; gap: 24px; } }
</style>
''', lang='html')]),

'Hero section': dict(
  ist=[('Above the fold', 'Bagian yang terlihat tanpa scroll; berisi pesan utama dan CTA.'),
       ('LCP (Largest Contentful Paint)', 'Metrik Core Web Vitals: waktu elemen terbesar (sering gambar hero) tampil; target ≤ 2,5 detik.'),
       ('fetchpriority="high"', 'Memberi tahu browser bahwa gambar hero penting untuk dimuat lebih dulu.'),
       ('CTA', 'Call to action; satu utama, satu sekunder.')],
  cx=[C('Hero yang cepat dimuat', '''
<section class="hero">
  <div class="hero-teks">
    <h1>Kopi Gayo, diseduh pelan untuk harimu</h1>
    <p>Biji pilihan petani Aceh Tengah, dipanggang tiap Senin di Medan.</p>
    <div class="cta"><a class="btn-primary" href="#pesan">Pesan sekarang</a><a class="btn-ghost" href="#menu">Lihat menu</a></div>
  </div>
  <img src="hero-800.avif" srcset="hero-480.avif 480w, hero-800.avif 800w, hero-1200.avif 1200w"
       sizes="(min-width: 1024px) 50vw, 100vw" width="1200" height="900"
       alt="Barista menuang kopi V60 di meja kayu" fetchpriority="high" decoding="async">
</section>
<style>
  .hero { display: grid; gap: 32px; align-items: center; padding-block: 48px; }
  @media (min-width: 1024px) { .hero { grid-template-columns: 1fr 1fr; padding-block: 96px; } }
  .hero img { width: 100%; height: auto; border-radius: 24px; }
</style>
''', lang='html')]),

'Tombol dan kartu dari komponen Figma': dict(
  ist=[('Component mapping', 'Satu komponen Figma = satu kelas/komponen kode dengan varian yang sama.'),
       ('BEM', 'Penamaan kelas Block__Element--Modifier: .kartu__judul, .btn--besar.'),
       ('Variant to modifier', 'Varian Figma (size=lg) menjadi modifier kelas (.btn--lg) atau atribut data-size.'),
       ('Reusable CSS', 'Gaya komponen tidak bergantung halaman tempat ia dipakai.')],
  cx=[C('Komponen kartu menu dengan BEM', '''
.kartu-menu { display: grid; gap: 8px; padding: 12px; border-radius: var(--radius-md); background: #fff;
              box-shadow: 0 1px 2px rgb(0 0 0 / .06), 0 4px 16px rgb(0 0 0 / .06); }
.kartu-menu__foto { aspect-ratio: 1; object-fit: cover; border-radius: calc(var(--radius-md) - 4px); width: 100%; }
.kartu-menu__nama { font: 600 1.0625rem/1.3 var(--font-body); }
.kartu-menu__harga { font-variant-numeric: tabular-nums; color: var(--color-accent); font-weight: 700; }
.kartu-menu--habis { opacity: .55; }
.kartu-menu--habis .kartu-menu__harga::after { content: " · Habis"; color: var(--color-text); font-weight: 500; }
''')]),

'Ikon dan gambar yang dioptimalkan': dict(
  ist=[('AVIF / WebP', 'Format gambar modern yang jauh lebih kecil dari JPEG/PNG.'),
       ('Lazy loading', 'loading="lazy" untuk gambar di bawah layar; jangan untuk gambar hero.'),
       ('width & height attributes', 'Mencegah layout bergeser saat gambar dimuat (CLS).'),
       ('SVG optimization', 'Membersihkan SVG dari metadata editor (SVGO) dan memakai currentColor.')],
  cx=[P('Perkiraan penghematan ukuran halaman', '''
gambar = [("hero", 1_850, "jpg"), ("menu-1", 420, "png"), ("menu-2", 390, "png"), ("menu-3", 410, "png"), ("barista", 980, "jpg")]
rasio = {"jpg": 0.35, "png": 0.25}            # perkiraan ukuran AVIF relatif (bergantung isi gambar)
sebelum = sum(kb for _, kb, _ in gambar)
sesudah = sum(kb * rasio[f] for _, kb, f in gambar)
for n, kb, f in gambar:
    print(f"{n:8} {kb:>5} KB {f} -> ~{kb * rasio[f]:>4.0f} KB avif")
print(f"total {sebelum} KB -> ~{sesudah:.0f} KB (hemat {1 - sesudah / sebelum:.0%})")
print(f"di jaringan 3G 1,6 Mbps: {sebelum * 8 / 1600:.1f} s -> {sesudah * 8 / 1600:.1f} s")
''')]),

'Section fitur dengan grid': dict(
  ist=[('CSS Grid', 'Tata letak dua dimensi untuk baris dan kolom.'),
       ('auto-fit + minmax', 'Grid yang otomatis menyesuaikan jumlah kolom tanpa media query.'),
       ('Subgrid', 'Anak grid mewarisi garis grid induk agar isi kartu sejajar antar-kartu.'),
       ('Gap', 'Jarak antar sel grid; lebih rapi dari margin.')],
  cx=[C('Grid fitur yang sejajar dengan subgrid', '''
.fitur { display: grid; gap: 24px; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); }
.fitur__item {
  display: grid; grid-row: span 3; grid-template-rows: subgrid;   /* ikon, judul, teks sejajar di semua kartu */
  gap: 8px; padding: 24px; border: 1px solid #EADBC8; border-radius: 16px;
}
.fitur__ikon { width: 40px; height: 40px; }
''')]),

'Testimoni dengan scroll-snap': dict(
  ist=[('Scroll snap', 'Scroll berhenti tepat di setiap item tanpa JavaScript carousel.'),
       ('Carousel accessibility', 'Kontrol harus bisa dipakai keyboard, tidak auto-play tanpa tombol jeda.'),
       ('overscroll-behavior', 'Mencegah scroll halaman ikut bergerak saat ujung carousel tercapai.'),
       ('scroll-padding', 'Jarak aman saat snap agar item tidak menempel tepi.')],
  cx=[C('Carousel testimoni tanpa library', '''
.testimoni {
  display: grid; grid-auto-flow: column; grid-auto-columns: min(85%, 360px); gap: 16px;
  overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-inline: 16px;
  padding: 4px 16px 16px; overscroll-behavior-x: contain;
}
.testimoni > figure { scroll-snap-align: start; margin: 0; padding: 20px; border-radius: 16px; background: #fff; }
.testimoni:focus-visible { outline: 3px solid var(--color-accent); }
/* HTML: <div class="testimoni" tabindex="0" role="region" aria-label="Testimoni pelanggan"> … </div> */
''')]),

'Tabel harga dengan paket unggulan': dict(
  ist=[('Pricing table', 'Perbandingan paket; satu paket disorot sebagai rekomendasi.'),
       ('Decoy effect', 'Paket pembanding yang membuat paket target terlihat lebih menarik; gunakan dengan jujur.'),
       ('Feature list semantics', 'Gunakan <ul> dan teks "termasuk/tidak termasuk", bukan hanya ikon centang.'),
       ('Price anchoring', 'Harga coret atau harga tahunan per bulan; tampilkan total yang dibayar dengan jelas.')],
  cx=[C('Kartu harga dengan paket unggulan', '''
<ul class="harga" role="list">
  <li class="paket"><h3>Seduh</h3><p class="nominal">Rp49.000<span>/bulan</span></p>
    <ul><li>2 bungkus 200 g</li><li>Ongkir Medan gratis</li></ul><a class="btn-ghost" href="/daftar?p=seduh">Pilih Seduh</a></li>
  <li class="paket paket--unggulan" aria-label="Paket Barista, paling populer">
    <p class="lencana">Paling populer</p><h3>Barista</h3><p class="nominal">Rp89.000<span>/bulan</span></p>
    <ul><li>4 bungkus 200 g</li><li>Ongkir seluruh Indonesia gratis</li><li>Pilih tingkat sangrai</li></ul>
    <a class="btn-primary" href="/daftar?p=barista">Pilih Barista</a></li>
</ul>
<style>
  .harga { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); padding: 0; }
  .paket { list-style: none; padding: 24px; border: 1px solid #EADBC8; border-radius: 20px; display: grid; gap: 12px; }
  .paket--unggulan { border: 2px solid var(--color-accent); box-shadow: 0 12px 32px rgb(180 83 9 / .15); }
  @media (min-width: 900px) { .paket--unggulan { transform: scale(1.04); } }
</style>
''', lang='html')]),

'Footer dan form newsletter': dict(
  ist=[('Footer navigation', 'Tautan sekunder: kontak, kebijakan privasi, sosial media, alamat.'),
       ('Double opt-in', 'Konfirmasi email sebelum dimasukkan ke daftar newsletter.'),
       ('Consent (UU PDP)', 'Persetujuan menerima email promosi harus eksplisit dan bisa ditarik.'),
       ('Form feedback', 'Pesan sukses/error diumumkan dengan aria-live.')],
  cx=[C('Form newsletter yang jelas dan aksesibel', '''
<form class="newsletter" novalidate>
  <label for="email-nl">Email</label>
  <div class="baris">
    <input id="email-nl" type="email" autocomplete="email" required aria-describedby="nl-info nl-status">
    <button type="submit">Langganan</button>
  </div>
  <p id="nl-info" class="kecil">Promo & menu baru 2x sebulan. Berhenti kapan saja lewat tautan di email.</p>
  <p id="nl-status" role="status" aria-live="polite"></p>
</form>
<script>
  document.querySelector(".newsletter").addEventListener("submit", (e) => {
    e.preventDefault();
    const i = e.target.querySelector("input"), s = document.getElementById("nl-status");
    s.textContent = i.checkValidity() ? "Cek email untuk konfirmasi langganan." : "Format email belum benar, contoh: nama@domain.com";
  });
</script>
''', lang='html')]),

'Mobile-first dan breakpoint dari desain': dict(
  ist=[('Mobile-first', 'Gaya dasar untuk layar kecil, lalu min-width media query menambah tata letak lebar.'),
       ('Design breakpoint', 'Lebar frame di Figma (360, 768, 1440) sebagai acuan, bukan satu-satunya lebar yang diuji.'),
       ('In-between sizes', 'Lebar di antara breakpoint (500, 900, 1100) yang sering memunculkan bug.'),
       ('Container width', 'Konten dibatasi max-width dan diberi gutter.')],
  cx=[P('Menguji ukuran di antara breakpoint desain', '''
desain = [360, 768, 1440]
breakpoint_css = [768, 1024]
uji = sorted(set(desain + [320, 414, 600, 900, 1024, 1180, 1920]))
def layout(w):
    return "1 kolom" if w < 768 else "2 kolom" if w < 1024 else "3 kolom"
for w in uji:
    tanda = "desain" if w in desain else "uji tambahan"
    konten = min(w - 32, 1200)
    print(f"{w:>5}px  {layout(w):8} lebar konten {konten:>5}px  ({tanda})")
''')]),

'Gambar responsif dengan srcset': dict(
  ist=[('srcset & sizes', 'Daftar varian gambar dan perkiraan lebar tampil agar browser memilih file yang tepat.'),
       ('Device pixel ratio (DPR)', 'Kepadatan piksel layar; HP modern 2x-3x.'),
       ('<picture>', 'Memilih format (AVIF/WebP/JPEG) atau potongan gambar berbeda per breakpoint (art direction).'),
       ('Image CDN', 'Layanan yang mengubah ukuran dan format gambar otomatis lewat URL.')],
  cx=[P('Menghitung file yang dipilih browser dari srcset', '''
varian = [480, 800, 1200, 1600]
def pilih(lebar_tampil_css, dpr):
    butuh = lebar_tampil_css * dpr
    return next((v for v in varian if v >= butuh), varian[-1]), butuh
for perangkat, viewport, dpr, sizes_vw in [("HP Android 360px", 360, 3, 1.0), ("iPhone 390px", 390, 3, 1.0),
                                            ("Tablet 768px", 768, 2, 1.0), ("Laptop 1440px", 1440, 1, 0.5)]:
    v, butuh = pilih(viewport * sizes_vw, dpr)
    print(f"{perangkat:17} butuh ~{butuh:>5.0f}px -> hero-{v}.avif")
''')]),

'Pixel-perfect: membandingkan dengan desain': dict(
  ist=[('Overlay comparison', 'Menumpuk screenshot desain di atas hasil build (PerfectPixel, Pixel Parallel).'),
       ('Visual diff', 'Perbandingan gambar otomatis yang menyorot piksel berbeda.'),
       ('Tolerance', 'Ambang perbedaan yang diterima (rendering font antar OS berbeda sedikit).'),
       ('Design QA notes', 'Daftar perbedaan beserta tangkapan layar dan prioritas perbaikan.')],
  cx=[P('Visual diff sederhana antara dua tangkapan (matriks piksel)', '''
import numpy as np
rng = np.random.default_rng(0)
desain = rng.integers(0, 256, (80, 120))          # anggap grayscale 120x80
build = desain.copy()
build[10:14, 20:100] = np.clip(build[10:14, 20:100] + 40, 0, 255)   # judul turun 4px / warna beda
build[60:70, 5:9] = 0                                               # ikon hilang
beda = np.abs(build.astype(int) - desain.astype(int)) > 16           # toleransi anti-aliasing
ys, xs = np.nonzero(beda)
print(f"piksel berbeda: {beda.mean():.2%}")
print(f"area berbeda: x {xs.min()}-{xs.max()}, y {ys.min()}-{ys.max()}")
print("lolos (≤ 1%)" if beda.mean() <= 0.01 else "perlu dicek manual")
''')]),

'Aksesibilitas hasil slicing': dict(
  ist=[('Keyboard navigation', 'Semua fungsi bisa dipakai dengan Tab, Enter, Spasi, Esc.'),
       ('Alt text', 'Deskripsi gambar yang bermakna; gambar dekoratif diberi alt="".'),
       ('Lighthouse / axe', 'Alat audit otomatis; hanya menangkap sebagian masalah, tetap uji manual.'),
       ('Screen reader testing', 'Uji dengan NVDA (Windows), VoiceOver (macOS/iOS), TalkBack (Android).')],
  cx=[P('Pemeriksaan otomatis kecil: alt, label, dan heading', '''
from html.parser import HTMLParser
html = """<h1>Kopi Kita</h1><h3>Menu</h3><img src="a.jpg"><img src="b.jpg" alt="">
<input id="e" type="email"><label for="n">Nama</label><input id="n"><button></button>"""
class Cek(HTMLParser):
    def __init__(self):
        super().__init__(); self.masalah, self.label_for, self.input_id, self.heading = [], set(), [], []
    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "img" and "alt" not in a: self.masalah.append(f"img {a.get('src')} tanpa alt")
        if tag == "label": self.label_for.add(a.get("for"))
        if tag == "input": self.input_id.append(a.get("id"))
        if tag in ("h1", "h2", "h3", "h4"): self.heading.append(int(tag[1]))
        if tag == "button": self._btn = True
    def handle_endtag(self, tag):
        if tag == "button" and getattr(self, "_btn", False): self.masalah.append("button tanpa teks/aria-label")
        self._btn = False
    def handle_data(self, d):
        if d.strip(): self._btn = False
c = Cek(); c.feed(html)
c.masalah += [f"input #{i} tanpa label" for i in c.input_id if i not in c.label_for]
c.masalah += [f"heading lompat h{a} -> h{b}" for a, b in zip(c.heading, c.heading[1:]) if b - a > 1]
print("\\n".join(c.masalah))
''')]),

'Proyek: landing page kedai kopi': dict(
  ist=[('Landing page', 'Halaman tunggal dengan satu tujuan konversi (pesan, daftar, kunjungi).'),
       ('Conversion goal', 'Aksi yang diukur: klik "Pesan via WhatsApp", isi form reservasi.'),
       ('Local SEO', 'Nama usaha, alamat, jam buka, dan data terstruktur LocalBusiness agar muncul di pencarian lokal.'),
       ('Open Graph', 'Meta tag pratinjau saat tautan dibagikan di WhatsApp/sosial media.')],
  cx=[C('Meta SEO lokal dan data terstruktur kedai kopi', '''
<title>Kopi Kita Medan · Kopi Gayo sangrai segar</title>
<meta name="description" content="Kedai kopi di Jl. Sei Batang Hari, Medan. Kopi Gayo disangrai tiap Senin. Buka 07.00-22.00.">
<meta property="og:title" content="Kopi Kita Medan">
<meta property="og:image" content="https://kopikita.id/og.jpg">
<script type="application/ld+json">
{
  "@context": "https://schema.org", "@type": "CafeOrCoffeeShop",
  "name": "Kopi Kita", "telephone": "+62-61-0000-000",
  "address": { "@type": "PostalAddress", "streetAddress": "Jl. Sei Batang Hari No. 10",
               "addressLocality": "Medan", "addressRegion": "Sumatera Utara", "addressCountry": "ID" },
  "openingHours": "Mo-Su 07:00-22:00", "servesCuisine": "Kopi"
}
</script>
''', lang='html')]),

'Deploy hasil slicing': dict(
  ist=[('Static hosting', 'Hosting berkas HTML/CSS/JS: GitHub Pages, Netlify, Vercel, Cloudflare Pages.'),
       ('Preview deployment', 'URL pratinjau otomatis untuk setiap branch/pull request agar klien bisa meninjau.'),
       ('Custom domain & HTTPS', 'Domain sendiri (kopikita.id) dengan sertifikat TLS otomatis.'),
       ('Cache headers', 'Aset bernama hash di-cache lama; HTML di-cache singkat.')],
  cx=[C('Konfigurasi header cache dan keamanan (Netlify/Cloudflare Pages _headers)', '''
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*.html
  Cache-Control: public, max-age=0, must-revalidate
''', lang='text')]),

'Daftar periksa QA sebelum serah terima': dict(
  ist=[('Cross-browser testing', 'Uji di Chrome, Safari (iOS!), Firefox, dan browser bawaan Samsung.'),
       ('Core Web Vitals', 'LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 (persentil 75).'),
       ('Acceptance', 'Klien menyetujui hasil berdasarkan daftar yang disepakati, bukan selera mendadak.'),
       ('Handover document', 'Panduan: cara mengubah teks/gambar, akses hosting, domain, dan kontak dukungan.')],
  cx=[P('Ringkasan QA dari hasil pemeriksaan', '''
hasil = {
    "LCP (s)": (2.1, 2.5, "<="), "CLS": (0.04, 0.1, "<="), "INP (ms)": (180, 200, "<="),
    "skor aksesibilitas Lighthouse": (96, 90, ">="), "ukuran halaman (KB)": (720, 1000, "<="),
    "lebar 320px tanpa scroll horizontal": (1, 1, ">="), "Safari iOS diuji": (0, 1, ">="),
}
gagal = []
for k, (v, batas, op) in hasil.items():
    ok = v <= batas if op == "<=" else v >= batas
    print(f"{'LULUS' if ok else 'GAGAL'}  {k:38} {v} (target {op} {batas})")
    if not ok: gagal.append(k)
print("Siap serah terima" if not gagal else f"Tunda serah terima: {gagal}")
''')]),

'Contoh desain: papan Figma "Kopi Kita"': dict(
  ist=[('Design board', 'Halaman Figma berisi semua frame: mobile, tablet, desktop, komponen, style.'),
       ('Frame naming', 'Nama frame jelas (Home / Mobile 360) memudahkan slicer menemukan bagian.'),
       ('Local styles / variables', 'Warna dan teks bernama di papan desain yang menjadi sumber token.'),
       ('Asset export', 'Tanda ekspor pada gambar/ikon yang perlu diunduh slicer.')],
  cx=[C('Inventaris papan desain sebelum mulai koding', '''
HALAMAN FIGMA "Kopi Kita"
├─ 🎨 Style       warna (6), teks (8), efek (2), grid (3)
├─ 🧩 Komponen    Button (primary/ghost × sm/md), KartuMenu (normal/habis), Navbar, Footer
├─ 📱 Mobile 360  Home, Menu, Lokasi
├─ 💻 Tablet 768  Home
└─ 🖥 Desktop 1440 Home, Menu

PERTANYAAN UNTUK DESAINER
1. Hover & focus tombol belum ada → pakai warna accent -10%?
2. Teks testimoni panjang (> 200 karakter) dipotong atau kartu memanjang?
3. Gambar hero desktop beda crop dengan mobile? (art direction <picture>)
''', lang='text')]),

'Langkah 1: audit desain dan inventaris komponen': dict(
  ist=[('Design audit', 'Memeriksa konsistensi desain sebelum koding: jarak, warna, komponen yang mirip.'),
       ('Component inventory', 'Daftar komponen unik dan di mana dipakai.'),
       ('Clarification log', 'Catatan pertanyaan ke desainer dan jawabannya.'),
       ('Estimation', 'Perkiraan waktu per section setelah inventaris lengkap.')],
  cx=[P('Mendeteksi nilai jarak yang tidak konsisten dari hasil inspeksi', '''
from collections import Counter
jarak = [16, 16, 24, 15, 16, 32, 24, 17, 48, 16, 24, 23, 32, 64, 16, 24]
c = Counter(jarak)
resmi = {4, 8, 12, 16, 24, 32, 48, 64}
print("dipakai:", dict(sorted(c.items())))
liar = {v: n for v, n in c.items() if v not in resmi}
print("di luar skala (tanyakan/bulatkan):", liar)
''')]),

'Langkah 2: token desain menjadi CSS variables': dict(
  ist=[('Token extraction', 'Mengambil nilai dari Figma Variables/Styles menjadi file token.'),
       ('Tokens Studio / Variables export', 'Plugin/fitur untuk mengekspor token JSON dari Figma.'),
       ('Single source', 'Token diubah di satu tempat lalu dibangkitkan ke CSS.'),
       ('Naming check', 'Nama token bermakna dan konsisten (color-text-muted, bukan abu2).')],
  cx=[P('Membangkitkan CSS variables dari daftar style Figma', '''
style = [("Warna/Latar", "#FFFBF5"), ("Warna/Teks", "#2B1D14"), ("Warna/Aksen", "#B45309"), ("Warna/Aksen Gelap", "#92400E"),
         ("Teks/Judul H1", "700 40/48 Fraunces"), ("Teks/Isi", "400 16/26 Inter")]
def slug(s):
    return s.lower().replace("warna/", "color-").replace("teks/", "type-").replace(" ", "-")
print(":root {")
for nama, v in style:
    if v.startswith("#"):
        print(f"  --{slug(nama)}: {v};")
    else:
        bobot, ukuran, font = v.split(" ", 2)
        px, lh = ukuran.split("/")
        print(f"  --{slug(nama)}: {bobot} {int(px) / 16:g}rem/{int(lh) / int(px):.3g} \\"{font}\\", system-ui, sans-serif;")
print("}")
''')]),

'Langkah 3: kerangka HTML semantik': dict(
  ist=[('Document outline', 'Urutan heading yang mencerminkan struktur konten.'),
       ('Content-first markup', 'Tulis HTML dari konten dan makna dulu, baru gaya.'),
       ('ARIA as last resort', 'Gunakan elemen HTML asli dulu; ARIA hanya jika tidak ada padanan.'),
       ('Validator', 'Periksa HTML dengan validator W3C untuk menangkap tag yang tidak ditutup.')],
  cx=[P('Membuat outline heading dari HTML', '''
import re
html = """<h1>Kopi Gayo diseduh pelan</h1><h2>Menu favorit</h2><h3>Kopi susu gula aren</h3><h3>V60 Gayo</h3>
<h2>Kenapa Kopi Kita</h2><h2>Testimoni</h2><h2>Lokasi & jam buka</h2>"""
for level, teks in re.findall(r"<h([1-6])>(.*?)</h\\1>", html):
    print("  " * (int(level) - 1) + f"h{level} {teks}")
''')]),

'Langkah 4: layout mobile-first untuk navbar dan hero': dict(
  ist=[('Base styles', 'Gaya tanpa media query adalah gaya untuk layar terkecil.'),
       ('Logical properties', 'padding-inline, margin-block: mendukung arah tulisan dan lebih ringkas.'),
       ('dvh', 'Satuan tinggi viewport dinamis yang memperhitungkan bilah alamat browser HP.'),
       ('Safe area', 'env(safe-area-inset-*) agar konten tidak tertutup notch atau bilah sistem.')],
  cx=[C('Hero mobile-first dengan dvh dan safe area', '''
.hero {
  min-height: calc(100dvh - var(--tinggi-header));
  padding-block: 32px;
  padding-inline: max(16px, env(safe-area-inset-left)) max(16px, env(safe-area-inset-right));
  display: grid; align-content: center; gap: 24px;
}
.hero h1 { font-size: clamp(2rem, 7vw, 3.5rem); line-height: 1.1; }
.hero .cta { display: grid; gap: 12px; }                 /* tombol bertumpuk di HP */
@media (min-width: 640px) { .hero .cta { grid-auto-flow: column; justify-content: start; } }
''')]),

'Langkah 5: komponen kartu produk dan grid': dict(
  ist=[('Intrinsic layout', 'Tata letak yang menyesuaikan ruang tanpa banyak breakpoint (auto-fill, minmax, clamp).'),
       ('line-clamp', 'Memotong teks setelah N baris dengan elipsis.'),
       ('Empty & loading state', 'Kartu skeleton saat memuat dan pesan saat menu kosong.'),
       ('Consistent card height', 'Tombol di dasar kartu sejajar memakai grid/flex dengan margin-top: auto.')],
  cx=[C('Grid kartu menu dengan judul 2 baris dan tombol sejajar', '''
.grid-menu { display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 220px), 1fr)); }
.kartu-menu { display: flex; flex-direction: column; gap: 8px; }
.kartu-menu__nama { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.kartu-menu .btn { margin-top: auto; }                   /* tombol selalu di dasar kartu */
.kartu-menu.skeleton * { color: transparent; background: linear-gradient(90deg, #eee, #f6f6f6, #eee); border-radius: 6px; }
''')]),

'Langkah 6: layout desktop untuk kontainer, navbar, dan hero': dict(
  ist=[('Layout shift at breakpoint', 'Perubahan tata letak besar di breakpoint; uji transisinya di lebar tepat batas.'),
       ('Max-width container', 'Konten desktop tidak melebar penuh di monitor 1920px.'),
       ('Hover-only features', 'Interaksi hover harus punya padanan untuk sentuh dan keyboard; cek @media (hover: hover).'),
       ('Grid template areas', 'Penamaan area grid agar perubahan layout per breakpoint mudah dibaca.')],
  cx=[C('Perubahan layout desktop dengan grid-template-areas', '''
.halaman { width: min(100% - 32px, 1200px); margin-inline: auto; }
.tentang { display: grid; gap: 24px; grid-template-areas: "foto" "teks" "angka"; }
@media (min-width: 1024px) {
  .tentang { grid-template-columns: 5fr 7fr; grid-template-areas: "foto teks" "foto angka"; gap: 32px 64px; }
}
.tentang .foto { grid-area: foto; } .tentang .teks { grid-area: teks; } .tentang .angka { grid-area: angka; }
@media (hover: hover) { .kartu-menu:hover { transform: translateY(-2px); } }
''')]),

'Langkah 7: layout desktop untuk produk, CTA, dan footer': dict(
  ist=[('Container width', 'Batas lebar isi (misal 1120 px) agar baris teks dan kartu tidak melebar di monitor besar.'),
       ('Gutter', 'Jarak antar kolom grid; di desain ini 16 di HP dan 24 di desktop.'),
       ('Minor breakpoint', 'Breakpoint kecil yang hanya menyempurnakan ukuran, bukan susunan.'),
       ('Visual regression', 'Membandingkan tangkapan layar tiap lebar dengan frame desain secara otomatis.')],
  cx=[C('Tangkapan layar tiga lebar untuk dibandingkan dengan frame Figma (Playwright)', '''
// npx playwright test qa-lebar.spec.js
import { test, expect } from '@playwright/test';
for (const lebar of [360, 768, 1440]) {
  test(`landing ${lebar}px sesuai desain`, async ({ page }) => {
    await page.setViewportSize({ width: lebar, height: 900 });
    await page.goto('http://localhost:5173/');
    await expect(page).toHaveScreenshot(`landing-${lebar}.png`, { fullPage: true, maxDiffPixelRatio: 0.01 });
  });
}
''', lang='js')]),

'Langkah 8: state, aksesibilitas, dan QA pixel-perfect': dict(
  ist=[('Interactive states', 'hover, focus-visible, active, disabled untuk semua elemen interaktif.'),
       ('Focus order', 'Urutan Tab mengikuti urutan visual dan logis.'),
       ('Reduced motion', 'Animasi dimatikan/dikurangi untuk pengguna yang memintanya.'),
       ('QA sign-off', 'Persetujuan desainer bahwa hasil sesuai desain.')],
  cx=[C('Gaya fokus global dan pengurangan animasi', '''
:where(a, button, input, select, textarea, [tabindex]):focus-visible {
  outline: 3px solid var(--color-accent);
  outline-offset: 3px;
  border-radius: 4px;
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important;
                           transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
''')]),

'Hasil akhir dan checklist serah terima': dict(
  ist=[('Deliverables', 'Repo kode, URL produksi, URL pratinjau, aset sumber, dokumentasi.'),
       ('README', 'Cara menjalankan, struktur folder, cara mengubah konten, cara deploy.'),
       ('Warranty period', 'Masa perbaikan bug gratis setelah serah terima (misalnya 14-30 hari).'),
       ('Lighthouse report', 'Lampiran skor performa, aksesibilitas, praktik terbaik, dan SEO.')],
  cx=[C('README serah terima proyek slicing', '''
# Kopi Kita – Landing Page

Produksi : https://kopikita.id       Pratinjau: https://preview.kopikita.pages.dev

## Struktur
index.html · css/ (tokens.css, base.css, components.css) · img/ (AVIF + fallback JPEG) · js/menu.js

## Mengubah konten
- Menu & harga: ubah `data/menu.json`, lalu push ke branch `main` (deploy otomatis ±1 menit)
- Jam buka: `index.html` bagian `<section id="lokasi">` dan data JSON-LD di `<head>`

## Kualitas saat serah terima (19/11/2026)
LCP 2,1 s · CLS 0,04 · Aksesibilitas 96 · Diuji: Chrome Android, Safari iOS 18, Firefox, Samsung Internet

## Garansi
Perbaikan bug 30 hari sejak serah terima. Perubahan desain di luar lingkup dihitung terpisah.
''', lang='markdown')]),
}
