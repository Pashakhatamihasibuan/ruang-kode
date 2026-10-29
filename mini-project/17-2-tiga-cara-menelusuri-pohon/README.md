# 17.2 Tiga cara menelusuri pohon

Untuk BST dari 8, 3, 10, 1, 6, cetak urutan pre-order, in-order, dan post-order.

## Langkah dari kalimat ke kode

1. Ketiganya sama: kunjungi kiri dan kanan secara rekursif.
2. Bedanya hanya posisi baris cetak: sebelum, di antara, atau sesudah.
3. In-order pada BST selalu terurut.

## Keluaran yang diharapkan

```
pre : 8 3 1 6 10 
in  : 1 3 6 8 10 
post: 1 6 3 10 8 
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
