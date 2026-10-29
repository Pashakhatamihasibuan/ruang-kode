a = [70, 85, 60, 90, 75]
total = 0
for i in range(len(a)):
    total += a[i]
rata = total // len(a)
print("Rata-rata:", rata)
for i in range(len(a)):
    if a[i] > rata:
        print("a[" + str(i) + "] =", a[i])
