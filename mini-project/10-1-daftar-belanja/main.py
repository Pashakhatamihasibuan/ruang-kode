belanja = []
belanja.append("beras")
belanja.append("telur")
belanja.append("susu")
print(belanja)
belanja.insert(1, "gula")
print(belanja)
belanja.remove("telur")
print(belanja)
belanja[belanja.index("susu")] = "teh"
print(belanja)
