def cari(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print("cek a[" + str(mid) + "] =", a[mid])
        if a[mid] == target: return mid
        elif a[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1

a = [3, 8, 15, 21, 30, 42, 57]
print("Ketemu di indeks", cari(a, 42))
