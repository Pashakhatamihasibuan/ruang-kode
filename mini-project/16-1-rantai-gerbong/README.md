# 16.1 Rantai gerbong

Bangun linked list dengan menambah di depan: 30, lalu 20, lalu 10. Cetak data node pertama, kedua, dan ketiga lewat .next.

## Langkah dari kalimat ke kode

1. addFirst: front = new ListNode(x, front).
2. Node pertama: front.data. Kedua: front.next.data.
3. Setiap .next = ikuti satu panah.

## Keluaran yang diharapkan

```
10
20
30
```

## Menjalankan solusi

```bash
javac Main.java && java Main
python3 main.py
```
