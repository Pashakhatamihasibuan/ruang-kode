"""Pendalaman jalur Python untuk Data Analysis: istilah dunia kerja dan contoh pandas/NumPy yang dijalankan."""
K = 'pda'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def S(t, code, lang='python', b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


DATA = '''import pandas as pd, numpy as np
rng = np.random.default_rng(7)
n = 600
df = pd.DataFrame({
    "order_id": np.arange(1001, 1001 + n),
    "tanggal": pd.Timestamp("2026-09-01") + pd.to_timedelta(rng.integers(0, 79, n), unit="D"),
    "kota": rng.choice(["Medan", "Bandung", "Surabaya", "Makassar"], n, p=[.3, .3, .25, .15]),
    "kategori": rng.choice(["Sembako", "Minuman", "Kebersihan", "Snack"], n),
    "qty": rng.integers(1, 6, n),
    "harga": rng.choice([8500, 12000, 23900, 31500, 78500], n),
})
df["total"] = df.qty * df.harga
'''

D = {
'Alur analisis data dengan Python': dict(
  ist=[('Business question', 'Pertanyaan yang ingin dijawab; menentukan data dan metrik yang dibutuhkan.'),
       ('EDA (Exploratory Data Analysis)', 'Penjelajahan awal: bentuk data, distribusi, nilai hilang, keanehan.'),
       ('Reproducible analysis', 'Analisis yang bisa dijalankan ulang orang lain dengan hasil sama (kode, versi library, seed).'),
       ('Insight vs observation', 'Observasi: "penjualan turun 12%". Insight: "turun karena stok minuman kosong 5 hari di Medan".')],
  cx=[P('Kerangka analisis: tanya → data → ringkas → rekomendasi', DATA + '''
print("Pertanyaan: kota dan kategori mana yang menyumbang omzet terbesar kuartal ini?")
print(f"Data: {len(df)} order, {df.tanggal.min():%d/%m} - {df.tanggal.max():%d/%m/%Y}")
ringkas = df.groupby("kota").total.sum().sort_values(ascending=False)
porsi = (ringkas / ringkas.sum() * 100).round(1)
print(pd.DataFrame({"omzet": ringkas, "porsi_%": porsi}))
print(f"Rekomendasi: fokus promosi di {ringkas.index[0]} dan {ringkas.index[1]} ({porsi.iloc[:2].sum():.0f}% omzet)")
''')]),

'Lingkungan: pip, conda, uv & venv': dict(
  ist=[('Virtual environment', 'Folder Python terpisah per proyek agar versi library tidak saling bentrok.'),
       ('requirements.txt / pyproject.toml', 'Daftar dependensi proyek; pyproject.toml adalah standar modern.'),
       ('Lock file', 'Mencatat versi pasti setiap paket (uv.lock, poetry.lock) agar hasil identik di semua mesin.'),
       ('uv', 'Pengelola paket dan venv berbasis Rust yang sangat cepat; banyak dipakai sejak 2024-2025.'),
       ('Kernel Jupyter', 'Lingkungan Python yang dipakai notebook; pastikan kernel sama dengan venv proyek.')],
  cx=[S('Menyiapkan proyek analisis dengan uv', '''
uv init analisis-penjualan && cd analisis-penjualan
uv add pandas matplotlib openpyxl          # menulis pyproject.toml + uv.lock
uv add --dev jupyterlab ruff pytest
uv run jupyter lab                          # jalan di venv proyek

# rekan tim cukup:
git clone ... && uv sync                    # memasang versi persis dari uv.lock

# padanan klasik
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
''', 'bash'),
      P('Mencatat versi library di awal notebook (bukti reproducible)', '''
import sys, importlib.metadata as md
print("Python", sys.version.split()[0])
for paket in ("pandas", "numpy", "matplotlib"):
    try:
        print(f"{paket:11} {md.version(paket)}")
    except md.PackageNotFoundError:
        print(f"{paket:11} belum terpasang")
''')]),

'Membaca file besar per potongan': dict(
  ist=[('Chunking', 'Membaca file per potongan (chunksize) agar tidak melebihi RAM.'),
       ('Streaming aggregation', 'Menjumlahkan hasil per potongan lalu menggabungkannya.'),
       ('usecols & dtype', 'Hanya memuat kolom yang dibutuhkan dengan tipe hemat memori.'),
       ('Out-of-core', 'Pengolahan data yang lebih besar dari memori; alatnya Polars streaming, DuckDB, Dask.')],
  cx=[P('Agregasi CSV besar per potongan dengan memori tetap', '''
import pandas as pd, numpy as np, io
rng = np.random.default_rng(0)
baris = 200_000
csv = io.StringIO()
pd.DataFrame({"kota": rng.choice(["Medan", "Bandung", "Surabaya"], baris),
              "total": rng.integers(5_000, 300_000, baris),
              "catatan": "kolom panjang yang tidak dipakai"}).to_csv(csv, index=False)
csv.seek(0)

hasil = None
for i, potong in enumerate(pd.read_csv(csv, usecols=["kota", "total"], dtype={"kota": "category"}, chunksize=50_000)):
    agg = potong.groupby("kota", observed=True).total.agg(["sum", "count"])
    hasil = agg if hasil is None else hasil.add(agg, fill_value=0)
print(f"{i + 1} potongan diproses")
hasil["rata"] = (hasil["sum"] / hasil["count"]).round(0)
print(hasil.astype("int64"))
''')]),

'Array NumPy & operasi vektor': dict(
  ist=[('ndarray', 'Array N-dimensi bertipe seragam; inti NumPy dan dasar pandas.'),
       ('Vectorized operation', 'Operasi pada seluruh array tanpa loop Python; puluhan kali lebih cepat.'),
       ('Universal function (ufunc)', 'Fungsi elemen-per-elemen seperti np.sqrt, np.log, np.where.'),
       ('dtype & memori', 'int64 = 8 byte per angka; int32/float32 menghemat separuh memori.')],
  cx=[P('Menghitung harga setelah diskon bertingkat dan PPN tanpa loop', '''
import numpy as np
harga = np.array([45_000, 120_000, 260_000, 510_000, 1_250_000])
diskon = np.where(harga >= 500_000, 0.15, np.where(harga >= 200_000, 0.10, 0.0))
setelah = harga * (1 - diskon)
ppn = np.round(setelah * 0.12)
print("diskon :", diskon)
print("bayar  :", (setelah + ppn).astype(int))
print("memori int64:", harga.nbytes, "byte | int32:", harga.astype(np.int32).nbytes, "byte")
''')]),

'Indexing, boolean mask & statistik': dict(
  ist=[('Boolean mask', 'Array True/False untuk memilih elemen yang memenuhi kondisi.'),
       ('Fancy indexing', 'Memilih elemen memakai array indeks, misalnya a[[0, 3, 5]].'),
       ('axis', 'Arah operasi: axis=0 per kolom (ke bawah), axis=1 per baris (ke samping).'),
       ('np.percentile', 'Persentil; p50 = median, p95 dipakai untuk metrik latensi.')],
  cx=[P('Latensi API: rata-rata menipu, persentil jujur', '''
import numpy as np
rng = np.random.default_rng(3)
latensi = np.concatenate([rng.normal(120, 20, 980), rng.normal(2_500, 300, 20)])   # 2% permintaan sangat lambat
lambat = latensi > 1_000
print(f"rata-rata : {latensi.mean():6.0f} ms")
print(f"p50       : {np.percentile(latensi, 50):6.0f} ms")
print(f"p95       : {np.percentile(latensi, 95):6.0f} ms")
print(f"p99       : {np.percentile(latensi, 99):6.0f} ms")
print(f"> 1 detik : {lambat.sum()} permintaan ({lambat.mean():.1%})")
per_jam = latensi.reshape(10, 100)                   # 10 jam x 100 permintaan
print("p95 per jam:", np.percentile(per_jam, 95, axis=1).round(0))
''')]),

'Series & DataFrame': dict(
  ist=[('Index', 'Label baris; bisa angka, tanggal, atau kode. Banyak operasi pandas menyelaraskan berdasarkan index.'),
       ('Alignment', 'Operasi dua Series menyamakan label dulu; label tanpa pasangan menjadi NaN.'),
       ('dtypes', 'Tipe tiap kolom; cek selalu setelah membaca data.'),
       ('Tidy data', 'Satu kolom satu variabel, satu baris satu observasi; format paling mudah dianalisis.')],
  cx=[P('Index alignment: jebakan yang sering membuat NaN', '''
import pandas as pd
target = pd.Series({"Medan": 100, "Bandung": 120, "Surabaya": 90})
realisasi = pd.Series({"Bandung": 130, "Medan": 95, "Makassar": 40})
print((realisasi / target * 100).round(1))           # urutan tidak penting, label yang dipasangkan
print("\\nDengan fill_value:")
print(realisasi.div(target, fill_value=0).mul(100).round(1).replace(float("inf"), float("nan")))
''', 'Makassar tidak punya target sehingga hasilnya NaN; ini sinyal data master perlu dilengkapi, bukan bug pandas.')]),

'Membaca CSV, Excel, JSON & web': dict(
  ist=[('Encoding', 'Cara teks disimpan; file Excel lama dari Windows sering cp1252/latin-1, bukan UTF-8.'),
       ('Delimiter & decimal', 'File CSV lokal Indonesia sering memakai ; sebagai pemisah dan , sebagai desimal.'),
       ('json_normalize', 'Meratakan JSON bersarang dari API menjadi tabel.'),
       ('Schema on read', 'Menentukan tipe kolom saat membaca (dtype, parse_dates) agar tidak salah tebak.')],
  cx=[P('CSV gaya Indonesia dan JSON API bersarang', '''
import pandas as pd, io
csv_id = io.StringIO("tanggal;produk;harga;qty\\n18/11/2026;Kopi 200g;31.500,00;2\\n19/11/2026;Gula 1kg;17.250,50;3\\n")
df = pd.read_csv(csv_id, sep=";", decimal=",", thousands=".", parse_dates=["tanggal"], dayfirst=True)
print(df.dtypes.to_dict())
print(df.assign(total=df.harga * df.qty))

api = [{"id": 1, "pelanggan": {"nama": "Rina", "kota": "Medan"}, "item": [{"sku": "K1", "qty": 2}, {"sku": "G1", "qty": 1}]},
       {"id": 2, "pelanggan": {"nama": "Dodi", "kota": "Bandung"}, "item": [{"sku": "K1", "qty": 1}]}]
print(pd.json_normalize(api, record_path="item", meta=["id", ["pelanggan", "kota"]]))
''')]),

'Memilih & menyaring: loc, iloc, query': dict(
  ist=[('loc', 'Memilih berdasarkan label dan kondisi: df.loc[mask, ["kolom"]].'),
       ('iloc', 'Memilih berdasarkan posisi angka: df.iloc[:5, 0:3].'),
       ('query', 'Filter dengan ekspresi string yang mudah dibaca; variabel luar dipanggil dengan @.'),
       ('SettingWithCopyWarning', 'Peringatan saat mengubah salinan hasil filter; gunakan .loc atau .copy(). Di pandas 3 Copy-on-Write menjadi bawaan.')],
  cx=[P('Tiga cara menyaring yang sama', DATA + '''
batas = 200_000
a = df.loc[(df.kota == "Medan") & (df.total >= batas), ["order_id", "kategori", "total"]]
b = df.query("kota == 'Medan' and total >= @batas")[["order_id", "kategori", "total"]]
c = df[df.kota.eq("Medan") & df.total.ge(batas)].filter(["order_id", "kategori", "total"])
print("hasil sama:", a.equals(b) and b.equals(c), "|", len(a), "order")
print(a.sort_values("total", ascending=False).head(3).to_string(index=False))
print("posisi baris 0-2, kolom 0-2 (iloc):")
print(df.iloc[:3, :3])
''')]),

'Nilai hilang: isna, dropna, fillna, ffill': dict(
  ist=[('MCAR / MAR / MNAR', 'Jenis nilai hilang: acak total, bergantung variabel lain, atau bergantung nilainya sendiri. Menentukan cara menanganinya.'),
       ('Imputation', 'Mengisi nilai hilang dengan median, modus, nilai sebelumnya, atau model.'),
       ('Forward fill', 'Mengisi dengan nilai terakhir yang diketahui; cocok untuk data sensor/harga.'),
       ('Missing indicator', 'Kolom penanda "dulu kosong" agar informasi kekosongan tidak hilang.')],
  cx=[P('Strategi berbeda untuk kolom berbeda', '''
import pandas as pd, numpy as np
df = pd.DataFrame({
    "tanggal": pd.date_range("2026-11-10", periods=7),
    "harga_cabai": [62_000, np.nan, np.nan, 65_000, 66_000, np.nan, 70_000],
    "kota": ["Medan", None, "Medan", "Medan", None, "Medan", "Medan"],
    "rating": [4.5, np.nan, 4.0, np.nan, 5.0, 3.5, np.nan],
})
print("jumlah kosong:", df.isna().sum().to_dict())
bersih = df.assign(
    harga_cabai=df.harga_cabai.ffill(),                        # harga pasar: pakai harga terakhir
    kota=df.kota.fillna(df.kota.mode()[0]),                    # kategori: modus
    rating_kosong=df.rating.isna().astype(int),                # simpan informasi kekosongan
    rating=df.rating.fillna(df.rating.median()),               # numerik: median
)
print(bersih.to_string(index=False))
''')]),

'Teks, tanggal & tipe data': dict(
  ist=[('.str accessor', 'Operasi teks vektor: strip, lower, contains, extract dengan regex.'),
       ('.dt accessor', 'Komponen tanggal: year, month, day_name, to_period.'),
       ('Timezone', 'Data server sering UTC; laporan Indonesia butuh Asia/Jakarta (WIB), Asia/Makassar, Asia/Jayapura.'),
       ('category dtype', 'Tipe hemat memori untuk kolom dengan sedikit nilai unik.')],
  cx=[P('Merapikan nomor HP, mengekstrak kode, dan konversi UTC ke WIB', '''
import pandas as pd
df = pd.DataFrame({
    "hp": ["0812-3456-7890", "+62 813 1111 2222", "62857 0000 1111", " 08991234567 "],
    "invoice": ["INV/MDN/2026/0012", "INV/BDG/2026/0450", "INV/SBY/2026/0007", "INV/MDN/2026/0013"],
    "waktu_utc": pd.to_datetime(["2026-11-18 23:30", "2026-11-19 01:15", "2026-11-19 10:00", "2026-11-19 16:45"], utc=True),
})
df["hp"] = df.hp.str.replace(r"\\D", "", regex=True).str.replace(r"^(62|0)", "+62", regex=True)
df["cabang"] = df.invoice.str.extract(r"INV/([A-Z]{3})/")
df["waktu_wib"] = df.waktu_utc.dt.tz_convert("Asia/Jakarta")
df["hari"] = df.waktu_wib.dt.day_name()
print(df[["hp", "cabang", "waktu_wib", "hari"]].to_string(index=False))
''', 'Order 23:30 UTC tanggal 18 sebenarnya terjadi tanggal 19 pukul 06:30 WIB. Laporan harian yang lupa konversi akan salah hari.')]),

'Duplikat & encoding kategori': dict(
  ist=[('Exact vs fuzzy duplicate', 'Duplikat persis vs mirip ("Toko Maju" dan "TOKO MAJU "). Fuzzy butuh normalisasi dulu.'),
       ('Dedup key', 'Kolom penentu keunikan; pilih dengan sadar, misalnya order_id, bukan seluruh baris.'),
       ('One-hot encoding', 'Mengubah kategori menjadi kolom 0/1 (get_dummies) untuk model.'),
       ('Ordinal encoding', 'Kategori berurutan (S < M < L) diubah ke angka berurutan.')],
  cx=[P('Normalisasi sebelum dedup, lalu encoding', '''
import pandas as pd
df = pd.DataFrame({
    "toko": ["Toko Maju", "TOKO MAJU ", "Toko  Maju", "Sinar Jaya", "Sinar Jaya"],
    "ukuran": ["M", "L", "M", "S", "S"],
    "kota": ["Medan", "Medan", "Medan", "Bandung", "Bandung"],
})
print("duplikat persis:", df.duplicated().sum())
df["toko_norm"] = df.toko.str.upper().str.split().str.join(" ")
print("duplikat setelah normalisasi:", df.duplicated(["toko_norm", "ukuran"]).sum())
unik = df.drop_duplicates(["toko_norm", "ukuran"]).copy()
unik["ukuran_ord"] = unik.ukuran.map({"S": 1, "M": 2, "L": 3})
print(pd.get_dummies(unik[["toko_norm", "ukuran_ord", "kota"]], columns=["kota"], dtype=int).to_string(index=False))
''')]),

'groupby & agregasi': dict(
  ist=[('Split-apply-combine', 'Pola groupby: pecah per kelompok, terapkan fungsi, gabungkan hasil.'),
       ('Named aggregation', 'agg(omzet=("total", "sum")) agar nama kolom hasil jelas.'),
       ('transform', 'Hasil agregasi dikembalikan sepanjang data asli; untuk porsi per kelompok atau z-score per grup.'),
       ('Weighted average', 'Rata-rata berbobot, misalnya harga rata-rata per unit = total ÷ qty, bukan mean(harga).')],
  cx=[P('Ringkasan per kota, porsi per kategori, dan rata-rata berbobot', DATA + '''
ringkas = df.groupby("kota").agg(order=("order_id", "count"), unit=("qty", "sum"), omzet=("total", "sum"))
ringkas["harga_per_unit"] = (ringkas.omzet / ringkas.unit).round(0)      # berbobot, bukan mean(harga)
print(ringkas.sort_values("omzet", ascending=False))
df["porsi_di_kota"] = df.total / df.groupby("kota").total.transform("sum")
top = df.groupby(["kota", "kategori"]).porsi_di_kota.sum().mul(100).round(1).unstack()
print(top)
''')]),

'merge & concat': dict(
  ist=[('Join type', 'inner, left, right, outer; left join paling sering dipakai untuk memperkaya data.'),
       ('Cardinality', 'one-to-one, one-to-many, many-to-many; many-to-many tak sengaja membuat baris berlipat.'),
       ('validate=', 'Parameter merge yang memastikan kardinalitas sesuai harapan, misalnya "many_to_one".'),
       ('indicator=True', 'Menambah kolom _merge untuk melihat baris yang tidak punya pasangan.')],
  cx=[P('Merge aman dengan validate dan indicator', '''
import pandas as pd
order = pd.DataFrame({"order_id": [1, 2, 3, 4], "kode_toko": ["MDN1", "BDG1", "MDN1", "SBY9"], "total": [100, 250, 80, 60]})
toko = pd.DataFrame({"kode_toko": ["MDN1", "BDG1", "SBY1"], "kota": ["Medan", "Bandung", "Surabaya"]})
hasil = order.merge(toko, on="kode_toko", how="left", validate="many_to_one", indicator=True)
print(hasil)
print("tanpa pasangan:", hasil.loc[hasil._merge == "left_only", "kode_toko"].tolist())

toko_dobel = pd.concat([toko, pd.DataFrame({"kode_toko": ["MDN1"], "kota": ["Medan (lama)"]})])
try:
    order.merge(toko_dobel, on="kode_toko", validate="many_to_one")
except pd.errors.MergeError as e:
    print("ditolak:", str(e)[:60])
''', 'Tanpa validate, master toko yang dobel diam-diam menggandakan order MDN1 dan omzet ikut membengkak.')]),

'pivot_table, crosstab & melt': dict(
  ist=[('Wide vs long format', 'Wide: satu kolom per bulan (enak dibaca). Long: satu baris per bulan (enak diolah).'),
       ('pivot_table', 'Membuat tabel ringkasan dua dimensi dengan fungsi agregasi dan margins (total).'),
       ('crosstab', 'Tabel frekuensi dua variabel; normalize untuk persentase.'),
       ('melt', 'Kebalikan pivot: wide menjadi long.')],
  cx=[P('Laporan bulanan wide, lalu kembali ke long', DATA + '''
df["bulan"] = df.tanggal.dt.strftime("%Y-%m")
wide = df.pivot_table(index="kota", columns="bulan", values="total", aggfunc="sum", margins=True, margins_name="Total")
print((wide / 1e6).round(1), "(juta rupiah)\\n")
print(pd.crosstab(df.kota, df.kategori, normalize="index").mul(100).round(0), "\\n")
long = wide.drop(index="Total", columns="Total").reset_index().melt(id_vars="kota", var_name="bulan", value_name="omzet")
print(long.head(4))
''')]),

'Rantai transformasi dengan assign & pipe': dict(
  ist=[('Method chaining', 'Menulis transformasi sebagai rantai metode tanpa variabel sementara; mudah dibaca atas-bawah.'),
       ('assign', 'Membuat/mengganti kolom di tengah rantai; menerima lambda yang melihat DataFrame terbaru.'),
       ('pipe', 'Memasukkan fungsi buatan sendiri ke dalam rantai.'),
       ('Pure transformation function', 'Fungsi yang menerima DataFrame dan mengembalikan DataFrame baru; mudah dites.')],
  cx=[P('Pipeline pembersihan yang bisa dites per langkah', '''
import pandas as pd

def buang_uji_coba(d):
    return d[~d.pelanggan.str.contains("test", case=False)]

def tandai_besar(d, batas):
    return d.assign(besar=d.total >= batas)

mentah = pd.DataFrame({"pelanggan": ["rina", "TEST user", "dodi", "sari"], "total": ["125000", "1", "98000", "450000"],
                       "tgl": ["2026-11-18", "2026-11-18", "2026-11-19", "2026-11-19"]})
hasil = (mentah
         .pipe(buang_uji_coba)
         .assign(total=lambda d: d.total.astype(int),
                 tgl=lambda d: pd.to_datetime(d.tgl),
                 pelanggan=lambda d: d.pelanggan.str.title())
         .pipe(tandai_besar, batas=200_000)
         .sort_values("total", ascending=False)
         .reset_index(drop=True))
print(hasil)
assert len(buang_uji_coba(mentah)) == 3
''')]),

'Pemusatan & sebaran': dict(
  ist=[('Mean vs median', 'Mean peka outlier; median lebih jujur untuk gaji, harga rumah, nilai transaksi.'),
       ('Standard deviation', 'Ukuran sebaran rata-rata dari mean.'),
       ('IQR', 'Rentang antar kuartil (Q3 − Q1); sebaran 50% data tengah, tahan outlier.'),
       ('Coefficient of variation', 'std ÷ mean; membandingkan kestabilan dua hal berbeda skala.')],
  cx=[P('Gaji tim: mean menyesatkan, median dan IQR lebih jujur', '''
import pandas as pd
gaji = pd.Series([6.5, 7, 7.2, 7.5, 8, 8.2, 8.5, 9, 9.5, 65], name="juta/bulan")   # satu direktur
print(f"mean   : {gaji.mean():.1f} juta")
print(f"median : {gaji.median():.1f} juta")
q1, q3 = gaji.quantile([.25, .75])
print(f"IQR    : {q3 - q1:.2f} juta (Q1 {q1:.2f}, Q3 {q3:.2f})")
penjualan = pd.DataFrame({"Cabang A": [100, 102, 98, 101, 99], "Cabang B": [60, 140, 90, 30, 180]})
print("koefisien variasi:", (penjualan.std() / penjualan.mean()).round(2).to_dict())
''')]),

'Outlier: IQR & z-score': dict(
  ist=[('Tukey fences', 'Batas outlier Q1 − 1,5×IQR dan Q3 + 1,5×IQR.'),
       ('z-score', '(x − mean) ÷ std; |z| > 3 sering dianggap ekstrem untuk data mendekati normal.'),
       ('Robust z-score (MAD)', 'Memakai median dan median absolute deviation; tidak ikut terpengaruh outlier.'),
       ('Outlier ≠ error', 'Outlier bisa data salah ketik atau kejadian nyata penting (pembelian grosir, fraud). Selidiki dulu sebelum dibuang.')],
  cx=[P('Tiga metode pada transaksi yang sama', '''
import pandas as pd, numpy as np
x = pd.Series([52, 48, 55, 61, 47, 50, 58, 53, 49, 900, 51, 56, 5_000], name="ribu_rp")
q1, q3 = x.quantile([.25, .75]); iqr = q3 - q1
iqr_out = x[(x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)]
z = (x - x.mean()) / x.std()
mad = (x - x.median()).abs().median()
rz = 0.6745 * (x - x.median()) / mad
print("IQR          :", iqr_out.tolist())
print("z-score > 3  :", x[z.abs() > 3].tolist(), "<- 900 lolos karena std ikut membengkak")
print("robust z > 3.5:", x[rz.abs() > 3.5].tolist())
''')]),

'Korelasi': dict(
  ist=[('Pearson', 'Mengukur hubungan linear; peka outlier.'),
       ('Spearman', 'Berbasis peringkat; menangkap hubungan monoton dan tahan outlier.'),
       ('Correlation ≠ causation', 'Es krim dan kasus tenggelam sama-sama naik di musim panas; penyebabnya cuaca.'),
       ('Confounder', 'Variabel ketiga yang memengaruhi keduanya.')],
  cx=[P('Pearson vs Spearman dan contoh confounder', '''
import pandas as pd, numpy as np
rng = np.random.default_rng(1)
suhu = rng.uniform(24, 36, 60)
es_krim = 20 * suhu + rng.normal(0, 25, 60)
listrik_ac = 15 * suhu + rng.normal(0, 25, 60)
df = pd.DataFrame({"suhu": suhu, "es_krim": es_krim, "listrik_ac": listrik_ac})
print(df.corr().round(2))
print("\\nes_krim vs listrik_ac tinggi karena keduanya dipengaruhi suhu (confounder).")
iklan = pd.Series([1, 2, 3, 4, 5, 6, 7, 8]); penjualan = pd.Series([10, 20, 28, 35, 40, 44, 47, 300])
print(f"Pearson {iklan.corr(penjualan):.2f} | Spearman {iklan.corr(penjualan, method='spearman'):.2f}")
''')]),

'Deret waktu: resample & rolling': dict(
  ist=[('Resample', 'Mengubah frekuensi: harian ke mingguan (W), bulanan (ME), dst.'),
       ('Rolling window', 'Jendela bergerak, misalnya rata-rata 7 hari untuk meredam fluktuasi harian.'),
       ('Seasonality', 'Pola berulang (akhir pekan, gajian, Ramadan, Harbolnas 12.12).'),
       ('YoY / MoM / WoW', 'Pertumbuhan dibanding tahun/bulan/minggu sebelumnya.')],
  cx=[P('Penjualan harian: rata-rata 7 hari, mingguan, dan WoW', '''
import pandas as pd, numpy as np
rng = np.random.default_rng(5)
hari = pd.date_range("2026-10-05", "2026-11-15", freq="D")   # Senin s.d. Minggu, 6 minggu penuh
efek_akhir_pekan = np.where(hari.dayofweek >= 5, 1.4, 1.0)
efek_gajian = np.where(hari.day >= 25, 1.25, 1.0)
s = pd.Series((1_000 * efek_akhir_pekan * efek_gajian + rng.normal(0, 80, len(hari))).round(), index=hari)
mingguan = s.resample("W-SUN").sum()
print(pd.DataFrame({"omzet_ribu": mingguan, "WoW_%": mingguan.pct_change().mul(100).round(1)}).tail(4))
print("rata-rata 7 hari terakhir:", s.rolling(7).mean().iloc[-1].round(0))
print("rata-rata per hari:", s.groupby(s.index.day_name()).mean().round(0).sort_values().to_dict())
''')]),

'Memilih grafik yang tepat': dict(
  ist=[('Chart chooser', 'Perbandingan: bar; tren: line; distribusi: histogram/box; komposisi: stacked bar; hubungan: scatter.'),
       ('Data-ink ratio', 'Prinsip Tufte: kurangi ornamen yang tidak membawa informasi.'),
       ('Pre-attentive attribute', 'Warna, ukuran, posisi yang langsung ditangkap mata; pakai satu warna sorotan untuk pesan utama.'),
       ('Axis truncation', 'Sumbu y bar chart yang tidak mulai dari nol membesar-besarkan selisih.')],
  cx=[P('Bar chart horizontal dengan satu warna sorotan', DATA + '''
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
omzet = df.groupby("kategori").total.sum().sort_values() / 1e6
warna = ["#c2410c" if k == omzet.idxmax() else "#a8a29e" for k in omzet.index]
fig, ax = plt.subplots(figsize=(6, 3))
ax.barh(omzet.index, omzet.values, color=warna)
ax.set_xlabel("Omzet (juta rupiah)"); ax.set_title(f"{omzet.idxmax()} menyumbang omzet terbesar", loc="left")
for s in ("top", "right"): ax.spines[s].set_visible(False)
for y, v in enumerate(omzet.values): ax.text(v, y, f" {v:.1f}", va="center")
fig.tight_layout(); fig.savefig("/tmp/omzet_kategori.png", dpi=120)
print(omzet.round(1).to_dict())
print("judul berisi kesimpulan, bukan sekadar 'Omzet per kategori'")
''')]),

'Grafik interaktif & dashboard': dict(
  ist=[('Plotly Express', 'Grafik interaktif (hover, zoom) dengan satu baris kode; bisa diekspor ke HTML.'),
       ('Streamlit', 'Membuat aplikasi dashboard dari skrip Python tanpa HTML/JS.'),
       ('Caching', 'st.cache_data agar data tidak dimuat ulang setiap interaksi.'),
       ('Self-service analytics', 'Pengguna bisnis memfilter sendiri tanpa meminta analis setiap kali.')],
  cx=[S('Dashboard penjualan dengan Streamlit + Plotly', '''
# app.py  ->  jalankan: streamlit run app.py
import pandas as pd, plotly.express as px, streamlit as st

st.set_page_config(page_title="Penjualan Toko Nusantara", layout="wide")

@st.cache_data(ttl=3600)
def muat():
    return pd.read_parquet("data/penjualan.parquet")

df = muat()
kota = st.sidebar.multiselect("Kota", sorted(df.kota.unique()), default=sorted(df.kota.unique()))
rentang = st.sidebar.date_input("Periode", (df.tanggal.min(), df.tanggal.max()))
f = df[df.kota.isin(kota) & df.tanggal.between(*map(pd.Timestamp, rentang))]

k1, k2, k3 = st.columns(3)
k1.metric("Omzet", f"Rp{f.total.sum()/1e6:,.1f} jt")
k2.metric("Order", f"{len(f):,}")
k3.metric("Rata-rata order", f"Rp{f.total.mean():,.0f}")

harian = f.groupby([pd.Grouper(key="tanggal", freq="D"), "kota"]).total.sum().reset_index()
st.plotly_chart(px.line(harian, x="tanggal", y="total", color="kota", title="Omzet harian"), use_container_width=True)
st.dataframe(f.sort_values("tanggal", ascending=False).head(100), hide_index=True)
''')]),

'SQL dari Python: sqlite3 & read_sql': dict(
  ist=[('Parameterized query', 'Nilai dikirim terpisah (?) untuk mencegah SQL injection; jangan pakai f-string.'),
       ('Push down computation', 'Biarkan database menyaring dan mengagregasi; tarik hasil kecil ke pandas.'),
       ('Connection string', 'Alamat database (postgresql://user@host/db); simpan di environment variable, bukan di kode.'),
       ('to_sql', 'Menulis DataFrame ke tabel; pakai if_exists dan chunksize.')],
  cx=[P('Query berparameter dan push down agregasi', DATA + '''
import sqlite3
con = sqlite3.connect(":memory:")
df.assign(tanggal=df.tanggal.dt.strftime("%Y-%m-%d")).to_sql("penjualan", con, index=False)

kota = "Medan'; DROP TABLE penjualan; --"         # input jahat
aman = pd.read_sql("SELECT COUNT(*) n FROM penjualan WHERE kota = ?", con, params=(kota,))
print("query berparameter aman, hasil:", aman.n.iloc[0])

ringkas = pd.read_sql("""
    SELECT substr(tanggal, 1, 7) AS bulan, kota, COUNT(*) AS trx, SUM(total) AS omzet
    FROM penjualan WHERE tanggal >= ? GROUP BY 1, 2 ORDER BY 1, omzet DESC""", con, params=("2026-11-01",))
print(f"ditarik {len(ringkas)} baris, bukan {len(df)}")
print(ringkas)
''')]),

'Polars, Dask & PySpark': dict(
  ist=[('Polars', 'DataFrame berbasis Rust dengan lazy API dan eksekusi paralel; sering 5-20x lebih cepat dari pandas.'),
       ('Lazy evaluation', 'Rencana query dioptimasi dulu (predicate/projection pushdown) baru dijalankan dengan collect().'),
       ('DuckDB', 'Database analitik in-process; menjalankan SQL langsung di file Parquet/CSV.'),
       ('Kapan pindah dari pandas', 'Data > RAM, proses terlalu lambat, atau pipeline produksi terjadwal.')],
  cx=[S('Pertanyaan yang sama di pandas, Polars, DuckDB, dan PySpark', '''
# pandas
df.query("tanggal >= '2026-11-01'").groupby("kota").agg(omzet=("total", "sum")).sort_values("omzet")

# Polars (lazy: hanya membaca kolom dan baris yang perlu)
import polars as pl
(pl.scan_parquet("penjualan/*.parquet")
   .filter(pl.col("tanggal") >= pl.date(2026, 11, 1))
   .group_by("kota").agg(pl.col("total").sum().alias("omzet"))
   .sort("omzet").collect())

# DuckDB (SQL langsung di file)
import duckdb
duckdb.sql("""SELECT kota, SUM(total) omzet FROM 'penjualan/*.parquet'
              WHERE tanggal >= DATE '2026-11-01' GROUP BY kota ORDER BY omzet""").df()

# PySpark (data di cluster)
from pyspark.sql import functions as F
(spark.read.parquet("s3://lake/penjualan/").where(F.col("tanggal") >= "2026-11-01")
      .groupBy("kota").agg(F.sum("total").alias("omzet")).orderBy("omzet").show())
''')]),

'Pengantar scikit-learn': dict(
  ist=[('Estimator API', 'Pola seragam fit() → predict()/transform() untuk semua model.'),
       ('Train/test split', 'Memisahkan data uji yang tidak pernah dilihat saat latihan.'),
       ('Pipeline & ColumnTransformer', 'Menggabungkan preprocessing dan model agar tidak terjadi data leakage.'),
       ('Baseline', 'Model paling sederhana (DummyRegressor) sebagai patokan yang harus dikalahkan.')],
  cx=[P('Prediksi nilai order: baseline vs regresi linear dalam Pipeline', DATA + '''
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

X = df[["kota", "kategori", "qty"]]; y = df.total
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)
prep = ColumnTransformer([("kat", OneHotEncoder(handle_unknown="ignore"), ["kota", "kategori"])], remainder="passthrough")
for nama, model in [("baseline (rata-rata)", DummyRegressor()), ("regresi linear", LinearRegression())]:
    pipa = make_pipeline(prep, model).fit(X_tr, y_tr)
    print(f"{nama:22} MAE = Rp{mean_absolute_error(y_te, pipa.predict(X_te)):,.0f}".replace(",", "."))
''', 'Kalau model tidak jauh lebih baik dari baseline, fiturnya belum cukup menjelaskan nilai order (di sini harga produk tidak dimasukkan).')]),

'Analisis penjualan Toko Nusantara': dict(
  ist=[('Executive summary', 'Tiga sampai lima kalimat di awal laporan: temuan utama dan rekomendasi.'),
       ('Cohort / RFM', 'Segmentasi pelanggan berdasarkan Recency, Frequency, Monetary.'),
       ('Actionable insight', 'Temuan yang jelas tindak lanjutnya, pemiliknya, dan cara mengukurnya.'),
       ('Notebook to report', 'Notebook dirapikan menjadi laporan (Quarto, Jupyter Book, slide) untuk pembaca non-teknis.')],
  cx=[P('Segmentasi RFM sederhana untuk rekomendasi kampanye', DATA + '''
df["pelanggan"] = rng.integers(1, 121, n)
acuan = df.tanggal.max() + pd.Timedelta(days=1)
rfm = df.groupby("pelanggan").agg(recency=("tanggal", lambda t: (acuan - t.max()).days),
                                  frequency=("order_id", "count"), monetary=("total", "sum"))
rfm["R"] = pd.qcut(rfm.recency, 3, labels=[3, 2, 1]).astype(int)
rfm["F"] = pd.qcut(rfm.frequency.rank(method="first"), 3, labels=[1, 2, 3]).astype(int)
rfm["segmen"] = np.select([(rfm.R == 3) & (rfm.F == 3), (rfm.R == 1) & (rfm.F >= 2), rfm.R == 1],
                          ["Juara", "Berisiko hilang", "Tidur"], "Potensial")
ring = rfm.groupby("segmen").agg(pelanggan=("R", "size"), omzet=("monetary", "sum"))
ring["porsi_omzet_%"] = (ring.omzet / ring.omzet.sum() * 100).round(1)
print(ring.sort_values("omzet", ascending=False))
print("Aksi: voucher comeback untuk 'Berisiko hilang', program poin untuk 'Juara'.")
''')]),
}
