# 14.1 Pengecek kurung

Periksa apakah kurung dalam teks seimbang: "(a[b]{c})", "(]", dan "((x)".

## Langkah dari kalimat ke kode

1. Kurung buka → push ke stack.
2. Kurung tutup → stack tidak boleh kosong, dan pop harus pasangannya.
3. Di akhir, stack harus kosong.

## Keluaran yang diharapkan

Java:

```
(a[b]{c}) -> true
(] -> false
((x) -> false
```

Python:

```
(a[b]{c}) -> True
(] -> False
((x) -> False
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
