class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return "..."

class Kucing(Hewan):
    def suara(self):
        return "Meong"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

kebun = [Kucing("Oyen"), Anjing("Doggo"), Hewan("Ikan")]
for h in kebun:
    print(h.nama + ":", h.suara())
