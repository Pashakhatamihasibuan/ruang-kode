# 19.2 Kasir diskon

Harga belanja: 30000, 75000, 120000, 45000, 60000. Barang di atas 50000 diberi diskon 20%. Hitung total yang dibayar untuk barang-barang yang didiskon saja.

## Langkah dari kalimat ke kode

1. "barang di atas 50000" → filter.
2. "diberi diskon 20%" → map: x -> x * 80 / 100.
3. "hitung total" → reduce / sum.

## Keluaran yang diharapkan

```
Total diskon: 204000
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
