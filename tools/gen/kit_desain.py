"""Pelajaran kit desain Figma yang bisa diunduh: studi kasus Kopi Kita (UX, UI, Design System) dan kit proyek
(Slicing Website, Slicing Mobile, Proyek Portofolio). Juga menulis src/js/desain-kit.js (katalog) dan
src/js/desain-img.js (thumbnail data URI, hanya untuk versi satu file/Artifact)."""
import base64, json, sys
from pathlib import Path
from mobile_lib import C, M, q

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/figma'))
import proyek_data as D
from svgkit import GAYA

KATALOG = {k['id']: k for k in json.loads((ROOT / 'desain/katalog.json').read_text())}
SPEC = {s['id']: s for s in D.SEMUA}
THUMB = ROOT / 'tools/figma/thumbs'
KK = 'kopi-kita-studi-kasus'


def dl(kit, pratinjau=None):
    return {'k': kit, 'p': f'{kit}--{pratinjau}' if pratinjau else kit}


def tulis_js():
    kit = {}
    for kid, k in KATALOG.items():
        s = SPEC.get(kid)
        kit[kid] = {'j': s['judul'] if s else 'Studi kasus Kopi Kita: riset sampai design system',
                    'b': s['token']['nama'] if s else 'Kopi Kita', 'g': GAYA[s['gaya']]['label'] if s else '8 gaya (utama: Modern minimal)',
                    'u': k['url'], 'kb': k['kb'], 'pf': (s['platform'] if s else 'hp+web')}
    img = {p.stem: 'data:image/webp;base64,' + base64.b64encode(p.read_bytes()).decode() for p in sorted(THUMB.glob('*.webp'))}
    (ROOT / 'src/js/desain-kit.js').write_text('/* Dibuat oleh tools/gen/kit_desain.py. Katalog kit desain Figma yang bisa diunduh. */\nconst KIT_DESAIN=' + json.dumps(kit, ensure_ascii=False) + ';\n')
    (ROOT / 'src/js/desain-img.js').write_text('/* Thumbnail kit desain (data URI) untuk versi satu file. Versi web memuat dari /desain/thumb/. */\nconst KIT_IMG=' + json.dumps(img) + ';\n')
    tujuan = ROOT / 'desain/thumb'
    tujuan.mkdir(parents=True, exist_ok=True)
    for p in THUMB.glob('*.webp'):
        (tujuan / p.name).write_bytes(p.read_bytes())


IMPOR = {'c': 'Impor kit ke Figma dalam 6 langkah', 'h': ['Langkah', 'Cara'], 'r': [
    ['1. Ekstrak & pasang font', 'Ekstrak ZIP, pasang font Google yang tertulis di README (Plus Jakarta Sans + font gaya kit).'],
    ['2. Seret SVG ke kanvas', 'Drag file .svg ke Figma atau Ctrl/Cmd+Shift+K. Nama layer dan teks tetap bisa diedit.'],
    ['3. Jadikan frame', 'Klik kanan grup > Frame selection (Ctrl/Cmd+Alt+G), beri nama sesuai file.'],
    ['4. Komponen & auto layout', 'Tombol/kartu: Create component (Ctrl/Cmd+Alt+K), gabungkan state jadi Variant; tumpukan: Shift+A.'],
    ['5. Token', 'Impor tokens.json (DTCG 2025.10) lewat Tokens Studio / Variables Import, hubungkan ke warna.'],
    ['6. Prototype', 'Buka prototype/index.html untuk melihat alur, lalu tiru di tab Prototype dengan Smart Animate.']]}


# ====================================================================== UX: studi kasus Kopi Kita
UX_KIT = [M('Kit Figma: studi kasus Kopi Kita (riset sampai handoff)', 'Menengah',
  'Satu studi kasus utuh yang bisa diunduh dan dibuka di Figma: persona, journey map, user flow, wireframe lo-fi, mid-fi, hi-fi dengan state, design system, redline, dan prototype beranimasi.',
  ['Figma', 'Riset', 'Wireframe', 'Prototype'], [
  C('Unduh kit Kopi Kita dan impor ke Figma',
    ['Kit ini berisi seluruh tahapan kerja UI/UX designer untuk satu produk: aplikasi pesan kopi <b>Kopi Kita</b> (HP) dan landing page-nya (web). Semua file berupa SVG dengan <b>layer bernama</b> dan <b>teks asli</b>, jadi setelah diimpor kamu bisa mengedit, membuat komponen, dan men-slicing-nya.',
     'Urutan folder mengikuti hierarki kerja industri: <b>01 riset</b>, <b>02 struktur</b>, <b>03 wireframe lo-fi</b>, <b>04 mid-fi</b>, <b>05 hi-fi</b> (plus state, variasi gaya, dan peta motion), <b>06 design system</b>, <b>07 handoff</b>. Ada juga <b>prototype/index.html</b> yang bisa dibuka di browser untuk merasakan alur dan animasinya.',
     'Batasan yang perlu kamu tahu: SVG tidak membawa <i>auto layout</i>, <i>component</i>, atau <i>variables</i> Figma. Itu sengaja jadi latihanmu: mengubah gambar statis menjadi sistem yang hidup.'],
    tb=[IMPOR], pts=['Kit = 1 ZIP berisi 7 tahap kerja UI/UX lengkap.', 'SVG: layer bernama, teks bisa diedit; auto layout dan komponen dibuat sendiri.', 'Buka prototype/index.html untuk melihat alur dan animasi.'],
    qs=[q('Kenapa setelah impor SVG kamu masih perlu membuat component dan auto layout sendiri?', ['SVG hanya membawa bentuk, teks, dan nama layer, bukan struktur Figma', 'Karena Figma tidak bisa membaca SVG', 'Karena file SVG-nya rusak'], 0, 'SVG adalah format gambar vektor; struktur khusus Figma harus dibangun di Figma.')]) | {'dl': [dl(KK, 'landing-desktop-1440')]},
  C('Tahap 1: riset (persona, empathy map, journey map)',
    ['Papan riset Kopi Kita disusun dari wawancara dan survei, bukan karangan. <b>Persona</b> Rina merangkum tujuan, frustrasi, perilaku, dan kebutuhan desain. <b>Empathy map</b> memetakan apa yang ia katakan, pikirkan, lakukan, dan rasakan pada jam 07.30. <b>Journey map</b> menunjukkan titik paling menyakitkan: saat membayar dan menunggu.',
     'Papan <b>problem statement</b> menutup tahap ini: satu kalimat masalah yang bisa diuji, tiga pertanyaan <i>How might we</i>, metrik HEART, dan asumsi yang harus divalidasi.',
     'Latihan: duplikat papan persona di Figma, lalu buat persona kedua (misalnya mahasiswa yang memesan untuk teman sekelas). Apa yang berubah di user flow?'],
    tb=[{'c': 'Isi folder 01-riset', 'h': ['File', 'Gunanya'], 'r': [['01-persona.svg', 'Siapa penggunanya dan apa kebutuhan desainnya'], ['02-empathy-map.svg', 'Emosi dan perilaku di momen kunci'], ['03-journey-map.svg', 'Tahap, pain point, peluang, kurva emosi'], ['04-problem-statement.svg', 'Masalah, HMW, metrik, asumsi']]}],
    pts=['Persona berbasis data, setiap poin punya bukti.', 'Journey map menunjukkan di tahap mana desain paling berdampak.', 'Problem statement + metrik membuat hasil desain bisa diuji.'],
    qs=[q('Apa yang membuat persona "berbasis data"?', ['Setiap poin bisa ditelusuri ke wawancara, survei, atau analitik', 'Memakai foto orang sungguhan', 'Ditulis sepanjang mungkin'], 0, 'Persona tanpa bukti hanyalah asumsi tim.')]) | {'dl': [dl(KK, '01-persona')]},
  C('Tahap 2: struktur (sitemap dan user flow)',
    ['Sitemap Kopi Kita memakai 4 tab navigasi bawah: Beranda, Menu, Pesanan, Akun. Masuk (OTP/passkey) baru diminta saat checkout pertama, sehingga orang bisa menjelajah menu tanpa akun.',
     'User flow "pesan ulang sebelum berangkat" menggambar jalur utama dan cabang: belum masuk, stok habis, gagal bayar. Setiap kotak di flow adalah satu layar yang nanti kamu temukan di folder wireframe.'],
    pts=['Sitemap = struktur; user flow = urutan langkah untuk satu tugas.', 'Gambar cabang error sejak awal, bukan setelah UI jadi.', 'Satu kotak flow = satu layar di tahap berikutnya.'],
    qs=[q('Kenapa cabang "gagal bayar" digambar di user flow?', ['Supaya layar dan pesan error dirancang sejak awal', 'Agar diagram terlihat ramai', 'Karena developer yang memintanya'], 0, 'State error adalah bagian dari desain, bukan tambahan.')]) | {'dl': [dl(KK, '02-user-flow')]},
  C('Tahap 3-5: lo-fi, mid-fi, hi-fi dan semua state',
    ['Tujuh layar HP yang sama tersedia dalam tiga fidelitas. <b>Lo-fi</b> memakai kotak dan bar abu-abu untuk membahas struktur. <b>Mid-fi</b> memakai teks asli tapi masih abu-abu, cocok untuk usability test awal. <b>Hi-fi</b> memakai warna, tipografi, dan ilustrasi final.',
     'Folder <b>state</b> berisi layar memuat (skeleton), keranjang kosong, dan pembayaran gagal. Landing page tersedia untuk desktop 1440 dan HP 390.',
     'Folder <b>variasi-gaya</b> berisi Beranda dan Detail produk dalam 7 gaya lain: Neo-brutalism, Liquid Glass, Material 3 Expressive, Dark mode, Claymorphism, Editorial, Retro Y2K. Layout sama, hanya token yang berubah.'],
    tb=[{'c': 'Kapan memakai tiap fidelitas', 'h': ['Fidelitas', 'Dipakai untuk', 'Jangan dipakai untuk'], 'r': [['Lo-fi', 'Diskusi struktur dan prioritas konten', 'Menilai warna atau gaya'], ['Mid-fi', 'Usability test awal, review alur', 'Presentasi ke klien akhir'], ['Hi-fi', 'Handoff, test akhir, portofolio', 'Eksplorasi awal yang masih berubah']]}],
    pts=['Satu layout bisa tampil dalam banyak gaya bila token dipisah dari komponen.', 'State memuat, kosong, dan error wajib ada di hi-fi.'],
    qs=[q('Apa yang berubah saat Kopi Kita diganti dari gaya Modern ke Neo-brutalism?', ['Token: warna garis, tebal garis, radius, font judul, bayangan', 'Urutan layar dan isi konten', 'Alur pembayaran'], 0, 'Gaya visual hidup di token; struktur dan konten tetap.')]) | {'dl': [dl(KK, 'eksplorasi-8-gaya')]},
  C('Prototype dan animasi: Smart Animate, durasi, easing',
    ['Papan <b>peta interaksi & motion</b> mencantumkan setiap sambungan: dari layar mana, pemicu apa, animasi apa, berapa milidetik, dan easing-nya. Buka <b>prototype/index.html</b> untuk merasakan hasilnya, lalu tiru di tab Prototype Figma.',
     'Aturan praktis: transisi layar 200-300 ms dengan <code>ease-out</code>; momen berhasil boleh memakai <i>spring</i> sampai 400 ms; tab tidak dianimasikan. <b>Smart Animate</b> hanya bekerja bila layer di dua frame punya nama yang sama, karena itu kit ini menamai layer dengan konsisten.',
     'Mikro-interaksi (tekan tombol, badge keranjang, skeleton, toast, centang berhasil) ada di bagian bawah prototype. Semuanya otomatis menjadi instan bila pengguna menyalakan <code>prefers-reduced-motion</code>.'],
    tb=[{'c': 'Spesifikasi motion Kopi Kita', 'h': ['Interaksi', 'Animasi', 'Durasi', 'Easing'], 'r': [['Menu ke Detail', 'Smart Animate (foto membesar)', '300 ms', 'ease-in-out'], ['Detail ke Keranjang', 'Move in dari kanan', '250 ms', 'ease-out'], ['Bayar berhasil', 'Smart Animate + Spring', '400 ms', 'spring'], ['Gagal bayar', 'Overlay dialog', '200 ms', 'ease-out'], ['Tekan tombol', 'scale 0.97', '100 ms', 'ease-out']]}],
    pts=['Durasi UI 100-400 ms; lebih lama terasa lambat.', 'Smart Animate butuh nama layer yang sama di kedua frame.', 'Hormati prefers-reduced-motion.'],
    qs=[q('Smart Animate antara dua frame tidak bergerak mulus. Penyebab paling mungkin?', ['Nama layer di kedua frame berbeda', 'Durasinya kurang dari 1 detik', 'Frame memakai font Google'], 0, 'Figma mencocokkan layer berdasarkan nama dan hierarki.')]) | {'dl': [dl(KK, 'peta-interaksi-motion')]},
  C('Kit proyek UI/UX: 6 mini + 4 besar',
    ['Setiap proyek di jalur Proyek UI/UX punya kit pendukung dengan gaya visual berbeda: layar untuk dicek kontrasnya, papan token DTCG, artikel untuk type scale, prototype untuk usability test, halaman untuk diaudit, kartu card sorting, design system multi-brand, redesign checkout, portal layanan publik, dan asisten AI bank.',
     'Pakai kit sebagai bahan, bukan jawaban. Untuk portofolio, ceritakan keputusanmu: apa yang kamu ubah dari kit, kenapa, dan bagaimana kamu mengujinya.'],
    pts=['10 kit, 10 gaya dan konteks berbeda.', 'Kit = bahan latihan; nilai portofolio ada di keputusan dan pengujianmu.']) | {'dl': [dl(i) for i in SPEC if i.startswith('ux-')]},
  ])]

# ====================================================================== UI: gaya visual
UI_KIT = [M('Kit Figma: 8 gaya visual dan mikro-interaksi', 'Menengah',
  'Satu layout Kopi Kita dalam delapan gaya visual populer 2026 (termasuk Liquid Glass dan Material 3 Expressive), lengkap dengan token per gaya dan demo mikro-interaksi.',
  ['Figma', 'Gaya visual', 'Token', 'Motion'], [
  C('Satu layout, delapan gaya visual',
    ['Gaya visual bukan soal selera semata. Setiap gaya punya kekuatan dan risiko. Kit Kopi Kita menyediakan Beranda dan Detail produk dalam 8 gaya, plus <code>tokens-gaya-*.json</code> untuk beberapa di antaranya, supaya kamu bisa membandingkan langsung.',
     'Perhatikan bahwa struktur, jarak, dan konten tidak berubah. Yang berubah hanya token: warna, radius, tebal garis, font judul, dan jenis bayangan. Inilah alasan design system memisahkan <b>token</b> dari <b>komponen</b>.'],
    tb=[{'c': 'Kapan memakai tiap gaya', 'h': ['Gaya', 'Cocok untuk', 'Risiko yang harus diuji'], 'r': [
        ['Modern minimal', 'Produk umum, fintech, layanan', 'Bisa terasa generik; butuh identitas lewat warna/ilustrasi'],
        ['Neo-brutalism', 'Produk kreatif, Gen Z, komunitas', 'Garis tebal melelahkan di layar padat data'],
        ['Liquid Glass (iOS 26)', 'Aplikasi Apple, media, kesehatan', 'Kontras teks di atas latar tembus pandang; siapkan fallback'],
        ['Material 3 Expressive', 'Aplikasi Android 16+', 'Bentuk dan warna kuat bisa bertabrakan dengan brand'],
        ['Dark mode', 'Dashboard, keuangan, malam hari', 'Aksen terlalu jenuh; kontras teks sekunder'],
        ['Claymorphism', 'Edukasi anak, gamifikasi', 'Batas elemen kabur, target sentuh tidak jelas'],
        ['Editorial', 'Berita, majalah, brand premium', 'Serif kecil sulit dibaca di HP murah'],
        ['Retro Y2K', 'Kampanye, event, musik', 'Cepat terasa usang; font mono melebar']]}],
    pts=['Gaya = kumpulan keputusan token.', 'Setiap gaya punya risiko aksesibilitas yang harus diuji.', 'Pilih satu gaya untuk produk, lalu kunci di design system.'],
    qs=[q('Risiko utama gaya Liquid Glass yang harus diuji?', ['Kontras teks di atas latar tembus pandang yang berubah-ubah', 'Ukuran file terlalu besar', 'Tidak bisa dipakai di web'], 0, 'Lapisan translusen membuat kontras bergantung pada konten di belakangnya.')]) | {'dl': [dl(KK, 'eksplorasi-8-gaya')]},
  C('Mikro-interaksi dan prototype di Figma',
    ['Buka <b>prototype/index.html</b> di kit mana pun. Di bagian bawah ada lima mikro-interaksi standar: tombol tekan (scale 0.97, 100 ms), badge keranjang (+1 dengan spring), skeleton shimmer, toast, dan centang berhasil.',
     'Di Figma, mikro-interaksi dibuat dengan <b>interactive components</b>: buat variant default dan tekan pada komponen tombol, lalu sambungkan <i>While pressing</i> ke variant tekan dengan Smart Animate 100 ms. Untuk toast, pakai <i>After delay</i> 4000 ms untuk kembali ke variant tersembunyi.'],
    pts=['Mikro-interaksi memberi umpan balik, bukan hiasan.', 'Interactive components: animasi di dalam komponen, berlaku di semua instance.'],
    qs=[q('Pemicu Figma yang tepat untuk efek tombol saat ditekan?', ['While pressing', 'After delay', 'On drag'], 0, 'While pressing aktif selama jari/klik menahan tombol.')]) | {'dl': [dl(KK, 'peta-interaksi-motion')]},
  ])]

# ====================================================================== DS: design system Kopi Kita
DS_KIT = [M('Kit Figma: design system Kopi Kita dan multi-brand', 'Menengah',
  'Papan fondasi (warna dengan rasio kontras, tipografi, spasi, radius, elevasi), komponen dengan semua state, tokens.json DTCG 2025.10, redline handoff, dan kit design system multi-brand.',
  ['Figma', 'Token DTCG', 'Komponen', 'Handoff'], [
  C('Fondasi dan tokens.json (DTCG 2025.10)',
    ['Papan <b>fondasi</b> menampilkan warna semantik lengkap dengan rasio kontras WCAG, skala tipografi rasio 1,2, spasi grid 4/8, radius, dan elevasi. Nama tokennya sama persis dengan isi <code>tokens.json</code>.',
     '<code>tokens.json</code> memakai format DTCG 2025.10: warna ditulis sebagai objek <code>{colorSpace, components, hex}</code>, token semantik merujuk primitif dengan alias seperti <code>{color.brand.primer}</code>, dan ada token motion (durasi, cubic-bezier).',
     'Impor ke Figma lewat Tokens Studio atau plugin Variables Import, lalu buat mode terang/gelap dengan <code>tokens-gaya-gelap.json</code>.'],
    tb=[{'c': 'Lapisan token', 'h': ['Lapisan', 'Contoh', 'Dipakai oleh'], 'r': [['Primitif', 'color.brand.primer = #8A4B2A', 'Token semantik saja'], ['Semantik', 'color.action.primary = {color.brand.primer}', 'Komponen'], ['Komponen', 'button.primary.bg = {color.action.primary}', 'Satu komponen']]}],
    pts=['Komponen merujuk token semantik, bukan nilai mentah.', 'DTCG 2025.10: format tukar token antar alat.'],
    qs=[q('Kenapa komponen tidak boleh langsung memakai #8A4B2A?', ['Ganti tema/brand jadi harus mengubah setiap komponen', 'Figma menolak warna hex', 'Hex lebih lambat dirender'], 0, 'Alias semantik membuat tema bisa diganti di satu tempat.')]) | {'dl': [dl(KK, '02-komponen-dan-state')]},
  C('Komponen, state, dan redline handoff',
    ['Papan komponen menata setiap komponen per baris dan setiap state per kolom: tombol 5 varian x 6 state, input 5 state, chip, segmen, radio, stepper, badge, kartu, skeleton, dialog, toast, navigasi. Di Figma, ubah setiap baris menjadi <b>Component Set</b> dengan properti <code>State</code>.',
     'Papan <b>redline</b> memberi jarak, ukuran, dan token pada layar Beranda dan Detail, plus catatan implementasi (target sentuh 48, safe area, angka tabular, fokus tidak tertutup). Papan <b>daftar aset</b> menjelaskan format ekspor tiap aset.'],
    pts=['Satu komponen = semua state-nya didesain.', 'Redline + catatan perilaku mengurangi tebak-tebakan developer.'],
    qs=[q('State mana yang paling sering lupa didesain?', ['Fokus keyboard dan memuat', 'Default', 'Hover di desktop'], 0, 'Keduanya tidak terlihat saat demo dengan mouse dan koneksi cepat.')]) | {'dl': [dl(KK, '01-redline')]},
  C('Design system multi-brand',
    ['Kit proyek <b>Design system multi-brand</b> berisi tiga brand (Nusa Group, Nusa Pay, Nusa Mart) dengan struktur token yang sama. Papan "satu komponen, tiga brand" membuktikan bahwa komponen tidak berubah, hanya token semantik yang berganti.',
     'Di Figma, buat satu koleksi Variables dengan tiga <b>mode</b> (satu per brand), lalu ganti mode di frame untuk melihat brand lain.'],
    pts=['Multi-brand = satu komponen, banyak set token.', 'Figma Variables: satu mode per brand.']) | {'dl': [dl('ux-besar-1-ds-multibrand'), dl('ux-mini-2-token-dtcg')]},
  ])]


# ====================================================================== Peta slicing per proyek
# blok desain -> elemen HTML, susunan di HP, susunan di desktop (web) / widget Flutter (mobile)
PETA_WEB = {
  'navbar': ('<header> + <nav>', 'logo + tombol, menu di balik tombol ☰', 'logo · menu flex gap 24 · CTA'),
  'topbar': ('<header> judul halaman', 'judul + tombol bertumpuk', 'flex space-between'),
  'hero': ('<section class="hero"> + <h1>', '1 kolom, gambar di bawah teks', 'grid 2 kolom 1fr 1fr, gap 48'),
  'fitur': ('<section> + <ul> kartu', '1 kolom', 'grid 3 kolom'),
  'kartu': ('<section> + <article> per kartu', '1 kolom (atau 2 jika kartu kecil)', 'grid repeat(4, 1fr) atau auto-fill minmax(240px,1fr)'),
  'testimoni': ('<section> + <blockquote>', '1 kolom / scroll-snap horizontal', 'grid 3 kolom'),
  'cta': ('<section class="cta">', 'judul di atas tombol', 'judul kiri, tombol kanan'),
  'footer': ('<footer> + <nav> per kolom', 'kolom bertumpuk', 'grid 4 kolom'),
  'form': ('<form> + <label> + pesan error', 'form penuh, ringkasan di bawah', 'grid form 2fr + ringkasan 1fr (sticky)'),
  'statistik': ('<section> + <dl>', 'grid 2 kolom', 'grid 4 kolom'),
  'grafik': ('<figure> + <svg>/<canvas> + <figcaption>', 'lebar penuh, tinggi 220', 'lebar penuh, tinggi 320'),
  'tabel': ('<table> dengan <caption>, <th scope>', 'bungkus overflow-x:auto atau ubah jadi kartu', 'tabel penuh'),
  'kanban': ('<section> per kolom + <ul role="list">', 'kolom scroll horizontal (scroll-snap)', 'grid 4 kolom'),
  'langkah': ('<ol> langkah', 'vertikal', 'horizontal 4 kolom'),
  'chat': ('<section> + <ol> pesan + <form>', 'percakapan penuh, input menempel bawah', 'daftar kiri 320 + percakapan kanan'),
}
PETA_HP = {
  'appbar': 'AppBar / TopAppBar (Compose)', 'sapaan': 'Row(Avatar, Column(Text, Text))', 'judul': 'Text(style: headlineSmall)',
  'bagian': 'Text(style: titleMedium) + jarak 16', 'saldo': 'Card(Column(Text nilai, Row(aksi IconButton)))', 'cari': 'SearchBar',
  'chips': 'Wrap / LazyRow(FilterChip)', 'banner': 'Card dengan gradien + FilledButton', 'list': 'ListView / LazyColumn(ListTile)',
  'grid': 'GridView.count(2) / LazyVerticalGrid', 'form': 'Form + TextFormField + FilledButton', 'langkah': 'Stepper / Row(progress)',
  'peta': 'Stack(Peta, Card info di bawah)', 'chat': 'ListView(reverse: true) gelembung', 'masukan_chat': 'Row(TextField, IconButton kirim) + imePadding',
  'ringkas': 'Card(Column(Row label-nilai))', 'grafik': 'CustomPaint / fl_chart', 'slot': 'Wrap(ChoiceChip) jam tersedia',
  'segmen': 'SegmentedButton', 'kosong': 'Column(ikon, teks, FilledButton) di tengah', 'spasi': 'SizedBox(height)',
}


def _css_token(t):
    return (':root {\n' + ''.join(f'  --{k}: {t[k]};\n' for k in ('primer', 'primer2', 'aksen', 'latar', 'permukaan', 'teks', 'teks2', 'garis', 'lembut', 'bahaya', 'sukses'))
            + f'  --radius: {t["radius"]}px;\n  --ruang-1: 8px; --ruang-2: 16px; --ruang-3: 24px; --ruang-4: 32px; --ruang-5: 48px;\n}}\n')


def _kerangka_web(spec):
    blok = [b for b in spec['layar'][0][1] if b[0] != 'spasi']
    tag = {'navbar': 'header', 'topbar': 'header', 'footer': 'footer'}
    html, css_hp, css_dt = [], [], []
    for jenis, d in blok:
        el = tag.get(jenis, 'section')
        jd = d.get('jd') if isinstance(d, dict) else None
        isi = f'<h2>{jd}</h2> … ' if jd and jenis not in ('hero',) else ('<h1>' + d.get('jd', '') + '</h1> … ' if jenis == 'hero' else '… ')
        html.append(f'  <{el} class="{jenis}">{isi}</{el}>')
        css_dt.append(f'  .{jenis} {{ /* desktop: {PETA_WEB.get(jenis, ("", "", "sesuai frame"))[2]} */ }}')
    sb = spec.get('sidebar')
    awal = '<div class="app">\n  <aside class="sidebar" aria-label="Navigasi">…</aside>\n  <main>\n' if sb else '<main>\n'
    akhir = '\n  </main>\n</div>' if sb else '\n</main>'
    h = '\n'.join(x for x in html if 'header' in x.split('>')[0]) + '\n' + awal + '\n'.join('  ' + x for x in html if 'header' not in x.split('>')[0] and 'footer' not in x.split('>')[0]) + akhir + '\n' + '\n'.join(x for x in html if x.strip().startswith('<footer'))
    c = (_css_token(spec['token']) + '\n/* 1. MOBILE dulu (tanpa media query): semua bagian 1 kolom, padding samping 16 */\n'
         + '.wadah, main > section, header, footer { padding-inline: var(--ruang-2); }\n'
         + ('.app { display: block; }\n.sidebar { display: none; }  /* di HP: ganti dengan tab bar bawah atau menu ☰ */\n' if sb else '')
         + '\n/* 2. DESKTOP sesuai frame web: isi maks 1200 di tengah */\n@media (min-width: 768px) {\n'
         + '  main > section, header, footer { padding-inline: max(var(--ruang-4), calc((100% - 1200px) / 2)); }\n'
         + ('  .app { display: grid; grid-template-columns: 240px 1fr; }\n  .sidebar { display: block; }\n' if sb else '')
         + '\n'.join(css_dt) + '\n}\n')
    return h.strip('\n'), c


def _tema_flutter(t):
    hx = lambda v: '0xFF' + v.lstrip('#').upper()
    return (f"final tema = ThemeData(\n  useMaterial3: true,\n  colorScheme: ColorScheme.fromSeed(\n    seedColor: const Color({hx(t['primer'])}),\n"
            f"    primary: const Color({hx(t['primer'])}),\n    secondary: const Color({hx(t['aksen'])}),\n    surface: const Color({hx(t['latar'])}),\n    error: const Color({hx(t['bahaya'])}),\n  ),\n"
            f"  cardTheme: CardThemeData(shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular({t['radius']}))),\n"
            f"  filledButtonTheme: FilledButtonThemeData(style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(48),\n"
            f"      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular({t['radius']})))),\n);\n")


def _kerangka_flutter(spec):
    nm, blok = spec['layar'][0][:2]
    kelas = 'Layar' + ''.join(w.capitalize() for w in nm.replace('/', ' ').split()[:2])
    anak = []
    for jenis, d in blok:
        if jenis == 'appbar':
            continue
        anak.append(f'          // {jenis}: {PETA_HP.get(jenis, "widget sesuai frame")}\n          const SizedBox(height: 16),')
    ab = any(j == 'appbar' for j, _ in blok)
    return (_tema_flutter(spec['token']) + f"\nclass {kelas} extends StatelessWidget {{\n  const {kelas}({{super.key}});\n  @override\n  Widget build(BuildContext context) {{\n    return Scaffold(\n"
            + ("      appBar: AppBar(title: const Text('" + nm + "')),\n" if ab else '')
            + "      body: SafeArea(\n        child: ListView(\n          padding: const EdgeInsets.all(16),\n          children: [\n" + '\n'.join(anak) + "\n          ],\n        ),\n      ),\n    );\n  }\n}")


# ====================================================================== Slicing: 6 mini + 4 besar
def _proyek(spec, jalur):
    s = spec
    jenis = 'mini' if s['tipe'] == 'mini' else 'besar'
    no = s['id'].split('-')[2]
    layar = ', '.join(x[0] for x in s.get('layar', []))
    d = C(f'{"Mini" if jenis == "mini" else "Besar"} {no}: {s["judul"]}',
             [f'<b>Brief.</b> {s["brief"]}',
              f'Kit berisi desain hi-fi ({layar}), wireframe lo-fi, variasi 3 gaya lain, prototype beranimasi, <code>tokens.json</code>, ikon, dan <code>BRIEF.md</code> berisi kriteria penerimaan. Gaya utama: <b>{GAYA[s["gaya"]]["label"]}</b>.',
              'Cara mengerjakan: impor ke Figma, periksa ukuran dengan Dev Mode, ubah token menjadi CSS custom properties' + (' atau ThemeData/MaterialTheme' if jalur == 'slm' else '') + ', lalu slicing per komponen dari yang terkecil (tombol, input, kartu) sebelum menyusun halaman.'],
             tb=[{'c': 'Kriteria selesai', 'h': ['Aspek', 'Target'], 'r': [['Kemiripan visual', 'Selisih maksimal 2px di breakpoint utama'], ['State', 'default, hover, fokus, tekan, nonaktif, memuat, kosong, error'],
                                                                         ['Responsif', '360 - 1440' if jalur == 'slw' else '360 - 430 lebar HP, aman di notch & gesture bar'], ['Aksesibilitas', 'WCAG 2.2 AA, target sentuh 48'],
                                                                         ['Animasi', 'Sesuai prototype, hormati reduced motion'], ['Portofolio', 'Studi kasus: masalah, keputusan, hasil']]}],
             pts=[f'Proyek {jenis}: {s["judul"]}.', f'Gaya visual: {GAYA[s["gaya"]]["label"]}.', 'Ambil nilai dari tokens.json, jangan menebak dari gambar.']) | {'dl': [dl(s['id'])]}
    return _gabung(d, _peta(s, jalur), jalur)


def _gabung(d, p, jalur):
    if not p:
        return d
    d['tb'] = p.pop('tb2') + d.get('tb', [])
    d['b'] = d['b'] + ['<b>Peta slicing.</b> Tabel di bawah memetakan setiap blok di frame desain ke ' + ('elemen HTML dan susunannya di HP dan desktop. Kode contoh adalah titik awal: token sudah diambil dari <code>tokens.json</code> kit ini, kerangka HTML mengikuti urutan blok di frame, dan CSS sudah dipisah menjadi gaya HP (dasar) dan desktop (media query 768 px). Isi setiap bagian sampai sama dengan frame web, lalu periksa di lebar 360, 768, dan 1440.' if jalur == 'slw' else 'widget Flutter atau Compose. Kode contoh sudah berisi ThemeData dari <code>tokens.json</code> kit ini dan urutan widget sesuai frame. Gambar pratinjau kit adalah review visualnya: jalankan di emulator 360 × 800 dp lalu bandingkan dengan gambar itu.')]
    d.update(p)
    return d


def _peta(s, jalur):
    """Peta slicing + kode awal agar desain di kit bisa langsung dikerjakan sampai sama."""
    blok = [b[0] for b in s['layar'][0][1] if b[0] != 'spasi'] if s.get('layar') else []
    if jalur == 'slw':
        h, c = _kerangka_web(s)
        return {'tb2': [{'c': 'Peta slicing: setiap blok di frame desain', 'h': ['Blok desain', 'Elemen HTML', 'Di HP (360)', 'Di desktop (1440)'],
                         'r': [[b] + list(PETA_WEB.get(b, ('<section>', '1 kolom', 'sesuai frame'))) for b in dict.fromkeys(blok)]}],
                'code': '<!-- index.html: kerangka semantik dari frame desain -->\n' + h + '\n\n/* style.css: token dari tokens.json + kerangka responsif */\n' + c, 'lang': 'html'}
    if jalur == 'slm':
        return {'tb2': [{'c': 'Peta slicing: setiap blok di frame desain', 'h': ['Blok desain', 'Widget Flutter / Compose'],
                         'r': [[b, PETA_HP.get(b, 'sesuai frame')] for b in dict.fromkeys(blok)]}],
                'code': _kerangka_flutter(s), 'lang': 'dart'}
    return {}


SLW_KIT = [M('Proyek slicing website: 6 mini + 4 besar', 'Menengah',
  'Sepuluh desain web siap slicing untuk portofolio, masing-masing dengan gaya visual berbeda, prototype beranimasi, dan token DTCG.',
  ['Figma', 'Slicing', 'Portofolio'], [_proyek(s, 'slw') for s in D.SLW])]
SLM_KIT = [M('Proyek slicing mobile: 6 mini + 4 besar', 'Menengah',
  'Sepuluh desain aplikasi HP siap slicing (Flutter, Compose, atau web mobile), masing-masing dengan gaya visual berbeda, prototype beranimasi, dan token DTCG.',
  ['Figma', 'Slicing', 'Flutter', 'Portofolio'], [_proyek(s, 'slm') for s in D.SLM])]


def pasang_proyek(PJ_FE, PJ_MOBILE, PJ_UIUX):
    """Menempelkan kit desain ke proyek berpenyelesaian (urutan Mini 1-6 lalu Besar 1-4)."""
    for mod, daftar in ((PJ_FE, D.SLW), (PJ_MOBILE, D.SLM), (PJ_UIUX, D.UX)):
        ls = [l for l in mod['lessons'] if l['t'].startswith(('Mini', 'Besar'))]
        for l, s in zip(ls, daftar):
            l['dl'] = [dl(s['id'])]


tulis_js()
