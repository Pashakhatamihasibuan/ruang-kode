# 17.1 Kamus angka (BST)

Masukkan 8, 3, 10, 1, 6, 14 ke binary search tree. Lalu cek apakah 6 dan 9 ada, dan hitung tinggi pohonnya.

## Langkah dari kalimat ke kode

1. add: kecil → kiri, besar → kanan, sampai ketemu null.
2. contains: ikuti arah yang sama; null berarti tidak ada.
3. tinggi = 1 + maks(tinggi kiri, tinggi kanan); pohon kosong = 0.

## Keluaran yang diharapkan

Java:

```
ada 6? true
ada 9? false
tinggi = 3
```

Python:

```
ada 6? True
ada 9? False
tinggi = 3
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
