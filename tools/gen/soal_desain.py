"""Soal latihan tambahan untuk jalur UX, Design System, Manajemen Sistem Informasi, dan SIM."""
from mobile_dart_x import S


def Tx(q, h, a): return S(q, h, a, lang='text')
def CS(q, h, a): return S(q, h, a, lang='css')
def H(q, h, a): return S(q, h, a, lang='html')
def Js(q, h, a): return S(q, h, a, lang='json')
def Sq(q, h, a): return S(q, h, a, lang='sql')
def Xl(q, h, a): return S(q, h, a, lang='excel')


UX = {
'Dua sistem berpikir': [
  Tx('Kelompokkan ke Sistem 1 (cepat, otomatis) atau Sistem 2 (lambat, berpikir): (a) menekan tombol hijau "Lanjut", (b) membandingkan tiga paket asuransi, (c) mengenali ikon keranjang, (d) mengisi NPWP.', 'Sistem 1 bekerja tanpa usaha sadar.',
     '(a) Sistem 1\n(b) Sistem 2\n(c) Sistem 1\n(d) Sistem 2'),
  Tx('Halaman checkout memaksa pengguna menghitung sendiri total setelah diskon. Kenapa buruk, dan bagaimana memperbaikinya?', 'Jangan memindahkan pekerjaan Sistem 2 ke pengguna jika sistem bisa menghitungnya.',
     'Pengguna harus memakai Sistem 2 (menghitung), sehingga lelah dan rawan salah.\nPerbaikan: tampilkan subtotal, diskon, ongkir, dan total akhir yang sudah\ndihitung, dengan total paling menonjol di dekat tombol bayar.'),
],
'Ekonomi perilaku & nudge': [
  Tx('Sebutkan bias perilaku di balik: (a) "Hemat Rp50.000!" lebih menarik dari "Bayar Rp150.000", (b) paket tengah paling laku saat ada paket mahal, (c) orang enggan mengganti pengaturan bawaan.', 'Framing, decoy/anchoring, default effect.',
     '(a) framing effect (dan loss aversion)\n(b) decoy effect / anchoring\n(c) default effect / status quo bias'),
  Tx('Bedakan nudge yang etis dan dark pattern, dengan satu contoh masing-masing.', 'Nudge membantu pengguna mencapai tujuannya sendiri dan mudah ditolak.',
     'Nudge etis: tabungan otomatis aktif secara bawaan tetapi bisa dimatikan dengan satu ketukan.\nDark pattern: tombol "Tidak, saya tidak suka hemat" untuk menolak langganan (confirmshaming),\natau pembatalan langganan yang disembunyikan.'),
],
'Model perilaku Fogg: B = MAP': [
  Tx('Pengguna aplikasi olahraga sangat ingin sehat tetapi tidak pernah membuka fitur latihan. Analisis dengan B = MAP dan usulkan perbaikan.', 'Motivasi sudah tinggi; periksa kemampuan (ability) dan pemicu (prompt).',
     'Motivasi: tinggi.\nAbility : rendah, latihan 45 menit dan butuh alat.\nPrompt  : tidak ada pengingat di waktu yang pas.\nPerbaikan: latihan 5 menit tanpa alat sebagai langkah pertama,\nlalu notifikasi pagi setelah alarm (prompt yang menempel ke kebiasaan lama).'),
  Tx('Kapan pemicu (prompt) justru mengganggu?', 'Lihat posisi pengguna di kurva motivasi dan kemampuan.',
     'Saat motivasi atau kemampuan pengguna di bawah garis aksi, pemicu hanya\nterasa sebagai gangguan (notifikasi diabaikan atau aplikasi dihapus).\nNaikkan kemampuan dulu (permudah) sebelum menambah pemicu.'),
],
'Hook model & kebiasaan': [
  Tx('Susun empat tahap Hook model (trigger, action, variable reward, investment) untuk aplikasi belajar bahasa.', 'Pemicu eksternal lalu internal; hadiah bervariasi; investasi yang membuat kembali.',
     'Trigger   : notifikasi "5 menit hari ini?" lalu rasa ingin menjaga runtutan.\nAction    : satu ketukan membuka pelajaran singkat.\nReward    : skor, kata baru, kejutan lencana (bervariasi).\nInvestment: menyimpan kosakata, runtutan hari, target mingguan.'),
  Tx('Kapan desain pembentuk kebiasaan menjadi tidak etis?', 'Gunakan "uji manipulasi": apakah kamu sendiri memakainya dan apakah memperbaiki hidup pengguna?',
     'Saat produk membentuk kebiasaan yang merugikan pengguna (judi, gulir tanpa henti)\natau saat pembuat sendiri tidak mau memakainya. Sediakan batas waktu,\nringkasan pemakaian, dan cara mudah berhenti.'),
],
'Kurangi beban: default, sedikit pilihan, aksi jelas': [
  Tx('Formulir pendaftaran meminta 14 isian. Sebutkan cara memangkas beban tanpa kehilangan data penting.', 'Tanya hanya yang perlu sekarang; isi otomatis; tunda sisanya.',
     '1. Minta yang wajib saja (nama, nomor HP, kata sandi/OTP).\n2. Isi otomatis dari data yang ada (kode pos -> kota).\n3. Tunda data tambahan ke profil setelah pengguna merasakan manfaat.\n4. Satu kolom per baris, label jelas, tombol aksi tunggal "Daftar".'),
  Tx('Halaman produk punya tombol "Beli", "Tambah ke keranjang", "Simpan", "Bandingkan", dan "Bagikan" dengan gaya sama. Bagaimana memperbaikinya?', 'Hick\'s Law dan hierarki aksi: satu aksi utama.',
     'Pilih satu aksi utama (misal "Tambah ke keranjang") dengan gaya paling menonjol,\njadikan "Beli sekarang" sekunder, dan pindahkan Simpan/Bandingkan/Bagikan\nmenjadi ikon tersier atau menu.'),
],
'Progres, bukti sosial & pengingat': [
  Tx('Tulis tiga elemen yang mendorong pengguna menyelesaikan profil di aplikasi lowongan kerja.', 'Progress bar, bukti sosial, pengingat yang relevan.',
     '1. Indikator progres "Profil 60% lengkap" dengan langkah berikutnya yang jelas.\n2. Bukti sosial: "Profil lengkap dilihat perekrut 3x lebih sering."\n3. Pengingat kontekstual setelah melamar: "Tambahkan pengalaman agar lamaranmu menonjol."'),
  Tx('Kapan bukti sosial bisa menjadi menyesatkan?', 'Angka palsu atau tekanan palsu.',
     'Saat angkanya palsu atau tidak bisa diverifikasi ("27 orang melihat ini" acak),\natau dipakai untuk menciptakan kelangkaan palsu. Itu dark pattern dan merusak kepercayaan.'),
],
'Outcome, aktor, dan aksi': [
  Tx('Tulis outcome, aktor, dan aksi untuk fitur "tabungan otomatis" di aplikasi bank.', 'Outcome = perubahan perilaku yang terukur.',
     'Outcome: 30% pengguna baru menabung rutin setiap bulan dalam 90 hari.\nAktor  : pekerja muda bergaji bulanan yang belum punya kebiasaan menabung.\nAksi   : mengaktifkan autodebet ke tabungan pada hari gajian.'),
  Tx('Ubah tujuan kabur "Meningkatkan engagement" menjadi outcome yang terukur.', 'Siapa, melakukan apa, seberapa banyak, kapan.',
     'Kabur : meningkatkan engagement.\nTerukur: menaikkan jumlah pengguna aktif mingguan yang menyelesaikan minimal\n1 pelajaran dari 35% menjadi 45% dalam satu kuartal.'),
],
'Kanvas bisnis, SWOT & kompetitor': [
  Tx('Buat SWOT singkat untuk kedai kopi kecil di dekat kampus yang ingin membuat aplikasi pesan antar.', 'Kekuatan dan kelemahan internal; peluang dan ancaman eksternal.',
     'S: lokasi dekat kampus, pelanggan setia, harga terjangkau\nW: tim kecil, belum punya sistem digital\nO: mahasiswa terbiasa pesan lewat aplikasi, jam belajar malam\nT: jaringan kopi besar dengan promo agresif, komisi aplikasi pihak ketiga'),
  Tx('Susun tabel analisis kompetitor untuk 3 aplikasi catatan keuangan pada 4 kriteria.', 'Kriteria: onboarding, pencatatan cepat, laporan, harga.',
     '              Onboarding   Catat cepat  Laporan       Harga\nAplikasi A    3 langkah    1 ketukan    grafik dasar  gratis + iklan\nAplikasi B    7 langkah    3 ketukan    sangat rinci  langganan\nAplikasi C    login bank   otomatis     kategori AI   freemium\nCelah: pencatatan sangat cepat + laporan sederhana tanpa iklan.'),
],
'Persona berbasis data': [
  Tx('Tulis persona berbasis data untuk aplikasi tabungan, lengkap dengan sumber datanya.', 'Tujuan, frustrasi, perilaku, kutipan nyata, dan dari mana datanya.',
     'Nama   : Dimas, 24 tahun, karyawan baru di Bekasi\nTujuan : dana darurat 3x gaji dalam setahun\nFrustrasi: lupa menabung, uang habis sebelum tanggal 20\nPerilaku: cek saldo 5x seminggu, belanja lewat e-wallet\nKutipan: "Niatnya nabung, tapi selalu nanti."\nSumber : 12 wawancara + survei 340 responden + data aplikasi 3 bulan'),
  Tx('Apa tanda persona yang dibuat-buat (bukan berbasis data)?', 'Detail yang tidak memengaruhi keputusan desain.',
     'Banyak detail hiasan (hobi, nama kucing) tanpa sumber, tidak ada perilaku terukur,\ntidak ada kutipan asli, dan tidak pernah dipakai untuk memutuskan apa pun.'),
],
'User story & peta pengalaman': [
  Tx('Tulis tiga user story dengan acceptance criteria untuk fitur "pengingat bayar tagihan".', 'Sebagai ..., saya ingin ..., agar .... Kriteria dalam format Diberikan/Ketika/Maka.',
     '1. Sebagai pengguna, saya ingin pengingat 3 hari sebelum jatuh tempo agar tidak kena denda.\n   Diberikan tagihan jatuh tempo tanggal 10, Ketika tanggal 7 pukul 09.00, Maka muncul notifikasi.\n2. Sebagai pengguna, saya ingin membayar langsung dari notifikasi agar cepat.\n3. Sebagai pengguna, saya ingin mematikan pengingat per tagihan agar tidak terganggu.'),
  Tx('Buat peta pengalaman (journey map) singkat untuk "membayar listrik pertama kali di aplikasi".', 'Tahap, aksi, pikiran, emosi, pain point, peluang.',
     'Tahap    : cari menu -> isi ID pelanggan -> cek tagihan -> bayar -> bukti\nPain     : menu tersembunyi; ID pelanggan sulit ditemukan; biaya admin baru terlihat di akhir\nEmosi    : bingung -> ragu -> cemas -> lega\nPeluang  : pintasan di beranda; contoh letak ID di struk; biaya admin tampil sejak awal'),
],
'Aturan tata letak yang baik': [
  CS('Buat tata letak kartu produk responsif: 1 kolom di ponsel, 2 di tablet, 3 di desktop, dengan jarak 16px.', 'grid-template-columns dengan repeat dan media query, atau auto-fit + minmax.',
     '.daftar {\n  display: grid;\n  gap: 16px;\n  grid-template-columns: 1fr;\n}\n@media (min-width: 640px) {\n  .daftar { grid-template-columns: repeat(2, 1fr); }\n}\n@media (min-width: 1024px) {\n  .daftar { grid-template-columns: repeat(3, 1fr); }\n}'),
  Tx('Sebutkan empat prinsip tata letak (Gestalt/hierarki) untuk halaman harga paket.', 'Kedekatan, kesamaan, kontras, keselarasan.',
     '1. Kedekatan: harga dan fitur satu paket dikelompokkan rapat.\n2. Kesamaan: semua kartu berstruktur sama agar mudah dibandingkan.\n3. Kontras: paket yang direkomendasikan diberi aksen dan label.\n4. Keselarasan: harga dan tombol sejajar di semua kartu.'),
],
'Fidelity prototipe & alat desain': [
  Tx('Pilih fidelity prototipe: (a) menguji alur pendaftaran dengan 5 pengguna minggu ini, (b) presentasi ke investor, (c) menguji animasi transisi.', 'Low-fi untuk struktur, high-fi untuk visual dan interaksi detail.',
     '(a) low/mid-fi: cepat dibuat, fokus pada alur\n(b) high-fi: tampilan meyakinkan\n(c) high-fi interaktif (Figma prototype/ProtoPie) atau kode'),
  Tx('Kenapa menguji prototipe low-fi sering memberi masukan yang lebih jujur?', 'Pengguna merasa desain belum "jadi".',
     'Pengguna tidak sibuk mengomentari warna atau font dan merasa lebih bebas\nmengkritik karena desain terlihat belum selesai, sehingga masukan fokus pada alur dan isi.'),
],
'A/B test yang benar': [
  Tx('Rancang A/B test untuk tombol "Daftar gratis" vs "Mulai belajar": hipotesis, metrik utama, metrik pengaman, dan durasi.', 'Satu perubahan, satu metrik utama, durasi minimal satu siklus mingguan.',
     'Hipotesis : "Mulai belajar" menaikkan pendaftaran karena fokus pada manfaat.\nMetrik    : tingkat pendaftaran dari pengunjung halaman.\nPengaman  : tingkat aktivasi 7 hari (agar tidak mendaftar lalu pergi).\nDurasi    : minimal 2 minggu penuh, sampel dihitung lebih dulu, tanpa mengintip lalu berhenti.'),
  Tx('Tim menghentikan A/B test pada hari ketiga karena varian B "sudah menang". Apa masalahnya?', 'Peeking dan efek hari dalam seminggu.',
     'Mengintip lalu berhenti saat hasil terlihat bagus menaikkan peluang hasil palsu.\nTiga hari juga belum mencakup pola hari kerja/akhir pekan.\nTentukan ukuran sampel dan durasi di awal, lalu patuhi.'),
],
}

DS = {
'Design system, pustaka komponen & atomic design': [
  Tx('Kelompokkan ke atom, molekul, organisme, template, atau halaman: (a) tombol, (b) kolom cari + tombol, (c) header situs, (d) kerangka halaman produk, (e) halaman produk "Kopi Gayo".', 'Dari terkecil ke terbesar.',
     '(a) atom\n(b) molekul\n(c) organisme\n(d) template\n(e) halaman'),
  Tx('Apa beda design system dan pustaka komponen (UI kit)?', 'Design system lebih dari sekadar komponen.',
     'Pustaka komponen: kumpulan komponen siap pakai (desain dan/atau kode).\nDesign system: komponen + token + prinsip + pedoman penggunaan + proses\nkontribusi dan tata kelola, menjadi sumber kebenaran bersama tim.'),
],
'Kapan tim butuh design system?': [
  Tx('Sebutkan empat tanda tim sudah butuh design system.', 'Inkonsistensi dan pekerjaan berulang.',
     '1. Ada 7 gaya tombol berbeda untuk fungsi yang sama.\n2. Desainer dan developer membuat ulang komponen yang sama di tiap fitur.\n3. Beberapa produk/tim harus terlihat satu merek.\n4. Review desain habis untuk membahas warna dan jarak, bukan masalah pengguna.'),
  Tx('Kapan design system justru belum perlu?', 'Pikirkan tahap produk dan ukuran tim.',
     'Saat produk masih mencari product-market fit dengan 1-2 desainer dan arah visual\nmasih sering berubah. Cukup mulai dari token dasar dan beberapa komponen inti.'),
],
'Audit visual & pilot': [
  Tx('Langkah apa saja untuk audit visual sebelum membangun design system?', 'Kumpulkan, kelompokkan, hitung variasi.',
     '1. Tangkap layar semua halaman penting.\n2. Kelompokkan elemen: tombol, warna, tipografi, ikon, form.\n3. Hitung variasinya (misal 23 warna abu-abu, 9 ukuran font).\n4. Tandai yang bisa disatukan dan presentasikan temuan ke tim.'),
  Tx('Kenapa design system sebaiknya diuji lewat satu proyek pilot dulu?', 'Belajar dari pemakaian nyata.',
     'Komponen diuji pada kebutuhan nyata, masalah ditemukan lebih cepat,\ntim mendapat contoh sukses untuk meyakinkan tim lain, dan risiko\nmengubah seluruh produk sekaligus berkurang.'),
],
'Prinsip desain & tone of voice': [
  Tx('Tulis tiga prinsip desain spesifik untuk aplikasi tabungan pelajar (bukan slogan umum).', 'Prinsip yang baik bisa dipakai memenangkan perdebatan desain.',
     '1. Uang selalu terlihat jelas: saldo dan dampak setiap aksi tampil sebelum konfirmasi.\n2. Satu langkah untuk kebiasaan baik: menabung harus bisa dilakukan dengan satu ketukan.\n3. Merayakan, bukan menghakimi: progres dipuji, kegagalan diberi jalan keluar.'),
  Tx('Tulis ulang pesan error "Transaksi gagal. Error 402." dengan tone yang ramah dan membantu.', 'Jelaskan apa yang terjadi, kenapa, dan apa yang bisa dilakukan.',
     'Pembayaran belum berhasil karena saldo kurang Rp12.000.\nIsi saldo atau pilih metode pembayaran lain, lalu coba lagi.'),
],
'Token: primitif, semantik, komponen': [
  Js('Tulis token dalam format DTCG untuk satu warna primitif, satu token semantik yang merujuknya, dan satu token komponen.', 'Token semantik merujuk primitif dengan sintaks {nama.token}.',
     '{\n  "color": {\n    "blue": { "600": { "$type": "color", "$value": "#0B6FA4" } },\n    "action": { "primary": { "$type": "color", "$value": "{color.blue.600}" } }\n  },\n  "button": {\n    "primary": { "background": { "$type": "color", "$value": "{color.action.primary}" } }\n  }\n}'),
  CS('Tulis token yang sama sebagai CSS custom property, lalu pakai di tombol.', 'Komponen hanya memakai token semantik/komponen, bukan nilai mentah.',
     ':root {\n  --color-blue-600: #0B6FA4;\n  --color-action-primary: var(--color-blue-600);\n  --button-primary-bg: var(--color-action-primary);\n}\n.tombol-utama {\n  background: var(--button-primary-bg);\n  color: #fff;\n}'),
],
'Warna fungsional & kontras': [
  Tx('Tentukan apakah lolos WCAG AA: (a) teks body abu #767676 di putih (4,54:1), (b) teks body #999999 di putih (2,85:1), (c) ikon tombol 3,2:1 terhadap latar.', 'Teks normal minimal 4,5:1; komponen UI dan teks besar minimal 3:1.',
     '(a) lolos (4,54 >= 4,5)\n(b) tidak lolos untuk teks body\n(c) lolos untuk komponen UI (>= 3:1)'),
  Tx('Kenapa status error tidak boleh hanya ditandai warna merah?', 'Sekitar 1 dari 12 laki-laki buta warna.',
     'Pengguna buta warna atau layar di bawah terik matahari mungkin tidak bisa membedakan merah.\nTambahkan ikon, teks pesan yang jelas, dan garis atau bentuk yang berbeda.'),
],
'Skala tipografi & jarak': [
  Tx('Hitung skala tipografi dengan dasar 16px dan rasio 1,25 untuk 4 langkah ke atas (bulatkan).', 'Setiap langkah dikali 1,25.',
     '16 -> 20 -> 25 -> 31 -> 39 px\n(body, h4, h3, h2, h1)'),
  CS('Buat token jarak berbasis 4/8 px dan pakai untuk padding kartu dan jarak antar elemen.', '--space-1: 4px, --space-2: 8px, --space-4: 16px, dan seterusnya.',
     ':root {\n  --space-1: 4px;\n  --space-2: 8px;\n  --space-3: 12px;\n  --space-4: 16px;\n  --space-6: 24px;\n}\n.kartu {\n  padding: var(--space-4);\n  display: grid;\n  gap: var(--space-2);\n}'),
],
'Mode gelap dengan token CSS': [
  CS('Definisikan token latar dan teks untuk mode terang, lalu ubah nilainya saat sistem memakai mode gelap.', 'Komponen tetap memakai var(--bg) dan var(--teks); hanya token yang berubah.',
     ':root {\n  --bg: #FFFFFF;\n  --teks: #1F2328;\n  --garis: #D0D7DE;\n}\n@media (prefers-color-scheme: dark) {\n  :root {\n    --bg: #0D1117;\n    --teks: #E6EDF3;\n    --garis: #30363D;\n  }\n}\nbody { background: var(--bg); color: var(--teks); }'),
  CS('Tambahkan pilihan tema manual dengan atribut <code>data-tema</code> yang mengalahkan pengaturan sistem.', 'Selector [data-tema="gelap"] dan [data-tema="terang"] di :root.',
     ':root[data-tema="gelap"] {\n  --bg: #0D1117;\n  --teks: #E6EDF3;\n  color-scheme: dark;\n}\n:root[data-tema="terang"] {\n  --bg: #FFFFFF;\n  --teks: #1F2328;\n  color-scheme: light;\n}'),
],
'Komponen tombol lengkap dengan state': [
  CS('Tulis CSS tombol dengan state hover, focus-visible, active, dan disabled.', 'Fokus harus terlihat jelas untuk pengguna keyboard.',
     '.tombol {\n  background: var(--button-primary-bg);\n  color: #fff;\n  border: 0;\n  border-radius: 8px;\n  padding: 10px 16px;\n  min-height: 44px;\n}\n.tombol:hover { filter: brightness(1.08); }\n.tombol:active { transform: translateY(1px); }\n.tombol:focus-visible { outline: 3px solid var(--fokus); outline-offset: 2px; }\n.tombol:disabled { opacity: .5; cursor: not-allowed; }'),
  H('Tulis HTML tombol dalam keadaan memuat (loading) yang tetap aksesibel.', 'aria-busy, teks yang dibaca pembaca layar, dan tombol dinonaktifkan sementara.',
     '<button class="tombol" type="submit" aria-busy="true" disabled>\n  <span class="spinner" aria-hidden="true"></span>\n  Menyimpan...\n</button>'),
],
'Anatomi komponen form & umpan balik': [
  H('Tulis kolom email lengkap: label, petunjuk, pesan error yang terhubung, dan status tidak valid.', 'label for, aria-describedby ke petunjuk dan error, aria-invalid.',
    '<label for="email">Email</label>\n<p id="email-petunjuk">Kami kirim bukti pembayaran ke sini.</p>\n<input id="email" type="email" autocomplete="email"\n       aria-describedby="email-petunjuk email-error" aria-invalid="true">\n<p id="email-error" class="error">Format email belum benar, contoh: rina@mail.id</p>'),
  Tx('Kapan validasi sebaiknya muncul: saat mengetik, saat meninggalkan kolom, atau saat kirim?', 'Jangan menyalahkan pengguna sebelum selesai mengetik.',
     'Saat meninggalkan kolom (blur) untuk format seperti email.\nSaat mengetik hanya untuk umpan balik positif atau kekuatan kata sandi.\nSaat kirim: ringkas semua error di atas form dan arahkan fokus ke error pertama.'),
],
'Dokumentasi & katalog komponen': [
  Tx('Susun isi halaman dokumentasi komponen Tombol.', 'Kapan dipakai, kapan tidak, varian, state, aksesibilitas, kode.',
     '1. Deskripsi singkat dan contoh hidup\n2. Kapan dipakai dan kapan tidak (contoh benar/salah)\n3. Varian: primer, sekunder, teks, bahaya\n4. Ukuran dan state\n5. Aksesibilitas: label, fokus, ukuran sentuh 44px\n6. Properti dan cuplikan kode\n7. Riwayat perubahan'),
  Tx('Sebutkan alat untuk katalog komponen dan dokumentasi design system.', 'Kode dan desain.',
     'Kode   : Storybook, Ladle, Histoire\nDesain : Figma library + Dev Mode\nSitus  : Zeroheight, Supernova, atau situs dokumentasi sendiri'),
],
'Versi, kontribusi & metrik adopsi': [
  Tx('Tentukan versi semver berikutnya dari 2.4.1 untuk: (a) memperbaiki warna fokus, (b) menambah varian tombol baru, (c) mengganti nama properti "type" menjadi "variant".', 'MAJOR.MINOR.PATCH.',
     '(a) 2.4.2 (patch)\n(b) 2.5.0 (minor, fitur baru kompatibel)\n(c) 3.0.0 (major, perubahan yang merusak)'),
  Tx('Sebutkan tiga metrik adopsi design system.', 'Seberapa banyak dipakai dan seberapa membantu.',
     '1. Persentase komponen di produk yang berasal dari design system.\n2. Jumlah tim/produk yang memakai versi terbaru.\n3. Waktu membangun fitur baru atau jumlah bug UI sebelum dan sesudah adopsi.'),
],
}

MSI = {
'Manajemen Sistem Informasi vs Sistem Informasi Manajemen': [
  Tx('Kelompokkan ke "Manajemen SI" (mengelola SI) atau "SIM" (sistem yang menghasilkan informasi untuk manajer): (a) laporan penjualan mingguan, (b) memilih vendor ERP, (c) anggaran TI tahunan, (d) dashboard stok.', 'Mengelola sistemnya vs memakai informasinya.',
     '(a) SIM\n(b) Manajemen SI\n(c) Manajemen SI\n(d) SIM'),
  Tx('Sebutkan dua tugas manajer SI di sebuah rumah sakit.', 'Perencanaan, pengadaan, keamanan, layanan.',
     '1. Merencanakan dan mengawasi penerapan sistem rekam medis elektronik.\n2. Menjamin keamanan data pasien dan ketersediaan sistem 24 jam.'),
],
'Data, informasi, dan pengetahuan': [
  Tx('Kelompokkan ke data, informasi, atau pengetahuan: (a) "27, 31, 29", (b) "suhu rata-rata gudang minggu ini 29 °C", (c) "di atas 30 °C cokelat meleleh, maka pengiriman siang ditunda".', 'Data mentah, data yang diberi konteks, pemahaman untuk bertindak.',
     '(a) data\n(b) informasi\n(c) pengetahuan'),
  Tx('Sebutkan lima ciri informasi yang berkualitas.', 'Akurat, tepat waktu, ...',
     'Akurat, tepat waktu, relevan, lengkap, dan mudah dipahami (ringkas).'),
],
'Komponen sistem informasi': [
  Tx('Uraikan lima komponen SI pada sistem kasir minimarket.', 'Hardware, software, data, prosedur, manusia (dan jaringan).',
     'Hardware : komputer kasir, pemindai barcode, printer struk\nSoftware : aplikasi POS, database\nData     : produk, harga, transaksi, stok\nProsedur : buka/tutup kasir, retur, setor uang\nManusia  : kasir, kepala toko, admin pusat\nJaringan : koneksi ke server pusat'),
  Tx('Sistem kasir baru gagal dipakai padahal aplikasinya bagus. Komponen mana yang kemungkinan terlupakan?', 'Teknologi saja tidak cukup.',
     'Komponen manusia dan prosedur: kasir tidak dilatih, prosedur lama tidak\ndiperbarui, dan tidak ada orang yang bertanggung jawab saat sistem bermasalah.'),
],
'SIM dan tingkat manajemen': [
  Tx('Pasangkan kebutuhan informasi dengan tingkat manajemen: (a) jadwal shift besok, (b) target penjualan kuartal per cabang, (c) membuka pasar di provinsi baru.', 'Operasional, taktis (menengah), strategis (puncak).',
     '(a) operasional\n(b) taktis\n(c) strategis'),
  Tx('Bagaimana bentuk informasi berbeda antara manajer operasional dan direksi?', 'Rinci dan sering vs ringkas dan jarang.',
     'Operasional: rinci, harian, data internal, terstruktur (daftar pesanan hari ini).\nDireksi    : ringkas, berkala, banyak data eksternal, tren dan perbandingan (KPI kuartal).'),
],
'Berpikir sistem: melihat gambaran utuh': [
  Tx('Identifikasi input, proses, output, dan umpan balik pada sistem perpustakaan sekolah.', 'Model sistem IPO + feedback.',
     'Input      : data buku, data siswa, permintaan pinjam\nProses     : pencatatan pinjam/kembali, hitung denda\nOutput     : bukti pinjam, laporan buku terpopuler, daftar terlambat\nUmpan balik: laporan keterlambatan dipakai untuk mengubah aturan masa pinjam'),
  Tx('Apa risiko memperbaiki satu bagian tanpa melihat sistem utuh? Beri contoh.', 'Optimasi lokal.',
     'Gudang mempercepat pengiriman dengan mengirim tanpa cek kualitas,\nlalu retur naik dan layanan pelanggan kewalahan. Satu bagian membaik,\nsistem secara keseluruhan memburuk.'),
],
'Melihat dari banyak sudut pandang': [
  Tx('Aplikasi absensi sekolah baru: tulis kepentingan siswa, guru, orang tua, dan admin TU.', 'Setiap pemangku kepentingan punya tujuan berbeda.',
     'Siswa    : absen cepat, tidak salah tercatat\nGuru     : rekap kelas otomatis, tidak menyita waktu mengajar\nOrang tua: notifikasi jika anak tidak hadir\nAdmin TU : laporan bulanan ke dinas tanpa input ulang'),
  Tx('Dua pemangku kepentingan berkonflik: bagian keuangan ingin persetujuan berlapis, tim penjualan ingin proses cepat. Bagaimana mencari jalan tengah?', 'Cari kebutuhan di balik posisi.',
     'Kebutuhan keuangan adalah kontrol risiko, kebutuhan penjualan adalah kecepatan.\nJalan tengah: persetujuan otomatis untuk transaksi di bawah batas tertentu,\npersetujuan berlapis hanya untuk nilai besar.'),
],
'Problem solving terstruktur': [
  Tx('Gunakan 5 Whys untuk masalah "laporan stok bulanan selalu terlambat".', 'Tanya "kenapa" berulang sampai ke akar.',
     '1. Kenapa terlambat? Data stok cabang masuk terlambat.\n2. Kenapa? Cabang mengirim spreadsheet manual.\n3. Kenapa manual? Tidak ada sistem input bersama.\n4. Kenapa? Proyek sistem stok ditunda karena anggaran.\n5. Kenapa? Dampak keterlambatan tidak pernah dihitung.\nAkar: belum ada kasus bisnis untuk sistem stok terpusat.'),
  Tx('Susun pohon masalah (issue tree) untuk "laba toko turun".', 'Laba = pendapatan - biaya.',
     'Laba turun\n├─ Pendapatan turun\n│  ├─ Jumlah transaksi turun\n│  └─ Nilai per transaksi turun\n└─ Biaya naik\n   ├─ Harga pokok naik\n   └─ Biaya operasional naik (sewa, gaji, listrik)'),
],
'Sebab-akibat, umpan balik, dan efek samping': [
  Tx('Gambarkan lingkaran umpan balik (feedback loop) untuk "ulasan bagus menaikkan penjualan".', 'Loop penguat: A naik -> B naik -> A naik lagi.',
     'Ulasan bagus -> lebih banyak pembeli -> lebih banyak ulasan -> peringkat naik\n-> lebih banyak pembeli (loop penguat).\nLoop penyeimbang: pesanan melonjak -> pengiriman terlambat -> ulasan buruk.'),
  Tx('Kebijakan "target panggilan per jam" di call center. Apa efek samping yang mungkin muncul?', 'Orang mengoptimalkan apa yang diukur.',
     'Agen memutus panggilan cepat tanpa menyelesaikan masalah, sehingga pelanggan\nmenelepon ulang, kepuasan turun, dan beban justru naik.\nUkur juga tingkat masalah selesai di panggilan pertama.'),
],
'Studi kasus: berpikir utuh dari masalah sampai solusi': [
  Tx('Koperasi sekolah sering kehabisan stok barang laris. Tulis alur dari masalah sampai solusi dalam 5 langkah.', 'Definisikan, cari akar, pilih solusi, uji, ukur.',
     '1. Definisi: barang laris habis rata-rata 6 hari per bulan.\n2. Akar: pencatatan stok manual, pemesanan hanya berdasarkan ingatan.\n3. Solusi: aplikasi kasir sederhana dengan peringatan stok minimum.\n4. Uji: coba 1 bulan untuk 20 barang terlaris.\n5. Ukur: hari kehabisan stok turun dari 6 menjadi 1.'),
  Tx('Apa saja yang harus dicek sebelum menyatakan solusi berhasil?', 'Bandingkan dengan kondisi awal dan efek samping.',
     'Metrik dibanding baseline, efek samping (stok menumpuk, modal terikat),\npenerimaan pengguna (kasir benar-benar memakai), dan biaya perawatan.'),
],
'TPS, MIS, DSS, dan EIS': [
  Tx('Tentukan jenis sistem: (a) mesin kasir mencatat penjualan, (b) laporan penjualan bulanan per cabang, (c) simulasi "bagaimana jika harga naik 10%", (d) dashboard ringkas untuk direktur.', 'TPS, MIS, DSS, EIS.',
     '(a) TPS\n(b) MIS\n(c) DSS\n(d) EIS'),
  Tx('Kenapa kualitas TPS menentukan kualitas MIS dan EIS?', 'Dari mana data laporan berasal?',
     'MIS dan EIS mengolah data yang dicatat TPS. Jika transaksi salah atau tidak\nlengkap, semua laporan dan dashboard di atasnya ikut salah (garbage in, garbage out).'),
],
'Sistem informasi fungsional': [
  Tx('Sebutkan satu sistem informasi untuk tiap fungsi: pemasaran, keuangan, SDM, produksi.', 'Fungsi bisnis utama.',
     'Pemasaran: CRM dan analitik kampanye\nKeuangan : akuntansi dan penggajian\nSDM      : HRIS (data karyawan, cuti, rekrutmen)\nProduksi : perencanaan produksi dan kontrol kualitas'),
  Tx('Apa masalah jika setiap fungsi punya sistem sendiri yang tidak terhubung?', 'Silo data.',
     'Data ganda dan tidak konsisten, input berulang, laporan lintas fungsi\nsulit dibuat, dan keputusan lambat. Solusinya integrasi atau ERP.'),
],
'ERP, CRM, dan SCM': [
  Tx('Pasangkan kebutuhan dengan sistem: (a) riwayat keluhan pelanggan, (b) jadwal pengiriman dari pemasok, (c) satu basis data untuk keuangan, stok, dan SDM.', 'CRM, SCM, ERP.',
     '(a) CRM\n(b) SCM\n(c) ERP'),
  Tx('Sebutkan tiga risiko implementasi ERP dan cara menguranginya.', 'ERP mengubah proses kerja.',
     '1. Proses lama dipaksakan ke ERP (kustomisasi berlebihan) -> ikuti praktik standar sebisa mungkin.\n2. Data migrasi kotor -> bersihkan data sebelum migrasi.\n3. Pengguna menolak -> libatkan sejak awal, pelatihan, dan dukungan pasca go-live.'),
],
'Database dan DBMS': [
  Tx('Sebutkan empat keuntungan DBMS dibanding menyimpan data di banyak file spreadsheet.', 'Redundansi, konsistensi, akses bersama, keamanan.',
     '1. Mengurangi data ganda (redundansi).\n2. Menjaga konsistensi dengan aturan (constraint).\n3. Banyak pengguna bisa mengakses bersamaan dengan aman.\n4. Hak akses, cadangan, dan pemulihan lebih terkendali.'),
  Sq('Tulis query untuk menampilkan 5 produk dengan stok di bawah 10, urut dari stok terkecil.', 'SELECT, WHERE, ORDER BY, LIMIT.',
     'SELECT nama, stok\nFROM produk\nWHERE stok < 10\nORDER BY stok ASC\nLIMIT 5;'),
],
'Merancang tabel dan relasi (ERD)': [
  Tx('Rancang entitas dan relasi untuk sistem peminjaman buku perpustakaan.', 'Siswa, Buku, Peminjaman; tentukan kardinalitas.',
     'SISWA (nis PK, nama, kelas)\nBUKU (kode_buku PK, judul, penulis)\nPEMINJAMAN (id PK, nis FK, kode_buku FK, tgl_pinjam, tgl_kembali)\n\nSISWA 1 --- N PEMINJAMAN N --- 1 BUKU\n(relasi banyak-ke-banyak siswa-buku dipecah oleh tabel PEMINJAMAN)'),
  Sq('Tulis CREATE TABLE untuk tabel PEMINJAMAN dengan kunci asing ke SISWA dan BUKU.', 'PRIMARY KEY, REFERENCES, NOT NULL.',
     'CREATE TABLE peminjaman (\n  id          INTEGER PRIMARY KEY,\n  nis         TEXT NOT NULL REFERENCES siswa(nis),\n  kode_buku   TEXT NOT NULL REFERENCES buku(kode_buku),\n  tgl_pinjam  DATE NOT NULL,\n  tgl_kembali DATE\n);'),
],
'Data warehouse, BI, dan kualitas data': [
  Tx('Sebutkan enam dimensi kualitas data dengan contoh masalahnya.', 'Akurasi, kelengkapan, konsistensi, ketepatan waktu, validitas, keunikan.',
     'Akurasi      : harga tercatat 1.800 padahal 18.000\nKelengkapan  : 20% pelanggan tanpa kota\nKonsistensi  : "Jkt", "Jakarta", "DKI" untuk kota yang sama\nTepat waktu  : data penjualan baru masuk 3 hari kemudian\nValiditas    : tanggal lahir 31/02/2001\nKeunikan     : satu transaksi tercatat dua kali'),
  Tx('Kenapa laporan BI tidak diambil langsung dari database transaksi (OLTP)?', 'Beban dan struktur data.',
     'Query analitik berat memperlambat transaksi pelanggan, data OLTP tersebar di\nbanyak tabel dan sistem, dan riwayat tidak disimpan. Warehouse menyatukan,\nmembersihkan, dan menyimpan riwayat khusus untuk analisis.'),
],
'Siklus hidup pengembangan sistem (SDLC)': [
  Tx('Urutkan tahap SDLC dan tulis satu keluaran (deliverable) tiap tahap.', 'Perencanaan, analisis, desain, implementasi, pengujian, pemeliharaan.',
     'Perencanaan   : dokumen kelayakan dan jadwal\nAnalisis      : dokumen kebutuhan (SRS)\nDesain        : ERD, desain UI, arsitektur\nImplementasi  : kode program\nPengujian     : laporan uji dan UAT\nPemeliharaan  : log perbaikan dan pembaruan'),
  Tx('Pilih waterfall atau agile: (a) sistem pelaporan pajak dengan aturan yang sudah pasti, (b) aplikasi startup yang kebutuhannya terus berubah.', 'Kepastian kebutuhan.',
     '(a) waterfall (kebutuhan stabil dan terdokumentasi)\n(b) agile/Scrum (rilis kecil, umpan balik cepat)'),
],
'Menggali kebutuhan dan memodelkan proses': [
  Tx('Kelompokkan ke kebutuhan fungsional atau non-fungsional: (a) sistem mencetak kuitansi, (b) halaman tampil di bawah 2 detik, (c) admin bisa menambah produk, (d) data dienkripsi.', 'Fungsional = apa yang dilakukan sistem.',
     '(a) fungsional\n(b) non-fungsional (kinerja)\n(c) fungsional\n(d) non-fungsional (keamanan)'),
  Tx('Tulis alur proses (as-is) pemesanan katering lewat WhatsApp, lalu satu perbaikan (to-be).', 'Langkah berurutan dan siapa pelakunya.',
     'As-is: pelanggan chat -> admin tanya menu & jumlah -> admin hitung manual\n-> kirim nomor rekening -> pelanggan kirim bukti -> admin cek mutasi -> catat di buku.\nTo-be: formulir pesanan online dengan total otomatis dan pembayaran QRIS\nyang langsung terverifikasi dan tercatat.'),
],
'Studi kelayakan dan biaya-manfaat': [
  Tx('Hitung payback period: sistem baru biaya Rp60 juta, menghemat Rp2,5 juta per bulan.', 'Biaya dibagi penghematan per bulan.',
     '60.000.000 / 2.500.000 = 24 bulan (2 tahun).'),
  Tx('Sebutkan lima aspek studi kelayakan (TELOS).', 'Technical, Economic, Legal, Operational, Schedule.',
     'Teknis    : teknologinya tersedia dan dikuasai tim?\nEkonomi   : manfaat lebih besar dari biaya?\nHukum     : sesuai regulasi (UU PDP, perpajakan)?\nOperasional: akan dipakai dan didukung pengguna?\nJadwal    : bisa selesai tepat waktu?'),
],
'Jaringan dan cloud computing': [
  Tx('Kelompokkan ke IaaS, PaaS, atau SaaS: (a) Google Workspace, (b) server virtual AWS EC2, (c) Heroku/Vercel untuk menjalankan aplikasi, (d) aplikasi akuntansi online.', 'Seberapa banyak yang dikelola penyedia.',
     '(a) SaaS\n(b) IaaS\n(c) PaaS\n(d) SaaS'),
  Tx('Sebutkan dua keuntungan dan dua risiko memindahkan sistem sekolah ke cloud.', 'Biaya, skala, ketergantungan, data.',
     'Keuntungan: tidak perlu membeli server sendiri; mudah diakses dan diskalakan.\nRisiko    : bergantung pada internet dan penyedia; lokasi dan privasi data harus dijaga.'),
],
'Keamanan informasi': [
  Tx('Pasangkan ancaman dengan aspek CIA yang terganggu: (a) data nilai siswa diubah diam-diam, (b) server diserang hingga mati, (c) data gaji bocor.', 'Confidentiality, integrity, availability.',
     '(a) integrity\n(b) availability\n(c) confidentiality'),
  Tx('Tulis lima kebijakan keamanan dasar untuk kantor kecil.', 'Kata sandi, MFA, pembaruan, cadangan, kesadaran.',
     '1. Kata sandi kuat + pengelola kata sandi.\n2. Autentikasi dua faktor untuk email dan sistem penting.\n3. Pembaruan perangkat lunak rutin.\n4. Cadangan 3-2-1 dan uji pemulihan.\n5. Pelatihan mengenali phishing.'),
],
'Perlindungan data pribadi dan kelangsungan bisnis': [
  Tx('Sebutkan empat hak subjek data menurut UU PDP yang harus didukung aplikasi.', 'Akses, koreksi, hapus, tarik persetujuan.',
     '1. Hak mengakses dan mendapat salinan data.\n2. Hak memperbaiki data yang salah.\n3. Hak menghapus data.\n4. Hak menarik persetujuan pemrosesan.'),
  Tx('Apa beda RPO dan RTO? Beri contoh untuk sistem kasir.', 'Berapa banyak data boleh hilang vs berapa lama boleh mati.',
     'RPO (Recovery Point Objective): batas data yang boleh hilang, misal 15 menit transaksi.\nRTO (Recovery Time Objective): batas waktu sistem boleh mati, misal 1 jam.'),
],
'SI untuk keunggulan bersaing': [
  Tx('Analisis lima kekuatan Porter singkat untuk aplikasi pesan antar makanan lokal.', 'Pesaing, pendatang baru, pengganti, pemasok, pembeli.',
     'Persaingan  : sangat tinggi (pemain besar dengan promo)\nPendatang   : sedang (butuh jaringan kurir dan mitra)\nPengganti   : beli langsung, masak sendiri\nPemasok     : restoran bisa pindah platform\nPembeli     : sensitif harga, mudah berpindah aplikasi'),
  Tx('Sebutkan tiga strategi SI untuk keunggulan bersaing dengan contohnya.', 'Biaya rendah, diferensiasi, fokus.',
     'Biaya rendah  : otomasi gudang menekan biaya per pesanan.\nDiferensiasi  : rekomendasi personal yang tepat.\nFokus/niche   : sistem khusus untuk bengkel motor di kota kecil.'),
],
'Transformasi digital, KPI, dan balanced scorecard': [
  Tx('Susun satu KPI untuk tiap perspektif balanced scorecard sebuah toko online.', 'Keuangan, pelanggan, proses internal, pembelajaran & pertumbuhan.',
     'Keuangan    : margin kotor per bulan\nPelanggan   : tingkat pembelian ulang 90 hari\nProses      : waktu proses pesanan sampai dikirim\nPembelajaran: jam pelatihan tim per kuartal'),
  Tx('Ubah KPI kabur "meningkatkan kepuasan pelanggan" menjadi KPI SMART.', 'Specific, Measurable, Achievable, Relevant, Time-bound.',
     'Menaikkan skor CSAT layanan pelanggan dari 78% menjadi 85%\npada akhir kuartal 2, diukur dari survei setelah tiket ditutup.'),
],
'Tata kelola TI dan manajemen proyek SI': [
  Tx('Isi matriks RACI untuk "migrasi data ke sistem baru": manajer proyek, tim TI, kepala keuangan, staf keuangan.', 'Responsible, Accountable, Consulted, Informed.',
     'Manajer proyek : A (akuntabel)\nTim TI         : R (mengerjakan)\nKepala keuangan: C (dimintai pendapat dan persetujuan data)\nStaf keuangan  : I (diberi tahu jadwal dan dampaknya)'),
  Tx('Proyek SI terlambat 2 bulan karena permintaan fitur terus bertambah. Apa namanya dan cara mencegahnya?', 'Scope creep.',
     'Scope creep. Cegah dengan ruang lingkup tertulis, proses permintaan perubahan\n(dinilai dampak waktu/biaya), prioritas MoSCoW, dan rilis bertahap.'),
],
'Di perusahaan: distributor dengan ERP': [
  Tx('Distributor sembako ingin ERP. Modul apa yang paling dulu diterapkan dan kenapa?', 'Mulai dari proses inti yang paling sakit.',
     'Penjualan, persediaan, dan pembelian lebih dulu karena inti bisnis distributor\nadalah arus barang. Akuntansi menyusul (terhubung otomatis), lalu SDM.'),
  Tx('Sebutkan tiga data master yang harus dibersihkan sebelum go-live ERP.', 'Data yang dipakai berulang oleh banyak transaksi.',
     '1. Master produk (kode, satuan, harga)\n2. Master pelanggan (nama, alamat, batas kredit)\n3. Master pemasok (nama, termin pembayaran)'),
],
'Di startup: dari spreadsheet ke sistem yang tumbuh': [
  Tx('Kapan startup sebaiknya pindah dari spreadsheet ke sistem/database?', 'Tanda-tanda spreadsheet tidak lagi cukup.',
     'Saat banyak orang mengedit bersamaan, data sering bentrok atau terhapus,\nrumus rumit dan rapuh, perlu hak akses berbeda, atau data sudah puluhan ribu baris.'),
  Tx('Susun langkah bertahap memigrasi data pesanan dari Google Sheets ke aplikasi.', 'Jangan berpindah sekaligus tanpa jalan kembali.',
     '1. Bersihkan dan bakukan kolom di spreadsheet.\n2. Rancang tabel dan impor data lama.\n3. Jalankan paralel 2 minggu dan bandingkan hasilnya.\n4. Pindah penuh, kunci spreadsheet menjadi arsip baca saja.'),
],
'Di sekolah: sistem informasi akademik terpadu': [
  Tx('Sebutkan modul utama sistem informasi akademik sekolah dan penggunanya.', 'Siswa, guru, TU, orang tua.',
     'Data siswa & kelas (TU), jadwal (wakasek), presensi (guru), nilai & rapor (guru, wali kelas),\npembayaran SPP (keuangan), portal orang tua (orang tua), laporan ke dinas (kepala sekolah).'),
  Tx('Data nilai siswa termasuk data pribadi. Tulis tiga pengaturan hak akses yang tepat.', 'Least privilege.',
     '1. Guru hanya bisa mengubah nilai mata pelajaran dan kelas yang diajarnya.\n2. Orang tua hanya melihat data anaknya sendiri.\n3. Perubahan nilai setelah rapor terbit dicatat (audit log) dan butuh persetujuan.'),
],
'Di organisasi: koperasi, yayasan, dan organisasi mahasiswa': [
  Tx('Organisasi mahasiswa ingin mencatat anggota, kegiatan, dan keuangan tanpa biaya. Usulkan solusi sederhana.', 'Alat gratis yang mudah diwariskan ke pengurus berikutnya.',
     'Google Forms + Sheets untuk data anggota dan kehadiran, Google Drive bersama\nuntuk dokumen, spreadsheet kas dengan format baku, dan akun milik organisasi\n(bukan pribadi) agar mudah diserahkan ke pengurus berikutnya.'),
  Tx('Koperasi simpan pinjam: informasi apa yang dibutuhkan pengurus setiap bulan?', 'Kesehatan keuangan dan risiko.',
     'Jumlah simpanan dan pinjaman beredar, anggota menunggak beserta umur tunggakan,\narus kas, sisa hasil usaha sementara, dan anggota baru/keluar.'),
],
'AI, analitik, dan otomatisasi': [
  Tx('Tentukan alat yang tepat: (a) memindahkan data dari email ke spreadsheet setiap hari, (b) memprediksi permintaan minggu depan, (c) menjawab pertanyaan pelanggan yang umum.', 'RPA/otomasi, analitik prediktif, chatbot AI.',
     '(a) otomatisasi alur kerja (RPA, Zapier/Make)\n(b) analitik prediktif / machine learning\n(c) chatbot AI dengan alih ke manusia untuk kasus rumit'),
  Tx('Sebutkan tiga risiko memakai AI generatif di layanan pelanggan dan cara mengendalikannya.', 'Jawaban salah, data pribadi, tanggung jawab.',
     '1. Jawaban keliru -> batasi ke basis pengetahuan resmi dan tampilkan sumber.\n2. Kebocoran data pribadi -> saring data sensitif, atur kebijakan penyimpanan.\n3. Pelanggan frustrasi -> sediakan tombol bicara dengan manusia.'),
],
'E-business, e-commerce, dan e-government': [
  Tx('Kelompokkan model e-commerce: (a) toko resmi merek di marketplace, (b) jual beli barang bekas antar pengguna, (c) pemasok ke restoran, (d) pembayaran pajak online.', 'B2C, C2C, B2B, G2C/C2G.',
     '(a) B2C\n(b) C2C\n(c) B2B\n(d) C2G (e-government)'),
  Tx('Sebutkan tiga layanan e-government di Indonesia dan manfaatnya.', 'Pajak, kependudukan, perizinan.',
     'DJP Online: lapor pajak tanpa antre.\nOSS (Online Single Submission): izin usaha terpadu.\nIdentitas Kependudukan Digital: dokumen kependudukan di ponsel.'),
],
'Etika SI dan karier di bidang sistem informasi': [
  Tx('Kamu menemukan dashboard internal menampilkan nomor HP pelanggan ke semua karyawan. Apa yang kamu lakukan?', 'Laporkan lewat jalur resmi; usulkan perbaikan.',
     'Laporkan ke atasan/petugas pelindungan data, usulkan penyamaran kolom dan\npembatasan akses sesuai peran, lalu catat insiden dan pastikan diperbaiki.\nJangan menyebarkan atau memakai data itu.'),
  Tx('Sebutkan lima peran karier di bidang sistem informasi.', 'Analisis, data, proyek, keamanan, produk.',
     'System analyst, business analyst, data analyst, IT project manager,\nIT security analyst (juga ERP consultant dan product manager).'),
],
'MSI dan UX Designer: siapa mengerjakan apa': [
  Tx('Siapa yang memimpin: (a) memetakan proses bisnis dan kebutuhan sistem, (b) wawancara pengguna dan prototipe layar, (c) memastikan sistem sesuai anggaran dan kebijakan TI?', 'Analis sistem/MSI vs UX designer.',
     '(a) analis sistem (MSI)\n(b) UX designer\n(c) manajer SI'),
  Tx('Tulis dua titik kolaborasi penting antara analis sistem dan UX designer.', 'Kebutuhan dan validasi.',
     '1. Menyamakan kebutuhan: proses bisnis (analis) diterjemahkan menjadi alur pengguna (UX).\n2. Validasi: hasil uji pengguna (UX) dipakai merevisi kebutuhan dan aturan bisnis (analis).'),
],
'Alur membuat aplikasi baru': [
  Tx('Urutkan alur membuat aplikasi baru dari ide sampai rilis.', 'Masalah dulu, kode belakangan.',
     '1. Definisikan masalah dan tujuan\n2. Riset pengguna dan kebutuhan\n3. Prioritaskan fitur (MVP)\n4. Rancang alur, wireframe, prototipe\n5. Uji prototipe\n6. Bangun dan uji (QA)\n7. Rilis bertahap dan ukur'),
  Tx('Tentukan fitur MVP aplikasi antrean puskesmas dari daftar: ambil nomor antre, notifikasi giliran, rekam medis lengkap, pembayaran online, estimasi waktu tunggu.', 'MVP = paling kecil yang sudah menyelesaikan masalah inti.',
     'MVP: ambil nomor antre, estimasi waktu tunggu, notifikasi giliran.\nNanti: pembayaran online, rekam medis lengkap.'),
],
'Alur memperbaiki aplikasi lama agar sesuai standar': [
  Tx('Susun langkah memperbaiki aplikasi lama agar sesuai standar (aksesibilitas, keamanan, UX).', 'Audit, prioritas, perbaiki bertahap, ukur.',
     '1. Audit: heuristik UX, WCAG 2.2, keamanan (OWASP), kinerja\n2. Kelompokkan temuan dan beri tingkat keparahan\n3. Prioritaskan dampak tinggi-usaha rendah\n4. Perbaiki bertahap dengan rilis kecil\n5. Uji ulang dan pantau metrik'),
  Tx('Tulis tiga temuan audit heuristik untuk formulir yang hanya memakai placeholder sebagai label dan menampilkan error "Input tidak valid".', 'Nielsen: pengenalan vs ingatan, bantuan memulihkan error.',
     '1. Placeholder hilang saat mengetik, pengguna lupa isian (severity 3).\n2. Pesan error tidak menjelaskan apa yang salah dan cara memperbaikinya (severity 3).\n3. Kolom tanpa label tidak terbaca pembaca layar (aksesibilitas, severity 4).'),
],
}

SIM = {
'Apa itu sistem informasi manajemen': [
  Tx('Sebutkan tiga keputusan manajer kedai kopi yang dibantu SIM, beserta informasi yang dibutuhkan.', 'Keputusan apa yang diambil setiap minggu?',
     '1. Jumlah bahan baku dipesan -> laporan pemakaian dan stok mingguan.\n2. Jadwal shift karyawan -> pola jam ramai per hari.\n3. Menu yang dihapus -> penjualan dan margin per menu.'),
  Tx('Apa beda data transaksi dan laporan manajemen?', 'Rinci per kejadian vs ringkas untuk keputusan.',
     'Data transaksi: satu baris per kejadian (struk no. 1023, 2 kopi, 09.14).\nLaporan manajemen: ringkasan untuk keputusan (penjualan kopi minggu ini naik 12%).'),
],
'Jenis laporan SIM': [
  Tx('Kelompokkan jenis laporan: (a) laporan stok setiap Senin, (b) peringatan stok di bawah minimum, (c) laporan khusus penjualan saat promo Ramadan diminta direktur, (d) rincian transaksi satu cabang dari laporan total.', 'Terjadwal, pengecualian, sesuai permintaan, drill-down.',
     '(a) terjadwal\n(b) pengecualian (exception)\n(c) sesuai permintaan (on-demand)\n(d) drill-down'),
  Tx('Kenapa laporan pengecualian menghemat waktu manajer?', 'Manajer hanya melihat yang butuh tindakan.',
     'Manajer tidak perlu membaca ratusan baris normal; laporan hanya muncul\nsaat ada yang menyimpang dari batas (stok rendah, biaya melebihi anggaran).'),
],
'Merancang laporan yang benar-benar dipakai': [
  Tx('Rancang laporan mingguan untuk kepala toko: judul, 3 angka utama, 1 grafik, dan bagian tindakan.', 'Mulai dari keputusan yang harus diambil.',
     'Judul   : Kinerja Toko Cabang Medan, 27 Okt - 2 Nov 2026\nAngka   : omzet (vs minggu lalu), jumlah transaksi, produk habis\nGrafik  : omzet harian 7 hari\nTindakan: 3 produk perlu dipesan ulang, 1 shift kekurangan orang'),
  Tx('Laporan 20 halaman dikirim setiap hari tetapi tidak pernah dibaca. Apa yang kamu lakukan?', 'Tanyakan pemakaian dan keputusan.',
     'Wawancarai penerima: keputusan apa yang mereka ambil dan angka apa yang dicari.\nRingkas menjadi 1 halaman berisi angka penting dan pengecualian,\nlampirkan rincian sebagai tautan, lalu ukur apakah laporan baru dibuka.'),
],
'Dari transaksi ke laporan': [
  Sq('Dari tabel transaksi (tanggal, produk, jumlah, harga), buat laporan omzet per produk bulan Oktober 2026, urut dari terbesar.', 'SUM(jumlah * harga), WHERE rentang tanggal, GROUP BY, ORDER BY.',
     "SELECT produk,\n       SUM(jumlah) AS terjual,\n       SUM(jumlah * harga) AS omzet\nFROM transaksi\nWHERE tanggal >= '2026-10-01' AND tanggal < '2026-11-01'\nGROUP BY produk\nORDER BY omzet DESC;"),
  Tx('Urutkan alur data dari kasir sampai laporan manajemen.', 'Input, simpan, olah, sajikan.',
     '1. Kasir mencatat transaksi (TPS)\n2. Data tersimpan di database\n3. Data dibersihkan dan diringkas (harian/mingguan)\n4. Laporan dan dashboard disajikan ke manajer\n5. Keputusan manajer menjadi umpan balik (harga, stok, jadwal)'),
],
'Membangun SIM sederhana dengan spreadsheet': [
  Xl('Sheet Transaksi berisi kolom Tanggal (A), Produk (B), Jumlah (C), Harga (D). Tulis rumus total omzet produk "Kopi" dan jumlah transaksi di bulan Oktober 2026.', 'SUMPRODUCT atau SUMIFS dengan kolom bantu omzet.',
     'Kolom E (omzet) : =C2*D2\nOmzet kopi      : =SUMIFS(E:E;B:B;"Kopi")\nTransaksi Okt   : =COUNTIFS(A:A;">="&DATE(2026;10;1);A:A;"<"&DATE(2026;11;1))'),
  Tx('Sebutkan empat aturan agar spreadsheet SIM tetap rapi dan bisa dipercaya.', 'Struktur tabel, validasi, pemisahan input dan laporan.',
     '1. Satu baris satu transaksi, satu kolom satu jenis data.\n2. Validasi data (daftar pilihan produk, format tanggal).\n3. Pisahkan sheet input, data master, dan laporan.\n4. Kunci sel rumus dan simpan riwayat versi.'),
],
'Mengukur keberhasilan SIM': [
  Tx('Tulis empat metrik keberhasilan SIM persediaan yang baru diterapkan.', 'Ukur pemakaian dan dampak bisnis.',
     '1. Persentase staf yang memakai sistem setiap hari\n2. Waktu menyusun laporan stok (sebelum vs sesudah)\n3. Jumlah kejadian kehabisan stok per bulan\n4. Selisih stok fisik vs sistem saat opname'),
  Tx('Model DeLone & McLean menilai keberhasilan SI dari enam dimensi. Sebutkan.', 'Kualitas, pemakaian, kepuasan, manfaat.',
     'Kualitas sistem, kualitas informasi, kualitas layanan,\npemakaian (intention to use / use), kepuasan pengguna, dan manfaat bersih (net benefits).'),
],
}

SOAL = {'UX_MODULES': UX, 'DS_MODULES': DS, 'MSI_MODULES': MSI, 'SIM_MODULES': SIM}
