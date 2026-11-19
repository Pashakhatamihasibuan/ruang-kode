"""Proyek Data Engineer berpenyelesaian: 6 mini (Python, dijalankan saat generate) + 4 besar berskala industri 2026-2027."""
from rb_pj_lib import MINI, BESAR, JALUR_M, q

# ---------------------------------------------------------------- MINI
ETL = '''import csv, io, sqlite3, json

# File harian dari 3 cabang (sebagian kotor). Di dunia nyata: s3://lake/raw/penjualan/tanggal=.../
FILE = {
    "2026-11-18": "order_id,cabang,produk,qty,harga\\n1,MDN,Kopi 200g,2,31500\\n2,BDG,Gula 1kg,1,17250\\n2,BDG,Gula 1kg,1,17250\\n3,SBY,Teh,x,9000\\n4,MDN,Beras 5kg,1,78500\\n",
    "2026-11-19": "order_id,cabang,produk,qty,harga\\n5,MDN,Kopi 200g,1,31500\\n6,SBY,Sabun,3,-1\\n7,BDG,Teh,4,9000\\n",
}

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE fakta_penjualan (tanggal TEXT, order_id INT, cabang TEXT, produk TEXT, qty INT, harga INT,
                              total INT, PRIMARY KEY (tanggal, order_id));
CREATE TABLE karantina (tanggal TEXT, baris INT, alasan TEXT, isi TEXT);
CREATE TABLE log_run (tanggal TEXT, dimuat INT, karantina INT, duplikat INT);
""")

def validasi(r):
    if not r["qty"].isdigit() or int(r["qty"]) <= 0: return "qty bukan angka positif"
    if not r["harga"].lstrip("-").isdigit() or int(r["harga"]) <= 0: return "harga tidak valid"
    if r["cabang"] not in {"MDN", "BDG", "SBY"}: return "cabang tidak dikenal"
    return None

def jalankan(tanggal):
    bersih, buruk, dilihat, dup = [], [], set(), 0
    for i, r in enumerate(csv.DictReader(io.StringIO(FILE[tanggal])), start=2):
        if r["order_id"] in dilihat:
            dup += 1; continue
        dilihat.add(r["order_id"])
        alasan = validasi(r)
        if alasan:
            buruk.append((tanggal, i, alasan, json.dumps(r))); continue
        q_, h = int(r["qty"]), int(r["harga"])
        bersih.append((tanggal, int(r["order_id"]), r["cabang"], r["produk"], q_, h, q_ * h))
    with db:                                                     # satu transaksi: semua atau tidak sama sekali
        db.execute("DELETE FROM fakta_penjualan WHERE tanggal = ?", (tanggal,))
        db.execute("DELETE FROM karantina WHERE tanggal = ?", (tanggal,))
        db.executemany("INSERT INTO fakta_penjualan VALUES (?,?,?,?,?,?,?)", bersih)
        db.executemany("INSERT INTO karantina VALUES (?,?,?,?)", buruk)
        db.execute("INSERT INTO log_run VALUES (?,?,?,?)", (tanggal, len(bersih), len(buruk), dup))

for t in ["2026-11-18", "2026-11-19", "2026-11-18"]:            # tanggal 18 dijalankan ulang (retry/backfill)
    jalankan(t)

print("LOG RUN"); [print(" ", r) for r in db.execute("SELECT * FROM log_run")]
print("KARANTINA"); [print(" ", r[:3]) for r in db.execute("SELECT * FROM karantina ORDER BY tanggal, baris")]
print("OMZET PER HARI & CABANG")
for r in db.execute("SELECT tanggal, cabang, COUNT(*), SUM(total) FROM fakta_penjualan GROUP BY 1, 2 ORDER BY 1, 2"):
    print(f"  {r[0]} {r[1]} {r[2]} order Rp{r[3]:,}".replace(",", "."))
print("total baris fakta:", db.execute("SELECT COUNT(*) FROM fakta_penjualan").fetchone()[0], "(tidak dobel walau run diulang)")
'''

INKREMENTAL = '''import sqlite3

src = sqlite3.connect(":memory:")          # database aplikasi (OLTP)
dwh = sqlite3.connect(":memory:")          # warehouse
src.executescript("""
CREATE TABLE pelanggan (id INT PRIMARY KEY, nama TEXT, kota TEXT, updated_at TEXT);
INSERT INTO pelanggan VALUES (1,'Rina','Medan','2026-11-17 09:00'), (2,'Dodi','Bandung','2026-11-17 10:00');
""")
dwh.executescript("""
CREATE TABLE dim_pelanggan (sk INTEGER PRIMARY KEY AUTOINCREMENT, id INT, nama TEXT, kota TEXT,
                            valid_from TEXT, valid_to TEXT DEFAULT '9999-12-31', is_current INT DEFAULT 1);
CREATE TABLE watermark (tabel TEXT PRIMARY KEY, nilai TEXT);
INSERT INTO watermark VALUES ('pelanggan', '1970-01-01 00:00');
""")

def sinkron():
    wm = dwh.execute("SELECT nilai FROM watermark WHERE tabel='pelanggan'").fetchone()[0]
    berubah = src.execute("SELECT id, nama, kota, updated_at FROM pelanggan WHERE updated_at > ? ORDER BY updated_at", (wm,)).fetchall()
    with dwh:
        for id_, nama, kota, ts in berubah:
            kini = dwh.execute("SELECT nama, kota FROM dim_pelanggan WHERE id=? AND is_current=1", (id_,)).fetchone()
            if kini == (nama, kota):
                continue                                          # tidak ada perubahan atribut
            if kini:
                dwh.execute("UPDATE dim_pelanggan SET valid_to=?, is_current=0 WHERE id=? AND is_current=1", (ts, id_))
            dwh.execute("INSERT INTO dim_pelanggan (id, nama, kota, valid_from) VALUES (?,?,?,?)", (id_, nama, kota, ts))
        if berubah:
            dwh.execute("UPDATE watermark SET nilai=? WHERE tabel='pelanggan'", (berubah[-1][3],))
    return len(berubah)

print("run 1 membaca", sinkron(), "baris")
src.executescript("""
UPDATE pelanggan SET kota='Jakarta', updated_at='2026-11-18 08:00' WHERE id=1;
INSERT INTO pelanggan VALUES (3,'Sari','Makassar','2026-11-18 09:30');
""")
print("run 2 membaca", sinkron(), "baris (hanya yang berubah)")
print("run 3 membaca", sinkron(), "baris")
print("\\nsk | id | nama | kota     | valid_from       | valid_to         | current")
for r in dwh.execute("SELECT * FROM dim_pelanggan ORDER BY id, sk"):
    print(f"{r[0]:>2} | {r[1]:>2} | {r[2]:4} | {r[3]:8} | {r[4]} | {r[5]:16} | {r[6]}")
print("\\nKota Rina pada 2026-11-17 12:00:",
      dwh.execute("SELECT kota FROM dim_pelanggan WHERE id=1 AND '2026-11-17 12:00' >= valid_from AND '2026-11-17 12:00' < valid_to").fetchone()[0])
'''

KUALITAS = '''from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field, ValidationError
import collections, json

class Transaksi(BaseModel):                      # kontrak data v3 (disepakati tim aplikasi & data)
    trx_id: str = Field(pattern=r"^TRX-\\d{6}$")
    merchant_id: int
    nominal: int = Field(gt=0, le=50_000_000)
    metode: str = Field(pattern=r"^(QRIS|VA|EWALLET|KARTU)$")
    waktu: datetime

batch = [
    {"trx_id": "TRX-000101", "merchant_id": 7, "nominal": 125000, "metode": "QRIS", "waktu": "2026-11-19T07:10:00"},
    {"trx_id": "TRX-000102", "merchant_id": 7, "nominal": 0, "metode": "QRIS", "waktu": "2026-11-19T07:11:00"},
    {"trx_id": "TRX-103", "merchant_id": 9, "nominal": 98000, "metode": "VA", "waktu": "2026-11-19T07:12:00"},
    {"trx_id": "TRX-000104", "merchant_id": 9, "nominal": 76000, "metode": "PAYLATER", "waktu": "2026-11-19T07:13:00"},
    {"trx_id": "TRX-000105", "merchant_id": "sembilan", "nominal": 50000, "metode": "VA", "waktu": "2026-11-19T07:14:00"},
] + [{"trx_id": f"TRX-{200+i:06d}", "merchant_id": 3, "nominal": 10000 + i, "metode": "EWALLET", "waktu": "2026-11-19T07:20:00"} for i in range(15)]

lolos, gagal = [], collections.Counter()
for r in batch:
    try:
        lolos.append(Transaksi(**r))
    except ValidationError as e:
        for err in e.errors():
            gagal[f"{err['loc'][0]}:{err['type']}"] += 1

sekarang = datetime(2026, 11, 19, 8, 0)
aturan = {
    "persentase baris valid >= 95%": len(lolos) / len(batch) >= 0.95,
    "freshness: data terbaru <= 1 jam": sekarang - max(t.waktu for t in lolos) <= timedelta(hours=1),
    "trx_id unik": len({t.trx_id for t in lolos}) == len(lolos),
    "volume >= 10 baris": len(lolos) >= 10,
}
laporan = {"tanggal": str(date(2026, 11, 19)), "total": len(batch), "valid": len(lolos),
           "gagal_per_aturan": dict(gagal), "cek": {k: ("LULUS" if v else "GAGAL") for k, v in aturan.items()}}
print(json.dumps(laporan, indent=2, ensure_ascii=False))
kode_keluar = 0 if all(aturan.values()) else 1
print("exit code:", kode_keluar, "-> orkestrator menandai task", "sukses" if kode_keluar == 0 else "GAGAL dan mengirim alert ke #data-alerts")
'''

STREAM = '''from collections import defaultdict, deque

# Event pembayaran dari Kafka (at-least-once: bisa duplikat), urutan waktu tidak selalu rapi
event = [
    ("e1", "M-07", 0, 50_000), ("e2", "M-07", 12, 75_000), ("e3", "M-11", 15, 20_000), ("e2", "M-07", 12, 75_000),
    ("e4", "M-07", 30, 1_200_000), ("e5", "M-07", 41, 1_500_000), ("e6", "M-07", 44, 1_350_000),
    ("e7", "M-11", 50, 25_000), ("e8", "M-07", 58, 1_800_000), ("e9", "M-07", 140, 60_000), ("e10", "M-11", 150, 22_000),
]
JENDELA, BATAS_JUMLAH, BATAS_NOMINAL = 60, 4, 5_000_000      # >4 trx atau >5 juta dalam 60 detik

sudah = set()                                               # di produksi: Redis SET dengan TTL / state store Flink
jendela = defaultdict(deque)
alert = []
for eid, merchant, t, nominal in event:
    if eid in sudah:
        print(f"t={t:>3}s {eid} duplikat diabaikan"); continue
    sudah.add(eid)
    w = jendela[merchant]
    w.append((t, nominal))
    while w and w[0][0] <= t - JENDELA:                      # buang event di luar jendela geser
        w.popleft()
    jumlah, total = len(w), sum(n for _, n in w)
    status = ""
    if jumlah > BATAS_JUMLAH or total > BATAS_NOMINAL:
        status = "  <-- ALERT"
        alert.append((t, merchant, jumlah, total))
    rp = f"{total:>9,}".replace(",", ".")
    print(f"t={t:>3}s {merchant} jendela: {jumlah} trx, Rp{rp}{status}")
print("\\nALERT dikirim ke tim risiko:", [(t, m) for t, m, *_ in alert])
'''

DAG = '''from graphlib import TopologicalSorter
from datetime import date, timedelta

GAGAL_SEKALI = {("ekstrak_order", "2026-11-17")}           # simulasi API sumber timeout sekali
dicoba = set()

def ekstrak_order(ds):
    if (("ekstrak_order", ds) in GAGAL_SEKALI) and ("ekstrak_order", ds) not in dicoba:
        dicoba.add(("ekstrak_order", ds)); raise TimeoutError("API timeout")
    return f"raw/order/{ds}"
def ekstrak_toko(ds): return f"raw/toko/{ds}"
def validasi(ds): return "ok"
def muat_silver(ds): return f"silver.order partisi {ds}"
def bangun_gold(ds): return "gold.omzet_harian"
def notifikasi(ds): return "slack #laporan"

TASK = {"ekstrak_order": ekstrak_order, "ekstrak_toko": ekstrak_toko, "validasi": validasi,
        "muat_silver": muat_silver, "bangun_gold": bangun_gold, "notifikasi": notifikasi}
GRAF = {"validasi": {"ekstrak_order", "ekstrak_toko"}, "muat_silver": {"validasi"},
        "bangun_gold": {"muat_silver"}, "notifikasi": {"bangun_gold"}}

def run_dag(ds, retries=2):
    status = {}
    for nama in TopologicalSorter(GRAF).static_order():
        if any(status.get(h) != "sukses" for h in GRAF.get(nama, ())):
            status[nama] = "upstream_failed"; continue
        for percobaan in range(retries + 1):
            try:
                TASK[nama](ds); status[nama] = "sukses"; break
            except Exception as e:
                jeda = 2 ** percobaan * 30
                print(f"  [{ds}] {nama} gagal ({e}); retry {percobaan + 1} dalam {jeda} detik")
                status[nama] = "gagal"
    return status

# backfill 3 hari (catchup), satu run per logical date
mulai = date(2026, 11, 16)
for i in range(3):
    ds = str(mulai + timedelta(days=i))
    st = run_dag(ds)
    ringkas = "SUKSES" if all(v == "sukses" for v in st.values()) else "GAGAL"
    print(f"run {ds}: {ringkas} | urutan: {' > '.join(st)}")
'''

MART = '''import sqlite3, random
random.seed(11)
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE raw_order (order_id INT, tgl TEXT, pelanggan TEXT, kota TEXT, produk TEXT, kategori TEXT, qty INT, harga INT);
CREATE TABLE dim_tanggal (tanggal_key INT PRIMARY KEY, tanggal TEXT, bulan TEXT, hari TEXT, akhir_pekan INT);
CREATE TABLE dim_produk (produk_key INTEGER PRIMARY KEY, produk TEXT UNIQUE, kategori TEXT);
CREATE TABLE dim_pelanggan (pelanggan_key INTEGER PRIMARY KEY, pelanggan TEXT UNIQUE, kota TEXT);
CREATE TABLE fakta_penjualan (order_id INT, tanggal_key INT, produk_key INT, pelanggan_key INT, qty INT, total INT);
""")
produk = [("Kopi 200g", "Minuman", 31500), ("Teh 25s", "Minuman", 9000), ("Beras 5kg", "Sembako", 78500),
          ("Gula 1kg", "Sembako", 17250), ("Sabun 450ml", "Kebersihan", 23900)]
pelanggan = [(f"P{i:03}", random.choice(["Medan", "Bandung", "Surabaya"])) for i in range(1, 41)]
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
for oid in range(1, 401):
    d = random.randint(1, 30); p = random.choice(produk); c = random.choice(pelanggan)
    db.execute("INSERT INTO raw_order VALUES (?,?,?,?,?,?,?,?)", (oid, f"2026-09-{d:02}", c[0], c[1], p[0], p[1], random.randint(1, 4), p[2]))

# 1 September 2026 = Selasa
db.executemany("INSERT INTO dim_tanggal VALUES (?,?,?,?,?)",
               [(20260900 + d, f"2026-09-{d:02}", "2026-09", hari[(d) % 7], int((d) % 7 >= 5)) for d in range(1, 31)])
db.executescript("""
INSERT INTO dim_produk (produk, kategori) SELECT DISTINCT produk, kategori FROM raw_order;
INSERT INTO dim_pelanggan (pelanggan, kota) SELECT DISTINCT pelanggan, kota FROM raw_order;
INSERT INTO fakta_penjualan
SELECT r.order_id, CAST(REPLACE(r.tgl, '-', '') AS INT), p.produk_key, c.pelanggan_key, r.qty, r.qty * r.harga
FROM raw_order r JOIN dim_produk p USING (produk) JOIN dim_pelanggan c USING (pelanggan);
""")
cek = db.execute("SELECT (SELECT COUNT(*) FROM raw_order), (SELECT COUNT(*) FROM fakta_penjualan), (SELECT SUM(qty*harga) FROM raw_order), (SELECT SUM(total) FROM fakta_penjualan)").fetchone()
rp = lambda n: f"{n:,}".replace(",", ".")
print(f"rekonsiliasi: baris {cek[0]} = {cek[1]}; omzet {rp(cek[2])} = {rp(cek[3])}")

print("\\n1) Omzet per kategori, akhir pekan vs hari kerja (juta)")
for r in db.execute("""SELECT p.kategori, ROUND(SUM(CASE WHEN t.akhir_pekan=1 THEN f.total END)/1e6,2),
                              ROUND(SUM(CASE WHEN t.akhir_pekan=0 THEN f.total END)/1e6,2)
                       FROM fakta_penjualan f JOIN dim_produk p USING (produk_key) JOIN dim_tanggal t USING (tanggal_key)
                       GROUP BY 1 ORDER BY 1"""):
    print("  ", r)
print("2) Top 3 pelanggan per kota (window function)")
for r in db.execute("""SELECT kota, pelanggan, omzet FROM (
                         SELECT c.kota, c.pelanggan, SUM(f.total) omzet,
                                ROW_NUMBER() OVER (PARTITION BY c.kota ORDER BY SUM(f.total) DESC) rk
                         FROM fakta_penjualan f JOIN dim_pelanggan c USING (pelanggan_key) GROUP BY 1, 2)
                       WHERE rk <= 3 ORDER BY kota, omzet DESC"""):
    print(f"   {r[0]:9} {r[1]} Rp{r[2]:,}".replace(",", "."))
'''

DE_MINI = [
MINI(1, 'Pipeline ETL harian yang idempoten dengan karantina',
  'Toko Nusantara mengirim file penjualan harian dari tiga cabang. Isinya sering kotor (qty berisi huruf, harga negatif, baris dobel), dan ketika job dijalankan ulang, laporan omzet ikut dobel.',
  ['Baca file per tanggal dan validasi setiap baris', 'Baris rusak masuk tabel karantina beserta alasan dan isi aslinya', 'Duplikat order_id dalam satu file dibuang', 'Muat ulang per partisi tanggal dalam satu transaksi (idempoten)', 'Tabel log_run untuk audit setiap eksekusi'],
  ['Fungsi <code>validasi()</code> mengembalikan alasan penolakan atau <code>None</code>.', 'Simpan baris rusak sebagai JSON agar bisa diperbaiki dan dimuat ulang.', 'Himpunan <code>dilihat</code> per file mendeteksi order_id yang muncul dua kali.', '<code>with db:</code> membungkus DELETE partisi + INSERT; gagal di tengah berarti tidak ada yang berubah.', 'Catat jumlah dimuat, dikarantina, dan duplikat per run.'],
  ETL, 'python', run=True,
  kunci='ganti sumber menjadi folder berpartisi <code>tanggal=YYYY-MM-DD</code>, tulis keluaran Parquet, dan jadwalkan dengan Airflow.',
  cek=q('Kenapa partisi tanggal dihapus dulu lalu diisi ulang dalam satu transaksi?', ['Agar run ulang untuk tanggal yang sama menghasilkan data yang sama tanpa dobel, dan tidak ada keadaan setengah jadi', 'Agar database lebih kecil', 'Karena SQLite tidak mendukung UPDATE'], 0, 'Idempotensi per partisi.')),

MINI(2, 'Incremental load dengan watermark dan SCD tipe 2',
  'Menyalin seluruh tabel pelanggan (8 juta baris) dari database aplikasi setiap jam membebani server produksi. Tim analitik juga butuh histori: kota pelanggan saat transaksi terjadi, bukan kota hari ini.',
  ['Hanya baca baris yang berubah sejak run terakhir (kolom updated_at)', 'Watermark tersimpan di warehouse dan maju setelah run sukses', 'Dimensi pelanggan SCD tipe 2: valid_from, valid_to, is_current', 'Run tanpa perubahan tidak menulis apa pun', 'Query point-in-time: atribut pelanggan pada waktu tertentu'],
  ['<code>SELECT ... WHERE updated_at &gt; :watermark ORDER BY updated_at</code>.', 'Simpan watermark = updated_at terbesar yang berhasil diproses, di transaksi yang sama.', 'Jika atribut berubah: tutup versi lama (valid_to, is_current=0) lalu sisipkan versi baru.', 'Bandingkan atribut versi aktif dengan baris sumber sebelum menulis.', '<code>WHERE waktu &gt;= valid_from AND waktu &lt; valid_to</code>.'],
  INKREMENTAL, 'python', run=True,
  kunci='tangani penghapusan (soft delete) dan ganti metode watermark dengan CDC berbasis log (Debezium) untuk menangkap perubahan yang tidak memperbarui updated_at.',
  cek=q('Kelemahan utama incremental load berbasis kolom updated_at?', ['Baris yang dihapus atau diubah tanpa memperbarui updated_at tidak terdeteksi', 'Terlalu cepat', 'Tidak bisa dipakai di SQL'], 0, 'Karena itu CDC berbasis log lebih andal.')),

MINI(3, 'Penjaga kualitas data dengan kontrak dan laporan',
  'Perusahaan payment gateway sering menerima data transaksi rusak dari tim aplikasi (nominal 0, metode pembayaran baru tanpa pemberitahuan). Dashboard keuangan sudah terlanjur salah sebelum ada yang sadar.',
  ['Kontrak data ditulis sebagai model Pydantic (pola ID, rentang nominal, nilai metode yang diizinkan)', 'Hitung pelanggaran per aturan, bukan berhenti di error pertama', 'Cek tingkat batch: persentase valid, freshness, keunikan, volume', 'Laporan JSON yang bisa dikirim ke Slack atau disimpan', 'Exit code 1 saat gagal agar orkestrator menghentikan pipeline'],
  ['<code>Field(pattern=..., gt=0, le=...)</code> menerjemahkan kesepakatan menjadi kode.', '<code>ValidationError.errors()</code> memberi lokasi dan jenis setiap pelanggaran.', 'Ambang dibuat eksplisit, misalnya ≥ 95% baris valid.', '<code>json.dumps(laporan, indent=2)</code>.', '<code>sys.exit(kode_keluar)</code> di skrip asli.'],
  KUALITAS, 'python', run=True,
  kunci='pindahkan aturan ke dbt tests atau Great Expectations/Soda, simpan histori hasil cek, dan tampilkan tren kualitas di dashboard.',
  cek=q('Kenapa pipeline harus berhenti (exit code ≠ 0) saat cek kualitas gagal?', ['Agar data rusak tidak menyebar ke tabel hilir dan dashboard sebelum diperiksa', 'Agar server istirahat', 'Karena Pydantic mewajibkannya'], 0, 'Fail fast di batas pipeline.')),

MINI(4, 'Deteksi lonjakan transaksi real-time dengan sliding window',
  'Tim risiko payment gateway ingin diberi tahu dalam hitungan detik saat sebuah merchant tiba-tiba menerima banyak transaksi bernilai besar (indikasi kartu curian atau pencucian uang). Event datang dari Kafka dan bisa terkirim dua kali.',
  ['Proses event satu per satu, bukan per batch harian', 'Deduplikasi event_id (at-least-once delivery)', 'Sliding window 60 detik per merchant', 'Alert saat lebih dari 4 transaksi atau total lebih dari Rp5 juta dalam jendela', 'Jendela otomatis membuang event lama'],
  ['Loop atas aliran event; state disimpan per merchant.', 'Himpunan <code>sudah</code>; di produksi Redis SET ber-TTL atau state store Flink.', '<code>deque</code> per merchant; buang dari kiri selama event lebih tua dari t − 60.', 'Hitung jumlah dan total jendela setiap event masuk.', 'Kirim alert ke topik <code>risk.alerts</code> dan kanal tim risiko.'],
  STREAM, 'python', run=True,
  kunci='implementasikan ulang dengan Kafka + Flink SQL (HOP window) atau Spark Structured Streaming, termasuk watermark untuk event terlambat.',
  cek=q('Kenapa deduplikasi event_id diperlukan di konsumen streaming?', ['Sistem at-least-once bisa mengirim ulang pesan; tanpa dedup transaksi terhitung dua kali dan memicu alert palsu', 'Agar Kafka lebih cepat', 'Karena event_id selalu kosong'], 0, 'Idempotent consumer.')),

MINI(5, 'Orkestrator mini: DAG, retry, dan backfill',
  'Sebelum memakai Airflow, tim ingin memahami cara kerja orkestrator: urutan task dari dependensi, retry saat API sumber timeout, task hilir tidak jalan bila hulu gagal, dan menjalankan ulang beberapa hari yang terlewat.',
  ['Definisi DAG sebagai graf dependensi', 'Urutan eksekusi topologis', 'Retry dengan exponential backoff', 'Status upstream_failed untuk task hilir', 'Backfill beberapa logical date, satu run per tanggal'],
  ['<code>graphlib.TopologicalSorter</code> menghasilkan urutan yang menghormati dependensi.', 'Iterasi <code>static_order()</code>; cek semua hulu sukses sebelum menjalankan task.', 'Jeda 30, 60, 120 detik (<code>2 ** percobaan * 30</code>).', 'Tandai task hilir tanpa menjalankannya agar mudah dilacak.', 'Setiap run menerima <code>ds</code> sehingga hasilnya hanya bergantung pada tanggal itu.'],
  DAG, 'python', run=True,
  kunci='tulis ulang sebagai DAG Airflow dengan TaskFlow API, tambahkan sensor file, SLA, dan notifikasi kegagalan ke Slack.',
  cek=q('Apa arti logical date (ds) pada run backfill 2026-11-16?', ['Run itu memproses data periode 16 November, walaupun dijalankan hari ini', 'Run itu dijalankan tepat pada 16 November', 'Tanggal pembuatan DAG'], 0, 'Periode data, bukan waktu eksekusi.')),

MINI(6, 'Star schema dan data mart penjualan',
  'Analis menulis query panjang langsung ke tabel order mentah dan hasilnya berbeda-beda antar orang. Manajer ingin satu data mart dengan definisi yang sama untuk semua laporan.',
  ['Dimensi tanggal (hari, akhir pekan), produk, dan pelanggan dengan surrogate key', 'Tabel fakta berisi kunci dimensi dan ukuran (qty, total)', 'Rekonsiliasi: jumlah baris dan omzet fakta sama dengan sumber', 'Query bisnis: kategori akhir pekan vs hari kerja', 'Top 3 pelanggan per kota dengan window function'],
  ['<code>dim_tanggal</code> dibuat sekali per hari kalender, kunci YYYYMMDD.', '<code>INSERT ... SELECT</code> dengan JOIN ke dimensi untuk mendapat surrogate key.', 'Bandingkan COUNT dan SUM sumber vs fakta sebelum mart dipublikasikan.', '<code>SUM(CASE WHEN akhir_pekan = 1 ...)</code>.', '<code>ROW_NUMBER() OVER (PARTITION BY kota ORDER BY omzet DESC)</code>.'],
  MART, 'python', run=True,
  kunci='tulis ulang sebagai proyek dbt (staging → intermediate → marts) dengan tes unique/not_null/relationships dan dokumentasi otomatis.',
  cek=q('Kenapa perlu rekonsiliasi jumlah baris dan omzet antara sumber dan tabel fakta?', ['Untuk membuktikan tidak ada baris hilang atau berlipat akibat JOIN sebelum mart dipakai laporan', 'Agar query lebih cepat', 'Karena SQLite memintanya'], 0, 'Kepercayaan pada angka.')),
]

# ---------------------------------------------------------------- BESAR
LAKEHOUSE = r'''# ingest/sumber_order.py  (dlt: ekstrak inkremental dari API marketplace ke lake)
import dlt
from dlt.sources.helpers import requests

@dlt.resource(name="order", write_disposition="merge", primary_key="order_id")
def order(updated_at=dlt.sources.incremental("updated_at", initial_value="2026-01-01T00:00:00Z")):
    url = "https://api.toko-contoh.id/v2/orders"
    params = {"updated_since": updated_at.last_value, "limit": 500}
    while url:
        r = requests.get(url, params=params, timeout=30); r.raise_for_status()
        body = r.json(); yield body["data"]
        url, params = body.get("next"), None

pipeline = dlt.pipeline("marketplace", destination="filesystem", dataset_name="bronze")   # -> Iceberg/Parquet di GCS/S3

-- models/staging/stg_order.sql  (dbt)
{{ config(materialized='incremental', unique_key='order_id', incremental_strategy='merge',
          partition_by={'field': 'tanggal', 'data_type': 'date'}) }}
select
    cast(order_id as int64)                         as order_id,
    date(timestamp(created_at), 'Asia/Jakarta')     as tanggal,
    lower(trim(status))                             as status,
    cast(total as numeric)                          as total,
    toko_id, pelanggan_id, updated_at
from {{ source('bronze', 'order') }}
{% if is_incremental() %}
where updated_at > (select max(updated_at) from {{ this }})
{% endif %}

# models/staging/_stg.yml
models:
  - name: stg_order
    config: { contract: { enforced: true } }
    columns:
      - name: order_id
        data_type: int64
        data_tests: [unique, not_null]
      - name: tanggal
        data_type: date
      - name: status
        data_type: string
        data_tests:
          - accepted_values: { values: [dibuat, dibayar, dikirim, selesai, batal] }
      - name: toko_id
        data_type: int64
        data_tests:
          - relationships: { to: ref('dim_toko'), field: toko_id }

# dags/marketplace_harian.py  (Airflow + Cosmos menjalankan dbt per model sebagai task)
with DAG("marketplace_harian", schedule="0 2 * * *", start_date=datetime(2026, 1, 1), catchup=False) as dag:
    ingest = PythonOperator(task_id="dlt_ingest", python_callable=lambda: pipeline.run(order()))
    dbt = DbtTaskGroup(group_id="dbt", project_config=ProjectConfig("/opt/dbt/marketplace"),
                       render_config=RenderConfig(test_behavior=TestBehavior.AFTER_EACH))
    ingest >> dbt'''

STREAMING = r'''-- 1) CDC: Debezium membaca WAL PostgreSQL -> topik Kafka pg.public.transaksi (Avro + Schema Registry)
-- connector.json (potongan)
-- { "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
--   "plugin.name": "pgoutput", "table.include.list": "public.transaksi",
--   "topic.prefix": "pg", "snapshot.mode": "initial" }

-- 2) Flink SQL: fitur real-time per kartu dalam jendela geser 10 menit
CREATE TABLE transaksi (
  trx_id STRING, kartu_hash STRING, merchant_id BIGINT, nominal DECIMAL(14,0),
  kota STRING, waktu TIMESTAMP(3),
  WATERMARK FOR waktu AS waktu - INTERVAL '30' SECOND
) WITH ('connector' = 'kafka', 'topic' = 'pg.public.transaksi', 'format' = 'debezium-avro-confluent', ...);

CREATE TABLE fitur_kartu WITH ('connector' = 'upsert-kafka', 'topic' = 'fitur.kartu', ...) AS
SELECT kartu_hash,
       HOP_END(waktu, INTERVAL '1' MINUTE, INTERVAL '10' MINUTE) AS sampai,
       COUNT(*)                     AS trx_10m,
       SUM(nominal)                 AS nominal_10m,
       COUNT(DISTINCT kota)         AS kota_10m,
       COUNT(DISTINCT merchant_id)  AS merchant_10m
FROM transaksi
GROUP BY kartu_hash, HOP(waktu, INTERVAL '1' MINUTE, INTERVAL '10' MINUTE);

-- 3) Aturan + skor model: kota berbeda >= 3 dalam 10 menit = impossible travel
INSERT INTO alert_risiko
SELECT kartu_hash, sampai, 'IMPOSSIBLE_TRAVEL' AS jenis, kota_10m
FROM fitur_kartu WHERE kota_10m >= 3;

-- 4) ClickHouse untuk dashboard investigasi (latensi query < 1 detik)
CREATE TABLE risiko.transaksi
( trx_id String, kartu_hash String, merchant_id UInt64, nominal Decimal(14,0), kota LowCardinality(String), waktu DateTime64(3, 'Asia/Jakarta') )
ENGINE = ReplacingMergeTree ORDER BY (kartu_hash, waktu, trx_id) PARTITION BY toYYYYMMDD(waktu) TTL toDate(waktu) + INTERVAL 400 DAY;'''

PLATFORM = r'''# infra/terraform/main.tf  — semua lingkungan dibuat dari modul yang sama
module "lake" {
  source        = "./modules/lake"
  env           = var.env                        # dev | staging | prod
  region        = "asia-southeast2"              # Jakarta: data residency
  retensi_raw   = 90
  kms_key       = google_kms_crypto_key.data.id  # enkripsi dengan kunci sendiri (CMEK)
}

module "airflow" {
  source         = "./modules/airflow-gke"       # Helm chart resmi di GKE Autopilot
  env            = var.env
  git_sync_repo  = "git@github.com:org/data-dags.git"
  worker_min     = var.env == "prod" ? 2 : 0
  worker_max     = 12
}

resource "google_bigquery_dataset_iam_member" "analis_gold" {
  dataset_id = "gold"
  role       = "roles/bigquery.dataViewer"
  member     = "group:analis@toko-contoh.id"     # least privilege: analis hanya baca gold
}

# .github/workflows/data-ci.yml  — setiap pull request
jobs:
  terraform:
    steps:
      - run: terraform fmt -check && terraform validate
      - run: terraform plan -out=plan.tfplan        # plan ditempel ke komentar PR untuk direview
  dbt-slim-ci:
    steps:
      - run: dbt deps
      - run: dbt build --select state:modified+ --defer --state ./prod-manifest --target ci   # hanya model yang berubah + hilirnya
      - run: python scripts/cek_kontrak.py --berubah   # tolak PR yang menghapus kolom tanpa versi kontrak baru
  biaya:
    steps:
      - run: python scripts/perkiraan_biaya.py --maks-gb-per-query 200   # FinOps: dry-run BigQuery, gagal jika melampaui batas

# runbook/insiden.md (potongan)
# 1. Cek dashboard observabilitas (freshness, volume, lag Kafka)
# 2. Tentukan blast radius dengan lineage (OpenLineage/Marquez)
# 3. Pause DAG hilir, perbaiki, backfill: airflow dags backfill -s 2026-11-16 -e 2026-11-18 marketplace_harian
# 4. Post-mortem tanpa menyalahkan dalam 3 hari kerja'''

RAG = r'''# pipeline/dokumen_ke_vektor.py  — data pipeline untuk aplikasi GenAI (asisten internal SOP perusahaan)
from dataclasses import dataclass
import hashlib, re

@dataclass
class Potongan:
    doc_id: str; versi: str; urutan: int; teks: str; judul: str; akses: list[str]; hash: str

def bersihkan(teks: str) -> str:
    teks = re.sub(r"\b\d{16}\b", "[NIK]", teks)                          # PII tidak boleh masuk indeks
    teks = re.sub(r"(\+62|0)8\d{8,11}", "[HP]", teks)
    return re.sub(r"\s+", " ", teks).strip()

def potong(doc, ukuran=800, tumpang=120):
    """Potong per judul bagian dulu, baru per jumlah karakter, dengan tumpang tindih agar konteks tidak terputus."""
    for b, bagian in enumerate(doc.bagian):
        teks = bersihkan(bagian.isi)
        for i in range(0, max(len(teks) - tumpang, 1), ukuran - tumpang):
            isi = teks[i:i + ukuran]
            yield Potongan(doc.id, doc.versi, b * 1000 + i // (ukuran - tumpang), isi, bagian.judul,
                           doc.akses, hashlib.sha256(isi.encode()).hexdigest())

def sinkron_indeks(dokumen_berubah, db, embed):
    """Inkremental: hanya potongan yang hash-nya berubah yang di-embed ulang (hemat biaya API)."""
    for doc in dokumen_berubah:
        lama = {r.hash for r in db.potongan_milik(doc.id)}
        baru = list(potong(doc))
        perlu = [p for p in baru if p.hash not in lama]
        vektor = embed([p.teks for p in perlu]) if perlu else []
        with db.transaksi():
            db.hapus_potongan_selain(doc.id, {p.hash for p in baru})       # versi lama tidak boleh dijawab lagi
            db.simpan(perlu, vektor)

-- pgvector: pencarian hybrid dengan filter hak akses (row-level)
SELECT id, judul, teks, 1 - (embedding <=> :q) AS skor
FROM potongan
WHERE akses && :grup_pengguna                       -- pengguna hanya melihat dokumen yang boleh dibaca
  AND berlaku = true
ORDER BY embedding <=> :q
LIMIT 8;

# eval/harian.py — kualitas data untuk AI
# - freshness: dokumen SOP yang diubah di Drive/Confluence harus masuk indeks <= 30 menit
# - coverage: % dokumen aktif yang punya potongan di indeks (target 100%)
# - golden set 120 pertanyaan: recall@8 sumber yang benar >= 0,9; jawaban mengutip sumber
# - audit PII: 0 kecocokan pola NIK/HP di tabel potongan'''

DE_BESAR = [
BESAR(1, 'Lakehouse e-commerce: ingest inkremental, dbt, dan orkestrasi',
  'Brand ritel omnichannel punya data di marketplace, toko online, POS 60 gerai, dan iklan digital. Setiap tim punya angka omzet berbeda. Mereka butuh satu platform data dengan definisi metrik tunggal yang diperbarui setiap pagi.',
  ['Ingest inkremental dari API dan database ke lapisan bronze (Parquet/Iceberg di object storage)', 'Transformasi dbt berlapis: staging → intermediate → marts, dengan model contract', 'Tes data otomatis (unique, not_null, relationships, accepted_values, freshness)', 'Orkestrasi Airflow dengan dbt per model sebagai task, retry, dan SLA jam 07.00', 'Dokumentasi dan lineage otomatis; semantic layer untuk metrik omzet, AOV, repeat rate'],
  'dlt / Airbyte, Google Cloud Storage atau S3, Apache Iceberg, BigQuery / Snowflake / Trino, dbt Core, Airflow + Astronomer Cosmos, OpenLineage, Looker / Metabase',
  [('Lapisan', 'bronze (mentah, append) → silver (bersih, dedup, tipe benar) → gold (fakta & dimensi, metrik)'), ('Ingestion', 'merge berdasarkan primary key + cursor updated_at; state disimpan dlt'),
   ('Transformasi', 'dbt incremental merge, partisi per tanggal WIB, cluster per toko'), ('Kualitas', 'dbt tests + source freshness; gagal → DAG berhenti dan alert Slack'),
   ('Tata kelola', 'pemilik per model, tag PII, akses per dataset, lineage di katalog'), ('Biaya', 'partisi + clustering, batas byte per query, model gold materialized table, staging view')],
  ['Inventarisasi sumber dan definisikan metrik bersama bisnis (tulis di dokumen definisi metrik).', 'Bangun ingest inkremental satu sumber dulu sampai stabil, lalu tambah sumber lain.', 'Tulis model dbt staging dengan contract dan tes, kemudian marts fakta/dimensi.', 'Hubungkan Airflow + Cosmos; tambah SLA, retry, dan alert.', 'Publikasikan dokumentasi, lineage, dan semantic layer; matikan spreadsheet lama.'],
  LAKEHOUSE, 'python', standar='satu definisi metrik, pipeline idempoten dan inkremental, tes data di setiap model, SLA terpantau, biaya per query terkendali, dokumentasi dan lineage tersedia',
  cek=q('Apa manfaat model contract (contract: enforced) di dbt?', ['Model gagal dibangun jika nama atau tipe kolom berubah dari yang disepakati, sehingga konsumen hilir tidak rusak diam-diam', 'Mempercepat query', 'Mengenkripsi kolom'], 0, 'Kontrak data di lapisan transformasi.')),

BESAR(2, 'Pipeline streaming deteksi fraud dengan CDC, Kafka, dan Flink',
  'Payment gateway memproses 3 juta transaksi per hari. Fraud dideteksi keesokan harinya dari laporan batch, ketika uang sudah hilang. Targetnya: transaksi mencurigakan ditandai kurang dari 5 detik setelah terjadi.',
  ['CDC dari PostgreSQL ke Kafka dengan Debezium (tanpa membebani aplikasi)', 'Schema Registry dan format Avro; perubahan skema dicek kompatibilitasnya', 'Fitur real-time per kartu dan merchant dengan jendela geser (Flink SQL), watermark untuk event terlambat', 'Aturan + skor model, alert ke tim risiko dalam < 5 detik', 'Penyimpanan analitik real-time (ClickHouse) untuk investigasi dan dashboard'],
  'PostgreSQL, Debezium, Apache Kafka (Confluent/Redpanda/MSK), Schema Registry, Apache Flink (SQL), ClickHouse, Grafana, Kubernetes',
  [('Alur', 'Postgres WAL → Debezium → Kafka → Flink (fitur + aturan) → topik alert + ClickHouse'), ('Jaminan', 'exactly-once di Flink (checkpoint + transactional sink), konsumen alert idempoten'),
   ('Skema', 'Avro + Schema Registry mode BACKWARD; perubahan breaking ditolak di CI'), ('Skala', 'partisi topik berdasarkan kartu_hash; paralelisme Flink = jumlah partisi'),
   ('Observabilitas', 'consumer lag, checkpoint duration, latensi end-to-end p99, jumlah alert per jam'), ('Privasi', 'nomor kartu di-hash sejak sumber; data mentah kartu tidak pernah masuk Kafka')],
  ['Aktifkan logical replication di PostgreSQL dan jalankan Debezium untuk satu tabel.', 'Daftarkan skema Avro dan uji perubahan kolom kompatibel vs tidak.', 'Tulis Flink SQL untuk fitur jendela 10 menit; uji dengan data replay dari Kafka.', 'Tambahkan aturan dan integrasi skor model; kirim alert ke topik dan Slack/PagerDuty.', 'Muat ke ClickHouse, bangun dashboard investigasi, ukur latensi end-to-end.'],
  STREAMING, 'sql', standar='latensi deteksi p99 < 5 detik, tidak ada transaksi hilang atau terhitung ganda, skema terkelola, lag terpantau, data kartu tidak pernah tersimpan mentah',
  cek=q('Kenapa memakai CDC (Debezium) dibanding query SELECT berkala ke tabel transaksi?', ['CDC membaca log database sehingga menangkap setiap insert/update/delete dengan latensi rendah tanpa membebani query produksi', 'CDC lebih mudah ditulis dengan Excel', 'SELECT berkala tidak bisa membaca tabel'], 0, 'Log-based change data capture.')),

BESAR(3, 'Platform data dengan Infrastructure as Code dan CI/CD',
  'Startup fintech berkembang dari 3 menjadi 15 orang tim data. Infrastruktur dibuat manual lewat konsol cloud, tidak ada lingkungan staging, perubahan dbt langsung ke produksi, dan tagihan cloud naik 4x dalam 6 bulan.',
  ['Seluruh infrastruktur (bucket, warehouse, IAM, Airflow di Kubernetes) ditulis dengan Terraform', 'Tiga lingkungan dev/staging/prod dari modul yang sama', 'CI untuk setiap PR: terraform plan, dbt slim CI, cek kontrak data, perkiraan biaya', 'Akses least privilege per peran dan enkripsi dengan kunci sendiri', 'Runbook insiden, on-call, dan dashboard biaya (FinOps)'],
  'Terraform/OpenTofu, Google Cloud (GKE Autopilot, BigQuery, GCS, KMS) atau padanan AWS, Helm, Airflow, dbt, GitHub Actions, OpenLineage/Marquez, Grafana',
  [('Repositori', 'infra/ (Terraform), dags/ (Airflow), dbt/ (model), contracts/ (YAML kontrak)'), ('Lingkungan', 'workspace/variabel per env; data produksi tidak bisa diakses dari dev'),
   ('CI/CD', 'PR → plan + tes; merge ke main → apply ke staging; tag rilis → apply ke prod'), ('Keamanan', 'IAM per grup, service account per workload, CMEK, audit log, secret di Secret Manager'),
   ('Keandalan', 'SLA per data product, alert freshness, runbook, on-call bergilir'), ('Biaya', 'label biaya per tim, batas byte per query, reservasi slot, laporan biaya mingguan')],
  ['Impor sumber daya yang sudah ada ke Terraform (<code>terraform import</code>) sebelum mengubah apa pun.', 'Buat modul dan tiga lingkungan; pindahkan Airflow ke GKE dengan Helm.', 'Siapkan GitHub Actions: plan di PR, apply bertahap setelah review.', 'Terapkan dbt slim CI dan cek kontrak; larang perubahan langsung di prod.', 'Tulis runbook, aktifkan on-call, dan pantau biaya per tim selama sebulan.'],
  PLATFORM, 'hcl', standar='tidak ada perubahan manual di konsol, setiap perubahan lewat PR dan review, lingkungan terpisah, akses minimum, biaya dipantau per tim, insiden punya runbook',
  cek=q('Kenapa hasil terraform plan ditempel di pull request sebelum apply?', ['Agar reviewer melihat persis sumber daya yang akan dibuat, diubah, atau dihapus sebelum terjadi di cloud', 'Agar build lebih cepat', 'Karena apply tidak bisa dijalankan tanpa komentar'], 0, 'Review perubahan infrastruktur.')),

BESAR(4, 'Pipeline data untuk aplikasi AI: dari dokumen ke indeks vektor',
  'Perusahaan logistik nasional membangun asisten AI internal yang menjawab pertanyaan karyawan dari 4.000 dokumen SOP, kebijakan HR, dan tarif. Masalah terbesarnya bukan model, tetapi data: dokumen usang masih dijawab, data pribadi bocor ke indeks, dan karyawan cabang bisa membaca dokumen direksi.',
  ['Ingest inkremental dokumen dari Google Drive/Confluence/SharePoint beserta versi dan hak aksesnya', 'Pembersihan dan masking PII sebelum chunking', 'Chunking berbasis struktur (judul bagian) dengan tumpang tindih; embed ulang hanya potongan yang berubah', 'Indeks vektor dengan filter hak akses per pengguna (pgvector atau vector DB)', 'Monitoring kualitas data AI: freshness, coverage, recall@k pada golden set, audit PII'],
  'Python, Airflow/Dagster, Unstructured/Docling untuk parsing, PostgreSQL + pgvector (atau Qdrant/Weaviate), model embedding multibahasa, Claude/LLM API, OpenLineage, Grafana',
  [('Ingest', 'webhook/perubahan dokumen → antrean → parsing (PDF, DOCX, tabel) → teks terstruktur'), ('Transformasi', 'masking PII, chunking per bagian 800 karakter + tumpang 120, metadata (versi, akses, tanggal berlaku)'),
   ('Indeks', 'hash per potongan; hanya potongan baru yang di-embed; potongan versi lama dihapus'), ('Keamanan', 'filter akses di query (row-level), audit siapa bertanya apa, retensi log'),
   ('Evaluasi', 'golden set 120 pertanyaan, recall@8 ≥ 0,9, jawaban wajib mengutip sumber'), ('Biaya', 'embedding inkremental, cache, batas token per pengguna')],
  ['Petakan sumber dokumen, pemilik, dan model hak aksesnya.', 'Bangun parser + masking PII dan uji pada 50 dokumen beragam (PDF scan, tabel tarif).', 'Implementasikan chunking dan sinkronisasi inkremental berbasis hash.', 'Buat indeks dengan filter akses dan uji dengan akun cabang vs direksi.', 'Siapkan evaluasi harian dan dashboard kualitas; libatkan pemilik SOP untuk memperbaiki dokumen yang sering salah dijawab.'],
  RAG, 'python', standar='dokumen usang tidak pernah dijawab, nol PII di indeks, hak akses dihormati di setiap query, indeks segar ≤ 30 menit, kualitas pencarian diukur dengan golden set',
  cek=q('Kenapa potongan dari versi dokumen lama harus dihapus dari indeks saat dokumen diperbarui?', ['Agar asisten tidak menjawab dengan aturan yang sudah tidak berlaku', 'Agar indeks lebih berwarna', 'Karena pgvector tidak bisa menyimpan dua versi'], 0, 'Freshness adalah kualitas data AI.')),
]

PJ_DE = JALUR_M('Data Engineer', 'Menengah',
  'Enam proyek mini Python yang dijalankan (ETL idempoten, incremental load + SCD2, penjaga kualitas data, deteksi lonjakan streaming, orkestrator mini, star schema) dan empat proyek besar berskala industri 2026-2027 (lakehouse e-commerce dengan dbt, streaming fraud dengan CDC-Kafka-Flink, platform data dengan Terraform dan CI/CD, pipeline data untuk aplikasi AI), lengkap dengan penyelesaiannya.',
  ['Data engineering projects', 'dbt', 'Airflow', 'Kafka & Flink', 'Data for AI'], DE_MINI, DE_BESAR)
