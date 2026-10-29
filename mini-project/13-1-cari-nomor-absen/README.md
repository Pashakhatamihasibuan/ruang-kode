# 13.1 Cari nomor absen

Daftar nomor terurut: 3, 8, 15, 21, 30, 42, 57. Cari nomor 42 dengan binary search dan cetak setiap tebakan tengahnya.

## Langkah dari kalimat ke kode

1. lo = 0, hi = panjang − 1.
2. Selama lo <= hi: hitung mid, bandingkan a[mid] dengan target.
3. Terlalu kecil → lo = mid + 1. Terlalu besar → hi = mid − 1.

## Keluaran yang diharapkan

```
cek a[3] = 21
cek a[5] = 42
Ketemu di indeks 5
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
