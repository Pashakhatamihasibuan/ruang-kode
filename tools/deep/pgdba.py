"""Pendalaman jalur DBA PostgreSQL: istilah dunia kerja dan contoh.
Contoh dengan pg=True dijalankan di PostgreSQL 16 sungguhan (psql), sehingga keluarannya asli; konfigurasi/shell sebagai kode rujukan."""
K = 'pgdba'

DIAM = "SET client_min_messages = warning;\nDROP ROLE IF EXISTS app_baca, app_tulis, analis, kasir_medan, kasir_bdg, toko_app;\nRESET client_min_messages;"


def G(t, code, b=None, setup=''):
    """Contoh SQL yang dijalankan di PostgreSQL 16 sungguhan."""
    return dict(t=t, b=b, code=code.strip('\n'), lang='sql', run=False, pg=True, setup=setup)


def S(t, code, lang, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


TOKO = '''CREATE TABLE pelanggan (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, nama text NOT NULL, kota text NOT NULL);
CREATE TABLE pesanan (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, pelanggan_id bigint NOT NULL REFERENCES pelanggan,
                      dibuat timestamptz NOT NULL, status text NOT NULL, total numeric(14,0) NOT NULL);
INSERT INTO pelanggan (nama, kota)
SELECT 'Pelanggan ' || g, (ARRAY['Medan','Bandung','Surabaya','Makassar','Denpasar'])[1 + g % 5] FROM generate_series(1, 20000) g;
INSERT INTO pesanan (pelanggan_id, dibuat, status, total)
SELECT 1 + (g::bigint * 7919) % 20000, timestamptz '2026-01-01 00:00+07' + (g % 320) * interval '1 day' + (g % 86400) * interval '1 second',
       (ARRAY['baru','dibayar','dikirim','selesai','batal'])[1 + g % 5], 10000 + (g::bigint * 37) % 2000000
FROM generate_series(1, 300000) g;
ANALYZE;'''

D = {
'PostgreSQL dan tugas seorang DBA': dict(
  ist=[('DBA (Database Administrator)', 'Penanggung jawab ketersediaan, kinerja, keamanan, dan keutuhan data di database.'),
       ('RPO / RTO', 'Recovery Point Objective (berapa banyak data boleh hilang) dan Recovery Time Objective (berapa lama boleh mati).'),
       ('SLA / SLO', 'Janji layanan ke pengguna, misalnya ketersediaan 99,95% per bulan (sekitar 22 menit downtime).'),
       ('Runbook', 'Prosedur tertulis langkah demi langkah untuk operasi rutin dan insiden (failover, restore).'),
       ('Managed database', 'Layanan cloud seperti Amazon RDS/Aurora, Cloud SQL, Azure Flexible Server; DBA tetap mengurus skema, query, dan akses.')],
  cx=[G('Mengenal server: versi, ukuran database, dan pengaturan penting', '''
SELECT current_setting('server_version') AS versi, current_database() AS db,
       pg_size_pretty(pg_database_size(current_database())) AS ukuran;
SELECT name, setting, unit, short_desc
FROM pg_settings
WHERE lower(name) IN ('max_connections', 'shared_buffers', 'work_mem', 'wal_level', 'timezone')
ORDER BY name;''', 'Pertanyaan pertama DBA saat memegang server baru: versi berapa, seberapa besar, dan bagaimana konfigurasinya.'),
      S('Menghitung anggaran downtime dari SLA', '''
SLA 99,9%   -> 43 menit 49 detik per bulan
SLA 99,95%  -> 21 menit 54 detik per bulan
SLA 99,99%  ->  4 menit 22 detik per bulan
Artinya: dengan 99,95%, satu kali restore 30 menit sudah melanggar SLA,
sehingga perlu replika siaga (failover < 1 menit), bukan hanya backup.''', 'text')]),

'Arsitektur proses dan penyimpanan': dict(
  ist=[('Postmaster', 'Proses induk PostgreSQL yang menerima koneksi dan membuat satu backend process per koneksi.'),
       ('Shared buffers', 'Cache halaman data (8 KB) di memori bersama; umumnya 25% RAM sebagai titik awal.'),
       ('WAL (Write-Ahead Log)', 'Log perubahan yang ditulis sebelum data; dasar crash recovery, replikasi, dan PITR.'),
       ('Checkpoint', 'Saat halaman kotor di memori ditulis ke disk sehingga WAL lama bisa didaur ulang.'),
       ('Background worker', 'Proses pendukung: checkpointer, background writer, WAL writer, autovacuum launcher.')],
  cx=[G('Melihat proses yang berjalan dan lokasi fisik sebuah tabel', '''
SELECT backend_type, count(*) FROM pg_stat_activity GROUP BY 1 ORDER BY 1;

CREATE TABLE contoh (id int);
INSERT INTO contoh SELECT generate_series(1, 100000);
SELECT pg_relation_filepath('contoh') AS file_di_disk,
       pg_size_pretty(pg_relation_size('contoh')) AS ukuran,
       pg_relation_size('contoh') / current_setting('block_size')::int AS jumlah_halaman_8kb;''',
      'Setiap tabel adalah berkas di direktori base/<oid database>/; datanya tersusun dalam halaman 8 KB.'),
      G('WAL bertambah setiap kali data berubah', '''
SELECT pg_current_wal_lsn() AS lsn_awal \\gset
CREATE TABLE log_uji AS SELECT g AS id, md5(g::text) AS isi FROM generate_series(1, 50000) g;
SELECT pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), :'lsn_awal')) AS wal_dihasilkan;''',
      'LSN (Log Sequence Number) adalah posisi di WAL. Selisih LSN dipakai juga untuk mengukur lag replikasi.')]),

'Instalasi dengan Docker dan psql': dict(
  ist=[('psql', 'Klien baris perintah resmi PostgreSQL; meta-command diawali backslash (\\dt, \\d+, \\x, \\timing).'),
       ('Volume', 'Penyimpanan Docker di luar container agar data tidak hilang saat container dihapus.'),
       ('PGDATA', 'Direktori data cluster PostgreSQL berisi berkas tabel, WAL, dan konfigurasi.'),
       ('Connection string', 'Alamat koneksi seperti postgresql://user:sandi@host:5432/db?sslmode=require.'),
       ('.pgpass / service file', 'Cara menyimpan kredensial koneksi tanpa menulis password di perintah atau skrip.')],
  cx=[S('docker compose untuk PostgreSQL 16 + pgAdmin', '''
# compose.yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD_FILE: /run/secrets/pg_sandi     # jangan tulis password langsung di file
      POSTGRES_DB: toko
      TZ: Asia/Jakarta
    ports: ["127.0.0.1:5432:5432"]                       # hanya bisa diakses dari mesin sendiri
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init:/docker-entrypoint-initdb.d               # skrip .sql dijalankan saat pertama dibuat
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d toko"]
      interval: 5s
    secrets: [pg_sandi]
volumes: { pgdata: {} }
secrets: { pg_sandi: { file: ./pg_sandi.txt } }

# docker compose up -d && docker compose exec db psql -U admin -d toko''', 'yaml'),
      G('Meta-command psql yang paling sering dipakai DBA', '''
CREATE TABLE produk (id serial PRIMARY KEY, nama text NOT NULL, harga numeric(12,0) CHECK (harga > 0));
CREATE INDEX ON produk (nama);
\\d produk
\\dt
\\x on
SELECT name, setting, unit, context, source, short_desc FROM pg_settings WHERE name = 'work_mem';''',
      '\\d menampilkan struktur tabel lengkap dengan indeks dan constraint; \\x on mengubah tampilan menjadi vertikal untuk baris yang lebar.')]),

'Database, schema, dan tabel': dict(
  ist=[('Cluster', 'Satu instance PostgreSQL berisi banyak database; role berlaku di seluruh cluster.'),
       ('Schema', 'Namespace di dalam database (public, sales, audit) untuk mengelompokkan objek dan hak akses.'),
       ('search_path', 'Urutan schema yang dicari saat nama objek ditulis tanpa awalan schema.'),
       ('Identity column', 'Kolom auto-increment standar SQL (GENERATED ALWAYS AS IDENTITY), pengganti serial.'),
       ('Migration', 'Perubahan skema berversi yang dijalankan berurutan dengan alat seperti Flyway, Liquibase, sqitch, atau Alembic.')],
  cx=[G('Memisahkan domain dengan schema dan search_path', '''
CREATE SCHEMA sales;
CREATE SCHEMA audit;
CREATE TABLE sales.pesanan (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, total numeric(14,0) NOT NULL);
CREATE TABLE audit.log (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, aksi text, waktu timestamptz DEFAULT now());

SET search_path = sales, public;
INSERT INTO pesanan (total) VALUES (125000), (98000);
SELECT * FROM pesanan;                      -- ditemukan di schema sales

SELECT table_schema, table_name FROM information_schema.tables
WHERE table_schema IN ('sales', 'audit') ORDER BY 1, 2;''')]),

'Tipe data dan constraint': dict(
  ist=[('numeric vs float', 'Uang wajib numeric (tepat); float/double punya galat pembulatan biner.'),
       ('timestamptz', 'Waktu dengan zona; disimpan dalam UTC dan ditampilkan sesuai TimeZone sesi. Pilihan default untuk kejadian nyata.'),
       ('CHECK constraint', 'Aturan bisnis di level database, misalnya total >= 0 atau status dalam daftar tertentu.'),
       ('Foreign key ON DELETE', 'Perilaku saat baris induk dihapus: RESTRICT, CASCADE, SET NULL.'),
       ('Exclusion constraint', 'Mencegah baris yang "bertabrakan", misalnya dua booking ruangan yang jamnya tumpang tindih.')],
  cx=[G('Kenapa uang memakai numeric, dan constraint menolak data salah', '''
SELECT 0.1::float8 + 0.2::float8 = 0.3::float8 AS float_sama, 0.1::numeric + 0.2::numeric = 0.3 AS numeric_sama;

CREATE TABLE transaksi (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nominal numeric(14,0) NOT NULL CHECK (nominal > 0),
  status text NOT NULL CHECK (status IN ('pending', 'sukses', 'gagal')),
  waktu timestamptz NOT NULL DEFAULT now()
);
INSERT INTO transaksi (nominal, status) VALUES (50000, 'sukses');
INSERT INTO transaksi (nominal, status) VALUES (-1, 'sukses');
INSERT INTO transaksi (nominal, status) VALUES (50000, 'SUKSES');''',
      'Validasi di aplikasi bisa dilewati (skrip impor, query manual); constraint di database selalu berlaku.'),
      G('Exclusion constraint: booking ruang rapat tidak boleh bentrok', '''
CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE booking (
  ruang text NOT NULL,
  waktu tstzrange NOT NULL,
  EXCLUDE USING gist (ruang WITH =, waktu WITH &&)
);
INSERT INTO booking VALUES ('Rapat-1', '[2026-11-20 09:00+07, 2026-11-20 10:00+07)');
INSERT INTO booking VALUES ('Rapat-1', '[2026-11-20 10:00+07, 2026-11-20 11:00+07)');   -- tepat bersambung: boleh
INSERT INTO booking VALUES ('Rapat-1', '[2026-11-20 09:30+07, 2026-11-20 10:30+07)');   -- tumpang tindih: ditolak''')]),

'JSONB dan tipe lanjutan': dict(
  ist=[('JSONB', 'JSON biner yang bisa diindeks; cocok untuk atribut fleksibel, bukan pengganti seluruh skema relasional.'),
       ('Operator ->, ->>, @>', 'Ambil nilai JSON, ambil sebagai teks, dan "berisi" (containment) yang didukung indeks GIN.'),
       ('GIN index', 'Generalized Inverted Index untuk JSONB, array, dan full-text search.'),
       ('Array dan range', 'Tipe bawaan PostgreSQL: text[], int4range, tstzrange beserta operatornya.'),
       ('Generated column', 'Kolom yang nilainya dihitung otomatis dari kolom lain (GENERATED ALWAYS AS ... STORED).')],
  cx=[G('Atribut produk fleksibel dengan JSONB dan indeks GIN', '''
CREATE TABLE produk (id serial PRIMARY KEY, nama text, atribut jsonb NOT NULL DEFAULT '{}');
INSERT INTO produk (nama, atribut) VALUES
 ('Kopi Gayo 250g', '{"jenis": "arabika", "roast": "medium", "asal": "Aceh", "halal": true}'),
 ('Kopi Toraja 250g', '{"jenis": "arabika", "roast": "dark", "asal": "Sulawesi Selatan", "halal": true}'),
 ('Teh Melati', '{"jenis": "teh", "kemasan": "celup", "isi": 25}');
CREATE INDEX produk_atribut_gin ON produk USING gin (atribut jsonb_path_ops);

SELECT nama, atribut->>'asal' AS asal FROM produk WHERE atribut @> '{"jenis": "arabika"}';
UPDATE produk SET atribut = atribut || '{"stok_gudang": 120}' WHERE nama LIKE 'Kopi Gayo%';
SELECT nama, jsonb_pretty(atribut) FROM produk WHERE id = 1;''')]),

'Role, GRANT, dan REVOKE': dict(
  ist=[('Role', 'Identitas di PostgreSQL; bisa berupa pengguna (LOGIN) atau grup.'),
       ('Least privilege', 'Beri hak sekecil mungkin; aplikasi tidak memakai superuser atau pemilik tabel.'),
       ('Group role', 'Role tanpa LOGIN yang menampung hak; pengguna menjadi anggotanya (GRANT grup TO pengguna).'),
       ('Default privileges', 'Hak otomatis untuk tabel yang dibuat di masa depan (ALTER DEFAULT PRIVILEGES).'),
       ('Predefined roles', 'Role bawaan seperti pg_read_all_data, pg_monitor untuk tugas umum.')],
  cx=[G('Role baca/tulis untuk aplikasi dan role analis yang hanya bisa membaca', '''
CREATE TABLE pesanan (id int PRIMARY KEY, total numeric);
INSERT INTO pesanan VALUES (1, 85000);

CREATE ROLE app_baca NOLOGIN;
CREATE ROLE app_tulis NOLOGIN IN ROLE app_baca;
GRANT USAGE ON SCHEMA public TO app_baca;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_baca;
GRANT INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO app_tulis;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO app_baca;
CREATE ROLE analis LOGIN IN ROLE app_baca;

SET ROLE analis;
SELECT * FROM pesanan;
DELETE FROM pesanan;
RESET ROLE;

SELECT grantee, privilege_type FROM information_schema.role_table_grants
WHERE table_name = 'pesanan' AND grantee LIKE 'app_%' ORDER BY 1, 2;''', setup=DIAM)]),

'Autentikasi: pg_hba.conf dan SSL': dict(
  ist=[('pg_hba.conf', 'Aturan siapa boleh terhubung dari mana dan dengan metode apa; dibaca dari atas, aturan pertama yang cocok berlaku.'),
       ('scram-sha-256', 'Metode password modern; md5 dan trust (tanpa password) sebaiknya tidak dipakai di produksi.'),
       ('hostssl', 'Jenis koneksi yang hanya cocok jika memakai TLS; tolak koneksi tanpa enkripsi dari jaringan.'),
       ('Connection pooler', 'PgBouncer/pgcat: menampung ribuan koneksi aplikasi ke sedikit koneksi database.')],
  cx=[S('pg_hba.conf produksi yang ketat', '''
# TYPE    DATABASE  USER         ADDRESS          METHOD
local     all       postgres                      peer                 # superuser hanya dari OS user postgres
hostssl   toko      toko_app     10.10.1.0/24     scram-sha-256        # subnet server aplikasi
hostssl   toko      +analis      10.20.0.0/16     scram-sha-256        # anggota grup analis dari VPN kantor
hostssl   replication replikator 10.10.9.11/32    scram-sha-256        # standby
host      all       all          0.0.0.0/0        reject               # sisanya ditolak

# postgresql.conf
ssl = on
ssl_min_protocol_version = 'TLSv1.3'
password_encryption = 'scram-sha-256'
# muat ulang tanpa restart: SELECT pg_reload_conf();''', 'conf'),
      G('Memeriksa aturan yang sedang aktif dan metode password', '''
SELECT line_number, type, database, user_name, address, auth_method
FROM pg_hba_file_rules ORDER BY line_number;
SHOW password_encryption;''', 'pg_hba_file_rules menampilkan isi pg_hba.conf beserta kesalahan sintaksnya sebelum di-reload. Cluster latihan ini memakai trust, yang tidak boleh dipakai di produksi.')]),

'Row-Level Security': dict(
  ist=[('Row-Level Security (RLS)', 'Kebijakan per baris: pengguna hanya melihat atau mengubah baris yang diizinkan.'),
       ('Policy', 'Aturan USING (baris mana yang terlihat) dan WITH CHECK (baris mana yang boleh ditulis).'),
       ('Multi-tenant', 'Satu database untuk banyak pelanggan/cabang; RLS memastikan data antar-tenant tidak bocor.'),
       ('BYPASSRLS / FORCE', 'Pemilik tabel dan superuser melewati RLS kecuali FORCE ROW LEVEL SECURITY.')],
  cx=[G('Kasir hanya melihat transaksi cabangnya sendiri', '''
CREATE TABLE transaksi (id int PRIMARY KEY, cabang text NOT NULL, total numeric NOT NULL);
INSERT INTO transaksi VALUES (1, 'medan', 125000), (2, 'bandung', 98000), (3, 'medan', 47000);
ALTER TABLE transaksi ENABLE ROW LEVEL SECURITY;
CREATE POLICY per_cabang ON transaksi
  USING (cabang = current_setting('app.cabang'))
  WITH CHECK (cabang = current_setting('app.cabang'));

CREATE ROLE kasir_medan LOGIN;
GRANT SELECT, INSERT ON transaksi TO kasir_medan;

SET ROLE kasir_medan;
SET app.cabang = 'medan';
SELECT * FROM transaksi;
INSERT INTO transaksi VALUES (4, 'bandung', 10000);
RESET ROLE;''', 'Aplikasi mengatur app.cabang dari token login; walaupun query lupa menulis WHERE cabang, data cabang lain tidak bocor.', setup=DIAM)]),

'Transaksi dan tingkat isolasi': dict(
  ist=[('ACID', 'Atomicity, Consistency, Isolation, Durability: jaminan transaksi database.'),
       ('Read Committed', 'Default PostgreSQL: setiap statement melihat data yang sudah di-commit saat statement dimulai.'),
       ('Repeatable Read / Serializable', 'Snapshot tetap sepanjang transaksi; Serializable juga mencegah anomali seperti write skew.'),
       ('Savepoint', 'Titik simpan di dalam transaksi untuk membatalkan sebagian tanpa membatalkan semuanya.'),
       ('SELECT ... FOR UPDATE', 'Mengunci baris yang dibaca agar tidak diubah transaksi lain sampai commit (cegah lost update).')],
  cx=[G('Transfer saldo yang atomik dan savepoint', '''
CREATE TABLE rekening (id text PRIMARY KEY, saldo numeric NOT NULL CHECK (saldo >= 0));
INSERT INTO rekening VALUES ('A', 100000), ('B', 50000);

BEGIN;
UPDATE rekening SET saldo = saldo - 150000 WHERE id = 'A';     -- melanggar CHECK
UPDATE rekening SET saldo = saldo + 150000 WHERE id = 'B';
COMMIT;                                                        -- transaksi gagal -> ROLLBACK
SELECT * FROM rekening ORDER BY id;

BEGIN;
UPDATE rekening SET saldo = saldo - 30000 WHERE id = 'A';
SAVEPOINT sebelum_bonus;
UPDATE rekening SET saldo = saldo + 999999 WHERE id = 'B';     -- salah input
ROLLBACK TO SAVEPOINT sebelum_bonus;
UPDATE rekening SET saldo = saldo + 30000 WHERE id = 'B';
COMMIT;
SELECT * FROM rekening ORDER BY id;''', 'Setelah satu statement gagal, PostgreSQL menolak statement berikutnya dalam transaksi itu sampai ROLLBACK. Tidak ada transfer setengah jadi.')]),

'MVCC, lock, dan deadlock': dict(
  ist=[('MVCC', 'Multi-Version Concurrency Control: UPDATE membuat versi baris baru sehingga pembaca tidak menunggu penulis.'),
       ('xmin / xmax', 'ID transaksi yang membuat dan menghapus sebuah versi baris (kolom sistem tersembunyi).'),
       ('Row lock vs table lock', 'Kunci per baris (FOR UPDATE) vs kunci tabel (ALTER TABLE, LOCK TABLE) yang memblokir lebih luas.'),
       ('Deadlock', 'Dua transaksi saling menunggu kunci; PostgreSQL mendeteksinya setelah deadlock_timeout dan membatalkan salah satu.'),
       ('lock_timeout', 'Batas waktu menunggu kunci; wajib saat migrasi agar ALTER TABLE tidak menahan antrean query.')],
  cx=[G('Melihat MVCC: UPDATE membuat versi baris baru', '''
CREATE TABLE produk (id int PRIMARY KEY, harga int);
INSERT INTO produk VALUES (1, 85000);
SELECT ctid, xmin, xmax, * FROM produk;
UPDATE produk SET harga = 90000 WHERE id = 1;
SELECT ctid, xmin, xmax, * FROM produk;''', 'ctid (posisi fisik) berubah dari (0,1) ke (0,2): versi lama masih ada di halaman sampai dibersihkan VACUUM.'),
      G('Deadlock sungguhan dengan dua sesi (sesi kedua lewat dblink)', '''
CREATE EXTENSION IF NOT EXISTS dblink;
CREATE TABLE stok (sku text PRIMARY KEY, qty int);
INSERT INTO stok VALUES ('KOPI', 10), ('GULA', 10);
SET deadlock_timeout = '200ms';
SELECT dblink_connect('sesi_b', format('dbname=%s host=/tmp port=%s user=postgres', current_database(), current_setting('port')));

BEGIN;
UPDATE stok SET qty = qty - 1 WHERE sku = 'KOPI';                                    -- sesi A kunci KOPI
SELECT dblink_exec('sesi_b', 'BEGIN; UPDATE stok SET qty = qty - 1 WHERE sku = \'\'GULA\'\'');   -- sesi B kunci GULA
SELECT dblink_send_query('sesi_b', 'UPDATE stok SET qty = qty - 1 WHERE sku = \'\'KOPI\'\'');    -- B menunggu A
SELECT pg_sleep(0.3);
UPDATE stok SET qty = qty - 1 WHERE sku = 'GULA';                                    -- A menunggu B -> deadlock
ROLLBACK;
SELECT dblink_disconnect('sesi_b');''', 'Pencegahannya: kunci baris selalu dalam urutan yang sama (misalnya urut SKU), transaksi pendek, dan retry otomatis untuk error 40P01.')]),

'VACUUM, autovacuum, dan bloat': dict(
  ist=[('Dead tuple', 'Versi baris lama hasil UPDATE/DELETE yang tidak lagi terlihat oleh transaksi mana pun.'),
       ('VACUUM', 'Menandai ruang dead tuple agar bisa dipakai ulang dan memperbarui visibility map; tidak mengunci baca/tulis.'),
       ('Bloat', 'Tabel/indeks membengkak karena ruang mati; memperlambat scan dan memboroskan cache.'),
       ('Transaction ID wraparound', 'Batas 2 miliar ID transaksi; VACUUM (freeze) wajib berjalan agar database tidak berhenti menerima tulisan.'),
       ('pg_repack', 'Ekstensi untuk membangun ulang tabel yang bloat tanpa kunci lama seperti VACUUM FULL.')],
  cx=[G('Mengukur dead tuple dan efek VACUUM', '''
CREATE EXTENSION IF NOT EXISTS pgstattuple;
CREATE TABLE sesi (id int PRIMARY KEY, data text) WITH (autovacuum_enabled = off);
INSERT INTO sesi SELECT g, repeat('x', 200) FROM generate_series(1, 20000) g;
UPDATE sesi SET data = repeat('y', 200);                -- setiap baris punya 1 versi mati
DELETE FROM sesi WHERE id % 2 = 0;

SELECT pg_size_pretty(table_len) AS ukuran, tuple_count AS hidup, dead_tuple_count AS mati,
       round(dead_tuple_percent) AS persen_mati, round(free_percent) AS persen_kosong
FROM pgstattuple('sesi');

VACUUM sesi;
SELECT pg_size_pretty(table_len) AS ukuran, tuple_count AS hidup, dead_tuple_count AS mati,
       round(dead_tuple_percent) AS persen_mati, round(free_percent) AS persen_kosong
FROM pgstattuple('sesi');''', 'VACUUM biasa mengosongkan ruang untuk dipakai ulang tetapi ukuran berkas tidak mengecil; VACUUM FULL atau pg_repack yang mengembalikan ruang ke OS.'),
      S('Menyetel autovacuum untuk tabel yang sering di-update', '''
-- Default: vacuum saat dead tuple > 50 + 20% baris. Untuk tabel 100 juta baris itu 20 juta baris mati!
ALTER TABLE pesanan SET (autovacuum_vacuum_scale_factor = 0.02, autovacuum_vacuum_threshold = 5000,
                         autovacuum_analyze_scale_factor = 0.01);

-- Pantau usia transaksi tertua (wraparound): waspada jika mendekati 1,5 miliar
SELECT datname, age(datfrozenxid) FROM pg_database ORDER BY 2 DESC;''', 'sql')]),

'Membaca EXPLAIN ANALYZE': dict(
  ist=[('Query plan', 'Rencana eksekusi yang dipilih planner berdasarkan statistik tabel.'),
       ('Seq Scan / Index Scan / Bitmap Heap Scan', 'Membaca seluruh tabel / mengikuti indeks per baris / mengumpulkan halaman dari indeks lalu membaca tabel.'),
       ('Estimated vs actual rows', 'Selisih besar antara perkiraan dan kenyataan menandakan statistik usang; jalankan ANALYZE.'),
       ('Buffers shared hit/read', 'Halaman yang ditemukan di cache vs dibaca dari disk (EXPLAIN (ANALYZE, BUFFERS)).'),
       ('Sargable', 'Kondisi yang bisa memakai indeks; fungsi pada kolom (date(dibuat) = ...) membuatnya tidak sargable.')],
  cx=[G('Dari Seq Scan ke pemindaian indeks pada 300 ribu pesanan', TOKO + '''

EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF, SUMMARY OFF)
SELECT * FROM pesanan WHERE pelanggan_id = 4242;

CREATE INDEX pesanan_pelanggan_idx ON pesanan (pelanggan_id);

EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF, SUMMARY OFF)
SELECT * FROM pesanan WHERE pelanggan_id = 4242;''', 'Perhatikan "Rows Removed by Filter": tanpa indeks, dua proses paralel membuang hampir 300 ribu baris untuk menemukan 15. Dengan indeks, hanya 15 blok yang dibaca.'),
      G('Fungsi pada kolom mematikan indeks (query tidak sargable)', TOKO + '''
CREATE INDEX pesanan_dibuat_idx ON pesanan (dibuat);

EXPLAIN (COSTS OFF)
SELECT count(*) FROM pesanan WHERE date(dibuat AT TIME ZONE 'Asia/Jakarta') = '2026-06-01';

EXPLAIN (COSTS OFF)
SELECT count(*) FROM pesanan WHERE dibuat >= '2026-06-01 00:00+07' AND dibuat < '2026-06-02 00:00+07';''')]),

'Jenis indeks dan kapan memakainya': dict(
  ist=[('B-tree', 'Indeks default untuk =, <, >, BETWEEN, ORDER BY; urutan kolom pada indeks komposit penting.'),
       ('Partial index', 'Indeks untuk sebagian baris (WHERE status = \'baru\'); kecil dan cepat.'),
       ('Covering index (INCLUDE)', 'Menyertakan kolom tambahan sehingga query cukup membaca indeks (Index Only Scan).'),
       ('GIN / GiST / BRIN', 'GIN untuk JSONB/array/full-text, GiST untuk range dan geometri, BRIN untuk tabel log besar yang berurutan waktu.'),
       ('CREATE INDEX CONCURRENTLY', 'Membuat indeks di produksi tanpa memblokir INSERT/UPDATE.')],
  cx=[G('Membandingkan ukuran indeks penuh, partial, dan BRIN', TOKO + '''
CREATE INDEX idx_status_penuh ON pesanan (status, dibuat);
CREATE INDEX idx_status_baru ON pesanan (dibuat) WHERE status = 'baru';
CREATE INDEX idx_dibuat_brin ON pesanan USING brin (dibuat);
CREATE INDEX idx_cover ON pesanan (pelanggan_id) INCLUDE (total);
VACUUM ANALYZE pesanan;                      -- visibility map terisi -> Index Only Scan bisa dipakai

SELECT indexrelname AS indeks, pg_size_pretty(pg_relation_size(indexrelid)) AS ukuran
FROM pg_stat_user_indexes WHERE relname = 'pesanan' ORDER BY pg_relation_size(indexrelid) DESC;

EXPLAIN (COSTS OFF) SELECT dibuat FROM pesanan WHERE status = 'baru' AND dibuat > '2026-11-01';
EXPLAIN (COSTS OFF) SELECT sum(total) FROM pesanan WHERE pelanggan_id = 77;''', 'BRIN hanya puluhan KB untuk 300 ribu baris karena menyimpan ringkasan per blok, bukan per baris. Cocok untuk tabel log yang terus bertambah.'),
      G('Pencarian teks "mengandung" dengan pg_trgm', '''
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE TABLE produk (id serial PRIMARY KEY, nama text);
INSERT INTO produk (nama) SELECT 'Produk ' || md5(g::text) FROM generate_series(1, 50000) g;
INSERT INTO produk (nama) VALUES ('Kopi Arabika Gayo 250g'), ('Kopi Robusta Lampung 1kg');
CREATE INDEX produk_nama_trgm ON produk USING gin (nama gin_trgm_ops);
ANALYZE produk;
EXPLAIN (COSTS OFF) SELECT nama FROM produk WHERE nama ILIKE '%arabika%';
SELECT nama FROM produk WHERE nama ILIKE '%arabika%';''', 'Indeks B-tree biasa tidak bisa dipakai untuk LIKE \'%kata%\'; trigram GIN bisa.')]),

'pg_stat_statements dan konfigurasi memori': dict(
  ist=[('pg_stat_statements', 'Ekstensi yang mengumpulkan statistik setiap bentuk query: jumlah panggilan, total waktu, baris.'),
       ('work_mem', 'Memori per operasi sort/hash per query; terlalu kecil memicu temp file ke disk, terlalu besar berisiko kehabisan RAM.'),
       ('effective_cache_size', 'Perkiraan memori cache OS + shared_buffers untuk membantu planner memilih indeks.'),
       ('Cache hit ratio', 'Persentase halaman yang ditemukan di shared buffers; OLTP sehat biasanya > 99%.'),
       ('Top-N query', 'Daftar query dengan total waktu terbesar; tempat pertama mencari optimasi.')],
  cx=[G('Menemukan query paling mahal', TOKO + '''
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
SELECT pg_stat_statements_reset() IS NOT NULL AS reset;

SELECT count(*) FROM pesanan WHERE pelanggan_id = 10;
SELECT count(*) FROM pesanan WHERE pelanggan_id = 11;
SELECT count(*) FROM pesanan WHERE pelanggan_id = 12;
SELECT status, sum(total) FROM pesanan GROUP BY status;
SELECT * FROM pelanggan WHERE id = 5;

SELECT calls, rows, left(regexp_replace(query, '\\s+', ' ', 'g'), 60) AS query
FROM pg_stat_statements
WHERE query NOT ILIKE '%pg_stat_statements%' AND query ILIKE 'select%'
ORDER BY total_exec_time DESC LIMIT 4;''', 'Query dengan nilai berbeda (pelanggan_id 10, 11, 12) dinormalisasi menjadi satu bentuk dengan $1, sehingga terlihat total dampaknya.'),
      G('work_mem terlalu kecil memaksa sort ke disk', TOKO + '''
SET work_mem = '256kB';
EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF, SUMMARY OFF) SELECT * FROM pesanan ORDER BY total DESC LIMIT 100000;
SET work_mem = '64MB';
EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF, SUMMARY OFF) SELECT * FROM pesanan ORDER BY total DESC LIMIT 100000;''',
      '"external merge Disk" berarti sort tumpah ke disk. Naikkan work_mem per sesi atau per role laporan, bukan global, karena dikalikan jumlah koneksi.')]),

'Backup logis dan fisik': dict(
  ist=[('Backup logis', 'pg_dump/pg_dumpall menghasilkan SQL atau format custom; fleksibel, lambat untuk database besar.'),
       ('Backup fisik', 'Salinan berkas data + WAL (pg_basebackup, pgBackRest, Barman); cepat dipulihkan.'),
       ('PITR', 'Point-In-Time Recovery: pulihkan ke detik tertentu memakai base backup + arsip WAL.'),
       ('Aturan 3-2-1', '3 salinan, 2 media berbeda, 1 di luar lokasi; ditambah uji restore berkala.'),
       ('Restore drill', 'Latihan restore terjadwal; backup yang tidak pernah diuji dianggap tidak ada.')],
  cx=[S('Backup logis dan fisik di dunia kerja', '''
# Logis: satu database, format custom (bisa restore sebagian tabel, paralel)
pg_dump -h db.internal -U backup -d toko -Fc -Z 6 -f toko_$(date +%F).dump
pg_restore -l toko_2026-11-19.dump | grep pesanan          # lihat isi
pg_restore -d toko_uji -j 4 --no-owner toko_2026-11-19.dump  # restore paralel ke database uji

# Fisik + PITR dengan pgBackRest (pgbackrest.conf: repo1 di S3, retensi 4 full)
pgbackrest --stanza=toko --type=full backup                 # Minggu 01.00
pgbackrest --stanza=toko --type=diff backup                 # Senin-Sabtu 01.00
# archive_command = 'pgbackrest --stanza=toko archive-push %p'   (WAL dikirim terus menerus)

# Insiden: tabel terhapus pukul 14:32:10 -> pulihkan ke 14:32:00 di server baru
pgbackrest --stanza=toko --type=time --target="2026-11-19 14:32:00+07" --target-action=promote restore''', 'bash'),
      G('Memeriksa kesiapan PITR dari dalam database', '''
SELECT name, setting FROM pg_settings
WHERE name IN ('wal_level', 'archive_mode', 'archive_command', 'max_wal_senders', 'full_page_writes') ORDER BY name;
SELECT archived_count, failed_count, last_archived_time IS NOT NULL AS pernah_mengarsip FROM pg_stat_archiver;''',
      'Di cluster latihan archive_mode masih off, artinya belum bisa PITR. Di produksi, failed_count yang naik harus memicu alert.')]),

'Replikasi dan high availability': dict(
  ist=[('Streaming replication', 'Standby menerima WAL dari primary secara terus menerus dan bisa dipakai untuk baca (hot standby).'),
       ('Synchronous vs asynchronous', 'Sync menunggu standby mengonfirmasi (RPO 0, lebih lambat); async lebih cepat dengan risiko kehilangan beberapa detik data.'),
       ('Replication slot', 'Menjamin WAL tidak dihapus sebelum diterima standby; slot yang macet bisa memenuhi disk.'),
       ('Failover / switchover', 'Mempromosikan standby menjadi primary saat primary mati / secara terencana untuk pemeliharaan.'),
       ('Patroni', 'Pengelola HA populer yang memakai etcd/Consul untuk memilih leader dan failover otomatis.'),
       ('Logical replication', 'Replikasi per tabel (publication/subscription); dipakai untuk upgrade versi besar dan CDC.')],
  cx=[S('Arsitektur HA 3 node dengan Patroni', '''
# patroni.yml (potongan)
scope: toko-prod
etcd3: { hosts: etcd-1:2379,etcd-2:2379,etcd-3:2379 }
bootstrap:
  dcs:
    ttl: 30
    maximum_lag_on_failover: 1048576            # standby tertinggal > 1 MB tidak boleh jadi primary
    synchronous_mode: true                      # minimal 1 standby sinkron -> RPO 0
    postgresql:
      parameters: { wal_level: replica, hot_standby: "on", max_wal_senders: 10, max_replication_slots: 10 }

# Aplikasi terhubung ke HAProxy/PgBouncer:
#   :5432 -> primary (cek REST Patroni GET /primary)
#   :5433 -> replika baca (GET /replica)
# Switchover terencana: patronictl switchover --candidate db-2 --force''', 'yaml'),
      G('Query pemantauan replikasi yang dijalankan di primary', '''
SELECT application_name, state, sync_state,
       pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn)) AS lag
FROM pg_stat_replication;

SELECT slot_name, active,
       pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) AS wal_ditahan
FROM pg_replication_slots;

SELECT pg_is_in_recovery() AS ini_standby;''', 'Di cluster latihan tidak ada standby sehingga hasilnya kosong. Di produksi, alert jika lag > 100 MB atau slot tidak aktif menahan WAL.')]),

'Pemantauan dan checklist harian DBA': dict(
  ist=[('pg_stat_activity', 'Daftar sesi aktif: query yang berjalan, status, berapa lama, dan apa yang ditunggu (wait_event).'),
       ('Idle in transaction', 'Sesi membuka transaksi lalu diam; menahan kunci dan menghambat VACUUM.'),
       ('Observability stack', 'postgres_exporter + Prometheus + Grafana, atau layanan seperti pganalyze, Datadog, CloudWatch.'),
       ('Capacity planning', 'Memperkirakan kebutuhan disk, CPU, koneksi beberapa bulan ke depan dari tren pertumbuhan.'),
       ('Alert fatigue', 'Terlalu banyak alert tidak penting sehingga yang penting terabaikan; alert harus bisa ditindaklanjuti.')],
  cx=[G('Query checklist pagi DBA', TOKO + '''
SELECT round(100.0 * sum(blks_hit) / nullif(sum(blks_hit) + sum(blks_read), 0), 2) AS cache_hit_pct
FROM pg_stat_database WHERE datname = current_database();

SELECT relname AS tabel, pg_size_pretty(pg_total_relation_size(relid)) AS total_dengan_indeks,
       n_live_tup AS baris_hidup, n_dead_tup AS baris_mati
FROM pg_stat_user_tables ORDER BY pg_total_relation_size(relid) DESC;

SELECT state, count(*) FROM pg_stat_activity WHERE backend_type = 'client backend' GROUP BY state;

SELECT pid, now() - xact_start AS lama, state, left(query, 40) AS query
FROM pg_stat_activity
WHERE xact_start < now() - interval '5 minutes' AND backend_type = 'client backend';''',
      'Checklist lengkap juga mencakup: hasil backup semalam, lag replikasi, ruang disk, error di log, dan usia transaksi tertua.'),
      S('Aturan alert Prometheus untuk PostgreSQL', '''
groups:
- name: postgresql
  rules:
  - alert: PostgresReplikasiTertinggal
    expr: pg_replication_lag_seconds > 30
    for: 5m
    labels: { severity: page }
  - alert: PostgresKoneksiHampirPenuh
    expr: sum(pg_stat_activity_count) / pg_settings_max_connections > 0.85
    for: 10m
    labels: { severity: warning }
  - alert: PostgresTransaksiIdleLama
    expr: pg_stat_activity_max_tx_duration{state="idle in transaction"} > 300
    labels: { severity: warning }
  - alert: PostgresBackupGagal
    expr: time() - pgbackrest_backup_last_full_time > 8 * 86400
    labels: { severity: page }''', 'yaml')]),
}
