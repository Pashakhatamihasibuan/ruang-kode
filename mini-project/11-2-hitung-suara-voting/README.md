# 11.2 Hitung suara voting

Hasil voting ketua kelas: Ani, Budi, Ani, Cici, Budi, Ani. Hitung suara setiap calon dan tentukan pemenangnya.

## Langkah dari kalimat ke kode

1. "berapa kali setiap …" → map dari nama ke jumlah.
2. m[nama] = (nilai lama atau 0) + 1.
3. Telusuri map untuk mencari jumlah terbesar.

## Keluaran yang diharapkan

Java:

```
{Ani=3, Budi=2, Cici=1}
Pemenang: Ani (3 suara)
```

Python:

```
{'Ani': 3, 'Budi': 2, 'Cici': 1}
Pemenang: Ani (3 suara)
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
