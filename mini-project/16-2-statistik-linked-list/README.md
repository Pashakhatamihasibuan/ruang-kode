# 16.2 Statistik linked list

Untuk linked list 4 → 9 → 2 → 7, hitung banyak node, jumlah, dan nilai terbesar dengan satu kali penelusuran.

## Langkah dari kalimat ke kode

1. cur = front, lalu while (cur != null).
2. Di setiap node: count++, total += data, perbarui maks.
3. Jangan lupa cur = cur.next agar tidak loop selamanya.

## Keluaran yang diharapkan

```
count=4 total=22 maks=9
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
