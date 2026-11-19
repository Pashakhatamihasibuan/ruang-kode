"""Pendalaman jalur SQL: istilah dunia kerja dan contoh tambahan (dijalankan di SQLite)."""
K = 'sql'

TOKO = """CREATE TABLE pelanggan (id INTEGER PRIMARY KEY, nama TEXT NOT NULL, kota TEXT, bergabung DATE);
CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT NOT NULL, kategori TEXT, harga INTEGER CHECK (harga > 0), stok INTEGER DEFAULT 0);
CREATE TABLE pesanan (id INTEGER PRIMARY KEY, pelanggan_id INTEGER REFERENCES pelanggan(id), tanggal DATE, status TEXT);
CREATE TABLE detail (pesanan_id INTEGER REFERENCES pesanan(id), produk_id INTEGER REFERENCES produk(id), qty INTEGER, harga INTEGER);
INSERT INTO pelanggan VALUES (1,'Sari','Medan','2025-11-02'),(2,'Budi','Jakarta','2026-01-15'),(3,'Ayu','Bandung','2026-02-20'),
 (4,'Rizki','Jakarta','2026-03-05'),(5,'Dewi','Surabaya','2026-04-11'),(6,'Fajar',NULL,'2026-06-30');
INSERT INTO produk VALUES (1,'Kopi Gayo 250g','Kopi',85000,40),(2,'Kopi Toraja 250g','Kopi',92000,0),(3,'Teh Melati','Teh',35000,120),
 (4,'Gula Aren 500g','Pelengkap',28000,75),(5,'French Press','Alat',210000,8),(6,'Filter V60','Alat',145000,15),(7,'Teh Hijau','Teh',42000,60);
INSERT INTO pesanan VALUES (101,1,'2026-09-03','selesai'),(102,2,'2026-09-10','selesai'),(103,1,'2026-09-21','selesai'),(104,3,'2026-10-02','batal'),
 (105,4,'2026-10-08','selesai'),(106,2,'2026-10-15','dikirim'),(107,5,'2026-10-28','selesai'),(108,1,'2026-11-04','dikirim');
INSERT INTO detail VALUES (101,1,2,85000),(101,4,1,28000),(102,5,1,210000),(103,1,1,85000),(103,3,3,35000),(104,6,1,145000),
 (105,2,2,92000),(105,4,2,28000),(106,7,4,42000),(107,1,1,85000),(107,6,1,145000),(108,3,2,35000),(108,1,3,85000);"""


def X(t, code, b=None, setup=TOKO, run=True):
    return dict(t=t, b=b, code=code, lang='sql', setup=setup if run else '', run=run)


D = {
'Basis data relasional: tabel, baris, kolom': dict(
  ist=[('Schema', 'Rancangan struktur database: tabel apa saja, kolomnya, tipe datanya, dan relasinya.'),
       ('Record / row', 'Satu baris data, misalnya satu pelanggan atau satu pesanan.'),
       ('Entity', 'Benda nyata yang dicatat sistem, misalnya Pelanggan atau Produk; biasanya menjadi satu tabel.'),
       ('Single source of truth', 'Satu sumber data resmi yang dipakai semua tim agar angka tidak berbeda-beda.')],
  cx=[X('Melihat isi tabel pertama kali', "SELECT * FROM pelanggan;", 'Langkah pertama analis saat menerima database baru: lihat sampel isinya.')]),
'Kelebihan RDBMS & SQL lawan NoSQL': dict(
  ist=[('RDBMS', 'Relational Database Management System: PostgreSQL, MySQL, SQL Server, Oracle, SQLite.'),
       ('NoSQL', 'Database non-relasional: dokumen (MongoDB), key-value (Redis), kolom lebar (Cassandra), graf (Neo4j).'),
       ('Schema-on-write', 'Struktur dicek saat data ditulis (RDBMS); kebalikannya schema-on-read (banyak NoSQL).'),
       ('Polyglot persistence', 'Memakai lebih dari satu jenis database dalam satu sistem sesuai kebutuhan.')],
  cx=[X('Constraint menolak data yang salah', "INSERT INTO produk (id, nama, kategori, harga) VALUES (99, 'Kopi Rusak', 'Kopi', -5000);",
        'RDBMS menjaga aturan data. Harga negatif ditolak oleh CHECK, sesuatu yang tidak otomatis di banyak NoSQL.', run=False)]),
'Sintaks & kata kunci SQL': dict(
  ist=[('DDL', 'Data Definition Language: CREATE, ALTER, DROP. Mengubah struktur.'),
       ('DML', 'Data Manipulation Language: SELECT, INSERT, UPDATE, DELETE. Mengubah atau membaca isi.'),
       ('DCL / TCL', 'DCL mengatur hak akses (GRANT, REVOKE); TCL mengatur transaksi (COMMIT, ROLLBACK).'),
       ('SQL style guide', 'Aturan penulisan tim: kata kunci huruf besar, satu klausa per baris, alias jelas.')],
  cx=[X('Query yang rapi sesuai style guide', "SELECT nama,\n       kategori,\n       harga\nFROM produk\nWHERE kategori = 'Kopi'\nORDER BY harga DESC;",
        'Satu klausa per baris memudahkan code review dan membaca diff di Git.')]),
'Tipe data': dict(
  ist=[('NUMERIC / DECIMAL', 'Tipe angka presisi tetap; wajib untuk uang agar tidak ada galat pembulatan.'),
       ('VARCHAR(n) / TEXT', 'Teks dengan atau tanpa batas panjang.'),
       ('TIMESTAMP WITH TIME ZONE', 'Waktu lengkap dengan zona; standar untuk log dan transaksi lintas wilayah (WIB, WITA, WIT).'),
       ('Type affinity', 'Di SQLite, tipe kolom hanya preferensi; PostgreSQL jauh lebih ketat.')],
  cx=[X('Mengapa uang tidak disimpan sebagai float', "SELECT 0.1 + 0.2 AS hasil_float,\n       0.1 + 0.2 = 0.3 AS sama_dengan_03,\n       (10 + 20) / 100.0 AS hasil_dalam_sen;",
        'Float tidak bisa menyimpan 0,1 dengan tepat. Simpan uang sebagai bilangan bulat (sen/rupiah) atau DECIMAL.', setup='')]),
'Operator': dict(
  ist=[('Predicate', 'Ekspresi yang bernilai benar/salah, misalnya harga > 50000.'),
       ('Three-valued logic', 'SQL punya TRUE, FALSE, dan UNKNOWN (karena NULL).'),
       ('Sargable', 'Kondisi yang bisa memakai index; WHERE harga > 50000 sargable, WHERE harga*2 > 100000 tidak.'),
       ('Wildcard', 'Karakter pengganti di LIKE: % untuk banyak karakter, _ untuk satu karakter.')],
  cx=[X('BETWEEN, IN, LIKE dalam satu query', "SELECT nama, kategori, harga\nFROM produk\nWHERE harga BETWEEN 30000 AND 150000\n  AND kategori IN ('Kopi', 'Alat')\n  AND nama LIKE '%0%';")]),
'SELECT & FROM': dict(
  ist=[('Projection', 'Memilih kolom tertentu saja (bukan SELECT *).'),
       ('Alias', 'Nama sementara untuk kolom atau tabel dengan AS.'),
       ('Computed column', 'Kolom hasil hitungan di query, misalnya harga * stok.'),
       ('SELECT * di produksi', 'Dihindari karena boros dan rapuh saat kolom tabel berubah.')],
  cx=[X('Nilai persediaan per produk', "SELECT nama,\n       harga,\n       stok,\n       harga * stok AS nilai_persediaan\nFROM produk;")]),
'WHERE: menyaring baris': dict(
  ist=[('Filter', 'Kondisi yang menyaring baris sebelum dikelompokkan.'),
       ('IS NULL', 'Satu-satunya cara benar mengecek NULL; = NULL selalu UNKNOWN.'),
       ('Selectivity', 'Seberapa sedikit baris yang lolos filter; makin selektif makin berguna index-nya.'),
       ('Hard-coded value', 'Nilai yang ditulis langsung di query; di aplikasi diganti parameter (?).')],
  cx=[X('Jebakan NULL', "SELECT nama, kota FROM pelanggan WHERE kota = NULL;\nSELECT nama, kota FROM pelanggan WHERE kota IS NULL;",
        'Query pertama tidak mengembalikan apa-apa. Fajar belum mengisi kota, dan hanya IS NULL yang menemukannya.')]),
'ORDER BY, LIMIT & DISTINCT': dict(
  ist=[('Pagination', 'Membagi hasil per halaman dengan LIMIT dan OFFSET (atau keyset pagination).'),
       ('Keyset pagination', 'WHERE id > id_terakhir LIMIT 20; jauh lebih cepat dari OFFSET besar.'),
       ('Top-N query', 'Mengambil N teratas, misalnya 5 produk termahal.'),
       ('Deterministic ordering', 'Urutan pasti; tambahkan kolom unik (id) sebagai pemecah seri.')],
  cx=[X('Halaman 2 dengan keyset pagination', "-- halaman 1\nSELECT id, nama FROM produk ORDER BY id LIMIT 3;\n-- halaman 2: mulai setelah id terakhir halaman 1 (3)\nSELECT id, nama FROM produk WHERE id > 3 ORDER BY id LIMIT 3;")]),
'Urutan eksekusi query': dict(
  ist=[('Logical query processing', 'Urutan logis: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.'),
       ('Query planner / optimizer', 'Bagian database yang memilih cara tercepat mengeksekusi query.'),
       ('Execution plan', 'Rencana eksekusi yang bisa dilihat dengan EXPLAIN.'),
       ('Alias scope', 'Alias dari SELECT belum dikenal di WHERE karena WHERE dievaluasi lebih dulu.')],
  cx=[X('Melihat rencana eksekusi', "EXPLAIN QUERY PLAN\nSELECT nama FROM produk WHERE kategori = 'Kopi' ORDER BY harga;",
        'Di PostgreSQL gunakan EXPLAIN ANALYZE. Kata SCAN berarti seluruh tabel dibaca, dan "TEMP B-TREE" berarti ada pengurutan tambahan.')]),
'Proyek mini: Katalog Toko Nusantara': dict(
  ist=[('Product catalog', 'Daftar produk dengan atribut (kategori, harga, stok) yang ditampilkan ke pelanggan.'),
       ('SKU', 'Stock Keeping Unit: kode unik tiap varian produk.'),
       ('Out of stock (OOS)', 'Stok habis; biasanya disembunyikan atau diberi label di katalog.'),
       ('Requirement', 'Kebutuhan yang ditulis jelas sebelum query dibuat.')],
  cx=[X('Katalog siap tampil: tersedia dulu, lalu termurah', "SELECT nama,\n       kategori,\n       harga,\n       CASE WHEN stok = 0 THEN 'Habis' ELSE 'Tersedia' END AS status\nFROM produk\nORDER BY stok = 0, harga;")]),
'INSERT: menambah baris': dict(
  ist=[('Bulk insert', 'Memasukkan banyak baris dalam satu perintah; jauh lebih cepat dari satu per satu.'),
       ('Upsert', 'Insert atau update jika sudah ada: ON CONFLICT ... DO UPDATE (PostgreSQL, SQLite).'),
       ('RETURNING', 'Mengembalikan baris yang baru dibuat, misalnya id hasil auto increment.'),
       ('Seed data', 'Data awal untuk pengembangan dan pengujian.')],
  cx=[X('Upsert stok dari pemasok', "INSERT INTO produk (id, nama, kategori, harga, stok)\nVALUES (3, 'Teh Melati', 'Teh', 35000, 30), (8, 'Teh Rosella', 'Teh', 39000, 25)\nON CONFLICT (id) DO UPDATE SET stok = produk.stok + excluded.stok;\nSELECT id, nama, stok FROM produk WHERE kategori = 'Teh';",
        'Produk 3 sudah ada, jadi stoknya ditambah. Produk 8 belum ada, jadi baris baru dibuat.')]),
'UPDATE & DELETE': dict(
  ist=[('Soft delete', 'Menandai baris terhapus (deleted_at) alih-alih menghapus fisik; data bisa dipulihkan dan diaudit.'),
       ('Hard delete', 'Menghapus baris sungguhan dengan DELETE.'),
       ('Safe update', 'Selalu jalankan SELECT dengan WHERE yang sama sebelum UPDATE/DELETE.'),
       ('Audit trail', 'Catatan siapa mengubah apa dan kapan.')],
  cx=[X('Cek dulu, baru ubah', "-- 1) lihat baris yang akan terkena\nSELECT id, nama, harga FROM produk WHERE kategori = 'Alat';\n-- 2) naikkan harga alat 5%\nUPDATE produk SET harga = CAST(harga * 1.05 AS INTEGER) WHERE kategori = 'Alat';\nSELECT id, nama, harga FROM produk WHERE kategori = 'Alat';")]),
'Fungsi agregat': dict(
  ist=[('KPI', 'Key Performance Indicator, misalnya omzet, jumlah pesanan, nilai rata-rata pesanan (AOV).'),
       ('AOV', 'Average Order Value: omzet dibagi jumlah pesanan.'),
       ('COUNT(*) vs COUNT(kolom)', 'COUNT(*) menghitung semua baris; COUNT(kolom) melewati NULL.'),
       ('Grand total', 'Total keseluruhan di baris paling bawah laporan.')],
  cx=[X('KPI penjualan dalam satu query', "SELECT COUNT(DISTINCT pesanan_id) AS pesanan,\n       SUM(qty * harga) AS omzet,\n       SUM(qty * harga) / COUNT(DISTINCT pesanan_id) AS aov\nFROM detail\nWHERE pesanan_id IN (SELECT id FROM pesanan WHERE status <> 'batal');")]),
'GROUP BY': dict(
  ist=[('Granularity / grain', 'Tingkat detail satu baris hasil, misalnya per kategori per bulan.'),
       ('Dimension', 'Kolom untuk mengelompokkan (kategori, kota, bulan).'),
       ('Measure / metric', 'Angka yang diagregasi (SUM omzet, COUNT pesanan).'),
       ('Rollup', 'Subtotal bertingkat; di PostgreSQL GROUP BY ROLLUP(...).')],
  cx=[X('Omzet per kategori per bulan', "SELECT strftime('%Y-%m', p.tanggal) AS bulan,\n       pr.kategori,\n       SUM(d.qty * d.harga) AS omzet\nFROM detail d\nJOIN pesanan p ON p.id = d.pesanan_id\nJOIN produk pr ON pr.id = d.produk_id\nWHERE p.status <> 'batal'\nGROUP BY bulan, pr.kategori\nORDER BY bulan, omzet DESC;")]),
'HAVING': dict(
  ist=[('Post-aggregation filter', 'Filter setelah agregasi; WHERE sebelum, HAVING sesudah.'),
       ('Threshold', 'Ambang batas, misalnya pelanggan dengan belanja di atas Rp200.000.'),
       ('Repeat customer', 'Pelanggan yang membeli lebih dari sekali.'),
       ('Segmentasi', 'Mengelompokkan pelanggan berdasarkan perilaku.')],
  cx=[X('Pelanggan repeat order', "SELECT pelanggan_id, COUNT(*) AS jumlah_pesanan\nFROM pesanan\nWHERE status <> 'batal'\nGROUP BY pelanggan_id\nHAVING COUNT(*) >= 2;")]),
'Proyek mini: Ringkasan stok gudang': dict(
  ist=[('Reorder point', 'Batas stok minimum yang memicu pemesanan ulang.'),
       ('Safety stock', 'Stok cadangan untuk berjaga dari lonjakan permintaan.'),
       ('Inventory value', 'Nilai persediaan = harga × stok.'),
       ('Stock-out rate', 'Persentase produk yang stoknya habis.')],
  cx=[X('Laporan gudang dengan status pemesanan ulang', "SELECT kategori,\n       COUNT(*) AS produk,\n       SUM(stok) AS total_stok,\n       SUM(harga * stok) AS nilai_persediaan,\n       SUM(CASE WHEN stok < 20 THEN 1 ELSE 0 END) AS perlu_pesan_ulang\nFROM produk\nGROUP BY kategori\nORDER BY nilai_persediaan DESC;")]),
'CREATE TABLE': dict(
  ist=[('Migration', 'Berkas perubahan skema bernomor yang dijalankan berurutan (Flyway, Liquibase, Alembic, Django migrations).'),
       ('Naming convention', 'Aturan penamaan: snake_case, tabel jamak/tunggal konsisten, kolom FK berakhiran _id.'),
       ('Surrogate key', 'Kunci buatan (id auto increment/UUID) yang tidak bermakna bisnis.'),
       ('Natural key', 'Kunci dari data bisnis, misalnya NIK atau kode SKU.')],
  cx=[X('Tabel dengan constraint lengkap', "CREATE TABLE kupon (\n  id INTEGER PRIMARY KEY,\n  kode TEXT NOT NULL UNIQUE,\n  diskon_persen INTEGER NOT NULL CHECK (diskon_persen BETWEEN 1 AND 90),\n  berlaku_sampai DATE NOT NULL,\n  dibuat_pada TEXT DEFAULT CURRENT_TIMESTAMP\n);\nINSERT INTO kupon (id, kode, diskon_persen, berlaku_sampai) VALUES (1, 'HARBOLNAS', 12, '2026-12-12');\nSELECT id, kode, diskon_persen, berlaku_sampai FROM kupon;", setup='')]),
'ALTER, DROP & TRUNCATE': dict(
  ist=[('Schema change', 'Perubahan struktur tabel di database yang sedang dipakai.'),
       ('Backward-compatible migration', 'Perubahan yang tidak merusak versi aplikasi lama: tambah kolom nullable dulu, isi, baru wajibkan.'),
       ('Expand-contract', 'Pola migrasi tanpa downtime: perluas skema, pindahkan data, lalu hapus yang lama.'),
       ('Destructive operation', 'DROP/TRUNCATE; wajib backup dan persetujuan.')],
  cx=[X('Menambah kolom tanpa merusak aplikasi lama', "ALTER TABLE produk ADD COLUMN berat_gram INTEGER;\nUPDATE produk SET berat_gram = 250 WHERE nama LIKE '%250g%';\nSELECT nama, berat_gram FROM produk WHERE kategori = 'Kopi';",
        'Kolom baru dibuat boleh NULL dulu. Aplikasi lama tetap jalan, lalu data diisi bertahap.')]),
'Primary key & foreign key': dict(
  ist=[('Referential integrity', 'Jaminan bahwa setiap foreign key menunjuk baris yang benar-benar ada.'),
       ('ON DELETE CASCADE / RESTRICT', 'Aturan saat baris induk dihapus: ikut hapus anak, atau tolak.'),
       ('Orphan record', 'Baris anak yang induknya sudah tidak ada.'),
       ('ERD', 'Entity Relationship Diagram: gambar tabel dan relasinya.')],
  cx=[X('Mendeteksi orphan record', "INSERT INTO detail VALUES (999, 1, 1, 85000);\nSELECT d.pesanan_id, d.produk_id\nFROM detail d\nLEFT JOIN pesanan p ON p.id = d.pesanan_id\nWHERE p.id IS NULL;",
        'SQLite tidak menegakkan foreign key secara bawaan (perlu PRAGMA foreign_keys = ON). Query ini adalah cara audit data yang sudah terlanjur kotor.')]),
'UNIQUE, NOT NULL & CHECK': dict(
  ist=[('Data integrity', 'Data benar dan konsisten; dijaga di database, bukan hanya di aplikasi.'),
       ('Business rule', 'Aturan bisnis, misalnya diskon maksimal 90%.'),
       ('Composite unique', 'Kombinasi kolom yang harus unik, misalnya (pesanan_id, produk_id).'),
       ('Defense in depth', 'Validasi berlapis: frontend, backend, dan database.')],
  cx=[X('Constraint menangkap kesalahan', "CREATE TABLE akun (email TEXT NOT NULL UNIQUE, saldo INTEGER NOT NULL CHECK (saldo >= 0));\nINSERT INTO akun VALUES ('sari@contoh.id', 50000);\nINSERT OR IGNORE INTO akun VALUES ('sari@contoh.id', 10000);\nSELECT * FROM akun;",
        'Email duplikat diabaikan karena UNIQUE. Tanpa OR IGNORE, database akan menolak dengan error constraint.', setup='')]),
'INNER JOIN': dict(
  ist=[('Join key', 'Kolom penghubung dua tabel, biasanya PK dan FK.'),
       ('Fan-out', 'Baris berlipat karena relasi satu-ke-banyak; penyebab angka SUM membengkak.'),
       ('Lookup', 'Mengambil atribut dari tabel referensi (nama produk dari id).'),
       ('Equi-join', 'JOIN dengan kondisi sama dengan (=).')],
  cx=[X('Detail pesanan yang bisa dibaca manusia', "SELECT p.id AS pesanan, pl.nama AS pelanggan, pr.nama AS produk, d.qty, d.qty * d.harga AS subtotal\nFROM detail d\nJOIN pesanan p ON p.id = d.pesanan_id\nJOIN pelanggan pl ON pl.id = p.pelanggan_id\nJOIN produk pr ON pr.id = d.produk_id\nWHERE p.id IN (101, 103);")]),
'LEFT, RIGHT & FULL OUTER JOIN': dict(
  ist=[('Anti-join', 'Mencari baris yang TIDAK punya pasangan: LEFT JOIN ... WHERE kanan.id IS NULL.'),
       ('Preserved table', 'Tabel yang semua barisnya dipertahankan dalam outer join.'),
       ('Data reconciliation', 'Mencocokkan dua sumber data untuk menemukan selisih; FULL OUTER JOIN berguna di sini.'),
       ('Dormant customer', 'Pelanggan terdaftar yang belum/tidak lagi bertransaksi.')],
  cx=[X('Pelanggan yang belum pernah memesan (anti-join)', "SELECT pl.nama, pl.bergabung\nFROM pelanggan pl\nLEFT JOIN pesanan p ON p.pelanggan_id = pl.id\nWHERE p.id IS NULL;")]),
'Self join & cross join': dict(
  ist=[('Hierarchy', 'Struktur atasan-bawahan dalam satu tabel (manager_id).'),
       ('Cartesian product', 'Semua kombinasi baris dua tabel; hasil CROSS JOIN.'),
       ('Scaffold table', 'Tabel kerangka (semua tanggal × semua produk) agar hari tanpa penjualan tetap muncul.'),
       ('Market basket', 'Analisis produk yang sering dibeli bersama; contoh klasik self join.')],
  cx=[X('Produk yang dibeli bersama (self join)', "SELECT a.produk_id AS produk_a, b.produk_id AS produk_b, COUNT(*) AS kali_bersama\nFROM detail a\nJOIN detail b ON a.pesanan_id = b.pesanan_id AND a.produk_id < b.produk_id\nGROUP BY a.produk_id, b.produk_id\nORDER BY kali_bersama DESC\nLIMIT 5;")]),
'JOIN banyak tabel': dict(
  ist=[('Star schema', 'Satu tabel fakta dikelilingi tabel dimensi; pola gudang data.'),
       ('Fact table', 'Tabel peristiwa terukur (detail penjualan).'),
       ('Dimension table', 'Tabel atribut deskriptif (produk, pelanggan, tanggal).'),
       ('Join order', 'Urutan join; ditentukan optimizer, tetapi tulislah dari fakta ke dimensi agar mudah dibaca.')],
  cx=[X('Omzet per kota per kategori', "SELECT COALESCE(pl.kota, '(kosong)') AS kota, pr.kategori, SUM(d.qty * d.harga) AS omzet\nFROM detail d\nJOIN pesanan p ON p.id = d.pesanan_id AND p.status <> 'batal'\nJOIN pelanggan pl ON pl.id = p.pelanggan_id\nJOIN produk pr ON pr.id = d.produk_id\nGROUP BY kota, pr.kategori\nORDER BY omzet DESC;")]),
'Proyek mini: Laporan pesanan pelanggan': dict(
  ist=[('Customer 360', 'Pandangan lengkap satu pelanggan: profil, pesanan, nilai belanja.'),
       ('Lifetime value (LTV)', 'Total nilai belanja pelanggan selama menjadi pelanggan.'),
       ('Last order date', 'Tanggal pesanan terakhir; dasar recency.'),
       ('Ad-hoc report', 'Laporan sekali jalan untuk pertanyaan mendadak.')],
  cx=[X('Ringkasan per pelanggan', "SELECT pl.nama,\n       COUNT(DISTINCT p.id) AS pesanan,\n       COALESCE(SUM(d.qty * d.harga), 0) AS ltv,\n       MAX(p.tanggal) AS terakhir\nFROM pelanggan pl\nLEFT JOIN pesanan p ON p.pelanggan_id = pl.id AND p.status <> 'batal'\nLEFT JOIN detail d ON d.pesanan_id = p.id\nGROUP BY pl.id\nORDER BY ltv DESC;",
        'Perhatikan filter status ditaruh di ON, bukan WHERE, agar pelanggan tanpa pesanan tetap muncul.')]),
'Subquery skalar, kolom & tabel': dict(
  ist=[('Scalar subquery', 'Subquery yang menghasilkan satu nilai.'),
       ('Derived table', 'Subquery di FROM yang diperlakukan sebagai tabel.'),
       ('Inline view', 'Nama lain derived table.'),
       ('Benchmark', 'Nilai pembanding, misalnya rata-rata harga kategori.')],
  cx=[X('Produk di atas rata-rata harga', "SELECT nama, harga,\n       (SELECT ROUND(AVG(harga)) FROM produk) AS rata_rata\nFROM produk\nWHERE harga > (SELECT AVG(harga) FROM produk);")]),
'Correlated subquery & EXISTS': dict(
  ist=[('Correlated subquery', 'Subquery yang merujuk kolom query luar; dievaluasi per baris.'),
       ('Semi-join', 'EXISTS: cukup tahu ada pasangan, tanpa menggandakan baris.'),
       ('Short-circuit', 'EXISTS berhenti di baris pertama yang cocok.'),
       ('NOT IN dan NULL', 'NOT IN dengan subquery yang mengandung NULL menghasilkan kosong; pakai NOT EXISTS.')],
  cx=[X('Produk termahal di setiap kategori', "SELECT kategori, nama, harga\nFROM produk p\nWHERE harga = (SELECT MAX(harga) FROM produk WHERE kategori = p.kategori)\nORDER BY kategori;"),
      X('Pelanggan yang pernah membeli alat', "SELECT nama FROM pelanggan pl\nWHERE EXISTS (\n  SELECT 1 FROM pesanan p JOIN detail d ON d.pesanan_id = p.id\n  JOIN produk pr ON pr.id = d.produk_id\n  WHERE p.pelanggan_id = pl.id AND pr.kategori = 'Alat'\n);")]),
'Proyek mini: Mencari produk istimewa': dict(
  ist=[('Best seller', 'Produk dengan penjualan tertinggi.'),
       ('Slow-moving', 'Produk yang lambat terjual; kandidat diskon.'),
       ('Dead stock', 'Stok yang tidak terjual sama sekali dalam periode tertentu.'),
       ('Pareto 80/20', 'Sebagian kecil produk sering menyumbang sebagian besar omzet.')],
  cx=[X('Dead stock: ada stok tetapi tidak pernah terjual', "SELECT nama, stok, harga * stok AS modal_tertahan\nFROM produk pr\nWHERE stok > 0\n  AND NOT EXISTS (SELECT 1 FROM detail d WHERE d.produk_id = pr.id);")]),
'Fungsi angka & teks': dict(
  ist=[('Data cleansing', 'Merapikan data: spasi berlebih, huruf besar-kecil, format angka.'),
       ('String normalization', 'Menyeragamkan teks, misalnya TRIM + LOWER sebelum membandingkan.'),
       ('Rounding rule', 'Aturan pembulatan yang disepakati bagian keuangan.'),
       ('Concatenation', 'Menggabungkan teks; || di SQL standar, CONCAT di MySQL.')],
  cx=[X('Membuat kode SKU dan label harga', "SELECT UPPER(SUBSTR(kategori, 1, 3)) || '-' || printf('%03d', id) AS sku,\n       nama,\n       'Rp' || replace(printf('%,d', harga), ',', '.') AS label_harga\nFROM produk;")]),
'Fungsi tanggal & waktu': dict(
  ist=[('Cohort', 'Kelompok pelanggan berdasarkan bulan bergabung.'),
       ('Date truncation', 'Memotong tanggal ke awal bulan/minggu: date_trunc di PostgreSQL, strftime di SQLite.'),
       ('Timezone', 'Simpan dalam UTC, tampilkan dalam zona pengguna (Asia/Jakarta).'),
       ('Days since last order', 'Selisih hari sejak pesanan terakhir; dasar churn dan recency.')],
  cx=[X('Hari sejak pesanan terakhir per pelanggan', "SELECT pl.nama,\n       MAX(p.tanggal) AS terakhir,\n       CAST(julianday('2026-11-19') - julianday(MAX(p.tanggal)) AS INTEGER) AS hari_sejak\nFROM pelanggan pl JOIN pesanan p ON p.pelanggan_id = pl.id\nGROUP BY pl.id\nORDER BY hari_sejak;")]),
'CASE, COALESCE & NULLIF': dict(
  ist=[('Bucketing', 'Mengelompokkan nilai ke rentang (murah, sedang, mahal) dengan CASE.'),
       ('Default value', 'Nilai pengganti NULL dengan COALESCE.'),
       ('Division by zero', 'Dicegah dengan NULLIF(pembagi, 0).'),
       ('Conditional aggregation', 'SUM(CASE WHEN ... THEN ... END) untuk pivot sederhana.')],
  cx=[X('Conditional aggregation: status pesanan per pelanggan', "SELECT pelanggan_id,\n       SUM(CASE WHEN status = 'selesai' THEN 1 ELSE 0 END) AS selesai,\n       SUM(CASE WHEN status = 'dikirim' THEN 1 ELSE 0 END) AS dikirim,\n       SUM(CASE WHEN status = 'batal' THEN 1 ELSE 0 END) AS batal,\n       ROUND(100.0 * SUM(status = 'batal') / NULLIF(COUNT(*), 0), 1) AS persen_batal\nFROM pesanan\nGROUP BY pelanggan_id;")]),
'Proyek mini: Merapikan laporan': dict(
  ist=[('Presentation layer', 'Lapisan tampilan; format angka sering lebih baik di BI tool daripada di SQL.'),
       ('Report-ready table', 'Tabel yang sudah siap ditampilkan tanpa olahan lagi.'),
       ('Label mapping', 'Mengubah kode menjadi label yang dipahami pembaca.'),
       ('Data dictionary', 'Dokumen arti tiap kolom dan metrik.')],
  cx=[X('Laporan status pesanan yang siap dibaca', "SELECT p.id AS 'No. Pesanan',\n       COALESCE(pl.kota, 'Belum diisi') AS Kota,\n       CASE p.status WHEN 'selesai' THEN 'Selesai' WHEN 'dikirim' THEN 'Dalam pengiriman' ELSE 'Dibatalkan' END AS Status\nFROM pesanan p JOIN pelanggan pl ON pl.id = p.pelanggan_id\nORDER BY p.tanggal DESC LIMIT 4;")]),
'View: query yang disimpan': dict(
  ist=[('Semantic layer', 'Lapisan definisi metrik bersama agar semua dashboard memakai rumus yang sama.'),
       ('Materialized view', 'View yang hasilnya disimpan fisik dan di-refresh berkala (PostgreSQL).'),
       ('Abstraction', 'Menyembunyikan kerumitan join di balik nama yang sederhana.'),
       ('Access control lewat view', 'Memberi akses ke view tanpa memberi akses ke tabel mentah.')],
  cx=[X('View penjualan bersih untuk tim BI', "CREATE VIEW v_penjualan AS\nSELECT p.tanggal, pl.kota, pr.kategori, d.qty * d.harga AS nilai\nFROM detail d\nJOIN pesanan p ON p.id = d.pesanan_id AND p.status <> 'batal'\nJOIN pelanggan pl ON pl.id = p.pelanggan_id\nJOIN produk pr ON pr.id = d.produk_id;\n\nSELECT kategori, SUM(nilai) AS omzet FROM v_penjualan GROUP BY kategori ORDER BY omzet DESC;")]),
'Index: mempercepat pencarian': dict(
  ist=[('B-tree index', 'Jenis index paling umum; cocok untuk =, <, >, ORDER BY.'),
       ('Covering index', 'Index yang memuat semua kolom yang dibutuhkan query; tabel tidak perlu dibaca.'),
       ('Composite index', 'Index beberapa kolom; urutan kolom penting (leftmost prefix).'),
       ('Write amplification', 'Setiap index menambah biaya INSERT/UPDATE.')],
  cx=[X('Rencana eksekusi sebelum dan sesudah index', "EXPLAIN QUERY PLAN SELECT * FROM pesanan WHERE pelanggan_id = 1;\nCREATE INDEX idx_pesanan_pelanggan ON pesanan(pelanggan_id);\nEXPLAIN QUERY PLAN SELECT * FROM pesanan WHERE pelanggan_id = 1;",
        'Sebelum index tertulis SCAN (baca seluruh tabel). Sesudahnya SEARCH ... USING INDEX.')]),
'BEGIN, COMMIT, ROLLBACK & SAVEPOINT': dict(
  ist=[('Unit of work', 'Sekumpulan perubahan yang harus berhasil semua atau gagal semua.'),
       ('Atomicity', 'Sifat "semua atau tidak sama sekali".'),
       ('Long-running transaction', 'Transaksi yang terlalu lama; mengunci data dan memperlambat sistem.'),
       ('Idempotent', 'Operasi yang aman diulang tanpa efek ganda (penting saat retry).')],
  cx=[X('Checkout: stok berkurang dan pesanan tercatat bersama', "BEGIN;\nINSERT INTO pesanan VALUES (109, 2, '2026-11-19', 'dibayar');\nINSERT INTO detail VALUES (109, 5, 1, 210000);\nUPDATE produk SET stok = stok - 1 WHERE id = 5;\nCOMMIT;\nSELECT id, nama, stok FROM produk WHERE id = 5;"),
      X('Rollback saat ada masalah', "BEGIN;\nUPDATE produk SET stok = stok - 5 WHERE id = 2;\nSELECT nama, stok FROM produk WHERE id = 2;\nROLLBACK;\nSELECT nama, stok FROM produk WHERE id = 2;",
        'Stok sempat menjadi -5 di dalam transaksi. Aplikasi mendeteksinya lalu melakukan ROLLBACK, sehingga data kembali seperti semula.')]),
'ACID & tingkat isolasi': dict(
  ist=[('Dirty read', 'Membaca data yang belum di-commit transaksi lain.'),
       ('Lost update', 'Dua transaksi mengubah baris sama; salah satu perubahan hilang.'),
       ('Read Committed / Repeatable Read / Serializable', 'Tingkat isolasi dari longgar ke ketat; PostgreSQL bawaannya Read Committed.'),
       ('Optimistic locking', 'Kolom versi dicek saat update; gagal jika sudah diubah orang lain.')],
  cx=[X('Optimistic locking dengan kolom versi', "ALTER TABLE produk ADD COLUMN versi INTEGER DEFAULT 1;\n-- dua kasir membaca produk 1 dengan versi 1, kasir A menyimpan duluan:\nUPDATE produk SET stok = stok - 1, versi = versi + 1 WHERE id = 1 AND versi = 1;\n-- kasir B masih membawa versi 1, update-nya tidak mengenai baris mana pun:\nUPDATE produk SET stok = stok - 2, versi = versi + 1 WHERE id = 1 AND versi = 1;\nSELECT id, stok, versi FROM produk WHERE id = 1;",
        'Update kedua mengenai 0 baris. Aplikasi lalu membaca ulang dan mencoba lagi, sehingga tidak ada lost update.')]),
'GRANT, REVOKE & SQL injection': dict(
  ist=[('Least privilege', 'Beri hak akses seminimal mungkin sesuai kebutuhan.'),
       ('Parameterized query / prepared statement', 'Nilai dikirim terpisah dari teks SQL; pencegah utama SQL injection.'),
       ('Role', 'Kumpulan hak akses yang diberikan ke banyak pengguna sekaligus.'),
       ('OWASP Top 10', 'Daftar risiko keamanan web paling umum; injection termasuk di dalamnya.')],
  cx=[X('Role read-only untuk tim analis (PostgreSQL)', "CREATE ROLE analis NOLOGIN;\nGRANT USAGE ON SCHEMA public TO analis;\nGRANT SELECT ON ALL TABLES IN SCHEMA public TO analis;\nALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO analis;\nCREATE ROLE sari LOGIN PASSWORD 'ganti-di-vault' IN ROLE analis;\nREVOKE ALL ON TABLE gaji FROM analis;", run=False),
      dict(t='Query rentan vs query berparameter (Python)', lang='python', code="import sqlite3\ncon = sqlite3.connect(':memory:')\ncon.execute(\"CREATE TABLE user (nama TEXT, peran TEXT)\")\ncon.executemany('INSERT INTO user VALUES (?, ?)', [('sari', 'admin'), ('budi', 'kasir')])\ninput_jahat = \"x' OR '1'='1\"\nrentan = con.execute(f\"SELECT * FROM user WHERE nama = '{input_jahat}'\").fetchall()\naman = con.execute('SELECT * FROM user WHERE nama = ?', (input_jahat,)).fetchall()\nprint('Rentan:', rentan)\nprint('Aman  :', aman)")]),
'Stored procedure & function': dict(
  ist=[('PL/pgSQL', 'Bahasa prosedural bawaan PostgreSQL untuk function dan trigger.'),
       ('Trigger', 'Kode yang otomatis berjalan saat INSERT/UPDATE/DELETE.'),
       ('Business logic di database', 'Pro: konsisten dan dekat data. Kontra: sulit diuji dan di-version-kan.'),
       ('SECURITY DEFINER', 'Function berjalan dengan hak pembuatnya; berbahaya jika tidak hati-hati.')],
  cx=[X('Trigger audit perubahan harga', "CREATE TABLE log_harga (produk_id INTEGER, lama INTEGER, baru INTEGER, waktu TEXT DEFAULT CURRENT_TIMESTAMP);\nCREATE TRIGGER trg_log_harga AFTER UPDATE OF harga ON produk\nWHEN OLD.harga <> NEW.harga\nBEGIN\n  INSERT INTO log_harga (produk_id, lama, baru) VALUES (OLD.id, OLD.harga, NEW.harga);\nEND;\nUPDATE produk SET harga = 89000 WHERE id = 1;\nSELECT produk_id, lama, baru FROM log_harga;",
        'Di PostgreSQL, isi trigger ditulis sebagai function PL/pgSQL. Idenya sama: setiap perubahan harga tercatat otomatis.')]),
'Teknik optimasi query': dict(
  ist=[('Slow query log', 'Log query yang melebihi batas waktu; titik awal optimasi.'),
       ('N+1 query', 'Satu query daftar lalu N query detail; diganti satu JOIN atau IN.'),
       ('Cardinality estimate', 'Perkiraan jumlah baris oleh optimizer; salah perkiraan membuat rencana buruk.'),
       ('pg_stat_statements', 'Ekstensi PostgreSQL untuk melihat query paling berat.')],
  cx=[X('Fungsi pada kolom mematikan index', "CREATE INDEX idx_tanggal ON pesanan(tanggal);\nEXPLAIN QUERY PLAN SELECT id FROM pesanan WHERE strftime('%Y-%m', tanggal) = '2026-10';\nEXPLAIN QUERY PLAN SELECT id FROM pesanan WHERE tanggal >= '2026-10-01' AND tanggal < '2026-11-01';",
        'Query pertama membungkus kolom dengan fungsi sehingga index tidak terpakai (SCAN). Rentang tanggal biasa membuatnya sargable (SEARCH).')]),
'CTE: WITH': dict(
  ist=[('CTE', 'Common Table Expression: query bernama yang membuat query panjang mudah dibaca.'),
       ('Pipeline transformasi', 'Rangkaian CTE seperti langkah-langkah: bersihkan → gabung → hitung.'),
       ('dbt model', 'Di dbt, setiap model biasanya ditulis sebagai rangkaian CTE.'),
       ('Readability', 'Keterbacaan; alasan utama memakai CTE dibanding subquery bertingkat.')],
  cx=[X('Kontribusi omzet tiap kategori', "WITH penjualan AS (\n  SELECT pr.kategori, d.qty * d.harga AS nilai\n  FROM detail d JOIN produk pr ON pr.id = d.produk_id\n  JOIN pesanan p ON p.id = d.pesanan_id AND p.status <> 'batal'\n), per_kategori AS (\n  SELECT kategori, SUM(nilai) AS omzet FROM penjualan GROUP BY kategori\n)\nSELECT kategori, omzet, ROUND(100.0 * omzet / (SELECT SUM(omzet) FROM per_kategori), 1) AS persen\nFROM per_kategori ORDER BY omzet DESC;")]),
'Query rekursif': dict(
  ist=[('Recursive CTE', 'CTE yang memanggil dirinya sendiri: bagian anchor + bagian rekursif.'),
       ('Hierarki organisasi', 'Struktur atasan-bawahan; contoh klasik query rekursif.'),
       ('Bill of materials', 'Daftar komponen bertingkat sebuah produk.'),
       ('Date spine', 'Deret tanggal lengkap untuk mengisi hari kosong di laporan.')],
  cx=[X('Date spine: penjualan harian termasuk hari tanpa pesanan', "WITH RECURSIVE hari(tgl) AS (\n  SELECT '2026-10-01'\n  UNION ALL\n  SELECT date(tgl, '+1 day') FROM hari WHERE tgl < '2026-10-10'\n)\nSELECT h.tgl, COUNT(p.id) AS pesanan\nFROM hari h LEFT JOIN pesanan p ON p.tanggal = h.tgl\nGROUP BY h.tgl;")]),
'Window function: ROW_NUMBER, RANK, DENSE_RANK': dict(
  ist=[('PARTITION BY', 'Membagi baris ke kelompok tanpa meringkasnya seperti GROUP BY.'),
       ('Deduplication', 'Menghapus duplikat dengan ROW_NUMBER() = 1 per kunci.'),
       ('Top-N per group', 'Mengambil N teratas di setiap kelompok.'),
       ('Ties', 'Nilai kembar; RANK melompat (1,1,3), DENSE_RANK tidak (1,1,2).')],
  cx=[X('Produk terlaris per kategori', "WITH jual AS (\n  SELECT pr.kategori, pr.nama, SUM(d.qty) AS unit\n  FROM detail d JOIN produk pr ON pr.id = d.produk_id GROUP BY pr.id\n)\nSELECT * FROM (\n  SELECT kategori, nama, unit, ROW_NUMBER() OVER (PARTITION BY kategori ORDER BY unit DESC) AS urut FROM jual\n) WHERE urut = 1;")]),
'LEAD, LAG & running total': dict(
  ist=[('Running total / cumulative sum', 'Jumlah berjalan: SUM(...) OVER (ORDER BY tanggal).'),
       ('MoM / YoY', 'Pertumbuhan dibanding bulan atau tahun sebelumnya.'),
       ('Frame clause', 'ROWS BETWEEN ... untuk rata-rata bergerak.'),
       ('Inter-purchase time', 'Jarak antar pembelian pelanggan; dihitung dengan LAG.')],
  cx=[X('Jarak hari antar pesanan tiap pelanggan', "SELECT pelanggan_id, tanggal,\n       LAG(tanggal) OVER (PARTITION BY pelanggan_id ORDER BY tanggal) AS sebelumnya,\n       CAST(julianday(tanggal) - julianday(LAG(tanggal) OVER (PARTITION BY pelanggan_id ORDER BY tanggal)) AS INTEGER) AS jarak_hari\nFROM pesanan\nWHERE pelanggan_id IN (1, 2);")]),
'Pivot, unpivot & dynamic SQL': dict(
  ist=[('Wide vs long format', 'Wide: satu kolom per kategori; long: satu baris per kategori. BI tool umumnya suka long.'),
       ('crosstab', 'Fungsi pivot di ekstensi tablefunc PostgreSQL.'),
       ('Dynamic SQL', 'SQL yang dirakit saat runtime; rawan injection jika tidak hati-hati.'),
       ('quote_ident / format()', 'Fungsi PostgreSQL untuk menyusun dynamic SQL dengan aman.')],
  cx=[X('Pivot omzet bulanan per kategori', "SELECT strftime('%Y-%m', p.tanggal) AS bulan,\n       SUM(CASE WHEN pr.kategori = 'Kopi' THEN d.qty * d.harga ELSE 0 END) AS kopi,\n       SUM(CASE WHEN pr.kategori = 'Teh' THEN d.qty * d.harga ELSE 0 END) AS teh,\n       SUM(CASE WHEN pr.kategori = 'Alat' THEN d.qty * d.harga ELSE 0 END) AS alat\nFROM detail d JOIN pesanan p ON p.id = d.pesanan_id JOIN produk pr ON pr.id = d.produk_id\nGROUP BY bulan;")]),
'Proyek mini: Peringkat & tren': dict(
  ist=[('Leaderboard', 'Papan peringkat; contoh umum RANK di dashboard.'),
       ('Trend analysis', 'Melihat arah perubahan dari waktu ke waktu.'),
       ('Share of wallet', 'Porsi belanja pelanggan di toko kita dibanding total kebutuhannya.'),
       ('Percentile', 'Posisi relatif; NTILE(4) membagi pelanggan ke kuartil.')],
  cx=[X('Kuartil pelanggan berdasarkan belanja', "WITH belanja AS (\n  SELECT p.pelanggan_id, SUM(d.qty * d.harga) AS total\n  FROM pesanan p JOIN detail d ON d.pesanan_id = p.id\n  WHERE p.status <> 'batal' GROUP BY p.pelanggan_id\n)\nSELECT pelanggan_id, total, NTILE(4) OVER (ORDER BY total DESC) AS kuartil,\n       RANK() OVER (ORDER BY total DESC) AS peringkat\nFROM belanja;")]),
'Database toko buku online': dict(
  ist=[('Normalisasi (1NF–3NF)', 'Memecah tabel agar tidak ada data berulang dan anomali update.'),
       ('Junction table', 'Tabel penghubung relasi banyak-ke-banyak, misalnya buku_penulis.'),
       ('Sample data', 'Data contoh realistis untuk menguji query.'),
       ('Acceptance query', 'Query yang membuktikan skema menjawab kebutuhan bisnis.')],
  cx=[X('Relasi banyak-ke-banyak: buku dan penulis', "CREATE TABLE buku (id INTEGER PRIMARY KEY, judul TEXT);\nCREATE TABLE penulis (id INTEGER PRIMARY KEY, nama TEXT);\nCREATE TABLE buku_penulis (buku_id INTEGER, penulis_id INTEGER, PRIMARY KEY (buku_id, penulis_id));\nINSERT INTO buku VALUES (1, 'Laut Bercerita'), (2, 'Belajar SQL Bersama');\nINSERT INTO penulis VALUES (1, 'Leila'), (2, 'Andi'), (3, 'Rina');\nINSERT INTO buku_penulis VALUES (1, 1), (2, 2), (2, 3);\nSELECT b.judul, GROUP_CONCAT(p.nama, ', ') AS penulis\nFROM buku b JOIN buku_penulis bp ON bp.buku_id = b.id JOIN penulis p ON p.id = bp.penulis_id\nGROUP BY b.id;", setup='')]),
}
