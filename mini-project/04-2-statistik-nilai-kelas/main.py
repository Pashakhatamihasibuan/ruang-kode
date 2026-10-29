nilai = [78, 92, 65, 88, 70]
total = 0
maks = nilai[0]
for n in nilai:
    total += n
    if n > maks:
        maks = n
print("Total     :", total)
print("Rata-rata :", total // len(nilai))
print("Tertinggi :", maks)
