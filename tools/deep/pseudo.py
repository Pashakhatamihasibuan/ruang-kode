"""Pendalaman jalur Logika & Pseudocode: istilah dunia kerja dan contoh pseudocode + terjemahan Python yang dijalankan."""
K = 'pseudo'


def P(t, pseudo, py, b=None):
    """Satu contoh: pseudocode (sebagai komentar) lalu terjemahan Python yang benar-benar dijalankan."""
    kom = '\n'.join('# ' + s if s else '#' for s in pseudo.strip('\n').split('\n'))
    return dict(t=t, b=b, code='# --- Pseudocode ---\n' + kom + '\n\n# --- Python ---\n' + py.strip('\n'))


def T(t, teks, b=None):
    """Contoh berupa teks (pseudocode/dokumen) yang tidak dijalankan."""
    return dict(t=t, b=b, code=teks.strip('\n'), lang='text', run=False)


D = {
'Tujuan pseudocode yang tidak terikat bahasa': dict(
  ist=[('Spesifikasi algoritma', 'Deskripsi langkah yang cukup jelas untuk diterjemahkan ke bahasa apa pun oleh orang lain.'),
       ('Technical design doc (TDD)', 'Dokumen rancangan sebelum koding; pseudocode sering dipakai di bagian "Proposed solution".'),
       ('Whiteboard interview', 'Wawancara kerja yang meminta kandidat menulis solusi di papan; pseudocode yang rapi dinilai positif.'),
       ('Language-agnostic', 'Tidak bergantung pada sintaks bahasa tertentu, sehingga bisa dibaca analis, QA, dan programmer.')],
  cx=[P('Satu pseudocode, langsung jadi Python', '''
ALGORITMA HitungDiskon
  INPUT total
  JIKA total >= 500000 MAKA diskon <- total * 0.1
  SELAIN ITU diskon <- 0
  OUTPUT total - diskon
''', '''
def hitung_diskon(total):
    diskon = total * 0.1 if total >= 500_000 else 0
    return total - diskon

for t in (250_000, 500_000, 1_200_000):
    print(f"total {t:>9,} -> bayar {hitung_diskon(t):>11,.0f}".replace(",", "."))
''', 'Aturan bisnis ditulis sekali dalam pseudocode, lalu developer Python, Java, atau Kotlin bisa menerjemahkannya tanpa salah paham.')]),

'Kata kunci standar dan gaya penulisan': dict(
  ist=[('Keyword UPPERCASE', 'Konvensi menulis IF, WHILE, RETURN dengan huruf besar agar struktur mudah dipindai.'),
       ('Indentasi blok', 'Isi blok digeser ke dalam; ENDIF/ENDWHILE menutup blok secara eksplisit.'),
       ('Assignment arrow (←)', 'Simbol pengisian nilai di buku teks dan ujian; di kode biasanya =.'),
       ('Style guide', 'Aturan penulisan bersama tim, misalnya PEP 8 untuk Python atau konvensi pseudocode kurikulum.')],
  cx=[T('Gaya yang konsisten vs tidak konsisten', '''
TIDAK KONSISTEN                    KONSISTEN
-----------------------------      ---------------------------------
if nilai>70 then lulus             IF nilai > 70 THEN
  print "ok"                           status <- "LULUS"
else Gagal                         ELSE
endif                                  status <- "TIDAK LULUS"
                                   ENDIF
                                   OUTPUT status
''', 'Sisi kanan memakai keyword huruf besar, indentasi 4 spasi, dan penutup blok yang jelas.')]),

'Variabel, tipe data, dan pengisian nilai': dict(
  ist=[('Identifier', 'Nama variabel. Gunakan nama bermakna seperti totalHarga, bukan x1.'),
       ('Tipe data primitif', 'INTEGER, REAL, BOOLEAN, CHAR, STRING.'),
       ('Konstanta', 'Nilai yang tidak berubah, misalnya PPN = 0.11. Ditulis huruf besar.'),
       ('Magic number', 'Angka tanpa nama di tengah kode (0.11, 86400). Reviewer biasanya meminta diganti konstanta.')],
  cx=[P('Konstanta menggantikan magic number', '''
CONST PPN <- 0.11
DECLARE harga : INTEGER
DECLARE pajak : REAL
harga <- 150000
pajak <- harga * PPN
OUTPUT harga + pajak
''', '''
PPN = 0.11
harga: int = 150_000
pajak: float = harga * PPN
print("Pajak :", round(pajak))
print("Total :", round(harga + pajak))
print("Tipe  :", type(harga).__name__, type(pajak).__name__)
''')]),

'Input dan output dasar': dict(
  ist=[('stdin / stdout', 'Aliran masukan dan keluaran standar program. Online judge (HackerRank, TOKI) membaca dari stdin.'),
       ('Parsing', 'Mengubah teks masukan menjadi angka atau struktur data.'),
       ('Validasi input', 'Memeriksa masukan sebelum dipakai; prinsip "jangan percaya input pengguna".'),
       ('Format output', 'Menata tampilan (lebar kolom, desimal, pemisah ribuan) sesuai kebutuhan pengguna.')],
  cx=[P('Membaca beberapa baris angka (gaya soal kompetisi)', '''
INPUT n
UNTUK i DARI 1 SAMPAI n
    INPUT nilai[i]
OUTPUT jumlah dan rata-rata
''', '''
import io, sys
sys.stdin = io.StringIO("4\\n80\\n75\\n90\\n68\\n")   # simulasi masukan

n = int(input())
nilai = [int(input()) for _ in range(n)]
print(f"Jumlah   : {sum(nilai)}")
print(f"Rata-rata: {sum(nilai) / n:.2f}")
''')]),

'Operasi aritmetika dan urutan operator': dict(
  ist=[('Precedence', 'Urutan prioritas operator: kurung, pangkat, kali/bagi/mod, tambah/kurang.'),
       ('DIV dan MOD', 'Pembagian bulat dan sisa bagi. Dipakai untuk konversi waktu, cek genap, dan digit.'),
       ('Floating point error', '0.1 + 0.2 tidak tepat 0.3. Untuk uang pakai bilangan bulat (sen/rupiah) atau Decimal.'),
       ('Overflow', 'Hasil melebihi batas tipe (misalnya int 32-bit). Python tidak overflow, Java dan C bisa.')],
  cx=[P('Konversi detik ke jam:menit:detik dengan DIV dan MOD', '''
INPUT total_detik
jam   <- total_detik DIV 3600
menit <- (total_detik MOD 3600) DIV 60
detik <- total_detik MOD 60
''', '''
for total in (59, 3_725, 86_399):
    jam, sisa = divmod(total, 3600)
    menit, detik = divmod(sisa, 60)
    print(f"{total:>6} detik = {jam:02}:{menit:02}:{detik:02}")
print("0.1 + 0.2 =", 0.1 + 0.2, "-> jangan pakai float untuk uang")
''')]),

'Algoritma sekuensial pertamamu': dict(
  ist=[('Sekuensial', 'Langkah dijalankan berurutan dari atas ke bawah tanpa cabang atau loop.'),
       ('IPO (Input-Process-Output)', 'Pola dasar setiap program: terima data, olah, keluarkan hasil.'),
       ('Dry run', 'Menjalankan algoritma di kepala/kertas dengan contoh data sebelum koding.'),
       ('Test case', 'Pasangan masukan dan keluaran yang diharapkan untuk memeriksa algoritma.')],
  cx=[P('Menghitung cicilan sederhana (IPO)', '''
INPUT harga, uang_muka, tenor_bulan, bunga_flat_tahun
pokok   <- harga - uang_muka
bunga   <- pokok * bunga_flat_tahun * tenor_bulan / 12
cicilan <- (pokok + bunga) / tenor_bulan
OUTPUT cicilan
''', '''
harga, dp, tenor, bunga_th = 18_000_000, 3_000_000, 12, 0.06
pokok = harga - dp
bunga = pokok * bunga_th * tenor / 12
cicilan = (pokok + bunga) / tenor
print(f"Pokok   : Rp{pokok:,.0f}".replace(",", "."))
print(f"Bunga   : Rp{bunga:,.0f}".replace(",", "."))
print(f"Cicilan : Rp{cicilan:,.0f}/bulan".replace(",", "."))
''')]),

'Ekspresi Boolean dan operator logika': dict(
  ist=[('Truth table', 'Tabel semua kombinasi nilai benar/salah untuk sebuah ekspresi.'),
       ('Short-circuit evaluation', 'AND berhenti saat bertemu salah, OR berhenti saat bertemu benar. Dipakai untuk mencegah error (cek None dulu).'),
       ('Hukum De Morgan', 'NOT (A AND B) = (NOT A) OR (NOT B). Berguna untuk menyederhanakan kondisi.'),
       ('Predicate', 'Fungsi yang mengembalikan Boolean, misalnya is_valid_email().')],
  cx=[P('Truth table dan pembuktian De Morgan', '''
UNTUK A DALAM {SALAH, BENAR}
  UNTUK B DALAM {SALAH, BENAR}
    OUTPUT A, B, A AND B, A OR B, NOT(A AND B) = (NOT A OR NOT B)
''', '''
print("A     B     AND   OR    DeMorgan")
for a in (False, True):
    for b in (False, True):
        dm = (not (a and b)) == ((not a) or (not b))
        print(f"{a!s:5} {b!s:5} {a and b!s:5} {a or b!s:5} {dm}")
''')]),

'IF satu cabang': dict(
  ist=[('Conditional statement', 'Pernyataan yang hanya dijalankan bila kondisi benar.'),
       ('Business rule', 'Aturan dari bisnis, misalnya "gratis ongkir bila belanja di atas 100 ribu".'),
       ('Default value', 'Nilai awal yang dipakai bila kondisi tidak terpenuhi; mengurangi kebutuhan ELSE.'),
       ('Feature flag', 'Kondisi IF untuk menyalakan/mematikan fitur tanpa deploy ulang.')],
  cx=[P('Default dulu, lalu IF untuk pengecualian', '''
ongkir <- 15000
JIKA belanja >= 100000 MAKA
    ongkir <- 0
ENDIF
''', '''
for belanja in (45_000, 100_000, 230_000):
    ongkir = 15_000
    if belanja >= 100_000:
        ongkir = 0
    print(f"belanja {belanja:>7} -> ongkir {ongkir}")
''')]),

'IF-ELSE: dua jalur': dict(
  ist=[('Branch', 'Satu jalur eksekusi dalam percabangan.'),
       ('Ternary / conditional expression', 'Bentuk singkat IF-ELSE dalam satu ekspresi: a if kondisi else b.'),
       ('Branch coverage', 'Ukuran pengujian: apakah setiap cabang pernah dijalankan oleh tes.'),
       ('Mutually exclusive', 'Dua jalur yang tidak mungkin terjadi bersamaan.')],
  cx=[P('Ganjil atau genap, dengan tes kedua cabang', '''
FUNGSI jenis(n)
  JIKA n MOD 2 = 0 MAKA RETURN "genap"
  SELAIN ITU RETURN "ganjil"
''', '''
def jenis(n):
    return "genap" if n % 2 == 0 else "ganjil"

assert jenis(4) == "genap"     # cabang IF
assert jenis(7) == "ganjil"    # cabang ELSE
assert jenis(-3) == "ganjil"   # kasus negatif
print("kedua cabang lolos tes:", [jenis(x) for x in (0, 1, -2, 15)])
''')]),

'CASE: memilih banyak jalur': dict(
  ist=[('Switch / match', 'Struktur multi-cabang; di Python 3.10+ ada match-case, di Java switch expression.'),
       ('Default / otherwise', 'Cabang untuk nilai yang tidak terduga. Wajib ada untuk ketahanan program.'),
       ('Lookup table', 'Mengganti CASE panjang dengan dictionary/peta; lebih mudah dirawat.'),
       ('Exhaustive', 'Semua kemungkinan nilai ditangani, misalnya pada enum.')],
  cx=[P('CASE status pesanan vs lookup table', '''
CASE status OF
  "PAID"     : OUTPUT "Dikemas"
  "SHIPPED"  : OUTPUT "Dalam perjalanan"
  "DONE"     : OUTPUT "Selesai"
  OTHERWISE  : OUTPUT "Status tidak dikenal"
ENDCASE
''', '''
def label_match(status):
    match status:
        case "PAID": return "Dikemas"
        case "SHIPPED": return "Dalam perjalanan"
        case "DONE": return "Selesai"
        case _: return "Status tidak dikenal"

LABEL = {"PAID": "Dikemas", "SHIPPED": "Dalam perjalanan", "DONE": "Selesai"}
for s in ("PAID", "DONE", "REFUND"):
    print(f"{s:8} | match: {label_match(s):22} | tabel: {LABEL.get(s, 'Status tidak dikenal')}")
''')]),

'Percabangan bersarang': dict(
  ist=[('Nested condition', 'IF di dalam IF. Lebih dari 3 tingkat biasanya sulit dibaca.'),
       ('Arrow anti-pattern', 'Kode yang menjorok makin ke kanan seperti mata panah karena IF bersarang dalam.'),
       ('Cyclomatic complexity', 'Jumlah jalur independen di fungsi; alat seperti SonarQube memberi peringatan bila terlalu tinggi.'),
       ('Decision table', 'Tabel kombinasi kondisi dan aksi untuk aturan yang rumit.')],
  cx=[P('Tarif parkir: bersarang vs diratakan', '''
JIKA jenis = "motor" MAKA
    JIKA jam <= 1 MAKA tarif <- 2000 SELAIN ITU tarif <- 2000 + (jam-1)*1000
SELAIN ITU
    JIKA jam <= 1 MAKA tarif <- 5000 SELAIN ITU tarif <- 5000 + (jam-1)*3000
''', '''
TARIF = {"motor": (2000, 1000), "mobil": (5000, 3000)}   # (jam pertama, jam berikutnya)

def tarif(jenis, jam):
    awal, lanjut = TARIF[jenis]
    return awal + max(0, jam - 1) * lanjut

for j, h in [("motor", 1), ("motor", 4), ("mobil", 1), ("mobil", 3)]:
    print(f"{j:5} {h} jam -> Rp{tarif(j, h):,}".replace(",", "."))
''', 'Versi Python meratakan percabangan dengan tabel tarif, sehingga menambah jenis kendaraan cukup satu baris.')]),

'Guard clause untuk menangani kesalahan': dict(
  ist=[('Guard clause / early return', 'Keluar lebih awal saat input tidak valid sehingga jalur utama tetap rata.'),
       ('Fail fast', 'Menolak data buruk sedini mungkin, bukan membiarkannya merusak proses berikutnya.'),
       ('Exception', 'Mekanisme error terstruktur (raise/throw) untuk kasus yang tidak bisa ditangani di tempat.'),
       ('Happy path', 'Jalur ketika semua berjalan normal.')],
  cx=[P('Transfer saldo dengan guard clause', '''
FUNGSI transfer(saldo, jumlah)
  JIKA jumlah <= 0 MAKA RETURN "Jumlah tidak valid"
  JIKA jumlah > saldo MAKA RETURN "Saldo tidak cukup"
  JIKA jumlah > 10000000 MAKA RETURN "Melebihi limit harian"
  RETURN "OK, sisa " + (saldo - jumlah)
''', '''
def transfer(saldo, jumlah):
    if jumlah <= 0:
        return "Jumlah tidak valid"
    if jumlah > saldo:
        return "Saldo tidak cukup"
    if jumlah > 10_000_000:
        return "Melebihi limit harian"
    return "OK, sisa " + f"{saldo - jumlah:,}".replace(",", ".")

saldo = 12_000_000
for j in (-5, 2_000_000, 11_500_000, 15_000_000):
    print(f"{j:>11,}".replace(",", ".") + " -> " + transfer(saldo, j))
''')]),

'FOR: perulangan pasti': dict(
  ist=[('Counter / loop variable', 'Variabel penghitung yang berubah tiap iterasi.'),
       ('Iterasi', 'Satu putaran perulangan.'),
       ('Range', 'Rentang nilai; di Python range(awal, akhir) tidak menyertakan akhir.'),
       ('Step', 'Besar langkah tiap iterasi, misalnya 2 atau -1.')],
  cx=[P('Tabel angsuran bulanan dengan FOR', '''
sisa <- 6000000
UNTUK bulan DARI 1 SAMPAI 6
    sisa <- sisa - 1000000
    OUTPUT bulan, sisa
''', '''
sisa = 6_000_000
for bulan in range(1, 7):
    sisa -= 1_000_000
    print(f"Bulan {bulan}: sisa Rp{sisa:>9,}".replace(",", "."))
print("Hitung mundur:", list(range(10, 0, -3)))
''')]),

'WHILE: perulangan bersyarat': dict(
  ist=[('Loop condition', 'Kondisi yang dicek sebelum tiap iterasi.'),
       ('Sentinel value', 'Nilai khusus penanda akhir data, misalnya 0 atau "selesai".'),
       ('Polling', 'Mengecek status berulang sampai siap; di produksi dibatasi jumlah percobaan dan jeda.'),
       ('Retry with backoff', 'Mencoba ulang dengan jeda yang makin panjang saat layanan gagal.')],
  cx=[P('Berapa tahun tabungan menjadi dua kali lipat?', '''
saldo <- 10000000; tahun <- 0
SELAMA saldo < 20000000
    saldo <- saldo * 1.06
    tahun <- tahun + 1
OUTPUT tahun
''', '''
saldo, tahun = 10_000_000, 0
while saldo < 20_000_000:
    saldo *= 1.06
    tahun += 1
print(f"Butuh {tahun} tahun; saldo Rp{saldo:,.0f}".replace(",", "."))
print("Aturan 72 memperkirakan:", round(72 / 6), "tahun")
''')]),

'REPEAT-UNTIL: dicek di akhir': dict(
  ist=[('Post-test loop', 'Perulangan yang memeriksa kondisi di akhir, jadi badan loop jalan minimal sekali.'),
       ('do-while', 'Nama REPEAT-UNTIL di Java, C, Kotlin. Python tidak punya; pakai while True + break.'),
       ('Menu loop', 'Pola klasik: tampilkan menu, proses pilihan, ulangi sampai pengguna memilih keluar.'),
       ('Input validation loop', 'Minta input ulang sampai valid.')],
  cx=[P('Minta PIN sampai benar (maksimal 3 kali)', '''
percobaan <- 0
REPEAT
    INPUT pin
    percobaan <- percobaan + 1
UNTIL pin = "1234" OR percobaan = 3
''', '''
masukan = iter(["0000", "9999", "1234"])
percobaan = 0
while True:                      # REPEAT
    pin = next(masukan)
    percobaan += 1
    print(f"percobaan {percobaan}: {pin}")
    if pin == "1234" or percobaan == 3:   # UNTIL
        break
print("Masuk" if pin == "1234" else "Kartu diblokir")
''')]),

'FOR, WHILE, dan DO-WHILE: contoh sederhana dan bedanya': dict(
  ist=[('Definite loop', 'Jumlah iterasi diketahui di awal (FOR).'),
       ('Indefinite loop', 'Jumlah iterasi bergantung kondisi (WHILE).'),
       ('Pre-test vs post-test', 'WHILE cek di awal (bisa 0 kali), DO-WHILE cek di akhir (minimal 1 kali).'),
       ('Idiomatic code', 'Memilih bentuk loop yang paling wajar di bahasa itu.')],
  cx=[P('Kondisi awal sudah salah: siapa yang tetap jalan?', '''
n <- 10
WHILE n < 5 DO OUTPUT "while"      // 0 kali
REPEAT OUTPUT "do-while" UNTIL n >= 5   // 1 kali
FOR i DARI 1 SAMPAI 0 DO OUTPUT "for"  // 0 kali
''', '''
n = 10
hasil = {"for": 0, "while": 0, "do-while": 0}
for i in range(1, 1):
    hasil["for"] += 1
while n < 5:
    hasil["while"] += 1
while True:
    hasil["do-while"] += 1
    if n >= 5:
        break
for k, v in hasil.items():
    print(f"{k:9}: dijalankan {v} kali")
''')]),

'Penghentian loop dan infinite loop': dict(
  ist=[('Termination condition', 'Kondisi yang pasti tercapai agar loop berhenti.'),
       ('Infinite loop', 'Loop yang tidak pernah berhenti; menyebabkan aplikasi hang atau CPU 100%.'),
       ('Loop invariant', 'Pernyataan yang selalu benar di setiap iterasi; dipakai untuk membuktikan kebenaran.'),
       ('Watchdog / timeout', 'Batas waktu atau batas iterasi sebagai pengaman di sistem produksi.')],
  cx=[P('Bug: variabel tidak berubah, dan pengamannya', '''
// SALAH: i tidak pernah bertambah
i <- 0
WHILE i < 5 DO OUTPUT i
// BENAR + pengaman
i <- 0; batas <- 1000
WHILE i < 5 AND batas > 0 DO OUTPUT i; i <- i + 1; batas <- batas - 1
''', '''
i, batas = 0, 1000
langkah = []
while i < 5 and batas > 0:
    langkah.append(i)
    i += 1          # tanpa baris ini loop tidak pernah berhenti
    batas -= 1
print("isi:", langkah, "| sisa batas:", batas)
''')]),

'Loop bersarang': dict(
  ist=[('Nested loop', 'Loop di dalam loop; total iterasi = perkalian jumlah iterasi masing-masing.'),
       ('O(n²)', 'Kompleksitas khas loop bersarang atas data yang sama; lambat untuk n besar.'),
       ('Outer / inner loop', 'Loop luar dan dalam; inner loop selesai penuh untuk tiap putaran outer.'),
       ('Grid traversal', 'Menjelajah tabel 2D baris demi baris.')],
  cx=[P('Mencari pasangan produk yang totalnya pas dengan budget', '''
UNTUK i DARI 0 SAMPAI n-1
  UNTUK j DARI i+1 SAMPAI n-1
    JIKA harga[i] + harga[j] = budget MAKA OUTPUT pasangan
''', '''
produk = [("Kaos", 85_000), ("Topi", 40_000), ("Celana", 160_000), ("Kaus kaki", 15_000), ("Jaket", 115_000)]
budget, cek = 200_000, 0
for i in range(len(produk)):
    for j in range(i + 1, len(produk)):
        cek += 1
        if produk[i][1] + produk[j][1] == budget:
            print("Pas:", produk[i][0], "+", produk[j][0])
print(f"{cek} pasangan diperiksa (n(n-1)/2 = {len(produk)*(len(produk)-1)//2})")
''')]),

'Pola akumulator': dict(
  ist=[('Accumulator', 'Variabel yang mengumpulkan hasil selama loop (jumlah, hitungan, maksimum).'),
       ('Inisialisasi', 'Nilai awal akumulator: 0 untuk jumlah, 1 untuk perkalian, elemen pertama untuk maksimum.'),
       ('Aggregate', 'Ringkasan data: SUM, COUNT, AVG, MIN, MAX. Sama seperti di SQL.'),
       ('Reduce / fold', 'Nama pola akumulator di pemrograman fungsional.')],
  cx=[P('Ringkasan penjualan harian dalam satu loop', '''
total <- 0; jumlah_trx <- 0; terbesar <- -1
UNTUK SETIAP trx DALAM transaksi
    total <- total + trx
    jumlah_trx <- jumlah_trx + 1
    JIKA trx > terbesar MAKA terbesar <- trx
''', '''
transaksi = [125_000, 48_000, 310_000, 76_500, 220_000]
total, jumlah, terbesar = 0, 0, float("-inf")
for trx in transaksi:
    total += trx
    jumlah += 1
    terbesar = max(terbesar, trx)
print(f"Total {total:,} | {jumlah} trx | rata {total/jumlah:,.0f} | terbesar {terbesar:,}".replace(",", "."))
''')]),

'Semua jenis perulangan: for, while, do-while, for-each, break, continue': dict(
  ist=[('for-each', 'Mengulang tiap elemen koleksi tanpa indeks; paling aman dari off-by-one.'),
       ('break', 'Keluar dari loop seketika.'),
       ('continue', 'Lewati sisa badan loop dan lanjut ke iterasi berikutnya.'),
       ('enumerate / indexed loop', 'Mendapat indeks dan nilai sekaligus.')],
  cx=[P('Memproses antrean pesanan dengan continue dan break', '''
UNTUK SETIAP p DALAM pesanan
    JIKA p.status = "BATAL" MAKA CONTINUE
    JIKA stok = 0 MAKA BREAK
    proses p; stok <- stok - 1
''', '''
pesanan = [("A1", "OK"), ("A2", "BATAL"), ("A3", "OK"), ("A4", "OK"), ("A5", "OK")]
stok = 2
for no, (kode, status) in enumerate(pesanan, start=1):
    if status == "BATAL":
        print(f"{no}. {kode} dilewati (batal)"); continue
    if stok == 0:
        print(f"{no}. {kode} stok habis, berhenti"); break
    stok -= 1
    print(f"{no}. {kode} diproses, sisa stok {stok}")
''')]),

'Dekomposisi top-down': dict(
  ist=[('Decomposition', 'Memecah masalah besar menjadi sub-masalah kecil yang bisa diselesaikan terpisah.'),
       ('Stepwise refinement', 'Menulis langkah kasar dulu, lalu memperinci tiap langkah.'),
       ('Work breakdown', 'Pembagian kerja dalam proyek; tiap sub-masalah bisa jadi tiket di Jira/Linear.'),
       ('Single responsibility', 'Setiap modul punya satu tugas yang jelas.')],
  cx=[P('Checkout toko online dipecah menjadi fungsi kecil', '''
checkout(keranjang):
    subtotal <- hitungSubtotal(keranjang)
    diskon   <- hitungDiskon(subtotal)
    ongkir   <- hitungOngkir(subtotal - diskon)
    RETURN subtotal - diskon + ongkir
''', '''
def hitung_subtotal(k): return sum(h * q for h, q in k)
def hitung_diskon(s): return int(s * 0.1) if s >= 300_000 else 0
def hitung_ongkir(s): return 0 if s >= 150_000 else 12_000

def checkout(keranjang):
    sub = hitung_subtotal(keranjang)
    dis = hitung_diskon(sub)
    ong = hitung_ongkir(sub - dis)
    return sub, dis, ong, sub - dis + ong

print("sub, diskon, ongkir, total =", checkout([(120_000, 2), (95_000, 1)]))
print("sub, diskon, ongkir, total =", checkout([(45_000, 1)]))
''')]),

'Fungsi dan nilai kembali': dict(
  ist=[('Signature', 'Nama fungsi, parameter, dan tipe kembalian.'),
       ('Return value', 'Hasil yang dikirim fungsi ke pemanggil.'),
       ('Pure function', 'Fungsi tanpa efek samping; masukan sama selalu memberi keluaran sama. Mudah dites.'),
       ('Unit test', 'Tes otomatis untuk satu fungsi.')],
  cx=[P('Fungsi murni BMI beserta unit test', '''
FUNGSI bmi(berat, tinggi_cm) -> REAL
    t <- tinggi_cm / 100
    RETURN berat / (t * t)
''', '''
def bmi(berat: float, tinggi_cm: float) -> float:
    t = tinggi_cm / 100
    return berat / (t * t)

def kategori(b: float) -> str:
    return "kurus" if b < 18.5 else "normal" if b < 25 else "berlebih" if b < 30 else "obesitas"

assert round(bmi(70, 175), 1) == 22.9
for berat, tinggi in [(50, 170), (70, 175), (88, 172)]:
    b = bmi(berat, tinggi)
    print(f"{berat} kg, {tinggi} cm -> BMI {b:.1f} ({kategori(b)})")
''')]),

'Prosedur untuk efek samping': dict(
  ist=[('Side effect', 'Perubahan di luar fungsi: mencetak, menulis file, mengubah database, mengirim email.'),
       ('Procedure', 'Subprogram tanpa nilai kembali yang tujuannya efek samping.'),
       ('Command-query separation', 'Pisahkan fungsi yang mengubah state (command) dari yang membaca (query).'),
       ('Logging', 'Mencatat kejadian untuk penelusuran masalah; contoh efek samping yang umum.')],
  cx=[P('Query menghitung, procedure mencetak', '''
FUNGSI totalNilai(daftar) -> INTEGER      // query, tanpa efek samping
PROSEDUR cetakRapor(nama, daftar)          // command, hanya mencetak
''', '''
def total_nilai(daftar):            # query
    return sum(daftar)

def cetak_rapor(nama, daftar):      # procedure: efek samping print
    print(f"Rapor {nama}")
    for i, n in enumerate(daftar, 1):
        print(f"  Mapel {i}: {n}")
    print(f"  Total : {total_nilai(daftar)}")

hasil = cetak_rapor("Sinta", [88, 92, 79])
print("nilai kembali prosedur:", hasil)
''')]),

'Parameter by value dan by reference': dict(
  ist=[('Pass by value', 'Fungsi menerima salinan; perubahan tidak terlihat di pemanggil.'),
       ('Pass by reference', 'Fungsi menerima rujukan ke data asli; perubahan terlihat di pemanggil.'),
       ('Pass by object reference', 'Model Python dan Java: rujukan disalin; objek mutable bisa berubah, objek immutable tidak.'),
       ('Defensive copy', 'Menyalin data sebelum diubah agar pemanggil tidak terkejut.')],
  cx=[P('Angka tidak berubah, list berubah', '''
PROSEDUR tambahSatu(BYVAL x)      // salinan
PROSEDUR tambahItem(BYREF daftar)  // data asli
''', '''
def tambah_satu(x):
    x += 1

def tambah_item(daftar):
    daftar.append("baru")

def tambah_item_aman(daftar):
    salinan = list(daftar)       # defensive copy
    salinan.append("baru")
    return salinan

n, d = 5, ["a"]
tambah_satu(n); tambah_item(d)
print("n:", n, "| d:", d)
asli = ["x"]
print("hasil aman:", tambah_item_aman(asli), "| asli tetap:", asli)
''')]),

'Ruang lingkup variabel dan enkapsulasi state': dict(
  ist=[('Scope', 'Wilayah kode tempat variabel dikenal: lokal, global, blok.'),
       ('Global state', 'Variabel global yang bisa diubah dari mana saja; sumber bug yang sulit dilacak.'),
       ('Encapsulation', 'Menyembunyikan state di dalam objek/modul dan hanya membukanya lewat fungsi.'),
       ('Shadowing', 'Variabel lokal bernama sama menutupi variabel luar.')],
  cx=[P('Counter global vs counter terenkapsulasi', '''
// Hindari: GLOBAL nomorAntrian diubah di mana saja
// Lebih baik: objek Antrian dengan method ambilNomor()
''', '''
class Antrian:
    def __init__(self, prefix):
        self._nomor = 0          # state tersembunyi
        self.prefix = prefix
    def ambil(self):
        self._nomor += 1
        return f"{self.prefix}{self._nomor:03}"

cs, teller = Antrian("A"), Antrian("B")
print(cs.ambil(), cs.ambil(), teller.ambil(), cs.ambil())
''')]),

'Rekursi dan base case': dict(
  ist=[('Base case', 'Kondisi berhenti rekursi. Tanpa ini terjadi stack overflow.'),
       ('Recursive case', 'Pemanggilan diri sendiri dengan masalah yang lebih kecil.'),
       ('Call stack', 'Tumpukan pemanggilan fungsi; Python membatasi sekitar 1000 tingkat.'),
       ('Memoization', 'Menyimpan hasil yang sudah dihitung agar rekursi tidak mengulang kerja.')],
  cx=[P('Menghitung total ukuran folder secara rekursif', '''
FUNGSI ukuran(node)
  JIKA node adalah file MAKA RETURN node.ukuran      // base case
  total <- 0
  UNTUK SETIAP anak DALAM node.isi: total <- total + ukuran(anak)
  RETURN total
''', '''
folder = {"src": {"main.py": 12, "util": {"a.py": 4, "b.py": 6}}, "README.md": 2, "img": {"logo.png": 120}}

def ukuran(node):
    if isinstance(node, int):      # base case: file
        return node
    return sum(ukuran(anak) for anak in node.values())

for nama, isi in folder.items():
    print(f"{nama:10} {ukuran(isi):>4} KB")
print(f"{'TOTAL':10} {ukuran(folder):>4} KB")
''')]),

'Array satu dimensi': dict(
  ist=[('Array', 'Kumpulan elemen bertipe sama di memori berurutan, diakses lewat indeks.'),
       ('Zero-based index', 'Indeks dimulai dari 0 di hampir semua bahasa modern; pseudocode buku kadang mulai 1.'),
       ('Fixed vs dynamic size', 'Array Java berukuran tetap; list Python dan ArrayList bisa tumbuh.'),
       ('Out of bounds', 'Mengakses indeks di luar rentang; IndexError di Python, ArrayIndexOutOfBoundsException di Java.')],
  cx=[P('Suhu harian: rata-rata dan hari di atas rata-rata', '''
DECLARE suhu : ARRAY[0..6] OF REAL
rata <- jumlah(suhu) / 7
UNTUK i DARI 0 SAMPAI 6: JIKA suhu[i] > rata MAKA OUTPUT hari[i]
''', '''
hari = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
suhu = [31.2, 32.5, 30.8, 33.1, 34.0, 29.9, 30.4]
rata = sum(suhu) / len(suhu)
print(f"Rata-rata: {rata:.2f}")
print("Di atas rata-rata:", [hari[i] for i in range(len(suhu)) if suhu[i] > rata])
try:
    suhu[7]
except IndexError as e:
    print("suhu[7] ->", type(e).__name__)
''')]),

'Indeks, traversal, dan memperbarui array': dict(
  ist=[('Traversal', 'Mengunjungi setiap elemen sekali.'),
       ('In-place update', 'Mengubah elemen langsung di array tanpa membuat array baru.'),
       ('Two-pointer', 'Teknik dua indeks bergerak dari ujung berbeda; umum di soal interview.'),
       ('Immutable update', 'Membuat array baru berisi perubahan; dipakai di React/Redux.')],
  cx=[P('Membalik array in-place dengan two-pointer', '''
kiri <- 0; kanan <- n - 1
SELAMA kiri < kanan
    tukar a[kiri] dan a[kanan]
    kiri <- kiri + 1; kanan <- kanan - 1
''', '''
a = [3, 8, 1, 9, 4, 7]
kiri, kanan = 0, len(a) - 1
while kiri < kanan:
    a[kiri], a[kanan] = a[kanan], a[kiri]
    kiri += 1; kanan -= 1
print("dibalik:", a)
harga = [10_000, 25_000, 40_000]
for i in range(len(harga)):
    harga[i] = int(harga[i] * 1.05)    # naik 5% in-place
print("harga baru:", harga)
''')]),

'Array multidimensi': dict(
  ist=[('Matriks', 'Array 2 dimensi berbentuk baris x kolom.'),
       ('Row-major order', 'Penyimpanan baris demi baris di memori (C, Python NumPy default).'),
       ('Jagged array', 'Array 2D dengan panjang baris berbeda.'),
       ('Tensor', 'Array berdimensi banyak; istilah utama di machine learning.')],
  cx=[P('Nilai siswa per mapel: total per baris dan rata per kolom', '''
nilai : ARRAY[siswa][mapel]
UNTUK s: totalSiswa[s] <- jumlah baris s
UNTUK m: rataMapel[m] <- jumlah kolom m / jumlahSiswa
''', '''
mapel = ["MTK", "IPA", "BIN"]
nilai = {"Ayu": [85, 90, 78], "Bima": [70, 65, 88], "Citra": [95, 92, 90]}
for nama, baris in nilai.items():
    print(f"{nama:6} {baris} total {sum(baris)}")
for m in range(len(mapel)):
    kolom = [b[m] for b in nilai.values()]
    print(f"rata {mapel[m]}: {sum(kolom) / len(kolom):.1f}")
''')]),

'Struktur record': dict(
  ist=[('Record / struct', 'Satu kesatuan data dengan beberapa field bertipe berbeda.'),
       ('Field', 'Bagian data di record, misalnya nama, harga, stok.'),
       ('DTO (Data Transfer Object)', 'Record yang dipakai mengirim data antar lapisan atau lewat API.'),
       ('dataclass / record', 'Fitur Python dan Java untuk membuat record dengan sedikit kode.')],
  cx=[P('Record produk dan laporan stok menipis', '''
TYPE Produk = RECORD
    sku : STRING; nama : STRING; stok : INTEGER; minimum : INTEGER
END RECORD
''', '''
from dataclasses import dataclass

@dataclass
class Produk:
    sku: str
    nama: str
    stok: int
    minimum: int = 5

gudang = [Produk("K-01", "Kopi 250g", 3), Produk("T-02", "Teh celup", 40), Produk("G-03", "Gula 1kg", 5, 10)]
for p in gudang:
    if p.stok <= p.minimum:
        print(f"Pesan ulang {p.sku} {p.nama}: stok {p.stok}, minimum {p.minimum}")
print(gudang[0])
''')]),

'Linear search dan binary search': dict(
  ist=[('Linear search', 'Memeriksa satu per satu; O(n); tidak perlu data terurut.'),
       ('Binary search', 'Membelah dua ruang pencarian; O(log n); wajib data terurut.'),
       ('Precondition', 'Syarat sebelum algoritma dijalankan, misalnya "array sudah terurut".'),
       ('bisect', 'Modul Python bawaan untuk binary search.')],
  cx=[P('Jumlah langkah linear vs binary pada 1 juta data', '''
FUNGSI binarySearch(a, target)
  lo <- 0; hi <- n - 1
  SELAMA lo <= hi
    mid <- (lo + hi) DIV 2
    JIKA a[mid] = target RETURN mid
    JIKA a[mid] < target MAKA lo <- mid + 1 SELAIN ITU hi <- mid - 1
  RETURN -1
''', '''
def linear(a, t):
    for i, v in enumerate(a):
        if v == t: return i, i + 1
    return -1, len(a)

def biner(a, t):
    lo, hi, langkah = 0, len(a) - 1, 0
    while lo <= hi:
        langkah += 1
        mid = (lo + hi) // 2
        if a[mid] == t: return mid, langkah
        if a[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return -1, langkah

data = list(range(0, 2_000_000, 2))     # 1 juta angka genap terurut
for t in (10, 1_999_998, 777):
    ada = "ada" if biner(data, t)[0] >= 0 else "tidak ada"
    print(f"cari {t:>9} ({ada:9}): linear {linear(data, t)[1]:>7} langkah | binary {biner(data, t)[1]:>2} langkah")
''')]),

'Bubble sort dan insertion sort': dict(
  ist=[('Stable sort', 'Urutan elemen yang sama tetap dipertahankan. Penting saat mengurutkan berdasarkan beberapa kolom.'),
       ('In-place sort', 'Mengurutkan tanpa array tambahan.'),
       ('Adaptive', 'Lebih cepat pada data yang hampir terurut; insertion sort mendekati O(n).'),
       ('Timsort', 'Algoritma bawaan Python dan Java untuk objek; gabungan merge sort dan insertion sort.')],
  cx=[P('Menghitung jumlah pertukaran pada data acak vs hampir terurut', '''
insertionSort(a):
  UNTUK i DARI 1 SAMPAI n-1
    kunci <- a[i]; j <- i - 1
    SELAMA j >= 0 DAN a[j] > kunci
      a[j+1] <- a[j]; j <- j - 1
    a[j+1] <- kunci
''', '''
def bubble(a):
    a, geser = a[:], 0
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]; geser += 1
    return a, geser

def insertion(a):
    a, geser = a[:], 0
    for i in range(1, len(a)):
        kunci, j = a[i], i - 1
        while j >= 0 and a[j] > kunci:
            a[j + 1] = a[j]; j -= 1; geser += 1
        a[j + 1] = kunci
    return a, geser

acak = [9, 4, 7, 1, 8, 2, 6, 3, 5]
hampir = [1, 2, 3, 5, 4, 6, 7, 9, 8]
for nama, d in (("acak", acak), ("hampir terurut", hampir)):
    print(f"{nama:15} bubble {bubble(d)[1]:>2} tukar | insertion {insertion(d)[1]:>2} geser | hasil {insertion(d)[0]}")
''')]),

'Trace table': dict(
  ist=[('Trace table', 'Tabel nilai setiap variabel di setiap langkah; alat utama debugging manual.'),
       ('Desk checking', 'Memeriksa algoritma di atas kertas tanpa komputer.'),
       ('Breakpoint', 'Titik henti di debugger IDE untuk melihat nilai variabel saat program berjalan.'),
       ('Watch expression', 'Ekspresi yang dipantau nilainya selama debugging.')],
  cx=[P('Mencetak trace table otomatis untuk algoritma FPB (Euclid)', '''
SELAMA b <> 0
    sisa <- a MOD b
    a <- b
    b <- sisa
OUTPUT a
''', '''
a, b, langkah = 84, 36, 0
print(f"{'langkah':>7} | {'a':>3} | {'b':>3} | {'sisa':>4}")
while b != 0:
    sisa = a % b
    langkah += 1
    print(f"{langkah:>7} | {a:>3} | {b:>3} | {sisa:>4}")
    a, b = b, sisa
print("FPB =", a)
''')]),

'Off-by-one dan kesalahan logika': dict(
  ist=[('Off-by-one error (OBOE)', 'Loop berjalan satu kali terlalu banyak atau sedikit; bug paling umum.'),
       ('Fencepost problem', 'Pagar 10 meter dengan tiang tiap 1 meter butuh 11 tiang, bukan 10.'),
       ('Boundary value testing', 'Menguji tepat di batas (0, 1, n-1, n, n+1).'),
       ('Logic error', 'Program berjalan tanpa error tetapi hasilnya salah.')],
  cx=[P('Bug klasik: menghitung halaman pagination', '''
// SALAH: halaman <- total DIV per_halaman
// BENAR: halaman <- (total + per_halaman - 1) DIV per_halaman
''', '''
def halaman_salah(total, per):
    return total // per

def halaman_benar(total, per):
    return (total + per - 1) // per     # pembulatan ke atas

print("total | salah | benar")
for total in (0, 1, 10, 11, 20, 21):
    print(f"{total:>5} | {halaman_salah(total, 10):>5} | {halaman_benar(total, 10):>5}")
''', 'Uji tepat di batas (10, 11, 20, 21) untuk menangkap off-by-one.')]),

'Kompleksitas waktu dan ruang': dict(
  ist=[('Big-O', 'Notasi pertumbuhan waktu/memori terhadap ukuran input pada kasus terburuk.'),
       ('O(1), O(log n), O(n), O(n log n), O(n²)', 'Kelas kompleksitas yang paling sering ditanyakan di interview.'),
       ('Space complexity', 'Tambahan memori yang dipakai algoritma.'),
       ('Trade-off waktu vs ruang', 'Memakai memori lebih (cache, hash set) agar lebih cepat.')],
  cx=[P('Cek duplikat: O(n²) vs O(n) dengan set', '''
// O(n²): bandingkan setiap pasangan
// O(n) : simpan yang sudah dilihat di himpunan
UNTUK SETIAP x DALAM data
    JIKA x DALAM dilihat MAKA RETURN BENAR
    tambahkan x ke dilihat
''', '''
import time

def duplikat_kuadrat(a):
    return any(a[i] == a[j] for i in range(len(a)) for j in range(i + 1, len(a)))

def duplikat_linear(a):
    dilihat = set()
    for x in a:
        if x in dilihat: return True
        dilihat.add(x)
    return False

for n in (1_000, 2_000, 4_000):
    data = list(range(n))
    t = time.perf_counter(); duplikat_kuadrat(data); k = time.perf_counter() - t
    t = time.perf_counter(); duplikat_linear(data); l = time.perf_counter() - t
    print(f"n={n:>5}: O(n^2) {k*1000:7.1f} ms | O(n) {l*1000:5.2f} ms")
print("Perhatikan: n naik 2x, O(n^2) naik sekitar 4x")
''')]),

'Menerjemahkan pseudocode ke Python': dict(
  ist=[('Translation mapping', 'Tabel padanan: ← menjadi =, ENDIF hilang karena indentasi, MOD menjadi %.'),
       ('Pythonic', 'Gaya penulisan yang wajar di Python (comprehension, enumerate, unpacking).'),
       ('Zero vs one-based', 'Pseudocode buku sering mulai indeks 1; Python mulai 0. Sesuaikan batas loop.'),
       ('Integer division', 'DIV di pseudocode adalah // di Python, bukan /.')],
  cx=[P('Pseudocode buku (indeks 1) diterjemahkan dengan benar', '''
maks <- A[1]
UNTUK i DARI 2 SAMPAI n
    JIKA A[i] > maks MAKA maks <- A[i]
tengah <- n DIV 2
''', '''
A = [42, 17, 88, 63, 5]
n = len(A)

maks = A[0]                      # A[1] di buku -> A[0] di Python
for i in range(1, n):            # 2..n di buku -> 1..n-1
    if A[i] > maks:
        maks = A[i]
tengah = n // 2                  # DIV -> //
print("maks:", maks, "| tengah:", tengah, "| bukan", n / 2)
print("versi Pythonic:", max(A))
''')]),

'Adaptasi ke bahasa bertipe kuat': dict(
  ist=[('Static typing', 'Tipe variabel dicek saat kompilasi (Java, Kotlin, TypeScript, Go).'),
       ('Type annotation', 'Petunjuk tipe di Python (int, list[str]) yang dicek alat seperti mypy/pyright.'),
       ('Type inference', 'Compiler menebak tipe dari nilai (var di Java, val di Kotlin).'),
       ('Null safety', 'Sistem tipe yang membedakan nilai boleh null dan tidak (String? di Kotlin).')],
  cx=[T('Satu pseudocode di Python, Java, Kotlin, dan TypeScript', '''
PSEUDOCODE
  FUNGSI rataRata(nilai : ARRAY OF INTEGER) -> REAL
      RETURN jumlah(nilai) / panjang(nilai)

PYTHON (dengan type hint)
  def rata_rata(nilai: list[int]) -> float:
      return sum(nilai) / len(nilai)

JAVA
  static double rataRata(int[] nilai) {
      return Arrays.stream(nilai).average().orElse(0);
  }

KOTLIN
  fun rataRata(nilai: List<Int>): Double = nilai.average()

TYPESCRIPT
  function rataRata(nilai: number[]): number {
    return nilai.reduce((a, b) => a + b, 0) / nilai.length;
  }
''', 'Perhatikan bahwa di Java pembagian dua int menghasilkan int; karena itu average() atau casting ke double diperlukan.')]),

'Standar dokumentasi dan keterbacaan': dict(
  ist=[('Docstring / Javadoc / KDoc', 'Komentar dokumentasi resmi di awal fungsi: tujuan, parameter, nilai kembali, contoh.'),
       ('Self-documenting code', 'Nama variabel dan fungsi yang menjelaskan dirinya sendiri sehingga komentar minimal.'),
       ('Code review', 'Pemeriksaan kode oleh rekan sebelum digabung; keterbacaan adalah kriteria utama.'),
       ('Doctest', 'Contoh di docstring yang sekaligus dijalankan sebagai tes.')],
  cx=[P('Docstring dengan doctest yang benar-benar diuji', '''
FUNGSI hariKerja(mulai, jumlahHari)
  // Menghitung tanggal selesai dengan melewati Sabtu dan Minggu
''', '''
import datetime as dt, doctest

def tambah_hari_kerja(mulai: dt.date, n: int) -> dt.date:
    """Tanggal setelah n hari kerja (Senin-Jumat) dari `mulai`.

    >>> tambah_hari_kerja(dt.date(2026, 11, 20), 1)   # Jumat + 1
    datetime.date(2026, 11, 23)
    >>> tambah_hari_kerja(dt.date(2026, 11, 16), 5)
    datetime.date(2026, 11, 23)
    """
    hari = mulai
    while n > 0:
        hari += dt.timedelta(days=1)
        if hari.weekday() < 5:
            n -= 1
    return hari

runner = doctest.DocTestRunner()
for tes in doctest.DocTestFinder().find(tambah_hari_kerja, globs={"dt": dt, "tambah_hari_kerja": tambah_hari_kerja}):
    runner.run(tes)
hasil = runner.summarize(verbose=False)
print(f"doctest: {hasil.attempted} contoh diuji, {hasil.failed} gagal")
print("SLA 3 hari kerja dari Kamis 19/11/2026:", tambah_hari_kerja(dt.date(2026, 11, 19), 3))
''')]),
}
