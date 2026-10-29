# 6.2 Penjumlah data kotor

Data dari formulir: "12", "abc", "7", "3x", "20". Jumlahkan yang berupa angka dan laporkan yang tidak valid.

## Langkah dari kalimat ke kode

1. Coba ubah setiap teks menjadi int di dalam try.
2. Jika gagal, catch menangkap error lalu cetak peringatan.
3. Hanya yang berhasil ditambahkan ke total.

## Keluaran yang diharapkan

```
Lewati: abc
Lewati: 3x
Total: 39
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
