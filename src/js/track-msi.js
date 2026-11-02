/* ===================== JALUR MANAJEMEN SISTEM INFORMASI =====================
   Kurikulum Ruang Kode (roadmap.sh belum punya peta MSI): konsep dasar, jenis sistem
   informasi, data, analisis dan perancangan, infrastruktur dan keamanan, strategi dan tata
   kelola, lalu penerapan di perusahaan, startup, sekolah, dan organisasi. Setiap pelajaran
   ditutup dengan contoh nyata dalam blok "Contoh penerapan". */
const MSI_MODULES=[
{t:'Dasar manajemen sistem informasi',lvl:'Pemula',d:'Beda MSI dan SIM, data dan informasi, komponen sistem, dan peran sistem informasi bagi setiap tingkat manajemen.',
 nodes:['MSI vs MIS','Data vs Information','System Components','Management Levels','Role of MIS'],
 lessons:[
  {k:'c',t:'Manajemen Sistem Informasi vs Sistem Informasi Manajemen',nodes:['MSI vs MIS'],lang:'text',run:false,
   b:['Dua istilah ini sering tertukar karena kata-katanya sama, hanya urutannya berbeda. <b>Sistem Informasi Manajemen (SIM)</b> adalah <b>sistemnya</b>: aplikasi dan prosedur yang mengolah data transaksi menjadi laporan untuk membantu manajer mengambil keputusan, misalnya laporan penjualan harian atau rekap presensi bulanan.',
      '<b>Manajemen Sistem Informasi (MSI)</b> adalah <b>cara mengelola</b> seluruh sistem informasi di sebuah organisasi. MSI menjawab pertanyaan manajerial: sistem apa yang perlu dibangun atau dibeli, berapa anggarannya, siapa yang bertanggung jawab, bagaimana proyeknya dijalankan, bagaimana datanya diamankan, dan bagaimana mengukur apakah investasi TI itu berhasil.',
      'Jadi SIM adalah salah satu <b>objek</b> yang dikelola dalam MSI, bersama sistem lain seperti ERP, CRM, aplikasi presensi, dan situs web. Seorang manajer TI di sekolah, misalnya, tidak hanya memakai SIAKAD (SIM), tetapi juga merencanakan pengadaannya, melatih guru, mengatur hak akses, menyiapkan cadangan data, dan menilai manfaatnya setiap tahun. Jalur ini mempelajari keduanya: memahami sistemnya, lalu cara mengelolanya.'],
   code:`Contoh penerapan: SIM vs MSI dalam satu organisasi

             SIM (sistemnya)                 MSI (cara mengelolanya)
Perusahaan   laporan stok & penjualan ERP    memilih vendor ERP, anggaran,
                                             jadwal migrasi, pelatihan staf
Startup      dasbor metrik pengguna          memutuskan bangun vs langganan
                                             SaaS, biaya cloud, keamanan akun
Sekolah      SIAKAD: nilai, rapor, presensi  rencana TI sekolah, hak akses
                                             guru, backup, evaluasi tahunan
Organisasi   aplikasi simpan pinjam koperasi siapa admin, aturan data anggota,
                                             serah terima saat pengurus ganti`,
   pts:['SIM = sistemnya: mengolah data menjadi informasi untuk keputusan manajer.','MSI = pengelolaannya: strategi, anggaran, proyek, keamanan, SDM, dan evaluasi TI.','SIM adalah salah satu objek yang dikelola dalam MSI.'],
   q:[['Kepala sekolah menyusun rencana anggaran dan jadwal penggantian server SIAKAD. Ini contoh?',['Manajemen Sistem Informasi','Sistem Informasi Manajemen','Perangkat lunak'],0,'Merencanakan dan membiayai sistem adalah kegiatan pengelolaan (MSI).'],
      ['Laporan penjualan mingguan otomatis untuk manajer cabang adalah contoh?',['Sistem Informasi Manajemen','Manajemen Sistem Informasi','Tata kelola TI'],0,'Itu keluaran sistem yang membantu keputusan, yaitu SIM.']]},
  {k:'c',t:'Data, informasi, dan pengetahuan',nodes:['Data vs Information'],lang:'text',run:false,
   b:['<b>Data</b> adalah fakta mentah yang belum diolah: angka penjualan per transaksi, daftar hadir siswa, atau jam masuk karyawan. Data sendirian jarang membantu orang mengambil keputusan.',
      '<b>Informasi</b> adalah data yang sudah diolah sehingga punya makna dan berguna bagi penerimanya: "penjualan cabang Medan turun 18% dibanding bulan lalu" atau "12 siswa kelas X-2 absen lebih dari 3 kali minggu ini". <b>Pengetahuan</b> muncul ketika informasi dipadukan dengan pengalaman untuk menjawab "lalu kita harus apa?".',
      'Informasi yang baik punya ciri: <b>akurat</b> (bebas salah), <b>tepat waktu</b> (datang sebelum keputusan dibuat), <b>relevan</b> (sesuai kebutuhan penerima), dan <b>lengkap</b> secukupnya. Laporan yang benar tapi terlambat seminggu sama tidak bergunanya dengan laporan yang cepat tapi salah.'],
   code:`Contoh penerapan: dari data ke keputusan

Perusahaan  data  : 4.210 struk kasir hari ini
            info  : produk A habis di 3 cabang sebelum jam 2 siang
            aksi  : naikkan stok minimum produk A di 3 cabang itu

Startup     data  : log klik aplikasi 50.000 pengguna
            info  : 40% pengguna berhenti di halaman verifikasi KTP
            aksi  : sederhanakan verifikasi, ukur ulang minggu depan

Sekolah     data  : presensi harian 960 siswa
            info  : kelas XI-4 rata-rata terlambat 2x seminggu
            aksi  : wali kelas memanggil siswa, cek jadwal angkot

Organisasi  data  : formulir pendaftaran 300 relawan
            info  : relawan terbanyak tersedia hari Sabtu pagi
            aksi  : pindahkan kegiatan bakti sosial ke Sabtu pagi`,
   pts:['Data = fakta mentah; informasi = data yang diolah dan bermakna.','Pengetahuan = informasi + pengalaman untuk bertindak.','Informasi yang baik: akurat, tepat waktu, relevan, lengkap.'],
   q:[['"Penjualan cabang Medan turun 18% bulan ini" termasuk?',['Informasi','Data mentah','Perangkat keras'],0,'Sudah diolah (dibandingkan) sehingga bermakna bagi manajer.'],
      ['Laporan stok akurat tetapi baru sampai setelah barang habis. Ciri apa yang gagal?',['Tepat waktu','Akurat','Relevan'],0,'Informasi harus datang sebelum keputusan dibuat.']]},
  {k:'c',t:'Komponen sistem informasi',nodes:['System Components','Input Process Output'],lang:'text',run:false,
   b:['Sistem adalah sekumpulan bagian yang bekerja sama mencapai tujuan. Sistem informasi bekerja dengan pola <b>input → proses → output</b>, ditambah <b>umpan balik</b> agar hasilnya bisa diperbaiki, dan <b>penyimpanan</b> agar data bisa dipakai lagi.',
      'Sistem informasi punya enam komponen: <b>perangkat keras</b> (komputer, server, ponsel, mesin kasir), <b>perangkat lunak</b> (aplikasi, sistem operasi), <b>data</b>, <b>prosedur</b> (aturan dan langkah kerja), <b>manusia</b> (pengguna, admin, pengembang), dan <b>jaringan</b> (internet, Wi-Fi, LAN).',
      'Kegagalan sistem jarang hanya karena teknologi. Aplikasi presensi secanggih apa pun gagal bila prosedurnya tidak jelas (siapa yang mengoreksi data salah?) atau penggunanya tidak dilatih. Karena itu sistem informasi dikelola sebagai gabungan teknologi, manusia, dan organisasi.'],
   code:`Contoh penerapan: sistem kasir minimarket (perusahaan)

Perangkat keras : komputer kasir, pemindai barcode, printer struk
Perangkat lunak : aplikasi POS, database stok
Data            : produk, harga, transaksi, stok
Prosedur        : buka kasir, retur barang, setor uang harian
Manusia         : kasir, kepala toko, tim IT pusat
Jaringan        : internet untuk kirim penjualan ke kantor pusat

Input  : scan barcode + jumlah
Proses : hitung total, kurangi stok
Output : struk, laporan penjualan harian
Umpan balik : stok di bawah minimum → usulan pesan ulang`,
   pts:['Pola dasar: input → proses → output + umpan balik + penyimpanan.','Enam komponen: hardware, software, data, prosedur, manusia, jaringan.','Sistem gagal lebih sering karena prosedur dan manusia daripada teknologi.'],
   q:[['Aturan "kasir wajib menyetor uang ke kepala toko setiap pukul 21.00" termasuk komponen?',['Prosedur','Perangkat keras','Jaringan'],0,'Prosedur adalah aturan dan langkah kerja.'],
      ['Usulan pesan ulang otomatis ketika stok rendah adalah contoh?',['Umpan balik','Input','Perangkat lunak saja'],0,'Hasil sistem dipakai untuk mengoreksi keadaan.']]},
  {k:'c',t:'SIM dan tingkat manajemen',nodes:['Management Levels','Role of MIS','Decision Types'],lang:'text',run:false,
   b:['Organisasi biasanya punya tiga tingkat manajemen. <b>Operasional</b> (supervisor, kepala gudang) mengurus pekerjaan harian. <b>Taktis/menengah</b> (manajer cabang, wakil kepala sekolah) mengubah rencana menjadi target bulanan. <b>Strategis/puncak</b> (direktur, kepala sekolah, ketua yayasan) menentukan arah jangka panjang.',
      'Setiap tingkat butuh informasi berbeda. Operasional butuh informasi <b>rinci dan cepat</b> (pesanan mana yang belum dikirim hari ini). Taktis butuh <b>ringkasan berkala</b> (penjualan per cabang bulan ini). Strategis butuh <b>tren dan perbandingan</b>, sering dengan data dari luar (pangsa pasar 3 tahun terakhir).',
      'Jenis keputusannya juga berbeda: <b>terstruktur</b> (aturan jelas, misalnya kapan memesan ulang stok), <b>semi-terstruktur</b> (sebagian aturan, sebagian penilaian, misalnya menentukan diskon), dan <b>tidak terstruktur</b> (membuka cabang di kota baru). <b>Sistem informasi manajemen</b> menyediakan laporan rutin yang menghubungkan ketiga tingkat ini.'],
   code:`Contoh penerapan: siapa butuh informasi apa

               Operasional           Taktis                    Strategis
Perusahaan     pesanan belum kirim   penjualan per cabang      buka cabang baru?
Startup        tiket CS hari ini     retensi pengguna bulanan  galang dana seri A?
Sekolah        siswa absen hari ini  nilai rata-rata per kelas tambah jurusan baru?
Organisasi     relawan bertugas      dana terkumpul per bulan  program 5 tahun ke depan

Rinci & cepat ───────────────► Ringkas & berkala ───────────► Tren & eksternal`,
   pts:['Tiga tingkat: operasional, taktis, strategis.','Makin tinggi tingkatnya, makin ringkas dan jangka panjang informasinya.','Keputusan: terstruktur, semi-terstruktur, tidak terstruktur.'],
   q:[['Kepala sekolah memutuskan membuka jurusan baru. Ini keputusan tingkat?',['Strategis, tidak terstruktur','Operasional, terstruktur','Taktis, terstruktur'],0,'Keputusan jangka panjang tanpa aturan baku.'],
      ['Laporan "penjualan per cabang bulan ini" paling dibutuhkan oleh?',['Manajemen taktis (manajer cabang/area)','Kasir','Pemegang saham saja'],0,'Ringkasan berkala untuk memantau target.']]}
 ]},
{t:'Jenis-jenis sistem informasi',lvl:'Pemula',d:'TPS, MIS, DSS, EIS, sistem fungsional, dan sistem terintegrasi ERP, CRM, SCM.',
 nodes:['TPS','MIS','DSS','EIS','Functional Systems','ERP','CRM','SCM'],
 lessons:[
  {k:'c',t:'TPS, MIS, DSS, dan EIS',nodes:['TPS','MIS','DSS','EIS'],lang:'text',run:false,
   b:['<b>Transaction Processing System (TPS)</b> mencatat transaksi harian: penjualan, pembayaran SPP, absensi. TPS adalah fondasi; tanpa data transaksi yang benar, sistem di atasnya ikut salah.',
      '<b>Management Information System (MIS)</b> merangkum data TPS menjadi laporan rutin untuk manajer menengah, misalnya laporan penjualan mingguan. <b>Decision Support System (DSS)</b> membantu keputusan semi-terstruktur dengan model dan simulasi "bagaimana jika": "jika harga naik 5%, berapa perkiraan laba?".',
      '<b>Executive Information System (EIS)</b> atau dashboard eksekutif menampilkan indikator utama secara ringkas untuk pimpinan puncak, sering dengan data eksternal dan kemampuan menelusuri (drill-down) sampai rincian.'],
   code:`Contoh penerapan: satu data, empat sistem (jaringan apotek)

TPS : kasir mencatat setiap penjualan obat
MIS : laporan mingguan "10 obat terlaris per cabang"
DSS : simulasi "jika stok paracetamol ditambah 20%,
      berapa risiko kedaluwarsa vs risiko kehabisan?"
EIS : dashboard direktur: omzet, margin, stok kritis,
      klik cabang → lihat rincian per hari

Sekolah   : TPS pembayaran SPP → MIS tunggakan per kelas
            → DSS skema cicilan → EIS kesehatan keuangan yayasan`,
   pts:['TPS: mencatat transaksi (fondasi).','MIS: laporan rutin untuk manajer menengah.','DSS: analisis "bagaimana jika" untuk keputusan semi-terstruktur.','EIS: ringkasan indikator untuk pimpinan puncak.'],
   q:[['Simulasi "jika harga naik 5%, berapa laba?" adalah ciri?',['DSS','TPS','EIS'],0,'DSS memakai model untuk menguji skenario.'],
      ['Mesin kasir yang mencatat setiap penjualan termasuk?',['TPS','MIS','DSS'],0,'Ia memproses transaksi harian.']]},
  {k:'c',t:'Sistem informasi fungsional',nodes:['Functional Systems','Accounting IS','HRIS','Marketing IS'],lang:'text',run:false,
   b:['Sistem informasi juga bisa dikelompokkan menurut fungsi bisnis. <b>SI akuntansi & keuangan</b> mencatat jurnal, utang-piutang, gaji, dan menyusun laporan keuangan. <b>SI sumber daya manusia (HRIS)</b> mengelola data karyawan, rekrutmen, cuti, penilaian kinerja, dan penggajian.',
      '<b>SI pemasaran</b> mengelola data pelanggan, kampanye, dan penjualan. <b>SI produksi & operasi</b> mengatur jadwal produksi, persediaan, dan kualitas. Di sekolah, padanannya adalah sistem akademik (nilai, jadwal), kesiswaan, keuangan, dan kepegawaian.',
      'Masalah klasik: setiap bagian membeli aplikasinya sendiri sehingga data tersebar (<b>silo informasi</b>). Bagian penjualan dan gudang punya angka stok berbeda, lalu rapat habis untuk berdebat angka mana yang benar. Inilah alasan sistem terintegrasi seperti ERP dibuat.'],
   code:`Contoh penerapan: fungsi yang sama, organisasi berbeda

Fungsi      Perusahaan          Startup            Sekolah             Organisasi
Keuangan    akuntansi, pajak    burn rate, runway  SPP, dana BOS       iuran, donasi
SDM         payroll, cuti       rekrutmen cepat    data guru & TU      data anggota/relawan
Pemasaran   kampanye, CRM       growth, iklan      PPDB, promosi       publikasi kegiatan
Operasi     produksi, gudang    sprint produk      jadwal pelajaran    agenda program

Tanda silo: "Angka siswa versi TU 958, versi BK 962. Mana yang benar?"`,
   pts:['SI fungsional: keuangan, SDM, pemasaran, produksi/operasi.','Sekolah punya padanan: akademik, kesiswaan, keuangan, kepegawaian.','Aplikasi terpisah per bagian menimbulkan silo informasi.'],
   q:[['Data guru, cuti, dan penggajian dikelola oleh?',['SI sumber daya manusia (HRIS)','SI pemasaran','SI produksi'],0,'HRIS mengelola data pegawai.'],
      ['Gudang dan penjualan punya angka stok berbeda. Masalah ini disebut?',['Silo informasi','Redundansi jaringan','Phishing'],0,'Data tersebar di aplikasi yang tidak terhubung.']]},
  {k:'c',t:'ERP, CRM, dan SCM',nodes:['ERP','CRM','SCM','Enterprise Systems'],lang:'text',run:false,
   b:['<b>Enterprise Resource Planning (ERP)</b> menyatukan keuangan, SDM, pembelian, persediaan, produksi, dan penjualan dalam satu database. Saat penjualan dicatat, stok, piutang, dan laporan keuangan ikut berubah otomatis. Contoh produk: SAP, Oracle, Odoo, dan ERP buatan lokal.',
      '<b>Customer Relationship Management (CRM)</b> mengelola hubungan dengan pelanggan: riwayat pembelian, keluhan, kampanye, dan peluang penjualan. <b>Supply Chain Management (SCM)</b> mengatur aliran barang dari pemasok, pabrik, gudang, sampai ke pelanggan.',
      'Menerapkan ERP bukan sekadar memasang aplikasi. Organisasi harus menyesuaikan proses kerjanya (<b>business process reengineering</b>), memindahkan data lama, dan melatih pengguna. Banyak proyek ERP gagal karena proses lama dipaksa masuk tanpa dibenahi.'],
   code:`Contoh penerapan: satu pesanan di perusahaan distribusi

Tanpa ERP                           Dengan ERP
sales catat di Excel                sales input pesanan sekali
gudang dikabari lewat WhatsApp      stok otomatis dipesan (reserved)
keuangan buat faktur manual         faktur & piutang terbentuk otomatis
direktur tunggu laporan akhir bulan dashboard penjualan real time

CRM di startup   : catat setiap lead dari Instagram → follow-up H+1
SCM di koperasi  : pantau stok beras dari petani anggota sampai toko koperasi
ERP di sekolah   : sistem terpadu PPDB → akademik → keuangan → alumni`,
   pts:['ERP: satu database untuk seluruh fungsi organisasi.','CRM: hubungan pelanggan; SCM: aliran barang dari pemasok ke pelanggan.','Keberhasilan ERP bergantung pada pembenahan proses dan pelatihan.'],
   q:[['Sistem yang membuat penjualan otomatis memperbarui stok dan piutang adalah?',['ERP','Email','Spreadsheet pribadi'],0,'ERP memakai satu database bersama.'],
      ['Mencatat setiap calon pelanggan dan jadwal follow-up paling cocok memakai?',['CRM','SCM','TPS gaji'],0,'CRM mengelola hubungan dan peluang penjualan.']]}
 ]},
{t:'Data dan database untuk manajemen',lvl:'Menengah',d:'Mengelola data dengan DBMS, merancang tabel, gudang data, BI, dan menjaga kualitas data.',
 nodes:['Database','DBMS','ERD','Data Warehouse','Business Intelligence','Data Quality'],
 lessons:[
  {k:'c',t:'Database dan DBMS',nodes:['Database','DBMS','Spreadsheet vs Database'],lang:'text',run:false,
   b:['Banyak organisasi memulai dengan spreadsheet. Masalah muncul saat data membesar dan dipakai banyak orang: salinan file berbeda-beda, rumus terhapus, dan tidak ada yang tahu versi mana yang terbaru.',
      '<b>Database</b> menyimpan data terstruktur dalam tabel yang saling berhubungan. <b>Database Management System (DBMS)</b> seperti MySQL, PostgreSQL, atau SQL Server mengatur akses banyak pengguna sekaligus, hak akses, cadangan, dan mencegah data ganda atau tidak konsisten.',
      'Bahasa untuk bertanya ke database adalah <b>SQL</b>. Manajer tidak harus menulis SQL setiap hari, tetapi memahami dasarnya membantu saat meminta laporan ke tim data. Kamu bisa mencobanya langsung di jalur SQL Ruang Kode.'],
   code:`Contoh penerapan: data siswa (sekolah)

Spreadsheet                          Database
- tiap wali kelas punya file sendiri  - satu tabel siswa untuk semua
- nama "M. Rizky" vs "Muhammad Rizki" - NIS unik, nama ditulis sekali
- file hilang saat laptop rusak       - dicadangkan otomatis setiap malam
- semua orang bisa ubah apa saja      - wali kelas hanya ubah kelasnya

Pertanyaan ke database:
SELECT kelas, COUNT(*) FROM siswa WHERE status = 'aktif' GROUP BY kelas;`,
   pts:['Spreadsheet cocok untuk awal, bermasalah saat data besar dan banyak pengguna.','DBMS mengatur akses bersama, hak akses, konsistensi, dan cadangan.','SQL adalah bahasa untuk mengambil data dari database.'],
   q:[['Kenapa NIS dipakai sebagai kunci data siswa, bukan nama?',['NIS unik, sedangkan nama bisa sama atau ditulis berbeda','Nama terlalu pendek','NIS lebih indah'],0,'Kunci harus unik dan tidak berubah.'],
      ['Fungsi DBMS yang membuat wali kelas hanya bisa mengubah data kelasnya sendiri adalah?',['Hak akses','Grafik','Kompresi'],0,'DBMS mengatur siapa boleh melakukan apa.']]},
  {k:'c',t:'Merancang tabel dan relasi (ERD)',nodes:['ERD','Entity','Relationship','Primary Key'],lang:'text',run:false,
   b:['Sebelum membuat database, rancang dulu <b>entitas</b> (hal yang datanya disimpan: Siswa, Kelas, Guru), <b>atribut</b> (NIS, nama, tanggal lahir), dan <b>relasi</b> antarentitas. Gambar rancangan ini disebut <b>Entity Relationship Diagram (ERD)</b>.',
      'Setiap tabel butuh <b>primary key</b> yang unik. Relasi dibuat lewat <b>foreign key</b>: tabel Pembayaran menyimpan NIS untuk menunjuk siswa yang membayar. Jenis relasi: satu-ke-satu, satu-ke-banyak (satu kelas punya banyak siswa), dan banyak-ke-banyak (siswa mengikuti banyak ekstrakurikuler, satu ekskul punya banyak siswa) yang dipecah dengan tabel penghubung.',
      'Prinsip <b>normalisasi</b>: simpan setiap fakta di satu tempat. Jika nama wali kelas ditulis ulang di setiap baris siswa, mengganti wali kelas berarti mengubah ratusan baris, dan satu saja terlewat membuat data tidak konsisten.'],
   code:`Contoh penerapan: ERD sederhana koperasi (organisasi)

ANGGOTA (no_anggota PK, nama, alamat, tgl_gabung)
SIMPANAN (id PK, no_anggota FK, tanggal, jenis, jumlah)
PINJAMAN (id PK, no_anggota FK, tanggal, pokok, tenor_bulan)
ANGSURAN (id PK, id_pinjaman FK, tanggal, jumlah)

ANGGOTA 1 ──< SIMPANAN       satu anggota, banyak simpanan
ANGGOTA 1 ──< PINJAMAN       satu anggota, banyak pinjaman
PINJAMAN 1 ──< ANGSURAN      satu pinjaman, banyak angsuran

Startup kursus online: PENGGUNA >──< KURSUS lewat tabel PENDAFTARAN`,
   pts:['ERD: entitas, atribut, relasi.','Primary key unik; foreign key menghubungkan tabel.','Relasi banyak-ke-banyak memakai tabel penghubung.','Normalisasi: setiap fakta disimpan di satu tempat.'],
   q:[['Satu kelas punya banyak siswa. Relasinya?',['Satu-ke-banyak','Satu-ke-satu','Tidak ada relasi'],0,'Kelas 1 ── banyak Siswa.'],
      ['Siswa bisa ikut banyak ekskul dan ekskul punya banyak siswa. Cara menyimpannya?',['Tabel penghubung (mis. KEANGGOTAAN_EKSKUL)','Satu kolom berisi daftar ekskul dipisah koma','Tidak bisa disimpan'],0,'Relasi banyak-ke-banyak dipecah menjadi dua relasi satu-ke-banyak.']]},
  {k:'c',t:'Data warehouse, BI, dan kualitas data',nodes:['Data Warehouse','Business Intelligence','Data Quality','Dashboard'],lang:'text',run:false,
   b:['Database transaksi dirancang untuk mencatat dengan cepat, bukan untuk analisis berat. <b>Data warehouse</b> mengumpulkan data dari banyak sistem (kasir, ERP, CRM, iklan) ke satu tempat yang dirancang untuk analisis, biasanya lewat proses <b>ETL</b> (extract, transform, load).',
      '<b>Business Intelligence (BI)</b> adalah alat dan proses untuk mengubah data itu menjadi laporan dan dashboard: Power BI, Tableau, Looker Studio, atau Metabase. Dashboard yang baik dimulai dari pertanyaan bisnis dan <b>KPI</b>, bukan dari grafik yang terlihat keren.',
      'Semua itu sia-sia bila datanya buruk: <i>garbage in, garbage out</i>. Dimensi <b>kualitas data</b>: akurat, lengkap, konsisten, tepat waktu, dan unik (tidak ganda). Tetapkan pemilik data (<b>data owner</b>) untuk setiap tabel penting agar jelas siapa yang bertanggung jawab memperbaikinya.'],
   code:`Contoh penerapan: dashboard pimpinan

Perusahaan : omzet, margin, stok kritis, piutang jatuh tempo
Startup    : pengguna aktif harian (DAU), retensi, CAC, burn rate
Sekolah    : kehadiran, rata-rata nilai per mapel, tunggakan SPP
Organisasi : donasi masuk, dana tersalurkan, jumlah penerima manfaat

Cek kualitas sebelum rapat:
[ ] tidak ada transaksi ganda           (unik)
[ ] semua cabang sudah kirim data       (lengkap)
[ ] definisi "pengguna aktif" sama      (konsisten)
[ ] data per kemarin, bukan bulan lalu  (tepat waktu)`,
   pts:['Data warehouse: menyatukan data dari banyak sistem untuk analisis (via ETL).','BI mengubah data menjadi dashboard berbasis KPI.','Kualitas data: akurat, lengkap, konsisten, tepat waktu, unik.','Setiap data penting butuh pemilik yang bertanggung jawab.'],
   q:[['Kenapa analisis berat tidak dijalankan langsung di database kasir?',['Bisa memperlambat transaksi; data warehouse dirancang untuk analisis','Database kasir tidak punya angka','Dilarang undang-undang'],0,'Sistem transaksi dan analisis punya kebutuhan berbeda.'],
      ['Dua cabang memakai definisi "pelanggan aktif" berbeda. Dimensi kualitas apa yang bermasalah?',['Konsistensi','Ketepatan waktu','Keunikan'],0,'Definisi harus sama agar angka bisa dibandingkan.']]}
 ]},
{t:'Analisis dan perancangan sistem',lvl:'Menengah',d:'SDLC, menggali kebutuhan, memodelkan proses, memilih metode, dan menilai kelayakan.',
 nodes:['SDLC','Requirements','DFD','Flowchart','Use Case','Waterfall','Agile','Feasibility Study'],
 lessons:[
  {k:'c',t:'Siklus hidup pengembangan sistem (SDLC)',nodes:['SDLC','Waterfall','Agile'],lang:'text',run:false,
   b:['<b>System Development Life Cycle (SDLC)</b> adalah tahapan membangun sistem: <b>perencanaan</b> (masalah dan tujuan), <b>analisis</b> (kebutuhan pengguna), <b>perancangan</b> (database, alur, tampilan), <b>implementasi</b> (membangun, menguji, memindahkan data, melatih pengguna), dan <b>pemeliharaan</b>.',
      'Metode <b>waterfall</b> menjalankan tahapan berurutan dan cocok bila kebutuhan sudah jelas dan jarang berubah, misalnya sistem penggajian yang mengikuti aturan tetap. Metode <b>agile</b> (misalnya Scrum) membangun sedikit demi sedikit dalam <b>sprint</b> 1 sampai 4 minggu, lalu meminta masukan pengguna, sehingga cocok untuk kebutuhan yang terus berubah seperti produk startup.',
      'Saat sistem baru siap, ada beberapa cara <b>konversi</b>: langsung (sistem lama dimatikan hari itu), paralel (keduanya jalan bersama sementara), bertahap (per modul), atau pilot (satu cabang dulu). Paralel paling aman tetapi paling mahal.'],
   code:`Contoh penerapan: memilih metode

Sistem penggajian perusahaan  → waterfall
  aturan pajak & BPJS jelas, salah hitung berisiko tinggi

Aplikasi startup pesan katering → agile (sprint 2 minggu)
  sprint 1: pesan & bayar  → uji ke 20 pelanggan
  sprint 2: langganan mingguan berdasarkan masukan

E-rapor sekolah → pilot
  dipakai kelas X dulu satu semester, baru seluruh sekolah

Sistem iuran organisasi alumni → paralel 2 bulan
  catatan Excel lama tetap jalan sampai angka cocok`,
   pts:['SDLC: perencanaan, analisis, perancangan, implementasi, pemeliharaan.','Waterfall untuk kebutuhan stabil; agile untuk kebutuhan yang berubah.','Konversi: langsung, paralel, bertahap, pilot.'],
   q:[['Startup belum yakin fitur apa yang paling dibutuhkan pelanggan. Metode paling cocok?',['Agile','Waterfall murni','Tidak perlu metode'],0,'Agile memberi masukan pengguna di setiap sprint.'],
      ['Sekolah mencoba e-rapor di kelas X dulu sebelum seluruh sekolah. Cara konversi ini disebut?',['Pilot','Langsung','Paralel'],0,'Diuji di satu bagian kecil terlebih dahulu.']]},
  {k:'c',t:'Menggali kebutuhan dan memodelkan proses',nodes:['Requirements','DFD','Flowchart','Use Case','BPMN'],lang:'text',run:false,
   b:['Kebutuhan dikumpulkan lewat <b>wawancara</b>, <b>observasi</b> (melihat langsung cara kerja), <b>kuesioner</b>, dan mempelajari <b>dokumen</b> seperti formulir dan laporan lama. Bedakan <b>kebutuhan fungsional</b> (sistem harus bisa mencetak kuitansi) dan <b>non-fungsional</b> (halaman terbuka di bawah 3 detik, data dicadangkan harian).',
      'Proses digambarkan dengan diagram. <b>Flowchart</b> menunjukkan langkah dan keputusan. <b>Data Flow Diagram (DFD)</b> menunjukkan aliran data antara pihak luar, proses, dan penyimpanan. <b>Use case diagram</b> menunjukkan siapa (aktor) bisa melakukan apa di sistem. <b>BPMN</b> sering dipakai perusahaan untuk proses bisnis lintas bagian.',
      'Jebakan umum: langsung mendigitalkan proses lama yang berbelit. Sebelum membuat aplikasi, tanyakan "langkah mana yang bisa dihapus?". Mengotomatiskan proses yang buruk hanya membuat kesalahan terjadi lebih cepat.'],
   code:`Contoh penerapan: izin tidak masuk sekolah

Proses lama (flowchart)
orang tua tulis surat → siswa bawa ke wali kelas → wali kelas
catat di buku → TU rekap akhir bulan → BK baru tahu 3 minggu kemudian

Use case sistem baru
Aktor Orang tua : ajukan izin + foto surat dokter
Aktor Wali kelas: setujui/tolak izin
Aktor BK        : lihat siswa dengan izin > 3 kali sebulan
Aktor TU        : unduh rekap kehadiran

Kebutuhan non-fungsional: bisa dibuka dari ponsel Android murah,
notifikasi lewat WhatsApp, data siswa hanya bisa dilihat pihak berwenang`,
   pts:['Teknik: wawancara, observasi, kuesioner, studi dokumen.','Fungsional = apa yang dilakukan; non-fungsional = seberapa baik.','Flowchart, DFD, use case, BPMN untuk memodelkan proses.','Sederhanakan proses sebelum mendigitalkannya.'],
   q:[['"Halaman harus terbuka di bawah 3 detik" termasuk kebutuhan?',['Non-fungsional','Fungsional','Strategis'],0,'Mengatur kualitas, bukan fungsi.'],
      ['Diagram yang menunjukkan aktor dan apa yang bisa mereka lakukan di sistem adalah?',['Use case diagram','Flowchart','Struk kasir'],0,'Use case menggambarkan interaksi aktor dengan sistem.']]},
  {k:'c',t:'Studi kelayakan dan biaya-manfaat',nodes:['Feasibility Study','TELOS','Cost Benefit','ROI'],lang:'text',run:false,
   b:['Sebelum membangun, nilai kelayakan proyek. Kerangka populer <b>TELOS</b>: <b>Technical</b> (teknologinya tersedia dan dikuasai?), <b>Economic</b> (manfaat lebih besar dari biaya?), <b>Legal</b> (sesuai aturan, termasuk perlindungan data pribadi?), <b>Operational</b> (pengguna mau dan mampu memakainya?), dan <b>Schedule</b> (selesai tepat waktu?).',
      'Analisis biaya-manfaat membandingkan biaya (lisensi, pengembangan, perangkat, pelatihan, pemeliharaan tahunan) dengan manfaat. Manfaat <b>berwujud</b> bisa dihitung: jam kerja yang dihemat, kesalahan yang berkurang. Manfaat <b>tidak berwujud</b> sulit dihitung tetapi penting: kepuasan pelanggan, citra sekolah.',
      'Ukuran sederhana: <b>ROI</b> = (manfaat − biaya) ÷ biaya, dan <b>payback period</b> = berapa lama sampai biaya kembali. Jangan lupa <b>total cost of ownership</b>: biaya bertahun-tahun setelah sistem jadi sering lebih besar dari biaya membuatnya.'],
   code:`Contoh penerapan: aplikasi kasir untuk 5 cabang toko bangunan

Biaya tahun 1
  langganan POS cloud 5 cabang x Rp 300.000 x 12   = Rp 18.000.000
  perangkat (tablet, printer, scanner)              = Rp 25.000.000
  pelatihan & migrasi data                          = Rp  7.000.000
  total                                             = Rp 50.000.000
Manfaat per tahun (perkiraan)
  selisih stok/kehilangan turun                     = Rp 36.000.000
  jam lembur rekap berkurang                        = Rp 18.000.000
  total                                             = Rp 54.000.000
ROI tahun 1 = (54 − 50) / 50 = 8%   payback ≈ 11 bulan
Tahun 2 biaya hanya langganan Rp 18 jt → ROI jauh lebih tinggi`,
   pts:['TELOS: teknis, ekonomi, legal, operasional, jadwal.','Manfaat berwujud dan tidak berwujud sama-sama dicatat.','ROI dan payback period; hitung total cost of ownership.'],
   q:[['Pegawai tidak mau memakai sistem baru karena merasa diawasi. Aspek kelayakan apa yang bermasalah?',['Operasional','Teknis','Jadwal'],0,'Kelayakan operasional menilai penerimaan pengguna.'],
      ['Biaya Rp 40 juta, manfaat Rp 50 juta. ROI-nya?',['25%','10%','125%'],0,'(50 − 40) ÷ 40 = 0,25.']]}
 ]},
{t:'Infrastruktur, cloud, dan keamanan',lvl:'Menengah',d:'Jaringan dan cloud, prinsip keamanan informasi, perlindungan data pribadi, dan kelangsungan bisnis.',
 nodes:['Network','Cloud Computing','SaaS','Information Security','CIA Triad','Data Privacy','Backup','Business Continuity'],
 lessons:[
  {k:'c',t:'Jaringan dan cloud computing',nodes:['Network','Cloud Computing','SaaS','PaaS','IaaS'],lang:'text',run:false,
   b:['Sistem informasi modern hampir selalu terhubung jaringan: <b>LAN</b> di dalam gedung, <b>internet</b> antarcabang, dan koneksi seluler untuk aplikasi di lapangan. Kualitas jaringan menentukan apakah sistem bisa dipakai di daerah dengan sinyal lemah, jadi pertimbangkan mode <b>offline</b> lalu sinkron saat tersambung.',
      '<b>Cloud computing</b> berarti menyewa sumber daya komputasi lewat internet. <b>SaaS</b> (software as a service) memakai aplikasi jadi seperti Google Workspace atau aplikasi akuntansi online. <b>PaaS</b> menyediakan platform untuk menjalankan aplikasi buatan sendiri. <b>IaaS</b> menyewakan server virtual dan penyimpanan.',
      'Keuntungan cloud: tanpa beli server di awal, mudah diperbesar, dan dicadangkan penyedia. Risikonya: biaya langganan terus berjalan, ketergantungan pada penyedia (<b>vendor lock-in</b>), dan aturan lokasi penyimpanan data. Pilihan <b>on-premise</b> (server sendiri) masih dipakai untuk data sangat sensitif atau koneksi internet yang tidak andal.'],
   code:`Contoh penerapan: memilih model

Startup 6 orang     → SaaS semua: email, dokumen, CRM, akuntansi online
                      + PaaS untuk menjalankan aplikasi produknya
Perusahaan manufaktur → ERP di IaaS/cloud privat + mesin pabrik on-premise
Sekolah             → SaaS: LMS (Google Classroom/Moodle cloud), e-rapor
                      + Wi-Fi sekolah dengan pembatasan situs
Organisasi relawan  → SaaS gratis/nirlaba: formulir online, spreadsheet bersama,
                      grup chat; data donatur di aplikasi dengan hak akses

Pertanyaan sebelum berlangganan:
- data disimpan di negara mana?   - bisa ekspor data kalau pindah?
- biaya naik kalau pengguna bertambah?`,
   pts:['Jaringan: LAN, internet, seluler; pertimbangkan mode offline.','SaaS = aplikasi jadi; PaaS = platform; IaaS = server sewaan.','Cloud: hemat modal awal, mudah diperbesar; risiko lock-in dan biaya berjalan.'],
   q:[['Sekolah memakai aplikasi LMS online tanpa mengelola servernya. Ini model?',['SaaS','IaaS','On-premise'],0,'Aplikasi jadi yang dipakai lewat internet.'],
      ['Sulitnya pindah penyedia karena data tidak bisa diekspor disebut?',['Vendor lock-in','Backup','Bandwidth'],0,'Ketergantungan pada satu penyedia.']]},
  {k:'c',t:'Keamanan informasi',nodes:['Information Security','CIA Triad','Access Control','Phishing'],lang:'text',run:false,
   b:['Keamanan informasi menjaga tiga hal yang dikenal sebagai <b>CIA triad</b>: <b>Confidentiality</b> (hanya orang berwenang yang bisa melihat), <b>Integrity</b> (data tidak diubah sembarangan), dan <b>Availability</b> (sistem bisa dipakai saat dibutuhkan).',
      'Ancaman paling umum justru bukan peretas canggih, melainkan <b>phishing</b> (pesan palsu yang memancing kata sandi atau kode OTP), kata sandi lemah atau dipakai bersama, perangkat hilang, dan <b>ransomware</b> yang mengunci file lalu meminta tebusan.',
      'Kontrol dasar yang murah tetapi efektif: <b>autentikasi dua faktor</b>, prinsip <b>hak akses minimum</b> (least privilege), pembaruan perangkat lunak, cadangan rutin yang disimpan terpisah, <b>log aktivitas</b>, dan pelatihan kesadaran keamanan untuk semua pengguna, bukan hanya tim IT.'],
   code:`Contoh penerapan: kontrol akses berdasarkan peran

Peran            Lihat nilai   Ubah nilai     Lihat data keuangan
Siswa            miliknya      -              tagihan miliknya
Guru mapel       kelasnya      mapelnya       -
Wali kelas       kelasnya      -              tunggakan kelasnya
Bendahara        -             -              semua
Kepala sekolah   semua         -              semua (hanya baca)

Startup  : developer tidak punya akses data produksi pelanggan
Kantor   : akun karyawan yang resign dinonaktifkan di hari terakhir
Organisasi: kata sandi akun media sosial disimpan di password manager,
            bukan di grup chat`,
   pts:['CIA: kerahasiaan, integritas, ketersediaan.','Ancaman umum: phishing, kata sandi lemah, perangkat hilang, ransomware.','Kontrol dasar: 2FA, hak akses minimum, update, backup, log, pelatihan.'],
   q:[['Nilai siswa diubah oleh orang tak berwenang. Aspek CIA apa yang dilanggar?',['Integrity','Availability','Confidentiality saja'],0,'Integritas berarti data tidak diubah sembarangan.'],
      ['Guru hanya bisa mengubah nilai mapel yang ia ajar. Ini penerapan?',['Hak akses minimum (least privilege)','Phishing','Vendor lock-in'],0,'Setiap peran hanya mendapat akses yang dibutuhkan.']]},
  {k:'c',t:'Perlindungan data pribadi dan kelangsungan bisnis',nodes:['Data Privacy','UU PDP','Backup','Business Continuity','Disaster Recovery'],lang:'text',run:false,
   b:['Di Indonesia, <b>UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)</b> mengatur pengumpulan dan pemrosesan data pribadi. Prinsipnya: kumpulkan seperlunya, jelaskan tujuannya, minta persetujuan yang jelas, jaga keamanannya, dan hormati hak pemilik data untuk mengakses, memperbaiki, atau meminta penghapusan.',
      'Data siswa, nasabah, pasien, dan donatur termasuk data pribadi. Data seperti kesehatan, keuangan, dan data anak termasuk kategori yang butuh perlindungan lebih ketat. Bila terjadi kebocoran, organisasi wajib memberi tahu pihak terdampak dalam batas waktu yang diatur.',
      '<b>Business continuity plan (BCP)</b> menyiapkan cara organisasi tetap berjalan saat terjadi gangguan: listrik padam, banjir, server rusak. Bagiannya, <b>disaster recovery plan</b>, mengatur pemulihan sistem. Aturan cadangan yang populer adalah <b>3-2-1</b>: 3 salinan data, di 2 jenis media, 1 di lokasi berbeda. Cadangan yang tidak pernah diuji pemulihannya belum bisa dipercaya.'],
   code:`Contoh penerapan: daftar periksa data pribadi

Formulir pendaftaran relawan (organisasi)
[x] hanya minta nama, nomor HP, domisili, hari tersedia
[ ] tidak minta foto KTP kalau tidak perlu
[x] tulis tujuan: "untuk menghubungi jadwal kegiatan"
[x] spreadsheet hanya bisa dibuka 2 pengurus

Rencana cadangan sekolah (aturan 3-2-1)
1. database e-rapor di server/cloud utama
2. salinan harian ke penyimpanan cloud kedua
3. salinan mingguan ke hard disk eksternal di brankas TU
Uji pulih setiap awal semester: berapa jam sampai data kembali?`,
   pts:['UU PDP (UU 27/2022): kumpulkan seperlunya, jelaskan tujuan, minta persetujuan, jaga keamanan.','Data anak, kesehatan, dan keuangan butuh perlindungan lebih ketat.','BCP dan disaster recovery menjaga organisasi tetap berjalan.','Cadangan 3-2-1 dan uji pemulihan secara berkala.'],
   q:[['Formulir relawan meminta foto KTP padahal tidak dipakai. Prinsip apa yang dilanggar?',['Minimisasi data (kumpulkan seperlunya)','Ketersediaan','Normalisasi'],0,'Data pribadi dikumpulkan sebatas tujuan.'],
      ['Aturan cadangan 3-2-1 berarti?',['3 salinan, 2 jenis media, 1 di lokasi berbeda','3 server, 2 admin, 1 password','Cadangan tiap 3 hari'],0,'Mengurangi risiko semua salinan hilang bersamaan.']]}
 ]},
{t:'Strategi dan tata kelola TI',lvl:'Lanjutan',d:'SI sebagai keunggulan bersaing, transformasi digital, KPI, tata kelola, dan manajemen proyek SI.',
 nodes:['Competitive Advantage','Porter Five Forces','Digital Transformation','KPI','Balanced Scorecard','IT Governance','COBIT','ITIL','Project Management'],
 lessons:[
  {k:'c',t:'SI untuk keunggulan bersaing',nodes:['Competitive Advantage','Porter Five Forces','Value Chain'],lang:'text',run:false,
   b:['Michael Porter menjelaskan <b>lima kekuatan</b> persaingan: pesaing yang ada, ancaman pendatang baru, ancaman produk pengganti, daya tawar pemasok, dan daya tawar pelanggan. Sistem informasi bisa memperkuat posisi menghadapi kelimanya, misalnya program loyalitas digital yang membuat pelanggan enggan pindah.',
      'Empat strategi umum: <b>keunggulan biaya</b> (operasi lebih efisien), <b>diferensiasi</b> (layanan yang beda), <b>fokus</b> pada ceruk pasar, dan <b>keintiman pelanggan</b> (mengenal pelanggan sangat baik). <b>Rantai nilai</b> (value chain) membantu menemukan kegiatan mana yang paling diuntungkan oleh SI.',
      'Keunggulan dari teknologi saja cepat ditiru. Yang sulit ditiru adalah gabungan data yang terkumpul bertahun-tahun, proses kerja yang matang, dan budaya organisasi yang memakai data dalam keputusan.'],
   code:`Contoh penerapan: strategi bersaing dengan SI

Perusahaan ritel   keunggulan biaya   : prediksi stok mengurangi barang kedaluwarsa
Startup logistik   diferensiasi       : lacak paket real time + estimasi tiba akurat
Sekolah swasta     keintiman pelanggan: portal orang tua, laporan perkembangan mingguan
Koperasi           fokus              : aplikasi simpan pinjam khusus petani anggota

Lima kekuatan, contoh toko online kecil:
pendatang baru   → mudah (buka toko di marketplace)
pengganti        → belanja langsung di pasar
daya tawar pembeli → tinggi (banding harga dalam 1 menit)
Respons SI: data pelanggan + rekomendasi produk + layanan purnajual cepat`,
   pts:['Lima kekuatan Porter memetakan tekanan persaingan.','Strategi: biaya, diferensiasi, fokus, keintiman pelanggan.','Keunggulan bertahan datang dari data, proses, dan budaya, bukan alat saja.'],
   q:[['Portal orang tua dengan laporan perkembangan anak mingguan mendukung strategi?',['Keintiman pelanggan/diferensiasi','Keunggulan biaya saja','Tidak terkait strategi'],0,'Layanan yang membuat orang tua merasa dikenal dan diperhatikan.'],
      ['Kenapa keunggulan dari teknologi saja tidak bertahan lama?',['Teknologi mudah dibeli dan ditiru pesaing','Teknologi selalu mahal','Teknologi dilarang'],0,'Yang sulit ditiru adalah data, proses, dan budaya.']]},
  {k:'c',t:'Transformasi digital, KPI, dan balanced scorecard',nodes:['Digital Transformation','KPI','Balanced Scorecard','OKR'],lang:'text',run:false,
   b:['Ada tiga tingkat perubahan: <b>digitisasi</b> (formulir kertas menjadi file), <b>digitalisasi</b> (proses dijalankan lewat sistem, misalnya pengajuan cuti online), dan <b>transformasi digital</b> (cara organisasi menciptakan nilai berubah, misalnya toko fisik menjadi layanan pesan antar berbasis data).',
      'Kemajuan diukur dengan <b>KPI</b> (key performance indicator) yang spesifik, terukur, dan punya target serta tenggat. <b>Balanced scorecard</b> menyeimbangkan empat perspektif: <b>keuangan</b>, <b>pelanggan</b>, <b>proses internal</b>, serta <b>pembelajaran & pertumbuhan</b>. Banyak startup memakai <b>OKR</b> (objective & key results) untuk target per kuartal.',
      'Transformasi digital gagal bila hanya dipimpin tim IT. Pimpinan harus memberi contoh, proses harus dirancang ulang, dan pegawai perlu dilatih serta dilibatkan sejak awal.'],
   code:`Contoh penerapan: balanced scorecard sekolah

Perspektif          KPI                                Target 2026
Keuangan            tunggakan SPP > 2 bulan            < 5% siswa
Pelanggan           kepuasan orang tua (survei)        ≥ 4,2 dari 5
Proses internal     rapor terbit tepat waktu           100% kelas
Pembelajaran        guru ikut pelatihan digital        ≥ 80% guru

OKR startup (kuartal ini)
Objective : pelanggan bisnis puas dan bertahan
KR1       : retensi bulan ke-3 naik dari 45% ke 60%
KR2       : waktu respons tiket rata-rata < 2 jam
KR3       : 30 testimoni pelanggan baru`,
   pts:['Digitisasi → digitalisasi → transformasi digital.','KPI spesifik, terukur, ada target dan tenggat.','Balanced scorecard: keuangan, pelanggan, proses internal, pembelajaran.','Transformasi butuh pimpinan, proses baru, dan pelatihan.'],
   q:[['Formulir cuti kertas di-scan menjadi PDF. Ini tingkat?',['Digitisasi','Transformasi digital','Diferensiasi'],0,'Hanya mengubah bentuk informasi menjadi digital.'],
      ['"Guru ikut pelatihan digital ≥ 80%" berada di perspektif balanced scorecard?',['Pembelajaran & pertumbuhan','Keuangan','Pelanggan'],0,'Mengukur kemampuan orang dalam organisasi.']]},
  {k:'c',t:'Tata kelola TI dan manajemen proyek SI',nodes:['IT Governance','COBIT','ITIL','Project Management','Change Management'],lang:'text',run:false,
   b:['<b>Tata kelola TI</b> (IT governance) memastikan investasi TI selaras dengan tujuan organisasi, risikonya dikelola, dan hasilnya terukur. Kerangka yang banyak dipakai: <b>COBIT</b> untuk tata kelola dan kontrol, <b>ITIL</b> untuk pengelolaan layanan TI (helpdesk, penanganan insiden, perubahan), dan <b>ISO/IEC 27001</b> untuk sistem manajemen keamanan informasi. Instansi pemerintah di Indonesia mengikuti kebijakan <b>SPBE</b> (Sistem Pemerintahan Berbasis Elektronik).',
      'Proyek SI dikelola dengan memperhatikan <b>ruang lingkup, waktu, biaya, dan kualitas</b>. Menambah fitur di tengah jalan tanpa mengubah jadwal atau anggaran (<b>scope creep</b>) adalah penyebab klasik proyek terlambat.',
      '<b>Manajemen perubahan</b> sama pentingnya dengan teknologi: jelaskan alasan perubahan, libatkan perwakilan pengguna, sediakan pelatihan dan pendamping, lalu rayakan keberhasilan awal. Pengguna yang merasa dipaksa akan kembali ke cara lama.'],
   code:`Contoh penerapan: piagam proyek sistem keanggotaan organisasi

Tujuan      : data 1.200 anggota rapi, iuran tercatat, laporan otomatis
Lingkup     : pendaftaran, iuran, kartu anggota digital
Bukan lingkup: aplikasi donasi, forum diskusi (fase 2)
Jadwal      : 3 bulan, uji coba di 1 cabang bulan ke-2
Anggaran    : Rp 35 juta + langganan Rp 500 ribu/bulan
Risiko      : pengurus cabang belum terbiasa → pelatihan 2 sesi + video
Ukuran sukses: 90% anggota terdata, laporan iuran keluar tanggal 5

Helpdesk ala ITIL di perusahaan:
insiden "printer kasir mati" → tiket → prioritas → selesai < 4 jam`,
   pts:['Tata kelola TI: selaras tujuan, risiko dikelola, hasil terukur.','Kerangka: COBIT, ITIL, ISO/IEC 27001; pemerintah: SPBE.','Proyek: lingkup, waktu, biaya, kualitas; waspadai scope creep.','Manajemen perubahan menentukan apakah sistem benar-benar dipakai.'],
   q:[['Di tengah proyek, pimpinan minta tambah fitur donasi tanpa menambah waktu dan biaya. Ini disebut?',['Scope creep','Backup','Normalisasi'],0,'Lingkup membengkak tanpa penyesuaian rencana.'],
      ['Kerangka yang fokus pada pengelolaan layanan TI seperti helpdesk dan insiden adalah?',['ITIL','ERD','Porter'],0,'ITIL adalah praktik manajemen layanan TI.']]}
 ]},
{t:'Penerapan MSI: studi kasus',lvl:'Lanjutan',d:'Contoh lengkap cara mengelola sistem informasi di perusahaan, startup, sekolah, dan organisasi.',
 nodes:['Case Study','Enterprise','Startup','School','Organization'],
 lessons:[
  {k:'c',t:'Di perusahaan: distributor dengan ERP',nodes:['Case Study','Enterprise','ERP'],lang:'text',run:false,
   b:['<b>PT Sumber Pangan Nusantara</b> (fiktif) mendistribusikan bahan makanan ke 600 toko di Sumatra Utara. Dulu pesanan dicatat sales di buku, stok di Excel gudang, dan faktur dibuat manual. Akibatnya: barang sering dijanjikan padahal habis, piutang macet tidak terpantau, dan laporan keuangan baru selesai tanggal 20 bulan berikutnya.',
      'Solusinya bertahap. <b>Tahap 1</b>: ERP untuk penjualan, persediaan, dan keuangan dalam satu database. <b>Tahap 2</b>: aplikasi sales di ponsel (pesanan langsung masuk ERP, cek stok di tempat). <b>Tahap 3</b>: dashboard BI untuk direksi dan DSS untuk menentukan stok minimum per gudang.',
      'Kunci keberhasilannya bukan aplikasinya, melainkan pembenahan proses (satu kode barang untuk semua gudang), pembersihan data pelanggan lama, uji coba di satu gudang, dan pelatihan sales yang sebelumnya terbiasa mencatat di buku.'],
   code:`Studi kasus perusahaan: sebelum vs sesudah (12 bulan)

Masalah                   Sistem                        Indikator
pesanan barang habis      ERP + stok real time di HP    pesanan gagal 9% → 2%
piutang macet             ERP piutang + peringatan      piutang > 60 hari turun 40%
laporan bulanan lambat    jurnal otomatis dari ERP      tutup buku tgl 20 → tgl 5
stok menumpuk             DSS stok minimum per gudang   nilai stok turun 15%

Jenis SI yang terlibat:
TPS (pesanan, faktur) → MIS (laporan cabang) → DSS (stok) → EIS (dashboard direksi)

Catatan: angka adalah ilustrasi untuk latihan, bukan data perusahaan nyata.`,
   pts:['Masalah awal: data tersebar, laporan lambat, stok tidak akurat.','Penerapan bertahap: ERP inti → aplikasi sales → BI/DSS.','Pembenahan proses, data, dan pelatihan menentukan hasil.'],
   q:[['Kenapa tahap pertama adalah ERP inti, bukan dashboard direksi?',['Dashboard butuh data transaksi yang benar lebih dulu','Dashboard lebih mahal','Direksi tidak butuh informasi'],0,'TPS/ERP adalah fondasi data untuk sistem di atasnya.'],
      ['Satu kode barang untuk semua gudang adalah contoh?',['Pembenahan proses dan standardisasi data','Phishing','Scope creep'],0,'Data yang seragam membuat integrasi berhasil.']]},
  {k:'c',t:'Di startup: dari spreadsheet ke sistem yang tumbuh',nodes:['Case Study','Startup','SaaS','Metrics'],lang:'text',run:false,
   b:['<b>Dapur Sehat</b> (fiktif) adalah startup katering sehat langganan di Jakarta. Di awal, 3 pendiri mengelola semuanya dengan formulir online, spreadsheet, dan grup WhatsApp. Ini wajar: di tahap awal, kecepatan mencoba ide lebih penting dari sistem yang rapi.',
      'Saat pelanggan mencapai 800 orang, masalah muncul: pesanan terlewat, tagihan salah, dan tidak ada yang tahu berapa pelanggan yang berhenti. Mereka memilih <b>SaaS</b> dulu (pembayaran online, CRM, akuntansi), lalu membangun aplikasi pemesanan sendiri karena alur langganannya unik.',
      'Startup hidup dari metrik: <b>CAC</b> (biaya mendapatkan satu pelanggan), <b>LTV</b> (nilai pelanggan selama berlangganan), <b>churn</b> (persentase pelanggan berhenti), dan <b>burn rate/runway</b> (berapa bulan uang cukup). Sistem informasinya dirancang agar angka-angka ini bisa dilihat setiap minggu.'],
   code:`Studi kasus startup: tumbuh bertahap

Tahap          Pelanggan  Sistem
Validasi ide   0–100      formulir online + spreadsheet + WhatsApp
Mulai tumbuh   100–1.000  SaaS: payment gateway, CRM, akuntansi online
Skala          1.000+     aplikasi pesan sendiri + data warehouse + dashboard

Dashboard mingguan pendiri
pelanggan aktif   : 1.240
churn bulanan     : 6,5%  (target < 5%)
CAC               : Rp 85.000
LTV (rata-rata)   : Rp 1.150.000   → LTV/CAC ≈ 13,5
runway            : 14 bulan

Prinsip: jangan membangun sendiri yang bisa disewa,
bangun sendiri hanya yang menjadi pembeda bisnis.`,
   pts:['Tahap awal: alat sederhana, fokus validasi ide.','Saat tumbuh: SaaS dulu, bangun sendiri hanya bagian pembeda.','Metrik utama: CAC, LTV, churn, burn rate/runway.'],
   q:[['Persentase pelanggan yang berhenti berlangganan disebut?',['Churn','CAC','Runway'],0,'Churn mengukur pelanggan yang hilang.'],
      ['Kenapa Dapur Sehat membangun aplikasi pemesanan sendiri tapi menyewa akuntansi?',['Alur langganan adalah pembeda bisnisnya; akuntansi bersifat umum','Akuntansi dilarang dibangun','Aplikasi sendiri selalu lebih murah'],0,'Bangun sendiri hanya yang menjadi pembeda.']]},
  {k:'c',t:'Di sekolah: sistem informasi akademik terpadu',nodes:['Case Study','School','Academic Information System'],lang:'text',run:false,
   b:['<b>SMA Harapan Bangsa</b> (fiktif) dengan 960 siswa punya data yang tersebar: PPDB di formulir online, nilai di file Excel tiap guru, presensi di buku, dan pembayaran SPP di buku kas bendahara. Sekolah juga wajib melaporkan data ke <b>Dapodik</b> (Data Pokok Pendidikan milik Kemendikdasmen).',
      'Sekolah membangun <b>Sistem Informasi Akademik (SIAKAD)</b> terpadu: modul PPDB, data induk siswa, jadwal, presensi berbasis kartu/QR, penilaian dan e-rapor, keuangan SPP, serta portal orang tua. Data induk diselaraskan dengan Dapodik agar tidak diketik dua kali.',
      'Tantangan terbesar adalah manusia: guru senior yang belum terbiasa, orang tua yang belum punya aplikasi, dan jaringan yang lemah. Solusinya pelatihan bertahap dengan guru pendamping, akses lewat browser ponsel, dan notifikasi WhatsApp untuk orang tua.'],
   code:`Studi kasus sekolah: modul SIAKAD dan penggunanya

Modul              Pengguna            Informasi yang dihasilkan
PPDB               calon siswa, panitia jumlah pendaftar per jalur
Data induk         TU                  data siswa sinkron dengan Dapodik
Presensi QR        siswa, wali kelas   siswa alpa > 3 hari → notifikasi BK
Penilaian/e-rapor  guru, wali kelas    rapor terbit tepat waktu
Keuangan           bendahara, ortu     tunggakan SPP per kelas
Portal orang tua   orang tua           nilai, kehadiran, tagihan anak
Dashboard          kepala sekolah      kehadiran, nilai, keuangan dalam 1 layar

Data pribadi anak → hak akses ketat, persetujuan orang tua, sesuai UU PDP`,
   pts:['Masalah: data akademik, presensi, dan keuangan tersebar.','SIAKAD terpadu + sinkron dengan Dapodik menghindari input ganda.','Kunci: pelatihan bertahap, akses dari ponsel, notifikasi ke orang tua.','Data anak harus dilindungi ketat.'],
   q:[['Kenapa data induk siswa diselaraskan dengan Dapodik?',['Agar data tidak diketik dua kali dan tetap konsisten','Agar siswa bisa bermain gim','Karena Dapodik adalah aplikasi kasir'],0,'Integrasi mencegah input ganda dan data berbeda.'],
      ['Notifikasi otomatis ke BK saat siswa alpa > 3 hari adalah contoh?',['Laporan pengecualian (exception report) dari MIS','TPS pembayaran','Vendor lock-in'],0,'Sistem hanya melapor saat ada kondisi yang perlu ditindaklanjuti.']]},
  {k:'c',t:'Di organisasi: koperasi, yayasan, dan organisasi mahasiswa',nodes:['Case Study','Organization','Nonprofit','Cooperative'],lang:'text',run:false,
   b:['Organisasi nirlaba dan kemasyarakatan juga perlu mengelola sistem informasinya, sering dengan anggaran kecil dan pengurus yang berganti. <b>Koperasi Tani Makmur</b> (fiktif) memakai aplikasi simpan pinjam agar setiap anggota bisa melihat saldo simpanan dan sisa pinjamannya, dan laporan Rapat Anggota Tahunan (RAT) dibuat dari data, bukan rekap manual.',
      '<b>Yayasan Peduli Pendidikan</b> (fiktif) mengelola donasi beasiswa. Sistemnya mencatat donatur, dana masuk, penerima beasiswa, dan laporan penyaluran. <b>Transparansi</b> adalah produk utamanya: donatur mendapat laporan ke mana dananya disalurkan.',
      'Organisasi mahasiswa atau OSIS punya tantangan khusus: pengurus berganti setiap tahun sehingga pengetahuan mudah hilang. Simpan data dan dokumen di akun milik organisasi (bukan akun pribadi ketua), buat <b>SOP</b> serah terima, dan pakai alat gratis yang sederhana agar pengurus baru cepat paham.'],
   code:`Studi kasus organisasi

Koperasi Tani Makmur
  anggota  : cek saldo simpanan & angsuran di aplikasi
  pengurus : laporan SHU dan RAT langsung dari data transaksi
  manfaat  : kepercayaan anggota naik, rekap RAT dari 3 minggu → 2 hari

Yayasan Peduli Pendidikan
  data     : donatur, donasi, penerima, penyaluran, bukti transfer
  laporan  : "Donasi Anda Rp 2.000.000 membiayai 4 siswa selama 6 bulan"
  kontrol  : dua orang menyetujui setiap penyaluran (pemisahan tugas)

BEM / OSIS
  akun organisasi (email, drive, media sosial) bukan akun pribadi
  folder: /SK  /Proposal  /LPJ  /Anggota  /Aset
  SOP serah terima: daftar akun, kata sandi di password manager, saldo kas`,
   pts:['Organisasi butuh sistem informasi sederhana, murah, dan mudah diwariskan.','Koperasi: transparansi simpanan, pinjaman, dan laporan RAT.','Yayasan: transparansi donasi dan pemisahan tugas.','OSIS/BEM: akun milik organisasi dan SOP serah terima.'],
   q:[['Kenapa akun media sosial organisasi tidak boleh memakai email pribadi ketua?',['Akses bisa hilang saat ketua berganti','Email pribadi tidak bisa dipakai login','Supaya lebih cepat'],0,'Aset digital harus milik organisasi agar bisa diwariskan.'],
      ['Setiap penyaluran dana disetujui dua orang berbeda. Kontrol ini disebut?',['Pemisahan tugas','Normalisasi','Agile'],0,'Mengurangi risiko kesalahan dan penyalahgunaan dana.']]}
 ]},
{t:'Tren, etika, dan karier',lvl:'Lanjutan',d:'AI dan analitik, e-business dan e-government, etika SI, serta peran profesi sistem informasi.',
 nodes:['AI & Analytics','E-business','E-government','IT Ethics','Careers'],
 lessons:[
  {k:'c',t:'AI, analitik, dan otomatisasi',nodes:['AI & Analytics','Automation','RPA'],lang:'text',run:false,
   b:['Analitik berkembang dari <b>deskriptif</b> (apa yang terjadi?), <b>diagnostik</b> (kenapa?), <b>prediktif</b> (apa yang mungkin terjadi?), sampai <b>preskriptif</b> (apa yang sebaiknya dilakukan?). Model machine learning dipakai untuk memprediksi permintaan, mendeteksi transaksi mencurigakan, atau siswa yang berisiko tertinggal.',
      '<b>AI generatif</b> membantu menulis draf surat, merangkum rapat, dan menjawab pertanyaan pelanggan. <b>Otomatisasi proses</b> (RPA dan alur kerja otomatis) mengerjakan tugas berulang seperti memindahkan data antar sistem atau mengirim pengingat tagihan.',
      'Gunakan dengan hati-hati: AI bisa salah dengan percaya diri, model bisa bias bila data latihnya bias, dan data pribadi tidak boleh dimasukkan sembarangan ke layanan AI publik. Keputusan penting tentang orang (penerimaan siswa, kredit, rekrutmen) tetap butuh pengawasan manusia.'],
   code:`Contoh penerapan: empat tingkat analitik

            Deskriptif         Diagnostik           Prediktif               Preskriptif
Perusahaan  penjualan turun    karena stok kosong   minggu depan butuh 1.200 pesan 1.300 hari Senin
Startup     churn 6,5%         pengguna baru bingung siapa yang akan berhenti kirim panduan + diskon
Sekolah     nilai MTK turun    materi pecahan       12 siswa berisiko remedial kelas tambahan Sabtu
Organisasi  donasi turun       kampanye terlambat   Desember donasi naik    mulai kampanye November

Aturan pemakaian AI di organisasi:
- jangan masukkan data pribadi ke layanan AI publik
- periksa ulang angka dan kutipan
- keputusan tentang orang tetap diputuskan manusia`,
   pts:['Analitik: deskriptif, diagnostik, prediktif, preskriptif.','AI generatif dan otomatisasi mempercepat tugas berulang.','Risiko: salah, bias, kebocoran data; manusia tetap mengawasi keputusan penting.'],
   q:[['"12 siswa diperkirakan akan remedial" termasuk analitik?',['Prediktif','Deskriptif','Diagnostik'],0,'Memperkirakan apa yang mungkin terjadi.'],
      ['Mana pemakaian AI yang paling berisiko?',['Memasukkan data nilai dan alamat siswa ke chatbot publik','Merangkum notulen rapat tanpa data pribadi','Membuat draf pengumuman libur'],0,'Data pribadi anak bisa bocor.']]},
  {k:'c',t:'E-business, e-commerce, dan e-government',nodes:['E-business','E-commerce','E-government','SPBE'],lang:'text',run:false,
   b:['<b>E-business</b> adalah penggunaan internet dan SI untuk menjalankan seluruh proses bisnis, sedangkan <b>e-commerce</b> khusus untuk jual beli online. Modelnya: <b>B2C</b> (bisnis ke konsumen), <b>B2B</b> (antarbisnis, misalnya distributor ke toko), <b>C2C</b> (antarkonsumen lewat marketplace), dan <b>B2G</b> (bisnis ke pemerintah, misalnya pengadaan elektronik).',
      'Pembayaran digital seperti transfer virtual account, e-wallet, dan <b>QRIS</b> (standar kode QR pembayaran nasional dari Bank Indonesia) membuat usaha kecil pun bisa menerima pembayaran nontunai dan langsung tercatat.',
      '<b>E-government</b> memakai SI untuk layanan publik. Di Indonesia arahnya diatur dalam <b>SPBE</b> (Sistem Pemerintahan Berbasis Elektronik): layanan administrasi kependudukan, perizinan, pajak, dan pengadaan barang/jasa secara elektronik. Prinsipnya sama dengan organisasi lain: integrasi data, keamanan, dan kemudahan bagi warga.'],
   code:`Contoh penerapan

B2C  : toko roti menerima pesanan via website + bayar QRIS
B2B  : distributor menerima pesanan dari 600 toko lewat aplikasi
C2C  : alumni menjual buku bekas lewat marketplace
B2G  : penyedia laptop ikut tender pengadaan elektronik pemerintah

Sekolah     : pembayaran SPP via virtual account → otomatis tercatat lunas
Organisasi  : donasi via QRIS → dashboard dana masuk real time
Desa        : layanan surat keterangan online, warga tidak perlu antre`,
   pts:['E-business: seluruh proses; e-commerce: jual beli online.','Model: B2C, B2B, C2C, B2G.','QRIS dan virtual account membuat pembayaran tercatat otomatis.','E-government di Indonesia mengikuti arah SPBE.'],
   q:[['Distributor menerima pesanan dari toko-toko lewat aplikasi. Modelnya?',['B2B','C2C','B2C'],0,'Transaksi antarbisnis.'],
      ['Manfaat utama SPP lewat virtual account bagi bendahara sekolah?',['Pembayaran otomatis tercatat per siswa','Siswa tidak perlu belajar','Tidak perlu bank'],0,'Setiap siswa punya nomor tagihan unik sehingga mudah dicocokkan.']]},
  {k:'c',t:'Etika SI dan karier di bidang sistem informasi',nodes:['IT Ethics','Digital Divide','Careers','Business Analyst'],lang:'text',run:false,
   b:['Sistem informasi membawa pertanyaan etis: <b>privasi</b> (seberapa jauh boleh memantau karyawan atau siswa?), <b>akurasi</b> (siapa bertanggung jawab bila data salah merugikan orang?), <b>kepemilikan</b> (hak cipta perangkat lunak dan data), dan <b>akses</b> (kesenjangan digital antara yang punya perangkat dan internet dengan yang tidak).',
      'Rancang sistem yang adil: sediakan alternatif bagi yang tidak punya ponsel, jangan memakai data untuk tujuan di luar yang dijanjikan, dan beri jalan bagi orang untuk mengoreksi data tentang dirinya.',
      'Karier di bidang ini beragam: <b>business analyst/system analyst</b> (menjembatani kebutuhan bisnis dan tim teknis), <b>ERP consultant</b>, <b>data/BI analyst</b>, <b>IT project manager</b>, <b>IT auditor</b>, <b>product manager</b>, dan <b>spesialis keamanan informasi</b>. Kemampuan intinya: memahami proses bisnis, berkomunikasi, membaca data, dan dasar teknologi.'],
   code:`Contoh dilema etis

Perusahaan : memasang pelacak lokasi di ponsel sales 24 jam
             → batasi ke jam kerja, jelaskan tujuan, minta persetujuan
Sekolah    : CCTV kelas ditayangkan ke orang tua
             → privasi siswa lain; cukup laporan, bukan siaran
Startup    : menjual data pengguna ke pihak ketiga
             → melanggar janji & UU PDP tanpa dasar hukum yang sah
Organisasi : pengumuman bantuan hanya lewat aplikasi
             → warga tanpa ponsel tertinggal; sediakan jalur offline

Peta karier MSI
Business analyst · ERP consultant · BI analyst · IT project manager
IT auditor · Product manager · Information security analyst`,
   pts:['Isu etis: privasi, akurasi, kepemilikan, akses.','Sistem adil menyediakan alternatif dan hak koreksi data.','Karier: business analyst, ERP consultant, BI analyst, PM, auditor, keamanan.'],
   q:[['Pengumuman bantuan hanya lewat aplikasi membuat warga tanpa ponsel tertinggal. Isu etis apa?',['Akses (kesenjangan digital)','Kepemilikan','Akurasi'],0,'Tidak semua orang punya perangkat dan internet.'],
      ['Peran yang menjembatani kebutuhan bisnis dengan tim teknis adalah?',['Business analyst','Kasir','Desainer logo'],0,'Business analyst menerjemahkan kebutuhan menjadi spesifikasi.']]}
 ]},
{t:'Membangun dan memperbaiki aplikasi bersama UX Designer',lvl:'Lanjutan',d:'Peran MSI dan UX Designer, alur membuat aplikasi baru, dan alur mengubah aplikasi lama agar sesuai standar.',
 nodes:['MSI and UX','New App Flow','App Improvement Flow'],
 lessons:[
  {k:'c',t:'MSI dan UX Designer: siapa mengerjakan apa',nodes:['MSI and UX'],lang:'text',run:false,
   b:['Aplikasi yang sukses butuh dua sudut pandang. Pengelola sistem informasi (MSI) memastikan aplikasi <b>layak bagi organisasi</b>: sesuai strategi, anggarannya masuk akal, datanya aman, patuh aturan, dan bisa dirawat bertahun-tahun. <b>UX Designer</b> memastikan aplikasi <b>layak bagi penggunanya</b>: mudah dipahami, cepat dipakai, dan benar-benar menyelesaikan masalah mereka.',
      'Keduanya bertemu di titik yang sama: <b>kebutuhan</b>. Analis sistem menulis kebutuhan bisnis dan aturan data, UX Designer menggali kebutuhan pengguna lewat riset dan persona, lalu keduanya menyepakati prioritas. Tanpa MSI, desain yang indah bisa gagal karena biaya, keamanan, atau integrasi. Tanpa UX, sistem yang lengkap fiturnya bisa ditinggalkan karena membingungkan.',
      'Untuk mendalami sisi pengguna, ikuti jalur <a href="#ux">UX Design</a>, terutama modul <a href="#ux-5-1">Riset &amp; persona</a>, <a href="#ux-6-1">Prototyping</a>, dan <a href="#ux-7-1">Mengukur dampak</a>. Jalur karier <b>Analis Sistem Informasi</b> di beranda menggabungkan MSI, SQL, BI, dan UX dalam satu urutan.'],
   code:`Contoh penerapan: pembagian peran

                 MSI / analis sistem             UX Designer
Perusahaan   ROI aplikasi gudang, integrasi  alur scan barang yang cepat
             ke ERP, hak akses per gudang    untuk petugas bersarung tangan
Startup      biaya cloud, keamanan akun,     onboarding 3 langkah, uji 5
             kepatuhan UU PDP                pengguna sebelum rilis
Sekolah      anggaran, data siswa aman,      tampilan rapor yang dipahami
             integrasi Dapodik               orang tua lewat ponsel murah
Organisasi   siapa admin, biaya hosting,     formulir donasi yang singkat
             serah terima pengurus           dan bisa dipakai lansia`,
   pts:['MSI: layak bagi organisasi (strategi, biaya, data, keamanan, perawatan).','UX: layak bagi pengguna (mudah, cepat, menyelesaikan masalah).','Keduanya menyepakati kebutuhan dan prioritas bersama.'],
   q:[['Siapa yang paling tepat menilai apakah aplikasi baru sesuai anggaran dan aturan perlindungan data?',['Pengelola sistem informasi (MSI)','UX Designer','Pengguna akhir'],0,'Kelayakan biaya, keamanan, dan kepatuhan adalah urusan pengelolaan SI.'],
      ['Pengguna bingung di halaman pembayaran. Langkah UX yang tepat dulu adalah?',['Uji kegunaan dengan beberapa pengguna','Membeli server baru','Menambah fitur'],0,'Amati pengguna nyata untuk menemukan penyebab kebingungan.']]},
  {k:'c',t:'Alur membuat aplikasi baru',nodes:['New App Flow'],lang:'text',run:false,
   b:['Membuat aplikasi baru dimulai dari <b>masalah</b>, bukan dari fitur. Alurnya menggabungkan SDLC dari sisi MSI dengan proses desain dari sisi UX: <b>(1) temukan masalah dan tujuan</b> (apa yang ingin diperbaiki dan bagaimana mengukurnya), <b>(2) riset pengguna</b> (wawancara, observasi), <b>(3) studi kelayakan</b> (TELOS, biaya-manfaat, bangun atau beli), <b>(4) tulis kebutuhan</b> (user story, aturan data, keamanan).',
      'Lalu <b>(5) rancang</b>: alur pengguna, wireframe, ERD, dan arsitektur. <b>(6) Buat prototipe dan uji</b> dengan 5 pengguna sebelum menulis banyak kode, karena memperbaiki desain di kertas jauh lebih murah daripada di aplikasi jadi. <b>(7) Bangun bertahap</b> (MVP dulu), <b>(8) uji</b> fungsi, keamanan, aksesibilitas, dan performa, <b>(9) rilis</b> dengan pelatihan dan migrasi data, lalu <b>(10) ukur</b> dengan KPI yang ditetapkan di langkah pertama.',
      'Setiap langkah punya pemilik dan hasil yang jelas, dan setiap gerbang punya keputusan "lanjut atau perbaiki". Inilah yang membedakan proyek yang dikelola dengan baik dari proyek yang hanya "dikerjakan".'],
   code:`Alur aplikasi baru: aplikasi pemesanan katering (startup Dapur Sehat)

 1 Masalah & tujuan  pesanan WA sering salah; target: salah kirim < 2%
 2 Riset pengguna    wawancara 8 pelanggan kantor + 3 kurir        (UX)
 3 Kelayakan         bangun web app vs pakai SaaS → SaaS + modul   (MSI)
 4 Kebutuhan         user story, data pesanan, aturan UU PDP       (MSI+UX)
 5 Rancangan         user flow, wireframe, ERD                     (UX+MSI)
 6 Prototipe & uji   Figma diuji 5 pelanggan, 3 masalah diperbaiki (UX)
 7 Bangun MVP        pesan, bayar QRIS, status kirim               (dev)
 8 Uji               fungsi, keamanan, WCAG 2.2 AA, HP murah       (QA)
 9 Rilis             pelatihan admin, pindah pelanggan bertahap    (MSI)
10 Ukur              salah kirim 1,4% → lanjut fitur langganan     (MSI+UX)

Sekolah     : alur yang sama untuk aplikasi izin siswa via ponsel orang tua
Organisasi  : alur yang sama untuk aplikasi pendataan relawan`,
   pts:['Mulai dari masalah dan tujuan yang terukur.','Riset dan prototipe diuji sebelum banyak kode ditulis.','Bangun bertahap (MVP), uji menyeluruh, rilis terencana, lalu ukur.'],
   q:[['Mengapa prototipe diuji ke pengguna sebelum aplikasi dibangun?',['Memperbaiki desain lebih murah sebelum dikodekan','Agar server lebih cepat','Agar tidak perlu KPI'],0,'Kesalahan yang ditemukan di prototipe jauh lebih murah diperbaiki.'],
      ['Langkah pertama membuat aplikasi baru adalah?',['Menentukan masalah dan tujuan terukur','Memilih warna logo','Menulis kode login'],0,'Tanpa masalah dan tujuan yang jelas, keberhasilan tidak bisa diukur.']]},
  {k:'c',t:'Alur memperbaiki aplikasi lama agar sesuai standar',nodes:['App Improvement Flow'],lang:'text',run:false,
   b:['Banyak organisasi tidak mulai dari nol: aplikasinya sudah ada tetapi lambat, membingungkan, tidak aman, atau tidak bisa dipakai di ponsel. Mengganti total itu mahal dan berisiko, jadi pendekatan yang umum adalah <b>audit, prioritaskan, lalu perbaiki bertahap</b>.',
      '<b>(1) Audit kondisi sekarang</b> dengan standar yang jelas: kegunaan (10 heuristik Nielsen, uji pengguna), aksesibilitas (<b>WCAG 2.2 AA</b>: kontras, keyboard, label form, ukuran target), keamanan (OWASP Top 10, hak akses, cadangan data), privasi (UU PDP: persetujuan terpisah, hak hapus data), performa (waktu muat di HP murah), dan tata kelola (siapa pemilik, dokumentasi). <b>(2) Kumpulkan bukti</b> dari analitik, keluhan, dan tiket bantuan. <b>(3) Analisis kesenjangan</b>: kondisi sekarang dibandingkan standar.',
      '<b>(4) Prioritaskan</b> temuan dengan matriks dampak vs usaha (keamanan dan hukum selalu didahulukan). <b>(5) Rancang ulang</b> bagian yang bermasalah bersama UX Designer dan uji prototipenya. <b>(6) Perbaiki bertahap</b> per rilis kecil, tanpa menghentikan layanan. <b>(7) Ukur ulang</b> dengan metrik yang sama seperti saat audit, sehingga perbaikan terbukti, bukan sekadar terasa.'],
   code:`Alur perbaikan: SIAKAD lama SMA Harapan Bangsa

Audit (temuan)                    Standar        Prioritas  Perbaikan
Login hanya captcha gambar        WCAG 3.3.8     Tinggi     OTP / passkey
Password guru disimpan polos      OWASP A02      Kritis     hash + reset massal
Tombol rapor 16px di ponsel       WCAG 2.5.8     Sedang     target ≥ 44px
Kontras teks abu 2.8:1            WCAG 1.4.3     Sedang     token warna 4.5:1
Halaman nilai 9 detik di 3G       performa       Tinggi     paginasi + cache
Tidak ada cadangan data           BCP 3-2-1      Kritis     backup harian + uji pulih

Ukur ulang setelah 3 rilis: waktu input nilai guru 12 → 5 menit,
keluhan orang tua turun 60%, skor audit aksesibilitas lolos AA.

Perusahaan : audit aplikasi absensi lama sebelum integrasi ke ERP
Startup    : audit onboarding yang membuat 40% pengguna berhenti
Organisasi : audit formulir donasi yang tidak bisa dipakai pembaca layar`,
   pts:['Audit dengan standar nyata: heuristik, WCAG 2.2, OWASP, UU PDP, performa.','Prioritaskan: keamanan dan hukum dulu, lalu dampak terbesar per usaha.','Perbaiki bertahap dan ukur ulang dengan metrik yang sama.'],
   q:[['Temuan audit mana yang harus diperbaiki paling dulu?',['Password disimpan tanpa enkripsi','Warna tombol kurang menarik','Ikon kurang modern'],0,'Risiko keamanan dan hukum selalu didahulukan.'],
      ['Bagaimana membuktikan perbaikan berhasil?',['Ukur ulang dengan metrik yang sama seperti saat audit','Bertanya ke pengembang','Menambah fitur baru'],0,'Bandingkan sebelum dan sesudah dengan ukuran yang sama.']]}
 ]},
{t:'Proyek akhir',lvl:'Lanjutan',d:'Rancang dan rencanakan pengelolaan sistem informasi untuk salah satu organisasi nyata di sekitarmu.',nodes:['Project'],
 lessons:[
  {k:'proj',t:'Rancang sistem informasi untuk organisasi pilihanmu',stack:'Analisis + ERD + mockup + spreadsheet/SQL',
   brief:'Pilih satu organisasi nyata di sekitarmu (usaha keluarga, startup teman, sekolahmu, OSIS/BEM, koperasi, atau masjid/komunitas). Temukan satu masalah informasi yang penting, lalu rancang sistem informasi untuk menyelesaikannya, lengkap dengan alasan bisnis dan rencana penerapan.',
   feats:['Profil organisasi dan problem statement (siapa, masalah apa, dampaknya)','Daftar pemangku kepentingan dan tingkat manajemennya','Kebutuhan fungsional dan non-fungsional (minimal 6)','Flowchart proses lama dan proses baru','Use case: aktor dan apa yang bisa dilakukan','ERD minimal 4 entitas dengan primary key dan foreign key','Mockup 3 layar utama dan 1 dashboard pimpinan dengan 4 KPI','Analisis TELOS dan perkiraan biaya-manfaat sederhana','Matriks hak akses per peran dan rencana cadangan 3-2-1','Rencana penerapan: metode, konversi, pelatihan, ukuran sukses'],
   steps:['Wawancara 2–3 orang di organisasi itu.','Gambar proses lama dan tandai titik masalah.','Tulis kebutuhan, use case, dan ERD.','Buat mockup dan dashboard, lalu minta masukan.','Hitung kelayakan dan tulis rencana penerapan.'],
   files:[['contoh-ringkasan.md','text',`Organisasi : Koperasi Karyawan PT Contoh (180 anggota)
Masalah    : saldo simpanan & pinjaman hanya di buku bendahara,
             anggota harus bertanya langsung; rekap RAT 3 minggu
Sistem     : aplikasi web simpan pinjam + portal anggota
Entitas    : ANGGOTA, SIMPANAN, PINJAMAN, ANGSURAN, PENGURUS
KPI        : 95% anggota aktif login, rekap RAT ≤ 2 hari,
             tunggakan > 30 hari < 3%
Kelayakan  : biaya Rp 15 jt + Rp 300 rb/bln, hemat ±60 jam kerja/tahun
Penerapan  : paralel 2 bulan dengan buku lama, pelatihan 2 sesi`]]}
 ]}
];
