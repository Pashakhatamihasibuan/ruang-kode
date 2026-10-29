# 12.2 Pengubah ke biner

Tulis method rekursif biner(n) yang mengembalikan bentuk biner dari n sebagai teks. Uji dengan 13 dan 6.

## Langkah dari kalimat ke kode

1. n % 2 = bit terakhir, n / 2 = bit-bit sisanya.
2. Base case: n < 2 → teksnya n itu sendiri.
3. Hasil = biner(n / 2) + bit terakhir (sisanya ditulis di depan).

## Keluaran yang diharapkan

```
13 = 1101
6  = 110
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
