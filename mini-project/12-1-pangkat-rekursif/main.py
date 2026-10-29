def pangkat(a, b):
    if b == 0:
        return 1
    return a * pangkat(a, b - 1)

print("2^5 =", pangkat(2, 5))
print("3^4 =", pangkat(3, 4))
