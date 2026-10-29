# 14.2 Antrean loket

Empat orang datang berurutan: Ani, Budi, Cici, Dodi. Loket melayani satu per satu sesuai urutan datang. Cetak siapa yang dilayani dan sisa antrean.

## Langkah dari kalimat ke kode

1. "sesuai urutan datang" → queue (FIFO).
2. Masukkan semua nama di belakang antrean.
3. Selama antrean tidak kosong: ambil dari depan, layani.

## Keluaran yang diharapkan

Java:

```
Melayani Ani, sisa [Budi, Cici, Dodi]
Melayani Budi, sisa [Cici, Dodi]
Melayani Cici, sisa [Dodi]
Melayani Dodi, sisa []
```

Python:

```
Melayani Ani, sisa ['Budi', 'Cici', 'Dodi']
Melayani Budi, sisa ['Cici', 'Dodi']
Melayani Cici, sisa ['Dodi']
Melayani Dodi, sisa []
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
