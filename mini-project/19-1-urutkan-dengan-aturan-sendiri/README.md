# 19.1 Urutkan dengan aturan sendiri

Urutkan nama Siti, Al, Budiman, Eka berdasarkan panjang nama (pendek dulu) memakai lambda, lalu cetak dalam huruf besar.

## Langkah dari kalimat ke kode

1. Aturan urut ditulis sebagai lambda: (a, b) -> a.length() - b.length() / key=lambda s: len(s).
2. Lambda kedua mengubah setiap nama: s -> s.toUpperCase().
3. Lambda = method kecil tanpa nama.

## Keluaran yang diharapkan

Java:

```
[Al, Eka, Siti, Budiman]
AL
EKA
SITI
BUDIMAN
```

Python:

```
['Al', 'Eka', 'Siti', 'Budiman']
AL
EKA
SITI
BUDIMAN
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
