class ArrayIntList:
    def __init__(self):
        self.data = [0] * 2
        self.size = 0

    def add(self, value):
        if self.size == len(self.data):
            self.data = self.data + [0] * len(self.data)
            print("Kapasitas naik menjadi", len(self.data))
        self.data[self.size] = value
        self.size += 1

    def __str__(self):
        return f"{self.data[:self.size]} size={self.size} kapasitas={len(self.data)}"

lst = ArrayIntList()
for x in range(10, 51, 10):
    lst.add(x)
print(lst)
