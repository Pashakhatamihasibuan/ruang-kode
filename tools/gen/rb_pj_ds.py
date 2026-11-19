"""Proyek Data Scientist berpenyelesaian: 6 mini (dijalankan saat generate) + 4 besar."""
from rb_pj_lib import MINI, BESAR, JALUR_M, q

DATA_PELANGGAN = '''import numpy as np, pandas as pd
rng = np.random.default_rng(7)
n = 3000
df = pd.DataFrame({
    'lama_bulan': rng.integers(1, 48, n),
    'paket': rng.choice(['Basic', 'Standar', 'Premium'], n, p=[.5, .35, .15]),
    'kota': rng.choice(['Jakarta', 'Bandung', 'Surabaya', 'Medan'], n),
    'tiket_keluhan': rng.poisson(1.2, n),
    'pemakaian_jam': rng.gamma(3, 6, n).round(1),
    'telat_bayar': rng.integers(0, 4, n),
})
logit = -1.2 - 0.05 * df.lama_bulan + 0.55 * df.tiket_keluhan - 0.06 * df.pemakaian_jam + 0.6 * df.telat_bayar + (df.paket == 'Basic') * 0.5
df['churn'] = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
'''

KODE_M1 = DATA_PELANGGAN + r'''from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score

X, y = df.drop(columns='churn'), df['churn']
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)
kat, num = ['paket', 'kota'], ['lama_bulan', 'tiket_keluhan', 'pemakaian_jam', 'telat_bayar']
prep = ColumnTransformer([('kat', OneHotEncoder(handle_unknown='ignore'), kat), ('num', StandardScaler(), num)])

def presisi_at_k(y_true, skor, k=0.2):
    top = np.argsort(-skor)[: int(len(skor) * k)]
    return y_true.to_numpy()[top].mean()

print(f'Churn rate: {y.mean():.1%}  (baseline acak: presisi@20% = {y_te.mean():.2f})')
aturan = (X_te['tiket_keluhan'] + X_te['telat_bayar']).to_numpy().astype(float)
print(f'Aturan bisnis (keluhan+telat): AUC {roc_auc_score(y_te, aturan):.3f}  presisi@20% {presisi_at_k(y_te, aturan):.2f}')
for nama, model in [('Logistic Regression', LogisticRegression(max_iter=1000)),
                    ('Gradient Boosting', HistGradientBoostingClassifier(max_depth=3, random_state=0))]:
    pipe = Pipeline([('prep', prep), ('model', model)]).fit(X_tr, y_tr)
    p = pipe.predict_proba(X_te)[:, 1]
    print(f'{nama:20}: AUC {roc_auc_score(y_te, p):.3f}  presisi@20% {presisi_at_k(y_te, p):.2f}')
print('Keputusan: kirim 20% pelanggan berisiko tertinggi ke tim retensi; model menang jika presisi@20% > aturan bisnis.')
'''

KODE_M2 = r'''import numpy as np, pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor

rng = np.random.default_rng(3)
n = 800
df = pd.DataFrame({
    'luas_tanah': rng.uniform(60, 300, n).round(),
    'kamar': rng.integers(1, 6, n),
    'jarak_tol_km': rng.uniform(0.5, 20, n).round(1),
    'kecamatan': rng.choice(['Cibubur', 'Bekasi Barat', 'Serpong', 'Depok'], n),
    'tahun_bangun': rng.integers(1995, 2026, n),
})
premi = df.kecamatan.map({'Cibubur': 1.15, 'Bekasi Barat': 0.95, 'Serpong': 1.35, 'Depok': 1.0})
df['harga_juta'] = (6.5 * df.luas_tanah + 90 * df.kamar - 25 * df.jarak_tol_km + 8 * (df.tahun_bangun - 1995)) * premi + rng.normal(0, 120, n)

# rekayasa fitur: umur bangunan dan harga per m2 tidak boleh memakai target
df['umur'] = 2026 - df['tahun_bangun']
X, y = df.drop(columns=['harga_juta', 'tahun_bangun']), df['harga_juta']
prep = make_column_transformer((OneHotEncoder(), ['kecamatan']), remainder='passthrough')
cv = KFold(5, shuffle=True, random_state=0)

hasil = {'Baseline (median)': np.mean(np.abs(y - y.median()))}
for nama, m in [('Ridge', RidgeCV(alphas=np.logspace(-2, 3, 20))), ('Random Forest', RandomForestRegressor(200, min_samples_leaf=3, random_state=0))]:
    s = -cross_val_score(make_pipeline(prep, m), X, y, cv=cv, scoring='neg_mean_absolute_error')
    hasil[nama] = s.mean()
    print(f'{nama:14} MAE {s.mean():6.0f} juta  (± {s.std():.0f} antar fold)')
print(f'Baseline       MAE {hasil["Baseline (median)"]:6.0f} juta')
terbaik = min(hasil, key=hasil.get)
print(f'Model dipilih: {terbaik}; rata-rata meleset Rp{hasil[terbaik] / 1000:.2f} miliar dari harga rata-rata Rp{y.mean() / 1000:.2f} miliar ({hasil[terbaik] / y.mean():.1%}).')
'''

KODE_M3 = r'''import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

pos = ['pengiriman cepat barang sesuai', 'kualitas bagus harga murah', 'penjual ramah respon cepat', 'packing rapi aman sampai',
       'mantap sesuai deskripsi', 'barang original puas banget', 'recommended seller terpercaya', 'cepat sampai kualitas oke']
neg = ['barang rusak saat sampai', 'pengiriman lama sekali kecewa', 'tidak sesuai foto jelek', 'penjual tidak responsif',
       'packing asal asalan penyok', 'barang palsu kecewa berat', 'warna beda ukuran salah', 'lama banget tidak dibalas']
rng = np.random.default_rng(1)
def campur(daftar, k):
    return [' '.join(rng.choice(' '.join(daftar).split(), size=rng.integers(3, 7))) for _ in range(k)]
teks = campur(pos, 300) + campur(neg, 300)
label = [1] * 300 + [0] * 300

X_tr, X_te, y_tr, y_te = train_test_split(teks, label, test_size=0.25, stratify=label, random_state=0)
vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)
clf = LogisticRegression(C=2, max_iter=1000).fit(vec.fit_transform(X_tr), y_tr)
print(classification_report(y_te, clf.predict(vec.transform(X_te)), target_names=['negatif', 'positif'], digits=2))

kata = np.array(vec.get_feature_names_out()); w = clf.coef_[0]
print('Pendorong POSITIF:', ', '.join(kata[np.argsort(w)[-6:]][::-1]))
print('Pendorong NEGATIF:', ', '.join(kata[np.argsort(w)[:6]]))
baru = ['barang sampai cepat dan original', 'sudah seminggu tidak dibalas penjual']
for t, p in zip(baru, clf.predict_proba(vec.transform(baru))[:, 1]):
    print(f'{p:.2f} positif  <- "{t}"')
'''

KODE_M4 = r'''import numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

rng = np.random.default_rng(4)
tgl = pd.date_range('2025-01-01', '2026-10-31', freq='D')
t = np.arange(len(tgl))
pola_minggu = np.array([0.9, 0.85, 0.9, 1.0, 1.15, 1.35, 1.25])[tgl.dayofweek]
gajian = np.where(tgl.day >= 25, 1.2, 1.0)
y = (200 + 0.12 * t) * pola_minggu * gajian + rng.normal(0, 12, len(t))
s = pd.DataFrame({'tanggal': tgl, 'unit': y.round()})

def fitur(d):
    d = d.copy()
    d['hari'] = d.tanggal.dt.dayofweek; d['tgl'] = d.tanggal.dt.day; d['bulan'] = d.tanggal.dt.month
    for lag in (7, 14, 28): d[f'lag{lag}'] = d.unit.shift(lag)
    d['rata7_lag7'] = d.unit.shift(7).rolling(7).mean()
    return d.dropna()

d = fitur(s)
kolom = ['hari', 'tgl', 'bulan', 'lag7', 'lag14', 'lag28', 'rata7_lag7']
mape = lambda a, b: np.mean(np.abs(a - b) / a) * 100
print('Backtest 3 lipatan (tiap lipatan memprediksi 28 hari berikutnya):')
for akhir in ['2026-08-31', '2026-09-30', '2026-10-03']:
    latih = d[d.tanggal <= akhir]; uji = d[(d.tanggal > akhir)].head(28)
    m = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, random_state=0).fit(latih[kolom], latih.unit)
    naif = uji['lag7']
    print(f'  s.d. {akhir}: MAPE model {mape(uji.unit, m.predict(uji[kolom])):.1f}% | seasonal naive {mape(uji.unit, naif):.1f}%')
print('Catatan: fitur hanya memakai lag >= 7 hari, jadi model bisa meramal 7 hari ke depan tanpa membocorkan masa depan.')
'''

KODE_M5 = r'''import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import average_precision_score, roc_auc_score, precision_recall_curve

X, y = make_classification(n_samples=40000, n_features=12, n_informative=6, weights=[0.99], class_sep=1.2, flip_y=0.002, random_state=2)
nilai = np.random.default_rng(2).gamma(2, 600_000, len(y))
X_tr, X_te, y_tr, y_te, v_tr, v_te = train_test_split(X, y, nilai, test_size=0.3, stratify=y, random_state=0)
print(f'Fraud di data uji: {y_te.sum()} dari {len(y_te)} ({y_te.mean():.2%})')

m = HistGradientBoostingClassifier(class_weight='balanced', max_iter=200, random_state=0).fit(X_tr, y_tr)
p = m.predict_proba(X_te)[:, 1]
print(f'ROC-AUC {roc_auc_score(y_te, p):.3f} | PR-AUC {average_precision_score(y_te, p):.3f} (acak = {y_te.mean():.3f})')

BIAYA_CEK = 15_000
def untung(th):
    tandai = p >= th
    diselamatkan = v_te[tandai & (y_te == 1)].sum()
    return diselamatkan - BIAYA_CEK * tandai.sum(), tandai.sum(), (tandai & (y_te == 1)).sum()
print('Ambang | ditandai | fraud tertangkap | untung bersih')
for th in [0.3, 0.5, 0.7, 0.9, 0.97]:
    u, n, tp = untung(th)
    print(f' {th:.2f}  | {n:8d} | {tp:4d} dari {y_te.sum()} | Rp{u / 1e6:8.1f} juta')
terbaik = max(np.linspace(0.05, 0.99, 95), key=lambda th: untung(th)[0])
print(f'Ambang optimal berdasarkan biaya: {terbaik:.2f} (bukan 0.5 bawaan)')
'''

KODE_M6 = r'''import numpy as np, pandas as pd

rng = np.random.default_rng(6)
produk = ['kopi arabika', 'kopi robusta', 'filter V60', 'grinder manual', 'teh hijau', 'teh melati', 'gula aren', 'susu oat', 'tumbler', 'kettle leher angsa']
grup = {0: [0, 1, 2, 3, 9], 1: [4, 5, 6, 8], 2: [0, 6, 7, 8]}
baris = []
for u in range(400):
    g = grup[u % 3]
    for i in rng.choice(g, size=rng.integers(2, len(g) + 1), replace=False):
        baris.append((u, int(i)))
    if rng.random() < 0.3: baris.append((u, int(rng.integers(0, 10))))
beli = pd.DataFrame(baris, columns=['user', 'item']).drop_duplicates()

# pisahkan satu item terakhir per user sebagai data uji (leave-one-out)
uji = beli.groupby('user').tail(1); latih = beli.drop(uji.index)
M = pd.crosstab(latih.user, latih.item).reindex(columns=range(10), fill_value=0).to_numpy().astype(float)
norm = np.linalg.norm(M, axis=0, keepdims=True) + 1e-9
sim = (M / norm).T @ (M / norm); np.fill_diagonal(sim, 0)

def rekomendasi(u, k=3):
    punya = M[u]
    skor = sim @ punya; skor[punya > 0] = -1
    return list(np.argsort(-skor)[:k])

hit = np.mean([row.item in rekomendasi(row.user) for row in uji.itertuples() if row.user < M.shape[0]])
populer = list(latih.item.value_counts().index[:3])
hit_pop = np.mean([row.item in populer for row in uji.itertuples()])
print(f'HitRate@3 item-based: {hit:.2f} | baseline produk terpopuler: {hit_pop:.2f}')
print('Mirip "filter V60":', [produk[j] for j in np.argsort(-sim[2])[:3]])
print('Untuk user 1 (punya:', [produk[i] for i in np.where(M[1] > 0)[0]], ') ->', [produk[i] for i in rekomendasi(1)])
'''

DS_MINI = [
MINI(1, 'Prediksi pelanggan yang akan berhenti (churn)',
  'Layanan internet rumahan kehilangan banyak pelanggan. Tim retensi hanya sanggup menelepon 20% pelanggan per bulan, jadi mereka perlu daftar siapa yang paling mungkin berhenti.',
  ['Baseline dulu: aturan bisnis sederhana sebelum model', 'Pipeline scikit-learn: encoding kategori + scaling + model dalam satu objek', 'Bandingkan Logistic Regression dan Gradient Boosting', 'Metrik sesuai keputusan: presisi@20%, bukan akurasi'],
  ['Bangkitkan atau muat data pelanggan, cek churn rate (data tidak seimbang).', 'Buat skor aturan (keluhan + telat bayar) sebagai patokan yang harus dikalahkan.', '<code>ColumnTransformer</code> + <code>Pipeline</code> agar praproses ikut tersimpan dan tidak bocor ke data uji.', 'Hitung presisi pada 20% skor tertinggi: dari yang ditelepon, berapa yang benar-benar akan churn.'],
  KODE_M1, 'python', run=True,
  kunci='tambahkan kalibrasi probabilitas (<code>CalibratedClassifierCV</code>) dan hitung nilai uang yang diselamatkan per kampanye.',
  cek=q('Kenapa memakai presisi@20% dan bukan akurasi?', ['Karena tim hanya bisa menghubungi 20% pelanggan, jadi yang penting ketepatan di kelompok itu', 'Karena akurasi tidak bisa dihitung', 'Karena presisi selalu lebih tinggi'], 0, 'Metrik mengikuti kapasitas dan keputusan bisnis.')),

MINI(2, 'Estimasi harga rumah dengan validasi silang',
  'Agen properti di Jabodetabek ingin alat bantu menaksir harga rumah dari luas tanah, jumlah kamar, jarak ke tol, kecamatan, dan tahun bangun.',
  ['Rekayasa fitur yang masuk akal (umur bangunan) tanpa memakai target', 'K-Fold cross-validation, bukan sekali split', 'Bandingkan baseline median, Ridge, dan Random Forest', 'Laporkan galat dalam rupiah dan persen agar dipahami agen'],
  ['Buat kolom <code>umur = 2026 - tahun_bangun</code>; jangan membuat fitur dari harga.', '<code>KFold(5, shuffle=True)</code> + <code>cross_val_score</code> dengan MAE.', 'Kecamatan di-one-hot di dalam pipeline agar tiap fold dilatih dengan benar.', 'Pilih model dengan MAE terkecil dan sebutkan variasinya antar fold.'],
  KODE_M2, 'python', run=True,
  kunci='buat interval prediksi dengan quantile regression agar agen tahu rentang harga, bukan satu angka.',
  cek=q('Kenapa validasi silang lebih bisa dipercaya daripada satu kali train/test split?', ['Hasilnya dirata-rata dari beberapa pembagian sehingga tidak bergantung keberuntungan satu split', 'Lebih cepat', 'Tidak butuh data uji'], 0, 'Variansi estimasi lebih kecil.')),

MINI(3, 'Klasifikasi sentimen ulasan marketplace',
  'Toko di marketplace menerima ratusan ulasan per hari. Pemilik ingin ulasan negatif otomatis ditandai agar segera dibalas, dan ingin tahu kata apa yang paling sering memicu keluhan.',
  ['Ubah teks menjadi angka dengan TF-IDF (unigram + bigram)', 'Latih Logistic Regression dan laporkan precision/recall per kelas', 'Tampilkan kata pendorong positif dan negatif (model bisa dijelaskan)', 'Coba prediksi pada ulasan baru'],
  ['Kumpulkan teks dan label; di sini dibuat sintetis dari kosakata ulasan nyata.', '<code>TfidfVectorizer(ngram_range=(1,2), min_df=2)</code> hanya di-fit pada data latih.', '<code>classification_report</code> untuk precision, recall, F1 per kelas.', 'Koefisien model per kata = arah dan kekuatan pengaruhnya.'],
  KODE_M3, 'python', run=True,
  kunci='bandingkan dengan model embedding (misalnya IndoBERT atau embedding API) dan ukur peningkatannya dengan data ulasan asli.',
  cek=q('Kenapa vectorizer hanya boleh di-fit pada data latih?', ['Agar kosakata dan bobot IDF tidak membocorkan informasi dari data uji', 'Agar lebih cepat', 'Karena data uji tidak punya teks'], 0, 'Mencegah data leakage.')),

MINI(4, 'Peramalan penjualan harian dengan backtest',
  'Kedai kopi dengan 1 gudang ingin meramal penjualan 4 minggu ke depan untuk memesan bahan baku. Pola mingguan dan efek tanggal gajian sangat terasa.',
  ['Fitur kalender (hari, tanggal, bulan) dan lag yang tidak membocorkan masa depan', 'Backtest beberapa lipatan berbasis waktu (bukan acak)', 'Bandingkan dengan seasonal naive (nilai minggu lalu)', 'Metrik MAPE yang mudah dipahami tim gudang'],
  ['Susun data harian lengkap tanpa tanggal bolong.', 'Lag minimal 7 hari karena peramalan dilakukan seminggu sebelumnya.', 'Latih sampai tanggal potong, uji 28 hari sesudahnya; ulangi untuk beberapa tanggal potong.', 'Model hanya layak dipakai jika konsisten mengalahkan seasonal naive.'],
  KODE_M4, 'python', run=True,
  kunci='tambahkan fitur hari libur nasional dan Ramadan, lalu buat prediksi kuantil P10/P90 untuk stok pengaman.',
  cek=q('Kenapa backtest deret waktu tidak boleh memakai pembagian acak?', ['Model akan melihat data masa depan saat latihan sehingga hasilnya terlalu optimis', 'Karena data terlalu kecil', 'Karena MAPE tidak bisa dihitung'], 0, 'Urutan waktu harus dijaga.')),

MINI(5, 'Deteksi transaksi penipuan dengan ambang berbasis biaya',
  'Dompet digital memiliki 1% transaksi penipuan. Setiap transaksi yang ditandai dicek manual dengan biaya Rp15.000, sedangkan penipuan yang lolos merugikan sebesar nilai transaksinya.',
  ['Tangani data sangat tidak seimbang (class_weight)', 'Ukur dengan PR-AUC, bukan hanya ROC-AUC atau akurasi', 'Hitung untung bersih untuk beberapa ambang', 'Pilih ambang optimal berdasarkan biaya, bukan 0,5'],
  ['Pisahkan data dengan <code>stratify</code> agar proporsi fraud sama di latih dan uji.', '<code>class_weight="balanced"</code> agar model tidak mengabaikan kelas kecil.', 'Untung = nilai fraud yang tertangkap − biaya cek × jumlah yang ditandai.', 'Cari ambang dengan untung terbesar dan jelaskan ke tim risiko.'],
  KODE_M5, 'python', run=True,
  kunci='tambahkan fitur kecepatan (jumlah transaksi per jam per akun) dan pantau pergeseran pola penipuan tiap minggu.',
  cek=q('Untuk fraud 1%, kenapa akurasi menyesatkan?', ['Model yang selalu menjawab "bukan fraud" sudah 99% akurat tetapi tidak berguna', 'Akurasi selalu rendah', 'Karena fraud tidak punya label'], 0, 'Pakai PR-AUC dan metrik biaya.')),

MINI(6, 'Rekomendasi produk "sering dibeli bersama"',
  'Toko perlengkapan kopi ingin menampilkan 3 rekomendasi produk di halaman keranjang untuk menaikkan nilai belanja.',
  ['Matriks pengguna × produk dari riwayat pembelian', 'Kemiripan antar produk dengan cosine similarity (item-based)', 'Evaluasi leave-one-out: HitRate@3', 'Bandingkan dengan baseline produk terpopuler'],
  ['Ubah transaksi menjadi matriks biner dengan <code>pd.crosstab</code>.', 'Normalisasi kolom lalu kalikan matriks untuk mendapat kemiripan semua pasangan produk.', 'Sembunyikan satu pembelian terakhir tiap pengguna, lalu cek apakah muncul di 3 rekomendasi.', 'Model berguna hanya jika HitRate-nya di atas rekomendasi produk terpopuler.'],
  KODE_M6, 'python', run=True,
  kunci='tambahkan aturan bisnis (stok habis tidak direkomendasikan) dan uji dampaknya dengan A/B test pada nilai keranjang.',
  cek=q('Apa itu evaluasi leave-one-out pada sistem rekomendasi?', ['Menyembunyikan satu interaksi per pengguna lalu mengecek apakah model merekomendasikannya', 'Menghapus satu produk dari katalog', 'Melatih model tanpa satu fitur'], 0, 'Meniru prediksi pembelian berikutnya.')),
]

DS_BESAR = [
BESAR(1, 'Platform prediksi churn sampai produksi (MLOps)',
  'Operator telekomunikasi ingin skor risiko churn harian untuk 2 juta pelanggan, bisa dipanggil dari CRM, dipantau kualitasnya, dan dilatih ulang otomatis bila performa turun.',
  ['Pipeline fitur yang sama untuk latih dan prediksi (tidak ada training-serving skew)', 'Eksperimen tercatat: parameter, metrik, dan artefak model', 'API prediksi dengan validasi input dan versi model', 'Pemantauan data drift dan performa, dengan pemicu latih ulang', 'Model card: tujuan, data, metrik per segmen, batasan'],
  'Python, scikit-learn/LightGBM, MLflow, FastAPI, Docker, PostgreSQL, Evidently, GitHub Actions',
  [('Data', 'tabel fitur harian di PostgreSQL/warehouse; label churn 30 hari ke depan'), ('Pelatihan', 'train.py: split berbasis waktu, LightGBM, kalibrasi, log ke MLflow'),
   ('Registry', 'MLflow Model Registry: Staging → Production setelah lolos ambang metrik'), ('Serving', 'FastAPI /predict dan batch harian; model dimuat dari registry'),
   ('Monitoring', 'Evidently: drift fitur (PSI/KS) mingguan, presisi@k saat label tiba'), ('CI/CD', 'test unit + test data (Great Expectations/pandera) + build image')],
  ['Definisikan label dan jendela waktu: fitur dari data sampai tanggal T, churn dihitung T+1 s.d. T+30.', 'Tulis modul fitur bersama (<code>fitur.py</code>) yang dipakai saat latih dan saat prediksi.', 'Latih dengan split berbasis waktu, catat semuanya ke MLflow, daftarkan model yang lolos ambang.', 'Bungkus model dengan FastAPI + Pydantic, kemas dengan Docker, sertakan versi model di respons.', 'Jadwalkan batch harian dan laporan drift mingguan; latih ulang jika presisi@20% turun di bawah ambang.', 'Tulis model card dan dokumentasi API untuk tim CRM.'],
  r'''# train.py
import mlflow, mlflow.lightgbm, lightgbm as lgb, pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from fitur import bangun_fitur, KOLOM_FITUR

def presisi_at_k(y, p, k=0.2):
    top = p.argsort()[::-1][: int(len(p) * k)]
    return y.to_numpy()[top].mean()

df = bangun_fitur(pd.read_parquet('snapshot_fitur.parquet'))
latih, valid = df[df.tanggal < '2026-09-01'], df[df.tanggal >= '2026-09-01']

mlflow.set_experiment('churn-harian')
with mlflow.start_run():
    params = dict(n_estimators=600, learning_rate=0.03, num_leaves=31, min_child_samples=100, subsample=0.8)
    base = lgb.LGBMClassifier(**params)
    model = CalibratedClassifierCV(base, method='isotonic', cv=3).fit(latih[KOLOM_FITUR], latih.churn)
    p = model.predict_proba(valid[KOLOM_FITUR])[:, 1]
    p20 = presisi_at_k(valid.churn, p)
    mlflow.log_params(params); mlflow.log_metric('presisi_at_20', p20)
    info = mlflow.sklearn.log_model(model, 'model', input_example=valid[KOLOM_FITUR].head(3))
    if p20 >= 0.45:
        mlflow.register_model(info.model_uri, 'churn')

# serve.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
import mlflow.pyfunc

app = FastAPI(title='Churn API')
MODEL = mlflow.pyfunc.load_model('models:/churn@production')

class Pelanggan(BaseModel):
    id_pelanggan: str
    lama_bulan: int = Field(ge=0, le=600)
    tiket_keluhan_30h: int = Field(ge=0)
    pemakaian_jam_30h: float = Field(ge=0)
    telat_bayar_90h: int = Field(ge=0)
    paket: str

@app.post('/predict')
def predict(items: list[Pelanggan]):
    X = pd.DataFrame([i.model_dump() for i in items])
    p = MODEL.predict(bangun_fitur(X)[KOLOM_FITUR])
    return [{'id_pelanggan': i.id_pelanggan, 'risiko': round(float(s), 4), 'model_version': MODEL.metadata.run_id} for i, s in zip(items, p)]

# monitor.py (dijadwalkan mingguan)
from evidently import Report
from evidently.presets import DataDriftPreset
ref = pd.read_parquet('fitur_referensi.parquet'); kini = pd.read_parquet('fitur_minggu_ini.parquet')
hasil = Report([DataDriftPreset()]).run(reference_data=ref[KOLOM_FITUR], current_data=kini[KOLOM_FITUR])
hasil.save_html('drift.html')''',
  'python', standar='split berbasis waktu, eksperimen terlacak, model registry, API tervalidasi, drift dipantau, model card tertulis',
  cek=q('Apa itu training-serving skew?', ['Perbedaan cara fitur dihitung saat latih dan saat produksi sehingga performa turun', 'Model terlalu besar', 'Server lambat'], 0, 'Dicegah dengan modul fitur bersama.')),

BESAR(2, 'Peramalan permintaan ritel multi-toko',
  'Jaringan minimarket dengan 300 toko dan 2.000 SKU ingin meramal permintaan 14 hari ke depan per toko per SKU untuk otomatisasi pemesanan, termasuk lonjakan saat Ramadan dan libur panjang.',
  ['Satu model global untuk semua seri (bukan 600 ribu model kecil)', 'Fitur kalender Indonesia: libur nasional, Ramadan, gajian, cuti bersama', 'Backtest bergulir dan metrik WAPE serta bias per kategori', 'Prediksi kuantil (P50, P90) untuk stok pengaman', 'Pipeline terjadwal dan dashboard akurasi untuk tim supply chain'],
  'Python, LightGBM, pandas/Polars, DuckDB atau BigQuery, Prefect/Airflow, Streamlit',
  [('Data', 'penjualan_harian(toko, sku, tanggal, unit, harga, promo), kalender_libur, master_toko'), ('Fitur', 'lag 14/21/28, rata-rata bergulir, harga relatif, promo, libur, Ramadan, toko & kategori'),
   ('Model', 'LightGBM objektif tweedie (P50) dan quantile (P90), satu model per kategori besar'), ('Evaluasi', 'backtest 4 lipatan × 14 hari; WAPE, bias, coverage P90'),
   ('Orkestrasi', 'Prefect flow harian: ekstrak → fitur → prediksi → tulis tabel prediksi'), ('Konsumen', 'sistem pemesanan otomatis + dashboard Streamlit')],
  ['Bangun tabel harian lengkap (isi 0 untuk hari tanpa penjualan) dan tandai stok habis agar tidak dikira permintaan nol.', 'Buat fitur dengan lag ≥ horizon (14 hari) agar tidak bocor.', 'Latih model global LightGBM dengan objektif tweedie untuk data banyak nol.', 'Backtest bergulir; bandingkan dengan seasonal naive dan rata-rata 4 minggu.', 'Latih model kuantil P90 untuk stok pengaman; cek coverage mendekati 90%.', 'Jadwalkan flow harian dan sajikan akurasi per kategori untuk tim supply chain.'],
  r'''import polars as pl, lightgbm as lgb, numpy as np

H = 14  # horizon hari
d = pl.read_parquet('penjualan_harian.parquet').sort(['toko', 'sku', 'tanggal'])
kal = pl.read_parquet('kalender_id.parquet')  # libur_nasional, cuti_bersama, ramadan_hari_ke, gajian

d = (d.join(kal, on='tanggal', how='left')
      .with_columns([pl.col('unit').shift(l).over(['toko', 'sku']).alias(f'lag{l}') for l in (14, 21, 28)])
      .with_columns(pl.col('unit').shift(H).rolling_mean(28).over(['toko', 'sku']).alias('rata28'),
                    (pl.col('harga') / pl.col('harga').mean().over('sku')).alias('harga_rel'),
                    pl.col('tanggal').dt.weekday().alias('hari'))
      .filter(pl.col('stok_habis') == 0)
      .drop_nulls(['lag28', 'rata28']))

FITUR = ['lag14', 'lag21', 'lag28', 'rata28', 'harga_rel', 'promo', 'hari', 'libur_nasional', 'cuti_bersama', 'ramadan_hari_ke', 'gajian', 'toko_cat', 'kategori_cat']

def wape(y, p): return np.abs(y - p).sum() / y.sum()

hasil = []
for potong in ['2026-07-31', '2026-08-31', '2026-09-30', '2026-10-31']:
    latih = d.filter(pl.col('tanggal') <= pl.lit(potong).str.to_date()).to_pandas()
    uji = d.filter((pl.col('tanggal') > pl.lit(potong).str.to_date()) & (pl.col('tanggal') <= pl.lit(potong).str.to_date() + pl.duration(days=H))).to_pandas()
    p50 = lgb.LGBMRegressor(objective='tweedie', n_estimators=800, learning_rate=0.05, num_leaves=255).fit(latih[FITUR], latih.unit)
    p90 = lgb.LGBMRegressor(objective='quantile', alpha=0.9, n_estimators=600, learning_rate=0.05).fit(latih[FITUR], latih.unit)
    uji['p50'], uji['p90'] = p50.predict(uji[FITUR]), p90.predict(uji[FITUR])
    hasil.append(dict(potong=potong, wape=wape(uji.unit, uji.p50), wape_naif=wape(uji.unit, uji.lag14),
                      bias=(uji.p50.sum() - uji.unit.sum()) / uji.unit.sum(), coverage_p90=(uji.unit <= uji.p90).mean()))
print(pl.DataFrame(hasil))

# flow.py (Prefect)
from prefect import flow, task
@task(retries=2)
def ekstrak(): ...
@task
def prediksi(): ...
@flow(name='forecast-harian')
def harian():
    ekstrak(); prediksi()''',
  'python', standar='backtest bergulir, baseline naif dikalahkan, WAPE dan bias per kategori, coverage kuantil dicek, stok habis ditangani',
  cek=q('Kenapa hari ketika stok habis dikeluarkan dari data latih?', ['Penjualan nol saat stok habis bukan berarti permintaan nol', 'Agar data lebih kecil', 'Karena LightGBM tidak bisa membaca nol'], 0, 'Censored demand.')),

BESAR(3, 'Asisten tanya-jawab dokumen dengan evaluasi (RAG + LLM)',
  'Perusahaan asuransi ingin asisten internal yang menjawab pertanyaan agen tentang polis dan SOP dari ribuan PDF, dengan sumber yang bisa dicek, dan kualitas jawabannya terukur sebelum dirilis.',
  ['Pipeline ingest: ekstrak PDF, potong (chunking), embedding, simpan di pgvector', 'Retrieval hibrida (vektor + kata kunci) dan reranking', 'Jawaban LLM wajib menyertakan kutipan sumber; menolak jika tidak ada dasar', 'Set evaluasi 150 pertanyaan: recall@5 retrieval, faithfulness, ketepatan jawaban', 'Guardrail: masking data pribadi dan log audit'],
  'Python, PostgreSQL + pgvector, Claude API, FastAPI, pytest, Langfuse/OpenTelemetry',
  [('Ingest', 'pypdf/unstructured → chunk 800 token tumpang tindih 100 → embedding → tabel chunk(id, dok, halaman, teks, embedding)'), ('Retrieval', 'top-20 vektor + top-20 BM25 → gabung (RRF) → rerank → 5 chunk'),
   ('Generasi', 'Claude dengan prompt: jawab hanya dari konteks, sebut [dok:halaman], katakan tidak tahu bila perlu'), ('Evaluasi', 'golden set pertanyaan → recall@5, LLM-as-judge faithfulness, review manusia sampel'),
   ('Observabilitas', 'trace tiap permintaan: latensi, token, biaya, skor')],
  ['Kumpulkan dokumen dan buat golden set pertanyaan bersama ahli (jawaban + halaman sumber).', 'Ingest dan uji recall@5 retrieval dulu, sebelum menyentuh LLM.', 'Tambahkan BM25 dan reranking jika recall rendah untuk istilah teknis polis.', 'Tulis prompt dengan aturan kutipan; uji faithfulness dengan LLM-as-judge dan cek manual 30 sampel.', 'Jadikan evaluasi test otomatis di CI: rilis gagal jika recall@5 atau faithfulness turun.', 'Pasang tracing, batas biaya, dan masking PII sebelum dibuka ke agen.'],
  r'''import anthropic, psycopg, json
from embed import embed  # fungsi embedding pilihanmu

cli = anthropic.Anthropic()
db = psycopg.connect('postgresql://localhost/polis')

def cari(pertanyaan, k=5):
    v = embed(pertanyaan)
    sql = """
    WITH vek AS (SELECT id, ROW_NUMBER() OVER (ORDER BY embedding <=> %(v)s::vector) r FROM chunk LIMIT 20),
         kata AS (SELECT id, ROW_NUMBER() OVER (ORDER BY ts_rank(tsv, plainto_tsquery('indonesian', %(q)s)) DESC) r
                  FROM chunk WHERE tsv @@ plainto_tsquery('indonesian', %(q)s) LIMIT 20)
    SELECT c.id, c.dok, c.halaman, c.teks,
           COALESCE(1.0/(60+vek.r),0) + COALESCE(1.0/(60+kata.r),0) AS skor
    FROM chunk c LEFT JOIN vek USING (id) LEFT JOIN kata USING (id)
    WHERE vek.id IS NOT NULL OR kata.id IS NOT NULL ORDER BY skor DESC LIMIT %(k)s"""
    return db.execute(sql, dict(v=v, q=pertanyaan, k=k)).fetchall()

SISTEM = ('Kamu asisten internal untuk agen asuransi. Jawab HANYA berdasarkan konteks. '
          'Setiap klaim diberi kutipan [dok:halaman]. Jika konteks tidak cukup, jawab "Tidak ditemukan di dokumen."')

def jawab(pertanyaan):
    ctx = cari(pertanyaan)
    konteks = '\n\n'.join(f'[{d}:{h}] {t}' for _, d, h, t, _ in ctx)
    r = cli.messages.create(model='claude-sonnet-5-5', max_tokens=800, system=SISTEM,
                            messages=[{'role': 'user', 'content': f'Konteks:\n{konteks}\n\nPertanyaan: {pertanyaan}'}])
    return r.content[0].text, ctx

# test_eval.py: dijalankan di CI
def test_recall_dan_faithfulness():
    gold = [json.loads(l) for l in open('golden_set.jsonl')]
    recall = sum(any(c[1] == g['dok'] and c[2] == g['halaman'] for c in cari(g['tanya'])) for g in gold) / len(gold)
    assert recall >= 0.85, f'recall@5 turun: {recall:.2f}'
    skor = []
    for g in gold[:40]:
        teks, ctx = jawab(g['tanya'])
        nilai = cli.messages.create(model='claude-haiku-5-5', max_tokens=5, messages=[{'role': 'user', 'content':
            f'Konteks:\n{ctx}\n\nJawaban:\n{teks}\n\nApakah setiap klaim jawaban didukung konteks? Balas 1 atau 0.'}]).content[0].text
        skor.append(nilai.strip() == '1')
    assert sum(skor) / len(skor) >= 0.9''',
  'python', standar='golden set dibuat bersama ahli, retrieval diukur terpisah dari generasi, kutipan wajib, evaluasi otomatis di CI, PII dimasking',
  cek=q('Kenapa recall retrieval diukur sebelum kualitas jawaban LLM?', ['Jika konteks yang benar tidak terambil, LLM tidak mungkin menjawab benar dari dokumen', 'Karena LLM tidak bisa dievaluasi', 'Agar lebih murah saja'], 0, 'Perbaiki tahap paling hulu dulu.')),

BESAR(4, 'Credit scoring yang adil dan bisa dijelaskan',
  'Fintech pinjaman produktif untuk UMKM ingin model skor kredit yang lebih akurat dari scorecard lama, tetapi wajib bisa menjelaskan alasan penolakan ke nasabah dan regulator, serta tidak diskriminatif.',
  ['Definisi target: gagal bayar 90+ hari dalam 12 bulan', 'Validasi out-of-time dan metrik industri: AUC, Gini, KS', 'Penjelasan per nasabah (SHAP) dan kode alasan penolakan', 'Uji keadilan antar kelompok (wilayah, jenis kelamin) dan pemantauan PSI', 'Dokumentasi model risk: model card, batasan, rencana pemantauan'],
  'Python, LightGBM monotonik, SHAP, scikit-learn, PostgreSQL, laporan dengan Quarto',
  [('Data', 'aplikasi pinjaman, riwayat transaksi e-wallet/QRIS UMKM (dengan persetujuan), biro kredit'), ('Model', 'LightGBM dengan constraint monotonik (mis. makin tinggi omzet → risiko tidak naik)'),
   ('Validasi', 'latih 2023–2024, uji out-of-time 2025; AUC, Gini = 2·AUC − 1, KS'), ('Penjelasan', 'SHAP per nasabah → 3 kode alasan teratas'),
   ('Keadilan', 'rasio persetujuan dan TPR antar kelompok; atribut sensitif tidak dipakai sebagai fitur'), ('Pemantauan', 'PSI skor dan fitur bulanan; ambang 0,1 waspada, 0,25 tindakan')],
  ['Tetapkan target, jendela observasi, dan populasi; buang fitur yang tidak tersedia saat aplikasi diajukan.', 'Latih LightGBM dengan constraint monotonik agar perilaku model masuk akal bagi analis risiko.', 'Validasi out-of-time; bandingkan Gini dengan scorecard lama.', 'Hitung SHAP untuk setiap keputusan dan petakan fitur ke kode alasan yang dimengerti nasabah.', 'Ukur keadilan antar kelompok; dokumentasikan temuan dan mitigasi.', 'Tulis model card dan pasang pemantauan PSI bulanan.'],
  r'''import lightgbm as lgb, numpy as np, pandas as pd, shap
from sklearn.metrics import roc_auc_score, roc_curve

df = pd.read_parquet('aplikasi_kredit.parquet')
latih, oot = df[df.tgl_aplikasi < '2025-01-01'], df[df.tgl_aplikasi >= '2025-01-01']
FITUR = ['omzet_bulanan', 'umur_usaha_bln', 'transaksi_qris_90h', 'rasio_cicilan', 'telat_bayar_12b', 'jumlah_pinjaman']
MONO = [-1, -1, -1, 1, 1, 1]  # arah yang diizinkan terhadap risiko

m = lgb.LGBMClassifier(n_estimators=500, learning_rate=0.03, num_leaves=15, monotone_constraints=MONO, min_child_samples=200)
m.fit(latih[FITUR], latih.gagal_bayar)
p = m.predict_proba(oot[FITUR])[:, 1]
auc = roc_auc_score(oot.gagal_bayar, p)
fpr, tpr, _ = roc_curve(oot.gagal_bayar, p)
print(f'OOT AUC {auc:.3f} | Gini {2 * auc - 1:.3f} | KS {np.max(tpr - fpr):.3f}')

# Kode alasan per nasabah dari SHAP
ALASAN = {'telat_bayar_12b': 'R01 Riwayat keterlambatan pembayaran', 'rasio_cicilan': 'R02 Cicilan terlalu besar dibanding pendapatan',
          'omzet_bulanan': 'R03 Omzet usaha belum mencukupi', 'umur_usaha_bln': 'R04 Usia usaha masih singkat',
          'transaksi_qris_90h': 'R05 Aktivitas transaksi usaha rendah', 'jumlah_pinjaman': 'R06 Jumlah pinjaman yang diajukan tinggi'}
ex = shap.TreeExplainer(m)
sv = ex.shap_values(oot[FITUR])
def alasan(i, k=3):
    urut = np.argsort(-sv[i])[:k]
    return [ALASAN[FITUR[j]] for j in urut if sv[i][j] > 0]

# Keadilan: rasio persetujuan antar kelompok (atribut sensitif TIDAK jadi fitur)
oot = oot.assign(setuju=p < 0.08)
grup = oot.groupby('wilayah').agg(rasio_setuju=('setuju', 'mean'), n=('setuju', 'size'))
grup['rasio_vs_tertinggi'] = grup.rasio_setuju / grup.rasio_setuju.max()
print(grup.round(3))  # tandai kelompok < 0.8 (aturan empat-perlima) untuk investigasi

# PSI bulanan
def psi(ref, kini, bins=10):
    q = np.quantile(ref, np.linspace(0, 1, bins + 1)); q[0], q[-1] = -np.inf, np.inf
    a = np.histogram(ref, q)[0] / len(ref) + 1e-6; b = np.histogram(kini, q)[0] / len(kini) + 1e-6
    return np.sum((b - a) * np.log(b / a))''',
  'python', standar='validasi out-of-time, Gini dan KS dilaporkan, kode alasan per keputusan, uji keadilan, PSI dipantau, model card untuk model risk management',
  cek=q('Untuk apa constraint monotonik pada model kredit?', ['Memastikan arah pengaruh fitur masuk akal, misalnya omzet lebih tinggi tidak menaikkan risiko', 'Membuat model lebih cepat', 'Menghapus fitur sensitif'], 0, 'Penting untuk penjelasan dan regulator.')),
]

PJ_DS = JALUR_M('Data Scientist', 'Menengah',
  'Enam proyek mini yang dijalankan dan bisa diulang (churn, harga rumah, sentimen ulasan, peramalan penjualan, deteksi penipuan, rekomendasi) dan empat proyek besar berskala industri (MLOps churn, peramalan ritel multi-toko, RAG dengan evaluasi, credit scoring yang adil), lengkap dengan penyelesaiannya.',
  ['Data science projects', 'scikit-learn', 'MLOps', 'Forecasting', 'LLM + RAG'], DS_MINI, DS_BESAR)
