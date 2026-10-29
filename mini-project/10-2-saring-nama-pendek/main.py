nama = ["Ani", "Budi", "Eko", "Ida", "Sari", "Tono"]
for i in range(len(nama) - 1, -1, -1):
    if len(nama[i]) < 4:
        nama.pop(i)
print(nama)
