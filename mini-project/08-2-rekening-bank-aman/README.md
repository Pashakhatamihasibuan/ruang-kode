# 8.2 Rekening bank aman

Buat kelas Rekening. setor dan tarik harus menolak jumlah tidak valid (negatif atau melebihi saldo). Saldo hanya bisa dibaca lewat getSaldo.

## Langkah dari kalimat ke kode

1. Field saldo dibuat private / _saldo.
2. Di dalam setor & tarik, cek dulu syaratnya dengan if.
3. Kembalikan true/false agar pemanggil tahu berhasil atau tidak.

## Keluaran yang diharapkan

Java:

```
true
false
true
Saldo: 30000
```

Python:

```
True
False
True
Saldo: 30000
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
