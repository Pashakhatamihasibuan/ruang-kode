from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self): ...

class Persegi(Bentuk):
    def __init__(self, s): self.s = s
    def luas(self): return self.s * self.s

class PersegiPanjang(Bentuk):
    def __init__(self, p, l): self.p, self.l = p, l
    def luas(self): return self.p * self.l

class Segitiga(Bentuk):
    def __init__(self, a, t): self.a, self.t = a, t
    def luas(self): return self.a * self.t // 2

daftar = [Persegi(4), PersegiPanjang(3, 5), Segitiga(6, 4)]
total = 0
for b in daftar:
    print(type(b).__name__ + ":", b.luas())
    total += b.luas()
print("Total:", total)
