# 15.1 ArrayList buatan sendiri

Buat kelas ArrayIntList dengan array internal berkapasitas 2. add(x) menggandakan kapasitas saat penuh. Tambahkan 5 angka dan cetak setiap kali kapasitas berubah.

## Langkah dari kalimat ke kode

1. Field: data (array) dan size.
2. Jika size == data.length → buat array 2× lebih besar, salin isi lama.
3. Taruh nilai di data[size], lalu size++.

## Keluaran yang diharapkan

```
Kapasitas naik menjadi 4
Kapasitas naik menjadi 8
[10, 20, 30, 40, 50] size=5 kapasitas=8
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
