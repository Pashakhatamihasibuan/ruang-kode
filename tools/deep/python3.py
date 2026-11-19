"""Pendalaman jalur Python (bagian 3: rekursi, struktur data, type hints, kualitas kode, konkurensi, web, latihan).
Contoh dijalankan dengan CPython 3.13 (hanya pustaka standar + Pydantic)."""
K = 'python'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Rekursi': dict(
  ist=[('Recursion', 'Fungsi yang memanggil dirinya sendiri untuk menyelesaikan versi masalah yang lebih kecil.'),
       ('Call stack', 'Tumpukan pemanggilan fungsi; setiap panggilan rekursif menambah satu frame.'),
       ('RecursionError', 'Error saat kedalaman rekursi melewati batas (bawaan sekitar 1000).'),
       ('Recursive data', 'Data yang bentuknya bersarang: folder, menu bertingkat, struktur organisasi, JSON.')],
  cx=[P('Menjumlah anggaran pada struktur organisasi bersarang', '''
org = {"nama": "Direksi", "anggaran": 500, "bawahan": [
         {"nama": "IT", "anggaran": 300, "bawahan": [
             {"nama": "Infra", "anggaran": 120, "bawahan": []},
             {"nama": "Aplikasi", "anggaran": 180, "bawahan": [{"nama": "Mobile", "anggaran": 90, "bawahan": []}]}]},
         {"nama": "Keuangan", "anggaran": 150, "bawahan": []}]}

def total(unit):
    return unit["anggaran"] + sum(total(b) for b in unit["bawahan"])

def cetak(unit, tingkat=0):
    print("  " * tingkat + f"- {unit['nama']} (total {total(unit)} jt)")
    for b in unit["bawahan"]: cetak(b, tingkat + 1)

cetak(org)
import sys
print("batas rekursi bawaan:", sys.getrecursionlimit())
''', 'Kedalaman struktur organisasi atau folder tidak diketahui sebelumnya, sehingga rekursi lebih alami daripada loop bersarang.')]),

'Base case & recursive case': dict(
  ist=[('Base case', 'Kondisi berhenti yang dijawab langsung tanpa rekursi.'),
       ('Recursive case', 'Langkah yang memanggil fungsi dengan masalah lebih kecil, mendekati base case.'),
       ('Infinite recursion', 'Rekursi tanpa base case yang tercapai; berakhir RecursionError.'),
       ('Divide and conquer', 'Strategi membagi masalah menjadi beberapa bagian kecil, menyelesaikan, lalu menggabungkan.')],
  cx=[P('Meratakan daftar kategori bersarang', '''
def ratakan(data):
    if not isinstance(data, list):        # base case: bukan list, kembalikan sebagai satu elemen
        return [data]
    hasil = []
    for x in data:                        # recursive case: setiap elemen diratakan
        hasil.extend(ratakan(x))
    return hasil

kategori = ["Elektronik", ["HP", ["Android", "iOS"], "Tablet"], [["Laptop"]], "Fashion"]
print(ratakan(kategori))

def tanpa_base(n): return tanpa_base(n - 1)
try: tanpa_base(5)
except RecursionError: print("tanpa base case -> RecursionError")
''')]),

'Rekursi pada angka': dict(
  ist=[('Factorial', 'n! = n x (n-1)!; contoh klasik rekursi dengan base case 0! = 1.'),
       ('Memoization', 'Menyimpan hasil pemanggilan agar subsoal yang sama tidak dihitung ulang.'),
       ('Exponential time', 'Rekursi Fibonacci naif bercabang dua sehingga waktunya O(2^n).'),
       ('Fast exponentiation', 'Menghitung a^n dengan membagi pangkat dua: O(log n) perkalian.')],
  cx=[P('Fibonacci naif vs memoization, dan pangkat cepat', '''
from functools import lru_cache
panggilan = 0
def fib_naif(n):
    global panggilan; panggilan += 1
    return n if n < 2 else fib_naif(n - 1) + fib_naif(n - 2)

@lru_cache(maxsize=None)
def fib_memo(n):
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)

print("fib(25) =", fib_naif(25), "dengan", f"{panggilan:,}".replace(",", "."), "panggilan naif")
print("fib(25) memo:", fib_memo(25), "dengan", fib_memo.cache_info().misses, "perhitungan unik")
print("fib(200) memo:", fib_memo(200))

def pangkat(a, n):
    if n == 0: return 1
    setengah = pangkat(a, n // 2)
    return setengah * setengah * (a if n % 2 else 1)
print("2^64 =", pangkat(2, 64), "| sama dengan **:", pangkat(3, 41) == 3 ** 41)
''')]),

'Binary search: membagi dua sampai ketemu': dict(
  ist=[('Halving', 'Setiap langkah membuang separuh data; 1 juta data selesai dalam paling banyak 20 langkah.'),
       ('Recursive vs iterative', 'Binary search bisa ditulis rekursif (lebih dekat ke definisi) atau iteratif (tanpa batas kedalaman).'),
       ('First / last occurrence', 'Varian yang mencari kemunculan pertama atau terakhir dari nilai yang berulang.'),
       ('Precondition: sorted', 'Binary search hanya benar pada data terurut; data tak terurut memberi jawaban salah tanpa error.')],
  cx=[P('Rekursif vs iteratif, kemunculan pertama, dan jebakan data tak terurut', '''
import math
def cari_rek(a, x, lo=0, hi=None):
    hi = len(a) - 1 if hi is None else hi
    if lo > hi: return -1
    mid = (lo + hi) // 2
    if a[mid] == x: return mid
    return cari_rek(a, x, mid + 1, hi) if a[mid] < x else cari_rek(a, x, lo, mid - 1)

def pertama(a, x):
    lo, hi, hasil = 0, len(a) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] >= x:
            if a[mid] == x: hasil = mid
            hi = mid - 1
        else: lo = mid + 1
    return hasil

tanggal = ["2026-11-01", "2026-11-03", "2026-11-03", "2026-11-03", "2026-11-07", "2026-11-12"]
print("rekursif cari 2026-11-07:", cari_rek(tanggal, "2026-11-07"))
print("transaksi pertama 2026-11-03 di indeks", pertama(tanggal, "2026-11-03"))
for n in [1_000, 1_000_000, 1_000_000_000]:
    print(f"{n:>13,} data -> maksimal {math.ceil(math.log2(n + 1))} langkah".replace(",", "."))
print("data tak terurut, cari 7:", cari_rek([9, 7, 1, 3, 5], 7), "(salah, padahal 7 ada di indeks 1)")
''')]),

'Pencarian & Pengurutan': dict(
  ist=[('Linear search', 'Memeriksa satu per satu: O(n), tidak butuh data terurut.'),
       ('Stable sort', 'Pengurutan yang menjaga urutan asli elemen bernilai sama; sorted() Python stabil.'),
       ('Timsort', 'Algoritma pengurutan bawaan Python (dan Java untuk objek): gabungan merge sort dan insertion sort.'),
       ('Sort then search', 'Jika data dicari berkali-kali, urutkan sekali lalu gunakan binary search.')],
  cx=[P('Pengurutan stabil untuk laporan bertingkat', '''
siswa = [("Ani", "XI-A", 88), ("Budi", "XI-B", 92), ("Citra", "XI-A", 92), ("Dedi", "XI-B", 88), ("Eka", "XI-A", 75)]
urut = sorted(siswa, key=lambda s: s[2], reverse=True)   # nilai menurun
urut = sorted(urut, key=lambda s: s[1])                 # lalu kelas; urutan nilai tetap terjaga (stabil)
for s in urut: print(*s)

def linear(data, target):
    for i, x in enumerate(data):
        if x[0] == target: return i
    return -1
print("posisi Dedi:", linear(siswa, "Dedi"), "| Zaki:", linear(siswa, "Zaki"))
''', 'Karena sort stabil, mengurutkan dua kali (kunci sekunder dulu, lalu kunci utama) memberi hasil bertingkat yang benar.')]),

'Binary search': dict(
  ist=[('Binary search', 'Mencari di data terurut dengan membuang separuh ruang pencarian tiap langkah: O(log n).'),
       ('Lower bound', 'Posisi pertama yang nilainya >= target; bisect_left di Python.'),
       ('Search on answer', 'Binary search atas jawaban numerik, misalnya kapasitas minimum yang cukup.'),
       ('Overflow-safe mid', 'lo + (hi - lo) // 2; di Python tidak overflow, tetapi penting di Java/C.')],
  cx=[P('Binary search manual, bisect, dan "search on answer"', '''
from bisect import bisect_left
harga = [5_000, 12_000, 18_000, 25_000, 40_000, 55_000, 90_000]

def cari(data, x):
    lo, hi, langkah = 0, len(data) - 1, 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2; langkah += 1
        if data[mid] == x: return mid, langkah
        if data[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return -1, langkah
print("cari 40.000:", cari(harga, 40_000), "| cari 41.000:", cari(harga, 41_000))
print("produk pertama >= 20.000 di indeks", bisect_left(harga, 20_000))

paket = [4, 8, 2, 7, 5, 9, 3]          # berat paket (kg) urut sesuai antrean
def cukup(kapasitas, hari=3):
    truk, isi = 1, 0
    for p in paket:
        if isi + p > kapasitas: truk, isi = truk + 1, 0
        isi += p
    return truk <= hari
lo, hi = max(paket), sum(paket)
while lo < hi:
    mid = (lo + hi) // 2
    if cukup(mid): hi = mid
    else: lo = mid + 1
print("kapasitas truk minimum agar selesai 3 hari:", lo, "kg")
''')]),

'Selection sort': dict(
  ist=[('Selection sort', 'Berulang memilih elemen terkecil dari sisa data lalu menukarnya ke depan: O(n²).'),
       ('In-place', 'Mengurutkan tanpa list tambahan; memori O(1).'),
       ('Number of swaps', 'Selection sort hanya melakukan paling banyak n-1 pertukaran; berguna jika menulis data mahal.'),
       ('Unstable', 'Selection sort tidak stabil: elemen bernilai sama bisa berubah urutan.')],
  cx=[P('Selection sort dengan penghitung perbandingan dan pertukaran', '''
def selection_sort(a):
    a = list(a); banding = tukar = 0
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            banding += 1
            if a[j] < a[m]: m = j
        if m != i:
            a[i], a[m] = a[m], a[i]; tukar += 1
    return a, banding, tukar

for n in [10, 100, 1000]:
    import random; random.seed(n)
    data = random.sample(range(10 * n), n)
    hasil, b, t = selection_sort(data)
    bb = f"{b:,}".replace(",", ".")
    print(f"n={n:>4}: {bb:>7} perbandingan, {t:>4} pertukaran, benar={hasil == sorted(data)}")
''', 'Perbandingan naik sekitar 100 kali saat n naik 10 kali, bukti nyata O(n²). Pertukaran tetap sedikit.')]),

'Menghitung Big-O': dict(
  ist=[('Big-O', 'Batas atas pertumbuhan waktu atau memori terhadap ukuran input n.'),
       ('Drop constants', 'O(2n) ditulis O(n); konstanta dan suku kecil diabaikan.'),
       ('Worst / average case', 'Kasus terburuk vs rata-rata; hash table O(1) rata-rata tetapi O(n) terburuk.'),
       ('Empirical profiling', 'Mengukur waktu nyata untuk beberapa ukuran n dan melihat rasio pertumbuhannya.')],
  cx=[P('Mengukur pertumbuhan secara empiris (operasi dihitung)', '''
def hitung(f, n):
    op = [0]
    f(n, op)
    return op[0]

def konstan(n, op): op[0] += 1
def log_n(n, op):
    while n > 1: n //= 2; op[0] += 1
def linier(n, op):
    for _ in range(n): op[0] += 1
def n_log_n(n, op):
    for _ in range(n): log_n(n, op)
def kuadrat(n, op):
    for _ in range(n):
        for _ in range(n): op[0] += 1

print(f"{'n':>6} {'O(1)':>5} {'O(log n)':>9} {'O(n)':>7} {'O(n log n)':>11} {'O(n^2)':>10}")
for n in [10, 100, 1000]:
    print(f"{n:>6} {hitung(konstan, n):>5} {hitung(log_n, n):>9} {hitung(linier, n):>7,} {hitung(n_log_n, n):>11,} {hitung(kuadrat, n):>10,}".replace(",", "."))
''', 'Menghitung operasi memberi angka yang sama di semua komputer, berbeda dengan mengukur detik.')]),

'Stack & Queue': dict(
  ist=[('Abstract data type', 'Struktur didefinisikan dari operasinya (push/pop, enqueue/dequeue), bukan implementasinya.'),
       ('LIFO / FIFO', 'Last In First Out (stack) vs First In First Out (queue).'),
       ('Message queue', 'Antrean pesan antarlayanan: RabbitMQ, Kafka, SQS, Redis Streams.'),
       ('Undo stack', 'Riwayat aksi disimpan di stack agar aksi terakhir bisa dibatalkan.')],
  cx=[P('Editor dengan undo/redo (stack) dan antrean cetak (queue)', '''
from collections import deque
teks, undo, redo = "", [], []
def ketik(s):
    global teks; undo.append(teks); redo.clear(); teks += s
def batal():
    global teks; redo.append(teks); teks = undo.pop()
def ulang():
    global teks; undo.append(teks); teks = redo.pop()

ketik("Halo"); ketik(" dunia"); ketik("!!!")
batal(); print("undo :", repr(teks)); ulang(); print("redo :", repr(teks))

cetak = deque()
for dok in ["invoice.pdf", "surat.docx", "laporan.xlsx"]: cetak.append(dok)
while cetak: print("mencetak", cetak.popleft())
''')]),

'Stack (LIFO)': dict(
  ist=[('push / pop / peek', 'Menaruh di atas, mengambil dari atas, melihat elemen teratas tanpa mengambil.'),
       ('Balanced brackets', 'Soal klasik validasi kurung dengan stack; dipakai di parser dan linter.'),
       ('Call stack', 'Stack yang dipakai runtime untuk menyimpan pemanggilan fungsi.'),
       ('Stack overflow', 'Stack penuh, misalnya karena rekursi terlalu dalam.')],
  cx=[P('Validasi kurung dan evaluasi ekspresi postfix', '''
def seimbang(s):
    pasangan, stack = {")": "(", "]": "[", "}": "{"}, []
    for i, c in enumerate(s):
        if c in "([{": stack.append((c, i))
        elif c in pasangan:
            if not stack or stack[-1][0] != pasangan[c]: return f"tidak seimbang di posisi {i}"
            stack.pop()
    return "seimbang" if not stack else f"kurung '{stack[-1][0]}' di posisi {stack[-1][1]} tidak ditutup"

for s in ['{"a": [1, 2]}', "f(x[0)]", "if (a > (b + c)"]: print(f"{s:<16} -> {seimbang(s)}")

def postfix(ekspr):                     # "3 4 + 2 *" = (3 + 4) * 2
    st = []
    for tok in ekspr.split():
        if tok in "+-*/":
            b, a = st.pop(), st.pop()
            st.append({"+": a + b, "-": a - b, "*": a * b, "/": a / b}[tok])
        else: st.append(float(tok))
    return st.pop()
print("3 4 + 2 * =", postfix("3 4 + 2 *"), "| 5 1 2 + 4 * + 3 - =", postfix("5 1 2 + 4 * + 3 -"))
''')]),

'Queue (FIFO)': dict(
  ist=[('enqueue / dequeue', 'Menambah di belakang, mengambil dari depan.'),
       ('Bounded queue', 'Antrean berkapasitas tetap; deque(maxlen=n) membuang elemen paling lama.'),
       ('Backpressure', 'Menahan atau menolak pekerjaan baru saat antrean penuh agar sistem tidak kewalahan.'),
       ('Round robin', 'Pembagian giliran bergantian, misalnya membagi tiket ke agen CS.')],
  cx=[P('Pembagian tiket round robin dan buffer log terbatas', '''
from collections import deque
agen = deque(["Rina", "Bayu", "Sinta"])
for tiket in range(101, 108):
    a = agen[0]; agen.rotate(-1)
    print(f"tiket #{tiket} -> {a}")

log = deque(maxlen=3)                   # hanya 3 log terakhir disimpan
for i in range(1, 7): log.append(f"event-{i}")
print("buffer log:", list(log))

antrean, KAPASITAS = deque(), 4
for req in range(1, 7):
    if len(antrean) >= KAPASITAS: print(f"request {req}: 503 sibuk, coba lagi nanti"); continue
    antrean.append(req)
print("diterima:", list(antrean))
''')]),

'Membuat Kelas Koleksi': dict(
  ist=[('Collection class', 'Kelas yang menyimpan banyak elemen dan menyediakan operasi untuk mengelolanya.'),
       ('collections.abc', 'Kelas dasar abstrak (Sequence, MutableMapping) yang melengkapi method otomatis.'),
       ('Iteration protocol', 'Menyediakan __iter__ agar koleksi bisa dipakai di for.'),
       ('Interface completeness', 'Dengan mewarisi Sequence, cukup __getitem__ dan __len__ untuk mendapat in, index, count, reversed.')],
  cx=[P('Koleksi SortedList berbasis collections.abc', '''
from collections.abc import Sequence
from bisect import insort, bisect_left

class SortedList(Sequence):
    def __init__(self, data=()): self._d = sorted(data)
    def __getitem__(self, i): return self._d[i]
    def __len__(self): return len(self._d)
    def add(self, x): insort(self._d, x)
    def __contains__(self, x):                 # O(log n), menggantikan versi O(n) bawaan
        i = bisect_left(self._d, x); return i < len(self._d) and self._d[i] == x
    def __repr__(self): return f"SortedList({self._d})"

s = SortedList([42, 7, 19])
s.add(3); s.add(25)
print(s, "| 19 in s:", 19 in s, "| index(25):", s.index(25), "| reversed:", list(reversed(s)))
print("count, index, reversed didapat gratis dari Sequence:", all(hasattr(s, m) for m in ["count", "index", "__reversed__"]))
''')]),

'Menambah elemen & memperbesar kapasitas': dict(
  ist=[('Resizing', 'Saat penuh, buat array baru lebih besar lalu salin isinya.'),
       ('Growth factor', 'Faktor pembesaran (sering 1.5x atau 2x); makin besar makin jarang menyalin tetapi boros memori.'),
       ('Amortized analysis', 'Biaya rata-rata per operasi dalam rangkaian panjang; append tetap O(1) teramortisasi.'),
       ('Copy cost', 'Jumlah elemen yang disalin saat resize; totalnya O(n) untuk n append.')],
  cx=[P('ArrayList buatan sendiri: menghitung biaya salin', '''
class ArrayList:
    def __init__(self, kap=2, faktor=2):
        self._data, self._n, self.faktor, self.disalin = [None] * kap, 0, faktor, 0
    def append(self, x):
        if self._n == len(self._data):
            baru = [None] * max(1, int(len(self._data) * self.faktor))
            for i in range(self._n): baru[i] = self._data[i]
            self.disalin += self._n; self._data = baru
        self._data[self._n] = x; self._n += 1

for faktor in [2, 1.5]:
    a = ArrayList(faktor=faktor)
    for i in range(100_000): a.append(i)
    kap, salin = (f"{x:,}".replace(",", ".") for x in (len(a._data), a.disalin))
    desimal = lambda x: f"{x:.1f}".replace(".", ",")
    print(f"faktor {desimal(faktor)}: kapasitas {kap}, total salin {salin} ({desimal(a.disalin / 100_000)} salinan per append)")

class TumbuhTetap(ArrayList):          # pembesaran +10 slot: salahnya di sini
    def append(self, x):
        if self._n == len(self._data):
            self._data += [None] * 10; self.disalin += self._n
        self._data[self._n] = x; self._n += 1
t = TumbuhTetap()
for i in range(20_000): t.append(i)
print(f"tambah +10 slot: {t.disalin:,} salinan untuk 20.000 append -> O(n²)".replace(",", "."))
''')]),

'Precondition & exception': dict(
  ist=[('Precondition', 'Syarat yang harus benar sebelum method dipanggil, misalnya indeks valid.'),
       ('Postcondition', 'Jaminan setelah method selesai, misalnya ukuran bertambah satu.'),
       ('Fail fast', 'Gagal sedini mungkin dengan pesan jelas daripada membiarkan data rusak menyebar.'),
       ('assert', 'Pemeriksaan untuk developer; bisa dimatikan dengan python -O, jadi jangan dipakai untuk validasi input.')],
  cx=[P('Stack dengan precondition yang jelas', '''
class StackKosong(Exception): pass

class Stack:
    def __init__(self, kapasitas):
        if not isinstance(kapasitas, int) or kapasitas <= 0:
            raise ValueError(f"kapasitas harus int positif, didapat {kapasitas!r}")
        self._d, self.kap = [], kapasitas
    def push(self, x):
        if len(self._d) >= self.kap: raise OverflowError(f"stack penuh ({self.kap})")
        n = len(self._d); self._d.append(x)
        assert len(self._d) == n + 1            # postcondition (alat debug)
    def pop(self):
        if not self._d: raise StackKosong("pop pada stack kosong")
        return self._d.pop()

for aksi in [lambda: Stack(0), lambda: Stack(1).pop(), lambda: [s := Stack(1), s.push(1), s.push(2)]]:
    try: aksi()
    except (ValueError, OverflowError, StackKosong) as e: print(f"{type(e).__name__}: {e}")
''')]),

'Linked List': dict(
  ist=[('Node', 'Simpul berisi data dan referensi ke simpul berikutnya.'),
       ('Head / tail', 'Simpul pertama dan terakhir; menyimpan tail membuat tambah di akhir O(1).'),
       ('Doubly linked list', 'Setiap simpul juga menunjuk ke sebelumnya; dipakai di LRU cache.'),
       ('Cache locality', 'Array lebih ramah cache CPU daripada linked list, sehingga sering lebih cepat dalam praktik.')],
  cx=[P('LRU cache dengan OrderedDict (doubly linked list di dalamnya)', '''
from collections import OrderedDict

class LRUCache:
    def __init__(self, kapasitas): self.kap, self.d = kapasitas, OrderedDict()
    def get(self, k):
        if k not in self.d: return None
        self.d.move_to_end(k); return self.d[k]          # O(1) berkat linked list internal
    def put(self, k, v):
        self.d[k] = v; self.d.move_to_end(k)
        if len(self.d) > self.kap:
            lama, _ = self.d.popitem(last=False); print(f"  usir {lama}")

c = LRUCache(2)
c.put("produk:1", "Kopi"); c.put("produk:2", "Teh")
c.get("produk:1")                                     # produk:1 jadi paling baru dipakai
c.put("produk:3", "Susu")                             # produk:2 diusir
print("isi cache:", list(c.d))
''', 'Redis, CDN, dan browser memakai kebijakan LRU (Least Recently Used) untuk memutuskan data mana yang dibuang.')]),

'Node & menambah di depan': dict(
  ist=[('Prepend', 'Menambah di depan linked list: O(1), cukup ubah head.'),
       ('Sentinel node', 'Simpul palsu di awal agar kode tidak perlu kasus khusus untuk list kosong.'),
       ('Persistent structure', 'Struktur yang versi lamanya tetap utuh; prepend pada linked list berbagi ekor yang sama.'),
       ('__slots__', 'Membatasi atribut objek agar hemat memori; berguna untuk jutaan Node.')],
  cx=[P('Prepend O(1) dan berbagi ekor antar versi', '''
class Node:
    __slots__ = ("data", "next")
    def __init__(self, data, next=None): self.data, self.next = data, next

def ke_list(n):
    out = []
    while n: out.append(n.data); n = n.next
    return out

v1 = Node("C", Node("D"))
v2 = Node("B", v1)          # prepend: versi baru
v3 = Node("A", v2)
alt = Node("X", v1)          # versi lain berbagi ekor yang sama
print("v3 :", ke_list(v3)); print("alt:", ke_list(alt)); print("v1 tetap:", ke_list(v1))
print("ekor dipakai bersama:", v2.next is alt.next)
''', 'Pola berbagi ekor ini dipakai riwayat commit Git dan struktur data immutable di bahasa fungsional.')]),

'Menelusuri linked list': dict(
  ist=[('Traversal', 'Berjalan dari head mengikuti next sampai None.'),
       ('Two pointers (fast/slow)', 'Dua penunjuk dengan kecepatan berbeda; dipakai mencari tengah dan mendeteksi siklus.'),
       ("Floyd's cycle detection", 'Algoritma kura-kura dan kelinci untuk mendeteksi loop pada linked list.'),
       ('In-place reversal', 'Membalik arah next tanpa memori tambahan.')],
  cx=[P('Tengah list, deteksi siklus, dan membalik', '''
class Node:
    def __init__(self, d, n=None): self.d, self.n = d, n
def buat(*xs):
    head = None
    for x in reversed(xs): head = Node(x, head)
    return head
def tampil(h):
    out = []
    while h: out.append(h.d); h = h.n
    return out

def tengah(h):
    lambat = cepat = h
    while cepat and cepat.n: lambat, cepat = lambat.n, cepat.n.n
    return lambat.d
def ada_siklus(h):
    lambat = cepat = h
    while cepat and cepat.n:
        lambat, cepat = lambat.n, cepat.n.n
        if lambat is cepat: return True
    return False
def balik(h):
    prev = None
    while h: h.n, prev, h = prev, h, h.n
    return prev

L = buat(1, 2, 3, 4, 5)
print("tengah:", tengah(L), "| siklus:", ada_siklus(L))
ekor = L.n.n.n.n; ekor.n = L.n.n            # buat siklus 5 -> 3
print("setelah dibuat siklus:", ada_siklus(L)); ekor.n = None
print("dibalik:", tampil(balik(L)))
''')]),

'Pohon Biner': dict(
  ist=[('Binary tree', 'Setiap simpul punya paling banyak dua anak: kiri dan kanan.'),
       ('Height', 'Panjang jalur terpanjang dari akar ke daun; menentukan kecepatan operasi.'),
       ('Leaf', 'Simpul tanpa anak.'),
       ('Expression tree', 'Pohon yang mewakili ekspresi matematika; dipakai compiler dan kalkulator.')],
  cx=[P('Pohon ekspresi: hitung dan cetak', '''
class N:
    def __init__(self, v, kiri=None, kanan=None): self.v, self.kiri, self.kanan = v, kiri, kanan

OPS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b}
def hitung(n):
    if n.v not in OPS: return n.v
    return OPS[n.v](hitung(n.kiri), hitung(n.kanan))
def infix(n):
    if n.v not in OPS: return str(n.v)
    return f"({infix(n.kiri)} {n.v} {infix(n.kanan)})"
def tinggi(n): return 0 if n is None else 1 + max(tinggi(n.kiri), tinggi(n.kanan))
def daun(n): return 0 if n is None else 1 if not (n.kiri or n.kanan) else daun(n.kiri) + daun(n.kanan)

# harga * qty - diskon, lalu + ongkir
pohon = N("+", N("-", N("*", N(25_000), N(4)), N(10_000)), N(15_000))
print(infix(pohon), "=", hitung(pohon))
print("tinggi:", tinggi(pohon), "| daun:", daun(pohon))
''')]),

'Menyisipkan ke BST': dict(
  ist=[('Binary search tree', 'Pohon biner dengan aturan: kiri < simpul < kanan.'),
       ('Degenerate tree', 'BST yang menjadi seperti linked list karena data masuk terurut; operasi menjadi O(n).'),
       ('Self-balancing tree', 'AVL, red-black tree, B-tree: menjaga tinggi O(log n) otomatis.'),
       ('B-tree', 'Pohon seimbang dengan banyak anak per simpul; struktur indeks database (PostgreSQL, MySQL).')],
  cx=[P('Urutan masuk menentukan tinggi BST', '''
import random
class N:
    __slots__ = ("k", "l", "r")
    def __init__(self, k): self.k, self.l, self.r = k, None, None

def sisip(akar, k):
    if akar is None: return N(k)
    n = akar
    while True:
        arah = "l" if k < n.k else "r"
        anak = getattr(n, arah)
        if anak is None: setattr(n, arah, N(k)); return akar
        n = anak

def tinggi(n):
    t, tumpuk = 0, [(n, 1)]
    while tumpuk:
        x, d = tumpuk.pop()
        if x: t = max(t, d); tumpuk += [(x.l, d + 1), (x.r, d + 1)]
    return t

data = list(range(1, 2001))
acak = data[:]; random.Random(1).shuffle(acak)
for nama, urutan in [("terurut", data), ("acak", acak)]:
    akar = None
    for k in urutan: akar = sisip(akar, k)
    print(f"{nama:<8}: tinggi {tinggi(akar)} untuk 2.000 data (ideal ~11)")
''', 'Inilah alasan database memakai B-tree yang selalu seimbang, bukan BST biasa.')]),

'Traversal in-order': dict(
  ist=[('In-order', 'Kiri, simpul, kanan; pada BST menghasilkan urutan menaik.'),
       ('Pre-order / post-order', 'Simpul dulu (menyalin pohon) / anak dulu (menghapus atau menghitung ukuran folder).'),
       ('Level-order (BFS)', 'Per tingkat dengan queue; dipakai menampilkan bagan organisasi per level.'),
       ('Iterative traversal', 'Traversal dengan stack eksplisit agar tidak terbatas kedalaman rekursi.')],
  cx=[P('Empat cara menelusuri pohon yang sama', '''
from collections import deque
class N:
    def __init__(self, k, l=None, r=None): self.k, self.l, self.r = k, l, r
#        50
#      /    \\
#    30      70
#   /  \\       \\
#  20  40      80
akar = N(50, N(30, N(20), N(40)), N(70, None, N(80)))

def inorder(n): return inorder(n.l) + [n.k] + inorder(n.r) if n else []
def preorder(n): return [n.k] + preorder(n.l) + preorder(n.r) if n else []
def postorder(n): return postorder(n.l) + postorder(n.r) + [n.k] if n else []
def level(n):
    out, q = [], deque([(n, 0)])
    while q:
        x, d = q.popleft()
        if x:
            if len(out) <= d: out.append([])
            out[d].append(x.k); q += [(x.l, d + 1), (x.r, d + 1)]
    return out
def inorder_iter(n):
    out, st = [], []
    while st or n:
        while n: st.append(n); n = n.l
        n = st.pop(); out.append(n.k); n = n.r
    return out

print("in-order  :", inorder(akar), "| iteratif sama:", inorder_iter(akar) == inorder(akar))
print("pre-order :", preorder(akar))
print("post-order:", postorder(akar))
print("per level :", level(akar))
''')]),

'Struktur Data Lanjutan': dict(
  ist=[('Trie', 'Pohon awalan kata; dipakai autocomplete dan routing URL.'),
       ('Union-Find', 'Struktur untuk mengelompokkan elemen yang terhubung; dipakai deduplikasi dan jaringan.'),
       ('Bloom filter', 'Struktur probabilistik hemat memori untuk "mungkin ada / pasti tidak ada".'),
       ('Graph', 'Simpul dan sisi; mewakili jaringan sosial, rute, dependensi.')],
  cx=[P('Autocomplete dengan trie', '''
class Trie:
    def __init__(self): self.anak, self.akhir, self.populer = {}, False, 0
    def tambah(self, kata, skor):
        n = self
        for c in kata: n = n.anak.setdefault(c, Trie())
        n.akhir, n.populer = True, skor
    def saran(self, awalan, k=3):
        n = self
        for c in awalan:
            if c not in n.anak: return []
            n = n.anak[c]
        hasil, st = [], [(n, awalan)]
        while st:
            x, s = st.pop()
            if x.akhir: hasil.append((x.populer, s))
            st += [(a, s + c) for c, a in x.anak.items()]
        return [s for _, s in sorted(hasil, reverse=True)[:k]]

t = Trie()
for kata, skor in [("kopi susu", 950), ("kopi gula aren", 870), ("kopi hitam", 400), ("kopiah", 120), ("kolak", 300)]:
    t.tambah(kata, skor)
print("ko   ->", t.saran("ko")); print("kopi ->", t.saran("kopi")); print("teh  ->", t.saran("teh"))
''')]),

'Hashing & collision': dict(
  ist=[('Hash function', 'Fungsi yang memetakan kunci ke angka (indeks bucket).'),
       ('Collision', 'Dua kunci berbeda menghasilkan indeks bucket sama.'),
       ('Chaining / open addressing', 'Dua cara menangani collision: list per bucket, atau mencari slot kosong lain (dipakai dict CPython).'),
       ('Load factor', 'Rasio elemen terhadap jumlah bucket; jika terlalu tinggi, tabel diperbesar (rehash).')],
  cx=[P('Hash table dengan chaining dan pengukuran collision', '''
def hash_djb2(s):
    h = 5381
    for c in s: h = (h * 33 + ord(c)) & 0xFFFFFFFF
    return h

def hash_jelek(s): return len(s)            # banyak kunci panjangnya sama

def uji(fungsi, bucket=16):
    kunci = [f"SKU-{i:04d}" for i in range(48)]
    tabel = [[] for _ in range(bucket)]
    for k in kunci: tabel[fungsi(k) % bucket].append(k)
    isi = [len(b) for b in tabel]
    return max(isi), sum(1 for x in isi if x == 0), len(kunci) / bucket

for nama, f in [("djb2", hash_djb2), ("panjang string", hash_jelek)]:
    terpanjang, kosong, lf = uji(f)
    print(f"{nama:<15} rantai terpanjang {terpanjang:>2}, bucket kosong {kosong:>2}, load factor {lf:.1f}")
''', 'Fungsi hash yang buruk menumpuk semua kunci di satu bucket, membuat pencarian turun dari O(1) menjadi O(n).')]),

'Heap & priority queue': dict(
  ist=[('Binary heap', 'Pohon lengkap yang disimpan dalam array; induk selalu <= anak (min-heap).'),
       ('Priority queue', 'Antrean yang selalu mengeluarkan elemen berprioritas tertinggi lebih dulu.'),
       ('heapq', 'Modul min-heap Python; push dan pop O(log n).'),
       ('Tie-breaker', 'Elemen kedua di tuple (misalnya nomor urut) agar prioritas seri tetap FIFO dan tidak membandingkan objek.')],
  cx=[P('Triase IGD dengan priority queue', '''
import heapq, itertools
urut = itertools.count()
antre = []
def datang(nama, triase):            # 1 = merah (gawat), 3 = hijau
    heapq.heappush(antre, (triase, next(urut), nama))

for n, t in [("Pak Ali", 3), ("Bu Sri", 2), ("Andi", 1), ("Nina", 3), ("Pak Joko", 1)]: datang(n, t)
WARNA = {1: "MERAH", 2: "KUNING", 3: "HIJAU"}
while antre:
    t, no, n = heapq.heappop(antre)
    print(f"tangani {n:<9} {WARNA[t]:<6} (datang ke-{no + 1})")
''', 'Pasien dengan triase sama dilayani sesuai urutan datang berkat nomor urut sebagai tie-breaker.')]),

'deque, heapq & bisect: struktur data siap pakai': dict(
  ist=[('deque', 'Antrean dua ujung dengan append/pop O(1) di kedua sisi.'),
       ('heapq.nlargest / merge', 'Top-k dan penggabungan beberapa sumber terurut.'),
       ('bisect / insort', 'Pencarian dan penyisipan pada list terurut.'),
       ('Sliding window', 'Jendela data bergerak; deque(maxlen) untuk rata-rata bergerak.')],
  cx=[P('Rata-rata bergerak, merge log, dan tarif berjenjang', '''
from collections import deque
import heapq, bisect

jendela, harga = deque(maxlen=3), [100, 102, 101, 105, 110, 108, 115]
print("MA-3:", [round(sum(jendela) / len(jendela), 1) for p in harga if not jendela.append(p) and len(jendela) == 3])

server_a = [("09:00:01", "A login"), ("09:00:07", "A bayar")]
server_b = [("09:00:03", "B login"), ("09:00:05", "B cari")]
print("log gabungan:", [m for _, m in heapq.merge(server_a, server_b)])

BATAS, TARIF = [0, 60_000_000, 250_000_000, 500_000_000], [0.05, 0.15, 0.25, 0.30]
def tarif_pph(penghasilan): return TARIF[bisect.bisect_right(BATAS, penghasilan) - 1]
print("lapisan tarif:", [f"{tarif_pph(p):.0%}" for p in (50e6, 60e6, 300e6, 1e9)])
''', 'Lapisan tarif mengikuti PPh 21 orang pribadi (UU HPP) untuk contoh saja. Pajak sebenarnya dihitung progresif per lapisan.')]),

'Anotasi tipe & modul typing': dict(
  ist=[('Type hint', 'Anotasi tipe pada parameter, return, dan variabel; tidak diperiksa saat runtime.'),
       ('Union / Optional', 'int | None (3.10+) untuk nilai yang boleh kosong.'),
       ('TypedDict', 'Mendeskripsikan bentuk dict, misalnya payload JSON dari API.'),
       ('Generic', 'Tipe dengan parameter, misalnya list[int] atau kelas Box[T] (sintaks class Box[T] di 3.12+).')],
  cx=[P('Anotasi untuk payload API dan fungsi generik', '''
from typing import TypedDict, Literal, NotRequired, get_type_hints

class Pesanan(TypedDict):
    id: int
    status: Literal["baru", "dibayar", "dikirim"]
    total: int
    catatan: NotRequired[str]

def pertama[T](data: list[T]) -> T | None:
    return data[0] if data else None

def ringkas(p: Pesanan) -> str:
    return f"#{p['id']} {p['status']} Rp{p['total']:,}".replace(",", ".")

p: Pesanan = {"id": 7, "status": "dibayar", "total": 250_000}
print(ringkas(p), "|", pertama([3, 1, 2]), "|", pertama([]))
print("anotasi ringkas:", get_type_hints(ringkas))
print("runtime tidak memeriksa:", ringkas({"id": "x", "status": "?", "total": 1}))
''', 'Baris terakhir membuktikan Python tidak menolak tipe salah saat runtime. Pemeriksaan dilakukan oleh mypy atau pyright sebelum kode dijalankan.')]),

'Pemeriksa tipe: mypy, pyright, pyrefly': dict(
  ist=[('Static type checker', 'Alat yang menganalisis kode tanpa menjalankannya untuk menemukan kesalahan tipe.'),
       ('Gradual typing', 'Anotasi bisa ditambahkan bertahap; kode tanpa anotasi dianggap Any.'),
       ('strict mode', 'Mode ketat yang mewajibkan anotasi dan melarang Any implisit.'),
       ('CI gate', 'Pemeriksaan tipe dijalankan di pipeline; pull request gagal jika ada error tipe.')],
  cx=[T('Bug yang ditangkap mypy sebelum produksi', '''
# toko.py
def diskon(total: int, persen: float) -> int:
    return round(total * persen / 100)

def cari_member(kode: str) -> dict | None:
    return None if kode == "" else {"kode": kode, "poin": 120}

harga = diskon("250000", 10)              # (1) str, bukan int
m = cari_member("M01")
print(m["poin"])                          # (2) m bisa None

$ mypy --strict toko.py
toko.py:8: error: Argument 1 to "diskon" has incompatible type "str"; expected "int"  [arg-type]
toko.py:10: error: Value of type "dict[Any, Any] | None" is not indexable  [index]
Found 2 errors in 1 file (checked 1 source file)

# perbaikan (2): narrowing
if m is not None:
    print(m["poin"])'''),
     T('Konfigurasi di pyproject.toml dan CI', '''
[tool.mypy]
python_version = "3.12"
strict = true
exclude = ["migrations/"]

[tool.pyright]
typeCheckingMode = "strict"

# .github/workflows/ci.yml (potongan)
- run: pip install mypy
- run: mypy src/
# Alternatif: pyright (Microsoft, dipakai Pylance di VS Code), pyrefly (Meta, berbasis Rust), ty (Astral).''', lang='text')]),

'Validasi data dengan Pydantic': dict(
  ist=[('Runtime validation', 'Memeriksa data saat program berjalan, misalnya body request API.'),
       ('BaseModel', 'Kelas Pydantic yang memvalidasi dan mengonversi field sesuai anotasi tipe.'),
       ('Coercion', 'Konversi otomatis yang wajar, misalnya "42" menjadi 42; strict mode mematikannya.'),
       ('ValidationError', 'Error berisi daftar field yang salah beserta alasannya; cocok dikirim sebagai respons 422.')],
  cx=[P('Validasi pendaftaran pengguna dengan Pydantic v2', '''
from pydantic import BaseModel, Field, field_validator, ValidationError
from datetime import date

class Daftar(BaseModel):
    nama: str = Field(min_length=2, max_length=60)
    email: str = Field(pattern=r"^[\\w.+-]+@[\\w-]+\\.[\\w.]+$")
    hp: str
    lahir: date
    @field_validator("hp")
    @classmethod
    def hp_indonesia(cls, v: str) -> str:
        d = "".join(c for c in v if c.isdigit())
        if d.startswith("0"): d = "62" + d[1:]
        if not (d.startswith("628") and 10 <= len(d) <= 15): raise ValueError("nomor HP Indonesia tidak valid")
        return d

ok = Daftar(nama="Sari Dewi", email="sari@contoh.id", hp="0812-3456-7890", lahir="2001-04-17")
print(ok.model_dump())
try:
    Daftar(nama="S", email="bukan-email", hp="12345", lahir="2001-13-40")
except ValidationError as e:
    for err in e.errors(): print(f"  {err['loc'][0]:<6} {err['msg']}")
''', 'FastAPI memakai Pydantic di balik layar. Model yang sama menjadi validasi request sekaligus dokumentasi OpenAPI.')]),

'Formatter & linter: black, ruff, yapf': dict(
  ist=[('Formatter', 'Alat yang menulis ulang tata letak kode secara otomatis (black, ruff format).'),
       ('Linter', 'Alat yang menemukan bug dan pelanggaran gaya tanpa menjalankan kode (ruff, flake8, pylint).'),
       ('pre-commit hook', 'Pemeriksaan otomatis sebelum commit agar kode berantakan tidak masuk repositori.'),
       ('Rule code', 'Kode aturan linter seperti F401 (import tidak dipakai) atau B006 (default mutable).')],
  cx=[T('Sebelum dan sesudah ruff', '''
# sebelum
import os,sys
def hitung( data , kali=[] ):
  hasil=[ x*2 for x in data if x!=None ]
  return hasil

$ ruff check .
app.py:1:8:  F401 [*] `os` imported but unused
app.py:1:11: F401 [*] `sys` imported but unused
app.py:2:28: B006 Do not use mutable data structures for argument defaults
app.py:3:38: E711 Comparison to `None` should be `cond is not None`
$ ruff check --fix . && ruff format .

# sesudah
def hitung(data, kali=None):
    hasil = [x * 2 for x in data if x is not None]
    return hasil'''),
     T('Konfigurasi tim di pyproject.toml dan pre-commit', '''
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "S"]   # pycodestyle, pyflakes, isort, bugbear, pyupgrade, bandit
ignore = ["E501"]

# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format''')]),

'Docstring, komentar & Sphinx': dict(
  ist=[('Docstring convention', 'Format docstring yang disepakati: Google style, NumPy style, atau reStructuredText.'),
       ('Why, not what', 'Komentar menjelaskan alasan keputusan, bukan mengulang apa yang sudah jelas dari kode.'),
       ('Sphinx / MkDocs', 'Generator situs dokumentasi dari docstring dan berkas Markdown/reST.'),
       ('Executable docs', 'Contoh di docstring yang bisa diuji dengan doctest agar dokumentasi tidak basi.')],
  cx=[P('Docstring gaya Google yang bisa dibaca help() dan diuji', '''
import inspect, doctest

def angsuran(pokok: int, bunga_tahunan: float, bulan: int) -> int:
    """Hitung angsuran bulanan dengan metode anuitas.

    Args:
        pokok: Jumlah pinjaman dalam rupiah.
        bunga_tahunan: Suku bunga per tahun, misalnya 0.12 untuk 12%.
        bulan: Tenor dalam bulan.

    Returns:
        Angsuran per bulan, dibulatkan ke rupiah terdekat.

    Example:
        >>> angsuran(12_000_000, 0.12, 12)
        1066185
    """
    r = bunga_tahunan / 12   # bank menghitung bunga bulanan dari bunga tahunan / 12
    return round(pokok * r / (1 - (1 + r) ** -bulan))

print(inspect.getdoc(angsuran).splitlines()[0])
runner = doctest.DocTestRunner()
for t in doctest.DocTestFinder().find(angsuran, "angsuran", globs={"angsuran": angsuran}): runner.run(t)
print("doctest:", runner.summarize(verbose=False))
''')]),

'Testing dengan pytest': dict(
  ist=[('pytest', 'Framework testing paling populer di Python: cukup fungsi test_ dan assert biasa.'),
       ('Fixture', 'Data atau sumber daya yang disiapkan untuk test, didefinisikan dengan @pytest.fixture.'),
       ('Parametrize', 'Menjalankan satu test dengan banyak kombinasi input lewat @pytest.mark.parametrize.'),
       ('Coverage', 'Persentase kode yang dijalankan test (pytest-cov); target umum 80% untuk logika bisnis.')],
  cx=[T('Test pytest dengan fixture dan parametrize', '''
# tests/test_keranjang.py
import pytest
from toko.keranjang import Keranjang, StokHabis

@pytest.fixture
def keranjang():
    return Keranjang(stok={"KOPI": 5, "TEH": 0})

@pytest.mark.parametrize("subtotal, ongkir", [(99_999, 15_000), (100_000, 0), (0, 0)])
def test_ongkir(subtotal, ongkir):
    assert Keranjang.ongkir(subtotal) == ongkir

def test_tambah_mengurangi_stok(keranjang):
    keranjang.tambah("KOPI", 2)
    assert keranjang.stok["KOPI"] == 3

def test_stok_habis_ditolak(keranjang):
    with pytest.raises(StokHabis, match="TEH"):
        keranjang.tambah("TEH", 1)

$ pytest -q --cov=toko
......                                                         [100%]
6 passed in 0.08s
Name                  Stmts   Miss  Cover
toko/keranjang.py        24      2    92%''', lang='python'),
     P('Pola yang sama dijalankan tanpa pytest (assert biasa)', '''
class StokHabis(Exception): pass
class Keranjang:
    def __init__(self, stok): self.stok = dict(stok)
    @staticmethod
    def ongkir(subtotal): return 0 if subtotal == 0 or subtotal >= 100_000 else 15_000
    def tambah(self, sku, n):
        if self.stok.get(sku, 0) < n: raise StokHabis(sku)
        self.stok[sku] -= n

hasil = []
for sub, harap in [(99_999, 15_000), (100_000, 0), (0, 0)]:      # "parametrize"
    hasil.append(("test_ongkir", sub, Keranjang.ongkir(sub) == harap))
k = Keranjang({"KOPI": 5, "TEH": 0}); k.tambah("KOPI", 2)
hasil.append(("test_tambah_mengurangi_stok", "", k.stok["KOPI"] == 3))
try: Keranjang({"TEH": 0}).tambah("TEH", 1); ok = False
except StokHabis as e: ok = "TEH" in str(e)
hasil.append(("test_stok_habis_ditolak", "", ok))
for nama, param, lulus in hasil: print(f"{'PASSED' if lulus else 'FAILED'} {nama} {param}")
print(f"{sum(h[2] for h in hasil)} passed")
''')]),

'unittest, doctest & tox': dict(
  ist=[('unittest', 'Framework testing bawaan berbasis kelas TestCase; dipakai Django dan proyek lama.'),
       ('setUp / tearDown', 'Method yang dijalankan sebelum dan sesudah setiap test.'),
       ('Mock', 'unittest.mock mengganti dependensi (API, email, waktu) dengan objek palsu yang bisa diperiksa.'),
       ('tox / nox', 'Menjalankan test di banyak versi Python dan lingkungan secara otomatis.')],
  cx=[P('unittest dengan mock untuk layanan email', '''
import unittest, io
from unittest.mock import Mock

class LayananPesanan:
    def __init__(self, email): self.email = email
    def checkout(self, user, total):
        if total <= 0: raise ValueError("total tidak valid")
        self.email.kirim(user, f"Pesanan Rp{total} diterima")
        return "OK"

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.email = Mock(); self.svc = LayananPesanan(self.email)
    def test_kirim_email_sekali(self):
        self.assertEqual(self.svc.checkout("sari@x.id", 5000), "OK")
        self.email.kirim.assert_called_once_with("sari@x.id", "Pesanan Rp5000 diterima")
    def test_total_nol_tidak_kirim_email(self):
        with self.assertRaises(ValueError): self.svc.checkout("sari@x.id", 0)
        self.email.kirim.assert_not_called()

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCheckout)
nama = [t.id().split(".")[-1] for t in suite]
hasil = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
gagal = {t.id().split(".")[-1] for t, _ in hasil.failures + hasil.errors}
for n in nama: print(("GAGAL " if n in gagal else "LULUS ") + n)
print(f"{hasil.testsRun} test, {len(gagal)} gagal")
'''),
     T('tox.ini: satu perintah, banyak versi Python', '''
[tox]
envlist = py311, py312, py313, lint

[testenv]
deps = pytest
commands = pytest -q

[testenv:lint]
deps = ruff
commands = ruff check .

$ tox
  py311: OK   py312: OK   py313: OK   lint: OK''')]),

'Threading & GIL': dict(
  ist=[('Thread', 'Alur eksekusi di dalam satu proses yang berbagi memori.'),
       ('GIL', 'Global Interpreter Lock: di CPython hanya satu thread menjalankan bytecode Python pada satu waktu.'),
       ('I/O-bound vs CPU-bound', 'Thread mempercepat tugas yang banyak menunggu (jaringan, disk), bukan tugas hitung berat.'),
       ('Free-threaded Python', 'Build CPython 3.13+ tanpa GIL (python3.13t), masih eksperimental.')],
  cx=[P('Thread untuk tugas I/O dan race condition yang dicegah lock', '''
import threading, time
from concurrent.futures import ThreadPoolExecutor

def unduh(url):
    time.sleep(0.2)                         # pura-pura menunggu jaringan
    return f"{url} selesai"
urls = [f"https://api.contoh.id/produk/{i}" for i in range(8)]
t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=8) as ex: hasil = list(ex.map(unduh, urls))
durasi = time.perf_counter() - t0
print(len(hasil), "unduhan;", "paralel (jauh < 1,6 detik):", durasi < 0.8)

saldo, kunci = 0, threading.Lock()
def setor_banyak():
    global saldo
    for _ in range(100_000):
        with kunci: saldo += 1              # tanpa lock, hasil bisa kurang dari 400.000
ts = [threading.Thread(target=setor_banyak) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
print("saldo akhir:", saldo)
''', '8 unduhan yang masing-masing menunggu 0,2 detik selesai sekitar 0,2 detik karena saat menunggu jaringan, GIL dilepas.')]),

'Multiprocessing': dict(
  ist=[('Process', 'Program terpisah dengan memori sendiri; setiap proses punya interpreter dan GIL sendiri.'),
       ('ProcessPoolExecutor', 'Kumpulan proses pekerja untuk membagi tugas CPU-bound ke beberapa inti CPU.'),
       ('Pickling', 'Data dan fungsi dikirim antarproses dengan diserialisasi; fungsi harus didefinisikan di tingkat modul.'),
       ('Overhead', 'Membuat proses dan mengirim data itu mahal; hanya layak untuk tugas yang cukup berat.')],
  cx=[T('Pola standar memproses gambar di banyak inti CPU', '''
# resize_massal.py
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from PIL import Image

def kecilkan(path: Path) -> str:
    with Image.open(path) as im:
        im.thumbnail((800, 800))
        im.save(path.with_name(path.stem + "_800.jpg"), quality=85)
    return path.name

if __name__ == "__main__":                       # wajib: proses anak mengimpor ulang modul ini
    files = list(Path("foto").glob("*.jpg"))
    with ProcessPoolExecutor() as ex:            # default: jumlah inti CPU
        for nama in ex.map(kecilkan, files, chunksize=8):
            print("selesai", nama)''', lang='python'),
     P('CPU-bound di beberapa proses (fungsi bawaan agar bisa di-pickle)', '''
import math, os
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
angka = [20_000, 21_000, 22_000, 23_000]
with ProcessPoolExecutor(max_workers=2, mp_context=mp.get_context("fork")) as ex:
    hasil = list(ex.map(math.factorial, angka))
for n, f in zip(angka, hasil):
    print(f"{n:,}! punya {int(math.log10(f)) + 1:,} digit".replace(",", "."))
print("inti CPU tersedia > 0:", (os.cpu_count() or 0) > 0)
''', 'Di halaman ini dipakai math.factorial karena fungsi yang dibuat di sel kode tidak bisa dikirim ke proses lain. Di berkas .py, fungsi tingkat modul bisa dipakai.')]),

'asyncio, async/await & gevent': dict(
  ist=[('Coroutine', 'Fungsi async def yang bisa berhenti sementara di await tanpa memblokir program.'),
       ('Event loop', 'Penjadwal yang menjalankan banyak coroutine bergantian dalam satu thread.'),
       ('asyncio.gather / TaskGroup', 'Menjalankan banyak coroutine bersamaan; TaskGroup (3.11+) membatalkan semua jika satu gagal.'),
       ('Semaphore / rate limit', 'Membatasi jumlah permintaan bersamaan agar tidak membebani API pihak lain.')],
  cx=[P('Memanggil 10 API bersamaan dengan batas 3 koneksi', '''
import asyncio, time

async def cek_ongkir(kurir, sem, log):
    async with sem:
        log.append(("mulai", kurir))
        await asyncio.sleep(0.1)                 # pura-pura menunggu HTTP
        return kurir, 9_000 + len(kurir) * 1_000

async def main():
    sem, log = asyncio.Semaphore(3), []
    kurir = ["JNE", "J&T", "SiCepat", "AnterAja", "POS", "Ninja", "Lion", "IDE", "SAP", "Wahana"]
    t0 = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        tugas = [tg.create_task(cek_ongkir(k, sem, log)) for k in kurir]
    durasi = time.perf_counter() - t0
    termurah = min((t.result() for t in tugas), key=lambda x: x[1])
    print("termurah:", termurah)
    print("10 panggilan, maks 3 bersamaan -> sekitar 4 gelombang:", 0.35 < durasi < 0.8)

asyncio.run(main())
''', 'Tanpa semaphore, 10 permintaan dikirim sekaligus dan API pihak ketiga bisa membalas 429 Too Many Requests.')]),

'Peta framework web Python': dict(
  ist=[('WSGI / ASGI', 'Antarmuka standar server dan aplikasi web Python: WSGI sinkron (Flask, Django), ASGI asinkron (FastAPI, Starlette).'),
       ('Full-stack vs micro framework', 'Django lengkap (ORM, admin, auth) vs Flask/FastAPI yang ringan dan dirakit sendiri.'),
       ('OpenAPI', 'Spesifikasi dokumentasi API; FastAPI membuatnya otomatis dari anotasi tipe.'),
       ('Application server', 'Gunicorn (WSGI) dan Uvicorn (ASGI) menjalankan aplikasi di produksi di belakang Nginx.')],
  cx=[T('Memilih framework untuk kebutuhan 2026', '''
Kebutuhan                                    Pilihan umum
Aplikasi bisnis lengkap + admin + ORM        Django (+ Django REST Framework / Django Ninja)
REST API modern, async, dokumentasi otomatis FastAPI (+ SQLAlchemy/SQLModel, Pydantic)
API/prototipe kecil, banyak tutorial         Flask
Dashboard data internal                      Streamlit, Dash, Reflex
Layanan real-time (WebSocket)                FastAPI/Starlette, Django Channels
Arsitektur produksi tipikal
  Nginx -> Gunicorn (WSGI) -> Django         atau   Nginx -> Uvicorn (ASGI) -> FastAPI''')]),

'Membuat REST API: Flask & FastAPI': dict(
  ist=[('REST resource', 'Data diekspos sebagai URL (/produk/7) dengan metode HTTP GET, POST, PUT, DELETE.'),
       ('Status code', '200 OK, 201 Created, 400/422 input salah, 404 tidak ada, 500 error server.'),
       ('Request validation', 'Body request divalidasi sebelum diproses; FastAPI memakai Pydantic.'),
       ('Idempotency', 'GET, PUT, DELETE boleh diulang tanpa efek tambahan; POST tidak.')],
  cx=[T('API produk dengan FastAPI', '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="API Toko")
DB: dict[int, dict] = {}

class ProdukBaru(BaseModel):
    nama: str = Field(min_length=2)
    harga: int = Field(gt=0)

@app.post("/produk", status_code=201)
def buat(p: ProdukBaru):
    pid = len(DB) + 1
    DB[pid] = {"id": pid, **p.model_dump()}
    return DB[pid]

@app.get("/produk/{pid}")
def ambil(pid: int):
    if pid not in DB:
        raise HTTPException(404, "produk tidak ditemukan")
    return DB[pid]

# jalankan: uvicorn main:app --reload   lalu buka http://127.0.0.1:8000/docs''', lang='python'),
     P('Konsep yang sama dengan WSGI murni (tanpa framework), diuji langsung', '''
import json, io
DB = {}
def app(environ, start_response):
    metode, path = environ["REQUEST_METHOD"], environ["PATH_INFO"]
    def kirim(status, body):
        start_response(status, [("Content-Type", "application/json")]); return [json.dumps(body).encode()]
    if metode == "POST" and path == "/produk":
        data = json.loads(environ["wsgi.input"].read() or b"{}")
        if not data.get("nama") or data.get("harga", 0) <= 0: return kirim("422 Unprocessable Entity", {"error": "nama/harga tidak valid"})
        pid = len(DB) + 1; DB[pid] = {"id": pid, **data}; return kirim("201 Created", DB[pid])
    if metode == "GET" and path.startswith("/produk/"):
        pid = int(path.rsplit("/", 1)[1])
        return kirim("200 OK", DB[pid]) if pid in DB else kirim("404 Not Found", {"error": "tidak ada"})
    return kirim("404 Not Found", {"error": "rute tidak ada"})

def panggil(metode, path, body=None):
    raw = json.dumps(body).encode() if body else b""
    status = []
    out = app({"REQUEST_METHOD": metode, "PATH_INFO": path, "wsgi.input": io.BytesIO(raw)}, lambda s, h: status.append(s))
    print(f"{metode:<4} {path:<10} -> {status[0]:<26} {out[0].decode()}")

panggil("POST", "/produk", {"nama": "Kopi Gayo", "harga": 85000})
panggil("POST", "/produk", {"nama": "", "harga": -1})
panggil("GET", "/produk/1"); panggil("GET", "/produk/9")
''', 'Flask dan Django adalah aplikasi WSGI seperti ini, dengan routing, validasi, dan keamanan yang sudah disiapkan.')]),

'Django: aplikasi web lengkap': dict(
  ist=[('MTV', 'Model-Template-View: pola Django (setara MVC).'),
       ('ORM', 'Object-Relational Mapper: tabel database diakses sebagai kelas Python.'),
       ('Migration', 'Berkas perubahan skema yang dibuat makemigrations dan diterapkan migrate.'),
       ('Django admin', 'Panel admin otomatis dari model; sangat mempercepat aplikasi internal.')],
  cx=[T('Potongan inti aplikasi Django', '''
# katalog/models.py
from django.db import models
class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.PositiveIntegerField()
    aktif = models.BooleanField(default=True)
    dibuat = models.DateTimeField(auto_now_add=True)

# katalog/admin.py
from django.contrib import admin
admin.site.register(Produk)

# katalog/views.py
from django.shortcuts import render
def daftar(request):
    produk = Produk.objects.filter(aktif=True).order_by("-dibuat")[:20]
    return render(request, "katalog/daftar.html", {"produk": produk})

# urls.py
urlpatterns = [path("produk/", daftar, name="daftar-produk")]

$ python manage.py makemigrations && python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver      # admin di http://127.0.0.1:8000/admin/''', lang='python')]),

'Format specifier: merapikan keluaran': dict(
  ist=[('Format spec mini-language', 'Sintaks setelah titik dua di f-string: [isi][rata][lebar][,][.presisi][tipe].'),
       ('Alignment', '< kiri, > kanan, ^ tengah; angka sebaiknya rata kanan.'),
       ('Thousands separator', ', atau _ sebagai pemisah ribuan; lokal Indonesia memakai titik.'),
       ('Percent / scientific', ':.1% untuk persen, :.2e untuk notasi ilmiah.')],
  cx=[P('Struk belanja yang rapi', '''
item = [("Kopi Gayo 250g", 2, 85_000), ("Gula aren cair", 1, 32_500), ("Susu oat 1L", 3, 29_900)]
LEBAR = 38
print(f"{'TOKO KOPI NUSANTARA':^{LEBAR}}")
print("=" * LEBAR)
sub = 0
for nama, q, h in item:
    sub += q * h
    print(f"{nama:<16}{q:>2} x{h:>8,}{q * h:>10,}".replace(",", "."))
ppn = round(sub * 0.11)
print("-" * LEBAR)
for label, v in [("Subtotal", sub), ("PPN 11%", ppn), ("TOTAL", sub + ppn)]:
    print(f"{label:<24}{'Rp':>2}{v:>12,}".replace(",", "."))
print(f"{'hemat member':<24}{0.075:>14.1%}")
print(f"{'kode':<8}{42:>06}  {255:#x}  {1_250_000:.2e}")
''')]),

'Kapan for, kapan while, kapan do-while': dict(
  ist=[('Iterating a collection', 'Gunakan for saat menelusuri elemen yang sudah ada.'),
       ('Condition-driven loop', 'Gunakan while saat berhenti bergantung kondisi yang berubah, bukan jumlah elemen.'),
       ('At-least-once loop', 'Gunakan pola do-while (while True + break) saat badan loop harus jalan minimal sekali.'),
       ('Polling', 'Memeriksa status berulang sampai siap, misalnya status pembayaran; selalu beri batas waktu.')],
  cx=[P('Tiga situasi nyata, tiga jenis loop', '''
import random
rng = random.Random(4)

keranjang = [("kopi", 2), ("teh", 1), ("gula", 3)]
for nama, q in keranjang:                       # for: elemen sudah diketahui
    print(f"for   : proses {q} {nama}")

status, cek = "PENDING", 0                      # while: berhenti saat kondisi berubah
while status == "PENDING" and cek < 10:
    cek += 1
    status = rng.choice(["PENDING", "PENDING", "PAID"])
print(f"while : status {status} setelah {cek} kali cek")

masukan = iter(["2", "1", "0"])                 # pilihan pengguna (disimulasikan)
while True:                                     # do-while: tampilkan menu minimal sekali
    pilihan = next(masukan)
    print(f"do    : menu ditampilkan, pengguna memilih {pilihan}")
    if pilihan == "0": break
''')]),

'Bilangan Fibonacci: for dan while': dict(
  ist=[('Iterative Fibonacci', 'Menyimpan dua nilai terakhir; O(n) waktu dan O(1) memori.'),
       ('Golden ratio', 'Rasio dua bilangan Fibonacci berurutan mendekati 1,618.'),
       ('Arbitrary precision', 'int Python tidak terbatas ukurannya, sehingga fib(1000) tetap tepat.'),
       ('Fibonacci retracement', 'Level 23,6%, 38,2%, 61,8% yang dipakai analisis teknikal trader.')],
  cx=[P('Fibonacci dengan for, while, rasio emas, dan bilangan besar', '''
def fib_for(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a

def fib_kurang_dari(batas):
    a, b, hasil = 0, 1, []
    while a < batas: hasil.append(a); a, b = b, a + b
    return hasil

print("10 pertama   :", [fib_for(i) for i in range(10)])
print("di bawah 100 :", fib_kurang_dari(100))
print("rasio F31/F30:", fib_for(31) / fib_for(30))
print("F(300) punya", len(str(fib_for(300))), "digit, tetap tepat")
''')]),

'Bubble sort: loop di dalam loop': dict(
  ist=[('Bubble sort', 'Menukar pasangan bersebelahan yang salah urut berulang kali: O(n²).'),
       ('Early termination', 'Berhenti jika satu putaran penuh tidak ada pertukaran; kasus terbaik menjadi O(n).'),
       ('Adaptive algorithm', 'Algoritma yang lebih cepat pada data yang hampir terurut.'),
       ('Pass', 'Satu putaran penuh di loop luar; setelah putaran ke-k, k elemen terbesar sudah di posisinya.')],
  cx=[P('Bubble sort dengan early exit pada data acak vs hampir terurut', '''
import random
def bubble(a):
    a = list(a); putaran = banding = 0
    for i in range(len(a) - 1):
        tukar = False; putaran += 1
        for j in range(len(a) - 1 - i):
            banding += 1
            if a[j] > a[j + 1]: a[j], a[j + 1] = a[j + 1], a[j]; tukar = True
        if not tukar: break
    return a, putaran, banding

acak = random.Random(7).sample(range(500), 200)
hampir = sorted(acak); hampir[50], hampir[51] = hampir[51], hampir[50]
for nama, d in [("acak", acak), ("hampir terurut", hampir)]:
    hasil, p, b = bubble(d)
    bb = f"{b:,}".replace(",", ".")
    print(f"{nama:<15} putaran {p:>3}, perbandingan {bb:>6}, benar {hasil == sorted(d)}")
''')]),

'FizzBuzz dan bilangan prima: break dan loop bersarang': dict(
  ist=[('FizzBuzz', 'Soal saringan wawancara klasik untuk menguji percabangan dan modulo.'),
       ('Trial division sampai √n', 'Cukup memeriksa pembagi sampai akar n; pembagi lebih besar punya pasangan lebih kecil.'),
       ('Sieve of Eratosthenes', 'Mencoret kelipatan untuk mendapat semua prima sampai n dalam O(n log log n).'),
       ('Rule table', 'FizzBuzz yang bisa diperluas dengan daftar aturan, bukan if bertumpuk.')],
  cx=[P('FizzBuzz berbasis aturan dan saringan prima', '''
ATURAN = [(3, "Fizz"), (5, "Buzz"), (7, "Bazz")]
def fizz(n): return "".join(k for d, k in ATURAN if n % d == 0) or str(n)
print(" ".join(fizz(i) for i in range(1, 22)))

def prima_bagi(n):
    if n < 2: return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0: return False          # break lebih awal begitu ada pembagi
    return True

def saringan(n):
    tanda = [True] * (n + 1); tanda[0] = tanda[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if tanda[i]: tanda[i * i::i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, p in enumerate(tanda) if p]

print("prima < 50:", saringan(50))
print("kedua cara sama sampai 10.000:", saringan(10_000) == [i for i in range(10_001) if prima_bagi(i)])
print("jumlah prima < 1 juta:", len(saringan(1_000_000)))
''')]),

'Faktorial, jumlah digit, dan palindrom': dict(
  ist=[('Digit extraction', 'Mengambil digit dengan % 10 dan // 10, atau lewat str(n).'),
       ('Checksum', 'Angka pemeriksa dari digit-digit data, misalnya algoritma Luhn pada nomor kartu.'),
       ('Palindrome', 'Teks atau angka yang sama dibaca dari depan dan belakang.'),
       ('Normalization', 'Membuang spasi, tanda baca, dan huruf besar sebelum memeriksa palindrom.')],
  cx=[P('Checksum Luhn, palindrom kalimat, dan digit faktorial', '''
import math
def luhn_valid(nomor):
    digit = [int(c) for c in nomor if c.isdigit()][::-1]
    total = 0
    for i, d in enumerate(digit):
        if i % 2 == 1:
            d *= 2
            if d > 9: d -= 9
        total += d
    return total % 10 == 0
for kartu in ["4111 1111 1111 1111", "4111 1111 1111 1112"]:
    print(kartu, "valid" if luhn_valid(kartu) else "TIDAK valid")

def palindrom(s):
    bersih = [c.lower() for c in s if c.isalnum()]
    return bersih == bersih[::-1]
print([palindrom(s) for s in ["Kasur ini rusak", "Ada apa", "12321", "Malam"]])

def jumlah_digit(n):
    t = 0
    while n: t, n = t + n % 10, n // 10
    return t
print("jumlah digit 100! =", jumlah_digit(math.factorial(100)), "| 100! punya", len(str(math.factorial(100))), "digit")
''', 'Algoritma Luhn dipakai untuk menolak salah ketik nomor kartu sebelum dikirim ke payment gateway.')]),
}
