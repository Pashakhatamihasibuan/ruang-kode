def diskon(a):
    for i in range(len(a)):
        a[i] = a[i] // 2

harga = [10000, 20000, 30000]
cadangan = harga.copy()
diskon(harga)
print("harga    =", harga)
print("cadangan =", cadangan)
