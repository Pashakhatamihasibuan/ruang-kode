# Ruang Kode: akademi coding, data & desain

Akademi teknologi visual berbahasa Indonesia dengan 16 jalur belajar, seperti LMS bootcamp. Kurikulum setiap jalur mengikuti [roadmap.sh](https://roadmap.sh).

Dikembangkan oleh **Pasha Khatami Hasibuan**.

**Versi online: https://ruang-kode-nine.vercel.app**

Bisa juga dibuka langsung dari `index.html` di browser. Tidak perlu instalasi atau server. Setiap push ke `main` otomatis di-deploy ulang ke Vercel.

## Jalur belajar

| Kategori | Jalur (roadmap.sh) |
|---|---|
| Pemrograman | Java, Python, TypeScript |
| Web & Frontend | Frontend Pemula, HTML, CSS, Frontend, React |
| Data | SQL, Python Analisis Data, Data Analyst, BI Analyst, Data Engineer |
| Desain | UX Design, Design System |
| Alat kerja | Git & GitHub |

Lima jalur karier menyusun jalur di atas dalam urutan yang disarankan: Frontend Developer, Data Analyst, Data Engineer, UI/UX Designer, dan Backend Java. Pelajaran yang sama di beberapa jalur hanya perlu dikerjakan sekali; progresnya dipakai bersama.

## Fitur

- **Navigasi**: menu Katalog per kategori, pencarian `Ctrl+K` (jalur, modul, pelajaran, istilah), tema terang/gelap/sistem, menu laci di ponsel.
- **Beranda**: dashboard untuk pengguna yang kembali (lanjutkan belajar, target harian, hari beruntun, XP, soal yang perlu diulang), jalur karier, dan katalog.
- **Halaman jalur**: tes penempatan, peta modul, ujian modul (lulus nilai 70), proyek akhir, dan sertifikat.
- **Jenis pelajaran**:
  - konsep dengan contoh kode yang sudah diuji (Java 21, Python 3.13 + pandas, Node 22 untuk TypeScript), tombol Jalankan, dan latihan "tebak keluaran";
  - contoh Python bisa diedit dan dijalankan di browser dengan Pyodide (butuh internet; di versi Artifact yang membatasi unduhan, kode asli tetap menampilkan keluaran terverifikasi);
  - praktik langsung HTML, CSS, JavaScript, dan React dengan pratinjau, konsol, dan tantangan yang diperiksa otomatis;
  - praktik SQL di konsol browser, termasuk database skema bintang untuk BI dan proyek mini dengan beberapa tantangan;
  - proyek akhir dengan daftar fitur, langkah kerja, berkas awal, dan pratinjau;
  - topik lima langkah dan lab interaktif Java/Python.
- **45 visual interaktif**, antara lain box model, flexbox, grid, event loop JavaScript, CSR/SSR/SSG, simulator Git, skema bintang, A/B test, MapReduce, Kafka, model Fogg, siklus Hook, token desain, pemeriksa kontras, dan skala tipografi.
- **Belajar saya**: kalender aktivitas, target harian, nilai ujian, nama untuk sertifikat, cadangan dan pemulihan progres.
- **Ulang**: setiap jawaban kuis atau ujian yang salah masuk daftar ulang sampai dijawab benar.
- **Kuis cerita** dan **glosarium**.

Progres tersimpan di `localStorage` browser.

## Struktur kode

`index.html` dihasilkan oleh `python3 build.py` dari folder `src/`:

- `src/css/base.css`, `lms.css`, `v4.css`: tampilan.
- `src/js/data.js`: bab, topik, glosarium, kuis cerita.
- `src/js/track-*.js`: kurikulum per jalur. `track-pda.js`, `track-da.js`, dan `track-de.js` dihasilkan skrip yang menjalankan setiap contoh Python untuk mengisi keluarannya.
- `src/js/sqlengine.js`, `sqldata.js`, `sqldata-bi.js`: mesin SQL kecil dan database contoh.
- `src/js/viz.js`, `viz2.js`, `viz3.js`: visualisasi.
- `src/js/app*.js`: data jalur dan progres, halaman, ruang pelajaran, navigasi dan rute.

## Mini project

Solusi Java (`Main.java`) dan Python (`main.py`) ada di folder [`mini-project/`](mini-project/). Semuanya sudah dikompilasi dan dijalankan. Keluaran di README tiap folder adalah hasil eksekusi aslinya.

| Topik | Project |
|---|---|
| 1.1 | [Kartu nama digital](mini-project/01-1-kartu-nama-digital/) |
| 1.2 | [Lirik lagu dengan reff](mini-project/01-2-lirik-lagu-dengan-reff/) |
| 2.1 | [Struk belanja](mini-project/02-1-struk-belanja/) |
| 2.2 | [Konversi detik ke jam](mini-project/02-2-konversi-detik-ke-jam/) |
| 2.3 | [Tabel perkalian](mini-project/02-3-tabel-perkalian/) |
| 2.4 | [Segitiga angka](mini-project/02-4-segitiga-angka/) |
| 3.1 | [Kalkulator BMI](mini-project/03-1-kalkulator-bmi/) |
| 3.2 | [Pembuat inisial](mini-project/03-2-pembuat-inisial/) |
| 3.3 | [Kalkulator umur](mini-project/03-3-kalkulator-umur/) |
| 4.1 | [Konversi nilai ke huruf](mini-project/04-1-konversi-nilai-ke-huruf/) |
| 4.2 | [Statistik nilai kelas](mini-project/04-2-statistik-nilai-kelas/) |
| 5.1 | [Target tabungan](mini-project/05-1-target-tabungan/) |
| 5.2 | [Pengecek tahun kabisat](mini-project/05-2-pengecek-tahun-kabisat/) |
| 5.3 | [Cetak daftar rapi](mini-project/05-3-cetak-daftar-rapi/) |
| 6.1 | [Rapor dari file](mini-project/06-1-rapor-dari-file/) |
| 6.2 | [Penjumlah data kotor](mini-project/06-2-penjumlah-data-kotor/) |
| 7.1 | [Suhu seminggu](mini-project/07-1-suhu-seminggu/) |
| 7.2 | [Di atas rata-rata](mini-project/07-2-di-atas-rata-rata/) |
| 7.3 | [Diskon yang menular](mini-project/07-3-diskon-yang-menular/) |
| 8.1 | [Rak buku](mini-project/08-1-rak-buku/) |
| 8.2 | [Rekening bank aman](mini-project/08-2-rekening-bank-aman/) |
| 9.1 | [Kebun binatang](mini-project/09-1-kebun-binatang/) |
| 9.2 | [Kalkulator luas bangun](mini-project/09-2-kalkulator-luas-bangun/) |
| 10.1 | [Daftar belanja](mini-project/10-1-daftar-belanja/) |
| 10.2 | [Saring nama pendek](mini-project/10-2-saring-nama-pendek/) |
| 11.1 | [Kata unik dalam kalimat](mini-project/11-1-kata-unik-dalam-kalimat/) |
| 11.2 | [Hitung suara voting](mini-project/11-2-hitung-suara-voting/) |
| 12.1 | [Pangkat rekursif](mini-project/12-1-pangkat-rekursif/) |
| 12.2 | [Pengubah ke biner](mini-project/12-2-pengubah-ke-biner/) |
| 13.1 | [Cari nomor absen](mini-project/13-1-cari-nomor-absen/) |
| 13.2 | [Urutkan tinggi badan](mini-project/13-2-urutkan-tinggi-badan/) |
| 13.3 | [Lomba kecepatan algoritma](mini-project/13-3-lomba-kecepatan-algoritma/) |
| 14.1 | [Pengecek kurung](mini-project/14-1-pengecek-kurung/) |
| 14.2 | [Antrean loket](mini-project/14-2-antrean-loket/) |
| 15.1 | [ArrayList buatan sendiri](mini-project/15-1-arraylist-buatan-sendiri/) |
| 15.2 | [Akses aman](mini-project/15-2-akses-aman/) |
| 16.1 | [Rantai gerbong](mini-project/16-1-rantai-gerbong/) |
| 16.2 | [Statistik linked list](mini-project/16-2-statistik-linked-list/) |
| 17.1 | [Kamus angka (BST)](mini-project/17-1-kamus-angka-bst/) |
| 17.2 | [Tiga cara menelusuri pohon](mini-project/17-2-tiga-cara-menelusuri-pohon/) |
| 18.1 | [Loker hash](mini-project/18-1-loker-hash/) |
| 18.2 | [Daftar tugas prioritas](mini-project/18-2-daftar-tugas-prioritas/) |
| 19.1 | [Urutkan dengan aturan sendiri](mini-project/19-1-urutkan-dengan-aturan-sendiri/) |
| 19.2 | [Kasir diskon](mini-project/19-2-kasir-diskon/) |
