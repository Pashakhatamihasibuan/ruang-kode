"""Pendalaman jalur Data Science & AI: istilah dunia kerja dan contoh tambahan yang dijalankan."""
K = 'dsci'

D = {
'Data scientist dan alur kerjanya': dict(
  ist=[('Stakeholder', 'Pihak yang memakai hasil analisis (tim produk, marketing, manajemen). Data scientist harus menerjemahkan pertanyaan mereka menjadi masalah data.'),
       ('CRISP-DM', 'Kerangka kerja standar proyek data: business understanding, data understanding, data preparation, modeling, evaluation, deployment.'),
       ('Baseline', 'Patokan paling sederhana (rata-rata, aturan bisnis lama) yang harus dikalahkan model sebelum dianggap berguna.'),
       ('Data leakage', 'Informasi dari masa depan atau dari target yang bocor ke fitur, membuat model tampak hebat saat latihan tetapi gagal di produksi.'),
       ('Notebook vs pipeline', 'Notebook (Jupyter) untuk eksplorasi; kode final dipindah ke skrip/paket yang bisa diuji dan dijadwalkan.')],
  cx=[dict(t='Menerjemahkan pertanyaan bisnis menjadi masalah ML', b='Setiap proyek dimulai dari tabel seperti ini, ditulis bersama stakeholder sebelum menyentuh data.',
           code="masalah = [\n    ('Pelanggan mana yang akan berhenti?', 'klasifikasi', 'churn 30 hari (0/1)', 'recall pada 20% risiko tertinggi'),\n    ('Berapa stok minggu depan?', 'regresi deret waktu', 'unit terjual per SKU', 'MAPE'),\n    ('Kelompok pelanggan seperti apa?', 'clustering', '(tanpa target)', 'profil segmen masuk akal'),\n    ('Apakah tombol baru menaikkan penjualan?', 'eksperimen A/B', 'konversi', 'selang kepercayaan selisih'),\n]\nfor tanya, jenis, target, metrik in masalah:\n    print(f'{tanya:40} -> {jenis:20} | target: {target:22} | metrik: {metrik}')")]),

'NumPy: array, vektorisasi, dan broadcasting': dict(
  ist=[('Vektorisasi', 'Menulis operasi pada seluruh array sekaligus, bukan loop Python. Di tim, kode loop atas jutaan baris biasanya diminta direvisi.'),
       ('Broadcasting', 'Aturan NumPy menyesuaikan bentuk array berbeda agar bisa dioperasikan, misalnya (3,4) dikurangi (4,).'),
       ('dtype', 'Tipe data array (int64, float32). float32 menghemat setengah memori dan umum di deep learning.'),
       ('Shape', 'Ukuran tiap dimensi array. Bug paling sering di ML adalah shape yang tidak cocok.')],
  cx=[dict(t='Loop vs vektorisasi: ukur sendiri', code="import numpy as np, time\nx = np.random.default_rng(0).random(1_000_000)\n\nt = time.perf_counter(); hasil = [v * 2 + 1 for v in x]; loop = time.perf_counter() - t\nt = time.perf_counter(); hasil2 = x * 2 + 1; vek = time.perf_counter() - t\nprint(f'sama: {np.allclose(hasil, hasil2)}')\nprint(f'vektorisasi kira-kira {loop / vek:.0f}x lebih cepat')"),
      dict(t='Broadcasting untuk standardisasi per kolom', b='Mengurangi rata-rata dan membagi simpangan baku setiap kolom tanpa loop.',
           code="import numpy as np\nX = np.array([[170, 65, 30], [160, 50, 25], [180, 80, 40]], dtype=float)  # tinggi, berat, umur\nZ = (X - X.mean(axis=0)) / X.std(axis=0)     # (3,3) - (3,) -> broadcasting\nprint('shape X:', X.shape, ' shape mean:', X.mean(axis=0).shape)\nprint(Z.round(2))\nprint('rata-rata kolom setelah standardisasi:', Z.mean(axis=0).round(6))")]),

'pandas: Series, DataFrame, dan membaca data': dict(
  ist=[('Index', 'Label baris di pandas. Salah paham index menyebabkan join dan penggabungan yang keliru.'),
       ('Method chaining', 'Menulis transformasi berurutan dengan titik (df.query(...).assign(...).groupby(...)); gaya yang disukai karena mudah dibaca dan di-review.'),
       ('Tidy data', 'Setiap kolom satu variabel, setiap baris satu observasi. Format ini memudahkan groupby dan visualisasi.'),
       ('Parquet', 'Format berkas kolumnar yang jauh lebih cepat dan kecil daripada CSV; standar di data lake.')],
  cx=[dict(t='Method chaining: dari data mentah ke ringkasan', code="import pandas as pd\ndf = pd.DataFrame({'kota': ['Medan', 'Medan', 'Bandung', 'Bandung', 'Jakarta'],\n                   'produk': ['Kopi', 'Teh', 'Kopi', 'Kopi', 'Teh'],\n                   'qty': [3, 1, 2, 5, 4], 'harga': [65000, 40000, 65000, 65000, 40000]})\nringkas = (df\n    .assign(nilai=lambda d: d.qty * d.harga)\n    .query('produk == \"Kopi\"')\n    .groupby('kota', as_index=False)\n    .agg(transaksi=('qty', 'size'), omzet=('nilai', 'sum'))\n    .sort_values('omzet', ascending=False))\nprint(ringkas)"),
      dict(t='Wide ke long (tidy) dengan melt', code="import pandas as pd\nwide = pd.DataFrame({'toko': ['A', 'B'], 'Jan': [10, 7], 'Feb': [12, 9], 'Mar': [15, 8]})\nlong = wide.melt(id_vars='toko', var_name='bulan', value_name='penjualan')\nprint(long)\nprint(long.pivot(index='toko', columns='bulan', values='penjualan'))")]),

'Vektor, matriks, dan perkalian matriks': dict(
  ist=[('Dot product', 'Jumlah hasil kali elemen dua vektor; dasar skor model linear dan kemiripan (similarity).'),
       ('Cosine similarity', 'Kemiripan arah dua vektor (−1 sampai 1); dipakai di pencarian semantik dan rekomendasi.'),
       ('Matrix multiplication', 'Inti semua lapisan neural network: keluaran = masukan @ bobot + bias.'),
       ('Embedding', 'Vektor angka yang mewakili kata, produk, atau pengguna sehingga kemiripan bisa dihitung.')],
  cx=[dict(t='Cosine similarity untuk mencari produk mirip', code="import numpy as np\n# fitur: [manis, pahit, asam, susu]\nproduk = {'Kopi Susu Aren': [0.8, 0.4, 0.1, 0.9], 'Espresso': [0.1, 0.9, 0.3, 0.0],\n          'Latte': [0.4, 0.4, 0.1, 0.9], 'Americano': [0.1, 0.8, 0.3, 0.0]}\nnama = list(produk); V = np.array(list(produk.values()))\nN = V / np.linalg.norm(V, axis=1, keepdims=True)\nS = N @ N.T\nfor i, n in enumerate(nama):\n    j = np.argsort(-S[i])[1]\n    print(f'{n:15} paling mirip {nama[j]:15} (cos={S[i, j]:.2f})')"),
      dict(t='Satu lapisan neural network = perkalian matriks', code="import numpy as np\nX = np.array([[1.0, 2.0, 0.5], [0.0, 1.0, 1.5]])     # 2 contoh, 3 fitur\nW = np.array([[0.2, -0.5], [0.4, 0.1], [-0.3, 0.8]])  # 3 masukan -> 2 neuron\nb = np.array([0.1, -0.2])\nH = np.maximum(0, X @ W + b)                          # ReLU\nprint('shape:', X.shape, '@', W.shape, '->', H.shape)\nprint(H)")]),

'Turunan dan gradient descent': dict(
  ist=[('Learning rate', 'Besar langkah tiap pembaruan bobot; hyperparameter yang paling sering disetel.'),
       ('Loss function', 'Fungsi yang mengukur seberapa salah model (MSE, cross-entropy). Training = meminimalkan loss.'),
       ('Epoch / batch', 'Epoch: satu putaran seluruh data. Batch: potongan data per pembaruan (mini-batch gradient descent).'),
       ('Konvergen', 'Loss berhenti turun secara berarti; tanda training bisa dihentikan (early stopping).')],
  cx=[dict(t='Mini-batch gradient descent untuk regresi', code="import numpy as np\nrng = np.random.default_rng(1)\nX = rng.normal(size=(1000, 2)); y = X @ np.array([3.0, -2.0]) + 0.5 + rng.normal(0, 0.1, 1000)\nw, b, lr = np.zeros(2), 0.0, 0.1\nfor epoch in range(5):\n    idx = rng.permutation(1000)\n    for s in range(0, 1000, 100):                  # batch 100\n        j = idx[s:s + 100]; err = X[j] @ w + b - y[j]\n        w -= lr * 2 * X[j].T @ err / len(j); b -= lr * 2 * err.mean()\n    print(f'epoch {epoch + 1}: loss={np.mean((X @ w + b - y) ** 2):.4f}  w={w.round(2)}  b={b:.2f}')")]),

'Statistik deskriptif dan distribusi': dict(
  ist=[('Median vs mean', 'Median tahan pencilan; untuk gaji, harga rumah, dan durasi sesi biasanya median yang dilaporkan.'),
       ('Persentil (p50, p95, p99)', 'Dipakai luas di tim teknik untuk latensi: "p95 waktu muat 1,2 detik" berarti 95% permintaan lebih cepat dari itu.'),
       ('Skewness', 'Kemiringan distribusi; data transaksi biasanya miring kanan (banyak kecil, sedikit sangat besar).'),
       ('IQR', 'Rentang antarkuartil (Q3 − Q1), dasar aturan pencilan 1,5 × IQR di boxplot.')],
  cx=[dict(t='Kenapa laporan memakai median dan p95', code="import numpy as np\nrng = np.random.default_rng(4)\nlatensi = np.concatenate([rng.normal(200, 30, 980), rng.normal(2500, 400, 20)])  # ms, ada lonjakan\nprint(f'mean   : {latensi.mean():.0f} ms  <- tertarik pencilan')\nprint(f'median : {np.median(latensi):.0f} ms')\nprint(f'p95    : {np.percentile(latensi, 95):.0f} ms   p99: {np.percentile(latensi, 99):.0f} ms')\nq1, q3 = np.percentile(latensi, [25, 75]); batas = q3 + 1.5 * (q3 - q1)\nprint(f'pencilan (> {batas:.0f} ms): {(latensi > batas).sum()} permintaan')")]),

'Probabilitas, sampling, dan teorema limit pusat': dict(
  ist=[('Sampling bias', 'Sampel tidak mewakili populasi, misalnya survei hanya lewat Instagram. Hasil analisis bisa menyesatkan.'),
       ('Stratified sampling', 'Mengambil sampel proporsional per kelompok (kota, kelas) agar semua kelompok terwakili.'),
       ('Standard error', 'Simpangan baku dari rata-rata sampel = σ/√n. Makin besar n, makin presisi.'),
       ('Bootstrap', 'Mengambil sampel ulang dengan pengembalian untuk memperkirakan ketidakpastian tanpa rumus.')],
  cx=[dict(t='Selang kepercayaan dengan bootstrap', b='Cara praktis yang sering dipakai analis untuk metrik yang rumusnya rumit, misalnya median.',
           code="import numpy as np\nrng = np.random.default_rng(2)\nbelanja = rng.lognormal(mean=12, sigma=0.8, size=400)       # nilai belanja (rupiah)\nmed = [np.median(rng.choice(belanja, belanja.size)) for _ in range(2000)]\nlo, hi = np.percentile(med, [2.5, 97.5])\nprint(f'median belanja: Rp{np.median(belanja):,.0f}')\nprint(f'selang 95% (bootstrap): Rp{lo:,.0f} s.d. Rp{hi:,.0f}')")]),

'Uji hipotesis dan p-value': dict(
  ist=[('Statistically significant', 'Hasil yang kecil kemungkinannya terjadi jika tidak ada efek (biasanya p &lt; 0,05). Bukan berarti efeknya besar atau penting.'),
       ('Practical significance', 'Apakah efeknya cukup besar untuk berarti bagi bisnis. Selalu laporkan besar efek dan selang kepercayaan.'),
       ('False positive (Type I)', 'Menyimpulkan ada efek padahal tidak. Makin banyak uji, makin besar peluangnya.'),
       ('p-hacking', 'Mencoba banyak analisis sampai menemukan p &lt; 0,05. Dilarang dalam praktik yang jujur; tetapkan rencana analisis di awal.')],
  cx=[dict(t='Bahaya menguji banyak metrik sekaligus', code="import numpy as np\nfrom scipy import stats\nrng = np.random.default_rng(0)\nsignifikan = 0\nfor metrik in range(20):                 # 20 metrik, padahal TIDAK ADA efek sungguhan\n    a, b = rng.normal(0, 1, 500), rng.normal(0, 1, 500)\n    signifikan += stats.ttest_ind(a, b).pvalue < 0.05\nprint(f'{signifikan} dari 20 metrik tampak signifikan hanya karena kebetulan')\nprint('Koreksi Bonferroni: ambang menjadi', 0.05 / 20)")]),

'A/B test: ukuran sampel, sensitivitas, dan metrik rasio': dict(
  ist=[('MDE (minimum detectable effect)', 'Efek terkecil yang ingin bisa dideteksi; menentukan berapa lama tes harus berjalan.'),
       ('Statistical power', 'Peluang mendeteksi efek yang memang ada; standar industri 80%.'),
       ('Guardrail metric', 'Metrik yang tidak boleh memburuk (waktu muat, keluhan) walau metrik utama naik.'),
       ('SRM (sample ratio mismatch)', 'Pembagian trafik tidak sesuai rencana (misal 50:50 jadi 52:48); tanda ada bug dan hasil tes tidak bisa dipercaya.')],
  cx=[dict(t='Cek SRM sebelum membaca hasil', code="from scipy import stats\nA, B = 50_812, 49_011                 # pengunjung tiap grup, rencana 50:50\nchi2, p = stats.chisquare([A, B])\nprint(f'proporsi A: {A / (A + B):.3%}  p-value SRM: {p:.2e}')\nprint('SRM terdeteksi: periksa pembagian trafik dulu!' if p < 0.001 else 'pembagian trafik sehat')")]),

'Regresi linear: menarik garis terbaik': dict(
  ist=[('Koefisien', 'Perubahan target untuk tambahan 1 unit fitur, dengan fitur lain tetap.'),
       ('Multikolinearitas', 'Fitur-fitur saling berkorelasi tinggi sehingga koefisien tidak stabil; cek dengan VIF.'),
       ('Residual', 'Selisih nilai asli dan tebakan; pola pada residual menandakan model kurang tepat.'),
       ('Heteroskedastisitas', 'Sebaran residual berubah seiring nilai tebakan; sering terjadi pada data harga.')],
  cx=[dict(t='Laporan regresi ala statsmodels', code="import numpy as np, pandas as pd\nimport statsmodels.formula.api as smf\nrng = np.random.default_rng(5)\ndf = pd.DataFrame({'luas': rng.uniform(30, 150, 120), 'jarak_km': rng.uniform(1, 25, 120)})\ndf['harga'] = 150 + 9 * df.luas - 12 * df.jarak_km + rng.normal(0, 80, 120)\nm = smf.ols('harga ~ luas + jarak_km', data=df).fit()\nprint(m.params.round(2))\nprint('R2:', round(m.rsquared, 3))\nprint(m.conf_int().round(2).rename(columns={0: 'batas bawah', 1: 'batas atas'}))")]),

'Deret waktu: tren, musiman, dan rolling': dict(
  ist=[('Seasonality', 'Pola berulang (mingguan, bulanan, Ramadan, gajian). Wajib dipertimbangkan dalam forecasting penjualan di Indonesia.'),
       ('Stationarity', 'Rata-rata dan varians tidak berubah seiring waktu; syarat banyak model klasik seperti ARIMA.'),
       ('Lag feature', 'Nilai periode sebelumnya sebagai fitur (penjualan kemarin, minggu lalu).'),
       ('Backtesting', 'Menguji model forecasting di masa lalu dengan jendela bergeser; jangan acak data deret waktu.')],
  cx=[dict(t='Fitur lag dan validasi berbasis waktu', code="import numpy as np, pandas as pd\nrng = np.random.default_rng(3)\ntgl = pd.date_range('2026-01-01', periods=120)\njual = 100 + 20 * (tgl.dayofweek >= 5) + np.arange(120) * 0.5 + rng.normal(0, 5, 120)\ndf = pd.DataFrame({'jual': jual}, index=tgl)\ndf['lag_1'] = df.jual.shift(1); df['lag_7'] = df.jual.shift(7)\ndf['rata7'] = df.jual.shift(1).rolling(7).mean()      # shift dulu agar tidak bocor\ndf = df.dropna()\nlatih, uji = df[:'2026-03-31'], df['2026-04-01':]\nmae_naif = (uji.jual - uji.lag_7).abs().mean()\nprint(f'baris latih {len(latih)}, uji {len(uji)} (dipisah berdasarkan waktu)')\nprint(f'MAE patokan musiman (lag 7): {mae_naif:.1f}')")]),

'Mencocokkan distribusi pada data': dict(
  ist=[('Lognormal', 'Distribusi umum untuk pendapatan, harga, dan nilai transaksi yang miring kanan.'),
       ('Poisson', 'Jumlah kejadian per satuan waktu (pesanan per jam, keluhan per hari).'),
       ('QQ-plot', 'Grafik untuk membandingkan data dengan distribusi teoretis.'),
       ('Goodness of fit', 'Seberapa cocok distribusi dengan data; diuji misalnya dengan Kolmogorov-Smirnov.')],
  cx=[dict(t='Peluang lonjakan pesanan dengan Poisson', b='Dipakai tim operasional untuk menentukan jumlah kurir.',
           code="from scipy import stats\nrata_per_jam = 18\nfor k in [20, 25, 30]:\n    print(f'P(pesanan > {k} per jam) = {stats.poisson.sf(k, rata_per_jam):.3f}')\nprint('kurir untuk menutup 99% jam:', int(stats.poisson.ppf(0.99, rata_per_jam)) // 4 + 1, '(1 kurir = 4 pesanan/jam)')")]),

'Memahami data: info, describe, dan nilai hilang': dict(
  ist=[('Data profiling', 'Pemeriksaan awal: tipe, jumlah kosong, nilai unik, rentang. Langkah wajib sebelum modeling.'),
       ('MCAR / MAR / MNAR', 'Jenis nilai hilang: acak total, bergantung kolom lain, atau bergantung nilainya sendiri. Menentukan cara mengisinya.'),
       ('Imputasi', 'Mengisi nilai hilang (median, modus, model). Hitung nilai pengisi dari data latih saja.'),
       ('Cardinality', 'Jumlah nilai unik kolom kategori; kardinalitas tinggi (ID, kode pos) perlu perlakuan khusus.')],
  cx=[dict(t='Laporan profil data dalam satu fungsi', code="import numpy as np, pandas as pd\ndf = pd.DataFrame({'umur': [25, np.nan, 41, 33, np.nan, 52], 'kota': ['Medan', 'Medan', None, 'Bandung', 'Jakarta', 'Medan'],\n                   'gaji': [5.2, 7.1, 9.0, np.nan, 6.4, 12.5], 'id': ['u1', 'u2', 'u3', 'u4', 'u5', 'u6']})\ndef profil(d):\n    return pd.DataFrame({'tipe': d.dtypes.astype(str), 'kosong_%': (100 * d.isna().mean()).round(0),\n                         'unik': d.nunique(), 'contoh': d.iloc[0]})\nprint(profil(df))\nprint('baris lengkap:', len(df.dropna()), 'dari', len(df))")]),

'Matplotlib: grafik garis, batang, dan histogram': dict(
  ist=[('Chart junk', 'Hiasan yang tidak menambah informasi (3D, bayangan, gradasi). Hindari di laporan profesional.'),
       ('Data-ink ratio', 'Prinsip Tufte: sebagian besar tinta grafik harus untuk data.'),
       ('Bin', 'Rentang kelompok di histogram; jumlah bin mengubah kesan bentuk distribusi.'),
       ('Small multiples', 'Banyak grafik kecil dengan sumbu sama untuk membandingkan kelompok.')],
  cx=[dict(t='Gaya grafik siap laporan', b='Pola yang dipakai banyak tim: hapus bingkai atas/kanan, beri judul berupa kesimpulan, dan label langsung.',
           code="import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nbulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun']\nomzet = [210, 198, 235, 260, 255, 301]\nfig, ax = plt.subplots(figsize=(6, 3))\nax.plot(bulan, omzet, marker='o', color='#C2185B')\nax.spines[['top', 'right']].set_visible(False)\nax.set_title('Omzet naik 43% sejak Januari (juta Rp)', loc='left')\nax.annotate('Promo gajian', xy=(5, 301), xytext=(3.2, 290), arrowprops={'arrowstyle': '->'})\nprint('judul =', ax.get_title(loc='left'))")]),

'Matplotlib: scatter, subplot, dan anotasi': dict(
  ist=[('Overplotting', 'Titik saling menumpuk sehingga pola tersembunyi; atasi dengan transparansi (alpha), sampel, atau hexbin.'),
       ('Facet', 'Membagi grafik per kategori (istilah di seaborn/ggplot).'),
       ('Annotation', 'Teks atau panah yang menjelaskan titik penting; membuat grafik "bercerita".'),
       ('Figure vs Axes', 'Figure = kanvas; Axes = satu panel grafik. Gaya berorientasi objek (fig, ax) lebih rapi untuk kode produksi.')],
  cx=[dict(t='Mengatasi overplotting', code="import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt, numpy as np\nrng = np.random.default_rng(0)\nx = rng.normal(size=20000); y = x * 0.6 + rng.normal(size=20000)\nfig, ax = plt.subplots(1, 2, figsize=(8, 3), sharey=True)\nax[0].scatter(x, y, s=2); ax[0].set_title('tanpa alpha: pekat')\nhb = ax[1].hexbin(x, y, gridsize=40, cmap='viridis'); ax[1].set_title('hexbin: kepadatan terlihat')\nprint('jumlah sel hexbin berisi:', int((hb.get_array() > 0).sum()))")]),

'Korelasi dan heatmap': dict(
  ist=[('Korelasi ≠ kausalitas', 'Dua hal bergerak bersama belum tentu saling menyebabkan; bisa ada faktor ketiga (confounder).'),
       ('Spearman', 'Korelasi berbasis peringkat; tahan pencilan dan hubungan monoton tidak lurus.'),
       ('Confounder', 'Variabel yang memengaruhi keduanya, misalnya musim panas menaikkan penjualan es krim dan kasus tenggelam.'),
       ('Feature redundancy', 'Fitur berkorelasi sangat tinggi; salah satu bisa dibuang.')],
  cx=[dict(t='Pearson vs Spearman saat ada pencilan', code="import numpy as np, pandas as pd\nrng = np.random.default_rng(1)\nx = np.arange(50, dtype=float); y = x + rng.normal(0, 5, 50)\ny[-1] = -300                                  # satu pencilan\nd = pd.DataFrame({'x': x, 'y': y})\nprint('Pearson :', round(d.corr().iloc[0, 1], 2))\nprint('Spearman:', round(d.corr(method='spearman').iloc[0, 1], 2))")]),

'Alur ML: fitur, target, dan train/test split': dict(
  ist=[('Holdout set', 'Data yang disimpan dan hanya dipakai sekali di akhir untuk penilaian jujur.'),
       ('Validation set', 'Data untuk memilih model dan hyperparameter, terpisah dari test.'),
       ('Class imbalance', 'Satu kelas jauh lebih sedikit (fraud 0,5%); akurasi menjadi menyesatkan.'),
       ('Reproducibility', 'Hasil bisa diulang: set random_state, catat versi data dan pustaka.')],
  cx=[dict(t='Train / validation / test dalam satu langkah', code="import numpy as np\nfrom sklearn.model_selection import train_test_split\nX = np.arange(1000).reshape(-1, 1); y = (np.arange(1000) % 10 == 0).astype(int)\nX_tmp, X_test, y_tmp, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)\nX_tr, X_val, y_tr, y_val = train_test_split(X_tmp, y_tmp, test_size=0.25, stratify=y_tmp, random_state=42)\nfor n, a in [('train', y_tr), ('val', y_val), ('test', y_test)]:\n    print(f'{n:5}: {len(a):4} baris, positif {a.mean():.1%}')")]),

'Regresi dan metriknya: MAE, RMSE, R²': dict(
  ist=[('MAPE', 'Rata-rata persentase kesalahan; mudah dipahami bisnis, tetapi rusak saat nilai asli mendekati nol.'),
       ('Bias model', 'Model cenderung menebak terlalu tinggi atau rendah; cek rata-rata residual.'),
       ('Quantile regression', 'Memprediksi persentil (misal p90 waktu kirim) untuk menjanjikan SLA.'),
       ('Target transformation', 'Memprediksi log(harga) lalu dikembalikan; membantu target miring kanan.')],
  cx=[dict(t='Membandingkan metrik pada kasus yang sama', code="import numpy as np\nasli = np.array([100, 120, 80, 300, 90])\ntebak = np.array([110, 115, 85, 200, 95])\ne = tebak - asli\nprint(f'MAE  : {np.abs(e).mean():.1f}')\nprint(f'RMSE : {np.sqrt((e ** 2).mean()):.1f}   <- terdorong satu kesalahan besar (300 vs 200)')\nprint(f'MAPE : {(np.abs(e) / asli).mean():.1%}')\nprint(f'bias : {e.mean():+.1f} (negatif = cenderung menebak terlalu rendah)')")]),

'Klasifikasi: logistic regression dan confusion matrix': dict(
  ist=[('Precision@k', 'Ketepatan pada k kasus teratas; cocok saat tim hanya sanggup menindaklanjuti sebagian (misal 200 pelanggan per minggu).'),
       ('Kalibrasi', 'Apakah peluang 0,8 benar-benar terjadi 80% kali; penting untuk keputusan berbasis risiko.'),
       ('F1-score', 'Rata-rata harmonik precision dan recall.'),
       ('Cost-sensitive', 'Memilih ambang berdasarkan biaya salah: FN dan FP punya harga berbeda.')],
  cx=[dict(t='Memilih ambang berdasarkan biaya', code="import numpy as np\nrng = np.random.default_rng(0)\ny = (rng.random(2000) < 0.2).astype(int)\nskor = np.clip(y * 0.35 + rng.normal(0.35, 0.18, 2000), 0, 1)\nBIAYA_FN, BIAYA_FP = 500_000, 50_000      # kehilangan pelanggan vs biaya voucher\nfor t in [0.3, 0.4, 0.5, 0.6, 0.7]:\n    p = skor >= t\n    fn, fp = ((~p) & (y == 1)).sum(), (p & (y == 0)).sum()\n    print(f'ambang {t}: FN={fn:3} FP={fp:4} biaya=Rp{fn * BIAYA_FN + fp * BIAYA_FP:,}')")]),

'Decision tree dan random forest': dict(
  ist=[('Feature importance', 'Ukuran kontribusi fitur; versi impurity bisa bias ke fitur kontinu, gunakan permutation importance untuk laporan.'),
       ('Out-of-bag (OOB)', 'Penilaian random forest memakai data yang tidak terambil saat bootstrap; validasi "gratis".'),
       ('max_depth / min_samples_leaf', 'Hyperparameter untuk membatasi pohon agar tidak overfit.'),
       ('Interpretability', 'Kemampuan menjelaskan keputusan model ke bisnis atau regulator.')],
  cx=[dict(t='Permutation importance yang lebih jujur', code="from sklearn.datasets import make_classification\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.inspection import permutation_importance\nfrom sklearn.model_selection import train_test_split\nX, y = make_classification(800, n_features=5, n_informative=2, n_redundant=0, random_state=0)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nrf = RandomForestClassifier(200, oob_score=True, random_state=0).fit(Xtr, ytr)\nprint('OOB score:', round(rf.oob_score_, 3))\npi = permutation_importance(rf, Xte, yte, n_repeats=10, random_state=0)\nfor i in pi.importances_mean.argsort()[::-1]:\n    print(f'fitur {i}: {pi.importances_mean[i]:.3f}')")]),

'Clustering K-Means: mengelompokkan tanpa label': dict(
  ist=[('Silhouette score', 'Ukuran seberapa rapat anggota satu kelompok dan seberapa terpisah dari kelompok lain (−1 sampai 1).'),
       ('Elbow method', 'Memilih k di titik penurunan inertia mulai melandai.'),
       ('Segmentasi', 'Istilah bisnis untuk hasil clustering pelanggan; setiap segmen perlu nama dan aksi.'),
       ('k-means++', 'Cara memilih pusat awal yang menyebar; bawaan scikit-learn.')],
  cx=[dict(t='Memilih k dengan silhouette', code="from sklearn.datasets import make_blobs\nfrom sklearn.cluster import KMeans\nfrom sklearn.metrics import silhouette_score\nX, _ = make_blobs(500, centers=4, cluster_std=1.0, random_state=3)\nfor k in range(2, 7):\n    lab = KMeans(k, n_init=10, random_state=0).fit_predict(X)\n    print(f'k={k}: silhouette={silhouette_score(X, lab):.3f}')")]),

'Validasi silang dan mencegah overfitting': dict(
  ist=[('K-fold CV', 'Data dibagi k bagian, model dilatih k kali; skor rata-rata lebih stabil.'),
       ('TimeSeriesSplit', 'CV untuk data waktu: latih di masa lalu, uji di masa depan.'),
       ('GroupKFold', 'Memastikan data satu pelanggan/pasien tidak muncul di latih dan uji sekaligus.'),
       ('Learning curve', 'Grafik skor terhadap jumlah data; menunjukkan apakah menambah data akan membantu.')],
  cx=[dict(t='Kebocoran karena grup yang sama', b='Satu pelanggan punya banyak baris. KFold biasa membuat skor terlalu optimis.',
           code="import numpy as np\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.model_selection import cross_val_score, KFold, GroupKFold\nrng = np.random.default_rng(0)\npelanggan = np.repeat(np.arange(100), 10)\nciri = rng.normal(size=(100, 3))[pelanggan] + rng.normal(0, 0.05, (1000, 3))\ny = rng.integers(0, 2, 100)[pelanggan]          # label acak per pelanggan: tidak ada pola sungguhan\nm = RandomForestClassifier(100, random_state=0)\nprint('KFold biasa :', cross_val_score(m, ciri, y, cv=KFold(5, shuffle=True, random_state=0)).mean().round(2))\nprint('GroupKFold  :', cross_val_score(m, ciri, y, cv=GroupKFold(5), groups=pelanggan).mean().round(2))")]),

'Linear regression dari nol': dict(
  ist=[('OLS', 'Ordinary least squares: metode mencari koefisien yang meminimalkan jumlah kuadrat residual.'),
       ('Intercept', 'Nilai tebakan saat semua fitur nol (b).'),
       ('Normal equation', 'Rumus tertutup w = (XᵀX)⁻¹Xᵀy; praktis untuk fitur sedikit.'),
       ('Feature scaling', 'Menyamakan skala fitur agar gradient descent stabil dan cepat.')],
  cx=[dict(t='Linear regression dengan banyak fitur memakai lstsq', code="import numpy as np\nrng = np.random.default_rng(8)\nX = rng.normal(size=(200, 3)); w_asli = np.array([2.0, -1.0, 0.5])\ny = X @ w_asli + 4 + rng.normal(0, 0.1, 200)\nXb = np.column_stack([np.ones(200), X])\nkoef, *_ = np.linalg.lstsq(Xb, y, rcond=None)\nprint('intercept:', koef[0].round(3), ' w:', koef[1:].round(3))")]),

'Regresi polinomial, overfitting, Ridge dan Lasso': dict(
  ist=[('Bias-variance trade-off', 'Model sederhana bias tinggi, model rumit varians tinggi; cari titik seimbang.'),
       ('Regularization', 'Denda pada koefisien besar agar model lebih sederhana dan stabil.'),
       ('Elastic Net', 'Gabungan L1 dan L2; dipakai saat banyak fitur saling berkorelasi.'),
       ('Hyperparameter alpha', 'Kekuatan denda; dipilih dengan cross-validation (RidgeCV, LassoCV).')],
  cx=[dict(t='LassoCV memilih fitur secara otomatis', code="import numpy as np\nfrom sklearn.linear_model import LassoCV\nrng = np.random.default_rng(0)\nX = rng.normal(size=(300, 10))\ny = 3 * X[:, 0] - 2 * X[:, 3] + rng.normal(0, 0.5, 300)     # hanya fitur 0 dan 3 berguna\nm = LassoCV(cv=5, random_state=0).fit(X, y)\nprint('alpha terpilih:', round(m.alpha_, 4))\nprint('koefisien:', m.coef_.round(2))\nprint('fitur yang dipakai:', np.flatnonzero(np.abs(m.coef_) > 1e-6).tolist())")]),

'Logistic regression dari nol': dict(
  ist=[('Log-odds (logit)', 'Logaritma dari peluang/(1−peluang); koefisien logistic regression bekerja di skala ini.'),
       ('Odds ratio', 'e^koefisien: berapa kali peluang relatif berubah per kenaikan 1 unit fitur.'),
       ('Cross-entropy', 'Nama lain log loss; loss standar klasifikasi termasuk di deep learning.'),
       ('Regularization C', 'Di scikit-learn, C = 1/kekuatan regularisasi; C kecil = model lebih sederhana.')],
  cx=[dict(t='Membaca odds ratio untuk laporan', code="import numpy as np\nfrom sklearn.linear_model import LogisticRegression\nrng = np.random.default_rng(1)\nkeluhan = rng.poisson(1.5, 1000); lama = rng.integers(1, 36, 1000)\np = 1 / (1 + np.exp(-(-1 + 0.7 * keluhan - 0.08 * lama)))\nchurn = (rng.random(1000) < p).astype(int)\nm = LogisticRegression().fit(np.column_stack([keluhan, lama]), churn)\nfor nama, k in zip(['keluhan', 'lama_bulan'], m.coef_[0]):\n    print(f'{nama:10}: koef {k:+.2f} -> odds x{np.exp(k):.2f} per +1')")]),

'K-Nearest Neighbors (KNN)': dict(
  ist=[('Lazy learner', 'Algoritma yang tidak membangun model saat training; semua kerja terjadi saat prediksi.'),
       ('Curse of dimensionality', 'Di dimensi tinggi semua titik terasa sama jauhnya sehingga KNN melemah.'),
       ('Distance metric', 'Euclidean, Manhattan, cosine; pilihannya memengaruhi hasil.'),
       ('Approximate nearest neighbor (ANN)', 'Pencarian tetangga cepat untuk jutaan vektor (FAISS, HNSW); dasar vector database.')],
  cx=[dict(t='Pengaruh standardisasi pada KNN', code="from sklearn.datasets import load_wine\nfrom sklearn.model_selection import cross_val_score\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nX, y = load_wine(return_X_y=True)\nprint('tanpa skala :', cross_val_score(KNeighborsClassifier(5), X, y, cv=5).mean().round(3))\nprint('dengan skala:', cross_val_score(make_pipeline(StandardScaler(), KNeighborsClassifier(5)), X, y, cv=5).mean().round(3))")]),

'Naive Bayes: klasifikasi teks': dict(
  ist=[('Tokenisasi', 'Memecah teks menjadi kata/token; langkah pertama setiap NLP.'),
       ('Stopword', 'Kata sangat umum ("yang", "dan") yang sering dibuang.'),
       ('TF-IDF', 'Bobot kata: sering di dokumen ini tetapi jarang di dokumen lain = penting.'),
       ('Laplace smoothing', 'Menambah hitungan kecil agar kata yang belum pernah muncul tidak membuat peluang nol.')],
  cx=[dict(t='TF-IDF + Naive Bayes dalam Pipeline', code="from sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.naive_bayes import MultinomialNB\nfrom sklearn.pipeline import make_pipeline\nulasan = ['barang bagus pengiriman cepat', 'kualitas mantap sesuai foto', 'puas banget recommended',\n          'barang rusak kecewa', 'pengiriman lama sekali', 'tidak sesuai deskripsi kecewa']\nlabel = ['positif'] * 3 + ['negatif'] * 3\nm = make_pipeline(TfidfVectorizer(), MultinomialNB()).fit(ulasan, label)\nfor t in ['pengiriman cepat barang mantap', 'kecewa barang tidak sesuai']:\n    print(f'{t:32} -> {m.predict([t])[0]}')")]),

'Decision tree dari nol: Gini dan pemisahan terbaik': dict(
  ist=[('Impurity', 'Ketidakmurnian kelompok; Gini dan entropy adalah ukuran yang umum.'),
       ('Information gain', 'Penurunan entropy setelah pemisahan.'),
       ('Pruning', 'Memangkas cabang yang tidak menambah akurasi untuk mencegah overfit.'),
       ('Greedy algorithm', 'Memilih pemisahan terbaik di setiap langkah tanpa melihat jauh ke depan.')],
  cx=[dict(t='Gini vs entropy pada kelompok yang sama', code="import numpy as np\ndef gini(p): return 1 - np.sum(np.square(p))\ndef entropy(p): p = np.array([x for x in p if x > 0]); return -np.sum(p * np.log2(p))\nfor p in [(1, 0), (0.9, 0.1), (0.7, 0.3), (0.5, 0.5)]:\n    print(f'proporsi {p}: Gini={gini(p):.3f}  entropy={entropy(p):.3f}')")]),

'Feature engineering dan Pipeline': dict(
  ist=[('Target encoding', 'Mengganti kategori dengan rata-rata target; kuat tetapi rawan bocor, hitung dalam CV.'),
       ('Feature store', 'Sistem penyimpan fitur yang sama untuk training dan produksi (Feast, Tecton).'),
       ('Training-serving skew', 'Fitur dihitung berbeda saat latihan dan produksi; penyebab umum model gagal.'),
       ('ColumnTransformer', 'Komponen scikit-learn untuk menerapkan transformasi berbeda per kolom.')],
  cx=[dict(t='Fitur tanggal dan rasio yang sering dipakai', code="import pandas as pd\nd = pd.DataFrame({'waktu': pd.to_datetime(['2026-11-01 08:15', '2026-11-08 21:40', '2026-11-25 12:05']),\n                  'total': [150000, 420000, 90000], 'item': [3, 6, 1]})\nf = d.assign(jam=d.waktu.dt.hour, akhir_pekan=d.waktu.dt.dayofweek >= 5,\n             tanggal_gajian=d.waktu.dt.day.isin([25, 26, 27, 28, 1]),\n             harga_per_item=d.total / d.item)\nprint(f.drop(columns='waktu'))")]),

'Gradient boosting dan tuning hyperparameter': dict(
  ist=[('Early stopping', 'Menghentikan penambahan pohon saat skor validasi berhenti membaik.'),
       ('RandomizedSearchCV', 'Mencoba kombinasi acak; lebih hemat daripada grid untuk banyak hyperparameter.'),
       ('Optuna / Bayesian optimization', 'Pencarian hyperparameter cerdas yang belajar dari percobaan sebelumnya.'),
       ('XGBoost / LightGBM / CatBoost', 'Pustaka boosting industri; CatBoost unggul untuk banyak kolom kategori.')],
  cx=[dict(t='Early stopping pada HistGradientBoosting', code="from sklearn.datasets import make_classification\nfrom sklearn.ensemble import HistGradientBoostingClassifier\nX, y = make_classification(3000, n_features=20, random_state=1)\nm = HistGradientBoostingClassifier(max_iter=1000, early_stopping=True, validation_fraction=0.15,\n                                   n_iter_no_change=20, random_state=0).fit(X, y)\nprint('pohon yang benar-benar dipakai:', m.n_iter_, 'dari maksimal 1000')")]),

'PCA: meringkas banyak fitur': dict(
  ist=[('Explained variance', 'Porsi variasi data yang dipertahankan setiap komponen.'),
       ('Loading', 'Bobot fitur asli dalam setiap komponen; dipakai untuk menafsirkan komponen.'),
       ('Dimensionality reduction', 'Mengurangi jumlah fitur sambil menjaga informasi.'),
       ('Whitening', 'Membuat komponen berskala sama; kadang dipakai sebelum algoritma lain.')],
  cx=[dict(t='Berapa komponen untuk 95% informasi?', code="import numpy as np\nfrom sklearn.datasets import load_digits\nfrom sklearn.decomposition import PCA\nX = load_digits().data\nkum = np.cumsum(PCA().fit(X).explained_variance_ratio_)\nfor target in [0.8, 0.9, 0.95]:\n    print(f'{target:.0%} variasi -> {np.searchsorted(kum, target) + 1} komponen dari {X.shape[1]}')")]),

'Support Vector Machine dan kernel': dict(
  ist=[('Kernel trick', 'Menghitung kemiripan di ruang berdimensi tinggi tanpa membentuk ruang itu secara eksplisit.'),
       ('Soft margin', 'Margin yang membolehkan sebagian kesalahan; diatur parameter C.'),
       ('RBF / Gaussian kernel', 'Kernel paling umum untuk pola melengkung.'),
       ('LinearSVC', 'Versi linear yang cepat untuk data teks berdimensi tinggi.')],
  cx=[dict(t='Mencari C dan gamma dengan GridSearchCV', code="from sklearn.datasets import make_moons\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.svm import SVC\nX, y = make_moons(400, noise=0.25, random_state=0)\ng = GridSearchCV(SVC(), {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 1, 10]}, cv=5).fit(X, y)\nprint('terbaik:', g.best_params_, ' akurasi CV:', round(g.best_score_, 3))")]),

'Ensemble: bagging, AdaBoost, dan stacking': dict(
  ist=[('Wisdom of crowds', 'Gabungan banyak model yang kesalahannya berbeda lebih akurat daripada satu model.'),
       ('Voting classifier', 'Ensemble paling sederhana: suara terbanyak (hard) atau rata-rata peluang (soft).'),
       ('Blending', 'Variasi stacking yang memakai satu set holdout, bukan CV.'),
       ('Diversity', 'Model dalam ensemble sebaiknya berbeda jenis agar kesalahannya tidak sama.')],
  cx=[dict(t='Soft voting dari tiga model berbeda', code="from sklearn.datasets import make_classification\nfrom sklearn.ensemble import VotingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.naive_bayes import GaussianNB\nfrom sklearn.model_selection import cross_val_score\nX, y = make_classification(800, n_features=10, n_informative=5, random_state=2)\nmodel = [('lr', LogisticRegression(max_iter=1000)), ('rf', RandomForestClassifier(100, random_state=0)), ('nb', GaussianNB())]\nfor n, m in model + [('voting', VotingClassifier(model, voting='soft'))]:\n    print(f'{n:7}: {cross_val_score(m, X, y, cv=5).mean():.3f}')")]),

'Gradient boosting dari nol': dict(
  ist=[('Weak learner', 'Model lemah (pohon dangkal) yang digabung berurutan menjadi kuat.'),
       ('Shrinkage', 'Nama lain learning rate pada boosting.'),
       ('Residual fitting', 'Setiap model baru belajar dari kesalahan model sebelumnya.'),
       ('Subsample (stochastic GB)', 'Melatih tiap pohon pada sebagian data untuk mengurangi overfit.')],
  cx=[dict(t='Pengaruh learning rate pada jumlah pohon', code="import numpy as np\nfrom sklearn.ensemble import GradientBoostingRegressor\nfrom sklearn.model_selection import train_test_split\nrng = np.random.default_rng(0); X = rng.uniform(0, 10, (600, 1)); y = np.sin(X[:, 0]) * 3 + rng.normal(0, 0.4, 600)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nfor lr in [1.0, 0.3, 0.05]:\n    m = GradientBoostingRegressor(n_estimators=300, learning_rate=lr, max_depth=2, random_state=0).fit(Xtr, ytr)\n    err = [np.mean((yte - p) ** 2) for p in m.staged_predict(Xte)]\n    print(f'lr={lr}: MSE uji terbaik {min(err):.3f} di pohon ke-{int(np.argmin(err)) + 1}')")]),

'Clustering lanjutan: DBSCAN dan hierarki': dict(
  ist=[('Density-based', 'Kelompok ditentukan oleh kepadatan titik, bukan jarak ke pusat.'),
       ('Dendrogram', 'Diagram pohon hasil clustering hierarki; dipotong untuk menentukan jumlah kelompok.'),
       ('Linkage', 'Cara mengukur jarak antar kelompok: single, complete, average, ward.'),
       ('HDBSCAN', 'Pengembangan DBSCAN yang tidak perlu menyetel eps; populer di industri.')],
  cx=[dict(t='Memilih eps dengan grafik jarak k-tetangga', code="import numpy as np\nfrom sklearn.datasets import make_moons\nfrom sklearn.neighbors import NearestNeighbors\nX, _ = make_moons(300, noise=0.06, random_state=2)\nd, _ = NearestNeighbors(n_neighbors=5).fit(X).kneighbors(X)\njarak = np.sort(d[:, -1])\nfor p in [50, 90, 95, 99]:\n    print(f'persentil {p}: {np.percentile(jarak, p):.3f}')\nprint('eps yang wajar berada di sekitar \"siku\" kurva, misalnya persentil 95')")]),

'Deteksi anomali: Isolation Forest': dict(
  ist=[('Outlier vs anomaly', 'Outlier = nilai ekstrem statistik; anomaly = kejadian tidak wajar yang perlu ditindak.'),
       ('Contamination', 'Perkiraan proporsi anomali dalam data.'),
       ('Local Outlier Factor (LOF)', 'Membandingkan kepadatan titik dengan tetangganya.'),
       ('Alert fatigue', 'Terlalu banyak peringatan palsu membuat tim mengabaikan semuanya; atur ambang dengan hati-hati.')],
  cx=[dict(t='Isolation Forest vs LOF', code="import numpy as np\nfrom sklearn.ensemble import IsolationForest\nfrom sklearn.neighbors import LocalOutlierFactor\nrng = np.random.default_rng(1)\nX = np.vstack([rng.normal(0, 1, (300, 2)), [[6, 6], [-5, 5], [0, 7]]])\niso = IsolationForest(contamination=0.01, random_state=0).fit_predict(X)\nlof = LocalOutlierFactor(n_neighbors=20, contamination=0.01).fit_predict(X)\nprint('Isolation Forest menandai indeks:', np.flatnonzero(iso == -1).tolist())\nprint('LOF menandai indeks             :', np.flatnonzero(lof == -1).tolist())")]),

't-SNE: peta 2D untuk data berdimensi tinggi': dict(
  ist=[('Perplexity', 'Perkiraan jumlah tetangga efektif di t-SNE (5–50).'),
       ('UMAP', 'Alternatif t-SNE yang lebih cepat dan menjaga struktur global lebih baik.'),
       ('Manifold learning', 'Keluarga metode yang mengasumsikan data berada di permukaan berdimensi rendah.'),
       ('Trustworthiness', 'Ukuran seberapa baik tetangga di peta 2D adalah tetangga asli.')],
  cx=[dict(t='Mengukur kualitas peta dengan trustworthiness', code="from sklearn.datasets import load_digits\nfrom sklearn.decomposition import PCA\nfrom sklearn.manifold import TSNE, trustworthiness\nX = load_digits().data[:500]\nfor nama, Z in [('PCA', PCA(2).fit_transform(X)), ('t-SNE', TSNE(2, random_state=0, init='pca').fit_transform(X))]:\n    print(f'{nama:6}: trustworthiness={trustworthiness(X, Z, n_neighbors=10):.3f}')")]),

'Sistem rekomendasi: collaborative filtering': dict(
  ist=[('Cold start', 'Pengguna atau item baru belum punya interaksi; atasi dengan content-based atau item populer.'),
       ('Implicit feedback', 'Sinyal tidak langsung (klik, tonton, beli) yang jauh lebih banyak daripada rating.'),
       ('Precision@k / Recall@k', 'Metrik rekomendasi: berapa dari k rekomendasi teratas yang relevan.'),
       ('Two-tower model', 'Arsitektur rekomendasi modern: satu jaringan untuk pengguna, satu untuk item, dicocokkan dengan dot product.')],
  cx=[dict(t='Rekomendasi item-ke-item dengan cosine similarity', code="import numpy as np\nitem = ['Kopi Gayo', 'Kopi Toraja', 'V60', 'Filter Kertas', 'Teh Hijau']\n# baris = pengguna, kolom = item, 1 = pernah membeli\nB = np.array([[1, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 0, 1]])\nN = B / np.linalg.norm(B, axis=0, keepdims=True)\nS = N.T @ N\nfor i in [2, 0]:\n    j = [k for k in np.argsort(-S[i]) if k != i][:2]\n    print(f'Pembeli {item[i]:10} juga membeli: {[item[k] for k in j]}')")]),

'Peta memilih algoritma': dict(
  ist=[('No free lunch', 'Tidak ada algoritma terbaik untuk semua masalah; selalu bandingkan.'),
       ('Model selection', 'Proses memilih model dan hyperparameter berdasarkan validasi.'),
       ('Explainability vs accuracy', 'Trade-off antara model mudah dijelaskan dan model paling akurat.'),
       ('AutoML', 'Alat yang mencoba banyak model otomatis; berguna sebagai patokan, bukan pengganti pemahaman.')],
  cx=[dict(t='Benchmark cepat beberapa model sekaligus', code="from sklearn.datasets import load_breast_cancer\nfrom sklearn.dummy import DummyClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import cross_val_score\nX, y = load_breast_cancer(return_X_y=True)\nmodel = {'patokan': DummyClassifier(), 'logistic': make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),\n         'random forest': RandomForestClassifier(200, random_state=0), 'boosting': HistGradientBoostingClassifier(random_state=0)}\nfor n, m in model.items():\n    print(f'{n:14}: AUC {cross_val_score(m, X, y, cv=5, scoring=\"roc_auc\").mean():.3f}')")]),

'Jaringan saraf dari nol dengan NumPy': dict(
  ist=[('Forward / backward pass', 'Forward menghitung keluaran; backward (backpropagation) menghitung gradien untuk memperbarui bobot.'),
       ('Activation function', 'Fungsi non-linear (ReLU, sigmoid, GELU) agar jaringan bisa mempelajari pola rumit.'),
       ('Vanishing gradient', 'Gradien mengecil di jaringan dalam sehingga lapisan awal tidak belajar; ReLU dan normalisasi membantu.'),
       ('PyTorch / TensorFlow', 'Framework industri yang menghitung gradien otomatis (autograd).')],
  cx=[dict(t='Cek gradien secara numerik', b='Teknik debugging klasik: bandingkan turunan rumus dengan perkiraan numerik.',
           code="import numpy as np\nsig = lambda z: 1 / (1 + np.exp(-z))\ndef loss(w, x=1.5, y=1.0):\n    p = sig(w * x); return -(y * np.log(p) + (1 - y) * np.log(1 - p))\nw = 0.3\ngrad_rumus = (sig(w * 1.5) - 1.0) * 1.5\ngrad_numerik = (loss(w + 1e-5) - loss(w - 1e-5)) / 2e-5\nprint(f'rumus: {grad_rumus:.6f}  numerik: {grad_numerik:.6f}  selisih: {abs(grad_rumus - grad_numerik):.1e}')")]),

'CNN, RNN, dan Transformer': dict(
  ist=[('Transfer learning', 'Memakai model yang sudah dilatih (ResNet, BERT) lalu menyesuaikan dengan data sendiri; cara standar di industri.'),
       ('Fine-tuning', 'Melatih ulang sebagian atau seluruh bobot model pra-latih pada data tugas baru.'),
       ('Data augmentation', 'Memperbanyak data latih dengan variasi (putar, potong, ubah warna) agar model lebih tangguh.'),
       ('Foundation model / LLM', 'Model raksasa pra-latih (GPT, Claude, Llama) yang dipakai lewat API atau di-fine-tune.')],
  cx=[dict(t='Menghitung parameter: kenapa CNN hemat', code="h, w, c = 64, 64, 3\ndense = (h * w * c) * 128 + 128\nconv = (3 * 3 * c) * 32 + 32\nprint(f'Lapisan dense 128 neuron  : {dense:,} parameter')\nprint(f'Lapisan konvolusi 32 filter: {conv:,} parameter (bobot dipakai bersama di seluruh gambar)')")]),

'Embedding dan attention': dict(
  ist=[('Token', 'Potongan teks yang diproses model; biaya API LLM dihitung per token.'),
       ('Context window', 'Jumlah token maksimum yang bisa dibaca model sekaligus.'),
       ('Vector database', 'Database khusus vektor (pgvector, Qdrant, Pinecone) untuk pencarian semantik dan RAG.'),
       ('RAG', 'Retrieval-augmented generation: mengambil dokumen relevan lalu memberikannya ke LLM sebagai konteks.')],
  cx=[dict(t='Pencarian semantik mini dengan embedding tiruan', code="import numpy as np\nrng = np.random.default_rng(0)\ntopik = {'pembayaran': rng.normal(size=8), 'pengiriman': rng.normal(size=8), 'akun': rng.normal(size=8)}\ndokumen = {'Cara bayar dengan QRIS': topik['pembayaran'] + rng.normal(0, .3, 8),\n           'Lacak paket kurir': topik['pengiriman'] + rng.normal(0, .3, 8),\n           'Lupa kata sandi': topik['akun'] + rng.normal(0, .3, 8)}\nkueri = topik['pengiriman'] + rng.normal(0, .3, 8)          # \"paket saya belum sampai\"\nskor = {d: v @ kueri / (np.linalg.norm(v) * np.linalg.norm(kueri)) for d, v in dokumen.items()}\nfor d, s in sorted(skor.items(), key=lambda x: -x[1]):\n    print(f'{s:.2f}  {d}')")]),

'Menyimpan model dan membuat API prediksi': dict(
  ist=[('Model registry', 'Tempat menyimpan versi model beserta metrik dan metadata (MLflow Model Registry).'),
       ('Inference / serving', 'Menjalankan model untuk prediksi di produksi, baik real-time (API) maupun batch.'),
       ('Latency SLA', 'Janji waktu respons, misalnya p95 &lt; 200 ms.'),
       ('Schema validation', 'Memastikan input API sesuai bentuk yang diharapkan (Pydantic) sebelum masuk model.')],
  cx=[dict(t='Menyimpan pipeline beserta metadata versinya', code="import json, joblib, tempfile, os, sklearn, hashlib\nfrom sklearn.datasets import load_iris\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\nX, y = load_iris(return_X_y=True)\npipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(X, y)\nfolder = tempfile.mkdtemp(); path = os.path.join(folder, 'model.joblib')\njoblib.dump(pipe, path)\nmeta = {'versi': '2026.11.19-1', 'sklearn': sklearn.__version__, 'fitur': ['sepal_l', 'sepal_w', 'petal_l', 'petal_w'],\n        'akurasi_latih': round(pipe.score(X, y), 3), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest()[:12]}\nprint(json.dumps({k: v for k, v in meta.items() if k != 'sklearn'}, indent=1))\nprint('model dimuat ulang memprediksi:', joblib.load(path).predict(X[:3]))")]),

'Docker, CI/CD, dan memantau data drift': dict(
  ist=[('Data drift', 'Distribusi data input berubah dibanding saat training.'),
       ('Concept drift', 'Hubungan fitur dan target berubah (perilaku pelanggan berubah setelah pandemi).'),
       ('Shadow deployment', 'Model baru berjalan diam-diam di samping model lama untuk dibandingkan tanpa memengaruhi pengguna.'),
       ('Canary release', 'Model baru dilepas ke sebagian kecil trafik dulu.')],
  cx=[dict(t='Uji drift dengan Kolmogorov-Smirnov per fitur', code="import numpy as np\nfrom scipy import stats\nrng = np.random.default_rng(0)\nlatih = {'umur': rng.normal(32, 8, 3000), 'belanja': rng.lognormal(12, .5, 3000)}\nsekarang = {'umur': rng.normal(32, 8, 1000), 'belanja': rng.lognormal(12.3, .5, 1000)}\nfor f in latih:\n    ks = stats.ks_2samp(latih[f], sekarang[f])\n    print(f'{f:8}: KS={ks.statistic:.3f} p={ks.pvalue:.1e} ->', 'DRIFT' if ks.pvalue < 0.01 else 'aman')")]),

'Proyek: memprediksi pelanggan yang akan churn': dict(
  ist=[('Model card', 'Dokumen singkat tentang tujuan model, data, metrik, batasan, dan risiko etis.'),
       ('Uplift', 'Tambahan hasil karena intervensi; model uplift mencari siapa yang paling terpengaruh oleh promo.'),
       ('Business impact', 'Dampak model dalam rupiah atau pelanggan yang diselamatkan; inilah yang dilaporkan ke manajemen.'),
       ('Retraining schedule', 'Jadwal melatih ulang model (bulanan) atau saat drift terdeteksi.')],
  cx=[dict(t='Menghitung dampak bisnis dari model', code="pelanggan_dihubungi = 2000\npresisi = 0.42                    # 42% yang dihubungi memang akan churn\ntingkat_selamat = 0.30            # 30% dari mereka batal churn setelah dihubungi\nnilai_pelanggan = 1_200_000       # nilai 12 bulan\nbiaya_kontak = 15_000\nselamat = pelanggan_dihubungi * presisi * tingkat_selamat\nuntung = selamat * nilai_pelanggan - pelanggan_dihubungi * biaya_kontak\nprint(f'pelanggan terselamatkan: {selamat:.0f}')\nprint(f'dampak bersih: Rp{untung:,.0f} per kampanye')")]),
}
