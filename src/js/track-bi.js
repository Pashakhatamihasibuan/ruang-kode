/* ===================== JALUR BI ANALYST =====================
   Mengikuti roadmap.sh/bi-analyst. Pelajaran SQL memakai database bintang SEED.bi
   (db:'bi'): fakta_penjualan + dim_tanggal, dim_produk, dim_toko. */
const OMZET='f.jumlah * f.harga * (100 - f.diskon_persen) / 100';
const BI_MODULES=[
{t:'Peran BI analyst',lvl:'Pemula',d:'Apa yang dikerjakan BI analyst, bedanya dengan peran data lain, dan cara berpikir bisnis.',
 nodes:['Introduction','What is BI?','BI Analyst vs Other Roles','Responsibilities','Skills','Business Acumen','Key Business Functions','Critical Thinking'],
 lessons:[
  {k:'c',t:'BI analyst dan peran data lainnya',nodes:['What is BI?','BI Analyst vs Other Roles','Responsibilities','Skills'],lang:'text',run:false,
   b:['<b>Business Intelligence</b> (BI) mengubah data operasional menjadi informasi yang dipakai mengambil keputusan rutin: dashboard penjualan harian, laporan stok, KPI bulanan.',
      'Perbedaan peran secara kasar: <b>data analyst</b> menjawab pertanyaan ad-hoc dengan analisis; <b>BI analyst</b> membangun model data, metrik, dan dashboard yang dipakai berulang oleh banyak orang; <b>data engineer</b> membangun pipeline yang mengalirkan data; <b>data scientist</b> membuat model prediksi.',
      'Keahlian inti BI analyst: SQL, pemodelan data (skema bintang), satu alat BI (Power BI, Tableau, Looker), statistik dasar, dan yang sering dilupakan: memahami bisnis dan berkomunikasi.'],
   code:`Senin pagi seorang BI analyst
08.30  cek dashboard omzet harian: data kemarin sudah masuk?
09.00  rapat dengan tim marketing: definisi "pelanggan aktif"
10.00  tulis measure DAX "Omzet MTD" dan "Omzet bulan lalu"
13.00  investigasi: kenapa omzet Medan turun 18%?
15.00  ubah dashboard stok sesuai masukan gudang
16.30  kirim ringkasan mingguan ke manajemen`,
   pts:['BI = data menjadi keputusan rutin.','BI analyst: model data, metrik, dashboard berulang.','SQL + pemodelan + alat BI + bisnis + komunikasi.'],
   q:[['Pekerjaan paling khas BI analyst?',['Membangun dashboard dan metrik yang dipakai rutin','Melatih model deep learning','Mengelola server Kafka'],0,'Fokusnya pelaporan dan metrik berulang.']]},
  {k:'c',t:'Berpikir seperti pemilik bisnis',nodes:['Business Acumen','Key Business Functions','Critical Thinking'],lang:'text',run:false,
   b:['Angka hanya bermakna jika kamu paham cara bisnis menghasilkan uang. Pelajari fungsi utama: penjualan, pemasaran, operasional, keuangan, SDM. Setiap fungsi punya pertanyaan dan metrik berbeda.',
      'Saat diminta "laporan penjualan", tanyakan kembali: <b>keputusan apa</b> yang akan diambil? Siapa yang membaca? Seberapa sering? Jawaban itu menentukan metrik, tingkat detail, dan bentuk laporan.',
      'Berpikir kritis: periksa definisi ("omzet" kotor atau bersih?), periksa sumber, dan cari penjelasan alternatif sebelum menyimpulkan.'],
   code:`Permintaan : "Tolong buatkan laporan penjualan."
Pertanyaan balik
- Keputusan apa?   → menentukan toko yang perlu promo
- Pembaca?          → manajer area, dibuka di ponsel
- Frekuensi?        → mingguan, Senin pagi
- Definisi omzet?   → setelah diskon, sebelum pajak
Hasil      : 1 halaman, omzet per toko vs target, tren 8 minggu`,
   pts:['Pahami cara bisnis menghasilkan uang.','Tanya keputusan, pembaca, frekuensi, definisi.','Periksa definisi dan penjelasan alternatif.'],
   q:[['Pertanyaan pertama terbaik saat menerima permintaan laporan?',['Keputusan apa yang akan diambil dari laporan ini?','Warna apa yang diinginkan?','Pakai Excel atau PDF?'],0,'Keputusan menentukan isi laporan.']]}
 ]},
{t:'Metrik & KPI',lvl:'Pemula',d:'Menentukan metrik yang tepat dan menghitungnya dengan SQL.',
 nodes:['Metrics and KPIs','CLV','Cohort Analysis','Sales Performance','Financial Performance','Marketing Campaigns'],
 lessons:[
  {k:'s',db:'bi',t:'Metrik, KPI & skema bintang',nodes:['Metrics and KPIs','Sales Performance'],viz:'starschema',
   b:['<b>Metrik</b> adalah angka yang diukur (omzet, jumlah transaksi). <b>KPI</b> adalah metrik yang dipilih untuk mengukur keberhasilan tujuan tertentu, lengkap dengan target: "omzet kuartal 2 Rp 65 juta".',
      'KPI yang baik itu spesifik, terukur, bisa dipengaruhi tim, dan punya pembanding (target, periode lalu). Hindari <b>vanity metric</b> seperti jumlah unduhan tanpa melihat pengguna aktif.',
      'Database latihan jalur ini memakai <b>skema bintang</b>: tabel <code>fakta_penjualan</code> berisi angka transaksi, dikelilingi tabel dimensi <code>dim_tanggal</code>, <code>dim_produk</code>, <code>dim_toko</code>. Omzet bersih = jumlah × harga × (100 − diskon) / 100.'],
   ex:[['Isi tabel fakta','SELECT * FROM fakta_penjualan LIMIT 10;'],
       ['Omzet bersih total & jumlah transaksi',`SELECT COUNT(*) AS transaksi,\n       SUM(${OMZET}) AS omzet_bersih\nFROM fakta_penjualan f;`],
       ['Rata-rata nilai transaksi per toko',`SELECT t.nama AS toko,\n       COUNT(*) AS transaksi,\n       ROUND(AVG(${OMZET})) AS rata_transaksi\nFROM fakta_penjualan f\nJOIN dim_toko t ON t.toko_id = f.toko_id\nGROUP BY t.nama\nORDER BY rata_transaksi DESC;`]],
   task:{q:'Hitung total jumlah barang terjual (kolom total_unit) per kategori produk, urutkan dari yang terbesar.',order:true,
     a:'SELECT p.kategori, SUM(f.jumlah) AS total_unit\nFROM fakta_penjualan f JOIN dim_produk p ON p.produk_id = f.produk_id\nGROUP BY p.kategori ORDER BY total_unit DESC;'},
   pts:['KPI = metrik + tujuan + target.','Hindari vanity metric.','Fakta berisi angka; dimensi berisi konteks.'],
   q:[['Mana yang KPI?',['Omzet kuartal 2 mencapai Rp 65 juta','Jumlah pengikut Instagram','Total baris di database'],0,'Terhubung tujuan dan punya target.']]},
  {k:'s',db:'bi',t:'Pertumbuhan, margin & kontribusi',nodes:['Financial Performance','Sales Performance','Metrics and KPIs'],
   b:['Metrik turunan yang paling sering diminta: <b>pertumbuhan</b> dibanding periode lalu (month-over-month), <b>margin kotor</b> = (omzet − HPP) / omzet, dan <b>kontribusi</b> = bagian satu kelompok terhadap total.',
      'Window function membuat semuanya bisa dihitung dalam satu query: <code>LAG</code> untuk periode lalu, <code>SUM(...) OVER ()</code> untuk total keseluruhan.',
      'Selalu tampilkan angka absolut di samping persentase. "Naik 200%" bisa berarti dari 1 menjadi 3 transaksi.'],
   ex:[['Pertumbuhan omzet bulanan',`WITH b AS (\n  SELECT d.bulan, d.nama_bulan, SUM(${OMZET}) AS omzet\n  FROM fakta_penjualan f JOIN dim_tanggal d ON d.tanggal_id = f.tanggal_id\n  GROUP BY d.bulan, d.nama_bulan\n)\nSELECT nama_bulan, omzet,\n       LAG(omzet) OVER (ORDER BY bulan) AS bulan_lalu,\n       ROUND(100.0 * (omzet - LAG(omzet) OVER (ORDER BY bulan)) / LAG(omzet) OVER (ORDER BY bulan), 1) AS tumbuh_persen\nFROM b ORDER BY bulan;`],
       ['Margin kotor per produk',`SELECT p.nama,\n       SUM(${OMZET}) AS omzet,\n       SUM(f.jumlah * p.hpp) AS hpp,\n       ROUND(100.0 * (SUM(${OMZET}) - SUM(f.jumlah * p.hpp)) / SUM(${OMZET}), 1) AS margin_persen\nFROM fakta_penjualan f JOIN dim_produk p ON p.produk_id = f.produk_id\nGROUP BY p.nama ORDER BY margin_persen DESC;`],
       ['Kontribusi tiap wilayah',`SELECT t.wilayah, SUM(${OMZET}) AS omzet,\n       ROUND(100.0 * SUM(${OMZET}) / SUM(SUM(${OMZET})) OVER (), 1) AS kontribusi_persen\nFROM fakta_penjualan f JOIN dim_toko t ON t.toko_id = f.toko_id\nGROUP BY t.wilayah ORDER BY omzet DESC;`]],
   task:{q:'Tampilkan kuartal dan jumlah transaksi (kolom transaksi) per kuartal dari dim_tanggal, urut kuartal.',order:true,
     a:'SELECT d.kuartal, COUNT(*) AS transaksi\nFROM fakta_penjualan f JOIN dim_tanggal d ON d.tanggal_id = f.tanggal_id\nGROUP BY d.kuartal ORDER BY d.kuartal;'},
   pts:['MoM: LAG(...) OVER (ORDER BY periode).','Margin = (omzet − HPP) / omzet.','Kontribusi: SUM(x) / SUM(SUM(x)) OVER ().','Persentase selalu dengan angka absolut.'],
   q:[['Fungsi untuk mengambil nilai periode sebelumnya?',['LAG','LEAD','RANK'],0,'LEAD mengambil periode berikutnya.']]},
  {k:'c',t:'CLV & analisis kohort',nodes:['CLV','Cohort Analysis','Marketing Campaigns'],lang:'sql',run:false,
   b:['<b>Customer Lifetime Value</b> (CLV) memperkirakan total keuntungan dari satu pelanggan selama hubungannya: rata-rata nilai pesanan × frekuensi per tahun × lama bertahan × margin. CLV menentukan berapa biaya akuisisi (CAC) yang masih masuk akal.',
      '<b>Analisis kohort</b> mengelompokkan pelanggan menurut bulan pertama mereka membeli, lalu melacak berapa persen yang kembali di bulan ke-1, ke-2, dan seterusnya. Hasilnya tabel segitiga yang memperlihatkan apakah retensi membaik.',
      'Kohort lebih jujur daripada angka total: pertumbuhan pengguna baru bisa menyembunyikan retensi yang memburuk.'],
   code:`-- kohort berdasarkan bulan pembelian pertama (PostgreSQL)
WITH pertama AS (
  SELECT pelanggan_id, DATE_TRUNC('month', MIN(tanggal)) AS kohort
  FROM pesanan GROUP BY pelanggan_id
)
SELECT p.kohort,
       DATE_PART('month', AGE(DATE_TRUNC('month', o.tanggal), p.kohort)) AS bulan_ke,
       COUNT(DISTINCT o.pelanggan_id) AS pelanggan
FROM pesanan o JOIN pertama p USING (pelanggan_id)
GROUP BY 1, 2 ORDER BY 1, 2;

kohort   bulan_ke 0  1    2    3
Jan      100%       38%  29%  25%
Feb      100%       41%  33%
Mar      100%       45%`,
   pts:['CLV ≈ nilai pesanan × frekuensi × lama × margin.','CLV dibanding CAC menentukan anggaran akuisisi.','Kohort: retensi per bulan bergabung.'],
   q:[['Dari tabel kohort, apa kesimpulannya?',['Retensi bulan ke-1 membaik dari Jan ke Mar','Retensi memburuk','Pelanggan Mar paling sedikit'],0,'38% → 41% → 45%.']]}
 ]},
{t:'Statistik untuk BI',lvl:'Menengah',d:'Statistik deskriptif dan inferensial yang dipakai sehari-hari di laporan.',
 nodes:['Descriptive Statistics','Central Tendency','Dispersion','Distribution','Inferential Statistics','Population & Sample','Hypothesis Testing','p-value','Confidence Intervals','Correlation vs Causation','A/B Testing','Seasonality','Forecasting'],
 lessons:[
  {k:'see',ref:'pda:Pemusatan & sebaran'},{k:'see',ref:'pda:Outlier: IQR & z-score'},{k:'see',ref:'pda:Korelasi'},
  {k:'c',t:'Sampel, p-value & selang kepercayaan',nodes:['Inferential Statistics','Population & Sample','Hypothesis Testing','p-value','Confidence Intervals','A/B Testing'],lang:'text',run:false,viz:'abtest',
   b:['Kita jarang punya data seluruh <b>populasi</b>; kita punya <b>sampel</b>. Statistik inferensial menaksir populasi dari sampel, lengkap dengan ketidakpastiannya.',
      '<b>Selang kepercayaan 95%</b>: jika pengambilan sampel diulang berkali-kali, 95% selang yang dihitung akan memuat nilai sebenarnya. Laporkan "konversi 12,9% (11,9–13,9%)" alih-alih hanya 12,9%.',
      '<b>p-value</b> adalah peluang melihat perbedaan sebesar ini atau lebih jika sebenarnya tidak ada perbedaan. p kecil (misalnya &lt; 0,05) berarti perbedaannya kecil kemungkinan kebetulan, bukan berarti efeknya besar.'],
   code:`Uji promo ongkir gratis (A/B)
         pengunjung  beli   konversi   CI 95%
A        4.000       448    11,2%      10,2–12,2%
B        4.000       516    12,9%      11,9–13,9%
Selisih +1,7 poin, p = 0,02 → signifikan pada α = 0,05`,
   pts:['Sampel → taksiran populasi + ketidakpastian.','Laporkan selang kepercayaan.','p-value kecil ≠ efek besar.'],
   q:[['p = 0,30 pada uji A/B berarti?',['Belum ada bukti cukup bahwa versi berbeda','B pasti lebih buruk','Efeknya 30%'],0,'Perbedaan masih wajar terjadi karena kebetulan.']]},
  {k:'s',db:'bi',t:'Musiman & peramalan sederhana',nodes:['Seasonality','Forecasting','Correlation vs Causation'],
   b:['Banyak bisnis punya pola <b>musiman</b>: penjualan naik menjelang Lebaran, akhir tahun, atau tanggal gajian. Bandingkan dengan periode yang sama tahun lalu (year-over-year) agar tidak salah membaca kenaikan musiman sebagai pertumbuhan.',
      '<b>Rata-rata bergerak</b> (moving average) menghaluskan fluktuasi dan menjadi dasar peramalan paling sederhana. Di SQL: <code>AVG(x) OVER (ORDER BY periode ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)</code>.',
      'Untuk peramalan serius gunakan model deret waktu (ETS, ARIMA, Prophet) yang sudah tersedia di Power BI dan Tableau.'],
   ex:[['Rata-rata bergerak 3 bulan',`WITH b AS (\n  SELECT d.bulan, d.nama_bulan, SUM(${OMZET}) AS omzet\n  FROM fakta_penjualan f JOIN dim_tanggal d ON d.tanggal_id = f.tanggal_id\n  GROUP BY d.bulan, d.nama_bulan\n)\nSELECT nama_bulan, omzet,\n       ROUND(AVG(omzet) OVER (ORDER BY bulan ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)) AS ma3\nFROM b ORDER BY bulan;`],
       ['Omzet per hari dalam minggu',`SELECT d.hari, COUNT(*) AS transaksi, SUM(${OMZET}) AS omzet\nFROM fakta_penjualan f JOIN dim_tanggal d ON d.tanggal_id = f.tanggal_id\nGROUP BY d.hari ORDER BY omzet DESC;`]],
   task:{q:'Hitung total unit Kopi Gayo per bulan (kolom bulan dan unit), urut bulan. Apakah ada tren?',order:true,
     a:"SELECT d.bulan, SUM(f.jumlah) AS unit\nFROM fakta_penjualan f\nJOIN dim_tanggal d ON d.tanggal_id = f.tanggal_id\nJOIN dim_produk p ON p.produk_id = f.produk_id\nWHERE p.nama = 'Kopi Gayo'\nGROUP BY d.bulan ORDER BY d.bulan;"},
   pts:['Bandingkan YoY untuk data musiman.','Moving average menghaluskan tren.','Model deret waktu untuk ramalan serius.'],
   q:[['Omzet Desember naik 40% dari November. Kesimpulan yang hati-hati?',['Bandingkan dulu dengan Desember tahun lalu','Bisnis pasti tumbuh 40%','Turunkan target'],0,'Bisa jadi efek musiman.']]}
 ]},
{t:'Data, gudang & pemodelan',lvl:'Menengah',d:'Sumber data, kualitas data, data warehouse, skema bintang, dan ETL.',
 nodes:['Data Sources','Databases','CSV','JSON','APIs','Data Formats','Data Quality','Accuracy','Duplicates','Missing Values','Outliers','Data Warehouse','Data Lake','Data Mart','Data Modeling for BI','Fact vs Dimension Tables','Star vs Snowflake Schema','Normalization vs Denormalization','ETL Basics','ETL Tools','dbt','Data Lineage'],
 lessons:[
  {k:'s',db:'bi',t:'Tabel fakta & dimensi',nodes:['Data Modeling for BI','Fact vs Dimension Tables','Star vs Snowflake Schema','Normalization vs Denormalization','Data Mart'],viz:'starschema',
   b:['<b>Tabel fakta</b> menyimpan peristiwa yang diukur (setiap baris penjualan) dengan angka dan kunci ke dimensi. <b>Tabel dimensi</b> menyimpan konteks deskriptif: kapan, apa, di mana, siapa.',
      '<b>Skema bintang</b> menghubungkan fakta langsung ke dimensi yang didenormalisasi (kota dan wilayah ada di satu tabel toko). <b>Skema snowflake</b> menormalisasi dimensi lebih lanjut (tabel kota terpisah), lebih hemat ruang tetapi query lebih rumit. Alat BI seperti Power BI bekerja paling baik dengan skema bintang.',
      'Tentukan <b>grain</b> (butir) fakta lebih dulu: "satu baris = satu produk dalam satu transaksi di satu toko per hari". Semua angka di fakta harus sesuai grain itu.'],
   ex:[['Bentuk dimensi toko','SELECT * FROM dim_toko;'],
       ['Query bintang: wilayah x kategori',`SELECT t.wilayah, p.kategori, SUM(${OMZET}) AS omzet\nFROM fakta_penjualan f\nJOIN dim_toko t ON t.toko_id = f.toko_id\nJOIN dim_produk p ON p.produk_id = f.produk_id\nGROUP BY t.wilayah, p.kategori\nORDER BY t.wilayah, omzet DESC;`]],
   task:{q:'Tampilkan nama toko dan omzet bersih (kolom omzet) hanya untuk kuartal 2, urutkan dari terbesar.',order:true,
     a:`SELECT t.nama, SUM(${OMZET}) AS omzet\nFROM fakta_penjualan f\nJOIN dim_toko t ON t.toko_id = f.toko_id\nJOIN dim_tanggal d ON d.tanggal_id = f.tanggal_id\nWHERE d.kuartal = 2\nGROUP BY t.nama ORDER BY omzet DESC;`},
   pts:['Fakta = angka peristiwa; dimensi = konteks.','Bintang: dimensi didenormalisasi; snowflake: dinormalisasi.','Tetapkan grain sebelum membangun fakta.'],
   q:[['Kolom "wilayah" sebaiknya disimpan di?',['Dimensi toko','Tabel fakta','Dimensi tanggal'],0,'Atribut deskriptif toko.']]},
  {k:'s',db:'bi',t:'Memeriksa kualitas data',nodes:['Data Quality','Accuracy','Duplicates','Missing Values','Outliers'],
   b:['Dashboard yang bagus dengan data salah lebih berbahaya daripada tidak ada dashboard. Periksa enam dimensi kualitas: <b>kelengkapan</b>, <b>keunikan</b>, <b>validitas</b> (nilai di rentang wajar), <b>konsistensi</b> antar sistem, <b>akurasi</b>, dan <b>ketepatan waktu</b>.',
      'Jadikan pemeriksaan ini query rutin (atau tes dbt) yang berjalan sebelum dashboard diperbarui.',
      'Jalankan contoh di bawah: periksa baris tanpa pasangan dimensi, diskon di luar rentang, dan kunci ganda.'],
   ex:[['Fakta tanpa dimensi (orphan)','SELECT COUNT(*) AS tanpa_produk\nFROM fakta_penjualan f LEFT JOIN dim_produk p ON p.produk_id = f.produk_id\nWHERE p.produk_id IS NULL;'],
       ['Nilai di luar rentang wajar','SELECT COUNT(*) AS aneh FROM fakta_penjualan\nWHERE jumlah <= 0 OR diskon_persen NOT BETWEEN 0 AND 50;'],
       ['Harga transaksi beda dari harga katalog','SELECT p.nama, f.harga AS harga_trx, p.harga AS harga_katalog, COUNT(*) AS n\nFROM fakta_penjualan f JOIN dim_produk p ON p.produk_id = f.produk_id\nWHERE f.harga <> p.harga GROUP BY p.nama, f.harga, p.harga;']],
   task:{q:'Periksa keunikan: tampilkan tanggal_id, produk_id, toko_id yang muncul lebih dari sekali di fakta_penjualan beserta jumlahnya (kolom n).',
     a:'SELECT tanggal_id, produk_id, toko_id, COUNT(*) AS n\nFROM fakta_penjualan\nGROUP BY tanggal_id, produk_id, toko_id\nHAVING COUNT(*) > 1;'},
   pts:['Kelengkapan, keunikan, validitas, konsistensi, akurasi, ketepatan waktu.','Jadikan pemeriksaan query rutin atau tes dbt.','Orphan = fakta tanpa pasangan dimensi.'],
   q:[['LEFT JOIN ... WHERE kanan IS NULL dipakai untuk?',['Mencari baris tanpa pasangan','Menghapus duplikat','Mengurutkan'],0,'Teknik standar mencari orphan.']]},
  {k:'c',t:'Warehouse, lake & ETL',nodes:['Data Warehouse','Data Lake','ETL Basics','ETL Tools','dbt','Data Lineage','Data Sources','Data Formats'],lang:'sql',run:false,viz:'etl',
   b:['<b>Data warehouse</b> (BigQuery, Snowflake, Redshift) menyimpan data terstruktur yang sudah dibersihkan untuk analitik. <b>Data lake</b> menyimpan data mentah dalam berbagai format dengan biaya murah. <b>Data mart</b> adalah potongan warehouse untuk satu departemen.',
      '<b>ETL</b> (extract, transform, load) mengambil data dari sumber, membersihkan, lalu memuat ke warehouse. Pola modern <b>ELT</b> memuat mentah dulu lalu mentransformasi di dalam warehouse dengan SQL, sering memakai <b>dbt</b>.',
      'dbt membuat setiap transformasi berupa berkas SELECT yang diberi versi di Git, diuji, dan terdokumentasi, sekaligus menggambar <b>lineage</b>: dari tabel mana sebuah angka berasal.'],
   code:`-- models/marts/fakta_penjualan.sql (dbt)
SELECT
    d.tanggal_id,
    t.produk_id,
    t.toko_id,
    t.jumlah,
    t.harga,
    COALESCE(t.diskon_persen, 0) AS diskon_persen
FROM {{ ref('stg_transaksi') }} t
JOIN {{ ref('dim_tanggal') }} d ON d.tanggal = t.tanggal
WHERE t.status = 'selesai'

-- models/marts/schema.yml
-- columns: produk_id → tests: [not_null, relationships: dim_produk]`,
   pts:['Warehouse terstruktur; lake mentah; mart per departemen.','ETL vs ELT; ELT dengan dbt populer.','dbt: SQL berversi, diuji, lineage otomatis.'],
   q:[['Dalam ELT, transformasi dilakukan di?',['Dalam warehouse setelah data dimuat','Sebelum data diambil','Di dashboard'],0,'Warehouse modern cukup kuat untuk transformasi.']]}
 ]},
{t:'SQL untuk BI',lvl:'Menengah',d:'Bagian jalur SQL yang paling sering dipakai BI analyst.',nodes:['Basic Queries','Advanced Queries'],
 lessons:[
  {k:'see',ref:'sql:GROUP BY'},{k:'see',ref:'sql:HAVING'},{k:'see',ref:'sql:JOIN banyak tabel'},{k:'see',ref:'sql:CASE, COALESCE & NULLIF'},
  {k:'see',ref:'sql:CTE: WITH'},{k:'see',ref:'sql:Window function: ROW_NUMBER, RANK, DENSE_RANK'},{k:'see',ref:'sql:LEAD, LAG & running total'}
 ]},
{t:'Visualisasi & dashboard',lvl:'Lanjutan',d:'Memilih grafik, merancang dashboard, dan bercerita dengan data.',
 nodes:['Chart Categories','Barplot','Lineplot','Scatterplot','Histogram','Heatmap','Map','Dashboard Design','Design Principles','Color Theory','Misleading Charts','Accessibility','Mobile Responsiveness','Communication & Storytelling','Presentation Design'],
 lessons:[
  {k:'see',ref:'pda:Memilih grafik yang tepat'},
  {k:'c',t:'Merancang dashboard',nodes:['Dashboard Design','Design Principles','Color Theory','Accessibility','Mobile Responsiveness'],lang:'text',run:false,
   b:['Dashboard dibaca seperti koran: pojok kiri atas paling dilihat. Taruh 3-5 <b>KPI utama</b> berupa angka besar dengan pembanding (vs target, vs periode lalu) di atas, tren di tengah, rincian di bawah.',
      'Satu dashboard, satu audiens, satu tujuan. Batasi warna: abu-abu untuk konteks, satu warna aksen untuk yang perlu diperhatikan, merah/hijau hanya untuk status dan selalu disertai ikon atau teks untuk pembaca buta warna.',
      'Banyak manajer membuka dashboard dari ponsel; buat tata letak ponsel di Power BI atau Tableau.'],
   code:`┌───────────────┬───────────────┬───────────────┬──────────────┐
│ Omzet bulan ini│ vs target     │ Margin kotor  │ Transaksi    │
│ Rp 21,5 jt    │ 96% ▼         │ 38,4%         │ 45           │
├───────────────┴───────────────┴───────────────┴──────────────┤
│ Tren omzet 6 bulan (garis) + garis target                    │
├──────────────────────────────┬───────────────────────────────┤
│ Omzet per toko (batang)      │ Produk dengan margin terendah │
└──────────────────────────────┴───────────────────────────────┘
Filter: periode · wilayah            Diperbarui: 30/10/2026 06.00`,
   pts:['KPI di atas, tren di tengah, rincian di bawah.','Satu audiens, satu tujuan.','Warna hemat; status tidak hanya dengan warna.','Sediakan tata letak ponsel.'],
   q:[['Di mana KPI terpenting diletakkan?',['Kiri atas','Kanan bawah','Di halaman kedua'],0,'Pola baca F/Z dimulai dari kiri atas.']]},
  {k:'c',t:'Grafik menyesatkan & bercerita dengan data',nodes:['Misleading Charts','Communication & Storytelling','Presentation Design'],lang:'text',run:false,
   b:['Grafik menyesatkan yang sering muncul: sumbu Y batang tidak dimulai dari nol, sumbu ganda dengan skala dipilih seenaknya, pie dengan 9 irisan, efek 3D, dan periode dipilih untuk menyembunyikan penurunan.',
      'Bercerita dengan data mengikuti pola: <b>konteks</b> (apa yang terjadi), <b>temuan</b> (satu insight utama), <b>implikasi</b> (kenapa penting), <b>rekomendasi</b> (apa yang harus dilakukan). Judul grafik menyatakan kesimpulan, bukan sekadar nama metrik.',
      'Sesuaikan kedalaman dengan audiens: direksi butuh kesimpulan dan pilihan keputusan; tim operasional butuh rincian.'],
   code:`Judul lemah : "Omzet per toko, Jan–Jun 2024"
Judul kuat  : "Toko Medan tumbuh 45% di Q2 setelah promo ongkir,
               Online turun 23%"

Konteks     : promo ongkir hanya di toko fisik sejak April
Temuan      : sebagian pembeli online pindah ke toko fisik
Implikasi   : biaya promo menggerus margin tanpa menambah pembeli
Rekomendasi : uji promo yang sama untuk kanal online selama 4 minggu`,
   pts:['Waspadai sumbu terpotong, sumbu ganda, 3D, pie berlebihan.','Konteks → temuan → implikasi → rekomendasi.','Judul grafik = kesimpulan.'],
   q:[['Grafik batang dengan sumbu Y mulai dari 90 berbahaya karena?',['Perbedaan kecil terlihat sangat besar','Lebih sulit dibuat','Warnanya berubah'],0,'Panjang batang harus sebanding dengan nilai.']]}
 ]},
{t:'Alat BI & cloud',lvl:'Lanjutan',d:'Power BI, Tableau, Looker, dan ekosistem cloud.',
 nodes:['BI Platforms','Power BI','Tableau','Looker','Qlik','Calculated Fields & Measures','Excel','Cloud Data Warehouses','Cloud BI Ecosystem','Providers: AWS, GCP, Azure'],
 lessons:[
  {k:'c',t:'Power BI, Tableau & Looker',nodes:['BI Platforms','Power BI','Tableau','Looker','Qlik','Calculated Fields & Measures','Excel'],lang:'text',run:false,
   b:['<b>Power BI</b> (Microsoft) paling banyak dipakai di perusahaan Indonesia karena terintegrasi dengan Excel dan Microsoft 365. Rumusnya memakai <b>DAX</b>. <b>Tableau</b> unggul dalam eksplorasi visual. <b>Looker</b> (Google) memakai lapisan semantik LookML yang didefinisikan sebagai kode.',
      'Konsep yang sama di semua alat: model data (relasi fakta-dimensi), <b>measure</b> (perhitungan yang mengikuti filter, misalnya total omzet), dan <b>calculated column</b> (dihitung per baris saat data dimuat).',
      'Kesalahan umum pemula: menghitung rata-rata dari persentase, atau membuat measure di kolom alih-alih di measure sehingga hasil tidak mengikuti filter.'],
   code:`-- DAX (Power BI)
Omzet Bersih =
SUMX ( fakta_penjualan,
       fakta_penjualan[jumlah] * fakta_penjualan[harga]
       * ( 100 - fakta_penjualan[diskon_persen] ) / 100 )

Omzet Bulan Lalu =
CALCULATE ( [Omzet Bersih], DATEADD ( dim_tanggal[tanggal], -1, MONTH ) )

Tumbuh MoM % =
DIVIDE ( [Omzet Bersih] - [Omzet Bulan Lalu], [Omzet Bulan Lalu] )`,
   pts:['Power BI (DAX), Tableau, Looker (LookML).','Measure mengikuti filter; calculated column per baris.','Hati-hati merata-ratakan persentase.'],
   q:[['Total omzet yang berubah saat pengguna memilih filter wilayah sebaiknya dibuat sebagai?',['Measure','Calculated column','Tabel baru'],0,'Measure dihitung ulang sesuai konteks filter.']]}
 ]},
{t:'Etika, privasi & karier',lvl:'Profesional',d:'Penggunaan data yang bertanggung jawab, regulasi, dan persiapan kerja.',
 nodes:['Ethical Data Use','Privacy','GDPR','CCPA','Bias Recognition','Algorithmic Bias','Building Your Portfolio','Interview Preparation','Certifications','Networking','Change Management'],
 lessons:[
  {k:'c',t:'Privasi data & UU PDP',nodes:['Ethical Data Use','Privacy','GDPR','CCPA','Bias Recognition','Algorithmic Bias'],lang:'text',run:false,
   b:['Di Indonesia, <b>UU Perlindungan Data Pribadi (UU 27/2022)</b> berlaku penuh sejak Oktober 2024. Prinsipnya mirip GDPR Eropa: data dikumpulkan seperlunya, untuk tujuan jelas, dengan persetujuan yang bisa ditarik, dan kebocoran wajib dilaporkan dalam 3×24 jam.',
      'Praktik BI yang bertanggung jawab: dashboard menampilkan data agregat, bukan nama dan nomor telepon; akses dibatasi per peran (row-level security); data pribadi disamarkan di lingkungan pengembangan.',
      'Waspadai bias: data historis bisa mencerminkan ketidakadilan masa lalu, dan metrik yang dipilih bisa merugikan kelompok tertentu.'],
   code:`Sebelum                                Sesudah
Dashboard CS: nama, HP, alamat lengkap  ID pelanggan + kota
Semua staf melihat semua wilayah        Row-level security per wilayah
Salinan produksi di laptop analis       Data dev disamarkan (masking)
Data disimpan selamanya                 Retensi 24 bulan, lalu dihapus`,
   pts:['UU PDP: seperlunya, bertujuan, persetujuan, laporan kebocoran 3×24 jam.','Agregat, akses per peran, masking.','Periksa bias data dan metrik.'],
   q:[['Cara membatasi manajer hanya melihat data wilayahnya di Power BI?',['Row-level security','Menyembunyikan halaman','Mengirim PDF'],0,'RLS menyaring data per pengguna.']]},
  {k:'c',t:'Portofolio & wawancara BI',nodes:['Building Your Portfolio','Interview Preparation','Certifications','Networking'],lang:'text',run:false,
   b:['Portofolio BI yang meyakinkan berisi 2-3 proyek ujung-ke-ujung: pertanyaan bisnis, sumber data, model data, dashboard (tautan publik Tableau Public atau Power BI), dan ringkasan rekomendasi.',
      'Wawancara biasanya terdiri dari tes SQL (JOIN, GROUP BY, window function), studi kasus ("omzet turun 15%, apa yang kamu periksa?"), dan presentasi dashboard.',
      'Sertifikasi yang dikenal: Microsoft PL-300 (Power BI Data Analyst), Tableau Desktop Specialist, dan Google Data Analytics.'],
   code:`Kerangka studi kasus "omzet turun 15%"
1. Validasi data: apakah pipeline terlambat? definisi berubah?
2. Pecah metrik: omzet = transaksi × nilai rata-rata
3. Segmentasi: wilayah, kanal, produk, pelanggan baru/lama
4. Waktu: mulai kapan? musiman? ada peristiwa (libur, harga naik)?
5. Hipotesis → data pendukung → rekomendasi`,
   pts:['2-3 proyek ujung-ke-ujung dengan tautan publik.','Tes SQL + studi kasus + presentasi.','PL-300, Tableau Specialist, Google Data Analytics.'],
   q:[['Langkah pertama saat KPI turun tajam?',['Pastikan datanya benar dan definisinya tidak berubah','Langsung lapor ke direksi','Ubah target'],0,'Banyak "penurunan" ternyata masalah data.']]}
 ]},
{t:'Proyek akhir',lvl:'Profesional',d:'Proyek BI ujung-ke-ujung dari model data sampai rekomendasi.',nodes:['End-to-end Analytics Project'],
 lessons:[
  {k:'proj',t:'Dashboard kinerja penjualan semester 1',stack:'SQL + Power BI/Tableau',
   brief:'Manajemen Toko Nusantara ingin tahu toko dan produk mana yang mendorong pertumbuhan semester 1 2024, dan di mana margin tergerus diskon. Bangun model data, metrik, dan dashboard satu halaman beserta rekomendasi.',
   feats:['Dokumen definisi metrik: omzet bersih, margin, MoM, kontribusi','Query SQL untuk setiap metrik dari skema bintang','Pemeriksaan kualitas data sebelum dashboard','4 KPI dengan pembanding di bagian atas','Tren bulanan dengan moving average','Matriks toko x kategori dengan margin','Tata letak versi ponsel','Ringkasan 5 kalimat: konteks, temuan, implikasi, rekomendasi'],
   steps:['Definisikan metrik bersama pemangku kepentingan.','Tulis query dan uji kualitas data.','Bangun model di alat BI dan buat measure.','Susun dashboard, minta masukan, perbaiki.','Tulis ringkasan dan presentasikan.'],
   files:[['metrik.sql','sql',`-- KPI ringkas semester 1
WITH f AS (
  SELECT f.*, d.bulan, d.kuartal, t.wilayah, p.kategori, p.hpp,
         ${OMZET} AS omzet
  FROM fakta_penjualan f
  JOIN dim_tanggal d ON d.tanggal_id = f.tanggal_id
  JOIN dim_toko t    ON t.toko_id    = f.toko_id
  JOIN dim_produk p  ON p.produk_id  = f.produk_id
)
SELECT kuartal,
       SUM(omzet) AS omzet,
       ROUND(100.0 * (SUM(omzet) - SUM(jumlah * hpp)) / SUM(omzet), 1) AS margin_persen,
       COUNT(*) AS transaksi
FROM f GROUP BY kuartal ORDER BY kuartal;`]],
   sql:{db:'bi',file:0}}
 ]}
];
