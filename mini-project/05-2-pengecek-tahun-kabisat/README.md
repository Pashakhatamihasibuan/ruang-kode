# 5.2 Pengecek tahun kabisat

Tahun kabisat: habis dibagi 4 dan tidak habis dibagi 100, atau habis dibagi 400. Cek tahun 1900, 2000, 2024, dan 2025.

## Langkah dari kalimat ke kode

1. "habis dibagi 4" → t % 4 == 0.
2. "dan tidak" → && !(...) / and not.
3. "atau" → || / or. Gunakan kurung agar jelas.

## Keluaran yang diharapkan

Java:

```
1900 kabisat? false
2000 kabisat? true
2024 kabisat? true
2025 kabisat? false
```

Python:

```
1900 kabisat? False
2000 kabisat? True
2024 kabisat? True
2025 kabisat? False
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
