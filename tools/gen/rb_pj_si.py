"""Proyek Analis Sistem Informasi / BI berpenyelesaian: 6 mini (Python, dijalankan saat generate) + 4 besar berskala industri 2026-2027."""
from rb_pj_lib import MINI, BESAR, JALUR_M, q

# ---------------------------------------------------------------- MINI
PROSES = '''from collections import defaultdict, Counter
from datetime import datetime

# Event log proses pengajuan klaim asuransi kesehatan (dari tabel audit sistem): kasus, aktivitas, waktu
LOG = """K1,Klaim diajukan,2026-11-03 08:10
K1,Verifikasi dokumen,2026-11-03 13:40
K1,Persetujuan medis,2026-11-05 10:00
K1,Pembayaran,2026-11-06 09:15
K2,Klaim diajukan,2026-11-03 09:00
K2,Verifikasi dokumen,2026-11-04 16:20
K2,Minta dokumen tambahan,2026-11-04 16:30
K2,Verifikasi dokumen,2026-11-07 11:00
K2,Persetujuan medis,2026-11-10 14:00
K2,Pembayaran,2026-11-11 10:00
K3,Klaim diajukan,2026-11-04 10:00
K3,Verifikasi dokumen,2026-11-04 15:00
K3,Persetujuan medis,2026-11-07 09:30
K3,Pembayaran,2026-11-07 15:00
K4,Klaim diajukan,2026-11-05 07:45
K4,Verifikasi dokumen,2026-11-06 08:00
K4,Minta dokumen tambahan,2026-11-06 08:05
K4,Verifikasi dokumen,2026-11-10 09:00
K4,Persetujuan medis,2026-11-13 16:00
K4,Pembayaran,2026-11-14 11:00"""

kasus = defaultdict(list)
for baris in LOG.splitlines():
    k, a, t = baris.split(",")
    kasus[k].append((a, datetime.fromisoformat(t)))

def jam(d): return d.total_seconds() / 3600

print("WAKTU SIKLUS PER KASUS")
for k, ev in kasus.items():
    print(f"  {k}: {jam(ev[-1][1] - ev[0][1]) / 24:4.1f} hari, {len(ev)} langkah")

print("VARIAN PROSES")
for varian, n in Counter(" > ".join(a for a, _ in ev) for ev in kasus.values()).most_common():
    print(f"  {n}x  {varian}")

tunggu = defaultdict(list)
for ev in kasus.values():
    for (a1, t1), (a2, t2) in zip(ev, ev[1:]):
        tunggu[f"{a1} -> {a2}"].append(jam(t2 - t1))
print("RATA-RATA WAKTU TUNGGU ANTAR-LANGKAH (bottleneck di atas)")
for trans, v in sorted(tunggu.items(), key=lambda x: -sum(x[1]) / len(x[1])):
    print(f"  {sum(v) / len(v):6.1f} jam  ({len(v)}x)  {trans}")
ulang = sum(1 for ev in kasus.values() if any(a == "Minta dokumen tambahan" for a, _ in ev))
print(f"Rework: {ulang}/{len(kasus)} klaim harus melengkapi dokumen -> checklist dokumen di formulir awal")
'''

KELAYAKAN = '''# Kelayakan aplikasi pemesanan & stok untuk 25 apotek: NPV, IRR, payback, dan analisis sensitivitas
INVESTASI = 1_350_000_000
BIAYA_OPS = 210_000_000                          # per tahun: cloud, lisensi, tim dukungan
MANFAAT = {"stok kedaluwarsa berkurang": 380_000_000, "lembur admin berkurang": 145_000_000,
           "penjualan hilang karena stok kosong": 320_000_000}
TAHUN, R = 5, 0.11

def arus(skala_manfaat=1.0, skala_biaya=1.0, adopsi=(0.4, 0.8, 1, 1, 1)):
    m = sum(MANFAAT.values()) * skala_manfaat
    return [-INVESTASI * skala_biaya] + [m * a - BIAYA_OPS for a in adopsi]

def npv(cf, r=R): return sum(c / (1 + r) ** t for t, c in enumerate(cf))
def irr(cf):
    lo, hi = -0.9, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv(cf, mid) > 0 else (lo, mid)
    return mid
def payback(cf):
    kum = cf[0]
    for t, c in enumerate(cf[1:], 1):
        if kum + c >= 0: return t - 1 + -kum / c
        kum += c

cf = arus()
rp = lambda x: ("-" if x < 0 else "") + f"Rp{abs(x) / 1e6:,.0f} jt".replace(",", ".")
print("arus kas:", [rp(c) for c in cf])
print(f"NPV {rp(npv(cf))} | IRR {irr(cf):.1%} | payback {payback(cf):.1f} tahun")
print("\\nSENSITIVITAS NPV")
for label, kw in [("manfaat -30%", dict(skala_manfaat=0.7)), ("investasi +25%", dict(skala_biaya=1.25)),
                  ("adopsi lambat", dict(adopsi=(0.2, 0.5, 0.7, 0.9, 1))), ("skenario buruk gabungan", dict(skala_manfaat=0.8, skala_biaya=1.2, adopsi=(0.2, 0.5, 0.7, 0.9, 1)))]:
    v = npv(arus(**kw))
    print(f"  {label:<24} {rp(v):>14}  {'masih layak' if v > 0 else 'TIDAK layak'}")
'''

KOPERASI = '''import sqlite3
# Sistem informasi koperasi simpan pinjam: ERD -> skema -> transaksi -> laporan manajemen
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE anggota (id INTEGER PRIMARY KEY, nama TEXT NOT NULL, unit TEXT NOT NULL, bergabung TEXT NOT NULL);
CREATE TABLE simpanan (id INTEGER PRIMARY KEY, anggota_id INT NOT NULL REFERENCES anggota, jenis TEXT
                       CHECK (jenis IN ('pokok','wajib','sukarela')), tgl TEXT, jumlah INT CHECK (jumlah > 0));
CREATE TABLE pinjaman (id INTEGER PRIMARY KEY, anggota_id INT NOT NULL REFERENCES anggota, tgl TEXT,
                       pokok INT, tenor INT, bunga_bln REAL);
CREATE TABLE angsuran (pinjaman_id INT REFERENCES pinjaman, ke INT, jatuh_tempo TEXT, dibayar TEXT,
                       PRIMARY KEY (pinjaman_id, ke));
INSERT INTO anggota VALUES (1,'Sri','Produksi','2023-02-01'),(2,'Budi','Gudang','2024-07-15'),
                           (3,'Nur','Keuangan','2025-01-10'),(4,'Agus','Produksi','2025-09-01');
INSERT INTO simpanan (anggota_id, jenis, tgl, jumlah) VALUES
 (1,'pokok','2023-02-01',100000),(1,'wajib','2026-10-01',50000),(1,'sukarela','2026-10-05',2000000),
 (2,'pokok','2024-07-15',100000),(2,'wajib','2026-10-01',50000),(3,'pokok','2025-01-10',100000),
 (3,'wajib','2026-10-01',50000),(3,'sukarela','2026-10-20',750000),(4,'pokok','2025-09-01',100000);
INSERT INTO pinjaman VALUES (1,2,'2026-06-01',6000000,12,0.01),(2,4,'2026-08-01',3000000,6,0.012),(3,1,'2026-09-01',10000000,24,0.009);
""")
# jadwal angsuran: bayar tepat waktu kecuali beberapa kasus
import datetime as dt
for pid, tgl, tenor in db.execute("SELECT id, tgl, tenor FROM pinjaman").fetchall():
    d = dt.date.fromisoformat(tgl)
    for k in range(1, tenor + 1):
        jt = dt.date(d.year + (d.month + k - 1) // 12, (d.month + k - 1) % 12 + 1, 10)
        if jt > dt.date(2026, 11, 19): bayar = None
        elif pid == 2 and k >= 2: bayar = None                      # Agus menunggak
        else: bayar = jt.isoformat()
        db.execute("INSERT INTO angsuran VALUES (?,?,?,?)", (pid, k, jt.isoformat(), bayar))

print("LAPORAN SIMPANAN PER ANGGOTA")
for r in db.execute("""SELECT a.nama, SUM(CASE WHEN jenis='pokok' THEN jumlah END), SUM(CASE WHEN jenis='wajib' THEN jumlah END),
                              COALESCE(SUM(CASE WHEN jenis='sukarela' THEN jumlah END),0), SUM(jumlah)
                       FROM simpanan s JOIN anggota a ON a.id = s.anggota_id GROUP BY a.nama ORDER BY 5 DESC"""):
    nama, *angka = r
    rp = [f"{x or 0:,}".replace(",", ".") for x in angka]
    print(f"  {nama:<5} pokok {rp[0]:>7}  wajib {rp[1]:>6}  sukarela {rp[2]:>9}  total {rp[3]:>9}")

print("EXCEPTION REPORT: angsuran tertunggak per 19 Nov 2026")
for r in db.execute("""SELECT a.nama, p.id, COUNT(*), MIN(g.jatuh_tempo), p.pokok / p.tenor * COUNT(*)
                       FROM angsuran g JOIN pinjaman p ON p.id = g.pinjaman_id JOIN anggota a ON a.id = p.anggota_id
                       WHERE g.dibayar IS NULL AND g.jatuh_tempo <= '2026-11-19' GROUP BY a.nama, p.id"""):
    pokok = f"{r[4]:,}".replace(",", ".")
    print(f"  {r[0]} pinjaman #{r[1]}: {r[2]} angsuran sejak {r[3]}, pokok tertunggak Rp{pokok}")

total_pinj = db.execute("SELECT SUM(pokok) FROM pinjaman").fetchone()[0]
macet = db.execute("SELECT SUM(pokok) FROM pinjaman WHERE id IN (SELECT pinjaman_id FROM angsuran WHERE dibayar IS NULL AND jatuh_tempo <= '2026-10-19')").fetchone()[0] or 0
print(f"NPL (tunggakan > 30 hari): {macet / total_pinj:.1%} dari portofolio pinjaman")
'''

RFM = '''import sqlite3, random
random.seed(11)
# Segmentasi pelanggan RFM untuk tim pemasaran toko daring
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE pesanan (pelanggan TEXT, tgl TEXT, total INT)")
profil = {"setia": (12, 5, 250000), "baru": (1, 3, 180000), "hampir_hilang": (4, 120, 200000), "hilang": (2, 250, 90000), "besar": (6, 20, 900000)}
for i in range(60):
    jenis = list(profil)[i % 5]
    n, terakhir, nilai = profil[jenis]
    for k in range(n):
        hari = terakhir + k * 21 + random.randint(0, 6)
        db.execute("INSERT INTO pesanan VALUES (?, date('2026-11-19', ?), ?)", (f"C{i:03}", f"-{hari} day", int(nilai * random.uniform(0.7, 1.3))))

rows = db.execute("""SELECT pelanggan, CAST(julianday('2026-11-19') - julianday(MAX(tgl)) AS INT) AS r, COUNT(*) AS f, SUM(total) AS m
                     FROM pesanan GROUP BY pelanggan""").fetchall()
def skor(nilai, semua, terbalik=False):
    urut = sorted(semua); posisi = sum(v <= nilai for v in urut) / len(urut)
    s = 1 + min(int(posisi * 5), 4)
    return 6 - s if terbalik else s
R = [r for _, r, _, _ in rows]; F = [f for _, _, f, _ in rows]; M = [m for _, _, _, m in rows]
def segmen(r, f, m):
    if r >= 4 and f >= 4: return "Champions"
    if r >= 4 and f <= 2: return "Pelanggan baru"
    if f >= 4 and m >= 5: return "Loyal bernilai tinggi"
    if r <= 2 and f >= 4: return "Berisiko hilang"
    if r <= 2: return "Hilang"
    return "Perlu perhatian"
hasil = {}
for p, r, f, m in rows:
    s = segmen(skor(r, R, True), skor(f, F), skor(m, M))
    hasil.setdefault(s, []).append(m)
AKSI = {"Champions": "program loyalitas, akses awal produk baru", "Pelanggan baru": "onboarding: voucher pembelian kedua",
        "Loyal bernilai tinggi": "account manager, penawaran paket grosir",
        "Berisiko hilang": "win-back personal + survei alasan", "Hilang": "kampanye murah, jangan beri diskon besar",
        "Perlu perhatian": "rekomendasi produk terkait"}
print(f"{'segmen':<22}{'pelanggan':>9}{'nilai total':>16}  tindakan")
for s, v in sorted(hasil.items(), key=lambda x: -sum(x[1])):
    nilai = f"{sum(v):,}".replace(",", ".")
    print(f"{s:<22}{len(v):>9}{nilai:>16}  {AKSI[s]}")
'''

MDM = '''from difflib import SequenceMatcher
import re

# Master data pelanggan dari 3 sistem (CRM, POS, e-commerce) penuh duplikat -> golden record
DATA = [
    ("CRM", "PT Maju Jaya Abadi", "021-5550123", "Jl. Gatot Subroto Kav. 5, Jakarta"),
    ("POS", "PT. MAJU JAYA ABADI", "(021) 555 0123", "Jl Gatot Subroto Kav 5 Jakarta Selatan"),
    ("WEB", "Maju Jaya Abadi", "+62 21 5550123", "Gatot Subroto 5, Jaksel"),
    ("CRM", "CV Sinar Terang", "0812-3456-7890", "Jl. Pahlawan 12, Surabaya"),
    ("POS", "CV Sinar Terang Elektrik", "081234567890", "Jl Pahlawan No 12 Surabaya"),
    ("WEB", "Toko Sinar", "085799990000", "Jl. Diponegoro 3, Malang"),
    ("CRM", "UD Berkah Tani", "0274-889911", "Jl. Kaliurang Km 7, Sleman"),
]
def norm_nama(n):
    n = n.lower().replace(".", " ")
    n = re.sub(r"\\b(pt|cv|ud|toko|tbk)\\b", " ", n)
    return " ".join(n.split())
def norm_hp(h):
    d = re.sub(r"\\D", "", h)
    return "0" + d[2:] if d.startswith("62") else d
def mirip(a, b):
    s_nama = SequenceMatcher(None, norm_nama(a[1]), norm_nama(b[1])).ratio()
    s_hp = 1.0 if norm_hp(a[2]) == norm_hp(b[2]) else 0.0
    return 0.6 * s_nama + 0.4 * s_hp, s_nama, s_hp

grup = list(range(len(DATA)))
def akar(i):
    while grup[i] != i: i = grup[i]
    return i
for i in range(len(DATA)):
    for j in range(i + 1, len(DATA)):
        skor, sn, sh = mirip(DATA[i], DATA[j])
        if skor >= 0.75:
            grup[akar(j)] = akar(i)
            print(f"cocok {skor:.2f} (nama {sn:.2f}, hp {sh:.0f}): {DATA[i][0]}:{DATA[i][1]}  ~  {DATA[j][0]}:{DATA[j][1]}")
klaster = {}
for i in range(len(DATA)): klaster.setdefault(akar(i), []).append(DATA[i])
print(f"\\n{len(DATA)} catatan -> {len(klaster)} pelanggan unik (golden record)")
PRIORITAS = {"CRM": 0, "POS": 1, "WEB": 2}                      # aturan survivorship: CRM paling tepercaya
for k in klaster.values():
    terbaik = min(k, key=lambda x: PRIORITAS[x[0]])
    print(f"  {terbaik[1]:<22} {norm_hp(terbaik[2]):<14} sumber: {', '.join(x[0] for x in k)}")
'''

RISIKO = '''# Gap assessment kontrol keamanan (mengacu ISO/IEC 27001:2022 Annex A) + register risiko untuk klinik
KONTROL = [  # (kode, kontrol, tingkat kematangan saat ini 0-5, target)
    ("5.15", "Kontrol akses berbasis peran", 2, 4), ("5.17", "Manajemen kata sandi & MFA", 1, 4),
    ("5.23", "Keamanan layanan cloud", 2, 3), ("5.30", "Kesiapan TIK untuk kelangsungan bisnis", 1, 3),
    ("6.3", "Pelatihan kesadaran keamanan", 2, 3), ("8.13", "Backup informasi", 2, 4),
    ("8.15", "Logging", 1, 3), ("8.24", "Penggunaan kriptografi", 2, 3),
]
print("GAP KONTROL (prioritas: gap terbesar)")
for kode, nama, kini, target in sorted(KONTROL, key=lambda x: -(x[3] - x[2])):
    print(f"  A.{kode:<5} {nama:<38} {kini} -> {target}  gap {target - kini}  {'#' * (target - kini)}")
rata = sum(k for *_, k, _ in KONTROL) / len(KONTROL)
print(f"Kematangan rata-rata {rata:.1f} dari 5")

RISIKO = [  # (risiko, kemungkinan, dampak, kontrol terkait, biaya mitigasi juta)
    ("Akun dokter dibobol (tanpa MFA)", 4, 5, "5.17", 18), ("Ransomware mengenkripsi rekam medis", 3, 5, "8.13", 45),
    ("Akses staf melebihi kebutuhan", 4, 3, "5.15", 12), ("Tidak ada jejak siapa membuka data pasien", 3, 4, "8.15", 25),
    ("Layanan cloud tunggal down", 2, 4, "5.30", 60),
]
print("\\nREGISTER RISIKO (risk = kemungkinan x dampak; nilai per biaya mitigasi)")
for r, l, d, k, biaya in sorted(RISIKO, key=lambda x: -(x[1] * x[2]) / x[4]):
    print(f"  skor {l * d:>2}  {r:<42} kontrol A.{k:<5} biaya Rp{biaya} jt  efisiensi {l * d / biaya:.2f}")
print("Rekomendasi kuartal ini: MFA, RBAC, dan logging akses data pasien (efisiensi tertinggi);\\n"
      "backup offline teruji dianggarkan berikutnya karena dampak ransomware tetap tinggi.")
'''

SI_MINI = [
MINI(1, 'Process mining sederhana dari event log klaim',
  'Perusahaan asuransi mengeluh klaim kesehatan lama dibayar, tetapi setiap divisi saling menyalahkan. Sistem sudah menyimpan log aktivitas. Ubah log itu menjadi fakta: waktu siklus, varian proses, bottleneck, dan rework.',
  ['Membaca event log (case id, aktivitas, waktu)', 'Waktu siklus per kasus dan varian proses', 'Waktu tunggu rata-rata antar-langkah (bottleneck)', 'Persentase rework dan rekomendasi perbaikan'],
  ['Kelompokkan event per kasus dan urutkan menurut waktu.', 'Hitung selisih waktu awal-akhir untuk waktu siklus; gabungkan urutan aktivitas menjadi varian.', 'Untuk setiap pasangan langkah berurutan, kumpulkan durasi tunggu lalu rata-ratakan.', 'Hitung kasus yang mengulang verifikasi dan usulkan perbaikan proses.'],
  PROSES, 'python', run=True,
  kunci='jalankan pada log nyata dengan pm4py (directly-follows graph, conformance checking) dan bandingkan dengan model BPMN yang seharusnya.',
  cek=q('Apa keunggulan process mining dibanding wawancara saja saat memetakan proses as-is?', ['Menunjukkan alur yang benar-benar terjadi beserta waktu dan variasinya dari data, bukan dari ingatan atau prosedur di atas kertas', 'Tidak perlu data sama sekali', 'Selalu menghasilkan proses yang lebih cepat'], 0, 'Fakta dari jejak sistem.')),

MINI(2, 'Studi kelayakan investasi dengan analisis sensitivitas',
  'Jaringan 25 apotek ingin membeli aplikasi pemesanan dan stok senilai Rp1,35 M. Direksi bertanya: masih layakkah jika manfaatnya meleset atau adopsi lambat? Buat analisis NPV, IRR, payback, dan sensitivitas.',
  ['Arus kas 5 tahun dengan kurva adopsi bertahap', 'NPV pada tingkat diskonto 11%, IRR dengan metode biseksi, payback', 'Skenario sensitivitas: manfaat turun, investasi naik, adopsi lambat, gabungan', 'Kesimpulan layak/tidak per skenario'],
  ['Susun manfaat per sumber (stok kedaluwarsa, lembur, penjualan hilang) dan biaya operasional.', 'Tulis fungsi npv, irr (cari tingkat diskonto saat NPV = 0), dan payback.', 'Bungkus pembentukan arus kas dalam fungsi berparameter agar skenario mudah diganti.', 'Tampilkan tabel sensitivitas untuk dibahas di rapat investasi.'],
  KELAYAKAN, 'python', run=True,
  kunci='tambahkan simulasi Monte Carlo (1.000 skenario acak) dan tampilkan peluang NPV negatif.',
  cek=q('Kenapa analisis sensitivitas penting dalam studi kelayakan?', ['Karena angka manfaat adalah perkiraan; pengambil keputusan perlu tahu seberapa besar perubahan asumsi yang membuat proyek tidak layak', 'Agar NPV selalu positif', 'Karena IRR tidak bisa dihitung tanpa sensitivitas'], 0, 'Uji asumsi paling rapuh.')),

MINI(3, 'Sistem informasi koperasi: dari ERD ke laporan manajemen',
  'Koperasi karyawan pabrik masih mencatat simpanan dan pinjaman di buku besar. Pengurus tidak tahu siapa yang menunggak sampai rapat tahunan. Rancang database dan laporan yang menjawab kebutuhan pengurus.',
  ['ERD: anggota, simpanan (pokok/wajib/sukarela), pinjaman, angsuran', 'Constraint untuk jenis simpanan dan jumlah positif', 'Laporan simpanan per anggota', 'Exception report angsuran tertunggak dan rasio NPL'],
  ['Turunkan tabel dari entitas dan relasinya; angsuran memakai kunci gabungan (pinjaman, ke).', 'Isi data contoh dan bangkitkan jadwal angsuran dari tanggal pinjaman dan tenor.', 'Gunakan SUM(CASE ...) untuk laporan pivot simpanan per jenis.', 'Filter angsuran yang jatuh tempo tetapi belum dibayar untuk exception report dan NPL.'],
  KOPERASI, 'python', run=True,
  kunci='tambahkan perhitungan SHU per anggota dan cetak kartu anggota digital berisi saldo simpanan.',
  cek=q('Kenapa exception report lebih berguna bagi pengurus daripada daftar semua angsuran?', ['Pengurus langsung melihat hal yang memerlukan tindakan (tunggakan) tanpa membaca ratusan baris normal', 'Karena lebih berwarna', 'Karena daftar lengkap tidak bisa dibuat SQL'], 0, 'Manajemen berdasarkan pengecualian.')),

MINI(4, 'Segmentasi pelanggan RFM untuk kampanye pemasaran',
  'Tim pemasaran toko daring mengirim promo yang sama ke semua pelanggan dan biaya diskonnya membengkak. Buat segmentasi RFM (recency, frequency, monetary) dari data pesanan beserta tindakan untuk setiap segmen.',
  ['Agregasi pesanan per pelanggan dengan SQL: recency, frequency, monetary', 'Skor 1-5 berbasis kuantil untuk setiap dimensi', 'Aturan segmen: Champions, Pelanggan baru, Loyal bernilai tinggi, Berisiko hilang, Hilang, Perlu perhatian', 'Ringkasan jumlah pelanggan, nilai, dan tindakan per segmen'],
  ['Hitung selisih hari dari pesanan terakhir, jumlah pesanan, dan total belanja per pelanggan.', 'Ubah nilai mentah menjadi skor kuantil (recency dibalik: makin baru makin tinggi).', 'Petakan kombinasi skor ke segmen dengan aturan yang mudah dijelaskan ke tim pemasaran.', 'Urutkan segmen menurut nilai dan tuliskan tindakan yang berbeda.'],
  RFM, 'python', run=True,
  kunci='ukur hasil kampanye per segmen dengan kelompok kontrol (holdout 10%) agar dampak promo bisa dibuktikan.',
  cek=q('Kenapa segmen "Hilang" sebaiknya tidak diberi diskon besar?', ['Peluang kembalinya rendah sehingga biaya diskon besar jarang terbayar; lebih efisien kampanye murah dan survei alasan', 'Karena mereka tidak punya email', 'Karena RFM melarangnya'], 0, 'Biaya per segmen harus sepadan dengan nilai.')),

MINI(5, 'Master data management: menggabungkan duplikat pelanggan',
  'Distributor punya data pelanggan di CRM, POS, dan e-commerce. Satu perusahaan tercatat dengan tiga ejaan berbeda sehingga limit kredit dan laporan penjualan per pelanggan salah. Buat proses pencocokan dan golden record.',
  ['Normalisasi nama badan usaha (PT, CV, UD, tanda baca) dan nomor telepon (+62/0)', 'Skor kemiripan gabungan nama (fuzzy) dan telepon (persis)', 'Pengelompokan catatan yang cocok (union-find)', 'Aturan survivorship: sumber paling tepercaya menjadi golden record'],
  ['Tulis fungsi normalisasi agar perbedaan format tidak dianggap perbedaan isi.', 'Gunakan SequenceMatcher untuk nama dan perbandingan persis untuk telepon, beri bobot.', 'Gabungkan pasangan dengan skor ≥ ambang menjadi klaster.', 'Pilih nilai dari sumber prioritas tertinggi dan catat asal setiap catatan.'],
  MDM, 'python', run=True,
  kunci='tambahkan antrean review manual untuk skor 0,6-0,75, dan simpan tabel pemetaan ID sumber ke ID master.',
  cek=q('Apa itu golden record dalam master data management?', ['Satu versi data terbaik untuk sebuah entitas (misalnya pelanggan) yang disusun dari beberapa sumber dengan aturan yang jelas', 'Data yang disimpan dalam warna emas', 'Backup data terbaru'], 0, 'Single source of truth.')),

MINI(6, 'Gap assessment keamanan informasi dan register risiko',
  'Klinik swasta akan bekerja sama dengan asuransi yang mensyaratkan pengelolaan keamanan informasi. Nilai kematangan kontrol terhadap ISO/IEC 27001:2022 Annex A, susun register risiko, dan pilih prioritas berdasarkan nilai per biaya.',
  ['Daftar kontrol Annex A yang relevan dengan tingkat kematangan saat ini dan target', 'Gap per kontrol dan kematangan rata-rata', 'Register risiko kemungkinan × dampak yang ditautkan ke kontrol', 'Prioritas mitigasi berdasarkan skor risiko per biaya'],
  ['Wawancara dan periksa bukti untuk menilai kematangan 0-5 setiap kontrol.', 'Urutkan menurut gap terbesar untuk peta jalan perbaikan.', 'Hitung skor risiko dan hubungkan ke kontrol yang memitigasinya.', 'Bagi skor dengan biaya mitigasi untuk memilih quick win.'],
  RISIKO, 'python', run=True,
  kunci='buat Statement of Applicability (SoA) lengkap dan rencana audit internal, lalu petakan ke kewajiban UU PDP.',
  cek=q('Kenapa prioritas mitigasi mempertimbangkan biaya, bukan hanya skor risiko?', ['Anggaran terbatas; kontrol murah yang menurunkan risiko besar (seperti MFA) memberi perlindungan paling banyak per rupiah', 'Karena risiko tinggi tidak perlu ditangani', 'Agar laporan lebih panjang'], 0, 'Efisiensi pengendalian.')),
]

# ---------------------------------------------------------------- BESAR
ERP = r'''# migrasi/impor_master.py — migrasi data distributor ke Odoo 18 lewat XML-RPC (dijalankan setelah UAT data)
import csv, xmlrpc.client
URL, DB = "https://erp.distributor-contoh.id", "prod"
uid = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common").authenticate(DB, "migrasi@contoh.id", API_KEY, {})
odoo = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
def panggil(model, metode, *args, **kw): return odoo.execute_kw(DB, uid, API_KEY, model, metode, list(args), kw)

laporan = {"dibuat": 0, "diperbarui": 0, "ditolak": []}
for r in csv.DictReader(open("bersih/pelanggan_golden.csv")):          # hasil MDM: sudah dedup & divalidasi
    if not r["npwp"] and r["tipe"] == "perusahaan":
        laporan["ditolak"].append((r["kode"], "NPWP wajib untuk faktur pajak")); continue
    nilai = {"name": r["nama"], "ref": r["kode"], "vat": r["npwp"], "phone": r["telepon"], "street": r["alamat"],
             "property_payment_term_id": TERMIN[r["termin"]], "credit_limit": float(r["limit_kredit"])}
    ada = panggil("res.partner", "search", [["ref", "=", r["kode"]]])
    if ada: panggil("res.partner", "write", ada, nilai); laporan["diperbarui"] += 1
    else:   panggil("res.partner", "create", nilai);   laporan["dibuat"] += 1
print(laporan)

# Rekonsiliasi wajib sebelum cut-over: saldo piutang per pelanggan di sistem lama == saldo awal di Odoo
#   SELECT kode, SUM(sisa) FROM piutang_lama GROUP BY kode   vs   account.move.line (akun piutang, saldo awal)

# Rencana cut-over (go-live 1 Jan, tutup buku 31 Des):
#   H-14  freeze master data, migrasi percobaan ke-3, UAT ulang skenario O2C & P2P
#   H-2   stok opname semua gudang -> saldo awal persediaan per lot
#   H-0   impor saldo awal (persediaan, piutang, hutang, GL), rekonsiliasi, tanda tangan CFO
#   H+1..H+30 hypercare: war room, tiket per modul, laporan harian ke steering committee'''

SIAKAD = r'''-- skema inti SIAKAD universitas (PostgreSQL) + sinkronisasi ke PDDikti (Neo Feeder)
CREATE TABLE mahasiswa (nim text PRIMARY KEY, nik_hash bytea NOT NULL, nama text NOT NULL, prodi_id int NOT NULL,
                        angkatan smallint NOT NULL, status text NOT NULL CHECK (status IN ('aktif','cuti','lulus','keluar','non-aktif')));
CREATE TABLE kelas (id bigint PRIMARY KEY, mk_kode text NOT NULL, semester text NOT NULL, dosen_nidn text NOT NULL,
                    kuota smallint NOT NULL CHECK (kuota > 0));
CREATE TABLE krs (nim text REFERENCES mahasiswa, kelas_id bigint REFERENCES kelas, disetujui_pa boolean DEFAULT false,
                  nilai_angka numeric(5,2), nilai_huruf text, PRIMARY KEY (nim, kelas_id));

-- Aturan bisnis di database: kuota kelas tidak boleh terlampaui saat war KRS (ribuan mahasiswa serentak)
CREATE FUNCTION cek_kuota() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  PERFORM 1 FROM kelas WHERE id = NEW.kelas_id FOR UPDATE;                    -- serialisasi per kelas
  IF (SELECT count(*) FROM krs WHERE kelas_id = NEW.kelas_id) >= (SELECT kuota FROM kelas WHERE id = NEW.kelas_id) THEN
    RAISE EXCEPTION 'Kelas penuh' USING ERRCODE = 'P0001';
  END IF;
  RETURN NEW;
END $$;
CREATE TRIGGER trg_kuota BEFORE INSERT ON krs FOR EACH ROW EXECUTE FUNCTION cek_kuota();

-- Early warning akademik untuk dosen PA (dipakai dashboard tiap awal semester)
CREATE VIEW peringatan_akademik AS
SELECT m.nim, m.nama, ips.ips, ips.sks, ipk.ipk
FROM mahasiswa m
JOIN LATERAL (SELECT round(sum(k.sks * b.bobot) / nullif(sum(k.sks), 0), 2) AS ips, sum(k.sks) AS sks
              FROM krs r JOIN kelas c ON c.id = r.kelas_id JOIN mata_kuliah k ON k.kode = c.mk_kode
              JOIN bobot_nilai b ON b.huruf = r.nilai_huruf WHERE r.nim = m.nim AND c.semester = '2026/2027-1') ips ON true
JOIN LATERAL (SELECT ipk FROM transkrip_ringkas t WHERE t.nim = m.nim) ipk ON true
WHERE m.status = 'aktif' AND (ips.ips < 2.0 OR ipk.ipk < 2.25);

# sinkron/feeder.py — kirim nilai ke PDDikti setelah dosen mengunci nilai (antrean + retry + log)
def kirim_nilai(semester):
    for baris in db.nilai_terkunci_belum_terkirim(semester):
        r = feeder.call("UpdateNilaiPerkuliahanKelas", token, key={"id_kelas_kuliah": baris.id_feeder, "id_registrasi_mahasiswa": baris.id_reg},
                        record={"nilai_angka": float(baris.nilai_angka), "nilai_huruf": baris.nilai_huruf, "nilai_indeks": baris.indeks})
        db.catat_sinkron(baris, r["error_code"], r["error_desc"])        # dashboard: % data tersinkron per prodi'''

BIPLAT = r'''-- models/marts/fct_penjualan_harian.sql (dbt) — satu definisi angka untuk semua dashboard
{{ config(materialized='incremental', unique_key=['tanggal', 'toko_id', 'produk_id'], partition_by={'field': 'tanggal', 'data_type': 'date'}) }}
select date(t.waktu, 'Asia/Jakarta') as tanggal, t.toko_id, d.produk_id,
       count(distinct t.transaksi_id) as jumlah_transaksi,
       sum(d.qty) as qty, sum(d.qty * d.harga) as omzet, sum(d.qty * p.hpp) as hpp
from {{ ref('stg_pos__transaksi') }} t
join {{ ref('stg_pos__detail') }} d using (transaksi_id)
join {{ ref('dim_produk') }} p on p.produk_id = d.produk_id and t.waktu between p.berlaku_dari and p.berlaku_sampai
where t.status = 'selesai'
{% if is_incremental() %} and date(t.waktu, 'Asia/Jakarta') >= date_sub(current_date('Asia/Jakarta'), interval 3 day) {% endif %}
group by 1, 2, 3

# models/marts/_metrics.yml — dbt Semantic Layer (MetricFlow)
semantic_models:
  - name: penjualan
    model: ref('fct_penjualan_harian')
    defaults: { agg_time_dimension: tanggal }
    entities: [{ name: toko, type: foreign, expr: toko_id }]
    measures:
      - { name: omzet, agg: sum }
      - { name: hpp, agg: sum }
    dimensions: [{ name: tanggal, type: time, type_params: { time_granularity: day } }]
metrics:
  - { name: omzet, type: simple, type_params: { measure: omzet } }
  - name: margin_kotor
    type: derived
    type_params: { expr: (omzet - hpp) / omzet, metrics: [omzet, hpp] }

# Power BI: row-level security per wilayah (role "Manajer Area")
#   [Wilayah] = LOOKUPVALUE(PetaAkses[Wilayah], PetaAkses[Email], USERPRINCIPALNAME())
# Tata kelola: setiap metrik punya pemilik bisnis, dashboard resmi diberi tanda "Certified",
# refresh 06.00 WIB, uji data dbt gagal -> dashboard menampilkan banner "data tertunda".'''

SPBE = r'''# arsitektur/perizinan-online.yaml — layanan perizinan usaha terpadu pemerintah kabupaten (selaras arsitektur SPBE)
layanan: Perizinan Berusaha Daerah (PBG, reklame, izin keramaian)
pengguna: [warga & pelaku UMKM, petugas front office DPMPTSP, dinas teknis, kepala dinas (tanda tangan elektronik)]
kanal: [web responsif, aplikasi Android ringan (< 15 MB), loket dengan pendampingan, WhatsApp notifikasi]
integrasi:
  - { sistem: OSS RBA (pusat),        cara: API, data: NIB & status perizinan }
  - { sistem: Dukcapil,               cara: API web service resmi, data: verifikasi NIK }
  - { sistem: BSrE (tanda tangan elektronik), cara: API, data: dokumen izin bertanda tangan }
  - { sistem: Bank daerah / QRIS,     cara: API + callback, data: pembayaran retribusi }
  - { sistem: Satu Data daerah,       cara: ekspor harian terjadwal, data: statistik izin (tanpa data pribadi) }
data:
  pribadi: [NIK, nama, alamat, nomor HP]      # dienkripsi, akses per peran, retensi sesuai jadwal retensi arsip
  terbuka: [jumlah izin per jenis per kecamatan, rata-rata waktu proses]
sla_layanan:
  - { jenis: reklame,     target_hari_kerja: 3 }
  - { jenis: PBG,         target_hari_kerja: 14 }
  - { tahap: verifikasi berkas, target_jam: 24, eskalasi: kepala bidang }
kpi:
  - persentase permohonan diajukan online (target 70% di tahun 1)
  - median waktu proses per jenis izin vs SLA
  - indeks kepuasan masyarakat (IKM) per layanan
  - persentase permohonan ditolak karena berkas tidak lengkap (target turun 50%)
keamanan: [penilaian risiko sebelum go-live, uji penetrasi pihak ketiga, MFA untuk petugas, log audit setiap perubahan status]
tata_kelola: [forum SPBE kabupaten, pemilik proses DPMPTSP, Diskominfo sebagai pengelola infrastruktur, review triwulanan]'''

SI_BESAR = [
BESAR(1, 'Implementasi ERP untuk distributor nasional',
  'Distributor barang konsumsi dengan 6 gudang dan 900 pelanggan toko memakai sistem akuntansi lama, Excel untuk stok, dan WhatsApp untuk order sales. Tutup buku butuh 18 hari, stok selisih 6%, dan piutang macet tidak terpantau. Direksi memutuskan mengimplementasikan ERP.',
  ['Fit-gap analysis proses O2C, P2P, persediaan multi-gudang, dan akuntansi (termasuk e-Faktur)', 'Desain proses to-be dengan prinsip adopsi standar dan kustomisasi minimal', 'Migrasi data bertahap: master (golden record), saldo awal, rekonsiliasi', 'UAT berbasis skenario bisnis dan pelatihan key user', 'Cut-over, hypercare 30 hari, dan pengukuran manfaat (tutup buku, selisih stok, DSO)'],
  'Odoo 18 / SAP Business One / Microsoft Dynamics 365 BC, Python untuk migrasi data, BPMN (Camunda Modeler/Bizagi), Jira untuk tiket UAT, Power BI untuk laporan manajemen',
  [('Lingkup', 'Penjualan, pembelian, persediaan (lot & kedaluwarsa), akuntansi, aplikasi sales mobile'), ('Tim', 'sponsor CFO, PM, 2 BA, konsultan vendor, key user per departemen'),
   ('Data', 'pembersihan & dedup master, 3 kali migrasi percobaan, rekonsiliasi ditandatangani'), ('Pengujian', '120 skenario UAT end-to-end, 0 isu kritis sebagai syarat go-live'),
   ('Perubahan', 'rencana komunikasi, pelatihan per peran, champion di tiap gudang'), ('Ukuran sukses', 'tutup buku ≤ 5 hari, selisih stok < 1%, DSO turun 10 hari dalam 6 bulan')],
  ['Petakan proses as-is dan lakukan fit-gap bersama key user.', 'Rancang to-be, putuskan setiap gap: ubah proses, konfigurasi, atau kustomisasi berbiaya jelas.', 'Bersihkan dan migrasikan data dalam beberapa putaran percobaan dengan rekonsiliasi.', 'Jalankan UAT, latih pengguna, siapkan runbook cut-over.', 'Go-live, hypercare, lalu ukur manfaat terhadap business case.'],
  ERP, 'python', standar='proses standar diadopsi sebanyak mungkin, data migrasi terekonsiliasi dan disetujui pemilik, UAT berbasis skenario nyata, manfaat diukur setelah go-live',
  cek=q('Kenapa prinsip "adopsi proses standar, kustomisasi minimal" penting dalam implementasi ERP?', ['Kustomisasi menambah biaya, risiko, dan menyulitkan upgrade; proses standar ERP umumnya sudah mewakili praktik terbaik', 'Karena ERP tidak bisa dikustomisasi', 'Agar karyawan tidak perlu pelatihan'], 0, 'Biaya jangka panjang kustomisasi.')),

BESAR(2, 'Sistem informasi akademik terpadu universitas',
  'Universitas swasta dengan 14.000 mahasiswa memakai 5 aplikasi terpisah untuk PMB, KRS, keuangan, e-learning, dan pelaporan PDDikti. Server tumbang setiap masa KRS, data mahasiswa berbeda di tiap sistem, dan pelaporan ke PDDikti dikerjakan manual berminggu-minggu.',
  ['Arsitektur terpadu dengan master data mahasiswa, dosen, dan kurikulum tunggal', 'KRS online yang tahan beban (kuota kelas aman saat ribuan akses bersamaan)', 'Integrasi keuangan (UKT/VA bank) dan e-learning (SSO, sinkron kelas)', 'Sinkronisasi otomatis ke PDDikti dengan antrean dan log', 'Dashboard akademik: early warning, kelulusan tepat waktu, beban dosen'],
  'PostgreSQL, backend Laravel/Django/Spring Boot, SSO (Keycloak), Moodle, API bank (virtual account), Neo Feeder PDDikti, Metabase/Power BI, uji beban k6',
  [('Data', 'master mahasiswa/dosen/kurikulum di satu database; NIK disimpan sebagai hash + terenkripsi'), ('KRS', 'aturan kuota dan prasyarat di database; antrean akses; uji beban 5.000 pengguna serentak'),
   ('Integrasi', 'VA bank untuk UKT (status bayar membuka KRS), SSO ke Moodle, sinkron PDDikti terjadwal'), ('Keamanan', 'akses per peran (mahasiswa, dosen PA, prodi, BAA), audit perubahan nilai'),
   ('Analitik', 'early warning IPS/IPK, kohort kelulusan, rasio dosen-mahasiswa untuk akreditasi'), ('Tata kelola', 'pemilik data per unit (BAA, keuangan, SDM), SOP perubahan nilai')],
  ['Petakan proses akademik dari PMB sampai wisuda dan sumber data masing-masing.', 'Rancang ERD terpadu dan rencana migrasi data dari 5 aplikasi lama.', 'Bangun modul KRS dengan aturan di database, lalu uji beban sebelum masa KRS.', 'Integrasikan keuangan, SSO, e-learning, dan sinkron PDDikti dengan pemantauan.', 'Luncurkan bertahap per fakultas, ukur waktu pelaporan, gangguan KRS, dan kepuasan.'],
  SIAKAD, 'sql', standar='satu sumber data akademik, KRS stabil saat puncak, aturan bisnis ditegakkan sistem, pelaporan PDDikti otomatis dan terpantau, data pribadi terlindungi',
  cek=q('Kenapa pemeriksaan kuota kelas diletakkan di database (dengan penguncian), bukan hanya di aplikasi?', ['Saat ribuan mahasiswa mendaftar bersamaan, pemeriksaan di aplikasi saja bisa lolos bersamaan (race condition) sehingga kelas melebihi kuota', 'Agar aplikasi tidak perlu ditulis', 'Karena database lebih berwarna'], 0, 'Integritas di bawah konkurensi.')),

BESAR(3, 'Platform BI perusahaan dengan satu definisi metrik',
  'Grup ritel dengan 120 toko punya 47 dashboard buatan masing-masing divisi. Angka omzet di rapat direksi berbeda antara keuangan, operasional, dan pemasaran, sehingga rapat habis untuk berdebat soal angka, bukan keputusan.',
  ['Inventaris dashboard dan definisi metrik yang beredar; sepakati kamus metrik', 'Model data terpusat (dbt) dengan tes kualitas dan dokumentasi', 'Semantic layer: omzet, margin, AOV, like-for-like growth didefinisikan sekali', 'Dashboard resmi bersertifikat dengan RLS per wilayah dan label kebaruan data', 'Tata kelola: pemilik metrik, proses permintaan dashboard baru, pensiun dashboard tak terpakai'],
  'BigQuery/Snowflake, dbt Core + Semantic Layer, Airflow, Power BI/Looker, Git + CI, data catalog (DataHub/OpenMetadata)',
  [('Model', 'staging → marts (fakta harian per toko-produk, dimensi SCD2) dengan tes unique/not_null/relationships'), ('Metrik', 'kamus metrik dengan pemilik, rumus, filter, contoh; disimpan sebagai kode'),
   ('Akses', 'RLS per wilayah, data pribadi pelanggan tidak masuk lapisan BI'), ('Kualitas', 'tes dbt gagal → banner "data tertunda", alert ke pemilik'),
   ('Adopsi', 'jumlah pengguna aktif mingguan, dashboard resmi vs liar, waktu rapat untuk keputusan'), ('Pensiun', 'dashboard tidak dibuka 60 hari diarsipkan setelah konfirmasi pemilik')],
  ['Kumpulkan semua definisi omzet yang beredar dan selenggarakan workshop penyepakatan dengan CFO.', 'Bangun model dbt dan tes; rekonsiliasi angka dengan laporan keuangan resmi.', 'Definisikan metrik di semantic layer dan bangun dashboard eksekutif bersertifikat.', 'Terapkan RLS, katalog data, dan proses permintaan dashboard.', 'Pensiunkan dashboard duplikat dan ukur adopsi serta waktu rapat.'],
  BIPLAT, 'sql', standar='satu definisi per metrik dengan pemilik, angka BI terekonsiliasi dengan laporan keuangan, kualitas data teruji otomatis, akses sesuai peran, adopsi terukur',
  cek=q('Apa masalah utama yang diselesaikan semantic layer?', ['Metrik didefinisikan sekali dan dipakai semua dashboard/alat, sehingga tidak ada versi angka berbeda antar-divisi', 'Mempercepat internet kantor', 'Menggantikan data warehouse'], 0, 'Satu definisi metrik.')),

BESAR(4, 'Transformasi digital layanan perizinan pemerintah daerah',
  'Pemerintah kabupaten menerima 9.000 permohonan izin per tahun lewat loket. Warga datang berkali-kali karena berkas kurang, status tidak bisa dilacak, rata-rata PBG selesai 47 hari, dan indeks kepuasan masyarakat rendah. Bupati menargetkan layanan perizinan online yang terintegrasi.',
  ['Riset pengguna: warga, UMKM, petugas loket, dinas teknis (termasuk pengguna dengan literasi digital rendah)', 'Service blueprint dan penyederhanaan proses (hapus syarat yang bisa diambil dari sistem lain)', 'Integrasi OSS RBA, Dukcapil, tanda tangan elektronik BSrE, pembayaran retribusi', 'Pelacakan status, notifikasi WhatsApp, dan SLA per tahap dengan eskalasi', 'Tata kelola SPBE, keamanan, dan dashboard kinerja layanan terbuka untuk publik'],
  'Arsitektur SPBE, BPMN, aplikasi web responsif + Android ringan, API gateway, PostgreSQL, BSrE, QRIS/bank daerah, Metabase untuk dashboard publik',
  [('Kanal', 'online mandiri, loket dengan pendampingan, WhatsApp notifikasi; tidak ada warga yang tertinggal'), ('Proses', 'syarat dikurangi (NIK diverifikasi otomatis), berkas dicek di awal dengan checklist'),
   ('Integrasi', 'OSS RBA, Dukcapil, BSrE, pembayaran; data izin ke Satu Data tanpa data pribadi'), ('Keamanan', 'penilaian risiko, uji penetrasi, MFA petugas, log audit status'),
   ('SLA', 'target per jenis izin dan per tahap, eskalasi otomatis, laporan mingguan ke kepala dinas'), ('Dampak', 'median waktu proses, % online, IKM, kunjungan ulang ke loket')],
  ['Lakukan riset kontekstual di loket dan wawancara warga serta petugas.', 'Susun service blueprint as-is/to-be; hapus syarat yang tidak perlu bersama dinas teknis.', 'Bangun MVP untuk izin reklame (sederhana) lalu PBG; integrasikan Dukcapil dan pembayaran.', 'Uji dengan warga, latih petugas, dan buka loket pendampingan.', 'Pantau SLA dan IKM, publikasikan dashboard kinerja, perluas ke jenis izin lain.'],
  SPBE, 'yaml', standar='layanan dirancang dari kebutuhan warga, syarat disederhanakan lewat integrasi, status transparan dengan SLA, inklusif bagi pengguna non-digital, data pribadi terlindungi, kinerja diukur dan dipublikasikan',
  cek=q('Kenapa loket pendampingan tetap dipertahankan walau layanan sudah online?', ['Agar warga dengan literasi digital rendah atau tanpa perangkat tetap terlayani (inklusif), sambil didampingi memakai sistem yang sama', 'Karena sistem online tidak bisa dipakai', 'Agar petugas tetap sibuk'], 0, 'Transformasi digital tidak boleh meninggalkan warga.')),
]

PJ_SI = JALUR_M('Analis Sistem Informasi & BI', 'Menengah',
  'Enam proyek mini Python yang dijalankan (process mining dari event log, studi kelayakan dengan sensitivitas, SI koperasi dari ERD ke laporan, segmentasi RFM, master data management, gap assessment ISO 27001) dan empat proyek besar berskala industri 2026-2027 (implementasi ERP distributor, SIAKAD terpadu, platform BI dengan satu definisi metrik, transformasi layanan perizinan daerah), lengkap dengan penyelesaiannya.',
  ['Process mining', 'Business case', 'Master data', 'BI & semantic layer', 'E-government'], SI_MINI, SI_BESAR)
