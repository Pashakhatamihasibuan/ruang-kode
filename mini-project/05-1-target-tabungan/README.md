# 5.1 Target tabungan

Tabungan awal 100000 bertambah 10% setiap tahun (pecahan rupiah dibuang). Berapa tahun sampai tabungan mencapai minimal 200000?

## Langkah dari kalimat ke kode

1. Kalimat "sampai mencapai" → while (saldo < target).
2. Di badan loop: saldo += saldo / 10, tahun++.
3. Cetak saldo setiap tahun supaya mudah dilacak.

## Keluaran yang diharapkan

```
Tahun 1: 110000
Tahun 2: 121000
Tahun 3: 133100
Tahun 4: 146410
Tahun 5: 161051
Tahun 6: 177156
Tahun 7: 194871
Tahun 8: 214358
Butuh 8 tahun
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
