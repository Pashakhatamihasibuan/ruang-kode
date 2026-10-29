suara = ["Ani", "Budi", "Ani", "Cici", "Budi", "Ani"]
hitung = {}
for s in suara:
    hitung[s] = hitung.get(s, 0) + 1
print(dict(sorted(hitung.items())))
juara = ""
maks = 0
for nama in sorted(hitung):
    if hitung[nama] > maks:
        maks = hitung[nama]
        juara = nama
print("Pemenang:", juara, "(" + str(maks), "suara)")
