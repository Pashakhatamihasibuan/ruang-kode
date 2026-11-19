"""Pendalaman jalur Manajemen Sistem Informasi: istilah dunia kerja dan contoh (Python/SQLite dijalankan; dokumen sebagai rujukan)."""
K = 'msi'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def Q(t, code, b=None, setup=''):
    return dict(t=t, b=b, code=code.strip('\n'), lang='sql', setup=setup)


D = {
'Manajemen Sistem Informasi vs Sistem Informasi Manajemen': dict(
  ist=[('Manajemen Sistem Informasi (MSI)', 'Disiplin mengelola seluruh sistem informasi organisasi: strategi, investasi, orang, proses, risiko, dan tata kelola.'),
       ('Sistem Informasi Manajemen (SIM)', 'Satu jenis sistem yang menyajikan laporan rutin untuk manajer menengah dari data transaksi.'),
       ('Business analyst / system analyst', 'Penerjemah kebutuhan bisnis menjadi spesifikasi sistem; jembatan antara pengguna dan tim teknis.'),
       ('IT governance', 'Cara organisasi memastikan TI selaras dengan tujuan bisnis, dikendalikan risikonya, dan terukur nilainya.')],
  cx=[T('Satu organisasi, dua sudut pandang', '''
Rumah sakit swasta 200 tempat tidur

Sudut pandang MSI (mengelola SI-nya):
  - Portofolio sistem: SIMRS, e-rekam medis, farmasi, akuntansi, HRIS, BPJS bridging
  - Anggaran TI tahun ini Rp4,2 M: 60% operasional, 40% proyek baru
  - Risiko: kebocoran data pasien, downtime saat jam praktik, vendor tunggal
  - Tata kelola: komite TI bulanan, SLA vendor, audit keamanan tahunan

Sudut pandang SIM (satu sistemnya):
  - Laporan harian: BOR (bed occupancy rate) 78%, pasien rawat inap 156
  - Laporan mingguan: klaim BPJS tertunda 42 berkas, nilai Rp318 juta
  - Laporan bulanan: pendapatan per poli, rata-rata lama rawat (ALOS) 3,9 hari''')]),

'Data, informasi, dan pengetahuan': dict(
  ist=[('DIKW pyramid', 'Data → Information → Knowledge → Wisdom: dari fakta mentah menjadi keputusan yang bijak.'),
       ('Metadata', 'Data tentang data: arti kolom, satuan, sumber, pemilik, kapan diperbarui.'),
       ('Single source of truth', 'Satu sumber data resmi yang disepakati agar tidak ada "angka versi masing-masing".'),
       ('Tacit vs explicit knowledge', 'Pengetahuan di kepala orang (pengalaman) vs yang sudah tertulis (SOP, wiki).')],
  cx=[P('Dari data transaksi menjadi informasi dan pengetahuan', '''
from collections import defaultdict
# DATA: catatan penjualan mentah toko bangunan (tanggal, barang, qty, harga)
data = [("2026-11-03", "Semen 50kg", 40, 68000), ("2026-11-03", "Cat 5L", 6, 245000),
        ("2026-11-10", "Semen 50kg", 55, 68000), ("2026-11-10", "Cat 5L", 4, 245000),
        ("2026-11-17", "Semen 50kg", 71, 69500), ("2026-11-17", "Cat 5L", 3, 245000)]

# INFORMASI: data diolah dan diberi konteks (per minggu, per barang)
per_barang = defaultdict(list)
for tgl, brg, q, h in data:
    per_barang[brg].append((tgl, q, q * h))
for brg, baris in per_barang.items():
    print(brg)
    for tgl, q, nilai in baris:
        print(f"  minggu {tgl}: {q:>3} unit  Rp{nilai:>11,}".replace(",", "."))

# PENGETAHUAN: pola + pengalaman -> dasar tindakan
semen = [q for _, q, _ in per_barang["Semen 50kg"]]
cat = [q for _, q, _ in per_barang["Cat 5L"]]
print(f"Semen naik {semen[-1] / semen[0] - 1:.0%} dalam 2 minggu, cat turun {1 - cat[-1] / cat[0]:.0%}.")
print("Pengetahuan pemilik: musim hujan = proyek cor naik, pengecatan ditunda.")
print("Keputusan (wisdom): tambah stok semen sebelum harga distributor naik, kurangi order cat bulan ini.")
''')]),

'Komponen sistem informasi': dict(
  ist=[('Lima komponen SI', 'Hardware, software, data, prosedur, dan orang (people); sistem gagal jika satu diabaikan.'),
       ('SOP', 'Standard Operating Procedure: prosedur baku yang menjadikan sistem dipakai dengan cara yang sama.'),
       ('Change management', 'Upaya mengelola sisi manusia saat sistem baru diterapkan: komunikasi, pelatihan, dukungan.'),
       ('Total cost of ownership (TCO)', 'Seluruh biaya selama umur sistem: lisensi, infrastruktur, implementasi, pelatihan, dukungan.')],
  cx=[P('Audit kesiapan lima komponen sebelum go-live', '''
# Skor 1-5 hasil observasi di 3 cabang sebelum aplikasi kasir baru diluncurkan
SKOR = {
    "Hardware":  {"Pusat": 5, "Medan": 4, "Kupang": 2},   # printer struk belum datang
    "Software":  {"Pusat": 5, "Medan": 5, "Kupang": 5},
    "Data":      {"Pusat": 4, "Medan": 3, "Kupang": 3},   # master harga belum diperbarui
    "Prosedur":  {"Pusat": 4, "Medan": 2, "Kupang": 2},   # SOP retur belum ada
    "Orang":     {"Pusat": 4, "Medan": 3, "Kupang": 1},   # kasir belum dilatih
}
cabang = ["Pusat", "Medan", "Kupang"]
print(f"{'komponen':<10}" + "".join(f"{c:>8}" for c in cabang))
for k, s in SKOR.items():
    print(f"{k:<10}" + "".join(f"{s[c]:>8}" for c in cabang))
for c in cabang:
    lemah = [k for k in SKOR if SKOR[k][c] <= 2]
    print(f"{c:<7} {'SIAP' if not lemah else 'TUNDA, perbaiki: ' + ', '.join(lemah)}")
''', 'Kebanyakan kegagalan implementasi bukan karena software, tetapi prosedur dan orang yang belum siap.')]),

'SIM dan tingkat manajemen': dict(
  ist=[('Operasional / taktis / strategis', 'Tiga tingkat keputusan: harian dan rinci, bulanan dan ringkas, tahunan dan berorientasi masa depan.'),
       ('Structured vs unstructured decision', 'Keputusan berulang dengan aturan jelas vs keputusan baru yang butuh pertimbangan.'),
       ('Drill-down', 'Kemampuan menelusur dari angka ringkas ke rincian penyusunnya.'),
       ('Exception report', 'Laporan yang hanya menampilkan hal di luar batas normal agar manajer fokus.')],
  cx=[P('Data yang sama, tiga tingkat laporan', '''
import statistics as st
# Penjualan harian 3 cabang selama 4 minggu (juta Rp)
P = {"Medan":    [12, 14, 13, 15, 18, 22, 20] * 4,
     "Bandung":  [10, 11, 10, 12, 14, 17, 16] * 3 + [7, 8, 7, 8, 9, 11, 10],
     "Surabaya": [15, 15, 16, 17, 19, 24, 23] * 4}

print("OPERASIONAL (kepala toko): penjualan kemarin")
for c, v in P.items(): print(f"  {c:<9} Rp{v[-1]} jt")

print("TAKTIS (manajer area): minggu ini vs rata-rata 3 minggu sebelumnya")
for c, v in P.items():
    kini, lalu = sum(v[-7:]), st.mean([sum(v[i:i + 7]) for i in (0, 7, 14)])
    tanda = "  <-- turun > 20%, cek" if kini < 0.8 * lalu else ""
    print(f"  {c:<9} {kini:>4} jt vs {lalu:>5.0f} jt ({kini / lalu - 1:+.0%}){tanda}")

print("STRATEGIS (direksi): kontribusi cabang bulan ini")
total = sum(sum(v) for v in P.values())
for c, v in P.items(): print(f"  {c:<9} {sum(v) / total:.0%}")
''')]),

'Berpikir sistem: melihat gambaran utuh': dict(
  ist=[('Systems thinking', 'Memahami masalah sebagai bagian dari sistem yang saling terhubung, bukan kejadian tunggal.'),
       ('Input–proses–output–feedback', 'Model dasar sistem: masukan diolah menjadi keluaran, dan hasilnya memengaruhi masukan berikutnya.'),
       ('Boundary', 'Batas sistem: apa yang termasuk dalam cakupan analisis dan apa yang menjadi lingkungan.'),
       ('Stakeholder', 'Pihak yang memengaruhi atau dipengaruhi sistem: pengguna, manajemen, pelanggan, regulator, vendor.')],
  cx=[P('Simulasi: menambah kasir tanpa memperbaiki gudang', '''
# Toko daring: pesanan masuk -> dikemas gudang -> dikirim. Manajer menambah CS untuk "mempercepat" layanan.
def simulasi(kapasitas_cs, kapasitas_gudang, hari=10, pesanan_per_hari=120):
    antre_cs = antre_gudang = 0
    for h in range(1, hari + 1):
        antre_cs += pesanan_per_hari
        diproses_cs = min(antre_cs, kapasitas_cs); antre_cs -= diproses_cs
        antre_gudang += diproses_cs
        dikemas = min(antre_gudang, kapasitas_gudang); antre_gudang -= dikemas
    return antre_cs, antre_gudang

for cs, gudang, label in [(100, 100, "awal"), (150, 100, "tambah CS saja"), (130, 130, "seimbangkan CS & gudang")]:
    a, b = simulasi(cs, gudang)
    print(f"{label:<24} antre di CS {a:>4}  antre di gudang {b:>4}  total tertunda {a + b:>4}")
''', 'Menambah CS hanya memindahkan antrean ke gudang. Berpikir sistem mencari hambatan (bottleneck) di seluruh alur.')]),

'Melihat dari banyak sudut pandang': dict(
  ist=[('Stakeholder analysis', 'Memetakan kepentingan, pengaruh, dan sikap setiap pihak terhadap perubahan.'),
       ('Power–interest grid', 'Matriks pengaruh × kepentingan untuk menentukan cara melibatkan setiap stakeholder.'),
       ('Empathy', 'Memahami masalah dari sisi orang yang mengalaminya, bukan dari asumsi tim proyek.'),
       ('Trade-off', 'Pilihan yang menguntungkan satu pihak sering mengorbankan pihak lain; harus dibuat sadar dan transparan.')],
  cx=[P('Power–interest grid untuk proyek absensi wajah', '''
STAKE = [  # (pihak, pengaruh 1-10, kepentingan 1-10, kekhawatiran utama)
    ("Direktur SDM", 9, 8, "data lembur akurat untuk penggajian"), ("Karyawan pabrik", 3, 9, "privasi data wajah"),
    ("Serikat pekerja", 7, 9, "data dipakai untuk sanksi"), ("Tim TI", 6, 6, "integrasi ke sistem gaji"),
    ("Direktur keuangan", 8, 4, "biaya lisensi"), ("Satpam", 2, 3, "antrean pagi"),
]
def kuadran(p, k):
    if p >= 6 and k >= 6: return "Kelola erat (libatkan dalam keputusan)"
    if p >= 6: return "Jaga kepuasan (laporan berkala)"
    if k >= 6: return "Informasikan (dengar & beri kabar)"
    return "Pantau"
for n, p, k, c in sorted(STAKE, key=lambda x: -(x[1] + x[2])):
    print(f"{n:<18} P{p} K{k}  {kuadran(p, k):<40} | {c}")
''')]),

'Problem solving terstruktur': dict(
  ist=[('Problem statement', 'Rumusan masalah yang spesifik dan terukur: siapa, apa, sejak kapan, seberapa besar dampaknya.'),
       ('Root cause analysis', 'Mencari akar masalah, bukan gejala: 5 Whys, diagram fishbone (Ishikawa).'),
       ('MECE', 'Mutually Exclusive, Collectively Exhaustive: memecah masalah tanpa tumpang tindih dan tanpa celah.'),
       ('Pareto 80/20', 'Sebagian kecil penyebab biasanya menimbulkan sebagian besar dampak.')],
  cx=[P('Pareto keluhan pelanggan untuk memilih masalah yang diselesaikan dulu', '''
KELUHAN = {"paket terlambat": 412, "salah kirim barang": 96, "aplikasi error saat bayar": 288, "refund lama": 174,
           "CS lambat membalas": 61, "barang rusak": 53, "promo tidak berlaku": 38, "lainnya": 22}
total = sum(KELUHAN.values()); kum = 0
for k, n in sorted(KELUHAN.items(), key=lambda x: -x[1]):
    kum += n
    bar = "#" * round(n / 20)
    print(f"{k:<26}{n:>4}  {kum / total:>5.0%}  {bar}")
print("3 penyebab teratas menyumbang", f"{sum(sorted(KELUHAN.values())[-3:]) / total:.0%}", "keluhan -> fokus di sini dulu")
'''),
     T('5 Whys untuk "paket terlambat"', '''
Masalah : 412 keluhan paket terlambat bulan Oktober (naik 3x dari September)
Why 1   : Kenapa terlambat?            -> 70% paket baru diserahkan ke kurir H+2
Why 2   : Kenapa diserahkan H+2?       -> packing gudang menumpuk sore hari
Why 3   : Kenapa menumpuk sore?        -> picking list baru dicetak jam 14.00
Why 4   : Kenapa dicetak jam 14.00?    -> sistem menunggu konfirmasi pembayaran manual dari finance
Why 5   : Kenapa konfirmasi manual?    -> integrasi notifikasi bank (webhook) belum dibuat sejak ganti payment gateway
Akar    : proses verifikasi pembayaran manual. Solusi: aktifkan webhook + picking list per jam.''')]),

'Sebab-akibat, umpan balik, dan efek samping': dict(
  ist=[('Reinforcing loop', 'Umpan balik yang memperkuat dirinya (pertumbuhan atau kemerosotan berantai).'),
       ('Balancing loop', 'Umpan balik yang menahan perubahan menuju keseimbangan.'),
       ('Delay', 'Jeda antara tindakan dan dampaknya; sering membuat orang bereaksi berlebihan.'),
       ('Unintended consequence', 'Efek samping yang tidak direncanakan dari sebuah kebijakan atau sistem.')],
  cx=[P('Efek samping KPI "jumlah tiket ditutup per hari"', '''
# CS dinilai dari tiket ditutup per hari. Agen mulai menutup tiket sebelum masalah benar-benar selesai.
tiket_baru, buka = 200, 0
print("hari  ditutup  dibuka_ulang  kepuasan")
for hari in range(1, 8):
    target_ditutup = 220                                   # tekanan KPI
    ditutup = min(buka + tiket_baru, target_ditutup)
    asal_tutup = max(0, ditutup - 180)                     # di atas 180/hari, sisanya ditutup asal
    dibuka_ulang = int(asal_tutup * 0.7)                   # 70% kembali sebagai keluhan berulang
    buka = buka + tiket_baru - ditutup + dibuka_ulang
    kepuasan = 4.5 - 0.004 * dibuka_ulang * hari
    print(f"{hari:>4}  {ditutup:>7}  {dibuka_ulang:>12}  {kepuasan:>8.2f}")
print("KPI 'ditutup' terlihat bagus, tetapi tiket berulang menumpuk dan kepuasan turun.")
print("Perbaikan: ukur first contact resolution dan CSAT, bukan hanya jumlah tiket ditutup.")
''')]),

'Studi kasus: berpikir utuh dari masalah sampai solusi': dict(
  ist=[('As-is vs to-be', 'Kondisi proses saat ini vs kondisi yang dituju setelah perbaikan.'),
       ('Quick win', 'Perbaikan kecil berdampak cepat untuk membangun kepercayaan sebelum perubahan besar.'),
       ('Pilot', 'Uji coba di lingkup kecil (satu cabang) sebelum diterapkan ke seluruh organisasi.'),
       ('Success metric', 'Ukuran keberhasilan yang disepakati sebelum solusi dibangun.')],
  cx=[P('Membandingkan opsi solusi dengan skor berbobot', '''
# Masalah: stok obat di 12 puskesmas sering kosong; laporan stok dikirim manual tiap akhir bulan
KRITERIA = {"dampak ke stok kosong": 0.35, "biaya": 0.20, "kemudahan dipakai petugas": 0.20,
            "waktu implementasi": 0.15, "keberlanjutan": 0.10}
OPSI = {
    "A. Template spreadsheet bersama": {"dampak ke stok kosong": 2, "biaya": 5, "kemudahan dipakai petugas": 4, "waktu implementasi": 5, "keberlanjutan": 2},
    "B. Aplikasi stok sederhana (web, offline)": {"dampak ke stok kosong": 4, "biaya": 3, "kemudahan dipakai petugas": 4, "waktu implementasi": 3, "keberlanjutan": 4},
    "C. Integrasi penuh ke SIMRS kabupaten": {"dampak ke stok kosong": 5, "biaya": 1, "kemudahan dipakai petugas": 3, "waktu implementasi": 1, "keberlanjutan": 5},
}
for nama, s in sorted(OPSI.items(), key=lambda x: -sum(KRITERIA[k] * x[1][k] for k in KRITERIA)):
    print(f"{sum(KRITERIA[k] * s[k] for k in KRITERIA):.2f}  {nama}")
print("Rencana: quick win A minggu ini, pilot B di 2 puskesmas 6 minggu, C masuk rencana tahun depan.")
''')]),

'TPS, MIS, DSS, dan EIS': dict(
  ist=[('TPS', 'Transaction Processing System: mencatat transaksi harian (kasir, pemesanan, absensi).'),
       ('MIS', 'Management Information System: laporan rutin dari data TPS untuk manajer menengah.'),
       ('DSS', 'Decision Support System: model dan skenario "bagaimana jika" untuk keputusan semi-terstruktur.'),
       ('EIS / executive dashboard', 'Ringkasan indikator kunci dan tren untuk pimpinan puncak.')],
  cx=[P('Dari TPS ke MIS ke DSS dalam satu skrip', '''
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE penjualan (tgl TEXT, produk TEXT, qty INT, harga INT, hpp INT)")
# TPS: transaksi tercatat satu per satu
trx = [("2026-11-1%d" % d, p, q, h, c) for d in range(8) for p, q, h, c in
       [("Roti tawar", 30 + d * 2, 18000, 11000), ("Donat", 50 - d, 7000, 3500), ("Kue ulang tahun", 2 + d % 3, 250000, 150000)]]
db.executemany("INSERT INTO penjualan VALUES (?,?,?,?,?)", trx)

print("MIS: laporan laba kotor per produk")
for p, q, laba in db.execute("SELECT produk, SUM(qty), SUM(qty*(harga-hpp)) FROM penjualan GROUP BY produk ORDER BY 3 DESC"):
    print(f"  {p:<16} {q:>4} unit  laba kotor Rp{laba:>9,}".replace(",", "."))

print("DSS: bagaimana jika harga donat naik 15% dan permintaan turun 8%?")
q, h, c = db.execute("SELECT SUM(qty), AVG(harga), AVG(hpp) FROM penjualan WHERE produk='Donat'").fetchone()
lama = q * (h - c); baru = q * 0.92 * (h * 1.15 - c)
print(f"  laba donat Rp{lama:,.0f} -> Rp{baru:,.0f} ({baru / lama - 1:+.0%})".replace(",", "."))
''')]),

'Sistem informasi fungsional': dict(
  ist=[('Functional IS', 'Sistem per fungsi bisnis: keuangan/akuntansi, SDM (HRIS), pemasaran, produksi, logistik.'),
       ('Silo informasi', 'Data terkurung di sistem masing-masing departemen sehingga sulit digabungkan.'),
       ('Master data', 'Data inti bersama (pelanggan, produk, pegawai) yang harus konsisten di semua sistem.'),
       ('Integration / API', 'Cara sistem bertukar data otomatis, bukan lewat ekspor-impor manual.')],
  cx=[P('Menemukan ketidakkonsistenan master data antar-silo', '''
HRIS    = {"P-101": "Rina Sari", "P-102": "Dodi Pratama", "P-103": "Ayu Lestari", "P-104": "Bagus W."}
PAYROLL = {"P-101": "Rina Sari", "P-102": "Dodi Pratama", "P-104": "Bagus Wicaksono", "P-105": "Fajar (kontrak)"}
ABSEN   = {"P-101": "RINA SARI", "P-103": "Ayu Lestari", "P-104": "Bagus W.", "P-105": "Fajar"}

semua = sorted(set(HRIS) | set(PAYROLL) | set(ABSEN))
print(f"{'ID':<6}{'HRIS':<16}{'Payroll':<18}{'Absensi':<14}catatan")
for i in semua:
    nilai = [s.get(i, "-") for s in (HRIS, PAYROLL, ABSEN)]
    unik = {n.lower() for n in nilai if n != "-"}
    cat = "tidak ada di HRIS (digaji tanpa data pegawai!)" if i not in HRIS else ("nama berbeda" if len(unik) > 1 else ("tidak tercatat di sistem lain" if "-" in nilai else ""))
    print(f"{i:<6}{nilai[0]:<16}{nilai[1]:<18}{nilai[2]:<14}{cat}")
''', 'Solusinya: HRIS menjadi sumber master data pegawai, dan sistem lain mengambil data lewat integrasi, bukan mengetik ulang.')]),

'ERP, CRM, dan SCM': dict(
  ist=[('ERP', 'Enterprise Resource Planning: satu sistem terpadu untuk keuangan, pembelian, persediaan, produksi, SDM (SAP, Oracle, Odoo, Microsoft Dynamics).'),
       ('CRM', 'Customer Relationship Management: mengelola prospek, penjualan, dan layanan pelanggan (Salesforce, HubSpot, Qontak).'),
       ('SCM', 'Supply Chain Management: perencanaan permintaan, pengadaan, gudang, distribusi.'),
       ('Fit-gap analysis', 'Membandingkan proses bisnis dengan fitur standar paket; gap diselesaikan dengan konfigurasi, perubahan proses, atau kustomisasi.')],
  cx=[P('Fit-gap sederhana sebelum memilih ERP', '''
KEBUTUHAN = [  # (proses, prioritas, status di paket standar: fit / config / gap)
    ("Pembelian dengan approval 3 tingkat", "wajib", "config"), ("Faktur pajak e-Faktur DJP", "wajib", "fit"),
    ("Stok multi-gudang + nomor batch", "wajib", "fit"), ("Komisi sales berjenjang khas perusahaan", "penting", "gap"),
    ("Integrasi marketplace (Tokopedia, Shopee)", "penting", "gap"), ("Laporan konsolidasi 3 PT", "wajib", "config"),
    ("Cetak label rak custom", "opsional", "gap"),
]
from collections import Counter
print(Counter(s for _, _, s in KEBUTUHAN))
for p, prio, s in KEBUTUHAN:
    if s == "gap":
        saran = "kustomisasi/add-on (hitung biaya)" if prio != "opsional" else "ubah proses atau tunda"
        print(f"GAP [{prio:<8}] {p:<42} -> {saran}")
fit = sum(s != "gap" for *_, s in KEBUTUHAN) / len(KEBUTUHAN)
print(f"cakupan standar + konfigurasi: {fit:.0%} (prinsip: adopsi proses standar, kustomisasi seminimal mungkin)")
''')]),

'Database dan DBMS': dict(
  ist=[('DBMS', 'Perangkat lunak pengelola database: PostgreSQL, MySQL, SQL Server, Oracle.'),
       ('Relational vs NoSQL', 'Tabel berelasi dengan SQL vs model dokumen/key-value/graf untuk kebutuhan tertentu.'),
       ('Redundansi & anomali', 'Data ganda menyebabkan anomali update (ubah di satu tempat, lupa di tempat lain).'),
       ('Backup & hak akses', 'Tanggung jawab dasar pengelola data: salinan cadangan teruji dan akses sesuai peran.')],
  cx=[Q('Anomali update di spreadsheet vs tabel yang dinormalisasi', '''
-- Spreadsheet: alamat pelanggan diulang di setiap pesanan
SELECT * FROM pesanan_flat;
UPDATE pesanan_flat SET alamat = 'Jl. Gatot Subroto 9' WHERE no = 1;   -- pelanggan pindah, hanya 1 baris diubah
SELECT pelanggan, COUNT(DISTINCT alamat) AS versi_alamat FROM pesanan_flat GROUP BY pelanggan;

-- Ternormalisasi: alamat hanya di satu tempat
UPDATE pelanggan SET alamat = 'Jl. Gatot Subroto 9' WHERE nama = 'CV Maju';
SELECT p.no, c.nama, c.alamat FROM pesanan p JOIN pelanggan c ON c.id = p.pelanggan_id;''',
     'Inilah alasan sistem informasi memakai database relasional, bukan satu sheet besar.',
     setup='''CREATE TABLE pesanan_flat (no INT, pelanggan TEXT, alamat TEXT, total INT);
INSERT INTO pesanan_flat VALUES (1,'CV Maju','Jl. Sudirman 1',500000),(2,'CV Maju','Jl. Sudirman 1',750000),(3,'CV Maju','Jl. Sudirman 1',120000);
CREATE TABLE pelanggan (id INT PRIMARY KEY, nama TEXT, alamat TEXT);
CREATE TABLE pesanan (no INT, pelanggan_id INT, total INT);
INSERT INTO pelanggan VALUES (1,'CV Maju','Jl. Sudirman 1');
INSERT INTO pesanan VALUES (1,1,500000),(2,1,750000),(3,1,120000);''')]),

'Merancang tabel dan relasi (ERD)': dict(
  ist=[('Entity, attribute, relationship', 'Benda yang dicatat, sifatnya, dan hubungannya; dasar ERD.'),
       ('Cardinality', 'Jumlah hubungan: one-to-one, one-to-many, many-to-many (butuh tabel penghubung).'),
       ('Primary key & foreign key', 'Pengenal unik baris dan penghubung ke tabel lain.'),
       ('Normalisasi (1NF-3NF)', 'Menyusun tabel agar tidak ada data berulang dan setiap kolom bergantung pada kuncinya.')],
  cx=[Q('ERD sistem akademik: mahasiswa–mata kuliah (many-to-many)', '''
CREATE TABLE mahasiswa (nim TEXT PRIMARY KEY, nama TEXT NOT NULL, prodi TEXT NOT NULL);
CREATE TABLE mata_kuliah (kode TEXT PRIMARY KEY, nama TEXT NOT NULL, sks INT NOT NULL CHECK (sks BETWEEN 1 AND 6));
CREATE TABLE krs (                                   -- tabel penghubung
  nim TEXT REFERENCES mahasiswa(nim), kode TEXT REFERENCES mata_kuliah(kode),
  semester TEXT, nilai TEXT, PRIMARY KEY (nim, kode, semester));
INSERT INTO mahasiswa VALUES ('2301001','Nadia','SI'),('2301002','Yoga','SI');
INSERT INTO mata_kuliah VALUES ('SI201','Basis Data',3),('SI202','Analisis Sistem',3),('SI203','Statistika',2);
INSERT INTO krs VALUES ('2301001','SI201','2026-1','A'),('2301001','SI202','2026-1','B'),
                       ('2301002','SI201','2026-1','B'),('2301002','SI203','2026-1','A');
SELECT m.nama, SUM(k.sks) AS total_sks,
       ROUND(SUM(k.sks * CASE r.nilai WHEN 'A' THEN 4 WHEN 'B' THEN 3 WHEN 'C' THEN 2 ELSE 0 END) * 1.0 / SUM(k.sks), 2) AS ips
FROM krs r JOIN mahasiswa m USING (nim) JOIN mata_kuliah k USING (kode)
GROUP BY m.nama;''')]),

'Data warehouse, BI, dan kualitas data': dict(
  ist=[('Data warehouse', 'Gudang data terpadu untuk analisis, terpisah dari database transaksi (BigQuery, Snowflake, Redshift).'),
       ('ETL / ELT', 'Extract, Transform, Load: memindahkan dan merapikan data dari sumber ke warehouse.'),
       ('Dimensi kualitas data', 'Kelengkapan, keakuratan, konsistensi, ketepatan waktu, keunikan, validitas.'),
       ('Data owner / steward', 'Pemilik bisnis yang bertanggung jawab atas definisi dan kualitas data tertentu.')],
  cx=[P('Skor kualitas data pelanggan sebelum masuk warehouse', '''
import re
DATA = [
    {"id": 1, "nama": "Rina", "hp": "081234567890", "email": "rina@contoh.id", "kota": "Medan"},
    {"id": 2, "nama": "", "hp": "0812", "email": "dodi@contoh", "kota": "Bandung"},
    {"id": 3, "nama": "Ayu", "hp": "+6281398765432", "email": "ayu@contoh.id", "kota": "surabaya"},
    {"id": 3, "nama": "Ayu L.", "hp": "+6281398765432", "email": "ayu@contoh.id", "kota": "Surabaya"},
    {"id": 5, "nama": "Bagus", "hp": None, "email": "bagus@contoh.id", "kota": "Makasar"},
]
KOTA = {"Medan", "Bandung", "Surabaya", "Makassar"}
cek = {
    "kelengkapan (nama & hp terisi)": [bool(r["nama"]) and bool(r["hp"]) for r in DATA],
    "validitas hp (format Indonesia)": [bool(r["hp"]) and bool(re.fullmatch(r"(\\+62|0)8\\d{8,11}", r["hp"])) for r in DATA],
    "validitas email": [bool(re.fullmatch(r"[^@]+@[^@]+\\.[a-z]{2,}", r["email"])) for r in DATA],
    "konsistensi kota (daftar baku)": [r["kota"] in KOTA for r in DATA],
    "keunikan id": [[x["id"] for x in DATA].count(r["id"]) == 1 for r in DATA],
}
for dim, hasil in cek.items():
    print(f"{dim:<34} {sum(hasil)}/{len(hasil)} = {sum(hasil) / len(hasil):.0%}")
''')]),

'Siklus hidup pengembangan sistem (SDLC)': dict(
  ist=[('SDLC', 'Tahapan membangun sistem: perencanaan, analisis, desain, implementasi, pengujian, deployment, pemeliharaan.'),
       ('Waterfall vs Agile', 'Tahap berurutan dengan dokumen lengkap vs iterasi pendek (sprint) dengan umpan balik berkala.'),
       ('UAT', 'User Acceptance Testing: pengguna bisnis menguji apakah sistem memenuhi kebutuhannya sebelum go-live.'),
       ('Go-live & hypercare', 'Peluncuran sistem dan masa pendampingan intensif beberapa minggu setelahnya.')],
  cx=[P('Membandingkan risiko waterfall dan agile dengan simulasi umpan balik', '''
# Kebutuhan berubah 8% per bulan. Waterfall baru menunjukkan hasil di bulan 9; agile setiap bulan.
def kesesuaian(bulan_umpan_balik, durasi=9, perubahan=0.08):
    sesuai = 1.0; log = []
    for b in range(1, durasi + 1):
        sesuai *= (1 - perubahan)                      # kebutuhan bergeser
        if b in bulan_umpan_balik: sesuai = min(1.0, sesuai + 0.85 * (1 - sesuai))  # koreksi setelah demo
        log.append(sesuai)
    return log
w = kesesuaian({9}); a = kesesuaian(set(range(1, 10)))
print("bulan  waterfall  agile")
for b in (1, 3, 6, 8, 9): print(f"{b:>5}  {w[b-1]:>9.0%}  {a[b-1]:>5.0%}")
print("Waterfall tetap cocok jika kebutuhan stabil dan diatur regulasi (misalnya sistem pelaporan pajak).")
''')]),

'Menggali kebutuhan dan memodelkan proses': dict(
  ist=[('Requirements elicitation', 'Menggali kebutuhan lewat wawancara, observasi, workshop, kuesioner, dan analisis dokumen.'),
       ('Functional vs non-functional', 'Apa yang dilakukan sistem vs kualitasnya (kecepatan, keamanan, ketersediaan).'),
       ('User story & acceptance criteria', '"Sebagai <peran>, saya ingin <aksi>, agar <manfaat>" + syarat terukur.'),
       ('BPMN', 'Business Process Model and Notation: standar diagram proses dengan swimlane, event, gateway.'),
       ('MoSCoW', 'Prioritas Must, Should, Could, Won\'t (kali ini).')],
  cx=[T('User story, acceptance criteria, dan prioritas MoSCoW', '''
US-07 [Must]  Sebagai staf gudang, saya ingin memindai barcode saat barang masuk,
              agar stok bertambah otomatis tanpa input manual.
  AC1: Pemindaian menambah stok sesuai qty di surat jalan dalam < 2 detik
  AC2: Barcode tidak dikenal menampilkan pesan "Barang belum terdaftar" + tombol daftar
  AC3: Bekerja offline dan sinkron saat koneksi kembali
US-08 [Should] Sebagai kepala gudang, saya ingin notifikasi stok di bawah minimum,
               agar bisa membuat PO sebelum barang habis.
US-09 [Could]  Sebagai manajer, saya ingin grafik perputaran stok per kategori.
US-10 [Won't]  Integrasi RFID (ditunda ke tahun depan, biaya perangkat).

Non-fungsional: tersedia 99,5% jam kerja, data tersimpan di pusat data Indonesia, akses per peran.'''),
     P('Model proses as-is vs to-be: menghitung waktu siklus', '''
AS_IS = [("Sales tulis order di kertas", 10), ("Admin ketik ulang ke Excel", 15), ("Tunggu approval via WA", 120),
         ("Gudang cek stok manual", 30), ("Finance buat faktur", 20)]
TO_BE = [("Sales input order di aplikasi", 5), ("Approval otomatis jika < limit kredit", 1),
         ("Stok tercek otomatis", 0), ("Faktur terbit otomatis", 1)]
for nama, langkah in (("AS-IS", AS_IS), ("TO-BE", TO_BE)):
    print(f"{nama}: {len(langkah)} langkah, {sum(m for _, m in langkah)} menit")
    for l, m in langkah: print(f"   {m:>4} mnt  {l}")
''')]),

'Studi kelayakan dan biaya-manfaat': dict(
  ist=[('Feasibility study', 'Kelayakan teknis, ekonomi, operasional, hukum, dan jadwal sebelum proyek disetujui.'),
       ('NPV', 'Net Present Value: nilai sekarang arus kas masa depan dikurangi investasi; positif = layak secara finansial.'),
       ('Payback period', 'Berapa lama investasi kembali dari manfaat bersih.'),
       ('ROI', 'Return on Investment: (manfaat − biaya) / biaya.'),
       ('Tangible vs intangible benefit', 'Manfaat terukur uang (hemat biaya) vs sulit diukur (kepuasan, reputasi).')],
  cx=[P('Analisis biaya-manfaat sistem gudang 5 tahun', '''
INVESTASI = 450_000_000                     # lisensi, perangkat, implementasi, pelatihan (tahun 0)
BIAYA_TAHUNAN = 60_000_000                  # langganan, dukungan, cloud
MANFAAT = [180_000_000, 260_000_000, 280_000_000, 290_000_000, 290_000_000]   # hemat stok mati, lembur, salah kirim
r = 0.10                                    # tingkat diskonto (biaya modal)

npv, kumulatif, payback = -INVESTASI, -INVESTASI, None
print("thn   arus bersih     nilai kini   kumulatif")
for t, m in enumerate(MANFAAT, 1):
    bersih = m - BIAYA_TAHUNAN
    pv = bersih / (1 + r) ** t
    npv += pv
    sebelum = kumulatif; kumulatif += bersih
    if payback is None and kumulatif >= 0: payback = t - 1 + (-sebelum) / bersih
    print(f"{t:>3} {bersih:>14,} {pv:>14,.0f} {kumulatif:>13,}".replace(",", "."))
total_biaya = INVESTASI + BIAYA_TAHUNAN * 5
print(f"NPV {npv:,.0f} | payback {payback:.1f} tahun | ROI 5 thn {(sum(MANFAAT) - total_biaya) / total_biaya:.0%}".replace(",", "."))
''')]),

'Jaringan dan cloud computing': dict(
  ist=[('IaaS / PaaS / SaaS', 'Sewa infrastruktur (server) / platform (database terkelola) / aplikasi jadi (Google Workspace).'),
       ('Shared responsibility model', 'Pembagian tanggung jawab keamanan antara penyedia cloud dan pelanggan.'),
       ('Region & data residency', 'Lokasi pusat data; regulasi tertentu mewajibkan data disimpan di Indonesia.'),
       ('SLA ketersediaan', 'Janji uptime penyedia, misalnya 99,9% per bulan, beserta kompensasinya.')],
  cx=[P('Membandingkan TCO server sendiri vs cloud selama 3 tahun', '''
ON_PREM = {"server & storage (thn 0)": 280e6, "UPS, rak, AC (thn 0)": 60e6, "listrik/thn": 36e6,
           "admin 0,5 FTE/thn": 72e6, "lisensi OS & backup/thn": 18e6, "penggantian disk/thn": 6e6}
CLOUD = {"VM + database terkelola/thn": 132e6, "backup & egress/thn": 14e6, "admin 0,2 FTE/thn": 29e6, "migrasi (thn 0)": 40e6}
def tco(item, tahun=3):
    return sum(v if "(thn 0)" in k else v * tahun for k, v in item.items())
for nama, it in (("On-premise", ON_PREM), ("Cloud", CLOUD)):
    print(f"{nama:<11} TCO 3 tahun Rp{tco(it) / 1e6:,.0f} juta".replace(",", "."))
print("Catatan non-biaya: cloud = skala cepat & DR lebih mudah; on-prem = kendali penuh, cocok jika regulasi ketat & beban stabil.")
''')]),

'Keamanan informasi': dict(
  ist=[('CIA triad', 'Confidentiality, Integrity, Availability: tiga tujuan keamanan informasi.'),
       ('Risk = likelihood × impact', 'Cara menilai risiko untuk menentukan prioritas pengendalian.'),
       ('ISO/IEC 27001', 'Standar sistem manajemen keamanan informasi (SMKI) yang banyak diminta mitra dan regulator.'),
       ('MFA & least privilege', 'Autentikasi berlapis dan hak akses seminimal mungkin; dua kontrol paling efektif.'),
       ('Phishing', 'Penipuan lewat pesan palsu untuk mencuri kredensial; penyebab utama insiden.')],
  cx=[P('Register risiko keamanan dengan matriks 5×5', '''
RISIKO = [  # (risiko, kemungkinan 1-5, dampak 1-5, kontrol yang ada)
    ("Akun email staf dibobol lewat phishing", 4, 4, "pelatihan setahun sekali"),
    ("Ransomware di PC keuangan", 3, 5, "antivirus"),
    ("Laptop berisi data pelanggan hilang", 3, 4, "tidak ada enkripsi"),
    ("Server down karena listrik", 2, 3, "UPS 15 menit"),
    ("Mantan pegawai masih punya akses", 4, 3, "tidak ada offboarding checklist"),
]
def level(s): return "TINGGI" if s >= 15 else "SEDANG" if s >= 8 else "RENDAH"
for r, l, d, k in sorted(RISIKO, key=lambda x: -x[1] * x[2]):
    print(f"{l * d:>3} {level(l * d):<7} {r:<40} kontrol: {k}")
print("Tindakan prioritas: MFA semua akun, backup offline teruji, enkripsi disk laptop, checklist offboarding.")
''')]),

'Perlindungan data pribadi dan kelangsungan bisnis': dict(
  ist=[('UU PDP (UU 27/2022)', 'Undang-undang Pelindungan Data Pribadi; berlaku penuh sejak Oktober 2024, termasuk sanksi.'),
       ('Data controller / processor', 'Pengendali menentukan tujuan pemrosesan; prosesor memproses atas nama pengendali (misalnya vendor cloud).'),
       ('BCP / DRP', 'Business Continuity Plan dan Disaster Recovery Plan: rencana tetap beroperasi dan pulih saat bencana.'),
       ('RPO / RTO', 'Batas data yang boleh hilang dan waktu pulih yang ditargetkan per sistem.'),
       ('Data breach notification', 'Kewajiban memberi tahu subjek data dan lembaga dalam 3×24 jam setelah kebocoran diketahui.')],
  cx=[P('Business impact analysis: menentukan RTO/RPO per sistem', '''
SISTEM = [  # (sistem, kerugian per jam downtime Rp juta, data per jam yang tak bisa dibuat ulang, wajib regulasi)
    ("Kasir & pembayaran", 85, "tinggi", True), ("Aplikasi gudang", 30, "sedang", False),
    ("Email & kolaborasi", 8, "rendah", False), ("Akuntansi", 5, "tinggi", True), ("Website profil", 1, "rendah", False),
]
def target(rugi, data, regulasi):
    rto = "15 menit" if rugi >= 50 else "4 jam" if rugi >= 10 else "24 jam"
    rpo = "0 (replikasi)" if data == "tinggi" and (rugi >= 50 or regulasi) else "1 jam" if data != "rendah" else "24 jam"
    return rto, rpo
print(f"{'sistem':<20}{'rugi/jam':>9}  {'RTO':<10}{'RPO':<14}")
for s, rugi, data, reg in SISTEM:
    rto, rpo = target(rugi, data, reg)
    print(f"{s:<20}{rugi:>7} jt  {rto:<10}{rpo:<14}")
''')]),

'SI untuk keunggulan bersaing': dict(
  ist=[('Porter five forces', 'Lima kekuatan persaingan: pesaing, pendatang baru, substitusi, pemasok, pembeli.'),
       ('Value chain', 'Rangkaian aktivitas yang menciptakan nilai; SI dapat memperkuat setiap mata rantai.'),
       ('Network effect', 'Nilai layanan naik seiring jumlah pengguna (marketplace, aplikasi pembayaran).'),
       ('Switching cost', 'Biaya/usaha pelanggan untuk pindah ke pesaing; SI yang terintegrasi menaikkannya.')],
  cx=[P('Efek jaringan pada marketplace dua sisi', '''
# Penjual tertarik jika banyak pembeli, pembeli tertarik jika banyak penjual
def simulasi(penjual, pembeli, bulan=6, subsidi_awal=False):
    for b in range(1, bulan + 1):
        tarik_penjual = 0.00004 * pembeli * penjual / (1 + penjual / 5000)
        tarik_pembeli = 0.0025 * penjual * pembeli / (1 + pembeli / 200000)
        if subsidi_awal and b <= 2: tarik_pembeli += 3000          # promo gratis ongkir di awal
        penjual = int(penjual * 0.97 + tarik_penjual); pembeli = int(pembeli * 0.95 + tarik_pembeli)
    return penjual, pembeli
print("tanpa subsidi      :", simulasi(300, 2000))
print("dengan subsidi awal:", simulasi(300, 2000, subsidi_awal=True))
print("Platform yang lebih dulu mencapai massa kritis cenderung terus tumbuh, pesaing kecil sulit mengejar.")
''')]),

'Transformasi digital, KPI, dan balanced scorecard': dict(
  ist=[('Digital transformation', 'Mengubah model bisnis dan cara kerja dengan teknologi, bukan sekadar digitalisasi formulir.'),
       ('Balanced scorecard', 'Kerangka KPI empat perspektif: keuangan, pelanggan, proses internal, pembelajaran & pertumbuhan.'),
       ('OKR', 'Objectives and Key Results: tujuan ambisius dengan hasil kunci terukur per kuartal.'),
       ('Leading vs lagging KPI', 'Indikator pendorong yang bisa dikendalikan vs indikator hasil akhir.')],
  cx=[P('Balanced scorecard dengan capaian dan status', '''
BSC = {
    "Keuangan":      [("Pendapatan digital (Rp M)", 12.0, 10.4, "naik"), ("Biaya per transaksi (Rp)", 2500, 2310, "turun")],
    "Pelanggan":     [("NPS", 45, 38, "naik"), ("Pelanggan aktif aplikasi (ribu)", 120, 131, "naik")],
    "Proses":        [("Waktu proses klaim (hari)", 3, 4.5, "turun"), ("Transaksi tanpa sentuhan manual", 0.80, 0.72, "naik")],
    "Pembelajaran":  [("Pegawai lulus pelatihan data (%)", 0.60, 0.65, "naik")],
}
for persp, kpi in BSC.items():
    print(persp)
    for nama, target, aktual, arah in kpi:
        capai = aktual / target if arah == "naik" else target / aktual
        status = "hijau" if capai >= 1 else "kuning" if capai >= 0.9 else "merah"
        print(f"  {nama:<36} target {target:<6} aktual {aktual:<6} {capai:>5.0%} {status}")
''')]),

'Tata kelola TI dan manajemen proyek SI': dict(
  ist=[('COBIT 2019', 'Kerangka tata kelola dan manajemen TI dari ISACA; dipakai auditor dan regulator perbankan.'),
       ('ITIL 4', 'Praktik terbaik manajemen layanan TI: incident, problem, change, service desk.'),
       ('Steering committee', 'Forum pimpinan yang memutuskan prioritas, anggaran, dan isu besar proyek SI.'),
       ('Earned Value (EV, PV, AC)', 'Mengukur kemajuan proyek dari sisi jadwal dan biaya secara objektif.'),
       ('RACI', 'Responsible, Accountable, Consulted, Informed: siapa berperan apa di setiap aktivitas.')],
  cx=[P('Earned value: apakah proyek SI terlambat dan boros?', '''
BAC = 1_200_000_000           # anggaran total proyek implementasi
PV = 600_000_000              # nilai pekerjaan yang direncanakan selesai sampai bulan ini
EV = 480_000_000              # nilai pekerjaan yang benar-benar selesai (40% lingkup)
AC = 560_000_000              # biaya aktual yang sudah keluar
SPI, CPI = EV / PV, EV / AC
EAC = BAC / CPI
print(f"SPI {SPI:.2f} -> {'terlambat' if SPI < 1 else 'sesuai/lebih cepat'} dari jadwal")
print(f"CPI {CPI:.2f} -> {'boros' if CPI < 1 else 'hemat'}: tiap Rp1 menghasilkan pekerjaan senilai Rp{CPI:.2f}")
rp = lambda x: f"{x / 1e6:,.0f}".replace(",", ".")
print(f"Perkiraan biaya akhir (EAC) Rp{rp(EAC)} juta, melebihi anggaran Rp{rp(EAC - BAC)} juta")
'''),
     T('Matriks RACI implementasi ERP', '''
Aktivitas                   Sponsor  PM   BA   Vendor  Key user  TI
Persetujuan lingkup          A       R    C    C       C         I
Desain proses to-be          I       A    R    C       R         C
Konfigurasi sistem           I       A    C    R       C         C
Migrasi data                 I       A    C    R       R         R
UAT                          I       A    C    C       R         I
Keputusan go-live            A       R    C    C       C         C''')]),

'Di perusahaan: distributor dengan ERP': dict(
  ist=[('Order-to-cash (O2C)', 'Proses dari pesanan pelanggan sampai uang diterima.'),
       ('Procure-to-pay (P2P)', 'Proses dari permintaan pembelian sampai pembayaran ke pemasok.'),
       ('Three-way match', 'Pencocokan PO, penerimaan barang, dan faktur pemasok sebelum dibayar.'),
       ('Days Sales Outstanding (DSO)', 'Rata-rata hari piutang tertagih; indikator kesehatan arus kas.')],
  cx=[P('Three-way match otomatis sebelum pembayaran pemasok', '''
PO      = {"PO-881": {"item": "Minyak goreng 2L", "qty": 500, "harga": 31000}, "PO-882": {"item": "Gula 1kg", "qty": 800, "harga": 16500}}
TERIMA  = {"PO-881": 500, "PO-882": 760}                          # gudang hanya menerima 760 gula
FAKTUR  = {"PO-881": {"qty": 500, "harga": 31000}, "PO-882": {"qty": 800, "harga": 16800}}
for po, p in PO.items():
    f, t = FAKTUR[po], TERIMA[po]
    masalah = []
    if f["qty"] != t: masalah.append(f"faktur {f['qty']} unit, diterima {t}")
    if f["harga"] != p["harga"]: masalah.append(f"harga faktur {f['harga']} != PO {p['harga']}")
    bayar = min(f["qty"], t) * p["harga"]
    rp = f"{bayar:,}".replace(",", ".")
    print(f"{po} {p['item']:<18} {'COCOK -> bayar' if not masalah else 'TAHAN: ' + '; '.join(masalah)}  Rp{rp}")
''')]),

'Di startup: dari spreadsheet ke sistem yang tumbuh': dict(
  ist=[('Product-market fit', 'Titik ketika produk jelas dibutuhkan pasar; sebelum itu sistem sebaiknya ringan dan mudah diubah.'),
       ('No-code / low-code', 'Membangun aplikasi tanpa/dengan sedikit kode (AppSheet, Glide, Airtable, Retool).'),
       ('Technical debt', 'Jalan pintas teknis yang mempercepat sekarang tetapi menambah biaya perubahan nanti.'),
       ('Scalability trigger', 'Tanda sistem harus ditingkatkan: volume transaksi, jumlah pengguna, kesalahan manual, kebutuhan audit.')],
  cx=[P('Kapan spreadsheet harus diganti? Pantau pemicu skala', '''
BULAN = ["Jan", "Mar", "Mei", "Jul", "Sep", "Nov"]
PESANAN = [180, 420, 950, 1800, 3100, 5200]
ADMIN = [1, 1, 2, 3, 4, 6]
SALAH_INPUT = [0.004, 0.006, 0.011, 0.018, 0.024, 0.031]
for b, p, a, s in zip(BULAN, PESANAN, ADMIN, SALAH_INPUT):
    pemicu = []
    if p > 1500: pemicu.append("volume")
    if a > 3: pemicu.append("banyak editor bersamaan")
    if s > 0.02: pemicu.append(f"salah input {s:.1%} (~{int(p * s)} pesanan)")
    print(f"{b}: {p:>5} pesanan, {a} admin  {'-> ' + ', '.join(pemicu) if pemicu else 'spreadsheet masih memadai'}")
''')]),

'Di sekolah: sistem informasi akademik terpadu': dict(
  ist=[('SIAKAD', 'Sistem informasi akademik: data siswa, jadwal, nilai, rapor, presensi.'),
       ('Dapodik', 'Data Pokok Pendidikan Kemendikdasmen; sistem sekolah harus sinkron dengannya.'),
       ('Role-based access', 'Hak akses berdasarkan peran: guru, wali kelas, kepala sekolah, orang tua, siswa.'),
       ('Early warning system', 'Deteksi dini siswa berisiko (kehadiran rendah, nilai turun) untuk intervensi.')],
  cx=[P('Early warning: siswa yang perlu perhatian wali kelas', '''
SISWA = [  # (nama, kehadiran 30 hari, rata-rata nilai bulan lalu, bulan ini, tugas terlambat)
    ("Andi", 0.97, 82, 84, 0), ("Bella", 0.78, 75, 64, 4), ("Citra", 0.93, 88, 87, 1),
    ("Dimas", 0.85, 70, 61, 2), ("Eka", 0.66, 72, 70, 5), ("Fani", 0.95, 91, 90, 0),
]
for n, hadir, lalu, kini, telat in SISWA:
    tanda = []
    if hadir < 0.85: tanda.append(f"hadir {hadir:.0%}")
    if kini - lalu <= -8: tanda.append(f"nilai turun {lalu}->{kini}")
    if telat >= 3: tanda.append(f"{telat} tugas terlambat")
    if len(tanda) >= 2: print(f"PRIORITAS {n:<6} " + "; ".join(tanda) + " -> hubungi orang tua & BK")
    elif tanda: print(f"PANTAU    {n:<6} " + "; ".join(tanda))
''')]),

'Di organisasi: koperasi, yayasan, dan organisasi mahasiswa': dict(
  ist=[('Akuntabilitas', 'Kewajiban organisasi melaporkan penggunaan dana secara terbuka kepada anggota/donatur.'),
       ('SHU', 'Sisa Hasil Usaha koperasi yang dibagikan sesuai jasa simpanan dan jasa transaksi anggota.'),
       ('Laporan donasi', 'Rincian sumber dan penggunaan dana yayasan per program.'),
       ('Digital record keeping', 'Arsip digital terstruktur menggantikan buku besar dan nota yang mudah hilang.')],
  cx=[P('Menghitung pembagian SHU koperasi berdasarkan jasa anggota', '''
SHU = 48_000_000
PORSI = {"jasa simpanan": 0.40, "jasa transaksi": 0.30}       # sisanya cadangan, pengurus, pendidikan
ANGGOTA = {"Bu Siti": (5_200_000, 18_000_000), "Pak Joko": (12_000_000, 6_500_000),
           "Mas Rudi": (2_500_000, 31_000_000), "Bu Ani": (8_300_000, 12_400_000)}   # (simpanan, belanja di koperasi)
ts = sum(s for s, _ in ANGGOTA.values()); tt = sum(t for _, t in ANGGOTA.values())
print(f"{'anggota':<9}{'jasa simpanan':>15}{'jasa transaksi':>16}{'total':>13}")
for n, (s, t) in ANGGOTA.items():
    js = SHU * PORSI["jasa simpanan"] * s / ts; jt = SHU * PORSI["jasa transaksi"] * t / tt
    print(f"{n:<9}{js:>15,.0f}{jt:>16,.0f}{js + jt:>13,.0f}".replace(",", "."))
''')]),

'AI, analitik, dan otomatisasi': dict(
  ist=[('Descriptive → predictive → prescriptive', 'Apa yang terjadi, apa yang akan terjadi, apa yang sebaiknya dilakukan.'),
       ('RPA', 'Robotic Process Automation: bot meniru langkah klik manusia untuk tugas berulang di aplikasi lama.'),
       ('Generative AI', 'Model yang membuat teks/gambar; dipakai untuk ringkasan, draf, asisten internal, dengan pengawasan manusia.'),
       ('Human-in-the-loop', 'Keputusan berisiko tetap ditinjau manusia; AI memberi rekomendasi dan alasan.')],
  cx=[P('Memilih proses yang layak diotomasi', '''
PROSES = [  # (proses, frekuensi/bulan, menit per kali, % berbasis aturan jelas, risiko kesalahan)
    ("Rekonsiliasi mutasi bank", 600, 6, 0.95, "sedang"), ("Input faktur pemasok dari PDF", 1400, 4, 0.80, "sedang"),
    ("Menjawab email keluhan", 900, 7, 0.40, "tinggi"), ("Rekap absensi ke payroll", 4, 240, 0.98, "tinggi"),
    ("Negosiasi harga dengan pemasok", 30, 90, 0.10, "tinggi"),
]
for p, f, m, aturan, risiko in sorted(PROSES, key=lambda x: -(x[1] * x[2] * x[3])):
    jam = f * m / 60
    cocok = "RPA/otomasi penuh" if aturan >= 0.9 else "AI + review manusia" if aturan >= 0.4 else "tetap manusia"
    print(f"{p:<32} {jam:>5.0f} jam/bln  aturan {aturan:.0%}  -> {cocok}")
''')]),

'E-business, e-commerce, dan e-government': dict(
  ist=[('B2B / B2C / C2C / G2C', 'Model transaksi elektronik antarbisnis, bisnis-konsumen, antarkonsumen, pemerintah-warga.'),
       ('Omnichannel', 'Pengalaman belanja terpadu di toko fisik, web, aplikasi, dan marketplace.'),
       ('SPBE', 'Sistem Pemerintahan Berbasis Elektronik: kerangka transformasi digital instansi pemerintah Indonesia.'),
       ('Conversion funnel', 'Tahapan pengunjung sampai membeli; tiap tahap punya tingkat konversi yang bisa diperbaiki.')],
  cx=[P('Funnel e-commerce dan tahap dengan kebocoran terbesar', '''
FUNNEL = [("Kunjungan", 120000), ("Lihat produk", 54000), ("Tambah ke keranjang", 9700),
          ("Mulai checkout", 5100), ("Bayar", 2950)]
for (a, na), (b, nb) in zip(FUNNEL, FUNNEL[1:]):
    print(f"{a:<20} -> {b:<20} {nb / na:>6.1%}  hilang {na - nb:>6,}".replace(",", "."))
print(f"konversi total {FUNNEL[-1][1] / FUNNEL[0][1]:.2%}")
''')]),

'Etika SI dan karier di bidang sistem informasi': dict(
  ist=[('Etika informasi', 'Privasi, akurasi, kepemilikan, dan aksesibilitas informasi (kerangka PAPA dari Mason).'),
       ('Algorithmic bias', 'Sistem otomatis yang merugikan kelompok tertentu karena data atau desain yang bias.'),
       ('Digital divide', 'Kesenjangan akses dan kemampuan digital antarwilayah dan kelompok masyarakat.'),
       ('Jalur karier SI', 'Business/system analyst, IT project manager, ERP consultant, IT auditor, data analyst, product manager.')],
  cx=[P('Memeriksa bias sederhana pada aturan persetujuan kredit otomatis', '''
PEMOHON = [  # (wilayah, penghasilan juta, punya slip gaji resmi, lunas tepat waktu sebelumnya)
    ("kota", 6, True, True), ("kota", 4, True, True), ("kota", 3, True, False), ("kota", 8, True, True),
    ("desa", 5, False, True), ("desa", 4, False, True), ("desa", 3, False, True), ("desa", 7, True, True),
]
aturan_lama = lambda w, g, slip, lunas: slip and g >= 4
aturan_baru = lambda w, g, slip, lunas: g >= 4 and (slip or lunas)      # riwayat bayar jadi alternatif bukti
for nama, f in (("aturan lama", aturan_lama), ("aturan baru", aturan_baru)):
    for w in ("kota", "desa"):
        grup = [p for p in PEMOHON if p[0] == w]
        print(f"{nama}: {w:<5} disetujui {sum(f(*p) for p in grup)}/{len(grup)}")
print("Syarat slip gaji resmi menyingkirkan pekerja informal di desa yang riwayat bayarnya baik.")
''')]),

'MSI dan UX Designer: siapa mengerjakan apa': dict(
  ist=[('Product trio', 'Product manager, designer, dan engineer lead yang memutuskan bersama apa yang dibangun.'),
       ('Business requirement vs user need', 'Kebutuhan organisasi (aturan, laporan, kontrol) vs kebutuhan pengguna (mudah, cepat, jelas).'),
       ('Design handoff', 'Penyerahan desain ke developer lengkap dengan state, spesifikasi, dan acceptance criteria.'),
       ('Definition of Ready', 'Syarat sebuah item siap dikerjakan: kebutuhan jelas, desain final, data tersedia.')],
  cx=[T('Pembagian kerja analis SI dan UX designer dalam satu fitur', '''
Fitur: pengajuan cuti online di HRIS

Analis SI / MSI                                  UX Designer
- Aturan bisnis: kuota cuti, carry over 5 hari   - Riset: bagaimana karyawan mengajukan cuti sekarang
- Alur approval: atasan -> HR jika > 3 hari      - User flow & wireframe (mobile-first, pabrik tanpa PC)
- Integrasi: saldo cuti -> payroll               - Prototype + usability test 5 karyawan
- Data & laporan: rekap cuti per divisi          - UI final, state kosong/error, teks tombol
- Kontrol: jejak audit, hak akses per peran      - Aksesibilitas & bahasa sederhana
- Acceptance criteria & UAT bersama HR           - Design QA bersama developer
Bersama: prioritas MoSCoW, definisi metrik (waktu approval, % pengajuan lewat aplikasi)''')]),

'Alur membuat aplikasi baru': dict(
  ist=[('Discovery', 'Fase memahami masalah, pengguna, dan tujuan bisnis sebelum membangun.'),
       ('MVP', 'Minimum Viable Product: versi terkecil yang sudah memberi nilai dan bisa dipelajari.'),
       ('Roadmap', 'Rencana rilis bertahap berdasarkan prioritas dan ketergantungan.'),
       ('Release & feedback loop', 'Rilis kecil, ukur, pelajari, perbaiki secara berulang.')],
  cx=[P('Menyusun MVP dengan skor RICE', '''
FITUR = [  # (fitur, reach pengguna/kuartal, impact 0.25-3, confidence 0-1, effort orang-minggu)
    ("Pengajuan cuti dari HP", 1800, 2, 0.9, 4), ("Approval berjenjang", 1800, 1, 0.8, 3),
    ("Kalender tim", 600, 1, 0.7, 3), ("Integrasi payroll otomatis", 1800, 2, 0.6, 8),
    ("Chatbot tanya saldo cuti", 1200, 0.5, 0.5, 5), ("Laporan cuti untuk HR", 15, 3, 0.9, 2),
]
skor = sorted(((r * i * c / e, f, e) for f, r, i, c, e in FITUR), reverse=True)
kapasitas, total = 12, 0
for s, f, e in skor:
    masuk = total + e <= kapasitas
    total += e if masuk else 0
    print(f"{s:>7.0f}  {f:<28} {e} org-mgg  {'MVP' if masuk else 'rilis berikutnya'}")
''')]),

'Alur memperbaiki aplikasi lama agar sesuai standar': dict(
  ist=[('Legacy system', 'Sistem lama yang masih dipakai tetapi sulit diubah, sering tanpa dokumentasi.'),
       ('Heuristic evaluation', 'Penilaian UI berdasarkan 10 heuristik Nielsen oleh evaluator berpengalaman.'),
       ('Strangler fig pattern', 'Mengganti sistem lama sedikit demi sedikit sambil tetap berjalan.'),
       ('Accessibility audit', 'Pemeriksaan kepatuhan WCAG 2.2 AA pada aplikasi yang sudah ada.')],
  cx=[P('Prioritas temuan audit aplikasi lama', '''
TEMUAN = [  # (temuan, kategori, severity 1-4, pengguna terdampak %, usaha perbaikan 1-5)
    ("Login tanpa MFA", "keamanan", 4, 100, 2), ("Form pendaftaran 4 halaman tanpa simpan otomatis", "UX", 3, 60, 3),
    ("Kontras teks abu-abu 2.8:1", "aksesibilitas", 3, 100, 1), ("Laporan bulanan butuh 9 menit", "kinerja", 2, 15, 4),
    ("Istilah 'Submit' dan 'Kirim' bercampur", "UX writing", 1, 100, 1), ("Tidak ada jejak audit perubahan data", "kepatuhan", 4, 5, 3),
]
for t, kat, sev, kena, usaha in sorted(TEMUAN, key=lambda x: -(x[2] * x[3] / 100) / x[4]):
    print(f"{sev * kena / 100 / usaha:>5.2f}  [{kat:<13}] {t}")
print("Quick win (usaha 1): kontras & istilah. Wajib walau usaha besar: MFA dan jejak audit (risiko hukum).")
''')]),

'Rancang sistem informasi untuk organisasi pilihanmu': dict(
  ist=[('Business case', 'Dokumen alasan investasi: masalah, opsi, biaya-manfaat, risiko, rekomendasi.'),
       ('Solution architecture', 'Gambaran komponen sistem, integrasi, data, dan infrastruktur.'),
       ('Implementation plan', 'Tahapan, jadwal, tim, anggaran, dan strategi go-live (big bang vs bertahap).'),
       ('Post-implementation review', 'Evaluasi setelah go-live: apakah manfaat yang dijanjikan tercapai.')],
  cx=[T('Kerangka dokumen proyek akhir (dipakai juga di dunia kerja)', '''
1. Ringkasan eksekutif (1 halaman)
2. Profil organisasi & masalah (data pendukung, Pareto, 5 Whys)
3. Stakeholder & kebutuhan (power-interest, user story MoSCoW, non-fungsional)
4. Proses as-is vs to-be (BPMN, waktu siklus)
5. Opsi solusi & skor berbobot (beli SaaS / kembangkan / hibrida)
6. Rancangan: ERD, arsitektur, integrasi, hak akses, laporan & KPI
7. Kelayakan: NPV, payback, risiko (matriks 5x5), kepatuhan UU PDP
8. Rencana implementasi: roadmap MVP, RACI, migrasi data, pelatihan, BCP
9. Ukuran keberhasilan & rencana evaluasi 3/6/12 bulan''')]),
}
