# 13.3 Lomba kecepatan algoritma

Hitung berapa kali langkah inti dijalankan oleh tiga pola (satu loop, loop bersarang, dan bagi dua) untuk n = 8 dan n = 1024.

## Langkah dari kalimat ke kode

1. Satu loop 1..n → tambah penghitung n kali.
2. Loop bersarang → n × n kali.
3. Bagi dua: while (n > 1) n /= 2 → sekitar log₂ n kali.

## Keluaran yang diharapkan

```
n=8 linear=8 kuadrat=64 log=3
n=1024 linear=1024 kuadrat=1048576 log=10
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
