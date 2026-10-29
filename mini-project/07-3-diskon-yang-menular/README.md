# 7.3 Diskon yang menular

Buat method diskon(harga) yang memotong setiap harga 50% langsung di array. Buktikan array asli ikut berubah, sedangkan salinannya tidak.

## Langkah dari kalimat ke kode

1. Buat salinan dulu: Arrays.copyOf / list.copy().
2. Kirim array asli ke method. Method menerima alamat yang sama.
3. Cetak keduanya untuk membandingkan.

## Keluaran yang diharapkan

```
harga    = [5000, 10000, 15000]
cadangan = [10000, 20000, 30000]
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
