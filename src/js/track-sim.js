/* ===================== JALUR SISTEM INFORMASI MANAJEMEN =====================
   Kurikulum Ruang Kode yang berfokus pada sistemnya: bagaimana SIM mengubah data transaksi
   menjadi laporan dan dasbor untuk keputusan manajer. Konsep dasar yang sama dengan jalur
   MSI dipinjam lewat {k:'see'} sehingga progresnya ikut tersimpan di pelajaran asal. */
const SIM_MODULES=[
{t:'Mengenal sistem informasi manajemen',lvl:'Pemula',d:'Pengertian, tujuan, dan ciri SIM, lalu data, komponen, dan tingkat manajemen.',
 nodes:['What is MIS','Data vs Information','Management Levels'],
 lessons:[
  {k:'c',t:'Apa itu sistem informasi manajemen',nodes:['What is MIS'],lang:'text',run:false,viz:'simmsi',
   b:['<b>Sistem Informasi Manajemen (SIM)</b> adalah sistem yang mengumpulkan data transaksi sehari-hari, mengolahnya, lalu menyajikannya sebagai <b>laporan rutin</b> dan <b>dasbor</b> agar manajer bisa merencanakan, mengendalikan, dan mengambil keputusan. Contohnya laporan penjualan per cabang setiap Senin, rekap presensi siswa per kelas, atau laporan simpanan anggota koperasi setiap akhir bulan.',
      'SIM yang baik punya ciri: memakai <b>satu sumber data</b> yang sama untuk semua bagian, menghasilkan laporan <b>terjadwal</b> dan bisa juga <b>sesuai permintaan</b>, menampilkan <b>pengecualian</b> (hal yang tidak normal) agar manajer tidak tenggelam dalam angka, serta bisa <b>dirinci</b> (drill-down) dari ringkasan ke detail.',
      'Jangan tertukar dengan <b>Manajemen Sistem Informasi (MSI)</b>. SIM adalah <b>sistemnya</b>; MSI adalah <b>cara mengelola</b> seluruh sistem informasi organisasi (strategi, anggaran, proyek, keamanan). Jalur ini fokus membangun dan memakai SIM. Untuk sisi pengelolaannya, lihat jalur <a href="#msi">Manajemen Sistem Informasi</a>.'],
   tb:[{c:'SIM di empat konteks',h:['Konteks','Data transaksi','Laporan SIM','Keputusan yang dibantu'],r:[
     ['Perusahaan','Penjualan kasir, penerimaan barang','Penjualan & stok per cabang (mingguan)','Pindahkan stok antarcabang, ubah stok minimum'],
     ['Startup','Pesanan, pembayaran, klik aplikasi','Dasbor pesanan, retensi, biaya per pelanggan','Kanal promosi mana yang dilanjutkan'],
     ['Sekolah','Presensi, nilai, pembayaran SPP','Rekap presensi & nilai per kelas, tunggakan SPP','Siapa butuh remedial, siapa dipanggil BK'],
     ['Organisasi','Setoran simpanan, iuran, donasi','Laporan simpanan, pinjaman, dan dana per bulan','Batas pinjaman, jadwal penagihan, program bantuan']]},
    {c:'SIM vs MSI',h:['Aspek','SIM','MSI'],r:[['Hakikat','Sistem (objek)','Kegiatan mengelola'],['Hasil','Laporan dan dasbor','Rencana, anggaran, kebijakan, proyek TI'],['Contoh','Laporan stok mingguan','Memutuskan mengganti aplikasi stok']]}],
   pts:['SIM mengubah data transaksi menjadi laporan dan dasbor untuk manajer.','Ciri SIM: satu sumber data, laporan terjadwal dan sesuai permintaan, pengecualian, drill-down.','SIM = sistemnya; MSI = cara mengelolanya.'],
   q:[['Rekap presensi siswa per kelas yang terbit tiap Jumat adalah contoh?',['Laporan SIM terjadwal','Kebijakan MSI','Perangkat keras'],0,'Laporan rutin dari data transaksi adalah keluaran SIM.'],
      ['Ciri SIM yang membantu manajer tidak tenggelam dalam angka adalah?',['Laporan pengecualian','Font yang besar','Jumlah menu yang banyak'],0,'Laporan pengecualian hanya menampilkan hal yang tidak normal.']]},
  {k:'see',ref:'msi:Data, informasi, dan pengetahuan'},
  {k:'see',ref:'msi:Komponen sistem informasi'},
  {k:'see',ref:'msi:SIM dan tingkat manajemen'}
 ]},
{t:'Jenis sistem di sekitar SIM',lvl:'Pemula',d:'TPS sebagai sumber data, SIM per fungsi, dan sistem terpadu ERP, CRM, SCM.',
 nodes:['TPS MIS DSS EIS','Functional IS','ERP CRM SCM'],
 lessons:[
  {k:'see',ref:'msi:TPS, MIS, DSS, dan EIS'},
  {k:'see',ref:'msi:Sistem informasi fungsional'},
  {k:'see',ref:'msi:ERP, CRM, dan SCM'}
 ]},
{t:'Laporan dan dasbor SIM',lvl:'Menengah',d:'Jenis laporan SIM, merancang laporan yang dipakai, dan dasbor untuk manajer.',
 nodes:['Report Types','Report Design','Dashboard'],
 lessons:[
  {k:'c',t:'Jenis laporan SIM',nodes:['Report Types'],lang:'text',run:false,viz:'reports',
   b:['Keluaran utama SIM adalah laporan. Ada empat jenis yang perlu kamu kenal. <b>Laporan terjadwal</b> terbit rutin pada waktu yang sama (harian, mingguan, bulanan), misalnya laporan penjualan setiap Senin pagi. <b>Laporan sesuai permintaan</b> (on-demand/ad hoc) dibuat saat manajer butuh jawaban tertentu, misalnya "berapa siswa kelas X yang belum bayar SPP hari ini?".',
      '<b>Laporan pengecualian</b> (exception report) hanya memuat hal yang keluar dari batas normal: stok di bawah minimum, siswa alpa lebih dari 3 hari, pinjaman telat lebih dari 30 hari. Manajer cukup membaca beberapa baris yang butuh tindakan. <b>Laporan drill-down</b> dimulai dari ringkasan lalu bisa dirinci: total penjualan nasional → per wilayah → per cabang → per kasir.',
      'Satu SIM yang baik menyediakan keempatnya dari <b>data yang sama</b>. Tanpa itu, setiap bagian membuat laporannya sendiri di spreadsheet dan angkanya mulai berbeda-beda.'],
   tb:[{c:'Empat jenis laporan SIM',h:['Jenis','Kapan dipakai','Perusahaan','Sekolah'],r:[
     ['Terjadwal','Pemantauan rutin','Penjualan per cabang tiap Senin','Rekap presensi per kelas tiap Jumat'],
     ['Sesuai permintaan','Pertanyaan khusus','Penjualan produk baru 3 hari terakhir','Siswa kelas X yang belum bayar SPP'],
     ['Pengecualian','Hanya yang tidak normal','Stok di bawah minimum','Siswa alpa > 3 hari'],
     ['Drill-down','Mencari penyebab','Nasional → wilayah → cabang → kasir','Sekolah → kelas → siswa → mapel']]},
    {c:'Di startup dan organisasi',h:['Jenis','Startup','Organisasi'],r:[['Terjadwal','Metrik mingguan pendiri','Laporan kas bulanan pengurus'],['Sesuai permintaan','Berapa pengguna dari kampanye X?','Siapa donatur terbesar tahun ini?'],['Pengecualian','Pembayaran gagal > 5%','Pinjaman telat > 30 hari'],['Drill-down','Total pesanan → kota → kanal','Total donasi → program → donatur']]}],
   pts:['Terjadwal: rutin. Sesuai permintaan: pertanyaan khusus.','Pengecualian: hanya yang butuh tindakan.','Drill-down: dari ringkasan ke detail untuk mencari penyebab.'],
   q:[['Kepala gudang hanya ingin melihat barang yang stoknya di bawah minimum. Laporan apa?',['Laporan pengecualian','Laporan terjadwal lengkap','Laporan drill-down'],0,'Hanya baris yang keluar dari batas normal yang ditampilkan.'],
      ['Direktur melihat penjualan turun, lalu mengeklik wilayah dan cabang untuk mencari penyebab. Ini?',['Drill-down','Laporan pengecualian','Laporan ad hoc'],0,'Drill-down merinci dari ringkasan ke detail.']]},
  {k:'c',t:'Merancang laporan yang benar-benar dipakai',nodes:['Report Design'],lang:'text',run:false,viz:'chartpick',
   b:['Banyak laporan dibuat tetapi tidak dibaca. Penyebabnya: tidak menjawab pertanyaan pembacanya, terlalu banyak angka, atau datang terlambat. Mulailah dari <b>pertanyaan dan keputusan</b>: siapa pembacanya, keputusan apa yang ia ambil, dan seberapa sering.',
      'Lalu pilih isi seperlunya: <b>indikator utama</b> di atas, <b>pembanding</b> (target, bulan lalu, tahun lalu) agar angka bermakna, dan <b>tanda</b> untuk hal yang butuh tindakan. Pilih bentuk visual sesuai pertanyaan: batang untuk membandingkan, garis untuk tren, tabel untuk angka yang perlu dibaca tepat.',
      'Tulis juga <b>definisi</b> setiap angka ("siswa aktif = terdaftar dan tidak cuti") dan <b>waktu data</b> ("data per kemarin 23.59"). Dua hal kecil ini mencegah rapat habis untuk berdebat angka mana yang benar.'],
   tb:[{c:'Lembar rancangan laporan',h:['Pertanyaan perancangan','Contoh: laporan SPP sekolah'],r:[['Siapa pembacanya?','Kepala sekolah dan bendahara'],['Keputusan apa yang diambil?','Siapa yang perlu dihubungi, perlukah skema cicilan'],['Seberapa sering?','Mingguan, tiap Senin'],['Indikator utama','Persentase siswa lunas, total tunggakan'],['Pembanding','Target 95% lunas, minggu lalu'],['Tanda tindakan','Kelas dengan tunggakan > 10% diberi warna merah'],['Definisi & waktu data','Tunggak = lewat tanggal 10; data per Minggu 23.59']]},
    {c:'Laporan yang dipakai vs diabaikan',h:['Diabaikan','Dipakai'],r:[['30 kolom angka tanpa pembanding','5 indikator + target + tren'],['Terbit tanggal 20 untuk bulan lalu','Terbit tanggal 2'],['Definisi berbeda tiap bagian','Satu definisi tertulis'],['Tidak ada tanda tindakan','Baris bermasalah ditandai']]}],
   pts:['Mulai dari pembaca, keputusan, dan frekuensi.','Indikator utama + pembanding + tanda tindakan.','Tulis definisi angka dan waktu data.'],
   q:[['Langkah pertama merancang laporan adalah?',['Menentukan pembaca dan keputusannya','Memilih warna grafik','Menambah sebanyak mungkin kolom'],0,'Laporan ada untuk membantu keputusan tertentu.'],
      ['Mengapa laporan butuh pembanding seperti target atau bulan lalu?',['Agar angka bermakna','Agar laporan lebih panjang','Agar tidak perlu definisi'],0,'Angka tanpa pembanding sulit dinilai baik atau buruk.']]},
  {k:'see',ref:'msi:Data warehouse, BI, dan kualitas data'}
 ]},
{t:'Data di balik SIM',lvl:'Menengah',d:'Database, relasi tabel, dan cara data transaksi diolah menjadi laporan.',
 nodes:['DBMS','ERD','Transaction to Report'],
 lessons:[
  {k:'see',ref:'msi:Database dan DBMS'},
  {k:'see',ref:'msi:Merancang tabel dan relasi (ERD)'},
  {k:'c',t:'Dari transaksi ke laporan',nodes:['Transaction to Report'],lang:'text',run:false,viz:'etl',
   b:['Setiap laporan SIM berasal dari <b>data transaksi</b> yang dicatat TPS. Alurnya: transaksi dicatat → data disimpan di database → data diringkas (dijumlah, dirata-rata, dikelompokkan) → disajikan sebagai laporan atau dasbor. Kalau pencatatan di awal salah, laporan di akhir pasti salah ("garbage in, garbage out").',
      'Peringkasan biasanya memakai <b>SQL</b>: <code>GROUP BY</code> untuk mengelompokkan per cabang atau per kelas, <code>SUM</code>/<code>COUNT</code>/<code>AVG</code> untuk menghitung, dan <code>WHERE</code> atau <code>HAVING</code> untuk laporan pengecualian. Kamu bisa mencoba query sungguhan di jalur <a href="#sql">SQL</a>.',
      'Untuk data besar atau dari banyak sistem, data dipindahkan dulu ke <b>data warehouse</b> lewat proses ETL agar laporan tidak memperlambat aplikasi kasir atau SIAKAD yang sedang dipakai.'],
   tb:[{c:'Dari transaksi ke laporan',h:['Konteks','Transaksi (TPS)','Ringkasan','Laporan SIM'],r:[
     ['Perusahaan','Baris penjualan kasir','Jumlah per cabang per minggu','Penjualan mingguan per cabang'],
     ['Startup','Event pesanan dan pembayaran','Hitung per kanal promosi','Biaya per pelanggan per kanal'],
     ['Sekolah','Presensi harian per siswa','Hitung alpa per siswa','Daftar siswa alpa > 3 hari'],
     ['Organisasi','Setoran dan angsuran','Saldo per anggota','Laporan pinjaman telat']]}],
   code:`-- Laporan terjadwal: penjualan per cabang minggu ini
SELECT cabang, SUM(total) AS omzet, COUNT(*) AS transaksi
FROM penjualan
WHERE tanggal >= '2026-10-26'
GROUP BY cabang
ORDER BY omzet DESC;

-- Laporan pengecualian: siswa alpa lebih dari 3 hari bulan ini
SELECT s.nama, s.kelas, COUNT(*) AS alpa
FROM presensi p JOIN siswa s ON s.nis = p.nis
WHERE p.status = 'A' AND p.tanggal >= '2026-10-01'
GROUP BY s.nis, s.nama, s.kelas
HAVING COUNT(*) > 3;`,
   pts:['Laporan berasal dari data transaksi: salah catat = salah laporan.','SQL GROUP BY + SUM/COUNT untuk ringkasan, HAVING untuk pengecualian.','Data besar dipindah ke warehouse lewat ETL.'],
   q:[['Klausa SQL yang cocok untuk laporan pengecualian "alpa lebih dari 3 hari" setelah pengelompokan adalah?',['HAVING','ORDER BY','SELECT *'],0,'HAVING menyaring hasil setelah GROUP BY.'],
      ['Apa arti "garbage in, garbage out"?',['Data masukan yang salah menghasilkan laporan yang salah','Data lama harus dihapus','Laporan harus dicetak'],0,'Kualitas laporan bergantung pada kualitas data transaksi.']]}
 ]},
{t:'SIM di berbagai organisasi',lvl:'Menengah',d:'Merancang SIM sederhana dan melihat penerapannya di perusahaan, startup, sekolah, dan organisasi.',
 nodes:['Spreadsheet MIS','Case Studies'],
 lessons:[
  {k:'c',t:'Membangun SIM sederhana dengan spreadsheet',nodes:['Spreadsheet MIS'],lang:'text',run:false,viz:'sheet',
   b:['Organisasi kecil tidak selalu perlu aplikasi mahal. SIM pertama bisa dibangun dengan <b>spreadsheet bersama</b> asalkan dirancang seperti database: satu lembar untuk satu jenis data, satu baris untuk satu transaksi, kolom dengan format tetap, dan tidak ada sel gabung.',
      'Susun tiga lapis: <b>lembar input</b> (diisi lewat formulir online agar format konsisten), <b>lembar olah</b> (rumus seperti SUMIFS, COUNTIFS, atau tabel pivot), dan <b>lembar laporan</b> (ringkasan, grafik, dan tanda merah untuk pengecualian). Pengguna biasa hanya boleh mengisi formulir dan membaca laporan.',
      'Spreadsheet cocok sampai kira-kira ribuan baris dan beberapa pengguna. Saat data tumbuh, banyak orang mengedit bersamaan, atau butuh hak akses rinci, saatnya pindah ke aplikasi atau database.'],
   tb:[{c:'SIM spreadsheet di empat konteks',h:['Konteks','Lembar input','Lembar olah','Lembar laporan'],r:[
     ['Perusahaan kecil','Formulir penjualan harian per toko','SUMIFS per toko dan produk','Omzet mingguan + produk terlaris'],
     ['Startup awal','Formulir pesanan pelanggan','Pivot pesanan per kota','Pesanan per minggu + pelanggan berulang'],
     ['Sekolah','Formulir presensi per kelas','COUNTIFS alpa per siswa','Siswa alpa > 3 hari (merah)'],
     ['Organisasi','Formulir setoran iuran','Saldo per anggota','Anggota menunggak > 2 bulan']]},
    {c:'Kapan pindah dari spreadsheet',h:['Tanda','Artinya'],r:[['Data > puluhan ribu baris, file lambat','Butuh database'],['Banyak orang mengedit bersamaan dan saling menimpa','Butuh aplikasi dengan transaksi'],['Butuh hak akses per baris (wali kelas hanya kelasnya)','Butuh sistem dengan peran pengguna'],['Data pribadi sensitif','Butuh kendali keamanan dan log audit']]}],
   pts:['Rancang spreadsheet seperti database: satu baris satu transaksi.','Tiga lapis: input (formulir), olah (rumus/pivot), laporan.','Pindah ke aplikasi saat data, pengguna, atau kebutuhan keamanan bertambah.'],
   q:[['Mengapa input sebaiknya lewat formulir online?',['Agar format data konsisten','Agar file lebih berwarna','Agar rumus tidak perlu'],0,'Formulir memaksa format yang sama untuk setiap isian.'],
      ['Tanda yang paling jelas bahwa SIM spreadsheet perlu diganti adalah?',['Butuh hak akses rinci untuk data pribadi','Ingin menambah grafik','Ingin mengganti warna'],0,'Spreadsheet sulit membatasi akses per baris dan mencatat log.']]},
  {k:'see',ref:'msi:Di perusahaan: distributor dengan ERP'},
  {k:'see',ref:'msi:Di startup: dari spreadsheet ke sistem yang tumbuh'},
  {k:'see',ref:'msi:Di sekolah: sistem informasi akademik terpadu'},
  {k:'see',ref:'msi:Di organisasi: koperasi, yayasan, dan organisasi mahasiswa'}
 ]},
{t:'Membangun dan menilai SIM',lvl:'Lanjutan',d:'Tahap pengembangan SIM, menggali kebutuhan, dan mengukur keberhasilan SIM.',
 nodes:['SDLC','Requirements','IS Success Model'],
 lessons:[
  {k:'see',ref:'msi:Siklus hidup pengembangan sistem (SDLC)'},
  {k:'see',ref:'msi:Menggali kebutuhan dan memodelkan proses'},
  {k:'see',ref:'msi:Alur membuat aplikasi baru'},
  {k:'c',t:'Mengukur keberhasilan SIM',nodes:['IS Success Model'],lang:'text',run:false,viz:'delone',
   b:['SIM yang sudah jalan belum tentu berhasil. Model <b>DeLone & McLean</b> menilai keberhasilan sistem informasi dari enam sisi: <b>kualitas sistem</b> (cepat, stabil, mudah dipakai), <b>kualitas informasi</b> (akurat, tepat waktu, lengkap), <b>kualitas layanan</b> (bantuan saat ada masalah), <b>penggunaan</b> (benar-benar dipakai), <b>kepuasan pengguna</b>, dan <b>manfaat bersih</b> bagi organisasi.',
      'Keenamnya saling berkaitan. Sistem yang lambat (kualitas sistem rendah) membuat orang kembali ke spreadsheet (penggunaan turun), sehingga manfaatnya tidak pernah terasa. Karena itu ukur dari beberapa sisi, jangan hanya bertanya "apakah sistemnya sudah jadi?".',
      'Ukuran yang praktis: waktu muat halaman, persentase laporan terbit tepat waktu, jumlah pengguna aktif mingguan, skor kepuasan dari survei singkat, jumlah tiket bantuan, dan dampak bisnis seperti waktu rekap yang berkurang.'],
   tb:[{c:'Enam dimensi DeLone & McLean',h:['Dimensi','Pertanyaan','Contoh ukuran (SIAKAD sekolah)'],r:[
     ['Kualitas sistem','Cepat, stabil, mudah?','Halaman nilai terbuka < 3 detik di HP'],
     ['Kualitas informasi','Akurat, tepat waktu?','Rapor terbit H+3, nol koreksi nilai'],
     ['Kualitas layanan','Ada bantuan saat bermasalah?','Tiket guru selesai < 1 hari'],
     ['Penggunaan','Benar-benar dipakai?','95% guru input nilai lewat sistem'],
     ['Kepuasan pengguna','Puas memakainya?','Survei guru & orang tua ≥ 4 dari 5'],
     ['Manfaat bersih','Apa dampaknya?','Waktu rekap rapor 2 minggu → 3 hari']]},
    {c:'Di konteks lain',h:['Konteks','Penggunaan','Manfaat bersih'],r:[['Perusahaan','Semua cabang input penjualan harian','Selisih stok turun 30%'],['Startup','Pendiri buka dasbor tiap minggu','Biaya promosi lebih efisien'],['Organisasi','Anggota cek saldo sendiri','Pertanyaan ke bendahara berkurang']]}],
   pts:['Keberhasilan SIM diukur dari enam dimensi DeLone & McLean.','Kualitas sistem dan informasi memengaruhi penggunaan dan kepuasan.','Pakai ukuran nyata: waktu muat, ketepatan laporan, pengguna aktif, survei, dampak.'],
   q:[['Guru kembali memakai spreadsheet karena SIAKAD lambat. Dimensi mana yang bermasalah dulu?',['Kualitas sistem','Manfaat bersih','Kualitas layanan'],0,'Sistem yang lambat menurunkan penggunaan.'],
      ['"Waktu rekap rapor turun dari 2 minggu ke 3 hari" mengukur dimensi?',['Manfaat bersih','Kualitas layanan','Kepuasan pengguna'],0,'Itu dampak nyata bagi organisasi.']]},
  {k:'see',ref:'msi:Alur memperbaiki aplikasi lama agar sesuai standar'}
 ]},
{t:'Proyek akhir',lvl:'Lanjutan',d:'Bangun SIM mini yang menghasilkan laporan nyata untuk organisasi pilihanmu.',nodes:['Project'],
 lessons:[
  {k:'proj',t:'Bangun SIM mini dengan laporan nyata',stack:'Formulir online + spreadsheet atau SQL + dasbor',
   brief:'Pilih satu organisasi di sekitarmu (toko keluarga, startup teman, kelas atau sekolahmu, koperasi, OSIS/BEM, atau komunitas). Bangun SIM mini yang mencatat satu jenis transaksi dan menghasilkan laporan yang benar-benar dipakai seorang manajer atau pengurus.',
   feats:['Satu jenis transaksi dicatat lewat formulir dengan format tetap','Minimal 30 baris data contoh (boleh fiktif, jangan data pribadi asli)','Satu laporan terjadwal (mingguan atau bulanan)','Satu laporan pengecualian dengan tanda yang jelas','Satu ringkasan yang bisa dirinci (drill-down) ke detail','Definisi setiap angka dan waktu data tertulis di laporan','Pembagian hak akses: siapa mengisi, siapa membaca','Penilaian keberhasilan dengan minimal 3 dimensi DeLone & McLean'],
   steps:['Wawancara satu calon pembaca laporan: keputusan apa yang ia ambil?','Isi lembar rancangan laporan (pembaca, keputusan, frekuensi, indikator).','Buat formulir input dan isi data contoh.','Buat lembar olah dengan rumus/pivot atau query SQL.','Susun laporan terjadwal, pengecualian, dan drill-down.','Minta pembaca mencoba selama satu minggu, lalu ukur dan perbaiki.'],
   files:[['rancangan-laporan.md','text',`SIM mini : Presensi kelas XI-2 (sekolah)
Pembaca  : wali kelas dan guru BK
Keputusan: siswa mana yang perlu dipanggil
Frekuensi: mingguan, tiap Jumat 14.00

Input    : formulir presensi harian (tanggal, NIS, status H/I/S/A)
Olah     : COUNTIFS status "A" per NIS per bulan
Laporan  : 1) rekap kehadiran kelas per minggu (terjadwal)
           2) siswa alpa > 3 hari bulan ini (pengecualian, merah)
           3) klik nama siswa → riwayat per tanggal (drill-down)

Definisi : alpa = tidak hadir tanpa surat; data per Jumat 12.00
Akses    : ketua kelas mengisi, wali kelas & BK membaca
Ukuran   : laporan terbit tiap Jumat (kualitas informasi),
           wali kelas membuka tiap minggu (penggunaan),
           waktu rekap 1 jam → 5 menit (manfaat bersih)`]]}
 ]}
];
