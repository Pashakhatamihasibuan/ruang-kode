"""Pendalaman jalur Python (bagian 1: fondasi sampai struktur data bawaan). Contoh dijalankan dengan CPython 3.13."""
K = 'python'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)



D = {
'Program Pertama': dict(
  ist=[('Interpreter', 'Program yang membaca dan menjalankan kode Python baris demi baris; yang umum dipakai adalah CPython.'),
       ('REPL', 'Read-Eval-Print Loop: mode interaktif (perintah python tanpa berkas) untuk mencoba kode cepat.'),
       ('Script', 'Berkas .py yang dijalankan dari terminal dengan python nama_berkas.py.'),
       ('Entry point', 'Blok if __name__ == "__main__": sebagai titik mulai saat berkas dijalankan langsung, bukan diimpor.')],
  cx=[P('Informasi lingkungan dan entry point', '''
import sys, platform

def main():
    print("Halo dari Python", platform.python_version())
    print("Implementasi:", platform.python_implementation())
    print("Versi minimal terpenuhi:", sys.version_info >= (3, 10))

if __name__ == "__main__":
    main()
''', 'Tim biasanya mencatat versi Python minimal di pyproject.toml. Memeriksa sys.version_info di awal mencegah error membingungkan di server lama.')]),

'Struktur program & statement': dict(
  ist=[('Statement', 'Satu perintah lengkap, umumnya satu baris: assignment, pemanggilan fungsi, return.'),
       ('Indentasi blok', 'Python memakai indentasi (standar 4 spasi) untuk menandai isi blok, bukan kurung kurawal.'),
       ('PEP 8', 'Panduan gaya resmi Python: penamaan snake_case, panjang baris, spasi di sekitar operator.'),
       ('Docstring', 'String di baris pertama modul, fungsi, atau kelas yang menjelaskan tujuannya; terbaca oleh help().')],
  cx=[P('Program kecil dengan struktur rapi', '''
"""Menghitung total belanja dengan PPN. Modul contoh struktur program."""

PPN = 0.11  # konstanta di tingkat modul, huruf besar

def total_bayar(subtotal: int) -> int:
    """Kembalikan subtotal ditambah PPN, dibulatkan ke rupiah."""
    return round(subtotal * (1 + PPN))

keranjang = [45_000, 120_000, 18_500]
print("Subtotal:", sum(keranjang))
print("Total + PPN:", total_bayar(sum(keranjang)))
print("Dokumentasi:", total_bayar.__doc__)
''', 'Urutan yang lazim: docstring modul, import, konstanta, fungsi, lalu kode yang dijalankan.')]),

'Variabel': dict(
  ist=[('snake_case', 'Konvensi nama variabel dan fungsi di Python: total_harga, jumlah_siswa.'),
       ('Dynamic typing', 'Tipe melekat pada nilai, bukan pada nama; satu nama bisa menunjuk nilai bertipe lain.'),
       ('Name binding', 'Assignment mengikat nama ke objek; x = y membuat dua nama ke objek yang sama.'),
       ('Magic number', 'Angka tanpa nama di tengah kode; ganti dengan konstanta bernama agar maksudnya jelas.')],
  cx=[P('Nama bermakna dan konstanta', '''
JAM_KERJA_PER_HARI = 8
UPAH_PER_JAM = 25_000
hari_masuk = 22
gaji_kotor = hari_masuk * JAM_KERJA_PER_HARI * UPAH_PER_JAM
print(f"Gaji kotor: Rp{gaji_kotor:,}".replace(",", "."))

# satu nama bisa diikat ulang ke tipe lain (boleh, tapi membingungkan)
status = 1
status = "aktif"
print(type(status).__name__, status)
''', 'Mengikat ulang nama ke tipe berbeda itu sah, tetapi reviewer biasanya memintanya dihindari karena menyulitkan pembaca dan type checker.')]),

'Tipe data & typecasting': dict(
  ist=[('int, float, str, bool', 'Empat tipe dasar: bilangan bulat, desimal, teks, dan benar/salah.'),
       ('Type conversion', 'Mengubah tipe secara eksplisit: int("42"), float("3.5"), str(10).'),
       ('Floating point error', 'Desimal biner tidak selalu tepat: 0.1 + 0.2 bukan 0.3 persis.'),
       ('Decimal', 'Tipe dari modul decimal untuk uang dan perhitungan yang harus presisi.')],
  cx=[P('Kenapa uang tidak disimpan sebagai float', '''
from decimal import Decimal, ROUND_HALF_UP

print(0.1 + 0.2, "==", 0.3, "?", 0.1 + 0.2 == 0.3)
harga = Decimal("19999.99")
qty = 3
total = (harga * qty).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
print("Decimal:", harga * qty, "-> dibulatkan", total)
print("int('042') =", int("042"), "| float('2.5') =", float("2.5"), "| bool('') =", bool(""))
''', 'Sistem keuangan menyimpan uang sebagai Decimal atau sebagai bilangan bulat dalam satuan terkecil (sen/rupiah), tidak pernah float.')]),

'Ekspresi & operator': dict(
  ist=[('Operator precedence', 'Urutan pengerjaan: ** lalu * / // % lalu + -; gunakan kurung agar maksud jelas.'),
       ('Floor division', '// membagi lalu membulatkan ke bawah: 7 // 2 = 3, -7 // 2 = -4.'),
       ('Modulo', '% memberi sisa bagi; dipakai untuk genap/ganjil, siklus, dan pembagian rata.'),
       ('Augmented assignment', 'Bentuk singkat seperti +=, -=, *= untuk memperbarui nilai.')],
  cx=[P('Membagi tagihan dan mengonversi durasi', '''
tagihan, orang = 250_000, 3
print("Tiap orang:", tagihan // orang, "| sisa:", tagihan % orang)

detik = 9_876
jam, sisa = divmod(detik, 3600)
menit, dtk = divmod(sisa, 60)
print(f"{detik} detik = {jam} jam {menit} menit {dtk} detik")
print("Precedence 2 + 3 * 4 =", 2 + 3 * 4, "| (2 + 3) * 4 =", (2 + 3) * 4)
''', 'divmod mengembalikan hasil bagi dan sisa sekaligus, pola yang sering dipakai untuk mengubah satuan waktu.')]),

'Operator lengkap: //, **, walrus, dan @': dict(
  ist=[('Exponentiation', '** untuk pangkat; pow(a, b, m) untuk pangkat modulo yang cepat.'),
       ('Walrus operator', ':= (Python 3.8+) mengisi variabel sekaligus memakai nilainya di dalam ekspresi.'),
       ('Matrix multiplication', '@ dipakai NumPy dan pustaka sains untuk perkalian matriks.'),
       ('Chained comparison', '0 <= x < 10 ditulis langsung, setara dengan 0 <= x and x < 10.')],
  cx=[P('Bunga majemuk, walrus, dan @ pada kelas sendiri', '''
modal, bunga, tahun = 10_000_000, 0.06, 5
print(f"Bunga majemuk {tahun} th: Rp{modal * (1 + bunga) ** tahun:,.0f}".replace(",", "."))

log = ["OK", "OK", "ERROR disk penuh", "OK", "ERROR timeout"]
if (n := sum("ERROR" in b for b in log)) > 1:
    print(f"Peringatan: {n} error")

class Matriks:
    def __init__(self, d): self.d = d
    def __matmul__(self, o):
        return Matriks([[sum(a * b for a, b in zip(r, k)) for k in zip(*o.d)] for r in self.d])
print((Matriks([[1, 2], [3, 4]]) @ Matriks([[5, 6], [7, 8]])).d)
print("suhu 0 <= 25 < 40:", 0 <= 25 < 40)
''')]),

'Membaca input pengguna': dict(
  ist=[('input()', 'Membaca satu baris dari keyboard; hasilnya selalu str.'),
       ('Input validation', 'Memeriksa input sebelum dipakai: tipe, rentang, dan format.'),
       ('sys.argv / argparse', 'Cara menerima input dari argumen terminal, umum untuk skrip otomasi.'),
       ('Never trust user input', 'Prinsip keamanan: setiap input dianggap salah atau berbahaya sampai terbukti valid.')],
  cx=[P('Validasi input dengan pesan yang jelas (input disimulasikan)', '''
def minta_umur(teks):
    teks = teks.strip()
    if not teks.isdigit():
        return None, f"'{teks}' bukan bilangan bulat positif"
    umur = int(teks)
    if not 17 <= umur <= 100:
        return None, f"umur {umur} di luar 17-100"
    return umur, "ok"

for masukan in ["25", " 30 ", "dua puluh", "-5", "150"]:
    print(repr(masukan), "->", minta_umur(masukan))
''', 'Di halaman, nilai diberikan langsung karena tidak ada keyboard. Di program nyata, gantilah dengan minta_umur(input("Umur: ")).'),
     P('Argumen terminal dengan argparse', '''
import argparse
p = argparse.ArgumentParser(description="Hitung cicilan")
p.add_argument("pokok", type=int)
p.add_argument("--tenor", type=int, default=12)
args = p.parse_args(["6000000", "--tenor", "6"])   # di terminal: python cicilan.py 6000000 --tenor 6
print(f"Cicilan: Rp{args.pokok // args.tenor:,}/bulan".replace(",", "."))
''', 'argparse otomatis membuat --help dan menolak input yang tipenya salah.')]),

'Fungsi (memecah program)': dict(
  ist=[('Decomposition', 'Memecah masalah besar menjadi fungsi kecil yang masing-masing punya satu tugas.'),
       ('Single Responsibility', 'Satu fungsi, satu alasan untuk berubah.'),
       ('Pure function', 'Fungsi tanpa efek samping: input sama selalu memberi output sama; mudah diuji.'),
       ('DRY', "Don't Repeat Yourself: logika yang dipakai berulang dijadikan fungsi.")],
  cx=[P('Memecah proses gaji menjadi fungsi kecil', '''
def gaji_pokok(hari, upah_harian):
    return hari * upah_harian

def lembur(jam, tarif=40_000):
    return jam * tarif

def potongan_bpjs(bruto, persen=0.04):
    return round(bruto * persen)

def slip(nama, hari, jam_lembur):
    bruto = gaji_pokok(hari, 180_000) + lembur(jam_lembur)
    neto = bruto - potongan_bpjs(bruto)
    return f"{nama:<6} bruto {bruto:>10,}  neto {neto:>10,}".replace(",", ".")

for n, h, j in [("Sari", 22, 5), ("Doni", 20, 0)]:
    print(slip(n, h, j))
''', 'Setiap fungsi bisa diuji sendiri. Jika tarif lembur berubah, hanya satu tempat yang diubah.')]),

'Parameter & return': dict(
  ist=[('Parameter vs argumen', 'Parameter adalah nama di definisi fungsi; argumen adalah nilai yang dikirim saat memanggil.'),
       ('Return value', 'Nilai yang dikirim balik fungsi; tanpa return, fungsi mengembalikan None.'),
       ('Multiple return', 'Mengembalikan beberapa nilai sekaligus sebagai tuple, lalu di-unpack.'),
       ('Guard clause', 'return lebih awal untuk kasus khusus agar alur utama tidak bersarang dalam.')],
  cx=[P('Guard clause dan beberapa nilai kembali', '''
def statistik(nilai):
    if not nilai:                         # guard clause
        return None, None, None
    return min(nilai), max(nilai), sum(nilai) / len(nilai)

terendah, tertinggi, rata = statistik([78, 92, 65, 88, 71])
print(f"min {terendah}, max {tertinggi}, rata-rata {rata:.1f}")
print("data kosong:", statistik([]))

def cetak(x):
    print("isi:", x)
print("fungsi tanpa return mengembalikan:", cetak("halo"))
''')]),

'Argumen default, keyword, *args, **kwargs': dict(
  ist=[('Default argument', 'Nilai bawaan parameter jika argumen tidak dikirim.'),
       ('Mutable default trap', 'Default berupa list/dict dibuat sekali dan dipakai bersama; gunakan None lalu buat baru.'),
       ('Keyword-only argument', 'Parameter setelah * wajib dipanggil dengan nama, mencegah salah urutan.'),
       ('*args / **kwargs', 'Menampung argumen posisi dan argumen bernama yang jumlahnya bebas.')],
  cx=[P('Jebakan default mutable dan argumen keyword-only', '''
def tambah_salah(item, keranjang=[]):
    keranjang.append(item); return keranjang

def tambah_benar(item, keranjang=None):
    keranjang = [] if keranjang is None else keranjang
    keranjang.append(item); return keranjang

print(tambah_salah("apel"), tambah_salah("jeruk"))     # list yang sama dipakai ulang!
print(tambah_benar("apel"), tambah_benar("jeruk"))

def transfer(dari, ke, *, jumlah, catatan=""):
    return f"{dari} -> {ke}: {jumlah:,} {catatan}".replace(",", ".")
print(transfer("BCA-01", "BRI-07", jumlah=1_500_000, catatan="(sewa)"))

def log(level, *pesan, **konteks):
    print(f"[{level}]", " ".join(pesan), konteks)
log("INFO", "user", "login", user_id=42, ip="10.0.0.5")
''', 'Keyword-only membuat panggilan seperti transfer(a, b, jumlah=...) tidak bisa tertukar antara jumlah dan argumen lain.')]),

'Scope variabel: aturan LEGB': dict(
  ist=[('LEGB', 'Urutan pencarian nama: Local, Enclosing, Global, Built-in.'),
       ('global / nonlocal', 'Kata kunci untuk mengubah variabel di scope global atau fungsi luar.'),
       ('Closure', 'Fungsi dalam yang mengingat variabel dari fungsi luarnya walau fungsi luar sudah selesai.'),
       ('Shadowing', 'Nama lokal menutupi nama luar, misalnya variabel bernama list atau sum yang menutupi built-in.')],
  cx=[P('Closure sebagai penghitung dan bahaya shadowing', '''
def buat_penghitung(awal=0):
    n = awal
    def berikutnya():
        nonlocal n
        n += 1
        return f"INV-{n:04d}"
    return berikutnya

nomor_invoice = buat_penghitung(41)
print(nomor_invoice(), nomor_invoice(), nomor_invoice())

def rata_rata(data):
    sum = 0                 # shadowing built-in sum di dalam fungsi ini
    for x in data: sum += x
    return sum / len(data)
print(rata_rata([4, 5, 6]), "| built-in sum tetap aman di luar:", sum([1, 2, 3]))
''', 'Linter seperti ruff memberi peringatan A001/A002 untuk nama yang menutupi built-in.')]),

'String': dict(
  ist=[('Immutable', 'String tidak bisa diubah di tempat; setiap operasi membuat string baru.'),
       ('Unicode', 'String Python menyimpan karakter Unicode; len() menghitung karakter, bukan byte.'),
       ('Encoding (UTF-8)', 'Cara mengubah teks menjadi byte untuk disimpan atau dikirim; standar web adalah UTF-8.'),
       ('Normalization', 'Merapikan teks sebelum dibandingkan: strip, lower/casefold, menghapus spasi ganda.')],
  cx=[P('Merapikan data nama dari formulir', '''
mentah = ["  budi SANTOSO ", "Siti  Aminah", "ANDI", "rené"]
for n in mentah:
    rapi = " ".join(n.split()).title()
    print(f"{n!r:<18} -> {rapi!r:<16} karakter {len(rapi)}, byte UTF-8 {len(rapi.encode())}")
print("casefold untuk membandingkan:", "Straße".casefold() == "STRASSE".casefold())
''', '"rené" punya 4 karakter tetapi 5 byte UTF-8. Ini penting saat kolom database dibatasi per byte.')]),

'f-string, slicing & method string': dict(
  ist=[('f-string', 'String berawalan f yang menyisipkan ekspresi di dalam {}; mendukung format seperti :,.2f dan :>10.'),
       ('Slicing', 's[awal:akhir:langkah]; indeks negatif menghitung dari belakang.'),
       ('Masking', 'Menyembunyikan sebagian data sensitif (NIK, nomor kartu) sebelum ditampilkan atau dicatat di log.'),
       ('str.join', 'Cara efisien menggabungkan banyak string; lebih cepat daripada + berulang.')],
  cx=[P('Masking data pribadi dan format laporan', '''
def mask(s, tampil=4):
    return "*" * (len(s) - tampil) + s[-tampil:]

nik, kartu, email = "3201123456780001", "4111111111111111", "budi.santoso@contoh.id"
print("NIK  :", mask(nik))
print("Kartu:", " ".join(mask(kartu)[i:i + 4] for i in range(0, 16, 4)))
user, domain = email.split("@")
print("Email:", user[0] + "*" * (len(user) - 2) + user[-1] + "@" + domain)
print(f"{'Produk':<10}|{'Harga':>12}|\\n{'Kopi':<10}|{18000:>12,.0f}|".replace(",", "."))
''', 'UU PDP mewajibkan perlindungan data pribadi. Masking di log dan tampilan adalah praktik standar.')]),

'Eksekusi Bersyarat': dict(
  ist=[('Branching', 'Program memilih jalur berbeda berdasarkan kondisi.'),
       ('Truthy / falsy', 'Nilai yang dianggap salah: 0, "", [], {}, None, False; selain itu dianggap benar.'),
       ('Business rule', 'Aturan bisnis (diskon, kelulusan, kelayakan kredit) yang diterjemahkan menjadi percabangan.'),
       ('Edge case', 'Nilai batas atau tak biasa yang sering memicu bug: 0, negatif, kosong, tepat di batas.')],
  cx=[P('Aturan ongkir dengan edge case', '''
def ongkir(total, jarak_km, member):
    if total <= 0:
        return "pesanan tidak valid"
    if member and total >= 100_000:
        return 0
    if jarak_km <= 5:
        return 8_000
    return 8_000 + (jarak_km - 5) * 2_000

for kasus in [(150_000, 12, True), (99_999, 3, True), (50_000, 9, False), (0, 2, False)]:
    print(kasus, "->", ongkir(*kasus))
print("list kosong falsy:", not [], "| None falsy:", not None)
''')]),

'if / elif / else': dict(
  ist=[('Mutually exclusive', 'Hanya satu cabang if/elif/else yang dijalankan, yaitu cabang pertama yang benar.'),
       ('Order matters', 'Urutan elif penting; kondisi paling spesifik ditulis lebih dulu.'),
       ('Lookup table', 'Mengganti rantai elif panjang dengan dict atau daftar ambang.'),
       ('bisect', 'Modul untuk mencari posisi nilai di daftar terurut; cocok untuk tabel ambang.')],
  cx=[P('Rantai elif vs tabel ambang dengan bisect', '''
from bisect import bisect_right

def huruf_elif(n):
    if n >= 85: return "A"
    elif n >= 75: return "B"
    elif n >= 65: return "C"
    elif n >= 50: return "D"
    else: return "E"

AMBANG, HURUF = [50, 65, 75, 85], "EDCBA"
def huruf_tabel(n):
    return HURUF[bisect_right(AMBANG, n)]

for n in [49, 50, 74, 75, 100]:
    print(n, huruf_elif(n), huruf_tabel(n))
''', 'Tabel ambang lebih mudah diubah oleh bagian akademik tanpa menyentuh logika, dan cocok disimpan di konfigurasi.')]),

'match-case & ekspresi kondisional': dict(
  ist=[('Structural pattern matching', 'match-case (Python 3.10+) mencocokkan bentuk data, bukan hanya nilai.'),
       ('Guard', 'Kondisi tambahan di pola: case {"jumlah": j} if j > 0.'),
       ('Wildcard _', 'Pola yang cocok dengan apa pun; dipakai sebagai cabang default.'),
       ('Conditional expression', 'Bentuk satu baris: a if kondisi else b.')],
  cx=[P('Memproses event webhook pembayaran dengan match-case', '''
def proses(event):
    match event:
        case {"type": "payment.paid", "amount": int(j)} if j > 0:
            return f"tandai lunas Rp{j:,}".replace(",", ".")
        case {"type": "payment.failed", "reason": alasan}:
            return f"kirim notifikasi gagal: {alasan}"
        case {"type": "refund", "amount": j, "order": [*items]}:
            return f"refund {j} untuk {len(items)} item"
        case {"type": t}:
            return f"abaikan event {t}"
        case _:
            return "payload tidak dikenal"

for e in [{"type": "payment.paid", "amount": 125000}, {"type": "payment.failed", "reason": "saldo kurang"},
          {"type": "refund", "amount": 5000, "order": ["A1", "B2"]}, {"type": "ping"}, "rusak"]:
    print(proses(e))
status = "aktif" if 125000 > 0 else "nonaktif"
print(status)
''', 'Payment gateway mengirim JSON dengan bentuk berbeda per jenis event. match-case membuat tiap bentuk terbaca jelas.')]),

'Algoritma kumulatif': dict(
  ist=[('Accumulator', 'Variabel yang menampung hasil berjalan: total, jumlah, maksimum.'),
       ('Running total', 'Jumlah berjalan per langkah, misalnya saldo setelah tiap transaksi.'),
       ('itertools.accumulate', 'Fungsi bawaan untuk menghasilkan running total atau running max.'),
       ('Initialization', 'Nilai awal akumulator harus tepat: 0 untuk jumlah, 1 untuk perkalian, elemen pertama untuk maksimum.')],
  cx=[P('Saldo berjalan rekening dan titik terendah', '''
from itertools import accumulate
mutasi = [500_000, -120_000, -75_000, 1_200_000, -900_000, -950_000, 300_000]
saldo_awal = 200_000
saldo = list(accumulate(mutasi, initial=saldo_awal))
for m, s in zip(mutasi, saldo[1:]):
    print(f"{m:>+10,}  saldo {s:>10,}{'  <-- minus!' if s < 0 else ''}".replace(",", "."))
print("Saldo terendah:", f"{min(saldo):,}".replace(",", "."))
''', 'Bank memakai pola ini untuk mendeteksi overdraft dan menghitung saldo rata-rata harian.')]),

'Data Primitif & Perulangan Pasti': dict(
  ist=[('Definite loop', 'Perulangan yang jumlah putarannya diketahui sebelum mulai, misalnya for i in range(n).'),
       ('range(start, stop, step)', 'Deret bilangan tanpa membuat list; stop tidak ikut.'),
       ('Off-by-one error', 'Bug karena batas loop kurang atau lebih satu.'),
       ('Iteration', 'Satu kali putaran loop.')],
  cx=[P('Jadwal cicilan dengan perulangan pasti', '''
pokok, tenor, bunga_bln = 6_000_000, 6, 0.01
angsuran_pokok = pokok // tenor
sisa = pokok
print("ke  pokok      bunga    angsuran   sisa")
for ke in range(1, tenor + 1):           # tenor + 1 karena stop tidak ikut
    bunga = round(sisa * bunga_bln)
    sisa -= angsuran_pokok
    print(f"{ke:>2} {angsuran_pokok:>9,} {bunga:>8,} {angsuran_pokok + bunga:>10,} {sisa:>10,}".replace(",", "."))
''', 'Skema ini disebut bunga efektif (menurun): bunga dihitung dari sisa pokok, sehingga angsuran makin kecil.')]),

'Perulangan for': dict(
  ist=[('Iterable', 'Objek yang bisa dilewati satu per satu: list, str, dict, file, range.'),
       ('for-each', 'for di Python selalu berjalan langsung atas elemen, bukan atas indeks.'),
       ('Loop variable', 'Nama yang menerima tiap elemen; tetap ada setelah loop selesai.'),
       ('Iterating dict', 'for k, v in d.items() untuk kunci dan nilai sekaligus.')],
  cx=[P('Rekap stok per gudang', '''
stok = {"Jakarta": {"beras": 120, "gula": 40}, "Bandung": {"beras": 35, "gula": 80}, "Medan": {"beras": 0, "gula": 15}}
for gudang, isi in stok.items():
    total = 0
    for barang, qty in isi.items():
        total += qty
    habis = [b for b, q in isi.items() if q == 0]
    print(f"{gudang:<8} total {total:>4} unit{'  habis: ' + ', '.join(habis) if habis else ''}")
''')]),

'Loop bersarang (nested loop)': dict(
  ist=[('Nested loop', 'Loop di dalam loop; jumlah kerja = putaran luar x putaran dalam.'),
       ('O(n²)', 'Kompleksitas khas loop bersarang atas data yang sama; lambat untuk data besar.'),
       ('Cartesian product', 'Semua pasangan dari dua himpunan; itertools.product menggantikan loop bersarang.'),
       ('Early exit', 'Keluar dari loop bersarang lebih awal, misalnya dengan return di dalam fungsi.')],
  cx=[P('Mencari pasangan transaksi kembar: O(n²) vs set', '''
import time
trx = [f"TRX{i}" for i in range(3000)] + ["TRX1500"]

t0 = time.perf_counter()
kembar = next((a for i, a in enumerate(trx) for b in trx[i + 1:] if a == b), None)
t_nested = time.perf_counter() - t0

t0 = time.perf_counter()
dilihat = set()
for a in trx:
    if a in dilihat:
        kembar2 = a; break
    dilihat.add(a)
t_set = time.perf_counter() - t0
print("nested:", kembar, "| set:", kembar2)
print("set jauh lebih cepat:", t_set * 50 < t_nested)
''', 'Waktu persisnya berbeda di tiap komputer, tetapi selisihnya selalu besar: jutaan perbandingan vs ribuan pengecekan set.')]),

'Logika & Perulangan Tak Pasti': dict(
  ist=[('Indefinite loop', 'Perulangan yang berhenti saat kondisi tertentu terpenuhi, jumlah putarannya tidak diketahui di awal.'),
       ('Sentinel value', 'Nilai khusus penanda akhir data, misalnya 0 atau "selesai".'),
       ('Retry with backoff', 'Mengulang operasi yang gagal dengan jeda yang makin lama; pola standar untuk jaringan.'),
       ('Infinite loop', 'Loop yang tidak pernah berhenti karena kondisinya tidak pernah salah.')],
  cx=[P('Retry dengan exponential backoff (jaringan disimulasikan)', '''
import random
random.seed(9)

def panggil_api():
    return random.random() > 0.7          # 30% peluang berhasil

percobaan, jeda, MAKS = 0, 0.5, 6
while True:
    percobaan += 1
    if panggil_api():
        print(f"berhasil pada percobaan {percobaan}")
        break
    if percobaan == MAKS:
        print("menyerah, catat ke log dan kirim alert"); break
    print(f"gagal, tunggu {jeda:.1f} detik lalu coba lagi")
    jeda *= 2
''', 'Jeda tidak benar-benar ditunggu di contoh ini. Di kode nyata pakai time.sleep(jeda) dan batas maksimum percobaan.')]),

'Perulangan while': dict(
  ist=[('Loop condition', 'Ekspresi yang diperiksa sebelum tiap putaran while.'),
       ('Loop invariant', 'Sifat yang selalu benar di awal tiap putaran; membantu membuktikan loop benar.'),
       ('Progress', 'Setiap putaran harus mendekatkan ke kondisi berhenti agar loop tidak abadi.'),
       ('Simulation', 'while sering dipakai untuk simulasi waktu: berapa bulan sampai target tercapai.')],
  cx=[P('Berapa bulan menabung sampai target DP rumah?', '''
target, saldo, setoran, bunga_tahunan = 60_000_000, 5_000_000, 2_500_000, 0.04
bulan = 0
while saldo < target:
    saldo = saldo * (1 + bunga_tahunan / 12) + setoran
    bulan += 1
print(f"Target tercapai di bulan ke-{bulan} ({bulan // 12} tahun {bulan % 12} bulan)")
print(f"Saldo akhir Rp{saldo:,.0f}".replace(",", "."))
''')]),

'Logika boolean & short-circuit': dict(
  ist=[('Short-circuit evaluation', 'and berhenti di nilai salah pertama, or berhenti di nilai benar pertama.'),
       ('Guard expression', 'x is not None and x.aktif: pemeriksaan kiri melindungi kanan dari error.'),
       ('Default with or', 'nama = masukan or "Tamu"; hati-hati karena 0 dan "" juga dianggap salah.'),
       ('any() / all()', 'Fungsi bawaan untuk memeriksa apakah ada atau semua elemen memenuhi kondisi.')],
  cx=[P('Short-circuit mencegah error', '''
def mahal():
    print("  (fungsi mahal dipanggil)")
    return True

user = None
print("aman:", user is not None and user["aktif"])   # kanan tidak dievaluasi
print("hasil False and ...:"); print(False and mahal())
print("hasil True or ...:"); print(True or mahal())

diskon = 0
print("jebakan or:", diskon or 10, "| benar:", 10 if diskon is None else diskon)
dokumen = {"ktp": True, "npwp": True, "slip_gaji": False}
print("semua lengkap:", all(dokumen.values()), "| ada yang lengkap:", any(dokumen.values()))
''', 'Jebakan or sering terjadi: diskon 0 yang sah ikut diganti 10. Gunakan pemeriksaan is None untuk nilai yang boleh 0.')]),

'Masalah fencepost': dict(
  ist=[('Fencepost problem', 'Ada n tiang tetapi n-1 bentang; muncul saat menaruh pemisah di antara elemen.'),
       ('Off-by-one', 'Kesalahan batas satu angka; keluarga bug yang sama dengan fencepost.'),
       ('Separator', 'Pemisah di antara elemen, misalnya koma, yang tidak boleh muncul di akhir.'),
       ('Pagination', 'Membagi data ke halaman; jumlah halaman = ceil(total / per_halaman), bukan total // per_halaman.')],
  cx=[P('Pemisah dan jumlah halaman yang benar', '''
import math
item = ["kopi", "teh", "susu", "roti"]
s = ""
for i, x in enumerate(item):
    s += x if i == 0 else ", " + x
print(s, "| atau:", ", ".join(item))

for total in [0, 1, 20, 21, 40]:
    print(f"{total:>2} data, 20/halaman -> salah {total // 20} halaman, benar {math.ceil(total / 20)} halaman")
''', 'Bug halaman terakhir yang hilang di aplikasi daftar sering berasal dari pembagian bulat yang lupa dibulatkan ke atas.')]),

'enumerate, zip, break, continue, else': dict(
  ist=[('enumerate', 'Memberi indeks sekaligus elemen; start=1 untuk penomoran manusia.'),
       ('zip / strict=True', 'Memasangkan beberapa iterable; strict=True (3.10+) error jika panjangnya beda.'),
       ('for-else', 'Blok else jalan hanya jika loop selesai tanpa break; cocok untuk pencarian.'),
       ('continue', 'Lewati sisa putaran ini dan lanjut ke elemen berikutnya.')],
  cx=[P('Validasi baris impor CSV', '''
nama = ["Ani", "Budi", "", "Dewi"]
nilai = [88, -5, 70, 91]
for no, (n, v) in enumerate(zip(nama, nilai, strict=True), start=2):   # baris 1 = header
    if not n:
        print(f"baris {no}: nama kosong, dilewati"); continue
    if not 0 <= v <= 100:
        print(f"baris {no}: nilai {v} tidak valid"); continue
    print(f"baris {no}: OK {n}={v}")

for kode in ["A01", "B07", "C03"]:
    if kode.startswith("Z"):
        print("ketemu", kode); break
else:
    print("tidak ada kode berawalan Z")
''')]),

'Semua jenis perulangan: for, while, do-while, for-each, break, continue': dict(
  ist=[('do-while', 'Loop yang badannya jalan minimal sekali; di Python ditulis while True + break di akhir.'),
       ('Loop-and-a-half', 'Pola membaca data, memeriksa berhenti di tengah, lalu memproses.'),
       ('Comprehension', 'Alternatif ringkas untuk loop yang membangun list, dict, atau set.'),
       ('Iterator protocol', 'for bekerja pada objek apa pun yang punya __iter__ dan __next__.')],
  cx=[P('Empat gaya perulangan untuk tugas yang sama', '''
data = [12, 7, 0, 25, 3]

total = 0
for x in data: total += x                       # for-each
print("for-each :", total)

i, total = 0, 0
while i < len(data): total += data[i]; i += 1   # while dengan indeks
print("while    :", total)

antrian = list(data); total = 0
while True:                                      # do-while: minimal sekali
    total += antrian.pop()
    if not antrian: break
print("do-while :", total)
print("built-in :", sum(data), "| comprehension genap:", [x for x in data if x % 2 == 0])
''')]),

'Boolean logic: AND, OR, NOT, tabel kebenaran, dan De Morgan': dict(
  ist=[('Truth table', 'Tabel semua kombinasi masukan dan hasil sebuah ekspresi logika.'),
       ('Hukum De Morgan', 'not (A and B) == (not A) or (not B); not (A or B) == (not A) and (not B).'),
       ('Simplifikasi kondisi', 'Menulis ulang kondisi agar lebih mudah dibaca tanpa mengubah artinya.'),
       ('Exhaustive testing', 'Menguji semua kombinasi; mungkin untuk sedikit variabel boolean.')],
  cx=[P('Membuktikan De Morgan dan menyederhanakan aturan akses', '''
from itertools import product
print(" A     B     not(A and B)  (not A) or (not B)")
for A, B in product([False, True], repeat=2):
    print(f"{A!s:<5} {B!s:<5} {not (A and B)!s:<13} {(not A) or (not B)!s}")

def tolak_lama(admin, pemilik, terkunci):
    return not ((admin or pemilik) and not terkunci)
def tolak_baru(admin, pemilik, terkunci):
    return (not admin and not pemilik) or terkunci
print("setara untuk semua kombinasi:", all(tolak_lama(*k) == tolak_baru(*k) for k in product([0, 1], repeat=3)))
''', 'Saat merefaktor kondisi rumit, uji kedua versi dengan semua kombinasi. Dengan 3 variabel hanya ada 8 kasus.')]),

'Random number: bilangan acak, rentang, seed, dan mengocok': dict(
  ist=[('PRNG', 'Pseudo-random number generator: deret yang tampak acak tetapi ditentukan oleh seed.'),
       ('Seed', 'Nilai awal PRNG; seed sama menghasilkan deret sama, berguna untuk pengujian.'),
       ('secrets', 'Modul untuk keacakan kriptografis (OTP, token); random tidak aman untuk keamanan.'),
       ('Sampling', 'Mengambil sebagian data secara acak: random.sample tanpa pengembalian.')],
  cx=[P('Undian, sampel audit, dan OTP yang aman', '''
import random, secrets
rng = random.Random(2026)                       # PRNG sendiri dengan seed: hasil bisa diulang
peserta = [f"P{i:03}" for i in range(1, 201)]
print("pemenang undian:", rng.sample(peserta, 3))
trx = list(range(1, 1001))
print("sampel audit 5 transaksi:", sorted(rng.sample(trx, 5)))
kartu = list("AKQJ"); rng.shuffle(kartu); print("kocok:", kartu)

otp = f"{secrets.randbelow(10**6):06d}"
print("OTP 6 digit:", len(otp) == 6 and otp.isdigit(), "| token:", len(secrets.token_urlsafe(32)), "karakter")
''', 'OTP dan token reset password wajib memakai secrets. Nilainya tidak ditampilkan di sini karena selalu berbeda.')]),

'List': dict(
  ist=[('Mutable sequence', 'List bisa diubah: tambah, hapus, ganti elemen.'),
       ('Index & negative index', 'Indeks dimulai 0; -1 adalah elemen terakhir.'),
       ('Amortized O(1) append', 'append rata-rata sangat cepat karena list memesan kapasitas lebih.'),
       ('Sorting with key', 'sorted(data, key=...) mengurutkan berdasarkan kolom atau perhitungan tertentu.')],
  cx=[P('Mengurutkan pesanan dengan beberapa kriteria', '''
pesanan = [("INV-07", "reguler", 250_000), ("INV-02", "express", 90_000), ("INV-05", "express", 410_000),
           ("INV-01", "reguler", 410_000), ("INV-09", "same-day", 120_000)]
PRIORITAS = {"same-day": 0, "express": 1, "reguler": 2}
urut = sorted(pesanan, key=lambda p: (PRIORITAS[p[1]], -p[2]))
for inv, layanan, total in urut:
    print(f"{inv}  {layanan:<9} {total:>8,}".replace(",", "."))
print("3 terbesar:", [p[0] for p in sorted(pesanan, key=lambda p: p[2], reverse=True)[:3]])
''', 'Key berupa tuple mengurutkan bertingkat: layanan dulu, lalu total menurun (dengan tanda minus).')]),

'Membuat & mengakses array': dict(
  ist=[('array module', 'array.array menyimpan angka bertipe sama secara padat; lebih hemat memori daripada list.'),
       ('IndexError', 'Error saat mengakses indeks di luar batas.'),
       ('List of lists', 'Struktur 2D sederhana: matriks[baris][kolom].'),
       ('Aliasing trap [[0]*n]*m', 'Mengalikan list berisi list menghasilkan baris yang sama dipakai bersama.')],
  cx=[P('Matriks kursi bioskop dan jebakan perkalian list', '''
salah = [[0] * 4] * 3
salah[0][1] = 1
print("salah:", salah)                      # semua baris ikut berubah!
kursi = [[0] * 4 for _ in range(3)]
kursi[0][1] = 1; kursi[2][3] = 1
for i, baris in enumerate(kursi):
    print(chr(65 + i), " ".join("X" if k else "." for k in baris))

from array import array
import sys
a = array("i", range(1000)); l = list(range(1000))
print("array lebih hemat memori:", sys.getsizeof(a) < sys.getsizeof(l) + sum(map(sys.getsizeof, l)))
''')]),

'Traversal: mencari maksimum': dict(
  ist=[('Linear scan', 'Menelusuri semua elemen sekali: O(n).'),
       ('max(key=...)', 'Mencari elemen terbesar berdasarkan kriteria tertentu.'),
       ('Argmax', 'Posisi atau identitas elemen terbesar, bukan nilainya saja.'),
       ('Top-k', 'k elemen terbesar; heapq.nlargest efisien untuk data besar.')],
  cx=[P('Penjual terbaik dan hari tersibuk', '''
import heapq
penjualan = {"Sari": 48_500_000, "Doni": 61_200_000, "Rina": 59_900_000, "Agus": 33_000_000, "Tono": 61_200_000}
terbaik = max(penjualan, key=penjualan.get)
print("terbaik:", terbaik, "(seri pertama yang ditemukan menang)")
print("top-3:", heapq.nlargest(3, penjualan.items(), key=lambda kv: kv[1]))

harian = [120, 98, 143, 143, 87]
mx, idx = harian[0], 0
for i, v in enumerate(harian[1:], 1):
    if v > mx: mx, idx = v, i
print(f"hari tersibuk indeks {idx} dengan {mx} pesanan")
''', 'Saat ada nilai seri, aturan pemenang harus ditentukan di spesifikasi (misalnya yang lebih dulu mencapai target).')]),

'Referensi (dua nama, satu array)': dict(
  ist=[('Reference semantics', 'Variabel menyimpan referensi ke objek; b = a tidak menyalin isi.'),
       ('Shallow copy', 'Salinan satu tingkat (list.copy(), a[:]); isi bersarang masih dipakai bersama.'),
       ('Deep copy', 'copy.deepcopy menyalin seluruh struktur bersarang.'),
       ('id() / is', 'Memeriksa apakah dua nama menunjuk objek yang sama.')],
  cx=[P('Template pesanan yang ikut berubah', '''
import copy
template = {"pelanggan": None, "item": [], "alamat": {"kota": "Bandung"}}

a = template                       # alias
b = template.copy()                # shallow
c = copy.deepcopy(template)        # deep
b["item"].append("kopi")
c["alamat"]["kota"] = "Medan"
print("template item:", template["item"], "<- ikut berubah lewat shallow copy")
print("template kota:", template["alamat"]["kota"], "<- aman karena deep copy")
print("a is template:", a is template, "| b is template:", b is template)
''', 'Bug ini sering muncul pada konfigurasi default yang tak sengaja diubah oleh satu request lalu terbawa ke request lain.')]),

'List Dinamis': dict(
  ist=[('Dynamic array', 'Array yang otomatis membesar; list Python adalah dynamic array.'),
       ('Capacity vs length', 'Kapasitas memori yang dipesan bisa lebih besar daripada jumlah elemen.'),
       ('Over-allocation', 'Strategi memesan ruang lebih agar append tidak selalu menyalin.'),
       ('Preallocation', 'Membuat list berukuran tetap di awal ([None] * n) bila ukuran sudah diketahui.')],
  cx=[P('Melihat list memesan kapasitas lebih', '''
import sys
data, ukuran_lama = [], sys.getsizeof([])
for i in range(40):
    data.append(i)
    u = sys.getsizeof(data)
    if u != ukuran_lama:
        print(f"len {len(data):>2}: memori {u} byte (kapasitas naik)")
        ukuran_lama = u
''', 'Angka byte bisa berbeda antarversi Python, tetapi polanya sama: kapasitas naik bertahap, tidak di setiap append.')]),

'add, sisip, hapus': dict(
  ist=[('append / extend', 'Menambah satu elemen / banyak elemen di akhir.'),
       ('insert(i, x)', 'Menyisipkan di posisi tertentu; O(n) karena elemen setelahnya digeser.'),
       ('remove / pop / del', 'Hapus berdasarkan nilai / posisi (mengembalikan nilai) / posisi atau slice.'),
       ('collections.deque', 'Struktur untuk tambah/hapus cepat di kedua ujung.')],
  cx=[P('Mengelola antrean pasien', '''
from collections import deque
antre = ["A01", "A02", "A03"]
antre.append("A04")
antre.insert(1, "PRIORITAS-L01")       # lansia didahulukan
antre.remove("A03")                    # pasien membatalkan
dipanggil = antre.pop(0)
print("dipanggil:", dipanggil, "| sisa:", antre)

d = deque(antre)
d.appendleft("DARURAT-01"); print("deque:", list(d), "| panggil:", d.popleft())
''', 'pop(0) pada list besar lambat karena menggeser semua elemen. Untuk antrean sungguhan gunakan deque.')]),

'Menghapus sambil berjalan mundur': dict(
  ist=[('Mutation during iteration', 'Mengubah list saat dilalui for bisa melewatkan elemen.'),
       ('Reverse iteration', 'Menelusuri dari belakang agar penghapusan tidak menggeser elemen yang belum diperiksa.'),
       ('Filter to new list', 'Cara paling aman: buat list baru berisi elemen yang dipertahankan.'),
       ('In-place', 'Mengubah objek yang sama; data[:] = ... mengganti isi tanpa mengganti objek.')],
  cx=[P('Tiga cara membuang sesi kedaluwarsa', '''
sesi = [5, 61, 62, 3, 90, 12]          # menit sejak aktif terakhir; > 60 kedaluwarsa
salah = list(sesi)
for s in salah:
    if s > 60: salah.remove(s)
print("salah  :", salah, "<- 62 terlewat")

mundur = list(sesi)
for i in range(len(mundur) - 1, -1, -1):
    if mundur[i] > 60: del mundur[i]
print("mundur :", mundur)

baru = [s for s in sesi if s <= 60]
print("filter :", baru)
''')]),

'Tuple & unpacking': dict(
  ist=[('Tuple', 'Urutan yang tidak bisa diubah; cocok untuk record tetap seperti koordinat.'),
       ('Unpacking', 'Membongkar elemen ke beberapa nama: x, y = titik.'),
       ('Star unpacking', 'pertama, *tengah, terakhir = data.'),
       ('namedtuple', 'Tuple dengan nama kolom; ringan dan mudah dibaca.')],
  cx=[P('Record transaksi dengan namedtuple', '''
from collections import namedtuple
Trx = namedtuple("Trx", "kode tanggal jumlah")
data = [Trx("T1", "2026-11-01", 150_000), Trx("T2", "2026-11-03", 82_500), Trx("T3", "2026-11-07", 410_000)]
for kode, tgl, jml in data:
    print(kode, tgl, jml)
pertama, *tengah, terakhir = data
print("pertama:", pertama.kode, "| tengah:", len(tengah), "| terakhir:", terakhir.jumlah)
a, b = 1, 2; a, b = b, a; print("swap:", a, b)
print("tuple bisa jadi kunci dict:", {("Jakarta", "2026-11"): 120}[("Jakarta", "2026-11")])
''')]),

'Koleksi: List, Set, Dict': dict(
  ist=[('Sequence vs set vs mapping', 'List berurutan, set unik tanpa urutan, dict pasangan kunci-nilai.'),
       ('Hashable', 'Objek yang bisa jadi elemen set atau kunci dict (str, int, tuple berisi immutable).'),
       ('Membership test', 'x in set dan x in dict rata-rata O(1); x in list O(n).'),
       ('Choosing a data structure', 'Pilih berdasarkan operasi yang paling sering dipakai.')],
  cx=[P('Memilih struktur data dari operasi yang dibutuhkan', '''
import timeit
ids = list(range(100_000)); ids_set = set(ids); ids_dict = dict.fromkeys(ids)
t_list = timeit.timeit(lambda: 99_999 in ids, number=200)
t_set = timeit.timeit(lambda: 99_999 in ids_set, number=200)
print("cek keanggotaan: set jauh lebih cepat dari list:", t_set * 100 < t_list)

KEBUTUHAN = [("urutan penting, boleh duplikat", "list"), ("cek 'sudah pernah?' cepat, unik", "set"),
             ("cari data berdasarkan kunci (NIK, SKU)", "dict"), ("record tetap, jadi kunci", "tuple")]
for k, s in KEBUTUHAN: print(f"{k:<40} -> {s}")
''')]),

'Set: himpunan tanpa duplikat': dict(
  ist=[('Deduplication', 'Membuang duplikat; set(data) cepat tetapi tidak menjaga urutan.'),
       ('dict.fromkeys', 'Dedup yang menjaga urutan kemunculan pertama.'),
       ('Set operations', 'Gabungan |, irisan &, selisih -, selisih simetris ^.'),
       ('frozenset', 'Set yang tidak bisa diubah sehingga bisa jadi kunci dict.')],
  cx=[P('Dedup email dan membandingkan peserta', '''
email = ["a@x.id", "B@x.id", "a@x.id", "c@x.id", "b@x.id"]
print("set() saja (B@ dan b@ dianggap beda):", len(set(email)), "email")
print("jaga urutan + normalisasi:", list(dict.fromkeys(e.lower() for e in email)))

daftar = {"ani", "budi", "citra", "dedi"}
hadir = {"budi", "citra", "eko"}
print("hadir & terdaftar:", sorted(daftar & hadir))
print("terdaftar tapi absen:", sorted(daftar - hadir))
print("hadir tanpa daftar:", sorted(hadir - daftar))
''')]),

'Map: menghitung kemunculan': dict(
  ist=[('Frequency count', 'Menghitung berapa kali tiap nilai muncul.'),
       ('Counter', 'collections.Counter: dict khusus menghitung, punya most_common().'),
       ('defaultdict', 'Dict yang otomatis membuat nilai awal untuk kunci baru.'),
       ('Group by', 'Mengelompokkan data berdasarkan kunci, misalnya pesanan per kota.')],
  cx=[P('Analisis log error dan pengelompokan', '''
from collections import Counter, defaultdict
log = ["ERROR db timeout", "WARN cache miss", "ERROR db timeout", "ERROR auth gagal", "INFO ok",
       "ERROR db timeout", "WARN cache miss", "ERROR auth gagal"]
level = Counter(b.split()[0] for b in log)
print("per level:", dict(level))
print("error terbanyak:", Counter(b for b in log if b.startswith("ERROR")).most_common(2))

pesanan = [("Bandung", 120_000), ("Medan", 80_000), ("Bandung", 45_000), ("Surabaya", 300_000)]
per_kota = defaultdict(list)
for kota, total in pesanan: per_kota[kota].append(total)
print({k: sum(v) for k, v in per_kota.items()})
''')]),

'Dictionary lanjutan & operasi set': dict(
  ist=[('dict merge |', 'Menggabungkan dict (3.9+); kunci di kanan menimpa kiri.'),
       ('setdefault / get', 'Mengambil nilai dengan default tanpa KeyError.'),
       ('Dict views', 'keys(), items() bisa dioperasikan seperti set: d1.keys() & d2.keys().'),
       ('Configuration layering', 'Konfigurasi default ditimpa konfigurasi lingkungan, lalu argumen pengguna.')],
  cx=[P('Lapisan konfigurasi dan perbandingan dua versi', '''
default = {"debug": False, "timeout": 30, "db": "sqlite", "bahasa": "id"}
produksi = {"db": "postgres", "timeout": 10}
cli = {"debug": True}
efektif = default | produksi | cli
print("efektif:", efektif)

v1 = {"harga": 18000, "stok": 40, "warna": "hitam"}
v2 = {"harga": 19500, "stok": 40, "ukuran": "L"}
print("kolom baru   :", v2.keys() - v1.keys())
print("kolom dihapus:", v1.keys() - v2.keys())
print("nilai berubah:", {k: (v1[k], v2[k]) for k in v1.keys() & v2.keys() if v1[k] != v2[k]})
''', 'Perbandingan seperti ini dipakai untuk audit trail: mencatat kolom apa saja yang berubah pada sebuah record.')]),
}
