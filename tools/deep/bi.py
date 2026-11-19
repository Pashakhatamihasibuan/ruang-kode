"""Pendalaman jalur BI Analyst: istilah dunia kerja dan contoh (Python/SQLite dijalankan; DAX/LookML sebagai rujukan)."""
K = 'bi'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def Q(t, code, b=None, setup=''):
    return dict(t=t, b=b, code=code.strip('\n'), lang='sql', setup=setup)


PENJUALAN = '''CREATE TABLE dim_tanggal (tgl TEXT PRIMARY KEY, bulan TEXT, hari TEXT);
CREATE TABLE dim_toko (toko_id INT PRIMARY KEY, nama TEXT, kota TEXT);
CREATE TABLE fakta_penjualan (tgl TEXT, toko_id INT, produk TEXT, qty INT, omzet INT, hpp INT);
INSERT INTO dim_toko VALUES (1,'Toko Merdeka','Medan'),(2,'Toko Dago','Bandung'),(3,'Toko Tunjungan','Surabaya');
WITH RECURSIVE d(x) AS (SELECT date('2026-01-01') UNION ALL SELECT date(x, '+1 day') FROM d WHERE x < '2026-06-30')
INSERT INTO dim_tanggal SELECT x, substr(x,1,7), strftime('%w', x) FROM d;
INSERT INTO fakta_penjualan
SELECT t.tgl, s.toko_id, p.produk,
       5 + ((julianday(t.tgl) * 7 + s.toko_id * 13 + p.k) % 11) + CAST(substr(t.bulan,6,2) AS INT) * s.toko_id
         + CASE WHEN t.hari IN ('0','6') THEN 8 ELSE 0 END,
       0, 0
FROM dim_tanggal t, dim_toko s, (SELECT 'Kopi' produk, 1 k UNION ALL SELECT 'Teh', 2 UNION ALL SELECT 'Roti', 3) p;
UPDATE fakta_penjualan SET omzet = qty * CASE produk WHEN 'Kopi' THEN 25000 WHEN 'Teh' THEN 15000 ELSE 20000 END,
                           hpp   = qty * CASE produk WHEN 'Kopi' THEN 11000 WHEN 'Teh' THEN 5000 ELSE 12000 END;'''

D = {
'BI analyst dan peran data lainnya': dict(
  ist=[('BI analyst', 'Mengubah data menjadi laporan, dashboard, dan insight untuk keputusan bisnis rutin.'),
       ('Analytics engineer', 'Membangun model data bersih dan teruji (dbt) yang dipakai BI analyst.'),
       ('Self-service BI', 'Pengguna bisnis bisa menjawab pertanyaannya sendiri dari model data yang disiapkan.'),
       ('Stakeholder', 'Pemakai hasil analisis: manajer penjualan, keuangan, operasional, direksi.')],
  cx=[T('Satu pertanyaan bisnis, siapa mengerjakan apa', '''
Pertanyaan: "Kenapa margin cabang Bandung turun 4 poin bulan ini?"

Data engineer     : pastikan data POS & pembelian Bandung masuk lengkap tiap pagi
Analytics engineer: model fakta_penjualan + dim_produk dengan hpp terbaru, teruji
BI analyst        : dashboard margin per kategori, temukan kopi susu hpp naik 18% (gula aren)
Data scientist    : (jika perlu) prediksi dampak kenaikan harga jual ke permintaan
Manajer           : memutuskan naikkan harga Rp2.000 atau ganti pemasok''')]),

'Berpikir seperti pemilik bisnis': dict(
  ist=[('So what?', 'Pertanyaan wajib setelah setiap angka: apa artinya bagi bisnis dan apa tindakannya.'),
       ('Unit economics', 'Untung-rugi per satu unit (per pesanan, per pelanggan) untuk menilai model bisnis.'),
       ('Opportunity cost', 'Nilai pilihan terbaik yang dikorbankan saat memilih satu opsi.'),
       ('Hypothesis-driven analysis', 'Mulai dari dugaan yang bisa diuji, bukan menggali data tanpa arah.')],
  cx=[P('Unit economics satu pesanan antar makanan', '''
HARGA_RATA = 62000
komponen = {"komisi platform (20%)": -0.20 * HARGA_RATA, "bahan baku (35%)": -0.35 * HARGA_RATA,
            "kemasan": -2500, "diskon promo yang ditanggung toko": -6000, "tenaga kerja per pesanan": -7000}
laba = HARGA_RATA + sum(komponen.values())
print(f"{'harga rata-rata':<34}Rp{HARGA_RATA:>8,.0f}".replace(",", "."))
for k, v in komponen.items(): print(f"{k:<34}Rp{v:>8,.0f}".replace(",", "."))
print(f"{'laba per pesanan':<34}Rp{laba:>8,.0f}  ({laba / HARGA_RATA:.0%})".replace(",", "."))
print("So what: tanpa promo, laba per pesanan naik ke", f"Rp{laba + 6000:,.0f}".replace(",", "."), "-> uji promo hanya di jam sepi.")
''')]),

'Metrik, KPI & skema bintang': dict(
  ist=[('Metric vs KPI', 'Metrik adalah angka apa pun; KPI adalah metrik terpilih yang terikat target strategis.'),
       ('North star metric', 'Satu metrik utama yang paling mencerminkan nilai bagi pelanggan dan bisnis.'),
       ('Star schema', 'Satu tabel fakta di tengah dikelilingi tabel dimensi; struktur standar model BI.'),
       ('Grain', 'Tingkat rincian satu baris fakta (per transaksi, per hari per toko); harus ditetapkan pertama.')],
  cx=[Q('KPI per toko dari skema bintang', '''
SELECT s.nama, s.kota,
       SUM(f.omzet) AS omzet,
       ROUND(1.0 * SUM(f.omzet - f.hpp) / SUM(f.omzet), 3) AS margin_kotor,
       ROUND(1.0 * SUM(f.omzet) / COUNT(DISTINCT f.tgl)) AS omzet_per_hari
FROM fakta_penjualan f JOIN dim_toko s USING (toko_id)
GROUP BY s.nama, s.kota ORDER BY omzet DESC;''', 'Grain fakta di sini: per tanggal × toko × produk.', setup=PENJUALAN)]),

'Pertumbuhan, margin & kontribusi': dict(
  ist=[('MoM / YoY growth', 'Pertumbuhan dibanding bulan lalu / bulan yang sama tahun lalu (menghilangkan efek musim).'),
       ('Gross margin', '(Omzet − HPP) / omzet; profitabilitas sebelum biaya operasional.'),
       ('Contribution', 'Porsi suatu bagian terhadap total, atau terhadap pertumbuhan total.'),
       ('Price–volume–mix', 'Memecah perubahan omzet menjadi efek harga, volume, dan bauran produk.')],
  cx=[Q('Pertumbuhan bulanan dan kontribusi produk', '''
WITH b AS (SELECT substr(tgl,1,7) AS bulan, produk, SUM(omzet) AS omzet, SUM(omzet - hpp) AS laba
           FROM fakta_penjualan GROUP BY 1, 2)
SELECT bulan, produk, omzet,
       ROUND(1.0 * omzet / LAG(omzet) OVER (PARTITION BY produk ORDER BY bulan) - 1, 3) AS mom,
       ROUND(1.0 * laba / omzet, 2) AS margin,
       ROUND(1.0 * omzet / SUM(omzet) OVER (PARTITION BY bulan), 2) AS kontribusi
FROM b WHERE bulan >= '2026-05' ORDER BY bulan, omzet DESC;''', setup=PENJUALAN)]),

'CLV & analisis kohort': dict(
  ist=[('Customer Lifetime Value (CLV)', 'Perkiraan laba dari seorang pelanggan selama hubungannya dengan bisnis.'),
       ('Cohort', 'Kelompok pelanggan yang memulai di periode sama (misalnya pembeli pertama Januari).'),
       ('Retention rate', 'Persentase kohort yang masih aktif di periode berikutnya.'),
       ('CAC & rasio CLV:CAC', 'Biaya akuisisi per pelanggan; rasio sehat sering dijadikan patokan sekitar 3:1.')],
  cx=[P('Tabel retensi kohort dan CLV sederhana', '''
KOHORT = {  # pelanggan aktif di bulan ke-0..4 sejak pembelian pertama
    "2026-01": [400, 188, 140, 122, 110], "2026-02": [520, 260, 198, 175],
    "2026-03": [610, 330, 262], "2026-04": [580, 302],
}
print("kohort   " + "".join(f"  M{i}" for i in range(5)))
for k, v in KOHORT.items():
    print(f"{k}  " + "".join(f"{x / v[0]:>5.0%}" for x in v))
aov, margin, beli_per_bln = 145000, 0.32, 1.3
retensi = [1, 0.47, 0.36, 0.31, 0.28] + [0.28 * 0.95 ** i for i in range(1, 8)]   # 12 bulan
clv = sum(r * beli_per_bln * aov * margin for r in retensi)
print(f"CLV 12 bulan ~ Rp{clv:,.0f}; dengan CAC Rp45.000 rasio CLV:CAC = {clv / 45000:.1f}".replace(",", "."))
''')]),

'Leading vs lagging indicator': dict(
  ist=[('Lagging indicator', 'Hasil akhir yang baru terlihat belakangan: omzet, churn, laba.'),
       ('Leading indicator', 'Sinyal awal yang memengaruhi hasil dan bisa dikendalikan: kunjungan sales, uji coba produk, waktu respons.'),
       ('Correlation lag', 'Jeda waktu antara perubahan indikator awal dan dampaknya ke hasil.'),
       ('Input metric', 'Metrik aktivitas yang dikerjakan tim setiap minggu untuk menggerakkan hasil.')],
  cx=[P('Apakah kunjungan sales minggu lalu memprediksi order minggu ini?', '''
import statistics as st
kunjungan = [42, 38, 55, 61, 47, 70, 66, 52, 75, 80, 58, 63]
order     = [31, 29, 33, 38, 47, 35, 49, 50, 38, 55, 57, 41]
def korelasi(a, b):
    ma, mb = st.mean(a), st.mean(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (len(a) * st.pstdev(a) * st.pstdev(b))
for lag in range(3):
    r = korelasi(kunjungan[:len(kunjungan) - lag], order[lag:])
    print(f"jeda {lag} minggu: korelasi {r:+.2f}")
print("Korelasi tertinggi pada jeda 1 minggu -> kunjungan adalah leading indicator order (tetap uji sebab-akibat).")
''')]),

'Sampel, p-value & selang kepercayaan': dict(
  ist=[('Sample vs population', 'Data yang diamati vs seluruh kelompok yang ingin disimpulkan.'),
       ('Confidence interval', 'Rentang yang kemungkinan besar memuat nilai sebenarnya (misalnya 95%).'),
       ('p-value', 'Peluang mendapat hasil seekstrem ini jika sebenarnya tidak ada perbedaan; bukan peluang hipotesis benar.'),
       ('Statistical vs practical significance', 'Perbedaan bisa signifikan secara statistik tetapi terlalu kecil untuk berarti bagi bisnis.')],
  cx=[P('A/B test halaman checkout: z-test dua proporsi', '''
from math import sqrt, erf
na, ka = 8200, 287      # varian A: pengunjung, pembeli
nb, kb = 8150, 338      # varian B
pa, pb = ka / na, kb / nb
p = (ka + kb) / (na + nb)
se = sqrt(p * (1 - p) * (1 / na + 1 / nb))
z = (pb - pa) / se
pval = 2 * (1 - 0.5 * (1 + erf(abs(z) / sqrt(2))))
se_d = sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
lo, hi = (pb - pa) - 1.96 * se_d, (pb - pa) + 1.96 * se_d
print(f"konversi A {pa:.2%}  B {pb:.2%}  selisih {pb - pa:+.2%}")
print(f"z = {z:.2f}, p-value = {pval:.3f}")
print(f"selang kepercayaan 95% selisih: {lo:+.2%} sampai {hi:+.2%}")
print("Kesimpulan:", "B lebih baik secara signifikan" if pval < 0.05 else "belum cukup bukti", "-> cek juga guardrail (refund, AOV)")
''')]),

'Musiman & peramalan sederhana': dict(
  ist=[('Seasonality', 'Pola berulang menurut waktu: akhir pekan, Ramadan, gajian, akhir tahun.'),
       ('Moving average', 'Rata-rata bergerak untuk menghaluskan fluktuasi dan melihat tren.'),
       ('Seasonal naive forecast', 'Ramalan = nilai periode musim yang sama sebelumnya; patokan dasar yang sulit dikalahkan.'),
       ('MAPE', 'Mean Absolute Percentage Error: rata-rata persentase kesalahan ramalan.')],
  cx=[P('Membandingkan dua metode ramalan penjualan harian', '''
# 4 minggu penjualan harian (Sen..Min) dengan pola akhir pekan
data = [52, 48, 50, 55, 70, 95, 88,  54, 50, 51, 58, 73, 99, 90,  56, 52, 53, 60, 75, 101, 94,  57, 53, 55, 61, 77, 104, 96]
latih, uji = data[:21], data[21:]
ma7 = [sum(latih[-7:]) / 7] * 7                     # rata-rata 7 hari terakhir
naif_musim = latih[-7:]                             # nilai hari yang sama minggu lalu
def mape(f, a): return sum(abs(x - y) / y for x, y in zip(f, a)) / len(a)
hari = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
print("hari aktual  MA7  naif-musiman")
for h, a, m, n in zip(hari, uji, ma7, naif_musim): print(f"{h:<4} {a:>6} {m:>5.0f} {n:>13}")
print(f"MAPE moving average {mape(ma7, uji):.1%} | MAPE seasonal naive {mape(naif_musim, uji):.1%}")
''')]),

'Tabel fakta & dimensi': dict(
  ist=[('Fact table', 'Tabel peristiwa terukur (penjualan, kunjungan) berisi angka dan kunci ke dimensi.'),
       ('Dimension table', 'Tabel konteks deskriptif: tanggal, produk, toko, pelanggan.'),
       ('Surrogate key', 'Kunci buatan di gudang data, terpisah dari ID sistem sumber.'),
       ('Slowly changing dimension (SCD)', 'Cara menyimpan perubahan atribut dimensi; tipe 2 menyimpan riwayat.'),
       ('Additive measure', 'Ukuran yang boleh dijumlah lintas semua dimensi (omzet); saldo/rasio tidak.')],
  cx=[Q('Fakta + dimensi tanggal: omzet hari kerja vs akhir pekan', '''
SELECT CASE WHEN d.hari IN ('0','6') THEN 'akhir pekan' ELSE 'hari kerja' END AS jenis_hari,
       COUNT(DISTINCT d.tgl) AS jumlah_hari,
       SUM(f.omzet) / COUNT(DISTINCT d.tgl) AS omzet_rata_per_hari
FROM fakta_penjualan f JOIN dim_tanggal d USING (tgl)
GROUP BY 1;''', setup=PENJUALAN)]),

'Memeriksa kualitas data': dict(
  ist=[('Data profiling', 'Meringkas isi kolom: jumlah null, nilai unik, min/maks, pola, untuk menemukan keanehan.'),
       ('Reconciliation', 'Membandingkan total di dashboard dengan sistem sumber (POS, akuntansi).'),
       ('Outlier', 'Nilai sangat jauh dari kebiasaan; bisa salah input atau kejadian nyata yang penting.'),
       ('Data freshness', 'Seberapa baru data; dashboard pagi harus menunjukkan kapan data terakhir diperbarui.')],
  cx=[P('Profiling cepat dan deteksi outlier dengan IQR', '''
import statistics as st
nilai = [125000, 98000, 143000, 87000, 112000, None, 131000, 9_800_000, 104000, 0, 118000, 99000, None, 127000]
ada = [v for v in nilai if v is not None]
print(f"baris {len(nilai)}, null {nilai.count(None)}, nol {ada.count(0)}, unik {len(set(ada))}")
q1, _, q3 = st.quantiles(ada, n=4)
iqr = q3 - q1; bawah, atas = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print(f"batas wajar Rp{bawah:,.0f} .. Rp{atas:,.0f}".replace(",", "."))
for v in ada:
    if v < bawah or v > atas:
        alasan = "transaksi nol: batal, uji coba, atau gratis?" if v == 0 else "salah ketik nol ekstra atau pesanan grosir?"
        print("  outlier:", f"Rp{v:,}".replace(",", "."), "-> cek:", alasan)
''')]),

'Warehouse, lake & ETL': dict(
  ist=[('Data warehouse', 'Penyimpanan terstruktur untuk analisis (BigQuery, Snowflake, Redshift).'),
       ('Data lake / lakehouse', 'Penyimpanan berkas mentah murah (object storage) dengan format tabel terbuka (Iceberg, Delta).'),
       ('ETL vs ELT', 'Transformasi sebelum dimuat vs dimuat dulu lalu ditransformasi di warehouse (pola modern dengan dbt).'),
       ('Semantic layer', 'Definisi metrik terpusat (Looker LookML, dbt Semantic Layer, Power BI model) agar angka konsisten.')],
  cx=[T('Definisi metrik di semantic layer (LookML)', '''
view: fakta_penjualan {
  sql_table_name: gold.fakta_penjualan ;;
  dimension_group: tgl { type: time  timeframes: [date, week, month]  sql: ${TABLE}.tgl ;; }
  dimension: toko_id { type: number  hidden: yes }
  measure: omzet        { type: sum  sql: ${TABLE}.omzet ;;  value_format_name: idr }
  measure: laba_kotor   { type: sum  sql: ${TABLE}.omzet - ${TABLE}.hpp ;; }
  measure: margin_kotor { type: number  sql: ${laba_kotor} / NULLIF(${omzet}, 0) ;;  value_format_name: percent_1 }
}
# Semua dashboard memakai measure yang sama -> tidak ada lagi "margin versi tim keuangan vs versi sales".''', lang='text')]),

'Running total & perubahan bulan ke bulan': dict(
  ist=[('Window function', 'Fungsi yang menghitung lintas baris tanpa meringkas: SUM() OVER, LAG, RANK.'),
       ('Running total (YTD)', 'Akumulasi dari awal periode sampai baris saat ini (year-to-date).'),
       ('LAG / LEAD', 'Mengambil nilai baris sebelumnya / berikutnya untuk menghitung perubahan.'),
       ('Rolling average', 'Rata-rata bergerak beberapa periode terakhir (ROWS BETWEEN 2 PRECEDING AND CURRENT ROW).')],
  cx=[Q('YTD, MoM, dan rata-rata bergerak 3 bulan', '''
WITH b AS (SELECT substr(tgl,1,7) AS bulan, SUM(omzet) AS omzet FROM fakta_penjualan GROUP BY 1)
SELECT bulan, omzet,
       SUM(omzet) OVER (ORDER BY bulan) AS ytd,
       ROUND(1.0 * omzet / LAG(omzet) OVER (ORDER BY bulan) - 1, 3) AS mom,
       ROUND(AVG(omzet) OVER (ORDER BY bulan ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)) AS rata3
FROM b ORDER BY bulan;''', setup=PENJUALAN)]),

'Merancang dashboard': dict(
  ist=[('Dashboard operasional / analitis / strategis', 'Pemantauan real-time / eksplorasi penyebab / ringkasan tren untuk pimpinan.'),
       ('Inverted pyramid layout', 'KPI utama di kiri atas, tren di tengah, rincian di bawah.'),
       ('Filter & drill-through', 'Kontrol untuk menyaring periode/wilayah dan menelusur ke halaman rincian.'),
       ('Data freshness label', 'Keterangan "data per 19 Nov 06.00 WIB" agar pembaca tahu kebaruan angka.')],
  cx=[T('Wireframe dashboard penjualan mingguan', '''
+--------------------------------------------------------------------------+
| Penjualan Mingguan          [Periode: 11-17 Nov v] [Wilayah: Semua v]    |
| Data per Senin 18 Nov 06.00 WIB                                          |
+--------------+--------------+--------------+-----------------------------+
| Omzet        | Margin kotor | Pesanan      | AOV                         |
| Rp4,82 M     | 41,3%        | 31.204       | Rp154.500                   |
| +6% vs mg lalu| -0,8 poin   | +4%          | +2%                         |
+--------------+--------------+--------------+-----------------------------+
| Tren omzet 12 minggu (garis, minggu ini disorot)                         |
+------------------------------------+-------------------------------------+
| Omzet per wilayah (bar, urut)      | Top 10 produk turun terbanyak (tabel)|
+------------------------------------+-------------------------------------+
| Klik wilayah -> halaman rincian toko (drill-through)                     |
+--------------------------------------------------------------------------+''')]),

'Grafik menyesatkan & bercerita dengan data': dict(
  ist=[('Truncated axis', 'Sumbu Y tidak mulai dari nol pada grafik batang sehingga perbedaan tampak berlebihan.'),
       ('Cherry-picking', 'Memilih periode atau data yang mendukung kesimpulan tertentu saja.'),
       ('Data storytelling', 'Konteks → temuan → implikasi → rekomendasi, didukung satu grafik yang jelas per pesan.'),
       ('Annotation', 'Catatan langsung di grafik (misalnya "promo 11.11") untuk menjelaskan lonjakan.')],
  cx=[P('Seberapa besar sumbu terpotong membesar-besarkan perbedaan?', '''
a, b = 9_400, 9_800                     # omzet (juta) dua cabang
for mulai in (0, 9_000, 9_300):
    ta, tb = a - mulai, b - mulai       # tinggi batang yang terlihat
    print(f"sumbu mulai {mulai:>5}: batang B tampak {tb / ta:.1f}x batang A (sebenarnya {b / a:.2f}x)")
''')]),

'Warna, urutan & angka di dashboard': dict(
  ist=[('Semantic color', 'Warna dengan makna konsisten: merah = di bawah target, hijau = di atas, abu-abu = konteks.'),
       ('Colorblind-safe palette', 'Palet yang tetap terbedakan untuk buta warna; jangan andalkan merah-hijau saja.'),
       ('Sorting', 'Urutkan kategori menurut nilai, kecuali urutan alami (bulan, tahapan funnel).'),
       ('Number formatting', 'Satuan konsisten (Rp4,8 M, 41,3%), pemisah ribuan sesuai lokal, tanpa desimal berlebihan.')],
  cx=[P('Format angka gaya Indonesia untuk kartu KPI', '''
def rp_singkat(x):
    for batas, sat in ((1e12, "T"), (1e9, "M"), (1e6, "jt"), (1e3, "rb")):
        if abs(x) >= batas: return f"Rp{x / batas:,.1f} {sat}".replace(".", ",")
    return f"Rp{x:,.0f}".replace(",", ".")
def persen(x, desimal=1): return f"{x * 100:.{desimal}f}%".replace(".", ",")
def ribuan(x): return f"{x:,.0f}".replace(",", ".")
for v in (4_823_500_000, 154_500, 2_310, 1_250_000_000_000): print(f"{v:>16} -> {rp_singkat(v)}")
print(persen(0.4132), persen(-0.008), ribuan(31204))
''')]),

'Power BI, Tableau & Looker': dict(
  ist=[('Power BI + DAX', 'Alat BI Microsoft; DAX adalah bahasa rumus measure (CALCULATE, filter context).'),
       ('Tableau', 'Alat visualisasi kuat untuk eksplorasi; calculated field dan LOD expression.'),
       ('Looker / Looker Studio', 'Looker memakai LookML (semantic layer); Looker Studio gratis untuk dashboard sederhana.'),
       ('Row-level security (BI)', 'Pembatasan baris data per pengguna di dashboard (manajer hanya melihat wilayahnya).')],
  cx=[T('Measure yang sama di tiga alat', '''
-- Power BI (DAX)
Margin Kotor % = DIVIDE( SUM(Fakta[Omzet]) - SUM(Fakta[HPP]), SUM(Fakta[Omzet]) )
Omzet YTD      = TOTALYTD( SUM(Fakta[Omzet]), Tanggal[Tgl] )
Omzet MoM %    = DIVIDE( [Omzet], CALCULATE([Omzet], DATEADD(Tanggal[Tgl], -1, MONTH)) ) - 1

-- Tableau (calculated field)
Margin Kotor %  : (SUM([Omzet]) - SUM([HPP])) / SUM([Omzet])
Omzet per toko  : { FIXED [Toko] : SUM([Omzet]) }          // LOD expression

-- Looker (LookML)
measure: margin_kotor { type: number  sql: (${omzet} - ${hpp}) / NULLIF(${omzet}, 0) ;; }''')]),

'Privasi data & UU PDP': dict(
  ist=[('Data minimization', 'Hanya mengumpulkan dan menampilkan data yang perlu untuk tujuan analisis.'),
       ('Pseudonymization', 'Mengganti identitas langsung dengan kode (hash) agar analisis tetap bisa tanpa nama.'),
       ('Aggregation threshold', 'Tidak menampilkan kelompok terlalu kecil (misalnya < 10 orang) agar individu tidak teridentifikasi.'),
       ('Access review', 'Peninjauan berkala siapa saja yang bisa melihat dashboard berisi data pribadi.')],
  cx=[P('Pseudonimisasi dan ambang agregasi sebelum data dibagikan', '''
import hashlib
GARAM = "rahasia-proyek-2026"            # disimpan terpisah, tidak ikut dibagikan
PELANGGAN = [("Rina", "081234567890", "Medan", 3), ("Dodi", "081298765432", "Bandung", 5),
             ("Ayu", "081311112222", "Medan", 2), ("Bagus", "081377778888", "Kupang", 7)]
for nama, hp, kota, n in PELANGGAN:
    kode = hashlib.sha256((GARAM + hp).encode()).hexdigest()[:10]
    print(f"{kode}  {kota:<8} {n} pesanan")
from collections import Counter
per_kota = Counter(k for _, _, k, _ in PELANGGAN)
for kota, n in per_kota.items():
    print(f"{kota:<8} {'disembunyikan (< 2 pelanggan)' if n < 2 else str(n) + ' pelanggan'}")
''')]),

'Portofolio & wawancara BI': dict(
  ist=[('Case study', 'Cerita proyek: masalah bisnis, data, pendekatan, temuan, dampak, dan pembelajaran.'),
       ('Take-home test', 'Tugas analisis dari perusahaan dengan dataset; dinilai SQL, logika, dan komunikasi.'),
       ('STAR method', 'Situation, Task, Action, Result: struktur menjawab pertanyaan perilaku.'),
       ('Business sense', 'Kemampuan mengaitkan angka dengan keputusan; sering lebih dinilai daripada kecanggihan grafik.')],
  cx=[T('Kerangka case study portofolio BI', '''
Judul   : Menurunkan stok mati 23% di jaringan apotek 14 cabang
Masalah : obat kedaluwarsa senilai Rp410 juta/tahun, pembelian berdasarkan feeling
Data    : 2 tahun transaksi POS (1,8 juta baris), stok harian, data pemasok
Aksi    : model fakta-dimensi di BigQuery, dashboard Looker Studio "stok berisiko" (umur > 120 hari,
          perputaran rendah), alert mingguan ke apoteker penanggung jawab
Hasil   : 6 bulan kemudian stok mati turun 23%, transfer antarcabang naik 3x
Belajar : angka saja tidak cukup; apoteker baru memakai dashboard setelah ada daftar tindakan per cabang''')]),

'Dashboard kinerja penjualan semester 1': dict(
  ist=[('Requirement gathering', 'Wawancara pengguna dashboard: keputusan apa, seberapa sering, angka apa.'),
       ('Data model', 'Skema bintang yang menjadi sumber dashboard.'),
       ('Insight summary', 'Tiga sampai lima temuan utama dalam kalimat, di atas dashboard.'),
       ('Handover', 'Dokumentasi definisi metrik, sumber data, jadwal refresh, dan pemilik dashboard.')],
  cx=[Q('Ringkasan semester 1 untuk halaman insight', '''
WITH t AS (SELECT s.kota, substr(f.tgl,1,7) AS bulan, SUM(f.omzet) AS omzet
           FROM fakta_penjualan f JOIN dim_toko s USING (toko_id) GROUP BY 1, 2)
SELECT kota,
       SUM(omzet) AS omzet_s1,
       MAX(CASE WHEN bulan = '2026-01' THEN omzet END) AS jan,
       MAX(CASE WHEN bulan = '2026-06' THEN omzet END) AS jun,
       ROUND(1.0 * MAX(CASE WHEN bulan = '2026-06' THEN omzet END) / MAX(CASE WHEN bulan = '2026-01' THEN omzet END) - 1, 2) AS tumbuh_jan_jun
FROM t GROUP BY kota ORDER BY omzet_s1 DESC;''', setup=PENJUALAN)]),
}
