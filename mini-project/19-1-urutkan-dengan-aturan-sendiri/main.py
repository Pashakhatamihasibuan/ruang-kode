nama = ["Siti", "Al", "Budiman", "Eka"]
nama.sort(key=lambda s: len(s))
print(nama)
for s in map(lambda s: s.upper(), nama):
    print(s)
