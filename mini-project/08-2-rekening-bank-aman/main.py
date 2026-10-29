class Rekening:
    def __init__(self):
        self._saldo = 0

    def setor(self, x):
        if x <= 0:
            return False
        self._saldo += x
        return True

    def tarik(self, x):
        if x <= 0 or x > self._saldo:
            return False
        self._saldo -= x
        return True

    def get_saldo(self):
        return self._saldo

r = Rekening()
print(r.setor(50000))
print(r.tarik(80000))
print(r.tarik(20000))
print("Saldo:", r.get_saldo())
