"""Pendalaman jalur Flowgorithm: istilah dunia kerja dan contoh flowchart (teks) + terjemahan Python yang dijalankan."""
K = 'flowg'


def F(t, alur, py, b=None):
    """Satu contoh: alur flowchart (sebagai komentar) lalu terjemahan Python yang benar-benar dijalankan."""
    kom = '\n'.join('# ' + s if s else '#' for s in alur.strip('\n').split('\n'))
    return dict(t=t, b=b, code='# --- Alur flowchart ---\n' + kom + '\n\n# --- Python ---\n' + py.strip('\n'))


def T(t, teks, b=None):
    return dict(t=t, b=b, code=teks.strip('\n'), lang='text', run=False)


D = {
'Flowchart dan Flowgorithm': dict(
  ist=[('Flowchart', 'Diagram alur yang memakai simbol standar untuk menggambarkan langkah algoritma atau proses bisnis.'),
       ('ISO 5807', 'Standar internasional simbol flowchart: terminal (oval), proses (persegi), keputusan (belah ketupat), input/output (jajar genjang).'),
       ('BPMN', 'Business Process Model and Notation: notasi proses bisnis yang dipakai analis sistem, turunan ide flowchart.'),
       ('Swimlane', 'Flowchart yang dibagi per lajur peran (pelanggan, kasir, gudang) untuk menunjukkan siapa melakukan apa.')],
  cx=[T('Simbol flowchart dan padanannya di Flowgorithm', '''
Simbol            Bentuk           Di Flowgorithm       Contoh isi
Terminal          oval             Main / End           Mulai, Selesai
Proses            persegi          Assign               total = harga * qty
Input             jajar genjang    Input                Input nilai
Output            jajar genjang    Output               Output "Lulus"
Keputusan         belah ketupat    If                   nilai >= 75 ?
Perulangan        segi enam        For / While / Do     For i = 1 to 10
Deklarasi         persegi bergaris Declare              Integer umur
Panggilan fungsi  persegi ganda    Call                 Call CetakStruk
Konektor          lingkaran        (otomatis)           A -> A'''),
     T('Flowchart proses bisnis dengan swimlane: pemesanan kopi', '''
PELANGGAN        | KASIR                         | BARISTA
-----------------+-------------------------------+------------------
(Mulai)          |                               |
[Pesan kopi] ----+-> [Catat pesanan]             |
                 |   <Bayar QRIS berhasil?>      |
                 |    | tidak -> [Minta metode lain]
                 |    | ya                       |
                 |   [Cetak nomor antre] --------+-> [Buat kopi]
[Terima kopi] <--+-------------------------------+-- [Panggil nomor]
(Selesai)        |                               |''', 'Analis sistem memakai flowchart seperti ini saat wawancara kebutuhan, sebelum ada satu baris kode pun.')]),

'Memasang dan memakai Flowgorithm': dict(
  ist=[('IDE visual', 'Lingkungan pemrograman berbasis gambar; Flowgorithm menjalankan flowchart langsung tanpa menulis kode.'),
       ('Variable Watch', 'Jendela Flowgorithm untuk melihat nilai variabel berubah selama program berjalan.'),
       ('Step / breakpoint', 'Menjalankan satu simbol per langkah untuk mencari kesalahan logika (debugging).'),
       ('Trace table', 'Tabel manual berisi nilai variabel di tiap langkah; versi kertas dari Variable Watch.')],
  cx=[F('Trace table otomatis: meniru Variable Watch', '''
Main
  Declare Integer i, total
  Assign total = 0
  For i = 1 to 5
    Assign total = total + i
  End For
  Output total
End
''', '''
total = 0
print(f"{'langkah':>7} | {'i':>2} | {'total':>5}")
for langkah, i in enumerate(range(1, 6), 1):
    total = total + i
    print(f"{langkah:>7} | {i:>2} | {total:>5}")
print("Output:", total)
''', 'Membuat trace table adalah keterampilan yang diuji di ujian sertifikasi dan wawancara: membaca kode tanpa menjalankannya.')]),

'Tipe data, Declare, dan aturan ekspresi': dict(
  ist=[('Strongly typed', 'Flowgorithm mewajibkan Declare dengan tipe (Integer, Real, String, Boolean) sebelum variabel dipakai.'),
       ('Integer division', 'Di Flowgorithm, 7 / 2 = 3.5 (Real); gunakan div untuk hasil bulat dan mod untuk sisa.'),
       ('String concatenation', 'Operator & di Flowgorithm menggabungkan teks: "Halo " & nama.'),
       ('Type mismatch', 'Error saat nilai tidak cocok dengan tipe variabel, misalnya teks dimasukkan ke Integer.')],
  cx=[F('Operator Flowgorithm dan padanannya di Python', '''
Declare Integer a, b
Declare Real hasil
Declare String nama
Assign a = 17
Assign b = 5
Assign hasil = a / b      -> 3.4
Output a div b            -> 3   (pembagian bulat)
Output a mod b            -> 2   (sisa bagi)
Output a ^ 2              -> 289 (pangkat)
Assign nama = "Sari"
Output "Halo " & nama     -> Halo Sari
''', '''
a, b = 17, 5
hasil = a / b
print("a / b   =", hasil)
print("a div b =", a // b)
print("a mod b =", a % b)
print("a ^ 2   =", a ** 2)
nama = "Sari"
print("Halo " + nama)
try:
    umur = int("tujuh belas")          # type mismatch
except ValueError:
    print("type mismatch: 'tujuh belas' bukan Integer")
''')]),

'Luas dan keliling lingkaran': dict(
  ist=[('IPO model', 'Input-Process-Output: kerangka dasar setiap program dan setiap fungsi.'),
       ('Konstanta pi', 'Gunakan konstanta bawaan (Flowgorithm: pi, Python: math.pi), jangan menulis 3.14 sendiri.'),
       ('Rounding', 'Membulatkan hasil untuk tampilan; perhitungan tetap memakai nilai penuh.'),
       ('Unit of measure', 'Satuan (cm, m²) wajib jelas di input dan output agar tidak salah tafsir.')],
  cx=[F('Menghitung kebutuhan cat kolam bundar', '''
Input diameter (meter), kedalaman (meter)
Assign r = diameter / 2
Assign luas_dasar = pi * r ^ 2
Assign luas_dinding = 2 * pi * r * kedalaman
Assign liter_cat = (luas_dasar + luas_dinding) / 10     (1 liter untuk 10 m²)
Output liter_cat dibulatkan ke atas
''', '''
import math
for diameter, kedalaman in [(4, 1.2), (6, 1.5)]:
    r = diameter / 2
    luas_dasar = math.pi * r ** 2
    luas_dinding = 2 * math.pi * r * kedalaman
    liter = math.ceil((luas_dasar + luas_dinding) / 10)
    print(f"kolam d={diameter} m: dasar {luas_dasar:.2f} m², dinding {luas_dinding:.2f} m² -> beli {liter} liter cat")
''', 'Rumus luas dan keliling lingkaran dipakai langsung di dunia nyata: estimasi bahan bangunan, cat, dan pagar.')]),

'Menghitung diskon belanja': dict(
  ist=[('Business rule', 'Aturan bisnis seperti "diskon 10% untuk belanja di atas Rp500.000" yang diterjemahkan ke algoritma.'),
       ('Tiered discount', 'Diskon bertingkat sesuai rentang belanja.'),
       ('Cap (maksimum diskon)', 'Batas atas diskon, misalnya "diskon 20% maks Rp50.000", umum di promo e-commerce.'),
       ('Order of operations', 'Urutan diskon, voucher, dan pajak memengaruhi total; harus disepakati dengan tim keuangan.')],
  cx=[F('Diskon bertingkat dengan batas maksimum', '''
Input belanja
If belanja >= 1000000 Then persen = 15
Else If belanja >= 500000 Then persen = 10
Else persen = 0
Assign diskon = belanja * persen / 100
If diskon > 100000 Then diskon = 100000        (maksimum Rp100.000)
Output belanja - diskon
''', '''
def bayar(belanja):
    persen = 15 if belanja >= 1_000_000 else 10 if belanja >= 500_000 else 0
    diskon = min(belanja * persen // 100, 100_000)
    return persen, diskon, belanja - diskon

for b in [300_000, 500_000, 800_000, 1_000_000, 2_500_000]:
    p, d, total = bayar(b)
    rp = lambda x: f"{x:,}".replace(",", ".")
    print(f"belanja {rp(b):>9}  diskon {p:>2}% = {rp(d):>7}  bayar {rp(total):>9}")
''', 'Perhatikan belanja Rp2.500.000: diskon 15% seharusnya Rp375.000, tetapi dibatasi Rp100.000.')]),

'Simbol If: ganjil atau genap': dict(
  ist=[('Decision symbol', 'Belah ketupat dengan dua jalur keluar: True dan False.'),
       ('Modulo test', 'n mod 2 = 0 berarti genap; pola yang sama untuk kelipatan apa pun.'),
       ('Parity', 'Sifat genap/ganjil; dipakai di checksum, pembagian giliran, dan nomor kendaraan ganjil-genap.'),
       ('Negative modulo', 'Hasil mod bilangan negatif berbeda antarbahasa; Python -3 % 2 = 1, Java -3 % 2 = -1.')],
  cx=[F('Aturan ganjil-genap kendaraan', '''
Input plat, tanggal
Assign digit = angka terakhir plat
If (digit mod 2) = (tanggal mod 2) Then
   Output "Boleh melintas"
Else
   Output "Dilarang melintas"
End If
''', '''
def boleh(plat, tanggal):
    angka = [c for c in plat if c.isdigit()]
    digit = int(angka[-1])
    return "boleh" if digit % 2 == tanggal % 2 else "DILARANG"

for plat in ["B 1234 ABC", "B 5677 XYZ", "D 2020 QQ"]:
    print(plat, "| tgl 19:", boleh(plat, 19), "| tgl 20:", boleh(plat, 20))
print("Python: -3 % 2 =", -3 % 2, "(Java memberi -1)")
''')]),

'If bersarang: nilai huruf': dict(
  ist=[('Nested if', 'If di dalam cabang If lain; mudah dibaca jika tidak lebih dari 2-3 tingkat.'),
       ('Else-if chain', 'Rangkaian If yang diperiksa berurutan dari batas tertinggi.'),
       ('Boundary value', 'Nilai tepat di batas (74, 75, 76) yang wajib diuji karena sering salah tanda > vs >=.'),
       ('Rubrik penilaian', 'Tabel konversi angka ke huruf yang ditetapkan institusi; sebaiknya disimpan sebagai data.')],
  cx=[F('Konversi nilai dengan uji nilai batas', '''
Input nilai
If nilai < 0 Or nilai > 100 Then Output "tidak valid"
Else If nilai >= 85 Then Output "A"
Else If nilai >= 75 Then Output "B"
Else If nilai >= 60 Then Output "C"
Else If nilai >= 45 Then Output "D"
Else Output "E"
''', '''
def huruf(n):
    if n < 0 or n > 100: return "tidak valid"
    elif n >= 85: return "A"
    elif n >= 75: return "B"
    elif n >= 60: return "C"
    elif n >= 45: return "D"
    else: return "E"

uji_batas = [-1, 0, 44, 45, 59, 60, 74, 75, 84, 85, 100, 101]
print(" ".join(f"{n}:{huruf(n)}" for n in uji_batas))
''', 'Daftar uji di atas adalah teknik boundary value analysis: menguji tepat di setiap batas dan satu angka di sekitarnya.')]),

'Simbol For: tabel perkalian dan hitung mundur': dict(
  ist=[('Counter-controlled loop', 'Perulangan dengan penghitung dari nilai awal ke nilai akhir.'),
       ('Step', 'Besar langkah; step -1 untuk hitung mundur, step 5 untuk loncat lima.'),
       ('Inclusive range', 'For Flowgorithm 1 to 10 termasuk 10; range Python tidak termasuk batas akhir.'),
       ('Nested For', 'For di dalam For untuk tabel dua dimensi seperti tabel perkalian.')],
  cx=[F('Tabel perkalian dan hitung mundur peluncuran', '''
For i = 1 to 5
   For j = 1 to 5
      Output i * j (tanpa pindah baris)
   End For
   Output baris baru
End For
For t = 10 to 0 step -2
   Output t
End For
''', '''
print("   " + "".join(f"{j:>4}" for j in range(1, 6)))
for i in range(1, 6):                       # 1 to 5 -> range(1, 6)
    print(f"{i:>2} " + "".join(f"{i * j:>4}" for j in range(1, 6)))
print("hitung mundur:", [t for t in range(10, -1, -2)])   # 10 to 0 step -2 -> range(10, -1, -2)
''')]),

'Deret Fibonacci dan faktorial': dict(
  ist=[('Accumulator', 'Variabel yang terus diperbarui: jumlah, hasil kali, atau dua suku terakhir deret.'),
       ('Factorial growth', 'n! tumbuh sangat cepat; 21! sudah melewati batas Integer 64-bit.'),
       ('Overflow', 'Nilai melebihi kapasitas tipe; Flowgorithm/Java Integer bisa meluap, int Python tidak.'),
       ('Permutasi', 'n! adalah banyaknya cara menyusun n benda berbeda; dipakai di penjadwalan dan peluang.')],
  cx=[F('Faktorial sebagai banyak cara menyusun jadwal', '''
Input n
Assign hasil = 1
For i = 1 to n
   Assign hasil = hasil * i
End For
Output hasil
''', '''
BATAS_INT64 = 2 ** 63 - 1
hasil = 1
for n in range(1, 23):
    hasil *= n
    if n in (5, 10, 20, 21, 22):
        catatan = "  <- melewati batas Integer 64-bit" if hasil > BATAS_INT64 else ""
        print(f"{n:>2}! = {hasil:,}{catatan}".replace(",", "."))
print("Cara menyusun urutan presentasi 8 kelompok:", f"{1 * 2 * 3 * 4 * 5 * 6 * 7 * 8:,}".replace(",", "."))

a, b = 0, 1
deret = []
for _ in range(12): deret.append(a); a, b = b, a + b
print("Fibonacci:", deret)
''')]),

'Simbol While: tebak angka': dict(
  ist=[('Pre-test loop', 'While memeriksa kondisi sebelum badan loop; bisa tidak jalan sama sekali.'),
       ('Sentinel', 'Kondisi berhenti dari data (tebakan benar), bukan dari jumlah putaran.'),
       ('Binary search strategy', 'Strategi menebak di tengah rentang; menebak angka 1-100 butuh paling banyak 7 kali.'),
       ('Max attempts', 'Batas percobaan agar loop pasti berhenti; dipakai juga di login (blokir setelah 5 kali salah).')],
  cx=[F('Komputer menebak angka dengan strategi tengah', '''
Assign bawah = 1, atas = 100, coba = 0
While tebakan <> rahasia
   Assign tebakan = (bawah + atas) div 2
   Assign coba = coba + 1
   If tebakan < rahasia Then bawah = tebakan + 1
   Else If tebakan > rahasia Then atas = tebakan - 1
End While
Output coba
''', '''
def tebak(rahasia):
    bawah, atas, coba, tebakan = 1, 100, 0, None
    while tebakan != rahasia:
        tebakan = (bawah + atas) // 2
        coba += 1
        if tebakan < rahasia: bawah = tebakan + 1
        elif tebakan > rahasia: atas = tebakan - 1
    return coba

for r in [50, 1, 100, 37, 73]:
    print(f"rahasia {r:>3}: tertebak dalam {tebak(r)} kali")
print("paling banyak:", max(tebak(r) for r in range(1, 101)), "kali untuk semua angka 1-100")
''')]),

'Simbol Do: menu yang berulang': dict(
  ist=[('Post-test loop', 'Do memeriksa kondisi setelah badan loop, jadi badan loop jalan minimal sekali.'),
       ('Menu-driven program', 'Program yang menampilkan menu, membaca pilihan, lalu mengulang sampai pengguna keluar.'),
       ('Input validation loop', 'Do-while untuk meminta input ulang sampai valid.'),
       ('State', 'Data yang bertahan antarputaran menu, misalnya saldo atau isi keranjang.')],
  cx=[F('Menu ATM sederhana (pilihan disimulasikan)', '''
Assign saldo = 500000
Do
   Output "1 Cek saldo  2 Tarik  0 Keluar"
   Input pilihan
   If pilihan = 1 Then Output saldo
   If pilihan = 2 Then Input jumlah ; If jumlah <= saldo Then saldo = saldo - jumlah
Loop While pilihan <> 0
''', '''
saldo = 500_000
masukan = iter([("1", 0), ("2", 200_000), ("2", 900_000), ("1", 0), ("0", 0)])
rp = lambda x: f"Rp{x:,}".replace(",", ".")
while True:
    pilihan, jumlah = next(masukan)
    if pilihan == "1": print("saldo:", rp(saldo))
    elif pilihan == "2":
        if jumlah <= saldo: saldo -= jumlah; print("tarik", rp(jumlah), "berhasil")
        else: print("tarik", rp(jumlah), "ditolak: saldo tidak cukup")
    if pilihan == "0": print("terima kasih"); break
''')]),

'Array dengan input': dict(
  ist=[('Array', 'Kumpulan nilai bertipe sama yang diakses dengan indeks; di Flowgorithm indeks mulai 0.'),
       ('Fixed size', 'Ukuran array Flowgorithm ditetapkan saat Declare; tidak bisa bertambah.'),
       ('Index out of bounds', 'Error saat mengakses indeks di luar 0..ukuran-1.'),
       ('Parallel arrays', 'Dua array yang indeksnya saling berpasangan (nama[i] dengan nilai[i]).')],
  cx=[F('Rekap nilai kelas dengan array', '''
Declare String nama[5]
Declare Integer nilai[5]
For i = 0 to 4
   Input nama[i], nilai[i]
End For
Hitung rata-rata, tertinggi, dan yang di bawah KKM 70
''', '''
nama = ["Ani", "Budi", "Citra", "Dedi", "Eka"]          # input disimulasikan
nilai = [88, 65, 92, 70, 58]
rata = sum(nilai) / len(nilai)
i_max = 0
for i in range(1, len(nilai)):
    if nilai[i] > nilai[i_max]: i_max = i
print(f"rata-rata {rata:.1f}, tertinggi {nama[i_max]} ({nilai[i_max]})")
print("remedial (< 70):", [nama[i] for i in range(len(nilai)) if nilai[i] < 70])
try:
    print(nilai[5])
except IndexError:
    print("nilai[5] -> error: indeks hanya 0 sampai 4")
''')]),

'Fungsi dan simbol Call': dict(
  ist=[('Function', 'Sub-program dengan nama, parameter, dan nilai kembali (Return).'),
       ('Call', 'Simbol untuk menjalankan fungsi tanpa memakai nilai kembalinya (prosedur).'),
       ('Modularity', 'Memecah flowchart besar menjadi fungsi kecil agar mudah dibaca, diuji, dan dipakai ulang.'),
       ('Parameter passing', 'Mengirim nilai ke fungsi; di Flowgorithm parameter dikirim sebagai salinan nilai.')],
  cx=[F('Fungsi BMI dan prosedur cetak laporan', '''
Function HitungBMI(Real berat, Real tinggi) Return Real
   Return berat / (tinggi ^ 2)
Function Kategori(Real bmi) Return String
   If bmi < 18.5 ... "Kurus" / < 25 "Normal" / < 30 "Gemuk" / lainnya "Obesitas"
Main
   Call CetakLaporan(nama, berat, tinggi)     (prosedur memanggil kedua fungsi)
''', '''
def hitung_bmi(berat, tinggi):
    return berat / tinggi ** 2

def kategori(bmi):
    if bmi < 18.5: return "Kurus"
    if bmi < 25: return "Normal"
    if bmi < 30: return "Gemuk"
    return "Obesitas"

def cetak_laporan(nama, berat, tinggi):
    bmi = hitung_bmi(berat, tinggi)
    print(f"{nama:<6} {berat:>5.1f} kg {tinggi:.2f} m  BMI {bmi:5.1f}  {kategori(bmi)}")

for data in [("Rudi", 52, 1.75), ("Sinta", 58, 1.62), ("Bayu", 85, 1.70), ("Tono", 102, 1.68)]:
    cetak_laporan(*data)
''')]),

'Proyek: kasir dengan diskon': dict(
  ist=[('POS (Point of Sale)', 'Sistem kasir: mencatat item, menghitung total, diskon, pajak, dan pembayaran.'),
       ('Subtotal / PPN / grand total', 'Urutan perhitungan struk; PPN dihitung dari harga setelah diskon.'),
       ('Change calculation', 'Menghitung kembalian dan memecahnya ke pecahan uang yang tersedia.'),
       ('Greedy algorithm', 'Mengambil pecahan terbesar dulu; tepat untuk sistem pecahan rupiah.')],
  cx=[F('Kasir lengkap: diskon, PPN, dan pecahan kembalian', '''
Input daftar item (harga, qty) sampai selesai
Assign subtotal = jumlah harga * qty
If subtotal >= 200000 Then diskon = 5%
Assign ppn = (subtotal - diskon) * 11%
Assign total = subtotal - diskon + ppn
Input uang ; Assign kembali = uang - total
For setiap pecahan dari terbesar: lembar = kembali div pecahan ; kembali = kembali mod pecahan
''', '''
item = [("Kopi susu", 28_000, 5), ("Croissant", 22_000, 2), ("Air mineral", 6_000, 4)]
rp = lambda x: f"Rp{x:,}".replace(",", ".")
subtotal = sum(h * q for _, h, q in item)
diskon = subtotal * 5 // 100 if subtotal >= 200_000 else 0
ppn = round((subtotal - diskon) * 0.11)
total = subtotal - diskon + ppn
for n, h, q in item: print(f"{n:<12} {q} x {rp(h):>9} = {rp(h * q):>10}")
print(f"subtotal {rp(subtotal)}, diskon {rp(diskon)}, PPN {rp(ppn)}, TOTAL {rp(total)}")

uang = 250_000
kembali = uang - total
print("bayar", rp(uang), "-> kembali", rp(kembali))
for pecahan in [100_000, 50_000, 20_000, 10_000, 5_000, 2_000, 1_000, 500, 200, 100]:
    lembar, kembali = divmod(kembali, pecahan)
    if lembar: print(f"  {lembar} x {rp(pecahan)}")
if kembali: print("  sisa", rp(kembali), "dibulatkan/didonasikan")
''')]),

'Dari flowchart ke kode: Source Code Viewer': dict(
  ist=[('Code generation', 'Flowgorithm menerjemahkan flowchart ke berbagai bahasa (Python, Java, C++, C#, JavaScript) lewat Source Code Viewer.'),
       ('Transpiler', 'Alat yang menerjemahkan satu bahasa sumber ke bahasa sumber lain.'),
       ('Idiomatic code', 'Kode yang ditulis sesuai gaya alami bahasanya; hasil generator biasanya perlu dirapikan.'),
       ('Low-code', 'Platform yang membangun aplikasi lewat diagram (OutSystems, Power Apps); ide yang sama dengan Flowgorithm.')],
  cx=[T('Kode hasil generator vs kode Python idiomatik', '''
# Hasil Source Code Viewer (gaya generator)        # Versi idiomatik setelah dirapikan
def Main():                                         def main():
    nilai = [0] * (5)                                   nilai = [88, 65, 92, 70, 58]
    total = 0                                           print(sum(nilai) / len(nilai))
    for i in range(0, 4 + 1, 1):
        nilai[i] = int(input())                     if __name__ == "__main__":
        total = total + nilai[i]                        main()
    rata = float(total) / 5
    print(rata)

Main()'''),
     F('Terjemahan yang sama dalam gaya idiomatik, dijalankan', '''
Declare Integer nilai[5], total
For i = 0 to 4
   Input nilai[i]
   Assign total = total + nilai[i]
End For
Output total / 5
''', '''
def main():
    nilai = [88, 65, 92, 70, 58]      # pengganti Input
    print("rata-rata:", sum(nilai) / len(nilai))

if __name__ == "__main__":
    main()
''', 'range(0, 4 + 1, 1) dari generator benar tetapi kaku. Programmer Python cukup menulis sum(nilai).')]),
}
