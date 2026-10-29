data = ["12", "abc", "7", "3x", "20"]
total = 0
for s in data:
    try:
        total += int(s)
    except ValueError:
        print("Lewati:", s)
print("Total:", total)
