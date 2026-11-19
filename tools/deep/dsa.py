"""Pendalaman jalur Struktur Data & Algoritma: istilah wawancara/industri dan contoh Python yang dijalankan."""
K = 'dsa'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Algoritma, struktur data, dan kenapa penting': dict(
  ist=[('Algorithm', 'Langkah-langkah terbatas dan jelas untuk menyelesaikan masalah.'),
       ('Data structure', 'Cara menyusun data di memori agar operasi tertentu cepat.'),
       ('Trade-off', 'Tidak ada struktur yang terbaik untuk semua hal; cepat mencari sering berarti lambat menyisip atau boros memori.'),
       ('Technical interview', 'Wawancara coding (live coding, LeetCode-style) di perusahaan teknologi yang menguji DSA.')],
  cx=[P('Struktur data yang tepat mengubah 1 juta operasi menjadi seketika', '''
import time, random
random.seed(1)
pelanggan = [f"C{i:06d}" for i in range(200_000)]
transaksi = random.choices(pelanggan, k=2_000) + ["C999999"]

t0 = time.perf_counter(); cocok_list = sum(1 for t in transaksi if t in pelanggan); t_list = time.perf_counter() - t0
indeks = set(pelanggan)
t0 = time.perf_counter(); cocok_set = sum(1 for t in transaksi if t in indeks); t_set = time.perf_counter() - t0
print("hasil sama:", cocok_list == cocok_set, "| cocok:", cocok_set, "dari", len(transaksi))
print("set lebih cepat lebih dari 100x:", t_list > 100 * t_set)
''', 'Inilah inti DSA: masalahnya sama, datanya sama, tetapi memilih set alih-alih list membuat program ratusan kali lebih cepat.')]),

'Notasi Big-O: O(1), O(n), O(n²), O(log n)': dict(
  ist=[('Asymptotic analysis', 'Menganalisis perilaku algoritma saat n sangat besar, mengabaikan konstanta.'),
       ('O(log n)', 'Waktu bertambah satu langkah setiap n dilipatgandakan; khas binary search dan pohon seimbang.'),
       ('Big-Omega / Big-Theta', 'Batas bawah (Ω) dan batas ketat (Θ); Big-O adalah batas atas.'),
       ('Scalability', 'Kemampuan sistem tetap cepat saat data tumbuh 10x atau 1000x.')],
  cx=[P('Berapa lama jika data tumbuh? Proyeksi dari 1 juta operasi per detik', '''
import math
OPS_PER_DETIK = 1_000_000
def waktu(op):
    d = op / OPS_PER_DETIK
    for satuan, s in [("tahun", 31_536_000), ("hari", 86_400), ("jam", 3_600), ("menit", 60), ("detik", 1)]:
        if d >= s: return f"{d / s:,.1f} {satuan}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "< 1 detik"
print(f"{'n':>12} {'O(log n)':>10} {'O(n)':>12} {'O(n log n)':>12} {'O(n²)':>14}")
for n in [1_000, 1_000_000, 100_000_000]:
    nn = f"{n:,}".replace(",", ".")
    print(f"{nn:>12} {waktu(math.log2(n)):>10} {waktu(n):>12} {waktu(n * math.log2(n)):>12} {waktu(n * n):>14}")
''', 'Untuk 100 juta data, O(n²) butuh ratusan tahun. Itulah sebabnya pemilihan algoritma menentukan apakah sebuah fitur bisa dirilis.')]),

'Kompleksitas waktu dan ruang': dict(
  ist=[('Space complexity', 'Memori tambahan yang dibutuhkan algoritma terhadap n.'),
       ('Time-space trade-off', 'Memakai memori lebih (cache, indeks) untuk mempercepat waktu.'),
       ('In-place algorithm', 'Algoritma yang hanya memakai memori tambahan O(1).'),
       ('Auxiliary space', 'Memori tambahan di luar input itu sendiri.')],
  cx=[P('Deteksi duplikat: tiga pilihan waktu vs memori', '''
import sys
data = list(range(50_000)) + [123]

# pilihan 1 (tidak dijalankan): loop bersarang, O(n²) waktu, O(1) memori -> 1,25 miliar perbandingan

def urut(a):                # pilihan 2: O(n log n) waktu, O(n) memori untuk salinan (O(1) jika boleh mengubah input)
    b = sorted(a)
    return any(b[i] == b[i + 1] for i in range(len(b) - 1))

def pakai_set(a):           # pilihan 3: O(n) waktu, O(n) memori
    lihat = set()
    for x in a:
        if x in lihat: return True
        lihat.add(x)
    return False

print("urut :", urut(data), "| set:", pakai_set(data))
print(f"memori set tambahan ~{sys.getsizeof(set(data)) // 1024:,} KB untuk {len(data):,} elemen".replace(",", "."))
''', 'Di server dengan memori lega, set adalah pilihan biasa. Di perangkat IoT dengan RAM kecil, mengurutkan di tempat bisa lebih tepat.')]),

'Array dan list dinamis': dict(
  ist=[('Contiguous memory', 'Elemen array disimpan berurutan di memori sehingga akses indeks O(1).'),
       ('Dynamic array', 'Array yang membesar otomatis dengan menyalin ke blok baru (list Python, ArrayList Java).'),
       ('Amortized O(1)', 'Biaya rata-rata append tetap konstan walau sesekali ada penyalinan besar.'),
       ('Insert in middle O(n)', 'Menyisip atau menghapus di tengah array menggeser semua elemen sesudahnya.')],
  cx=[P('Biaya sisip di depan vs di belakang', '''
import timeit
for n in [10_000, 40_000]:
    depan = timeit.timeit(lambda: [None] and (l := []) or [l.insert(0, i) for i in range(n)], number=1)
    belakang = timeit.timeit(lambda: [None] and (l := []) or [l.append(i) for i in range(n)], number=1)
    print(f"n={n:>6,}: insert(0) lebih lambat dari append: {depan > 3 * belakang}".replace(",", "."))
from collections import deque
d = deque(); [d.appendleft(i) for i in range(5)]
print("butuh sisip di depan? pakai deque:", list(d))
''')]),

'Two pointers': dict(
  ist=[('Two pointers', 'Dua indeks yang bergerak di array (dari dua ujung atau searah) untuk menghindari loop bersarang.'),
       ('Sorted input', 'Banyak pola two pointers mensyaratkan data terurut.'),
       ('Two Sum (sorted)', 'Soal klasik: cari dua angka berjumlah target dalam O(n).'),
       ('Merge step', 'Menggabungkan dua list terurut dengan dua penunjuk; inti merge sort.')],
  cx=[P('Pasangan produk sesuai budget dan menggabungkan dua jadwal', '''
harga = sorted([12_000, 45_000, 30_000, 8_000, 27_000, 50_000, 15_000])
def pasangan_pas(harga, budget):
    kiri, kanan, hasil = 0, len(harga) - 1, []
    while kiri < kanan:
        s = harga[kiri] + harga[kanan]
        if s == budget: hasil.append((harga[kiri], harga[kanan])); kiri += 1; kanan -= 1
        elif s < budget: kiri += 1
        else: kanan -= 1
    return hasil
print("bundel tepat Rp57.000:", pasangan_pas(harga, 57_000))

def gabung(a, b):
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print("jadwal gabungan:", gabung(["08:00", "10:30", "15:00"], ["09:15", "10:30", "13:00", "17:45"]))
''')]),

'Sliding window dan prefix sum': dict(
  ist=[('Sliding window', 'Jendela yang bergeser di atas data; menghitung ulang hanya bagian yang masuk dan keluar.'),
       ('Prefix sum', 'Array jumlah kumulatif sehingga jumlah rentang [i, j] dihitung O(1).'),
       ('Rate limiter', 'Membatasi jumlah request per jendela waktu; memakai sliding window.'),
       ('Range query', 'Pertanyaan atas rentang data: jumlah, rata-rata, maksimum.')],
  cx=[P('Penjualan 7 hari terbaik dan rate limiter', '''
from itertools import accumulate
from collections import deque
harian = [12, 15, 9, 22, 30, 18, 25, 40, 35, 10, 8, 28, 33, 31]
k = 7
jendela = sum(harian[:k]); terbaik, mulai = jendela, 0
for i in range(k, len(harian)):
    jendela += harian[i] - harian[i - k]
    if jendela > terbaik: terbaik, mulai = jendela, i - k + 1
print(f"7 hari terbaik: hari {mulai + 1}-{mulai + k}, total {terbaik}")

pre = [0] + list(accumulate(harian))
print("jumlah hari 4-10 (prefix sum O(1)):", pre[10] - pre[3])

def limiter(maks, detik):
    log = deque()
    def izinkan(t):
        while log and log[0] <= t - detik: log.popleft()
        if len(log) < maks: log.append(t); return "200"
        return "429"
    return izinkan
izin = limiter(3, 10)
print("request:", [(t, izin(t)) for t in [0, 2, 4, 5, 11, 12, 13, 14]])
''')]),

'Linked list': dict(
  ist=[('Singly / doubly linked', 'Simpul menunjuk ke berikutnya saja, atau juga ke sebelumnya.'),
       ('O(1) insert at known node', 'Menyisip di posisi yang sudah dipegang hanya mengubah penunjuk.'),
       ('Dummy head', 'Simpul palsu di depan untuk menyederhanakan kasus tepi.'),
       ('Use case', 'LRU cache, antrean tugas, undo history, adjacency list graph.')],
  cx=[P('Membalik, menggabungkan, dan menghapus duplikat', '''
class N:
    def __init__(self, v, nx=None): self.v, self.nx = v, nx
def dari(*xs):
    h = None
    for x in reversed(xs): h = N(x, h)
    return h
def ke(h):
    o = []
    while h: o.append(h.v); h = h.nx
    return o

def gabung_urut(a, b):
    dummy = ekor = N(0)
    while a and b:
        if a.v <= b.v: ekor.nx, a = a, a.nx
        else: ekor.nx, b = b, b.nx
        ekor = ekor.nx
    ekor.nx = a or b
    return dummy.nx

def hapus_dup(h):
    cur = h
    while cur and cur.nx:
        if cur.v == cur.nx.v: cur.nx = cur.nx.nx
        else: cur = cur.nx
    return h

g = gabung_urut(dari(1, 3, 3, 7), dari(2, 3, 8))
print("gabung:", ke(g)); print("tanpa duplikat:", ke(hapus_dup(g)))
''')]),

'Stack (LIFO)': dict(
  ist=[('Monotonic stack', 'Stack yang isinya dijaga naik atau turun; menyelesaikan soal "elemen lebih besar berikutnya" dalam O(n).'),
       ('Call stack', 'Stack yang menyimpan pemanggilan fungsi; rekursi memakai stack secara implisit.'),
       ('DFS iterative', 'Penelusuran graph secara mendalam dengan stack eksplisit.'),
       ('Parser', 'Compiler dan validator JSON/HTML memakai stack untuk mencocokkan tanda buka dan tutup.')],
  cx=[P('Monotonic stack: berapa hari sampai harga saham naik', '''
harga = [73, 74, 75, 71, 69, 72, 76, 73]
tunggu = [0] * len(harga)
st = []                                  # indeks hari dengan harga menurun
for i, h in enumerate(harga):
    while st and harga[st[-1]] < h:
        j = st.pop(); tunggu[j] = i - j
    st.append(i)
for h, t in zip(harga, tunggu):
    print(f"harga {h}: {'naik setelah ' + str(t) + ' hari' if t else 'tidak naik lagi'}")
''', 'Solusi naif membandingkan setiap hari dengan semua hari sesudahnya (O(n²)). Monotonic stack cukup sekali jalan.')]),

'Queue (FIFO) dan deque': dict(
  ist=[('Queue', 'Antrean FIFO: enqueue di belakang, dequeue di depan.'),
       ('Deque', 'Double-ended queue: operasi O(1) di kedua ujung.'),
       ('Monotonic deque', 'Deque yang menjaga urutan untuk mencari maksimum jendela geser dalam O(n).'),
       ('Task queue', 'Antrean pekerjaan latar (Celery, RQ, Sidekiq) yang diproses worker.')],
  cx=[P('Suhu maksimum setiap jendela 3 jam (monotonic deque)', '''
from collections import deque
suhu = [27, 29, 31, 30, 28, 33, 32, 26, 25, 29]
k, dq, maks = 3, deque(), []
for i, s in enumerate(suhu):
    while dq and dq[0] <= i - k: dq.popleft()          # keluar dari jendela
    while dq and suhu[dq[-1]] <= s: dq.pop()            # buang yang tidak mungkin jadi maksimum
    dq.append(i)
    if i >= k - 1: maks.append(suhu[dq[0]])
print("maks per 3 jam:", maks)
print("cek naif     :", [max(suhu[i:i + k]) for i in range(len(suhu) - k + 1)])
''')]),

'Cara kerja hash table': dict(
  ist=[('Hash function', 'Mengubah kunci menjadi angka yang menentukan bucket.'),
       ('Collision resolution', 'Chaining (list per bucket) atau open addressing (cari slot lain).'),
       ('Load factor & rehash', 'Jika elemen/bucket melewati ambang (misal 0,75), tabel diperbesar dan semua kunci dihitung ulang.'),
       ('Consistent hashing', 'Teknik membagi kunci ke banyak server sehingga menambah server hanya memindah sedikit kunci (Redis Cluster, Cassandra).')],
  cx=[P('Hash table sederhana dengan rehash otomatis', '''
class HashMap:
    def __init__(self): self.b, self.n, self.rehash = [[] for _ in range(4)], 0, 0
    def _i(self, k):
        h = 0
        for c in str(k): h = (h * 31 + ord(c)) % 2**32
        return h % len(self.b)
    def put(self, k, v):
        bucket = self.b[self._i(k)]
        for p in bucket:
            if p[0] == k: p[1] = v; return
        bucket.append([k, v]); self.n += 1
        if self.n / len(self.b) > 0.75:
            lama = [p for bk in self.b for p in bk]
            self.b = [[] for _ in range(len(self.b) * 2)]; self.n = 0; self.rehash += 1
            for kk, vv in lama: self.put(kk, vv)
    def get(self, k):
        return next((v for kk, v in self.b[self._i(k)] if kk == k), None)

m = HashMap()
for i in range(20): m.put(f"SKU-{i}", i * 1000)
print("SKU-7:", m.get("SKU-7"), "| SKU-99:", m.get("SKU-99"))
print("bucket:", len(m.b), "| rehash terjadi:", m.rehash, "kali | rantai terpanjang:", max(map(len, m.b)))
''')]),

'Pola dict dan set untuk soal nyata': dict(
  ist=[('Frequency map', 'Menghitung kemunculan dengan dict/Counter; dasar banyak soal string dan log.'),
       ('Complement lookup', 'Pola Two Sum: simpan yang sudah dilihat, cari pasangan target - x.'),
       ('Grouping key', 'Kunci kanonik (misal huruf terurut) untuk mengelompokkan anagram atau data mirip.'),
       ('Idempotency key', 'Kunci unik request yang disimpan di set/DB agar pembayaran tidak diproses dua kali.')],
  cx=[P('Two Sum, kelompok anagram, dan pencegahan pembayaran ganda', '''
from collections import defaultdict
def two_sum(nums, target):
    lihat = {}
    for i, x in enumerate(nums):
        if target - x in lihat: return lihat[target - x], i
        lihat[x] = i
print("two sum:", two_sum([25_000, 40_000, 15_000, 60_000], 75_000))

kata = ["kasur", "rusak", "makan", "sukar", "kaman", "raja", "jara"]
kel = defaultdict(list)
for w in kata: kel["".join(sorted(w))].append(w)
print("anagram:", [g for g in kel.values() if len(g) > 1])

diproses = set()
def bayar(idempotency_key, jumlah):
    if idempotency_key in diproses: return "duplikat, diabaikan"
    diproses.add(idempotency_key); return f"debit {jumlah}"
print([bayar(k, 50_000) for k in ["req-81f", "req-81f", "req-9a2"]])
''')]),

'Rekursi': dict(
  ist=[('Recurrence relation', 'Persamaan yang menyatakan biaya masalah dari biaya submasalahnya, misal T(n) = 2T(n/2) + n.'),
       ('Backtracking', 'Rekursi yang mencoba pilihan, lalu mundur jika jalan buntu.'),
       ('Tail recursion', 'Panggilan rekursif sebagai langkah terakhir; Python tidak mengoptimalkannya.'),
       ('Recursion tree', 'Gambar pohon pemanggilan untuk menghitung total kerja rekursi.')],
  cx=[P('Semua kombinasi menu paket dan pohon pemanggilan', '''
def kombinasi(pilihan, k, mulai=0, sekarang=None, hasil=None):
    sekarang = [] if sekarang is None else sekarang
    hasil = [] if hasil is None else hasil
    if len(sekarang) == k:                    # base case
        hasil.append(tuple(sekarang)); return hasil
    for i in range(mulai, len(pilihan)):
        sekarang.append(pilihan[i])
        kombinasi(pilihan, k, i + 1, sekarang, hasil)
        sekarang.pop()                        # mundur (backtrack)
    return hasil
menu = ["nasi", "ayam", "tempe", "sayur"]
print("paket 2 lauk:", kombinasi(menu, 2))

def pohon(n, tingkat=0):
    print("  " * tingkat + f"fib({n})")
    if n >= 2: pohon(n - 1, tingkat + 1); pohon(n - 2, tingkat + 1)
pohon(4)
''')]),

'Binary search': dict(
  ist=[('Invariant', 'Target, jika ada, selalu di rentang [lo, hi]; menjaga ini mencegah bug batas.'),
       ('Lower / upper bound', 'Posisi pertama >= x dan posisi pertama > x; dasar menghitung kemunculan.'),
       ('Binary search on answer', 'Mencari jawaban numerik minimum/maksimum yang memenuhi syarat monoton.'),
       ('git bisect', 'Binary search atas riwayat commit untuk menemukan commit yang memperkenalkan bug.')],
  cx=[P('Mencari commit penyebab bug ala git bisect', '''
commits = [f"c{i:03d}" for i in range(1, 129)]
BUG_MULAI = 87
def tes_gagal(c): return int(c[1:]) >= BUG_MULAI      # pura-pura menjalankan test suite

lo, hi, langkah = 0, len(commits) - 1, 0
while lo < hi:
    mid = (lo + hi) // 2; langkah += 1
    if tes_gagal(commits[mid]): hi = mid
    else: lo = mid + 1
print(f"commit pertama yang rusak: {commits[lo]} (ditemukan dalam {langkah} tes dari {len(commits)} commit)")

from bisect import bisect_left, bisect_right
nilai = [55, 60, 60, 60, 72, 80, 80, 91]
print("jumlah nilai 60:", bisect_right(nilai, 60) - bisect_left(nilai, 60))
''', 'Dengan 128 commit, cukup 7 kali menjalankan test, bukan 128 kali. Fitur git bisect bekerja persis seperti ini.')]),

'Sorting dasar: bubble dan insertion sort': dict(
  ist=[('Insertion sort', 'Menyisipkan tiap elemen ke posisi yang benar di bagian yang sudah terurut; O(n²) tetapi cepat untuk data kecil atau hampir terurut.'),
       ('Adaptive', 'Lebih cepat jika input sudah hampir terurut; insertion sort O(n) pada data terurut.'),
       ('Stable', 'Elemen bernilai sama mempertahankan urutan awal; bubble dan insertion sort stabil.'),
       ('Hybrid sort', 'Timsort dan introsort memakai insertion sort untuk potongan kecil.')],
  cx=[P('Insertion sort pada data hampir terurut (feed yang terus bertambah)', '''
import random
def insertion(a):
    a = list(a); geser = 0
    for i in range(1, len(a)):
        x, j = a[i], i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]; j -= 1; geser += 1
        a[j + 1] = x
    return a, geser

rng = random.Random(5)
hampir = list(range(1000))
for _ in range(10):
    i = rng.randrange(999); hampir[i], hampir[i + 1] = hampir[i + 1], hampir[i]
acak = rng.sample(range(1000), 1000)
for nama, d in [("hampir terurut", hampir), ("acak", acak)]:
    hasil, g = insertion(d)
    gg = f"{g:,}".replace(",", ".")
    print(f"{nama:<15}: {gg:>7} pergeseran, benar {hasil == sorted(d)}")
''')]),

'Merge sort dan quick sort': dict(
  ist=[('Divide and conquer', 'Bagi data, urutkan bagian, lalu gabungkan (merge sort) atau partisi di sekitar pivot (quick sort).'),
       ('O(n log n)', 'Batas bawah pengurutan berbasis perbandingan.'),
       ('Pivot selection', 'Pivot buruk (selalu elemen pertama pada data terurut) membuat quick sort O(n²).'),
       ('External sort', 'Merge sort untuk data yang lebih besar dari RAM: urutkan potongan, lalu gabungkan dari disk.')],
  cx=[P('Merge sort, quick sort, dan bahaya pivot buruk', '''
import random, sys
sys.setrecursionlimit(5000)
def merge_sort(a):
    if len(a) <= 1: return a
    m = len(a) // 2; l, r = merge_sort(a[:m]), merge_sort(a[m:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]: out.append(l[i]); i += 1
        else: out.append(r[j]); j += 1
    return out + l[i:] + r[j:]

hit = [0]
def quick(a, pivot):
    if len(a) <= 1: return a
    p = pivot(a); hit[0] += len(a)
    return quick([x for x in a if x < p], pivot) + [x for x in a if x == p] + quick([x for x in a if x > p], pivot)

data = list(range(2000))                    # sudah terurut: kasus terburuk pivot pertama
print("merge sort benar:", merge_sort(random.Random(2).sample(data, 2000)) == data)
for nama, pv in [("pivot elemen pertama", lambda a: a[0]), ("pivot acak", lambda a: random.Random(len(a)).choice(a))]:
    hit[0] = 0; quick(data, pv)
    print(f"{nama:<21}: {hit[0]:>9,} perbandingan".replace(",", "."))
''')]),

'Binary tree dan penelusuran': dict(
  ist=[('DFS order', 'Pre-order, in-order, post-order: urutan mengunjungi simpul terhadap anak-anaknya.'),
       ('BFS / level order', 'Mengunjungi per tingkat dengan queue.'),
       ('Serialization', 'Mengubah pohon menjadi teks/array untuk disimpan atau dikirim, lalu dibangun ulang.'),
       ('DOM tree', 'Halaman web adalah pohon; browser dan React menelusurinya terus-menerus.')],
  cx=[P('Ukuran folder (post-order) dan tampilan per tingkat (BFS)', '''
from collections import deque
fs = ("/", 0, [("src", 0, [("app.py", 12, []), ("db.py", 8, [])]), ("data", 0, [("jual.csv", 340, []), ("arsip", 0, [("2025.csv", 900, [])])]), ("README.md", 3, [])])

def ukuran(node):                           # post-order: anak dulu baru induk
    nama, kb, anak = node
    return kb + sum(ukuran(a) for a in anak)

def cetak(node, ind=0):                     # pre-order
    nama, kb, anak = node
    print("  " * ind + f"{nama} ({ukuran(node)} KB)")
    for a in anak: cetak(a, ind + 1)
cetak(fs)

q, tingkat = deque([(fs, 0)]), {}
while q:
    (nama, _, anak), d = q.popleft()
    tingkat.setdefault(d, []).append(nama)
    q.extend((a, d + 1) for a in anak)
print("per tingkat:", tingkat)
''')]),

'Binary search tree': dict(
  ist=[('BST property', 'Semua kunci di subpohon kiri < simpul < semua kunci di subpohon kanan.'),
       ('Successor', 'Kunci terkecil yang lebih besar; dipakai saat menghapus simpul dengan dua anak.'),
       ('Range query', 'Mengambil semua kunci di rentang [a, b] dengan memangkas cabang yang tidak perlu.'),
       ('Balanced BST', 'AVL / red-black tree menjaga tinggi O(log n); TreeMap Java memakai red-black tree.')],
  cx=[P('BST untuk jadwal: cari, rentang, dan validasi', '''
class N:
    def __init__(self, k, v): self.k, self.v, self.l, self.r = k, v, None, None
def sisip(n, k, v):
    if not n: return N(k, v)
    if k < n.k: n.l = sisip(n.l, k, v)
    elif k > n.k: n.r = sisip(n.r, k, v)
    else: n.v = v
    return n
def rentang(n, a, b, out):
    if not n: return out
    if a < n.k: rentang(n.l, a, b, out)
    if a <= n.k <= b: out.append((n.k, n.v))
    if n.k < b: rentang(n.r, a, b, out)
    return out
def valid(n, lo=None, hi=None):
    if not n: return True
    if (lo is not None and n.k <= lo) or (hi is not None and n.k >= hi): return False
    return valid(n.l, lo, n.k) and valid(n.r, n.k, hi)

akar = None
for jam, acara in [("10:00", "rapat tim"), ("08:30", "stand-up"), ("13:00", "demo klien"), ("09:15", "review PR"), ("15:30", "1:1"), ("11:45", "makan siang")]:
    akar = sisip(akar, jam, acara)
print("jadwal 09:00-12:00:", rentang(akar, "09:00", "12:00", []))
print("pohon valid:", valid(akar))
''')]),

'Heap dan priority queue': dict(
  ist=[('Min-heap / max-heap', 'Akar selalu terkecil / terbesar; disimpan sebagai array dengan anak di 2i+1 dan 2i+2.'),
       ('Heapify O(n)', 'Membangun heap dari array sekaligus lebih cepat daripada n kali push.'),
       ('Top-k streaming', 'Menjaga k terbesar dari aliran data dengan min-heap berukuran k.'),
       ('Scheduler', 'Penjadwal tugas (cron, OS, Kubernetes) memakai priority queue berdasarkan waktu/prioritas.')],
  cx=[P('Top-5 produk terlaris dari aliran pesanan dan penjadwal tugas', '''
import heapq, random
rng = random.Random(8)
terjual = {f"SKU-{i:03d}": rng.randint(1, 5000) for i in range(10_000)}
top = []
for sku, n in terjual.items():               # streaming: memori O(k), bukan O(n)
    if len(top) < 5: heapq.heappush(top, (n, sku))
    elif n > top[0][0]: heapq.heapreplace(top, (n, sku))
print("top-5:", sorted(top, reverse=True))
print("sama dengan nlargest:", sorted(top, reverse=True) == heapq.nlargest(5, ((n, s) for s, n in terjual.items())))

tugas = [(30, "kirim laporan"), (5, "backup DB"), (15, "sinkron stok"), (5, "rotasi log")]
heapq.heapify(tugas)
while tugas:
    t, nama = heapq.heappop(tugas); print(f"menit {t:>2}: {nama}")
''')]),

'Representasi graph, BFS, dan DFS': dict(
  ist=[('Adjacency list', 'Setiap simpul menyimpan daftar tetangganya; hemat untuk graph jarang (sparse).'),
       ('BFS', 'Breadth-first search: per lapis dengan queue; memberi jalur terpendek pada graph tak berbobot.'),
       ('DFS', 'Depth-first search: menyelam sedalam mungkin dengan stack/rekursi; dipakai deteksi siklus dan komponen.'),
       ('Connected component', 'Kelompok simpul yang saling terhubung; misalnya cluster akun yang saling terkait.')],
  cx=[P('Derajat koneksi (BFS) dan cluster akun penipuan (DFS)', '''
from collections import deque
teman = {"Ani": ["Budi", "Citra"], "Budi": ["Ani", "Dedi"], "Citra": ["Ani", "Dedi", "Eka"], "Dedi": ["Budi", "Citra", "Fajar"],
         "Eka": ["Citra"], "Fajar": ["Dedi"], "Gita": ["Hadi"], "Hadi": ["Gita"]}
def derajat(asal):
    jarak, q = {asal: 0}, deque([asal])
    while q:
        u = q.popleft()
        for v in teman[u]:
            if v not in jarak: jarak[v] = jarak[u] + 1; q.append(v)
    return jarak
print("koneksi dari Ani:", derajat("Ani"))

# akun yang memakai perangkat/nomor yang sama dihubungkan
pakai_sama = [("A1", "A2"), ("A2", "A5"), ("A3", "A4"), ("A6", "A6"), ("A5", "A7")]
g = {}
for a, b in pakai_sama: g.setdefault(a, set()).add(b); g.setdefault(b, set()).add(a)
lihat, cluster = set(), []
for s in g:
    if s in lihat: continue
    st, komp = [s], []
    while st:
        u = st.pop()
        if u in lihat: continue
        lihat.add(u); komp.append(u); st.extend(g[u] - lihat)
    cluster.append(sorted(komp))
print("cluster akun:", sorted(cluster, key=len, reverse=True))
''')]),

'Dijkstra: jalur terpendek berbobot': dict(
  ist=[('Weighted graph', 'Sisi memiliki bobot: jarak, waktu, atau biaya.'),
       ('Relaxation', 'Memperbarui jarak terbaik ke simpul jika ditemukan jalur yang lebih pendek.'),
       ('Non-negative weights', 'Dijkstra mensyaratkan bobot tidak negatif; jika ada negatif, pakai Bellman-Ford.'),
       ('A* search', 'Dijkstra plus heuristik jarak ke tujuan; dipakai aplikasi peta dan game.')],
  cx=[P('Rute pengiriman tercepat antar gudang (menit)', '''
import heapq
jalan = {"Gudang": {"A": 12, "B": 7}, "A": {"C": 5, "D": 15}, "B": {"A": 3, "C": 14, "E": 25},
         "C": {"D": 4, "E": 9}, "D": {"Pelanggan": 6}, "E": {"Pelanggan": 3}, "Pelanggan": {}}
def dijkstra(g, s):
    dist, prev, pq = {s: 0}, {}, [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in g[u].items():
            if d + w < dist.get(v, float("inf")):
                dist[v], prev[v] = d + w, u; heapq.heappush(pq, (d + w, v))
    return dist, prev
dist, prev = dijkstra(jalan, "Gudang")
rute, x = [], "Pelanggan"
while x != "Gudang": rute.append(x); x = prev[x]
print("rute:", " -> ".join(["Gudang"] + rute[::-1]), f"({dist['Pelanggan']} menit)")
print("waktu ke semua titik:", dist)
''')]),

'Topological sort': dict(
  ist=[('DAG', 'Directed Acyclic Graph: graph berarah tanpa siklus; mewakili dependensi.'),
       ("Kahn's algorithm", 'Topological sort dengan menghitung in-degree dan memproses simpul tanpa prasyarat.'),
       ('Cycle detection', 'Jika tidak semua simpul terproses, ada dependensi melingkar.'),
       ('Build system / DAG scheduler', 'Make, Gradle, Airflow, dan dbt menjalankan tugas sesuai urutan topologis.')],
  cx=[P('Urutan menjalankan pipeline data (gaya Airflow/dbt)', '''
from collections import deque
butuh = {"ekstrak_orders": [], "ekstrak_produk": [], "bersihkan_orders": ["ekstrak_orders"],
         "dim_produk": ["ekstrak_produk"], "fakta_penjualan": ["bersihkan_orders", "dim_produk"],
         "dashboard": ["fakta_penjualan"], "email_laporan": ["dashboard"]}
def topo(butuh):
    indeg = {t: len(p) for t, p in butuh.items()}
    anak = {t: [] for t in butuh}
    for t, ps in butuh.items():
        for p in ps: anak[p].append(t)
    q, urut = deque(sorted(t for t, d in indeg.items() if d == 0)), []
    while q:
        t = q.popleft(); urut.append(t)
        for a in anak[t]:
            indeg[a] -= 1
            if indeg[a] == 0: q.append(a)
    return urut if len(urut) == len(butuh) else f"SIKLUS terdeteksi di {sorted(set(butuh) - set(urut))}"
for i, t in enumerate(topo(butuh), 1): print(i, t)
butuh["ekstrak_orders"] = ["email_laporan"]          # dependensi melingkar
print(topo(butuh))
''')]),

'Dynamic programming: memoization dan tabulation': dict(
  ist=[('Overlapping subproblems', 'Submasalah yang sama muncul berulang; syarat DP bermanfaat.'),
       ('Optimal substructure', 'Solusi optimal tersusun dari solusi optimal submasalah.'),
       ('Memoization (top-down)', 'Rekursi + cache hasil.'),
       ('Tabulation (bottom-up)', 'Mengisi tabel dari kasus terkecil; tanpa rekursi sehingga aman untuk n besar.')],
  cx=[P('Jumlah koin minimum untuk kembalian (bottom-up)', '''
def koin_min(koin, target):
    INF = float("inf")
    dp = [0] + [INF] * target
    pakai = [0] * (target + 1)
    for x in range(1, target + 1):
        for k in koin:
            if k <= x and dp[x - k] + 1 < dp[x]:
                dp[x], pakai[x] = dp[x - k] + 1, k
    if dp[target] == INF: return None
    hasil = []
    while target: hasil.append(pakai[target]); target -= pakai[target]
    return hasil

print("koin rupiah, 2.800 :", koin_min([100, 200, 500, 1000], 2800))
print("koin aneh 1,3,4 -> 6:", koin_min([1, 3, 4], 6), "(greedy salah: [4, 1, 1])")
print("tidak mungkin       :", koin_min([500, 1000], 2_700))
''', 'Pada sistem koin rupiah, greedy kebetulan optimal. Pada sistem koin sembarang, hanya DP yang menjamin jawaban minimum.')]),

'Knapsack 0/1 dan LCS': dict(
  ist=[('0/1 knapsack', 'Memilih barang (diambil utuh atau tidak) dengan kapasitas terbatas untuk nilai maksimum.'),
       ('LCS', 'Longest Common Subsequence: subsekuens terpanjang yang sama dari dua teks.'),
       ('diff', 'Alat diff dan Git memakai algoritma mirip LCS untuk menampilkan baris yang berubah.'),
       ('Pseudo-polynomial', 'Knapsack O(n x W) cepat untuk kapasitas W kecil, tetapi lambat jika W sangat besar.')],
  cx=[P('Memilih fitur sprint dalam kapasitas tim dan diff dua versi teks', '''
fitur = [("Login OTP", 5, 40), ("Dark mode", 3, 15), ("Export PDF", 4, 30), ("Notifikasi", 2, 20), ("Chat CS", 8, 55)]
KAP = 12                                   # story point satu sprint
dp = [[0] * (KAP + 1) for _ in range(len(fitur) + 1)]
for i, (_, sp, nilai) in enumerate(fitur, 1):
    for c in range(KAP + 1):
        dp[i][c] = dp[i - 1][c]
        if sp <= c: dp[i][c] = max(dp[i][c], dp[i - 1][c - sp] + nilai)
pilih, c = [], KAP
for i in range(len(fitur), 0, -1):
    if dp[i][c] != dp[i - 1][c]: pilih.append(fitur[i - 1][0]); c -= fitur[i - 1][1]
print(f"nilai bisnis {dp[-1][KAP]} dengan fitur: {pilih[::-1]}")

def diff(a, b):
    L = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            L[i][j] = L[i + 1][j + 1] + 1 if a[i] == b[j] else max(L[i + 1][j], L[i][j + 1])
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]: out.append("  " + a[i]); i += 1; j += 1
        elif L[i + 1][j] >= L[i][j + 1]: out.append("- " + a[i]); i += 1
        else: out.append("+ " + b[j]); j += 1
    return out + ["- " + x for x in a[i:]] + ["+ " + x for x in b[j:]]
lama = ["import os", "def main():", "    print('halo')", "main()"]
baru = ["import os", "import sys", "def main():", "    print('halo dunia')", "main()"]
print("\\n".join(diff(lama, baru)))
''')]),

'Greedy dan backtracking': dict(
  ist=[('Greedy choice', 'Mengambil pilihan terbaik lokal di setiap langkah; benar hanya untuk masalah tertentu.'),
       ('Interval scheduling', 'Memilih kegiatan terbanyak tanpa bentrok dengan mengurutkan berdasarkan waktu selesai.'),
       ('Backtracking', 'Mencoba pilihan secara rekursif dan mundur saat melanggar batasan.'),
       ('Pruning', 'Memangkas cabang pencarian yang pasti gagal agar backtracking cepat.')],
  cx=[P('Memakai ruang rapat (greedy) dan jadwal piket tanpa bentrok (backtracking)', '''
rapat = [("Sprint review", 9, 11), ("Stand-up", 9, 10), ("1:1", 10, 11), ("Demo", 11, 12), ("Retro", 10, 13), ("Sync", 12, 13)]
dipilih, selesai = [], 0
for nama, mulai, akhir in sorted(rapat, key=lambda r: r[2]):     # urut waktu selesai
    if mulai >= selesai: dipilih.append(nama); selesai = akhir
print("rapat terbanyak di 1 ruang:", dipilih)

orang = ["Ani", "Budi", "Citra", "Dedi"]
tidak_bisa = {"Ani": {"Sen"}, "Budi": {"Sel", "Rab"}, "Citra": {"Sen", "Sel"}, "Dedi": {"Rab"}}
hari = ["Sen", "Sel", "Rab", "Kam"]
def atur(i=0, jadwal=None, dicoba=[0]):
    jadwal = jadwal or {}
    if i == len(hari): return jadwal
    for o in orang:
        dicoba[0] += 1
        if o in jadwal.values() or hari[i] in tidak_bisa[o]: continue    # pruning
        hasil = atur(i + 1, {**jadwal, hari[i]: o})
        if hasil: return hasil
    return None
print("jadwal piket:", atur())
''')]),
}
