import random

# 1. Desimal acak: 0.0 sampai KURANG DARI 1.0
r = random.random()
print(f"desimal: {r:.4f}")

# 2. Dadu 1..6: randint memasukkan KEDUA batas
print("5 dadu :", end="")
for i in range(5):
    print(" " + str(random.randint(1, 6)), end="")
print()

# 3. Rentang bebas bawah..atas
bawah, atas = 10, 20
print("10..20 :", random.randint(bawah, atas))

# 4. Lempar dadu sampai keluar angka 6
lemparan, hasil = 0, 0
while hasil != 6:
    hasil = random.randint(1, 6)
    lemparan += 1
print(f"dapat 6 setelah {lemparan} lemparan")

# 5. Memilih satu isi list dan mengocok list
menu = ["soto", "bakso", "gado-gado", "nasi goreng"]
print("menu   :", random.choice(menu))
kartu = [1, 2, 3, 4, 5]
random.shuffle(kartu)
print("kocok  :", kartu)

# 6. Seed sama menghasilkan urutan yang sama (berguna untuk pengujian)
a = random.Random(42)
b = random.Random(42)
sama = all(a.randint(0, 99) == b.randint(0, 99) for _ in range(5))
print("seed 42 dua kali, urutan sama:", sama)
