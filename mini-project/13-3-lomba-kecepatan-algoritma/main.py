def linear(n):
    c = 0
    for i in range(n): c += 1
    return c

def kuadrat(n):
    c = 0
    for i in range(n):
        for j in range(n): c += 1
    return c

def logaritma(n):
    c = 0
    while n > 1:
        n //= 2
        c += 1
    return c

for n in [8, 1024]:
    print(f"n={n} linear={linear(n)} kuadrat={kuadrat(n)} log={logaritma(n)}")
