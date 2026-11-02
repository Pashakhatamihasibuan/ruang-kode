"""Soal latihan tambahan untuk jalur Python Analisis Data, Data Analyst, BI Analyst, dan Data Engineer.

Keluaran soal Python ditulis RUN lalu diisi otomatis oleh isi_keluaran.py dengan menjalankan jawabannya.
"""
from mobile_dart_x import S


def P(q, h, a, out=None): return S(q, h, a, out, lang='python')
def Tx(q, h, a): return S(q, h, a, lang='text')
def Bs(q, h, a): return S(q, h, a, lang='bash')
def Sq(q, h, a): return S(q, h, a, lang='sql')
def Ym(q, h, a): return S(q, h, a, lang='yaml')
def Xl(q, h, a): return S(q, h, a, lang='excel')
def Js(q, h, a): return S(q, h, a, lang='json')


PDA = {
'Alur analisis data dengan Python': [
  Tx('Tulis rencana analisis (pertanyaan, data, pembersihan, eksplorasi, simpulan, komunikasi) untuk: "Kenapa penjualan es kopi turun bulan Oktober?"', 'Ikuti enam langkah: tanya, kumpulkan, bersihkan, eksplorasi, simpulkan, komunikasikan.',
     'Pertanyaan : penjualan es kopi Oktober turun berapa persen, di cabang mana, sejak kapan?\nData       : ekspor kasir Agustus-Oktober, data cuaca harian, daftar promo\nBersihkan  : samakan nama produk, buang transaksi batal, tanggal ke datetime\nEksplorasi : omzet harian per cabang, bandingkan hari hujan vs cerah, cek promo berakhir\nSimpulan   : penurunan 18% terpusat di 2 cabang, bertepatan dengan musim hujan dan promo selesai\nKomunikasi : 1 grafik garis per cabang + 3 kalimat rekomendasi'),
  Tx('Kapan memakai JupyterLab, Google Colab, dan VS Code untuk analisis?', 'Bandingkan instalasi, berbagi, dan kebutuhan proyek.',
     'JupyterLab : di komputer sendiri, data sensitif tetap lokal.\nColab      : tanpa instalasi, mudah dibagikan, ada GPU gratis terbatas.\nVS Code    : notebook + skrip + Git dalam satu editor, cocok saat analisis jadi proyek kode.'),
],
'Lingkungan: pip, conda, uv & venv': [
  Bs('Buat lingkungan proyek analisis dengan uv, pasang pandas dan seaborn, lalu jalankan JupyterLab.', 'uv venv, uv pip install, lalu jalankan jupyter dari lingkungan itu.',
     'uv venv\nsource .venv/bin/activate\nuv pip install pandas seaborn jupyterlab\nuv pip freeze > requirements.txt\njupyter lab'),
  Bs('Buat lingkungan conda bernama "analisis" dengan Python 3.12 dan pandas, lalu ekspor ke file.', 'conda create -n nama python=versi paket; conda env export.',
     'conda create -n analisis python=3.12 pandas matplotlib -y\nconda activate analisis\nconda env export > environment.yml\n# rekan: conda env create -f environment.yml'),
],
'Array NumPy & operasi vektor': [
  P('Harga 5 produk <code>[18000, 25000, 12000, 30000, 9000]</code>. Dengan NumPy, beri diskon 10%, tambah PPN 11%, lalu bulatkan ke rupiah.', 'Operasi vektor berlaku ke semua elemen tanpa loop.',
    'import numpy as np\n\nharga = np.array([18000, 25000, 12000, 30000, 9000])\nakhir = np.round(harga * 0.9 * 1.11).astype(int)\nprint(akhir)\nprint(akhir.sum())', '[17982 24975 11988 29970  8991]\n93906'),
  P('Buat array 1 sampai 12, ubah menjadi 3 baris x 4 kolom, lalu hitung jumlah tiap kolom dan tiap baris.', 'np.arange, reshape, sum(axis=0) untuk kolom, axis=1 untuk baris.',
    'import numpy as np\n\nm = np.arange(1, 13).reshape(3, 4)\nprint(m)\nprint(m.sum(axis=0))\nprint(m.sum(axis=1))', '[[ 1  2  3  4]\n [ 5  6  7  8]\n [ 9 10 11 12]]\n[15 18 21 24]\n[10 26 42]'),
],
'Indexing, boolean mask & statistik': [
  P('Dari nilai ujian <code>[78, 92, 55, 61, 88, 47, 95]</code>, ambil yang lulus (&gt;= 60), hitung rata-rata dan jumlah yang lulus.', 'mask = nilai >= 60; nilai[mask].',
    'import numpy as np\n\nnilai = np.array([78, 92, 55, 61, 88, 47, 95])\nlulus = nilai[nilai >= 60]\nprint(lulus)\nprint(lulus.mean().round(1), (nilai >= 60).sum())', '[78 92 61 88 95]\n82.8 5'),
  P('Ganti semua nilai di bawah 60 menjadi 60 (remedial) memakai <code>np.where</code>, lalu cetak nilai maksimum, minimum, dan simpangan bakunya.', 'np.where(kondisi, jika_benar, jika_salah).',
    'import numpy as np\n\nnilai = np.array([78, 92, 55, 61, 88, 47, 95])\nbaru = np.where(nilai < 60, 60, nilai)\nprint(baru)\nprint(baru.max(), baru.min(), baru.std().round(2))', '[78 92 60 61 88 60 95]\n95 60 14.65'),
],
'Series & DataFrame': [
  P('Buat DataFrame 4 produk (nama, kategori, harga, stok), tambah kolom nilai_stok = harga x stok, lalu tampilkan info bentuk dan tipe kolom.', 'pd.DataFrame(dict), df["baru"] = ..., df.shape, df.dtypes.',
    'import pandas as pd\n\ndf = pd.DataFrame({\n    "nama": ["Kopi", "Teh", "Roti", "Susu"],\n    "kategori": ["Minuman", "Minuman", "Makanan", "Minuman"],\n    "harga": [18000, 8000, 12000, 15000],\n    "stok": [20, 50, 15, 30],\n})\ndf["nilai_stok"] = df["harga"] * df["stok"]\nprint(df)\nprint(df.shape)', '   nama kategori  harga  stok  nilai_stok\n0  Kopi  Minuman  18000    20      360000\n1   Teh  Minuman   8000    50      400000\n2  Roti  Makanan  12000    15      180000\n3  Susu  Minuman  15000    30      450000\n(4, 5)'),
  P('Buat Series omzet per hari dengan indeks nama hari, lalu ambil hari dengan omzet tertinggi dan rata-ratanya.', 'pd.Series(nilai, index=...), idxmax(), mean().',
    'import pandas as pd\n\nomzet = pd.Series([1.2, 0.9, 1.5, 2.1, 2.8], index=["Sen", "Sel", "Rab", "Kam", "Jum"])\nprint(omzet.idxmax(), omzet.max())\nprint(round(omzet.mean(), 2))', 'Jum 2.8\n1.7'),
],
'Membaca CSV, Excel, JSON & web': [
  P('Baca CSV gaya Indonesia (pemisah titik koma, desimal koma, tanggal dd/mm/yyyy) dari teks berikut.', 'sep=";", decimal=",", lalu pd.to_datetime dengan format. io.StringIO untuk teks.',
    'import io\nimport pandas as pd\n\nteks = """tanggal;produk;harga\n01/10/2026;Kopi;18500,5\n02/10/2026;Teh;8000\n"""\ndf = pd.read_csv(io.StringIO(teks), sep=";", decimal=",")\ndf["tanggal"] = pd.to_datetime(df["tanggal"], format="%d/%m/%Y")\nprint(df["tanggal"].dt.strftime("%d %b %Y").tolist())\nprint(df["harga"].sum())', "['01 Oct 2026', '02 Oct 2026']\n26500.5"),
  P('Ubah data JSON bersarang dari API menjadi tabel datar dengan <code>pd.json_normalize</code>.', 'Kolom bersarang menjadi nama bertitik, misalnya alamat.kota.',
    'import pandas as pd\n\ndata = [\n    {"id": 1, "nama": "Rina", "alamat": {"kota": "Medan", "kode_pos": "20112"}},\n    {"id": 2, "nama": "Sandi", "alamat": {"kota": "Bandung", "kode_pos": "40115"}},\n]\nprint(pd.json_normalize(data))', '   id   nama alamat.kota alamat.kode_pos\n0   1   Rina       Medan           20112\n1   2  Sandi     Bandung           40115'),
],
'Memilih & menyaring: loc, iloc, query': [
  P('Dari data produk, pilih minuman dengan harga di bawah 16.000 memakai <code>loc</code> dan <code>query</code>, tampilkan kolom nama dan harga saja.', 'df.loc[kondisi, ["kolom"]]; kondisi digabung dengan &amp; dan tanda kurung.',
    'import pandas as pd\n\ndf = pd.DataFrame({\n    "nama": ["Kopi", "Teh", "Roti", "Susu"],\n    "kategori": ["Minuman", "Minuman", "Makanan", "Minuman"],\n    "harga": [18000, 8000, 12000, 15000],\n})\nprint(df.loc[(df["kategori"] == "Minuman") & (df["harga"] < 16000), ["nama", "harga"]])\nprint(df.query("kategori == \'Minuman\' and harga < 16000")["nama"].tolist())', "   nama  harga\n1   Teh   8000\n3  Susu  15000\n['Teh', 'Susu']"),
  P('Apa beda <code>df.iloc[0:2]</code> dan <code>df.loc[0:2]</code> pada indeks angka 0, 1, 2, 3?', 'iloc berbasis posisi (ujung tidak ikut), loc berbasis label (ujung ikut).',
    'import pandas as pd\n\ndf = pd.DataFrame({"x": [10, 20, 30, 40]})\nprint(len(df.iloc[0:2]))\nprint(len(df.loc[0:2]))', '2\n3'),
],
'Nilai hilang: isna, dropna, fillna, ffill': [
  P('Hitung nilai kosong per kolom, isi kota kosong dengan "Tidak diketahui" dan harga kosong dengan median, lalu buang baris tanpa produk.', 'isna().sum(), fillna({...}), dropna(subset=[...]).',
    'import numpy as np\nimport pandas as pd\n\ndf = pd.DataFrame({\n    "produk": ["Kopi", "Teh", None, "Susu"],\n    "kota": ["Medan", None, "Bandung", "Medan"],\n    "harga": [18000, np.nan, 12000, 15000],\n})\nprint(df.isna().sum().to_dict())\ndf = df.fillna({"kota": "Tidak diketahui", "harga": df["harga"].median()})\ndf = df.dropna(subset=["produk"])\nprint(df)', "{'produk': 1, 'kota': 1, 'harga': 1}\n  produk             kota    harga\n0   Kopi            Medan  18000.0\n1    Teh  Tidak diketahui  15000.0\n3   Susu            Medan  15000.0"),
  P('Data suhu sensor per jam punya jam yang kosong. Isi dengan nilai sebelumnya (ffill) dan dengan interpolasi, lalu bandingkan.', 'ffill() menyalin nilai terakhir; interpolate() menarik garis lurus.',
    'import numpy as np\nimport pandas as pd\n\nsuhu = pd.Series([26.0, np.nan, np.nan, 29.0])\nprint(suhu.ffill().tolist())\nprint(suhu.interpolate().tolist())', '[26.0, 26.0, 26.0, 29.0]\n[26.0, 27.0, 28.0, 29.0]'),
],
'Teks, tanggal & tipe data': [
  P('Bersihkan kolom kota <code>[" medan", "MEDAN ", "Bandung"]</code> dan kolom harga <code>["Rp18.000", "Rp 9.500", "12000"]</code> menjadi angka.', '.str.strip().str.title(); .str.replace(r"[^0-9]", "", regex=True) lalu astype(int).',
    'import pandas as pd\n\ndf = pd.DataFrame({"kota": [" medan", "MEDAN ", "Bandung"], "harga": ["Rp18.000", "Rp 9.500", "12000"]})\ndf["kota"] = df["kota"].str.strip().str.title()\ndf["harga"] = df["harga"].str.replace(r"[^0-9]", "", regex=True).astype(int)\nprint(df)\nprint(df["kota"].nunique())', '      kota  harga\n0    Medan  18000\n1    Medan   9500\n2  Bandung  12000\n2'),
  P('Dari kolom tanggal transaksi, ambil nama hari, bulan, dan selisih hari dari tanggal pertama.', 'pd.to_datetime, .dt.day_name(), .dt.month, pengurangan tanggal lalu .dt.days.',
    'import pandas as pd\n\nt = pd.to_datetime(pd.Series(["2026-10-01", "2026-10-15", "2026-11-02"]))\nprint(t.dt.day_name().tolist())\nprint(t.dt.month.tolist())\nprint((t - t.min()).dt.days.tolist())', "['Thursday', 'Thursday', 'Monday']\n[10, 10, 11]\n[0, 14, 32]"),
],
'Duplikat & encoding kategori': [
  P('Temukan dan buang transaksi ganda berdasarkan id_trx, simpan yang terakhir.', 'duplicated(subset=..., keep=...) dan drop_duplicates.',
    'import pandas as pd\n\ndf = pd.DataFrame({"id_trx": [101, 102, 102, 103], "jumlah": [1, 2, 3, 1]})\nprint(df.duplicated(subset="id_trx").sum())\nprint(df.drop_duplicates(subset="id_trx", keep="last"))', '1\n   id_trx  jumlah\n0     101       1\n2     102       3\n3     103       1'),
  P('Ubah kolom ukuran (S, M, L) menjadi angka berurutan dan kolom kota menjadi one-hot.', 'map untuk urutan (ordinal), pd.get_dummies untuk nominal.',
    'import pandas as pd\n\ndf = pd.DataFrame({"ukuran": ["M", "S", "L"], "kota": ["Medan", "Bandung", "Medan"]})\ndf["ukuran_num"] = df["ukuran"].map({"S": 1, "M": 2, "L": 3})\nprint(pd.get_dummies(df, columns=["kota"], dtype=int))', '  ukuran  ukuran_num  kota_Bandung  kota_Medan\n0      M           2             0           1\n1      S           1             1           0\n2      L           3             0           1'),
],
'groupby & agregasi': [
  P('Hitung omzet total, rata-rata, dan jumlah transaksi per kota, urut dari omzet terbesar.', 'groupby("kota").agg(total=("omzet","sum"), ...).',
    'import pandas as pd\n\ndf = pd.DataFrame({\n    "kota": ["Medan", "Bandung", "Medan", "Jakarta", "Jakarta", "Medan"],\n    "omzet": [36000, 24000, 18000, 90000, 45000, 12000],\n})\nhasil = (df.groupby("kota")\n           .agg(total=("omzet", "sum"), rata=("omzet", "mean"), trx=("omzet", "size"))\n           .sort_values("total", ascending=False))\nprint(hasil)', '          total     rata  trx\nkota                         \nJakarta  135000  67500.0    2\nMedan     66000  22000.0    3\nBandung   24000  24000.0    1'),
  P('Tambahkan kolom persentase kontribusi setiap transaksi terhadap total kotanya memakai <code>transform</code>.', 'transform("sum") mengembalikan nilai sepanjang baris asli.',
    'import pandas as pd\n\ndf = pd.DataFrame({"kota": ["Medan", "Medan", "Bandung"], "omzet": [30000, 10000, 24000]})\ndf["persen"] = (df["omzet"] / df.groupby("kota")["omzet"].transform("sum") * 100).round(1)\nprint(df)', '      kota  omzet  persen\n0    Medan  30000    75.0\n1    Medan  10000    25.0\n2  Bandung  24000   100.0'),
],
'merge & concat': [
  P('Gabungkan tabel transaksi dengan tabel produk untuk menghitung omzet, dan tampilkan transaksi yang produknya tidak dikenal.', 'merge(how="left", indicator=True); baris "left_only" tidak punya pasangan.',
    'import pandas as pd\n\ntrx = pd.DataFrame({"kode": ["K1", "T1", "X9"], "jumlah": [2, 3, 1]})\nproduk = pd.DataFrame({"kode": ["K1", "T1"], "harga": [18000, 8000]})\ngab = trx.merge(produk, on="kode", how="left", indicator=True)\ngab["omzet"] = gab["jumlah"] * gab["harga"]\nprint(gab)\nprint(gab.loc[gab["_merge"] == "left_only", "kode"].tolist())', "  kode  jumlah    harga     _merge    omzet\n0   K1       2  18000.0       both  36000.0\n1   T1       3   8000.0       both  24000.0\n2   X9       1      NaN  left_only      NaN\n['X9']"),
  P('Gabungkan data penjualan Oktober dan November yang kolomnya sama menjadi satu tabel, dengan kolom penanda bulan.', 'pd.concat([...], keys=[...]) lalu reset_index.',
    'import pandas as pd\n\nokt = pd.DataFrame({"produk": ["Kopi", "Teh"], "omzet": [500, 200]})\nnov = pd.DataFrame({"produk": ["Kopi", "Teh"], "omzet": [650, 180]})\nsemua = pd.concat([okt, nov], keys=["Okt", "Nov"], names=["bulan", None]).reset_index(level=0)\nprint(semua)', '  bulan produk  omzet\n0   Okt   Kopi    500\n1   Okt    Teh    200\n0   Nov   Kopi    650\n1   Nov    Teh    180'),
],
'pivot_table, crosstab & melt': [
  P('Buat pivot omzet dengan kota sebagai baris dan produk sebagai kolom, isi kosong dengan 0, dan tambah total.', 'pivot_table(index, columns, values, aggfunc="sum", fill_value=0, margins=True).',
    'import pandas as pd\n\ndf = pd.DataFrame({\n    "kota": ["Medan", "Medan", "Bandung", "Bandung", "Medan"],\n    "produk": ["Kopi", "Teh", "Kopi", "Kopi", "Kopi"],\n    "omzet": [36, 8, 18, 18, 18],\n})\nprint(df.pivot_table(index="kota", columns="produk", values="omzet",\n                     aggfunc="sum", fill_value=0, margins=True, margins_name="Total"))', 'produk   Kopi  Teh  Total\nkota                     \nBandung    36    0     36\nMedan      54    8     62\nTotal      90    8     98'),
  P('Ubah tabel lebar (kolom Jan, Feb, Mar) menjadi tabel panjang dengan kolom bulan dan omzet.', 'melt(id_vars=..., var_name=..., value_name=...).',
    'import pandas as pd\n\nlebar = pd.DataFrame({"kota": ["Medan", "Bandung"], "Jan": [10, 7], "Feb": [12, 8], "Mar": [9, 11]})\npanjang = lebar.melt(id_vars="kota", var_name="bulan", value_name="omzet")\nprint(panjang.head(4))\nprint(len(panjang))', '      kota bulan  omzet\n0    Medan   Jan     10\n1  Bandung   Jan      7\n2    Medan   Feb     12\n3  Bandung   Feb      8\n6'),
],
'Pemusatan & sebaran': [
  P('Gaji (juta) 7 karyawan: <code>[5, 5.5, 6, 6, 7, 8, 35]</code>. Hitung mean, median, modus, dan simpangan baku. Ukuran mana yang paling mewakili?', 'Satu gaji direktur menarik mean ke atas; median lebih tahan outlier.',
    'import pandas as pd\n\ngaji = pd.Series([5, 5.5, 6, 6, 7, 8, 35])\nprint(round(gaji.mean(), 2), gaji.median(), gaji.mode()[0], round(gaji.std(), 2))\nprint(gaji.describe().round(2))', '10.36 6.0 6.0 10.91\ncount     7.00\nmean     10.36\nstd      10.91\nmin       5.00\n25%       5.75\n50%       6.00\n75%       7.50\nmax      35.00\ndtype: float64'),
  P('Bandingkan sebaran dua cabang yang rata-ratanya sama memakai simpangan baku dan koefisien variasi.', 'CV = std / mean; makin besar makin tidak stabil.',
    'import pandas as pd\n\ndf = pd.DataFrame({"A": [100, 102, 98, 101, 99], "B": [60, 140, 80, 120, 100]})\nprint(df.mean().tolist())\nprint((df.std() / df.mean()).round(3).to_dict())', "[100.0, 100.0]\n{'A': 0.016, 'B': 0.316}"),
],
'Outlier: IQR & z-score': [
  P('Temukan outlier omzet harian dengan metode IQR (di luar Q1 - 1,5 IQR dan Q3 + 1,5 IQR).', 'quantile([.25, .75]), lalu batas bawah dan atas.',
    'import pandas as pd\n\nomzet = pd.Series([120, 135, 128, 140, 132, 410, 125, 30])\nq1, q3 = omzet.quantile([0.25, 0.75])\niqr = q3 - q1\nbawah, atas = q1 - 1.5 * iqr, q3 + 1.5 * iqr\nprint(bawah, atas)\nprint(omzet[(omzet < bawah) | (omzet > atas)].tolist())', '105.0 155.0\n[410, 30]'),
  P('Tandai outlier dengan z-score lebih dari 2 untuk data yang sama. Kenapa hasilnya bisa berbeda dengan IQR?', 'z = (x - mean) / std. Outlier besar ikut menaikkan std sehingga z-score kurang peka.',
    'import pandas as pd\n\nomzet = pd.Series([120, 135, 128, 140, 132, 410, 125, 30])\nz = (omzet - omzet.mean()) / omzet.std()\nprint(z.round(2).tolist())\nprint(omzet[z.abs() > 2].tolist())', '[-0.3, -0.16, -0.22, -0.11, -0.19, 2.34, -0.25, -1.11]\n[410]'),
],
'Korelasi': [
  P('Hitung korelasi Pearson antara biaya iklan dan penjualan, lalu matriks korelasi tiga kolom.', 'df["a"].corr(df["b"]) dan df.corr().',
    'import pandas as pd\n\ndf = pd.DataFrame({\n    "iklan": [1, 2, 3, 4, 5, 6],\n    "penjualan": [12, 15, 21, 24, 30, 33],\n    "retur": [5, 5, 4, 4, 3, 2],\n})\nprint(round(df["iklan"].corr(df["penjualan"]), 3))\nprint(df.corr().round(2))', '0.995\n           iklan  penjualan  retur\niklan       1.00       1.00  -0.96\npenjualan   1.00       1.00  -0.97\nretur      -0.96      -0.97   1.00'),
  Tx('Data menunjukkan penjualan es krim berkorelasi kuat dengan kasus tenggelam. Apakah es krim menyebabkan tenggelam?', 'Korelasi bukan sebab-akibat. Cari variabel ketiga.',
     'Tidak. Keduanya sama-sama naik saat cuaca panas (variabel pengganggu/confounder).\nUntuk klaim sebab-akibat perlu eksperimen (A/B test) atau analisis yang\nmengendalikan variabel lain.'),
],
'Memilih grafik yang tepat': [
  Tx('Pilih jenis grafik untuk: (a) omzet 12 bulan, (b) omzet 5 cabang, (c) sebaran umur pelanggan, (d) hubungan diskon dan jumlah beli, (e) gaji per divisi.', 'Tren: garis; bandingkan: batang; distribusi: histogram; hubungan: scatter; sebaran antargrup: boxplot.',
     '(a) grafik garis\n(b) batang horizontal, diurutkan\n(c) histogram\n(d) scatter plot\n(e) boxplot per divisi'),
  P('Buat grafik batang horizontal omzet per kota yang diurutkan, dengan judul yang menyampaikan temuan.', 'sort_values lalu plot.barh; judul berupa kalimat temuan.',
    'import matplotlib\nmatplotlib.use("Agg")\nimport matplotlib.pyplot as plt\nimport pandas as pd\n\nomzet = pd.Series({"Medan": 66, "Bandung": 24, "Jakarta": 135}).sort_values()\nfig, ax = plt.subplots(figsize=(6, 3))\nomzet.plot.barh(ax=ax, color="#0B6FA4")\nax.set_title("Jakarta menyumbang 60% omzet bulan ini")\nax.set_xlabel("Omzet (ribu Rp)")\nfig.tight_layout()\nfig.savefig("omzet_kota.png", dpi=150)\nprint(omzet.idxmax(), round(omzet.max() / omzet.sum() * 100))', 'Jakarta 60'),
],
'Grafik interaktif & dashboard': [
  P('Buat grafik garis interaktif Plotly omzet harian per kota dan simpan sebagai HTML.', 'px.line(df, x, y, color), fig.write_html.',
    'import pandas as pd\nimport plotly.express as px\n\ndf = pd.DataFrame({\n    "tanggal": pd.date_range("2026-10-01", periods=3).tolist() * 2,\n    "kota": ["Medan"] * 3 + ["Bandung"] * 3,\n    "omzet": [10, 12, 9, 7, 8, 11],\n})\nfig = px.line(df, x="tanggal", y="omzet", color="kota", title="Omzet harian per kota")\nfig.write_html("omzet.html")'),
  P('Tulis aplikasi Streamlit dengan filter kategori dan metrik total omzet.', 'st.selectbox, st.metric, st.bar_chart. Jalankan dengan streamlit run app.py.',
    'import pandas as pd\nimport streamlit as st\n\ndf = pd.read_csv("penjualan.csv")\nkategori = st.selectbox("Kategori", sorted(df["kategori"].unique()))\npilih = df[df["kategori"] == kategori]\nst.metric("Total omzet", f"Rp {pilih[\'omzet\'].sum():,}".replace(",", "."))\nst.bar_chart(pilih.groupby("kota")["omzet"].sum())'),
],
'SQL dari Python: sqlite3 & read_sql': [
  P('Buat database SQLite di memori, isi tabel penjualan, lalu baca hasil agregasi SQL langsung ke DataFrame.', 'sqlite3.connect(":memory:"), df.to_sql, pd.read_sql.',
    'import sqlite3\nimport pandas as pd\n\ncon = sqlite3.connect(":memory:")\npd.DataFrame({"kota": ["Medan", "Bandung", "Medan"], "omzet": [36000, 24000, 18000]}).to_sql("penjualan", con, index=False)\nsql = "SELECT kota, SUM(omzet) AS total FROM penjualan GROUP BY kota ORDER BY total DESC"\nprint(pd.read_sql(sql, con))', '      kota  total\n0    Medan  54000\n1  Bandung  24000'),
  P('Kenapa query dengan input pengguna harus memakai parameter? Tulis versi yang aman.', 'Tanda ? atau :nama diisi lewat params, bukan f-string.',
    'import sqlite3\nimport pandas as pd\n\ncon = sqlite3.connect(":memory:")\ncon.execute("CREATE TABLE produk (nama TEXT, harga INT)")\ncon.executemany("INSERT INTO produk VALUES (?, ?)", [("Kopi", 18000), ("Teh", 8000)])\nnama_input = "Kopi\' OR \'1\'=\'1"           # input jahat\nprint(pd.read_sql("SELECT * FROM produk WHERE nama = ?", con, params=[nama_input]))', 'Empty DataFrame\nColumns: [nama, harga]\nIndex: []'),
],
'Polars, Dask & PySpark': [
  P('Tulis agregasi omzet per kota memakai Polars dengan lazy API.', 'pl.scan_csv(...).group_by(...).agg(...).collect().',
    'import polars as pl\n\nhasil = (\n    pl.scan_csv("penjualan.csv")\n      .filter(pl.col("omzet") > 0)\n      .group_by("kota")\n      .agg(pl.col("omzet").sum().alias("total"))\n      .sort("total", descending=True)\n      .collect()\n)\nprint(hasil)'),
  Tx('Pilih alat: (a) CSV 300 MB di laptop, (b) 20 GB file Parquet di satu mesin besar, (c) 5 TB data di klaster.', 'pandas untuk kecil, Polars/DuckDB untuk menengah di satu mesin, Spark untuk klaster.',
     '(a) pandas (atau Polars bila ingin lebih cepat)\n(b) Polars atau DuckDB (lazy, multithread); Dask jika ingin API mirip pandas\n(c) PySpark di klaster (Databricks, EMR, Dataproc)'),
],
'Pengantar scikit-learn': [
  P('Latih model regresi linear untuk memprediksi penjualan dari biaya iklan, bagi data latih dan uji, lalu hitung R².', 'train_test_split, LinearRegression().fit, model.score.',
    'from sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import train_test_split\nimport numpy as np\n\nX = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])\ny = np.array([12, 15, 21, 24, 30, 33, 38, 41])\nX_latih, X_uji, y_latih, y_uji = train_test_split(X, y, test_size=0.25, random_state=42)\nmodel = LinearRegression().fit(X_latih, y_latih)\nprint(round(model.score(X_uji, y_uji), 3))\nprint(model.predict([[10]]).round(1))'),
  Tx('Kenapa data harus dibagi menjadi data latih dan data uji?', 'Model bisa "menghafal" data latih (overfitting).',
     'Model dinilai dengan data yang belum pernah dilihatnya, agar skor mencerminkan\nkinerja pada data baru. Jika dinilai dengan data latih, skornya terlalu optimis\nkarena model bisa sekadar menghafal (overfitting).'),
],
}

DA = {
'Empat jenis analitik': [
  Tx('Kelompokkan pertanyaan berikut ke deskriptif, diagnostik, prediktif, atau preskriptif: (a) Berapa omzet bulan lalu? (b) Kenapa omzet Medan turun? (c) Berapa omzet Desember nanti? (d) Berapa stok kopi yang harus dipesan?', 'Apa yang terjadi, kenapa, apa yang akan terjadi, apa yang harus dilakukan.',
     '(a) deskriptif\n(b) diagnostik\n(c) prediktif\n(d) preskriptif'),
  Tx('Tulis satu contoh pertanyaan tiap jenis analitik untuk aplikasi ojek online.', 'Mulai dari yang paling sederhana (deskriptif).',
     'Deskriptif  : berapa perjalanan per hari minggu lalu?\nDiagnostik  : kenapa pembatalan naik di Bekasi hari Senin?\nPrediktif   : berapa permintaan saat hujan Jumat sore?\nPreskriptif : berapa insentif pengemudi agar waktu tunggu di bawah 5 menit?'),
],
'Jenis data & skala ukur': [
  Tx('Tentukan skala ukur: (a) jenis kelamin, (b) tingkat kepuasan 1-5, (c) suhu °C, (d) berat badan, (e) peringkat lomba.', 'Nominal, ordinal, interval, rasio.',
     '(a) nominal\n(b) ordinal\n(c) interval (0 °C bukan "tidak ada suhu")\n(d) rasio (0 kg berarti tidak ada berat)\n(e) ordinal'),
  Tx('Kenapa tidak tepat menghitung rata-rata kode pos atau nomor HP?', 'Angka yang hanya label tetap data nominal.',
     'Kode pos dan nomor HP adalah label (nominal), bukan besaran.\nRata-ratanya tidak punya arti. Ringkas dengan frekuensi (modus) atau jumlah unik.'),
],
'Fungsi dasar: SUM, AVERAGE, COUNT, IF': [
  Xl('Kolom B2:B11 berisi nilai ujian. Tulis rumus untuk total, rata-rata, jumlah siswa yang mengisi, dan jumlah yang lulus (&gt;= 75).', 'SUM, AVERAGE, COUNT, COUNTIF.',
     '=SUM(B2:B11)\n=AVERAGE(B2:B11)\n=COUNT(B2:B11)\n=COUNTIF(B2:B11;">=75")'),
  Xl('Di C2, tulis rumus predikat: A jika &gt;= 85, B jika &gt;= 75, selain itu C. Lalu tulis versi IFS.', 'IF bersarang dibaca dari syarat paling ketat.',
     '=IF(B2>=85;"A";IF(B2>=75;"B";"C"))\n=IFS(B2>=85;"A";B2>=75;"B";TRUE;"C")\n\n(Excel berbahasa Inggris memakai koma sebagai pemisah argumen.)'),
],
'Teks & tanggal: TRIM, PROPER, SUBSTITUTE, DATEDIF': [
  Xl('Sel A2 berisi "  rina   SIREGAR ". Rapikan menjadi "Rina Siregar", lalu ubah "Rp18.000" di B2 menjadi angka.', 'PROPER(TRIM(...)); SUBSTITUTE untuk membuang "Rp" dan titik, lalu VALUE.',
     '=PROPER(TRIM(A2))\n=VALUE(SUBSTITUTE(SUBSTITUTE(B2;"Rp";"");".";""))'),
  Xl('Tanggal lahir di A2. Tulis rumus umur dalam tahun pada hari ini dan nama hari lahirnya.', 'DATEDIF(awal;akhir;"Y"), TEXT(tanggal;"dddd").',
     '=DATEDIF(A2;TODAY();"Y")\n=TEXT(A2;"dddd")'),
],
'Lookup & pivot table': [
  Xl('Sheet Produk berisi kode di kolom A dan harga di kolom C. Ambil harga untuk kode di B2 memakai XLOOKUP dan VLOOKUP, dengan pesan "Tidak ada" jika tidak ditemukan.', 'XLOOKUP(kunci; kolom_cari; kolom_hasil; jika_tidak_ada).',
     '=XLOOKUP(B2;Produk!A:A;Produk!C:C;"Tidak ada")\n=IFERROR(VLOOKUP(B2;Produk!A:C;3;FALSE);"Tidak ada")'),
  Tx('Susun pivot table untuk menjawab "omzet per kota per bulan dan kota mana yang tumbuh tercepat".', 'Tentukan baris, kolom, nilai, dan filter.',
     'Baris  : kota\nKolom  : bulan (kelompokkan tanggal per bulan)\nNilai  : SUM omzet\nFilter : kategori produk (opsional)\nLalu tambah kolom hitung % pertumbuhan bulan terakhir vs sebelumnya dan urutkan.'),
],
'Python atau R?': [
  Tx('Pilih Python atau R untuk: (a) tim produk yang juga membangun API, (b) penelitian statistik di kampus, (c) analis yang bekerja dengan data engineer.', 'Python: serba guna dan dekat dengan rekayasa. R: kuat di statistik dan akademik.',
     '(a) Python: satu bahasa untuk analisis dan aplikasi.\n(b) R: paket statistik lengkap dan umum di jurnal.\n(c) Python: sama dengan alat engineer (Airflow, PySpark).'),
  P('Tulis padanan Python (pandas) dari kode R dplyr: <code>df %&gt;% filter(omzet &gt; 0) %&gt;% group_by(kota) %&gt;% summarise(total = sum(omzet))</code>.', 'Rangkaian method pandas: query/loc, groupby, agg.',
    'import pandas as pd\n\ndf = pd.DataFrame({"kota": ["Medan", "Medan", "Bandung"], "omzet": [10, -2, 7]})\nprint(df[df["omzet"] > 0].groupby("kota", as_index=False).agg(total=("omzet", "sum")))', '      kota  total\n0  Bandung      7\n1    Medan     10'),
],
'API & web scraping': [
  P('Ambil data JSON dari API dengan requests, tangani error HTTP, dan ubah menjadi DataFrame.', 'requests.get(url, params, timeout), raise_for_status(), resp.json().',
    'import pandas as pd\nimport requests\n\nresp = requests.get("https://api.contoh.id/produk", params={"kategori": "minuman"}, timeout=10)\nresp.raise_for_status()\ndf = pd.DataFrame(resp.json()["data"])\nprint(df.head())'),
  Tx('Sebutkan aturan etis sebelum melakukan web scraping.', 'Hormati pemilik situs dan data pribadi.',
     '1. Utamakan API resmi bila ada.\n2. Baca robots.txt dan ketentuan layanan.\n3. Batasi kecepatan permintaan (jeda, tidak membebani server).\n4. Jangan mengambil data pribadi tanpa dasar hukum (UU PDP).\n5. Cantumkan sumber data.'),
],
'Rentang, varians & bentuk distribusi': [
  P('Hitung rentang, varians, simpangan baku, dan kemiringan (skewness) waktu antar (menit): <code>[20, 22, 25, 25, 28, 30, 75]</code>.', 'max - min, var(), std(), skew(). Skew positif berarti ekor kanan panjang.',
    'import pandas as pd\n\nwaktu = pd.Series([20, 22, 25, 25, 28, 30, 75])\nprint(waktu.max() - waktu.min())\nprint(round(waktu.var(), 2), round(waktu.std(), 2))\nprint(round(waktu.skew(), 2))', '55\n368.48 19.2\n2.48'),
  Tx('Distribusi pendapatan biasanya miring ke kanan. Bagaimana urutan mean, median, dan modus?', 'Ekor panjang menarik mean ke arahnya.',
     'Miring kanan: modus < median < mean.\nKarena itu laporan pendapatan biasanya memakai median.'),
],
'Regresi linear sederhana': [
  P('Hitung garis regresi penjualan terhadap iklan dengan NumPy, lalu prediksi penjualan jika iklan 10.', 'np.polyfit(x, y, 1) memberi kemiringan dan titik potong.',
    'import numpy as np\n\niklan = np.array([1, 2, 3, 4, 5, 6])\npenjualan = np.array([12, 15, 21, 24, 30, 33])\nb, a = np.polyfit(iklan, penjualan, 1)\nprint(round(b, 2), round(a, 2))\nprint(round(b * 10 + a, 1))', '4.37 7.2\n50.9'),
  Tx('Kemiringan regresi 4,3 artinya apa dalam bahasa bisnis? Apa batas tafsirannya?', 'Setiap tambahan satu unit x ...',
     'Setiap tambahan 1 juta biaya iklan, penjualan naik rata-rata sekitar 4,3 unit.\nBatas: hanya berlaku di rentang data yang diamati, dan hubungan ini belum\ntentu sebab-akibat (bisa ada faktor lain seperti musim).'),
],
'Funnel & stacked chart': [
  P('Hitung konversi tiap tahap funnel: kunjungan 10.000, lihat produk 4.200, keranjang 1.300, bayar 520.', 'Konversi tahap = tahap / tahap sebelumnya; konversi total = tahap / tahap pertama.',
    'import pandas as pd\n\nf = pd.Series({"kunjungan": 10000, "lihat": 4200, "keranjang": 1300, "bayar": 520})\nprint((f / f.shift(1) * 100).round(1).tolist())\nprint((f / f.iloc[0] * 100).round(1).tolist())', '[nan, 42.0, 31.0, 40.0]\n[100.0, 42.0, 13.0, 5.2]'),
  Tx('Kapan memakai stacked bar 100% daripada stacked bar biasa?', 'Komposisi vs jumlah.',
     'Stacked bar biasa: ingin melihat total dan bagiannya sekaligus.\nStacked bar 100%: hanya ingin membandingkan komposisi (persentase) antar grup\nyang totalnya berbeda jauh.'),
],
'Big data, MapReduce & Spark': [
  P('Simulasikan MapReduce untuk menghitung kata dalam tiga baris teks dengan Python biasa (map, shuffle, reduce).', 'Map: (kata, 1). Shuffle: kelompokkan per kata. Reduce: jumlahkan.',
    'from collections import defaultdict\n\nbaris = ["kopi susu", "kopi teh", "teh manis kopi"]\npasangan = [(k, 1) for b in baris for k in b.split()]   # map\ngrup = defaultdict(list)\nfor k, v in pasangan:                                     # shuffle\n    grup[k].append(v)\nhasil = {k: sum(v) for k, v in grup.items()}              # reduce\nprint(hasil)', "{'kopi': 3, 'susu': 1, 'teh': 2, 'manis': 1}"),
  Tx('Sebutkan 3V big data beserta contohnya di e-commerce.', 'Volume, velocity, variety.',
     'Volume  : miliaran baris log klik per bulan.\nVelocity: ribuan transaksi per detik saat flash sale.\nVariety : data tabel pesanan, teks ulasan, gambar produk, log JSON.'),
],
'Peta machine learning untuk analis': [
  Tx('Tentukan jenis tugas ML: (a) memprediksi harga rumah, (b) mendeteksi transaksi penipuan, (c) mengelompokkan pelanggan tanpa label, (d) merekomendasikan produk.', 'Regresi, klasifikasi, clustering, rekomendasi.',
     '(a) regresi (supervised)\n(b) klasifikasi (supervised, data tidak seimbang)\n(c) clustering (unsupervised), misal K-Means\n(d) sistem rekomendasi (collaborative filtering)'),
  Tx('Model penipuan akurasinya 99%, padahal hanya 1% transaksi yang penipuan. Kenapa angka ini menyesatkan, dan metrik apa yang lebih tepat?', 'Model yang selalu menjawab "bukan penipuan" juga 99% akurat.',
     'Akurasi tinggi bisa didapat tanpa menangkap satu pun penipuan.\nPakai precision, recall, dan F1 untuk kelas penipuan, serta confusion matrix.'),
],
}

BI = {
'BI analyst dan peran data lainnya': [
  Tx('Siapa yang paling cocok mengerjakan: (a) dashboard KPI penjualan mingguan, (b) pipeline data dari aplikasi ke warehouse, (c) model prediksi churn?', 'BI analyst, data engineer, data scientist.',
     '(a) BI analyst\n(b) data engineer\n(c) data scientist (dibantu analyst untuk definisi dan evaluasi bisnis)'),
  Tx('Sebutkan lima keterampilan inti BI analyst.', 'Gabungan teknis dan bisnis.',
     '1. SQL\n2. Pemodelan data (skema bintang)\n3. Alat BI (Power BI/Tableau/Looker)\n4. Pemahaman bisnis dan KPI\n5. Komunikasi dan visualisasi data'),
],
'Berpikir seperti pemilik bisnis': [
  Tx('Manajer berkata: "Buatkan dashboard penjualan." Tulis lima pertanyaan klarifikasi sebelum mulai.', 'Siapa, keputusan apa, seberapa sering, metrik apa, data apa.',
     '1. Siapa yang akan memakai dashboard ini?\n2. Keputusan apa yang akan diambil dari dashboard ini?\n3. Seberapa sering dilihat (harian, mingguan)?\n4. Metrik apa yang dianggap sukses, dan targetnya berapa?\n5. Data apa yang tersedia dan seberapa bisa dipercaya?'),
  Tx('Omzet naik 20% tetapi laba turun. Tulis tiga hipotesis yang perlu dicek.', 'Pikirkan harga, biaya, dan bauran produk.',
     '1. Diskon besar menaikkan volume tetapi menekan margin.\n2. Biaya (bahan baku, ongkir, iklan) naik lebih cepat dari omzet.\n3. Bauran produk bergeser ke produk bermargin rendah.'),
],
'CLV & analisis kohort': [
  P('Hitung CLV sederhana: rata-rata belanja Rp150.000, 2 kali sebulan, margin 30%, rata-rata pelanggan bertahan 18 bulan.', 'CLV = nilai belanja x frekuensi x margin x lama bertahan.',
    'belanja, frekuensi, margin, bulan = 150_000, 2, 0.30, 18\nclv = belanja * frekuensi * margin * bulan\nprint(f"Rp{clv:,.0f}".replace(",", "."))', 'Rp1.620.000'),
  P('Buat tabel retensi kohort dari data pesanan: kohort = bulan pertama beli, kolom = bulan ke-berapa sejak itu.', 'Bulan pertama per pelanggan dengan groupby().transform("min"), lalu selisih bulan, lalu pivot jumlah pelanggan unik.',
    'import pandas as pd\n\ndf = pd.DataFrame({\n    "pelanggan": ["A", "A", "B", "B", "C", "C", "D"],\n    "bulan": pd.to_datetime(["2026-01", "2026-02", "2026-01", "2026-03", "2026-02", "2026-03", "2026-02"]),\n})\ndf["kohort"] = df.groupby("pelanggan")["bulan"].transform("min")\ndf["ke"] = (df["bulan"].dt.year - df["kohort"].dt.year) * 12 + (df["bulan"].dt.month - df["kohort"].dt.month)\ntabel = df.pivot_table(index=df["kohort"].dt.strftime("%Y-%m"), columns="ke", values="pelanggan", aggfunc="nunique", fill_value=0)\nprint(tabel)', 'ke       0  1  2\nkohort          \n2026-01  2  1  1\n2026-02  2  1  0'),
],
'Sampel, p-value & selang kepercayaan': [
  P('Rata-rata belanja sampel 100 pelanggan Rp85.000 dengan simpangan baku Rp20.000. Hitung selang kepercayaan 95%.', 'Rata-rata ± 1,96 x (s / akar n).',
    'import math\n\nrata, s, n = 85_000, 20_000, 100\nmoe = 1.96 * s / math.sqrt(n)\nprint(round(rata - moe), round(rata + moe))', '81080 88920'),
  Tx('A/B test tombol baru: p-value 0,03 dengan batas 0,05. Apa artinya, dan apa yang TIDAK berarti?', 'p-value adalah peluang melihat hasil seekstrem ini jika sebenarnya tidak ada beda.',
     'Artinya: jika tombol baru sebenarnya tidak berpengaruh, peluang melihat selisih\nsebesar ini atau lebih hanya 3%, jadi hasilnya signifikan pada taraf 5%.\nTIDAK berarti: peluang tombol baru lebih baik 97%, atau efeknya besar.\nTetap lihat besar efek (misal +0,4 poin konversi) dan selang kepercayaannya.'),
],
'Warehouse, lake & ETL': [
  Tx('Bedakan ETL dan ELT, dan kenapa ELT populer di cloud warehouse.', 'Di mana transformasi dilakukan?',
     'ETL: data diubah dulu di server terpisah, baru dimuat ke warehouse.\nELT: data mentah dimuat dulu, lalu diubah di dalam warehouse dengan SQL (misal dbt).\nELT populer karena warehouse cloud (BigQuery, Snowflake) kuat dan murah untuk\nmenghitung, dan data mentah tetap tersimpan untuk diolah ulang.'),
  Tx('Pilih tempat menyimpan: (a) tabel penjualan bersih untuk dashboard, (b) file log mentah dan gambar, (c) keduanya dengan satu format terbuka.', 'Warehouse, lake, lakehouse.',
     '(a) data warehouse\n(b) data lake\n(c) lakehouse (Delta Lake, Apache Iceberg)'),
],
'Merancang dashboard': [
  Tx('Susun tata letak dashboard penjualan untuk manajer: apa yang di atas, tengah, dan bawah?', 'Pola Z/F: KPI utama di kiri atas, rincian di bawah.',
     'Atas  : 4 kartu KPI (omzet, transaksi, rata-rata belanja, margin) + perbandingan periode lalu\nTengah: tren omzet harian (garis) dan omzet per cabang (batang terurut)\nBawah : tabel produk teratas dan filter tanggal/cabang\nMaksimal 5-7 visual; setiap visual menjawab satu pertanyaan.'),
  Tx('Sebutkan empat kesalahan umum pada dashboard.', 'Pikirkan kepadatan, warna, konteks, dan pembaruan.',
     '1. Terlalu banyak grafik dalam satu halaman.\n2. Warna dipakai untuk hiasan, bukan makna.\n3. Angka tanpa pembanding (target, periode lalu).\n4. Tidak jelas kapan data terakhir diperbarui.'),
],
'Grafik menyesatkan & bercerita dengan data': [
  Tx('Grafik batang omzet memakai sumbu Y mulai dari 95 juta sehingga kenaikan dari 98 ke 100 juta terlihat dua kali lipat. Apa masalahnya dan perbaikannya?', 'Grafik batang harus mulai dari nol.',
     'Panjang batang mewakili nilai, jadi sumbu yang terpotong membesar-besarkan selisih.\nPerbaikan: mulai sumbu Y dari 0, atau pakai grafik garis/titik bila ingin\nmenonjolkan perubahan kecil, lalu tulis angka kenaikannya (+2%).'),
  Tx('Ubah judul "Omzet per bulan 2026" menjadi judul yang bercerita.', 'Judul berisi temuan utama, bukan nama variabel.',
     'Omzet naik 35% sejak program member diluncurkan pada Juni'),
],
'Power BI, Tableau & Looker': [
  Tx('Tulis rumus DAX untuk total omzet, omzet bulan lalu, dan pertumbuhan persen.', 'SUM, CALCULATE dengan DATEADD, DIVIDE.',
     'Total Omzet = SUM(Penjualan[omzet])\nOmzet Bulan Lalu = CALCULATE([Total Omzet], DATEADD(Kalender[Tanggal], -1, MONTH))\nPertumbuhan % = DIVIDE([Total Omzet] - [Omzet Bulan Lalu], [Omzet Bulan Lalu])'),
  Tx('Pilih alat BI: (a) perusahaan yang sudah memakai Microsoft 365, (b) tim yang butuh visual eksplorasi kaya, (c) perusahaan berbasis Google Cloud yang ingin metrik terpusat.', 'Power BI, Tableau, Looker.',
     '(a) Power BI\n(b) Tableau\n(c) Looker (LookML sebagai lapisan semantik terpusat)'),
],
'Privasi data & UU PDP': [
  Tx('Kamu membuat dashboard pelanggan. Data mana yang harus disamarkan atau dibuang menurut prinsip UU PDP?', 'Prinsip minimisasi data dan tujuan yang jelas.',
     'Samarkan atau buang: nama lengkap, NIK, nomor HP, email, alamat rinci.\nCukup tampilkan agregat (per kota, per segmen) atau ID samaran.\nBatasi akses dashboard sesuai peran, dan catat siapa yang membuka data rinci.'),
  Sq('Tulis query yang menyamarkan email menjadi "r***@mail.id" dan hanya menampilkan 4 digit terakhir nomor HP.', 'LEFT, SUBSTR/SUBSTRING, POSITION/INSTR, RIGHT.',
     "SELECT\n  LEFT(email, 1) || '***' || SUBSTR(email, INSTR(email, '@')) AS email_samaran,\n  '********' || RIGHT(no_hp, 4) AS hp_samaran\nFROM pelanggan;"),
],
'Portofolio & wawancara BI': [
  Tx('Susun struktur studi kasus portofolio BI dalam lima bagian.', 'Masalah, data, proses, hasil, dampak.',
     '1. Masalah bisnis (1-2 kalimat)\n2. Data dan sumbernya\n3. Proses: pembersihan, model data, metrik\n4. Dashboard (tangkapan layar + tautan)\n5. Temuan dan rekomendasi, beserta dampaknya'),
  Tx('Jawab pertanyaan wawancara dengan metode STAR: "Ceritakan saat datamu ternyata salah."', 'Situation, Task, Action, Result.',
     'S: Dashboard omzet menunjukkan lonjakan 40% dalam sehari.\nT: Memastikan angka benar sebelum rapat direksi.\nA: Menelusuri ke tabel sumber, menemukan transaksi ganda akibat pipeline\n   yang jalan dua kali, lalu menambah pemeriksaan duplikat.\nR: Angka dikoreksi sebelum rapat, dan pemeriksaan otomatis mencegah kejadian ulang.'),
],
}

DE = {
'Siklus hidup data engineering': [
  Tx('Urutkan tahap siklus hidup data engineering dan beri contoh alat di tiap tahap.', 'Generation, ingestion, storage, transformation, serving.',
     'Generation     : aplikasi kasir, sensor, log web\nIngestion      : Airbyte, Fivetran, Kafka\nStorage        : S3/GCS, BigQuery, Snowflake\nTransformation : dbt, Spark\nServing        : dashboard BI, reverse ETL, model ML\n(Undercurrent: keamanan, orkestrasi, DataOps, tata kelola)'),
  Tx('Apa yang terjadi jika tahap ingestion tidak mencatat waktu data diambil?', 'Pikirkan pelacakan dan pemrosesan ulang.',
     'Sulit melacak data datang dari kapan (lineage), sulit memproses ulang\nsebagian data, dan sulit mendeteksi data yang terlambat atau ganda.\nTambahkan kolom ingested_at dan simpan data mentah per tanggal.'),
],
'Data engineer, analyst & scientist': [
  Tx('Siapa yang memegang: (a) memperbaiki pipeline yang gagal tengah malam, (b) menjelaskan kenapa churn naik, (c) melatih model rekomendasi?', 'Engineer, analyst, scientist.',
     '(a) data engineer\n(b) data analyst\n(c) data scientist / ML engineer'),
  Tx('Apa itu analytics engineer?', 'Perannya di antara engineer dan analyst.',
     'Peran di antara data engineer dan analyst: mengubah data mentah di warehouse\nmenjadi model yang bersih dan teruji (biasanya dengan dbt dan SQL),\nsehingga analyst bisa langsung memakainya.'),
],
'Linux & shell untuk data': [
  Bs('Dari <code>penjualan.csv</code> (kolom: tanggal,kota,omzet), hitung jumlah baris tanpa header, 3 kota terbanyak, dan total omzet.', 'tail -n +2, cut -d, -f, sort | uniq -c | sort -rn, awk untuk menjumlah.',
     'tail -n +2 penjualan.csv | wc -l\ntail -n +2 penjualan.csv | cut -d, -f2 | sort | uniq -c | sort -rn | head -3\nawk -F, \'NR > 1 { total += $3 } END { print total }\' penjualan.csv'),
  Bs('Jadwalkan skrip <code>/opt/etl/harian.sh</code> setiap hari pukul 02.00 dan simpan log-nya.', 'crontab -e, format: menit jam hari bulan hari_minggu.',
     'crontab -e\n# lalu tambahkan baris:\n0 2 * * * /opt/etl/harian.sh >> /var/log/etl/harian.log 2>&1'),
],
'Dasar sistem terdistribusi': [
  Tx('Jelaskan replikasi dan partisi (sharding) dengan contoh database pesanan.', 'Salinan vs pembagian.',
     'Replikasi: data pesanan yang sama disalin ke beberapa server agar tetap\n  tersedia jika satu mati dan agar pembacaan bisa disebar.\nPartisi  : pesanan dibagi ke beberapa server, misal berdasarkan id pelanggan,\n  agar setiap server menyimpan dan mengolah sebagian data saja.'),
  Tx('Apa itu exactly-once, at-least-once, dan at-most-once dalam pengiriman pesan?', 'Berapa kali pesan bisa diproses?',
     'At-most-once : pesan bisa hilang, tidak pernah ganda.\nAt-least-once: pesan tidak hilang, tetapi bisa ganda (perlu idempotensi).\nExactly-once : setiap pesan diproses tepat sekali (paling mahal, butuh dukungan sistem).'),
],
'OLTP vs OLAP & penyimpanan kolom': [
  Tx('Kelompokkan ke OLTP atau OLAP: (a) menyimpan pesanan baru, (b) total omzet per bulan 3 tahun, (c) mengubah alamat pelanggan, (d) dashboard tren kategori.', 'Transaksi kecil vs analisis besar.',
     '(a) OLTP\n(b) OLAP\n(c) OLTP\n(d) OLAP'),
  Tx('Kenapa penyimpanan kolom (Parquet, BigQuery) cepat untuk <code>SELECT SUM(omzet) FROM penjualan</code>?', 'Kolom mana saja yang dibaca?',
     'Hanya kolom omzet yang dibaca dari disk, bukan seluruh baris.\nNilai dalam satu kolom bertipe sama sehingga mudah dikompresi,\njadi data yang dibaca jauh lebih kecil.'),
],
'NoSQL, CAP & skala': [
  Tx('Pilih database: (a) keranjang belanja sementara, (b) katalog produk dengan atribut berbeda-beda, (c) jaringan pertemanan, (d) data sensor per detik.', 'Key-value, dokumen, graf, time series.',
     '(a) key-value (Redis)\n(b) dokumen (MongoDB)\n(c) graf (Neo4j)\n(d) time series (TimescaleDB, InfluxDB)'),
  Tx('Menurut teorema CAP, saat jaringan terputus (partisi), sistem harus memilih apa?', 'Consistency atau availability.',
     'Memilih antara konsistensi (menolak permintaan agar data tidak berbeda)\natau ketersediaan (tetap melayani walau data mungkin belum terbaru).\nContoh: sistem bank cenderung C, linimasa media sosial cenderung A.'),
],
'Slowly changing dimension (SCD tipe 2)': [
  Sq('Pelanggan Rina pindah dari Medan ke Bandung pada 2026-10-01. Tulis SQL SCD tipe 2: tutup baris lama dan tambah baris baru.', 'Kolom berlaku_dari, berlaku_sampai, aktif.',
     "UPDATE dim_pelanggan\nSET berlaku_sampai = DATE '2026-09-30', aktif = FALSE\nWHERE id_pelanggan = 17 AND aktif = TRUE;\n\nINSERT INTO dim_pelanggan (id_pelanggan, nama, kota, berlaku_dari, berlaku_sampai, aktif)\nVALUES (17, 'Rina', 'Bandung', DATE '2026-10-01', DATE '9999-12-31', TRUE);"),
  Tx('Bedakan SCD tipe 1 dan tipe 2. Kapan memakai masing-masing?', 'Timpa atau simpan riwayat.',
     'Tipe 1: nilai lama ditimpa, tanpa riwayat. Cocok untuk koreksi salah ketik.\nTipe 2: baris baru dengan rentang berlaku, riwayat tersimpan.\nCocok jika laporan masa lalu harus memakai nilai saat itu (misal kota pelanggan).'),
],
'Warehouse, lake, lakehouse & mesh': [
  Tx('Apa itu arsitektur medallion (bronze, silver, gold)?', 'Lapisan kualitas data di lakehouse.',
     'Bronze: data mentah apa adanya dari sumber.\nSilver: data dibersihkan, disamakan formatnya, digabungkan.\nGold  : tabel siap pakai untuk dashboard dan model (agregat bisnis).'),
  Tx('Kapan organisasi butuh data mesh?', 'Pikirkan ukuran organisasi dan kemacetan tim data pusat.',
     'Saat organisasi besar dengan banyak domain (pemasaran, logistik, keuangan)\ndan tim data pusat menjadi kemacetan. Setiap domain memiliki dan\nmenerbitkan "data product" sendiri dengan standar bersama (tata kelola federasi).'),
],
'Batch, streaming & hybrid': [
  Tx('Pilih batch atau streaming: (a) laporan omzet harian, (b) deteksi penipuan kartu, (c) rekap gaji bulanan, (d) stok gudang real time.', 'Seberapa cepat hasil dibutuhkan?',
     '(a) batch\n(b) streaming\n(c) batch\n(d) streaming (atau micro-batch beberapa detik)'),
  Tx('Apa itu event time dan processing time, dan kenapa penting di streaming?', 'Data bisa datang terlambat.',
     'Event time: kapan peristiwa terjadi (transaksi di kasir).\nProcessing time: kapan sistem memprosesnya.\nData dari HP yang offline bisa datang terlambat; agregasi per jam harus\nmemakai event time dan watermark agar data terlambat tetap masuk jam yang benar.'),
],
'Idempotensi & upsert': [
  Sq('Tulis upsert PostgreSQL: masukkan stok produk, atau perbarui jika kode produk sudah ada.', 'INSERT ... ON CONFLICT (kunci) DO UPDATE SET ... = EXCLUDED....',
     "INSERT INTO stok (kode, jumlah, diperbarui)\nVALUES ('K1', 40, NOW())\nON CONFLICT (kode)\nDO UPDATE SET jumlah = EXCLUDED.jumlah,\n              diperbarui = EXCLUDED.diperbarui;"),
  P('Tunjukkan bahwa memuat data harian dua kali tidak membuat data ganda jika memakai upsert berdasarkan kunci.', 'Pakai dict sebagai tabel: kunci yang sama ditimpa, bukan ditambah.',
    'tabel = {}\n\ndef muat(baris):\n    for r in baris:\n        tabel[(r["tanggal"], r["kode"])] = r     # upsert berdasarkan kunci\n\nharian = [{"tanggal": "2026-11-01", "kode": "K1", "jumlah": 5},\n          {"tanggal": "2026-11-01", "kode": "T1", "jumlah": 3}]\nmuat(harian)\nmuat(harian)          # dijalankan ulang\nprint(len(tabel))', '2'),
],
'Orkestrasi dengan Airflow': [
  P('Tulis DAG Airflow harian dengan tiga tugas berurutan: ekstrak, transformasi, muat.', 'Pakai TaskFlow API (@dag, @task) dan schedule="@daily".',
    'from datetime import datetime\nfrom airflow.decorators import dag, task\n\n@dag(schedule="@daily", start_date=datetime(2026, 11, 1), catchup=False, tags=["penjualan"])\ndef penjualan_harian():\n    @task\n    def ekstrak():\n        return [{"kode": "K1", "jumlah": 5}]\n\n    @task\n    def transformasi(baris):\n        return [r | {"omzet": r["jumlah"] * 18000} for r in baris]\n\n    @task\n    def muat(baris):\n        print(f"memuat {len(baris)} baris")\n\n    muat(transformasi(ekstrak()))\n\npenjualan_harian()'),
  Tx('Apa itu backfill dan kenapa tugas Airflow harus idempoten?', 'Menjalankan ulang tanggal yang lalu.',
     'Backfill: menjalankan DAG untuk tanggal-tanggal lampau (misal setelah bug diperbaiki).\nKarena satu tanggal bisa dijalankan lebih dari sekali, tugas harus idempoten:\nhasil akhirnya sama walau dijalankan berulang (pakai upsert/overwrite partisi).'),
],
'Reverse ETL': [
  Tx('Berikan dua contoh reverse ETL di toko online.', 'Data dari warehouse dikirim kembali ke alat operasional.',
     '1. Skor pelanggan "berisiko churn" dari warehouse dikirim ke CRM agar tim CS menghubungi.\n2. Segmen "pembeli kopi setia" dikirim ke alat email marketing untuk promo khusus.'),
  Tx('Risiko apa yang perlu dijaga saat reverse ETL?', 'Data kembali ke sistem yang dipakai orang setiap hari.',
     'Data salah langsung berdampak ke pelanggan (email salah sasaran),\nbatas kuota API alat tujuan, sinkronisasi ganda, dan privasi:\nkirim kolom seperlunya saja dan pastikan ada persetujuan pemakaian data.'),
],
'Kafka: topik, partisi & consumer group': [
  P('Tulis producer Kafka (kafka-python) yang mengirim event pesanan ke topik "pesanan" dengan kunci id pelanggan.', 'Kunci yang sama selalu masuk partisi yang sama, sehingga urutannya terjaga.',
    'import json\nfrom kafka import KafkaProducer\n\nproducer = KafkaProducer(\n    bootstrap_servers="localhost:9092",\n    key_serializer=str.encode,\n    value_serializer=lambda v: json.dumps(v).encode(),\n)\nproducer.send("pesanan", key="pelanggan-17", value={"id": 901, "total": 36000})\nproducer.flush()'),
  Tx('Topik punya 6 partisi. Apa yang terjadi jika consumer group berisi 2, 6, dan 8 consumer?', 'Satu partisi hanya dibaca satu consumer dalam satu group.',
     '2 consumer: masing-masing membaca 3 partisi.\n6 consumer: masing-masing 1 partisi (paralel maksimum).\n8 consumer: 6 aktif, 2 menganggur.'),
],
'Antrean pesan & komunikasi asinkron': [
  P('Simulasikan antrean pesan dengan <code>queue.Queue</code>: produsen memasukkan 3 pesanan, konsumen memprosesnya satu per satu.', 'put, get, task_done; produsen dan konsumen tidak perlu menunggu satu sama lain.',
    'import queue\n\nantre = queue.Queue()\nfor i in (101, 102, 103):\n    antre.put({"id": i})\n\nwhile not antre.empty():\n    pesan = antre.get()\n    print("proses pesanan", pesan["id"])\n    antre.task_done()', 'proses pesanan 101\nproses pesanan 102\nproses pesanan 103'),
  Tx('Apa itu dead letter queue (DLQ)?', 'Ke mana pesan yang terus gagal diproses?',
     'Antrean khusus untuk pesan yang gagal diproses setelah beberapa kali percobaan.\nPesan dipindahkan ke DLQ agar tidak memblokir antrean utama,\nlalu diperiksa dan diproses ulang secara manual atau otomatis.'),
],
'Apache Spark & PySpark': [
  P('Tulis kode PySpark yang membaca Parquet penjualan, menghitung omzet per kota, dan menulis hasilnya per tanggal.', 'spark.read.parquet, groupBy().agg(F.sum()), write.partitionBy().',
    'from pyspark.sql import SparkSession, functions as F\n\nspark = SparkSession.builder.appName("omzet").getOrCreate()\ndf = spark.read.parquet("s3://data/penjualan/")\nhasil = (df.filter(F.col("omzet") > 0)\n           .groupBy("tanggal", "kota")\n           .agg(F.sum("omzet").alias("total")))\nhasil.write.mode("overwrite").partitionBy("tanggal").parquet("s3://data/omzet_kota/")'),
  Tx('Apa beda transformation dan action di Spark, dan apa itu lazy evaluation?', 'filter dan groupBy vs count dan write.',
     'Transformation (filter, select, groupBy) hanya membangun rencana kerja.\nAction (count, show, write) memicu eksekusi rencana itu.\nLazy evaluation membuat Spark bisa mengoptimalkan seluruh rencana sebelum jalan.'),
],
'Peta layanan cloud untuk data': [
  Tx('Isi padanan layanan di AWS, Google Cloud, dan Azure untuk: object storage, data warehouse, streaming.', 'S3, BigQuery, Kinesis, ...',
     '                 AWS        Google Cloud   Azure\nObject storage   S3         Cloud Storage  Blob Storage / ADLS\nData warehouse   Redshift   BigQuery       Synapse / Fabric\nStreaming        Kinesis    Pub/Sub        Event Hubs'),
  Tx('Sebutkan tiga cara menghemat biaya query di BigQuery.', 'Biaya dihitung dari data yang dipindai.',
     '1. Pilih kolom yang perlu saja (hindari SELECT *).\n2. Partisi tabel per tanggal dan filter tanggal di WHERE.\n3. Clustering pada kolom yang sering difilter, dan pakai tabel agregat untuk dashboard.'),
],
'Docker, Kubernetes & Terraform': [
  S('Tulis Dockerfile untuk skrip ETL Python yang memasang dependensi dari requirements.txt.', 'Mulai dari image python slim, salin requirements dulu agar cache layer terpakai.',
    'FROM python:3.12-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY etl.py .\nCMD ["python", "etl.py"]', lang='docker'),
  S('Tulis resource Terraform untuk bucket GCS bernama "toko-data-mentah" di region asia-southeast2.', 'resource "google_storage_bucket".',
    'resource "google_storage_bucket" "mentah" {\n  name     = "toko-data-mentah"\n  location = "asia-southeast2"\n\n  uniform_bucket_level_access = true\n}', lang='hcl'),
],
'Tes pipeline & observabilitas data': [
  Ym('Tulis tes dbt untuk model <code>fakta_penjualan</code>: id_trx unik dan tidak null, omzet tidak null, dan kota hanya nilai yang diizinkan.', 'tests: unique, not_null, accepted_values di schema.yml.',
     'version: 2\nmodels:\n  - name: fakta_penjualan\n    columns:\n      - name: id_trx\n        tests: [unique, not_null]\n      - name: omzet\n        tests: [not_null]\n      - name: kota\n        tests:\n          - accepted_values:\n              values: ["Medan", "Bandung", "Jakarta"]'),
  P('Tulis pemeriksaan kualitas data sederhana dengan pandas: jumlah baris, duplikat, nilai negatif, dan kesegaran data.', 'Kumpulkan hasil dalam dict, lalu gagal jika ada pelanggaran.',
    'import pandas as pd\n\ndf = pd.DataFrame({"id_trx": [1, 2, 2, 3], "omzet": [36000, -5, 18000, 9000],\n                   "tanggal": pd.to_datetime(["2026-11-01"] * 4)})\ncek = {\n    "baris": len(df),\n    "duplikat": int(df["id_trx"].duplicated().sum()),\n    "omzet_negatif": int((df["omzet"] < 0).sum()),\n    "umur_data_hari": (pd.Timestamp("2026-11-02") - df["tanggal"].max()).days,\n}\nprint(cek)\nprint("GAGAL" if cek["duplikat"] or cek["omzet_negatif"] else "LULUS")', "{'baris': 4, 'duplikat': 1, 'omzet_negatif': 1, 'umur_data_hari': 1}\nGAGAL"),
],
'Keamanan & privasi data': [
  P('Ganti email pelanggan dengan pseudonim yang konsisten memakai hash SHA-256 bergaram (salt).', 'hashlib.sha256((salt + email).encode()).hexdigest(); email yang sama selalu menghasilkan pseudonim yang sama.',
    'import hashlib\n\nSALT = "rahasia-dari-secret-manager"\n\ndef samarkan(email):\n    return hashlib.sha256((SALT + email.lower()).encode()).hexdigest()[:12]\n\nprint(samarkan("rina@mail.id") == samarkan("RINA@mail.id"))\nprint(len(samarkan("rina@mail.id")))', 'True\n12'),
  Tx('Terapkan prinsip least privilege untuk tim data: siapa mendapat akses apa?', 'Akses seminimal yang dibutuhkan pekerjaan.',
     'Data engineer : tulis ke lapisan bronze/silver, baca semua lapisan.\nAnalyst       : baca lapisan gold, tanpa kolom data pribadi.\nPipeline      : service account khusus per pipeline, bukan akun pribadi.\nData pribadi  : hanya peran tertentu, dengan log akses dan masking kolom.'),
],
}

SOAL = {'PDA_MODULES': PDA, 'DA_MODULES': DA, 'BI_MODULES': BI, 'DE_MODULES': DE}
