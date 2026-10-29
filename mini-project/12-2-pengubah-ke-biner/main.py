def biner(n):
    if n < 2:
        return str(n)
    return biner(n // 2) + str(n % 2)

print("13 =", biner(13))
print("6  =", biner(6))
