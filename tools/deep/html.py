"""Pendalaman jalur HTML: istilah dunia kerja dan contoh markup siap pakai."""
K = 'html'


def H(t, code, b=None, lang='html'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def J(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='js')


D = {
'Cara web bekerja': dict(
  ist=[('Request-response', 'Browser mengirim HTTP request, server membalas response berisi status, header, dan body.'),
       ('DNS', 'Sistem yang menerjemahkan nama domain (tokokopi.id) menjadi alamat IP server.'),
       ('Status code', '200 OK, 301/302 redirect, 404 tidak ditemukan, 500 error server.'),
       ('CDN', 'Content Delivery Network: salinan berkas statis di server dekat pengguna (Jakarta, Singapura) agar cepat.')],
  cx=[J('Membedah URL dan respons HTTP sungguhan', '''
import http from "node:http";
const server = http.createServer((req, res) => {
  res.writeHead(req.url === "/" ? 200 : 404, { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "max-age=3600" });
  res.end(req.url === "/" ? "<!doctype html><title>Toko</title><h1>Halo</h1>" : "<h1>404</h1>");
}).listen(0);
const port = server.address().port;
const url = new URL(`http://localhost:${port}/produk/kopi?warna=hitam&hal=2#ulasan`);
console.log({ protokol: url.protocol, host: url.hostname, path: url.pathname, query: Object.fromEntries(url.searchParams), hash: url.hash });
for (const path of ["/", "/produk/kopi"]) {
  const r = await fetch(`http://localhost:${port}${path}`);
  console.log(path, "->", r.status, r.statusText, "|", r.headers.get("content-type"), "|", (await r.text()).slice(0, 30));
}
server.close();
''', 'Hash (#ulasan) tidak pernah dikirim ke server; browser memakainya untuk menggulir ke elemen dengan id="ulasan".')]),

'Struktur dokumen HTML': dict(
  ist=[('<!doctype html>', 'Deklarasi agar browser memakai standards mode, bukan quirks mode.'),
       ('lang attribute', '<html lang="id"> membantu pembaca layar memilih pelafalan dan mesin pencari memahami bahasa.'),
       ('meta viewport', 'Wajib untuk halaman responsif agar lebar layout mengikuti lebar perangkat.'),
       ('Head vs body', 'head berisi metadata (judul, CSS, meta); body berisi konten yang terlihat.')],
  cx=[H('Kerangka dokumen standar produksi', '''
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kopi Gayo Arabika 250 g | Toko Kopi Nusantara</title>
  <meta name="description" content="Kopi Gayo arabika single origin, sangrai medium. Gratis ongkir Jabodetabek.">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/css/app.css">
  <script src="/js/app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#utama">Lewati ke konten utama</a>
  <header>…</header>
  <main id="utama">…</main>
  <footer>…</footer>
</body>
</html>''', 'Judul halaman berformat "Nama halaman | Nama situs" adalah konvensi SEO yang umum.')]),

'Tag, atribut & elemen': dict(
  ist=[('Element', 'Tag pembuka + isi + tag penutup; beberapa elemen kosong (img, input, br) tidak punya penutup.'),
       ('Global attribute', 'Atribut yang berlaku di semua elemen: id, class, hidden, title, lang, data-*.'),
       ('Boolean attribute', 'Atribut yang aktif hanya dengan ditulis: disabled, required, checked.'),
       ('Validator', 'validator.w3.org atau html-validate memeriksa kesalahan markup.')],
  cx=[H('Markup salah vs benar yang sering lolos tanpa disadari', '''
<!-- SALAH -->
<p>Promo <b>hari ini<p>diskon 20%</b>       <!-- p di dalam p, b tidak ditutup benar -->
<img src="kopi.jpg">                          <!-- tanpa alt -->
<button disabled="false">Bayar</button>       <!-- tetap disabled! nilai tidak berpengaruh -->
<div id="harga"></div><div id="harga"></div>  <!-- id harus unik -->

<!-- BENAR -->
<p>Promo <strong>hari ini</strong>: diskon 20%</p>
<img src="kopi.jpg" alt="Bungkus kopi Gayo 250 gram" width="400" height="400">
<button>Bayar</button>                        <!-- hapus atribut untuk mengaktifkan -->
<div id="harga-utama"></div><div id="harga-coret"></div>''')]),

'Judul & paragraf': dict(
  ist=[('Heading hierarchy', 'h1 sampai h6 membentuk kerangka dokumen; jangan melompati tingkat demi ukuran font.'),
       ('Satu h1', 'Praktik umum: satu h1 per halaman berisi topik utama.'),
       ('Document outline', 'Pembaca layar menavigasi lewat daftar heading; heading yang rapi = navigasi cepat.'),
       ('Line length', 'Paragraf nyaman dibaca pada 45-75 karakter per baris.')],
  cx=[H('Hierarki heading halaman artikel', '''
<main>
  <h1>Cara Menyeduh Kopi V60 di Rumah</h1>
  <p>Panduan ini cocok untuk pemula dan hanya butuh 10 menit.</p>
  <h2>Alat yang dibutuhkan</h2>
    <h3>Wajib</h3>
    <h3>Opsional</h3>
  <h2>Langkah menyeduh</h2>
    <h3>1. Bilas kertas filter</h3>
    <h3>2. Blooming 30 detik</h3>
  <h2>Kesalahan umum</h2>
</main>
<!-- Ukuran tampilan diatur CSS. Jangan memakai h4 hanya karena "ukurannya pas". -->''')]),

'Penekanan & teks khusus': dict(
  ist=[('strong vs b', 'strong = penting secara makna; b = tebal tanpa makna tambahan.'),
       ('em vs i', 'em = penekanan yang mengubah makna kalimat; i = istilah asing atau nama ilmiah.'),
       ('mark', 'Menandai teks yang relevan, misalnya kata kunci pencarian di hasil.'),
       ('time / abbr', 'time datetime="..." untuk tanggal yang bisa dibaca mesin; abbr untuk singkatan.')],
  cx=[H('Teks dengan makna yang bisa dibaca mesin', '''
<p><strong>Peringatan:</strong> stok tinggal 3.</p>
<p>Biji <i lang="la">Coffea arabica</i> ditanam di ketinggian 1.200 mdpl.</p>
<p>Hasil pencarian untuk "gayo": Kopi <mark>Gayo</mark> Arabika</p>
<p>Promo berakhir <time datetime="2026-11-30T23:59+07:00">30 November pukul 23.59 WIB</time>.</p>
<p>Harga sudah termasuk <abbr title="Pajak Pertambahan Nilai">PPN</abbr> 11%.</p>
<p>Harga: <del>Rp100.000</del> <ins>Rp85.000</ins></p>
<p>Tekan <kbd>Ctrl</kbd> + <kbd>K</kbd> untuk mencari.</p>''')]),

'Kutipan, kode & karakter khusus': dict(
  ist=[('blockquote / q / cite', 'Kutipan panjang, kutipan pendek, dan judul karya yang dikutip.'),
       ('pre / code', 'pre menjaga spasi dan baris; code menandai potongan kode.'),
       ('HTML entity', 'Penulisan karakter khusus: &lt; &gt; &amp; &nbsp; &copy;.'),
       ('Escaping', 'Mengubah < dan & menjadi entity agar tidak ditafsirkan sebagai tag; kunci mencegah XSS.')],
  cx=[H('Testimoni, potongan kode, dan entity', '''
<figure>
  <blockquote cite="https://contoh.id/ulasan/42">
    <p>Pengirimannya cepat, kopinya wangi sekali. Sudah langganan 6 bulan.</p>
  </blockquote>
  <figcaption>Rina, pelanggan dari Bandung</figcaption>
</figure>

<p>Untuk memasang, jalankan <code>npm install toko-ui</code>.</p>
<pre><code>&lt;button class="btn"&gt;Beli&lt;/button&gt;
if (a &lt; b &amp;&amp; c) { … }</code></pre>

<p>&copy; 2026 Toko Kopi Nusantara &middot; Rp&nbsp;85.000</p>''', '&nbsp; mencegah "Rp" dan angkanya terpisah ke dua baris.')]),

'details, summary & dialog: interaksi tanpa JavaScript': dict(
  ist=[('details / summary', 'Komponen buka-tutup bawaan yang aksesibel tanpa JavaScript; cocok untuk FAQ.'),
       ('name attribute pada details', 'Beberapa details dengan name sama menjadi accordion eksklusif (hanya satu terbuka).'),
       ('dialog', 'Modal bawaan; showModal() memberi fokus, backdrop, dan tombol Esc otomatis.'),
       ('Popover API', 'Atribut popover dan popovertarget untuk menu/tooltip tanpa JavaScript.')],
  cx=[H('FAQ accordion, modal konfirmasi, dan popover', '''
<details name="faq" open>
  <summary>Berapa lama pengiriman?</summary>
  <p>1-2 hari kerja untuk Jabodetabek, 3-5 hari untuk luar Jawa.</p>
</details>
<details name="faq">
  <summary>Bisa bayar di tempat (COD)?</summary>
  <p>Bisa untuk pesanan di bawah Rp1.000.000.</p>
</details>

<button popovertarget="info-ongkir">Info ongkir</button>
<div id="info-ongkir" popover>Gratis ongkir untuk belanja di atas Rp150.000.</div>

<button onclick="document.querySelector('#hapus').showModal()">Hapus akun</button>
<dialog id="hapus" aria-labelledby="judul-hapus">
  <form method="dialog">
    <h2 id="judul-hapus">Hapus akun permanen?</h2>
    <p>Riwayat pesanan akan hilang dan tidak bisa dikembalikan.</p>
    <button value="batal" autofocus>Batal</button>
    <button value="hapus">Ya, hapus</button>
  </form>
</dialog>''', 'form method="dialog" menutup modal dan mengisi dialog.returnValue dengan nilai tombol yang ditekan.')]),

'Link': dict(
  ist=[('Absolute vs relative URL', 'https://… lengkap vs /produk atau ../gambar.jpg relatif terhadap halaman.'),
       ('rel="noopener noreferrer"', 'Untuk link target="_blank" ke situs lain agar halaman baru tidak bisa mengakses window.opener.'),
       ('Descriptive link text', 'Teks link menjelaskan tujuan ("Unduh katalog PDF"), bukan "klik di sini".'),
       ('download / tel: / mailto:', 'Link untuk mengunduh, menelepon, atau membuka aplikasi email.')],
  cx=[H('Link yang aksesibel dan aman', '''
<nav aria-label="Navigasi utama">
  <a href="/" aria-current="page">Beranda</a>
  <a href="/produk">Produk</a>
  <a href="#kontak">Kontak</a>
</nav>

<!-- buruk -->
Katalog terbaru bisa diunduh <a href="/katalog.pdf">di sini</a>.
<!-- baik -->
<a href="/katalog-2026.pdf" download>Unduh katalog 2026 (PDF, 2,4 MB)</a>

<a href="https://wa.me/6281234567890?text=Halo%2C%20saya%20mau%20pesan" target="_blank" rel="noopener noreferrer">
  Pesan lewat WhatsApp <span class="sr-only">(membuka tab baru)</span>
</a>
<a href="tel:+622112345678">(021) 1234 5678</a>''')]),

'Gambar & figure': dict(
  ist=[('alt text', 'Deskripsi gambar untuk pembaca layar dan saat gambar gagal dimuat; alt="" untuk gambar dekoratif.'),
       ('width / height', 'Menulis ukuran asli mencegah Cumulative Layout Shift (konten melompat saat gambar dimuat).'),
       ('srcset / sizes', 'Browser memilih file gambar sesuai lebar layar dan kepadatan piksel.'),
       ('Modern formats', 'AVIF dan WebP jauh lebih kecil dari JPEG; gunakan picture untuk fallback.')],
  cx=[H('Gambar produk responsif dan cepat', '''
<figure>
  <picture>
    <source type="image/avif" srcset="kopi-400.avif 400w, kopi-800.avif 800w, kopi-1200.avif 1200w" sizes="(min-width: 768px) 50vw, 100vw">
    <source type="image/webp" srcset="kopi-400.webp 400w, kopi-800.webp 800w, kopi-1200.webp 1200w" sizes="(min-width: 768px) 50vw, 100vw">
    <img src="kopi-800.jpg" alt="Kopi Gayo dalam kemasan cokelat 250 gram dengan biji kopi di sekitarnya"
         width="800" height="800" loading="lazy" decoding="async">
  </picture>
  <figcaption>Kopi Gayo Arabika, sangrai medium.</figcaption>
</figure>

<!-- Gambar utama di atas lipatan: jangan lazy, beri prioritas -->
<img src="hero.webp" alt="" width="1600" height="600" fetchpriority="high">''', 'Gambar hero dekoratif memakai alt="" agar pembaca layar melewatinya, dan tidak di-lazy-load karena memengaruhi LCP.')]),

'Audio, video & iframe': dict(
  ist=[('controls / muted / playsinline', 'Atribut video; autoplay di browser modern hanya diizinkan jika muted.'),
       ('track (captions)', 'Berkas WebVTT untuk teks terjemahan dan aksesibilitas tunarungu.'),
       ('iframe sandbox', 'Membatasi apa yang boleh dilakukan konten tersemat (skrip, form, popup).'),
       ('loading="lazy" pada iframe', 'Menunda memuat peta atau video sampai mendekati layar.')],
  cx=[H('Video produk dengan teks dan peta yang aman', '''
<video controls preload="metadata" poster="seduh-poster.jpg" width="1280" height="720" playsinline>
  <source src="cara-seduh.webm" type="video/webm">
  <source src="cara-seduh.mp4" type="video/mp4">
  <track kind="captions" src="cara-seduh.id.vtt" srclang="id" label="Bahasa Indonesia" default>
  Browser Anda tidak mendukung video. <a href="cara-seduh.mp4">Unduh videonya</a>.
</video>

<iframe src="https://www.google.com/maps/embed?pb=…" title="Lokasi toko di peta"
        width="600" height="400" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        sandbox="allow-scripts allow-same-origin allow-popups"></iframe>''')]),

'Daftar': dict(
  ist=[('ul / ol / li', 'Daftar tanpa urutan, daftar berurutan, dan butirnya.'),
       ('dl / dt / dd', 'Daftar deskripsi: pasangan istilah dan penjelasan, cocok untuk spesifikasi produk.'),
       ('Semantic navigation', 'Menu navigasi umumnya ul di dalam nav; pembaca layar menyebut jumlah item.'),
       ('ol start / reversed', 'Mengatur nomor awal atau urutan mundur, misalnya peringkat.')],
  cx=[H('Langkah, spesifikasi, dan menu', '''
<ol>
  <li>Tambahkan produk ke keranjang</li>
  <li>Isi alamat pengiriman</li>
  <li>Pilih pembayaran (QRIS, VA, COD)</li>
</ol>

<dl class="spesifikasi">
  <dt>Asal</dt>      <dd>Aceh Tengah</dd>
  <dt>Proses</dt>    <dd>Semi-washed</dd>
  <dt>Ketinggian</dt><dd>1.200-1.600 mdpl</dd>
  <dt>Catatan rasa</dt><dd>Cokelat, rempah</dd><dd>Keasaman rendah</dd>
</dl>

<ol reversed start="3"><li>Toraja</li><li>Kintamani</li><li>Gayo</li></ol>''')]),

'Tabel': dict(
  ist=[('thead / tbody / tfoot', 'Mengelompokkan baris judul, isi, dan ringkasan tabel.'),
       ('th scope', 'scope="col" atau "row" memberi tahu pembaca layar header mana yang berlaku untuk sel.'),
       ('caption', 'Judul tabel yang dibacakan pertama oleh pembaca layar.'),
       ('Tabel untuk data, bukan layout', 'Tata letak halaman memakai CSS Grid/Flexbox; tabel hanya untuk data tabular.')],
  cx=[H('Tabel laporan penjualan yang aksesibel', '''
<div class="tabel-gulir" role="region" aria-labelledby="cap-jual" tabindex="0">
  <table>
    <caption id="cap-jual">Penjualan per cabang, Oktober 2026</caption>
    <thead>
      <tr><th scope="col">Cabang</th><th scope="col">Transaksi</th><th scope="col">Omzet</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">Bandung</th><td>1.204</td><td>Rp182.400.000</td></tr>
      <tr><th scope="row">Medan</th><td>987</td><td>Rp141.900.000</td></tr>
    </tbody>
    <tfoot>
      <tr><th scope="row">Total</th><td>2.191</td><td>Rp324.300.000</td></tr>
    </tfoot>
  </table>
</div>''', 'Pembungkus dengan tabindex dan overflow-x: auto membuat tabel lebar bisa digulir di ponsel dengan keyboard maupun sentuhan.')]),

'Form, label & input': dict(
  ist=[('label for', 'Menghubungkan label ke input; klik label memfokuskan input dan pembaca layar membacanya.'),
       ('name attribute', 'Kunci data saat form dikirim; tanpa name, nilai input tidak terkirim.'),
       ('autocomplete', 'Petunjuk isi otomatis (email, tel, street-address, one-time-code) yang mempercepat pengisian.'),
       ('fieldset / legend', 'Mengelompokkan input terkait, wajib untuk grup radio.')],
  cx=[H('Form alamat pengiriman yang ramah isi otomatis', '''
<form action="/checkout" method="post">
  <label for="nama">Nama penerima</label>
  <input id="nama" name="nama" autocomplete="name" required>

  <label for="hp">Nomor HP</label>
  <input id="hp" name="hp" type="tel" inputmode="numeric" autocomplete="tel" placeholder="0812xxxxxxx" required>

  <label for="alamat">Alamat lengkap</label>
  <textarea id="alamat" name="alamat" autocomplete="street-address" rows="3" required></textarea>

  <fieldset>
    <legend>Metode pengiriman</legend>
    <label><input type="radio" name="kirim" value="reguler" checked> Reguler (2-3 hari)</label>
    <label><input type="radio" name="kirim" value="instan"> Instan (hari ini)</label>
  </fieldset>

  <label for="otp">Kode OTP</label>
  <input id="otp" name="otp" inputmode="numeric" autocomplete="one-time-code" maxlength="6">
  <button type="submit">Lanjut ke pembayaran</button>
</form>''', 'autocomplete="one-time-code" membuat iOS dan Android menawarkan kode OTP dari SMS secara otomatis.')]),

'Validasi bawaan': dict(
  ist=[('Constraint validation', 'Atribut required, min, max, minlength, pattern, type="email" divalidasi browser sebelum submit.'),
       (':user-invalid', 'Pseudo-class CSS yang aktif setelah pengguna berinteraksi, sehingga error tidak muncul sebelum mengetik.'),
       ('setCustomValidity', 'Pesan validasi kustom dari JavaScript, misalnya konfirmasi kata sandi.'),
       ('Server-side validation', 'Validasi browser bisa dilewati; server wajib memvalidasi ulang.')],
  cx=[H('Validasi bawaan + pesan kustom', '''
<form>
  <label for="email">Email</label>
  <input id="email" type="email" name="email" required>

  <label for="sandi">Kata sandi</label>
  <input id="sandi" type="password" name="sandi" minlength="8" required
         pattern="(?=.*\\d)(?=.*[a-zA-Z]).{8,}" aria-describedby="aturan-sandi">
  <p id="aturan-sandi">Minimal 8 karakter, berisi huruf dan angka.</p>

  <label for="ulang">Ulangi kata sandi</label>
  <input id="ulang" type="password" required>

  <label for="jumlah">Jumlah (1-10)</label>
  <input id="jumlah" type="number" min="1" max="10" step="1" value="1">
  <button>Daftar</button>
</form>
<style> input:user-invalid { border-color: #c62828; } </style>
<script>
  const ulang = document.querySelector("#ulang");
  ulang.addEventListener("input", () => {
    ulang.setCustomValidity(ulang.value === sandi.value ? "" : "Kata sandi tidak sama");
  });
</script>''')]),

'Unggah file': dict(
  ist=[('enctype="multipart/form-data"', 'Wajib di form yang mengirim file.'),
       ('accept', 'Membatasi jenis file yang ditawarkan pemilih file (image/*, .pdf); tetap periksa di server.'),
       ('capture', 'Di ponsel, membuka kamera langsung untuk foto KTP atau bukti transfer.'),
       ('Upload security', 'Server memeriksa ukuran, tipe sebenarnya (magic bytes), dan menyimpan dengan nama acak di luar folder publik.')],
  cx=[H('Unggah bukti transfer dengan pratinjau dan batas ukuran', '''
<form action="/bukti" method="post" enctype="multipart/form-data">
  <label for="bukti">Foto bukti transfer (JPG/PNG, maks 2 MB)</label>
  <input id="bukti" name="bukti" type="file" accept="image/jpeg,image/png" capture="environment" required>
  <img id="pratinjau" alt="" hidden width="240">
  <p id="pesan" role="alert"></p>
  <button>Kirim</button>
</form>
<script>
  bukti.addEventListener("change", () => {
    const f = bukti.files[0];
    if (f && f.size > 2 * 1024 * 1024) {
      pesan.textContent = "Ukuran file lebih dari 2 MB."; bukti.value = ""; return;
    }
    pesan.textContent = "";
    pratinjau.src = URL.createObjectURL(f); pratinjau.alt = "Pratinjau bukti transfer"; pratinjau.hidden = false;
  });
</script>''')]),

'Tipe input modern & datalist': dict(
  ist=[('Input types', 'date, time, datetime-local, color, range, search, url, tel memberi keyboard dan pemilih yang tepat.'),
       ('inputmode', 'Petunjuk keyboard virtual (numeric, decimal, email) tanpa mengubah validasi.'),
       ('datalist', 'Saran isian (autocomplete) yang tetap mengizinkan nilai bebas.'),
       ('output', 'Elemen untuk menampilkan hasil perhitungan dari input.')],
  cx=[H('Form pemesanan meja dengan input modern', '''
<form oninput="hasil.value = (orang.valueAsNumber * 75000).toLocaleString('id-ID')">
  <label for="tgl">Tanggal</label>
  <input id="tgl" type="date" min="2026-11-20" max="2026-12-31" required>

  <label for="jam">Jam</label>
  <input id="jam" type="time" min="10:00" max="21:00" step="1800" required>

  <label for="orang">Jumlah orang: <output for="orang" id="jumlah-orang">2</output></label>
  <input id="orang" type="range" min="1" max="12" value="2"
         oninput="this.previousElementSibling.querySelector('output').value = this.value">

  <label for="cabang">Cabang</label>
  <input id="cabang" list="daftar-cabang" placeholder="Ketik nama kota">
  <datalist id="daftar-cabang">
    <option value="Bandung - Dago"><option value="Bandung - Braga"><option value="Jakarta - Kemang">
  </datalist>

  <p>Perkiraan minimum: Rp<output name="hasil" for="orang">150.000</output></p>
</form>''')]),

'Elemen semantik': dict(
  ist=[('Semantic HTML', 'Elemen yang menjelaskan makna konten (header, nav, main, article, aside, footer).'),
       ('Landmark', 'Wilayah halaman yang bisa dilompati pembaca layar; dibentuk otomatis oleh elemen semantik.'),
       ('article vs section', 'article berdiri sendiri (postingan, kartu produk); section bagian bertema dengan heading.'),
       ('Div soup', 'Halaman yang seluruhnya div; sulit diakses, sulit dibaca, dan lemah untuk SEO.')],
  cx=[H('Kerangka halaman toko dengan landmark', '''
<header>
  <a href="/" aria-label="Toko Kopi Nusantara, beranda"><img src="logo.svg" alt="" width="120" height="32"></a>
  <nav aria-label="Utama">…</nav>
  <search><form role="search"><input type="search" aria-label="Cari produk"></form></search>
</header>
<main>
  <h1>Kopi Single Origin</h1>
  <section aria-labelledby="terlaris">
    <h2 id="terlaris">Terlaris minggu ini</h2>
    <article class="kartu-produk">
      <h3>Kopi Gayo</h3> <p>Rp85.000</p>
    </article>
  </section>
  <aside aria-label="Promo">Gratis ongkir di atas Rp150.000</aside>
</main>
<footer>
  <address>Jl. Braga No. 10, Bandung · <a href="mailto:halo@tokokopi.id">halo@tokokopi.id</a></address>
</footer>''')]),

'div, span, class & data-*': dict(
  ist=[('div / span', 'Pembungkus tanpa makna: div untuk blok, span untuk potongan teks.'),
       ('class naming', 'Nama kelas menjelaskan peran (kartu-produk, tombol-utama), bukan tampilan (merah-besar).'),
       ('data-* attribute', 'Menyimpan data kecil untuk JavaScript; dibaca lewat element.dataset.'),
       ('Hook class', 'Kelas khusus JavaScript seperti js-tambah agar refaktor CSS tidak merusak perilaku.')],
  cx=[H('Kartu produk dengan data-* untuk JavaScript', '''
<article class="kartu-produk" data-sku="KP-GAYO-250" data-harga="85000" data-stok="3">
  <h3 class="kartu-produk__judul">Kopi Gayo</h3>
  <p class="kartu-produk__harga">Rp<span class="angka">85.000</span></p>
  <span class="lencana lencana--peringatan">Sisa 3</span>
  <button class="tombol tombol--utama" data-aksi="tambah">Tambah</button>
</article>
<script>
  document.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-aksi='tambah']");
    if (!btn) return;
    const { sku, harga, stok } = btn.closest("[data-sku]").dataset;   // data-sku -> dataset.sku
    console.log(sku, Number(harga), Number(stok));
  });
</script>''')]),

'Memasang CSS': dict(
  ist=[('External stylesheet', '<link rel="stylesheet"> ke berkas .css; bisa di-cache browser dan dipakai banyak halaman.'),
       ('Render-blocking', 'CSS di head menahan render sampai selesai dimuat; jaga ukurannya kecil.'),
       ('Critical CSS', 'CSS minimum untuk tampilan awal ditulis inline agar halaman cepat tampil.'),
       ('media attribute', 'Stylesheet khusus (print, layar lebar) tidak memblokir render saat tidak cocok.')],
  cx=[H('Tiga cara memasang CSS dan kapan memakainya', '''
<head>
  <!-- 1. Inline critical CSS: tampilan di atas lipatan, kecil (< 14 KB) -->
  <style>
    body{margin:0;font-family:system-ui,sans-serif} .hero{min-height:60vh;display:grid;place-items:center}
  </style>
  <!-- 2. Eksternal: berkas utama, nama ber-hash agar bisa di-cache lama -->
  <link rel="stylesheet" href="/assets/app.3f9a1c.css">
  <!-- 3. Kondisional: tidak memblokir render di layar -->
  <link rel="stylesheet" href="/assets/print.css" media="print">
  <link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
</head>
<!-- Hindari style="" di elemen kecuali nilai dinamis dari JavaScript (misalnya --progress: 40%) -->''')]),

'Memuat JavaScript': dict(
  ist=[('defer', 'Unduh paralel, jalankan setelah HTML selesai di-parse, sesuai urutan; pilihan default untuk skrip aplikasi.'),
       ('async', 'Unduh paralel, jalankan segera setelah selesai tanpa urutan; cocok untuk analitik.'),
       ('type="module"', 'Skrip ES module; otomatis defer dan mendukung import.'),
       ('Third-party script', 'Skrip pihak ketiga (chat, iklan) memperlambat halaman dan berisiko keamanan; muat seperlunya.')],
  cx=[H('Urutan pemuatan skrip yang tepat', '''
<head>
  <!-- aplikasi: module (defer otomatis), tidak memblokir parsing -->
  <script type="module" src="/assets/main.8b2e.js"></script>
  <!-- analitik: async, urutan tidak penting -->
  <script async src="https://analytics.contoh.id/a.js"></script>
  <!-- skrip lama tanpa module -->
  <script defer src="/assets/legacy.js"></script>
</head>
<body>
  …
  <!-- widget chat dimuat hanya setelah pengguna menekan tombol -->
  <button id="buka-chat">Chat dengan CS</button>
  <script type="module">
    document.querySelector("#buka-chat").addEventListener("click", async () => {
      const { mulaiChat } = await import("/assets/chat.js");
      mulaiChat();
    }, { once: true });
  </script>
</body>''')]),

'Aksesibilitas dasar': dict(
  ist=[('WCAG 2.2 AA', 'Standar aksesibilitas web yang menjadi acuan regulasi (dan European Accessibility Act sejak 2025).'),
       ('Keyboard accessible', 'Semua fungsi bisa dipakai dengan Tab, Enter, Space, dan Esc; fokus selalu terlihat.'),
       ('ARIA', 'Atribut tambahan untuk pembaca layar; aturan pertama ARIA: pakai elemen HTML asli jika bisa.'),
       ('Screen reader', 'Pembaca layar seperti NVDA, JAWS, VoiceOver, dan TalkBack.')],
  cx=[H('Tombol palsu vs tombol asli, dan pesan status', '''
<!-- BURUK: tidak bisa difokus, tidak bisa ditekan dengan keyboard, tidak diumumkan sebagai tombol -->
<div class="btn" onclick="simpan()">Simpan</div>

<!-- BAIK: fokus, Enter/Space, dan peran tombol didapat gratis -->
<button type="button" onclick="simpan()">Simpan</button>

<!-- Tombol ikon wajib punya nama yang bisa dibaca -->
<button aria-label="Hapus Kopi Gayo dari keranjang"><svg aria-hidden="true">…</svg></button>

<!-- Pesan yang muncul dinamis diumumkan pembaca layar -->
<p role="status" aria-live="polite" id="status-keranjang"></p>

<!-- Error terhubung ke input -->
<label for="hp">Nomor HP</label>
<input id="hp" aria-invalid="true" aria-describedby="hp-error">
<p id="hp-error">Nomor HP harus diawali 08 atau +62.</p>''')]),

'Meta tag & SEO dasar': dict(
  ist=[('title & meta description', 'Judul dan ringkasan yang tampil di hasil pencarian; unik untuk setiap halaman.'),
       ('Canonical URL', 'link rel="canonical" menunjuk versi utama halaman agar duplikat (filter, UTM) tidak bersaing.'),
       ('robots', 'meta name="robots" content="noindex" untuk halaman yang tidak boleh muncul di pencarian.'),
       ('sitemap.xml & robots.txt', 'Berkas untuk membantu mesin pencari menemukan dan menjelajah halaman.')],
  cx=[H('Head halaman produk yang siap SEO', '''
<head>
  <title>Kopi Gayo Arabika 250 g - Sangrai Medium | Toko Kopi Nusantara</title>
  <meta name="description" content="Kopi Gayo arabika single origin dari Aceh Tengah. Notes cokelat dan rempah. Kirim hari ini, gratis ongkir di atas Rp150.000.">
  <link rel="canonical" href="https://tokokopi.id/produk/kopi-gayo-250">
  <link rel="alternate" hreflang="id" href="https://tokokopi.id/produk/kopi-gayo-250">
  <link rel="alternate" hreflang="en" href="https://tokokopi.id/en/products/gayo-coffee-250">
</head>
<!-- Halaman hasil pencarian internal dan keranjang tidak perlu diindeks -->
<meta name="robots" content="noindex, follow">''')]),

'Performa & keamanan di HTML': dict(
  ist=[('Resource hints', 'preconnect, dns-prefetch, preload, prefetch untuk mempercepat sumber daya penting.'),
       ('Subresource Integrity (SRI)', 'Atribut integrity memastikan file dari CDN tidak dimodifikasi.'),
       ('Content Security Policy', 'Header/meta yang membatasi sumber skrip dan gaya; pertahanan utama terhadap XSS.'),
       ('referrerpolicy', 'Mengatur informasi URL asal yang dikirim ke situs lain.')],
  cx=[H('Head yang cepat dan aman', '''
<head>
  <meta http-equiv="Content-Security-Policy"
        content="default-src 'self'; img-src 'self' https://cdn.tokokopi.id data:; script-src 'self'; style-src 'self'; frame-ancestors 'none'">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <link rel="preconnect" href="https://cdn.tokokopi.id" crossorigin>
  <link rel="preload" as="image" href="/hero.avif" fetchpriority="high">
  <script src="https://cdn.jsdelivr.net/npm/dayjs@1.11.13/dayjs.min.js"
          integrity="sha384-…hash-dari-berkas…" crossorigin="anonymous" defer></script>
</head>
<!-- Di produksi, CSP lebih baik dikirim sebagai header HTTP dari server/CDN. -->''')]),

'Open Graph & data terstruktur': dict(
  ist=[('Open Graph', 'Meta og:title, og:image, og:description yang menentukan pratinjau saat link dibagikan di WhatsApp, Facebook, LinkedIn.'),
       ('Twitter/X card', 'Meta twitter:card untuk pratinjau di X.'),
       ('JSON-LD', 'Data terstruktur schema.org di dalam <script type="application/ld+json">.'),
       ('Rich result', 'Tampilan hasil pencarian dengan harga, rating, dan stok berkat data terstruktur.')],
  cx=[H('Pratinjau WhatsApp dan rich result produk', '''
<meta property="og:type" content="product">
<meta property="og:title" content="Kopi Gayo Arabika 250 g">
<meta property="og:description" content="Notes cokelat dan rempah. Kirim hari ini.">
<meta property="og:image" content="https://tokokopi.id/og/kopi-gayo-1200x630.jpg">
<meta property="og:url" content="https://tokokopi.id/produk/kopi-gayo-250">
<meta name="twitter:card" content="summary_large_image">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Kopi Gayo Arabika 250 g",
  "image": "https://tokokopi.id/img/kopi-gayo.jpg",
  "sku": "KP-GAYO-250",
  "brand": { "@type": "Brand", "name": "Toko Kopi Nusantara" },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "214" },
  "offers": { "@type": "Offer", "price": "85000", "priceCurrency": "IDR",
              "availability": "https://schema.org/InStock", "url": "https://tokokopi.id/produk/kopi-gayo-250" }
}
</script>''', 'Gambar Open Graph berukuran 1200 x 630 piksel tampil tajam di hampir semua platform.')]),

'Halaman profil & portofolio': dict(
  ist=[('Case study', 'Cerita proyek: masalah, peran, proses, hasil terukur; lebih meyakinkan daripada daftar teknologi.'),
       ('Lighthouse score', 'Skor performa, aksesibilitas, praktik terbaik, dan SEO; target di atas 90.'),
       ('Personal branding', 'Domain sendiri, foto profesional, tautan GitHub/LinkedIn, dan cara menghubungi yang jelas.'),
       ('Checklist rilis', 'Validasi HTML, uji keyboard, uji ponsel, meta OG, favicon, 404, dan analitik.')],
  cx=[H('Kerangka portofolio yang dinilai recruiter', '''
<body>
  <a class="skip-link" href="#utama">Lewati ke konten</a>
  <header><nav aria-label="Utama"><a href="#proyek">Proyek</a> <a href="#tentang">Tentang</a> <a href="#kontak">Kontak</a></nav></header>
  <main id="utama">
    <section aria-labelledby="intro">
      <h1 id="intro">Rina Wulandari, Frontend Developer</h1>
      <p>Membangun antarmuka yang cepat dan mudah diakses untuk UMKM dan layanan publik.</p>
      <a href="/cv-rina.pdf" download>Unduh CV (PDF, 180 KB)</a>
    </section>
    <section id="proyek" aria-labelledby="judul-proyek">
      <h2 id="judul-proyek">Proyek pilihan</h2>
      <article>
        <h3>Checkout toko kopi</h3>
        <p><strong>Masalah:</strong> 38% pengguna berhenti di halaman alamat.</p>
        <p><strong>Yang saya lakukan:</strong> menyederhanakan form 11 menjadi 6 field, autocomplete alamat.</p>
        <p><strong>Hasil:</strong> konversi naik 14%, Lighthouse aksesibilitas 100.</p>
        <p><a href="https://github.com/rina/checkout">Kode</a> · <a href="https://checkout-demo.vercel.app">Demo</a></p>
      </article>
    </section>
    <section id="kontak" aria-labelledby="judul-kontak"><h2 id="judul-kontak">Kontak</h2> …</section>
  </main>
</body>''')]),
}
