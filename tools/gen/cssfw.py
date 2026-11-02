"""Isi jalur Tailwind CSS dan Bootstrap 5. Semua pelajaran jenis w dengan pratinjau langsung."""
from mobile_lib import W, C, M, q

# ======================================================================
# TAILWIND CSS
# ======================================================================
TW = [
M('Mengenal Tailwind CSS', 'Pemula',
  'Apa itu utility-first, cara memasang Tailwind, dan kelas dasar untuk jarak, warna, dan huruf.',
  ['Utility-first', 'Installation', 'Spacing', 'Colors', 'Typography'], [
  W('Utility-first dan cara memasang',
    ['Tailwind CSS adalah framework <b>utility-first</b>: alih-alih menulis CSS sendiri, kamu menempelkan kelas kecil yang masing-masing melakukan satu hal, misalnya <code>p-4</code> (padding), <code>bg-sky-600</code> (warna latar), <code>rounded-lg</code> (sudut membulat).',
     'Untuk belajar dan mencoba cepat, cukup pasang <b>Play CDN</b>: <code>&lt;script src="https://cdn.tailwindcss.com"&gt;&lt;/script&gt;</code>. Pratinjau di halaman ini memakai cara itu (Tailwind 3.4). Untuk proyek sungguhan, pasang lewat npm agar CSS yang dihasilkan kecil dan hanya berisi kelas yang dipakai.',
     'Cara pasang Tailwind v4 di proyek Vite: <code>npm install tailwindcss @tailwindcss/vite</code>, tambahkan plugin <code>tailwindcss()</code> di <code>vite.config.js</code>, lalu tulis <code>@import "tailwindcss";</code> di file CSS utama. Di v3 kamu memakai <code>tailwind.config.js</code> dan tiga baris <code>@tailwind base; @tailwind components; @tailwind utilities;</code>.',
     'Kelas di Tailwind v3 dan v4 hampir sama, jadi yang kamu pelajari di sini berlaku di keduanya.'],
    html='''<div class="max-w-sm mx-auto mt-6 p-6 bg-white rounded-xl shadow-md">
  <h1 class="text-2xl font-bold text-slate-800">Toko Nusantara</h1>
  <p class="mt-2 text-slate-600">Kopi, teh, dan camilan pilihan.</p>
  <button class="mt-4 px-4 py-2 bg-sky-600 text-white rounded-lg">Belanja sekarang</button>
</div>''',
    fw='tw',
    task={'q': 'Ubah tombol menjadi hijau: ganti <code>bg-sky-600</code> dengan <code>bg-emerald-600</code>.',
          'test': "document.querySelector('button').classList.contains('bg-emerald-600')",
          'hint': 'Cukup ganti nama kelasnya di atribut class pada tombol.'},
    pts=['Utility-first: satu kelas, satu tugas gaya.', 'Play CDN untuk mencoba; npm + Vite untuk proyek.', 'v4: @import "tailwindcss"; v3: tailwind.config.js + @tailwind.'],
    qs=[q('Apa arti utility-first?', ['Menyusun tampilan dari banyak kelas kecil yang masing-masing satu tugas', 'Menulis semua CSS di satu file besar', 'Memakai komponen siap pakai saja'], 0, 'Setiap kelas utilitas mengatur satu properti CSS.'),
        q('Baris apa yang dipakai Tailwind v4 di file CSS?', ['@import "tailwindcss";', '@tailwind all;', '@use tailwind;'], 0, 'v4 cukup satu baris import.')]),
  W('Jarak, ukuran, dan warna',
    ['Skala jarak Tailwind: angka 1 = 0.25rem (4px). Jadi <code>p-4</code> = padding 16px, <code>m-2</code> = margin 8px. Tambahkan arah: <code>px</code> (kiri-kanan), <code>py</code> (atas-bawah), <code>mt</code>, <code>mb</code>, <code>ml</code>, <code>mr</code>.',
     'Lebar dan tinggi: <code>w-64</code> (16rem), <code>w-full</code>, <code>w-1/2</code>, <code>h-12</code>, <code>max-w-md</code>.',
     'Warna mengikuti pola <code>{properti}-{warna}-{tingkat}</code>: <code>bg-rose-500</code>, <code>text-slate-700</code>, <code>border-amber-300</code>. Tingkat 50 paling terang sampai 950 paling gelap. Tambah transparansi dengan garis miring: <code>bg-sky-600/20</code>.',
     'Kalau butuh nilai khusus, pakai kurung siku (arbitrary value): <code>w-[310px]</code>, <code>bg-[#B4532A]</code>.'],
    html='''<div class="p-6 space-y-3">
  <div class="p-2 bg-amber-100 text-amber-900 rounded">p-2</div>
  <div class="p-4 bg-amber-200 text-amber-900 rounded">p-4</div>
  <div class="p-8 bg-amber-300 text-amber-900 rounded">p-8</div>
  <div class="w-1/2 py-2 px-4 bg-[#B4532A] text-white rounded">w-1/2 dengan warna khusus</div>
</div>''',
    fw='tw',
    task={'q': 'Beri kotak pertama padding <code>p-6</code> dan latar <code>bg-rose-200</code>.',
          'test': "(e=>e.classList.contains('p-6')&&e.classList.contains('bg-rose-200'))(document.querySelector('.space-y-3 > div'))",
          'hint': 'Ganti p-2 menjadi p-6 dan bg-amber-100 menjadi bg-rose-200 di div pertama.'},
    pts=['1 unit = 0.25rem = 4px.', 'Pola warna: bg-/text-/border- + nama + tingkat 50–950.', 'Nilai khusus memakai [ ], misalnya w-[310px].'],
    qs=[q('Berapa padding dari kelas p-4?', ['16px (1rem)', '4px', '40px'], 0, '4 × 0.25rem = 1rem = 16px.'),
        q('Kelas mana yang memberi warna teks abu-abu gelap?', ['text-slate-700', 'bg-slate-700', 'font-slate-700'], 0, 'Awalan text- mengatur warna teks.')]),
  W('Tipografi',
    ['Ukuran huruf: <code>text-xs</code>, <code>text-sm</code>, <code>text-base</code>, <code>text-lg</code>, <code>text-xl</code> sampai <code>text-9xl</code>.',
     'Tebal huruf: <code>font-normal</code>, <code>font-medium</code>, <code>font-semibold</code>, <code>font-bold</code>. Keluarga huruf: <code>font-sans</code>, <code>font-serif</code>, <code>font-mono</code>.',
     'Lainnya: <code>leading-relaxed</code> (jarak baris), <code>tracking-wide</code> (jarak huruf), <code>uppercase</code>, <code>italic</code>, <code>underline</code>, <code>text-center</code>, <code>truncate</code> (potong dengan elipsis).'],
    html='''<article class="p-6 max-w-prose">
  <p class="text-xs uppercase tracking-widest text-slate-500">Resep</p>
  <h1 class="text-3xl font-serif text-slate-900">Kopi Tubruk</h1>
  <p class="mt-3 text-base text-slate-700">Seduh dua sendok kopi bubuk dengan air mendidih, aduk, lalu tunggu ampasnya turun.</p>
</article>''',
    fw='tw',
    task={'q': 'Jadikan paragraf terakhir lebih lega: tambahkan kelas <code>leading-relaxed</code>.',
          'test': "document.querySelector('article p:last-child').classList.contains('leading-relaxed')",
          'hint': 'Tambahkan leading-relaxed di atribut class paragraf terakhir.'},
    pts=['text-* untuk ukuran, font-* untuk tebal dan keluarga.', 'leading-* jarak baris, tracking-* jarak huruf.'],
    qs=[q('Kelas apa untuk huruf tebal?', ['font-bold', 'text-bold', 'bold'], 0, 'Ketebalan memakai awalan font-.')]),
]),
M('Tata letak dan responsif', 'Menengah',
  'Flexbox, grid, layar responsif, dan keadaan seperti hover, focus, serta mode gelap.',
  ['Flexbox', 'Grid', 'Responsive Design', 'Hover, Focus', 'Dark Mode'], [
  W('Flexbox dan Grid',
    ['<code>flex</code> menjadikan elemen wadah flexbox. Atur arah dengan <code>flex-row</code>/<code>flex-col</code>, perataan dengan <code>justify-between</code>, <code>justify-center</code>, <code>items-center</code>, dan jarak antaranak dengan <code>gap-4</code>.',
     '<code>grid</code> plus <code>grid-cols-3</code> membuat tiga kolom sama lebar. <code>col-span-2</code> membuat satu anak memakan dua kolom.',
     'Pola umum navbar: <code>flex items-center justify-between</code>. Pola galeri kartu: <code>grid grid-cols-2 gap-4</code>.'],
    html='''<nav class="flex items-center justify-between p-4 bg-slate-800 text-white">
  <b>Ruang</b>
  <div class="flex gap-4 text-sm"><a>Beranda</a><a>Kursus</a><a>Masuk</a></div>
</nav>
<section id="galeri" class="grid grid-cols-2 gap-4 p-4">
  <div class="p-4 bg-sky-100 rounded">Dart</div>
  <div class="p-4 bg-sky-100 rounded">Kotlin</div>
  <div class="p-4 bg-sky-100 rounded">Flutter</div>
  <div class="p-4 bg-sky-100 rounded">Compose</div>
</section>''',
    fw='tw',
    task={'q': 'Ubah galeri menjadi tiga kolom dengan <code>grid-cols-3</code>.',
          'test': "document.getElementById('galeri').classList.contains('grid-cols-3')",
          'hint': 'Ganti grid-cols-2 menjadi grid-cols-3 pada section#galeri.'},
    pts=['flex + justify-* + items-* + gap-*.', 'grid + grid-cols-N + col-span-N.'],
    qs=[q('Kelas mana yang menaruh anak flex di tengah secara vertikal?', ['items-center', 'justify-center', 'align-middle'], 0, 'items-* mengatur sumbu silang (vertikal pada flex-row).')]),
  W('Desain responsif',
    ['Tailwind <b>mobile-first</b>: kelas tanpa awalan berlaku di semua ukuran, kelas berawalan berlaku mulai lebar tertentu ke atas.',
     'Titik henti bawaan: <code>sm</code> 640px, <code>md</code> 768px, <code>lg</code> 1024px, <code>xl</code> 1280px, <code>2xl</code> 1536px.',
     'Contoh: <code>grid-cols-1 md:grid-cols-3</code> berarti satu kolom di ponsel dan tiga kolom mulai 768px. <code>hidden md:block</code> menyembunyikan elemen di layar kecil.',
     'Ubah lebar jendela pratinjau (atau buka di ponsel) untuk melihat perbedaannya.'],
    html='''<div id="kartu" class="grid grid-cols-1 gap-3 p-4">
  <div class="p-4 bg-emerald-100 rounded">Satu</div>
  <div class="p-4 bg-emerald-100 rounded">Dua</div>
  <div class="p-4 bg-emerald-100 rounded">Tiga</div>
</div>
<p class="px-4 text-sm text-slate-500"><span class="sm:hidden">Layar kecil</span><span class="hidden sm:inline">Layar sm ke atas</span></p>''',
    fw='tw',
    task={'q': 'Buat kartu tampil tiga kolom mulai layar <code>md</code>: tambahkan <code>md:grid-cols-3</code>.',
          'test': "document.getElementById('kartu').classList.contains('md:grid-cols-3')",
          'hint': 'Tambahkan md:grid-cols-3 di atribut class div#kartu.'},
    pts=['Mobile-first: kelas polos untuk ponsel, awalan untuk layar lebih besar.', 'sm 640, md 768, lg 1024, xl 1280, 2xl 1536.'],
    qs=[q('Kelas md:text-lg berlaku kapan?', ['Mulai lebar 768px ke atas', 'Hanya di bawah 768px', 'Hanya tepat 768px'], 0, 'Awalan berarti "mulai dari ukuran ini ke atas".')]),
  W('Hover, focus, dan mode gelap',
    ['Awalan keadaan (variant) menerapkan kelas hanya saat kondisi tertentu: <code>hover:bg-sky-700</code>, <code>focus:ring-2</code>, <code>active:scale-95</code>, <code>disabled:opacity-50</code>.',
     '<code>group</code> dan <code>group-hover:</code> mengubah anak saat induknya di-hover. <code>peer</code> dan <code>peer-checked:</code> mengubah elemen saudara.',
     'Mode gelap: <code>dark:bg-slate-900</code>. Secara bawaan mengikuti pengaturan sistem; di v3 kamu bisa memakai strategi kelas (<code>darkMode: \'class\'</code>) agar bisa diganti lewat tombol.',
     'Tambahkan <code>transition</code> dan <code>duration-200</code> agar perubahan terlihat halus.'],
    html='''<div class="p-6 space-y-4">
  <button id="beli" class="px-4 py-2 bg-sky-600 text-white rounded-lg transition duration-200">Arahkan kursor ke saya</button>
  <input class="block w-full border border-slate-300 rounded-lg px-3 py-2 outline-none focus:ring-2 focus:ring-sky-400" placeholder="Klik untuk fokus">
  <a class="group block p-4 border rounded-lg hover:border-sky-500">
    <b class="group-hover:text-sky-600">Kursus Flutter</b>
    <p class="text-sm text-slate-500">Arahkan kursor ke kartu ini.</p>
  </a>
</div>''',
    fw='tw',
    task={'q': 'Buat tombol menggelap saat di-hover dengan <code>hover:bg-sky-800</code>.',
          'test': "document.getElementById('beli').classList.contains('hover:bg-sky-800')",
          'hint': 'Tambahkan hover:bg-sky-800 pada tombol#beli.'},
    pts=['Variant: hover:, focus:, active:, disabled:, dark:.', 'group/group-hover: dan peer/peer-checked: untuk relasi elemen.'],
    qs=[q('Awalan mana untuk mode gelap?', ['dark:', 'night:', 'theme-dark:'], 0, 'Tailwind memakai variant dark:.')]),
]),
M('Komponen, kustomisasi, dan proyek', 'Menengah',
  'Form, menyatukan kelas dengan @apply, mengatur tema sendiri, dan membuat landing page.',
  ['Forms', '@apply', 'Theme', 'Configuration', 'Project'], [
  W('Form yang rapi',
    ['Form dibangun dari utilitas biasa: <code>block</code>, <code>w-full</code>, <code>border</code>, <code>rounded-lg</code>, <code>px-3 py-2</code>, dan <code>focus:ring</code>.',
     'Untuk keadaan tidak valid, pakai variant <code>invalid:border-rose-500</code>. Plugin resmi <code>@tailwindcss/forms</code> menyamakan gaya bawaan input di semua browser.',
     'Tetap pakai <code>&lt;label&gt;</code> yang terhubung ke input lewat <code>for</code>/<code>id</code> agar mudah diakses.'],
    html='''<form class="max-w-sm p-6 space-y-4">
  <div>
    <label for="email" class="block text-sm font-medium text-slate-700">Email</label>
    <input id="email" type="email" required class="mt-1 block w-full border border-slate-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-sky-400 outline-none">
  </div>
  <div>
    <label for="sandi" class="block text-sm font-medium text-slate-700">Kata sandi</label>
    <input id="sandi" type="password" class="mt-1 block w-full border border-slate-300 rounded-lg px-3 py-2">
  </div>
  <button class="w-full py-2 bg-sky-600 text-white rounded-lg">Masuk</button>
</form>''',
    fw='tw',
    task={'q': 'Samakan input kata sandi dengan input email: tambahkan <code>focus:ring-2</code> dan <code>focus:ring-sky-400</code>.',
          'test': "(e=>e.classList.contains('focus:ring-2')&&e.classList.contains('focus:ring-sky-400'))(document.getElementById('sandi'))",
          'hint': 'Salin kelas focus:ring-2 focus:ring-sky-400 dari input email ke input#sandi.'},
    pts=['Form = utilitas biasa + focus:ring.', 'invalid: untuk validasi visual; @tailwindcss/forms untuk gaya dasar input.'],
    qs=[q('Kenapa label tetap penting walau ada placeholder?', ['Pembaca layar dan klik label membutuhkannya', 'Supaya Tailwind bekerja', 'Tidak penting'], 0, 'Label adalah nama aksesibel input.')]),
  W('Komponen dan @apply',
    ['Kelas yang panjang dan berulang bisa disatukan. Cara yang disarankan: buat <b>komponen</b> di framework kamu (React, Vue, Blade) agar kelas ditulis sekali.',
     'Alternatifnya, <code>@apply</code> di file CSS: <code>.btn { @apply px-4 py-2 rounded-lg bg-sky-600 text-white; }</code>. Di Play CDN, tulis di dalam <code>&lt;style type="text/tailwindcss"&gt;</code>.',
     'Gunakan @apply secukupnya. Kalau semuanya dipindah ke CSS, kamu kehilangan manfaat utama Tailwind: gaya terlihat langsung di HTML.'],
    html='''<style type="text/tailwindcss">
  .btn { @apply px-4 py-2 rounded-lg font-medium text-white; }
  .btn-utama { @apply bg-sky-600 hover:bg-sky-700; }
</style>
<div class="p-6 flex gap-3">
  <button class="btn btn-utama">Simpan</button>
  <button class="btn btn-utama">Kirim</button>
  <button id="hapus" class="btn bg-slate-500">Hapus</button>
</div>''',
    fw='tw',
    task={'q': 'Tambahkan kelas komponen <code>.btn-bahaya</code> berisi <code>@apply bg-rose-600;</code>, lalu pakai di tombol Hapus menggantikan <code>bg-slate-500</code>.',
          'test': "document.getElementById('hapus').classList.contains('btn-bahaya')&&/btn-bahaya/.test(document.querySelector('style[type=\"text/tailwindcss\"]').textContent)",
          'hint': 'Tulis .btn-bahaya { @apply bg-rose-600; } di dalam style, lalu ganti bg-slate-500 dengan btn-bahaya.'},
    pts=['Utamakan komponen di framework.', '@apply menyatukan utilitas menjadi satu kelas CSS.'],
    qs=[q('Di Play CDN, @apply ditulis di mana?', ['<style type="text/tailwindcss">', '<script>', 'Atribut class'], 0, 'Play CDN hanya memproses style dengan type text/tailwindcss.')]),
  W('Tema dan konfigurasi',
    ['Warna merek, font, dan jarak sendiri didaftarkan di tema. Di <b>v3</b> lewat <code>tailwind.config.js</code> bagian <code>theme.extend</code>. Di Play CDN, isi <code>tailwind.config = {...}</code> di skrip.',
     'Di <b>v4</b>, tema ditulis di CSS: <code>@theme { --color-merek: #B4532A; --font-judul: "Fraunces", serif; }</code>. Setelah itu kelas <code>bg-merek</code> dan <code>font-judul</code> langsung tersedia.',
     'Contoh di bawah mendaftarkan warna <code>merek</code> lewat skrip konfigurasi.'],
    html='''<script>
  tailwind.config = { theme: { extend: { colors: { merek: '#B4532A', krem: '#FBF3E4' } } } }
</script>
<div class="p-6 bg-krem">
  <h1 class="text-2xl font-bold text-merek">Kedai Kopi Senja</h1>
  <button id="pesan" class="mt-3 px-4 py-2 text-white rounded-lg bg-slate-700">Pesan</button>
</div>''',
    fw='tw',
    task={'q': 'Pakai warna tema: ganti <code>bg-slate-700</code> pada tombol dengan <code>bg-merek</code>.',
          'test': "document.getElementById('pesan').classList.contains('bg-merek')",
          'hint': 'Kelas bg-merek tersedia karena merek didaftarkan di theme.extend.colors.'},
    pts=['v3: theme.extend di tailwind.config.js.', 'v4: @theme { --color-*: ... } di CSS.'],
    qs=[q('Setelah --color-merek didaftarkan di @theme (v4), kelas apa yang muncul?', ['bg-merek, text-merek, border-merek, dll.', 'Hanya .merek', 'Tidak ada'], 0, 'Tailwind membuat semua utilitas warna dari token itu.')]),
  W('Proyek: landing page responsif',
    ['Saatnya menggabungkan semuanya: navbar flex, hero dengan tipografi besar, grid fitur yang responsif, dan tombol dengan hover.',
     'Perhatikan pola mobile-first: grid satu kolom di ponsel, tiga kolom mulai <code>md</code>.',
     'Tantangan: tambahkan satu kartu fitur keempat dan buat grid menjadi empat kolom di layar <code>lg</code>.'],
    html='''<header class="flex items-center justify-between px-6 py-4 border-b">
  <b class="text-lg">Ruang<span class="text-sky-600">Kode</span></b>
  <a class="px-3 py-1.5 text-sm bg-sky-600 hover:bg-sky-700 text-white rounded-lg">Daftar</a>
</header>
<main class="px-6 py-10 text-center">
  <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight">Belajar coding, langkah demi langkah</h1>
  <p class="mt-3 text-slate-600 max-w-xl mx-auto">Dari Dart sampai Kotlin, langsung praktik di browser.</p>
</main>
<section id="fitur" class="grid grid-cols-1 md:grid-cols-3 gap-4 px-6 pb-10">
  <div class="p-5 rounded-xl bg-slate-50 border"><b>Editor langsung</b><p class="text-sm text-slate-600">Tulis kode, lihat hasilnya.</p></div>
  <div class="p-5 rounded-xl bg-slate-50 border"><b>Kuis</b><p class="text-sm text-slate-600">Uji pemahaman tiap pelajaran.</p></div>
  <div class="p-5 rounded-xl bg-slate-50 border"><b>Peta belajar</b><p class="text-sm text-slate-600">Ikuti urutan yang jelas.</p></div>
</section>''',
    fw='tw',
    task={'q': 'Tambahkan kartu fitur keempat di <code>#fitur</code> dan beri grid kelas <code>lg:grid-cols-4</code>.',
          'test': "(g=>g.children.length>=4&&g.classList.contains('lg:grid-cols-4'))(document.getElementById('fitur'))",
          'hint': 'Salin satu div kartu, ubah isinya, lalu tambahkan lg:grid-cols-4 pada section#fitur.'},
    pts=['Gabungkan flex, grid, tipografi, dan variant.', 'Mulai dari ponsel, lalu tambah awalan md:/lg:.'],
    qs=[q('Urutan kelas mana yang benar untuk 1 kolom di ponsel dan 3 kolom di tablet?', ['grid-cols-1 md:grid-cols-3', 'md:grid-cols-1 grid-cols-3', 'grid-cols-3 sm:grid-cols-1'], 0, 'Kelas polos untuk layar kecil, awalan untuk layar besar.')]),
]),
]

# ======================================================================
# BOOTSTRAP 5
# ======================================================================
BS = [
M('Mengenal Bootstrap 5', 'Pemula',
  'Cara memasang Bootstrap, sistem grid 12 kolom, dan kelas utilitas.',
  ['Installation', 'Grid System', 'Utilities', 'Typography', 'Colors'], [
  W('Memasang Bootstrap 5',
    ['Bootstrap adalah framework CSS dengan <b>komponen siap pakai</b> (tombol, kartu, navbar, modal) dan sistem grid. Versi 5 tidak lagi membutuhkan jQuery.',
     'Cara cepat: tambahkan CSS di <code>&lt;head&gt;</code> dan bundle JS di akhir <code>&lt;body&gt;</code> dari CDN jsDelivr: <code>bootstrap@5.3.3/dist/css/bootstrap.min.css</code> dan <code>bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js</code>. Bundle sudah berisi Popper untuk dropdown dan tooltip.',
     'Lewat npm: <code>npm install bootstrap</code>, lalu <code>import "bootstrap/dist/css/bootstrap.min.css"</code> dan <code>import "bootstrap"</code> di file JS utama.',
     'Pratinjau di halaman ini sudah memuat Bootstrap 5.3, jadi kamu cukup menulis HTML.'],
    html='''<div class="container py-4">
  <h1 class="display-6">Toko Nusantara</h1>
  <p class="lead">Kopi, teh, dan camilan pilihan.</p>
  <button class="btn btn-primary">Belanja sekarang</button>
</div>''',
    fw='bs',
    task={'q': 'Ubah tombol menjadi hijau dengan mengganti <code>btn-primary</code> menjadi <code>btn-success</code>.',
          'test': "document.querySelector('.btn').classList.contains('btn-success')",
          'hint': 'Ganti nama kelas btn-primary menjadi btn-success.'},
    pts=['Bootstrap 5 = komponen + grid + utilitas, tanpa jQuery.', 'CSS di head, bootstrap.bundle.min.js di akhir body.'],
    qs=[q('Apa isi bootstrap.bundle.min.js selain JS Bootstrap?', ['Popper', 'jQuery', 'React'], 0, 'Popper dibutuhkan dropdown, tooltip, dan popover.'),
        q('Apakah Bootstrap 5 memerlukan jQuery?', ['Tidak', 'Ya', 'Hanya untuk grid'], 0, 'Sejak v5 Bootstrap memakai JavaScript biasa.')]),
  W('Sistem grid 12 kolom',
    ['Grid Bootstrap terdiri dari <code>.container</code> → <code>.row</code> → <code>.col</code>. Setiap baris dibagi 12 kolom.',
     '<code>col-4</code> mengambil 4 dari 12 kolom (sepertiga). Tambahkan titik henti: <code>col-12 col-md-6 col-lg-4</code> berarti penuh di ponsel, setengah mulai 768px, sepertiga mulai 992px.',
     'Titik henti Bootstrap: <code>sm</code> 576px, <code>md</code> 768px, <code>lg</code> 992px, <code>xl</code> 1200px, <code>xxl</code> 1400px. Jarak antarkolom diatur dengan <code>g-3</code> (gutter).'],
    html='''<div class="container py-3">
  <div class="row g-3">
    <div class="col-12 col-md-6"><div class="p-3 bg-info-subtle border rounded">Dart</div></div>
    <div class="col-12 col-md-6"><div class="p-3 bg-info-subtle border rounded">Kotlin</div></div>
    <div class="col-12 col-md-6"><div class="p-3 bg-info-subtle border rounded">Flutter</div></div>
    <div class="col-12 col-md-6"><div class="p-3 bg-info-subtle border rounded">Compose</div></div>
  </div>
</div>''',
    fw='bs',
    task={'q': 'Buat setiap kolom menjadi sepertiga lebar di layar besar: tambahkan <code>col-lg-4</code> pada keempat kolom.',
          'test': "[...document.querySelectorAll('.row > div')].every(d=>d.classList.contains('col-lg-4'))",
          'hint': 'Tambahkan col-lg-4 setelah col-md-6 di setiap div kolom.'},
    pts=['container → row → col.', '12 kolom per baris; col-md-6 = setengah mulai md.', 'Gutter: g-0 sampai g-5.'],
    qs=[q('Berapa lebar col-3 dalam baris 12 kolom?', ['Seperempat', 'Sepertiga', 'Setengah'], 0, '3/12 = 1/4.')]),
  W('Utilitas, tipografi, dan warna',
    ['Bootstrap juga punya kelas utilitas: jarak <code>m-3</code>, <code>p-2</code>, <code>mt-4</code>, <code>px-5</code> (skala 0–5), tampilan <code>d-flex</code>, <code>d-none d-md-block</code>, perataan <code>justify-content-between</code>, <code>align-items-center</code>, <code>text-center</code>.',
     'Warna tema: <code>primary</code>, <code>secondary</code>, <code>success</code>, <code>danger</code>, <code>warning</code>, <code>info</code>, <code>light</code>, <code>dark</code>. Dipakai sebagai <code>text-danger</code>, <code>bg-warning</code>, <code>border-success</code>.',
     'Tipografi: <code>display-1</code> sampai <code>display-6</code> untuk judul besar, <code>lead</code> untuk paragraf pembuka, <code>fw-bold</code>, <code>fs-5</code>, <code>text-muted</code>/<code>text-body-secondary</code>.'],
    html='''<div class="container py-3">
  <div class="d-flex justify-content-between align-items-center p-3 bg-light border rounded">
    <span class="fw-bold">Pesanan #1024</span>
    <span id="status" class="badge bg-secondary">Diproses</span>
  </div>
  <p class="mt-3 text-body-secondary">Estimasi tiba: 2 hari.</p>
</div>''',
    fw='bs',
    task={'q': 'Ubah status menjadi hijau dengan <code>bg-success</code> menggantikan <code>bg-secondary</code>.',
          'test': "document.getElementById('status').classList.contains('bg-success')",
          'hint': 'Ganti bg-secondary pada span#status.'},
    pts=['Jarak: m-/p- + arah + skala 0–5.', 'd-flex, justify-content-*, align-items-*.', 'Warna tema: primary, success, danger, warning, info, dll.'],
    qs=[q('Kelas mana yang menyembunyikan elemen di ponsel tapi menampilkannya mulai md?', ['d-none d-md-block', 'd-md-none d-block', 'hide-md'], 0, 'd-none untuk semua, lalu d-md-block mulai md.')]),
]),
M('Komponen Bootstrap', 'Menengah',
  'Tombol, kartu, alert, badge, navbar, form dengan validasi, dan modal.',
  ['Buttons', 'Cards', 'Alerts', 'Navbar', 'Forms', 'Validation', 'Modal'], [
  W('Tombol, kartu, alert, dan badge',
    ['Tombol: <code>btn btn-primary</code>, versi garis tepi <code>btn-outline-primary</code>, ukuran <code>btn-sm</code>/<code>btn-lg</code>.',
     'Kartu: <code>.card</code> berisi <code>.card-img-top</code>, <code>.card-body</code>, <code>.card-title</code>, <code>.card-text</code>.',
     'Alert untuk pesan: <code>alert alert-warning</code>. Badge untuk label kecil: <code>badge text-bg-danger</code>.'],
    html='''<div class="container py-3">
  <div class="alert alert-warning">Stok kopi Gayo tinggal sedikit.</div>
  <div class="card" style="max-width:18rem">
    <div class="card-body">
      <h5 class="card-title">Kopi Gayo <span class="badge text-bg-danger">Baru</span></h5>
      <p class="card-text">Arabika dari Aceh, 250 gram.</p>
      <a class="btn btn-primary">Rp 85.000</a>
    </div>
  </div>
</div>''',
    fw='bs',
    task={'q': 'Tambahkan tombol kedua di dalam kartu dengan kelas <code>btn btn-outline-secondary</code>.',
          'test': "!!document.querySelector('.card .btn.btn-outline-secondary')",
          'hint': 'Tulis <a class="btn btn-outline-secondary">Detail</a> setelah tombol pertama.'},
    pts=['btn + btn-{warna} atau btn-outline-{warna}.', 'card → card-body → card-title/card-text.', 'alert alert-{warna}; badge text-bg-{warna}.'],
    qs=[q('Kelas apa untuk tombol bergaris tepi merah?', ['btn btn-outline-danger', 'btn btn-danger-outline', 'btn-border-red'], 0, 'Pola btn-outline-{warna}.')]),
  W('Navbar yang bisa dilipat',
    ['Navbar Bootstrap otomatis berubah menjadi menu hamburger di layar kecil. Kuncinya: <code>navbar-expand-lg</code> (melebar mulai lg), tombol <code>navbar-toggler</code>, dan wadah <code>collapse navbar-collapse</code>.',
     'Tombol pembuka memakai atribut <code>data-bs-toggle="collapse"</code> dan <code>data-bs-target="#menu"</code>. Tidak perlu menulis JavaScript sendiri, bundle Bootstrap yang menanganinya.',
     'Pratinjau ini sempit, jadi kamu akan melihat tombol hamburger. Klik untuk membuka menu.'],
    html='''<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">RuangKode</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu" aria-controls="menu" aria-expanded="false" aria-label="Buka menu">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link active" href="#">Beranda</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Kursus</a></li>
      </ul>
    </div>
  </div>
</nav>''',
    fw='bs',
    task={'q': 'Tambahkan item menu ketiga "Masuk" di dalam <code>.navbar-nav</code>.',
          'test': "document.querySelectorAll('.navbar-nav .nav-item').length>=3",
          'hint': 'Salin satu <li class="nav-item">...</li> dan ganti teksnya.'},
    pts=['navbar-expand-{bp} menentukan kapan menu melebar.', 'data-bs-toggle="collapse" + data-bs-target="#id".'],
    qs=[q('Atribut apa yang menghubungkan tombol ke menu yang dilipat?', ['data-bs-target', 'data-target-menu', 'href saja'], 0, 'data-bs-target berisi selector elemen collapse.')]),
  W('Form dan validasi',
    ['Input memakai <code>form-control</code>, pilihan <code>form-select</code>, kotak centang <code>form-check-input</code>, label <code>form-label</code>.',
     'Validasi bawaan: beri form atribut <code>novalidate</code> dan kelas <code>needs-validation</code>. Saat dikirim, tambahkan kelas <code>was-validated</code> agar Bootstrap menampilkan <code>.invalid-feedback</code> di bawah input yang salah.',
     'Kamu juga bisa menandai satu input secara manual dengan <code>is-invalid</code> atau <code>is-valid</code>.'],
    html='''<form id="daftar" class="container py-3 needs-validation" novalidate>
  <div class="mb-3">
    <label for="nama" class="form-label">Nama</label>
    <input id="nama" class="form-control" required>
    <div class="invalid-feedback">Nama wajib diisi.</div>
  </div>
  <div class="mb-3">
    <label for="kelas" class="form-label">Kelas</label>
    <select id="kelas" class="form-select"><option>Flutter</option><option>Compose</option></select>
  </div>
  <button class="btn btn-primary">Daftar</button>
</form>''',
    js='''const f = document.getElementById('daftar');
f.addEventListener('submit', e => {
  e.preventDefault();
  // tandai form agar Bootstrap menampilkan pesan validasi
  f.classList.add('was-validated');
  if (f.checkValidity()) console.log('Terkirim:', f.nama.value);
});''',
    fw='bs',
    task={'q': 'Tambahkan input email (<code>type="email"</code>, kelas <code>form-control</code>, <code>required</code>) beserta pesan <code>invalid-feedback</code>.',
          'test': "(e=>!!e&&e.required&&e.classList.contains('form-control')&&!!e.parentElement.querySelector('.invalid-feedback'))(document.querySelector('#daftar input[type=email]'))",
          'hint': 'Salin blok div.mb-3 untuk Nama, ganti id, label, dan type menjadi email.'},
    pts=['form-control, form-select, form-check-input, form-label.', 'novalidate + was-validated menampilkan invalid-feedback.'],
    qs=[q('Kelas apa yang membuat Bootstrap menampilkan pesan validasi untuk seluruh form?', ['was-validated', 'is-validated', 'validate-all'], 0, 'was-validated dipasang pada form.')]),
  W('Modal dan komponen JavaScript',
    ['Modal adalah kotak dialog. Strukturnya <code>.modal</code> → <code>.modal-dialog</code> → <code>.modal-content</code> → header, body, footer.',
     'Membukanya cukup dengan tombol berisi <code>data-bs-toggle="modal"</code> dan <code>data-bs-target="#idModal"</code>. Tombol tutup memakai <code>data-bs-dismiss="modal"</code>.',
     'Komponen lain yang memakai pola sama: dropdown (<code>data-bs-toggle="dropdown"</code>), tooltip, offcanvas, accordion, dan toast. Bisa juga dibuka lewat JS: <code>new bootstrap.Modal(el).show()</code>.'],
    html='''<div class="container py-3">
  <button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#konfirmasi">Hapus akun</button>
</div>
<div class="modal fade" id="konfirmasi" tabindex="-1" aria-labelledby="judulModal" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header"><h5 class="modal-title" id="judulModal">Yakin?</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div>
      <div class="modal-body">Akun yang dihapus tidak bisa dipulihkan.</div>
      <div class="modal-footer">
        <button class="btn btn-danger">Ya, hapus</button>
      </div>
    </div>
  </div>
</div>''',
    fw='bs',
    task={'q': 'Tambahkan tombol "Batal" di footer modal yang menutup modal (<code>data-bs-dismiss="modal"</code>).',
          'test': "!!document.querySelector('.modal-footer [data-bs-dismiss=\"modal\"]')",
          'hint': 'Tulis <button class="btn btn-secondary" data-bs-dismiss="modal">Batal</button> di .modal-footer.'},
    pts=['data-bs-toggle="modal" + data-bs-target membuka modal.', 'data-bs-dismiss="modal" menutupnya.', 'Bisa juga lewat new bootstrap.Modal(el).'],
    qs=[q('Atribut apa untuk tombol yang menutup modal?', ['data-bs-dismiss="modal"', 'data-bs-close', 'onclick="close()"'], 0, 'data-bs-dismiss menutup komponen induknya.')]),
]),
M('Kustomisasi dan proyek', 'Menengah',
  'Mengubah tema lewat variabel CSS dan Sass, mode gelap, lalu membuat halaman lengkap.',
  ['CSS Variables', 'Sass', 'Color Modes', 'Project'], [
  W('Variabel CSS, Sass, dan mode gelap',
    ['Bootstrap 5.3 menyimpan warna dan ukuran di <b>variabel CSS</b> berawalan <code>--bs-</code>. Kamu bisa menimpanya: <code>:root { --bs-primary: #B4532A; --bs-primary-rgb: 180,83,42; }</code>. Untuk tombol, ubah variabel komponennya, misalnya <code>.btn-primary { --bs-btn-bg: #B4532A; }</code>.',
     'Untuk kustomisasi menyeluruh, pakai <b>Sass</b>: <code>npm install bootstrap sass</code>, lalu di <code>main.scss</code> tulis <code>$primary: #B4532A;</code> sebelum <code>@import "bootstrap/scss/bootstrap";</code>. Semua komponen ikut berubah.',
     'Mode gelap: tambahkan <code>data-bs-theme="dark"</code> pada <code>&lt;html&gt;</code> atau pada satu elemen saja.'],
    html='''<div class="container py-3">
  <button id="utama" class="btn btn-primary">Tombol utama</button>
  <div id="kotak" class="card mt-3"><div class="card-body">Kartu ini bisa dibuat gelap.</div></div>
</div>''',
    css='''.btn-primary {
  --bs-btn-bg: #B4532A;
  --bs-btn-border-color: #B4532A;
  --bs-btn-hover-bg: #8F3F1F;
}''',
    fw='bs',
    task={'q': 'Buat kartu tampil gelap dengan menambahkan atribut <code>data-bs-theme="dark"</code> pada <code>#kotak</code>.',
          'test': "document.getElementById('kotak').getAttribute('data-bs-theme')==='dark'",
          'hint': 'Tulis data-bs-theme="dark" di tag div#kotak.'},
    pts=['Variabel --bs-* bisa ditimpa di CSS.', 'Sass: ubah $primary dll. sebelum import Bootstrap.', 'data-bs-theme="dark" untuk mode gelap.'],
    qs=[q('Cara paling menyeluruh mengganti warna primer Bootstrap?', ['Mengubah $primary di Sass sebelum import', 'Menambah !important di setiap tombol', 'Mengedit bootstrap.min.css'], 0, 'Sass membangun ulang semua komponen dengan nilai baru.')]),
  W('Proyek: halaman kursus',
    ['Gabungkan navbar, hero, grid kartu yang responsif, dan footer.',
     'Perhatikan grid: <code>row-cols-1 row-cols-md-3</code> adalah cara singkat membuat semua kolom anak sama lebar.',
     'Tantangan: tambahkan kartu kursus keempat dan ubah grid menjadi empat kolom di layar <code>lg</code> dengan <code>row-cols-lg-4</code>.'],
    html='''<nav class="navbar bg-body-tertiary border-bottom"><div class="container"><span class="navbar-brand fw-bold">RuangKode</span><a class="btn btn-sm btn-primary">Daftar</a></div></nav>
<header class="container py-5 text-center">
  <h1 class="display-5 fw-bold">Jadi developer mobile</h1>
  <p class="lead text-body-secondary">Belajar Dart, Flutter, Kotlin, dan Compose dari nol.</p>
</header>
<section class="container pb-5">
  <div id="kursus" class="row row-cols-1 row-cols-md-3 g-3">
    <div class="col"><div class="card h-100"><div class="card-body"><h5 class="card-title">Dart</h5><p class="card-text">Bahasa di balik Flutter.</p></div></div></div>
    <div class="col"><div class="card h-100"><div class="card-body"><h5 class="card-title">Flutter</h5><p class="card-text">Satu kode untuk Android dan iOS.</p></div></div></div>
    <div class="col"><div class="card h-100"><div class="card-body"><h5 class="card-title">Kotlin</h5><p class="card-text">Bahasa resmi Android.</p></div></div></div>
  </div>
</section>
<footer class="border-top py-3 text-center small text-body-secondary">© 2026 RuangKode</footer>''',
    fw='bs',
    task={'q': 'Tambahkan kartu keempat di <code>#kursus</code> dan kelas <code>row-cols-lg-4</code>.',
          'test': "(g=>g.children.length>=4&&g.classList.contains('row-cols-lg-4'))(document.getElementById('kursus'))",
          'hint': 'Salin satu div.col, ubah judulnya, lalu tambahkan row-cols-lg-4 pada div#kursus.'},
    pts=['row-cols-* menyamakan lebar semua kolom anak.', 'card h-100 membuat tinggi kartu seragam.'],
    qs=[q('Tailwind dan Bootstrap, mana yang menyediakan komponen siap pakai seperti modal?', ['Bootstrap', 'Tailwind', 'Keduanya sama persis'], 0, 'Tailwind fokus pada utilitas; Bootstrap menyertakan komponen dan JS-nya.')]),
]),
]
