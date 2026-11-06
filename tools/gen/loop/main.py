# 1. for: jumlah putaran sudah pasti
for i in range(1, 4):
    print("for: i =", i)

# 2. while: kondisi dicek DULU, bisa 0 kali
n = 3
while n > 0:
    print("while: n =", n)
    n -= 1

# 3. do-while: Python tidak punya, tiru dengan while True + break
x = 10
while True:
    print("do-while: x =", x, "(tetap jalan sekali)")
    x += 1
    if not x < 5:
        break

# 4. for-each: for di Python memang menelusuri isi koleksi
buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print("for-each:", b)

# 5. bersarang: loop di dalam loop
for baris in range(1, 3):
    isi = [str(baris * kolom) for kolom in range(1, 4)]
    print("nested:", " ".join(isi))

# 6. break: keluar dari loop lebih awal
hasil = []
for i in range(1, 11):
    if i == 4:
        break
    hasil.append(str(i))
print("break:", " ".join(hasil))

# 7. continue: lewati sisa badan untuk putaran ini saja
hasil = []
for i in range(1, 7):
    if i % 2 == 0:
        continue
    hasil.append(str(i))
print("continue:", " ".join(hasil))
