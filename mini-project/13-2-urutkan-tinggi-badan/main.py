a = [165, 150, 172, 158]
for i in range(len(a) - 1):
    m = i
    for j in range(i + 1, len(a)):
        if a[j] < a[m]: m = j
    a[i], a[m] = a[m], a[i]
    print("Putaran", str(i + 1) + ":", a)
