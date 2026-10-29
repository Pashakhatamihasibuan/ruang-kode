tabel = [[] for _ in range(5)]
for k in [12, 7, 9, 3, 15]:
    tabel[k % 5].append(k)
for i in range(5):
    tanda = "  <- collision" if len(tabel[i]) > 1 else ""
    print("[" + str(i) + "] " + str(tabel[i]) + tanda)
