# 18.1 Loker hash

Buat tabel hash 5 ember dengan chaining. Masukkan kunci 12, 7, 9, 3, 15, lalu cetak isi setiap ember dan tunjukkan collision.

## Langkah dari kalimat ke kode

1. indeks = kunci % 5.
2. Setiap ember adalah list; kunci baru di-append ke ember itu.
3. Ember berisi lebih dari satu kunci = terjadi collision.

## Keluaran yang diharapkan

```
[0] [15]
[1] []
[2] [12, 7]  <- collision
[3] [3]
[4] [9]
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
