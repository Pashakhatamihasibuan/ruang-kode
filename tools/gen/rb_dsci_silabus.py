"""Tambahan jalur Data Science & AI agar cakupannya lengkap dari dasar sampai dampak bisnis:
Python dan pandas sehari-hari, uji hipotesis langkah demi langkah, empat tujuan grafik, pembersihan data,
EDA dan feature engineering, data tidak seimbang, metrik bisnis per industri, studi kasus end-to-end, dan karier.

Pelajaran baru DITAMBAHKAN DI AKHIR modul yang sudah ada, dan modul baru di akhir jalur,
agar progres pelajar yang tersimpan (id = jalur-modul-pelajaran) tidak bergeser.
Semua contoh Python dijalankan saat generate sehingga keluarannya selalu cocok dengan kodenya."""
from rb_lib import P, PF, T, SP, M, q
from rb_pj_lib import MINI

# ---------------------------------------------------------------------------
# Data bersama
# ---------------------------------------------------------------------------
DATA_PELANGGAN = """import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
n = 300
df = pd.DataFrame({
    'umur': rng.integers(18, 60, n),
    'lama_bulan': rng.integers(1, 48, n),
    'belanja_bln': rng.normal(350, 120, n).round(0).clip(50),
    'keluhan': rng.poisson(1.2, n),
    'kota': rng.choice(['Jakarta', 'Bandung', 'Surabaya', 'Medan'], n),
})
skor = -1.2 + 0.9 * df['keluhan'] - 0.06 * df['lama_bulan'] - 0.003 * (df['belanja_bln'] - 350)
df['churn'] = (rng.random(n) < 1 / (1 + np.exp(-skor))).astype(int)
"""

TOKO = """import pandas as pd

pelanggan = pd.DataFrame({
    'id_pelanggan': [101, 102, 103, 104, 105, 106, 107],
    'nama': ['Ayu', 'Bima', 'Citra', 'Dodi', 'Eka', 'Fajar', 'Gita'],
    'kota': ['Medan', 'Bandung', 'Medan', 'Jakarta', 'Bandung', 'Jakarta', 'Medan'],
})
pesanan = pd.DataFrame({
    'id_pesanan': [1, 2, 3, 4, 5, 6, 7, 8],
    'id_pelanggan': [101, 103, 101, 104, 105, 101, 104, 103],
    'nilai': [120_000, 85_000, 64_000, 310_000, 45_000, 99_000, 150_000, 72_000],
    'status': ['selesai', 'selesai', 'batal', 'selesai', 'selesai', 'selesai', 'retur', 'selesai'],
})
"""

# ---------------------------------------------------------------------------
# Modul 1: Peran data scientist dan alat utamanya (ditambah di akhir)
# ---------------------------------------------------------------------------
L_PYTHON = P('Python inti untuk data: list, dict, kondisi, loop, dan fungsi',
  ['Sebelum pandas, kuasai lima bahan dasar Python yang dipakai setiap hari: <b>list</b> (daftar berurutan), <b>dict</b> (pasangan kunci-nilai, cocok untuk satu baris data), <b>if/elif/else</b>, <b>for/while</b> beserta <code>break</code> dan <code>continue</code>, serta <b>fungsi</b> dengan nilai bawaan (default). Satu transaksi biasanya disimpan sebagai dict, dan banyak transaksi sebagai list berisi dict.',
   'Data scientist biasanya menulis kode di <b>Jupyter Lab</b> atau notebook di VS Code: kode dijalankan per sel, hasil dan grafik langsung tampil di bawahnya, dan sel Markdown dipakai untuk catatan. Kebiasaan yang dicari tim: jalankan ulang dari atas (<i>Restart &amp; Run All</i>) sebelum dibagikan, beri judul tiap bagian, dan pindahkan fungsi yang sudah stabil ke berkas <code>.py</code> agar bisa diuji.',
   'Contoh di bawah mengolah transaksi mentah tanpa pustaka apa pun: lewati transaksi batal dengan <code>continue</code>, berhenti saat bertemu penanda akhir data dengan <code>break</code>, lalu menghitung total per kota dengan dict. Pola ini persis yang nanti dikerjakan pandas dalam satu baris, jadi memahaminya membuat pandas terasa masuk akal.'],
  "transaksi = [\n    {'kota': 'Medan', 'nilai': 120_000, 'status': 'selesai'},\n    {'kota': 'Bandung', 'nilai': 85_000, 'status': 'batal'},\n    {'kota': 'Medan', 'nilai': 64_000, 'status': 'selesai'},\n    {'kota': 'Jakarta', 'nilai': 310_000, 'status': 'selesai'},\n    {'kota': None, 'nilai': 0, 'status': 'AKHIR'},       # penanda akhir berkas\n    {'kota': 'Bandung', 'nilai': 999_000, 'status': 'selesai'},\n]\n\ndef kategori(nilai, batas_besar=200_000):\n    \"\"\"Kelompokkan nilai transaksi; batas bisa diubah lewat argumen.\"\"\"\n    if nilai >= batas_besar:\n        return 'besar'\n    elif nilai >= 80_000:\n        return 'sedang'\n    return 'kecil'\n\ntotal_kota = {}\nfor t in transaksi:\n    if t['status'] == 'AKHIR':\n        break                      # data setelah penanda diabaikan\n    if t['status'] != 'selesai':\n        continue                   # lewati yang batal\n    total_kota[t['kota']] = total_kota.get(t['kota'], 0) + t['nilai']\n    print(f\"{t['kota']:8} {t['nilai']:>8,}  {kategori(t['nilai'])}\")\n\nprint(total_kota)\nprint('dengan batas 100 ribu:', [kategori(t['nilai'], batas_besar=100_000) for t in transaksi[:4]])",
  pts=['Satu baris data = dict, banyak baris = list berisi dict.', 'continue melewati satu putaran, break menghentikan loop.', 'Fungsi dengan nilai default membuat aturan bisnis mudah diubah.', 'Notebook: jalankan ulang dari atas sebelum dibagikan.'],
  qs=[q('Transaksi berstatus batal harus dilewati tetapi loop tetap berlanjut. Kata kunci yang tepat?', ['continue', 'break', 'return'], 0, 'continue melompat ke putaran berikutnya.'),
      q('<code>kategori(150_000, batas_besar=100_000)</code> menghasilkan?', ["'besar'", "'sedang'", "'kecil'"], 0, '150 ribu ≥ batas 100 ribu.')],
  so=[SP('Buat fungsi <code>faktorial(n)</code> memakai loop <code>for</code>, lalu cetak hasil untuk n = 0, 1, 5, dan 10. Ingat 0! = 1.', 'Mulai dari hasil = 1 lalu kalikan 2 sampai n.',
         "def faktorial(n):\n    hasil = 1\n    for i in range(2, n + 1):\n        hasil *= i\n    return hasil\n\nfor n in [0, 1, 5, 10]:\n    print(n, faktorial(n))"),
      SP('Dari list <code>[12, 7, 0, 30, -1, 9]</code>, jumlahkan angka sampai bertemu -1 (penanda akhir) dan lewati angka 0.', 'Pakai break untuk -1 dan continue untuk 0.',
         "total = 0\nfor x in [12, 7, 0, 30, -1, 9]:\n    if x == -1:\n        break\n    if x == 0:\n        continue\n    total += x\nprint(total)")],
  nodes=['Learn Python Programming Language'])

L_PANDAS_HARIAN = P('pandas sehari-hari: membuat, menyimpan, mengurutkan, dan mengubah tipe',
  ['DataFrame bisa dibuat dari dict berisi list (satu list per kolom) atau dari list berisi dict (satu dict per baris). Menyimpan dan membaca kembali memakai <code>to_csv</code>/<code>read_csv</code> atau <code>to_excel</code>/<code>read_excel</code>; selalu tulis <code>index=False</code> agar nomor baris tidak ikut menjadi kolom.',
   'Pemeriksaan cepat yang dilakukan setiap kali menerima data: <code>len(df)</code> untuk jumlah baris, <code>df.columns</code> untuk nama kolom, <code>head()</code>, <code>tail()</code>, dan <code>sample(n, random_state=...)</code> untuk melihat baris acak (baris awal sering tidak mewakili). <code>describe()</code> merangkum kolom angka, <code>describe(include="object")</code> merangkum kolom teks.',
   'Tiga operasi yang paling sering: <code>sort_values</code> (bisa beberapa kolom sekaligus), <code>rename(columns={...})</code> untuk nama kolom yang rapi, dan <code>astype</code> atau <code>pd.to_datetime</code> untuk tipe yang benar. Tanggal yang masih berupa teks tidak bisa dihitung selisihnya, dan kategori bertipe <code>category</code> menghemat memori.'],
  "import io\nimport pandas as pd\n\ndf = pd.DataFrame({\n    'Tgl Order': ['2026-03-02', '2026-03-01', '2026-03-05', '2026-03-03', '2026-03-04'],\n    'Kota': ['Medan', 'Bandung', 'Medan', 'Jakarta', 'Bandung'],\n    'Qty': ['3', '1', '5', '2', '4'],          # angka tapi tersimpan sebagai teks\n    'Harga': [65000, 40000, 65000, 52000, 40000],\n})\nprint('baris:', len(df), '| kolom:', list(df.columns))\n\n# rapikan nama kolom dan tipe\ndf = df.rename(columns={'Tgl Order': 'tanggal', 'Kota': 'kota', 'Qty': 'qty', 'Harga': 'harga'})\ndf['qty'] = df['qty'].astype(int)\ndf['tanggal'] = pd.to_datetime(df['tanggal'])\ndf['kota'] = df['kota'].astype('category')\ndf['nilai'] = df['qty'] * df['harga']\n\nprint(df.sort_values(['kota', 'nilai'], ascending=[True, False]).to_string(index=False))\nprint(df.sample(2, random_state=1)[['kota', 'nilai']])\nprint(df['nilai'].describe().round(0))\n\n# simpan lalu baca kembali (di sini ke memori; di laptop cukup nama berkas)\nberkas = io.StringIO()\ndf.to_csv(berkas, index=False)\nberkas.seek(0)\nbaca = pd.read_csv(berkas, parse_dates=['tanggal'])\nprint('setelah dibaca ulang:', baca.shape, '| tanggal terbaru:', baca['tanggal'].max().date())",
  pts=['Cek len, columns, head, tail, dan sample setiap menerima data.', 'rename untuk nama kolom, astype dan to_datetime untuk tipe.', 'sort_values bisa beberapa kolom dengan arah berbeda.', 'to_csv(index=False) agar indeks tidak ikut tersimpan.'],
  qs=[q('Kolom qty berisi "3", "1", "5" (teks). Jumlahnya akan salah karena?', ['Teks dijumlahkan dengan cara disambung, jadi ubah dulu dengan astype(int)', 'pandas tidak bisa menjumlah', 'Harus memakai loop'], 0, 'Tipe data menentukan perilaku operasi.'),
      q('Kenapa <code>sample()</code> lebih baik daripada hanya <code>head()</code> untuk mengenali data?', ['Baris awal sering tidak mewakili, misalnya terurut menurut tanggal', 'sample lebih cepat', 'head tidak bisa dipakai pada CSV'], 0, 'Baris acak memberi gambaran yang lebih jujur.')],
  so=[SP('Buat DataFrame berisi kolom <code>Nama Produk</code> dan <code>Stok</code> (3 baris bebas), ganti nama kolomnya menjadi <code>produk</code> dan <code>stok</code>, lalu urutkan dari stok terbesar.', 'rename(columns=...) lalu sort_values(..., ascending=False).',
         "import pandas as pd\ndf = pd.DataFrame({'Nama Produk': ['Kopi', 'Teh', 'Gula'], 'Stok': [12, 30, 7]})\ndf = df.rename(columns={'Nama Produk': 'produk', 'Stok': 'stok'})\nprint(df.sort_values('stok', ascending=False).to_string(index=False))")],
  nodes=['Data Understanding'])

L_PANDAS_GABUNG = P('Menyaring dan menggabungkan: isin, anti-join, apply, dan map',
  ['<code>loc</code> memilih dengan label dan kondisi, <code>iloc</code> dengan posisi angka. Beberapa kondisi digabung dengan <code>&amp;</code> (dan) serta <code>|</code> (atau), masing-masing di dalam tanda kurung. Untuk "nilainya salah satu dari daftar ini", pakai <code>isin([...])</code> daripada menulis banyak <code>|</code>.',
   '<code>merge</code> menggabungkan tabel seperti JOIN di SQL: <code>inner</code> (hanya yang cocok di kedua tabel), <code>left</code> (semua baris kiri), <code>right</code>, dan <code>outer</code>. Pertanyaan "pelanggan mana yang belum pernah memesan?" dijawab dengan <b>anti-join</b>: left join dengan <code>indicator=True</code>, lalu ambil baris yang hanya ada di kiri. <code>concat</code> menumpuk tabel dengan kolom yang sama, misalnya data Januari dan Februari.',
   '<code>apply</code> menjalankan fungsi per baris atau per kolom; <code>Series.map</code> menerjemahkan nilai dengan dict atau fungsi, dan <code>DataFrame.map</code> (pengganti <code>applymap</code> yang sudah usang sejak pandas 2.1) menjalankan fungsi ke setiap sel. Gunakan seperlunya: operasi vektor seperti <code>df["a"] * df["b"]</code> jauh lebih cepat daripada <code>apply</code> baris demi baris.'],
  TOKO + "\n# 1) isin: pesanan yang bermasalah\nprint(pesanan[pesanan['status'].isin(['batal', 'retur'])])\n\n# 2) anti-join: pelanggan yang belum pernah memesan\ngabung = pelanggan.merge(pesanan, on='id_pelanggan', how='left', indicator=True)\nbelum = gabung.loc[gabung['_merge'] == 'left_only', ['id_pelanggan', 'nama', 'kota']]\nprint('Belum pernah memesan:\\n', belum.to_string(index=False))\n\n# 3) total belanja per kota (hanya pesanan selesai)\nselesai = pesanan[pesanan['status'] == 'selesai']\nper_kota = (selesai.merge(pelanggan, on='id_pelanggan', how='inner')\n                   .groupby('kota', as_index=False)['nilai'].sum()\n                   .sort_values('nilai', ascending=False))\nprint(per_kota.to_string(index=False))\n\n# 4) map dan apply\npesanan['status_id'] = pesanan['status'].map({'selesai': 1, 'batal': 0, 'retur': 0})\npesanan['ukuran'] = pesanan['nilai'].apply(lambda x: 'besar' if x >= 100_000 else 'kecil')\nprint(pesanan[['nilai', 'status_id', 'ukuran']].head(4))\nprint(pesanan[['nilai']].head(3).map(lambda x: f'Rp{x:,}'))",
  pts=['isin untuk banyak nilai sekaligus.', 'Anti-join: left join + indicator=True, ambil left_only.', 'merge = JOIN, concat = menumpuk.', 'map untuk menerjemahkan nilai; apply secukupnya.'],
  qs=[q('Cara pandas mencari pelanggan yang tidak punya pesanan sama sekali?', ["Left join dengan indicator=True lalu ambil '_merge' == 'left_only'", 'Inner join lalu hitung baris', 'concat dua tabel'], 0, 'Anti-join.'),
      q('Kenapa hasil per kota memakai inner join setelah menyaring pesanan selesai?', ['Hanya pesanan yang punya pelanggan dan berstatus selesai yang dihitung', 'Inner join selalu lebih cepat', 'Agar pelanggan tanpa pesanan muncul dengan nilai 0'], 0, 'Inner join hanya menyimpan pasangan yang cocok.')],
  so=[SP('Dengan tabel <code>pelanggan</code> dan <code>pesanan</code> di atas, hitung jumlah pesanan (semua status) per nama pelanggan, termasuk yang 0 pesanan.', 'Left join, lalu groupby nama dan hitung id_pesanan dengan count (NaN tidak dihitung).',
         TOKO + "g = pelanggan.merge(pesanan, on='id_pelanggan', how='left')\nprint(g.groupby('nama')['id_pesanan'].count().sort_values(ascending=False))")],
  nodes=['Data Understanding', 'Data Analysis'])

# ---------------------------------------------------------------------------
# Modul 3: Statistik dan probabilitas (ditambah di akhir)
# ---------------------------------------------------------------------------
L_UJI_LANGKAH = P('Uji hipotesis langkah demi langkah: statistik uji dan nilai kritis',
  ['Setiap uji hipotesis mengikuti lima langkah yang sama. <b>(1)</b> Tulis <b>H0</b> (status quo, "tidak ada perubahan") dan <b>H1</b> (klaim yang ingin dibuktikan). <b>(2)</b> Pilih <b>tingkat kepercayaan</b>, misalnya 95%, yang berarti <b>α = 0,05</b>: risiko menolak H0 padahal H0 benar. <b>(3)</b> Hitung <b>statistik uji</b>, misalnya <code>t = (rata-rata sampel − nilai H0) / (s / √n)</code>. <b>(4)</b> Bandingkan dengan <b>nilai kritis</b> atau p-value. <b>(5)</b> Simpulkan dalam bahasa bisnis.',
   '<b>Satu sisi atau dua sisi?</b> Jika H1 hanya peduli satu arah ("waktu antar lebih <i>lama</i> dari janji 30 menit"), pakai uji satu sisi: seluruh α diletakkan di satu ekor, nilai kritisnya <code>t(1−α, df)</code>. Jika H1 "berbeda" ke arah mana pun, pakai dua sisi: α dibagi ke dua ekor, nilai kritisnya <code>±t(1−α/2, df)</code>. Tentukan sebelum melihat data, bukan setelahnya.',
   '<b>Daerah kritis</b> (daerah penolakan) adalah nilai statistik uji yang terlalu ekstrem jika H0 benar. Dulu nilai kritis dibaca dari <b>tabel t</b> berdasarkan derajat bebas (df = n − 1); sekarang cukup <code>scipy.stats.t.ppf</code>, yang hasilnya sama dengan tabel. Dua cara menyimpulkan selalu sepakat: |t| melewati nilai kritis ⇔ p-value &lt; α.'],
  "import numpy as np\nfrom scipy import stats\n\n# Klaim: rata-rata waktu antar 30 menit. Tim operasional curiga lebih lama.\nwaktu = np.array([31.5, 29.0, 34.2, 33.1, 30.8, 35.6, 28.9, 32.4, 33.8, 31.1,\n                  36.0, 30.2, 32.9, 29.7, 34.5, 31.8])\nmu0, alpha = 30, 0.05\nn, rata, s = len(waktu), waktu.mean(), waktu.std(ddof=1)\nt_hitung = (rata - mu0) / (s / np.sqrt(n))\ndf = n - 1\nprint(f'n={n}, rata-rata={rata:.2f}, s={s:.2f}, t={t_hitung:.3f}, df={df}')\n\n# 'tabel t' versi kode\nprint('df  | satu sisi 0,05 | dua sisi 0,05')\nfor d in [5, 10, 15, 30]:\n    print(f'{d:3} | {stats.t.ppf(0.95, d):14.3f} | {stats.t.ppf(0.975, d):13.3f}')\n\nkritis_1 = stats.t.ppf(1 - alpha, df)\nkritis_2 = stats.t.ppf(1 - alpha / 2, df)\np_1 = 1 - stats.t.cdf(t_hitung, df)\np_2 = 2 * (1 - stats.t.cdf(abs(t_hitung), df))\nprint(f'satu sisi: kritis {kritis_1:.3f}, p={p_1:.5f} -> {\"tolak H0\" if t_hitung > kritis_1 else \"gagal tolak H0\"}')\nprint(f'dua sisi : kritis ±{kritis_2:.3f}, p={p_2:.5f} -> {\"tolak H0\" if abs(t_hitung) > kritis_2 else \"gagal tolak H0\"}')\n\ncek = stats.ttest_1samp(waktu, mu0, alternative='greater')\nprint(f'scipy: t={cek.statistic:.3f}, p={cek.pvalue:.5f}')\nprint('Kesimpulan: rata-rata waktu antar lebih lama dari 30 menit; janji di aplikasi perlu dikoreksi.')",
  tb=[{'c': 'Lima langkah uji hipotesis', 'h': ['Langkah', 'Isi', 'Contoh waktu antar'],
       'r': [['1. Hipotesis', 'H0 status quo, H1 klaim', 'H0: μ = 30; H1: μ > 30'],
             ['2. α', '1 − tingkat kepercayaan', 'α = 0,05 (95%)'],
             ['3. Statistik uji', 't = (x̄ − μ0) / (s/√n)', 't hitung dari 16 pengiriman'],
             ['4. Keputusan', 't melewati nilai kritis atau p < α', 'bandingkan dengan t(0,95; 15)'],
             ['5. Kesimpulan', 'Bahasa bisnis + besar efek', 'Janji waktu antar perlu dikoreksi']]}],
  pts=['H0 status quo, H1 klaim; α = 1 − tingkat kepercayaan.', 'Satu sisi: α di satu ekor. Dua sisi: α/2 di tiap ekor.', 'Nilai kritis dari tabel t = stats.t.ppf.', '|t| > nilai kritis ⇔ p-value < α.'],
  qs=[q('H1: "rata-rata berbeda dari 30" (lebih besar atau lebih kecil). Uji yang tepat?', ['Dua sisi', 'Satu sisi kanan', 'Satu sisi kiri'], 0, 'Kedua arah dianggap penting.'),
      q('Pada α = 0,05 dan df = 15, nilai kritis satu sisi lebih kecil dari dua sisi. Akibatnya?', ['Uji satu sisi lebih mudah menolak H0 ke arah yang dipilih', 'Uji satu sisi selalu lebih benar', 'Tidak ada pengaruh'], 0, 'Seluruh α berada di satu ekor.'),
      q('Tingkat kepercayaan 99% berarti α sebesar?', ['0,01', '0,99', '0,05'], 0, 'α = 1 − 0,99.')],
  so=[SP('Hitung nilai kritis t dua sisi untuk α = 0,01 dan df = 20, lalu nilai kritis satu sisi untuk α = 0,01 dan df yang sama.', 'stats.t.ppf(1 - α/2, df) dan stats.t.ppf(1 - α, df).',
         "from scipy import stats\nprint(round(stats.t.ppf(1 - 0.01 / 2, 20), 3), round(stats.t.ppf(1 - 0.01, 20), 3))")],
  nodes=['Hypothesis Testing'])

L_KASUS_TTEST = PF('Studi kasus t-test: apakah program voucher menaikkan belanja?',
  ['Sebuah aplikasi kedai kopi menguji voucher "beli 2 gratis 1" selama dua minggu. Pelanggan dibagi acak: <b>kontrol</b> (tanpa voucher) dan <b>perlakuan</b> (mendapat voucher). Pertanyaan bisnis: apakah belanja per pelanggan naik cukup besar untuk menutup biaya voucher?',
   'Karena dua kelompok berisi orang yang berbeda, kita memakai <b>t-test dua sampel independen</b>. Varians dua kelompok tidak dijamin sama, jadi pakai versi <b>Welch</b> (<code>equal_var=False</code>), yang menjadi pilihan aman di industri. H1 satu arah: perlakuan &gt; kontrol, sehingga <code>alternative="greater"</code>. Jika pelanggan yang sama diukur sebelum dan sesudah, pakai <b>t-test berpasangan</b> (<code>ttest_rel</code>).',
   'Signifikan secara statistik belum tentu menguntungkan. Hitung <b>selang kepercayaan</b> selisih rata-rata dan bandingkan dengan <b>biaya voucher per pelanggan</b>. Keputusan diambil dari angka rupiah, bukan dari p-value saja.'],
  "import numpy as np\nimport matplotlib.pyplot as plt\nfrom scipy import stats\n\nrng = np.random.default_rng(21)\nkontrol = rng.gamma(4, 18_000, 420).round(-2)       # belanja 2 minggu (rupiah)\nvoucher = rng.gamma(4, 21_000, 410).round(-2)\nbiaya_voucher = 4_500                               # rata-rata biaya per pelanggan perlakuan\n\nhasil = stats.ttest_ind(voucher, kontrol, equal_var=False, alternative='greater')\nselisih = voucher.mean() - kontrol.mean()\nse = np.sqrt(voucher.var(ddof=1) / len(voucher) + kontrol.var(ddof=1) / len(kontrol))\nci = stats.t.interval(0.95, df=min(len(voucher), len(kontrol)) - 1, loc=selisih, scale=se)\n\nprint(f'kontrol : Rp{kontrol.mean():,.0f} (n={len(kontrol)})')\nprint(f'voucher : Rp{voucher.mean():,.0f} (n={len(voucher)})')\nprint(f'selisih : Rp{selisih:,.0f}, 95% CI Rp{ci[0]:,.0f} s.d. Rp{ci[1]:,.0f}')\nprint(f'Welch t = {hasil.statistic:.2f}, p (satu sisi) = {hasil.pvalue:.4f}')\nmargin = 0.35                                        # margin kotor kedai\nuntung = selisih * margin - biaya_voucher\nprint(f'tambahan laba kotor per pelanggan: Rp{selisih * margin:,.0f} - biaya Rp{biaya_voucher:,} = Rp{untung:,.0f}')\nprint('Keputusan:', 'lanjutkan voucher' if hasil.pvalue < 0.05 and untung > 0 else 'jangan diperluas dulu')\n\nplt.figure(figsize=(6.4, 3.2))\nbins = np.linspace(0, 250_000, 40)\nplt.hist(kontrol, bins=bins, alpha=0.6, label='kontrol')\nplt.hist(voucher, bins=bins, alpha=0.6, label='voucher')\nplt.axvline(kontrol.mean(), color='tab:blue', linestyle='--')\nplt.axvline(voucher.mean(), color='tab:orange', linestyle='--')\nplt.xlabel('belanja 2 minggu (Rp)'); plt.title('Sebaran belanja: kontrol vs voucher'); plt.legend()",
  pts=['Dua kelompok berbeda: t-test independen (Welch).', 'Orang yang sama sebelum-sesudah: t-test berpasangan.', 'Laporkan selang kepercayaan selisih, bukan hanya p-value.', 'Keputusan akhir memakai laba setelah biaya.'],
  qs=[q('Data belanja pelanggan yang sama sebelum dan sesudah mendapat voucher. Uji yang tepat?', ['t-test berpasangan (ttest_rel)', 't-test independen', 'Chi-square'], 0, 'Pengamatan berpasangan per orang.'),
      q('Hasil signifikan (p < 0,05) tetapi tambahan laba lebih kecil dari biaya voucher. Keputusan?', ['Jangan diperluas, efeknya nyata tetapi tidak menguntungkan', 'Langsung diperluas karena signifikan', 'Ulangi sampai p lebih kecil'], 0, 'Signifikansi statistik ≠ manfaat bisnis.')],
  nodes=['Hypothesis Testing', 'AB Testing'])

# ---------------------------------------------------------------------------
# Modul 5: EDA dan visualisasi (ditambah di akhir)
# ---------------------------------------------------------------------------
L_EMPAT_GRAFIK = PF('Empat tujuan grafik: perbandingan, distribusi, hubungan, dan komposisi',
  ['Pilih grafik dari <b>pertanyaannya</b>, bukan dari selera. Hampir semua pertanyaan masuk ke salah satu dari empat tujuan: <b>perbandingan</b> (kategori mana yang lebih besar, bagaimana berubah dari waktu ke waktu), <b>distribusi</b> (bagaimana sebaran nilai), <b>hubungan</b> (apakah dua variabel bergerak bersama), dan <b>komposisi</b> (bagian dari keseluruhan).',
   'Pasangan yang aman: perbandingan → batang (kategori) atau garis (waktu); distribusi → histogram atau box plot; hubungan → scatter (dan heatmap korelasi untuk banyak variabel); komposisi → batang bertumpuk 100%. <b>Pie chart</b> hanya layak untuk 2–3 bagian; lebih dari itu mata manusia sulit membandingkan sudut.',
   'Aturan yang dipakai tim data profesional: judul berupa <b>kesimpulan</b> ("Churn tertinggi di Medan"), bukan nama variabel; urutkan batang; mulai sumbu batang dari nol; dan beri warna menonjol hanya pada hal yang ingin disorot.'],
  DATA_PELANGGAN + "import matplotlib.pyplot as plt\n\ndf['segmen'] = pd.cut(df['lama_bulan'], [0, 6, 24, 48], labels=['baru', 'menengah', 'setia'])\nfig, ax = plt.subplots(2, 2, figsize=(9, 6))\n\n# perbandingan\nrata = df.groupby('kota')['belanja_bln'].mean().sort_values()\nax[0, 0].barh(rata.index, rata.values, color='tab:gray')\nax[0, 0].set_title('Perbandingan: belanja rata-rata per kota')\n\n# distribusi\ndata_box = [df.loc[df.churn == c, 'lama_bulan'] for c in (0, 1)]\nax[0, 1].boxplot(data_box)\nax[0, 1].set_xticks([1, 2], ['bertahan', 'churn'])\nax[0, 1].set_title('Distribusi: lama berlangganan')\n\n# hubungan\nax[1, 0].scatter(df['lama_bulan'], df['belanja_bln'], c=df['churn'], cmap='coolwarm', s=10)\nax[1, 0].set_xlabel('lama (bulan)'); ax[1, 0].set_ylabel('belanja')\nax[1, 0].set_title('Hubungan: lama vs belanja (merah = churn)')\n\n# komposisi\nkomp = pd.crosstab(df['segmen'], df['churn'], normalize='index') * 100\nax[1, 1].bar(komp.index.astype(str), komp[0], label='bertahan', color='tab:blue')\nax[1, 1].bar(komp.index.astype(str), komp[1], bottom=komp[0], label='churn', color='tab:red')\nax[1, 1].set_title('Komposisi: % churn per segmen'); ax[1, 1].legend(loc='lower right')\nfig.tight_layout()\nprint(komp.round(1))",
  tb=[{'c': 'Memilih grafik dari tujuan', 'h': ['Tujuan', 'Pertanyaan', 'Grafik yang aman'],
       'r': [['Perbandingan', 'Mana yang lebih besar? Bagaimana tren?', 'Batang terurut, garis untuk waktu'],
             ['Distribusi', 'Bagaimana sebarannya? Ada outlier?', 'Histogram, box plot'],
             ['Hubungan', 'Apakah X dan Y bergerak bersama?', 'Scatter, heatmap korelasi'],
             ['Komposisi', 'Berapa porsi tiap bagian?', 'Batang bertumpuk 100%, pie (2-3 bagian)']]}],
  pts=['Empat tujuan: perbandingan, distribusi, hubungan, komposisi.', 'Judul grafik = kesimpulan.', 'Pie hanya untuk 2-3 bagian.', 'Sorot satu hal dengan warna.'],
  qs=[q('Ingin menunjukkan porsi metode bayar (6 jenis) per kota. Grafik paling jelas?', ['Batang bertumpuk 100%', 'Pie per kota', 'Scatter'], 0, 'Komposisi dengan banyak bagian.'),
      q('Melihat apakah ada outlier pada lama berlangganan. Grafik yang cocok?', ['Box plot', 'Pie chart', 'Garis'], 0, 'Box plot menandai titik di luar 1,5 × IQR.')],
  nodes=['Data Visualization'])

L_BERSIH = P('Membersihkan data: duplikat, nilai mustahil, dan outlier',
  ['Data dari sistem nyata hampir selalu punya tiga masalah selain nilai hilang. <b>Duplikat</b>: baris yang sama tercatat dua kali (sering karena tombol ditekan dua kali atau proses impor diulang). Bedakan duplikat <b>persis</b> (<code>duplicated()</code>) dan duplikat <b>kunci</b> (<code>duplicated(subset=["id"])</code>), lalu putuskan baris mana yang dipertahankan, misalnya yang terbaru.',
   '<b>Nilai mustahil</b>: umur 230 tahun, harga negatif, tanggal di masa depan. Ini bukan outlier melainkan kesalahan, jadi tandai sebagai kosong (NaN) lalu tangani seperti nilai hilang. Tuliskan aturannya sebagai kode agar bisa diulang setiap ada data baru.',
   '<b>Outlier</b> adalah nilai ekstrem yang mungkin benar (pelanggan korporat yang belanja 50 kali lipat). Deteksi dengan aturan <b>IQR</b> (di luar Q1 − 1,5·IQR dan Q3 + 1,5·IQR) atau z-score. Pilihan penanganan: biarkan (jika memang penting), <b>capping/winsorizing</b> ke batas, transformasi log, atau pisahkan sebagai segmen sendiri. Jangan menghapus outlier hanya karena "mengganggu grafik".'],
  "import numpy as np\nimport pandas as pd\n\ndf = pd.DataFrame({\n    'id': [1, 2, 2, 3, 4, 5, 6, 7, 8, 8],\n    'umur': [25, 31, 31, 230, 42, 19, -3, 37, 28, 28],\n    'belanja': [320, 410, 410, 280, 9_800, 150, 300, 365, 390, 395],\n    'diperbarui': pd.to_datetime(['2026-05-01', '2026-05-02', '2026-05-02', '2026-05-02', '2026-05-03',\n                                  '2026-05-03', '2026-05-04', '2026-05-04', '2026-05-05', '2026-05-07']),\n})\nprint('duplikat persis:', df.duplicated().sum(), '| duplikat id:', df.duplicated(subset=['id']).sum())\ndf = (df.sort_values('diperbarui')\n        .drop_duplicates(subset=['id'], keep='last'))      # simpan versi terbaru per id\n\n# nilai mustahil -> NaN, lalu isi median\nmustahil = ~df['umur'].between(15, 100)\nprint('umur mustahil:', df.loc[mustahil, 'umur'].tolist())\ndf.loc[mustahil, 'umur'] = np.nan\ndf['umur'] = df['umur'].fillna(df['umur'].median())\n\n# outlier belanja dengan IQR\nq1, q3 = df['belanja'].quantile([0.25, 0.75])\natas = q3 + 1.5 * (q3 - q1)\nprint(f'batas atas IQR: {atas:.0f} | outlier:', df.loc[df['belanja'] > atas, 'belanja'].tolist())\ndf['belanja_cap'] = df['belanja'].clip(upper=round(atas))   # capping\ndf['belanja_log'] = np.log1p(df['belanja']).round(2)    # alternatif: transformasi log\nprint(df[['id', 'umur', 'belanja', 'belanja_cap', 'belanja_log']].to_string(index=False))\nprint('rata-rata sebelum/sesudah capping:', round(df['belanja'].mean()), round(df['belanja_cap'].mean()))",
  pts=['Duplikat persis vs duplikat kunci; simpan versi terbaru.', 'Nilai mustahil adalah kesalahan: jadikan NaN.', 'Outlier bisa benar: capping, log, atau segmen sendiri.', 'Tulis aturan pembersihan sebagai kode yang bisa diulang.'],
  qs=[q('Umur pelanggan tercatat -3. Penanganan yang tepat?', ['Anggap kesalahan, jadikan NaN, lalu isi atau buang sesuai aturan', 'Biarkan karena itu outlier', 'Ubah menjadi 3'], 0, 'Nilai mustahil bukan outlier.'),
      q('<code>drop_duplicates(subset=["id"], keep="last")</code> setelah diurutkan menurut tanggal artinya?', ['Menyimpan baris terbaru untuk setiap id', 'Menghapus semua id ganda', 'Menyimpan baris pertama'], 0, 'keep="last" pada data terurut waktu.')],
  so=[SP('Dari Series <code>[12, 15, 14, 13, 90, 16, 11]</code>, hitung batas atas IQR lalu cetak nilai yang termasuk outlier.', 'quantile(0.25) dan quantile(0.75), batas = Q3 + 1,5 × IQR.',
         "import pandas as pd\ns = pd.Series([12, 15, 14, 13, 90, 16, 11])\nq1, q3 = s.quantile([0.25, 0.75])\natas = q3 + 1.5 * (q3 - q1)\nprint(atas, s[s > atas].tolist())")],
  nodes=['Data Understanding', 'Exploratory Data Analysis'])

L_EDA_UNI_MULTI = PF('EDA univariat, bivariat, dan multivariat',
  ['<b>Univariat</b>: satu kolom pada satu waktu. Untuk angka lihat pusat, sebaran, kemiringan, dan outlier; untuk kategori lihat frekuensi dan kategori langka. <b>Bivariat</b>: hubungan dua kolom, terutama setiap fitur terhadap target, misalnya churn rate per kelompok lama berlangganan.',
   '<b>Multivariat</b>: tiga kolom atau lebih sekaligus. Di sinilah pola yang tersembunyi muncul: churn tinggi di pelanggan baru, tetapi jauh lebih tinggi lagi pada pelanggan baru yang membayar manual. Alat yang sering dipakai: <code>pd.crosstab</code> atau <code>pivot_table</code> dua dimensi, lalu ditampilkan sebagai heatmap.',
   'Tutup setiap EDA dengan <b>daftar temuan yang bisa ditindaklanjuti</b>: fitur yang menjanjikan untuk model, masalah data yang harus diperbaiki, dan hipotesis untuk diuji. EDA tanpa kesimpulan hanyalah kumpulan grafik.'],
  DATA_PELANGGAN + "import matplotlib.pyplot as plt\n\nrng2 = np.random.default_rng(3)\ndf['metode_bayar'] = np.where(rng2.random(len(df)) < 0.35 + 0.35 * df['churn'], 'transfer manual', 'autodebet')\ndf['kel_lama'] = pd.cut(df['lama_bulan'], [0, 6, 12, 24, 48], labels=['0-6', '7-12', '13-24', '25-48'])\n\n# univariat\nprint('kemiringan belanja:', round(df['belanja_bln'].skew(), 2))\nprint(df['metode_bayar'].value_counts(normalize=True).round(2))\n\n# bivariat: fitur vs target\nprint((df.groupby('kel_lama', observed=True)['churn'].mean() * 100).round(1))\n\n# multivariat: lama x metode bayar -> churn rate\npv = df.pivot_table(index='kel_lama', columns='metode_bayar', values='churn', aggfunc='mean', observed=True) * 100\nprint(pv.round(1))\n\nfig, ax = plt.subplots(figsize=(5.4, 3.4))\nim = ax.imshow(pv.values, cmap='Reds', vmin=0, vmax=100)\nax.set_xticks(range(pv.shape[1]), pv.columns); ax.set_yticks(range(pv.shape[0]), pv.index)\nfor i in range(pv.shape[0]):\n    for j in range(pv.shape[1]):\n        ax.text(j, i, f'{pv.values[i, j]:.0f}%', ha='center', va='center')\nax.set_ylabel('lama berlangganan (bulan)')\nax.set_title('Churn tertinggi: pelanggan baru + transfer manual')\nfig.colorbar(im)",
  pts=['Univariat: satu kolom. Bivariat: fitur vs target.', 'Multivariat: pivot dua dimensi + heatmap.', 'Akhiri EDA dengan temuan yang bisa ditindaklanjuti.'],
  qs=[q('Membandingkan churn rate per kombinasi lama berlangganan dan metode bayar termasuk analisis?', ['Multivariat', 'Univariat', 'Deskriptif satu kolom'], 0, 'Tiga variabel sekaligus.'),
      q('Hasil EDA yang paling berguna bagi tim adalah?', ['Daftar temuan, masalah data, dan hipotesis yang bisa ditindaklanjuti', 'Sebanyak mungkin grafik', 'Satu angka akurasi'], 0, 'EDA harus berujung pada keputusan.')],
  nodes=['Exploratory Data Analysis', 'Data Analysis'])

L_FITUR = P('Feature engineering: membuat variabel baru yang bermakna',
  ['<b>Feature engineering</b> mengubah data mentah menjadi sinyal yang lebih mudah dipelajari model. Jenis yang paling sering: <b>rasio</b> (keluhan per bulan), <b>kelompok</b> (lama berlangganan dijadikan rentang), <b>bagian tanggal</b> (hari dalam minggu, jam, apakah tanggal gajian), <b>penanda</b> (is_new, is_weekend), dan <b>agregat dari tabel transaksi</b> (frekuensi, total, dan jarak hari sejak transaksi terakhir, atau RFM).',
   'Fitur yang baik lahir dari pemahaman bisnis: "pelanggan yang lama tidak bertransaksi cenderung pergi" menjadi fitur <code>hari_sejak_terakhir</code>. Uji cepat setiap fitur baru dengan melihat hubungannya ke target (churn rate per kelompok), lalu pastikan lewat validasi silang.',
   'Bahaya terbesarnya adalah <b>kebocoran data</b>: fitur yang memakai informasi setelah titik prediksi, misalnya "jumlah tiket pembatalan" yang baru ada setelah pelanggan memutuskan pergi. Selalu tetapkan <b>tanggal potong</b> dan hitung fitur hanya dari data sebelum tanggal itu.'],
  "import numpy as np\nimport pandas as pd\n\nrng = np.random.default_rng(11)\ntrx = pd.DataFrame({\n    'id': rng.integers(1, 7, 40),\n    'tanggal': pd.Timestamp('2026-01-01') + pd.to_timedelta(rng.integers(0, 150, 40), unit='D'),\n    'nilai': rng.gamma(3, 40_000, 40).round(-3),\n})\npotong = pd.Timestamp('2026-05-01')                   # titik prediksi\nlalu = trx[trx['tanggal'] < potong]                   # hanya data SEBELUM tanggal potong\n\nfitur = (lalu.groupby('id')\n             .agg(frekuensi=('nilai', 'size'), total=('nilai', 'sum'), terakhir=('tanggal', 'max'))\n             .assign(hari_sejak_terakhir=lambda d: (potong - d['terakhir']).dt.days,\n                     rata_per_trx=lambda d: (d['total'] / d['frekuensi']).round(-2),\n                     tidak_aktif_30=lambda d: (d['hari_sejak_terakhir'] > 30).astype(int))\n             .drop(columns='terakhir'))\nprint(fitur)\n\nlalu = lalu.assign(hari=lalu['tanggal'].dt.day_name(), akhir_pekan=lalu['tanggal'].dt.dayofweek >= 5)\nprint(lalu.groupby('akhir_pekan')['nilai'].mean().round(-2))\nprint('transaksi setelah tanggal potong (tidak boleh dipakai sebagai fitur):', (trx['tanggal'] >= potong).sum())",
  pts=['Jenis fitur: rasio, kelompok, bagian tanggal, penanda, agregat (RFM).', 'Fitur baik berasal dari pemahaman bisnis.', 'Tetapkan tanggal potong untuk mencegah kebocoran data.'],
  qs=[q('Fitur "jumlah permintaan berhenti berlangganan" untuk memprediksi churn bermasalah karena?', ['Informasinya baru ada setelah keputusan churn, jadi bocor', 'Bukan angka', 'Terlalu sedikit nilai'], 0, 'Data leakage.'),
      q('Recency dalam RFM artinya?', ['Jarak hari sejak transaksi terakhir', 'Jumlah transaksi', 'Total nilai belanja'], 0, 'R = recency, F = frequency, M = monetary.')],
  so=[SP('Dari DataFrame <code>pd.DataFrame({"belanja": [300, 120, 900], "lama_bulan": [10, 2, 30]})</code>, buat kolom <code>belanja_per_bulan_langganan</code> (belanja dibagi lama_bulan, dibulatkan 1 desimal) dan kolom <code>baru</code> (1 jika lama_bulan ≤ 6).', 'Pakai assign atau operasi kolom langsung.',
         "import pandas as pd\ndf = pd.DataFrame({'belanja': [300, 120, 900], 'lama_bulan': [10, 2, 30]})\ndf['belanja_per_bulan_langganan'] = (df['belanja'] / df['lama_bulan']).round(1)\ndf['baru'] = (df['lama_bulan'] <= 6).astype(int)\nprint(df.to_string(index=False))")],
  nodes=['Exploratory Data Analysis', 'Feature Engineering'])

# ---------------------------------------------------------------------------
# Modul 6: Machine learning klasik (ditambah di akhir)
# ---------------------------------------------------------------------------
L_PERSIAPAN = P('Peta ML dan persiapan data sebelum model',
  ['Dua pertanyaan menentukan jenis masalah. <b>Ada target (label) atau tidak?</b> Jika ada, itu <b>supervised learning</b>; jika tidak (misalnya mengelompokkan pelanggan), itu <b>unsupervised</b>. <b>Targetnya angka atau kelas?</b> Angka (harga, jumlah) berarti <b>regresi</b>; kelas (churn ya/tidak, jenis penyakit) berarti <b>klasifikasi</b>.',
   'Persiapan sebelum model: kategori diubah menjadi angka (<b>one-hot</b> untuk kategori tanpa urutan seperti kota, <b>ordinal</b> untuk yang berurutan seperti Basic &lt; Standar &lt; Premium), fitur angka diskalakan untuk model berbasis jarak atau gradien (logistic regression, KNN, SVM), lalu data dibagi latih dan uji.',
   'Urutannya penting: <b>bagi data dulu, baru pelajari skala dan encoding dari data latih saja</b>. Jika <code>StandardScaler</code> di-fit pada seluruh data, statistik data uji ikut bocor ke model. Cara aman dan standar industri adalah memasukkan semua langkah ke dalam <code>Pipeline</code>.'],
  "import numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.linear_model import LogisticRegression\n\nmasalah = {'Tebak harga rumah': ('supervised', 'regresi'),\n           'Tebak pelanggan churn': ('supervised', 'klasifikasi'),\n           'Kelompokkan pelanggan': ('unsupervised', 'clustering')}\nfor m, (a, b) in masalah.items():\n    print(f'{m:22} -> {a:12} | {b}')\n\nrng = np.random.default_rng(0)\nn = 400\ndf = pd.DataFrame({'kota': rng.choice(['Medan', 'Bandung', 'Jakarta'], n),\n                   'paket': rng.choice(['Basic', 'Standar', 'Premium'], n),\n                   'lama_bulan': rng.integers(1, 48, n), 'keluhan': rng.poisson(1.2, n)})\ndf['churn'] = (rng.random(n) < 0.15 + 0.1 * df['keluhan'].clip(0, 4) - 0.003 * df['lama_bulan']).astype(int)\n\nX, y = df.drop(columns='churn'), df['churn']\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)\npra = ColumnTransformer([\n    ('kota', OneHotEncoder(handle_unknown='ignore'), ['kota']),\n    ('paket', OrdinalEncoder(categories=[['Basic', 'Standar', 'Premium']]), ['paket']),\n    ('angka', StandardScaler(), ['lama_bulan', 'keluhan']),\n])\npipe = Pipeline([('pra', pra), ('model', LogisticRegression(max_iter=1000))]).fit(X_tr, y_tr)\nprint('kolom setelah praproses:', list(pipe.named_steps['pra'].get_feature_names_out()))\nprint('akurasi uji:', round(pipe.score(X_te, y_te), 3))",
  pts=['Ada target → supervised; tidak ada → unsupervised.', 'Target angka → regresi; kelas → klasifikasi.', 'One-hot untuk kategori tanpa urutan, ordinal untuk yang berurutan.', 'Split dulu, fit praproses di data latih (Pipeline).'],
  qs=[q('Memprediksi lama (hari) pasien dirawat termasuk?', ['Supervised, regresi', 'Supervised, klasifikasi', 'Unsupervised'], 0, 'Target berupa angka.'),
      q('Kenapa StandardScaler tidak boleh di-fit pada seluruh data sebelum split?', ['Statistik data uji bocor ke model sehingga skor uji terlalu optimis', 'Karena lebih lambat', 'Karena scaler hanya untuk kategori'], 0, 'Kebocoran data.')],
  nodes=['Machine Learning', 'Supervised Learning', 'Unsupervised Learning'])

L_TIDAK_SEIMBANG = P('Data tidak seimbang: class_weight, oversampling, dan metrik yang jujur',
  ['Di banyak masalah nyata kelas penting sangat jarang: penipuan 1%, gagal bayar 5%, pasien kembali dirawat 10%. Model yang selalu menebak "tidak" sudah mendapat akurasi 95% tetapi tidak berguna. Karena itu <b>akurasi menyesatkan</b>; pakai <b>precision</b>, <b>recall</b>, <b>F1</b>, dan <b>PR-AUC</b> (average precision).',
   'Tiga cara menangani: <b>(1)</b> <code>class_weight="balanced"</code> agar kesalahan pada kelas langka dihukum lebih berat (paling sederhana, tanpa mengubah data); <b>(2)</b> <b>resampling</b> data latih: oversampling kelas langka (acak atau SMOTE dari pustaka <code>imbalanced-learn</code>) atau undersampling kelas mayoritas; <b>(3)</b> <b>menggeser ambang</b> keputusan sesuai biaya.',
   'Aturan wajib: resampling <b>hanya pada data latih</b>, tidak pernah pada data uji, karena data uji harus mencerminkan dunia nyata. Gunakan <code>stratify=y</code> saat membagi data agar proporsi kelas langka sama di latih dan uji.'],
  "import numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.utils import resample\nfrom sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, average_precision_score\n\nrng = np.random.default_rng(5)\nn = 4000\nX = pd.DataFrame({'telat_bayar': rng.poisson(0.6, n), 'rasio_utang': rng.beta(2, 5, n), 'lama_kerja': rng.integers(0, 20, n)})\nlogit = -4.4 + 0.9 * X['telat_bayar'] + 3.0 * X['rasio_utang'] - 0.05 * X['lama_kerja']\ny = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)\nprint(f'proporsi gagal bayar: {y.mean():.1%}')\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)\n\ndef nilai(nama, model, Xl, yl):\n    model.fit(Xl, yl)\n    p = model.predict(X_te)\n    ap = average_precision_score(y_te, model.predict_proba(X_te)[:, 1])\n    print(f'{nama:22} akurasi={accuracy_score(y_te, p):.3f} precision={precision_score(y_te, p, zero_division=0):.2f} '\n          f'recall={recall_score(y_te, p):.2f} F1={f1_score(y_te, p):.2f} PR-AUC={ap:.3f}')\n\nnilai('tanpa penanganan', LogisticRegression(max_iter=1000), X_tr, y_tr)\nnilai('class_weight=balanced', LogisticRegression(max_iter=1000, class_weight='balanced'), X_tr, y_tr)\n\nlatih = X_tr.assign(y=y_tr)\nlangka = latih[latih.y == 1]\nbanyak = latih[latih.y == 0]\nnaik = pd.concat([banyak, resample(langka, n_samples=len(banyak), replace=True, random_state=0)])\nnilai('oversampling (latih)', LogisticRegression(max_iter=1000), naik.drop(columns='y'), naik['y'])",
  pts=['Kelas langka: akurasi menyesatkan.', 'Pakai precision, recall, F1, PR-AUC.', 'class_weight, resampling (hanya data latih), atau geser ambang.', 'stratify=y saat split.'],
  qs=[q('Model tanpa penanganan mendapat akurasi tinggi tetapi recall 0. Artinya?', ['Model hampir selalu menebak kelas mayoritas', 'Model sempurna', 'Data uji salah'], 0, 'Akurasi didominasi kelas mayoritas.'),
      q('Oversampling sebaiknya diterapkan ke?', ['Data latih saja', 'Data uji saja', 'Seluruh data sebelum split'], 0, 'Data uji harus mencerminkan dunia nyata.')],
  nodes=['Classification', 'Model Evaluation'])

# ---------------------------------------------------------------------------
# Modul baru: Dari model ke keputusan bisnis
# ---------------------------------------------------------------------------
L_METRIK_INDUSTRI = P('Metrik bisnis per industri: keuangan, pemasaran, kesehatan, logistik',
  ['Model dinilai tim data dengan AUC atau RMSE, tetapi dinilai manajemen dengan <b>metrik bisnis</b>. Tugas data scientist adalah menjembatani keduanya. Setiap industri punya metrik utama yang berbeda, jadi kenali bahasanya sebelum presentasi.',
   '<b>Keuangan</b>: approval rate, bad rate / NPL (porsi kredit macet), dan <b>expected loss = PD × LGD × EAD</b>. <b>Pemasaran dan penjualan</b>: conversion rate, CAC (biaya akuisisi per pelanggan), ROAS (pendapatan per rupiah iklan), dan LTV (nilai pelanggan seumur hidup); aturan praktis yang sering dipakai: LTV/CAC ≥ 3. <b>Kesehatan</b>: sensitivitas (pasien sakit yang terdeteksi), spesifisitas, dan PPV; kesalahan melewatkan pasien sakit biasanya jauh lebih mahal. <b>Logistik</b>: on-time delivery rate, rata-rata waktu antar, biaya per pengiriman, dan MAPE untuk peramalan permintaan.',
   'Contoh di bawah menghitung semua metrik itu dari angka kecil yang mudah diikuti. Biasakan setiap laporan model diakhiri satu kalimat seperti "model ini menurunkan bad rate dari 6,1% menjadi 4,3% pada approval rate yang sama".'],
  "import numpy as np\n\n# Keuangan: 1.000 pengajuan pinjaman\ndisetujui, macet = 720, 31\npd_, lgd, ead = 0.045, 0.6, 8_000_000\nprint(f'[Keuangan] approval {disetujui / 1000:.0%}, bad rate {macet / disetujui:.1%}, expected loss/pinjaman Rp{pd_ * lgd * ead:,.0f}')\n\n# Pemasaran\niklan, klik, beli, pendapatan = 25_000_000, 18_000, 540, 97_200_000\nmargin_bln, umur_bln = 38_000, 14\ncac = iklan / beli\nltv = margin_bln * umur_bln\nprint(f'[Pemasaran] konversi {beli / klik:.1%}, CAC Rp{cac:,.0f}, ROAS {pendapatan / iklan:.2f}x, LTV Rp{ltv:,.0f}, LTV/CAC {ltv / cac:.1f}')\n\n# Kesehatan: skrining 2.000 pasien\ntp, fn, fp, tn = 86, 14, 190, 1710\nprint(f'[Kesehatan] sensitivitas {tp / (tp + fn):.0%}, spesifisitas {tn / (tn + fp):.0%}, PPV {tp / (tp + fp):.0%}')\n\n# Logistik\ntepat, total, biaya = 4_620, 5_000, 61_500_000\naktual = np.array([120, 135, 150, 128, 160])\nramalan = np.array([110, 140, 138, 130, 172])\nmape = np.mean(np.abs(aktual - ramalan) / aktual)\nprint(f'[Logistik] on-time {tepat / total:.1%}, biaya/kiriman Rp{biaya / total:,.0f}, MAPE ramalan {mape:.1%}')",
  tb=[{'c': 'Metrik utama per industri', 'h': ['Industri', 'Metrik', 'Yang ditanyakan manajemen'],
       'r': [['Keuangan', 'Approval rate, bad rate/NPL, expected loss', 'Berapa banyak yang bisa disetujui tanpa menambah kredit macet?'],
             ['Pemasaran & penjualan', 'Konversi, CAC, ROAS, LTV', 'Apakah setiap rupiah iklan kembali lebih banyak?'],
             ['Kesehatan', 'Sensitivitas, spesifisitas, PPV', 'Berapa pasien berisiko yang terlewat?'],
             ['Logistik & transportasi', 'On-time rate, waktu antar, biaya/kiriman, MAPE', 'Apakah paket tiba tepat waktu dengan biaya wajar?']]}],
  pts=['Model dinilai manajemen lewat metrik bisnis.', 'Expected loss = PD × LGD × EAD.', 'LTV/CAC dan ROAS untuk pemasaran.', 'Sensitivitas penting di kesehatan; on-time rate dan MAPE di logistik.'],
  qs=[q('PD 5%, LGD 60%, EAD Rp10 juta. Expected loss per pinjaman?', ['Rp300.000', 'Rp500.000', 'Rp6.000.000'], 0, '0,05 × 0,6 × 10 juta.'),
      q('Dalam skrining penyakit serius, metrik yang paling dijaga biasanya?', ['Sensitivitas (recall)', 'Akurasi', 'Spesifisitas saja'], 0, 'Melewatkan pasien sakit paling mahal.')],
  so=[SP('Biaya iklan Rp12 juta menghasilkan 300 pelanggan baru. Margin per pelanggan Rp25.000 per bulan dan rata-rata bertahan 10 bulan. Hitung CAC, LTV, dan rasio LTV/CAC.', 'CAC = biaya / pelanggan; LTV = margin × umur.',
         "cac = 12_000_000 / 300\nltv = 25_000 * 10\nprint(cac, ltv, round(ltv / cac, 2))")],
  nodes=['Business Metrics'])

L_CHURN_RUPIAH = PF('Kasus churn: dari peluang ke rupiah',
  ['Tim retensi punya anggaran kampanye: setiap pelanggan yang dihubungi diberi voucher Rp50.000. Jika pelanggan yang hampir churn berhasil ditahan, perusahaan mempertahankan margin sekitar Rp600.000 per tahun, tetapi tidak semua yang dihubungi mau bertahan (misalnya 35% berhasil).',
   'Dengan peluang churn dari model, nilai harapan menghubungi satu pelanggan = <code>p_churn × tingkat_berhasil × nilai_pelanggan − biaya</code>. Urutkan pelanggan dari peluang tertinggi, lalu jumlahkan nilai harapan untuk setiap ukuran kampanye. Titik puncak <b>kurva laba</b> menunjukkan berapa banyak pelanggan yang layak dihubungi.',
   'Bandingkan dengan dua strategi patokan: menghubungi semua orang dan memilih acak. Angka yang dibawa ke rapat bukan "AUC 0,78", melainkan "menghubungi 25% pelanggan teratas memberi laba bersih Rp X, Y kali lipat dibanding acak".'],
  DATA_PELANGGAN + "import matplotlib.pyplot as plt\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_predict\n\nX = df[['umur', 'lama_bulan', 'belanja_bln', 'keluhan']]\np = cross_val_predict(LogisticRegression(max_iter=1000), X, df['churn'], cv=5, method='predict_proba')[:, 1]\n\nbiaya, berhasil, nilai = 50_000, 0.35, 600_000\nurut = np.sort(p)[::-1]\nlaba_kum = np.cumsum(urut * berhasil * nilai - biaya)\nporsi = np.arange(1, len(urut) + 1) / len(urut)\nterbaik = laba_kum.argmax()\nacak = porsi * len(p) * (df['churn'].mean() * berhasil * nilai - biaya)\n\nprint(f'hubungi semua : Rp{laba_kum[-1]:,.0f}')\nprint(f'hubungi {porsi[terbaik]:.0%} teratas ({terbaik + 1} orang): Rp{laba_kum[terbaik]:,.0f}')\nprint(f'acak dengan jumlah sama: Rp{acak[terbaik]:,.0f}')\n\nplt.figure(figsize=(6.2, 3.4))\nplt.plot(porsi, laba_kum / 1e6, label='urut menurut model')\nplt.plot(porsi, acak / 1e6, '--', color='gray', label='acak')\nplt.axvline(porsi[terbaik], color='tab:red', linewidth=1)\nplt.xlabel('porsi pelanggan dihubungi'); plt.ylabel('laba bersih (juta Rp)')\nplt.title('Kurva laba kampanye retensi'); plt.legend()",
  pts=['Nilai harapan = p × berhasil × nilai − biaya.', 'Kurva laba menunjukkan ukuran kampanye terbaik.', 'Selalu bandingkan dengan acak dan "hubungi semua".'],
  qs=[q('p churn 0,4, tingkat berhasil 35%, nilai pelanggan Rp600.000, biaya Rp50.000. Nilai harapan menghubungi?', ['Rp34.000', 'Rp240.000', '−Rp50.000'], 0, '0,4 × 0,35 × 600.000 − 50.000 = 34.000.'),
      q('Kenapa laba turun jika semua pelanggan dihubungi?', ['Pelanggan berpeluang churn rendah tetap memakan biaya voucher', 'Model menjadi salah', 'Pelanggan bosan'], 0, 'Nilai harapan negatif di bagian bawah daftar.')],
  nodes=['Business Metrics', 'Model Evaluation'])

L_KREDIT = PF('Kasus kredit: menentukan ambang persetujuan pinjaman',
  ['Lembaga pembiayaan ingin menyetujui sebanyak mungkin pengajuan tanpa menaikkan kredit macet. Model memberi <b>PD</b> (probability of default) setiap pemohon. Kebijakannya sederhana: setujui jika PD di bawah ambang. Ambang rendah berarti aman tetapi sedikit nasabah; ambang tinggi berarti banyak nasabah tetapi bad rate naik.',
   'Untuk memilih ambang, buat tabel <b>approval rate vs bad rate</b> dan hitung <b>laba harapan</b> setiap ambang: nasabah lancar memberi bunga, nasabah macet menimbulkan kerugian sebesar LGD × plafon. Pilih ambang dengan laba terbesar yang masih di bawah batas risiko yang ditetapkan manajemen risiko.',
   'Di industri, PD sering diubah menjadi <b>skor kredit</b> (misalnya 300–850) dengan aturan PDO (points to double the odds) agar mudah dipakai petugas. Model kredit juga wajib bisa dijelaskan dan diaudit keadilannya, karena keputusan menolak pinjaman berdampak langsung pada orang.'],
  "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import train_test_split\n\nrng = np.random.default_rng(8)\nn = 6000\nX = pd.DataFrame({'telat_bayar_12bln': rng.poisson(0.5, n), 'rasio_cicilan': rng.beta(2, 5, n),\n                  'lama_kerja_thn': rng.integers(0, 25, n), 'pinjaman_aktif': rng.integers(0, 5, n)})\nlogit = -3.6 + 0.8 * X.telat_bayar_12bln + 3.2 * X.rasio_cicilan - 0.06 * X.lama_kerja_thn + 0.25 * X.pinjaman_aktif\ny = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.4, stratify=y, random_state=0)\npd_hat = LogisticRegression(max_iter=1000).fit(X_tr, y_tr).predict_proba(X_te)[:, 1]\n\nplafon, bunga, lgd = 10_000_000, 0.18, 0.65\nbaris = []\nfor ambang in [0.03, 0.05, 0.08, 0.12, 0.20, 1.0]:\n    setuju = pd_hat < ambang\n    macet = y_te[setuju]\n    laba = ((1 - macet) * plafon * bunga - macet * plafon * lgd).sum()\n    baris.append([ambang, setuju.mean(), macet.mean() if setuju.any() else 0, laba / 1e6])\ntabel = pd.DataFrame(baris, columns=['ambang_PD', 'approval', 'bad_rate', 'laba_juta'])\nprint(tabel.round(3).to_string(index=False))\nprint('ambang dengan laba terbesar:', tabel.loc[tabel.laba_juta.idxmax(), 'ambang_PD'])\n\n# PD -> skor kredit: 600 poin = odds 50:1, setiap 20 poin odds menjadi 2x\nodds = (1 - pd_hat) / pd_hat\nskor = 600 + 20 / np.log(2) * np.log(odds / 50)\nprint('contoh PD -> skor:', [(round(float(a), 3), int(b)) for a, b in zip(pd_hat[:3], skor[:3])])\n\nplt.figure(figsize=(5.8, 3.3))\nplt.plot(tabel.approval, tabel.bad_rate * 100, 'o-')\nfor _, r in tabel.iterrows():\n    plt.annotate(f'PD<{r.ambang_PD:g}', (r.approval, r.bad_rate * 100), textcoords='offset points', xytext=(4, -10), fontsize=8)\nplt.xlabel('approval rate'); plt.ylabel('bad rate (%)')\nplt.title('Makin banyak disetujui, makin tinggi bad rate')",
  pts=['Kebijakan: setujui jika PD < ambang.', 'Pilih ambang dari tabel approval, bad rate, dan laba.', 'PD bisa diubah menjadi skor kredit dengan PDO.', 'Model kredit wajib bisa dijelaskan dan adil.'],
  qs=[q('Ambang PD dinaikkan dari 5% ke 12%. Yang biasanya terjadi?', ['Approval rate dan bad rate sama-sama naik', 'Keduanya turun', 'Approval turun, bad rate naik'], 0, 'Lebih banyak pemohon berisiko ikut disetujui.'),
      q('Kenapa ambang tidak dipilih dari akurasi tertinggi?', ['Kerugian macet dan keuntungan nasabah lancar tidak sama besar', 'Akurasi tidak bisa dihitung', 'Karena data tidak seimbang saja'], 0, 'Biaya kesalahan tidak simetris.')],
  nodes=['Business Metrics', 'Classification'])

L_KOMUNIKASI = P('Menyampaikan hasil model ke pengambil keputusan',
  ['Hasil model baru bernilai jika dipahami dan dipakai. Struktur satu halaman yang umum dipakai di industri: <b>(1) keputusan yang diminta</b>, <b>(2) temuan utama dalam angka bisnis</b>, <b>(3) bagaimana model bekerja dalam satu kalimat</b>, <b>(4) faktor yang paling berpengaruh</b>, <b>(5) risiko dan batasan</b>, <b>(6) langkah berikutnya</b>. Mulai dari kesimpulan, bukan dari proses.',
   'Untuk menjelaskan faktor berpengaruh, <b>permutation importance</b> adalah cara yang jujur dan bisa dipakai untuk model apa pun: acak satu kolom di data uji, lalu lihat seberapa besar skor model turun. Untuk penjelasan per orang ("kenapa pelanggan ini dinilai berisiko"), tim biasanya memakai SHAP.',
   'Hindari jargon (ROC-AUC, log loss) di slide utama; taruh di lampiran. Sebutkan ketidakpastian dengan jujur ("perkiraan laba Rp120–180 juta"), dan sepakati cara memantau keberhasilan setelah model dipakai.'],
  DATA_PELANGGAN + "from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.inspection import permutation_importance\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import roc_auc_score\n\nX = df[['umur', 'lama_bulan', 'belanja_bln', 'keluhan']]; y = df['churn']\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)\nm = RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=0).fit(X_tr, y_tr)\nimp = permutation_importance(m, X_te, y_te, scoring='roc_auc', n_repeats=20, random_state=0)\nurut = sorted(zip(X.columns, imp.importances_mean), key=lambda x: -x[1])\n\nnama = {'keluhan': 'jumlah keluhan', 'lama_bulan': 'lama berlangganan', 'belanja_bln': 'belanja bulanan', 'umur': 'umur'}\np = m.predict_proba(X_te)[:, 1]\natas = np.argsort(-p)[:int(len(p) * 0.2)]\ntangkap = y_te.iloc[atas].sum() / y_te.sum()\n\nprint('RINGKASAN UNTUK TIM RETENSI')\nprint('1. Keputusan: siapa yang dihubungi dalam kampanye bulan depan.')\nprint(f'2. Temuan: menghubungi 20% pelanggan teratas menangkap {tangkap:.0%} pelanggan yang akan berhenti (acak: 20%).')\nprint('3. Cara kerja: model belajar dari riwayat pelanggan yang pernah berhenti.')\nprint('4. Faktor terkuat: ' + ', '.join(nama[f] for f, v in urut[:2] if v > 0) + '.')\nprint('5. Risiko: data hanya 300 pelanggan; pantau hasil kampanye sebelum diperluas.')\nprint('6. Berikutnya: uji coba A/B kampanye pada 2 kota selama 4 minggu.')\nprint(f'[lampiran] ROC-AUC uji = {roc_auc_score(y_te, p):.3f}; importance:', {f: round(float(v), 3) for f, v in urut})",
  pts=['Mulai dari keputusan dan angka bisnis.', 'Permutation importance untuk faktor berpengaruh.', 'Jargon teknis masuk lampiran.', 'Sampaikan ketidakpastian dan rencana pemantauan.'],
  qs=[q('Kalimat pembuka presentasi model yang paling efektif?', ['"Menghubungi 20% pelanggan teratas menangkap separuh calon churn"', '"Kami memakai random forest dengan 200 pohon"', '"ROC-AUC model kami 0,78"'], 0, 'Mulai dari dampak bisnis.'),
      q('Permutation importance mengukur?', ['Seberapa besar skor turun jika satu kolom diacak', 'Koefisien regresi', 'Jumlah nilai hilang'], 0, 'Semakin turun, semakin penting.')],
  nodes=['Business Metrics', 'Data Storytelling'])

L_KARIER = T('Karier data scientist 2026-2030: peran, portofolio, dan wawancara',
  ['Lowongan "data scientist" kini terbagi menjadi beberapa peran: <b>product/analytics data scientist</b> (eksperimen, metrik, SQL kuat), <b>ML/applied scientist</b> (membangun model prediksi), <b>ML engineer/MLOps</b> (membawa model ke produksi), dan <b>AI engineer</b> (membangun aplikasi di atas LLM: RAG, evaluasi, agen). Fondasinya sama: Python, SQL, statistik, dan kemampuan menerjemahkan masalah bisnis.',
   '<b>Portofolio yang dilirik perekrut</b>: 3–4 proyek yang menyelesaikan masalah bisnis nyata dari awal sampai akhir, masing-masing dengan README yang menjelaskan masalah, data, pendekatan, hasil dalam angka bisnis, dan batasan; kode rapi dalam repositori (bukan satu notebook panjang); dan minimal satu model yang bisa dicoba (API atau aplikasi kecil). Kualitas lebih penting daripada jumlah.',
   '<b>Tahap wawancara</b> yang umum: penyaringan CV, tes SQL dan Python, statistik dan eksperimen (A/B test), studi kasus ML ("bagaimana kamu membangun model deteksi penipuan?"), take-home project atau presentasi, lalu wawancara perilaku. Latih menjelaskan proyekmu dengan struktur masalah → pendekatan → hasil → apa yang akan kamu lakukan berbeda.'],
  "Rencana 90 hari menuju lamaran pertama\n\nBulan 1  Fondasi\n  - Python, pandas, SQL: 30 menit latihan setiap hari\n  - Statistik: uji hipotesis, selang kepercayaan, A/B test\n\nBulan 2  Proyek end-to-end\n  - 2 studi kasus (klasifikasi + regresi) dengan 6 langkah:\n    pemahaman bisnis, pembersihan, EDA, persiapan, model, kesimpulan bisnis\n  - README berisi angka bisnis, bukan hanya akurasi\n\nBulan 3  Produksi dan lamaran\n  - 1 model disajikan lewat API + Docker, dipantau driftnya\n  - Profil GitHub dan LinkedIn rapi, 3 proyek tersemat\n  - Latihan wawancara: SQL, statistik, studi kasus ML, presentasi 10 menit",
  lang='text',
  tb=[{'c': 'Peran di keluarga data science', 'h': ['Peran', 'Fokus', 'Keahlian pembeda'],
       'r': [['Product/analytics DS', 'Metrik, eksperimen, insight', 'SQL, statistik, A/B test, komunikasi'],
             ['ML/applied scientist', 'Model prediksi', 'Algoritma ML, evaluasi, feature engineering'],
             ['ML engineer/MLOps', 'Model di produksi', 'API, Docker, CI/CD, pemantauan'],
             ['AI engineer', 'Aplikasi berbasis LLM', 'RAG, evaluasi LLM, prompt dan tool, keamanan']]}],
  pts=['Peran: analytics DS, applied scientist, ML engineer, AI engineer.', 'Portofolio: 3-4 proyek end-to-end dengan angka bisnis.', 'Wawancara: SQL, statistik, studi kasus ML, presentasi.'],
  qs=[q('Isi README proyek portofolio yang paling dicari perekrut?', ['Masalah, pendekatan, hasil dalam angka bisnis, dan batasan', 'Daftar semua pustaka yang dipakai', 'Hanya skor akurasi'], 0, 'Perekrut menilai cara berpikir dan dampak.'),
      q('Peran yang paling menekankan A/B test dan metrik produk?', ['Product/analytics data scientist', 'ML engineer', 'AI engineer'], 0, 'Eksperimen dan metrik adalah inti peran itu.')],
  nodes=['Career'])

BISNIS = M('Dari model ke keputusan bisnis', 'Lanjutan',
  'Menerjemahkan metrik model menjadi metrik bisnis di keuangan, pemasaran, kesehatan, dan logistik; menghitung nilai rupiah kampanye churn; memilih ambang persetujuan kredit; menyampaikan hasil ke pengambil keputusan; dan menyiapkan karier.',
  ['Business Metrics', 'Model Evaluation', 'Data Storytelling', 'Career'],
  [L_METRIK_INDUSTRI, L_CHURN_RUPIAH, L_KREDIT, L_KOMUNIKASI, L_KARIER])

# ---------------------------------------------------------------------------
# Modul baru: Studi kasus end-to-end (kode final disembunyikan sampai tombol ditekan)
# ---------------------------------------------------------------------------
ENAM = ['Pemahaman bisnis: rumuskan keputusan, target, dan metrik keberhasilan.',
        'Pembersihan data: duplikat, nilai mustahil, nilai hilang, dan outlier.',
        'EDA: hubungan fitur dengan target, lalu tulis temuan.',
        'Persiapan data: fitur baru, encoding, split latih-uji tanpa kebocoran.',
        'Pemodelan dan evaluasi: baseline, dua model atau lebih, metrik yang sesuai.',
        'Kesimpulan bisnis: angka rupiah atau operasional, rekomendasi, dan risiko.']

KODE_K1 = r'''# main.py - Studi kasus 1: keterlambatan pengiriman
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, recall_score, precision_score

# 1) PEMAHAMAN BISNIS
# Keputusan: paket berisiko telat diberi prioritas sortir + notifikasi proaktif ke pembeli.
# Target: telat = 1 jika tiba melewati janji. Metrik: recall pada 15% paket berisiko tertinggi.
rng = np.random.default_rng(42)
n = 5000
df = pd.DataFrame({
    'id_kiriman': np.arange(n),
    'jarak_km': rng.gamma(2.2, 60, n).round(1),
    'berat_kg': rng.gamma(1.6, 1.8, n).round(2),
    'layanan': rng.choice(['reguler', 'kilat', 'ekonomi'], n, p=[.55, .25, .2]),
    'pulau_tujuan': rng.choice(['Jawa', 'Sumatra', 'Kalimantan', 'Sulawesi', 'Papua'], n, p=[.5, .2, .12, .1, .08]),
    'jam_pickup': rng.integers(7, 22, n),
    'hari_libur': rng.random(n) < 0.12,
    'beban_gudang': rng.normal(0.7, 0.15, n).clip(0.2, 1.3).round(2),
})
logit = (-3.0 + 0.006 * df.jarak_km + 0.9 * (df.pulau_tujuan.isin(['Papua', 'Sulawesi'])) + 0.7 * df.hari_libur
         + 2.2 * (df.beban_gudang - 0.7) + 0.08 * (df.jam_pickup - 14).clip(0) - 0.6 * (df.layanan == 'kilat'))
df['telat'] = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
df = pd.concat([df, df.sample(40, random_state=1)])            # duplikat dari impor ulang
df.loc[df.sample(25, random_state=2).index, 'berat_kg'] = -1    # nilai mustahil dari timbangan rusak

# 2) PEMBERSIHAN
df = df.drop_duplicates(subset='id_kiriman')
df.loc[df.berat_kg <= 0, 'berat_kg'] = np.nan
df['berat_kg'] = df['berat_kg'].fillna(df['berat_kg'].median())
print(f'baris bersih: {len(df)}, telat: {df.telat.mean():.1%}')

# 3) EDA
print((df.groupby('pulau_tujuan')['telat'].mean() * 100).round(1).sort_values(ascending=False).to_dict())
print('telat saat gudang padat (>0,85):', f"{df.loc[df.beban_gudang > 0.85, 'telat'].mean():.1%}",
      '| normal:', f"{df.loc[df.beban_gudang <= 0.85, 'telat'].mean():.1%}")

# 4) PERSIAPAN
df['pickup_malam'] = (df.jam_pickup >= 18).astype(int)
df['km_per_kg'] = (df.jarak_km / (df.berat_kg + 0.5)).round(1)
fitur_kat = ['layanan', 'pulau_tujuan']
fitur_num = ['jarak_km', 'berat_kg', 'jam_pickup', 'beban_gudang', 'pickup_malam', 'km_per_kg']
X = df[fitur_kat + fitur_num].assign(hari_libur=df.hari_libur.astype(int))
y = df['telat']
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)
pra = ColumnTransformer([('kat', OneHotEncoder(handle_unknown='ignore'), fitur_kat),
                         ('num', StandardScaler(), fitur_num + ['hari_libur'])])

# 5) PEMODELAN DAN EVALUASI
def top_k(p, k=0.15):
    ambang = np.quantile(p, 1 - k)
    tebak = (p >= ambang).astype(int)
    return recall_score(y_te, tebak), precision_score(y_te, tebak)

aturan = (X_te.pulau_tujuan.isin(['Papua', 'Sulawesi']) * 1.0 + X_te.beban_gudang).values
print(f'baseline aturan : recall@15% {top_k(aturan)[0]:.2f}')
for nama, model in [('logistic', LogisticRegression(max_iter=1000)),
                    ('boosting', HistGradientBoostingClassifier(max_depth=3, learning_rate=0.08, random_state=0))]:
    pipe = Pipeline([('pra', pra), ('model', model)]).fit(X_tr, y_tr)
    p = pipe.predict_proba(X_te)[:, 1]
    r, pr = top_k(p)
    print(f'{nama:16}: AUC {roc_auc_score(y_te, p):.3f} | recall@15% {r:.2f} | precision@15% {pr:.2f}')

# 6) KESIMPULAN BISNIS
biaya_telat, biaya_prioritas, tertolong = 35_000, 4_000, 0.5   # kompensasi, biaya sortir, porsi yang jadi tepat waktu
k = int(0.15 * len(p))
telat_tertangkap = y_te.values[np.argsort(-p)[:k]].sum()
hemat = telat_tertangkap * tertolong * biaya_telat - k * biaya_prioritas
print(f'Prioritaskan {k} paket (15%): {telat_tertangkap} paket telat ditangani, perkiraan hemat Rp{hemat:,.0f} per {len(y_te)} kiriman.')
'''

KODE_K2 = r'''# main.py - Studi kasus 2: pasien kembali dirawat dalam 30 hari
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score, average_precision_score

# 1) PEMAHAMAN BISNIS
# Keputusan: pasien berisiko tinggi mendapat telepon perawat + kontrol lebih awal setelah pulang.
# Target: dirawat_lagi = 1 jika masuk lagi <= 30 hari. Metrik: sensitivitas (recall) dengan kapasitas perawat 25%.
rng = np.random.default_rng(3)
n = 4000
df = pd.DataFrame({
    'umur': rng.integers(18, 92, n),
    'lama_rawat': rng.gamma(2, 2.3, n).round().clip(1),
    'jumlah_obat': rng.poisson(6, n),
    'rawat_inap_12bln': rng.poisson(0.7, n),
    'diagnosis': rng.choice(['jantung', 'diabetes', 'paru', 'bedah', 'lainnya'], n, p=[.2, .2, .15, .25, .2]),
    'hba1c': rng.normal(7.2, 1.4, n).round(1),
    'kontrol_terjadwal': rng.random(n) < 0.6,
})
logit = (-3.3 + 0.025 * (df.umur - 50) + 0.12 * df.lama_rawat + 0.06 * df.jumlah_obat + 0.55 * df.rawat_inap_12bln
         + 0.5 * df.diagnosis.isin(['jantung', 'paru']) - 0.6 * df.kontrol_terjadwal)
df['dirawat_lagi'] = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
df.loc[df.diagnosis != 'diabetes', 'hba1c'] = np.nan            # hanya diukur untuk pasien diabetes
df.loc[df.sample(30, random_state=4).index, 'umur'] = 150       # salah input

# 2) PEMBERSIHAN
df.loc[~df.umur.between(0, 110), 'umur'] = np.nan
print(f'pasien: {len(df)}, dirawat lagi: {df.dirawat_lagi.mean():.1%}, umur tidak valid: {df.umur.isna().sum()}')
df['hba1c_diukur'] = df.hba1c.notna().astype(int)              # nilai kosong yang bermakna

# 3) EDA
print('per diagnosis (%):', (df.groupby('diagnosis')['dirawat_lagi'].mean() * 100).round(1).to_dict())
print('kontrol terjadwal vs tidak (%):', (df.groupby('kontrol_terjadwal')['dirawat_lagi'].mean() * 100).round(1).to_dict())

# 4) PERSIAPAN
df['lansia'] = (df.umur >= 65).astype(float)
df['polifarmasi'] = (df.jumlah_obat >= 8).astype(int)
num = ['umur', 'lama_rawat', 'jumlah_obat', 'rawat_inap_12bln', 'hba1c', 'lansia', 'polifarmasi', 'hba1c_diukur']
X = df[num + ['diagnosis']].assign(kontrol=df.kontrol_terjadwal.astype(int))
y = df['dirawat_lagi']
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)
pra = ColumnTransformer([('num', make_pipeline(SimpleImputer(strategy='median'), StandardScaler()), num + ['kontrol']),
                         ('kat', OneHotEncoder(handle_unknown='ignore'), ['diagnosis'])])

# 5) PEMODELAN DAN EVALUASI (class_weight untuk kelas langka)
cv = StratifiedKFold(5, shuffle=True, random_state=0)
kandidat = {'logistic': LogisticRegression(max_iter=2000, class_weight='balanced'),
            'random forest': RandomForestClassifier(300, min_samples_leaf=20, class_weight='balanced', random_state=0)}
for nama, m in kandidat.items():
    s = cross_val_score(Pipeline([('pra', pra), ('m', m)]), X_tr, y_tr, cv=cv, scoring='average_precision')
    print(f'{nama:14}: PR-AUC cv {s.mean():.3f} ± {s.std():.3f}')
pipe = Pipeline([('pra', pra), ('m', kandidat['logistic'])]).fit(X_tr, y_tr)
p = pipe.predict_proba(X_te)[:, 1]
ambang = np.quantile(p, 0.75)                                    # kapasitas perawat: 25% pasien
tebak = (p >= ambang).astype(int)
print(f'uji: PR-AUC {average_precision_score(y_te, p):.3f} | sensitivitas {recall_score(y_te, tebak):.2f} | PPV {precision_score(y_te, tebak):.2f}')

# 6) KESIMPULAN BISNIS
biaya_rawat, biaya_program, efektif = 18_000_000, 350_000, 0.25
dicegah = recall_score(y_te, tebak) * y_te.sum() * efektif
neto = dicegah * biaya_rawat - tebak.sum() * biaya_program
print(f'Program untuk {tebak.sum()} pasien mencegah sekitar {dicegah:.0f} rawat ulang, hemat bersih Rp{neto:,.0f}.')
print('Catatan: model membantu prioritas, keputusan klinis tetap pada dokter; audit kinerja per kelompok umur.')
'''

KODE_K3 = r'''# main.py - Studi kasus 3: menaksir harga mobil bekas
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

# 1) PEMAHAMAN BISNIS
# Keputusan: platform jual-beli memberi "harga wajar" otomatis saat penjual memasang iklan.
# Target: harga (juta rupiah). Metrik: MAE dalam rupiah dan MAPE; target MAPE < 12%.
rng = np.random.default_rng(12)
n = 3500
merek = rng.choice(['Toyota', 'Honda', 'Daihatsu', 'Suzuki', 'Mitsubishi', 'Hyundai'], n, p=[.3, .22, .18, .12, .1, .08])
dasar = pd.Series(merek).map({'Toyota': 260, 'Honda': 250, 'Daihatsu': 180, 'Suzuki': 190, 'Mitsubishi': 270, 'Hyundai': 300}).values
df = pd.DataFrame({
    'merek': merek,
    'tahun': rng.integers(2012, 2026, n),
    'km': rng.gamma(2.5, 22_000, n).round(-2),
    'transmisi': rng.choice(['manual', 'otomatis'], n, p=[.4, .6]),
    'bahan_bakar': rng.choice(['bensin', 'diesel', 'hybrid'], n, p=[.75, .17, .08]),
    'kota': rng.choice(['Jabodetabek', 'Bandung', 'Surabaya', 'Medan', 'Makassar'], n),
})
umur = 2026 - df.tahun
harga = (dasar * 0.9 ** umur * (1 - df.km / 600_000) * np.where(df.transmisi == 'otomatis', 1.08, 1)
         * df.bahan_bakar.map({'bensin': 1, 'diesel': 1.12, 'hybrid': 1.3}).values * rng.lognormal(0, 0.08, n))
df['harga_juta'] = harga.round(1)
df.loc[df.sample(20, random_state=5).index, 'harga_juta'] = 1.0    # iklan salah ketik
df.loc[df.sample(15, random_state=6).index, 'km'] = 9_999_999

# 2) PEMBERSIHAN
df = df[(df.harga_juta > 20) & (df.km < 500_000)].copy()
print(f'iklan valid: {len(df)}, median harga: Rp{df.harga_juta.median():.0f} juta')

# 3) EDA
print('median harga per merek:', df.groupby('merek')['harga_juta'].median().round(0).sort_values().to_dict())
print('korelasi harga dengan tahun dan km:', df[['harga_juta', 'tahun', 'km']].corr()['harga_juta'].round(2).to_dict())

# 4) PERSIAPAN
df['umur_mobil'] = 2026 - df.tahun
df['km_per_tahun'] = (df.km / df.umur_mobil.clip(lower=1)).round(-2)
kat = ['merek', 'transmisi', 'bahan_bakar', 'kota']
num = ['umur_mobil', 'km', 'km_per_tahun']
X, y = df[kat + num], df['harga_juta']
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)
pra = ColumnTransformer([('kat', OneHotEncoder(handle_unknown='ignore'), kat)], remainder='passthrough')

# 5) PEMODELAN DAN EVALUASI (harga miring kanan: modelkan log harga)
cv = KFold(5, shuffle=True, random_state=0)
kandidat = {
    'baseline median': DummyRegressor(strategy='median'),
    'ridge (log)': TransformedTargetRegressor(Ridge(alpha=1.0), func=np.log, inverse_func=np.exp),
    'boosting (log)': TransformedTargetRegressor(HistGradientBoostingRegressor(max_iter=300, learning_rate=0.06, random_state=0),
                                                 func=np.log, inverse_func=np.exp),
}
skor = {}
for nama, m in kandidat.items():
    s = -cross_val_score(Pipeline([('pra', pra), ('m', m)]), X_tr, y_tr, cv=cv, scoring='neg_mean_absolute_percentage_error')
    skor[nama] = s.mean()
    print(f'{nama:16}: MAPE cv {s.mean():.1%}')
terbaik = min(skor, key=skor.get)                      # pilih dari validasi silang, bukan dari data uji
print('model terpilih:', terbaik)
final = Pipeline([('pra', pra), ('m', kandidat[terbaik])]).fit(X_tr, y_tr)
pred = final.predict(X_te)
print(f'uji: MAE Rp{mean_absolute_error(y_te, pred):.1f} juta | MAPE {mean_absolute_percentage_error(y_te, pred):.1%}')

# 6) KESIMPULAN BISNIS
contoh = pd.DataFrame([{'merek': 'Toyota', 'transmisi': 'otomatis', 'bahan_bakar': 'bensin', 'kota': 'Medan',
                        'umur_mobil': 4, 'km': 52_000, 'km_per_tahun': 13_000}])
taksir = final.predict(contoh)[0]
print(f'Contoh iklan: harga wajar Rp{taksir:.0f} juta (rentang Rp{taksir * 0.9:.0f}-{taksir * 1.1:.0f} juta).')
print('Rekomendasi: tampilkan rentang, bukan satu angka; latih ulang bulanan karena harga pasar bergeser.')
'''

KODE_K4 = r'''# main.py - Studi kasus 4: prioritas lead penjualan B2B
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import roc_auc_score

# 1) PEMAHAMAN BISNIS
# Keputusan: tim sales (kapasitas 300 demo/bulan) memilih lead mana yang dihubungi dulu.
# Target: jadi_pelanggan = 1 jika lead membeli dalam 60 hari. Metrik: konversi pada 300 lead teratas & pendapatan.
rng = np.random.default_rng(9)
n = 3000
df = pd.DataFrame({
    'sumber': rng.choice(['iklan', 'webinar', 'referensi', 'organik', 'pameran'], n, p=[.35, .15, .1, .3, .1]),
    'industri': rng.choice(['ritel', 'manufaktur', 'jasa', 'pendidikan'], n),
    'karyawan': rng.lognormal(3.5, 1.1, n).round().clip(1, 5000),
    'kunjungan_web': rng.poisson(4, n),
    'unduh_brosur': rng.random(n) < 0.3,
    'buka_email': rng.integers(0, 10, n),
    'hari_sejak_daftar': rng.integers(0, 90, n),
})
logit = (-3.2 + 0.9 * (df.sumber == 'referensi') + 0.6 * (df.sumber == 'webinar') + 0.18 * df.kunjungan_web
         + 0.7 * df.unduh_brosur + 0.12 * df.buka_email + 0.25 * np.log1p(df.karyawan) - 0.015 * df.hari_sejak_daftar)
df['jadi_pelanggan'] = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
df.loc[df.sample(60, random_state=3).index, 'sumber'] = np.nan     # form tanpa sumber

# 2) PEMBERSIHAN
df['sumber'] = df['sumber'].fillna('tidak diketahui')
df['karyawan'] = df['karyawan'].clip(upper=df['karyawan'].quantile(0.99))
print(f'lead: {len(df)}, konversi rata-rata: {df.jadi_pelanggan.mean():.1%}')

# 3) EDA
print('konversi per sumber (%):', (df.groupby('sumber')['jadi_pelanggan'].mean() * 100).round(1).sort_values(ascending=False).to_dict())
df['kel_web'] = pd.cut(df.kunjungan_web, [-1, 1, 4, 8, 50], labels=['0-1', '2-4', '5-8', '9+'])
print('konversi per kunjungan web (%):', (df.groupby('kel_web', observed=True)['jadi_pelanggan'].mean() * 100).round(1).to_dict())

# 4) PERSIAPAN
df['skor_minat'] = df.kunjungan_web + 2 * df.unduh_brosur + 0.5 * df.buka_email
df['log_karyawan'] = np.log1p(df.karyawan)
kat = ['sumber', 'industri']
num = ['log_karyawan', 'kunjungan_web', 'buka_email', 'hari_sejak_daftar', 'skor_minat']
X = df[kat + num].assign(unduh_brosur=df.unduh_brosur.astype(int))
y = df['jadi_pelanggan']
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
pra = ColumnTransformer([('kat', OneHotEncoder(handle_unknown='ignore'), kat),
                         ('num', StandardScaler(), num + ['unduh_brosur'])])

# 5) PEMODELAN DAN EVALUASI + tuning
grid = GridSearchCV(Pipeline([('pra', pra), ('m', RandomForestClassifier(random_state=0))]),
                    {'m__n_estimators': [200], 'm__max_depth': [4, 8], 'm__min_samples_leaf': [10, 30]},
                    cv=4, scoring='roc_auc')
grid.fit(X_tr, y_tr)
logit_m = Pipeline([('pra', pra), ('m', LogisticRegression(max_iter=1000))]).fit(X_tr, y_tr)
p_rf, p_lr = grid.predict_proba(X_te)[:, 1], logit_m.predict_proba(X_te)[:, 1]
print(f'random forest terbaik {grid.best_params_} AUC {roc_auc_score(y_te, p_rf):.3f}')
print(f'logistic regression AUC {roc_auc_score(y_te, p_lr):.3f}')

# 6) KESIMPULAN BISNIS
kapasitas = int(300 * len(y_te) / n)                  # porsi kapasitas untuk data uji
nilai_kontrak = 45_000_000
cv_lr = cross_val_score(logit_m, X_tr, y_tr, cv=4, scoring='roc_auc').mean()
p = p_lr if cv_lr >= grid.best_score_ else p_rf           # pilih dari validasi silang, bukan dari data uji
pilih_model = y_te.values[np.argsort(-p)[:kapasitas]]
pilih_acak = y_te.sample(kapasitas, random_state=0).values
print(f'{kapasitas} lead teratas: konversi {pilih_model.mean():.1%} vs acak {pilih_acak.mean():.1%}')
print(f'tambahan pendapatan dibanding acak: Rp{(pilih_model.sum() - pilih_acak.sum()) * nilai_kontrak:,.0f}')
print('Rekomendasi: urutkan antrean CRM dengan skor model; lead referensi dan webinar ditangani dalam 24 jam.')
'''


def KASUS(no, nama, masalah, wajib, code, kunci, cek):
    assert len(wajib) == len(ENAM)
    """Studi kasus enam langkah: kode final lengkap disembunyikan sampai pelajar menekan tombol."""
    d = MINI(no, nama, masalah, wajib, ENAM, code, 'python', run=True, kunci=kunci, cek=cek)
    d['t'] = f'Studi kasus {no}: {nama}'
    d['pts'] = [f'Studi kasus {no}: {nama}.', 'Enam langkah: bisnis, bersihkan, EDA, persiapan, model, kesimpulan.', 'Kerjakan dulu sendiri, lalu buka kode final untuk code review.']
    d['nodes'] = ['Exploratory Data Analysis', 'Machine Learning', 'Business Metrics']
    d['tb'] = [{'c': 'Enam langkah dan isinya di kasus ini', 'h': ['Langkah', 'Yang dikerjakan'],
                'r': [[e.split(':')[0], w] for e, w in zip(ENAM, wajib)]}]
    return d


STUDI_KASUS = M('Studi kasus end-to-end', 'Profesional',
  'Empat proyek lengkap dengan enam langkah yang sama seperti di tim data sungguhan: pemahaman bisnis, pembersihan, EDA, persiapan data, pemodelan dan evaluasi, lalu kesimpulan bisnis. Setiap proyek punya kode final berstandar industri yang bisa dibuka setelah mencoba sendiri.',
  ['Exploratory Data Analysis', 'Machine Learning', 'Model Evaluation', 'Business Metrics'], [
  KASUS(1, 'Memprediksi paket yang akan terlambat',
    'Perusahaan ekspedisi menanggung kompensasi Rp35.000 setiap paket terlambat. Gudang bisa memprioritaskan sortir untuk sekitar 15% paket per hari. Paket mana yang harus didahulukan?',
    ['Target telat (0/1), keputusan prioritas sortir untuk 15% paket, metrik recall@15%', 'Buang duplikat impor ulang, ubah berat timbangan yang mustahil menjadi NaN lalu isi median', 'Bandingkan keterlambatan per pulau tujuan dan saat gudang padat', 'Fitur pickup malam dan rasio jarak per berat; one-hot dan scaling di Pipeline', 'Baseline aturan vs logistic regression vs gradient boosting dengan AUC dan recall@15%', 'Hitung penghematan kompensasi dalam rupiah untuk paket yang diprioritaskan'],
    KODE_K1, 'tambahkan data cuaca per hari dan uji apakah recall@15% naik; buat dasbor harian daftar paket prioritas.',
    q('Kenapa metriknya recall@15% dan bukan akurasi?', ['Gudang hanya bisa memprioritaskan 15% paket, jadi yang penting berapa paket telat yang tertangkap di kelompok itu', 'Akurasi terlalu sulit dihitung', 'Karena data tidak punya label'], 0, 'Metrik mengikuti kapasitas operasional.')),
  KASUS(2, 'Mencegah pasien kembali dirawat dalam 30 hari',
    'Rumah sakit dikenai biaya besar setiap pasien kembali dirawat dalam 30 hari. Perawat hanya sanggup menelepon dan menjadwalkan kontrol awal untuk sekitar 25% pasien yang pulang.',
    ['Target dirawat lagi ≤ 30 hari, kapasitas perawat 25% pasien, metrik sensitivitas', 'Umur tidak valid menjadi NaN; HbA1c kosong diberi penanda karena kekosongannya bermakna', 'Bandingkan tingkat rawat ulang per diagnosis dan per status kontrol terjadwal', 'Fitur lansia dan polifarmasi; imputasi median di dalam Pipeline', 'class_weight="balanced", validasi silang dengan PR-AUC, lalu sensitivitas dan PPV di data uji', 'Hitung rawat ulang yang dicegah dan penghematan bersih, plus catatan etika klinis'],
    KODE_K2, 'ukur sensitivitas terpisah untuk pasien lansia dan non-lansia, lalu periksa apakah model adil untuk keduanya.',
    q('Kolom HbA1c kosong untuk pasien non-diabetes. Penanganan yang tepat?', ['Isi nilai tengah dan tambahkan penanda hba1c_diukur karena kekosongannya bermakna', 'Hapus semua pasien non-diabetes', 'Isi dengan 0'], 0, 'Kosong yang bermakna perlu penanda.')),
  KASUS(3, 'Menaksir harga wajar mobil bekas',
    'Platform jual-beli mobil ingin menampilkan "harga wajar" otomatis saat penjual memasang iklan, agar harga tidak terlalu tinggi (tidak laku) atau terlalu rendah (penjual rugi).',
    ['Target harga (juta rupiah) untuk fitur harga wajar, metrik MAE dan MAPE < 12%', 'Buang iklan salah ketik: harga Rp1 juta dan odometer 9.999.999 km', 'Median harga per merek dan korelasi harga dengan tahun serta km', 'Fitur umur mobil dan km per tahun; one-hot merek, transmisi, bahan bakar, kota', 'Baseline median vs Ridge vs boosting pada log harga, pilih dari validasi silang', 'Tampilkan rentang harga wajar untuk satu iklan contoh dan rencana latih ulang'],
    KODE_K3, 'tambahkan selang prediksi dengan quantile regression (HistGradientBoostingRegressor loss="quantile") sebagai pengganti ±10%.',
    q('Kenapa target harga dimodelkan dalam bentuk log?', ['Harga miring ke kanan dan galatnya cenderung sebanding dengan harga', 'Agar model lebih cepat', 'Karena harga negatif'], 0, 'Log membuat galat relatif lebih seimbang.')),
  KASUS(4, 'Memprioritaskan lead penjualan B2B',
    'Perusahaan software kasir menerima ribuan pendaftar demo setiap bulan, tetapi tim sales hanya mampu melakukan 300 demo. Lead mana yang dihubungi lebih dulu?',
    ['Target jadi pelanggan dalam 60 hari, kapasitas 300 demo per bulan, metrik konversi lead teratas', 'Sumber lead kosong menjadi "tidak diketahui", jumlah karyawan ekstrem dipotong di persentil 99', 'Konversi per sumber lead dan per tingkat kunjungan web', 'Fitur skor minat dan log jumlah karyawan; encoding dan scaling di Pipeline', 'Tuning random forest dengan GridSearchCV vs logistic regression, pilih dari validasi silang', 'Tambahan pendapatan dibanding memilih lead acak dan aturan prioritas untuk tim sales'],
    KODE_K4, 'simpan model terbaik dengan joblib lalu buat endpoint FastAPI /skor-lead yang dipanggil CRM saat lead baru masuk.',
    q('Kenapa hasil dibandingkan dengan pemilihan lead secara acak?', ['Agar terlihat tambahan nilai yang benar-benar diberikan model', 'Karena acak selalu lebih baik', 'Agar AUC naik'], 0, 'Baseline menunjukkan dampak model.')),
])

# ---------------------------------------------------------------------------
# Penempatan (dipanggil dari rb_dsci.py)
# ---------------------------------------------------------------------------
TAMBAH_DI_MODUL = {
    'Peran data scientist dan alat utamanya': [L_PYTHON, L_PANDAS_HARIAN, L_PANDAS_GABUNG],
    'Statistik dan probabilitas': [L_UJI_LANGKAH, L_KASUS_TTEST],
    'EDA dan visualisasi dengan pandas & Matplotlib': [L_EMPAT_GRAFIK, L_BERSIH, L_EDA_UNI_MULTI, L_FITUR],
    'Machine learning klasik dengan scikit-learn': [L_PERSIAPAN, L_TIDAK_SEIMBANG],
}
MODUL_BARU = [BISNIS, STUDI_KASUS]


def pasang(dsci):
    judul = {m['t']: m for m in dsci}
    for t, ls in TAMBAH_DI_MODUL.items():
        judul[t]['lessons'].extend(ls)
    dsci.extend(MODUL_BARU)

# analogi "Sekilas" ditulis tangan agar tidak salah tebak dari judul
ANALOGI = {
    'Python inti untuk data: list, dict, kondisi, loop, dan fungsi': 'List, dict, kondisi, dan loop itu seperti kasir yang memeriksa struk satu per satu: lewati yang batal, berhenti di akhir tumpukan, lalu jumlahkan per kota.',
    'pandas sehari-hari: membuat, menyimpan, mengurutkan, dan mengubah tipe': 'DataFrame itu seperti lembar kerja spreadsheet yang bisa diperintah lewat kode: diberi nama kolom yang rapi, diurutkan, lalu disimpan.',
    'Menyaring dan menggabungkan: isin, anti-join, apply, dan map': 'merge itu seperti mencocokkan daftar tamu dengan buku tamu: yang tidak pernah tanda tangan adalah hasil anti-join.',
    'Uji hipotesis langkah demi langkah: statistik uji dan nilai kritis': 'Uji hipotesis itu seperti sidang: terdakwa dianggap tidak bersalah (H0) sampai bukti cukup kuat melewati batas yang disepakati sebelumnya.',
    'Studi kasus t-test: apakah program voucher menaikkan belanja?': 'Eksperimen voucher itu seperti mencoba resep baru di separuh cabang: bandingkan hasilnya, lalu hitung apakah tambahan untung menutup biaya bahan.',
    'Empat tujuan grafik: perbandingan, distribusi, hubungan, dan komposisi': 'Memilih grafik itu seperti memilih alat dapur: pisau untuk memotong, panci untuk merebus. Setiap pertanyaan punya grafik yang paling pas.',
    'Membersihkan data: duplikat, nilai mustahil, dan outlier': 'Membersihkan data itu seperti mencuci sayur sebelum dimasak: buang yang busuk, pisahkan yang ganda, dan periksa yang ukurannya aneh.',
    'EDA univariat, bivariat, dan multivariat': 'EDA itu seperti detektif yang memeriksa satu petunjuk, lalu pasangan petunjuk, lalu seluruh papan bukti sampai polanya terlihat.',
    'Feature engineering: membuat variabel baru yang bermakna': 'Feature engineering itu seperti meracik bumbu: bahan mentah yang sama terasa jauh lebih jelas setelah diolah dengan takaran yang tepat.',
    'Peta ML dan persiapan data sebelum model': 'Persiapan data itu seperti menyiapkan bahan sebelum memasak: dicuci, dipotong seragam, dan bahan ujian tidak boleh dicicipi lebih dulu.',
    'Data tidak seimbang: class_weight, oversampling, dan metrik yang jujur': 'Data tidak seimbang itu seperti mencari jarum di tumpukan jerami: menebak "jerami" terus memang hampir selalu benar, tetapi jarumnya tidak pernah ditemukan.',
    'Metrik bisnis per industri: keuangan, pemasaran, kesehatan, logistik': 'Metrik bisnis itu seperti kurs mata uang: menerjemahkan nilai model ke bahasa yang dipahami bank, pemasar, dokter, dan kurir.',
    'Kasus churn: dari peluang ke rupiah': 'Kampanye retensi itu seperti memancing dengan umpan terbatas: tebar umpan di tempat ikannya paling banyak, bukan di seluruh danau.',
    'Kasus kredit: menentukan ambang persetujuan pinjaman': 'Ambang persetujuan itu seperti tinggi palang di pintu masuk: makin tinggi palangnya makin banyak yang masuk, termasuk yang berisiko.',
    'Menyampaikan hasil model ke pengambil keputusan': 'Presentasi model itu seperti laporan dokter ke pasien: mulai dari diagnosis dan langkah berikutnya, istilah teknis cukup di lampiran.',
    'Karier data scientist 2026-2030: peran, portofolio, dan wawancara': 'Portofolio itu seperti etalase toko: perekrut hanya melihat sebentar, jadi pajang hasil terbaik dengan label harga yang jelas.',
    'Studi kasus 1: Memprediksi paket yang akan terlambat': 'Seperti petugas sortir yang tahu paket mana yang paling mungkin terlambat, lalu menaruhnya di jalur cepat lebih dulu.',
    'Studi kasus 2: Mencegah pasien kembali dirawat dalam 30 hari': 'Seperti perawat yang menelepon lebih dulu pasien yang paling mungkin kembali ke rumah sakit, karena waktunya terbatas.',
    'Studi kasus 3: Menaksir harga wajar mobil bekas': 'Seperti penaksir di showroom: melihat merek, umur, dan odometer, lalu menyebut rentang harga yang wajar.',
    'Studi kasus 4: Memprioritaskan lead penjualan B2B': 'Seperti antrean prioritas di kantor sales: calon pembeli yang paling serius dilayani lebih dulu.',
}
for _m in [BISNIS, STUDI_KASUS] + [{'lessons': v} for v in TAMBAH_DI_MODUL.values()]:
    for _l in _m['lessons']:
        _l['an'] = ANALOGI[_l['t']]
assert len(ANALOGI) == 20
for _l in (L_TIDAK_SEIMBANG, L_KOMUNIKASI):
    _l['v3'] = None   # visual 3D otomatis dari judul tidak cocok
