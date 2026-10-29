with open("nilai.txt") as f:
    for line in f:
        t = line.split()
        a = int(t[1])
        b = int(t[2])
        print(t[0] + ":", (a + b) // 2)
