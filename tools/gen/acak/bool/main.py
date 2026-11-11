# 1. Hasil perbandingan selalu boolean: True atau False
nilai, hadir = 82, 70
nilai_cukup = nilai >= 75
hadir_cukup = hadir >= 80
print("nilai_cukup =", nilai_cukup)
print("hadir_cukup =", hadir_cukup)

# 2. and, or, not (ditulis dengan kata)
print("AND: lulus =", nilai_cukup and hadir_cukup)
print("OR : remedial =", not nilai_cukup or not hadir_cukup)
print("NOT: not hadir_cukup =", not hadir_cukup)

# 3. Tabel kebenaran semua kombinasi p dan q
tf = [True, False]
print("p     q     AND   OR    XOR")
for p in tf:
    for q in tf:
        print(f"{p!s:<6}{q!s:<6}{p and q!s:<6}{p or q!s:<6}{p ^ q}")

# 4. Hukum De Morgan, dicek untuk semua kombinasi
hukum1 = all((not (p and q)) == (not p or not q) for p in tf for q in tf)
hukum2 = all((not (p or q)) == (not p and not q) for p in tf for q in tf)
print("De Morgan 1: not (p and q) == not p or not q ->", hukum1)
print("De Morgan 2: not (p or q) == not p and not q ->", hukum2)

# 5. Urutan: not dulu, lalu and, baru or
print("True or False and False =", True or False and False)

# 6. Short-circuit: sisi kanan tidak dihitung jika hasil sudah pasti
pembagi = 0
if pembagi != 0 and 10 / pembagi > 1:
    print("hasil bagi besar")
else:
    print("short-circuit: 10 / 0 tidak pernah dihitung")
