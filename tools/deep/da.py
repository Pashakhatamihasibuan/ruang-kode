"""Pendalaman jalur Data Analyst: istilah dunia kerja, rumus spreadsheet, dan contoh Python/pandas yang dijalankan."""
K = 'da'


def P(t, code, b=None, setup=None):
    d = dict(t=t, b=b, code=code.strip('\n'), lang='python')
    if setup:
        d['setup'] = setup
    return d


def X(t, code, b=None, lang='excel'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Empat jenis analitik': dict(
  ist=[('Descriptive analytics', 'Apa yang terjadi? Laporan omzet, dashboard KPI.'),
       ('Diagnostic analytics', 'Mengapa terjadi? Drill-down, segmentasi, analisis akar masalah.'),
       ('Predictive analytics', 'Apa yang kemungkinan terjadi? Forecast penjualan, prediksi churn.'),
       ('Prescriptive analytics', 'Apa yang sebaiknya dilakukan? Rekomendasi stok, harga, atau target promosi.'),
       ('KPI', 'Key Performance Indicator: metrik utama yang dipantau terhadap target.')],
  cx=[P('Satu dataset, empat pertanyaan analitik', r'''
import random
random.seed(7)
bulan = ["Jul", "Agu", "Sep", "Okt", "Nov"]
omzet = [412, 438, 405, 371, 352]          # juta rupiah
kota = {"Jakarta": [190, 196, 188, 185, 182], "Bandung": [120, 131, 117, 92, 80], "Surabaya": [102, 111, 100, 94, 90]}

print(f"1. Deskriptif : omzet Nov {omzet[-1]} jt, turun {abs(omzet[-1] / omzet[2] - 1):.1%} dari Sep")
turun = {k: v[-1] - v[2] for k, v in kota.items()}
penyebab = min(turun, key=turun.get)
print("2. Diagnostik : penurunan terbesar di", penyebab, f"({turun[penyebab]} jt sejak Sep)")
tren = (omzet[-1] - omzet[0]) / (len(omzet) - 1)
print("3. Prediktif  : jika tren berlanjut, Des ~", round(omzet[-1] + tren), "jt")
print(f"4. Preskriptif: prioritaskan investigasi {penyebab} (stok, kurir, kompetitor) sebelum menambah anggaran iklan nasional")
''', 'Semakin ke bawah, nilai bisnisnya semakin tinggi, tetapi juga semakin butuh data yang bersih dan asumsi yang jelas.')]),

'Jenis data & skala ukur': dict(
  ist=[('Kualitatif vs kuantitatif', 'Kategori (kota, status) vs angka (omzet, umur).'),
       ('Nominal', 'Kategori tanpa urutan: metode bayar, provinsi.'),
       ('Ordinal', 'Kategori berurutan: rating 1-5, tingkat pendidikan; jarak antar level tidak pasti sama.'),
       ('Interval', 'Angka berjarak sama tanpa nol mutlak: suhu °C, tahun.'),
       ('Rasio', 'Angka dengan nol mutlak; perbandingan bermakna: omzet, berat, durasi.'),
       ('Diskrit vs kontinu', 'Hasil menghitung (jumlah order) vs hasil mengukur (berat paket).')],
  cx=[P('Menentukan skala dan ringkasan yang tepat per kolom', r'''
import statistics as st

data = {
    "metode_bayar": ["QRIS", "VA", "QRIS", "COD", "QRIS", "VA"],
    "rating": [5, 4, 5, 2, 4, 3],
    "suhu_gudang_c": [27.5, 28.1, 26.9, 29.4, 27.8, 28.0],
    "total_belanja": [125000, 89000, 240000, 56000, 310000, 98000],
}
skala = {"metode_bayar": "nominal", "rating": "ordinal", "suhu_gudang_c": "interval", "total_belanja": "rasio"}

for kol, nilai in data.items():
    s = skala[kol]
    if s == "nominal":
        ringkas = f"modus = {st.mode(nilai)}"
    elif s == "ordinal":
        ringkas = f"median = {st.median(nilai)}, modus = {st.mode(nilai)}"
    elif s == "interval":
        ringkas = f"rata-rata = {st.mean(nilai):.1f}, beda maks-min = {max(nilai) - min(nilai):.1f}"
    else:
        rata = f"{st.mean(nilai):,.0f}".replace(",", ".")
        ringkas = f"rata-rata = Rp{rata}, maks/min = {max(nilai) / min(nilai):.1f}x"
    print(f"{kol:<15} {s:<9} {ringkas}")
print("Catatan: rata-rata rating ordinal sering dipakai di industri, tapi laporkan juga median dan sebarannya.")
''')]),

'Fungsi dasar: SUM, AVERAGE, COUNT, IF': dict(
  ist=[('Cell reference', 'Relatif (A2), absolut ($A$2), campuran ($A2); menentukan perilaku saat rumus disalin.'),
       ('SUMIFS / COUNTIFS / AVERAGEIFS', 'Agregasi dengan banyak kriteria; pengganti pivot sederhana.'),
       ('IFS & IFERROR', 'Kondisi bertingkat tanpa IF bersarang; menangani error seperti #DIV/0!.'),
       ('Named range & Table', 'Nama untuk rentang (Ctrl+T di Excel) agar rumus mudah dibaca dan otomatis meluas.'),
       ('Data validation', 'Dropdown dan batasan input agar data entri tidak kotor.')],
  cx=[X('Rumus laporan penjualan harian', r'''
   A          B          C        D      E           F
1  Tanggal    Kota       Produk   Qty    Harga       Total
2  01/11/2026 Jakarta    Kopi     3      65000       =D2*E2
...
F2   =D2*E2
H2   =SUM(F2:F500)                                   total omzet
H3   =AVERAGE(F2:F500)                               rata-rata per transaksi
H4   =COUNTA(A2:A500)                                jumlah transaksi
H5   =SUMIFS(F:F, B:B, "Bandung", C:C, "Kopi")       omzet kopi di Bandung
H6   =COUNTIFS(F:F, ">=200000")                      transaksi besar
H7   =IFERROR(H5/H2, 0)                              porsi Bandung, aman dari #DIV/0!
G2   =IFS(F2>=200000, "Besar", F2>=100000, "Sedang", TRUE, "Kecil")
I2   =F2*$K$1                                        $K$1 = tarif PPN 11% (absolut)

Google Sheets: =QUERY(A1:F500, "select B, sum(F) where C = 'Kopi' group by B order by sum(F) desc")'''),
      P('Rumus yang sama dengan pandas', r'''
import pandas as pd
df = pd.DataFrame({
    "kota": ["Jakarta", "Bandung", "Bandung", "Surabaya", "Jakarta", "Bandung"],
    "produk": ["Kopi", "Kopi", "Teh", "Kopi", "Teh", "Kopi"],
    "qty": [3, 2, 5, 1, 4, 6],
    "harga": [65000, 65000, 18000, 65000, 18000, 65000],
})
df["total"] = df["qty"] * df["harga"]                                      # =D2*E2
df["ukuran"] = pd.cut(df["total"], [0, 100000, 200000, float("inf")], right=False, labels=["Kecil", "Sedang", "Besar"])  # =IFS(...)
rp = lambda x: "Rp" + f"{x:,.0f}".replace(",", ".")
print("SUM        :", rp(df["total"].sum()))
print("AVERAGE    :", rp(df["total"].mean()))
print("COUNTA     :", len(df))
print("SUMIFS     :", rp(df.loc[(df.kota == "Bandung") & (df.produk == "Kopi"), "total"].sum()))
print("COUNTIFS   :", (df["total"] >= 200000).sum())
print(df[["kota", "produk", "total", "ukuran"]].to_string(index=False))
''')]),

'Teks & tanggal: TRIM, PROPER, SUBSTITUTE, DATEDIF': dict(
  ist=[('TRIM / CLEAN', 'Menghapus spasi berlebih dan karakter tak terlihat dari hasil copy-paste.'),
       ('PROPER / UPPER / LOWER', 'Menyeragamkan huruf besar-kecil nama dan kota.'),
       ('SUBSTITUTE / TEXTSPLIT', 'Mengganti teks dan memecah kolom (Excel 365).'),
       ('DATEDIF / NETWORKDAYS', 'Selisih tanggal dalam hari/bulan/tahun dan hari kerja.'),
       ('Serial date', 'Excel menyimpan tanggal sebagai angka hari sejak 1900; format hanya tampilan.')],
  cx=[X('Membersihkan nama, nomor HP, dan menghitung umur pelanggan', r'''
B2  =PROPER(TRIM(A2))                                   "  rina   WIJAYA " -> "Rina Wijaya"
D2  ="+62" & MID(SUBSTITUTE(SUBSTITUTE(C2,"-","")," ",""), 2, 15)   "0812-3456 7890" -> "+6281234567890"
F2  =DATEDIF(E2, TODAY(), "Y")                          umur dalam tahun
G2  =NETWORKDAYS(H2, I2, Libur!A:A)                     hari kerja pesanan diproses
J2  =TEXT(E2, "dd mmmm yyyy")                           tampil "17 Agustus 1995" (lokal Indonesia)
K2  =LEFT(L2, FIND("@", L2) - 1)                        nama pengguna dari email'''),
      P('Versi pandas: string accessor dan tanggal', r'''
import pandas as pd
df = pd.DataFrame({
    "nama": ["  rina   WIJAYA ", "budi santoso", "SITI  aminah"],
    "hp": ["0812-3456 7890", "+62 857 1111 2222", "08139999000"],
    "lahir": ["17/08/1995", "02/01/2001", "30/11/1988"],
    "pesan": ["2026-11-03", "2026-11-07", "2026-11-14"],
    "kirim": ["2026-11-05", "2026-11-12", "2026-11-17"],
})
df["nama"] = df["nama"].str.split().str.join(" ").str.title()
df["hp"] = "+62" + df["hp"].str.replace(r"[\s-]", "", regex=True).str.replace(r"^(\+62|0)", "", regex=True)
df["lahir"] = pd.to_datetime(df["lahir"], format="%d/%m/%Y")
hari_ini = pd.Timestamp("2026-11-19")
df["umur"] = ((hari_ini - df["lahir"]).dt.days // 365.25).astype(int)
df["hari_kerja"] = [len(pd.bdate_range(a, b)) - 1 for a, b in zip(df["pesan"], df["kirim"])]
print(df[["nama", "hp", "umur", "hari_kerja"]].to_string(index=False))
''')]),

'Lookup & pivot table': dict(
  ist=[('VLOOKUP / XLOOKUP', 'Mencari nilai dari tabel lain; XLOOKUP lebih fleksibel dan tidak rusak saat kolom disisipkan.'),
       ('INDEX + MATCH', 'Kombinasi klasik pencarian dua arah.'),
       ('Lookup key', 'Kolom kunci unik (SKU, ID pelanggan) yang menghubungkan dua tabel.'),
       ('Pivot table', 'Meringkas data dengan menyeret field ke Rows, Columns, Values, Filters.'),
       ('Calculated field', 'Kolom hitungan di dalam pivot, misalnya margin = omzet - modal.')],
  cx=[X('XLOOKUP dan pivot', r'''
=XLOOKUP(C2, Produk!A:A, Produk!C:C, "tidak ada")              harga dari tabel Produk berdasarkan SKU
=VLOOKUP(C2, Produk!A:C, 3, FALSE)                              versi lama; FALSE = cocok persis
=INDEX(Produk!C:C, MATCH(C2, Produk!A:A, 0))                   setara

Pivot: Insert > PivotTable
  Rows    : Kota
  Columns : Bulan
  Values  : Sum of Total, Count of No_Pesanan
  Filters : Kategori = Kopi'''),
      P('merge (lookup) dan pivot_table dengan pandas', r'''
import pandas as pd
transaksi = pd.DataFrame({
    "bulan": ["Okt", "Okt", "Okt", "Nov", "Nov", "Nov", "Nov"],
    "kota": ["Jakarta", "Bandung", "Jakarta", "Bandung", "Jakarta", "Surabaya", "Bandung"],
    "sku": ["KP1", "TH1", "KP2", "KP1", "KP1", "XX9", "TH1"],
    "qty": [3, 5, 1, 2, 4, 1, 3],
})
produk = pd.DataFrame({"sku": ["KP1", "KP2", "TH1"], "nama": ["Kopi Gayo", "Kopi Toraja", "Teh Melati"],
                       "harga": [65000, 72000, 18000], "modal": [41000, 47000, 9000]})

df = transaksi.merge(produk, on="sku", how="left", validate="many_to_one")     # = XLOOKUP
hilang = df[df["nama"].isna()]
print("SKU tanpa pasangan (#N/A):", hilang["sku"].tolist())
df = df.dropna(subset=["nama"])
df["omzet"] = df["qty"] * df["harga"]
df["margin"] = df["qty"] * (df["harga"] - df["modal"])                       # calculated field
pv = df.pivot_table(index="kota", columns="bulan", values="omzet", aggfunc="sum", fill_value=0, margins=True, margins_name="Total")
print(pv.map(lambda x: f"{x:,.0f}".replace(",", ".")).to_string())
print("margin per kota:", df.groupby("kota")["margin"].sum().to_dict())
''')]),

'Python atau R?': dict(
  ist=[('Python (pandas, Polars)', 'Bahasa serbaguna; kuat untuk otomasi, pipeline, dan ML; paling banyak diminta lowongan.'),
       ('R (tidyverse)', 'Kuat untuk statistik dan visualisasi (ggplot2); populer di riset dan akademik.'),
       ('Jupyter / Quarto', 'Notebook dan dokumen analisis yang menggabungkan kode, hasil, dan narasi.'),
       ('Polars', 'DataFrame berbasis Rust yang jauh lebih cepat dari pandas untuk data besar.'),
       ('Reproducibility', 'Analisis yang bisa dijalankan ulang orang lain dengan hasil sama.')],
  cx=[X('Tugas yang sama di pandas, Polars, dan R', r'''
# pandas
df.groupby("kota", as_index=False).agg(omzet=("total", "sum")).sort_values("omzet", ascending=False)

# Polars
df.group_by("kota").agg(pl.col("total").sum().alias("omzet")).sort("omzet", descending=True)

# R (dplyr)
df |> group_by(kota) |> summarise(omzet = sum(total)) |> arrange(desc(omzet))

# SQL (sering paling penting di lowongan analis)
SELECT kota, SUM(total) AS omzet FROM transaksi GROUP BY kota ORDER BY omzet DESC;''', lang='python'),
      P('Matriks keputusan memilih alat', r'''
kriteria = {"lowongan lokal": 0.35, "statistik": 0.15, "otomasi & pipeline": 0.2, "visualisasi": 0.15, "kurva belajar": 0.15}
skor = {"Python": [5, 4, 5, 4, 4], "R": [2, 5, 3, 5, 3], "Spreadsheet saja": [4, 2, 1, 3, 5]}
hasil = {a: sum(w * s for w, s in zip(kriteria.values(), v)) for a, v in skor.items()}
for a, s in sorted(hasil.items(), key=lambda x: -x[1]):
    print(f"{a:<17} {s:.2f} {'█' * round(s * 6)}")
print("Saran: SQL + spreadsheet sebagai dasar, lalu Python. Pelajari R bila bekerja di riset/kesehatan.")
''')]),

'API & web scraping': dict(
  ist=[('REST API', 'Sumber data terstruktur (JSON) lewat HTTP; cara paling rapi mengambil data.'),
       ('API key & rate limit', 'Kunci akses dan batas jumlah request per menit.'),
       ('Pagination', 'Data dibagi per halaman (page/limit atau cursor).'),
       ('Web scraping', 'Mengambil data dari HTML; cek robots.txt, syarat layanan, dan UU PDP sebelum melakukannya.'),
       ('BeautifulSoup / Playwright', 'Parser HTML dan browser otomatis untuk situs yang dirender JavaScript.')],
  cx=[P('Mengambil API berhalaman dan mem-parsing HTML (server lokal)', r'''
import json, threading, urllib.request
from html.parser import HTMLParser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

PRODUK = [{"id": i, "nama": f"Produk {i}", "harga": 10000 + i * 2500} for i in range(1, 24)]
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/api/produk":
            hal = int(parse_qs(u.query).get("page", ["1"])[0]); per = 10
            isi = {"data": PRODUK[(hal - 1) * per: hal * per], "next": hal + 1 if hal * per < len(PRODUK) else None}
            body, tipe = json.dumps(isi).encode(), "application/json"
        else:
            body = b"<ul><li class='harga' data-sku='A1'>Rp45.000</li><li class='harga' data-sku='B2'>Rp18.500</li></ul>"
            tipe = "text/html"
        self.send_response(200); self.send_header("Content-Type", tipe); self.end_headers(); self.wfile.write(body)

srv = HTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{srv.server_port}"

semua, hal, req = [], 1, 0
while hal:
    with urllib.request.urlopen(f"{base}/api/produk?page={hal}") as r:
        j = json.load(r); req += 1
    semua += j["data"]; hal = j["next"]
rata = f"{sum(p['harga'] for p in semua) // len(semua):,}".replace(",", ".")
print(f"API: {len(semua)} produk dari {req} halaman, harga rata-rata Rp{rata}")

class AmbilHarga(HTMLParser):
    def __init__(self): super().__init__(); self.hasil, self._sku = {}, None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("class") == "harga": self._sku = a["data-sku"]
    def handle_data(self, data):
        if self._sku: self.hasil[self._sku] = int(data.replace("Rp", "").replace(".", "")); self._sku = None

with urllib.request.urlopen(base + "/toko") as r:
    p = AmbilHarga(); p.feed(r.read().decode())
print("Scraping HTML:", p.hasil)
srv.shutdown()
''', 'Di dunia nyata gunakan requests/httpx dan BeautifulSoup, beri jeda antar request, patuhi robots.txt, dan jangan mengambil data pribadi.')]),

'Menstandarkan data kotor dengan pandas': dict(
  ist=[('Data cleaning', 'Memperbaiki format, duplikat, nilai hilang, dan nilai tidak wajar; bisa 60-80% waktu analis.'),
       ('Missing value', 'NaN/None; diisi (imputasi), dibuang, atau ditandai sesuai konteks.'),
       ('Deduplication', 'Menghapus baris ganda berdasarkan kunci bisnis, bukan seluruh kolom.'),
       ('Outlier', 'Nilai ekstrem; periksa dulu apakah salah input atau kejadian nyata.'),
       ('Data quality check', 'Aturan otomatis: unik, tidak null, rentang wajar, format benar.')],
  cx=[P('Pipeline pembersihan data transaksi', r'''
import pandas as pd
mentah = pd.DataFrame({
    "id": ["T01", "T02", "T02", "T03", "T04", "T05", "T06"],
    "tanggal": ["2026-11-01", "01/11/2026", "01/11/2026", "2026-11-02", "2026/11/03", None, "2026-11-04"],
    "kota": ["jakarta ", "JAKARTA", "JAKARTA", "Bdg", "bandung", "Surabaya", "sby"],
    "total": ["125.000", "89000", "89000", "Rp240.000", "-5000", "56000", "9900000"],
})
laporan = {"baris awal": len(mentah)}
df = mentah.drop_duplicates(subset="id").copy()
laporan["duplikat dibuang"] = len(mentah) - len(df)

def ke_tanggal(s):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"):        # format yang diketahui dari sumber data
        try:
            return pd.to_datetime(s, format=fmt)
        except (ValueError, TypeError):
            pass
    return pd.NaT
df["tanggal"] = df["tanggal"].map(ke_tanggal)
peta_kota = {"bdg": "Bandung", "sby": "Surabaya"}
df["kota"] = df["kota"].str.strip().str.lower().replace(peta_kota).str.title()
df["total"] = pd.to_numeric(df["total"].str.replace(r"[^\d-]", "", regex=True), errors="coerce")

laporan["tanggal kosong"] = int(df["tanggal"].isna().sum())
laporan["total negatif"] = int((df["total"] < 0).sum())
q1, q3 = df["total"].quantile([0.25, 0.75])
batas = q3 + 3 * (q3 - q1)
df["cek_outlier"] = df["total"] > batas
bersih = df[(df["total"] > 0) & df["tanggal"].notna()]
laporan["baris bersih"] = len(bersih)
print(bersih.to_string(index=False))
print(laporan)
''', 'Outlier T06 (Rp9,9 juta) tidak dibuang otomatis, hanya ditandai. Bisa saja itu pesanan grosir yang sah, jadi konfirmasi dulu ke tim penjualan.')]),

'Rentang, varians & bentuk distribusi': dict(
  ist=[('Range & IQR', 'Selisih maks-min, dan selisih kuartil 3 dan 1 yang tahan outlier.'),
       ('Varians & simpangan baku', 'Rata-rata kuadrat jarak dari mean; simpangan baku dalam satuan aslinya.'),
       ('Coefficient of variation', 'Simpangan baku dibagi mean; membandingkan sebaran antar skala berbeda.'),
       ('Skewness', 'Kemencengan; data transaksi biasanya menceng kanan (banyak kecil, sedikit sangat besar).'),
       ('Kurtosis', 'Ketebalan ekor distribusi; ekor tebal berarti nilai ekstrem lebih sering.')],
  cx=[P('Membandingkan dua cabang dengan rata-rata sama', r'''
import statistics as st
cabang = {
    "Cabang A": [48, 50, 52, 49, 51, 50, 47, 53, 50, 50],
    "Cabang B": [20, 85, 31, 76, 50, 12, 90, 44, 58, 34],
}
def skew(x):
    m, s, n = st.mean(x), st.stdev(x), len(x)
    return n / ((n - 1) * (n - 2)) * sum(((v - m) / s) ** 3 for v in x)

print(f"{'':10}{'mean':>6}{'range':>7}{'stdev':>7}{'CV':>7}{'skew':>7}")
for nama, x in cabang.items():
    m, s = st.mean(x), st.stdev(x)
    print(f"{nama:10}{m:>6.1f}{max(x) - min(x):>7}{s:>7.1f}{s / m:>7.0%}{skew(x):>7.2f}")
print("Rata-rata sama (50 transaksi/hari), tapi B sangat tidak stabil: stok dan jadwal staf harus lebih fleksibel.")

transaksi = [35, 42, 38, 51, 47, 39, 44, 41, 36, 48, 40, 43, 37, 45, 950]
print(f"\nData menceng kanan: mean {st.mean(transaksi):.0f} rb vs median {st.median(transaksi):.0f} rb, skew {skew(transaksi):.1f}")
print("Laporkan median untuk 'belanja tipikal' pelanggan.")
''')]),

'Regresi linear sederhana': dict(
  ist=[('Regresi linear', 'Model y = a + b·x untuk melihat hubungan dan memprediksi.'),
       ('Slope (koefisien)', 'Perubahan y untuk setiap kenaikan 1 satuan x.'),
       ('R² (koefisien determinasi)', 'Proporsi variasi y yang dijelaskan model; 0 sampai 1.'),
       ('Residual', 'Selisih nilai aktual dan prediksi; pola pada residual menandakan model kurang tepat.'),
       ('Korelasi ≠ kausalitas', 'Hubungan statistik belum tentu sebab-akibat; butuh eksperimen atau desain studi.')],
  cx=[P('Belanja iklan vs penjualan: koefisien, R², dan prediksi', r'''
import statistics as st
iklan = [5, 8, 10, 12, 15, 18, 20, 25, 28, 30]          # juta rupiah per minggu
order = [120, 150, 178, 190, 230, 255, 270, 320, 330, 352]

b, a = st.linear_regression(iklan, order)
pred = [a + b * x for x in iklan]
ss_res = sum((y - p) ** 2 for y, p in zip(order, pred))
ss_tot = sum((y - st.mean(order)) ** 2 for y in order)
r2 = 1 - ss_res / ss_tot
print(f"order = {a:.1f} + {b:.2f} x iklan(jt)   R² = {r2:.3f}   r = {st.correlation(iklan, order):.3f}")
print(f"Setiap tambahan Rp1 juta iklan ~ +{b:.1f} order per minggu")
for x in [22, 40]:
    catatan = "" if min(iklan) <= x <= max(iklan) else "  (ekstrapolasi di luar data, hati-hati)"
    print(f"prediksi iklan {x} jt -> {a + b * x:.0f} order{catatan}")
print("residual:", [round(y - p) for y, p in zip(order, pred)])
''', 'Nilai R² tinggi bukan bukti iklan menyebabkan penjualan. Musim, promo, dan kompetitor bisa ikut berperan. Uji A/B atau holdout region memberi bukti yang lebih kuat.')]),

'Persentil, kuartil & median': dict(
  ist=[('Median (P50)', 'Nilai tengah; tahan terhadap outlier.'),
       ('Kuartil (Q1, Q3)', 'Persentil 25 dan 75; batas kotak pada box plot.'),
       ('Persentil (P90, P95, P99)', 'Dipakai untuk SLA, misalnya 95% pesanan terkirim dalam N hari.'),
       ('IQR rule', 'Outlier bila < Q1 - 1,5·IQR atau > Q3 + 1,5·IQR.'),
       ('Five-number summary', 'Min, Q1, median, Q3, maks; ringkasan box plot.')],
  cx=[P('Durasi pengiriman: ringkasan lima angka dan SLA', r'''
import random, statistics as st
random.seed(3)
durasi = sorted([round(random.lognormvariate(1.0, 0.45), 1) for _ in range(400)])  # hari

q = st.quantiles(durasi, n=100, method="inclusive")
p = lambda k: q[k - 1]
q1, med, q3 = p(25), p(50), p(75)
iqr = q3 - q1
outlier = [d for d in durasi if d > q3 + 1.5 * iqr]
print(f"min {min(durasi)} | Q1 {q1:.1f} | median {med:.1f} | Q3 {q3:.1f} | maks {max(durasi)}  (hari)")
print(f"mean {st.mean(durasi):.2f} > median {med:.2f}: data menceng kanan")
print(f"P90 {p(90):.1f} hari, P95 {p(95):.1f} hari")
print(f"Outlier (> {q3 + 1.5 * iqr:.1f} hari): {len(outlier)} pesanan, terlama {max(outlier)} hari")
sla = 5
print(f"SLA 'terkirim ≤ {sla} hari': {sum(d <= sla for d in durasi) / len(durasi):.1%} pesanan memenuhi")
''')]),

'Funnel & stacked chart': dict(
  ist=[('Conversion funnel', 'Tahapan pengguna dari kunjungan sampai pembelian dengan rasio per langkah.'),
       ('Step conversion vs overall', 'Rasio antar-langkah vs rasio dari awal ke akhir.'),
       ('Stacked bar (100%)', 'Membandingkan komposisi antar-kelompok, misalnya metode bayar per kota.'),
       ('Drop-off', 'Langkah dengan kehilangan pengguna terbesar; prioritas perbaikan.'),
       ('Cohort', 'Kelompok pengguna berdasarkan waktu mulai; untuk retensi.')],
  cx=[P('Funnel checkout dan komposisi metode bayar', r'''
langkah = [("Lihat produk", 48200), ("Tambah ke keranjang", 9640), ("Mulai checkout", 5300), ("Isi alamat", 4100), ("Bayar", 2870)]
print(f"{'Langkah':<20}{'Pengguna':>9}{'dari sebelumnya':>17}{'dari awal':>11}")
for i, (n, v) in enumerate(langkah):
    step = f"{v / langkah[i - 1][1]:.1%}" if i else "-"
    print(f"{n:<20}{v:>9,}{step:>17}{v / langkah[0][1]:>11.1%}  {'█' * round(v / langkah[0][1] * 40)}".replace(",", "."))
drop = min(range(1, len(langkah)), key=lambda i: langkah[i][1] / langkah[i - 1][1])
print(f"Drop-off terbesar: {langkah[drop - 1][0]} -> {langkah[drop][0]}")

print("\nKomposisi metode bayar (100% stacked):")
bayar = {"Jakarta": {"QRIS": 52, "VA": 30, "COD": 18}, "Medan": {"QRIS": 28, "VA": 25, "COD": 47}}
sim = {"QRIS": "▓", "VA": "▒", "COD": "░"}
for kota, d in bayar.items():
    tot = sum(d.values())
    batang = "".join(sim[k] * round(v / tot * 40) for k, v in d.items())
    print(f"{kota:<8} {batang}  " + "  ".join(f"{k} {v / tot:.0%}" for k, v in d.items()))
print("Legenda:", "  ".join(f"{s} {k}" for k, s in sim.items()))
''')]),

'Dari temuan ke rekomendasi': dict(
  ist=[('Insight', 'Temuan yang menjelaskan "mengapa" dan relevan untuk keputusan, bukan sekadar angka.'),
       ('So what?', 'Pertanyaan wajib setelah setiap temuan: apa dampaknya bagi bisnis?'),
       ('Pyramid principle', 'Mulai dari kesimpulan, lalu argumen pendukung, lalu data.'),
       ('Impact sizing', 'Memperkirakan nilai rupiah dari sebuah rekomendasi.'),
       ('Executive summary', 'Ringkasan satu halaman untuk pengambil keputusan.')],
  cx=[P('Menghitung dampak rekomendasi dan menyusun ringkasan', r'''
pengunjung_bulanan = 48200
konversi_sekarang = 2870 / 48200
aov = 168000                       # average order value
temuan = [
    ("Ongkir baru terlihat di langkah bayar", "Tampilkan estimasi ongkir di halaman produk", 0.004),
    ("Form alamat 14 field, 31% keluar di sini", "Isi otomatis dari kode pos, kurangi jadi 7 field", 0.003),
    ("COD tidak tersedia di luar Jawa", "Uji COD di Medan dan Makassar", 0.0015),
]
rp = lambda x: "Rp" + f"{x:,.0f}".replace(",", ".")
print("RINGKASAN EKSEKUTIF")
print(f"Konversi saat ini {konversi_sekarang:.2%}. Tiga perbaikan checkout diperkirakan menambah omzet {rp(sum(d for *_, d in temuan) * pengunjung_bulanan * aov)}/bulan.\n")
for i, (t, r, naik) in enumerate(sorted(temuan, key=lambda x: -x[2]), 1):
    tambahan = naik * pengunjung_bulanan * aov
    print(f"{i}. {r}")
    print(f"   Temuan : {t}")
    print(f"   Dampak : +{naik * 100:.2f} poin konversi ≈ {rp(tambahan)}/bulan")
print("\nLangkah berikut: uji A/B 2 minggu untuk rekomendasi 1 sebelum rilis penuh.")
''')]),

'Big data, MapReduce & Spark': dict(
  ist=[('Big data (3V)', 'Volume, Velocity, Variety; data yang tidak muat atau terlalu lambat diproses satu mesin.'),
       ('MapReduce', 'Pola map (proses per potongan) lalu reduce (gabungkan hasil); dasar Hadoop.'),
       ('Apache Spark', 'Mesin pemrosesan terdistribusi di memori; PySpark dan Spark SQL.'),
       ('Data lakehouse', 'Penyimpanan murah ala data lake dengan fitur tabel ala warehouse (Delta Lake, Iceberg).'),
       ('BigQuery / Snowflake / Databricks', 'Platform data cloud yang umum dipakai perusahaan.')],
  cx=[P('Word count gaya MapReduce', r'''
from collections import Counter
from functools import reduce

ulasan = [
    "pengiriman cepat kopi enak", "kopi enak harga mahal", "pengiriman lambat kemasan rusak",
    "kemasan rapi pengiriman cepat", "harga mahal tapi kopi enak", "pengiriman lambat sekali",
] * 1000
STOP = {"tapi", "sekali"}

def map_fase(potongan):                                  # berjalan di tiap worker / node
    return Counter(w for kalimat in potongan for w in kalimat.split() if w not in STOP)

def reduce_fase(a, b):                                   # menggabungkan hasil antar node
    return a + b

n = 4
potongan = [ulasan[i::n] for i in range(n)]
hasil_map = list(map(map_fase, potongan))                # di Spark: rdd.flatMap(...).map(...)
total = reduce(reduce_fase, hasil_map)                   # di Spark: reduceByKey(add)
print(f"{len(ulasan):,} ulasan dibagi ke {n} worker".replace(",", "."))
for kata, jml in total.most_common(6):
    print(f"  {kata:<11}{jml:>5}")
''', 'Fungsi map dan reduce sengaja ditulis tanpa state bersama. Itulah syarat agar pekerjaan bisa dipecah ke ratusan mesin seperti di Spark.'),
      X('Tugas yang sama di PySpark dan Spark SQL', r'''
from pyspark.sql import SparkSession, functions as F
spark = SparkSession.builder.appName("ulasan").getOrCreate()
df = spark.read.parquet("s3://data-toko/ulasan/2026/*")
(df.select(F.explode(F.split("teks", " ")).alias("kata"))
   .groupBy("kata").count().orderBy(F.desc("count")).show(10))

-- Spark SQL / BigQuery
SELECT kata, COUNT(*) AS n
FROM ulasan, UNNEST(SPLIT(teks, ' ')) AS kata
GROUP BY kata ORDER BY n DESC LIMIT 10;''', lang='python')]),

'Peta machine learning untuk analis': dict(
  ist=[('Supervised learning', 'Belajar dari data berlabel: regresi (angka) dan klasifikasi (kategori).'),
       ('Unsupervised learning', 'Mencari pola tanpa label: clustering segmentasi pelanggan.'),
       ('Train/test split', 'Memisahkan data latih dan uji agar evaluasi jujur.'),
       ('Overfitting', 'Model hafal data latih tetapi buruk di data baru.'),
       ('Baseline', 'Model paling sederhana sebagai pembanding; ML harus mengalahkannya.')],
  cx=[P('Klasifikasi churn: baseline vs aturan sederhana vs k-NN', r'''
import random
random.seed(17)

def buat(n):
    data = []
    for _ in range(n):
        hari = random.randint(1, 120); order = random.randint(1, 20); keluhan = random.randint(0, 4)
        p = min(0.95, 0.05 + hari / 160 + keluhan * 0.12 - order * 0.015)
        data.append(((hari, order, keluhan), int(random.random() < p)))
    return data

data = buat(600)
latih, uji = data[:450], data[450:]
akurasi = lambda pred: sum(p == y for p, (_, y) in zip(pred, uji)) / len(uji)

mayoritas = round(sum(y for _, y in latih) / len(latih))
print(f"baseline (selalu tebak {mayoritas})     : {akurasi([mayoritas] * len(uji)):.1%}")
aturan = [int(x[0] > 60 or x[2] >= 3) for x, _ in uji]
print(f"aturan bisnis (>60 hari / ≥3 keluhan): {akurasi(aturan):.1%}")

def knn(x, k=15):
    skala = (120, 20, 4)
    jarak = sorted((sum(((a - b) / s) ** 2 for a, b, s in zip(x, xl, skala)), yl) for xl, yl in latih)
    return round(sum(y for _, y in jarak[:k]) / k)
print(f"k-NN (k=15)                          : {akurasi([knn(x) for x, _ in uji]):.1%}")
''', 'Model ML hanya layak dipakai bila jelas lebih baik dari baseline dan aturan sederhana. Untuk produksi gunakan scikit-learn dan validasi silang.')]),

'Investigasi penurunan konversi toko online': dict(
  ist=[('Root cause analysis', 'Menelusuri penyebab utama dengan memecah metrik per dimensi.'),
       ('Metric decomposition', 'Omzet = pengunjung × konversi × AOV; cari komponen yang berubah.'),
       ('Segmentation', 'Memecah per perangkat, kanal, wilayah, dan versi aplikasi.'),
       ('Simpson\'s paradox', 'Tren gabungan bisa berlawanan dengan tren tiap segmen karena perubahan komposisi.'),
       ('Hypothesis-driven analysis', 'Daftar hipotesis, data yang dibutuhkan, lalu terima atau tolak satu per satu.')],
  cx=[P('Memecah penurunan konversi per segmen', r'''
import pandas as pd
df = pd.DataFrame({
    "minggu": ["M1"] * 4 + ["M2"] * 4,
    "perangkat": ["Android", "iOS", "Desktop", "Android-baru"] * 2,
    "sesi": [21000, 6000, 9000, 0, 14000, 6100, 8800, 8000],
    "order": [567, 222, 279, 0, 378, 226, 270, 64],
})
tot = df.groupby("minggu")[["sesi", "order"]].sum()
tot["konversi"] = tot["order"] / tot["sesi"]
print("Gabungan:")
print(tot.assign(konversi=tot["konversi"].map("{:.2%}".format)).to_string())

seg = df[df.sesi > 0].assign(konversi=lambda d: d.order / d.sesi)
pv = seg.pivot_table(index="perangkat", columns="minggu", values="konversi")
pv["selisih_poin"] = (pv["M2"] - pv["M1"]) * 100
print("\nPer perangkat:")
print(pv.to_string(float_format=lambda x: f"{x:.3f}"))
print("\nTemuan: segmen lama stabil; penurunan berasal dari 'Android-baru' (aplikasi versi baru) dengan konversi",
      f"{64 / 8000:.1%}. Hipotesis: bug di checkout versi baru -> cek log error & rollback bertahap.")
''', 'Konversi gabungan turun dari 2,97% ke 2,54%, padahal Android lama, iOS, dan Desktop hampir tidak berubah. Pergeseran pengguna ke versi aplikasi baru yang bermasalah menjadi penyebabnya.')]),
}
