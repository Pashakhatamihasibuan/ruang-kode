# 1.2 Lirik lagu dengan reff

Cetak lirik lagu pendek yang punya reff (chorus) dua kali. Reff ditulis sekali sebagai method, lalu dipanggil dua kali.

## Langkah dari kalimat ke kode

1. Cari bagian yang berulang: itulah reff.
2. Buat method reff() berisi baris-baris reff.
3. Di main: bait 1 → reff() → bait 2 → reff().

## Keluaran yang diharapkan

```
Pagi cerah datang lagi
  Ayo belajar, ayo coba
  Kode jalan, hati gembira
Sore tiba, langit jingga
  Ayo belajar, ayo coba
  Kode jalan, hati gembira
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
