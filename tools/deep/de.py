"""Pendalaman jalur Data Engineering: istilah dunia kerja dan contoh (Python dijalankan; Airflow/Spark/Terraform sebagai kode rujukan)."""
K = 'de'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def S(t, code, lang, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Siklus hidup data engineering': dict(
  ist=[('Source system', 'Sistem asal data: database aplikasi, API pihak ketiga, log, file dari mitra.'),
       ('Ingestion', 'Proses mengambil data dari sumber ke platform data.'),
       ('Serving layer', 'Lapisan tempat data siap dipakai: dashboard, model ML, reverse ETL.'),
       ('Undercurrents', 'Hal yang menyertai semua tahap: keamanan, data management, DataOps, orkestrasi, arsitektur (istilah dari buku Fundamentals of Data Engineering).'),
       ('SLA data', 'Janji kapan data tersedia, misalnya "laporan penjualan kemarin siap jam 07.00".')],
  cx=[P('Siklus mini: generate → ingest → transform → serve', '''
import csv, io, sqlite3

# 1) Source system: ekspor CSV dari aplikasi kasir
sumber = io.StringIO("id,tanggal,cabang,total\\n1,2026-11-18,Medan,125000\\n2,2026-11-18,Medan,98000\\n3,2026-11-18,Bandung,210500\\n")

# 2) Ingestion: muat apa adanya ke tabel raw
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE raw_penjualan (id INT, tanggal TEXT, cabang TEXT, total INT)")
db.executemany("INSERT INTO raw_penjualan VALUES (?,?,?,?)", [tuple(r.values()) for r in csv.DictReader(sumber)])

# 3) Transformation: model siap pakai
db.execute("""CREATE TABLE mart_penjualan_harian AS
              SELECT tanggal, cabang, COUNT(*) trx, SUM(total) omzet FROM raw_penjualan GROUP BY 1, 2""")

# 4) Serving: dibaca dashboard
for baris in db.execute("SELECT * FROM mart_penjualan_harian ORDER BY omzet DESC"):
    print(baris)
''')]),

'Data engineer, analyst & scientist': dict(
  ist=[('Analytics engineer', 'Peran di antara DE dan analis: memodelkan data di warehouse dengan SQL/dbt, menjaga definisi metrik.'),
       ('Platform engineer (data)', 'Membangun infrastruktur data (cluster, CI, akses) yang dipakai tim lain.'),
       ('Data product', 'Dataset atau layanan data yang punya pemilik, dokumentasi, SLA, dan pengguna jelas.'),
       ('Hand-off', 'Serah terima antar peran; titik rawan salah paham definisi.')],
  cx=[P('Siapa mengerjakan apa: satu permintaan, tiga peran', '''
permintaan = "Kenapa repeat order turun 15% bulan ini?"
tugas = [
    ("Data engineer", "Pastikan data order & pelanggan masuk tiap jam, tanpa duplikat; tambah tabel event aplikasi."),
    ("Analytics engineer", "Definisikan repeat_order di dbt; satu definisi untuk semua dashboard."),
    ("Data analyst", "Pecah penurunan per kota, kanal, dan kohort; laporkan ke manajer."),
    ("Data scientist", "Bangun model prediksi pelanggan berisiko tidak repeat; uji A/B voucher."),
]
print("Permintaan:", permintaan)
for peran, kerja in tugas:
    print(f"- {peran:18} {kerja}")
''')]),

'Linux & shell untuk data': dict(
  ist=[('Pipe (|)', 'Menyambung keluaran satu perintah ke masukan perintah lain.'),
       ('grep, awk, sort, uniq, wc', 'Alat baris perintah untuk menyaring dan meringkas teks tanpa memuat semua ke memori.'),
       ('cron', 'Penjadwal bawaan Linux; pendahulu orkestrator seperti Airflow.'),
       ('Exit code', '0 berarti sukses; selain 0 berarti gagal. Orkestrator memakai ini untuk menandai task gagal.'),
       ('set -euo pipefail', 'Baris wajib di skrip bash produksi agar error tidak diam-diam diabaikan.')],
  cx=[S('Meringkas log akses tanpa Python', '''
#!/usr/bin/env bash
set -euo pipefail

# 10 endpoint paling sering error 5xx kemarin
zcat /var/log/nginx/access.log.1.gz \\
  | awk '$9 ~ /^5/ {print $7}' \\
  | sort | uniq -c | sort -rn | head -10

# ukuran file per partisi tanggal
du -sh /data/raw/penjualan/tanggal=2026-11-* | sort -k2

# jadwal di crontab: setiap hari 01:30
# 30 1 * * * /opt/etl/muat_penjualan.sh >> /var/log/etl.log 2>&1
''', 'bash'),
      P('Hal yang sama dengan Python streaming (hemat memori)', '''
import collections, io
log = io.StringIO("""1.1.1.1 - - [18/Nov/2026:10:01:02 +0700] "GET /api/produk HTTP/1.1" 200 512
2.2.2.2 - - [18/Nov/2026:10:01:05 +0700] "POST /api/checkout HTTP/1.1" 502 0
3.3.3.3 - - [18/Nov/2026:10:02:11 +0700] "POST /api/checkout HTTP/1.1" 503 0
4.4.4.4 - - [18/Nov/2026:10:03:40 +0700] "GET /api/keranjang HTTP/1.1" 500 0
""")
hitung = collections.Counter()
for baris in log:                      # baris per baris, tidak memuat seluruh file
    bagian = baris.split()              # awk: $9 = bagian[8] (status), $7 = bagian[6] (path)
    if bagian[8].startswith("5"):
        hitung[bagian[6]] += 1
for path, n in hitung.most_common():
    print(f"{n:>3} {path}")
''')]),

'Dasar sistem terdistribusi': dict(
  ist=[('Horizontal scaling', 'Menambah mesin, bukan memperbesar satu mesin (vertical).'),
       ('Partitioning / sharding', 'Membagi data ke beberapa node berdasarkan kunci.'),
       ('Replication', 'Menyalin data ke beberapa node untuk ketahanan dan baca paralel.'),
       ('At-least-once / exactly-once', 'Jaminan pengiriman pesan; at-least-once berarti duplikat mungkin terjadi.'),
       ('Data skew', 'Satu partisi jauh lebih besar dari yang lain sehingga satu node menjadi lambat.')],
  cx=[P('Hash partitioning dan deteksi data skew', '''
import hashlib, collections

def partisi(kunci, n):
    return int(hashlib.md5(kunci.encode()).hexdigest(), 16) % n

# 10.000 order; satu merchant besar menyumbang 40%
order = ["merchant_besar"] * 4000 + [f"merchant_{i % 600}" for i in range(6000)]
beban = collections.Counter(partisi(m, 4) for m in order)
for p in range(4):
    print(f"partisi {p}: {beban[p]:>5} baris {'#' * (beban[p] // 250)}")

# salting: pecah kunci panas menjadi 8 sub-kunci (merchant_besar#0..#7)
beban2 = collections.Counter(partisi(m + (f"#{i % 8}" if m == "merchant_besar" else ""), 4) for i, m in enumerate(order))
print("setelah salting:", [beban2[p] for p in range(4)])
''')]),

'OLTP vs OLAP & penyimpanan kolom': dict(
  ist=[('OLTP', 'Sistem transaksi: banyak operasi kecil (insert/update satu baris), contoh PostgreSQL aplikasi.'),
       ('OLAP', 'Sistem analitik: sedikit query besar yang memindai jutaan baris, contoh BigQuery, Snowflake, ClickHouse.'),
       ('Columnar storage', 'Data disimpan per kolom sehingga query yang hanya butuh 3 kolom tidak membaca 50 kolom lain.'),
       ('Compression', 'Kolom berisi nilai mirip dikompres jauh lebih kecil (dictionary, run-length encoding).')],
  cx=[P('Row store vs column store: berapa byte yang dibaca?', '''
import random, zlib, json
random.seed(1)
kota = ["Medan", "Bandung", "Surabaya", "Makassar"]
baris = [{"id": i, "kota": random.choice(kota), "total": random.randint(10, 500) * 1000,
          "catatan": "x" * 60, "alamat": "Jl. Contoh No. %d" % i} for i in range(20_000)]

row_store = [json.dumps(b).encode() for b in baris]
kolom = {k: json.dumps([b[k] for b in baris]).encode() for k in baris[0]}

baca_row = sum(len(r) for r in row_store)            # SUM(total) GROUP BY kota harus baca semua baris utuh
baca_kol = len(kolom["kota"]) + len(kolom["total"])  # hanya 2 kolom
print(f"row store dibaca   : {baca_row/1e6:.2f} MB")
print(f"column store dibaca: {baca_kol/1e6:.2f} MB")
print(f"kolom 'kota' terkompres: {len(kolom['kota'])/1e3:.0f} KB -> {len(zlib.compress(kolom['kota']))/1e3:.0f} KB")
''')]),

'NoSQL, CAP & skala': dict(
  ist=[('CAP theorem', 'Saat terjadi network partition, sistem memilih Consistency atau Availability.'),
       ('Eventual consistency', 'Semua replika akhirnya sama, tetapi untuk sesaat bisa berbeda.'),
       ('Key-value, document, wide-column, graph', 'Empat keluarga NoSQL: Redis, MongoDB, Cassandra, Neo4j.'),
       ('Access pattern first', 'Di NoSQL, skema dirancang dari pola query, bukan dari normalisasi.')],
  cx=[P('Simulasi eventual consistency antar dua replika', '''
replika = {"jakarta": {"stok_A": 10}, "singapura": {"stok_A": 10}}
antrean_replikasi = []

def tulis(node, k, v):
    replika[node][k] = v
    antrean_replikasi.append((node, k, v))

def sinkron():
    while antrean_replikasi:
        asal, k, v = antrean_replikasi.pop(0)
        for n in replika:
            replika[n][k] = v

tulis("jakarta", "stok_A", 9)
print("sebelum sinkron:", {n: r["stok_A"] for n, r in replika.items()}, "<- pembaca di Singapura melihat data lama")
sinkron()
print("setelah sinkron:", {n: r["stok_A"] for n, r in replika.items()})
''')]),

'Slowly changing dimension (SCD tipe 2)': dict(
  ist=[('Dimension table', 'Tabel deskriptif (pelanggan, produk) yang dipakai bersama tabel fakta.'),
       ('SCD tipe 1', 'Timpa nilai lama; histori hilang.'),
       ('SCD tipe 2', 'Simpan versi baru sebagai baris baru dengan valid_from, valid_to, is_current.'),
       ('Surrogate key', 'Kunci buatan per versi baris, berbeda dari natural key (id pelanggan).'),
       ('Snapshot (dbt)', 'Fitur dbt yang menjalankan SCD tipe 2 otomatis.')],
  cx=[dict(t='SCD tipe 2 dengan SQL: pelanggan pindah kota', lang='sql', code='''-- 1) tutup versi lama yang berubah
UPDATE dim_pelanggan
SET valid_to = '2026-11-19', is_current = 0
WHERE is_current = 1
  AND pelanggan_id IN (SELECT s.pelanggan_id FROM stg_pelanggan s
                       JOIN dim_pelanggan d ON d.pelanggan_id = s.pelanggan_id AND d.is_current = 1
                       WHERE d.kota <> s.kota);

-- 2) masukkan versi baru (pelanggan baru atau yang berubah)
INSERT INTO dim_pelanggan (pelanggan_id, nama, kota, valid_from, valid_to, is_current)
SELECT s.pelanggan_id, s.nama, s.kota, '2026-11-19', '9999-12-31', 1
FROM stg_pelanggan s
LEFT JOIN dim_pelanggan d ON d.pelanggan_id = s.pelanggan_id AND d.is_current = 1
WHERE d.pelanggan_id IS NULL;

SELECT sk, pelanggan_id, nama, kota, valid_from, valid_to, is_current FROM dim_pelanggan ORDER BY pelanggan_id, sk;''',
           setup='''CREATE TABLE dim_pelanggan (sk INTEGER PRIMARY KEY AUTOINCREMENT, pelanggan_id INT, nama TEXT, kota TEXT, valid_from TEXT, valid_to TEXT, is_current INT);
INSERT INTO dim_pelanggan (pelanggan_id, nama, kota, valid_from, valid_to, is_current) VALUES
 (1, 'Rina', 'Medan', '2025-01-01', '9999-12-31', 1),
 (2, 'Dodi', 'Bandung', '2025-03-10', '9999-12-31', 1);
CREATE TABLE stg_pelanggan (pelanggan_id INT, nama TEXT, kota TEXT);
INSERT INTO stg_pelanggan VALUES (1, 'Rina', 'Jakarta'), (2, 'Dodi', 'Bandung'), (3, 'Sari', 'Makassar');''',
           b='Rina pindah dari Medan ke Jakarta: versi lama ditutup, versi baru dibuka. Laporan penjualan 2025 tetap tercatat untuk Medan.')]),

'Warehouse, lake, lakehouse & mesh': dict(
  ist=[('Data warehouse', 'Penyimpanan terstruktur untuk analitik dengan skema tetap (BigQuery, Snowflake, Redshift).'),
       ('Data lake', 'Penyimpanan file mentah murah di object storage (S3, GCS) dalam format apa pun.'),
       ('Lakehouse', 'Lake + fitur warehouse (transaksi ACID, skema, time travel) lewat format tabel Delta Lake, Apache Iceberg, atau Hudi.'),
       ('Medallion architecture', 'Lapisan bronze (mentah), silver (bersih), gold (siap bisnis).'),
       ('Data mesh', 'Pendekatan organisasi: tiap domain memiliki dan melayani data product-nya sendiri.')],
  cx=[P('Medallion: bronze → silver → gold dengan pandas', '''
import pandas as pd

bronze = pd.DataFrame({   # apa adanya dari sumber, termasuk yang kotor
    "order_id": [101, 102, 102, 103, 104],
    "tgl": ["2026-11-18", "2026-11-18", "2026-11-18", "18/11/2026", "2026-11-19"],
    "kota": ["medan ", "Bandung", "Bandung", "MEDAN", None],
    "total": ["125000", "98000", "98000", "210500", "50000"],
})
silver = (bronze.drop_duplicates("order_id")
          .assign(tgl=lambda d: pd.to_datetime(d.tgl, format="mixed", dayfirst=True),
                  kota=lambda d: d.kota.str.strip().str.title(),
                  total=lambda d: d.total.astype(int))
          .dropna(subset=["kota"]))
gold = silver.groupby([silver.tgl.dt.date, "kota"]).agg(trx=("order_id", "count"), omzet=("total", "sum")).reset_index()
print(f"bronze {len(bronze)} baris -> silver {len(silver)} baris -> gold {len(gold)} baris")
print(gold.to_string(index=False))
''')]),

'Format kolom & partisi: Parquet': dict(
  ist=[('Parquet', 'Format file kolom terkompresi; standar de facto data lake. Menyimpan skema dan statistik min/max per row group.'),
       ('Hive-style partitioning', 'Folder seperti tanggal=2026-11-19/ sehingga engine bisa melewati folder yang tidak relevan.'),
       ('Partition pruning', 'Query dengan WHERE tanggal = ... hanya membaca satu folder.'),
       ('Small files problem', 'Ribuan file kecil memperlambat query; gabungkan (compaction) ke ukuran 128 MB-1 GB.'),
       ('Predicate pushdown', 'Filter diterapkan saat membaca file memakai statistik min/max, bukan setelah semua dimuat.')],
  cx=[P('Partisi gaya Hive dan partition pruning (disimulasikan dengan CSV)', '''
import pandas as pd, pathlib, tempfile

akar = pathlib.Path(tempfile.mkdtemp()) / "penjualan"
df = pd.DataFrame({"tanggal": ["2026-11-17"] * 3 + ["2026-11-18"] * 4 + ["2026-11-19"] * 2,
                   "kota": list("MBSMBSMMB"), "total": [10, 20, 30, 40, 50, 60, 70, 80, 90]})
for tgl, bagian in df.groupby("tanggal"):                 # df.to_parquet(akar, partition_cols=["tanggal"])
    folder = akar / f"tanggal={tgl}"
    folder.mkdir(parents=True)
    bagian.drop(columns="tanggal").to_csv(folder / "part-0000.csv", index=False)

print(sorted(p.relative_to(akar.parent).as_posix() for p in akar.rglob("*.csv")))
target = "2026-11-18"
dibaca = [p for p in akar.glob(f"tanggal={target}/*.csv")]   # pruning: hanya 1 folder
hasil = pd.concat(pd.read_csv(p) for p in dibaca)
print(f"file dibaca: {len(dibaca)} dari {len(list(akar.rglob('*.csv')))} | total {target}: {hasil.total.sum()}")
''')]),

'Batch, streaming & hybrid': dict(
  ist=[('Batch', 'Memproses kumpulan data per periode (per jam/hari). Sederhana dan murah.'),
       ('Streaming', 'Memproses event begitu datang; latensi detik. Dipakai untuk fraud, notifikasi, dashboard live.'),
       ('Micro-batch', 'Batch sangat kecil (misalnya tiap 30 detik), cara kerja Spark Structured Streaming.'),
       ('Lambda vs Kappa architecture', 'Lambda: jalur batch + streaming terpisah; Kappa: satu jalur streaming yang bisa di-replay.'),
       ('Event time vs processing time', 'Waktu kejadian vs waktu diproses; data terlambat (late data) ditangani dengan watermark.')],
  cx=[P('Tumbling window per menit dengan event time dan data terlambat', '''
from collections import defaultdict
event = [  # (event_time detik, nominal) — datang tidak berurutan
    (5, 100), (42, 250), (61, 80), (30, 120), (119, 60), (65, 300), (58, 40), (190, 500), (70, 10),
]
WATERMARK = 60       # data lebih telat 60 detik dari event terbaru dibuang
jendela, maks_waktu, dibuang = defaultdict(int), 0, []
for t, n in event:
    maks_waktu = max(maks_waktu, t)
    if t < maks_waktu - WATERMARK:
        dibuang.append((t, n)); continue
    jendela[t // 60] += n
for w in sorted(jendela):
    print(f"menit {w}: total {jendela[w]}")
print("terlambat & dibuang:", dibuang)
''')]),

'Idempotensi & upsert': dict(
  ist=[('Idempotent pipeline', 'Dijalankan berkali-kali untuk periode yang sama, hasilnya tetap sama. Syarat aman untuk retry dan backfill.'),
       ('Upsert / MERGE', 'Insert jika belum ada, update jika sudah ada, berdasarkan kunci.'),
       ('Delete-insert per partisi', 'Hapus partisi tanggal X lalu isi ulang; pola idempoten paling sederhana.'),
       ('Backfill', 'Menjalankan ulang pipeline untuk periode lampau, misalnya setelah memperbaiki bug.')],
  cx=[P('Pipeline tidak idempoten vs idempoten (dijalankan dua kali)', '''
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE salah (tgl TEXT, cabang TEXT, omzet INT)")
db.execute("CREATE TABLE benar (tgl TEXT, cabang TEXT, omzet INT, PRIMARY KEY (tgl, cabang))")
data = [("2026-11-18", "Medan", 1_250_000), ("2026-11-18", "Bandung", 980_000)]

def muat_salah():
    db.executemany("INSERT INTO salah VALUES (?,?,?)", data)

def muat_benar():
    db.executemany("""INSERT INTO benar VALUES (?,?,?)
                      ON CONFLICT (tgl, cabang) DO UPDATE SET omzet = excluded.omzet""", data)

for _ in range(2):        # retry otomatis Airflow menjalankan task dua kali
    muat_salah(); muat_benar()
print("tidak idempoten:", db.execute("SELECT SUM(omzet) FROM salah").fetchone()[0], "<- dobel!")
print("idempoten (upsert):", db.execute("SELECT SUM(omzet) FROM benar").fetchone()[0])
''')]),

'Orkestrasi dengan Airflow': dict(
  ist=[('DAG', 'Directed Acyclic Graph: kumpulan task dan ketergantungannya.'),
       ('Operator / TaskFlow (@task)', 'Cara mendefinisikan task; TaskFlow API memakai fungsi Python biasa.'),
       ('Logical date (dulu execution_date)', 'Periode data yang diproses run tersebut, bukan waktu run berjalan.'),
       ('Catchup & backfill', 'Menjalankan run untuk tanggal-tanggal yang terlewat.'),
       ('Sensor', 'Task yang menunggu kondisi (file datang, tabel siap).'),
       ('Alternatif', 'Dagster (asset-based), Prefect, dan layanan terkelola seperti Cloud Composer / MWAA.')],
  cx=[S('DAG harian dengan TaskFlow API (Airflow 2.x/3.x)', '''
from datetime import datetime, timedelta
from airflow.decorators import dag, task

@dag(schedule="30 1 * * *", start_date=datetime(2026, 11, 1), catchup=True, max_active_runs=1,
     default_args={"retries": 3, "retry_delay": timedelta(minutes=5)}, tags=["penjualan"])
def penjualan_harian():

    @task
    def ekstrak(ds=None) -> str:
        # ds = logical date (YYYY-MM-DD): selalu proses periode itu, bukan "hari ini"
        return unduh_dari_api(tanggal=ds, tujuan=f"s3://lake/raw/penjualan/tanggal={ds}/")

    @task
    def validasi(path: str) -> str:
        cek_kontrak(path, kontrak="kontrak/penjualan_v2.yaml")    # gagal -> task merah, tidak lanjut
        return path

    @task
    def muat(path: str, ds=None):
        jalankan_sql(f"DELETE FROM silver.penjualan WHERE tanggal = '{ds}'")   # idempoten
        jalankan_sql(f"INSERT INTO silver.penjualan SELECT * FROM read_parquet('{path}*')")

    muat(validasi(ekstrak()))

penjualan_harian()
''', 'python', 'Setiap run memproses tanggal ds sehingga backfill November cukup dengan menyalakan catchup.'),
      P('Urutan eksekusi DAG dengan topological sort (konsep di balik scheduler)', '''
from graphlib import TopologicalSorter
dag = {"ekstrak_order": [], "ekstrak_pelanggan": [], "validasi": ["ekstrak_order", "ekstrak_pelanggan"],
       "muat_silver": ["validasi"], "dbt_gold": ["muat_silver"], "refresh_dashboard": ["dbt_gold"], "kirim_slack": ["dbt_gold"]}
ts = TopologicalSorter(dag); ts.prepare(); gelombang = 1
while ts.is_active():
    siap = sorted(ts.get_ready())
    print(f"gelombang {gelombang}: {siap}  (boleh paralel)")
    ts.done(*siap); gelombang += 1
''')]),

'Reverse ETL': dict(
  ist=[('Reverse ETL', 'Mengirim data hasil olahan warehouse kembali ke alat operasional (CRM, email marketing, iklan).'),
       ('Operational analytics', 'Memakai data analitik langsung di operasi harian, bukan hanya dashboard.'),
       ('Sync mode', 'Cara sinkronisasi: upsert, mirror, append; plus penanganan record terhapus.'),
       ('Alat', 'Hightouch, Census, atau skrip sendiri yang memanggil API tujuan.')],
  cx=[P('Mengirim hanya perubahan (diff) segmen pelanggan ke CRM', '''
tetap = {f"c{i}": "loyal" for i in range(5, 1005)}            # 1.000 kontak tidak berubah
kemarin = {"c1": "loyal", "c2": "berisiko", "c3": "baru", **tetap}
hari_ini = {"c1": "loyal", "c2": "loyal", "c4": "baru", **tetap}

tambah = {k: v for k, v in hari_ini.items() if k not in kemarin}
ubah = {k: v for k, v in hari_ini.items() if k in kemarin and kemarin[k] != v}
hapus = [k for k in kemarin if k not in hari_ini]

for k, v in {**tambah, **ubah}.items():
    print(f"PATCH /crm/contacts/{k}  segment={v}")
for k in hapus:
    print(f"PATCH /crm/contacts/{k}  segment=null")
print(f"{len(tambah) + len(ubah) + len(hapus)} panggilan API, bukan {len(hari_ini) + len(hapus)} jika sinkron penuh")
''')]),

'Kontrak data & validasi skema': dict(
  ist=[('Data contract', 'Kesepakatan tertulis antara produsen dan konsumen data: skema, tipe, aturan, SLA, pemilik.'),
       ('Schema evolution', 'Perubahan skema yang kompatibel (tambah kolom opsional) vs breaking (hapus/ganti tipe).'),
       ('Schema registry', 'Tempat menyimpan versi skema event (Avro/Protobuf) di Kafka.'),
       ('Quarantine / dead-letter', 'Tempat menampung baris yang gagal validasi agar pipeline tetap jalan.')],
  cx=[P('Validasi baris dengan Pydantic dan karantina', '''
from pydantic import BaseModel, Field, ValidationError, field_validator
from datetime import date

class Penjualan(BaseModel):          # kontrak v2
    order_id: int
    tanggal: date
    cabang: str = Field(min_length=2)
    total: int = Field(ge=0)
    metode: str = "TUNAI"            # kolom baru opsional -> perubahan kompatibel

    @field_validator("cabang")
    @classmethod
    def rapikan(cls, v): return v.strip().title()

masuk = [
    {"order_id": 1, "tanggal": "2026-11-18", "cabang": " medan", "total": 125000, "metode": "QRIS"},
    {"order_id": 2, "tanggal": "2026-11-31", "cabang": "Bandung", "total": 98000},
    {"order_id": "x3", "tanggal": "2026-11-18", "cabang": "Surabaya", "total": -5},
]
valid, karantina = [], []
for r in masuk:
    try:
        valid.append(Penjualan(**r))
    except ValidationError as e:
        karantina.append((r.get("order_id"), [f"{x['loc'][0]}: {x['type']}" for x in e.errors()]))
print("valid:", [(v.order_id, v.cabang, v.metode) for v in valid])
for oid, err in karantina:
    print("karantina:", oid, err)
''')]),

'Kafka: topik, partisi & consumer group': dict(
  ist=[('Topic & partition', 'Topik dibagi ke partisi; urutan hanya dijamin di dalam satu partisi.'),
       ('Message key', 'Pesan dengan key sama selalu masuk partisi yang sama (urutan per pelanggan/order terjaga).'),
       ('Consumer group', 'Kelompok consumer yang berbagi partisi; satu partisi dibaca satu consumer dalam grup.'),
       ('Offset & commit', 'Posisi baca consumer; commit setelah proses agar tidak hilang saat crash.'),
       ('Consumer lag', 'Selisih pesan terbaru dan offset consumer; metrik utama kesehatan streaming.')],
  cx=[P('Simulasi partisi berbasis key, consumer group, dan lag', '''
import zlib
from collections import defaultdict
N_PARTISI = 3
log = defaultdict(list)
for i, (order, status) in enumerate([("INV-7", "dibuat"), ("INV-8", "dibuat"), ("INV-7", "dibayar"), ("INV-9", "dibuat"),
                                     ("INV-8", "dibayar"), ("INV-7", "dikirim"), ("INV-9", "dibatalkan")]):
    p = zlib.crc32(order.encode()) % N_PARTISI         # key -> partisi tetap
    log[p].append((order, status))

grup = {"consumer-1": [0, 1], "consumer-2": [2]}       # pembagian partisi dalam satu group
offset = {0: 0, 1: 0, 2: 0}
for c, parts in grup.items():
    for p in parts:
        for order, status in log[p][:2]:              # anggap baru sempat proses 2 pesan
            offset[p] += 1
        print(f"{c} p{p}: {log[p]}")
for p in range(N_PARTISI):
    print(f"lag p{p} = {len(log[p]) - offset[p]}")
''', 'Perhatikan semua status INV-7 berada di partisi yang sama, sehingga urutannya dibuat → dibayar → dikirim tetap terjaga.')]),

'Antrean pesan & komunikasi asinkron': dict(
  ist=[('Message queue', 'Antrean tugas (RabbitMQ, SQS, Pub/Sub): pesan dihapus setelah diproses, berbeda dengan log Kafka yang bisa dibaca ulang.'),
       ('Producer / consumer', 'Pengirim dan penerima pesan yang tidak perlu aktif bersamaan.'),
       ('Dead-letter queue (DLQ)', 'Antrean untuk pesan yang gagal diproses setelah beberapa percobaan.'),
       ('Backpressure', 'Mekanisme memperlambat produsen saat konsumen kewalahan.'),
       ('Idempotent consumer', 'Konsumen yang aman menerima pesan yang sama lebih dari sekali.')],
  cx=[P('Worker dengan retry, DLQ, dan idempotensi', '''
import queue
q, dlq, sudah = queue.Queue(), [], set()
for pesan in [("m1", "kirim_email:rina"), ("m2", "kirim_email:GAGAL"), ("m1", "kirim_email:rina"), ("m3", "kirim_email:dodi")]:
    q.put((pesan, 0))

def proses(isi):
    if "GAGAL" in isi:
        raise RuntimeError("SMTP timeout")

while not q.empty():
    (mid, isi), coba = q.get()
    if mid in sudah:
        print(f"{mid} duplikat, dilewati"); continue
    try:
        proses(isi); sudah.add(mid); print(f"{mid} sukses")
    except RuntimeError as e:
        if coba + 1 >= 3:
            dlq.append((mid, str(e))); print(f"{mid} -> DLQ setelah 3 percobaan")
        else:
            q.put(((mid, isi), coba + 1))
print("DLQ:", dlq)
''')]),

'Apache Spark & PySpark': dict(
  ist=[('Driver & executor', 'Driver merencanakan job; executor di banyak mesin mengerjakan partisi data.'),
       ('Lazy evaluation', 'Transformasi (filter, select) baru dijalankan saat ada action (count, write).'),
       ('Shuffle', 'Pemindahan data antar executor saat groupBy/join; operasi paling mahal.'),
       ('Broadcast join', 'Tabel kecil dikirim ke semua executor untuk menghindari shuffle.'),
       ('Adaptive Query Execution (AQE)', 'Spark 3+ menyesuaikan rencana saat berjalan, termasuk menangani skew.')],
  cx=[S('Job PySpark: omzet harian per kota dengan broadcast join', '''
from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder.appName("omzet_harian")
         .config("spark.sql.adaptive.enabled", "true").getOrCreate())

order = spark.read.parquet("s3://lake/silver/order/")              # miliaran baris, berpartisi tanggal
toko = spark.read.parquet("s3://lake/silver/toko/")                # ribuan baris

hasil = (order
         .where(F.col("tanggal") == "2026-11-18")                   # partition pruning
         .join(F.broadcast(toko), "toko_id")                        # tanpa shuffle tabel besar
         .groupBy("tanggal", "kota")
         .agg(F.count("*").alias("trx"), F.sum("total").alias("omzet")))

hasil.explain()                                                     # periksa: BroadcastHashJoin
(hasil.write.mode("overwrite")
      .option("partitionOverwriteMode", "dynamic")                  # idempoten per partisi
      .partitionBy("tanggal").parquet("s3://lake/gold/omzet_harian/"))
''', 'python'),
      P('Konsep map → shuffle → reduce dengan Python biasa', '''
from collections import defaultdict
partisi = [  # data tersebar di 3 executor
    [("Medan", 100), ("Bandung", 50), ("Medan", 70)],
    [("Bandung", 30), ("Surabaya", 90)],
    [("Medan", 20), ("Surabaya", 10), ("Bandung", 40)],
]
# map-side combine (seperti partial aggregation di Spark)
lokal = [defaultdict(int) for _ in partisi]
for i, p in enumerate(partisi):
    for kota, n in p:
        lokal[i][kota] += n
print("hasil per executor:", [dict(x) for x in lokal])
# shuffle: kirim per kunci ke reducer, lalu reduce
akhir = defaultdict(int)
for x in lokal:
    for kota, n in x.items():
        akhir[kota] += n
print("setelah shuffle & reduce:", dict(sorted(akhir.items())))
''')]),

'Peta layanan cloud untuk data': dict(
  ist=[('Object storage', 'S3 (AWS), GCS (Google), Azure Blob/ADLS; fondasi data lake.'),
       ('Managed warehouse', 'BigQuery, Redshift, Synapse/Fabric, Snowflake, Databricks SQL.'),
       ('Managed streaming', 'Kinesis/MSK, Pub/Sub, Event Hubs, Confluent Cloud.'),
       ('Region & data residency', 'Lokasi data; regulasi tertentu (PP 71/2019, aturan OJK) mewajibkan atau mengatur penyimpanan di Indonesia. Region Jakarta tersedia di AWS, GCP, dan Azure (Indonesia Central).'),
       ('FinOps', 'Praktik mengendalikan biaya cloud: label biaya, partisi, batas query, reserved capacity.')],
  cx=[P('Padanan layanan antar cloud', '''
peta = [
    ("Object storage", "S3", "Cloud Storage", "Blob/ADLS Gen2"),
    ("Warehouse", "Redshift", "BigQuery", "Synapse / Fabric"),
    ("Streaming", "Kinesis / MSK", "Pub/Sub", "Event Hubs"),
    ("Orkestrasi", "MWAA (Airflow)", "Cloud Composer", "Data Factory"),
    ("Spark terkelola", "EMR / Glue", "Dataproc", "Databricks / Synapse Spark"),
    ("Katalog", "Glue Data Catalog", "Dataplex", "Purview"),
]
print(f"{'Kebutuhan':16} | {'AWS':18} | {'Google Cloud':15} | Azure")
for r in peta:
    print(f"{r[0]:16} | {r[1]:18} | {r[2]:15} | {r[3]}")
''')]),

'Docker, Kubernetes & Terraform': dict(
  ist=[('Container image', 'Paket aplikasi beserta dependensinya; berjalan sama di laptop dan server.'),
       ('Kubernetes (K8s)', 'Orkestrator container: menjadwalkan pod, restart otomatis, autoscaling.'),
       ('Infrastructure as Code (IaC)', 'Infrastruktur ditulis sebagai kode (Terraform/OpenTofu) dan direview seperti kode aplikasi.'),
       ('terraform plan / apply', 'plan menunjukkan perubahan; apply menjalankannya. Plan wajib direview sebelum apply.'),
       ('State file', 'Catatan Terraform tentang sumber daya yang dikelola; disimpan remote dengan locking.')],
  cx=[S('Dockerfile job ETL dan Terraform bucket + dataset', '''
# Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY etl/ etl/
USER 1000                                   # jangan jalan sebagai root
ENTRYPOINT ["python", "-m", "etl.muat_penjualan"]

# main.tf
resource "google_storage_bucket" "lake" {
  name                        = "nusantara-lake-prod"
  location                    = "ASIA-SOUTHEAST2"          # Jakarta
  uniform_bucket_level_access = true
  lifecycle_rule {
    condition { age = 90, matches_prefix = ["raw/"] }
    action    { type = "SetStorageClass", storage_class = "COLDLINE" }
  }
}

resource "google_bigquery_dataset" "gold" {
  dataset_id = "gold"
  location   = "asia-southeast2"
  default_partition_expiration_ms = null
  labels = { tim = "data", biaya = "analitik" }
}
''', 'dockerfile')]),

'Tes pipeline & observabilitas data': dict(
  ist=[('Data quality check', 'Aturan: not null, unique, accepted values, rentang, referential integrity.'),
       ('Freshness', 'Seberapa baru data; contoh "tabel order paling lambat 2 jam dari sekarang".'),
       ('Volume anomaly', 'Jumlah baris turun/naik drastis dari biasanya; tanda sumber bermasalah.'),
       ('Data observability', 'Pemantauan freshness, volume, skema, distribusi, dan lineage (Monte Carlo, Elementary, Soda).'),
       ('Unit test transformasi', 'Tes fungsi transformasi dengan data kecil buatan sebelum dipakai di data asli.')],
  cx=[P('Cek kualitas: not null, unique, rentang, freshness, dan volume', '''
import pandas as pd
from datetime import datetime, timedelta

sekarang = datetime(2026, 11, 19, 8, 0)
df = pd.DataFrame({"order_id": [1, 2, 2, 4, 5], "total": [125000, None, 98000, -10, 50000],
                   "dibuat": pd.to_datetime(["2026-11-19 05:10", "2026-11-19 05:40", "2026-11-19 05:40", "2026-11-19 05:55", "2026-11-19 06:01"])})
histori_volume = [1180, 1215, 1190, 1240, 1205]       # baris per hari sebelumnya

cek = {
    "order_id unik": df.order_id.is_unique,
    "total tidak null": df.total.notna().all(),
    "total >= 0": (df.total.dropna() >= 0).all(),
    "freshness <= 2 jam": sekarang - df.dibuat.max() <= timedelta(hours=2),
    "volume wajar (>50% rata-rata)": len(df) > 0.5 * sum(histori_volume) / len(histori_volume),
}
for nama, lolos in cek.items():
    print(f"{'LULUS' if lolos else 'GAGAL'}  {nama}")
print("Pipeline dihentikan dan tim di-alert" if not all(cek.values()) else "Lanjut ke gold")
''')]),

'Keamanan & privasi data': dict(
  ist=[('PII', 'Data pribadi yang mengidentifikasi orang: NIK, nama, nomor HP, email, alamat.'),
       ('Masking & tokenization', 'Menyamarkan (0812****890) atau mengganti dengan token yang bisa dipetakan balik oleh sistem berwenang.'),
       ('Pseudonymization (hashing + salt)', 'Mengganti ID dengan hash agar analisis tetap bisa digabung tanpa melihat identitas.'),
       ('Least privilege & RBAC', 'Akses minimum sesuai peran; analis tidak perlu kolom NIK.'),
       ('UU PDP', 'UU No. 27/2022: dasar pemrosesan, hak subjek data, notifikasi kebocoran 3x24 jam.')],
  cx=[P('Masking dan pseudonymization sebelum data masuk lapisan analitik', '''
import hashlib, hmac, re
SALT = b"rahasia-dari-secret-manager"     # jangan ditulis di kode produksi

def pseudonim(nilai):
    return hmac.new(SALT, nilai.encode(), hashlib.sha256).hexdigest()[:16]

def samarkan_hp(hp):
    return re.sub(r"^(\\+?\\d{4})\\d+(\\d{3})$", r"\\1****\\2", hp)

def samarkan_email(e):
    nama, domain = e.split("@")
    return nama[0] + "***@" + domain

pelanggan = [("3271010101900001", "081234567890", "rina.s@mail.id"), ("1271020202920002", "+6285211112222", "dodi@contoh.co.id")]
for nik, hp, email in pelanggan:
    print(pseudonim(nik), samarkan_hp(hp), samarkan_email(email))
print("NIK sama -> pseudonim sama:", pseudonim(pelanggan[0][0]) == pseudonim("3271010101900001"))
''')]),

'Lineage & katalog data': dict(
  ist=[('Data lineage', 'Peta asal-usul data: tabel mana dibuat dari tabel mana, lewat transformasi apa.'),
       ('Impact analysis', 'Menjawab "kalau kolom ini diubah, dashboard apa yang rusak?" memakai lineage.'),
       ('Data catalog', 'Mesin pencari metadata: deskripsi, pemilik, tag PII, kualitas (DataHub, OpenMetadata, Unity Catalog).'),
       ('OpenLineage', 'Standar terbuka untuk mengirim event lineage dari Airflow, Spark, dbt.')],
  cx=[P('Impact analysis: apa saja yang terdampak bila raw.order berubah?', '''
lineage = {   # tabel -> turunan langsung
    "raw.order": ["silver.order"],
    "raw.pelanggan": ["silver.pelanggan"],
    "silver.order": ["gold.omzet_harian", "gold.repeat_order"],
    "silver.pelanggan": ["gold.repeat_order", "gold.segmen_pelanggan"],
    "gold.omzet_harian": ["dashboard.penjualan", "reverse_etl.crm"],
    "gold.repeat_order": ["dashboard.retensi"],
    "gold.segmen_pelanggan": ["reverse_etl.crm"],
}

def hilir(node, seen=None):
    seen = seen if seen is not None else []
    for anak in lineage.get(node, []):
        if anak not in seen:
            seen.append(anak); hilir(anak, seen)
    return seen

for akar in ("raw.order", "raw.pelanggan"):
    print(f"{akar} -> {hilir(akar)}")
''')]),

'Pipeline penjualan harian Toko Nusantara': dict(
  ist=[('Runbook', 'Dokumen langkah penanganan saat pipeline gagal: siapa dihubungi, cara rerun, cara backfill.'),
       ('Definition of done pipeline', 'Idempoten, ada tes kualitas, alert, dokumentasi, dan pemilik.'),
       ('On-call', 'Jadwal piket menangani insiden data di luar jam kerja.'),
       ('Post-mortem', 'Analisis insiden tanpa menyalahkan individu, berisi akar masalah dan tindakan pencegahan.')],
  cx=[P('Pipeline lengkap kecil: ekstrak → validasi → upsert → laporan', '''
import sqlite3, pandas as pd, io

csv_harian = {"2026-11-18": "order_id,cabang,total\\n1,Medan,125000\\n2,Bandung,98000\\n3,Medan,-1\\n",
              "2026-11-19": "order_id,cabang,total\\n4,Medan,210000\\n5,Surabaya,75000\\n"}
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE fakta (tanggal TEXT, order_id INT, cabang TEXT, total INT, PRIMARY KEY (tanggal, order_id))")

def jalankan(tanggal):
    df = pd.read_csv(io.StringIO(csv_harian[tanggal]))
    buruk = df[df.total < 0]
    df = df[df.total >= 0]
    db.execute("DELETE FROM fakta WHERE tanggal = ?", (tanggal,))            # idempoten per tanggal
    db.executemany("INSERT INTO fakta VALUES (?,?,?,?)", [(tanggal, *r) for r in df.itertuples(index=False)])
    return len(df), len(buruk)

for tgl in ("2026-11-18", "2026-11-19", "2026-11-18"):                       # 18 dijalankan ulang (backfill)
    ok, karantina = jalankan(tgl)
    print(f"run {tgl}: {ok} dimuat, {karantina} dikarantina")
print(pd.read_sql("SELECT tanggal, cabang, COUNT(*) trx, SUM(total) omzet FROM fakta GROUP BY 1, 2 ORDER BY 1, 2", db).to_string(index=False))
''')]),
}
