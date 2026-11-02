"""Tambahan jalur Tailwind CSS dan Bootstrap 5: soal latihan per pelajaran dan modul lanjutan."""
from mobile_lib import W, C, M, q
from mobile_dart_x import S


def H(soal, petunjuk, jawab):
    return S(soal, petunjuk, jawab, lang='html')


TW_SO = {
'Utility-first dan cara memasang': [
  H('Buat kartu profil: lebar maksimal <code>max-w-xs</code>, padding 6, latar putih, sudut <code>rounded-2xl</code>, bayangan <code>shadow-lg</code>, berisi nama tebal dan peran berwarna abu-abu.', 'Gabungkan kelas di satu div, lalu kelas teks di h2 dan p.',
    '<div class="max-w-xs p-6 bg-white rounded-2xl shadow-lg">\n  <h2 class="text-xl font-bold text-slate-900">Rina Siregar</h2>\n  <p class="text-slate-500">Flutter Developer</p>\n</div>'),
  H('Tulis isi file CSS utama dan potongan konfigurasi Vite untuk memasang Tailwind v4.', 'Plugin @tailwindcss/vite dan satu baris @import.',
    '<!-- src/style.css -->\n@import "tailwindcss";\n\n<!-- vite.config.js -->\nimport { defineConfig } from \'vite\'\nimport tailwindcss from \'@tailwindcss/vite\'\nexport default defineConfig({ plugins: [tailwindcss()] })'),
],
'Jarak, ukuran, dan warna': [
  H('Buat tiga lencana status: "Lunas" hijau, "Menunggu" kuning, "Batal" merah, masing-masing <code>px-3 py-1 rounded-full text-sm</code> dengan latar tingkat 100 dan teks tingkat 800.', 'Pola bg-{warna}-100 text-{warna}-800.',
    '<span class="px-3 py-1 rounded-full text-sm bg-emerald-100 text-emerald-800">Lunas</span>\n<span class="px-3 py-1 rounded-full text-sm bg-amber-100 text-amber-800">Menunggu</span>\n<span class="px-3 py-1 rounded-full text-sm bg-rose-100 text-rose-800">Batal</span>'),
  H('Buat kotak 120×120 piksel tepat berwarna #B4532A dengan nilai arbitrer.', 'w-[120px] h-[120px] bg-[#B4532A].',
    '<div class="w-[120px] h-[120px] bg-[#B4532A] rounded-lg"></div>'),
],
'Tipografi': [
  H('Buat kutipan: teks besar miring, garis kiri tebal berwarna, dan nama penulis kecil berhuruf kapital.', 'border-l-4 border-sky-500 pl-4 italic text-lg; uppercase tracking-wide text-xs untuk nama.',
    '<blockquote class="border-l-4 border-sky-500 pl-4">\n  <p class="text-lg italic text-slate-800">"Kode yang baik adalah kode yang mudah dibaca orang lain."</p>\n  <footer class="mt-2 text-xs uppercase tracking-wide text-slate-500">Mentor Ruang Kode</footer>\n</blockquote>'),
  H('Potong judul panjang menjadi satu baris berelipsis di dalam kotak selebar 200 px.', 'truncate memerlukan lebar terbatas.',
    '<h3 class="w-[200px] truncate font-semibold">Belajar Kotlin Multiplatform dari nol sampai rilis</h3>'),
],
'Flexbox dan Grid': [
  H('Buat footer tiga kolom yang ditumpuk di ponsel dan berjajar mulai md, dengan jarak 6.', 'flex flex-col md:flex-row gap-6, atau grid grid-cols-1 md:grid-cols-3.',
    '<footer class="grid grid-cols-1 md:grid-cols-3 gap-6 p-6 bg-slate-900 text-slate-300">\n  <div><b class="text-white">RuangKode</b><p class="text-sm">Belajar coding berbahasa Indonesia.</p></div>\n  <div><b class="text-white">Jalur</b><p class="text-sm">Dart, Kotlin, Tailwind</p></div>\n  <div><b class="text-white">Kontak</b><p class="text-sm">halo@ruangkode.id</p></div>\n</footer>'),
  H('Buat tata letak dasbor: sidebar selebar 1 kolom dan konten 3 kolom dalam grid 4 kolom.', 'grid grid-cols-4, lalu col-span-3 pada konten.',
    '<div class="grid grid-cols-4 gap-4 p-4 min-h-[200px]">\n  <aside class="col-span-1 bg-slate-100 rounded p-3">Menu</aside>\n  <main class="col-span-3 bg-white border rounded p-3">Konten</main>\n</div>'),
],
'Desain responsif': [
  H('Buat judul yang berukuran <code>text-2xl</code> di ponsel, <code>text-4xl</code> mulai md, dan <code>text-6xl</code> mulai lg.', 'Tumpuk kelas dengan awalan berbeda.',
    '<h1 class="text-2xl md:text-4xl lg:text-6xl font-extrabold">Belajar Flutter</h1>'),
  H('Tampilkan menu navigasi hanya mulai md, dan tombol hamburger hanya di ponsel.', 'hidden md:flex untuk menu; md:hidden untuk tombol.',
    '<nav class="flex items-center justify-between p-4">\n  <b>RuangKode</b>\n  <div class="hidden md:flex gap-4"><a>Beranda</a><a>Kursus</a></div>\n  <button class="md:hidden" aria-label="Buka menu">☰</button>\n</nav>'),
],
'Hover, focus, dan mode gelap': [
  H('Buat kartu yang sedikit membesar dan bayangannya menebal saat di-hover, dengan transisi halus.', 'transition duration-200 hover:scale-105 hover:shadow-xl.',
    '<div class="p-6 bg-white rounded-xl shadow transition duration-200 hover:scale-105 hover:shadow-xl">Kursus Kotlin</div>'),
  H('Buat kotak centang yang membuat teks di sebelahnya tercoret saat dicentang, tanpa JavaScript.', 'Beri input kelas peer, lalu span dengan peer-checked:line-through.',
    '<label class="flex items-center gap-2">\n  <input type="checkbox" class="peer">\n  <span class="peer-checked:line-through peer-checked:text-slate-400">Belajar Tailwind</span>\n</label>'),
  H('Buat kartu yang berwarna terang dan otomatis gelap di mode gelap.', 'bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100.',
    '<div class="p-6 rounded-xl bg-white text-slate-900 dark:bg-slate-800 dark:text-slate-100">Mode gelap mengikuti sistem</div>'),
],
'Form yang rapi': [
  H('Tambahkan pesan error merah di bawah input email yang hanya terlihat jika input tidak valid dan sudah diisi.', 'Kelas peer pada input, lalu p dengan hidden peer-[&:not(:placeholder-shown):invalid]:block. Bentuk lebih sederhana: invalid:border-rose-500 pada input.',
    '<input type="email" placeholder=" " class="peer block w-full border rounded-lg px-3 py-2 invalid:[&:not(:placeholder-shown)]:border-rose-500">\n<p class="hidden mt-1 text-sm text-rose-600 peer-[&:not(:placeholder-shown):invalid]:block">Format email belum benar.</p>'),
  H('Buat select dan textarea yang gayanya seragam dengan input lain.', 'Pakai kelas yang sama: block w-full border rounded-lg px-3 py-2.',
    '<select class="block w-full border border-slate-300 rounded-lg px-3 py-2">\n  <option>Flutter</option><option>Compose</option>\n</select>\n<textarea rows="3" class="mt-3 block w-full border border-slate-300 rounded-lg px-3 py-2" placeholder="Catatan"></textarea>'),
],
'Komponen dan @apply': [
  H('Buat kelas komponen <code>.kartu</code> dengan @apply (padding 6, latar putih, sudut xl, bayangan) dan pakai di dua kartu.', 'Tulis di <style type="text/tailwindcss">.',
    '<style type="text/tailwindcss">\n  .kartu { @apply p-6 bg-white rounded-xl shadow; }\n</style>\n<div class="kartu">Dart</div>\n<div class="kartu mt-4">Kotlin</div>'),
],
'Tema dan konfigurasi': [
  H('Daftarkan font "Fraunces" sebagai <code>font-judul</code> dan jarak khusus <code>18</code> = 4.5rem lewat konfigurasi Play CDN.', 'theme.extend.fontFamily dan theme.extend.spacing.',
    "<script>\n  tailwind.config = { theme: { extend: {\n    fontFamily: { judul: ['Fraunces', 'serif'] },\n    spacing: { 18: '4.5rem' }\n  } } }\n</script>\n<h1 class=\"font-judul text-3xl mt-18\">Kedai Kopi Senja</h1>"),
  H('Tulis versi Tailwind v4 dari konfigurasi warna merek #B4532A dan krem #FBF3E4.', 'Di v4, tema ditulis di CSS dengan @theme dan variabel --color-*.',
    '@import "tailwindcss";\n\n@theme {\n  --color-merek: #B4532A;\n  --color-krem: #FBF3E4;\n}'),
],
'Proyek: landing page responsif': [
  H('Tambahkan bagian testimoni dua kolom (satu kolom di ponsel) dengan foto bulat, nama, dan kutipan.', 'grid md:grid-cols-2 gap-4; foto memakai w-12 h-12 rounded-full.',
    '<section class="grid md:grid-cols-2 gap-4 px-6 pb-10">\n  <figure class="p-5 border rounded-xl">\n    <div class="flex items-center gap-3">\n      <div class="w-12 h-12 rounded-full bg-sky-200"></div>\n      <figcaption><b>Rina</b><p class="text-sm text-slate-500">Mahasiswa</p></figcaption>\n    </div>\n    <blockquote class="mt-3 text-slate-700">"Materinya runtut dan ada latihannya."</blockquote>\n  </figure>\n  <figure class="p-5 border rounded-xl">\n    <div class="flex items-center gap-3">\n      <div class="w-12 h-12 rounded-full bg-emerald-200"></div>\n      <figcaption><b>Budi</b><p class="text-sm text-slate-500">Guru SMK</p></figcaption>\n    </div>\n    <blockquote class="mt-3 text-slate-700">"Cocok untuk kelas praktik."</blockquote>\n  </figure>\n</section>'),
],
}

TW_QX = {
'Jarak, ukuran, dan warna': [q('Kelas bg-sky-600/20 berarti?', ['Warna sky-600 dengan opasitas 20%', 'Lebar 20', 'Padding 20'], 0, 'Garis miring mengatur transparansi.')],
'Flexbox dan Grid': [q('Kelas untuk jarak antaranak flex atau grid?', ['gap-4', 'space-4', 'margin-4'], 0, 'gap bekerja di flex dan grid.')],
'Hover, focus, dan mode gelap': [q('Awalan untuk mengubah anak saat induknya di-hover?', ['peer-hover:', 'group-hover:', 'child-hover:'], 1, 'Induk diberi kelas group.')],
'Komponen dan @apply': [q('Kekurangan memakai @apply berlebihan?', ['Gaya tidak lagi terlihat langsung di HTML', 'Tidak bisa responsif', 'Membuat error'], 0, 'Manfaat utama utility-first hilang.')],
}

BS_SO = {
'Memasang Bootstrap 5': [
  H('Tulis kerangka HTML lengkap yang memuat Bootstrap 5.3.3 dari CDN jsDelivr.', 'link CSS di head, script bundle sebelum </body>, dan meta viewport.',
    '<!doctype html>\n<html lang="id">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>Toko</title>\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">\n</head>\n<body>\n  <h1 class="container">Halo, Bootstrap!</h1>\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>\n</body>\n</html>'),
  H('Buat tiga tombol berdampingan: Simpan (primary), Batal (outline-secondary), Hapus (danger, kecil).', 'btn btn-primary, btn btn-outline-secondary, btn btn-danger btn-sm.',
    '<div class="d-flex gap-2">\n  <button class="btn btn-primary">Simpan</button>\n  <button class="btn btn-outline-secondary">Batal</button>\n  <button class="btn btn-danger btn-sm">Hapus</button>\n</div>'),
],
'Sistem grid 12 kolom': [
  H('Buat tata letak sidebar 3 kolom dan konten 9 kolom mulai md, ditumpuk di ponsel.', 'row lalu col-md-3 dan col-md-9.',
    '<div class="container">\n  <div class="row g-3">\n    <aside class="col-md-3"><div class="p-3 bg-light border">Menu</div></aside>\n    <main class="col-md-9"><div class="p-3 border">Konten</div></main>\n  </div>\n</div>'),
  H('Buat satu kolom selebar 6 yang berada di tengah baris.', 'offset-3 menggeser kolom 3 satuan, atau justify-content-center pada row.',
    '<div class="row justify-content-center">\n  <div class="col-6"><div class="p-3 border text-center">Tengah</div></div>\n</div>'),
],
'Utilitas, tipografi, dan warna': [
  H('Buat bilah ringkasan: teks kiri "Total belanja", angka kanan tebal berwarna hijau, sejajar vertikal, padding 3, garis tepi, sudut membulat.', 'd-flex justify-content-between align-items-center p-3 border rounded; fw-bold text-success.',
    '<div class="d-flex justify-content-between align-items-center p-3 border rounded">\n  <span>Total belanja</span>\n  <span class="fw-bold text-success fs-5">Rp66.150</span>\n</div>'),
  H('Sembunyikan kolom keterangan di ponsel dan tampilkan mulai lg.', 'd-none d-lg-block.',
    '<p class="d-none d-lg-block text-body-secondary">Keterangan tambahan untuk layar lebar.</p>'),
],
'Tombol, kartu, alert, dan badge': [
  H('Buat alert sukses yang bisa ditutup dengan tombol silang.', 'alert alert-success alert-dismissible fade show + button.btn-close data-bs-dismiss="alert".',
    '<div class="alert alert-success alert-dismissible fade show" role="alert">\n  Pesanan berhasil dibuat.\n  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Tutup"></button>\n</div>'),
  H('Buat tiga kartu produk sama tinggi berdampingan mulai md.', 'row row-cols-1 row-cols-md-3 g-3 dan card h-100.',
    '<div class="row row-cols-1 row-cols-md-3 g-3">\n  <div class="col"><div class="card h-100"><div class="card-body"><h5 class="card-title">Kopi Gayo</h5><p class="card-text">Rp85.000</p></div></div></div>\n  <div class="col"><div class="card h-100"><div class="card-body"><h5 class="card-title">Kopi Toraja</h5><p class="card-text">Rp90.000</p></div></div></div>\n  <div class="col"><div class="card h-100"><div class="card-body"><h5 class="card-title">Kopi Kintamani</h5><p class="card-text">Rp80.000</p></div></div></div>\n</div>'),
],
'Navbar yang bisa dilipat': [
  H('Ubah navbar agar melebar mulai md (bukan lg) dan menu rata kanan.', 'navbar-expand-md; tambahkan ms-auto pada ul.navbar-nav.',
    '<nav class="navbar navbar-expand-md bg-body-tertiary">\n  <div class="container-fluid">\n    <a class="navbar-brand" href="#">RuangKode</a>\n    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu" aria-controls="menu" aria-expanded="false" aria-label="Buka menu"><span class="navbar-toggler-icon"></span></button>\n    <div class="collapse navbar-collapse" id="menu">\n      <ul class="navbar-nav ms-auto">\n        <li class="nav-item"><a class="nav-link" href="#">Beranda</a></li>\n        <li class="nav-item"><a class="nav-link" href="#">Kursus</a></li>\n      </ul>\n    </div>\n  </div>\n</nav>'),
],
'Form dan validasi': [
  H('Buat dua field berdampingan (Nama depan, Nama belakang) mulai md memakai grid di dalam form.', 'div.row.g-3 lalu col-md-6 untuk setiap field.',
    '<form class="row g-3">\n  <div class="col-md-6"><label class="form-label" for="dp">Nama depan</label><input id="dp" class="form-control"></div>\n  <div class="col-md-6"><label class="form-label" for="bl">Nama belakang</label><input id="bl" class="form-control"></div>\n</form>'),
  H('Buat kotak centang persetujuan yang wajib dicentang, terpisah dari kotak centang langganan berita.', 'form-check + form-check-input + form-check-label; required hanya pada persetujuan.',
    '<div class="form-check">\n  <input class="form-check-input" type="checkbox" id="setuju" required>\n  <label class="form-check-label" for="setuju">Saya menyetujui pemrosesan data untuk pendaftaran</label>\n  <div class="invalid-feedback">Centang untuk melanjutkan.</div>\n</div>\n<div class="form-check">\n  <input class="form-check-input" type="checkbox" id="berita">\n  <label class="form-check-label" for="berita">Kirimi saya info kelas baru (opsional)</label>\n</div>'),
],
'Modal dan komponen JavaScript': [
  H('Buka modal lewat JavaScript, bukan atribut data, saat halaman selesai dimuat.', 'new bootstrap.Modal(elemen).show().',
    '<script>\n  const m = new bootstrap.Modal(document.getElementById(\'konfirmasi\'));\n  m.show();\n</script>'),
  H('Buat modal yang berada di tengah layar dan tidak tertutup saat area luar diklik.', 'modal-dialog-centered; data-bs-backdrop="static" pada .modal.',
    '<div class="modal fade" id="info" data-bs-backdrop="static" tabindex="-1" aria-hidden="true">\n  <div class="modal-dialog modal-dialog-centered">\n    <div class="modal-content">\n      <div class="modal-body">Pembayaran sedang diproses.</div>\n      <div class="modal-footer"><button class="btn btn-primary" data-bs-dismiss="modal">Mengerti</button></div>\n    </div>\n  </div>\n</div>'),
],
'Variabel CSS, Sass, dan mode gelap': [
  H('Ubah sudut membulat semua komponen menjadi lebih besar lewat variabel CSS.', 'Timpa --bs-border-radius (dan variannya) di :root.',
    '<style>\n  :root {\n    --bs-border-radius: .75rem;\n    --bs-border-radius-lg: 1rem;\n    --bs-border-radius-sm: .5rem;\n  }\n</style>'),
  H('Tulis file Sass yang mengganti warna primer menjadi #B4532A dan font dasar menjadi Inter.', 'Variabel Sass ditulis sebelum @import bootstrap.',
    '// main.scss\n$primary: #B4532A;\n$font-family-base: "Inter", system-ui, sans-serif;\n\n@import "bootstrap/scss/bootstrap";'),
],
'Proyek: halaman kursus': [
  H('Tambahkan bagian FAQ memakai accordion Bootstrap dengan dua pertanyaan.', 'accordion > accordion-item > accordion-header (button) + accordion-collapse.',
    '<div class="accordion container mb-5" id="faq">\n  <div class="accordion-item">\n    <h2 class="accordion-header"><button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#q1">Apakah gratis?</button></h2>\n    <div id="q1" class="accordion-collapse collapse show" data-bs-parent="#faq"><div class="accordion-body">Ya, semua materi gratis.</div></div>\n  </div>\n  <div class="accordion-item">\n    <h2 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#q2">Perlu instal sesuatu?</button></h2>\n    <div id="q2" class="accordion-collapse collapse" data-bs-parent="#faq"><div class="accordion-body">Cukup browser untuk sebagian besar latihan.</div></div>\n  </div>\n</div>'),
],
}

BS_QX = {
'Sistem grid 12 kolom': [q('Titik henti lg di Bootstrap 5 mulai lebar?', ['768px', '992px', '1200px'], 1, 'sm 576, md 768, lg 992, xl 1200, xxl 1400.')],
'Tombol, kartu, alert, dan badge': [q('Atribut untuk tombol penutup alert?', ['data-bs-dismiss="alert"', 'data-close', 'onclick="hide()"'], 0, 'Sama polanya dengan modal.')],
'Form dan validasi': [q('Kelas untuk menandai satu input tidak valid secara manual?', ['is-invalid', 'invalid', 'has-error'], 0, 'is-valid untuk yang benar.')],
}

TW_MORE = [
M('Efek, posisi, dan interaksi', 'Menengah', 'Posisi dan lapisan, transformasi dan animasi, menu interaktif dengan sedikit JavaScript, dan apa yang baru di Tailwind v4.', ['Position', 'Transforms', 'Animation', 'Tailwind v4'], [
  W('Posisi, z-index, dan overflow',
    ['<code>relative</code> menjadikan elemen patokan, lalu anak <code>absolute</code> diletakkan dengan <code>top-2</code>, <code>right-2</code>, <code>inset-0</code>. <code>fixed</code> menempel di layar, dan <code>sticky top-0</code> menempel saat digulir.',
     'Lapisan diatur dengan <code>z-10</code>, <code>z-20</code>, sampai <code>z-50</code>. Konten yang meluber diatur dengan <code>overflow-hidden</code>, <code>overflow-auto</code>, atau <code>overflow-x-auto</code> (untuk tabel lebar).',
     'Pola umum: lencana di pojok gambar, header lengket, dan lapisan gelap di atas gambar hero.'],
    html='''<header class="sticky top-0 z-10 bg-white/90 backdrop-blur border-b px-4 py-3 font-bold">Header lengket</header>
<div class="p-4 space-y-4">
  <div id="foto" class="w-56 h-36 rounded-xl bg-gradient-to-br from-amber-300 to-rose-400">
    <span id="lencana" class="px-2 py-1 text-xs font-bold text-white bg-rose-600 rounded">Baru</span>
  </div>
  <p class="text-slate-600">Gulir ke bawah untuk melihat header tetap di atas.</p>
  <div class="h-64"></div>
</div>''',
    fw='tw',
    task={'q': 'Taruh lencana di pojok kanan atas foto: beri <code>#foto</code> kelas <code>relative</code> dan lencana kelas <code>absolute top-2 right-2</code>.',
          'test': "(f=>f.classList.contains('relative'))(document.getElementById('foto'))&&(l=>['absolute','top-2','right-2'].every(c=>l.classList.contains(c)))(document.getElementById('lencana'))",
          'hint': 'Induk relative menjadi patokan posisi anak absolute.'},
    pts=['relative + absolute untuk posisi di dalam elemen.', 'sticky top-0 untuk header lengket.', 'z-* untuk urutan lapisan.'],
    qs=[q('Agar anak absolute diposisikan terhadap induknya, induk diberi kelas?', ['relative', 'static', 'block'], 0, 'Tanpa relative, patokannya elemen lain di atasnya.')]),
  W('Transform, transisi, dan animasi',
    ['Transformasi: <code>scale-105</code>, <code>rotate-6</code>, <code>-translate-y-1</code>. Gabungkan dengan variant: <code>hover:-translate-y-1</code> membuat kartu terangkat saat di-hover.',
     'Transisi: <code>transition</code> (warna, opasitas, transform), <code>duration-300</code>, dan <code>ease-out</code>. Tanpa kelas transition, perubahan terjadi seketika.',
     'Animasi bawaan: <code>animate-spin</code> (ikon memuat), <code>animate-pulse</code> (skeleton loading), <code>animate-bounce</code>, <code>animate-ping</code>. Hormati pengguna yang memilih mengurangi animasi dengan <code>motion-reduce:animate-none</code>.'],
    html='''<div class="p-6 space-y-6">
  <div id="kartu" class="w-60 p-5 bg-white border rounded-xl shadow-sm">Arahkan kursor ke kartu ini</div>
  <div class="flex items-center gap-3">
    <div class="w-6 h-6 border-4 border-sky-500 border-t-transparent rounded-full animate-spin motion-reduce:animate-none"></div>
    <span>Memuat data...</span>
  </div>
  <div class="w-60 space-y-2 animate-pulse">
    <div class="h-4 bg-slate-200 rounded"></div>
    <div class="h-4 w-2/3 bg-slate-200 rounded"></div>
  </div>
</div>''',
    fw='tw',
    task={'q': 'Buat kartu terangkat saat di-hover: tambahkan <code>transition</code>, <code>hover:-translate-y-1</code>, dan <code>hover:shadow-lg</code>.',
          'test': "(k=>['transition','hover:-translate-y-1','hover:shadow-lg'].every(c=>k.classList.contains(c)))(document.getElementById('kartu'))",
          'hint': 'Tiga kelas itu ditambahkan pada div#kartu.'},
    pts=['scale, rotate, translate untuk transformasi.', 'transition + duration agar halus.', 'animate-spin, animate-pulse; motion-reduce untuk aksesibilitas.'],
    qs=[q('Animasi yang cocok untuk skeleton loading?', ['animate-pulse', 'animate-bounce', 'animate-spin'], 0, 'Denyut halus menandakan konten sedang dimuat.')]),
  W('Menu ponsel dengan sedikit JavaScript',
    ['Tailwind hanya mengurus tampilan. Untuk interaksi seperti membuka menu, cukup JavaScript kecil yang menambah atau membuang kelas: <code>menu.classList.toggle(\'hidden\')</code>.',
     'Jangan lupa aksesibilitas: perbarui <code>aria-expanded</code> pada tombol agar pembaca layar tahu menu sedang terbuka atau tertutup.',
     'Di proyek React atau Vue, kelas ditentukan dari state, misalnya <code>className={buka ? \'block\' : \'hidden\'}</code>.'],
    html='''<nav class="bg-slate-900 text-white">
  <div class="flex items-center justify-between p-4">
    <b>RuangKode</b>
    <button id="tombol" class="px-3 py-1 border border-white/40 rounded" aria-expanded="false" aria-controls="menu">Menu</button>
  </div>
  <div id="menu" class="hidden flex-col gap-2 px-4 pb-4">
    <a class="block">Beranda</a><a class="block">Kursus</a><a class="block">Masuk</a>
  </div>
</nav>''',
    js='''const tombol = document.getElementById('tombol');
const menu = document.getElementById('menu');
tombol.addEventListener('click', () => {
  // tulis kodemu di sini: tampilkan/sembunyikan menu
});''',
    fw='tw',
    task={'q': 'Lengkapi JavaScript: saat tombol diklik, toggle kelas <code>hidden</code> pada menu dan perbarui <code>aria-expanded</code>. Klik tombolnya sekali lalu tekan Periksa.',
          'test': "(m=>!m.classList.contains('hidden'))(document.getElementById('menu'))&&document.getElementById('tombol').getAttribute('aria-expanded')==='true'",
          'hint': "const buka = menu.classList.toggle('hidden') === false; tombol.setAttribute('aria-expanded', buka);"},
    pts=['Tailwind untuk gaya, JS kecil untuk interaksi.', 'classList.toggle(\'hidden\').', 'Perbarui aria-expanded.'],
    qs=[q('classList.toggle(\'hidden\') mengembalikan true jika?', ['Kelas baru saja ditambahkan', 'Kelas dihapus', 'Selalu true'], 0, 'true = kelas sekarang ada.')]),
  C('Tailwind v4: apa yang baru dan cara migrasi', [
     'Tailwind v4 (rilis 2025) ditulis ulang agar jauh lebih cepat. Perubahan terbesar: konfigurasi pindah dari <code>tailwind.config.js</code> ke CSS. Kamu cukup menulis <code>@import "tailwindcss";</code> dan mengatur tema dengan <code>@theme</code>.',
     'Deteksi file otomatis (tidak perlu lagi mengisi <code>content</code>), warna bawaan memakai ruang warna OKLCH yang lebih cerah, dan fitur CSS modern seperti container query (<code>@container</code> dan <code>@md:</code>) sudah bawaan.',
     'Beberapa nama kelas berubah, misalnya <code>shadow-sm</code> menjadi <code>shadow-xs</code> dan <code>rounded</code> sekarang setara <code>rounded-sm</code> lama. Jalankan <code>npx @tailwindcss/upgrade</code> untuk memigrasi proyek v3 secara otomatis, lalu periksa hasilnya.'],
    '/* v3: tailwind.config.js */\n/* module.exports = {\n     content: ["./src/**/*.{html,js}"],\n     theme: { extend: { colors: { merek: "#B4532A" } } }\n   } */\n\n/* v4: semuanya di CSS */\n@import "tailwindcss";\n\n@theme {\n  --color-merek: #B4532A;\n  --font-judul: "Fraunces", serif;\n  --breakpoint-3xl: 1920px;\n}\n\n/* kelas buatan sendiri */\n@utility tengah {\n  display: grid;\n  place-items: center;\n}',
    None, lang='css',
    tb=[{'c': 'Tailwind v3 dibanding v4', 'h': ['Hal', 'v3', 'v4'], 'r': [['Konfigurasi', 'tailwind.config.js', '@theme di CSS'], ['Memuat', '@tailwind base/components/utilities', '@import "tailwindcss"'], ['Daftar file', 'content: [...] wajib', 'Otomatis'], ['Plugin Vite', 'postcss + autoprefixer', '@tailwindcss/vite'], ['Kelas khusus', '@layer components', '@utility'], ['Container query', 'Plugin terpisah', 'Bawaan (@container, @md:)']]}],
    so=[S('Tambahkan titik henti khusus <code>3xl</code> = 1920px dan warna <code>aksen</code> di Tailwind v4.', 'Variabel --breakpoint-* dan --color-* di dalam @theme.',
          '@import "tailwindcss";\n\n@theme {\n  --breakpoint-3xl: 1920px;\n  --color-aksen: #0F5F8A;\n}', lang='css'),
        S('Buat kartu yang berubah menjadi dua kolom saat wadahnya (bukan layar) selebar md, memakai container query v4.', 'Induk diberi kelas @container, anak memakai @md:grid-cols-2.',
          '<div class="@container">\n  <div class="grid grid-cols-1 @md:grid-cols-2 gap-4">\n    <img src="kopi.jpg" alt="Kopi Gayo" class="rounded-lg">\n    <p>Kopi Gayo dari dataran tinggi Aceh.</p>\n  </div>\n</div>', lang='html')],
    pts=['v4: @import "tailwindcss" dan @theme.', 'Deteksi file otomatis, container query bawaan.', 'npx @tailwindcss/upgrade untuk migrasi.'],
    qs=[q('Di v4, warna merek didaftarkan di mana?', ['tailwind.config.js', 'Blok @theme di CSS', 'package.json'], 1, 'Konfigurasi berbasis CSS.')]),
]),
]

BS_MORE = [
M('Komponen lanjutan Bootstrap', 'Menengah', 'Dropdown, tab, accordion, offcanvas, toast, tooltip, tabel, list group, dan pagination.', ['Dropdown', 'Tabs', 'Offcanvas', 'Toast', 'Tables'], [
  W('Dropdown, tab, dan accordion',
    ['<b>Dropdown</b>: tombol dengan <code>data-bs-toggle="dropdown"</code> dan daftar <code>.dropdown-menu</code> berisi <code>.dropdown-item</code>.',
     '<b>Tab</b>: <code>.nav.nav-tabs</code> berisi tombol <code>data-bs-toggle="tab"</code> yang menunjuk ke <code>.tab-pane</code> di dalam <code>.tab-content</code>.',
     '<b>Accordion</b>: daftar bagian yang bisa dilipat. Tambahkan <code>data-bs-parent</code> agar hanya satu bagian terbuka dalam satu waktu. Semua ini berjalan tanpa JavaScript tambahan.'],
    html='''<div class="container py-3">
  <div class="dropdown mb-3">
    <button class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Urutkan</button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Termurah</a></li>
      <li><a class="dropdown-item" href="#">Terbaru</a></li>
    </ul>
  </div>
  <ul class="nav nav-tabs" role="tablist">
    <li class="nav-item"><button class="nav-link active" data-bs-toggle="tab" data-bs-target="#deskripsi" type="button" role="tab">Deskripsi</button></li>
    <li class="nav-item"><button class="nav-link" data-bs-toggle="tab" data-bs-target="#ulasan" type="button" role="tab">Ulasan</button></li>
  </ul>
  <div id="isiTab" class="tab-content border border-top-0 p-3">
    <div class="tab-pane fade show active" id="deskripsi" role="tabpanel">Kopi arabika 250 gram.</div>
    <div class="tab-pane fade" id="ulasan" role="tabpanel">★★★★★ Enak sekali.</div>
  </div>
</div>''',
    fw='bs',
    task={'q': 'Tambahkan tab ketiga "Pengiriman" lengkap dengan tab-pane berisi teksnya.',
          'test': "document.querySelectorAll('.nav-tabs .nav-link').length>=3&&document.querySelectorAll('#isiTab .tab-pane').length>=3",
          'hint': 'Salin satu li.nav-item dan satu div.tab-pane, beri id baru, dan samakan data-bs-target dengan id itu.'},
    pts=['dropdown: data-bs-toggle="dropdown".', 'tab: data-bs-toggle="tab" + tab-pane.', 'accordion: data-bs-parent agar satu terbuka.'],
    qs=[q('Atribut accordion agar hanya satu bagian terbuka?', ['data-bs-parent', 'data-single', 'aria-expanded'], 0, 'Menunjuk ke wadah accordion.')]),
  W('Offcanvas, toast, dan tooltip',
    ['<b>Offcanvas</b> adalah panel yang meluncur dari tepi layar, cocok untuk menu samping atau filter di ponsel. Dibuka dengan <code>data-bs-toggle="offcanvas"</code>.',
     '<b>Toast</b> adalah notifikasi kecil yang muncul lalu hilang. Toast dan <b>tooltip</b> perlu diaktifkan dengan JavaScript: <code>new bootstrap.Toast(el).show()</code> dan <code>new bootstrap.Tooltip(el)</code>.',
     'Komponen yang perlu diaktifkan lewat JS ini disebut opt-in, karena demi performa Bootstrap tidak memasangnya otomatis.'],
    html='''<div class="container py-3 d-flex gap-2 flex-wrap">
  <button class="btn btn-outline-dark" data-bs-toggle="offcanvas" data-bs-target="#filter">Filter</button>
  <button id="btnToast" class="btn btn-success">Tambah ke keranjang</button>
  <button id="info" class="btn btn-outline-secondary" data-bs-toggle="tooltip" data-bs-title="Gratis ongkir di atas Rp100.000">Info ongkir</button>
</div>
<div class="offcanvas offcanvas-start" tabindex="-1" id="filter">
  <div class="offcanvas-header"><h5 class="offcanvas-title">Filter</h5><button class="btn-close" data-bs-dismiss="offcanvas" aria-label="Tutup"></button></div>
  <div class="offcanvas-body">Harga, kategori, rating...</div>
</div>
<div class="toast-container position-fixed bottom-0 end-0 p-3">
  <div id="notif" class="toast" role="status" aria-live="polite">
    <div class="toast-body">Produk ditambahkan ke keranjang.</div>
  </div>
</div>''',
    js='''document.getElementById('btnToast').addEventListener('click', () => {
  new bootstrap.Toast(document.getElementById('notif')).show();
});
// aktifkan tooltip di sini''',
    fw='bs',
    task={'q': 'Aktifkan tooltip pada tombol <code>#info</code> dengan <code>new bootstrap.Tooltip(...)</code>, lalu tekan Jalankan dan Periksa.',
          'test': "!!(window.bootstrap&&bootstrap.Tooltip.getInstance(document.getElementById('info')))",
          'hint': "new bootstrap.Tooltip(document.getElementById('info'));"},
    pts=['offcanvas untuk panel samping.', 'Toast dan tooltip diaktifkan dengan JS.', 'toast-container position-fixed untuk posisi.'],
    qs=[q('Komponen mana yang harus diaktifkan lewat JavaScript?', ['Tooltip', 'Card', 'Grid'], 0, 'Tooltip dan popover bersifat opt-in.')]),
  W('Tabel, list group, dan pagination',
    ['Tabel: <code>.table</code> lalu tambahan <code>.table-striped</code> (belang), <code>.table-hover</code>, <code>.table-sm</code>. Bungkus dengan <code>.table-responsive</code> agar tabel lebar bisa digulir di ponsel tanpa merusak halaman.',
     '<b>List group</b> (<code>.list-group</code> dan <code>.list-group-item</code>) cocok untuk daftar pengaturan atau riwayat, dan bisa dipadukan dengan badge.',
     '<b>Pagination</b> (<code>.pagination</code>, <code>.page-item</code>, <code>.page-link</code>) untuk berpindah halaman data. Tandai halaman aktif dengan <code>.active</code> dan <code>aria-current="page"</code>.'],
    html='''<div class="container py-3">
  <div class="table-responsive">
    <table id="tabel" class="table">
      <thead><tr><th>Produk</th><th class="text-end">Harga</th><th class="text-end">Stok</th></tr></thead>
      <tbody>
        <tr><td>Kopi Gayo</td><td class="text-end">85.000</td><td class="text-end">12</td></tr>
        <tr><td>Kopi Toraja</td><td class="text-end">90.000</td><td class="text-end">4</td></tr>
        <tr><td>Kopi Kintamani</td><td class="text-end">80.000</td><td class="text-end">0</td></tr>
      </tbody>
    </table>
  </div>
  <nav aria-label="Halaman produk">
    <ul class="pagination">
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
    </ul>
  </nav>
</div>''',
    fw='bs',
    task={'q': 'Beri tabel kelas <code>table-striped</code> dan <code>table-hover</code>, lalu tandai halaman 1 sebagai aktif (<code>active</code> pada li pertama).',
          'test': "(t=>t.classList.contains('table-striped')&&t.classList.contains('table-hover'))(document.getElementById('tabel'))&&document.querySelector('.pagination .page-item').classList.contains('active')",
          'hint': 'Tambahkan dua kelas pada table#tabel dan active pada li.page-item pertama.'},
    pts=['table + table-striped/hover, bungkus table-responsive.', 'list-group untuk daftar.', 'pagination dengan active dan aria-current.'],
    qs=[q('Kenapa tabel dibungkus .table-responsive?', ['Agar bisa digulir horizontal di layar sempit', 'Agar berwarna', 'Agar bisa diurutkan'], 0, 'Halaman tidak ikut melebar.')]),
  W('Utilitas lanjutan: stack, posisi, dan rasio',
    ['<code>.hstack</code> dan <code>.vstack</code> adalah jalan pintas flexbox dengan <code>gap-*</code>. <code>.ms-auto</code> mendorong elemen ke kanan.',
     'Posisi: <code>position-relative</code>, <code>position-absolute</code>, <code>top-0 start-100 translate-middle</code> untuk badge notifikasi di pojok tombol.',
     'Rasio: <code>.ratio .ratio-16x9</code> menjaga video atau gambar tetap proporsional. <code>object-fit-cover</code> memotong gambar agar penuh tanpa gepeng.'],
    html='''<div class="container py-3">
  <div class="hstack gap-3 p-3 border rounded">
    <b>Keranjang</b>
    <button id="lonceng" class="btn btn-primary ms-auto">
      Notifikasi
    </button>
  </div>
  <div class="ratio ratio-16x9 mt-3 bg-secondary-subtle rounded"><div class="d-flex align-items-center justify-content-center">Area video 16:9</div></div>
</div>''',
    fw='bs',
    task={'q': 'Tambahkan badge merah angka 3 di pojok kanan atas tombol: tombol diberi <code>position-relative</code>, badge diberi <code>position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger</code>.',
          'test': "(b=>b.classList.contains('position-relative')&&!!b.querySelector('.badge.position-absolute.bg-danger'))(document.getElementById('lonceng'))",
          'hint': '<span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">3</span> di dalam tombol.'},
    pts=['hstack/vstack + gap.', 'position-* + translate-middle untuk badge pojok.', 'ratio-16x9 untuk proporsi tetap.'],
    qs=[q('Kelas yang mendorong elemen ke kanan di dalam flex?', ['ms-auto', 'float-end', 'text-end'], 0, 'margin-start auto memakan ruang kosong.')]),
]),
]
