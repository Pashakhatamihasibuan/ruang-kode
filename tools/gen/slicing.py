"""Isi jalur Slicing Website (Figma ke HTML/CSS, lab langsung) dan Slicing Mobile (Figma ke Flutter dan Jetpack Compose)."""
from mobile_lib import W, C, M, q
from mobile_dart_x import S
from uidesign import L, H, X, T, G, RULES


def D(soal, petunjuk, jawab, out=None):
    return S(soal, petunjuk, jawab, out, lang='dart')


def K(soal, petunjuk, jawab, out=None):
    return S(soal, petunjuk, jawab, out, lang='kotlin')


BASE = 'body { font-family: system-ui, sans-serif; margin: 0; color: #1F2933; }\n'

SLW = [
M('Persiapan slicing', 'Pemula',
  'Apa itu slicing, membaca desain di Figma Dev Mode, memindahkan token desain ke CSS variables, dan menyusun HTML semantik dari desain.',
  ['Slicing', 'Figma Dev Mode', 'Design tokens', 'Semantic HTML'], [
  C('Apa itu slicing dan alurnya',
    ['<b>Slicing</b> adalah mengubah desain statis (Figma, Adobe XD, Penpot) menjadi halaman web atau aplikasi yang benar-benar berjalan. Istilah ini berasal dari zaman dulu, saat desain Photoshop "diiris" menjadi potongan gambar. Sekarang yang diiris adalah <b>struktur</b>: section, komponen, dan token.',
     'Alur kerja slicer profesional: (1) <b>pelajari desain</b> secara utuh, termasuk versi mobile dan desktop; (2) <b>pecah halaman</b> menjadi section (navbar, hero, fitur, testimoni, harga, footer); (3) temukan <b>komponen berulang</b> (tombol, kartu, input); (4) catat <b>token</b> (warna, font, spacing, radius); (5) siapkan <b>aset</b> (ikon SVG, gambar WebP); (6) tulis <b>HTML semantik</b> dulu; (7) tulis CSS <b>mobile-first</b>; (8) bandingkan dengan desain (<b>pixel-perfect</b>); (9) uji di perangkat nyata.',
     'Kesalahan pemula: langsung menulis CSS dari section paling atas sampai bawah tanpa melihat pola. Hasilnya tombol yang sama ditulis lima kali dengan ukuran sedikit berbeda. Luangkan 15 menit di awal untuk mencatat komponen dan token, dan kamu akan menghemat berjam-jam.'],
    tb=[{'c': 'Pembagian halaman landing page', 'h': ['Section', 'Elemen HTML', 'Komponen di dalamnya'], 'r': [
      ['Navbar', 'header > nav', 'Logo, link, tombol masuk, tombol menu (mobile)'], ['Hero', 'section', 'Judul, deskripsi, 2 tombol, gambar'],
      ['Fitur', 'section', 'Kartu fitur × 3 sampai 6 (ikon, judul, teks)'], ['Testimoni', 'section', 'Kartu kutipan, foto, nama'],
      ['Harga', 'section', 'Kartu paket × 3, lencana "Paling populer"'], ['Footer', 'footer', 'Link, form newsletter, hak cipta']]}],
    pts=['Slicing = desain statis menjadi kode yang berjalan.', 'Pecah section, temukan komponen dan token dulu.', 'HTML semantik dulu, lalu CSS mobile-first.'],
    qs=[q('Langkah yang sebaiknya dilakukan sebelum menulis CSS?', ['Mencatat komponen berulang dan token', 'Mengekspor semua frame jadi PNG', 'Menulis JavaScript'], 0, 'Pola dulu, kode kemudian.'),
        q('Kenapa slicing dimulai dari mobile?', ['Layar kecil lebih mudah diperluas daripada sebaliknya', 'Desainer selalu mulai dari mobile', 'Aturan Figma'], 0, 'Mobile-first: tambahkan aturan saat layar melebar.')]),
  C('Membaca desain di Figma Dev Mode',
    ['<b>Dev Mode</b> (ikon &lt;/&gt; atau Shift + D di Figma) adalah tampilan khusus developer. Klik elemen untuk melihat <b>ukuran</b>, <b>jarak</b> ke elemen lain (tahan Alt atau Option sambil mengarahkan kursor), <b>warna</b> dan nama variabelnya, <b>tipografi</b>, serta potongan kode CSS. Developer tidak bisa mengubah desain secara tidak sengaja di mode ini.',
     'Cara membaca auto layout: frame dengan auto layout ditampilkan sebagai <code>display: flex</code>, lengkap dengan <code>gap</code>, <code>padding</code>, dan arah. Hug contents berarti lebar mengikuti isi, Fill container berarti <code>flex: 1</code> atau <code>width: 100%</code>. Jangan menyalin <code>position: absolute</code> dan <code>width</code> piksel tetap dari panel kode mentah-mentah; itu hanya cocok untuk ukuran frame itu saja.',
     'Kebiasaan baik: periksa nama <b>variabel</b> (misalnya <code>color/brand/600</code>) dan pakai nama itu di CSS, bukan kode hex. Periksa juga apakah frame ditandai <b>Ready for dev</b>; frame lain mungkin masih eksplorasi. Jika tidak punya akses Dev Mode (berbayar), mode Inspect di akun gratis tetap menampilkan ukuran dan warna.'],
    tb=[{'c': 'Figma ke CSS', 'h': ['Di Figma', 'Di CSS'], 'r': [
      ['Auto layout horizontal, gap 16', 'display: flex; gap: 16px'], ['Auto layout vertical', 'display: flex; flex-direction: column'],
      ['Padding 24 / 16', 'padding: 24px 16px'], ['Hug contents', 'width: auto (atau fit-content)'], ['Fill container', 'flex: 1 atau width: 100%'],
      ['Corner radius 12', 'border-radius: 12px'], ['Drop shadow 0 4 12 #0000001F', 'box-shadow: 0 4px 12px rgb(0 0 0 / .12)'],
      ['Text Inter 16/24 Medium', 'font: 500 16px/24px Inter'], ['Constraints Left & Right', 'lebar melar mengikuti induk'], ['Layer opacity 60%', 'opacity: .6']]}],
    pts=['Dev Mode: ukuran, jarak, variabel, kode.', 'Auto layout = flexbox; jangan salin posisi absolut mentah.', 'Pakai nama variabel, cek status Ready for dev.'],
    qs=[q('Cara melihat jarak antara dua elemen di Figma?', ['Pilih satu elemen, tahan Alt/Option, arahkan ke elemen lain', 'Klik kanan lalu Measure', 'Tidak bisa'], 0, 'Figma menampilkan jarak merah.'),
        q('Panel kode Figma menulis position: absolute; left: 132px. Sebaiknya?', ['Salin persis', 'Terjemahkan ke flex atau grid sesuai auto layout', 'Abaikan elemennya'], 1, 'Posisi absolut hanya pas di satu ukuran frame.')]),
  L('Token desain ke CSS variables',
    ['Langkah pertama menulis CSS dari desain: pindahkan <b>token</b> ke <code>:root</code>. Buka panel Variables di Figma (atau Local styles untuk file lama) dan salin warna, font, spacing, radius, dan bayangan menjadi CSS variables.',
     'Setelah token ada, <b>semua</b> aturan CSS memakai <code>var(--...)</code>. Jika desainer mengubah warna merek minggu depan, kamu cukup mengubah satu baris. Jika desain punya mode gelap, tambahkan blok token kedua.',
     'Beri nama variabel sama seperti di Figma agar mudah dicocokkan: <code>color/brand/600</code> menjadi <code>--color-brand-600</code>, <code>spacing/4</code> menjadi <code>--spacing-4</code>.',
     'Desain di pratinjau memakai warna merek #0F766E dan radius 12. Pindahkan ke token.'],
    html='''<section class="promo">
  <h2>Kelas baru: Slicing Website</h2>
  <p>Ubah desain Figma menjadi halaman nyata.</p>
  <a class="tombol" href="#">Daftar</a>
</section>''',
    css=BASE + ''':root {
  /* token dari Figma: tulis di sini */
}
.promo { margin: 16px; padding: 24px; border-radius: 12px; background: #CCFBF1; }
.promo h2 { margin: 0 0 8px; color: #134E4A; }
.tombol { display: inline-block; margin-top: 8px; padding: 12px 24px; border-radius: 12px; background: #0F766E; color: #fff; text-decoration: none; font-weight: 600; }''',
    task={'q': 'Buat token <code>--color-brand-600: #0F766E</code> dan <code>--radius-md: 12px</code> di <code>:root</code>, lalu pakai keduanya di <code>.tombol</code>.',
          'test': f"getComputedStyle(document.documentElement).getPropertyValue('--color-brand-600').trim().toLowerCase()==='#0f766e'&&{RULES}.some(r=>r.selectorText==='.tombol'&&/var\\(--color-brand-600\\)/.test(r.style.cssText)&&/var\\(--radius-md\\)/.test(r.style.cssText))",
          'hint': ':root { --color-brand-600: #0F766E; --radius-md: 12px } lalu .tombol { background: var(--color-brand-600); border-radius: var(--radius-md) }'},
    pts=['Token dari Figma Variables ke :root.', 'Semua aturan memakai var().', 'Nama variabel sama dengan nama di Figma.'],
    qs=[q('Nama CSS yang cocok untuk variabel Figma spacing/4?', ['--spacing-4', '--s4px', '--jarak'], 0, 'Sama dengan nama di Figma.')],
    cek={'css': ':root{--color-brand-600:#0F766E;--radius-md:12px}.tombol{background:var(--color-brand-600);border-radius:var(--radius-md)}'}),
  L('HTML semantik dari desain',
    ['Desain hanya menunjukkan <b>rupa</b>; slicer yang menentukan <b>makna</b>. Navbar adalah <code>&lt;header&gt;</code> berisi <code>&lt;nav&gt;</code>, isi utama adalah <code>&lt;main&gt;</code>, setiap bagian adalah <code>&lt;section&gt;</code> dengan judul, kartu artikel adalah <code>&lt;article&gt;</code>, dan bagian bawah adalah <code>&lt;footer&gt;</code>.',
     'Judul harus berurutan: satu <code>&lt;h1&gt;</code> per halaman (biasanya judul hero), lalu <code>&lt;h2&gt;</code> untuk judul section, <code>&lt;h3&gt;</code> untuk judul kartu. Pilih tag berdasarkan <b>tingkat</b>, bukan ukuran huruf di desain; ukuran diatur oleh CSS.',
     'Yang terlihat seperti tombol tetapi pindah halaman adalah <code>&lt;a&gt;</code>; yang menjalankan aksi di halaman yang sama adalah <code>&lt;button&gt;</code>. HTML semantik membuat halaman terbaca pembaca layar, mudah ditemukan Google, dan lebih mudah di-styling.',
     'Kerangka di pratinjau hanya berisi div. Ganti dengan landmark yang tepat.'],
    html='''<div class="atas"><div class="logo">RuangKode</div><div class="menu"><a href="#">Kelas</a><a href="#">Harga</a></div></div>
<div class="isi">
  <div class="judul-besar">Belajar slicing dari desain nyata</div>
  <p>Latihan dengan file Figma sungguhan.</p>
</div>
<div class="bawah">© 2026 RuangKode</div>''',
    css=BASE + '''.atas, header { display: flex; justify-content: space-between; align-items: center; padding: 16px; border-bottom: 1px solid #E4E7EB; }
.menu, nav { display: flex; gap: 16px; }
.isi, main { padding: 24px 16px; }
.judul-besar, h1 { font-size: 28px; font-weight: 700; margin: 0 0 8px; }
.bawah, footer { padding: 16px; color: #52606D; font-size: 14px; }''',
    task={'q': 'Ganti kerangkanya: <code>header</code> berisi <code>nav</code>, <code>main</code> berisi <code>h1</code>, dan <code>footer</code>.',
          'test': "!!document.querySelector('header nav')&&!!document.querySelector('main h1')&&!!document.querySelector('footer')",
          'hint': '<header><div class="logo">RuangKode</div><nav>...</nav></header><main><h1>...</h1><p>...</p></main><footer>...</footer>'},
    pts=['header, nav, main, section, article, footer.', 'Satu h1, judul berurutan.', 'Pindah halaman: a. Aksi di halaman: button.'],
    qs=[q('Tombol "Lihat kelas" yang membuka halaman lain sebaiknya memakai?', ['button', 'a', 'div'], 1, 'Navigasi memakai tautan.'),
        q('Berapa h1 dalam satu halaman?', ['Satu', 'Satu per section', 'Bebas'], 0, 'h1 adalah judul halaman.')],
    cek={'html': '<header><nav><a>Kelas</a></nav></header><main><h1>Judul</h1></main><footer>c</footer>'}),
]),
M('Slicing komponen', 'Pemula',
  'Navbar responsif, hero section, tombol dan kartu dari komponen Figma, serta ikon dan gambar yang dioptimalkan.',
  ['Navbar', 'Hero', 'Components', 'Images'], [
  L('Navbar responsif',
    ['Navbar di desain biasanya: logo di kiri, link di tengah atau kanan, tombol aksi di kanan. Di CSS cukup flexbox: <code>display: flex; justify-content: space-between; align-items: center</code>.',
     'Di mobile, link biasanya disembunyikan di balik tombol menu (hamburger). Cara tanpa JavaScript: <code>&lt;details&gt;</code> dan <code>&lt;summary&gt;</code>. Cara umum: tombol dengan <code>aria-expanded</code> yang mengubah kelas menu lewat JavaScript. Ukur tinggi navbar dari desain (biasanya 56 sampai 72 px) dan pastikan setiap link punya area klik yang cukup.',
     'Untuk navbar yang tetap terlihat saat menggulir, pakai <code>position: sticky; top: 0</code> dan beri latar serta <code>z-index</code> agar konten tidak tembus.',
     'Navbar di pratinjau masih menumpuk. Susun dengan flexbox.'],
    html='''<header class="nav">
  <a class="logo" href="#">Kopi<b>Nusa</b></a>
  <nav class="link"><a href="#">Menu</a><a href="#">Lokasi</a><a href="#">Tentang</a></nav>
  <a class="cta" href="#">Pesan</a>
</header>
<main style="padding:16px">Konten halaman...</main>''',
    css=BASE + '''.nav { padding: 12px 16px; border-bottom: 1px solid #E7E0D8; background: #FFFBF5; }
.logo { font-size: 20px; color: #3E2723; text-decoration: none; }
.link { display: flex; gap: 16px; }
.link a { color: #5D4037; text-decoration: none; padding: 8px 0; }
.cta { background: #6D4C41; color: #fff; padding: 8px 16px; border-radius: 999px; text-decoration: none; }''',
    task={'q': 'Jadikan <code>.nav</code> flex: <code>display: flex; justify-content: space-between; align-items: center</code>, dan buat navbar menempel saat menggulir (<code>position: sticky; top: 0</code>).',
          'test': f"(s=>s.display==='flex'&&s.justifyContent==='space-between'&&s.position==='sticky')({G.format('.nav')})",
          'hint': '.nav { display: flex; justify-content: space-between; align-items: center; gap: 16px; position: sticky; top: 0 }'},
    pts=['Navbar: flex + space-between + align-items center.', 'Mobile: menu tersembunyi dengan aria-expanded.', 'Sticky: position sticky, top 0, latar, z-index.'],
    qs=[q('Properti yang mendorong logo ke kiri dan tombol ke kanan?', ['justify-content: space-between', 'text-align: justify', 'float: right'], 0, 'Ruang dibagi di antara item.')],
    cek={'css': '.nav{display:flex;justify-content:space-between;align-items:center;position:sticky;top:0}'}),
  L('Hero section',
    ['<b>Hero</b> adalah section pertama yang dilihat pengunjung: judul (h1), satu sampai dua kalimat penjelas, satu sampai dua tombol, dan gambar. Di desktop biasanya dua kolom (teks kiri, gambar kanan); di mobile menjadi satu kolom dengan gambar di bawah atau di atas teks.',
     'Ukur dari desain: lebar maksimum teks, jarak judul ke deskripsi, jarak ke tombol. Judul hero memakai ukuran fluid (<code>clamp()</code>) agar tidak terlalu besar di ponsel.',
     'Dua tombol berdampingan bisa terlalu lebar di ponsel kecil. Pakai <code>display: flex; flex-wrap: wrap; gap: 12px</code> agar tombol kedua turun ke baris baru jika tidak muat, bukan memaksa halaman melebar.',
     'Grup tombol di pratinjau belum bisa turun baris.'],
    html='''<section class="hero">
  <div class="teks">
    <h1>Kopi lokal, diseduh hari ini</h1>
    <p>Biji kopi dari Gayo, Toraja, dan Kintamani. Diantar hangat dalam 30 menit.</p>
    <div class="aksi"><a class="btn utama" href="#">Pesan sekarang</a><a class="btn kedua" href="#">Lihat menu lengkap</a></div>
  </div>
  <div class="gambar" role="img" aria-label="Secangkir kopi"></div>
</section>''',
    css=BASE + '''.hero { display: grid; gap: 24px; padding: 32px 16px; background: #FFF8EE; }
@media (min-width: 768px) { .hero { grid-template-columns: 1fr 1fr; align-items: center; padding: 64px 48px; } }
h1 { font-size: clamp(1.75rem, 1rem + 3vw, 3rem); line-height: 1.15; margin: 0 0 12px; color: #3E2723; }
.teks p { margin: 0 0 24px; color: #5D4037; max-width: 45ch; }
.aksi { display: flex; gap: 12px; }
.btn { padding: 12px 20px; border-radius: 12px; text-decoration: none; font-weight: 600; white-space: nowrap; }
.utama { background: #6D4C41; color: #fff; }
.kedua { border: 1px solid #6D4C41; color: #6D4C41; }
.gambar { aspect-ratio: 4 / 3; border-radius: 24px; background: radial-gradient(circle at 40% 40%, #D7B899, #6D4C41); }''',
    task={'q': 'Beri <code>.aksi</code> <code>flex-wrap: wrap</code> agar tombol turun baris di layar sempit.',
          'test': f"{G.format('.aksi')}.flexWrap==='wrap'",
          'hint': '.aksi { flex-wrap: wrap }'},
    pts=['Hero: h1, penjelas singkat, 1–2 tombol, gambar.', 'Dua kolom di desktop, satu kolom di mobile.', 'flex-wrap agar tombol tidak memaksa halaman melebar.'],
    qs=[q('Kenapa grup tombol hero diberi flex-wrap?', ['Agar tombol turun baris di layar sempit', 'Agar tombol berwarna', 'Agar animasi jalan'], 0, 'Tidak ada scroll horizontal.')],
    cek={'css': '.aksi{flex-wrap:wrap}'}),
  L('Tombol dan kartu dari komponen Figma',
    ['Komponen di Figma (tombol, kartu, badge) ditulis <b>sekali</b> sebagai kelas CSS, lalu dipakai ulang. Ambil semua <b>variant</b>-nya dari component set: ukuran, warna, state. Jangan lupa state yang tidak terlihat di frame utama: <b>hover</b>, <b>focus-visible</b>, <b>active</b>, <b>disabled</b>.',
     'Efek hover kartu di desain sering berupa bayangan yang lebih tebal dan kartu sedikit naik. Tulis dengan <code>transition</code> agar halus (150 sampai 250 ms), dan hormati pengguna yang mematikan animasi dengan <code>@media (prefers-reduced-motion: reduce)</code>.',
     'Nilai bayangan Figma <code>X 0, Y 8, Blur 24, Spread 0, #000 12%</code> menjadi <code>box-shadow: 0 8px 24px rgb(0 0 0 / .12)</code>.',
     'Kartu menu di pratinjau belum punya efek hover.'],
    html='''<div class="grid">
  <article class="kartu"><div class="foto"></div><h3>Kopi Susu Aren</h3><p>Rp22.000</p></article>
  <article class="kartu"><div class="foto"></div><h3>Americano</h3><p>Rp18.000</p></article>
</div>''',
    css=BASE + '''.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 16px; padding: 16px; }
.kartu { background: #fff; border-radius: 16px; padding: 12px; box-shadow: 0 1px 3px rgb(0 0 0 / .12); transition: box-shadow .2s, transform .2s; }
.kartu h3 { margin: 12px 0 4px; font-size: 16px; }
.kartu p { margin: 0; color: #6D4C41; font-weight: 600; }
.foto { aspect-ratio: 1; border-radius: 12px; background: #D7B899; }
@media (prefers-reduced-motion: reduce) { .kartu { transition: none; } }''',
    task={'q': 'Tambahkan aturan <code>.kartu:hover</code> dengan <code>box-shadow: 0 8px 24px rgb(0 0 0 / .12)</code> dan <code>transform: translateY(-2px)</code>.',
          'test': f"{RULES}.some(r=>r.selectorText&&r.selectorText.includes('.kartu:hover')&&r.style.boxShadow&&r.style.transform.includes('translateY'))",
          'hint': '.kartu:hover { box-shadow: 0 8px 24px rgb(0 0 0 / .12); transform: translateY(-2px) }'},
    pts=['Satu komponen Figma = satu kelas CSS dengan semua variant dan state.', 'Transisi 150–250 ms dan prefers-reduced-motion.', 'Bayangan Figma X Y Blur Spread → box-shadow.'],
    qs=[q('Drop shadow Figma Y 4, Blur 12, hitam 10% menjadi?', ['box-shadow: 0 4px 12px rgb(0 0 0 / .1)', 'shadow: 4 12', 'text-shadow: 4px'], 0, 'Urutan: x y blur warna.')],
    cek={'css': '.kartu:hover{box-shadow:0 8px 24px rgb(0 0 0 / .12);transform:translateY(-2px)}'}),
  L('Ikon dan gambar yang dioptimalkan',
    ['Ekspor dari Figma: <b>ikon</b> sebagai SVG (pilih ikon, Export, SVG), lalu sisipkan inline atau sebagai <code>&lt;img&gt;</code>. <b>Foto</b> sebagai WebP atau AVIF, dengan lebar 1× dan 2× ukuran tampilannya. Foto 4000 px untuk kartu 300 px membuat halaman lambat terutama di koneksi seluler.',
     'Setiap <code>&lt;img&gt;</code> wajib: <code>alt</code> (deskripsi singkat, atau <code>alt=""</code> jika dekoratif), <code>width</code> dan <code>height</code> (agar browser menyiapkan ruang dan halaman tidak "melompat" saat gambar dimuat, yang diukur sebagai CLS), serta <code>loading="lazy"</code> untuk gambar di bawah layar pertama.',
     'Gambar hero di layar pertama justru <b>jangan</b> diberi lazy; beri <code>fetchpriority="high"</code> agar dimuat paling awal.',
     'Gambar di pratinjau belum punya atribut penting.'],
    html='''<section class="galeri">
  <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 3'%3E%3Crect width='4' height='3' fill='%23D7B899'/%3E%3C/svg%3E">
</section>''',
    css=BASE + '''.galeri { padding: 16px; }
.galeri img { max-width: 100%; height: auto; border-radius: 12px; display: block; }''',
    task={'q': 'Beri gambar <code>alt="Biji kopi Gayo"</code>, <code>width="400"</code>, <code>height="300"</code>, dan <code>loading="lazy"</code>.',
          'test': "(i=>i.alt.length>0&&i.getAttribute('width')&&i.getAttribute('height')&&i.loading==='lazy')(document.querySelector('.galeri img'))",
          'hint': '<img src="..." alt="Biji kopi Gayo" width="400" height="300" loading="lazy">'},
    pts=['Ikon SVG, foto WebP/AVIF 1× dan 2×.', 'alt, width, height, loading="lazy".', 'Gambar hero: tanpa lazy, fetchpriority="high".'],
    qs=[q('Kenapa img diberi width dan height?', ['Agar halaman tidak melompat saat gambar dimuat', 'Agar gambar lebih tajam', 'Wajib untuk SEO'], 0, 'Browser menyiapkan ruang lebih dulu (mengurangi CLS).'),
        q('Gambar hero di bagian paling atas sebaiknya?', ['loading="lazy"', 'Tanpa lazy, fetchpriority="high"'], 1, 'Harus dimuat paling awal.')],
    cek={'html': '<section class="galeri"><img alt="Biji kopi" width="400" height="300" loading="lazy" src="data:,"></section>'}),
]),
M('Slicing section halaman', 'Menengah',
  'Section fitur dengan grid, testimoni dengan scroll-snap, tabel harga dengan paket unggulan, serta footer dan form newsletter.',
  ['Features', 'Testimonials', 'Pricing', 'Footer'], [
  L('Section fitur dengan grid',
    ['Section fitur biasanya: judul section, subjudul, lalu 3 sampai 6 kartu berisi ikon, judul, dan teks singkat. Di desain desktop 3 kolom, tablet 2 kolom, ponsel 1 kolom. Dengan <code>repeat(auto-fit, minmax(240px, 1fr))</code>, kamu tidak perlu menulis media query sama sekali.',
     'Ukur <b>gap</b> antar kartu dan <b>jarak</b> judul section ke grid dari desain. Biasanya judul section rata tengah dengan lebar teks terbatas, sedangkan isi kartu rata kiri.',
     'Ikon di kartu fitur sering diletakkan di dalam lingkaran atau kotak berwarna lembut. Buat dengan <code>display: grid; place-items: center</code> dan ukuran tetap (48 × 48).',
     'Grid fitur di pratinjau belum dibuat.'],
    html='''<section class="fitur">
  <h2>Kenapa belajar di sini?</h2>
  <div class="grid">
    <article><span class="ikon">⚡</span><h3>Langsung praktik</h3><p>Editor jalan di browser, tanpa instalasi.</p></article>
    <article><span class="ikon">🇮🇩</span><h3>Bahasa Indonesia</h3><p>Penjelasan runtut dengan contoh lokal.</p></article>
    <article><span class="ikon">📱</span><h3>Bisa offline</h3><p>Pasang sebagai aplikasi di ponsel.</p></article>
  </div>
</section>''',
    css=BASE + '''.fitur { padding: 48px 16px; max-width: 1080px; margin: 0 auto; }
.fitur h2 { text-align: center; margin: 0 0 32px; }
.grid article { padding: 24px; border-radius: 16px; background: #F5F7FA; }
.grid h3 { margin: 16px 0 8px; font-size: 18px; }
.grid p { margin: 0; color: #52606D; }
.ikon { width: 48px; height: 48px; display: grid; place-items: center; border-radius: 12px; background: #E0F2F1; font-size: 22px; }''',
    task={'q': 'Jadikan <code>.grid</code> grid fluid: <code>display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px</code>.',
          'test': f"{G.format('.grid')}.display==='grid'&&parseFloat({G.format('.grid')}.rowGap)===24&&{RULES}.some(r=>r.selectorText==='.grid'&&/auto-(fit|fill)/.test(r.style.gridTemplateColumns))",
          'hint': '.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px }'},
    pts=['auto-fit + minmax: 1–3 kolom tanpa media query.', 'Judul section rata tengah, isi kartu rata kiri.', 'Ikon dalam kotak 48 × 48 dengan place-items: center.'],
    qs=[q('Keuntungan auto-fit minmax untuk section fitur?', ['Jumlah kolom menyesuaikan lebar tanpa media query', 'Kartu berwarna otomatis', 'Mengurutkan kartu'], 0, 'Grid menghitung sendiri.')],
    cek={'css': '.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px}'}),
  L('Testimoni dengan scroll-snap',
    ['Desain mobile sering menampilkan testimoni sebagai <b>carousel</b> yang digeser horizontal. Kamu tidak perlu library JavaScript: CSS <b>scroll-snap</b> sudah cukup. Wadahnya <code>display: flex; overflow-x: auto; scroll-snap-type: x mandatory</code>, setiap kartu <code>scroll-snap-align: start</code> dan lebar tetap (misalnya 85% layar).',
     'Sisakan sebagian kartu berikutnya terlihat (peek) agar pengguna tahu bisa digeser. Pastikan carousel juga bisa digeser dengan keyboard (beri <code>tabindex="0"</code> dan label pada wadah), dan jangan memutar otomatis tanpa tombol jeda.',
     'Di desktop, carousel yang sama bisa berubah menjadi grid tiga kolom dengan media query.',
     'Wadah testimoni di pratinjau sudah menggulir, tetapi belum "mengunci" ke kartu.'],
    html='''<section class="testi" aria-label="Testimoni siswa" tabindex="0">
  <blockquote class="k">"Akhirnya paham flexbox setelah 3 hari."<cite>Rina, Medan</cite></blockquote>
  <blockquote class="k">"Proyek slicing pertamaku diterima klien."<cite>Andi, Makassar</cite></blockquote>
  <blockquote class="k">"Materinya runtut dan ada soal latihannya."<cite>Sari, Bandung</cite></blockquote>
</section>''',
    css=BASE + '''.testi { display: flex; gap: 12px; overflow-x: auto; padding: 16px; }
.k { flex: 0 0 85%; margin: 0; padding: 24px; border-radius: 16px; background: #EEF2FF; font-size: 17px; }
.k cite { display: block; margin-top: 12px; font-size: 14px; font-style: normal; color: #4338CA; }''',
    task={'q': 'Tambahkan <code>scroll-snap-type: x mandatory</code> pada <code>.testi</code> dan <code>scroll-snap-align: start</code> pada <code>.k</code>.',
          'test': f"{G.format('.testi')}.scrollSnapType.includes('x')&&{G.format('.k')}.scrollSnapAlign.includes('start')",
          'hint': '.testi { scroll-snap-type: x mandatory } .k { scroll-snap-align: start }'},
    pts=['Carousel tanpa JS: overflow-x + scroll-snap.', 'Sisakan peek kartu berikutnya.', 'Bisa digeser keyboard, jangan autoplay tanpa jeda.'],
    qs=[q('Kenapa kartu carousel dibuat 85% lebar, bukan 100%?', ['Agar kartu berikutnya terlihat sedikit sebagai petunjuk bisa digeser', 'Agar hemat memori', 'Aturan CSS'], 0, 'Peek memberi isyarat.')],
    cek={'css': '.testi{scroll-snap-type:x mandatory}.k{scroll-snap-align:start}'}),
  L('Tabel harga dengan paket unggulan',
    ['Section harga berisi 2 sampai 4 kartu paket: nama, harga, periode, daftar fitur, dan tombol. Satu paket biasanya <b>ditonjolkan</b> (paling populer) dengan border tebal warna merek, lencana, dan tombol primary, sementara paket lain memakai tombol secondary.',
     'Tulis harga dengan format lokal yang benar: <b>Rp49.000</b> per bulan (titik sebagai pemisah ribuan, tanpa spasi setelah Rp). Fitur ditulis sebagai daftar <code>&lt;ul&gt;</code> dengan tanda centang; fitur yang tidak termasuk jangan hanya diberi warna abu-abu, beri juga teks atau ikon silang.',
     'Agar tombol semua kartu sejajar di bawah walau daftar fiturnya beda panjang, jadikan kartu <code>display: flex; flex-direction: column</code> dan beri tombol <code>margin-top: auto</code>.',
     'Kartu Pro di pratinjau harus menjadi paket unggulan.'],
    html='''<section class="harga">
  <article class="paket"><h3>Gratis</h3><p class="h">Rp0</p><ul><li>✓ 50 pelajaran</li></ul><a href="#" class="b">Mulai</a></article>
  <article class="paket pro"><h3>Pro</h3><p class="h">Rp49.000<small>/bulan</small></p><ul><li>✓ Semua pelajaran</li><li>✓ Sertifikat</li><li>✓ Proyek dinilai mentor</li></ul><a href="#" class="b">Pilih Pro</a></article>
</section>''',
    css=BASE + '''.harga { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; padding: 16px; }
.paket { display: flex; flex-direction: column; padding: 24px; border: 1px solid #D5D9E0; border-radius: 16px; }
.paket h3 { margin: 0; }
.h { font-size: 28px; font-weight: 700; margin: 8px 0 16px; }
.h small { font-size: 14px; font-weight: 400; color: #52606D; }
.paket ul { list-style: none; padding: 0; margin: 0 0 24px; display: grid; gap: 8px; }
.b { margin-top: auto; text-align: center; padding: 12px; border-radius: 12px; border: 1px solid #1D5FA8; color: #1D5FA8; text-decoration: none; font-weight: 600; }''',
    task={'q': 'Tonjolkan paket Pro: <code>.pro</code> diberi <code>border: 2px solid #1D5FA8</code>, dan tombolnya (<code>.pro .b</code>) berlatar <code>#1D5FA8</code> dengan teks putih.',
          'test': f"parseFloat({G.format('.pro')}.borderTopWidth)>=2&&{G.format('.pro .b')}.backgroundColor==='rgb(29, 95, 168)'",
          'hint': '.pro { border: 2px solid #1D5FA8 } .pro .b { background: #1D5FA8; color: #fff }'},
    pts=['Satu paket unggulan: border, lencana, tombol primary.', 'Format harga Rp49.000.', 'Tombol sejajar bawah: flex column + margin-top: auto.'],
    qs=[q('Cara membuat tombol semua kartu sejajar di bawah?', ['Kartu flex column, tombol margin-top: auto', 'Tinggi kartu tetap 500px', 'position: absolute'], 0, 'Ruang kosong dipakai margin auto.')],
    cek={'css': '.pro{border:2px solid #1D5FA8}.pro .b{background:#1D5FA8;color:#fff}'}),
  L('Footer dan form newsletter',
    ['Footer berisi kelompok link (Produk, Perusahaan, Bantuan), media sosial, form newsletter, dan hak cipta. Di desktop kelompok link berdampingan; di mobile bertumpuk atau dilipat.',
     'Form newsletter di desain sering hanya menampilkan input dengan placeholder "Email kamu" dan tombol. Input tetap butuh <b>label</b>; jika desain tidak menampilkannya, sembunyikan secara visual dengan kelas <code>.sr-only</code> tetapi tetap terbaca pembaca layar. Pakai <code>type="email"</code> dan <code>autocomplete="email"</code> agar keyboard ponsel menampilkan tombol @.',
     'Ikon media sosial yang hanya berupa ikon wajib punya <code>aria-label</code> ("Instagram Ruang Kode").',
     'Form newsletter di pratinjau belum punya label dan tipe input yang tepat.'],
    html='''<footer class="kaki">
  <form class="news">
    <input id="surel" placeholder="Email kamu">
    <button>Langganan</button>
  </form>
  <p>© 2026 RuangKode</p>
</footer>''',
    css=BASE + '''.kaki { padding: 32px 16px; background: #0F172A; color: #CBD5E1; }
.news { display: flex; gap: 8px; flex-wrap: wrap; max-width: 420px; }
.news input { flex: 1; min-width: 200px; padding: 12px; border-radius: 10px; border: 1px solid #475569; background: #1E293B; color: #fff; font-size: 16px; }
.news button { padding: 12px 20px; border: 0; border-radius: 10px; background: #F59E0B; color: #1F2933; font-weight: 600; }
.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }''',
    task={'q': 'Tambahkan <code>&lt;label class="sr-only" for="surel"&gt;Email&lt;/label&gt;</code>, lalu beri input <code>type="email"</code> dan <code>autocomplete="email"</code>.',
          'test': "!!document.querySelector('label[for=\"surel\"]')&&document.getElementById('surel').type==='email'&&document.getElementById('surel').autocomplete==='email'",
          'hint': '<label class="sr-only" for="surel">Email</label><input id="surel" type="email" autocomplete="email" placeholder="Email kamu">'},
    pts=['Label tetap ada; sembunyikan secara visual dengan .sr-only.', 'type="email" dan autocomplete="email".', 'Ikon sosial butuh aria-label.'],
    qs=[q('Desain tidak menampilkan label input. Solusi yang benar?', ['Hapus label', 'Label dengan kelas sr-only', 'Pakai placeholder saja'], 1, 'Tetap terbaca pembaca layar.')],
    cek={'html': '<form class="news"><label class="sr-only" for="surel">Email</label><input id="surel" type="email" autocomplete="email"></form>'}),
]),
M('Responsif dan pixel-perfect', 'Menengah',
  'Mobile-first dengan breakpoint dari desain, gambar responsif dengan srcset, membandingkan hasil dengan desain, dan aksesibilitas hasil slicing.',
  ['Mobile-first', 'srcset', 'Pixel-perfect', 'Accessibility'], [
  L('Mobile-first dan breakpoint dari desain',
    ['Desainer biasanya memberi dua atau tiga frame: mobile (360 atau 390), tablet (768), dan desktop (1440). <b>Mobile-first</b> berarti CSS dasar ditulis untuk mobile, lalu ditambah dengan <code>@media (min-width: ...)</code> untuk layar yang lebih lebar. Kodenya lebih ringkas daripada sebaliknya.',
     'Breakpoint diambil dari titik desain <b>berubah</b>, bukan dari nama perangkat. Jika frame tablet menunjukkan kartu menjadi 2 kolom, tulis <code>@media (min-width: 768px)</code>. Di antara dua frame, bayangkan sendiri perilakunya: apa yang melar, apa yang dibatasi lebar maksimumnya.',
     'Uji di DevTools (Ctrl + Shift + M) dengan menyeret lebar layar pelan-pelan dari 320 sampai 1600 px. Bagian yang rusak di lebar "tanggung" seperti 900 px sering terlewat jika hanya mengecek tiga ukuran frame.',
     'Daftar kelas di pratinjau satu kolom. Buat 2 kolom mulai lebar 600px.'],
    html='''<ul class="daftar">
  <li>HTML</li><li>CSS</li><li>JavaScript</li><li>Figma</li>
</ul>''',
    css=BASE + '''.daftar { list-style: none; margin: 0; padding: 16px; display: grid; gap: 12px; }
.daftar li { padding: 16px; border-radius: 12px; background: #F0FDFA; font-weight: 600; }
/* tulis media query di bawah */''',
    task={'q': 'Tambahkan <code>@media (min-width: 600px) { .daftar { grid-template-columns: 1fr 1fr; } }</code>.',
          'test': f"{RULES}.some(r=>r.media&&/min-width/.test(r.media.mediaText)&&[...r.cssRules].some(x=>x.selectorText==='.daftar'&&x.style.gridTemplateColumns))",
          'hint': '@media (min-width: 600px) { .daftar { grid-template-columns: 1fr 1fr } }'},
    pts=['CSS dasar untuk mobile, tambah dengan min-width.', 'Breakpoint dari titik desain berubah.', 'Seret lebar layar pelan-pelan, jangan hanya 3 ukuran.'],
    qs=[q('Mobile-first memakai media query?', ['min-width', 'max-width'], 0, 'Aturan ditambahkan saat layar melebar.')],
    cek={'css': '@media (min-width:600px){.daftar{grid-template-columns:1fr 1fr}}'}),
  L('Gambar responsif dengan srcset',
    ['Satu gambar besar untuk semua layar membuang kuota pengguna ponsel. Atribut <code>srcset</code> memberi browser beberapa pilihan file, dan <code>sizes</code> memberi tahu lebar tampil gambar. Browser lalu memilih file terkecil yang tetap tajam untuk layar itu.',
     'Contoh: <code>srcset="kopi-480.webp 480w, kopi-960.webp 960w, kopi-1440.webp 1440w"</code> dan <code>sizes="(min-width: 768px) 50vw, 100vw"</code>. Artinya: di layar lebar gambar tampil selebar setengah layar, di ponsel selebar penuh.',
     'Jika desain meminta <b>potongan berbeda</b> (art direction), misalnya foto lebar di desktop tetapi potongan persegi di mobile, pakai <code>&lt;picture&gt;</code> dengan beberapa <code>&lt;source media="..."&gt;</code>.',
     'Gambar di pratinjau hanya punya satu file.'],
    html='''<img class="foto" src="kopi-960.webp" alt="Barista menyeduh kopi" width="960" height="640">''',
    css=BASE + '''.foto { display: block; max-width: 100%; height: auto; background: #D7B899; }''',
    task={'q': 'Tambahkan <code>srcset</code> dengan tiga ukuran (480w, 960w, 1440w) dan <code>sizes="(min-width: 768px) 50vw, 100vw"</code>.',
          'test': "(i=>(i.getAttribute('srcset')||'').split(',').length>=3&&/\\d+w/.test(i.getAttribute('srcset'))&&!!i.getAttribute('sizes'))(document.querySelector('.foto'))",
          'hint': 'srcset="kopi-480.webp 480w, kopi-960.webp 960w, kopi-1440.webp 1440w" sizes="(min-width: 768px) 50vw, 100vw"'},
    pts=['srcset: daftar file dengan lebar aslinya (w).', 'sizes: lebar tampil gambar di setiap kondisi.', 'picture + source untuk potongan berbeda.'],
    qs=[q('Apa arti 960w di srcset?', ['Lebar asli file 960 piksel', 'Tampilkan 960 piksel', 'Lebar layar 960'], 0, 'Browser memakai info ini untuk memilih.')],
    cek={'html': '<img class="foto" alt="x" srcset="a.webp 480w, b.webp 960w, c.webp 1440w" sizes="(min-width: 768px) 50vw, 100vw">'}),
  C('Pixel-perfect: membandingkan dengan desain',
    ['<b>Pixel-perfect</b> berarti hasil slicing sesuai desain sampai detail: jarak, ukuran huruf, warna, radius, bayangan. Ini bukan soal obsesi 1 piksel, melainkan menghormati keputusan desainer dan menjaga konsistensi produk.',
     'Cara membandingkan: (1) ekspor frame desain sebagai PNG pada lebar yang sama; (2) buka hasilmu di DevTools device mode dengan lebar yang sama; (3) pakai ekstensi overlay seperti <b>PerfectPixel</b> untuk menumpuk gambar desain semi-transparan di atas halaman; (4) atau letakkan tangkapan layar berdampingan dan periksa per section.',
     'Prioritaskan perbedaan berdasarkan dampak: <b>tinggi</b> (warna salah, font salah, elemen hilang, layout rusak di ukuran tertentu), <b>sedang</b> (jarak antar section, ukuran ikon), <b>rendah</b> (selisih 1 sampai 2 px yang disebabkan perbedaan render font antar sistem operasi). Diskusikan dengan desainer perbedaan yang memang tidak bisa dihindari.'],
    tb=[{'c': 'Daftar periksa visual per section', 'h': ['Periksa', 'Cara'], 'r': [
      ['Font dan ketebalan', 'DevTools → Computed → font-family, font-weight'], ['Ukuran dan line-height', 'Bandingkan dengan panel Figma'],
      ['Warna', 'Eyedropper DevTools vs nilai variabel Figma'], ['Jarak antar elemen', 'Hover di DevTools menampilkan margin dan padding'],
      ['Radius dan bayangan', 'Bandingkan dengan overlay'], ['Lebar maksimum konten', 'Cek di 1440 dan 1920 px'],
      ['Teks panjang', 'Ganti teks dengan kalimat 2× lebih panjang'], ['State', 'Hover, focus, disabled sesuai desain']]}],
    pts=['Pixel-perfect: jarak, huruf, warna, radius, bayangan sesuai desain.', 'Bandingkan di lebar yang sama dengan overlay.', 'Prioritaskan berdasarkan dampak.'],
    qs=[q('Perbedaan mana yang paling penting diperbaiki dulu?', ['Selisih 1 px karena render font', 'Warna tombol utama salah', 'Bayangan sedikit lebih tipis'], 1, 'Dampaknya paling terlihat dan merusak konsistensi merek.')]),
  L('Aksesibilitas hasil slicing',
    ['Desain jarang menunjukkan hal yang tidak terlihat, padahal itu tanggung jawab slicer: <b>urutan fokus</b> keyboard yang logis, <b>indikator fokus</b> yang jelas, <b>alt</b> gambar, <b>label</b> form, <b>bahasa</b> halaman (<code>&lt;html lang="id"&gt;</code>), dan <b>skip link</b>.',
     '<b>Skip link</b> adalah tautan pertama di halaman, tersembunyi sampai difokuskan dengan Tab, yang langsung melompat ke konten utama. Pengguna keyboard tidak perlu melewati 15 link navbar di setiap halaman.',
     'Uji cepat setelah slicing: tekan Tab dari atas sampai bawah tanpa mouse; jalankan Lighthouse (tab Lighthouse di DevTools, kategori Accessibility); zoom browser 200% dan pastikan tidak ada teks terpotong atau scroll horizontal.',
     'Halaman di pratinjau belum punya skip link.'],
    html='''<header class="nav"><a href="#">Beranda</a><a href="#">Kelas</a><a href="#">Harga</a><a href="#">Blog</a><a href="#">Masuk</a></header>
<main><h1>Kelas Slicing Website</h1><p>Konten utama halaman.</p></main>''',
    css=BASE + '''.nav { display: flex; gap: 12px; flex-wrap: wrap; padding: 12px 16px; border-bottom: 1px solid #E4E7EB; }
main { padding: 24px 16px; }
.skip { position: absolute; left: 8px; top: -48px; background: #1F2933; color: #fff; padding: 8px 12px; border-radius: 8px; }
.skip:focus { top: 8px; }''',
    task={'q': 'Tambahkan <code>&lt;a class="skip" href="#isi"&gt;Lewati ke konten&lt;/a&gt;</code> sebagai elemen pertama, dan beri <code>main</code> <code>id="isi"</code>.',
          'test': "(a=>!!a&&a.classList.contains('skip')&&a.getAttribute('href')==='#isi')(document.body.querySelector('a'))&&!!document.querySelector('main#isi')",
          'hint': '<a class="skip" href="#isi">Lewati ke konten</a> di paling atas, lalu <main id="isi">'},
    pts=['Slicer bertanggung jawab atas fokus, alt, label, lang, skip link.', 'Skip link melompati navigasi.', 'Uji: Tab, Lighthouse, zoom 200%.'],
    qs=[q('Siapa yang paling diuntungkan skip link?', ['Pengguna keyboard dan pembaca layar', 'Mesin pencari', 'Desainer'], 0, 'Tidak perlu melewati navigasi berulang.')],
    cek={'html': '<a class="skip" href="#isi">Lewati</a><main id="isi">x</main>'}),
]),
M('Proyek dan serah terima', 'Menengah',
  'Proyek landing page lengkap, deploy hasil slicing, dan daftar periksa QA sebelum diserahkan ke klien.',
  ['Project', 'Deploy', 'QA'], [
  L('Proyek: landing page kedai kopi',
    ['Saatnya menggabungkan semua: navbar sticky, hero, fitur, harga, dan footer dalam satu halaman. Kerangka di pratinjau sudah memakai token, HTML semantik, dan grid fluid. Lengkapi bagian yang belum sesuai desain.',
     'Spesifikasi desain: navbar menempel di atas saat menggulir, hero dua kolom mulai 768 px, kartu menu memakai grid auto-fill minimal 180 px, dan semua warna dari token.',
     'Setelah tantangan selesai, salin kode ke VS Code, buka dengan Live Server, lalu uji di ponselmu lewat jaringan Wi-Fi yang sama. Langkah berikutnya: deploy, dibahas di pelajaran selanjutnya.'],
    html='''<header class="nav"><a class="logo" href="#">Kopi<b>Nusa</b></a><a class="btn" href="#menu">Pesan</a></header>
<main>
  <section class="hero"><div><h1>Kopi lokal, diseduh hari ini</h1><p>Gayo, Toraja, Kintamani. Diantar 30 menit.</p><a class="btn" href="#menu">Lihat menu</a></div><div class="foto" role="img" aria-label="Kopi"></div></section>
  <section id="menu" class="menu"><h2>Menu favorit</h2>
    <div class="grid"><article class="kartu"><h3>Kopi Susu Aren</h3><p>Rp22.000</p></article><article class="kartu"><h3>Americano</h3><p>Rp18.000</p></article><article class="kartu"><h3>Kopi Tubruk</h3><p>Rp15.000</p></article></div>
  </section>
</main>
<footer class="kaki">© 2026 KopiNusa</footer>''',
    css=''':root { --brand: #6D4C41; --brand-soft: #FFF8EE; --ink: #3E2723; --radius: 16px; --space: 16px; }
body { font-family: system-ui, sans-serif; margin: 0; color: var(--ink); }
.nav { display: flex; justify-content: space-between; align-items: center; padding: 12px var(--space); background: #fff; border-bottom: 1px solid #E7E0D8; }
.logo { color: var(--ink); text-decoration: none; font-size: 20px; }
.btn { display: inline-block; background: var(--brand); color: #fff; padding: 10px 18px; border-radius: 999px; text-decoration: none; font-weight: 600; }
.hero { display: grid; gap: 24px; padding: 32px var(--space); background: var(--brand-soft); }
@media (min-width: 768px) { .hero { grid-template-columns: 1fr 1fr; align-items: center; } }
.hero h1 { font-size: clamp(1.75rem, 1rem + 3vw, 3rem); margin: 0 0 12px; }
.foto { aspect-ratio: 4 / 3; border-radius: 24px; background: radial-gradient(circle at 40% 40%, #D7B899, var(--brand)); }
.menu { padding: 32px var(--space); }
.kartu { padding: var(--space); border-radius: var(--radius); background: #F5F0EB; }
.kartu h3 { margin: 0 0 4px; font-size: 16px; }
.kartu p { margin: 0; font-weight: 600; color: var(--brand); }
.kaki { padding: 24px var(--space); background: var(--ink); color: #EFE6DD; }''',
    task={'q': 'Selesaikan dua hal: navbar <code>.nav</code> menempel (<code>position: sticky; top: 0; z-index: 10</code>), dan <code>.grid</code> menjadi grid fluid <code>repeat(auto-fill, minmax(180px, 1fr))</code> dengan gap 16px.',
          'test': f"{G.format('.nav')}.position==='sticky'&&{G.format('.grid')}.display==='grid'&&{RULES}.some(r=>r.selectorText==='.grid'&&/auto-(fill|fit)/.test(r.style.gridTemplateColumns))",
          'hint': '.nav { position: sticky; top: 0; z-index: 10 } .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 16px }'},
    pts=['Gabungkan token, HTML semantik, flex, dan grid.', 'Uji di ponsel lewat Live Server.', 'Selesaikan spesifikasi sebelum menambah hiasan.'],
    qs=[q('Kenapa navbar sticky butuh z-index?', ['Agar konten yang digulir tidak tampil di atasnya', 'Agar lebih cepat', 'Agar berwarna'], 0, 'Navbar tetap di lapisan atas.')],
    cek={'css': '.nav{position:sticky;top:0;z-index:10}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:16px}'}),
  C('Deploy hasil slicing',
    ['Klien ingin melihat hasilnya di internet, bukan file zip. Tiga cara gratis yang paling umum: <b>GitHub Pages</b> (push ke repositori, aktifkan Pages di Settings), <b>Netlify</b> (seret folder ke app.netlify.com/drop), dan <b>Vercel</b> (hubungkan repositori GitHub, setiap push otomatis di-deploy dan setiap branch dapat URL pratinjau).',
     'Sebelum deploy: pastikan file utama bernama <code>index.html</code>, semua path relatif (<code>./css/style.css</code>, bukan <code>C:\\Users\\...</code>), nama file huruf kecil tanpa spasi (server Linux membedakan <code>Logo.png</code> dan <code>logo.png</code>), dan gambar sudah dikompres.',
     'Setelah deploy, kirim link ke klien dan uji sendiri di ponsel dengan data seluler (bukan Wi-Fi kantor) untuk merasakan kecepatan aslinya. Jalankan PageSpeed Insights (pagespeed.web.dev) dan catat skornya.'],
    code='# GitHub Pages lewat terminal\ngit init\ngit add .\ngit commit -m "Slicing landing page KopiNusa"\ngit branch -M main\ngit remote add origin https://github.com/namakamu/kopinusa.git\ngit push -u origin main\n# Lalu: Settings → Pages → Branch: main → Save\n# Situs tersedia di https://namakamu.github.io/kopinusa/', lang='bash',
    tb=[{'c': 'Pilihan hosting gratis', 'h': ['Layanan', 'Cara', 'Kelebihan'], 'r': [['GitHub Pages', 'Push ke repo, aktifkan Pages', 'Sekalian portofolio di GitHub'], ['Netlify Drop', 'Seret folder ke browser', 'Paling cepat, tanpa Git'], ['Vercel', 'Hubungkan repo GitHub', 'URL pratinjau setiap branch']]}],
    pts=['GitHub Pages, Netlify, Vercel.', 'index.html, path relatif, nama file huruf kecil.', 'Uji dengan data seluler dan PageSpeed Insights.'],
    qs=[q('Gambar tampil di laptop tapi rusak setelah deploy. Penyebab paling umum?', ['Beda huruf besar-kecil nama file atau path absolut', 'Internet lambat', 'Browser lama'], 0, 'Server Linux peka huruf besar-kecil.')]),
  C('Daftar periksa QA sebelum serah terima',
    ['Sebelum menyerahkan hasil slicing, jalankan daftar periksa ini. Klien dan desainer akan menemukan masalah yang sama jika kamu melewatkannya, dan kesan pertama sulit diulang.',
     'Kelompokkan pemeriksaan menjadi: <b>visual</b> (sesuai desain di 360, 768, 1440 px), <b>fungsi</b> (semua link dan tombol bekerja, form tervalidasi), <b>aksesibilitas</b> (Tab, alt, label, kontras), <b>performa</b> (gambar terkompres, skor Lighthouse), <b>kompatibilitas</b> (Chrome, Safari iOS, Firefox, Samsung Internet), dan <b>SEO dasar</b> (title, meta description, Open Graph).',
     'Tulis laporan singkat saat serah terima: link deploy, browser yang sudah diuji, skor Lighthouse, dan daftar perbedaan dengan desain yang disengaja beserta alasannya. Laporan ini membuatmu terlihat profesional dan mencegah perdebatan di kemudian hari.'],
    tb=[{'c': 'Daftar periksa serah terima', 'h': ['Kelompok', 'Periksa'], 'r': [
      ['Visual', 'Sesuai desain di 360, 768, 1440 px; tidak ada scroll horizontal'], ['Fungsi', 'Semua link, tombol, menu mobile, dan form bekerja'],
      ['Aksesibilitas', 'Tab berurutan, fokus terlihat, alt, label, kontras 4,5:1'], ['Performa', 'Gambar WebP terkompres, Lighthouse Performance ≥ 90'],
      ['Kompatibilitas', 'Chrome, Safari iOS, Firefox, Samsung Internet'], ['SEO', 'title, meta description, Open Graph, favicon, lang="id"'],
      ['Konten', 'Tidak ada lorem ipsum, ejaan benar, format Rp dan tanggal benar'], ['Serah terima', 'Link deploy, repositori, laporan pengujian']]}],
    pts=['Visual, fungsi, aksesibilitas, performa, kompatibilitas, SEO.', 'Uji di Safari iOS dan Samsung Internet juga.', 'Serahkan laporan pengujian.'],
    qs=[q('Browser mana yang sering terlupa diuji padahal banyak dipakai di Indonesia?', ['Samsung Internet', 'Internet Explorer 6', 'Netscape'], 0, 'Bawaan banyak ponsel Samsung.')]),
]),
]

SLW_SO = {
'Apa itu slicing dan alurnya': [
  T('Ambil satu landing page yang kamu suka. Pecah menjadi section, lalu daftar komponen berulang dan token warna yang kamu temukan.', 'Tulis section dari atas ke bawah, lalu cari elemen yang sama bentuknya.',
    'Contoh:\nSection : navbar, hero, logo klien, fitur (6 kartu), testimoni, harga (3 paket), FAQ, footer\nKomponen: tombol (primary, secondary), kartu fitur, kartu harga, item FAQ\nToken   : brand #4F46E5, teks #111827, abu #6B7280, latar #F9FAFB, radius 12, spacing 8/16/24/48'),
],
'Membaca desain di Figma Dev Mode': [
  X('Dev Mode menampilkan: auto layout vertical, gap 12, padding 20/24, fill #F8FAFC, radius 16, stroke 1 #E2E8F0, shadow 0 2 8 #0F172A14. Tulis CSS-nya.', 'Terjemahkan satu per satu, warna alpha 14 hex ≈ 8%.',
    '.kartu {\n  display: flex;\n  flex-direction: column;\n  gap: 12px;\n  padding: 20px 24px;\n  background: #F8FAFC;\n  border: 1px solid #E2E8F0;\n  border-radius: 16px;\n  box-shadow: 0 2px 8px rgb(15 23 42 / .08);\n}'),
],
'Token desain ke CSS variables': [
  X('Ubah daftar variabel Figma berikut menjadi CSS: color/brand/500 #6366F1, color/text/primary #111827, spacing/2 8, spacing/4 16, radius/lg 16, font/body Inter.', 'Garis miring menjadi tanda hubung, angka spacing diberi px.',
    ':root {\n  --color-brand-500: #6366F1;\n  --color-text-primary: #111827;\n  --spacing-2: 8px;\n  --spacing-4: 16px;\n  --radius-lg: 16px;\n  --font-body: "Inter", system-ui, sans-serif;\n}'),
],
'HTML semantik dari desain': [
  H('Tulis kerangka HTML semantik untuk halaman blog: navbar, judul artikel, info penulis, isi, artikel terkait (3 kartu), footer.', 'header/nav, main/article, aside atau section, footer.',
    '<header><nav>...</nav></header>\n<main>\n  <article>\n    <h1>Judul artikel</h1>\n    <p class="meta">Oleh Rina · 5 menit baca</p>\n    <p>Isi...</p>\n  </article>\n  <section aria-labelledby="terkait">\n    <h2 id="terkait">Artikel terkait</h2>\n    <article><h3>...</h3></article>\n    <article><h3>...</h3></article>\n    <article><h3>...</h3></article>\n  </section>\n</main>\n<footer>...</footer>'),
],
'Navbar responsif': [
  H('Buat navbar dengan tombol menu mobile tanpa JavaScript memakai details dan summary.', 'summary menjadi tombol, isi details adalah daftar link.',
    '<header class="nav">\n  <a class="logo" href="/">KopiNusa</a>\n  <details class="menu-m">\n    <summary aria-label="Buka menu">☰</summary>\n    <nav><a href="#menu">Menu</a><a href="#lokasi">Lokasi</a><a href="#tentang">Tentang</a></nav>\n  </details>\n</header>'),
],
'Hero section': [
  X('Tulis CSS hero dua kolom mulai 900px, dengan gambar di atas teks pada mobile.', 'Mobile: order gambar -1. Desktop: grid 2 kolom dan order normal.',
    '.hero { display: grid; gap: 24px; }\n.hero .gambar { order: -1; }\n@media (min-width: 900px) {\n  .hero { grid-template-columns: 1.1fr 1fr; align-items: center; }\n  .hero .gambar { order: 0; }\n}'),
],
'Tombol dan kartu dari komponen Figma': [
  X('Tulis tombol primary dengan state hover, focus-visible, active, dan disabled.', 'Lima aturan untuk satu komponen.',
    '.btn-primary { background: #4F46E5; color: #fff; padding: 12px 20px; border: 0; border-radius: 12px; font-weight: 600; transition: background .15s; }\n.btn-primary:hover { background: #4338CA; }\n.btn-primary:focus-visible { outline: 3px solid #A5B4FC; outline-offset: 2px; }\n.btn-primary:active { transform: translateY(1px); }\n.btn-primary:disabled { background: #C7D2FE; cursor: not-allowed; }'),
],
'Ikon dan gambar yang dioptimalkan': [
  H('Tulis tag gambar hero yang dimuat paling awal, dan gambar galeri yang dimuat lambat.', 'Hero: fetchpriority high tanpa lazy. Galeri: loading lazy.',
    '<img src="hero.webp" alt="Barista menuang susu" width="1200" height="800" fetchpriority="high">\n<img src="galeri-1.webp" alt="Interior kedai" width="600" height="400" loading="lazy">'),
],
'Section fitur dengan grid': [
  X('Buat grid fitur yang tepat 3 kolom di desktop (≥ 1024px), 2 kolom di tablet, 1 kolom di ponsel, memakai media query.', 'Mobile-first dengan min-width.',
    '.grid { display: grid; gap: 24px; }\n@media (min-width: 640px) { .grid { grid-template-columns: repeat(2, 1fr); } }\n@media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, 1fr); } }'),
],
'Testimoni dengan scroll-snap': [
  X('Ubah carousel testimoni menjadi grid 3 kolom tanpa scroll di layar ≥ 1024px.', 'Di media query, ganti display dan matikan overflow.',
    '@media (min-width: 1024px) {\n  .testi { display: grid; grid-template-columns: repeat(3, 1fr); overflow: visible; }\n  .k { flex: none; }\n}'),
],
'Tabel harga dengan paket unggulan': [
  H('Tambahkan lencana "Paling populer" di kartu Pro dan fitur yang tidak termasuk di kartu Gratis dengan ikon dan teks.', 'Jangan hanya abu-abu; tulis "Tidak termasuk".',
    '<article class="paket pro">\n  <span class="lencana">Paling populer</span>\n  ...\n</article>\n<article class="paket">\n  <ul>\n    <li>✓ 50 pelajaran</li>\n    <li class="tidak">✕ Sertifikat <span class="sr-only">(tidak termasuk)</span></li>\n  </ul>\n</article>'),
],
'Footer dan form newsletter': [
  H('Tulis tautan ikon Instagram dan YouTube yang aksesibel.', 'aria-label pada tautan, aria-hidden pada ikon.',
    '<a href="https://instagram.com/ruangkode" aria-label="Instagram Ruang Kode"><svg aria-hidden="true" width="24" height="24">...</svg></a>\n<a href="https://youtube.com/@ruangkode" aria-label="YouTube Ruang Kode"><svg aria-hidden="true" width="24" height="24">...</svg></a>'),
],
'Mobile-first dan breakpoint dari desain': [
  T('Desain punya frame 390 (1 kolom kartu), 834 (2 kolom), 1440 (4 kolom, lebar konten maks 1200). Tulis rencana breakpoint dan CSS-nya.', 'Breakpoint dari titik perubahan; container maks 1200.',
    '.wrap { max-width: 1200px; margin: 0 auto; padding: 0 16px; }\n.grid { display: grid; gap: 16px; }\n@media (min-width: 768px)  { .grid { grid-template-columns: repeat(2, 1fr); } }\n@media (min-width: 1200px) { .grid { grid-template-columns: repeat(4, 1fr); } }'),
],
'Gambar responsif dengan srcset': [
  H('Tulis elemen picture: desktop memakai foto lebar 16:9, ponsel memakai potongan persegi.', 'source dengan media min-width untuk desktop, img sebagai cadangan.',
    '<picture>\n  <source media="(min-width: 768px)" srcset="hero-lebar-1280.webp 1280w, hero-lebar-1920.webp 1920w" sizes="100vw">\n  <img src="hero-persegi-720.webp" srcset="hero-persegi-480.webp 480w, hero-persegi-720.webp 720w" sizes="100vw" alt="Kedai KopiNusa" width="720" height="720">\n</picture>'),
],
'Pixel-perfect: membandingkan dengan desain': [
  T('Kamu menemukan 5 perbedaan: (a) tombol radius 8 seharusnya 12, (b) font fallback tampil karena salah nama, (c) jarak section 64 seharusnya 80, (d) teks 1 px lebih tinggi di Windows, (e) menu mobile tidak muncul. Urutkan prioritasnya.', 'Dampak terbesar dulu.',
    '1. (e) menu mobile tidak muncul (fungsi rusak)\n2. (b) font salah (merusak tampilan seluruh halaman)\n3. (c) jarak section\n4. (a) radius tombol\n5. (d) selisih render font antar OS: catat, umumnya diterima'),
],
'Aksesibilitas hasil slicing': [
  T('Tulis 5 langkah uji aksesibilitas cepat yang bisa kamu lakukan dalam 10 menit setelah slicing.', 'Keyboard, Lighthouse, zoom, alt, kontras.',
    '1. Tekan Tab dari atas ke bawah: urutan logis dan fokus terlihat.\n2. Lighthouse → Accessibility, perbaiki semua temuan merah.\n3. Zoom 200%: tidak ada teks terpotong atau scroll horizontal.\n4. Matikan gambar atau baca alt di DevTools: alt bermakna.\n5. Cek kontras teks abu-abu dengan DevTools color picker.'),
],
'Proyek: landing page kedai kopi': [
  X('Tambahkan section FAQ ke proyek memakai details/summary, dengan gaya yang memakai token proyek.', 'details untuk setiap pertanyaan, summary sebagai pertanyaan.',
    '.faq details { border-bottom: 1px solid #E7E0D8; padding: var(--space) 0; }\n.faq summary { cursor: pointer; font-weight: 600; color: var(--ink); }\n.faq summary::marker { color: var(--brand); }\n.faq p { margin: 8px 0 0; }'),
],
'Deploy hasil slicing': [
  T('Hasil deploy GitHub Pages tampil tanpa CSS. Path di HTML: <code>/css/style.css</code>, situs di <code>namakamu.github.io/kopinusa/</code>. Apa penyebab dan perbaikannya?', 'Garis miring di awal merujuk ke akar domain, bukan folder proyek.',
    'Penyebab: /css/style.css dicari di namakamu.github.io/css/style.css (akar domain),\nbukan di /kopinusa/css/style.css.\nPerbaikan: pakai path relatif css/style.css atau ./css/style.css.'),
],
'Daftar periksa QA sebelum serah terima': [
  T('Tulis laporan serah terima singkat untuk proyek KopiNusa.', 'Link, browser yang diuji, skor, perbedaan yang disengaja.',
    'Proyek  : Landing page KopiNusa\nLink    : https://kopinusa.vercel.app\nRepo    : github.com/namakamu/kopinusa\nDiuji di: Chrome 131, Safari iOS 18, Firefox 133, Samsung Internet 27; lebar 360, 768, 1440\nLighthouse: Performance 96, Accessibility 100, Best Practices 100, SEO 100\nPerbedaan disengaja: bayangan kartu dibuat lebih tipis di dark mode agar kontras tetap 4,5:1 (disetujui desainer 12/11).'),
],
}

SLM = [
M('Persiapan slicing mobile', 'Pemula',
  'Membaca desain mobile (frame, dp dan pt, safe area), mengekspor aset dan ikon untuk Flutter dan Android, serta memindahkan token ke ThemeData dan MaterialTheme.',
  ['Mobile frames', 'Assets', 'Theme'], [
  C('Membaca desain mobile',
    ['Desain mobile di Figma biasanya memakai frame <b>360 × 800</b> (Android) atau <b>390 × 844</b> / <b>393 × 852</b> (iPhone). Satuan di Figma adalah piksel logis, yang sama dengan <b>dp</b> di Android (dan Flutter) dan <b>pt</b> di iOS. Jadi padding 16 di Figma menjadi <code>16.dp</code> di Compose dan <code>16</code> di Flutter, tanpa konversi.',
     'Perhatikan area yang tidak boleh diisi konten penting: <b>status bar</b> di atas, <b>notch</b> atau kamera, dan <b>gesture bar</b> di bawah. Di Flutter, bungkus layar dengan <code>SafeArea</code>; di Compose, pakai <code>Scaffold</code> dan parameter <code>innerPadding</code> atau <code>Modifier.windowInsetsPadding</code>. Sejak Android 15, aplikasi tampil <b>edge-to-edge</b> secara bawaan, jadi inset wajib ditangani.',
     'Ukuran target sentuh minimal <b>48 × 48 dp</b> di Android dan <b>44 × 44 pt</b> di iOS, walau ikonnya hanya 24. Jika desain menunjukkan ikon tanpa area sentuh, tanyakan ke desainer atau perbesar area sentuhnya tanpa mengubah tampilan.'],
    tb=[{'c': 'Figma ke Flutter dan Compose', 'h': ['Figma', 'Flutter', 'Jetpack Compose'], 'r': [
      ['16 (px logis)', '16 (logical pixel)', '16.dp'], ['Text 16', 'fontSize: 16', '16.sp'], ['Frame 360 × 800', 'MediaQuery.sizeOf(context)', 'LocalConfiguration / WindowSizeClass'],
      ['Safe area', 'SafeArea(child: ...)', 'Scaffold innerPadding, WindowInsets'], ['Target sentuh 48', 'minimumSize: Size(48, 48)', 'Modifier.minimumInteractiveComponentSize()']]}],
    pts=['Piksel Figma = dp (Android, Flutter) = pt (iOS).', 'Hormati status bar, notch, gesture bar: SafeArea dan insets.', 'Target sentuh 48 dp / 44 pt.'],
    qs=[q('Padding 24 di Figma menjadi apa di Compose?', ['24.dp', '48.dp', '24.px'], 0, 'Satu banding satu.'),
        q('Ukuran huruf di Compose memakai satuan?', ['dp', 'sp', 'pt'], 1, 'sp mengikuti pengaturan ukuran huruf pengguna.')]),
  C('Ekspor aset dan ikon',
    ['<b>Ikon</b>: ekspor sebagai SVG. Di Flutter, pakai paket <code>flutter_svg</code>, atau ubah ikon menjadi font ikon. Di Android, impor SVG lewat <b>Resource Manager → Vector Asset</b> sehingga menjadi file XML di <code>res/drawable</code>. Jika ikon ada di Material Symbols, langsung pakai <code>Icons.Outlined.ShoppingCart</code> tanpa ekspor.',
     '<b>Gambar bitmap</b>: Flutter memakai folder resolusi <code>assets/images/</code>, <code>assets/images/2.0x/</code>, <code>assets/images/3.0x/</code> dengan nama file yang sama; Flutter memilih otomatis. Android memakai <code>drawable-mdpi</code>, <code>-hdpi</code>, <code>-xhdpi</code>, <code>-xxhdpi</code>, <code>-xxxhdpi</code> (1×, 1,5×, 2×, 3×, 4×), atau cukup WebP satu ukuran besar di <code>drawable-nodpi</code> untuk ilustrasi.',
     'Nama aset: huruf kecil, garis bawah, tanpa spasi (<code>ic_cart.xml</code>, <code>img_onboarding_1.webp</code>). Android menolak nama dengan huruf besar atau tanda hubung.'],
    code='# pubspec.yaml (Flutter)\ndependencies:\n  flutter_svg: ^2.0.10\n\nflutter:\n  assets:\n    - assets/icons/\n    - assets/images/\n\n# Struktur folder\nassets/\n  icons/ic_cart.svg\n  images/img_hero.png\n  images/2.0x/img_hero.png\n  images/3.0x/img_hero.png', lang='yaml',
    pts=['Ikon SVG: flutter_svg atau Vector Asset Android.', 'Bitmap: folder 2.0x 3.0x (Flutter) atau drawable-xxhdpi (Android).', 'Nama aset huruf kecil dan garis bawah.'],
    qs=[q('Nama file mana yang ditolak Android?', ['ic_cart.xml', 'Ic-Cart.xml', 'img_hero.webp'], 1, 'Huruf besar dan tanda hubung tidak boleh.'),
        q('Di Flutter, gambar 3× disimpan di?', ['assets/images/3.0x/', 'assets/images@3x/', 'res/drawable-xxhdpi/'], 0, 'Folder resolusi dengan nama file yang sama.')]),
  C('Token desain ke ThemeData dan MaterialTheme',
    ['Sama seperti di web, langkah pertama slicing mobile adalah memindahkan token. Di Flutter, warna masuk ke <code>ColorScheme</code> dan gaya teks ke <code>TextTheme</code> di dalam <code>ThemeData</code>. Di Compose, warna masuk ke <code>lightColorScheme()</code> atau <code>darkColorScheme()</code> dan teks ke <code>Typography</code> di dalam <code>MaterialTheme</code>.',
     'Setelah itu, widget mengambil warna dari tema, bukan kode hex: <code>Theme.of(context).colorScheme.primary</code> di Flutter, <code>MaterialTheme.colorScheme.primary</code> di Compose. Dark mode cukup menyediakan skema kedua.',
     'Jika desainer memakai Material Theme Builder di Figma, kamu bisa langsung mengekspor kode tema untuk Flutter dan Compose dari plugin itu.'],
    code='''// Flutter
final tema = ThemeData(
  useMaterial3: true,
  colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF6D4C41)),
  textTheme: const TextTheme(
    headlineSmall: TextStyle(fontSize: 24, fontWeight: FontWeight.w600, height: 32 / 24),
    bodyLarge: TextStyle(fontSize: 16, height: 24 / 16),
    labelLarge: TextStyle(fontSize: 14, fontWeight: FontWeight.w500, letterSpacing: 0.1),
  ),
);

// Pemakaian
Text('Menu favorit', style: Theme.of(context).textTheme.headlineSmall);
Container(color: Theme.of(context).colorScheme.primaryContainer);''', lang='dart',
    tb=[{'c': 'Token ke tema', 'h': ['Token', 'Flutter', 'Compose'], 'r': [
      ['color/primary', 'colorScheme.primary', 'MaterialTheme.colorScheme.primary'], ['color/surface', 'colorScheme.surface', 'MaterialTheme.colorScheme.surface'],
      ['Title/Medium', 'textTheme.titleMedium', 'MaterialTheme.typography.titleMedium'], ['radius/md 12', 'BorderRadius.circular(12)', 'RoundedCornerShape(12.dp)'], ['spacing/4 16', 'EdgeInsets.all(16)', 'Modifier.padding(16.dp)']]}],
    pts=['Warna ke ColorScheme, teks ke TextTheme / Typography.', 'Widget mengambil dari tema, bukan hex.', 'Material Theme Builder bisa mengekspor kode tema.'],
    qs=[q('Di Compose, warna utama tema diambil dengan?', ['MaterialTheme.colorScheme.primary', 'Color.Primary', 'R.color.primary'], 0, 'Dari tema yang aktif.')]),
]),
M('Slicing layar login', 'Pemula',
  'Memetakan auto layout ke Row, Column, dan padding, lalu men-slicing layar login di Flutter dan Jetpack Compose.',
  ['Layout mapping', 'Flutter', 'Compose'], [
  C('Memetakan auto layout ke Row dan Column',
    ['Auto layout Figma diterjemahkan hampir satu banding satu. <b>Vertical</b> menjadi <code>Column</code>, <b>horizontal</b> menjadi <code>Row</code>, <b>gap</b> menjadi <code>SizedBox</code> atau <code>spacing</code> (Flutter 3.27+) dan <code>Arrangement.spacedBy()</code> di Compose, <b>padding</b> menjadi <code>Padding</code> atau <code>Modifier.padding</code>.',
     '<b>Fill container</b> menjadi <code>Expanded</code> (Flutter) atau <code>Modifier.weight(1f)</code> / <code>fillMaxWidth()</code> (Compose). <b>Hug contents</b> adalah perilaku bawaan. Elemen bertumpuk (gambar dengan lencana di pojok) menjadi <code>Stack</code> di Flutter dan <code>Box</code> di Compose.',
     'Daftar panjang yang bisa digulir jangan memakai Column biasa: pakai <code>ListView.builder</code> (Flutter) atau <code>LazyColumn</code> (Compose) agar hanya item yang terlihat yang dibuat.'],
    tb=[{'c': 'Auto layout ke widget', 'h': ['Figma', 'Flutter', 'Compose'], 'r': [
      ['Vertical, gap 16', 'Column(spacing: 16)', 'Column(verticalArrangement = Arrangement.spacedBy(16.dp))'], ['Horizontal, gap 8', 'Row(spacing: 8)', 'Row(horizontalArrangement = Arrangement.spacedBy(8.dp))'],
      ['Padding 24', 'Padding(padding: EdgeInsets.all(24))', 'Modifier.padding(24.dp)'], ['Fill container (sumbu utama)', 'Expanded(child: ...)', 'Modifier.weight(1f)'],
      ['Fill container (lebar)', 'SizedBox(width: double.infinity)', 'Modifier.fillMaxWidth()'], ['Align center', 'crossAxisAlignment: center', 'horizontalAlignment = Alignment.CenterHorizontally'],
      ['Elemen bertumpuk', 'Stack + Positioned', 'Box + Modifier.align()'], ['Daftar panjang', 'ListView.builder', 'LazyColumn']]}],
    pts=['Vertical = Column, horizontal = Row.', 'Fill = Expanded / weight; bertumpuk = Stack / Box.', 'Daftar panjang = ListView.builder / LazyColumn.'],
    qs=[q('Fill container di dalam Row Compose menjadi?', ['Modifier.weight(1f)', 'Modifier.wrapContentWidth()', 'Arrangement.End'], 0, 'Mengisi sisa ruang.'),
        q('Lencana di pojok kanan atas foto produk di Flutter memakai?', ['Row', 'Stack + Positioned', 'ListView'], 1, 'Elemen bertumpuk.')]),
  C('Layar login di Flutter',
    ['Desain login: logo, judul "Masuk", subjudul, field email, field kata sandi dengan tombol tampilkan, link "Lupa kata sandi" rata kanan, tombol Masuk lebar penuh, dan teks "Belum punya akun? Daftar" di bawah. Padding layar 24, gap antar field 16, tombol tinggi 52.',
     'Strukturnya: <code>Scaffold</code> → <code>SafeArea</code> → <code>SingleChildScrollView</code> (agar tidak tertutup keyboard) → <code>Padding</code> → <code>Column</code>. Warna dan teks diambil dari tema. Field memakai <code>TextFormField</code> dengan <code>InputDecoration</code> berlabel, bukan hanya hint.',
     'Perhatikan detail dari desain yang sering terlewat: <code>keyboardType: TextInputType.emailAddress</code>, <code>textInputAction: TextInputAction.next</code> agar tombol keyboard pindah ke field berikutnya, dan <code>autofillHints</code> agar pengelola sandi bisa mengisi otomatis.'],
    code='''class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  bool _sembunyi = true;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context);
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            spacing: 16,
            children: [
              const SizedBox(height: 32),
              Text('Masuk', style: t.textTheme.headlineMedium),
              Text('Lanjutkan belajarmu hari ini.', style: t.textTheme.bodyLarge),
              const TextField(
                keyboardType: TextInputType.emailAddress,
                textInputAction: TextInputAction.next,
                autofillHints: [AutofillHints.email],
                decoration: InputDecoration(labelText: 'Email', border: OutlineInputBorder()),
              ),
              TextField(
                obscureText: _sembunyi,
                autofillHints: const [AutofillHints.password],
                decoration: InputDecoration(
                  labelText: 'Kata sandi',
                  border: const OutlineInputBorder(),
                  suffixIcon: IconButton(
                    tooltip: _sembunyi ? 'Tampilkan sandi' : 'Sembunyikan sandi',
                    icon: Icon(_sembunyi ? Icons.visibility : Icons.visibility_off),
                    onPressed: () => setState(() => _sembunyi = !_sembunyi),
                  ),
                ),
              ),
              Align(
                alignment: Alignment.centerRight,
                child: TextButton(onPressed: () {}, child: const Text('Lupa kata sandi?')),
              ),
              FilledButton(
                style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(52)),
                onPressed: () {},
                child: const Text('Masuk'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}''', lang='dart',
    pts=['Scaffold → SafeArea → SingleChildScrollView → Column.', 'labelText, keyboardType, textInputAction, autofillHints.', 'Tombol lebar penuh: minimumSize Size.fromHeight(52).'],
    qs=[q('Kenapa layar login dibungkus SingleChildScrollView?', ['Agar tidak tertutup keyboard dan bisa digulir', 'Agar lebih cepat', 'Wajib di Flutter'], 0, 'Keyboard memakan separuh layar.'),
        q('Properti yang membuat tombol keyboard pindah ke field berikutnya?', ['textInputAction: TextInputAction.next', 'autofocus: true', 'maxLines: 2'], 0, 'Keyboard menampilkan tombol Next.')]),
  C('Layar login di Jetpack Compose',
    ['Desain yang sama di Compose: <code>Scaffold</code> memberi <code>innerPadding</code> untuk inset sistem, lalu <code>Column</code> dengan <code>verticalScroll</code>, <code>imePadding()</code> agar naik di atas keyboard, dan <code>Arrangement.spacedBy(16.dp)</code> untuk gap.',
     'State field disimpan dengan <code>rememberSaveable</code> agar tidak hilang saat layar diputar. <code>OutlinedTextField</code> sudah punya label mengambang sesuai Material 3. Opsi keyboard diatur lewat <code>KeyboardOptions</code>.',
     'Nilai ukuran diambil langsung dari Figma: padding 24.dp, tinggi tombol 52.dp, radius 12.dp. Warna dan gaya teks dari <code>MaterialTheme</code>.'],
    code='''@Composable
fun LoginScreen(onMasuk: (String, String) -> Unit) {
    var email by rememberSaveable { mutableStateOf("") }
    var sandi by rememberSaveable { mutableStateOf("") }
    var sembunyi by rememberSaveable { mutableStateOf(true) }

    Scaffold { innerPadding ->
        Column(
            modifier = Modifier
                .padding(innerPadding)
                .imePadding()
                .verticalScroll(rememberScrollState())
                .padding(24.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            Spacer(Modifier.height(32.dp))
            Text("Masuk", style = MaterialTheme.typography.headlineMedium)
            Text("Lanjutkan belajarmu hari ini.", style = MaterialTheme.typography.bodyLarge)
            OutlinedTextField(
                value = email, onValueChange = { email = it },
                label = { Text("Email") }, singleLine = true,
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Email, imeAction = ImeAction.Next),
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = sandi, onValueChange = { sandi = it },
                label = { Text("Kata sandi") }, singleLine = true,
                visualTransformation = if (sembunyi) PasswordVisualTransformation() else VisualTransformation.None,
                trailingIcon = {
                    IconButton(onClick = { sembunyi = !sembunyi }) {
                        Icon(
                            if (sembunyi) Icons.Filled.Visibility else Icons.Filled.VisibilityOff,
                            contentDescription = if (sembunyi) "Tampilkan sandi" else "Sembunyikan sandi"
                        )
                    }
                },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Password, imeAction = ImeAction.Done),
                modifier = Modifier.fillMaxWidth()
            )
            TextButton(onClick = {}, modifier = Modifier.align(Alignment.End)) { Text("Lupa kata sandi?") }
            Button(
                onClick = { onMasuk(email, sandi) },
                shape = RoundedCornerShape(12.dp),
                modifier = Modifier.fillMaxWidth().height(52.dp)
            ) { Text("Masuk") }
        }
    }
}''', lang='kotlin',
    pts=['Scaffold innerPadding + imePadding + verticalScroll.', 'rememberSaveable untuk state field.', 'contentDescription untuk ikon yang bisa ditekan.'],
    qs=[q('Modifier yang membuat konten naik di atas keyboard?', ['imePadding()', 'fillMaxSize()', 'clip()'], 0, 'IME = keyboard di layar.'),
        q('Kenapa memakai rememberSaveable, bukan remember?', ['Isi field tidak hilang saat layar diputar', 'Lebih cepat', 'Wajib untuk TextField'], 0, 'Bertahan saat konfigurasi berubah.')]),
]),
M('Slicing daftar, kartu, dan navigasi', 'Menengah',
  'Grid kartu produk di Flutter dan Compose, serta bottom navigation dan top app bar sesuai desain.',
  ['Grid', 'Cards', 'Navigation bar'], [
  C('Kartu produk dan grid di Flutter',
    ['Desain katalog: grid 2 kolom, gap 12, padding layar 16. Kartu berisi foto rasio 1:1 dengan radius 12, nama produk (maksimal 2 baris), harga tebal berwarna primary, dan tombol tambah kecil.',
     'Pakai <code>GridView.builder</code> dengan <code>SliverGridDelegateWithFixedCrossAxisCount</code> (jumlah kolom tetap) atau <code>SliverGridDelegateWithMaxCrossAxisExtent</code> (lebar maksimum kartu, jumlah kolom menyesuaikan layar, mirip auto-fill di CSS). Atur <code>childAspectRatio</code> agar tinggi kartu cukup untuk foto dan teks, atau pakai <code>mainAxisExtent</code> untuk tinggi tetap.',
     'Teks panjang dibatasi dengan <code>maxLines: 2</code> dan <code>overflow: TextOverflow.ellipsis</code>. Format harga Rupiah dengan paket <code>intl</code>: <code>NumberFormat.currency(locale: \'id\', symbol: \'Rp\', decimalDigits: 0)</code>.'],
    code='''final rupiah = NumberFormat.currency(locale: 'id', symbol: 'Rp', decimalDigits: 0);

GridView.builder(
  padding: const EdgeInsets.all(16),
  gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
    maxCrossAxisExtent: 200,
    mainAxisSpacing: 12,
    crossAxisSpacing: 12,
    mainAxisExtent: 260,
  ),
  itemCount: produk.length,
  itemBuilder: (context, i) {
    final p = produk[i];
    final t = Theme.of(context);
    return Card(
      clipBehavior: Clip.antiAlias,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AspectRatio(aspectRatio: 1, child: Image.asset(p.foto, fit: BoxFit.cover)),
          Padding(
            padding: const EdgeInsets.all(12),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              spacing: 4,
              children: [
                Text(p.nama, maxLines: 2, overflow: TextOverflow.ellipsis, style: t.textTheme.titleSmall),
                Text(rupiah.format(p.harga),
                    style: t.textTheme.titleMedium?.copyWith(color: t.colorScheme.primary, fontWeight: FontWeight.w700)),
              ],
            ),
          ),
        ],
      ),
    );
  },
)''', lang='dart', out='Kopi Susu Aren\nRp22.000',
    pts=['GridView.builder dengan MaxCrossAxisExtent mirip auto-fill.', 'AspectRatio 1 + BoxFit.cover untuk foto.', 'maxLines + ellipsis, format Rupiah dengan intl.'],
    qs=[q('Delegate yang menyesuaikan jumlah kolom dengan lebar layar?', ['SliverGridDelegateWithMaxCrossAxisExtent', 'SliverGridDelegateWithFixedCrossAxisCount'], 0, 'Menentukan lebar maksimum, bukan jumlah kolom.')]),
  C('Kartu produk dan LazyVerticalGrid di Compose',
    ['Di Compose, grid yang bisa digulir adalah <code>LazyVerticalGrid</code>. <code>GridCells.Fixed(2)</code> untuk dua kolom tetap, atau <code>GridCells.Adaptive(minSize = 160.dp)</code> untuk jumlah kolom yang menyesuaikan layar, persis seperti <code>auto-fill minmax(160px, 1fr)</code> di CSS.',
     'Kartu memakai <code>Card</code> Material 3. Foto dimuat dari internet dengan pustaka <b>Coil</b> (<code>AsyncImage</code>) dan dipotong dengan <code>ContentScale.Crop</code> serta <code>Modifier.aspectRatio(1f)</code>.',
     'Beri setiap item <code>key</code> yang stabil (misalnya id produk) agar Compose tidak menggambar ulang semua kartu saat daftar berubah.'],
    code='''@Composable
fun KatalogGrid(produk: List<Produk>, onTambah: (Produk) -> Unit) {
    val rupiah = remember { NumberFormat.getCurrencyInstance(Locale("id", "ID")).apply { maximumFractionDigits = 0 } }
    LazyVerticalGrid(
        columns = GridCells.Adaptive(minSize = 160.dp),
        contentPadding = PaddingValues(16.dp),
        horizontalArrangement = Arrangement.spacedBy(12.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        items(produk, key = { it.id }) { p ->
            Card(shape = RoundedCornerShape(12.dp)) {
                AsyncImage(
                    model = p.fotoUrl, contentDescription = p.nama,
                    contentScale = ContentScale.Crop,
                    modifier = Modifier.fillMaxWidth().aspectRatio(1f)
                )
                Column(Modifier.padding(12.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
                    Text(p.nama, maxLines = 2, overflow = TextOverflow.Ellipsis, style = MaterialTheme.typography.titleSmall)
                    Text(
                        rupiah.format(p.harga),
                        style = MaterialTheme.typography.titleMedium,
                        fontWeight = FontWeight.Bold,
                        color = MaterialTheme.colorScheme.primary
                    )
                }
            }
        }
    }
}''', lang='kotlin',
    pts=['LazyVerticalGrid + GridCells.Adaptive mirip auto-fill.', 'AsyncImage (Coil) + ContentScale.Crop + aspectRatio.', 'key yang stabil untuk setiap item.'],
    qs=[q('GridCells.Adaptive(160.dp) di layar 400dp (abaikan padding) menghasilkan berapa kolom?', ['1', '2', '3'], 1, '400 / 160 = 2 kolom muat.')]),
  C('Bottom navigation dan top app bar',
    ['Material 3 menyebut bottom navigation sebagai <b>NavigationBar</b>: 3 sampai 5 tujuan, ikon dan label, indikator pill di item aktif. Di Flutter: <code>NavigationBar</code> dengan <code>NavigationDestination</code>. Di Compose: <code>NavigationBar</code> dengan <code>NavigationBarItem</code>.',
     'Gunakan ikon <b>outlined</b> untuk item tidak aktif dan <b>filled</b> untuk item aktif jika desain memintanya (Flutter: <code>icon</code> dan <code>selectedIcon</code>). Badge jumlah notifikasi memakai widget <code>Badge</code> di keduanya.',
     '<b>Top app bar</b>: <code>AppBar</code> (Flutter) atau <code>TopAppBar</code> / <code>CenterAlignedTopAppBar</code> (Compose). Desain dengan judul besar yang mengecil saat menggulir menjadi <code>SliverAppBar.large</code> di Flutter dan <code>LargeTopAppBar</code> dengan <code>scrollBehavior</code> di Compose.'],
    code='''// Flutter
NavigationBar(
  selectedIndex: indeks,
  onDestinationSelected: (i) => setState(() => indeks = i),
  destinations: const [
    NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'Beranda'),
    NavigationDestination(icon: Icon(Icons.menu_book_outlined), selectedIcon: Icon(Icons.menu_book), label: 'Menu'),
    NavigationDestination(
      icon: Badge(label: Text('2'), child: Icon(Icons.shopping_bag_outlined)),
      selectedIcon: Icon(Icons.shopping_bag), label: 'Pesanan'),
    NavigationDestination(icon: Icon(Icons.person_outline), selectedIcon: Icon(Icons.person), label: 'Profil'),
  ],
)

// Jetpack Compose
NavigationBar {
    tujuan.forEachIndexed { i, t ->
        NavigationBarItem(
            selected = indeks == i,
            onClick = { indeks = i },
            icon = { Icon(if (indeks == i) t.ikonAktif else t.ikon, contentDescription = null) },
            label = { Text(t.label) }
        )
    }
}''', lang='dart',
    pts=['NavigationBar: 3–5 tujuan, ikon + label, indikator.', 'icon dan selectedIcon untuk outlined dan filled.', 'SliverAppBar.large / LargeTopAppBar untuk judul besar yang mengecil.'],
    qs=[q('Kenapa contentDescription ikon NavigationBarItem boleh null?', ['Karena label teks sudah menjelaskan tujuannya', 'Karena ikon tidak penting', 'Aturan Kotlin'], 0, 'Menghindari dibacakan dua kali.')]),
]),
M('Responsif dan pixel-perfect mobile', 'Menengah',
  'Layar berbagai ukuran dengan LayoutBuilder dan WindowSizeClass, pengujian pixel-perfect dengan golden dan screenshot test, serta proyek slicing aplikasi kedai kopi.',
  ['Adaptive layout', 'Golden tests', 'Project'], [
  C('Layar berbagai ukuran',
    ['Desain biasanya hanya untuk ponsel 360 sampai 393 dp, tetapi aplikasi juga berjalan di ponsel kecil (320 dp), ponsel lipat, dan tablet. Uji desain di ukuran <b>terkecil</b> (teks tidak terpotong, tombol tidak bertumpuk) dan <b>terbesar</b> (konten tidak melar terlalu lebar).',
     'Flutter: <code>LayoutBuilder</code> memberi lebar induk, <code>MediaQuery.sizeOf(context)</code> memberi ukuran layar. Compose: <code>currentWindowAdaptiveInfo().windowSizeClass</code> memberi kelas <b>compact</b> (&lt; 600 dp), <b>medium</b> (600 sampai 839), dan <b>expanded</b> (≥ 840). Pustaka <b>adaptive navigation suite</b> otomatis mengganti NavigationBar menjadi NavigationRail di layar lebar.',
     'Jangan lupa pengguna dengan <b>ukuran huruf besar</b> di pengaturan sistem. Uji dengan skala huruf 1,3× dan 2×: tinggi tetap pada kontainer teks adalah penyebab utama teks terpotong. Pakai tinggi minimum, bukan tinggi tetap.'],
    code='''// Flutter: 2 kolom di ponsel, 4 kolom mulai 600 dp
LayoutBuilder(
  builder: (context, c) {
    final kolom = c.maxWidth >= 840 ? 4 : c.maxWidth >= 600 ? 3 : 2;
    return GridView.count(crossAxisCount: kolom, children: kartu);
  },
)

// Compose: NavigationBar di ponsel, NavigationRail di layar lebar
val kelas = currentWindowAdaptiveInfo().windowSizeClass
if (kelas.isWidthAtLeastBreakpoint(WindowSizeClass.WIDTH_DP_MEDIUM_LOWER_BOUND)) {
    Row { NavigationRail { /* ... */ }; Konten() }
} else {
    Scaffold(bottomBar = { NavigationBar { /* ... */ } }) { Konten() }
}''', lang='dart',
    tb=[{'c': 'Kelas ukuran jendela', 'h': ['Kelas', 'Lebar', 'Contoh perangkat', 'Navigasi'], 'r': [['Compact', '< 600 dp', 'Ponsel tegak', 'NavigationBar'], ['Medium', '600–839 dp', 'Tablet tegak, lipat terbuka', 'NavigationRail'], ['Expanded', '≥ 840 dp', 'Tablet mendatar, desktop', 'NavigationRail atau drawer']]}],
    pts=['Uji di ukuran terkecil dan terbesar.', 'LayoutBuilder / WindowSizeClass: compact, medium, expanded.', 'Uji skala huruf 1,3× dan 2×; hindari tinggi tetap.'],
    qs=[q('Teks terpotong saat pengguna memperbesar huruf. Penyebab paling umum?', ['Kontainer dengan tinggi tetap', 'Warna teks', 'Font tidak terpasang'], 0, 'Pakai tinggi minimum.')]),
  C('Pixel-perfect dan golden test',
    ['Di mobile, membandingkan dengan desain dilakukan dengan menjalankan aplikasi di emulator berukuran sama dengan frame Figma (misalnya Pixel 7, 412 × 915 dp), mengambil tangkapan layar, lalu menumpuknya dengan ekspor frame di Figma (opacity 50%). Flutter juga punya <b>Flutter Inspector</b> dengan "Show guidelines" untuk melihat padding dan batas widget.',
     'Agar tampilan yang sudah benar tidak rusak diam-diam di kemudian hari, buat <b>golden test</b> (Flutter) atau <b>screenshot test</b> (Compose, dengan Roborazzi atau Paparazzi). Tes merender widget, menyimpan gambar acuan, dan gagal jika tampilan berubah walau satu piksel.',
     'Simpan gambar acuan di repositori, dan perbarui hanya jika perubahan tampilan memang disengaja (<code>flutter test --update-goldens</code>).'],
    code='''// test/kartu_produk_golden_test.dart
void main() {
  testWidgets('KartuProduk sesuai desain', (tester) async {
    tester.view.physicalSize = const Size(360, 300);
    tester.view.devicePixelRatio = 1.0;
    await tester.pumpWidget(MaterialApp(
      theme: temaKopiNusa,
      home: const Scaffold(body: KartuProduk(nama: 'Kopi Susu Aren', harga: 22000)),
    ));
    await expectLater(find.byType(KartuProduk), matchesGoldenFile('goldens/kartu_produk.png'));
  });
}

// Jalankan pertama kali (membuat gambar acuan):
//   flutter test --update-goldens
// Jalankan berikutnya (membandingkan):
//   flutter test''', lang='dart',
    pts=['Bandingkan di emulator berukuran sama dengan frame Figma.', 'Golden test (Flutter) dan screenshot test (Roborazzi, Paparazzi).', 'Perbarui acuan hanya untuk perubahan yang disengaja.'],
    qs=[q('Apa fungsi golden test?', ['Mendeteksi perubahan tampilan yang tidak disengaja', 'Menguji kecepatan jaringan', 'Mengompres gambar'], 0, 'Gambar acuan dibandingkan setiap kali tes jalan.')]),
  C('Proyek: slicing aplikasi kedai kopi',
    ['Proyek akhir: slicing empat layar aplikasi KopiNusa dari desain (atau buat desain sederhana sendiri di Figma terlebih dahulu): <b>Login</b>, <b>Beranda</b> (sapaan, banner promo, kategori chip, grid produk), <b>Detail produk</b> (foto besar, pilihan ukuran dan gula dengan SegmentedButton atau ChoiceChip, jumlah, tombol Tambah), dan <b>Keranjang</b> (daftar item, total, tombol Bayar).',
     'Pilih salah satu: Flutter atau Jetpack Compose. Kerjakan berurutan: tema dan token dulu, lalu komponen (KartuProduk, ChipKategori, BarisKeranjang), baru susun layar. Pakai data dummy dari list lokal.',
     'Kriteria selesai di tabel bawah. Unggah ke GitHub dengan README berisi tangkapan layar setiap layar dan perbandingan dengan desain.'],
    tb=[{'c': 'Kriteria selesai', 'h': ['Aspek', 'Kriteria'], 'r': [
      ['Tema', 'Warna dan teks dari ColorScheme dan TextTheme/Typography, tidak ada hex di widget'], ['Komponen', 'Minimal 3 komponen dipakai ulang dengan parameter'],
      ['Layout', 'Tidak ada overflow di 320 dp dan di skala huruf 1,3×'], ['Navigasi', 'NavigationBar 4 tujuan, kembali dari detail ke beranda'],
      ['Aksesibilitas', 'Target sentuh 48 dp, contentDescription / semanticLabel untuk ikon'], ['Format', 'Harga Rupiah Rp22.000'],
      ['Uji', 'Minimal 1 golden atau screenshot test untuk KartuProduk'], ['Dokumentasi', 'README dengan tangkapan layar dan cara menjalankan']]}],
    pts=['Tema dulu, komponen, lalu layar.', 'Uji 320 dp dan skala huruf besar.', 'README dengan perbandingan desain.'],
    qs=[q('Urutan kerja slicing aplikasi yang disarankan?', ['Layar dulu, tema terakhir', 'Tema dan token, komponen, lalu layar', 'Acak'], 1, 'Fondasi dulu agar tidak menulis ulang.')]),
]),
]

SLM_SO = {
'Membaca desain mobile': [
  T('Frame Figma 390 × 844 berisi: padding layar 20, judul 28/34, kartu tinggi 120 radius 16, tombol tinggi 52. Tulis nilai Flutter dan Compose-nya.', 'Satu banding satu; huruf memakai sp di Compose.',
    'Flutter : EdgeInsets.all(20), TextStyle(fontSize: 28, height: 34 / 28), SizedBox(height: 120), BorderRadius.circular(16), Size.fromHeight(52)\nCompose : Modifier.padding(20.dp), fontSize = 28.sp, lineHeight = 34.sp, Modifier.height(120.dp), RoundedCornerShape(16.dp), Modifier.height(52.dp)'),
],
'Ekspor aset dan ikon': [
  D('Tampilkan ikon SVG keranjang 24×24 berwarna primary tema di Flutter.', 'SvgPicture.asset dengan colorFilter.',
    "SvgPicture.asset(\n  'assets/icons/ic_cart.svg',\n  width: 24,\n  height: 24,\n  colorFilter: ColorFilter.mode(Theme.of(context).colorScheme.primary, BlendMode.srcIn),\n  semanticsLabel: 'Keranjang',\n)"),
],
'Token desain ke ThemeData dan MaterialTheme': [
  K('Buat skema warna terang Compose dari token: primary #6D4C41, onPrimary #FFFFFF, primaryContainer #FFDBCF, surface #FFF8F5.', 'lightColorScheme dengan parameter bernama.',
    'val KopiLight = lightColorScheme(\n    primary = Color(0xFF6D4C41),\n    onPrimary = Color(0xFFFFFFFF),\n    primaryContainer = Color(0xFFFFDBCF),\n    surface = Color(0xFFFFF8F5)\n)\n\n@Composable\nfun KopiTheme(content: @Composable () -> Unit) {\n    MaterialTheme(colorScheme = KopiLight, content = content)\n}'),
],
'Memetakan auto layout ke Row dan Column': [
  D('Terjemahkan ke Flutter: frame horizontal, padding 16, gap 12, align center; anak: avatar 40×40, kolom teks (Fill), ikon chevron (Hug).', 'Row + Expanded untuk Fill.',
    'Padding(\n  padding: const EdgeInsets.all(16),\n  child: Row(\n    spacing: 12,\n    children: [\n      const CircleAvatar(radius: 20),\n      Expanded(\n        child: Column(\n          crossAxisAlignment: CrossAxisAlignment.start,\n          children: const [Text(\'Rina Siregar\'), Text(\'Flutter Developer\')],\n        ),\n      ),\n      const Icon(Icons.chevron_right),\n    ],\n  ),\n)'),
],
'Layar login di Flutter': [
  D('Tambahkan validasi pada field email login: wajib diisi dan harus mengandung @, dengan pesan error berbahasa Indonesia.', 'TextFormField + validator di dalam Form.',
    "TextFormField(\n  decoration: const InputDecoration(labelText: 'Email', border: OutlineInputBorder()),\n  keyboardType: TextInputType.emailAddress,\n  validator: (v) {\n    if (v == null || v.trim().isEmpty) return 'Email wajib diisi';\n    if (!v.contains('@')) return 'Format email belum benar, contoh: nama@contoh.com';\n    return null;\n  },\n)"),
],
'Layar login di Jetpack Compose': [
  K('Tampilkan pesan error di bawah OutlinedTextField email jika tidak mengandung @.', 'Parameter isError dan supportingText.',
    'val salah = email.isNotEmpty() && !email.contains("@")\nOutlinedTextField(\n    value = email, onValueChange = { email = it },\n    label = { Text("Email") },\n    isError = salah,\n    supportingText = { if (salah) Text("Format email belum benar, contoh: nama@contoh.com") },\n    modifier = Modifier.fillMaxWidth()\n)'),
],
'Kartu produk dan grid di Flutter': [
  D('Tambahkan lencana "Baru" di pojok kiri atas foto kartu produk.', 'Stack dengan Positioned.',
    "Stack(\n  children: [\n    AspectRatio(aspectRatio: 1, child: Image.asset(p.foto, fit: BoxFit.cover)),\n    Positioned(\n      top: 8, left: 8,\n      child: Container(\n        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),\n        decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(99)),\n        child: const Text('Baru', style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600)),\n      ),\n    ),\n  ],\n)"),
],
'Kartu produk dan LazyVerticalGrid di Compose': [
  K('Tambahkan lencana "Baru" di pojok kiri atas foto kartu Compose.', 'Box dengan Modifier.align(Alignment.TopStart).',
    'Box {\n    AsyncImage(model = p.fotoUrl, contentDescription = p.nama, contentScale = ContentScale.Crop,\n        modifier = Modifier.fillMaxWidth().aspectRatio(1f))\n    Surface(\n        shape = CircleShape, color = Color.White,\n        modifier = Modifier.align(Alignment.TopStart).padding(8.dp)\n    ) {\n        Text("Baru", style = MaterialTheme.typography.labelMedium, modifier = Modifier.padding(horizontal = 8.dp, vertical = 2.dp))\n    }\n}'),
],
'Bottom navigation dan top app bar': [
  K('Buat CenterAlignedTopAppBar dengan judul "KopiNusa" dan tombol ikon keranjang di kanan.', 'actions berisi IconButton dengan contentDescription.',
    'CenterAlignedTopAppBar(\n    title = { Text("KopiNusa") },\n    actions = {\n        IconButton(onClick = onKeranjang) {\n            Icon(Icons.Outlined.ShoppingCart, contentDescription = "Keranjang")\n        }\n    }\n)'),
],
'Layar berbagai ukuran': [
  D('Batasi lebar konten maksimal 600 dan letakkan di tengah agar tidak melar di tablet.', 'Center + ConstrainedBox.',
    'Center(\n  child: ConstrainedBox(\n    constraints: const BoxConstraints(maxWidth: 600),\n    child: konten,\n  ),\n)'),
],
'Pixel-perfect dan golden test': [
  T('Tulis langkah membandingkan layar Beranda di emulator dengan frame Figma.', 'Ukuran sama, tangkapan layar, tumpuk dengan opacity.',
    '1. Buat emulator dengan lebar sama dengan frame (misal 412 dp).\n2. Jalankan aplikasi, ambil tangkapan layar Beranda.\n3. Ekspor frame Figma pada skala yang sama dengan densitas emulator.\n4. Tumpuk di Figma: tangkapan layar di atas, opacity 50%.\n5. Catat selisih jarak, ukuran huruf, warna; perbaiki yang berdampak besar dulu.'),
],
'Proyek: slicing aplikasi kedai kopi': [
  T('Tulis daftar komponen yang akan kamu buat untuk proyek KopiNusa beserta parameternya.', 'Komponen yang muncul lebih dari sekali.',
    'KartuProduk(nama, harga, foto, onTambah)\nChipKategori(label, terpilih, onTap)\nBannerPromo(judul, subjudul, gambar)\nPemilihJumlah(nilai, onKurang, onTambah)\nBarisKeranjang(produk, jumlah, onUbah, onHapus)\nTombolUtama(label, onPressed, memuat)'),
],
}
