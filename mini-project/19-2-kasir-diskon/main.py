from functools import reduce

harga = [30000, 75000, 120000, 45000, 60000]
mahal = filter(lambda x: x > 50000, harga)
diskon = map(lambda x: x * 80 // 100, mahal)
total = reduce(lambda a, b: a + b, diskon, 0)
print("Total diskon:", total)
