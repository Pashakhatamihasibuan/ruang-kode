# 12.1 Pangkat rekursif

Tulis method pangkat(a, b) secara rekursif tanpa loop dan tanpa Math.pow / **. Hitung 2⁵ dan 3⁴.

## Langkah dari kalimat ke kode

1. Base case: a pangkat 0 = 1.
2. Recursive case: a^b = a × a^(b − 1).
3. Setiap panggilan mengurangi b, jadi pasti mencapai 0.

## Keluaran yang diharapkan

```
2^5 = 32
3^4 = 81
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
