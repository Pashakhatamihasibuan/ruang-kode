"""Soal latihan tambahan untuk jalur SQL (database Toko Nusantara).

Keluaran ditulis RUN lalu diisi isi_sql.js yang menjalankan jawaban di mesin SQL situs ini.
"""
from mobile_dart_x import S


def Q(q, h, a, out='RUN'): return S(q, h, a, out, lang='sql')
def Tx(q, h, a): return S(q, h, a, lang='text')


SQL = {
'Basis data relasional: tabel, baris, kolom': [
  Q('Tampilkan nama, jabatan, dan divisi semua karyawan.', 'SELECT kolom1, kolom2 FROM tabel;',
    'SELECT nama, jabatan, divisi FROM karyawan;'),
  Tx('Pada tabel produk, sebutkan contoh baris, kolom, primary key, dan sel.', 'Baris = satu data, kolom = satu atribut.',
     'Baris      : (1, Kopi Gayo, Minuman, 85000, 40) adalah satu produk\nKolom      : nama, kategori, harga, stok\nPrimary key: id, unik untuk setiap produk\nSel        : harga Kopi Gayo = 85000'),
],
'Kelebihan RDBMS & SQL lawan NoSQL': [
  Tx('Pilih RDBMS atau NoSQL: (a) saldo rekening bank, (b) log klik jutaan per menit, (c) katalog produk dengan atribut sangat beragam, (d) pesanan dengan relasi pelanggan dan produk.', 'Transaksi ketat dan relasi kuat cocok untuk RDBMS.',
     '(a) RDBMS (ACID)\n(b) NoSQL (wide-column/time series)\n(c) NoSQL dokumen (atau kolom JSON di RDBMS)\n(d) RDBMS'),
  Tx('Sebutkan tiga kelebihan SQL dibanding mengolah data di spreadsheet.', 'Skala, integritas, akses bersama.',
     '1. Sanggup jutaan baris dengan cepat (index).\n2. Aturan data dijaga database (tipe, NOT NULL, foreign key).\n3. Banyak pengguna dan aplikasi bisa mengakses bersamaan dengan hak akses.'),
],
'Sintaks & kata kunci SQL': [
  Q('Tampilkan nama dan kategori produk, lalu urutkan berdasarkan nama.', 'Kata kunci boleh huruf kecil, tetapi konvensinya huruf besar.',
    'SELECT nama, kategori\nFROM produk\nORDER BY nama;'),
  Q('Perbaiki query yang salah ini: <code>SELECT nama harga FORM produk</code>', 'Kolom dipisah koma, dan kata kuncinya FROM.',
    'SELECT nama, harga FROM produk;'),
],
'Tipe data': [
  Q('Tampilkan nama produk dan harga setelah PPN 11%, dibulatkan tanpa desimal.', 'Kalikan dengan 1.11 dan pakai ROUND.',
    'SELECT nama, ROUND(harga * 1.11) AS harga_ppn FROM produk;'),
  Q('Tampilkan id pesanan dan tahun pesanannya sebagai angka.', 'EXTRACT(YEAR FROM kolom_tanggal).',
    'SELECT id, EXTRACT(YEAR FROM tanggal) AS tahun FROM pesanan;'),
],
'Operator': [
  Q('Tampilkan produk dengan harga antara 20.000 dan 80.000 yang kategorinya bukan Bumbu.', 'BETWEEN ... AND ... dan &lt;&gt; atau NOT.',
    "SELECT nama, kategori, harga\nFROM produk\nWHERE harga BETWEEN 20000 AND 80000\n  AND kategori <> 'Bumbu';"),
  Q('Tampilkan pelanggan dari Jakarta atau Bandung yang namanya mengandung huruf "i".', 'IN (...) dan LIKE \'%i%\'.',
    "SELECT nama, kota\nFROM pelanggan\nWHERE kota IN ('Jakarta', 'Bandung')\n  AND nama LIKE '%i%';"),
],
'SELECT & FROM': [
  Q('Tampilkan nama produk sebagai "produk" dan harga per 100 gram sebagai "harga_per_100g" (anggap tiap produk 250 gram).', 'Alias dengan AS; harga * 100 / 250.',
    'SELECT nama AS produk, harga * 100 / 250 AS harga_per_100g FROM produk;'),
  Q('Tampilkan label "Nama (Kota)" untuk setiap pelanggan dalam satu kolom bernama label. Apa yang terjadi pada pelanggan yang kotanya kosong?', 'Gabungkan teks dengan ||. Menggabungkan dengan NULL menghasilkan NULL; pakai COALESCE jika ingin teks pengganti.',
    "SELECT nama || ' (' || kota || ')' AS label FROM pelanggan;"),
],
'WHERE: menyaring baris': [
  Q('Tampilkan pelanggan yang kotanya belum diisi.', 'Pakai IS NULL, bukan = NULL.',
    'SELECT id, nama FROM pelanggan WHERE kota IS NULL;'),
  Q('Tampilkan produk yang stoknya habis atau harganya di atas 100.000.', 'Gabungkan kondisi dengan OR.',
    'SELECT nama, harga, stok FROM produk WHERE stok = 0 OR harga > 100000;'),
],
'ORDER BY, LIMIT & DISTINCT': [
  Q('Tampilkan 3 produk dengan stok terbanyak.', 'ORDER BY stok DESC lalu LIMIT 3.',
    'SELECT nama, stok FROM produk ORDER BY stok DESC LIMIT 3;'),
  Q('Tampilkan daftar kota pelanggan tanpa duplikat dan tanpa NULL, urut abjad.', 'DISTINCT, WHERE ... IS NOT NULL, ORDER BY.',
    'SELECT DISTINCT kota FROM pelanggan WHERE kota IS NOT NULL ORDER BY kota;'),
],
'Urutan eksekusi query': [
  Tx('Urutkan cara database menjalankan klausa: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT.', 'Database mulai dari tabel sumber, bukan dari SELECT.',
     'FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT'),
  Q('Kenapa <code>WHERE nilai &gt; 1000000</code> gagal jika nilai adalah alias di SELECT? Tulis versi yang benar.', 'WHERE dijalankan sebelum SELECT, jadi alias belum ada. Ulangi ekspresinya.',
    'SELECT nama, harga * stok AS nilai\nFROM produk\nWHERE harga * stok > 1000000\nORDER BY nilai DESC;'),
],
'INSERT: menambah baris': [
  Q('Tambahkan dua produk sekaligus: Gula Aren (Bumbu, 22.000, stok 60) dan Kopi Toraja (Minuman, 95.000, stok 25), lalu tampilkan produk id 9 dan 10.', 'Satu INSERT dengan beberapa kelompok VALUES.',
    "INSERT INTO produk (id, nama, kategori, harga, stok) VALUES\n  (9, 'Gula Aren', 'Bumbu', 22000, 60),\n  (10, 'Kopi Toraja', 'Minuman', 95000, 25);\nSELECT id, nama, harga FROM produk WHERE id >= 9;"),
  Q('Tambahkan pesanan baru id 120 untuk pelanggan 5 tanggal 2024-12-01 tanpa menyebut status, lalu lihat status bawaannya.', 'Kolom yang tidak diisi memakai DEFAULT.',
    "INSERT INTO pesanan (id, pelanggan_id, tanggal) VALUES (120, 5, '2024-12-01');\nSELECT id, status FROM pesanan WHERE id = 120;"),
],
'UPDATE & DELETE': [
  Q('Naikkan harga semua produk kategori Minuman sebesar 10%, lalu tampilkan hasilnya.', 'UPDATE ... SET harga = ROUND(harga * 1.1) WHERE ... (dibulatkan agar tidak ada sisa desimal).',
    "UPDATE produk SET harga = ROUND(harga * 1.1) WHERE kategori = 'Minuman';\nSELECT nama, harga FROM produk WHERE kategori = 'Minuman';"),
  Q('Hapus semua pesanan berstatus batal beserta detailnya, lalu hitung sisa pesanan.', 'Hapus dulu baris anak (detail_pesanan) agar foreign key tidak dilanggar.',
    "DELETE FROM detail_pesanan\nWHERE pesanan_id IN (SELECT id FROM pesanan WHERE status = 'batal');\nDELETE FROM pesanan WHERE status = 'batal';\nSELECT COUNT(*) AS sisa FROM pesanan;"),
],
'Fungsi agregat': [
  Q('Hitung jumlah pelanggan, jumlah kota berbeda, dan tanggal bergabung paling awal.', 'COUNT(*), COUNT(DISTINCT ...), MIN.',
    'SELECT COUNT(*) AS pelanggan,\n       COUNT(DISTINCT kota) AS kota,\n       MIN(bergabung) AS pertama\nFROM pelanggan;'),
  Q('Hitung rata-rata harga produk Camilan, dibulatkan tanpa desimal.', 'AVG dengan WHERE, lalu ROUND.',
    "SELECT ROUND(AVG(harga)) AS rata_camilan FROM produk WHERE kategori = 'Camilan';"),
],
'GROUP BY': [
  Q('Tampilkan jumlah karyawan dan total gaji per divisi, urut dari total gaji terbesar.', 'GROUP BY divisi dengan COUNT dan SUM.',
    'SELECT divisi, COUNT(*) AS orang, SUM(gaji) AS total_gaji\nFROM karyawan\nGROUP BY divisi\nORDER BY total_gaji DESC;'),
  Q('Tampilkan jumlah pelanggan per kota, termasuk yang kotanya kosong.', 'NULL menjadi satu kelompok sendiri.',
    'SELECT kota, COUNT(*) AS n FROM pelanggan GROUP BY kota ORDER BY n DESC, kota;'),
],
'HAVING': [
  Q('Tampilkan divisi yang rata-rata gajinya di atas 10 juta.', 'Kondisi pada hasil agregat memakai HAVING.',
    'SELECT divisi, AVG(gaji) AS rata\nFROM karyawan\nGROUP BY divisi\nHAVING AVG(gaji) > 10000000;'),
  Q('Tampilkan pelanggan_id yang punya lebih dari satu pesanan selesai.', 'WHERE menyaring baris dulu, HAVING menyaring kelompok.',
    "SELECT pelanggan_id, COUNT(*) AS n\nFROM pesanan\nWHERE status = 'selesai'\nGROUP BY pelanggan_id\nHAVING COUNT(*) > 1;"),
],
'CREATE TABLE': [
  Q('Buat tabel kategori (id INTEGER PRIMARY KEY, nama TEXT NOT NULL), isi tiga baris, lalu tampilkan.', 'CREATE TABLE lalu INSERT dan SELECT.',
    "CREATE TABLE kategori (\n  id INTEGER PRIMARY KEY,\n  nama TEXT NOT NULL\n);\nINSERT INTO kategori VALUES (1, 'Minuman'), (2, 'Camilan'), (3, 'Bumbu');\nSELECT * FROM kategori;"),
  Q('Buat tabel pengiriman dengan kolom status yang bawaannya "diproses", lalu tambah satu baris tanpa status.', 'DEFAULT pada definisi kolom.',
    "CREATE TABLE pengiriman (\n  id INTEGER PRIMARY KEY,\n  pesanan_id INTEGER,\n  kurir TEXT,\n  status TEXT DEFAULT 'diproses'\n);\nINSERT INTO pengiriman (id, pesanan_id, kurir) VALUES (1, 107, 'JNE');\nSELECT * FROM pengiriman;"),
],
'ALTER, DROP & TRUNCATE': [
  Q('Tambahkan kolom berat (INTEGER) ke tabel produk, isi berat Kopi Gayo 250, lalu tampilkan nama dan berat dua produk pertama.', 'ALTER TABLE ... ADD COLUMN.',
    'ALTER TABLE produk ADD COLUMN berat INTEGER;\nUPDATE produk SET berat = 250 WHERE id = 1;\nSELECT nama, berat FROM produk WHERE id <= 2;'),
  Tx('Apa beda DELETE, TRUNCATE, dan DROP?', 'Hapus baris, kosongkan tabel, hapus tabel.',
     'DELETE  : menghapus baris tertentu (bisa pakai WHERE), tercatat per baris.\nTRUNCATE: mengosongkan seluruh isi tabel dengan cepat, struktur tetap.\nDROP    : menghapus tabel beserta struktur dan isinya.'),
],
'Primary key & foreign key': [
  Q('Coba tambahkan detail pesanan untuk pesanan 999 yang tidak ada. Apa yang terjadi?', 'Foreign key menolak nilai yang tidak ada di tabel induk.',
    'INSERT INTO detail_pesanan VALUES (999, 1, 1);'),
  Tx('Kenapa detail_pesanan memakai primary key gabungan (pesanan_id, produk_id)?', 'Satu produk hanya boleh muncul sekali per pesanan.',
     'Kombinasi pesanan dan produk harus unik: satu produk muncul sekali di satu pesanan\n(jumlahnya disimpan di kolom jumlah). Kunci gabungan mencegah baris ganda.'),
],
'UNIQUE, NOT NULL & CHECK': [
  Q('Coba ubah harga Teh Melati menjadi -5. Constraint apa yang menolaknya?', 'Lihat definisi kolom harga di tabel produk.',
    'UPDATE produk SET harga = -5 WHERE id = 2;'),
  Q('Buat tabel member dengan email UNIQUE, lalu coba masukkan email yang sama dua kali.', 'Baris kedua harus ditolak.',
    "CREATE TABLE member (\n  id INTEGER PRIMARY KEY,\n  email TEXT NOT NULL UNIQUE\n);\nINSERT INTO member VALUES (1, 'rina@mail.id');\nINSERT INTO member VALUES (2, 'rina@mail.id');"),
],
'INNER JOIN': [
  Q('Tampilkan id pesanan, tanggal, dan nama pelanggan untuk pesanan berstatus selesai.', 'JOIN pelanggan ON pelanggan.id = pesanan.pelanggan_id.',
    "SELECT s.id, s.tanggal, p.nama\nFROM pesanan s\nJOIN pelanggan p ON p.id = s.pelanggan_id\nWHERE s.status = 'selesai'\nORDER BY s.id;"),
  Q('Tampilkan nama produk dan total unit terjual per produk, urut dari terbanyak.', 'JOIN detail_pesanan dengan produk, lalu GROUP BY.',
    'SELECT pr.nama, SUM(d.jumlah) AS terjual\nFROM detail_pesanan d\nJOIN produk pr ON pr.id = d.produk_id\nGROUP BY pr.nama\nORDER BY terjual DESC;'),
],
'LEFT, RIGHT & FULL OUTER JOIN': [
  Q('Tampilkan semua pelanggan beserta jumlah pesanannya, termasuk yang belum pernah memesan (0).', 'LEFT JOIN lalu COUNT(kolom tabel kanan).',
    'SELECT p.nama, COUNT(s.id) AS n_pesanan\nFROM pelanggan p\nLEFT JOIN pesanan s ON s.pelanggan_id = p.id\nGROUP BY p.nama\nORDER BY n_pesanan DESC, p.nama;'),
  Q('Tampilkan produk yang tidak terjual sama sekali di bulan November 2024.', 'LEFT JOIN ke subquery penjualan November, lalu WHERE kolom kanan IS NULL.',
    "SELECT pr.nama\nFROM produk pr\nLEFT JOIN (\n  SELECT d.produk_id\n  FROM detail_pesanan d\n  JOIN pesanan s ON s.id = d.pesanan_id\n  WHERE s.tanggal >= '2024-11-01'\n) nov ON nov.produk_id = pr.id\nWHERE nov.produk_id IS NULL;"),
],
'Self join & cross join': [
  Q('Tampilkan pasangan karyawan yang satu divisi (tanpa memasangkan dengan diri sendiri dan tanpa pasangan ganda).', 'Self join dengan a.id &lt; b.id.',
    'SELECT a.nama AS karyawan1, b.nama AS karyawan2, a.divisi\nFROM karyawan a\nJOIN karyawan b ON a.divisi = b.divisi AND a.id < b.id\nORDER BY a.divisi, a.nama;'),
  Q('Buat semua kombinasi ukuran (S, L) dengan produk Minuman memakai CROSS JOIN.', 'Buat tabel ukuran kecil dengan SELECT ... UNION ALL.',
    "WITH ukuran(u) AS (SELECT 'S' UNION ALL SELECT 'L')\nSELECT pr.nama, ukuran.u\nFROM produk pr\nCROSS JOIN ukuran\nWHERE pr.kategori = 'Minuman'\nORDER BY pr.nama, ukuran.u;"),
],
'JOIN banyak tabel': [
  Q('Tampilkan nama pelanggan, nama produk, dan jumlah untuk semua pesanan berstatus selesai.', 'Gabungkan empat tabel: pesanan, pelanggan, detail_pesanan, produk.',
    "SELECT p.nama AS pelanggan, pr.nama AS produk, d.jumlah\nFROM pesanan s\nJOIN pelanggan p ON p.id = s.pelanggan_id\nJOIN detail_pesanan d ON d.pesanan_id = s.id\nJOIN produk pr ON pr.id = d.produk_id\nWHERE s.status = 'selesai'\nORDER BY p.nama, pr.nama;"),
  Q('Hitung total belanja (jumlah x harga) per kota pelanggan, urut dari terbesar.', 'JOIN empat tabel lalu GROUP BY kota.',
    'SELECT p.kota, SUM(d.jumlah * pr.harga) AS total\nFROM pesanan s\nJOIN pelanggan p ON p.id = s.pelanggan_id\nJOIN detail_pesanan d ON d.pesanan_id = s.id\nJOIN produk pr ON pr.id = d.produk_id\nGROUP BY p.kota\nORDER BY total DESC;'),
],
'Subquery skalar, kolom & tabel': [
  Q('Tampilkan karyawan yang gajinya di atas rata-rata seluruh karyawan.', 'Subquery skalar di WHERE: (SELECT AVG(gaji) FROM karyawan).',
    'SELECT nama, gaji\nFROM karyawan\nWHERE gaji > (SELECT AVG(gaji) FROM karyawan)\nORDER BY gaji DESC;'),
  Q('Tampilkan nama produk beserta selisih harganya dari harga termurah.', 'Subquery skalar di SELECT.',
    'SELECT nama, harga - (SELECT MIN(harga) FROM produk) AS selisih\nFROM produk\nORDER BY selisih;'),
],
'Correlated subquery & EXISTS': [
  Q('Tampilkan produk yang harganya paling mahal di kategorinya masing-masing.', 'Correlated subquery: bandingkan dengan MAX(harga) dari kategori yang sama.',
    'SELECT nama, kategori, harga\nFROM produk p\nWHERE harga = (SELECT MAX(harga) FROM produk WHERE kategori = p.kategori)\nORDER BY kategori;'),
  Q('Tampilkan pelanggan yang belum pernah punya pesanan, memakai NOT EXISTS.', 'NOT EXISTS (SELECT 1 FROM pesanan WHERE pelanggan_id = p.id).',
    'SELECT nama\nFROM pelanggan p\nWHERE NOT EXISTS (SELECT 1 FROM pesanan s WHERE s.pelanggan_id = p.id);'),
],
'Fungsi angka & teks': [
  Q('Buat kode SKU dari 3 huruf pertama kategori (huruf besar), tanda hubung, dan id produk.', 'UPPER, SUBSTRING, dan ||.',
    "SELECT nama, UPPER(SUBSTRING(kategori, 1, 3)) || '-' || id AS sku FROM produk;"),
  Q('Tampilkan nama produk yang panjangnya lebih dari 10 karakter beserta panjangnya.', 'LENGTH(nama).',
    'SELECT nama, LENGTH(nama) AS panjang FROM produk WHERE LENGTH(nama) > 10 ORDER BY panjang DESC;'),
],
'Fungsi tanggal & waktu': [
  Q('Tampilkan nama pelanggan dan lama menjadi member (hari) per 31 Desember 2024.', "DATEDIFF(day, bergabung, '2024-12-31').",
    "SELECT nama, DATEDIFF(day, bergabung, '2024-12-31') AS hari\nFROM pelanggan\nORDER BY hari DESC;"),
  Q('Hitung jumlah pesanan per bulan (format YYYY-MM).', "STRFTIME('%Y-%m', tanggal) lalu GROUP BY.",
    "SELECT STRFTIME('%Y-%m', tanggal) AS bulan, COUNT(*) AS n\nFROM pesanan\nGROUP BY bulan\nORDER BY bulan;"),
],
'CASE, COALESCE & NULLIF': [
  Q('Kelompokkan karyawan: gaji &gt;= 15 juta "Manajemen", &gt;= 8 juta "Senior", selain itu "Staf". Hitung jumlah tiap kelompok.', 'CASE di SELECT, lalu GROUP BY alias.',
    "SELECT CASE WHEN gaji >= 15000000 THEN 'Manajemen'\n            WHEN gaji >= 8000000 THEN 'Senior'\n            ELSE 'Staf' END AS kelompok,\n       COUNT(*) AS n\nFROM karyawan\nGROUP BY kelompok\nORDER BY n DESC;"),
  Q('Tampilkan nama karyawan dan id atasannya; jika tidak punya atasan tulis 0.', 'COALESCE(atasan_id, 0).',
    'SELECT nama, COALESCE(atasan_id, 0) AS atasan FROM karyawan;'),
],
'View: query yang disimpan': [
  Q('Buat view v_ringkas_kategori berisi kategori, jumlah produk, dan total stok, lalu pakai untuk menampilkan kategori dengan stok di atas 100.', 'CREATE VIEW ... AS SELECT ... GROUP BY.',
    'CREATE VIEW v_ringkas_kategori AS\nSELECT kategori, COUNT(*) AS n, SUM(stok) AS total_stok\nFROM produk\nGROUP BY kategori;\nSELECT * FROM v_ringkas_kategori WHERE total_stok > 100;'),
  Tx('Sebutkan tiga manfaat view.', 'Penyederhanaan, keamanan, konsistensi.',
     '1. Menyederhanakan query rumit (JOIN panjang cukup ditulis sekali).\n2. Keamanan: pengguna diberi akses ke view tanpa kolom sensitif.\n3. Konsistensi: definisi metrik yang sama dipakai semua laporan.'),
],
'Index: mempercepat pencarian': [
  Q('Buat index pada kolom kategori di tabel produk, lalu jalankan query yang memanfaatkannya.', 'CREATE INDEX nama ON tabel(kolom).',
    "CREATE INDEX idx_produk_kategori ON produk(kategori);\nSELECT nama FROM produk WHERE kategori = 'Camilan';"),
  Tx('Kapan index justru merugikan?', 'Index harus ikut diperbarui setiap data berubah.',
     'Pada tabel yang sangat sering di-INSERT/UPDATE, index memperlambat penulisan.\nIndex pada kolom dengan sedikit nilai berbeda (misal jenis kelamin) jarang membantu,\ndan setiap index memakan ruang penyimpanan.'),
],
'BEGIN, COMMIT, ROLLBACK & SAVEPOINT': [
  Q('Dalam transaksi, coba kurangi saldo Andi 600.000. Kenapa ditolak, dan apa yang harus dilakukan setelahnya?', 'Saldo Andi hanya 500.000 dan CHECK (saldo &gt;= 0) menolak perubahan. Akhiri dengan ROLLBACK agar transaksi dibatalkan.',
    'BEGIN;\nUPDATE rekening SET saldo = saldo - 600000 WHERE id = 1;'),
  Q('Transfer 100.000 dari Budi ke Andi dalam satu transaksi, lalu tampilkan saldo keduanya.', 'BEGIN, dua UPDATE, COMMIT.',
    'BEGIN;\nUPDATE rekening SET saldo = saldo - 100000 WHERE id = 2;\nUPDATE rekening SET saldo = saldo + 100000 WHERE id = 1;\nCOMMIT;\nSELECT * FROM rekening;'),
],
'ACID & tingkat isolasi': [
  Tx('Jelaskan A, C, I, D dengan contoh transfer bank.', 'Atomicity, Consistency, Isolation, Durability.',
     'Atomicity  : debit dan kredit terjadi bersama atau tidak sama sekali.\nConsistency: total saldo tetap benar dan aturan (saldo >= 0) dijaga.\nIsolation  : transfer lain yang berjalan bersamaan tidak melihat keadaan setengah jadi.\nDurability : setelah COMMIT, hasil tetap ada walau server mati.'),
  Tx('Pasangkan anomali dengan tingkat isolasi yang mencegahnya: dirty read, non-repeatable read, phantom read.', 'READ COMMITTED, REPEATABLE READ, SERIALIZABLE.',
     'Dirty read            : dicegah mulai READ COMMITTED\nNon-repeatable read   : dicegah mulai REPEATABLE READ\nPhantom read          : dicegah SERIALIZABLE'),
],
'GRANT, REVOKE & SQL injection': [
  Tx('Tulis perintah untuk memberi role analis akses baca ke tabel produk dan pesanan, lalu mencabut akses ke pesanan.', 'GRANT ... ON ... TO ...; REVOKE ... ON ... FROM ...;',
     'GRANT SELECT ON produk TO analis;\nGRANT SELECT ON pesanan TO analis;\nREVOKE SELECT ON pesanan FROM analis;'),
  Tx('Input login berisi <code>\' OR \'1\'=\'1</code>. Kenapa query yang dirangkai dengan string berbahaya, dan apa solusinya?', 'Pakai parameter (prepared statement).',
     "Query menjadi: SELECT * FROM pengguna WHERE nama = '' OR '1'='1'\nKondisi selalu benar, sehingga semua baris lolos.\nSolusi: prepared statement / query berparameter, misalnya\nSELECT * FROM pengguna WHERE nama = ? dengan nilai dikirim terpisah."),
],
'Stored procedure & function': [
  Tx('Tulis stored procedure PostgreSQL <code>tambah_stok(p_id, p_jumlah)</code> yang menambah stok produk.', 'CREATE PROCEDURE ... LANGUAGE plpgsql AS $$ BEGIN ... END $$;',
     'CREATE PROCEDURE tambah_stok(p_id INT, p_jumlah INT)\nLANGUAGE plpgsql\nAS $$\nBEGIN\n  UPDATE produk SET stok = stok + p_jumlah WHERE id = p_id;\nEND;\n$$;\n\nCALL tambah_stok(7, 25);'),
  Tx('Kapan logika sebaiknya di stored procedure dan kapan di kode aplikasi?', 'Pertimbangkan dekat-data, pengujian, dan portabilitas.',
     'Stored procedure: operasi berat dekat data, aturan yang harus sama untuk\nsemua aplikasi, mengurangi bolak-balik jaringan.\nKode aplikasi: logika bisnis yang sering berubah, mudah dites dan di-versioning,\ntidak terikat satu merek database.'),
],
'Teknik optimasi query': [
  Q('Tulis ulang query ini agar lebih efisien: <code>SELECT * FROM produk WHERE UPPER(kategori) = \'MINUMAN\'</code>', 'Ambil kolom yang perlu saja dan jangan bungkus kolom berindex dengan fungsi.',
    "SELECT nama, harga FROM produk WHERE kategori = 'Minuman';"),
  Q('Ganti subquery IN dengan EXISTS untuk mencari pelanggan yang pernah memesan.', 'EXISTS berhenti begitu satu baris ditemukan.',
    'SELECT nama\nFROM pelanggan p\nWHERE EXISTS (SELECT 1 FROM pesanan s WHERE s.pelanggan_id = p.id)\nORDER BY nama;'),
],
'CTE: WITH': [
  Q('Dengan CTE, hitung total belanja per pesanan, lalu tampilkan pesanan yang totalnya di atas rata-rata semua pesanan.', 'Dua CTE: total per pesanan, lalu bandingkan dengan AVG.',
    'WITH total AS (\n  SELECT d.pesanan_id, SUM(d.jumlah * pr.harga) AS belanja\n  FROM detail_pesanan d\n  JOIN produk pr ON pr.id = d.produk_id\n  GROUP BY d.pesanan_id\n)\nSELECT pesanan_id, belanja\nFROM total\nWHERE belanja > (SELECT AVG(belanja) FROM total)\nORDER BY belanja DESC;'),
  Q('Dengan CTE, hitung jumlah karyawan per divisi lalu tampilkan divisi terbesar saja.', 'CTE lalu ORDER BY ... LIMIT 1.',
    'WITH per_divisi AS (\n  SELECT divisi, COUNT(*) AS n FROM karyawan GROUP BY divisi\n)\nSELECT divisi, n FROM per_divisi ORDER BY n DESC LIMIT 1;'),
],
'Query rekursif': [
  Q('Dengan WITH RECURSIVE, buat deret angka 1 sampai 5 beserta kuadratnya.', 'Anchor SELECT 1, lalu UNION ALL n + 1 sampai batas.',
    'WITH RECURSIVE angka(n) AS (\n  SELECT 1\n  UNION ALL\n  SELECT n + 1 FROM angka WHERE n < 5\n)\nSELECT n, n * n AS kuadrat FROM angka;'),
  Q('Tampilkan rantai atasan untuk Vino sampai direktur.', 'Mulai dari Vino, lalu naik lewat atasan_id.',
    "WITH RECURSIVE rantai AS (\n  SELECT id, nama, atasan_id, 0 AS naik FROM karyawan WHERE nama = 'Vino'\n  UNION ALL\n  SELECT k.id, k.nama, k.atasan_id, r.naik + 1\n  FROM karyawan k JOIN rantai r ON k.id = r.atasan_id\n)\nSELECT naik, nama FROM rantai ORDER BY naik;"),
],
'Window function: ROW_NUMBER, RANK, DENSE_RANK': [
  Q('Tampilkan karyawan dengan gaji tertinggi di setiap divisi memakai ROW_NUMBER.', 'PARTITION BY divisi ORDER BY gaji DESC, lalu ambil no = 1.',
    'WITH urut AS (\n  SELECT nama, divisi, gaji,\n         ROW_NUMBER() OVER (PARTITION BY divisi ORDER BY gaji DESC) AS no\n  FROM karyawan\n)\nSELECT divisi, nama, gaji FROM urut WHERE no = 1 ORDER BY divisi;'),
  Q('Tampilkan gaji semua karyawan beserta RANK dan DENSE_RANK. Kenapa angkanya berbeda setelah ada gaji yang sama?', 'Nilai yang sama mendapat peringkat sama; RANK melompati angka berikutnya.',
    "SELECT nama, gaji,\n  RANK() OVER (ORDER BY gaji DESC) AS rnk,\n  DENSE_RANK() OVER (ORDER BY gaji DESC) AS dense\nFROM karyawan\nORDER BY rnk, nama;"),
],
'LEAD, LAG & running total': [
  Q('Tampilkan gaji karyawan divisi Penjualan urut dari kecil, beserta total kumulatifnya.', 'SUM(gaji) OVER (ORDER BY ...).',
    "SELECT nama, gaji,\n  SUM(gaji) OVER (ORDER BY gaji, nama) AS kumulatif\nFROM karyawan\nWHERE divisi = 'Penjualan'\nORDER BY gaji, nama;"),
  Q('Tampilkan produk urut harga, beserta harga produk berikutnya yang lebih mahal dan selisihnya.', 'LEAD(harga) OVER (ORDER BY harga).',
    'SELECT nama, harga,\n  LEAD(harga) OVER (ORDER BY harga) AS berikutnya,\n  LEAD(harga) OVER (ORDER BY harga) - harga AS selisih\nFROM produk\nORDER BY harga;'),
],
'Pivot, unpivot & dynamic SQL': [
  Q('Buat pivot jumlah karyawan per divisi menjadi satu baris (kolom gudang, penjualan, pusat).', 'SUM(CASE WHEN divisi = ... THEN 1 ELSE 0 END).',
    "SELECT\n  SUM(CASE WHEN divisi = 'Gudang' THEN 1 ELSE 0 END) AS gudang,\n  SUM(CASE WHEN divisi = 'Penjualan' THEN 1 ELSE 0 END) AS penjualan,\n  SUM(CASE WHEN divisi = 'Pusat' THEN 1 ELSE 0 END) AS pusat\nFROM karyawan;"),
  Q('Unpivot data Madu Hutan: ubah kolom harga dan stok menjadi baris (atribut, nilai).', 'Dua SELECT digabung UNION ALL.',
    "SELECT nama, 'harga' AS atribut, harga AS nilai FROM produk WHERE nama = 'Madu Hutan'\nUNION ALL\nSELECT nama, 'stok', stok FROM produk WHERE nama = 'Madu Hutan';"),
],
}

# keluaran hasil menjalankan jawaban di mesin SQL situs (dibuat oleh isi_sql.py)
import json as _json, os as _os
_OUT = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'soal_sql_out.json'), encoding='utf-8'))
for _t, _L in SQL.items():
    for _i, _s in enumerate(_L):
        if _s.get('out') == 'RUN':
            _s['out'] = _OUT[f'{_t}#{_i}']

SOAL = {'SQL_MODULES': SQL}
