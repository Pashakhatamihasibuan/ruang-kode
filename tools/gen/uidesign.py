"""Isi jalur UI Design: 6 modul x 5 pelajaran. Hampir semua pelajaran berupa lab HTML/CSS dengan tantangan otomatis.
Kunci 'cek' (dipakai uji otomatis, dibuang sebelum ditulis) berisi CSS atau HTML yang membuat tantangan lulus."""
from mobile_lib import W, C, M, q
from mobile_dart_x import S


def L(t, b, html, css, task, pts, qs, cek):
    d = W(t, b, html, css=css, task=task, pts=pts, qs=qs)
    d['cek'] = cek
    return d


def H(soal, petunjuk, jawab):
    return S(soal, petunjuk, jawab, lang='html')


def X(soal, petunjuk, jawab):
    return S(soal, petunjuk, jawab, lang='css')


def T(soal, petunjuk, jawab):
    return S(soal, petunjuk, jawab, lang='text')


G = "getComputedStyle(document.querySelector('{}'))"
RULES = "[...document.styleSheets].flatMap(s=>[...s.cssRules])"
# fungsi kontras WCAG yang dipakai di beberapa tes
LUM = "(c=>{const v=c.match(/[\\d.]+/g).slice(0,3).map(x=>{x/=255;return x<=0.03928?x/12.92:((x+0.055)/1.055)**2.4});return 0.2126*v[0]+0.7152*v[1]+0.0722*v[2]})"

UI = [
M('Fondasi desain antarmuka', 'Pemula',
  'Hierarki visual, prinsip Gestalt, grid 8 poin, perataan dan keseimbangan, serta jarak untuk kepadatan dan keterbacaan.',
  ['Visual hierarchy', 'Gestalt', '8-point grid', 'Alignment', 'Spacing'], [
  L('Hierarki visual',
    ['<b>Hierarki visual</b> adalah urutan mata pengguna membaca layar: apa yang dilihat pertama, kedua, dan terakhir. Desainer mengatur urutan itu dengan <b>ukuran</b>, <b>ketebalan</b>, <b>warna dan kontras</b>, <b>posisi</b>, serta <b>ruang kosong</b> di sekitar elemen.',
     'Aturan praktis: setiap layar punya <b>satu</b> hal terpenting (judul, angka utama, atau tombol aksi utama). Jika semua elemen sama besar dan sama tebal, mata tidak tahu harus mulai dari mana, dan pengguna merasa layar itu "ramai" walau isinya sedikit.',
     'Uji cepat: <b>squint test</b>. Sipitkan mata sampai layar buram. Elemen yang masih terlihat jelas adalah puncak hierarkimu. Jika yang menonjol justru label kecil atau ikon dekoratif, hierarkinya terbalik.',
     'Kartu produk di pratinjau dibuat rata semua: judul, harga, dan deskripsi sama ukuran. Perbaiki hierarkinya.'],
    html='''<article class="kartu">
  <p class="kategori">Kopi susu</p>
  <h2 class="judul">Es Kopi Gula Aren</h2>
  <p class="harga">Rp18.000</p>
  <p class="desk">Espresso, susu segar, dan gula aren asli dari Banten.</p>
  <button class="aksi">Tambah ke keranjang</button>
</article>''',
    css='''body { font-family: system-ui, sans-serif; background: #F4F1EC; margin: 0; padding: 24px; color: #2B2724; }
.kartu { max-width: 320px; background: #fff; border-radius: 16px; padding: 24px; }
.kartu p, .kartu h2 { font-size: 16px; font-weight: 400; margin: 0 0 8px; }
.kategori { color: #7A716A; }
.aksi { margin-top: 16px; width: 100%; padding: 12px; border: 0; border-radius: 10px; background: #8A4B2A; color: #fff; font-size: 16px; }''',
    task={'q': 'Jadikan judul puncak hierarki: <code>.judul</code> minimal 24px dan tebal minimal 700. Buat <code>.harga</code> tebal minimal 600.',
          'test': f"parseFloat({G.format('.judul')}.fontSize)>=24&&{G.format('.judul')}.fontWeight>=700&&{G.format('.harga')}.fontWeight>=600",
          'hint': '.kartu .judul { font-size: 24px; font-weight: 700 } dan .kartu .harga { font-weight: 600 }. Pakai selector .kartu .judul agar lebih kuat dari .kartu h2.'},
    pts=['Hierarki diatur dengan ukuran, tebal, kontras, posisi, dan ruang kosong.', 'Satu layar, satu hal terpenting.', 'Squint test untuk memeriksa hierarki.'],
    qs=[q('Apa tanda hierarki visual yang buruk?', ['Semua elemen sama besar dan sama tebal', 'Judul lebih besar dari deskripsi', 'Ada satu tombol utama'], 0, 'Mata tidak tahu harus mulai dari mana.'),
        q('Squint test dipakai untuk?', ['Mengukur kontras warna secara pasti', 'Melihat elemen mana yang paling menonjol', 'Menguji kecepatan muat'], 1, 'Yang tetap terlihat saat buram adalah puncak hierarki.')],
    cek={'css': '.kartu .judul{font-size:24px;font-weight:700}.kartu .harga{font-weight:600}'}),
  L('Prinsip Gestalt',
    ['<b>Gestalt</b> adalah prinsip psikologi tentang cara otak mengelompokkan apa yang dilihat. Lima yang paling sering dipakai di UI: <b>proximity</b> (yang berdekatan dianggap satu kelompok), <b>similarity</b> (yang mirip dianggap sejenis), <b>common region</b> (yang berada di satu bingkai dianggap satu kelompok), <b>closure</b> (otak melengkapi bentuk yang terputus), dan <b>figure-ground</b> (memisahkan objek dari latar).',
     'Proximity paling sering salah di form. Jika jarak label ke input-nya <b>sama</b> dengan jarak label ke input di atasnya, pengguna ragu label itu milik input yang mana. Aturannya: jarak <b>di dalam</b> kelompok harus jelas lebih kecil daripada jarak <b>antar</b> kelompok.',
     'Similarity dipakai untuk link dan tombol: semua yang bisa diklik memakai warna yang sama, dan warna itu tidak dipakai untuk teks biasa. Common region dipakai untuk kartu: satu kartu, satu produk.',
     'Form di pratinjau punya jarak yang sama di mana-mana. Perbaiki dengan proximity.'],
    html='''<form class="form">
  <div class="grup"><label class="lbl" for="n">Nama lengkap</label><input id="n"></div>
  <div class="grup"><label class="lbl" for="e">Email</label><input id="e" type="email"></div>
  <div class="grup"><label class="lbl" for="p">Nomor HP</label><input id="p" type="tel"></div>
</form>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; color: #1F2933; }
.form { max-width: 320px; }
.grup { margin-bottom: 12px; }
.lbl { display: block; font-size: 14px; font-weight: 600; margin-bottom: 12px; }
input { width: 100%; box-sizing: border-box; padding: 10px 12px; border: 1px solid #9AA5B1; border-radius: 8px; font-size: 16px; }''',
    task={'q': 'Terapkan proximity: jarak label ke input (<code>.lbl</code> margin-bottom) maksimal 8px, dan jarak antar <code>.grup</code> minimal 24px.',
          'test': f"parseFloat({G.format('.lbl')}.marginBottom)<=8&&parseFloat({G.format('.grup')}.marginBottom)>=24",
          'hint': '.lbl { margin-bottom: 4px } .grup { margin-bottom: 24px }'},
    pts=['Proximity: jarak di dalam kelompok lebih kecil dari jarak antar kelompok.', 'Similarity: yang bisa diklik punya satu gaya yang konsisten.', 'Common region: satu bingkai, satu kelompok.'],
    qs=[q('Label berjarak 12px ke input-nya dan 12px ke input di atasnya. Prinsip apa yang dilanggar?', ['Similarity', 'Proximity', 'Closure'], 1, 'Jarak yang sama membuat kelompok tidak jelas.'),
        q('Semua link berwarna biru dan bergaris bawah. Ini memakai prinsip?', ['Similarity', 'Figure-ground', 'Closure'], 0, 'Elemen yang mirip dianggap sejenis.')],
    cek={'css': '.lbl{margin-bottom:4px}.grup{margin-bottom:24px}'}),
  L('Grid 8 poin',
    ['<b>Grid 8 poin</b> berarti semua ukuran dan jarak memakai kelipatan 8: 8, 16, 24, 32, 40, 48, 64. Untuk penyesuaian halus (ikon, jarak teks kecil) boleh setengahnya, 4. Material Design, Apple, dan hampir semua design system memakai sistem ini.',
     'Kenapa 8? Layar umum (360, 768, 1280, 1440 px) habis dibagi 8, dan kelipatan 8 tetap utuh saat diskalakan 1,5× atau 2× di layar beresolusi tinggi. Yang lebih penting: tim tidak perlu berdebat apakah jarak itu 13 atau 14 piksel. Pilihannya terbatas, keputusan lebih cepat, dan hasilnya konsisten.',
     'Di Figma, atur <b>nudge amount</b> (Shift + panah) menjadi 8, aktifkan layout grid 8 px, dan pakai nilai spacing auto layout dari skala yang sama. Di kode, simpan skalanya sebagai token: <code>--space-1: 8px; --space-2: 16px; ...</code>.',
     'Kartu di pratinjau memakai angka acak (13px, 7px, 10px). Rapikan ke grid 8.'],
    html='''<section class="kartu">
  <h3>Kelas Flutter Dasar</h3>
  <p>12 pelajaran · 4 jam</p>
  <ul class="daftar"><li>Widget dan layout</li><li>State dan form</li><li>Navigasi</li></ul>
</section>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; }
.kartu { max-width: 320px; padding: 13px 7px; border: 1px solid #D5D9E0; border-radius: 10px; }
.kartu h3 { margin: 0 0 5px; }
.daftar { display: grid; gap: 10px; padding-left: 20px; }''',
    task={'q': 'Ubah padding <code>.kartu</code> dan <code>gap</code> pada <code>.daftar</code> menjadi kelipatan 8 (misalnya padding 24px, gap 8px).',
          'test': f"(s=>['paddingTop','paddingRight','paddingBottom','paddingLeft'].every(k=>parseFloat(s[k])%8===0))({G.format('.kartu')})&&parseFloat({G.format('.daftar')}.rowGap)%8===0",
          'hint': '.kartu { padding: 24px } .daftar { gap: 8px }'},
    pts=['Semua jarak dan ukuran kelipatan 8, setengahnya 4 untuk detail.', 'Pilihan terbatas mempercepat keputusan dan menjaga konsistensi.', 'Simpan skala sebagai token spacing.'],
    qs=[q('Mana yang TIDAK mengikuti grid 8 poin?', ['24px', '40px', '18px'], 2, '18 bukan kelipatan 8 (atau 4).'),
        q('Keuntungan utama grid 8 poin bagi tim?', ['Warna lebih cerah', 'Pilihan jarak terbatas sehingga konsisten', 'Ukuran file lebih kecil'], 1, 'Tidak ada lagi perdebatan 13 atau 14 piksel.')],
    cek={'css': '.kartu{padding:24px}.daftar{gap:8px}'}),
  L('Perataan dan keseimbangan',
    ['<b>Perataan</b> (alignment) membuat elemen terasa terhubung walau berjauhan. Setiap elemen sebaiknya sejajar dengan sesuatu: tepi kiri judul sejajar dengan tepi kiri paragraf, tombol sejajar dengan input di atasnya. Di Figma, perhatikan garis merah petunjuk saat menggeser elemen.',
     'Untuk teks lebih dari dua baris, <b>rata kiri</b> paling mudah dibaca, karena mata selalu kembali ke titik awal yang sama. Rata tengah cocok untuk judul pendek atau empty state, tetapi melelahkan untuk paragraf. Jangan mencampur rata kiri dan rata tengah dalam satu kartu.',
     '<b>Keseimbangan</b> adalah sebaran "berat visual" di layar. <b>Simetris</b> terasa formal dan stabil (halaman login). <b>Asimetris</b> terasa dinamis (hero dengan teks di kiri dan gambar besar di kanan), tetapi tetap butuh grid agar tidak terlihat berantakan.',
     'Kartu di pratinjau mencampur rata tengah dan rata kiri. Samakan perataannya.'],
    html='''<article class="isi">
  <h3 class="tengah">Promo Akhir Bulan</h3>
  <p>Diskon 20% untuk semua kelas mobile sampai 30 November.</p>
  <p class="tengah">Gunakan kode RUANG20 saat pembayaran.</p>
  <a href="#">Lihat syarat</a>
</article>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.isi { max-width: 340px; padding: 24px; background: #FFF7E6; border-radius: 12px; }
.isi > * { margin: 0 0 8px; }
.tengah { text-align: center; }''',
    task={'q': 'Buat semua isi kartu rata kiri, sejajar satu garis.',
          'test': "[...document.querySelectorAll('.isi > *')].every(e=>['left','start'].includes(getComputedStyle(e).textAlign))",
          'hint': 'Ubah .tengah { text-align: left } atau hapus kelas tengah dari elemen.'},
    pts=['Setiap elemen sejajar dengan sesuatu.', 'Paragraf: rata kiri. Rata tengah hanya untuk teks pendek.', 'Simetris terasa stabil, asimetris terasa dinamis.'],
    qs=[q('Perataan paling mudah dibaca untuk paragraf panjang?', ['Rata tengah', 'Rata kiri', 'Rata kanan'], 1, 'Mata kembali ke titik awal yang sama setiap baris.'),
        q('Hero dengan teks di kiri dan foto besar di kanan adalah keseimbangan?', ['Simetris', 'Asimetris'], 1, 'Berat visual tidak dicerminkan.')],
    cek={'css': '.tengah{text-align:left}'}),
  L('Jarak untuk kepadatan dan keterbacaan',
    ['<b>Kepadatan</b> (density) adalah seberapa banyak informasi di satu layar. Aplikasi kasir, dashboard, dan tabel data butuh kepadatan <b>tinggi</b> agar pengguna ahli melihat banyak data sekaligus. Aplikasi belajar, onboarding, dan halaman marketing butuh kepadatan <b>rendah</b> agar nyaman dibaca.',
     'Tiga alat pengatur kepadatan: <b>padding</b> di dalam komponen (sel tabel, tombol), <b>gap</b> antar elemen, dan <b>line-height</b> teks. Untuk paragraf, line-height 1,4 sampai 1,6 kali ukuran huruf. Untuk sel tabel, padding vertikal 8 px (padat) sampai 16 px (lega).',
     'Banyak design system menyediakan <b>mode kepadatan</b>: comfortable dan compact. Material 3 menyebutnya density scale (0, -1, -2, -3), setiap tingkat mengurangi tinggi komponen 4 dp. Jangan memadatkan target sentuh di bawah 44 sampai 48 px di ponsel.',
     'Tabel di pratinjau terlalu sesak untuk dibaca santai. Longgarkan.'],
    html='''<table class="tabel">
  <thead><tr><th>Kelas</th><th>Siswa</th><th>Selesai</th></tr></thead>
  <tbody>
    <tr><td>Flutter Dasar</td><td>1.240</td><td>68%</td></tr>
    <tr><td>Kotlin Pemula</td><td>980</td><td>72%</td></tr>
    <tr><td>UI Design</td><td>1.530</td><td>81%</td></tr>
  </tbody>
</table>
<p class="teks">Persentase selesai dihitung dari siswa yang menuntaskan semua pelajaran dan kuis dalam 60 hari sejak mendaftar.</p>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; color: #1F2933; }
.tabel { border-collapse: collapse; width: 100%; max-width: 420px; font-size: 14px; }
.tabel th, .tabel td { padding: 2px 4px; border-bottom: 1px solid #E4E7EB; text-align: left; }
.teks { max-width: 420px; font-size: 14px; line-height: 1.1; }''',
    task={'q': 'Beri sel tabel padding vertikal minimal 12px, dan paragraf <code>.teks</code> line-height minimal 1.5.',
          'test': f"parseFloat({G.format('.tabel td')}.paddingTop)>=12&&parseFloat({G.format('.teks')}.lineHeight)/parseFloat({G.format('.teks')}.fontSize)>=1.5",
          'hint': '.tabel th, .tabel td { padding: 12px 16px } .teks { line-height: 1.6 }'},
    pts=['Kepadatan tinggi untuk pengguna ahli, rendah untuk bacaan santai.', 'Atur dengan padding, gap, dan line-height.', 'Target sentuh tetap 44 sampai 48 px.'],
    qs=[q('Dashboard gudang untuk staf yang memantau ratusan barang paling cocok dengan kepadatan?', ['Tinggi', 'Rendah'], 0, 'Pengguna ahli butuh melihat banyak data sekaligus.'),
        q('Line-height yang nyaman untuk paragraf?', ['1.0', '1.4 sampai 1.6', '3.0'], 1, 'Cukup lega tanpa terlihat terpisah-pisah.')],
    cek={'css': '.tabel th,.tabel td{padding:12px 16px}.teks{line-height:1.6}'}),
]),
M('Sistem tipografi digital', 'Pemula',
  'Memilih typeface, skala tipe modular, line height, tracking, panjang baris, peran tipografi semantik, dan tipografi responsif.',
  ['Typeface', 'Type scale', 'Line height', 'Text styles', 'Responsive type'], [
  L('Memilih typeface',
    ['<b>Typeface</b> (keluarga huruf) membawa kepribadian. <b>Sans-serif</b> (Inter, Plus Jakarta Sans, Roboto) netral dan jelas di layar, pilihan aman untuk UI. <b>Serif</b> (Lora, Merriweather) terasa editorial dan tepercaya, cocok untuk judul atau bacaan panjang. <b>Monospace</b> (JetBrains Mono) untuk kode dan angka yang harus sejajar.',
     'Kriteria memilih font UI: (1) tinggi huruf kecil (<b>x-height</b>) cukup besar agar terbaca di ukuran 12 sampai 14 px, (2) bentuk <b>I l 1</b> dan <b>O 0</b> mudah dibedakan, (3) punya cukup <b>ketebalan</b> (400, 500, 600, 700), (4) mendukung karakter bahasa target, dan (5) lisensinya jelas. Google Fonts aman untuk proyek komersial.',
     'Batasi <b>maksimal dua keluarga</b>: satu untuk judul, satu untuk isi, atau satu keluarga saja dengan beberapa ketebalan. Font sistem (<code>system-ui</code>) memuat instan dan terasa "asli" di setiap perangkat, sehingga banyak aplikasi besar memakainya.',
     'Halaman di pratinjau memakai font dekoratif untuk teks UI. Ganti dengan font sistem.'],
    html='''<main class="hal">
  <h1>Pengaturan akun</h1>
  <p>Ubah nama, email, dan kata sandi. Perubahan email perlu dikonfirmasi lewat tautan yang kami kirim.</p>
  <p class="kecil">Kode verifikasi: Il1O0 · terakhir diubah 12/11/2026</p>
</main>''',
    css='''body { margin: 0; padding: 24px; font-family: "Brush Script MT", "Comic Sans MS", cursive; color: #1F2933; }
.hal { max-width: 420px; }
.kecil { font-size: 13px; color: #52606D; }''',
    task={'q': 'Ganti <code>font-family</code> body menjadi tumpukan font sistem yang diawali <code>system-ui</code>.',
          'test': "getComputedStyle(document.body).fontFamily.startsWith('system-ui')",
          'hint': 'body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif }'},
    pts=['Sans-serif untuk UI, serif untuk editorial, mono untuk kode.', 'Periksa x-height, I l 1 dan O 0, ketebalan, dan lisensi.', 'Maksimal dua keluarga huruf.'],
    qs=[q('Kenapa bentuk I, l, dan 1 harus mudah dibedakan?', ['Agar estetis', 'Agar kode, password, dan angka tidak salah baca', 'Agar file lebih kecil'], 1, 'Salah baca karakter bisa membuat pengguna gagal login.'),
        q('Berapa keluarga huruf maksimal yang disarankan dalam satu produk?', ['Dua', 'Empat', 'Tidak ada batas'], 0, 'Lebih dari itu terasa tidak konsisten.')],
    cek={'css': 'body{font-family:system-ui,sans-serif}'}),
  L('Skala tipe modular',
    ['<b>Skala tipe modular</b> adalah daftar ukuran huruf yang dihitung dari <b>ukuran dasar</b> dikali <b>rasio</b> berulang. Dasar 16 px dengan rasio 1,25 (major third): 16 → 20 → 25 → 31,25 → 39. Dengan rasio 1,2 (minor third): 16 → 19,2 → 23 → 27,6.',
     'Rasio kecil (1,125 sampai 1,2) cocok untuk aplikasi padat dan layar kecil, karena beda antar tingkat halus. Rasio besar (1,333 sampai 1,5) cocok untuk halaman marketing dengan judul besar. Hasil hitungan biasanya dibulatkan ke angka genap atau kelipatan 4.',
     'Keuntungannya: ukuran huruf tidak dipilih asal-asalan, sehingga semua judul terasa satu keluarga. Di CSS, rasio bisa disimpan sebagai variabel dan dihitung dengan <code>calc()</code>, sehingga mengubah satu angka mengubah seluruh skala.',
     'Pratinjau memakai rasio 1,5, terlalu dramatis untuk halaman aplikasi. Ubah rasionya.'],
    html='''<div class="contoh">
  <h1>Judul halaman (fs-3)</h1>
  <h2>Subjudul (fs-2)</h2>
  <h3>Judul kartu (fs-1)</h3>
  <p>Teks isi memakai ukuran dasar 16 px.</p>
</div>''',
    css=''':root {
  --r: 1.5;
  --fs-0: 1rem;
  --fs-1: calc(var(--fs-0) * var(--r));
  --fs-2: calc(var(--fs-1) * var(--r));
  --fs-3: calc(var(--fs-2) * var(--r));
}
body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; }
h1 { font-size: var(--fs-3); margin: 0 0 8px; }
h2 { font-size: var(--fs-2); margin: 0 0 8px; }
h3 { font-size: var(--fs-1); margin: 0 0 8px; }
p { font-size: var(--fs-0); }''',
    task={'q': 'Ubah <code>--r</code> menjadi <b>1.25</b> (major third). h1 akan menjadi sekitar 31,25px.',
          'test': "Math.abs(parseFloat(getComputedStyle(document.querySelector('h1')).fontSize)-31.25)<0.6",
          'hint': ':root { --r: 1.25 }'},
    pts=['Skala = ukuran dasar × rasio berulang.', 'Rasio kecil untuk aplikasi, besar untuk marketing.', 'Simpan rasio di variabel agar mudah diubah.'],
    qs=[q('Dasar 16 dan rasio 1,25. Berapa tingkat kedua (16 × 1,25 × 1,25)?', ['20', '25', '32'], 1, '16 × 1,5625 = 25.'),
        q('Aplikasi kasir yang padat cocok dengan rasio?', ['1.125 sampai 1.2', '1.5 sampai 1.618'], 0, 'Beda antar tingkat halus, hemat ruang.')],
    cek={'css': ':root{--r:1.25}'}),
  L('Line height, tracking, dan panjang baris',
    ['<b>Line height</b> (leading) adalah jarak antar baris. Paragraf butuh 1,4 sampai 1,6; judul besar cukup 1,1 sampai 1,25, karena jarak yang terlalu lega membuat baris judul terlihat terpisah.',
     '<b>Tracking</b> (letter-spacing) adalah jarak antar huruf. Teks kecil berhuruf kapital (label, overline) butuh tracking positif sekitar 0,04 sampai 0,1 em agar terbaca. Judul sangat besar justru sedikit dirapatkan (-0,01 sampai -0,02 em).',
     '<b>Panjang baris</b> (measure) yang nyaman adalah <b>45 sampai 75 karakter</b>, ideal sekitar 65. Baris terlalu panjang membuat mata kehilangan awal baris berikutnya. Di CSS, satuan <code>ch</code> (lebar karakter 0) pas untuk ini: <code>max-width: 65ch</code>.',
     'Artikel di pratinjau terlalu rapat dan terlalu lebar di layar besar. Perbaiki.'],
    html='''<article class="artikel">
  <p class="overline">Tips belajar</p>
  <h2>Belajar 30 menit sehari lebih efektif daripada 5 jam sekali seminggu</h2>
  <p class="isi">Otak memperkuat ingatan saat kita mengulang materi dengan jeda. Teknik ini disebut spaced repetition. Mulailah dengan satu pelajaran pendek, kerjakan kuisnya, lalu ulangi pelajaran yang sama dua hari kemudian sebelum lanjut ke materi baru.</p>
</article>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; color: #1F2933; }
.overline { font-size: 12px; text-transform: uppercase; color: #8A4B2A; margin: 0; }
h2 { font-size: 28px; line-height: 1.6; margin: 8px 0 16px; }
.isi { font-size: 17px; line-height: 1.15; }''',
    task={'q': 'Atur: <code>.artikel</code> max-width 65ch, <code>.isi</code> line-height 1.6, dan <code>.overline</code> letter-spacing positif.',
          'test': f"{G.format('.artikel')}.maxWidth!=='none'&&parseFloat({G.format('.isi')}.lineHeight)/17>=1.5&&parseFloat({G.format('.overline')}.letterSpacing)>0",
          'hint': '.artikel { max-width: 65ch } .isi { line-height: 1.6 } .overline { letter-spacing: 0.08em }'},
    pts=['Paragraf 1,4–1,6; judul besar 1,1–1,25.', 'Label kapital kecil: tracking positif.', 'Panjang baris 45–75 karakter, max-width: 65ch.'],
    qs=[q('Panjang baris ideal untuk paragraf?', ['20 karakter', 'Sekitar 65 karakter', '150 karakter'], 1, 'Antara 45 dan 75.'),
        q('Label kecil huruf kapital sebaiknya diberi tracking?', ['Positif', 'Negatif', 'Nol'], 0, 'Huruf kapital kecil terlihat terlalu rapat tanpa tracking.')],
    cek={'css': '.artikel{max-width:65ch}.isi{line-height:1.6}.overline{letter-spacing:.08em}'}),
  L('Peran tipografi semantik',
    ['Daripada menamai gaya teks dengan ukurannya ("Inter 24 Bold"), design system modern menamainya dengan <b>peran</b>: <b>display</b> (angka atau judul sangat besar), <b>headline</b> (judul halaman), <b>title</b> (judul kartu dan dialog), <b>body</b> (isi), dan <b>label</b> (tombol, tab, chip, keterangan kecil). Material 3 memakai lima peran ini, masing-masing dalam ukuran large, medium, dan small.',
     'Kenapa peran? Karena ukuran bisa berubah (misalnya di tablet semua sedikit lebih besar), tetapi peran tidak. Developer cukup menulis <code>title-medium</code>, dan jika desainer mengubah ukurannya, seluruh aplikasi ikut berubah.',
     'Setiap peran adalah paket: ukuran, line-height, ketebalan, tracking, dan kadang huruf kapital. Di Figma, simpan sebagai <b>Text Style</b> dengan nama bertingkat seperti <code>Title/Medium</code>. Di kode, simpan sebagai kelas atau token.',
     'Pratinjau sudah punya kelas peran, tetapi <code>.label</code> belum lengkap.'],
    html='''<section class="kartu">
  <p class="label">Progres minggu ini</p>
  <p class="display">86%</p>
  <h3 class="title">Kelas UI Design</h3>
  <p class="body">Kamu sudah menyelesaikan 26 dari 30 pelajaran. Tinggal modul handoff.</p>
</section>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; color: #1D1B20; }
.kartu { max-width: 340px; padding: 24px; border-radius: 16px; background: #F3EDF7; }
.kartu > * { margin: 0 0 8px; }
.display { font-size: 45px; line-height: 52px; font-weight: 400; letter-spacing: 0; }
.title { font-size: 16px; line-height: 24px; font-weight: 500; letter-spacing: 0.15px; }
.body { font-size: 14px; line-height: 20px; font-weight: 400; letter-spacing: 0.25px; }
.label { font-size: 12px; line-height: 16px; }''',
    task={'q': 'Lengkapi peran <code>.label</code>: tebal 500, huruf kapital (<code>uppercase</code>), dan letter-spacing positif.',
          'test': f"(s=>s.fontWeight>=500&&s.textTransform==='uppercase'&&parseFloat(s.letterSpacing)>0)({G.format('.label')})",
          'hint': '.label { font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px }'},
    pts=['Namai gaya teks dengan peran, bukan ukuran.', 'Peran: display, headline, title, body, label.', 'Satu peran = paket ukuran, line-height, tebal, tracking.'],
    qs=[q('Nama gaya teks mana yang paling tahan perubahan?', ['Inter-24-Bold', 'title-large', 'Besar-Hitam'], 1, 'Peran tidak berubah walau ukurannya diubah.'),
        q('Teks pada tombol dan tab memakai peran?', ['display', 'label', 'body'], 1, 'Label untuk teks kontrol yang pendek.')],
    cek={'css': '.label{font-weight:500;text-transform:uppercase;letter-spacing:.5px}'}),
  L('Tipografi responsif',
    ['Ukuran judul yang pas di laptop (48 px) terlalu besar di ponsel 360 px, dan sebaliknya. Cara lama memakai <b>media query</b>: 28 px di ponsel, lalu 40 px mulai lebar 768 px. Hasilnya melompat di titik tertentu.',
     'Cara modern memakai <b>tipografi fluid</b> dengan <code>clamp(minimum, ideal, maksimum)</code>: <code>font-size: clamp(1.75rem, 1rem + 3vw, 3rem)</code>. Ukuran tumbuh halus mengikuti lebar layar, tetapi tidak pernah di bawah 28 px atau di atas 48 px. Bagian ideal selalu campuran <code>rem</code> dan <code>vw</code>, agar teks tetap ikut membesar saat pengguna memperbesar ukuran huruf di pengaturan browser.',
     'Teks isi biasanya cukup 16 px sampai 18 px tanpa fluid. Jangan pernah membuat teks isi di bawah 16 px di ponsel, karena iOS akan otomatis memperbesar halaman saat input bertulisan lebih kecil dari 16 px difokuskan.',
     'Ubah judul hero di pratinjau menjadi fluid. Lalu ubah lebar jendela pratinjau untuk melihatnya tumbuh.'],
    html='''<header class="hero">
  <h1>Belajar coding dari nol, dalam Bahasa Indonesia</h1>
  <p>Gratis, interaktif, dan bisa dipakai offline.</p>
</header>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; }
.hero { padding: 32px 16px; background: #0F172A; color: #F8FAFC; }
.hero h1 { font-size: 48px; line-height: 1.15; margin: 0 0 12px; }
.hero p { font-size: 18px; margin: 0; color: #CBD5E1; }''',
    task={'q': 'Ganti <code>font-size</code> judul <code>.hero h1</code> dengan <code>clamp()</code>, misalnya <code>clamp(1.75rem, 1rem + 3vw, 3rem)</code>.',
          'test': f"{RULES}.some(r=>r.style&&/clamp\\(/.test(r.style.fontSize))",
          'hint': '.hero h1 { font-size: clamp(1.75rem, 1rem + 3vw, 3rem) }'},
    pts=['clamp(min, ideal, max) untuk ukuran fluid.', 'Bagian ideal campur rem dan vw agar zoom tetap bekerja.', 'Teks isi minimal 16 px di ponsel.'],
    qs=[q('Kenapa bagian ideal clamp sebaiknya memakai rem + vw, bukan vw saja?', ['Agar teks tetap membesar saat pengguna menambah ukuran huruf', 'Agar lebih cepat', 'Wajib di CSS'], 0, 'vw saja mengabaikan pengaturan ukuran huruf pengguna.'),
        q('clamp(1.75rem, 1rem + 3vw, 3rem) di layar sangat lebar menghasilkan?', ['1.75rem', '3rem', 'Tak terbatas'], 1, 'Dibatasi nilai maksimum.')],
    cek={'css': '.hero h1{font-size:clamp(1.75rem,1rem + 3vw,3rem)}'}),
]),
M('Teori warna dan aksesibilitas', 'Menengah',
  'Properti warna dan model warna layar, kontras WCAG, palet tint dan shade, warna semantik untuk state, dan dark mode.',
  ['Color models', 'WCAG contrast', 'Palette', 'Semantic color', 'Dark mode'], [
  L('Properti warna dan model warna layar',
    ['Setiap warna punya tiga properti: <b>hue</b> (rona: merah, biru, hijau, diukur 0 sampai 360 derajat di roda warna), <b>saturation</b> (kepekatan: abu-abu sampai menyala), dan <b>lightness</b> atau value (gelap sampai terang).',
     'Layar membuat warna dari cahaya merah, hijau, dan biru: model <b>RGB</b>, ditulis heksadesimal (<code>#8A4B2A</code>) atau <code>rgb(138 75 42)</code>. Untuk desainer, <b>HSL</b> lebih intuitif: <code>hsl(21 53% 35%)</code>, karena membuat versi lebih terang cukup menaikkan angka lightness. Model <b>OKLCH</b> yang lebih baru membuat perubahan lightness terasa merata di semua hue, sehingga kini dipakai Tailwind v4.',
     'Cetak memakai <b>CMYK</b> (tinta), bukan RGB. Itulah sebabnya warna yang menyala di layar bisa terlihat kusam saat dicetak. Untuk produk digital, bekerja di ruang warna sRGB (atau Display P3 untuk layar modern) dan selalu cek di perangkat nyata.',
     'Tombol di pratinjau memakai HSL dengan hue dari variabel. Ubah hue-nya.'],
    html='''<div class="baris">
  <button class="tombol">Daftar sekarang</button>
  <span class="kode">hsl(var(--hue) 70% 40%)</span>
</div>''',
    css=''':root { --hue: 21; }
body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.baris { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
.tombol { background: hsl(var(--hue) 70% 40%); color: #fff; border: 0; padding: 12px 24px; border-radius: 10px; font-size: 16px; }
.kode { font-family: ui-monospace, monospace; color: #52606D; }''',
    task={'q': 'Ubah <code>--hue</code> menjadi <b>210</b> agar tombol menjadi biru, tanpa menyentuh saturation dan lightness.',
          'test': "getComputedStyle(document.documentElement).getPropertyValue('--hue').trim()==='210'",
          'hint': ':root { --hue: 210 }'},
    pts=['Hue, saturation, lightness.', 'Layar memakai RGB; HSL dan OKLCH lebih mudah diatur desainer.', 'Cetak memakai CMYK, warna bisa berbeda.'],
    qs=[q('Untuk membuat versi warna lebih terang di HSL, ubah?', ['Hue', 'Saturation', 'Lightness'], 2, 'Lightness mengatur gelap-terang.'),
        q('Hue 120 kira-kira berwarna?', ['Merah', 'Hijau', 'Biru'], 1, '0 merah, 120 hijau, 240 biru.')],
    cek={'css': ':root{--hue:210}'}),
  L('Kontras WCAG',
    ['<b>WCAG</b> (Web Content Accessibility Guidelines) mengukur kontras sebagai rasio luminansi dua warna, dari 1:1 (sama) sampai 21:1 (hitam di atas putih). Standar <b>AA</b> yang dipakai hampir semua regulasi: teks normal minimal <b>4,5:1</b>, teks besar (24 px, atau 18,66 px tebal) minimal <b>3:1</b>, dan komponen UI seperti border input dan ikon minimal <b>3:1</b>. Level AAA: 7:1.',
     'Pelanggaran paling umum: teks abu-abu muda di atas putih. <code>#9CA3AF</code> di atas putih hanya 2,5:1, terlihat "elegan" di monitor desainer, tetapi tidak terbaca di bawah sinar matahari atau oleh pengguna lansia. <code>#6B7280</code> sudah 4,8:1.',
     'Alat cek: plugin Figma (Stark, Contrast), panel Accessibility di Chrome DevTools, atau webaim.org/resources/contrastchecker. Tes otomatis di bawah menghitung rasio dengan rumus WCAG yang sama.',
     'Teks keterangan di pratinjau gagal AA. Gelapkan warnanya.'],
    html='''<div class="kartu">
  <h3>Ujian akhir modul</h3>
  <p class="ket">Dibuka Senin, 10 November 2026 pukul 08.00 WIB. Durasi 45 menit.</p>
</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; background: #fff; }
.kartu { max-width: 340px; padding: 24px; border: 1px solid #E5E7EB; border-radius: 12px; background: #FFFFFF; }
h3 { margin: 0 0 8px; color: #111827; }
.ket { margin: 0; font-size: 15px; color: #9CA3AF; }''',
    task={'q': 'Ubah warna <code>.ket</code> agar kontrasnya dengan latar putih minimal <b>4.5:1</b> (misalnya <code>#4B5563</code>).',
          'test': f"(()=>{{const L={LUM},a=L(getComputedStyle(document.querySelector('.ket')).color);return (1.05)/(a+0.05)>=4.5}})()",
          'hint': '.ket { color: #4B5563 } memberi rasio sekitar 7,6:1.'},
    pts=['AA: teks normal 4,5:1, teks besar dan komponen UI 3:1.', 'Abu-abu muda di atas putih adalah pelanggaran paling umum.', 'Cek dengan plugin Figma atau DevTools.'],
    qs=[q('Kontras minimal teks normal untuk WCAG AA?', ['3:1', '4.5:1', '7:1'], 1, '7:1 untuk AAA.'),
        q('Border input harus berkontras minimal berapa terhadap latarnya?', ['1.5:1', '3:1', '4.5:1'], 1, 'Komponen UI non-teks: 3:1.')],
    cek={'css': '.ket{color:#4B5563}'}),
  L('Palet tint dan shade',
    ['Satu warna merek tidak cukup. UI butuh <b>skala</b>: versi sangat terang untuk latar (50, 100), menengah untuk border (200, 300), warna utama (500, 600), dan gelap untuk teks dan hover (700, 800, 900). <b>Tint</b> = dicampur putih (lebih terang), <b>shade</b> = dicampur hitam (lebih gelap).',
     'Cara membuat skala: tentukan warna utama di tingkat 500 atau 600, lalu ubah <b>lightness</b> bertahap dengan hue tetap. Sedikit menggeser hue dan menaikkan saturasi di tingkat gelap membuat warna terlihat lebih hidup. Alat bantu: uicolors.app, Tailwind palette generator, atau <code>color-mix(in oklch, warna 60%, black)</code> di CSS modern.',
     'Skala ini juga kunci aksesibilitas: pasangan yang aman biasanya berjarak minimal 4 sampai 5 tingkat, misalnya teks 800 di atas latar 100, atau teks putih di atas tombol 600.',
     'Palet di pratinjau baru sampai 700. Tambahkan tingkat 900.'],
    html='''<div class="palet">
  <div class="chip c100">100</div><div class="chip c300">300</div><div class="chip c500">500</div><div class="chip c700">700</div>
</div>
<p class="contoh">Lencana: <span class="lencana">Terverifikasi</span></p>''',
    css=''':root { --h: 152; }
body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; }
.palet { display: grid; grid-template-columns: repeat(auto-fill, minmax(64px, 1fr)); gap: 8px; }
.chip { height: 64px; border-radius: 10px; display: grid; place-items: end start; padding: 6px; font-size: 12px; }
.c100 { background: hsl(var(--h) 60% 92%); }
.c300 { background: hsl(var(--h) 55% 72%); }
.c500 { background: hsl(var(--h) 60% 42%); color: #fff; }
.c700 { background: hsl(var(--h) 65% 28%); color: #fff; }
.lencana { background: hsl(var(--h) 60% 92%); color: hsl(var(--h) 65% 28%); padding: 2px 10px; border-radius: 99px; }''',
    task={'q': 'Tambahkan chip <code>&lt;div class="chip c900"&gt;900&lt;/div&gt;</code> dan beri <code>.c900</code> latar yang lebih gelap dari 700 (misalnya lightness 16%) dengan teks putih.',
          'test': f"(()=>{{const L={LUM},a=document.querySelector('.c900'),b=document.querySelector('.c700');return !!a&&L(getComputedStyle(a).backgroundColor)<L(getComputedStyle(b).backgroundColor)}})()",
          'hint': 'HTML: <div class="chip c900">900</div>. CSS: .c900 { background: hsl(var(--h) 70% 16%); color: #fff }'},
    pts=['Skala 50–900: terang untuk latar, gelap untuk teks.', 'Tint dicampur putih, shade dicampur hitam.', 'Pasangan aman berjarak 4–5 tingkat.'],
    qs=[q('Tingkat mana yang cocok untuk latar lencana yang lembut?', ['100', '600', '900'], 0, 'Tingkat terang untuk latar.'),
        q('Shade dibuat dengan mencampur warna dengan?', ['Putih', 'Hitam', 'Abu-abu'], 1, 'Tint dengan putih, shade dengan hitam.')],
    cek={'html_add': '<div class="palet"><div class="chip c900">900</div></div>', 'css': '.c900{background:hsl(var(--h) 70% 16%);color:#fff}'}),
  L('Warna semantik untuk state',
    ['<b>Warna semantik</b> diberi nama berdasarkan <b>makna</b>, bukan rupanya: <code>success</code> (hijau), <code>warning</code> (kuning atau oranye), <code>error</code> atau <code>danger</code> (merah), dan <code>info</code> (biru). Setiap makna punya pasangan latar lembut, border, dan teks gelap dari skala yang sama.',
     'Aturan WCAG 1.4.1: <b>warna tidak boleh menjadi satu-satunya penanda</b>. Sekitar 1 dari 12 laki-laki buta warna merah-hijau. Jadi field error diberi warna merah <b>dan</b> ikon <b>dan</b> pesan teks yang menjelaskan. Status pesanan diberi warna <b>dan</b> label "Lunas" atau "Batal".',
     'Jangan memakai merah untuk hal yang bukan bahaya atau error (misalnya warna merek), karena pengguna akan mengira ada masalah. Di Indonesia, merah juga dipakai untuk harga diskon; itu boleh, selama konsisten dan tidak dicampur dengan pesan error di layar yang sama.',
     'Alert ketiga di pratinjau seharusnya error, tetapi tampil seperti info biasa.'],
    html='''<div class="alert success"><b>✓</b> Pembayaran berhasil diterima.</div>
<div class="alert warning"><b>!</b> Kuota tersisa 2 kursi.</div>
<div class="alert info"><b>i</b> Kartu kredit ditolak oleh bank.</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; display: grid; gap: 8px; max-width: 420px; }
.alert { padding: 12px 16px; border-radius: 10px; border-left: 4px solid; display: flex; gap: 10px; }
.success { background: #E7F6EC; border-color: #1E7B45; color: #14532D; }
.warning { background: #FFF4E0; border-color: #B45309; color: #7C2D12; }
.info { background: #E8F1FB; border-color: #1D5FA8; color: #173B66; }
.error { background: #FDECEC; border-color: #B42318; color: #7A1A12; }''',
    task={'q': 'Ubah alert ketiga menjadi state error: ganti kelas <code>info</code> menjadi <code>error</code>, ganti ikonnya menjadi <b>✕</b>, dan awali pesannya dengan kata <b>Gagal:</b> agar tidak bergantung pada warna saja.',
          'test': "(a=>!!a&&a.textContent.includes('Gagal')&&a.textContent.includes('✕'))(document.querySelector('.alert.error'))",
          'hint': '<div class="alert error"><b>✕</b> Gagal: kartu kredit ditolak oleh bank.</div>'},
    pts=['Namai warna berdasarkan makna: success, warning, error, info.', 'Warna tidak boleh satu-satunya penanda: tambahkan ikon dan teks.', 'Merah hanya untuk bahaya dan error.'],
    qs=[q('Field error hanya diberi border merah. Apa masalahnya?', ['Tidak ada', 'Pengguna buta warna tidak tahu ada error', 'Merah terlalu terang'], 1, 'WCAG 1.4.1: jangan mengandalkan warna saja.'),
        q('Nama token mana yang semantik?', ['--red-600', '--color-error', '--merah-tua'], 1, 'Menyebut makna, bukan rupa.')],
    cek={'html': '<div class="alert success"><b>✓</b> Pembayaran berhasil diterima.</div><div class="alert error"><b>✕</b> Gagal: kartu ditolak.</div>'}),
  L('Dark mode',
    ['Dark mode bukan sekadar membalik warna. Prinsipnya: (1) latar <b>abu-abu sangat gelap</b> (#121212 sampai #1C1B1F), bukan hitam murni, agar bayangan dan lapisan tetap terlihat; (2) teks <b>putih yang sedikit diredam</b> (sekitar 87% opasitas) agar tidak menyilaukan; (3) <b>elevasi</b> ditunjukkan dengan latar yang sedikit lebih terang, bukan bayangan; (4) warna aksen <b>dikurangi saturasinya</b> dan dinaikkan lightness-nya (tingkat 200 sampai 300), karena warna pekat bergetar di atas latar gelap.',
     'Implementasi yang rapi memakai <b>token</b>: komponen hanya memakai <code>var(--bg)</code>, <code>var(--fg)</code>, <code>var(--surface)</code>. Lalu tema gelap cukup mendefinisikan ulang nilai token di <code>@media (prefers-color-scheme: dark)</code> atau di <code>[data-theme="dark"]</code>.',
     'Kontras tetap wajib diuji di kedua tema. Gambar dan ilustrasi juga perlu dicek: logo hitam akan hilang di latar gelap.',
     'Aplikasi di pratinjau sudah memakai token, tetapi tema gelapnya belum ditulis.'],
    html='''<div class="app" data-theme="dark">
  <div class="kartu">
    <h3>Ringkasan belajar</h3>
    <p>3 pelajaran selesai hari ini.</p>
    <button>Lanjutkan</button>
  </div>
</div>''',
    css=''':root, [data-theme="light"] { --bg: #FFFFFF; --surface: #F3F4F6; --fg: #111827; --accent: #1D5FA8; --on-accent: #FFFFFF; }
/* tulis token tema gelap di sini */

body { margin: 0; font-family: system-ui, sans-serif; }
.app { background: var(--bg); color: var(--fg); padding: 24px; min-height: 100vh; box-sizing: border-box; }
.kartu { background: var(--surface); padding: 24px; border-radius: 16px; max-width: 320px; }
button { background: var(--accent); color: var(--on-accent); border: 0; padding: 10px 20px; border-radius: 10px; }''',
    task={'q': 'Tulis aturan <code>[data-theme="dark"]</code> yang mengisi token: <code>--bg: #121417</code>, <code>--surface: #1E2227</code>, <code>--fg: #E6E8EB</code>, <code>--accent: #8DB8F2</code>, <code>--on-accent: #0B1B33</code>.',
          'test': f"(()=>{{const L={LUM};return L(getComputedStyle(document.querySelector('.app')).backgroundColor)<0.05&&L(getComputedStyle(document.querySelector('.app')).color)>0.6}})()",
          'hint': '[data-theme="dark"] { --bg: #121417; --surface: #1E2227; --fg: #E6E8EB; --accent: #8DB8F2; --on-accent: #0B1B33 }'},
    pts=['Latar abu-abu sangat gelap, bukan hitam murni.', 'Elevasi dengan latar lebih terang, aksen lebih lembut.', 'Komponen memakai token, tema hanya mengganti nilainya.'],
    qs=[q('Kenapa latar dark mode tidak hitam murni #000?', ['Agar bayangan dan lapisan tetap terlihat dan tidak terlalu kontras', 'Hitam tidak didukung browser', 'Agar hemat baterai'], 0, 'Abu-abu gelap memberi ruang untuk elevasi.'),
        q('Di dark mode, kartu yang "lebih tinggi" ditunjukkan dengan?', ['Bayangan lebih tebal', 'Latar sedikit lebih terang', 'Border merah'], 1, 'Bayangan hampir tidak terlihat di latar gelap.')],
    cek={'css': '[data-theme="dark"]{--bg:#121417;--surface:#1E2227;--fg:#E6E8EB;--accent:#8DB8F2;--on-accent:#0B1B33}'}),
]),
M('Arsitektur komponen', 'Menengah',
  'Anatomi input form, state dan hierarki tombol, kartu, modal, sheet, dan popover, serta auto layout dan batasan tata letak dinamis.',
  ['Form input', 'Button states', 'Cards', 'Overlays', 'Auto layout'], [
  L('Anatomi input form',
    ['Input form yang lengkap terdiri dari: <b>label</b> (selalu terlihat, di atas input), <b>field</b> (kotak isian), <b>placeholder</b> opsional (contoh format, bukan pengganti label), <b>helper text</b> (petunjuk di bawah), <b>pesan error</b> (menggantikan helper saat salah), serta penanda <b>wajib</b> atau <b>opsional</b>.',
     'Kesalahan paling umum: memakai placeholder sebagai label. Saat pengguna mulai mengetik, placeholder hilang dan pengguna lupa field itu untuk apa. Placeholder juga biasanya abu-abu muda dan gagal kontras.',
     'Di kode, label harus terhubung ke input dengan <code>&lt;label for="id"&gt;</code>, agar pembaca layar menyebutkan labelnya dan mengklik label ikut memfokuskan input. Pesan error dihubungkan dengan <code>aria-describedby</code>, dan field yang salah diberi <code>aria-invalid="true"</code>.',
     'Field email di pratinjau hanya punya placeholder. Tambahkan label yang terhubung.'],
    html='''<form class="form">
  <div class="field">
    <input id="email" type="email" placeholder="Email" aria-describedby="email-help">
    <p id="email-help" class="help">Kami kirim kode verifikasi ke alamat ini.</p>
  </div>
</form>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; color: #1F2933; }
.form { max-width: 320px; }
label { display: block; font-size: 14px; font-weight: 600; margin-bottom: 4px; }
input { width: 100%; box-sizing: border-box; padding: 12px; font-size: 16px; border: 1px solid #7B8794; border-radius: 8px; }
input:focus { outline: 2px solid #1D5FA8; outline-offset: 2px; }
.help { font-size: 13px; color: #52606D; margin: 4px 0 0; }''',
    task={'q': 'Tambahkan <code>&lt;label for="email"&gt;Email&lt;/label&gt;</code> di atas input, lalu ubah placeholder menjadi contoh format seperti <code>nama@contoh.com</code>.',
          'test': "!!document.querySelector('label[for=\"email\"]')&&document.getElementById('email').placeholder.includes('@')",
          'hint': '<label for="email">Email</label> sebelum <input ... placeholder="nama@contoh.com">'},
    pts=['Label selalu terlihat, placeholder hanya contoh format.', 'label for menghubungkan label ke input.', 'Error: aria-invalid dan aria-describedby.'],
    qs=[q('Kenapa placeholder tidak boleh menggantikan label?', ['Hilang saat mengetik dan biasanya kontrasnya rendah', 'Tidak didukung browser', 'Membuat form lebih lambat'], 0, 'Pengguna lupa field itu untuk apa.'),
        q('Atribut apa yang menghubungkan pesan error ke input?', ['aria-describedby', 'title', 'name'], 0, 'Pembaca layar membacakan pesan itu saat input difokuskan.')],
    cek={'html': '<label for="email">Email</label><input id="email" type="email" placeholder="nama@contoh.com">'}),
  L('State dan hierarki tombol',
    ['<b>Hierarki tombol</b>: <b>primary</b> (latar penuh, satu per layar untuk aksi utama), <b>secondary</b> (garis tepi atau latar lembut), <b>tertiary</b> atau text button (hanya teks, untuk aksi ringan seperti "Batal"). Aksi berbahaya (hapus) memakai warna danger, dan sebaiknya bukan tombol yang paling menonjol.',
     'Setiap tombol butuh tujuh <b>state</b>: default, <b>hover</b> (desktop), <b>focus-visible</b> (navigasi keyboard), <b>pressed</b> atau active, <b>disabled</b>, <b>loading</b>, dan kadang <b>selected</b>. State yang paling sering terlupa adalah focus: tanpa garis fokus yang jelas, pengguna keyboard tidak tahu sedang berada di mana.',
     'Gunakan <code>:focus-visible</code>, bukan <code>:focus</code>, agar garis fokus muncul saat navigasi keyboard tetapi tidak saat tombol diklik dengan mouse. WCAG 2.2 meminta indikator fokus yang jelas: garis minimal 2 px dengan kontras 3:1.',
     'Tombol di pratinjau sudah punya hover dan disabled, tetapi belum punya fokus. Tekan Tab di pratinjau untuk melihat masalahnya.'],
    html='''<div class="aksi">
  <button class="btn primary">Simpan</button>
  <button class="btn secondary">Pratinjau</button>
  <button class="btn tertiary">Batal</button>
  <button class="btn primary" disabled>Kirim</button>
</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.aksi { display: flex; gap: 8px; flex-wrap: wrap; }
.btn { font: inherit; font-weight: 600; padding: 10px 20px; border-radius: 10px; border: 1px solid transparent; cursor: pointer; outline: none; min-height: 44px; }
.primary { background: #1D5FA8; color: #fff; }
.primary:hover { background: #174C86; }
.secondary { background: #fff; color: #1D5FA8; border-color: #1D5FA8; }
.secondary:hover { background: #E8F1FB; }
.tertiary { background: transparent; color: #1D5FA8; }
.btn:disabled { background: #E4E7EB; color: #7B8794; border-color: transparent; cursor: not-allowed; }''',
    task={'q': 'Tambahkan aturan <code>.btn:focus-visible</code> dengan <code>outline</code> minimal 2px dan <code>outline-offset</code> 2px.',
          'test': f"{RULES}.some(r=>r.selectorText&&r.selectorText.includes(':focus-visible')&&parseFloat(r.style.outlineWidth)>=2)",
          'hint': '.btn:focus-visible { outline: 3px solid #F59E0B; outline-offset: 2px }'},
    pts=['Primary satu per layar, secondary, tertiary.', 'State: default, hover, focus-visible, pressed, disabled, loading.', 'Focus-visible minimal 2 px, kontras 3:1.'],
    qs=[q('Berapa tombol primary yang disarankan dalam satu layar?', ['Satu', 'Tiga', 'Sebanyak mungkin'], 0, 'Satu aksi utama yang jelas.'),
        q('Kenapa memakai :focus-visible, bukan :focus?', ['Garis fokus muncul untuk keyboard, tidak saat diklik mouse', 'Lebih cepat', ':focus sudah usang'], 0, 'Tetap aksesibel tanpa mengganggu pengguna mouse.')],
    cek={'css': '.btn:focus-visible{outline:3px solid #F59E0B;outline-offset:2px}'}),
  L('Kartu',
    ['<b>Kartu</b> mengelompokkan informasi tentang <b>satu hal</b>: satu produk, satu artikel, satu kelas. Anatominya: <b>media</b> (gambar), <b>header</b> (judul, subjudul), <b>isi</b> singkat, dan <b>aksi</b>. Tidak semua bagian wajib, tetapi urutannya sebaiknya konsisten di seluruh produk.',
     'Gambar di kartu harus punya <b>rasio tetap</b> (16:9, 4:3, atau 1:1), agar grid kartu rapi walau foto aslinya berbeda ukuran. Di CSS: <code>aspect-ratio: 16 / 9</code> dengan <code>object-fit: cover</code>. Di Figma: frame dengan rasio tetap dan gambar mode Fill.',
     'Jika seluruh kartu bisa diklik, jangan taruh terlalu banyak tombol di dalamnya, karena target klik bertumpuk membingungkan. Pilih: kartu yang bisa diklik dengan satu tujuan, atau kartu statis dengan tombol aksi yang jelas.',
     'Area media di kartu pratinjau belum punya rasio, sehingga tingginya nol.'],
    html='''<article class="kartu">
  <div class="media" role="img" aria-label="Ilustrasi kelas Flutter"></div>
  <div class="isi">
    <p class="label">Mobile · Pemula</p>
    <h3>Flutter dari Nol</h3>
    <p>Bangun aplikasi Android dan iOS pertamamu dalam 4 minggu.</p>
    <a href="#" class="aksi">Lihat kelas</a>
  </div>
</article>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; background: #F4F5F7; }
.kartu { max-width: 320px; background: #fff; border-radius: 16px; overflow: hidden; box-shadow: 0 1px 3px rgb(0 0 0 / .12); }
.media { width: 100%; background: linear-gradient(135deg, #0D5DB8, #63D9B5); }
.isi { padding: 16px 24px 24px; }
.isi > * { margin: 0 0 8px; }
.label { font-size: 12px; color: #52606D; text-transform: uppercase; letter-spacing: .06em; }
.aksi { color: #0D5DB8; font-weight: 600; }''',
    task={'q': 'Beri <code>.media</code> rasio <code>aspect-ratio: 16 / 9</code>.',
          'test': f"{G.format('.media')}.aspectRatio.replace(/\\s/g,'')==='16/9'",
          'hint': '.media { aspect-ratio: 16 / 9 }'},
    pts=['Satu kartu, satu hal.', 'Media dengan rasio tetap dan object-fit: cover.', 'Pilih: seluruh kartu bisa diklik, atau tombol aksi yang jelas.'],
    qs=[q('Kenapa gambar kartu diberi aspect-ratio tetap?', ['Agar grid rapi walau ukuran foto asli berbeda', 'Agar gambar lebih tajam', 'Agar file kecil'], 0, 'Tinggi kartu menjadi seragam.'),
        q('Kartu yang seluruhnya bisa diklik berisi 4 tombol berbeda. Masalahnya?', ['Target klik bertumpuk dan membingungkan', 'Tidak ada', 'Kartu terlalu kecil'], 0, 'Pilih satu pola interaksi.')],
    cek={'css': '.media{aspect-ratio:16/9}'}),
  L('Modal, sheet, dan popover',
    ['Ketiganya adalah <b>lapisan</b> di atas konten. <b>Modal dialog</b> menghentikan alur dan meminta keputusan (konfirmasi hapus, form singkat); latar di belakangnya digelapkan (scrim) dan tidak bisa diklik. <b>Bottom sheet</b> muncul dari bawah layar ponsel, mudah dijangkau jempol, cocok untuk pilihan dan filter. <b>Popover</b> atau menu kecil menempel pada elemen pemicunya, tanpa menghentikan alur.',
     'Aturan pakai: modal hanya untuk hal yang <b>benar-benar butuh perhatian</b>, karena setiap modal memotong pekerjaan pengguna. Selalu sediakan cara keluar yang jelas (tombol tutup, tombol Batal, tombol Esc, tap di scrim). Di dalam modal, fokus keyboard harus terkunci (focus trap) dan kembali ke pemicu saat ditutup.',
     'Di HTML modern, pakai <code>&lt;dialog&gt;</code> dengan <code>showModal()</code> untuk modal, dan atribut <code>popover</code> untuk popover. Keduanya sudah menangani lapisan, Esc, dan aksesibilitas dasar.',
     'Sheet di pratinjau masih mengalir di dalam halaman. Tempelkan ke bawah layar.'],
    html='''<main class="hal"><h2>Daftar kelas</h2><p>Ketuk Filter untuk menyaring kelas.</p></main>
<div class="scrim"></div>
<section class="sheet" aria-label="Filter">
  <div class="pegangan"></div>
  <h3>Filter kelas</h3>
  <label><input type="checkbox" checked> Gratis</label>
  <label><input type="checkbox"> Bersertifikat</label>
  <button>Terapkan</button>
</section>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; min-height: 100vh; }
.hal { padding: 16px; }
.scrim { position: fixed; inset: 0; background: rgb(0 0 0 / .4); }
.sheet { background: #fff; border-radius: 20px 20px 0 0; padding: 12px 24px 24px; display: grid; gap: 12px; z-index: 1; }
.pegangan { width: 32px; height: 4px; border-radius: 2px; background: #9AA5B1; margin: 0 auto 8px; }
.sheet h3 { margin: 0; }
.sheet button { padding: 12px; border: 0; border-radius: 12px; background: #1D5FA8; color: #fff; font: inherit; font-weight: 600; }''',
    task={'q': 'Jadikan <code>.sheet</code> bottom sheet: <code>position: fixed</code>, menempel di bawah (<code>left: 0; right: 0; bottom: 0</code>).',
          'test': f"(s=>s.position==='fixed'&&s.bottom==='0px'&&s.left==='0px')({G.format('.sheet')})",
          'hint': '.sheet { position: fixed; left: 0; right: 0; bottom: 0 }'},
    pts=['Modal menghentikan alur, sheet dari bawah, popover menempel pada pemicu.', 'Selalu ada cara keluar: tutup, Batal, Esc, tap scrim.', 'Pakai dialog dan atribut popover.'],
    qs=[q('Memilih urutan dan filter di ponsel paling nyaman dengan?', ['Modal di tengah', 'Bottom sheet', 'Halaman baru'], 1, 'Mudah dijangkau jempol.'),
        q('Apa itu scrim?', ['Lapisan gelap di belakang modal', 'Animasi tombol', 'Jenis font'], 0, 'Menandakan konten di belakang tidak aktif.')],
    cek={'css': '.sheet{position:fixed;left:0;right:0;bottom:0}'}),
  L('Auto layout dan batasan tata letak dinamis',
    ['<b>Auto layout</b> di Figma membuat frame menyusun anaknya otomatis, persis seperti flexbox di CSS: arah (horizontal atau vertikal), <b>gap</b> (jarak antar anak), <b>padding</b>, dan perataan. Saat teks tombol berubah dari "Simpan" menjadi "Simpan perubahan", tombol ikut melebar sendiri.',
     'Setiap anak punya aturan ukuran: <b>Hug contents</b> (selebar isinya, sama dengan <code>width: auto</code>), <b>Fill container</b> (mengisi sisa ruang, sama dengan <code>flex: 1</code>), atau <b>Fixed</b> (ukuran tetap). Ditambah <b>min dan max width</b> agar tidak terlalu sempit atau lebar.',
     '<b>Constraints</b> (batasan) mengatur perilaku elemen saat frame induk diubah ukurannya: menempel kiri, kanan, kiri-dan-kanan (melar), tengah, atau skala. Desain yang memakai auto layout dan constraints dengan benar sudah "responsif" sejak di Figma, dan developer tinggal menerjemahkannya ke flex dan grid.',
     'Baris notifikasi di pratinjau: teks harus Fill, tombol harus Hug di kanan.'],
    html='''<div class="notif">
  <span class="ikon">🔔</span>
  <p class="isi">Kelas Kotlin dimulai besok pukul 19.00 WIB.</p>
  <button class="tutup">Tutup</button>
</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; }
.notif { display: flex; align-items: center; gap: 12px; padding: 12px 16px; background: #FFF7E6; border-radius: 12px; max-width: 520px; }
.isi { margin: 0; }
.tutup { font: inherit; border: 0; background: none; color: #8A4B2A; font-weight: 600; padding: 8px; }''',
    task={'q': 'Jadikan <code>.isi</code> Fill container (<code>flex: 1</code>) agar tombol Tutup terdorong ke kanan.',
          'test': f"{G.format('.isi')}.flexGrow==='1'",
          'hint': '.isi { flex: 1 }'},
    pts=['Auto layout = flexbox: arah, gap, padding, perataan.', 'Hug = auto, Fill = flex: 1, Fixed = ukuran tetap.', 'Constraints mengatur perilaku saat induk diubah ukurannya.'],
    qs=[q('Fill container di Figma setara dengan CSS?', ['width: auto', 'flex: 1', 'position: absolute'], 1, 'Mengisi sisa ruang.'),
        q('Tombol yang melebar sendiri saat teksnya bertambah memakai?', ['Hug contents', 'Fixed', 'Constraints scale'], 0, 'Selebar isinya.')],
    cek={'css': '.isi{flex:1}'}),
]),
M('Design system dan token', 'Menengah',
  'Fondasi token, penamaan global dan alias, varian dan properti komponen, set ikon dan aset, serta dokumentasi pedoman pola.',
  ['Design tokens', 'Naming', 'Variants', 'Icons', 'Documentation'], [
  L('Fondasi design token',
    ['<b>Design token</b> adalah keputusan desain yang diberi nama dan disimpan sebagai data: warna, ukuran huruf, jarak, radius, bayangan, durasi animasi. Bukan <code>#1D5FA8</code> yang ditulis di 40 tempat, melainkan <code>color.brand.600</code> yang dirujuk 40 kali. Mengubah satu token mengubah seluruh produk.',
     'Token ditulis sekali dalam format netral (JSON mengikuti spesifikasi DTCG, Design Tokens Community Group), lalu diubah otomatis menjadi CSS variables, konstanta Dart, Kotlin, atau Swift dengan alat seperti Style Dictionary. Di Figma, token disimpan sebagai <b>Variables</b>.',
     'Kategori token dasar: <b>color</b>, <b>typography</b> (keluarga, ukuran, tebal, line-height), <b>spacing</b>, <b>radius</b>, <b>shadow</b> atau elevation, <b>motion</b> (durasi, easing), dan <b>breakpoint</b>.',
     'Tombol di pratinjau masih memakai warna dan angka langsung. Ganti dengan token.'],
    html='''<button class="tombol">Mulai belajar</button>''',
    css=''':root {
  --color-brand-600: #1D5FA8;
  --color-white: #FFFFFF;
  --space-2: 16px;
  --space-3: 24px;
  --radius-md: 10px;
}
body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.tombol { background: #1D5FA8; color: #FFFFFF; padding: 16px 24px; border-radius: 10px; border: 0; font: inherit; font-weight: 600; }''',
    task={'q': 'Ubah <code>.tombol</code> agar semua nilainya memakai token: <code>var(--color-brand-600)</code>, <code>var(--color-white)</code>, <code>var(--space-2)</code>, <code>var(--space-3)</code>, dan <code>var(--radius-md)</code>.',
          'test': f"{RULES}.some(r=>r.selectorText==='.tombol'&&(r.style.cssText.match(/var\\(--/g)||[]).length>=4)",
          'hint': '.tombol { background: var(--color-brand-600); color: var(--color-white); padding: var(--space-2) var(--space-3); border-radius: var(--radius-md); ... }'},
    pts=['Token = keputusan desain bernama, disimpan sebagai data.', 'Format DTCG, diubah ke banyak platform dengan Style Dictionary.', 'Kategori: color, typography, spacing, radius, shadow, motion.'],
    qs=[q('Keuntungan utama token?', ['Mengubah satu nilai mengubah seluruh produk', 'File CSS lebih kecil', 'Tidak perlu Figma'], 0, 'Satu sumber kebenaran.'),
        q('Di Figma, token disimpan sebagai?', ['Variables', 'Frames', 'Plugins'], 0, 'Figma Variables mendukung mode seperti light dan dark.')],
    cek={'css': '.tombol{background:var(--color-brand-600);color:var(--color-white);padding:var(--space-2) var(--space-3);border-radius:var(--radius-md)}'}),
  L('Penamaan token global dan alias',
    ['Token disusun dalam tiga lapis. <b>Global</b> atau primitive: nilai mentah tanpa makna, misalnya <code>blue-600: #1D5FA8</code>, <code>space-4: 16px</code>. <b>Alias</b> atau semantic: peran, merujuk ke global, misalnya <code>color-action-primary: {blue-600}</code>, <code>color-text-danger: {red-700}</code>. <b>Component</b>: khusus satu komponen, merujuk ke alias, misalnya <code>button-primary-bg: {color-action-primary}</code>.',
     'Komponen hanya boleh memakai token alias atau component, <b>tidak pernah</b> global langsung. Dengan begitu, rebranding dari biru ke hijau cukup mengubah satu baris alias. Dark mode cukup mengubah ke mana alias menunjuk.',
     'Pola penamaan yang umum: <b>kategori-peran-varian-state</b>, misalnya <code>color-bg-surface</code>, <code>color-text-muted</code>, <code>color-border-input-focus</code>. Pakai kata yang dipahami desainer dan developer, dan konsisten dalam satu bahasa.',
     'Pratinjau baru punya token global. Buat token alias untuk aksi utama.'],
    html='''<button class="tombol">Bayar sekarang</button>''',
    css=''':root {
  /* global */
  --blue-600: #1D5FA8;
  --green-600: #1E7B45;
  --white: #FFFFFF;
  /* alias: tulis di sini */
}
body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.tombol { background: var(--color-action-primary, #999); color: var(--white); border: 0; padding: 16px 24px; border-radius: 10px; font: inherit; font-weight: 600; }''',
    task={'q': 'Tambahkan token alias <code>--color-action-primary: var(--green-600)</code> di <code>:root</code>. Tombol akan berubah hijau tanpa menyentuh aturan <code>.tombol</code>.',
          'test': f"getComputedStyle(document.documentElement).getPropertyValue('--color-action-primary').trim()!==''&&{G.format('.tombol')}.backgroundColor==='rgb(30, 123, 69)'",
          'hint': ':root { --color-action-primary: var(--green-600) }'},
    pts=['Tiga lapis: global, alias (semantic), component.', 'Komponen tidak memakai token global langsung.', 'Pola nama: kategori-peran-varian-state.'],
    qs=[q('Mana token alias?', ['--blue-600', '--color-text-danger', '#1D5FA8'], 1, 'Menyebut peran, merujuk ke global.'),
        q('Rebranding biru ke hijau paling mudah jika komponen memakai?', ['Token global', 'Token alias', 'Kode warna langsung'], 1, 'Cukup ubah ke mana alias menunjuk.')],
    cek={'css': ':root{--color-action-primary:var(--green-600)}'}),
  L('Varian dan properti komponen',
    ['Satu komponen punya banyak bentuk. Di Figma, bentuk-bentuk itu disusun sebagai <b>variants</b> dalam satu <b>component set</b>, dengan <b>properties</b>: <code>Size = sm | md | lg</code>, <code>Variant = primary | secondary | danger</code>, <code>State = default | hover | disabled</code>, <code>Icon = true | false</code>. Pengguna komponen tinggal memilih dari panel kanan.',
     'Selain variant property, Figma punya <b>boolean property</b> (tampilkan atau sembunyikan ikon), <b>text property</b> (ubah label tanpa membongkar komponen), dan <b>instance swap</b> (ganti ikon dengan ikon lain). Desain yang baik membatasi jumlah kombinasi agar tidak meledak: 3 ukuran × 3 varian × 4 state = 36 varian sudah banyak.',
     'Properti di Figma sebaiknya bernama sama dengan prop di kode: <code>&lt;Button size="lg" variant="danger"&gt;</code> di React, <code>Button(size = Size.Large)</code> di Compose. Di CSS, varian bisa memakai kelas modifier (<code>.btn--lg</code>) atau atribut data (<code>[data-size="lg"]</code>).',
     'Tombol di pratinjau sudah punya ukuran sm dan md. Lengkapi ukuran lg.'],
    html='''<div class="baris">
  <button class="btn" data-size="sm">Kecil</button>
  <button class="btn" data-size="md">Sedang</button>
  <button class="btn" data-size="lg">Besar</button>
</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.baris { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.btn { font: inherit; font-weight: 600; border: 0; border-radius: 10px; background: #1D5FA8; color: #fff; box-sizing: border-box; }
.btn[data-size="sm"] { height: 32px; padding: 0 12px; font-size: 14px; }
.btn[data-size="md"] { height: 40px; padding: 0 16px; font-size: 15px; }''',
    task={'q': 'Tambahkan aturan <code>.btn[data-size="lg"]</code> dengan tinggi <b>48px</b>, padding kiri-kanan 24px, dan font-size 16px.',
          'test': "Math.round(document.querySelector('[data-size=\"lg\"]').getBoundingClientRect().height)===48",
          'hint': '.btn[data-size="lg"] { height: 48px; padding: 0 24px; font-size: 16px }'},
    pts=['Variants dalam satu component set, diatur lewat properties.', 'Boolean, text, dan instance swap property.', 'Nama properti Figma = nama prop di kode.'],
    qs=[q('Menyembunyikan ikon di tombol Figma paling tepat memakai?', ['Variant baru', 'Boolean property', 'Detach instance'], 1, 'Satu saklar tampil atau sembunyi.'),
        q('Kenapa nama properti Figma sebaiknya sama dengan prop di kode?', ['Agar handoff jelas dan tidak perlu menerjemahkan', 'Aturan Figma', 'Agar file kecil'], 0, 'Desainer dan developer memakai bahasa yang sama.')],
    cek={'css': '.btn[data-size="lg"]{height:48px;padding:0 24px;font-size:16px}'}),
  L('Set ikon dan aset',
    ['Ikon dalam satu produk harus berasal dari <b>satu set</b> dengan gaya seragam: grid yang sama (biasanya 24 × 24 dengan area aman 2 px), ketebalan garis sama (1,5 atau 2 px), sudut sama, dan gaya sama (outline atau filled). Set populer: Material Symbols, Lucide, Phosphor, Heroicons. Mencampur set membuat UI terasa "tambal sulam".',
     'Format: <b>SVG</b> untuk ikon dan ilustrasi sederhana (tajam di semua ukuran, bisa diwarnai dengan <code>currentColor</code>). <b>PNG</b> atau <b>WebP</b> untuk foto dan gambar kompleks, diekspor @1x, @2x, @3x untuk mobile. Di Figma, atur <b>Export settings</b> pada setiap aset dan beri nama dengan pola konsisten: <code>ic_cart_24.svg</code>, <code>img_onboarding_1@2x.png</code>.',
     'Aksesibilitas ikon: ikon dekoratif diberi <code>aria-hidden="true"</code>. Tombol yang hanya berisi ikon <b>wajib</b> punya nama yang bisa dibaca: <code>aria-label="Keranjang"</code>. Target sentuhnya tetap minimal 44 sampai 48 px walau ikonnya 24 px.',
     'Tombol keranjang di pratinjau hanya berisi ikon dan tidak punya nama.'],
    html='''<button class="ikon-btn">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.6 12.4a2 2 0 0 0 2 1.6h8.8a2 2 0 0 0 2-1.6L22 7H6"/></svg>
</button>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.ikon-btn { width: 48px; height: 48px; display: grid; place-items: center; border: 0; border-radius: 12px; background: #E8F1FB; color: #1D5FA8; }''',
    task={'q': 'Beri tombol <code>aria-label="Keranjang"</code>, dan beri SVG di dalamnya <code>aria-hidden="true"</code>.',
          'test': "(b=>b.getAttribute('aria-label')==='Keranjang'&&b.querySelector('svg').getAttribute('aria-hidden')==='true')(document.querySelector('.ikon-btn'))",
          'hint': '<button class="ikon-btn" aria-label="Keranjang"><svg aria-hidden="true" ...>'},
    pts=['Satu set ikon dengan grid, garis, dan gaya seragam.', 'SVG untuk ikon, PNG/WebP @1x @2x @3x untuk gambar.', 'Tombol ikon wajib punya aria-label, ikon dekoratif aria-hidden.'],
    qs=[q('Format terbaik untuk ikon yang perlu berubah warna mengikuti teks?', ['PNG', 'SVG dengan currentColor', 'JPG'], 1, 'SVG tajam dan bisa diwarnai.'),
        q('Tombol hanya berisi ikon tempat sampah. Apa yang wajib ditambahkan?', ['aria-label="Hapus"', 'title saja', 'Tidak perlu apa-apa'], 0, 'Pembaca layar butuh nama tombol.')],
    cek={'html': '<button class="ikon-btn" aria-label="Keranjang"><svg aria-hidden="true" width="24" height="24"></svg></button>'}),
  L('Dokumentasi pedoman pola',
    ['Komponen tanpa dokumentasi akan dipakai dengan cara yang berbeda-beda oleh setiap orang. Halaman dokumentasi yang baik berisi: <b>deskripsi</b> singkat, <b>kapan dipakai</b> dan <b>kapan tidak</b>, <b>anatomi</b> (bagian-bagian bernomor), <b>varian dan state</b>, <b>contoh Do dan Don\'t</b>, <b>panduan konten</b> (panjang label, gaya kalimat), <b>aksesibilitas</b>, dan <b>kode</b>.',
     'Contoh <b>Do dan Don\'t</b> adalah bagian yang paling sering dibaca, karena langsung menunjukkan kesalahan umum. Taruh berdampingan: kiri hijau "Lakukan", kanan merah "Jangan", masing-masing dengan alasan satu kalimat.',
     'Dokumentasi bisa dibuat di Figma (halaman khusus di library), Zeroheight, Supernova, atau Storybook untuk kode. Yang penting: satu tempat yang diketahui semua orang, dan diperbarui setiap kali komponen berubah, lengkap dengan changelog.',
     'Halaman dokumentasi tombol di pratinjau baru punya contoh Do.'],
    html='''<section class="dok">
  <h2>Tombol primary</h2>
  <p>Untuk satu aksi utama di setiap layar.</p>
  <div class="contoh">
    <figure class="do"><div class="demo"><button class="p">Simpan</button><button class="s">Batal</button></div><figcaption><b>Lakukan:</b> satu primary, aksi lain secondary.</figcaption></figure>
  </div>
</section>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 16px; color: #1F2933; }
.contoh { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }
figure { margin: 0; border-radius: 12px; overflow: hidden; border-top: 4px solid; background: #F5F7FA; }
.do { border-color: #1E7B45; }
.dont { border-color: #B42318; }
.demo { padding: 24px; display: flex; gap: 8px; }
figcaption { padding: 12px 16px; font-size: 14px; background: #fff; }
.p, .s { font: inherit; padding: 8px 16px; border-radius: 8px; border: 1px solid #1D5FA8; }
.p { background: #1D5FA8; color: #fff; }
.s { background: #fff; color: #1D5FA8; }''',
    task={'q': 'Tambahkan contoh <code>&lt;figure class="dont"&gt;</code> di dalam <code>.contoh</code>: dua tombol primary berdampingan, dengan keterangan "<b>Jangan:</b> dua primary di satu layar."',
          'test': "(f=>!!f&&f.querySelectorAll('.p').length>=2&&f.textContent.includes('Jangan'))(document.querySelector('.contoh .dont'))",
          'hint': '<figure class="dont"><div class="demo"><button class="p">Simpan</button><button class="p">Kirim</button></div><figcaption><b>Jangan:</b> dua primary di satu layar.</figcaption></figure>'},
    pts=['Isi dokumentasi: kapan dipakai, anatomi, varian, Do/Don\'t, konten, aksesibilitas, kode.', 'Do dan Don\'t berdampingan dengan alasan.', 'Satu tempat, diperbarui bersama changelog.'],
    qs=[q('Bagian dokumentasi yang paling cepat mencegah kesalahan umum?', ['Riwayat versi', 'Contoh Do dan Don\'t', 'Daftar kontributor'], 1, 'Menunjukkan langsung yang benar dan salah.'),
        q('Storybook paling cocok untuk mendokumentasikan?', ['Komponen kode', 'Riset pengguna', 'Anggaran proyek'], 0, 'Menampilkan komponen kode dengan semua state.')],
    cek={'html': '<div class="contoh"><figure class="dont"><div class="demo"><button class="p">A</button><button class="p">B</button></div><figcaption><b>Jangan:</b> dua primary.</figcaption></figure></div>'}),
]),
M('Layout responsif dan handoff', 'Menengah',
  'Breakpoint fluid dan aturan container, pola navigasi mobile, layout dashboard desktop, redlining dan spesifikasi, serta sesi handoff kolaboratif.',
  ['Breakpoints', 'Mobile navigation', 'Dashboard layout', 'Redlines', 'Handoff'], [
  L('Breakpoint fluid dan aturan container',
    ['<b>Breakpoint</b> adalah lebar layar tempat tata letak berubah. Titik yang umum: <b>&lt; 600</b> (ponsel), <b>600 sampai 839</b> (tablet tegak dan lipat), <b>840 sampai 1199</b> (tablet mendatar, laptop kecil), <b>≥ 1200</b> (desktop). Material 3 menamainya compact, medium, expanded, large, dan extra-large. Tentukan breakpoint dari <b>konten</b> yang mulai rusak, bukan dari merek perangkat.',
     'Di antara breakpoint, layout harus <b>fluid</b>: kolom melebar mengikuti layar. Grid web yang umum: 4 kolom di ponsel (margin 16 px), 8 kolom di tablet (margin 24 sampai 32 px), 12 kolom di desktop. <b>Container</b> membatasi lebar maksimum isi (misalnya 1200 px) agar baris teks tidak terlalu panjang di monitor lebar.',
     'Teknik CSS tanpa media query: <code>grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))</code> membuat kartu otomatis 1, 2, 3, atau 4 kolom sesuai ruang. Container query (<code>@container</code>) membuat komponen menyesuaikan lebar <b>induknya</b>, bukan lebar layar.',
     'Grid kartu di pratinjau terkunci 3 kolom dan sesak di layar kecil.'],
    html='''<div class="container">
  <div class="grid">
    <div class="kartu">Dart</div><div class="kartu">Flutter</div><div class="kartu">Kotlin</div>
    <div class="kartu">Compose</div><div class="kartu">KMP</div><div class="kartu">UI Design</div>
  </div>
</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 16px clamp(16px, 4vw, 32px); }
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.kartu { padding: 24px 16px; border-radius: 12px; background: #E8F1FB; font-weight: 600; }''',
    task={'q': 'Ubah <code>.grid</code> menjadi fluid: <code>grid-template-columns: repeat(auto-fit, minmax(160px, 1fr))</code>.',
          'test': f"{RULES}.some(r=>r.selectorText==='.grid'&&/auto-(fit|fill)/.test(r.style.gridTemplateColumns))",
          'hint': '.grid { grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)) }'},
    pts=['Breakpoint dari konten: compact, medium, expanded.', '4, 8, 12 kolom; container membatasi lebar maksimum.', 'auto-fit + minmax dan container query.'],
    qs=[q('Breakpoint sebaiknya ditentukan berdasarkan?', ['Merek ponsel terlaris', 'Titik saat konten mulai rusak', 'Selera klien'], 1, 'Konten yang menentukan.'),
        q('repeat(auto-fit, minmax(240px, 1fr)) di layar 1000 px menghasilkan berapa kolom (abaikan gap)?', ['2', '4', '6'], 1, '1000 / 240 = 4 kolom muat.')],
    cek={'css': '.grid{grid-template-columns:repeat(auto-fit,minmax(160px,1fr))}'}),
  L('Pola navigasi mobile',
    ['Pola navigasi utama di ponsel: <b>bottom navigation bar</b> (3 sampai 5 tujuan utama, selalu terlihat, mudah dijangkau jempol), <b>tab bar atas</b> (berpindah antar tampilan dalam satu bagian), <b>navigation drawer</b> (menu samping untuk banyak tujuan, tapi tersembunyi sehingga jarang ditemukan), dan <b>top app bar</b> dengan tombol kembali.',
     'Aturan bottom navigation: setiap item punya <b>ikon dan label</b> (label tidak boleh disembunyikan, ikon saja sering disalahpahami), item aktif ditandai dengan lebih dari warna (indikator pill di Material 3, ikon filled di iOS), dan target sentuh minimal 48 dp tinggi.',
     'Di kode, tandai item aktif dengan <code>aria-current="page"</code>. Hormati area aman (safe area) di bawah layar iPhone dan Android modern dengan <code>padding-bottom: env(safe-area-inset-bottom)</code>.',
     'Bottom nav di pratinjau belum menandai halaman aktif dan terlalu pendek.'],
    html='''<nav class="bottom-nav" aria-label="Navigasi utama">
  <a href="#" class="item"><span aria-hidden="true">🏠</span>Beranda</a>
  <a href="#" class="item aktif"><span aria-hidden="true">📚</span>Kelas</a>
  <a href="#" class="item"><span aria-hidden="true">🏆</span>Peringkat</a>
  <a href="#" class="item"><span aria-hidden="true">👤</span>Profil</a>
</nav>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; min-height: 100vh; background: #F4F5F7; }
.bottom-nav { position: fixed; left: 0; right: 0; bottom: 0; display: flex; background: #fff; border-top: 1px solid #E4E7EB; padding-bottom: env(safe-area-inset-bottom); }
.item { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 4px 0; font-size: 12px; color: #52606D; text-decoration: none; }
.aktif { color: #0D5DB8; font-weight: 600; }''',
    task={'q': 'Beri item Kelas <code>aria-current="page"</code>, dan buat setiap <code>.item</code> minimal 56px tingginya (misalnya <code>min-height: 56px</code>).',
          'test': "!!document.querySelector('.bottom-nav [aria-current=\"page\"]')&&[...document.querySelectorAll('.bottom-nav .item')].every(a=>a.getBoundingClientRect().height>=56)",
          'hint': '<a ... class="item aktif" aria-current="page"> dan .item { min-height: 56px; justify-content: center }'},
    pts=['Bottom nav: 3–5 tujuan, ikon + label, mudah dijangkau.', 'Item aktif ditandai lebih dari warna, aria-current="page".', 'Target 48 dp dan safe area bawah.'],
    qs=[q('Aplikasi punya 4 tujuan utama yang sering dipakai. Pola terbaik di ponsel?', ['Navigation drawer', 'Bottom navigation', 'Footer link'], 1, 'Selalu terlihat dan mudah dijangkau jempol.'),
        q('Bolehkah label bottom navigation disembunyikan agar rapi?', ['Boleh', 'Tidak, ikon saja sering disalahpahami'], 1, 'Label membuat tujuan jelas.')],
    cek={'html': '<nav class="bottom-nav"><a class="item" aria-current="page" style="min-height:56px">A</a><a class="item" style="min-height:56px">B</a></nav>'}),
  L('Layout dashboard desktop',
    ['Dashboard desktop biasanya terdiri dari: <b>sidebar</b> navigasi (lebar tetap 240 sampai 280 px, bisa diciutkan menjadi ikon), <b>header</b> (judul halaman, pencarian, profil), dan <b>area utama</b> berisi kartu KPI di atas, grafik di tengah, dan tabel detail di bawah. Urutan ini mengikuti cara orang membaca: ringkasan dulu, detail kemudian.',
     'Letakkan angka terpenting di <b>kiri atas</b> area utama, karena pembaca bahasa Latin memindai dengan pola F. Kartu KPI berisi: label, angka besar, perubahan (naik 12% dibanding minggu lalu) dengan ikon panah, bukan hanya warna.',
     'CSS Grid dengan <b>grid-template-areas</b> membuat struktur dashboard terbaca seperti peta. Di layar kecil, ubah area menjadi satu kolom dan sidebar menjadi drawer atau bottom nav.',
     'Dashboard di pratinjau belum punya struktur. Susun dengan grid-template-areas.'],
    html='''<div class="dash">
  <aside class="side">Menu</aside>
  <header class="head">Ringkasan penjualan</header>
  <main class="main">
    <div class="kpi"><small>Pendapatan</small><b>Rp48,2 jt</b><span>▲ 12%</span></div>
    <div class="kpi"><small>Pesanan</small><b>1.284</b><span>▲ 4%</span></div>
    <div class="kpi"><small>Retur</small><b>23</b><span>▼ 2%</span></div>
  </main>
</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; }
.dash { display: grid; min-height: 100vh; gap: 0; }
.side { grid-area: sidebar; background: #0F172A; color: #CBD5E1; padding: 16px; }
.head { grid-area: header; padding: 16px 24px; border-bottom: 1px solid #E4E7EB; font-weight: 700; }
.main { grid-area: main; padding: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; align-content: start; }
.kpi { display: grid; gap: 4px; padding: 16px; border-radius: 12px; background: #F5F7FA; }
.kpi b { font-size: 24px; }''',
    task={'q': 'Beri <code>.dash</code> struktur: <code>grid-template-columns: 200px 1fr</code> dan <code>grid-template-areas: "sidebar header" "sidebar main"</code>.',
          'test': f"(s=>s.gridTemplateAreas.includes('sidebar')&&s.gridTemplateAreas.includes('main'))({G.format('.dash')})",
          'hint': '.dash { grid-template-columns: 200px 1fr; grid-template-rows: auto 1fr; grid-template-areas: "sidebar header" "sidebar main" }'},
    pts=['Sidebar, header, area utama: KPI, grafik, tabel.', 'Angka terpenting di kiri atas (pola F).', 'grid-template-areas sebagai peta layout.'],
    qs=[q('Di mana angka terpenting dashboard diletakkan?', ['Kanan bawah', 'Kiri atas', 'Di dalam sidebar'], 1, 'Mata memindai dengan pola F.'),
        q('Kartu KPI menampilkan perubahan turun hanya dengan warna merah. Perbaikannya?', ['Tambahkan ikon panah dan teks persentase', 'Pakai merah lebih gelap', 'Hilangkan'], 0, 'Jangan mengandalkan warna saja.')],
    cek={'css': '.dash{grid-template-columns:200px 1fr;grid-template-areas:"sidebar header" "sidebar main"}'}),
  L('Redlining dan spesifikasi',
    ['<b>Redlining</b> adalah memberi anotasi ukuran pada desain: jarak, padding, ukuran huruf, radius, warna, dan perilaku. Dulu digambar manual dengan garis merah; sekarang Figma <b>Dev Mode</b> menampilkannya otomatis saat developer mengklik elemen, lengkap dengan nilai token.',
     'Yang tetap harus ditulis desainer, karena tidak terlihat di gambar statis: <b>perilaku responsif</b> (apa yang melar, apa yang tetap), <b>semua state</b> (hover, focus, disabled, loading, error, empty), <b>teks terpanjang</b> (nama 40 huruf, harga Rp1.250.000.000), <b>animasi</b> (durasi, easing), dan <b>logika</b> (kapan tombol aktif, validasi apa).',
     'Spesifikasi yang baik memakai <b>nama token</b>, bukan angka mentah: tulis "padding space-2 / space-3, radius-md, color-action-primary", bukan "16px, 24px, 10px, #1D5FA8". Developer tinggal mencocokkan token yang sama di kode.',
     'Tombol di pratinjau belum sesuai spesifikasi: padding 16px atas-bawah dan 24px kiri-kanan, radius 12px.'],
    html='''<div class="spes">
  <button class="tombol">Konfirmasi pesanan</button>
  <ul>
    <li>Padding: space-2 (16px) atas-bawah, space-3 (24px) kiri-kanan</li>
    <li>Radius: radius-lg (12px)</li>
    <li>Tinggi minimum: 48px</li>
  </ul>
</div>''',
    css='''body { font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
.spes ul { font-size: 14px; color: #52606D; padding-left: 20px; }
.tombol { font: inherit; font-weight: 600; background: #1D5FA8; color: #fff; border: 0; padding: 10px 14px; border-radius: 4px; }''',
    task={'q': 'Sesuaikan <code>.tombol</code> dengan spesifikasi: padding 16px 24px, border-radius 12px, min-height 48px.',
          'test': f"(s=>parseFloat(s.paddingTop)===16&&parseFloat(s.paddingLeft)===24&&parseFloat(s.borderTopLeftRadius)===12&&parseFloat(s.minHeight)>=48)({G.format('.tombol')})",
          'hint': '.tombol { padding: 16px 24px; border-radius: 12px; min-height: 48px }'},
    pts=['Dev Mode menampilkan ukuran otomatis.', 'Tulis yang tak terlihat: responsif, state, teks terpanjang, animasi, logika.', 'Spesifikasi memakai nama token.'],
    qs=[q('Informasi apa yang TIDAK muncul otomatis di Dev Mode dari satu frame statis?', ['Ukuran huruf', 'Perilaku saat teks sangat panjang', 'Warna latar'], 1, 'Perilaku harus ditulis desainer.'),
        q('Spesifikasi yang baik menulis warna sebagai?', ['#1D5FA8', 'color-action-primary', 'biru'], 1, 'Nama token yang sama dipakai di kode.')],
    cek={'css': '.tombol{padding:16px 24px;border-radius:12px;min-height:48px}'}),
  C('Sesi handoff kolaboratif',
    ['<b>Handoff</b> bukan melempar file Figma lalu pergi. Handoff yang baik adalah <b>percakapan</b> yang dimulai sejak awal: developer ikut melihat wireframe untuk memberi tahu batasan teknis, dan desainer tetap terlibat sampai fitur dirilis.',
     'Format sesi handoff (30 sampai 60 menit): (1) desainer menjelaskan <b>masalah pengguna</b> dan tujuan fitur, bukan hanya gambarnya; (2) <b>walkthrough alur</b> dari awal sampai akhir, termasuk jalur error dan empty state; (3) membahas <b>komponen</b>: mana yang sudah ada di design system, mana yang baru; (4) membahas <b>kasus tepi</b> dan perilaku responsif; (5) menyepakati <b>acceptance criteria</b> yang bisa diuji.',
     'Siapkan file Figma yang rapi sebelum sesi: halaman terpisah untuk "Siap dikembangkan" (Ready for dev), nama frame jelas, komponen dari library, anotasi untuk perilaku, dan prototype untuk alur. Tandai frame dengan status <b>Ready for dev</b> di Dev Mode agar developer tahu mana yang final.',
     'Setelah dibangun, lakukan <b>design QA</b>: desainer membandingkan hasil build di perangkat nyata dengan desain, mencatat selisih sebagai tiket dengan tangkapan layar, lalu memprioritaskannya bersama tim. Selisih 1 px tidak sama pentingnya dengan state error yang hilang.'],
    tb=[{'c': 'Daftar periksa handoff', 'h': ['Bagian', 'Yang disiapkan'], 'r': [
      ['Konteks', 'Masalah pengguna, tujuan, metrik keberhasilan'], ['Alur', 'Prototype dari awal sampai akhir, termasuk error dan batal'],
      ['Layar', 'Semua state: default, loading, empty, error, sukses, data panjang'], ['Responsif', 'Ponsel, tablet, desktop, atau aturan melar'],
      ['Komponen', 'Dari library; komponen baru ditandai dan didokumentasikan'], ['Token', 'Warna, tipografi, spacing memakai nama token'],
      ['Konten', 'Teks final, pesan error, teks terpanjang'], ['Aset', 'Ikon SVG, gambar @1x @2x @3x, nama file konsisten'],
      ['Aksesibilitas', 'Urutan fokus, label pembaca layar, kontras'], ['Acceptance criteria', 'Kondisi yang bisa diuji untuk setiap perilaku']]},
        {'c': 'Contoh acceptance criteria', 'h': ['Kondisi', 'Hasil yang diharapkan'], 'r': [
      ['Email kosong lalu tekan Daftar', 'Pesan "Email wajib diisi" di bawah field, fokus pindah ke field email'],
      ['Email tanpa @', 'Pesan "Format email belum benar, contoh: nama@contoh.com"'],
      ['Tombol Daftar ditekan', 'Tombol menampilkan loading dan tidak bisa ditekan dua kali'],
      ['Server gagal', 'Banner error dengan tombol Coba lagi, isian tidak hilang']]}],
    pts=['Handoff adalah percakapan sejak awal, bukan melempar file.', 'Sesi: konteks, alur, komponen, kasus tepi, acceptance criteria.', 'Design QA di perangkat nyata setelah dibangun.'],
    qs=[q('Kapan developer sebaiknya mulai dilibatkan?', ['Setelah desain final', 'Sejak wireframe', 'Setelah rilis'], 1, 'Batasan teknis diketahui lebih awal.'),
        q('Apa itu design QA?', ['Menguji kode dengan unit test', 'Membandingkan hasil build dengan desain di perangkat nyata', 'Membuat ulang desain'], 1, 'Selisih dicatat dan diprioritaskan.'),
        q('Acceptance criteria yang baik bersifat?', ['Bisa diuji', 'Umum seperti "harus bagus"', 'Hanya untuk desainer'], 0, 'Setiap kondisi punya hasil yang jelas.')]),
]),
]

UI_SO = {
'Hierarki visual': [
  T('Lakukan squint test pada halaman beranda aplikasi bank atau e-commerce di ponselmu. Tulis tiga elemen yang paling menonjol, lalu nilai: apakah itu memang yang terpenting?', 'Sipitkan mata atau buramkan tangkapan layar. Bandingkan dengan tujuan utama halaman.',
    'Contoh jawaban (aplikasi e-commerce):\n1. Banner promo besar  → menonjol, tapi bukan tujuan utama pengguna\n2. Kolom pencarian      → seharusnya paling menonjol\n3. Ikon keranjang       → cukup\nRekomendasi: perbesar kolom pencarian, kecilkan banner.'),
  X('Tulis CSS untuk kartu notifikasi dengan hierarki: judul 18px tebal 700, isi 14px abu-abu tua, waktu 12px abu-abu.', 'Bedakan dengan ukuran, tebal, dan warna sekaligus.',
    '.notif-judul { font-size: 18px; font-weight: 700; color: #111827; }\n.notif-isi   { font-size: 14px; color: #374151; }\n.notif-waktu { font-size: 12px; color: #6B7280; }'),
],
'Prinsip Gestalt': [
  T('Sebutkan prinsip Gestalt yang dipakai pada: (a) kartu produk berbingkai, (b) semua tautan berwarna sama, (c) ikon lingkaran putus-putus yang tetap terbaca sebagai lingkaran.', 'Common region, similarity, closure.',
    '(a) Common region\n(b) Similarity\n(c) Closure'),
  X('Tulis CSS jarak untuk daftar pengaturan: jarak judul grup ke item pertama 8px, antar item 4px, antar grup 32px.', 'Jarak di dalam kelompok lebih kecil dari jarak antar kelompok.',
    '.grup { margin-bottom: 32px; }\n.grup h3 { margin: 0 0 8px; }\n.grup .item + .item { margin-top: 4px; }'),
],
'Grid 8 poin': [
  T('Rapikan nilai berikut ke grid 8 (atau 4 untuk detail): 13, 18, 22, 30, 45, 6.', 'Bulatkan ke kelipatan 8 terdekat; nilai kecil boleh 4.',
    '13 → 12 atau 16\n18 → 16\n22 → 24\n30 → 32\n45 → 48\n6  → 4 atau 8'),
  X('Buat token spacing skala 8 dari 4 sampai 64 sebagai CSS variables.', 'Satu variabel per langkah.',
    ':root {\n  --space-0-5: 4px;\n  --space-1: 8px;\n  --space-2: 16px;\n  --space-3: 24px;\n  --space-4: 32px;\n  --space-5: 40px;\n  --space-6: 48px;\n  --space-8: 64px;\n}'),
],
'Perataan dan keseimbangan': [
  T('Halaman login: logo, judul, dua input, tombol, dan link "Lupa sandi". Usulkan perataan dan keseimbangannya, beri alasan.', 'Login sederhana cocok simetris; input dan tombol sejajar satu kolom.',
    'Keseimbangan simetris: satu kolom di tengah, lebar maks 400px.\nLogo dan judul rata tengah (teks pendek).\nLabel, input, tombol rata kiri dalam kolom yang sama, lebar penuh.\nLink "Lupa sandi" rata kanan di bawah field sandi, sejajar tepi kanan input.'),
],
'Jarak untuk kepadatan dan keterbacaan': [
  X('Buat dua mode kepadatan tabel dengan atribut data: comfortable (padding sel 16px) dan compact (padding sel 8px).', 'Pakai selector atribut pada tabel.',
    'table[data-density="comfortable"] td { padding: 16px; }\ntable[data-density="compact"] td { padding: 8px 12px; }'),
],
'Memilih typeface': [
  T('Pilih pasangan font untuk aplikasi belajar anak SD dan untuk aplikasi laporan keuangan perusahaan. Jelaskan alasannya.', 'Pertimbangkan kepribadian, keterbacaan angka, dan x-height.',
    'Aplikasi anak: Nunito atau Baloo 2 (bulat, ramah, x-height besar) + font sistem untuk teks panjang.\nLaporan keuangan: Inter atau IBM Plex Sans (netral, angka tabular sejajar) + IBM Plex Mono untuk kode akun.'),
  H('Tulis tag link Google Fonts untuk Plus Jakarta Sans ketebalan 400, 600, 700 dan CSS pemakaiannya dengan fallback.', 'Pakai display=swap dan tumpukan fallback sistem.',
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">\n\n<style>\n  body { font-family: "Plus Jakarta Sans", system-ui, sans-serif; }\n</style>'),
],
'Skala tipe modular': [
  T('Hitung skala tipe dasar 16 dengan rasio 1,2 untuk 4 tingkat ke atas, lalu bulatkan ke bilangan bulat.', '16 × 1,2 berulang.',
    '16\n16 × 1,2 = 19,2  → 19 (atau 20)\n19,2 × 1,2 = 23,04 → 23 (atau 24)\n23,04 × 1,2 = 27,65 → 28\n27,65 × 1,2 = 33,18 → 33 (atau 32)'),
],
'Line height, tracking, dan panjang baris': [
  X('Tulis CSS untuk: overline 12px kapital tracking 0.08em, judul 32px line-height 1.2 tracking -0.01em, paragraf 17px line-height 1.6 max 65ch.', 'Tiga aturan terpisah.',
    '.overline { font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; }\nh1 { font-size: 32px; line-height: 1.2; letter-spacing: -0.01em; }\np { font-size: 17px; line-height: 1.6; max-width: 65ch; }'),
],
'Peran tipografi semantik': [
  X('Buat token peran tipografi headline-small, title-medium, body-large, dan label-large sebagai CSS variables shorthand <code>font</code>.', 'Shorthand font: tebal ukuran/line-height keluarga.',
    ':root {\n  --font-family: system-ui, sans-serif;\n  --headline-small: 400 24px/32px var(--font-family);\n  --title-medium: 500 16px/24px var(--font-family);\n  --body-large: 400 16px/24px var(--font-family);\n  --label-large: 500 14px/20px var(--font-family);\n}\nh2 { font: var(--headline-small); }'),
],
'Tipografi responsif': [
  X('Buat judul fluid dari 24px (layar 360px) sampai 40px, dan subjudul dari 18px sampai 24px.', 'clamp(min, rem + vw, max).',
    'h1 { font-size: clamp(1.5rem, 1rem + 2.5vw, 2.5rem); }\nh2 { font-size: clamp(1.125rem, 1rem + 1vw, 1.5rem); }'),
],
'Properti warna dan model warna layar': [
  T('Ubah warna hsl(210 70% 40%) menjadi versi lebih terang untuk latar, versi lebih gelap untuk teks, dan versi abu-abu.', 'Ubah lightness untuk terang-gelap, saturation untuk abu-abu.',
    'Latar terang : hsl(210 70% 94%)\nTeks gelap   : hsl(210 70% 22%)\nAbu-abu      : hsl(210 8% 40%)'),
],
'Kontras WCAG': [
  T('Nilai pasangan ini terhadap WCAG AA: (a) teks #FFFFFF di atas #1D5FA8, (b) teks #9CA3AF di atas #FFFFFF, (c) border input #D1D5DB di atas #FFFFFF.', 'Teks normal 4,5:1, komponen UI 3:1.',
    '(a) sekitar 6,4:1 → lulus AA untuk teks\n(b) sekitar 2,5:1 → gagal (butuh 4,5:1)\n(c) sekitar 1,5:1 → gagal untuk komponen UI (butuh 3:1); pakai #6B7280 atau lebih gelap'),
  X('Tulis gaya placeholder yang tetap lulus kontras 4,5:1 di atas putih.', 'Gelapkan abu-abunya.',
    'input::placeholder { color: #6B7280; opacity: 1; }'),
],
'Palet tint dan shade': [
  X('Buat skala 100 sampai 900 (5 tingkat) untuk hue 352 (merah merek) memakai hsl.', 'Hue tetap, lightness turun.',
    ':root {\n  --red-100: hsl(352 85% 94%);\n  --red-300: hsl(352 75% 76%);\n  --red-500: hsl(352 70% 50%);\n  --red-700: hsl(352 75% 34%);\n  --red-900: hsl(352 80% 18%);\n}'),
],
'Warna semantik untuk state': [
  H('Tulis markup field error yang tidak bergantung pada warna saja: label, input dengan aria-invalid, ikon, dan pesan yang terhubung.', 'aria-invalid dan aria-describedby.',
    '<label for="hp">Nomor HP</label>\n<input id="hp" type="tel" aria-invalid="true" aria-describedby="hp-err">\n<p id="hp-err" class="error"><span aria-hidden="true">⚠</span> Nomor HP minimal 10 digit, contoh: 081234567890</p>'),
],
'Dark mode': [
  X('Tulis token warna untuk tema terang dan gelap yang mengikuti pengaturan sistem, dengan penimpa manual lewat data-theme.', 'Bare :root, media query dengan :not, dan [data-theme].',
    ':root { --bg: #FFFFFF; --fg: #111827; --surface: #F3F4F6; }\n@media (prefers-color-scheme: dark) {\n  :root:not([data-theme="light"]) { --bg: #121417; --fg: #E6E8EB; --surface: #1E2227; }\n}\n:root[data-theme="dark"] { --bg: #121417; --fg: #E6E8EB; --surface: #1E2227; }\nbody { background: var(--bg); color: var(--fg); }'),
],
'Anatomi input form': [
  H('Buat field kata sandi lengkap: label, input, helper "Minimal 8 karakter", dan tombol tampilkan sandi dengan aria-label.', 'Helper dihubungkan dengan aria-describedby.',
    '<label for="sandi">Kata sandi</label>\n<div class="sandi">\n  <input id="sandi" type="password" aria-describedby="sandi-help" autocomplete="new-password">\n  <button type="button" aria-label="Tampilkan kata sandi">👁</button>\n</div>\n<p id="sandi-help">Minimal 8 karakter.</p>'),
],
'State dan hierarki tombol': [
  X('Tulis state loading untuk tombol: teks disembunyikan, muncul spinner, dan tombol tidak bisa diklik.', 'Pakai atribut aria-busy dan pointer-events.',
    '.btn[aria-busy="true"] { color: transparent; pointer-events: none; position: relative; }\n.btn[aria-busy="true"]::after {\n  content: ""; position: absolute; inset: 0; margin: auto; width: 18px; height: 18px;\n  border: 2px solid #fff; border-right-color: transparent; border-radius: 50%;\n  animation: putar .7s linear infinite;\n}\n@keyframes putar { to { transform: rotate(360deg); } }'),
],
'Kartu': [
  X('Buat grid kartu 1 sampai 4 kolom otomatis dengan gambar 4:3 yang tidak gepeng.', 'auto-fill minmax dan object-fit.',
    '.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px; }\n.kartu img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; display: block; }'),
],
'Modal, sheet, dan popover': [
  H('Tulis modal konfirmasi hapus memakai elemen dialog, dengan tombol Batal dan Hapus.', 'dialog + form method="dialog" menutup otomatis.',
    '<button onclick="konfirmasi.showModal()">Hapus kelas</button>\n<dialog id="konfirmasi" aria-labelledby="judul-hapus">\n  <h2 id="judul-hapus">Hapus kelas ini?</h2>\n  <p>Progres belajar di kelas ini akan hilang.</p>\n  <form method="dialog">\n    <button value="batal">Batal</button>\n    <button value="hapus" class="danger">Hapus</button>\n  </form>\n</dialog>'),
],
'Auto layout dan batasan tata letak dinamis': [
  T('Terjemahkan pengaturan Figma ini ke CSS: frame auto layout horizontal, gap 12, padding 16 24, align center; anak 1 Fixed 40×40, anak 2 Fill, anak 3 Hug.', 'flex, gap, padding, align-items, flex: none / 1.',
    '.baris { display: flex; align-items: center; gap: 12px; padding: 16px 24px; }\n.anak1 { width: 40px; height: 40px; flex: none; }\n.anak2 { flex: 1; min-width: 0; }\n.anak3 { flex: none; }'),
],
'Fondasi design token': [
  T('Tulis token tombol dalam format JSON DTCG: warna latar, warna teks, dan radius.', 'Setiap token punya $value dan $type.',
    '{\n  "button": {\n    "bg":     { "$type": "color",     "$value": "{color.action.primary}" },\n    "text":   { "$type": "color",     "$value": "{color.white}" },\n    "radius": { "$type": "dimension", "$value": "10px" }\n  }\n}'),
],
'Penamaan token global dan alias': [
  T('Kelompokkan token ini ke global, alias, atau component: blue-600, color-text-muted, button-primary-bg, space-4, color-border-focus, card-radius.', 'Global = nilai mentah; alias = peran; component = khusus komponen.',
    'Global    : blue-600, space-4\nAlias     : color-text-muted, color-border-focus\nComponent : button-primary-bg, card-radius'),
],
'Varian dan properti komponen': [
  T('Rancang properti komponen Badge: ukuran, warna semantik, ikon. Hitung jumlah varian jika semua dibuat sebagai variant.', 'Kalikan jumlah nilai setiap properti; ikon sebaiknya boolean property.',
    'Size    : sm, md                     (2)\nTone    : neutral, success, warning, error, info (5)\nIcon    : boolean property (bukan variant)\nJumlah variant = 2 × 5 = 10 (ikon tidak menggandakan karena boolean)'),
],
'Set ikon dan aset': [
  T('Buat aturan penamaan file untuk 3 ikon dan 2 ilustrasi onboarding yang diekspor untuk Android dan iOS.', 'Pola: jenis_nama_ukuran, kepadatan @2x @3x.',
    'ic_home_24.svg\nic_search_24.svg\nic_cart_24.svg\nimg_onboarding_1.png, img_onboarding_1@2x.png, img_onboarding_1@3x.png\nimg_onboarding_2.png, img_onboarding_2@2x.png, img_onboarding_2@3x.png'),
],
'Dokumentasi pedoman pola': [
  T('Tulis kerangka dokumentasi komponen Toast (notifikasi singkat).', 'Deskripsi, kapan dipakai, anatomi, varian, Do/Don\'t, konten, aksesibilitas.',
    'Toast\nDeskripsi : pesan singkat tentang hasil aksi, hilang sendiri.\nKapan     : konfirmasi ringan (Tersimpan, Disalin).\nJangan    : untuk error penting atau yang butuh keputusan (pakai dialog/banner).\nAnatomi   : 1 ikon, 2 pesan, 3 aksi opsional (Urungkan).\nVarian    : neutral, success, error.\nDo        : maksimal 1 baris, kata kerja lampau ("Kelas disimpan").\nDon\'t     : dua toast bertumpuk.\nAksesibilitas: role="status", tampil minimal 4 detik, bisa ditutup.'),
],
'Breakpoint fluid dan aturan container': [
  X('Buat komponen kartu yang berubah menjadi horizontal saat induknya minimal 480px, memakai container query.', 'container-type: inline-size, lalu @container.',
    '.wadah { container-type: inline-size; }\n.kartu { display: grid; gap: 12px; }\n@container (min-width: 480px) {\n  .kartu { grid-template-columns: 160px 1fr; }\n}'),
],
'Pola navigasi mobile': [
  T('Aplikasi punya 7 tujuan: Beranda, Kelas, Jadwal, Peringkat, Pesan, Profil, Pengaturan. Rancang navigasi mobile-nya.', 'Bottom nav maksimal 5; sisanya ke Profil atau menu lain.',
    'Bottom nav (4): Beranda, Kelas, Jadwal, Profil\nPesan: ikon di top app bar (dengan badge)\nPeringkat: tab di halaman Kelas\nPengaturan: di dalam halaman Profil'),
],
'Layout dashboard desktop': [
  X('Ubah dashboard menjadi satu kolom di bawah 840px: sidebar disembunyikan, header di atas main.', 'Media query yang mengubah grid-template-areas.',
    '@media (max-width: 839px) {\n  .dash { grid-template-columns: 1fr; grid-template-areas: "header" "main"; }\n  .side { display: none; }\n}'),
],
'Redlining dan spesifikasi': [
  T('Tulis spesifikasi lengkap untuk komponen input pencarian (bukan hanya ukuran).', 'Ukuran, token, state, perilaku, teks panjang, aksesibilitas.',
    'Tinggi 48, padding space-2, radius-full, ikon 20 kiri\nToken: color-bg-surface, color-border-input, color-text-muted (placeholder)\nState: default, focus (border 2px color-border-focus), filled (tampil tombol hapus), disabled\nPerilaku: cari setelah berhenti mengetik 300 ms; Enter langsung cari; Esc mengosongkan\nTeks panjang: terpotong dengan elipsis, tidak melebarkan input\nAksesibilitas: role="search", label tersembunyi "Cari kelas", tombol hapus aria-label="Hapus pencarian"'),
],
'Sesi handoff kolaboratif': [
  T('Tulis 4 acceptance criteria untuk fitur "Lupa kata sandi".', 'Format: kondisi → hasil yang diharapkan, termasuk jalur gagal.',
    '1. Email terdaftar dikirim → muncul pesan "Cek email untuk tautan reset" dan tombol kirim ulang aktif setelah 60 detik.\n2. Email tidak terdaftar → pesan yang sama (tidak membocorkan apakah email terdaftar).\n3. Format email salah → pesan di bawah field, fokus kembali ke field.\n4. Tautan reset kedaluwarsa (lebih dari 30 menit) → halaman "Tautan kedaluwarsa" dengan tombol minta tautan baru.'),
],
}
