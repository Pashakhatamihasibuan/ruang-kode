# 10.1 Daftar belanja

Mulai dari daftar kosong. Tambahkan beras, telur, susu. Sisipkan gula di posisi 1. Hapus telur. Ganti susu menjadi teh. Cetak hasil setiap langkah.

## Langkah dari kalimat ke kode

1. "tambahkan" → add / append.
2. "sisipkan di posisi" → add(i, x) / insert(i, x).
3. "hapus" → remove / remove(x). "ganti" → set / L[i] = x.

## Keluaran yang diharapkan

Java:

```
[beras, telur, susu]
[beras, gula, telur, susu]
[beras, gula, susu]
[beras, gula, teh]
```

Python:

```
['beras', 'telur', 'susu']
['beras', 'gula', 'telur', 'susu']
['beras', 'gula', 'susu']
['beras', 'gula', 'teh']
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
