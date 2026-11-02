nama = "Rina"
umur = 20
ipk = 3.4567
# f-string: {nilai:spesifikasi}
print(f"Nama: {nama}, umur {umur}, IPK {ipk:.2f}")

# lebar dan perataan: > kanan, < kiri, ^ tengah, 0 isi nol
print(f"[{nama:>8}] [{nama:<8}] [{nama:^8}] [{umur:05d}]")

# pemisah ribuan, persen, basis lain, notasi ilmiah
print(f"Gaji {7500000:,} | diskon {0.15:.0%} | hex {255:x} | biner {5:b}")
print(f"{123456.789:.3e} | {umur > 17} | {nama!r}")

# debugging cepat: {variabel=} mencetak nama dan nilainya
print(f"{umur=}, {ipk=:.1f}")

# gaya lama yang masih ditemui di kode lama dan logging
print("Nama: %s, umur %d, IPK %.2f" % (nama, umur, ipk))
print("Kode: INV-{:04d}".format(7))

# struk belanja
barang = ["Kopi susu", "Roti bakar", "Air mineral"]
harga = [18000, 22500, 5000]
print(f"{'Barang':<12} {'Harga':>10}")
for b, h in zip(barang, harga):
    print(f"{b:<12} {h:>10,}")
print(f"{'TOTAL':<12} {sum(harga):>10,}")
