"""Studi kasus step by step: contoh desain + slicing (web dan mobile), proyek desain UI, design system dunia nyata, dan portofolio.
Semua modul ditambahkan di akhir jalur agar alamat pelajaran lama tidak bergeser."""
from mobile_lib import W, C, M, q
from mobile_dart_x import S
from uidesign import L, H, X, T, G, RULES


def D(soal, petunjuk, jawab):
    return S(soal, petunjuk, jawab, lang='dart')


def K(soal, petunjuk, jawab):
    return S(soal, petunjuk, jawab, lang='kotlin')


# ===================================================================
#  Desain contoh: landing page "Kopi Kita"
# ===================================================================
KARTU = ''.join(f'''
      <article class="kartu">
        <div class="kartu-foto" style="--foto:{w}" role="img" aria-label="Kemasan {n}"></div>
        <h3>{n}</h3>
        <p class="asal">{a}</p>
        <p class="harga">{h}</p>
        <a class="btn btn-primer" href="#">Tambah</a>
      </article>''' for n, a, h, w in [
    ('Kopi Gayo', 'Aceh · medium roast', 'Rp85.000', '#B07A52'),
    ('Kopi Toraja', 'Sulawesi · dark roast', 'Rp95.000', '#6E4A33'),
    ('Kopi Kintamani', 'Bali · light roast', 'Rp90.000', '#C9A27E')])

ISI = '''
    <section class="hero">
      <div class="hero-teks">
        <p class="eyebrow">Roastery Medan sejak 2019</p>
        <h1>Kopi Nusantara, dipanggang setiap minggu</h1>
        <p class="lead">Biji pilihan dari Gayo, Toraja, dan Kintamani, dikirim ke rumahmu dalam 2 hari.</p>
        <div class="aksi"><a class="btn btn-primer" href="#">Lihat menu</a><a class="btn btn-garis" href="#">Langganan</a></div>
      </div>
      <div class="hero-gambar" role="img" aria-label="Biji kopi di atas karung goni"></div>
    </section>
    <section class="produk">
      <h2>Paling dicari</h2>
      <div class="grid">''' + KARTU + '''
      </div>
    </section>
    <section class="cta">
      <h2>Diskon 10% untuk langganan pertama</h2>
      <form class="cta-form" onsubmit="return false">
        <label class="sr" for="em">Email</label>
        <input id="em" type="email" placeholder="email@contoh.id">
        <button class="btn btn-aksen">Daftar</button>
      </form>
    </section>'''

NAV = '''<a class="logo" href="#">Kopi Kita</a>
    <nav class="menu" aria-label="Utama"><a href="#">Menu</a><a href="#">Cerita</a><a href="#">Lokasi</a></nav>
    <a class="btn btn-primer" href="#">Pesan</a>'''

KAKI = '<p>© 2026 Kopi Kita · Jl. Gatot Subroto 12, Medan</p>'

HALAMAN = f'''<header class="nav">
    {NAV}
  </header>
  <main>{ISI}
  </main>
  <footer class="kaki">{KAKI}</footer>'''

# versi "div semua" untuk latihan HTML semantik
DIVS = (HALAMAN.replace('<header class="nav">', '<div class="nav">').replace('</header>', '</div>')
        .replace('<main>', '<div class="isi">').replace('</main>', '</div>')
        .replace('<footer class="kaki">', '<div class="kaki">').replace('</footer>', '</div>')
        .replace('<section ', '<div ').replace('</section>', '</div>')
        .replace('<nav class="menu" aria-label="Utama">', '<div class="menu">').replace('</nav>', '</div>'))

TOKEN = ''':root {
  --warna-primer: #8A4B2A;
  --warna-primer-gelap: #6B3A20;
  --warna-aksen: #E9B872;
  --latar: #FBF7F2;
  --permukaan: #FFFFFF;
  --teks: #2B2724;
  --teks-2: #6B625B;
  --garis: #E8DFD5;
  --radius: 12px;
  --ruang-1: 8px; --ruang-2: 16px; --ruang-3: 24px; --ruang-4: 32px; --ruang-5: 48px;
}
'''
DASAR = '''* { box-sizing: border-box; }
body { margin: 0; font: 16px/1.5 system-ui, sans-serif; background: var(--latar); color: var(--teks); }
h1, h2, h3, p { margin: 0; }
a { color: inherit; }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
.btn { display: inline-flex; align-items: center; justify-content: center; padding: 0 var(--ruang-2); height: 44px;
       border-radius: var(--radius); font-weight: 600; text-decoration: none; border: 2px solid transparent; font-size: 15px; cursor: pointer; }
.btn-primer { background: var(--warna-primer); color: #fff; }
.btn-garis { border-color: var(--warna-primer); color: var(--warna-primer); }
.btn-aksen { background: var(--warna-aksen); color: var(--teks); }
'''
NAVHERO = '''.nav { display: flex; justify-content: space-between; align-items: center; gap: var(--ruang-2); padding: var(--ruang-2); background: var(--permukaan); border-bottom: 1px solid var(--garis); }
.logo { font-weight: 800; font-size: 20px; text-decoration: none; color: var(--warna-primer); }
.menu { display: none; gap: var(--ruang-3); }
.menu a { text-decoration: none; color: var(--teks-2); }
.hero { display: grid; gap: var(--ruang-3); padding: var(--ruang-4) var(--ruang-2); }
.eyebrow { font-size: 13px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; color: var(--warna-primer); }
.hero h1 { font-size: 28px; line-height: 1.2; margin: var(--ruang-1) 0 var(--ruang-2); text-wrap: balance; }
.lead { color: var(--teks-2); }
.aksi { display: flex; flex-wrap: wrap; gap: var(--ruang-1); margin-top: var(--ruang-3); }
.hero-gambar { aspect-ratio: 4 / 3; border-radius: var(--radius); background: radial-gradient(circle at 30% 40%, #B07A52 0 12%, transparent 13%), radial-gradient(circle at 65% 60%, #6E4A33 0 14%, transparent 15%), #D9C2A7; }
'''
KARTUCSS = '''.produk { padding: var(--ruang-4) var(--ruang-2); }
.produk h2, .cta h2 { font-size: 22px; margin-bottom: var(--ruang-3); }
.grid { display: grid; gap: var(--ruang-2); }
.kartu { background: var(--permukaan); border: 1px solid var(--garis); border-radius: var(--radius); padding: var(--ruang-2); display: grid; gap: var(--ruang-1); }
.kartu-foto { aspect-ratio: 1; border-radius: 8px; background: var(--foto); }
.kartu h3 { font-size: 18px; }
.asal { font-size: 14px; color: var(--teks-2); }
.harga { font-weight: 700; font-size: 18px; }
.cta { margin: 0 var(--ruang-2) var(--ruang-4); padding: var(--ruang-3); border-radius: var(--radius); background: var(--warna-primer-gelap); color: #fff; }
.cta h2 { margin-bottom: var(--ruang-2); }
.cta-form { display: flex; flex-wrap: wrap; gap: var(--ruang-1); }
.cta-form input { flex: 1 1 180px; height: 44px; padding: 0 12px; border-radius: var(--radius); border: 0; font-size: 16px; }
.kaki { padding: var(--ruang-3) var(--ruang-2); font-size: 14px; color: var(--teks-2); border-top: 1px solid var(--garis); }
'''
DESKTOP = '''@media (min-width: 768px) {
  .menu { display: flex; }
  .hero { grid-template-columns: 1fr 1fr; align-items: center; padding: var(--ruang-5) var(--ruang-4); }
  .hero h1 { font-size: 40px; }
  .produk { padding: var(--ruang-5) var(--ruang-4); }
  .grid { grid-template-columns: repeat(3, 1fr); }
  .cta { margin: 0 var(--ruang-4) var(--ruang-5); }
}
'''
STATE = '''.btn:hover { filter: brightness(1.08); }
.btn:focus-visible, .menu a:focus-visible, input:focus-visible { outline: 3px solid var(--warna-aksen); outline-offset: 2px; }
.btn:active { transform: translateY(1px); }
'''
FINAL_CSS = TOKEN + DASAR + NAVHERO + KARTUCSS + DESKTOP + STATE

# papan desain ala Figma: frame mobile + desktop, redline, token
PAPAN_HTML = '''<div class="papan">
  <p class="label">Frame · Mobile 360 × 1280 · Landing Kopi Kita (Ready for dev)</p>
  <div class="frame m">
    <div class="halaman">''' + HALAMAN + '''</div>
    <span class="rl" style="top:62px;left:0;width:16px" data-v="16"></span>
    <span class="rl v" style="top:64px;left:120px;height:32px" data-v="32"></span>
    <span class="tag" style="top:150px;right:6px">H1 28/34 · 800</span>
    <span class="tag" style="top:286px;right:6px">Tombol 44 · r12</span>
  </div>
  <p class="label">Token</p>
  <div class="token">
    <span style="--c:#8A4B2A">primer<br>#8A4B2A</span><span style="--c:#6B3A20">primer-gelap<br>#6B3A20</span>
    <span style="--c:#E9B872">aksen<br>#E9B872</span><span style="--c:#FBF7F2">latar<br>#FBF7F2</span>
    <span style="--c:#2B2724">teks<br>#2B2724</span><span style="--c:#6B625B">teks-2<br>#6B625B</span>
  </div>
  <p class="label">Tipografi dan jarak</p>
  <table class="spek"><tr><th>Gaya</th><th>Mobile</th><th>Desktop</th></tr>
    <tr><td>H1</td><td>28 / 1.2 · 800</td><td>40 / 1.2 · 800</td></tr>
    <tr><td>H2</td><td>22 · 700</td><td>22 · 700</td></tr>
    <tr><td>Body</td><td>16 / 1.5</td><td>16 / 1.5</td></tr>
    <tr><td>Jarak</td><td colspan="2">8 · 16 · 24 · 32 · 48 (grid 8 poin)</td></tr>
    <tr><td>Breakpoint</td><td colspan="2">768 px: menu tampil, hero 2 kolom, produk 3 kolom</td></tr></table>
</div>'''
PAPAN_CSS = FINAL_CSS.replace('body {', '.halaman {') + '''
body { margin: 0; background: #2C2C2C; font-family: system-ui, sans-serif; }
.papan { padding: 16px; color: #EDEDED; }
.label { font-size: 12px; color: #B5B5B5; margin: 16px 0 8px; }
.frame { position: relative; width: 360px; max-width: 100%; background: var(--latar); box-shadow: 0 0 0 1px #4A90E2; }
.rl { position: absolute; border-top: 1px solid #F24E1E; }
.rl.v { border-top: 0; border-left: 1px solid #F24E1E; }
.rl::after { content: attr(data-v); position: absolute; background: #F24E1E; color: #fff; font: 600 10px/1 system-ui; padding: 2px 4px; border-radius: 3px; top: -8px; left: 4px; }
.tag { position: absolute; background: #7B61FF; color: #fff; font: 600 10px/1 system-ui; padding: 3px 6px; border-radius: 3px; }
.token { display: flex; flex-wrap: wrap; gap: 8px; }
.token span { font-size: 11px; line-height: 1.3; width: 96px; }
.token span::before { content: ""; display: block; height: 40px; border-radius: 6px; background: var(--c); margin-bottom: 4px; box-shadow: inset 0 0 0 1px #555; }
.spek { border-collapse: collapse; font-size: 12px; color: #EDEDED; }
.spek td, .spek th { border: 1px solid #555; padding: 4px 8px; text-align: left; }
'''

SLW_KASUS = [
M('Studi kasus: slicing landing page step by step', 'Menengah',
  'Satu desain utuh, landing page roastery "Kopi Kita", di-slicing dari nol mengikuti alur kerja slicer profesional: audit desain, token, HTML semantik, layout mobile-first, komponen, breakpoint, state dan aksesibilitas, lalu QA dan serah terima.',
  ['Design handoff', 'Design tokens', 'Semantic HTML', 'Mobile-first', 'Components', 'Breakpoints', 'Pixel-perfect QA'], [
  W('Contoh desain: papan Figma "Kopi Kita"',
    ['Ini contoh desain yang akan kita slicing sampai jadi. Pratinjau menampilkan tiruan papan <b>Figma Dev Mode</b>: frame mobile 360 px yang sudah ditandai <b>Ready for dev</b>, garis merah <b>redline</b> berisi jarak dalam px, label ungu berisi spesifikasi komponen, palet <b>token warna</b>, dan tabel tipografi serta breakpoint.',
     'Di proyek nyata, desainer menyerahkan file Figma berisi frame mobile dan desktop, halaman komponen, dan halaman style guide. Tugas slicer adalah mengubahnya menjadi HTML dan CSS yang <b>setia pada desain</b> (pixel-perfect), <b>responsif</b>, <b>aksesibel</b>, dan <b>mudah dirawat</b>.',
     'Perhatikan baik-baik sebelum menulis kode: berapa section yang ada, komponen apa yang berulang, berapa ukuran jarak yang dipakai, dan apa yang berubah di layar lebar. Pelajaran berikutnya mengikuti tujuh langkah standar industri, satu langkah per pelajaran.'],
    PAPAN_HTML, css=PAPAN_CSS,
    pts=['Desain lengkap: frame mobile dan desktop, komponen, style guide.', 'Redline memberi jarak, label memberi spesifikasi.', 'Amati dulu sebelum menulis kode.'],
    qs=[q('Frame yang boleh mulai di-slicing biasanya ditandai?', ['Ready for dev', 'Draft', 'Archive'], 0, 'Frame lain mungkin masih eksplorasi.')]),
  C('Langkah 1: audit desain dan inventaris komponen',
    ['Slicer profesional tidak langsung menulis CSS. Langkah pertama adalah <b>audit desain</b> selama 15 sampai 30 menit: buka semua frame (mobile, tablet, desktop), catat section, komponen berulang, token, aset, dan hal yang belum jelas.',
     'Hasil audit berupa <b>inventaris</b>: daftar section, daftar komponen beserta variannya (tombol primer, tombol garis, tombol aksen), daftar token, daftar aset yang harus diekspor, dan daftar <b>pertanyaan untuk desainer</b>. Pertanyaan yang ditanyakan di awal jauh lebih murah daripada revisi di akhir.',
     'Yang sering terlewat dan wajib ditanyakan: state hover, fokus, nonaktif, dan error; perilaku teks yang sangat panjang; tampilan saat data kosong; dan apa yang terjadi di antara dua breakpoint (misalnya lebar 600 px).'],
    "INVENTARIS · Landing Kopi Kita\n\nSection  : nav, hero, produk (3 kartu), cta langganan, footer\nKomponen : Tombol (primer, garis, aksen) tinggi 44, radius 12\n           Kartu produk: foto 1:1, nama, asal, harga, tombol\n           Input email + tombol (form satu baris, membungkus di layar sempit)\nToken    : 6 warna, radius 12, jarak 8/16/24/32/48, H1 28->40\nAset     : logo SVG, 3 foto produk WebP (2x), foto hero WebP\nBreakpoint: 768 px (menu tampil, hero 2 kolom, produk 3 kolom)\n\nPERTANYAAN UNTUK DESAINER\n1. State hover dan fokus tombol belum ada di file. Boleh pakai brightness +8% dan outline aksen?\n2. Di mobile, menu disembunyikan. Apakah perlu tombol hamburger?\n3. Nama produk yang panjang (2 baris) dipotong atau dibiarkan membungkus?",
    None, 'text',
    tb=[{'c': 'Checklist audit desain', 'h': ['Periksa', 'Pertanyaan'], 'r': [
      ['Frame', 'Ada versi mobile, tablet, desktop? Mana yang Ready for dev?'], ['Komponen', 'Apa saja yang berulang? Berapa varian?'],
      ['Token', 'Apakah warna dan teks memakai variabel atau style Figma?'], ['State', 'Hover, fokus, aktif, nonaktif, error, memuat, kosong?'],
      ['Konten', 'Teks panjang, angka besar, nama dua baris?'], ['Aset', 'Format apa, ukuran berapa, perlu 2x?'], ['Interaksi', 'Animasi, sticky, scroll, modal?']]}],
    pts=['Audit 15 sampai 30 menit sebelum coding.', 'Inventaris: section, komponen, token, aset, pertanyaan.', 'Tanyakan state dan kasus ekstrem di awal.'],
    qs=[q('Kapan waktu terbaik bertanya soal state hover yang tidak ada di desain?', ['Saat audit, sebelum coding', 'Setelah halaman selesai', 'Tidak perlu ditanyakan'], 0, 'Murah di awal, mahal di akhir.')],
    so=[T('Buat inventaris singkat untuk sebuah halaman login: section, komponen, token, dan dua pertanyaan untuk desainer.', 'Pikirkan state error dan lupa kata sandi.',
          'Section: logo, judul, form, tautan daftar\nKomponen: input (default, fokus, error), tombol primer, tautan\nToken: warna primer, merah error, radius 12, jarak 8/16/24\nPertanyaan: 1) Pesan error tampil di bawah input atau di atas form? 2) Ada opsi tampilkan kata sandi?')]),
  L('Langkah 2: token desain menjadi CSS variables',
    ['Pindahkan semua nilai dari style guide ke <b>CSS custom properties</b> di <code>:root</code>: warna, radius, dan skala jarak. Setelah itu, CSS komponen hanya boleh memakai <code>var(--...)</code>, bukan kode hex langsung. Jika brand berganti warna, cukup ubah satu baris.',
     'Pakai nama <b>semantik</b> yang sama dengan nama variabel di Figma (<code>--warna-primer</code>, <code>--teks-2</code>), bukan nama warna (<code>--coklat</code>). Nama yang sama memudahkan desainer dan developer berbicara dalam bahasa yang sama.',
     'Di pratinjau, halaman sudah punya struktur dan gaya dasar, tetapi token belum didefinisikan sehingga warna dan jarak berantakan.'],
    HALAMAN, DASAR + NAVHERO + KARTUCSS,
    {'q': 'Definisikan token di <code>:root</code>: minimal <code>--warna-primer: #8A4B2A</code>, <code>--latar: #FBF7F2</code>, <code>--teks: #2B2724</code>, <code>--radius: 12px</code>, dan <code>--ruang-2: 16px</code>.',
     'test': "(s=>s.getPropertyValue('--warna-primer').trim().toUpperCase()==='#8A4B2A'&&s.getPropertyValue('--latar').trim().toUpperCase()==='#FBF7F2'&&s.getPropertyValue('--radius').trim()==='12px'&&s.getPropertyValue('--ruang-2').trim()==='16px')(getComputedStyle(document.documentElement))",
     'hint': 'Salin blok :root dari tabel token papan desain: :root { --warna-primer: #8A4B2A; --latar: #FBF7F2; --teks: #2B2724; --radius: 12px; --ruang-2: 16px; ... }'},
    ['Token di :root, komponen memakai var().', 'Nama semantik sama dengan Figma.', 'Ganti brand cukup satu baris.'],
    [q('Nama token yang paling baik?', ['--warna-primer', '--coklat-tua', '--c1'], 0, 'Semantik, sesuai peran.')],
    {'css': TOKEN}),
  L('Langkah 3: kerangka HTML semantik',
    ['Sebelum mengatur tampilan, susun <b>struktur</b> yang benar. Setiap section desain menjadi elemen semantik: <code>&lt;header&gt;</code> untuk navbar, <code>&lt;nav&gt;</code> untuk menu, <code>&lt;main&gt;</code> untuk isi utama (hanya satu per halaman), <code>&lt;section&gt;</code> untuk tiap bagian dengan judul, <code>&lt;article&gt;</code> untuk kartu yang berdiri sendiri, dan <code>&lt;footer&gt;</code>.',
     'Struktur semantik membantu pembaca layar (pengguna tunanetra bisa melompat antar landmark), mesin pencari, dan rekan developer. Urutan heading juga harus runtut: satu <code>h1</code>, lalu <code>h2</code> untuk tiap section, <code>h3</code> untuk judul kartu.',
     'Pratinjau berisi halaman yang ditulis dengan <code>div</code> semua. Tampilannya sama, tetapi maknanya hilang.'],
    DIVS, TOKEN + DASAR + NAVHERO + KARTUCSS,
    {'q': 'Ganti div pembungkus dengan elemen semantik: ada <code>header</code>, <code>nav</code>, satu <code>main</code> berisi minimal 3 <code>section</code>, dan <code>footer</code>.',
     'test': "!!document.querySelector('header .logo')&&!!document.querySelector('header nav')&&document.querySelectorAll('main').length===1&&document.querySelectorAll('main > section').length>=3&&!!document.querySelector('footer')",
     'hint': '<div class="nav"> menjadi <header class="nav">, <div class="menu"> menjadi <nav class="menu">, <div class="isi"> menjadi <main>, setiap <div class="hero|produk|cta"> menjadi <section>, <div class="kaki"> menjadi <footer>.'},
    ['header, nav, main, section, article, footer.', 'Satu h1, lalu h2 per section.', 'Landmark membantu pembaca layar dan SEO.'],
    [q('Berapa elemen main yang boleh ada di satu halaman?', ['Satu', 'Satu per section', 'Bebas'], 0, 'Landmark isi utama.')],
    {'html': HALAMAN}),
  L('Langkah 4: layout mobile-first untuk navbar dan hero',
    ['Tulis CSS untuk layar <b>terkecil dulu</b> (360 px), tanpa media query. Navbar: logo kiri, tombol kanan, sejajar vertikal, dengan <b>flexbox</b>. Menu disembunyikan di mobile sesuai desain. Hero: satu kolom, judul 28 px, jarak sesuai redline.',
     'Salin angka dari redline, bukan dari perkiraan mata: padding 16 px di sisi, 32 px di atas dan bawah hero, jarak antar tombol 8 px. Semua angka itu ada di skala token (<code>--ruang-1</code> sampai <code>--ruang-5</code>), jadi pakai variabelnya.',
     'Pratinjau sudah punya token dan gaya tombol, tetapi navbar dan hero belum ditata.'],
    HALAMAN, TOKEN + DASAR + KARTUCSS.replace('.produk {', '.produk { clear: both; '),
    {'q': 'Tata <code>.nav</code> dengan flex: <code>justify-content: space-between</code> dan <code>align-items: center</code>. Beri <code>.hero h1</code> ukuran 28px, dan sembunyikan <code>.menu</code> di mobile.',
     'test': f"{G.format('.nav')}.display==='flex'&&{G.format('.nav')}.justifyContent==='space-between'&&{G.format('.nav')}.alignItems==='center'&&parseFloat({G.format('.hero h1')}.fontSize)===28&&{G.format('.menu')}.display==='none'",
     'hint': '.nav { display: flex; justify-content: space-between; align-items: center; padding: var(--ruang-2) } .hero h1 { font-size: 28px } .menu { display: none }'},
    ['Mobile dulu, tanpa media query.', 'Angka dari redline, ditulis dengan token.', 'Flexbox untuk navbar.'],
    [q('Kenapa menulis CSS mobile lebih dulu?', ['Gaya dasar sederhana lalu ditambah untuk layar lebar', 'Desktop tidak penting', 'Media query lebih cepat'], 0, 'Min-width menambah, bukan membatalkan.')],
    {'css': NAVHERO}),
  L('Langkah 5: komponen kartu produk dan grid',
    ['Kartu produk muncul tiga kali: tulis <b>satu komponen</b> <code>.kartu</code>, bukan tiga gaya terpisah. Anatominya dari desain: foto rasio 1:1, nama 18 px, asal 14 px abu-abu, harga 18 px tebal, tombol penuh. Jarak di dalam kartu 8 px, padding 16 px, radius 12 px, garis tepi 1 px.',
     'Susun kartu dengan <b>CSS Grid</b> dan <code>gap</code>, bukan margin di tiap kartu. Di mobile cukup satu kolom; nanti di breakpoint desktop tinggal mengubah jumlah kolom.',
     'Konten nyata bisa lebih panjang dari desain. Uji dengan mengganti nama produk menjadi dua baris dan pastikan kartu tetap rapi.'],
    HALAMAN, TOKEN + DASAR + NAVHERO + ''.join(b for b in KARTUCSS.splitlines(True) if not b.startswith(('.grid', '.kartu', '.asal', '.harga'))),
    {'q': 'Buat <code>.grid</code> menjadi grid dengan gap 16px, dan beri <code>.kartu</code> radius 12px, padding 16px, serta garis tepi 1px.',
     'test': f"{G.format('.grid')}.display==='grid'&&{G.format('.grid')}.rowGap==='16px'&&{G.format('.kartu')}.borderTopLeftRadius==='12px'&&{G.format('.kartu')}.paddingTop==='16px'&&{G.format('.kartu')}.borderTopWidth==='1px'",
     'hint': '.grid { display: grid; gap: var(--ruang-2) } .kartu { background: var(--permukaan); border: 1px solid var(--garis); border-radius: var(--radius); padding: var(--ruang-2); display: grid; gap: var(--ruang-1) }'},
    ['Satu komponen untuk elemen berulang.', 'Grid + gap, bukan margin per kartu.', 'Uji dengan konten yang lebih panjang.'],
    [q('Tiga kartu produk sebaiknya ditata dengan?', ['Satu kelas .kartu + grid dengan gap', 'Tiga kelas berbeda', 'Tabel HTML'], 0, 'Komponen dipakai ulang.')],
    {'css': '.grid { display: grid; gap: var(--ruang-2); }\n.kartu { background: var(--permukaan); border: 1px solid var(--garis); border-radius: var(--radius); padding: var(--ruang-2); display: grid; gap: var(--ruang-1); }\n.kartu-foto { aspect-ratio: 1; border-radius: 8px; background: var(--foto); }\n.kartu h3 { font-size: 18px; }\n.asal { font-size: 14px; color: var(--teks-2); }\n.harga { font-weight: 700; font-size: 18px; }\n'}),
  L('Langkah 6: breakpoint desktop',
    ['Setelah mobile rapi, tambahkan <b>satu media query</b> <code>@media (min-width: 768px)</code> sesuai catatan desain: menu tampil, hero dua kolom, judul 40 px, produk tiga kolom, padding sisi 32 px.',
     'Jangan menyalin semua gaya ke dalam media query; tulis hanya yang <b>berubah</b>. Periksa juga lebar di antara breakpoint (600, 900, 1200 px) dengan menyeret lebar jendela browser atau memakai mode responsif DevTools (Ctrl + Shift + M).',
     'Di layar sangat lebar (1440 px ke atas), batasi lebar isi dengan <code>max-width</code> dan <code>margin-inline: auto</code> agar baris teks tidak terlalu panjang.'],
    HALAMAN, TOKEN + DASAR + NAVHERO + KARTUCSS + STATE,
    {'q': 'Tambahkan <code>@media (min-width: 768px)</code> yang membuat <code>.grid</code> menjadi 3 kolom (<code>repeat(3, 1fr)</code>) dan <code>.menu</code> tampil sebagai flex.',
     'test': f"{RULES}.some(r=>r.media&&/min-width/.test(r.conditionText)&&[...r.cssRules].some(x=>x.selectorText==='.grid'&&/repeat\\(3|1fr 1fr 1fr/.test(x.style.gridTemplateColumns))&&[...r.cssRules].some(x=>x.selectorText==='.menu'&&x.style.display==='flex'))",
     'hint': '@media (min-width: 768px) { .menu { display: flex } .grid { grid-template-columns: repeat(3, 1fr) } .hero { grid-template-columns: 1fr 1fr } .hero h1 { font-size: 40px } }'},
    ['Satu media query min-width, hanya yang berubah.', 'Uji lebar di antara breakpoint.', 'Batasi lebar isi di layar sangat lebar.'],
    [q('Isi media query desktop sebaiknya?', ['Hanya gaya yang berubah dari mobile', 'Salinan semua gaya', 'Gaya mobile yang dibatalkan'], 0, 'Lebih ringkas dan mudah dirawat.')],
    {'css': DESKTOP}),
  L('Langkah 7: state, aksesibilitas, dan QA pixel-perfect',
    ['Desain statis hanya menampilkan satu keadaan. Lengkapi <b>state interaktif</b>: hover, <b>fokus keyboard</b> (<code>:focus-visible</code> dengan outline yang kontras), aktif, dan nonaktif. Pastikan target sentuh minimal 44 px dan setiap input punya label (boleh disembunyikan secara visual dengan kelas <code>.sr</code>).',
     '<b>QA pixel-perfect</b>: tumpuk tangkapan layar hasil di atas desain (ekstensi PerfectPixel atau fitur overlay di Figma) pada 360 px dan 1440 px. Periksa jarak, ukuran font, warna, dan perataan. Lalu uji di perangkat nyata, mode gelap sistem, zoom 200%, navigasi dengan Tab saja, dan Lighthouse (target aksesibilitas 95+).',
     'Terakhir, <b>serah terima</b>: kirim tautan pratinjau (Vercel, Netlify), daftar perbedaan yang disengaja beserta alasannya, dan jawaban atas pertanyaan audit. Desainer meninjau, lalu pull request digabungkan.'],
    HALAMAN, TOKEN + DASAR + NAVHERO + KARTUCSS + DESKTOP,
    {'q': 'Tambahkan gaya fokus keyboard: aturan <code>.btn:focus-visible</code> dengan outline minimal 2px, dan pastikan <code>.btn</code> setinggi minimal 44px.',
     'test': f"{RULES}.some(r=>r.selectorText&&r.selectorText.includes('.btn:focus-visible')&&parseFloat(r.style.outlineWidth||r.style.outline.match(/\\d+/)?.[0]||0)>=2)&&parseFloat({G.format('.btn')}.height)>=44",
     'hint': '.btn:focus-visible { outline: 3px solid var(--warna-aksen); outline-offset: 2px }'},
    ['Lengkapi hover, fokus, aktif, nonaktif.', 'Overlay hasil di atas desain pada 360 dan 1440 px.', 'Serah terima: tautan pratinjau, catatan perbedaan, review desainer.'],
    [q('Alat untuk memeriksa pixel-perfect?', ['Overlay tangkapan layar di atas desain', 'Menebak dengan mata', 'Hanya Lighthouse'], 0, 'Perbedaan langsung terlihat.'),
     q('Kenapa memakai :focus-visible, bukan menghapus outline?', ['Pengguna keyboard harus tahu posisi fokus', 'Agar lebih cantik', 'Wajib oleh Figma'], 0, 'WCAG 2.4.7 Focus Visible.')],
    {'css': STATE}),
  W('Hasil akhir dan checklist serah terima',
    ['Inilah hasil slicing lengkap: token, HTML semantik, layout mobile-first, komponen kartu, breakpoint 768 px, serta state fokus. Ubah lebar pratinjau (di layar lebar) untuk melihat perubahan layout, dan tekan Tab untuk melihat fokus keyboard.',
     'Bandingkan dengan papan desain di pelajaran pertama. Perbedaan yang tersisa harus disengaja dan dicatat, misalnya state hover yang ditambahkan karena tidak ada di file desain.',
     'Pakai checklist di bawah setiap kali menyerahkan hasil slicing. Checklist ini mencakup standar yang biasa diperiksa reviewer di agensi dan tim produk.'],
    HALAMAN, css=FINAL_CSS,
    pts=['Token, semantik, mobile-first, komponen, breakpoint, state.', 'Perbedaan dengan desain harus disengaja dan dicatat.', 'Pakai checklist yang sama setiap proyek.'],
    qs=[q('Yang wajib ada saat menyerahkan hasil slicing?', ['Tautan pratinjau dan catatan perbedaan', 'Hanya file ZIP', 'Tangkapan layar desktop saja'], 0, 'Desainer bisa meninjau langsung.')]),
]),
]
SLW_KASUS[0]['lessons'][-1]['tb'] = [{'c': 'Checklist serah terima slicing', 'h': ['Area', 'Kriteria lulus'], 'r': [
    ['Kesetiaan desain', 'Overlay 360 dan 1440 px: jarak, font, warna sesuai; perbedaan dicatat'],
    ['Responsif', 'Tidak ada scroll horizontal dari 320 sampai 1920 px'], ['Semantik', 'Landmark lengkap, satu h1, heading runtut'],
    ['Aksesibilitas', 'Kontras AA, fokus terlihat, label input, alt gambar, target 44 px'], ['Performa', 'Gambar WebP berukuran pas, lazy di bawah layar, Lighthouse 90+'],
    ['Kode', 'Token dipakai, tanpa angka ajaib, kelas konsisten, lolos validator'], ['Serah terima', 'Tautan pratinjau, catatan, PR siap direview']]}]


# ===================================================================
#  Desain contoh mobile: layar Masuk aplikasi Kopi Kita
# ===================================================================
LOGIN_HTML = '''<div class="papan">
  <p class="label">Frame · Android 360 × 800 dp · Masuk (Ready for dev)</p>
  <div class="hp">
    <div class="status"><span>09.41</span><span>▲ ◼ 87%</span></div>
    <div class="isi">
      <div class="logo">KK</div>
      <h1>Masuk</h1>
      <p class="sub">Pesan kopi favoritmu lebih cepat.</p>
      <label>Email<span class="in">rina@contoh.id</span></label>
      <label>Kata sandi<span class="in">••••••••<b>👁</b></span></label>
      <p class="lupa">Lupa kata sandi?</p>
      <span class="btn">Masuk</span>
      <p class="atau">atau</p>
      <span class="btn garis">Lanjut dengan Google</span>
      <p class="daftar">Belum punya akun? <b>Daftar</b></p>
    </div>
    <span class="rl" style="top:118px;left:0;width:24px" data-v="24"></span>
    <span class="tag" style="top:150px;right:4px">Judul 24/32 sp · Bold</span>
    <span class="tag" style="top:214px;right:4px">Input 56 dp · r12</span>
    <span class="tag" style="top:356px;right:4px">Tombol 48 dp · r12</span>
    <span class="rl v" style="top:282px;left:60px;height:16px" data-v="16"></span>
  </div>
  <p class="label">Token</p>
  <table class="spek"><tr><th>Token</th><th>Nilai</th><th>Flutter</th><th>Compose</th></tr>
    <tr><td>primary</td><td>#8A4B2A</td><td>colorScheme.primary</td><td>MaterialTheme.colorScheme.primary</td></tr>
    <tr><td>surface</td><td>#FBF7F2</td><td>colorScheme.surface</td><td>colorScheme.surface</td></tr>
    <tr><td>Judul</td><td>24/32 sp bold</td><td>textTheme.headlineSmall</td><td>typography.headlineSmall</td></tr>
    <tr><td>Margin layar</td><td>24 dp</td><td>EdgeInsets.all(24)</td><td>padding(24.dp)</td></tr>
    <tr><td>Jarak antar field</td><td>16 dp</td><td>SizedBox(height: 16)</td><td>Spacer(Modifier.height(16.dp))</td></tr></table>
</div>'''
LOGIN_CSS = '''body { margin: 0; background: #2C2C2C; font-family: system-ui, sans-serif; }
.papan { padding: 16px; color: #EDEDED; }
.label { font-size: 12px; color: #B5B5B5; margin: 16px 0 8px; }
.hp { position: relative; width: 300px; max-width: 100%; background: #FBF7F2; color: #2B2724; border-radius: 24px; overflow: hidden; box-shadow: 0 0 0 1px #4A90E2; }
.status { display: flex; justify-content: space-between; font-size: 11px; padding: 8px 20px; }
.isi { padding: 16px 20px 24px; display: grid; gap: 10px; }
.logo { width: 48px; height: 48px; border-radius: 12px; background: #8A4B2A; color: #fff; display: grid; place-items: center; font-weight: 800; }
h1 { margin: 6px 0 0; font-size: 22px; }
.sub { margin: 0; color: #6B625B; font-size: 13px; }
label { display: grid; gap: 4px; font-size: 12px; font-weight: 600; }
.in { display: flex; justify-content: space-between; height: 44px; align-items: center; padding: 0 12px; border: 1px solid #C9BBAE; border-radius: 12px; font-weight: 400; font-size: 14px; background: #fff; }
.in b { font-weight: 400; }
.lupa { margin: 0; text-align: right; font-size: 12px; color: #8A4B2A; font-weight: 600; }
.btn { display: grid; place-items: center; height: 40px; border-radius: 12px; background: #8A4B2A; color: #fff; font-weight: 700; font-size: 14px; }
.btn.garis { background: #fff; color: #2B2724; border: 1px solid #C9BBAE; }
.atau { margin: 0; text-align: center; font-size: 12px; color: #6B625B; }
.daftar { margin: 4px 0 0; text-align: center; font-size: 12px; }
.daftar b { color: #8A4B2A; }
.rl { position: absolute; border-top: 1px solid #F24E1E; }
.rl.v { border-top: 0; border-left: 1px solid #F24E1E; }
.rl::after { content: attr(data-v); position: absolute; background: #F24E1E; color: #fff; font: 600 10px/1 system-ui; padding: 2px 4px; border-radius: 3px; top: -8px; left: 4px; }
.tag { position: absolute; background: #7B61FF; color: #fff; font: 600 10px/1 system-ui; padding: 3px 6px; border-radius: 3px; }
.spek { border-collapse: collapse; font-size: 11px; color: #EDEDED; display: block; overflow-x: auto; }
.spek td, .spek th { border: 1px solid #555; padding: 4px 6px; text-align: left; white-space: nowrap; }
'''

SLM_KASUS = [
M('Studi kasus: slicing layar Masuk step by step', 'Menengah',
  'Satu desain layar Masuk aplikasi "Kopi Kita" di-slicing ke Flutter dan Jetpack Compose mengikuti alur standar industri: membaca spesifikasi, token menjadi tema, kerangka layar, komponen, state dan validasi, adaptif, lalu QA dan serah terima.',
  ['Design handoff', 'dp and sp', 'Theme', 'Scaffold', 'TextField', 'Validation', 'Adaptive layout', 'Golden test'], [
  W('Contoh desain: layar Masuk',
    ['Pratinjau menampilkan tiruan frame <b>Figma</b> untuk layar Masuk aplikasi Android: margin layar 24 dp, judul 24/32 sp tebal, input setinggi 56 dp dengan radius 12, jarak antar field 16 dp, dan tombol utama 48 dp. Tabel token di bawahnya sudah memetakan setiap nilai ke Flutter dan Compose.',
     'Ingat satuan mobile: <b>dp</b> (density-independent pixel) untuk ukuran dan jarak, <b>sp</b> untuk teks agar ikut membesar saat pengguna memperbesar huruf di pengaturan. 1 px di Figma pada frame 360 sama dengan 1 dp.',
     'Ada hal yang tidak terlihat di gambar statis tetapi tetap harus dibuat: keyboard yang menutupi form, pesan error, tombol saat memuat, tampilan kata sandi, mode gelap, dan layar kecil atau tablet. Langkah-langkah berikut menanganinya satu per satu.'],
    LOGIN_HTML, css=LOGIN_CSS,
    pts=['dp untuk ukuran, sp untuk teks.', 'Token desain dipetakan ke tema Flutter dan Compose.', 'Rencanakan state yang tidak terlihat di desain.'],
    qs=[q('Satuan untuk ukuran teks di Android?', ['sp', 'dp', 'px'], 0, 'Ikut pengaturan ukuran huruf pengguna.')]),
  C('Langkah 1: membaca spesifikasi dan memecah layar',
    ['Pecah layar dari atas ke bawah menjadi blok: status bar dan safe area, logo, judul dan subjudul, field email, field kata sandi dengan ikon mata, tautan lupa, tombol Masuk, pemisah "atau", tombol Google, dan tautan daftar.',
     'Catat untuk setiap blok: ukuran, jarak ke blok sebelumnya, gaya teks, dan <b>perilaku</b>. Contoh: field email memakai keyboard email dan tombol Next; field kata sandi memakai tombol Done yang langsung menekan Masuk.',
     'Tentukan juga apa yang terjadi saat keyboard muncul: isi harus bisa di-scroll agar tombol Masuk tidak tertutup.'],
    "Masuk (360 × 800 dp)\n├─ SafeArea, padding 24\n├─ Logo 48 × 48, r12              jarak bawah 24\n├─ Judul \"Masuk\" headlineSmall      jarak bawah 4\n├─ Subjudul bodyMedium, onSurfaceVariant   jarak bawah 32\n├─ TextField Email (56, r12)       keyboard email, aksi Next   jarak 16\n├─ TextField Kata sandi (56, r12)  ikon mata, aksi Done        jarak 8\n├─ \"Lupa kata sandi?\" rata kanan, TextButton                   jarak 24\n├─ Tombol Masuk FilledButton 48, lebar penuh                   jarak 16\n├─ Pemisah \"atau\"                                              jarak 16\n├─ OutlinedButton Google 48, lebar penuh                       jarak 24\n└─ \"Belum punya akun? Daftar\" rata tengah\n\nState: default · fokus · error per field · memuat (tombol nonaktif + spinner) · gagal (snackbar)",
    None, 'text',
    pts=['Pecah layar menjadi blok dari atas ke bawah.', 'Catat ukuran, jarak, gaya, dan perilaku keyboard.', 'Daftar state sebelum coding.'],
    qs=[q('Aksi keyboard yang tepat untuk field kata sandi terakhir?', ['Done, lalu langsung menekan Masuk', 'Next', 'Search'], 0, 'Menghemat satu ketukan.')]),
  C('Langkah 2: token menjadi tema',
    ['Jangan menulis warna dan ukuran teks langsung di setiap widget. Masukkan token ke <b>tema</b>: <code>ThemeData</code> dengan <code>ColorScheme.fromSeed</code> di Flutter, atau <code>MaterialTheme</code> dengan <code>lightColorScheme</code> di Compose. Bentuk input dan tombol (radius 12) juga diatur sekali di tema.',
     'Dengan tema, mode gelap tinggal menambah skema gelap, dan semua komponen Material 3 otomatis mengikuti.',
     'Kode di bawah memakai Flutter. Versi Compose ada di soal latihan.'],
    "final temaKopi = ThemeData(\n  useMaterial3: true,\n  colorScheme: ColorScheme.fromSeed(\n    seedColor: const Color(0xFF8A4B2A),\n    primary: const Color(0xFF8A4B2A),\n    surface: const Color(0xFFFBF7F2),\n  ),\n  textTheme: const TextTheme(\n    headlineSmall: TextStyle(fontSize: 24, height: 32 / 24, fontWeight: FontWeight.w700),\n  ),\n  inputDecorationTheme: InputDecorationTheme(\n    filled: true,\n    fillColor: Colors.white,\n    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),\n  ),\n  filledButtonTheme: FilledButtonThemeData(\n    style: FilledButton.styleFrom(\n      minimumSize: const Size.fromHeight(48),\n      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),\n    ),\n  ),\n);\n\n// MaterialApp(theme: temaKopi, darkTheme: temaKopiGelap, home: const LayarMasuk())",
    None, 'dart',
    pts=['Token masuk ke tema, bukan ke setiap widget.', 'Bentuk input dan tombol diatur sekali.', 'Mode gelap cukup skema kedua.'],
    qs=[q('Keuntungan mengatur radius tombol di tema?', ['Semua tombol konsisten tanpa diulang', 'Aplikasi lebih kecil', 'Wajib di Material 3'], 0, 'Satu sumber kebenaran.')],
    so=[K('Tulis tema Compose dengan primary #8A4B2A, surface #FBF7F2, dan headlineSmall 24/32 sp bold.', 'lightColorScheme dan Typography.',
          "private val Skema = lightColorScheme(\n    primary = Color(0xFF8A4B2A),\n    surface = Color(0xFFFBF7F2),\n)\nprivate val Huruf = Typography(\n    headlineSmall = TextStyle(fontSize = 24.sp, lineHeight = 32.sp, fontWeight = FontWeight.Bold),\n)\n\n@Composable\nfun TemaKopi(isi: @Composable () -> Unit) =\n    MaterialTheme(colorScheme = Skema, typography = Huruf, shapes = Shapes(medium = RoundedCornerShape(12.dp)), content = isi)")]),
  C('Langkah 3: kerangka layar, safe area, dan scroll',
    ['Bungkus layar dengan <code>Scaffold</code> dan <b>safe area</b> agar tidak tertimpa status bar atau notch. Isi diletakkan dalam kolom yang bisa di-<b>scroll</b>, supaya saat keyboard muncul pengguna tetap bisa mencapai tombol Masuk.',
     'Pakai padding 24 dp dari token. Batasi lebar maksimum isi (misalnya 480 dp) dan letakkan di tengah agar di tablet form tidak melebar sepanjang layar.',
     'Kerangka Compose padanannya: <code>Scaffold</code> + <code>Column(Modifier.verticalScroll(rememberScrollState()).imePadding().padding(24.dp).widthIn(max = 480.dp))</code>.'],
    "class LayarMasuk extends StatelessWidget {\n  const LayarMasuk({super.key});\n\n  @override\n  Widget build(BuildContext context) {\n    final t = Theme.of(context).textTheme;\n    return Scaffold(\n      body: SafeArea(\n        child: Center(\n          child: SingleChildScrollView(\n            padding: const EdgeInsets.all(24),\n            child: ConstrainedBox(\n              constraints: const BoxConstraints(maxWidth: 480),\n              child: Column(\n                crossAxisAlignment: CrossAxisAlignment.stretch,\n                children: [\n                  const Align(alignment: Alignment.centerLeft, child: LogoKopi(ukuran: 48)),\n                  const SizedBox(height: 24),\n                  Text('Masuk', style: t.headlineSmall),\n                  const SizedBox(height: 4),\n                  Text('Pesan kopi favoritmu lebih cepat.', style: t.bodyMedium),\n                  const SizedBox(height: 32),\n                  const FormMasuk(),\n                ],\n              ),\n            ),\n          ),\n        ),\n      ),\n    );\n  }\n}",
    None, 'dart',
    pts=['Scaffold + SafeArea.', 'Isi bisa di-scroll agar tidak tertutup keyboard.', 'Lebar maksimum 480 dp untuk tablet.'],
    qs=[q('Kenapa isi layar Masuk dibungkus scroll?', ['Agar tombol tetap terjangkau saat keyboard muncul', 'Agar lebih cepat', 'Wajib di semua layar'], 0, 'Keyboard memakan separuh layar.')]),
  C('Langkah 4: komponen form sesuai spesifikasi',
    ['Buat field email dan kata sandi dengan <code>TextFormField</code> (Flutter) atau <code>OutlinedTextField</code> (Compose). Lengkapi atribut yang tidak terlihat di desain tetapi penting: <code>keyboardType</code>, <code>textInputAction</code>, <code>autofillHints</code> (agar password manager bekerja), dan ikon untuk menampilkan kata sandi.',
     'Jarak antar elemen mengikuti redline (16, 8, 24 dp). Tombol utama memakai FilledButton lebar penuh setinggi 48 dp dari tema; tombol Google memakai OutlinedButton.',
     'Label teks yang dibaca pembaca layar (TalkBack) harus jelas: ikon mata perlu <code>tooltip</code> atau contentDescription "Tampilkan kata sandi".'],
    "class FormMasuk extends StatefulWidget {\n  const FormMasuk({super.key});\n  @override\n  State<FormMasuk> createState() => _FormMasukState();\n}\n\nclass _FormMasukState extends State<FormMasuk> {\n  bool sembunyi = true;\n\n  @override\n  Widget build(BuildContext context) {\n    return AutofillGroup(\n      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [\n        const TextField(\n          keyboardType: TextInputType.emailAddress,\n          textInputAction: TextInputAction.next,\n          autofillHints: [AutofillHints.email],\n          decoration: InputDecoration(labelText: 'Email'),\n        ),\n        const SizedBox(height: 16),\n        TextField(\n          obscureText: sembunyi,\n          textInputAction: TextInputAction.done,\n          autofillHints: const [AutofillHints.password],\n          decoration: InputDecoration(\n            labelText: 'Kata sandi',\n            suffixIcon: IconButton(\n              tooltip: sembunyi ? 'Tampilkan kata sandi' : 'Sembunyikan kata sandi',\n              icon: Icon(sembunyi ? Icons.visibility : Icons.visibility_off),\n              onPressed: () => setState(() => sembunyi = !sembunyi),\n            ),\n          ),\n        ),\n        const SizedBox(height: 8),\n        Align(alignment: Alignment.centerRight,\n            child: TextButton(onPressed: () {}, child: const Text('Lupa kata sandi?'))),\n        const SizedBox(height: 24),\n        FilledButton(onPressed: () {}, child: const Text('Masuk')),\n        const SizedBox(height: 16),\n        const Text('atau', textAlign: TextAlign.center),\n        const SizedBox(height: 16),\n        OutlinedButton(onPressed: () {}, child: const Text('Lanjut dengan Google')),\n      ]),\n    );\n  }\n}",
    None, 'dart',
    pts=['keyboardType, textInputAction, autofillHints.', 'Jarak sesuai redline, ukuran dari tema.', 'Tooltip untuk ikon agar terbaca TalkBack.'],
    qs=[q('Atribut yang membuat password manager bisa mengisi form?', ['autofillHints', 'obscureText', 'keyboardType'], 0, 'Membantu juga aksesibilitas (WCAG 3.3.8).')],
    so=[K('Tulis field kata sandi Compose dengan ikon mata untuk menampilkan atau menyembunyikan, tinggi minimal 56 dp.', 'OutlinedTextField + visualTransformation + trailingIcon.',
          "var sandi by remember { mutableStateOf(\"\") }\nvar lihat by remember { mutableStateOf(false) }\nOutlinedTextField(\n    value = sandi,\n    onValueChange = { sandi = it },\n    label = { Text(\"Kata sandi\") },\n    singleLine = true,\n    visualTransformation = if (lihat) VisualTransformation.None else PasswordVisualTransformation(),\n    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Password, imeAction = ImeAction.Done),\n    trailingIcon = {\n        IconButton(onClick = { lihat = !lihat }) {\n            Icon(if (lihat) Icons.Default.VisibilityOff else Icons.Default.Visibility,\n                 contentDescription = if (lihat) \"Sembunyikan kata sandi\" else \"Tampilkan kata sandi\")\n        }\n    },\n    shape = RoundedCornerShape(12.dp),\n    modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp),\n)")]),
  C('Langkah 5: state, validasi, dan memuat',
    ['Desain biasanya hanya menampilkan keadaan normal. Slicer melengkapi <b>state</b>: pesan error di bawah field yang salah, tombol nonaktif dan spinner saat memuat agar tidak ditekan dua kali, serta snackbar jika server gagal.',
     'Validasi saat pengguna menekan Masuk, lalu validasi ulang per field setelah pengguna memperbaikinya. Tulis pesan yang menjelaskan cara memperbaiki: "Format email belum benar, contoh: nama@contoh.id", bukan "Input tidak valid".',
     'Di Compose, simpan state di ViewModel sebagai <code>StateFlow</code> berisi data class <code>UiMasuk(email, sandi, errorEmail, memuat)</code>.'],
    "Future<void> masuk() async {\n  final valid = _form.currentState!.validate();\n  if (!valid) return;\n  setState(() => memuat = true);\n  try {\n    await auth.masuk(email.text.trim(), sandi.text);\n    if (mounted) context.go('/beranda');\n  } on AuthGagal {\n    if (mounted) {\n      ScaffoldMessenger.of(context).showSnackBar(\n        const SnackBar(content: Text('Email atau kata sandi salah')),\n      );\n    }\n  } finally {\n    if (mounted) setState(() => memuat = false);\n  }\n}\n\nString? cekEmail(String? v) =>\n    (v == null || !RegExp(r'^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$').hasMatch(v.trim()))\n        ? 'Format email belum benar, contoh: nama@contoh.id'\n        : null;\n\n// tombol: nonaktif + spinner saat memuat\nFilledButton(\n  onPressed: memuat ? null : masuk,\n  child: memuat\n      ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2))\n      : const Text('Masuk'),\n)",
    None, 'dart',
    pts=['Lengkapi state error, memuat, gagal.', 'Pesan error menjelaskan cara memperbaiki.', 'Nonaktifkan tombol saat memuat.'],
    qs=[q('Kenapa tombol Masuk dinonaktifkan saat memuat?', ['Mencegah permintaan ganda', 'Agar warna berubah', 'Aturan Material'], 0, 'Ketukan ganda mengirim dua permintaan.')]),
  C('Langkah 6: QA dengan desain dan serah terima',
    ['Bandingkan hasil dengan desain di <b>perangkat nyata</b> atau emulator 360 × 800 dp. Ambil tangkapan layar dan tumpuk di atas frame Figma (opacity 50%). Periksa jarak, ukuran teks, warna, dan radius.',
     'Uji kasus yang tidak ada di desain: ukuran huruf sistem 200%, layar kecil 320 dp, tablet, mode gelap, orientasi lanskap, TalkBack, dan keyboard terbuka. Kunci tampilan dengan <b>golden test</b> (Flutter) atau <b>screenshot test</b> seperti Roborazzi atau Paparazzi (Compose) agar perubahan tak sengaja langsung ketahuan.',
     'Serah terima: rekaman layar alur Masuk, tangkapan layar setiap state, daftar perbedaan yang disengaja, dan build uji (Firebase App Distribution atau internal testing Play).'],
    "testWidgets('layar Masuk sesuai desain', (tester) async {\n  tester.view.physicalSize = const Size(1080, 2400);   // 360 × 800 dp pada 3x\n  tester.view.devicePixelRatio = 3;\n  await tester.pumpWidget(MaterialApp(theme: temaKopi, home: const LayarMasuk()));\n  await expectLater(find.byType(LayarMasuk), matchesGoldenFile('goldens/masuk_360.png'));\n});\n\n// perbarui golden setelah desain disetujui:\n// flutter test --update-goldens",
    None, 'dart',
    tb=[{'c': 'Checklist QA slicing mobile', 'h': ['Uji', 'Lulus jika'], 'r': [
      ['Overlay 360 × 800', 'Jarak, teks, warna, radius sesuai desain'], ['Huruf 200%', 'Teks tidak terpotong, layar bisa di-scroll'],
      ['Layar 320 dp dan tablet', 'Tidak ada overflow, form maksimal 480 dp'], ['Mode gelap', 'Kontras tetap AA'],
      ['TalkBack', 'Semua tombol dan ikon terbaca jelas'], ['Keyboard terbuka', 'Tombol Masuk tetap bisa dicapai'], ['Golden test', 'Lulus di CI']]}],
    pts=['Overlay dengan frame Figma di 360 × 800 dp.', 'Uji huruf besar, layar kecil, tablet, gelap, TalkBack.', 'Golden atau screenshot test untuk mengunci tampilan.'],
    qs=[q('Alat Flutter untuk mengunci tampilan layar dari perubahan tak sengaja?', ['Golden test', 'Hot reload', 'pub get'], 0, 'Membandingkan gambar piksel.')]),
]),
]


# ===================================================================
#  UI Design: proyek desain step by step + portofolio
# ===================================================================
WIRE_HTML = '''<div class="layar">
  <div class="kotak judul">Logo · Lokasi outlet ▾</div>
  <div class="kotak cari">🔍 Cari menu</div>
  <div class="kotak banner">Banner promo</div>
  <div class="baris"><div class="kotak chip">Kopi</div><div class="kotak chip">Non-kopi</div><div class="kotak chip">Roti</div></div>
  <div class="kotak item">[foto] Nama menu · harga · (+)</div>
  <div class="kotak item">[foto] Nama menu · harga · (+)</div>
  <div class="kotak item">[foto] Nama menu · harga · (+)</div>
  <div class="kotak bar">Keranjang (2) · Rp36.000 · Bayar</div>
</div>'''
WIRE_CSS = '''body { margin: 0; padding: 16px; background: #EEE; font: 13px/1.4 ui-monospace, monospace; color: #444; }
.layar { width: 300px; max-width: 100%; background: #fff; padding: 12px; display: grid; gap: 8px; border: 2px solid #999; border-radius: 16px; }
.kotak { border: 1.5px dashed #888; border-radius: 6px; padding: 10px; background: #F7F7F7; }
.baris { display: flex; gap: 8px; }
.banner { height: 70px; }
'''

UI_PROYEK = [
M('Proyek: mendesain aplikasi step by step', 'Menengah',
  'Mendesain aplikasi pemesanan kopi dari brief sampai handoff mengikuti proses standar industri: brief, riset, user flow, wireframe, style guide, komponen, desain hi-fi dan state, prototipe dan uji, lalu handoff.',
  ['Design brief', 'Competitive analysis', 'User flow', 'Wireframe', 'Style guide', 'Components', 'High fidelity', 'Prototype', 'Usability testing', 'Handoff'], [
  C('Langkah 1: brief, masalah, dan target',
    ['Setiap proyek desain dimulai dari <b>brief</b>, bukan dari Figma. Brief menjawab: siapa penggunanya, masalah apa yang diselesaikan, apa tujuan bisnisnya, bagaimana keberhasilan diukur, apa batasannya (waktu, platform, brand), dan apa yang <b>tidak</b> dikerjakan.',
     'Tulis <b>problem statement</b> dengan pola: "[Pengguna] kesulitan [melakukan apa] karena [penyebab], sehingga [dampak]." Lalu tetapkan metrik, misalnya waktu memesan dan persentase pesanan yang selesai.',
     'Proyek di modul ini: aplikasi pemesanan kopi "Kopi Kita" untuk pekerja kantoran yang ingin memesan sebelum tiba di outlet. Simpan brief ini; isinya akan menjadi bab pembuka studi kasus portofoliomu.'],
    "BRIEF · Aplikasi pemesanan Kopi Kita\n\nPengguna     : pekerja kantoran 22-35 th di Medan, memesan 3-5 kali seminggu\nMasalah      : antre 10-15 menit di jam 07.30-08.30 karena memesan dan membayar di kasir\nProblem statement:\n  Pekerja kantoran kesulitan membeli kopi sebelum masuk kerja karena antrean\n  panjang di kasir, sehingga terlambat atau batal membeli.\nTujuan bisnis: 30% pesanan pagi lewat aplikasi dalam 3 bulan\nMetrik       : waktu pesan < 60 detik, tingkat selesai checkout > 80%, SUS > 75\nPlatform     : Android dulu (78% pengguna), lalu iOS\nBatasan      : 6 minggu, brand sudah ada (coklat kopi + krem), bayar QRIS dan e-wallet\nDi luar lingkup: program poin, pengantaran",
    None, 'text',
    pts=['Mulai dari brief, bukan dari Figma.', 'Problem statement + metrik keberhasilan.', 'Tulis juga apa yang di luar lingkup.'],
    qs=[q('Isi brief yang paling sering terlupa?', ['Metrik keberhasilan dan hal di luar lingkup', 'Warna favorit klien', 'Nama file Figma'], 0, 'Tanpa metrik, desain tidak bisa dinilai.')],
    so=[T('Tulis problem statement untuk aplikasi antrean puskesmas.', 'Pola: pengguna, kesulitan, penyebab, dampak.',
          'Pasien lansia kesulitan mendapatkan nomor antrean puskesmas karena harus datang sebelum subuh, sehingga banyak yang kelelahan atau batal berobat.')]),
  C('Langkah 2: riset cepat, benchmark, dan moodboard',
    ['Lakukan riset seperlunya: <b>wawancara</b> 5 pengguna (cukup untuk menemukan pola utama), <b>benchmark</b> 3 sampai 5 aplikasi sejenis (Fore, Kopi Kenangan, Starbucks, GoFood), dan catat pola yang sudah dikenal pengguna. Jangan menyalin; ambil pelajaran.',
     'Rangkum menjadi <b>insight</b> yang bisa ditindaklanjuti, misalnya "Pengguna memesan menu yang sama hampir setiap hari" → sediakan "Pesan lagi" di beranda.',
     'Buat <b>moodboard</b>: kumpulan foto, palet, tipografi, dan contoh UI yang mewakili suasana brand (hangat, cepat, ramah). Moodboard menyamakan selera tim dan klien sebelum detail visual dibuat.'],
    "BENCHMARK (aplikasi kopi)\n| Aplikasi   | Yang bagus                        | Yang kurang                  |\n|------------|-----------------------------------|------------------------------|\n| A          | Pesan lagi 1 ketukan di beranda   | Banner promo menutupi menu   |\n| B          | Pilih outlet otomatis via lokasi  | Kustomisasi menu 4 layar     |\n| C          | Estimasi siap diambil (menit)     | Checkout wajib daftar dulu   |\n\nINSIGHT\n1. 4 dari 5 pengguna memesan menu yang sama setiap pagi  -> fitur Pesan lagi\n2. Pengguna ingin tahu kapan pesanan siap               -> estimasi waktu jelas\n3. Gula dan es paling sering diubah                      -> kustomisasi 1 layar",
    None, 'text',
    pts=['Wawancara 5 pengguna, benchmark 3 sampai 5 aplikasi.', 'Ubah temuan menjadi insight yang bisa ditindaklanjuti.', 'Moodboard menyamakan selera sebelum detail visual.'],
    qs=[q('Tujuan benchmark yang benar?', ['Belajar pola dan celah, bukan menyalin', 'Menyalin aplikasi terlaris', 'Mencari logo'], 0, 'Ambil pelajaran.')]),
  W('Langkah 3: user flow dan wireframe',
    ['<b>User flow</b> menggambarkan langkah pengguna mencapai tujuan: Buka aplikasi → pilih outlet → pilih menu → atur gula dan es → keranjang → bayar QRIS → lihat estimasi siap. Tandai titik keputusan dan kondisi error (outlet tutup, stok habis, bayar gagal).',
     '<b>Wireframe</b> adalah kerangka hitam putih yang membahas <b>struktur dan prioritas</b>, bukan warna. Pratinjau menampilkan wireframe beranda: lokasi outlet di atas, pencarian, banner, kategori, daftar menu dengan tombol tambah, dan bar keranjang menempel di bawah (zona jempol).',
     'Buat 2 sampai 3 alternatif wireframe dan uji cepat dengan rekan sebelum memilih satu. Mengubah kotak abu-abu jauh lebih murah daripada mengubah desain hi-fi.'],
    WIRE_HTML, css=WIRE_CSS,
    pts=['User flow: langkah, keputusan, error.', 'Wireframe membahas struktur, bukan warna.', 'Buat beberapa alternatif sebelum memilih.'],
    qs=[q('Kenapa bar keranjang diletakkan di bawah?', ['Mudah dijangkau jempol (Fitts\'s Law)', 'Agar terlihat modern', 'Aturan Android'], 0, 'Aksi utama di zona jempol.')]),
  L('Langkah 4: style guide (warna, tipografi, jarak)',
    ['Setelah struktur disetujui, tetapkan <b>style guide</b>: palet warna semantik (primer, permukaan, teks, sukses, peringatan, error), skala tipografi (misalnya 12, 14, 16, 20, 24, 32 dengan rasio sekitar 1,25), grid 8 poin, radius, dan bayangan. Simpan sebagai <b>variables</b> dan <b>text styles</b> di Figma.',
     'Setiap pasangan teks dan latar wajib lolos kontras WCAG AA: 4,5:1 untuk teks biasa, 3:1 untuk teks besar dan komponen. Periksa dengan plugin Stark atau situs WebAIM Contrast Checker.',
     'Pratinjau adalah halaman style guide. Warna teks sekunder terlalu pucat sehingga gagal kontras.'],
    '''<div class="sg">
  <h1>Kopi Kita · Style guide</h1>
  <div class="palet"><span style="--c:#8A4B2A">Primer</span><span style="--c:#FBF7F2">Permukaan</span><span style="--c:#2B2724">Teks</span><span style="--c:#1E7B4F">Sukses</span><span style="--c:#B42318">Error</span></div>
  <p class="t32">Judul 32 · Bold</p><p class="t20">Subjudul 20 · Semibold</p><p class="t16">Body 16 · Regular, line-height 1,5</p>
  <p class="sekunder">Teks sekunder 14 untuk keterangan menu</p>
</div>''',
    '''body { margin: 0; padding: 24px; font-family: system-ui, sans-serif; background: #FBF7F2; color: #2B2724; }
h1 { font-size: 20px; margin: 0 0 16px; }
.palet { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }
.palet span { width: 88px; font-size: 12px; }
.palet span::before { content: ""; display: block; height: 48px; border-radius: 8px; background: var(--c); box-shadow: inset 0 0 0 1px #0002; margin-bottom: 4px; }
p { margin: 0 0 8px; }
.t32 { font-size: 32px; font-weight: 700; } .t20 { font-size: 20px; font-weight: 600; } .t16 { font-size: 16px; }
.sekunder { font-size: 14px; color: #B8ADA3; }''',
    {'q': 'Perbaiki warna <code>.sekunder</code> agar kontrasnya terhadap latar #FBF7F2 minimal 4,5:1 (misalnya #6B625B).',
     'test': "(()=>{const L=c=>{const v=c.match(/[\\d.]+/g).slice(0,3).map(x=>{x/=255;return x<=0.03928?x/12.92:((x+0.055)/1.055)**2.4});return 0.2126*v[0]+0.7152*v[1]+0.0722*v[2]};const a=L(getComputedStyle(document.querySelector('.sekunder')).color),b=L(getComputedStyle(document.body).backgroundColor);return (Math.max(a,b)+0.05)/(Math.min(a,b)+0.05)>=4.5})()",
     'hint': '.sekunder { color: #6B625B } memberi kontras sekitar 5,8:1.'},
    ['Palet semantik, skala tipografi, grid 8, radius, bayangan.', 'Simpan sebagai variables dan text styles.', 'Semua pasangan warna lolos WCAG AA.'],
    [q('Kontras minimum teks biasa menurut WCAG AA?', ['4,5:1', '3:1', '7:1'], 0, '3:1 untuk teks besar.')],
    {'css': '.sekunder{color:#6B625B}'}),
  C('Langkah 5: komponen, varian, dan auto layout',
    ['Ubah elemen berulang menjadi <b>komponen</b> Figma: tombol, input, kartu menu, chip kategori, bar keranjang. Setiap komponen punya <b>varian</b> (primer, sekunder, teks) dan <b>properti</b> (ukuran, ikon kiri, state). Bangun dengan <b>auto layout</b> agar ukurannya mengikuti isi dan mudah dibaca developer.',
     'Wajib lengkap: state <b>default, hover, pressed, focus, disabled, loading</b> untuk tombol; <b>default, focus, filled, error, disabled</b> untuk input. Komponen yang statenya tidak lengkap akan membuat developer menebak.',
     'Beri nama layer dan komponen dengan rapi (<code>Button/Primary/Large</code>), dan pakai variables untuk warna serta jarak agar mode gelap tinggal berganti mode.'],
    "Komponen: Button\n  Properti : Varian = Primer | Sekunder | Teks\n             Ukuran = Besar (48) | Sedang (40)\n             Ikon kiri = ya | tidak\n             State = Default | Hover | Pressed | Focus | Disabled | Loading\n  Auto layout: horizontal, padding 16 x 12, gap 8, hug contents\n  Token    : fill = color/action/primary, teks = color/text/on-primary, radius = radius/md (12)\n\nKomponen: Kartu menu\n  Slot     : foto 64 x 64 r8 · nama (16 semibold) · keterangan (14) · harga (16 bold) · tombol tambah\n  Varian   : Normal | Habis (foto 50% + label 'Habis') | Di keranjang (stepper - 1 +)",
    None, 'text',
    pts=['Komponen + varian + properti.', 'State lengkap untuk setiap komponen interaktif.', 'Auto layout dan variables untuk konsistensi.'],
    qs=[q('State tombol yang paling sering lupa didesain?', ['Focus dan loading', 'Default', 'Ukuran besar'], 0, 'Developer jadi menebak.')]),
  C('Langkah 6: desain hi-fi, state layar, dan prototipe',
    ['Rangkai komponen menjadi layar <b>high fidelity</b> untuk setiap langkah user flow. Jangan hanya happy path: desain juga <b>empty state</b> (keranjang kosong), <b>loading</b> (skeleton), <b>error</b> (pembayaran gagal), <b>offline</b>, dan konten ekstrem (nama menu dua baris, harga jutaan).',
     'Hubungkan layar menjadi <b>prototipe</b> interaktif di Figma, lalu lakukan <b>usability test</b> dengan 5 pengguna. Beri tugas realistis ("Pesan es kopi susu kurang manis untuk diambil di outlet Kesawan"), amati tanpa membantu, catat di mana mereka ragu.',
     'Ukur tingkat keberhasilan tugas, waktu, dan skor SUS. Perbaiki masalah terbesar, lalu uji lagi. Catat versi sebelum dan sesudah; ini bahan terkuat portofoliomu.'],
    "HASIL USABILITY TEST (5 peserta, prototipe v1)\nTugas: pesan es kopi susu kurang manis, ambil di outlet Kesawan\n\n| Temuan                                         | Peserta | Keparahan | Perbaikan v2                       |\n|------------------------------------------------|---------|-----------|------------------------------------|\n| Tidak sadar outlet salah (default outlet lama) | 3/5     | Tinggi    | Konfirmasi outlet di keranjang     |\n| Pilihan gula tersembunyi di 'Lainnya'          | 4/5     | Tinggi    | Gula dan es tampil langsung        |\n| Tombol bayar tertutup keyboard catatan         | 2/5     | Sedang    | Catatan dipindah ke bottom sheet   |\n\nv1: berhasil 2/5, rata-rata 94 detik, SUS 61\nv2: berhasil 5/5, rata-rata 48 detik, SUS 82",
    None, 'text',
    pts=['Desain semua state, bukan hanya happy path.', 'Prototipe + usability test 5 pengguna.', 'Catat metrik sebelum dan sesudah perbaikan.'],
    qs=[q('Kenapa 5 peserta cukup untuk satu putaran usability test?', ['Sudah menemukan sebagian besar masalah utama', 'Aturan Figma', 'Lebih banyak selalu membingungkan'], 0, 'Lebih baik beberapa putaran kecil.')]),
  C('Langkah 7: handoff ke developer',
    ['<b>Handoff</b> yang baik membuat developer tidak perlu bertanya. Siapkan: halaman Figma "Ready for dev" yang rapi, style guide dan komponen yang dipakai, anotasi perilaku (validasi, animasi, scroll, batas karakter), semua state, aset yang bisa diekspor, serta <b>acceptance criteria</b>.',
     'Lakukan sesi walkthrough 30 menit dengan developer, lalu ikut <b>design QA</b>: bandingkan hasil build dengan desain di perangkat nyata dan catat perbedaan sebagai tiket.',
     'Setelah rilis, pantau metrik dari brief (waktu pesan, tingkat selesai checkout). Hasilnya menjadi bagian "Dampak" di studi kasus portofolio.'],
    "ANOTASI · Layar Keranjang\n- Stepper jumlah: minimal 1; menekan '-' saat 1 memunculkan konfirmasi hapus\n- Total diperbarui langsung, animasi angka 150 ms ease-out\n- Catatan maksimal 100 karakter, penghitung tampil setelah 80\n- Outlet berbeda dari lokasi terdekat: banner kuning 'Pastikan outlet benar'\n- Tombol Bayar menempel di bawah, di atas keyboard; nonaktif jika keranjang kosong\n\nACCEPTANCE CRITERIA\nGiven keranjang berisi 2 item\nWhen pengguna menekan '-' pada item berjumlah 1\nThen muncul dialog 'Hapus Es Kopi Susu dari keranjang?' dengan tombol Hapus dan Batal",
    None, 'text',
    pts=['Ready for dev, anotasi, state, aset, acceptance criteria.', 'Walkthrough lalu design QA.', 'Pantau metrik setelah rilis.'],
    qs=[q('Apa itu design QA?', ['Membandingkan hasil build dengan desain sebelum rilis', 'Menguji kode backend', 'Mengecek ejaan brief'], 0, 'Desainer ikut memastikan hasil setia.')]),
]),

M('Portofolio UI designer', 'Menengah',
  'Menyusun studi kasus yang meyakinkan perekrut, mendesain halaman portofolio, memilih platform, dan menghindari kesalahan umum.',
  ['Portfolio', 'Case study', 'Storytelling', 'Behance', 'Dribbble', 'Personal website'], [
  C('Struktur studi kasus yang dibaca perekrut',
    ['Perekrut rata-rata melihat portofolio hanya beberapa menit. Mereka mencari <b>cara berpikir</b>, bukan sekadar gambar cantik. Karena itu setiap proyek ditulis sebagai <b>studi kasus</b> dengan alur cerita: masalah, proses, keputusan, dan hasil.',
     'Struktur standar: (1) <b>ringkasan</b> di atas: peran, tim, durasi, alat, dan satu kalimat hasil; (2) <b>masalah dan tujuan</b>; (3) <b>riset dan insight</b>; (4) <b>proses</b>: flow, wireframe, iterasi beserta alasannya; (5) <b>solusi</b>: layar final dengan penjelasan; (6) <b>dampak</b>: angka sebelum dan sesudah; (7) <b>refleksi</b>: apa yang dipelajari dan akan dilakukan berbeda.',
     'Cukup 3 studi kasus yang kuat. Lebih baik satu proyek mendalam daripada sepuluh tangkapan layar tanpa cerita. Proyek latihan (seperti aplikasi Kopi Kita) boleh, asalkan prosesnya nyata dan jujur disebut sebagai proyek konsep.'],
    "STUDI KASUS · Kopi Kita: pesan kopi sebelum tiba\n\nRingkasan : UI/UX Designer (solo) · 6 minggu · Figma, Maze\n            Waktu pesan turun dari 94 ke 48 detik, SUS naik dari 61 ke 82.\nMasalah   : antre 10-15 menit di pagi hari membuat pekerja batal membeli\nRiset     : 5 wawancara, benchmark 3 aplikasi -> 3 insight utama\nProses    : user flow -> 3 alternatif wireframe -> style guide -> komponen\n            -> prototipe -> 2 putaran usability test\nKeputusan : 'Pesan lagi' di beranda karena 4/5 pengguna memesan menu yang sama\nSolusi    : 6 layar utama + state kosong, memuat, gagal\nDampak    : berhasil 5/5, 48 detik, SUS 82 (proyek konsep, diuji dengan prototipe)\nRefleksi  : berikutnya menguji dengan pengguna lansia dan pembaca layar",
    None, 'text',
    tb=[{'c': 'Isi studi kasus', 'h': ['Bagian', 'Isi', 'Panjang'], 'r': [
      ['Ringkasan', 'Peran, tim, durasi, alat, hasil satu kalimat', '3 sampai 5 baris'], ['Masalah', 'Problem statement, tujuan, metrik', '1 paragraf'],
      ['Riset', 'Metode dan 3 insight utama dengan bukti', '1 sampai 2 layar'], ['Proses', 'Flow, wireframe, iterasi, alasan keputusan', 'Bagian terpanjang'],
      ['Solusi', 'Layar final dengan anotasi', '3 sampai 6 gambar'], ['Dampak', 'Angka sebelum dan sesudah', 'Singkat dan jelas'], ['Refleksi', 'Pelajaran dan langkah berikutnya', '1 paragraf']]}],
    pts=['Perekrut mencari cara berpikir.', 'Ringkasan, masalah, riset, proses, solusi, dampak, refleksi.', '3 studi kasus mendalam lebih baik dari 10 gambar.'],
    qs=[q('Bagian studi kasus yang paling menunjukkan cara berpikir?', ['Proses dan alasan setiap keputusan', 'Foto profil', 'Daftar alat'], 0, 'Kenapa, bukan hanya apa.')]),
  L('Mendesain halaman portofolio',
    ['Halaman portofolio adalah proyek desain itu sendiri: hierarki jelas, tipografi rapi, cepat dimuat, dan nyaman di ponsel. Bagian utama: <b>hero</b> singkat (nama, peran, satu kalimat keahlian), <b>3 kartu studi kasus</b> dengan judul dan hasil, <b>tentang</b>, dan <b>kontak</b>.',
     'Kartu studi kasus menampilkan gambar sampul, judul berorientasi hasil ("Memangkas waktu pesan kopi 49%"), peran, dan label proyek (konsep atau nyata). Hindari judul kosong seperti "Redesign App".',
     'Pratinjau berisi kerangka halaman portofolio. Kartu proyek belum tersusun sebagai grid.'],
    '''<header class="hero"><p class="peran">UI/UX Designer · Medan</p><h1>Rina Siregar</h1><p>Merancang aplikasi yang memangkas langkah, diuji dengan pengguna nyata.</p></header>
<section class="proyek"><h2>Studi kasus</h2>
  <div class="daftar">
    <a class="kasus" href="#"><div class="sampul s1"></div><h3>Memangkas waktu pesan kopi 49%</h3><p>Kopi Kita · UI/UX · proyek konsep</p></a>
    <a class="kasus" href="#"><div class="sampul s2"></div><h3>Antrean puskesmas tanpa datang subuh</h3><p>Sehat Desa · UX research · 2025</p></a>
    <a class="kasus" href="#"><div class="sampul s3"></div><h3>Design system untuk 4 produk UMKM</h3><p>Lapak · Design system · freelance</p></a>
  </div></section>''',
    '''body { margin: 0; font-family: system-ui, sans-serif; color: #1F2328; background: #FAFAF7; }
.hero { padding: 32px 16px; } .hero h1 { font-size: 36px; margin: 4px 0 8px; } .peran { color: #8A4B2A; font-weight: 700; margin: 0; }
.proyek { padding: 0 16px 32px; }
.kasus { display: block; text-decoration: none; color: inherit; background: #fff; border-radius: 16px; padding: 12px; border: 1px solid #E5E2DA; }
.kasus h3 { font-size: 18px; margin: 12px 0 4px; } .kasus p { margin: 0; color: #5B5F66; font-size: 14px; }
.sampul { aspect-ratio: 16 / 10; border-radius: 10px; } .s1 { background: #D9C2A7; } .s2 { background: #BFD8CF; } .s3 { background: #C9CCE8; }''',
    {'q': 'Susun <code>.daftar</code> sebagai grid dengan gap minimal 16px, dan beri judul kartu <code>.kasus h3</code> tebal minimal 600.',
     'test': f"{G.format('.daftar')}.display==='grid'&&parseFloat({G.format('.daftar')}.rowGap)>=16&&{G.format('.kasus h3')}.fontWeight>=600",
     'hint': '.daftar { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)) } .kasus h3 { font-weight: 700 }'},
    ['Hero, 3 studi kasus, tentang, kontak.', 'Judul kartu berorientasi hasil.', 'Portofolio harus nyaman di ponsel.'],
    [q('Judul studi kasus yang lebih kuat?', ['Memangkas waktu pesan kopi 49%', 'Redesign App', 'Proyek 1'], 0, 'Langsung menunjukkan dampak.')],
    {'css': '.daftar{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}.kasus h3{font-weight:700}'}),
  C('Platform, presentasi, dan kesalahan umum',
    ['Platform: <b>situs pribadi</b> (Framer, Webflow, atau buatan sendiri dari jalur Slicing Website) memberi kendali penuh dan terlihat profesional; <b>Behance</b> cocok untuk studi kasus panjang; <b>Dribbble</b> untuk potongan visual; <b>LinkedIn</b> untuk ringkasan dan tautan. Siapkan juga versi PDF 10 sampai 15 halaman untuk dikirim lewat email.',
     'Presentasi visual: mockup perangkat secukupnya, latar netral, anotasi singkat di samping layar, dan konsistensi gaya antar proyek. Untuk wawancara, siapkan cerita 5 menit per proyek: masalah, keputusan tersulit, hasil.',
     'Kesalahan umum: hanya menampilkan layar akhir, menyalin redesign aplikasi terkenal tanpa riset, mengaku hasil yang tidak terukur, membagikan desain klien yang terikat NDA (samarkan atau minta izin), dan portofolio yang tidak bisa dibuka di ponsel.'],
    "CHECKLIST PORTOFOLIO SEBELUM DIKIRIM\n[ ] 3 studi kasus dengan masalah, proses, keputusan, dampak, refleksi\n[ ] Peran dan kontribusi ditulis jujur (solo atau tim, apa bagianmu)\n[ ] Proyek konsep diberi label konsep\n[ ] Angka hasil bisa dipertanggungjawabkan\n[ ] Tidak melanggar NDA klien\n[ ] Bisa dibuka cepat di ponsel, gambar dikompres\n[ ] Kontras teks lolos AA, gambar punya alt\n[ ] Tautan Figma prototipe dapat dibuka\n[ ] Kontak jelas: email dan LinkedIn\n[ ] Versi PDF 10-15 halaman",
    None, 'text',
    pts=['Situs pribadi + Behance/Dribbble + LinkedIn + PDF.', 'Siapkan cerita 5 menit per proyek.', 'Jujur soal peran, angka, dan NDA.'],
    qs=[q('Apa yang harus dilakukan terhadap desain klien yang terikat NDA?', ['Minta izin atau samarkan detail', 'Tetap dibagikan utuh', 'Dihapus dari CV'], 0, 'Melanggar NDA merusak reputasi.')]),
]),
]


# ===================================================================
#  UX Design: design system dunia nyata + portofolio UX
# ===================================================================
UX_DS = [
M('Design system dunia nyata', 'Menengah',
  'Mempelajari design system yang dipakai perusahaan besar (Google Material 3, Apple HIG, Microsoft Fluent, IBM Carbon, Atlassian, Shopify Polaris), cara memakainya lewat CDN dan paket, design token, serta cara memilih dan mengadaptasinya.',
  ['Design systems', 'Material Design 3', 'Human Interface Guidelines', 'Fluent', 'Carbon', 'Polaris', 'Design tokens', 'CDN'], [
  C('Apa itu design system dan kenapa penting untuk UX',
    ['<b>Design system</b> adalah sumber kebenaran tunggal sebuah produk: prinsip desain, token (warna, tipografi, jarak), komponen beserta kode, pola interaksi, panduan konten, dan aturan aksesibilitas. Bukan sekadar UI kit di Figma.',
     'Untuk UX, design system memberi <b>konsistensi</b> (pengguna belajar sekali, bisa dipakai di semua layar), <b>kecepatan</b> (tim tidak mendesain ulang tombol), dan <b>kualitas bawaan</b> (komponen sudah lolos uji aksesibilitas dan usability).',
     'Ada tiga lapisan token yang umum: <b>primitive</b> (<code>coklat-600 = #8A4B2A</code>), <b>semantic</b> (<code>color.action.primary</code>), dan <b>component</b> (<code>button.primary.background</code>). Format pertukarannya kini distandarkan oleh W3C Design Tokens Community Group (DTCG).'],
    "{\n  \"color\": {\n    \"coklat\": { \"600\": { \"$type\": \"color\", \"$value\": \"#8A4B2A\" } },\n    \"action\": {\n      \"primary\": { \"$type\": \"color\", \"$value\": \"{color.coklat.600}\" }\n    }\n  },\n  \"button\": {\n    \"primary\": {\n      \"background\": { \"$type\": \"color\", \"$value\": \"{color.action.primary}\" }\n    }\n  },\n  \"radius\": { \"md\": { \"$type\": \"dimension\", \"$value\": \"12px\" } }\n}",
    None, 'json',
    pts=['Design system = prinsip, token, komponen, pola, konten, aksesibilitas.', 'Konsistensi, kecepatan, kualitas bawaan.', 'Token tiga lapis: primitive, semantic, component.'],
    qs=[q('Token yang sebaiknya dipakai langsung oleh komponen?', ['Semantic atau component', 'Primitive', 'Kode hex langsung'], 0, 'Agar tema bisa diganti.')]),
  C('Material Design 3, Apple HIG, dan design system besar lainnya',
    ['<b>Material Design 3</b> (Google) dipakai di Android dan banyak aplikasi web: dynamic color dari wallpaper, skala tipografi (display, headline, title, body, label), komponen lengkap, dan versi Expressive dengan motion berbasis fisika. Dokumentasi: m3.material.io.',
     '<b>Apple Human Interface Guidelines</b> mengatur aplikasi iOS, iPadOS, dan macOS: navigasi tab bar, Dynamic Type, SF Symbols, area sentuh 44 pt, dan material Liquid Glass. Ikuti konvensi platform agar pengguna iPhone merasa familier.',
     'Design system terbuka lain yang layak dipelajari: <b>Microsoft Fluent 2</b>, <b>IBM Carbon</b> (sangat kuat di aksesibilitas dan data), <b>Atlassian</b> (produk kolaborasi), <b>Shopify Polaris</b> (e-commerce dan panduan konten yang bagus), <b>GOV.UK</b> (layanan publik, bahasa sederhana), serta <b>Ant Design</b> (dasbor enterprise).'],
    "Pilih referensi sesuai produk:\n- Aplikasi Android            -> Material Design 3\n- Aplikasi iOS                 -> Apple HIG\n- Dasbor admin / data         -> IBM Carbon, Ant Design\n- E-commerce dan seller center -> Shopify Polaris\n- Layanan publik              -> GOV.UK Design System\n- Aplikasi kantor / Windows   -> Microsoft Fluent 2\n- Tools kolaborasi            -> Atlassian Design System",
    None, 'text',
    tb=[{'c': 'Perbandingan design system populer', 'h': ['Design system', 'Pemilik', 'Kekuatan', 'Kode'], 'r': [
      ['Material 3', 'Google', 'Dynamic color, komponen lengkap, Android', 'Jetpack Compose, Flutter, Material Web'],
      ['Human Interface Guidelines', 'Apple', 'Konvensi iOS, Dynamic Type, SF Symbols', 'SwiftUI, UIKit'],
      ['Fluent 2', 'Microsoft', 'Lintas platform Microsoft 365', 'Fluent UI React, Web Components'],
      ['Carbon', 'IBM', 'Aksesibilitas, visualisasi data', 'React, Web Components, Svelte'],
      ['Polaris', 'Shopify', 'Pola e-commerce, panduan konten', 'Polaris Web Components'],
      ['GOV.UK', 'Pemerintah Inggris', 'Bahasa sederhana, form layanan publik', 'HTML, CSS, Nunjucks'],
      ['Ant Design', 'Ant Group', 'Dasbor enterprise, tabel, form', 'React']]}],
    pts=['Material 3 untuk Android, HIG untuk iOS.', 'Carbon, Polaris, GOV.UK, Fluent, Atlassian, Ant sebagai referensi.', 'Ikuti konvensi platform pengguna.'],
    qs=[q('Design system yang paling cocok jadi referensi aplikasi layanan publik?', ['GOV.UK Design System', 'Ant Design', 'Dribbble'], 0, 'Fokus bahasa sederhana dan form layanan.')]),
  C('Memakai design system lewat CDN dan paket',
    ['Banyak design system bisa langsung dipakai di halaman web lewat <b>CDN</b> (Content Delivery Network) tanpa proses build: cukup satu tag <code>&lt;script&gt;</code> atau <code>&lt;link&gt;</code>. Cocok untuk prototipe cepat, uji usability dengan HTML sungguhan, atau halaman statis.',
     'Contoh: <b>Bootstrap</b> dari jsDelivr, <b>Material Web</b> (komponen Material 3 untuk web), <b>Shoelace / Web Awesome</b> (web components netral), <b>Google Fonts</b> untuk tipografi, dan <b>Material Symbols</b> untuk ikon. Selalu tulis versi yang pasti agar tampilan tidak berubah sendiri.',
     'Untuk produk jangka panjang, pasang lewat <b>npm</b> agar versinya terkunci, ukuran bisa dioptimasi, dan tidak bergantung pada server pihak ketiga. Pertimbangkan juga privasi pengguna: CDN pihak ketiga dapat melihat alamat IP pengunjung.'],
    "<!-- Tipografi dan ikon dari Google Fonts -->\n<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap\">\n<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded\">\n\n<!-- Bootstrap 5 dari jsDelivr (versi dikunci) -->\n<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css\">\n\n<!-- Komponen Material 3 untuk web -->\n<script type=\"module\">\n  import 'https://esm.run/@material/web@2.2.0/all.js';\n</script>\n\n<md-filled-button>Pesan sekarang</md-filled-button>\n<md-outlined-text-field label=\"Email\" type=\"email\"></md-outlined-text-field>\n<span class=\"material-symbols-rounded\">local_cafe</span>\n\n<!-- Ganti warna Material lewat token CSS -->\n<style>\n  :root { --md-sys-color-primary: #8A4B2A; --md-sys-shape-corner-full: 12px; }\n</style>",
    None, 'html',
    pts=['CDN: satu tag, cocok untuk prototipe dan halaman statis.', 'Kunci versi di URL.', 'npm untuk produk jangka panjang.'],
    qs=[q('Kenapa versi di URL CDN harus ditulis pasti?', ['Agar tampilan tidak berubah tiba-tiba saat versi baru rilis', 'Agar lebih cepat', 'Wajib oleh browser'], 0, 'Versi terbaru bisa mengubah komponen.')]),
  C('Memilih, mengadaptasi, dan mengaudit design system',
    ['Jangan membuat design system dari nol jika timmu kecil. Pilih fondasi (Material 3 untuk aplikasi Android, Bootstrap atau Tailwind untuk web cepat), lalu <b>adaptasi</b>: ganti token warna, tipografi, dan radius sesuai brand, tambahkan komponen khusus (kartu menu, stepper keranjang), dan tulis panduan pemakaian.',
     'Audit UX berkala: cari komponen ganda (lima gaya tombol berbeda), ketidakkonsistenan istilah ("Keranjang" vs "Troli"), dan pelanggaran aksesibilitas. Catat di <b>inventaris antarmuka</b>, lalu konsolidasikan.',
     'Ukur adopsi: berapa persen layar memakai komponen resmi, berapa lama fitur baru selesai, dan berapa bug UI per rilis. Design system adalah produk; ia butuh pemilik, changelog, dan versi.'],
    "AUDIT INVENTARIS ANTARMUKA · Kopi Kita v1\n| Elemen   | Variasi ditemukan | Target | Tindakan                         |\n|----------|-------------------|--------|----------------------------------|\n| Tombol   | 7 gaya            | 3      | Primer, sekunder, teks           |\n| Input    | 4 tinggi berbeda  | 1      | 56 dp, radius 12                 |\n| Abu teks | 9 kode warna      | 2      | --teks, --teks-2                 |\n| Istilah  | Keranjang/Troli   | 1      | 'Keranjang' di semua layar        |\n| Kontras  | 3 pasangan < 4,5  | 0      | Ganti --teks-2 ke #6B625B         |",
    None, 'text',
    pts=['Adaptasi fondasi yang ada, jangan mulai dari nol.', 'Audit: komponen ganda, istilah, aksesibilitas.', 'Design system adalah produk dengan pemilik dan versi.'],
    qs=[q('Langkah pertama untuk tim kecil yang butuh design system?', ['Adaptasi fondasi seperti Material 3 dengan token brand', 'Membuat semua komponen dari nol', 'Menunggu tim besar'], 0, 'Hemat waktu dan sudah teruji.')]),
]),

M('Portofolio UX designer', 'Menengah',
  'Menunjukkan proses UX yang kuat di portofolio: riset, sintesis, keputusan berbasis bukti, dampak terukur, dan cara mempresentasikannya saat wawancara.',
  ['UX portfolio', 'Case study', 'Research synthesis', 'Impact', 'Interview'], [
  C('Studi kasus UX: menonjolkan riset dan keputusan',
    ['Portofolio UX dinilai dari <b>kualitas proses</b>: bagaimana kamu memahami masalah, memilih metode riset, menyintesis temuan, dan mengambil keputusan berdasarkan bukti. Layar akhir tetap ditampilkan, tetapi bukan bintang utamanya.',
     'Tunjukkan artefak riset yang dirapikan: rencana riset, kutipan pengguna (dengan izin dan disamarkan), affinity map, journey map, persona berbasis data, dan prioritas masalah. Jelaskan <b>kenapa</b> memilih metode itu dan apa batasannya.',
     'Ceritakan juga keputusan yang sulit atau ide yang ditolak beserta alasannya. Perekrut senior menghargai kejujuran tentang kegagalan dan trade-off.'],
    "STUDI KASUS UX · Sehat Desa: antrean puskesmas daring\n\nPeran    : UX researcher & designer (tim 3) · 8 minggu\nPertanyaan riset: kenapa pasien lansia tetap datang subuh walau ada nomor antrean WhatsApp?\nMetode   : observasi di 2 puskesmas, 8 wawancara (5 lansia, 3 petugas), analisis 600 chat\nInsight  :\n  1. Lansia tidak percaya nomor digital karena pernah dilewati petugas\n  2. Anak/cucu yang mendaftarkan, tetapi lansia yang datang\n  3. Petugas tidak bisa melihat status antrean daring di loket\nKeputusan: SMS status otomatis + layar antrean di loket (bukan aplikasi baru),\n           karena 60% lansia memakai ponsel non-smartphone\nIde ditolak: aplikasi Android khusus (adopsi rendah, biaya tinggi)\nDampak   : pilot 1 bulan, kedatangan sebelum 06.00 turun 70%",
    None, 'text',
    pts=['Proses dan keputusan berbasis bukti adalah bintang utama.', 'Tampilkan artefak riset yang rapi dan alasan metodenya.', 'Ceritakan ide yang ditolak dan trade-off.'],
    qs=[q('Apa yang paling dinilai perekrut UX?', ['Cara memahami masalah dan mengambil keputusan berbasis bukti', 'Jumlah layar yang didesain', 'Jumlah plugin Figma'], 0, 'Proses lebih penting dari gambar.')]),
  C('Menulis dampak dan metrik dengan jujur',
    ['Dampak terbaik berupa <b>angka sebelum dan sesudah</b>: tingkat keberhasilan tugas, waktu tugas, konversi, skor SUS atau CSAT, jumlah tiket bantuan, retensi. Sebutkan sumbernya (usability test 5 orang, analitik 30 hari, A/B test).',
     'Jika proyek belum dirilis atau proyek konsep, jangan mengarang angka produksi. Tulis hasil dari uji prototipe, atau hipotesis dan cara mengukurnya: "Metrik yang akan dipantau: waktu pesan dan tingkat selesai checkout."',
     'Selain angka, dampak kualitatif juga bernilai: kutipan pengguna, perubahan cara tim bekerja, atau keputusan bisnis yang diambil berkat risetmu.'],
    "Lemah : 'Desain baru membuat pengguna lebih puas.'\nKuat  : 'Di usability test (n=5), tingkat keberhasilan naik dari 2/5 ke 5/5\n         dan waktu rata-rata turun dari 94 ke 48 detik.'\n\nLemah : 'Meningkatkan konversi.'\nKuat  : 'A/B test 3 minggu (12.400 sesi): checkout selesai naik dari 61% ke 69%\n         (p < 0,05).'\n\nProyek konsep: 'Belum dirilis. Hipotesis: Pesan lagi memangkas waktu pesan\n         < 60 detik; akan diukur dengan event analytics pesan_mulai dan pesan_selesai.'",
    None, 'text',
    pts=['Angka sebelum dan sesudah beserta sumbernya.', 'Proyek konsep: hasil uji prototipe atau hipotesis, bukan angka karangan.', 'Dampak kualitatif juga bernilai.'],
    qs=[q('Cara menulis dampak untuk proyek konsep?', ['Hasil uji prototipe atau hipotesis yang akan diukur', 'Mengarang angka konversi', 'Tidak menulis apa pun'], 0, 'Jujur dan tetap menunjukkan cara berpikir.')]),
  C('Presentasi portofolio saat wawancara',
    ['Wawancara desain sering berupa <b>presentasi portofolio</b> 30 sampai 45 menit. Pilih 2 proyek yang paling relevan dengan perusahaan, dan siapkan alur: konteks (1 menit), masalah (2 menit), proses dan keputusan kunci (8 menit), solusi (3 menit), dampak dan refleksi (2 menit).',
     'Antisipasi pertanyaan: "Apa yang akan kamu lakukan berbeda?", "Bagaimana kamu meyakinkan stakeholder yang tidak setuju?", "Bagaimana kamu bekerja dengan developer?", "Kenapa memilih metode riset itu?" Latih jawaban dengan contoh nyata.',
     'Beberapa perusahaan memberi <b>design challenge</b> (tugas rumah atau whiteboard). Tunjukkan proses: klarifikasi masalah, asumsi, alternatif, keputusan, dan cara memvalidasi, bukan hanya layar cantik.'],
    "ALUR PRESENTASI 15 MENIT PER PROYEK\n00-01  Siapa aku dan peranku di proyek ini\n01-03  Masalah dan kenapa penting (data awal)\n03-11  Proses: riset -> insight -> 2 keputusan kunci (dengan bukti)\n11-14  Solusi: 3 layar utama, satu demo prototipe\n14-15  Dampak, refleksi, dan apa langkah berikutnya\n\nPERTANYAAN YANG PERLU DILATIH\n- Apa keputusan tersulit dan kenapa?\n- Kapan risetmu membuktikan asumsimu salah?\n- Bagaimana kamu menangani masukan yang bertentangan?\n- Bagaimana memastikan hasil build sesuai desain?",
    None, 'text',
    pts=['Pilih 2 proyek paling relevan.', 'Alur: konteks, masalah, proses, solusi, dampak.', 'Latih jawaban untuk pertanyaan umum dan design challenge.'],
    qs=[q('Fokus utama saat mengerjakan design challenge?', ['Proses: klarifikasi, asumsi, alternatif, keputusan, validasi', 'Hanya layar akhir yang cantik', 'Memakai sebanyak mungkin warna'], 0, 'Penilai melihat cara berpikir.')]),
]),
]
