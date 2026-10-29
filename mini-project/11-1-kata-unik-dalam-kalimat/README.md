# 11.1 Kata unik dalam kalimat

Dari kalimat "saya suka kopi dan saya suka teh", cetak kata-kata unik secara terurut dan jumlahnya.

## Langkah dari kalimat ke kode

1. Pecah kalimat menjadi kata dengan split.
2. Masukkan semua kata ke set: duplikat otomatis dibuang.
3. Pakai TreeSet / sorted() agar urutannya pasti.

## Keluaran yang diharapkan

Java:

```
[dan, kopi, saya, suka, teh]
Jumlah kata unik: 5
```

Python:

```
['dan', 'kopi', 'saya', 'suka', 'teh']
Jumlah kata unik: 5
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
