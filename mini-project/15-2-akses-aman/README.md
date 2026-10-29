# 15.2 Akses aman

Tambahkan method get(index) yang melempar exception bila index di luar 0..size−1. Uji dengan indeks valid dan tidak valid.

## Langkah dari kalimat ke kode

1. Precondition dicek di baris pertama method.
2. Pesan exception menyebut indeks yang salah.
3. Pemanggil memakai try / catch untuk menangkapnya.

## Keluaran yang diharapkan

```
get(1) = 9
Error: index 3 di luar 0..2
Error: index -1 di luar 0..2
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
