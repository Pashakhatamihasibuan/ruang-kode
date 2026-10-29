saldo = 100000
tahun = 0
while saldo < 200000:
    saldo += saldo // 10
    tahun += 1
    print("Tahun", str(tahun) + ":", saldo)
print("Butuh", tahun, "tahun")
