def bmi(berat, tinggi_cm):
    m = tinggi_cm / 100
    hasil = berat / (m * m)
    return round(hasil, 1)

print("Andi:", bmi(60, 170))
print("Bela:", bmi(48, 155))
