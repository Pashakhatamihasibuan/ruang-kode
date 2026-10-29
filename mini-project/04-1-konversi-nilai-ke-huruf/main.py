def huruf(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    else:
        return "D"

for n in [95, 82, 74, 50]:
    print(n, "->", huruf(n))
