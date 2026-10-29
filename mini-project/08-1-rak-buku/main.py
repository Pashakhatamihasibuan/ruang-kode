class Buku:
    def __init__(self, judul, halaman):
        self.judul = judul
        self.halaman = halaman

    def info(self):
        return self.judul + " (" + str(self.halaman) + " hlm)"

a = Buku("Laskar Pelangi", 529)
b = Buku("Bumi", 440)
print(a.info())
print(b.info())
