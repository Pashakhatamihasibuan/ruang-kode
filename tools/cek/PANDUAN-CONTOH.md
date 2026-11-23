# Panduan contoh bertahap

Aturan untuk semua contoh kode di Ruang Kode (contoh utama, contoh lain, dan kasus di bagian Pendalaman).

## Prinsip

1. **Bertahap.** Contoh di sebuah pelajaran hanya boleh memakai konsep yang sudah diajarkan di pelajaran itu atau
   sebelumnya di jalur yang sama. Contoh di pelajaran "Variabel" hanya memakai assignment, angka/teks, operator
   aritmetika sederhana, dan `print`. Tidak ada fungsi, f-string, if, loop, list, import, atau class.
2. **Fokus.** Setiap contoh memperlihatkan konsep pelajaran itu, bukan konsep lain.
3. **Lebih dari satu.** Setiap pelajaran berkode punya contoh utama ditambah minimal 2 (idealnya 3) contoh lain
   dengan kasus berbeda tapi tetap tentang konsep yang sama. Contoh: Variabel → (1) data siswa, (2) harga belanja di
   warung, (3) jarak tempuh ojek, (4) menukar isi dua variabel.
4. **Kasus dekat dengan pelajar Indonesia.** Rupiah, sekolah, kantin, toko daring, ojek, nilai rapor, pulsa, kereta,
   cuaca, dsb. Nama orang Indonesia yang beragam. Bahasa Indonesia baku dan sederhana, komentar kode dalam bahasa
   Indonesia, nama variabel mengikuti konvensi bahasanya (snake_case di Python, camelCase di Java/JS/Kotlin/Dart).
5. **Keluaran benar.** Setiap contoh yang bisa dijalankan punya `out` yang persis sama dengan keluaran program.
   Hasilkan `out` dengan menjalankan kode, jangan menebak.
6. **Kode final, standar industri 2026.** Rapi, idiomatis untuk level pelajaran itu, tanpa praktik buruk.
   Kalau kode belum boleh memakai konsep yang "lebih benar" (misalnya fungsi), tulis versi sederhana yang tetap benar.
7. **Pendalaman** (`cx`, "kasus nyata") boleh lebih panjang dan bernuansa industri, tetapi tetap hanya memakai konsep
   yang sudah diajarkan. Kalau kasus lama melompat, tulis ulang dengan konsep yang ada (jumlah kasus boleh sama).
8. **Contoh utama** yang sudah bertahap dan bagus jangan diganti. Ganti hanya bila melompat atau salah.
   Bila mengganti contoh utama dan pelajaran itu punya tabel "Dari kalimat ke kode" (`trs`), tulis `trs` baru yang
   cocok dengan kode baru.

## Tempat menulis

- Contoh: `src/contoh/<jalur>.json` (atau `src/contoh/<jalur>.<bagian>.json` untuk jalur besar yang dikerjakan
  beberapa orang). Format ada di docstring `tools/build/contoh.py`. Dikunci dengan id pelajaran (misalnya `python-1-3`).
- Aturan urutan konsep: `tools/cek/aturan/<jalur>.json`, berisi
  `{"aturan": [["nama konsep", "regex di kode", "regex judul pelajaran pengenal"], ...], "abaikan": [id...]}`.
  `abaikan` hanya untuk pelajaran yang memang tidak butuh banyak contoh (misalnya instalasi alat).

## Cara memeriksa

    python3 tools/cek/urutan.py <jalur>      # 0 contoh melompat, 0 pelajaran dengan contoh lain < 2
    python3 tools/cek/jalankan.py <jalur>    # 0 beda (python, js, ts, java, dart, kotlin dijalankan sungguhan)

Data sumber pelajaran: urutan di `web/src/data/catalog.json`, isi di `web/src/data/t/<jalur>.json`
(`b` = materi, `code`/`out` = contoh utama, `trs` = tabel kalimat ke kode, `deep.cx` = Pendalaman).
