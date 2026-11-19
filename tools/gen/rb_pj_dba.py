"""Proyek DBA PostgreSQL berpenyelesaian: 6 mini (SQL dijalankan di PostgreSQL 16 sungguhan saat generate) + 4 besar berskala industri 2026-2027."""
from rb_pj_lib import MINI, BESAR, JALUR_M, q
from pg_lib import pg

DIAM = "SET client_min_messages = warning;\nDROP ROLE IF EXISTS tenant_app;\nRESET client_min_messages;"

# ---------------------------------------------------------------- MINI
SKEMA = '''-- Skema inti toko online dengan constraint dan audit trail perubahan harga
CREATE TABLE kategori (id smallint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, nama text NOT NULL UNIQUE);
CREATE TABLE produk (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  sku        text NOT NULL UNIQUE CHECK (sku ~ '^[A-Z]{3}-[0-9]{4}$'),
  nama       text NOT NULL,
  kategori_id smallint NOT NULL REFERENCES kategori ON DELETE RESTRICT,
  harga      numeric(12,0) NOT NULL CHECK (harga > 0),
  stok       integer NOT NULL DEFAULT 0 CHECK (stok >= 0),
  diubah     timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE audit_harga (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, produk_id bigint NOT NULL,
  harga_lama numeric(12,0), harga_baru numeric(12,0), oleh text NOT NULL DEFAULT current_user, waktu timestamptz NOT NULL DEFAULT now()
);

CREATE FUNCTION catat_harga() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  IF NEW.harga IS DISTINCT FROM OLD.harga THEN
    INSERT INTO audit_harga (produk_id, harga_lama, harga_baru) VALUES (OLD.id, OLD.harga, NEW.harga);
    NEW.diubah := now();
  END IF;
  RETURN NEW;
END $$;
CREATE TRIGGER trg_audit_harga BEFORE UPDATE OF harga ON produk FOR EACH ROW EXECUTE FUNCTION catat_harga();

INSERT INTO kategori (nama) VALUES ('Minuman'), ('Sembako');
INSERT INTO produk (sku, nama, kategori_id, harga, stok) VALUES
  ('KOP-0001', 'Kopi Gayo 250g', 1, 85000, 40), ('GUL-0001', 'Gula Aren 500g', 2, 32000, 25);

-- Uji aturan: setiap baris berikut harus ditolak
INSERT INTO produk (sku, nama, kategori_id, harga) VALUES ('kopi-1', 'SKU salah format', 1, 10000);
UPDATE produk SET stok = stok - 50 WHERE sku = 'KOP-0001';
DELETE FROM kategori WHERE nama = 'Minuman';

-- Perubahan harga tercatat otomatis
UPDATE produk SET harga = 89000 WHERE sku = 'KOP-0001';
UPDATE produk SET harga = 87000 WHERE sku = 'KOP-0001';
UPDATE produk SET stok = 38 WHERE sku = 'KOP-0001';            -- bukan perubahan harga: tidak dicatat
SELECT p.sku, a.harga_lama, a.harga_baru, a.oleh FROM audit_harga a JOIN produk p ON p.id = a.produk_id ORDER BY a.id;'''

DATA_TOKO = '''CREATE TABLE pelanggan (id bigint PRIMARY KEY, nama text NOT NULL, kota text NOT NULL);
CREATE TABLE pesanan (id bigint PRIMARY KEY, pelanggan_id bigint NOT NULL REFERENCES pelanggan,
                      dibuat timestamptz NOT NULL, status text NOT NULL, total numeric(14,0) NOT NULL);
INSERT INTO pelanggan SELECT g, 'Pelanggan ' || g, (ARRAY['Medan','Bandung','Surabaya','Makassar','Denpasar'])[1 + (g / 3) % 5]
FROM generate_series(1, 50000) g;
INSERT INTO pesanan SELECT g, 1 + (g::bigint * 7919) % 50000,
       timestamptz '2026-01-01 00:00+07' + (g % 320) * interval '1 day' + (g % 86400) * interval '1 second',
       (ARRAY['baru','dibayar','dikirim','selesai','batal'])[1 + g % 5], 10000 + (g::bigint * 37) % 990000
FROM generate_series(1, 400000) g;
ANALYZE;'''

TUNING = '''-- Laporan "omzet per kota bulan Oktober untuk pesanan selesai" dikeluhkan lambat
\\timing off
EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF, SUMMARY OFF)
SELECT pl.kota, count(*) AS pesanan, sum(p.total) AS omzet
FROM pesanan p JOIN pelanggan pl ON pl.id = p.pelanggan_id
WHERE p.status = 'selesai' AND to_char(p.dibuat, 'YYYY-MM') = '2026-10'
GROUP BY pl.kota;

-- Perbaikan 1: kondisi tanggal dibuat sargable (rentang setengah terbuka, bukan fungsi pada kolom)
-- Perbaikan 2: indeks parsial sesuai pola laporan, INCLUDE kolom yang dibaca
CREATE INDEX pesanan_selesai_dibuat ON pesanan (dibuat) INCLUDE (pelanggan_id, total) WHERE status = 'selesai';
VACUUM ANALYZE pesanan;

EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF, SUMMARY OFF)
SELECT pl.kota, count(*) AS pesanan, sum(p.total) AS omzet
FROM pesanan p JOIN pelanggan pl ON pl.id = p.pelanggan_id
WHERE p.status = 'selesai' AND p.dibuat >= '2026-10-01 00:00+07' AND p.dibuat < '2026-11-01 00:00+07'
GROUP BY pl.kota;

SELECT pl.kota, count(*) AS pesanan, sum(p.total) AS omzet
FROM pesanan p JOIN pelanggan pl ON pl.id = p.pelanggan_id
WHERE p.status = 'selesai' AND p.dibuat >= '2026-10-01 00:00+07' AND p.dibuat < '2026-11-01 00:00+07'
GROUP BY pl.kota ORDER BY omzet DESC;'''

RLS = '''-- SaaS kasir: banyak toko (tenant) dalam satu database, data tidak boleh bocor antar-tenant
CREATE TABLE tenant (id int PRIMARY KEY, nama text);
CREATE TABLE penjualan (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, tenant_id int NOT NULL REFERENCES tenant,
                        produk text, total numeric NOT NULL);
CREATE INDEX ON penjualan (tenant_id);
INSERT INTO tenant VALUES (1, 'Kopi Senja Medan'), (2, 'Warung Bu Tini Bandung');
INSERT INTO penjualan (tenant_id, produk, total) VALUES (1, 'Kopi susu', 25000), (1, 'Croissant', 30000), (2, 'Nasi rames', 18000);

ALTER TABLE penjualan ENABLE ROW LEVEL SECURITY;
ALTER TABLE penjualan FORCE ROW LEVEL SECURITY;             -- pemilik tabel pun tunduk pada policy
CREATE POLICY isolasi_tenant ON penjualan
  USING (tenant_id = current_setting('app.tenant_id', true)::int)
  WITH CHECK (tenant_id = current_setting('app.tenant_id', true)::int);

CREATE ROLE tenant_app NOLOGIN;
GRANT SELECT, INSERT, UPDATE ON penjualan TO tenant_app;
GRANT USAGE ON SEQUENCE penjualan_id_seq TO tenant_app;

SET ROLE tenant_app;
-- 1) Tanpa konteks tenant: tidak melihat apa pun (gagal aman)
SELECT count(*) AS terlihat_tanpa_tenant FROM penjualan;
-- 2) Aplikasi menyetel tenant dari token login, per transaksi
BEGIN; SET LOCAL app.tenant_id = '1';
SELECT tenant_id, produk, total FROM penjualan;
UPDATE penjualan SET total = 0;                              -- hanya baris tenant 1 yang tersentuh
INSERT INTO penjualan (tenant_id, produk, total) VALUES (2, 'Sisipan jahat', 1);
ROLLBACK;
-- 3) Tenant 2 melihat datanya sendiri dan tidak terpengaruh
BEGIN; SET LOCAL app.tenant_id = '2';
SELECT tenant_id, produk, total FROM penjualan;
COMMIT;
RESET ROLE;'''

PARTISI = '''-- Tabel log aktivitas 40 juta baris/bulan: partisi per bulan, retensi 3 bulan
CREATE TABLE log_aktivitas (
  id bigint GENERATED ALWAYS AS IDENTITY, pengguna_id bigint NOT NULL, aksi text NOT NULL,
  waktu timestamptz NOT NULL, PRIMARY KEY (id, waktu)
) PARTITION BY RANGE (waktu);

DO $$
DECLARE b date;
BEGIN
  FOR b IN SELECT generate_series(date '2026-08-01', date '2026-12-01', interval '1 month')::date LOOP
    EXECUTE format('CREATE TABLE log_aktivitas_%s PARTITION OF log_aktivitas FOR VALUES FROM (%L) TO (%L)',
                   to_char(b, 'YYYYMM'), b, b + interval '1 month');
  END LOOP;
END $$;
CREATE TABLE log_aktivitas_default PARTITION OF log_aktivitas DEFAULT;      -- penampung data salah tanggal
CREATE INDEX ON log_aktivitas (pengguna_id, waktu);                          -- otomatis dibuat di setiap partisi

INSERT INTO log_aktivitas (pengguna_id, aksi, waktu)
SELECT g % 5000, (ARRAY['login','lihat','beli','logout'])[1 + g % 4],
       timestamptz '2026-08-01 00:00+07' + (g % 120) * interval '1 day' + (g % 3600) * interval '1 second'
FROM generate_series(1, 120000) g;
ANALYZE log_aktivitas;

SELECT tableoid::regclass AS partisi, count(*) FROM log_aktivitas GROUP BY 1 ORDER BY 1;

-- Partition pruning: query 1 minggu hanya menyentuh 1 partisi
EXPLAIN (COSTS OFF)
SELECT count(*) FROM log_aktivitas WHERE waktu >= '2026-11-10 00:00+07' AND waktu < '2026-11-17 00:00+07';

-- Retensi: lepas partisi Agustus (instan, tanpa DELETE jutaan baris dan tanpa bloat), arsipkan lalu hapus
ALTER TABLE log_aktivitas DETACH PARTITION log_aktivitas_202608;
DROP TABLE log_aktivitas_202608;
SELECT count(*) AS sisa_baris, min(waktu)::date AS data_tertua FROM log_aktivitas;'''

HEALTH = '''-- Skrip health check DBA: koneksi, query yang memblokir, transaksi menggantung, tabel bloat, indeks tak terpakai
CREATE EXTENSION IF NOT EXISTS dblink;
CREATE TABLE saldo (id int PRIMARY KEY, nilai int);
INSERT INTO saldo SELECT g, 1000 FROM generate_series(1, 1000) g;
CREATE INDEX saldo_nilai_idx ON saldo (nilai);                 -- indeks yang tidak pernah dipakai
UPDATE saldo SET nilai = nilai + 1;                             -- menghasilkan 1000 dead tuple
\\o /dev/null
SELECT pg_stat_force_next_flush();

-- Simulasi insiden: sesi A memegang kunci lalu diam (idle in transaction), sesi B menunggu
SELECT dblink_connect('a', format('dbname=%s host=/tmp port=%s user=postgres application_name=job_rekonsiliasi', current_database(), current_setting('port')));
SELECT dblink_connect('b', format('dbname=%s host=/tmp port=%s user=postgres application_name=api_transfer', current_database(), current_setting('port')));
SELECT dblink_exec('a', 'BEGIN; UPDATE saldo SET nilai = 0 WHERE id = 7');
SELECT dblink_send_query('b', 'UPDATE saldo SET nilai = 5 WHERE id = 7');
SELECT pg_sleep(0.5);
\\o

\\echo '== 1. Siapa memblokir siapa'
SELECT blocked.application_name AS menunggu, blocking.application_name AS pemblokir,
       blocking.state AS status_pemblokir, left(blocked.query, 45) AS query_tertahan
FROM pg_stat_activity blocked
JOIN pg_stat_activity blocking ON blocking.pid = ANY (pg_blocking_pids(blocked.pid));

\\echo '== 2. Tabel dengan dead tuple tinggi'
SELECT relname, n_live_tup, n_dead_tup, round(100.0 * n_dead_tup / nullif(n_live_tup + n_dead_tup, 0)) AS persen_mati
FROM pg_stat_user_tables WHERE n_dead_tup > 0 ORDER BY n_dead_tup DESC;

\\echo '== 3. Indeks yang tidak pernah dipakai (kandidat hapus setelah dicek di replika juga)'
SELECT indexrelname, idx_scan, pg_size_pretty(pg_relation_size(indexrelid)) AS ukuran
FROM pg_stat_user_indexes i JOIN pg_index USING (indexrelid)
WHERE idx_scan = 0 AND NOT indisunique;

\\echo '== 4. Tindakan: hentikan sesi pemblokir yang idle in transaction'
SELECT application_name, pg_terminate_backend(pid) AS dihentikan
FROM pg_stat_activity WHERE application_name = 'job_rekonsiliasi' AND state = 'idle in transaction';
\\o /dev/null
SELECT pg_sleep(0.3);
\\o
SELECT dblink_get_result('b') IS NOT NULL AS transfer_berhasil_lanjut;
SELECT nilai AS saldo_id7 FROM saldo WHERE id = 7;'''

MIGRASI = '''-- Migrasi tanpa downtime pada tabel yang sedang dipakai: tambah kolom wajib + indeks + FK
CREATE TABLE pengguna (id bigint PRIMARY KEY, email text NOT NULL);
CREATE TABLE cabang (id int PRIMARY KEY, nama text);
INSERT INTO cabang VALUES (1, 'Pusat'), (2, 'Medan');
INSERT INTO pengguna SELECT g, 'u' || g || '@contoh.id' FROM generate_series(1, 200000) g;

SET lock_timeout = '3s';            -- jangan pernah menunggu kunci tanpa batas di produksi

-- Langkah 1: kolom dengan DEFAULT konstan -> PostgreSQL 11+ tidak menulis ulang tabel (instan)
ALTER TABLE pengguna ADD COLUMN cabang_id int NOT NULL DEFAULT 1;
ALTER TABLE pengguna ADD COLUMN diverifikasi boolean;

-- Langkah 2: backfill bertahap per 50.000 baris (transaksi pendek, tidak menahan kunci lama)
DO $$
DECLARE awal bigint := 0; n int;
BEGIN
  LOOP
    UPDATE pengguna SET diverifikasi = false WHERE id > awal AND id <= awal + 50000 AND diverifikasi IS NULL;
    GET DIAGNOSTICS n = ROW_COUNT;
    EXIT WHEN awal >= 200000;
    RAISE NOTICE 'batch % sampai %: % baris', awal + 1, awal + 50000, n;
    awal := awal + 50000;
    COMMIT;
  END LOOP;
END $$;

-- Langkah 3: NOT NULL lewat CHECK NOT VALID lalu VALIDATE (validasi tanpa memblokir tulisan)
ALTER TABLE pengguna ADD CONSTRAINT diverifikasi_wajib CHECK (diverifikasi IS NOT NULL) NOT VALID;
ALTER TABLE pengguna VALIDATE CONSTRAINT diverifikasi_wajib;

-- Langkah 4: indeks tanpa memblokir INSERT/UPDATE
CREATE INDEX CONCURRENTLY pengguna_cabang_idx ON pengguna (cabang_id);

-- Langkah 5: foreign key NOT VALID lalu VALIDATE
ALTER TABLE pengguna ADD CONSTRAINT pengguna_cabang_fk FOREIGN KEY (cabang_id) REFERENCES cabang NOT VALID;
ALTER TABLE pengguna VALIDATE CONSTRAINT pengguna_cabang_fk;

\\d pengguna'''

DBA_MINI = [
MINI(1, 'Skema toko dengan constraint dan audit trail harga',
  'Toko online sering menemukan stok minus, SKU berantakan, dan tidak ada yang tahu siapa yang mengubah harga saat promo salah. Rancang skema inti yang menolak data salah di level database dan mencatat setiap perubahan harga secara otomatis.',
  ['Identity column, foreign key dengan ON DELETE RESTRICT', 'CHECK constraint untuk format SKU, harga > 0, stok ≥ 0', 'Tabel audit dan trigger BEFORE UPDATE OF harga', 'Bukti: baris salah ditolak dan perubahan harga tercatat beserta pelakunya'],
  ['Buat tabel referensi dulu (kategori), lalu produk dengan constraint lengkap.', 'Tulis fungsi trigger PL/pgSQL yang membandingkan OLD dan NEW dengan IS DISTINCT FROM.', 'Pasang trigger hanya untuk kolom harga agar perubahan stok tidak membanjiri audit.', 'Uji dengan data salah (harus ditolak) dan dua perubahan harga (harus tercatat).'],
  SKEMA, 'sql', out=pg(SKEMA),
  kunci='tambahkan ekstensi pgaudit untuk mencatat semua DDL, dan buat laporan perubahan harga harian untuk tim promo.',
  cek=q('Kenapa aturan stok ≥ 0 sebaiknya ditulis sebagai CHECK constraint, bukan hanya divalidasi di aplikasi?', ['Constraint selalu berlaku untuk semua jalur tulis (aplikasi, skrip, query manual), sehingga data tidak pernah rusak', 'Constraint membuat query SELECT lebih cepat', 'Aplikasi tidak bisa memvalidasi angka'], 0, 'Database adalah penjaga terakhir integritas data.')),

MINI(2, 'Tuning laporan penjualan yang lambat',
  'Laporan omzet per kota untuk bulan tertentu memakan waktu lama dan membebani database produksi setiap kali manajer membukanya. Diagnosis dengan EXPLAIN ANALYZE, perbaiki query dan indeks, lalu buktikan perbedaannya.',
  ['Baca rencana awal dan temukan penyebab (fungsi pada kolom tanggal, scan seluruh tabel)', 'Tulis ulang kondisi tanggal menjadi rentang yang sargable', 'Buat indeks parsial sesuai pola laporan dengan INCLUDE', 'Bandingkan rencana sebelum dan sesudah, dan pastikan hasilnya sama'],
  ['Jalankan EXPLAIN (ANALYZE) dan cari "Rows Removed by Filter" yang besar.', 'Ganti to_char(dibuat) = ... dengan dibuat >= awal AND dibuat < awal bulan berikutnya.', 'Buat indeks pada (dibuat) WHERE status = selesai, sertakan pelanggan_id dan total.', 'VACUUM ANALYZE, ulangi EXPLAIN, dan jalankan query final.'],
  TUNING, 'sql', out=pg(TUNING, DATA_TOKO),
  kunci='aktifkan pg_stat_statements dan auto_explain (log_min_duration 500 ms) agar query lambat berikutnya ketahuan otomatis.',
  cek=q('Kenapa to_char(dibuat, \'YYYY-MM\') = \'2026-10\' tidak bisa memakai indeks pada kolom dibuat?', ['Indeks menyimpan nilai dibuat, bukan hasil fungsi; planner harus menghitung fungsi untuk setiap baris', 'Karena to_char tidak ada di PostgreSQL', 'Karena indeks tidak bisa dipakai untuk tanggal'], 0, 'Tulis kondisi yang sargable.')),

MINI(3, 'Isolasi data multi-tenant dengan Row-Level Security',
  'Aplikasi SaaS kasir melayani ribuan toko dalam satu database. Satu bug WHERE yang terlupa bisa membocorkan penjualan toko lain. Terapkan RLS sebagai lapisan pengaman kedua yang tetap aman walau aplikasi lupa memfilter.',
  ['Kolom tenant_id di setiap tabel bisnis dan indeksnya', 'Policy USING dan WITH CHECK berbasis setelan sesi app.tenant_id', 'FORCE ROW LEVEL SECURITY dan role aplikasi tanpa hak BYPASSRLS', 'Bukti: tanpa konteks tidak melihat apa pun, tidak bisa menyisipkan data ke tenant lain'],
  ['Tambahkan tenant_id NOT NULL + indeks agar filter RLS tetap cepat.', 'Aktifkan dan paksa RLS, lalu buat policy dengan current_setting(..., true) agar gagal aman.', 'Aplikasi memanggil SET LOCAL app.tenant_id di awal setiap transaksi.', 'Uji tiga skenario: tanpa tenant, tenant 1 (update dan sisipan jahat), tenant 2.'],
  RLS, 'sql', out=pg(RLS, DIAM),
  kunci='uji performa dengan 10.000 tenant, dan pastikan pooler PgBouncer mode transaction tetap aman karena memakai SET LOCAL.',
  cek=q('Kenapa memakai SET LOCAL, bukan SET, untuk app.tenant_id di balik connection pooler?', ['SET LOCAL hanya berlaku sampai transaksi selesai, sehingga koneksi yang dipakai ulang tidak membawa tenant pengguna sebelumnya', 'SET LOCAL lebih cepat dieksekusi', 'SET tidak bisa dipakai untuk teks'], 0, 'Konteks bocor antar-request adalah bug klasik pooler.')),

MINI(4, 'Partisi tabel log per bulan dengan retensi',
  'Tabel log aktivitas tumbuh 40 juta baris per bulan. DELETE data lama tiap malam memakan berjam-jam dan membuat bloat. Ubah menjadi tabel berpartisi per bulan, buktikan partition pruning, dan terapkan retensi dengan melepas partisi.',
  ['Declarative partitioning RANGE per bulan dibuat dengan perulangan', 'Partisi DEFAULT untuk data bertanggal di luar rentang', 'Indeks di tabel induk yang otomatis menurun ke setiap partisi', 'Retensi: DETACH lalu DROP partisi lama, bukan DELETE'],
  ['Buat tabel induk PARTITION BY RANGE (waktu) dengan primary key yang menyertakan waktu.', 'Gunakan DO block + format() untuk membuat partisi bulanan.', 'Isi data, lalu periksa sebaran baris per partisi dan EXPLAIN untuk query satu minggu.', 'Lepas partisi tertua dan pastikan data tertua kini bulan berikutnya.'],
  PARTISI, 'sql', out=pg(PARTISI),
  kunci='otomatiskan pembuatan partisi bulan depan dan penghapusan partisi lama dengan pg_partman + pg_cron, dan arsipkan partisi ke Parquet di object storage sebelum DROP.',
  cek=q('Kenapa menghapus data lama dengan DROP partisi lebih baik daripada DELETE?', ['DROP partisi instan dan tidak meninggalkan dead tuple, sedangkan DELETE jutaan baris lambat, menghasilkan WAL besar, dan bloat', 'DELETE tidak bisa dipakai di PostgreSQL', 'DROP partisi menyimpan data ke arsip otomatis'], 0, 'Retensi berbasis partisi.')),

MINI(5, 'Health check DBA: blocking, bloat, dan indeks tak terpakai',
  'Tengah malam, API transfer tiba-tiba timeout. Ternyata sebuah job rekonsiliasi membuka transaksi lalu macet sambil memegang kunci. Buat skrip health check yang menemukan pemblokir, tabel bloat, dan indeks mubazir, lalu tangani insidennya.',
  ['Simulasi dua sesi sungguhan (dblink): satu idle in transaction, satu menunggu', 'Query pemblokir memakai pg_blocking_pids', 'Laporan dead tuple dan indeks yang tidak pernah dipakai', 'Tindakan terukur: hentikan hanya sesi pemblokir, lalu verifikasi transaksi yang tertahan berhasil'],
  ['Buat dua koneksi dblink dengan application_name berbeda agar mudah dikenali.', 'Join pg_stat_activity dengan dirinya sendiri lewat pg_blocking_pids(pid).', 'Baca pg_stat_user_tables dan pg_stat_user_indexes untuk bloat dan indeks tak terpakai.', 'Hentikan sesi dengan pg_terminate_backend, lalu pastikan sesi B melanjutkan transaksinya.'],
  HEALTH, 'sql', out=pg(HEALTH),
  kunci='set idle_in_transaction_session_timeout = 5min untuk role job, kirim hasil health check ke Slack setiap pagi, dan buat dashboard Grafana dari query yang sama.',
  cek=q('Apa risiko sesi "idle in transaction" yang dibiarkan lama?', ['Menahan kunci sehingga query lain menunggu, dan menghambat VACUUM membersihkan dead tuple', 'Menghemat memori server', 'Tidak ada risiko karena sesi sedang diam'], 0, 'Pasang idle_in_transaction_session_timeout.')),

MINI(6, 'Migrasi skema tanpa downtime',
  'Tim produk butuh kolom cabang wajib, flag verifikasi, indeks, dan foreign key di tabel pengguna yang sedang melayani ribuan request per detik. Migrasi naif dengan ALTER TABLE ... NOT NULL dan CREATE INDEX biasa bisa mengunci tabel bermenit-menit.',
  ['lock_timeout agar migrasi gagal cepat alih-alih menahan antrean', 'Kolom dengan DEFAULT konstan (instan sejak PostgreSQL 11)', 'Backfill bertahap per batch dengan COMMIT di prosedur', 'CHECK/FK NOT VALID lalu VALIDATE, dan CREATE INDEX CONCURRENTLY'],
  ['Set lock_timeout di awal setiap skrip migrasi.', 'Tambahkan kolom; isi kolom baru dalam batch kecil dengan DO block yang melakukan COMMIT per batch.', 'Tambahkan constraint NOT VALID (cepat), lalu VALIDATE (tidak memblokir tulisan).', 'Buat indeks dengan CONCURRENTLY dan periksa hasil akhir dengan \\d.'],
  MIGRASI, 'sql', out=pg(MIGRASI),
  kunci='kemas langkah-langkah ini sebagai migrasi Flyway/sqitch dengan versi, dan uji di salinan database produksi (dari backup) sebelum dijalankan.',
  cek=q('Apa keuntungan menambah constraint dengan NOT VALID lalu VALIDATE CONSTRAINT secara terpisah?', ['Pemeriksaan baris lama dilakukan tanpa mengunci tulisan, sementara baris baru langsung diperiksa sejak constraint ditambahkan', 'Constraint menjadi opsional', 'Tabel otomatis dipartisi'], 0, 'Pola migrasi aman di tabel besar.')),
]

# ---------------------------------------------------------------- BESAR
HA = r'''# cluster.yaml — CloudNativePG: PostgreSQL 16 HA 3 instance di Kubernetes, backup ke object storage, PITR
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata: { name: toko-db, namespace: data }
spec:
  instances: 3                                   # 1 primary + 2 standby di zona berbeda
  imageName: ghcr.io/cloudnative-pg/postgresql:16.6
  minSyncReplicas: 1
  maxSyncReplicas: 1                             # RPO 0 untuk transaksi
  postgresql:
    parameters:
      shared_buffers: 4GB
      effective_cache_size: 12GB
      work_mem: 32MB
      max_connections: "300"
      wal_compression: zstd
      idle_in_transaction_session_timeout: 5min
      shared_preload_libraries: pg_stat_statements,pgaudit
  affinity: { topologyKey: topology.kubernetes.io/zone, enablePodAntiAffinity: true }
  storage: { size: 500Gi, storageClass: premium-rwo }
  walStorage: { size: 100Gi, storageClass: premium-rwo }   # WAL di disk terpisah
  backup:
    retentionPolicy: "30d"
    barmanObjectStore:
      destinationPath: s3://backup-db-prod/toko
      s3Credentials: { inheritFromIAMRole: true }
      wal: { compression: zstd, maxParallel: 4 }
  monitoring: { enablePodMonitor: true }         # metrik ke Prometheus
---
apiVersion: postgresql.cnpg.io/v1
kind: ScheduledBackup
metadata: { name: toko-db-harian, namespace: data }
spec: { schedule: "0 0 18 * * *", cluster: { name: toko-db }, backupOwnerReference: self }   # 01.00 WIB
---
apiVersion: postgresql.cnpg.io/v1
kind: Pooler
metadata: { name: toko-db-rw, namespace: data }
spec: { cluster: { name: toko-db }, instances: 2, type: rw, pgbouncer: { poolMode: transaction, parameters: { max_client_conn: "5000", default_pool_size: "40" } } }

# Restore drill bulanan: buat cluster baru dari backup ke titik waktu tertentu, jalankan cek checksum & jumlah baris
#   bootstrap: { recovery: { source: toko-db, recoveryTarget: { targetTime: "2026-11-19 14:32:00+07" } } }
# Uji failover kuartalan: kubectl cnpg promote toko-db toko-db-2   -> ukur waktu sampai aplikasi pulih (target < 30 s)'''

UPGRADE = r'''-- Upgrade PostgreSQL 12 (EOL) -> 16 dengan logical replication: downtime hanya beberapa detik saat cutover
-- ===== Di server LAMA (12) =====
ALTER SYSTEM SET wal_level = logical;                     -- butuh restart terjadwal sekali
CREATE ROLE replikator WITH LOGIN REPLICATION PASSWORD :'sandi';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO replikator;
-- Semua tabel wajib punya primary key atau REPLICA IDENTITY agar UPDATE/DELETE bisa direplikasi
SELECT c.relname FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public' AND c.relkind = 'r'
  AND NOT EXISTS (SELECT 1 FROM pg_index i WHERE i.indrelid = c.oid AND i.indisprimary);
CREATE PUBLICATION pub_upgrade FOR ALL TABLES;

-- ===== Di server BARU (16) =====
-- 1) Skema saja: pg_dump --schema-only -d toko_lama | psql -d toko
-- 2) Langganan: salinan awal + perubahan berjalan
CREATE SUBSCRIPTION sub_upgrade
  CONNECTION 'host=db-lama.internal dbname=toko user=replikator sslmode=require'
  PUBLICATION pub_upgrade WITH (copy_data = true, streaming = on);

-- 3) Pantau sampai lag ~0
SELECT subname, received_lsn, latest_end_lsn, last_msg_receipt_time FROM pg_stat_subscription;

-- 4) Validasi data: jumlah baris dan checksum per tabel di kedua sisi
SELECT 'pesanan' AS tabel, count(*), md5(string_agg(id::text || total::text, ',' ORDER BY id)) FROM pesanan;

-- ===== Cutover (jendela 5 menit, diumumkan) =====
-- a) Aplikasi mode baca-saja / PgBouncer PAUSE
-- b) Pastikan lag 0, lalu SINKRONKAN SEQUENCE (logical replication tidak membawa nilai sequence):
SELECT format('SELECT setval(%L, %s, true);', sequencename, last_value)
FROM pg_sequences WHERE last_value IS NOT NULL;           -- jalankan di lama, eksekusi hasilnya di baru
-- c) DROP SUBSCRIPTION sub_upgrade;  arahkan PgBouncer ke server baru;  RESUME
-- d) ANALYZE semua tabel di server baru; pantau pg_stat_statements 24 jam; server lama dibiarkan 7 hari untuk rollback'''

TUNE = r'''# postgresql.conf — server OLTP fintech: 32 vCPU, 128 GB RAM, NVMe; titik awal lalu disesuaikan dengan data
shared_buffers = 32GB                    # ~25% RAM
effective_cache_size = 96GB              # ~75% RAM: petunjuk untuk planner
work_mem = 16MB                          # per operasi sort/hash; laporan berat pakai role khusus dengan nilai lebih besar
maintenance_work_mem = 2GB               # VACUUM, CREATE INDEX lebih cepat
max_connections = 300                    # ribuan koneksi aplikasi lewat PgBouncer, bukan langsung
random_page_cost = 1.1                   # NVMe: akses acak hampir semurah berurutan
effective_io_concurrency = 200
wal_compression = zstd
max_wal_size = 32GB                      # checkpoint lebih jarang, I/O lebih rata
checkpoint_completion_target = 0.9
autovacuum_max_workers = 6
autovacuum_vacuum_cost_limit = 2000      # autovacuum cukup agresif untuk tabel transaksi
log_min_duration_statement = 500ms       # catat query > 0,5 detik
log_lock_waits = on
shared_preload_libraries = 'pg_stat_statements,auto_explain'
auto_explain.log_min_duration = '2s'
auto_explain.log_analyze = on

# pgbouncer.ini
[databases]
ledger = host=10.10.1.10 port=5432 dbname=ledger
[pgbouncer]
pool_mode = transaction
max_client_conn = 8000
default_pool_size = 60
server_idle_timeout = 60
query_wait_timeout = 15

-- Laporan mingguan "Top 10 query" untuk tim engineering (dari pg_stat_statements)
SELECT queryid, calls, round(total_exec_time / 1000) AS total_detik, round(mean_exec_time, 1) AS rata_ms,
       round(100 * total_exec_time / sum(total_exec_time) OVER (), 1) AS persen_beban,
       shared_blks_read, temp_blks_written, left(query, 80) AS query
FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 10;'''

AMAN = r'''-- Keamanan & kepatuhan database layanan kesehatan (UU PDP, audit, prinsip least privilege)
-- 1) Audit: siapa membaca/mengubah data sensitif (pgaudit) -> dikirim ke SIEM
ALTER SYSTEM SET pgaudit.log = 'ddl, role, write';
ALTER ROLE dokter SET pgaudit.log = 'read, write';          -- akses rekam medis oleh dokter diaudit penuh
SELECT pg_reload_conf();

-- 2) Pemisahan data: PII di schema terpisah, kolom sensitif dienkripsi di aplikasi (envelope encryption + KMS)
CREATE SCHEMA pii AUTHORIZATION pemilik_data;
CREATE TABLE pii.pasien (id uuid PRIMARY KEY, nik_hash bytea UNIQUE, nik_enc bytea, nama text, tgl_lahir date, hp_enc bytea);
REVOKE ALL ON SCHEMA pii FROM PUBLIC;

-- 3) View tersamar untuk analis: tidak pernah melihat NIK/HP asli, umur dibulatkan per 5 tahun
CREATE VIEW analitik.pasien_tersamar WITH (security_barrier) AS
SELECT id, left(nama, 1) || '***' AS inisial, (date_part('year', age(tgl_lahir))::int / 5) * 5 AS kelompok_umur
FROM pii.pasien;
GRANT SELECT ON analitik.pasien_tersamar TO analis;

-- 4) Akses just-in-time: role darurat aktif maksimal 2 jam, dicatat dan disetujui lewat tiket
CREATE ROLE dba_darurat NOLOGIN;
-- (otomasi) GRANT dba_darurat TO budi;  ALTER ROLE budi VALID UNTIL now() + interval '2 hours';

-- 5) Hak subjek data: penghapusan (right to erasure) dengan jejak audit, bukan DELETE diam-diam
CREATE PROCEDURE pii.hapus_pasien(p_id uuid, p_tiket text) LANGUAGE plpgsql SECURITY DEFINER SET search_path = pii, pg_temp AS $$
BEGIN
  UPDATE pii.pasien SET nik_enc = NULL, hp_enc = NULL, nama = '[dihapus]' WHERE id = p_id;
  INSERT INTO audit.permintaan_data (pasien_id, jenis, tiket, waktu) VALUES (p_id, 'hapus', p_tiket, now());
END $$;
REVOKE ALL ON PROCEDURE pii.hapus_pasien FROM PUBLIC;
GRANT EXECUTE ON PROCEDURE pii.hapus_pasien TO petugas_privasi;

-- 6) Pemeriksaan berkala: role dengan hak berlebih, password kedaluwarsa, koneksi tanpa SSL
SELECT rolname, rolsuper, rolbypassrls, rolvaliduntil FROM pg_roles WHERE rolsuper OR rolbypassrls ORDER BY 1;
SELECT usename, client_addr, ssl FROM pg_stat_ssl JOIN pg_stat_activity USING (pid) WHERE NOT ssl AND client_addr IS NOT NULL;'''

DBA_BESAR = [
BESAR(1, 'PostgreSQL high availability di Kubernetes dengan backup dan PITR',
  'Marketplace menjalankan PostgreSQL di satu VM tanpa replika. Saat disk rusak, toko mati 6 jam dan data 4 jam terakhir hilang. Targetnya RPO 0 untuk transaksi, RTO < 1 menit, dan restore yang teruji setiap bulan.',
  ['Cluster 3 instance di zona berbeda dengan failover otomatis', 'Replikasi sinkron minimal 1 standby (RPO 0)', 'Backup harian + arsip WAL terus-menerus ke object storage, retensi 30 hari', 'Connection pooler (PgBouncer) dan pemisahan endpoint baca/tulis', 'Restore drill bulanan dan uji failover kuartalan dengan hasil terukur'],
  'Kubernetes, CloudNativePG (atau Patroni di VM), PgBouncer, S3/GCS dengan IAM, Prometheus + Grafana, pgaudit',
  [('Topologi', '1 primary + 2 standby anti-affinity per zona; WAL di volume terpisah'), ('Durabilitas', 'synchronous standby 1, wal_compression zstd, arsip WAL ke object storage'),
   ('Akses', 'Pooler rw (transaction mode) dan ro untuk laporan; aplikasi tidak tahu primary mana'), ('Backup', 'base backup harian 01.00 WIB + WAL kontinu; PITR ke detik mana pun dalam 30 hari'),
   ('Pemantauan', 'lag replikasi, umur backup terakhir, ruang disk, koneksi, query lambat; alert ke on-call'), ('Uji', 'restore drill bulanan (catat durasi & validasi data), failover kuartalan (target < 30 s)')],
  ['Ukur kebutuhan: ukuran data, laju WAL per jam, RPO/RTO yang disepakati bisnis.', 'Pasang operator dan cluster di staging; uji failover dengan mematikan pod primary.', 'Konfigurasikan backup + arsip WAL, lakukan PITR percobaan ke cluster baru.', 'Migrasikan data produksi (logical replication) dan pindahkan aplikasi lewat Pooler.', 'Jadwalkan drill, dokumentasikan runbook, dan pantau SLO.'],
  HA, 'yaml', standar='RPO dan RTO tertulis dan terbukti lewat drill, backup diuji secara berkala, failover otomatis teruji, akses lewat pooler, pemantauan dan runbook tersedia',
  cek=q('Apa yang membuat RPO menjadi 0 pada arsitektur ini?', ['Replikasi sinkron: commit baru dianggap berhasil setelah minimal satu standby menerima WAL-nya', 'Backup harian pukul 01.00', 'PgBouncer mode transaction'], 0, 'Synchronous replication.')),

BESAR(2, 'Upgrade versi besar PostgreSQL dengan downtime minimal',
  'Perusahaan logistik masih memakai PostgreSQL 12 yang sudah end-of-life, dengan database 2 TB yang melayani pelacakan paket 24 jam. pg_upgrade di tempat berisiko dan butuh jendela panjang. Targetnya: pindah ke PostgreSQL 16 dengan downtime di bawah 5 menit dan rencana rollback.',
  ['Inventaris: ekstensi, tabel tanpa primary key, fitur usang, kompatibilitas aplikasi', 'Logical replication dari 12 ke 16 dengan salinan awal dan perubahan berjalan', 'Validasi data: jumlah baris dan checksum per tabel', 'Sinkronisasi sequence dan cutover lewat PgBouncer PAUSE/RESUME', 'Rollback plan: server lama dipertahankan dan bisa menjadi tujuan replikasi balik'],
  'PostgreSQL 12 → 16, logical replication (publication/subscription), pg_dump --schema-only, PgBouncer, pgBackRest, skrip validasi Python',
  [('Persiapan', 'wal_level = logical, replica identity semua tabel, uji aplikasi di 16 (staging)'), ('Sinkronisasi', 'publication FOR ALL TABLES, subscription copy_data + streaming'),
   ('Validasi', 'count + md5 per tabel/partisi, sampling query bisnis kritis di kedua sisi'), ('Cutover', 'PAUSE pooler → lag 0 → setval sequence → ganti host → RESUME; target < 5 menit'),
   ('Pasca', 'ANALYZE penuh, pantau pg_stat_statements dan error 24 jam, server lama standby 7 hari'), ('Risiko', 'DDL selama replikasi tidak ikut (freeze migrasi skema), sequence, large objects')],
  ['Audit kompatibilitas dan perbaiki tabel tanpa primary key.', 'Bangun server 16, salin skema, buat subscription, dan pantau sampai lag nol.', 'Jalankan validasi data otomatis dan uji beban baca di server baru.', 'Gladi bersih cutover di staging dengan stopwatch; susun runbook menit per menit.', 'Cutover produksi di jam sepi, pantau, dan pensiunkan server lama setelah masa aman.'],
  UPGRADE, 'sql', standar='downtime terukur sesuai target, data tervalidasi dengan checksum, sequence tersinkron, runbook dan rollback teruji di gladi bersih',
  cek=q('Kenapa nilai sequence harus disinkronkan manual saat cutover dengan logical replication?', ['Logical replication menyalin baris tabel tetapi tidak menyalin posisi sequence, sehingga INSERT pertama di server baru bisa bentrok primary key', 'Sequence tidak ada di PostgreSQL 16', 'Agar indeks dibangun ulang'], 0, 'Langkah yang sering terlupa.')),

BESAR(3, 'Tuning dan observability database fintech',
  'Aplikasi pembayaran mengalami latensi p99 naik dari 80 ms ke 2 detik setiap tanggal gajian. CPU database 95%, koneksi penuh, dan tim saling menyalahkan antara aplikasi dan database. Kamu diminta menemukan akar masalah dengan data dan menyiapkan observability berkelanjutan.',
  ['Baseline metrik: TPS, latensi, koneksi, cache hit, I/O, lock waits', 'pg_stat_statements + auto_explain untuk menemukan query terberat dan rencana buruknya', 'Konfigurasi memori/WAL/autovacuum sesuai hardware dan beban', 'PgBouncer transaction pooling untuk mengendalikan koneksi', 'Dashboard dan laporan mingguan Top-10 query untuk tim engineering'],
  'PostgreSQL 16, pg_stat_statements, auto_explain, PgBouncer, postgres_exporter + Prometheus + Grafana, pganalyze/pgBadger, pgbench untuk uji beban',
  [('Diagnosis', 'korelasikan lonjakan dengan pg_stat_statements per jam; cari query dengan persen beban tertinggi'), ('Query', 'indeks yang tepat, hapus N+1 dari ORM, batasi kolom, keyset pagination'),
   ('Koneksi', '8.000 klien → 60 koneksi server per pool; query_wait_timeout untuk gagal cepat'), ('Konfigurasi', 'shared_buffers 25%, random_page_cost 1.1 (NVMe), checkpoint diratakan, autovacuum agresif'),
   ('Observability', 'Grafana: TPS, p95/p99, lock waits, replikasi, bloat; log query > 500 ms'), ('Proses', 'review indeks di setiap PR yang mengubah query; laporan Top-10 setiap Senin')],
  ['Kumpulkan baseline 1 minggu termasuk tanggal gajian sebelumnya.', 'Urutkan query berdasarkan total waktu; perbaiki 3 teratas bersama developer dan ukur ulang.', 'Pasang PgBouncer dan sesuaikan konfigurasi; uji dengan pgbench dan replay beban.', 'Bangun dashboard + alert dan laporan mingguan otomatis.', 'Bandingkan metrik sebelum dan sesudah di tanggal gajian berikutnya; dokumentasikan.'],
  TUNE, 'conf', standar='keputusan berbasis metrik sebelum/sesudah, query terberat ditangani di akar masalah, koneksi dikendalikan pooler, observability berkelanjutan dan bisa dibaca developer',
  cek=q('Kenapa query diurutkan berdasarkan total_exec_time, bukan mean_exec_time, saat mencari prioritas tuning?', ['Query cepat yang dipanggil jutaan kali bisa memakan beban server lebih besar daripada query lambat yang jarang dipanggil', 'Karena mean_exec_time selalu nol', 'Agar laporan lebih pendek'], 0, 'Dampak total = waktu × jumlah panggilan.')),

BESAR(4, 'Keamanan dan kepatuhan database data sensitif',
  'Jaringan klinik menyimpan rekam medis dan data pribadi 3 juta pasien. Audit internal menemukan analis memakai akun superuser bersama, NIK tersimpan polos, tidak ada jejak siapa membaca data pasien, dan permintaan penghapusan data sesuai UU PDP belum bisa dipenuhi.',
  ['Role per fungsi dengan least privilege; tidak ada akun bersama dan superuser untuk aplikasi', 'Enkripsi kolom sensitif (envelope encryption + KMS) dan hash untuk pencarian', 'Audit akses dengan pgaudit ke SIEM; akses data pasien oleh dokter tercatat', 'View tersamar untuk analitik; akses darurat just-in-time dengan batas waktu', 'Prosedur hak subjek data (akses, koreksi, hapus) dengan jejak audit'],
  'PostgreSQL 16, pgaudit, pgcrypto/enkripsi di aplikasi + KMS (AWS KMS/GCP KMS/HashiCorp Vault), RLS, SSL/TLS 1.3, SIEM (Wazuh/Elastic), Teleport/Boundary untuk akses',
  [('Identitas', 'SSO + akses lewat bastion (Teleport); password diganti secret dinamis dari Vault'), ('Data', 'schema pii terpisah, kolom NIK/HP terenkripsi, nik_hash untuk pencarian persis'),
   ('Akses', 'role per fungsi, view tersamar untuk analis, RLS per klinik, JIT untuk DBA'), ('Audit', 'pgaudit read/write untuk tabel PII, log dikirim ke SIEM, retensi sesuai regulasi'),
   ('Jaringan', 'hostssl saja, TLS 1.3, database tidak terbuka ke internet'), ('Kepatuhan', 'prosedur hak subjek data, pemberitahuan insiden 3×24 jam, review akses per kuartal')],
  ['Inventarisasi data sensitif dan pemetaan siapa butuh akses apa (bersama legal & DPO).', 'Bangun role per fungsi, cabut superuser bersama, pasang akses lewat bastion dengan SSO.', 'Migrasikan kolom sensitif ke bentuk terenkripsi secara bertahap; buat view tersamar.', 'Aktifkan pgaudit + SIEM; buat alert untuk pola akses tidak wajar.', 'Implementasikan prosedur hak subjek data dan jadwalkan review akses kuartalan.'],
  AMAN, 'sql', standar='least privilege terbukti dari audit role, data sensitif tidak tersimpan polos, setiap akses data pasien tercatat, hak subjek data bisa dipenuhi dengan jejak, review akses berkala',
  cek=q('Kenapa NIK disimpan sebagai hash (untuk pencarian) dan ciphertext (untuk ditampilkan) secara terpisah?', ['Hash memungkinkan pencarian persis tanpa mendekripsi, sedangkan ciphertext hanya didekripsi oleh layanan berizin saat benar-benar perlu', 'Agar ukuran tabel lebih kecil', 'Karena PostgreSQL tidak bisa menyimpan angka 16 digit'], 0, 'Pisahkan kebutuhan cari dan tampil.')),
]

PJ_DBA = JALUR_M('DBA PostgreSQL', 'Menengah',
  'Enam proyek mini yang dijalankan di PostgreSQL 16 sungguhan (skema dengan constraint dan audit trigger, tuning laporan lambat, isolasi multi-tenant dengan RLS, partisi dan retensi, health check blocking dan bloat, migrasi tanpa downtime) dan empat proyek besar berskala industri 2026-2027 (HA di Kubernetes dengan PITR, upgrade versi besar via logical replication, tuning dan observability fintech, keamanan dan kepatuhan data sensitif), lengkap dengan penyelesaiannya.',
  ['PostgreSQL', 'Tuning', 'Row-Level Security', 'High availability', 'Security'], DBA_MINI, DBA_BESAR)
