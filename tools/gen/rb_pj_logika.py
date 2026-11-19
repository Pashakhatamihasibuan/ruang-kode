"""Proyek jalur Logika, Python & Algoritma: 6 mini (Python, dijalankan) + 4 besar berskala industri 2026-2027."""
from rb_pj_lib import MINI, BESAR, JALUR_M
from rb_lib import q

# ---------------------------------------------------------------- MINI
VALIDATOR = r'''import csv, io, re
from collections import Counter

# Data pendaftaran pelanggan dari formulir & impor Excel: belum bersih
CSV = """nama,nik,hp,email,tgl_lahir
  budi SANTOSO ,3201123456780001,0812-3456-7890,Budi.S@Contoh.id,17/04/1999
Siti Aminah,32011234567800,+62 857 1111 2222,siti@contoh,1998-02-30
ANDI,3273010101010002,62811223344,andi@contoh.id,05-11-2001
rené wijaya,3201123456780001,0813 9999 0000,rene@contoh.id,2010-01-15
,3174050505050005,08123,kosong@contoh.id,1990-12-01
"""

class BarisTidakValid(Exception):
    pass

def norm_nama(s):
    s = " ".join(s.split())
    if len(s) < 2: raise BarisTidakValid("nama kosong")
    return s.title()

def norm_nik(s):
    if not re.fullmatch(r"\d{16}", s): raise BarisTidakValid(f"NIK harus 16 digit (didapat {len(s)})")
    return s

def norm_hp(s):
    d = re.sub(r"\D", "", s)
    if d.startswith("0"): d = "62" + d[1:]
    if not (d.startswith("628") and 10 <= len(d) <= 15): raise BarisTidakValid(f"HP tidak valid: {s}")
    return d

def norm_email(s):
    s = s.strip().lower()
    if not re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", s): raise BarisTidakValid(f"email tidak valid: {s}")
    return s

def norm_tgl(s):
    from datetime import date
    for pola in (r"(\d{4})-(\d{2})-(\d{2})", r"(\d{2})[/-](\d{2})[/-](\d{4})"):
        m = re.fullmatch(pola, s.strip())
        if m:
            a, b, c = map(int, m.groups())
            y, mo, d = (a, b, c) if a > 31 else (c, b, a)
            try: t = date(y, mo, d)
            except ValueError: raise BarisTidakValid(f"tanggal mustahil: {s}")
            umur = (date(2026, 11, 19) - t).days // 365
            if umur < 17: raise BarisTidakValid(f"umur {umur} di bawah 17")
            return t.isoformat()
    raise BarisTidakValid(f"format tanggal tidak dikenal: {s}")

bersih, ditolak, nik_terpakai = [], [], set()
for no, r in enumerate(csv.DictReader(io.StringIO(CSV)), start=2):
    try:
        rec = {"nama": norm_nama(r["nama"]), "nik": norm_nik(r["nik"]), "hp": norm_hp(r["hp"]),
               "email": norm_email(r["email"]), "tgl_lahir": norm_tgl(r["tgl_lahir"])}
        if rec["nik"] in nik_terpakai: raise BarisTidakValid("NIK duplikat")
        nik_terpakai.add(rec["nik"]); bersih.append(rec)
    except BarisTidakValid as e:
        ditolak.append((no, str(e)))

print(f"{len(bersih)} baris lolos, {len(ditolak)} ditolak")
for r in bersih:
    print(f"  {r['nama']:<14} NIK ************{r['nik'][-4:]}  {r['hp']:<14} {r['email']:<16} {r['tgl_lahir']}")
print("Laporan penolakan (kirim balik ke admin):")
for no, alasan in ditolak: print(f"  baris {no}: {alasan}")
print("Jenis masalah:", dict(Counter(a.split(" ")[0] for _, a in ditolak)))
'''

KASIR = r'''from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP

class StokTidakCukup(Exception): pass
class VoucherTidakBerlaku(Exception): pass

@dataclass
class Produk:
    sku: str
    nama: str
    harga: int
    stok: int

@dataclass
class Keranjang:
    item: dict = field(default_factory=dict)          # sku -> qty
    voucher: str | None = None

class Toko:
    PPN = Decimal("0.11")
    VOUCHER = {"HEMAT10": ("persen", 10, 100_000), "ONGKIR15": ("potong", 15_000, 75_000)}   # (jenis, nilai, minimum belanja)

    def __init__(self, produk):
        self.produk = {p.sku: p for p in produk}
        self.log = []

    def tambah(self, k, sku, qty):
        p = self.produk[sku]
        if p.stok - k.item.get(sku, 0) < qty:
            raise StokTidakCukup(f"{p.nama}: sisa {p.stok - k.item.get(sku, 0)}, diminta {qty}")
        k.item[sku] = k.item.get(sku, 0) + qty

    def hitung(self, k):
        sub = sum(self.produk[s].harga * q for s, q in k.item.items())
        diskon = 0
        if k.voucher:
            if k.voucher not in self.VOUCHER: raise VoucherTidakBerlaku(f"{k.voucher} tidak dikenal")
            jenis, nilai, minimum = self.VOUCHER[k.voucher]
            if sub < minimum: raise VoucherTidakBerlaku(f"{k.voucher} butuh minimum belanja Rp{minimum:,}".replace(",", "."))
            diskon = sub * nilai // 100 if jenis == "persen" else nilai
        dpp = sub - diskon
        ppn = int((Decimal(dpp) * self.PPN).quantize(Decimal("1"), ROUND_HALF_UP))
        return sub, diskon, ppn, dpp + ppn

    def checkout(self, k, bayar):
        sub, diskon, ppn, total = self.hitung(k)
        if bayar < total: raise ValueError(f"uang kurang Rp{total - bayar:,}".replace(",", "."))
        for s, q in k.item.items(): self.produk[s].stok -= q        # stok berkurang hanya jika transaksi sukses
        self.log.append(total)
        rp = lambda x: f"{x:,}".replace(",", ".")
        print("-" * 34)
        for s, q in k.item.items():
            p = self.produk[s]; print(f"{p.nama:<14}{q:>3} x{rp(p.harga):>7} {rp(p.harga * q):>8}")
        for label, v in [("Subtotal", sub), (f"Voucher {k.voucher or '-'}", -diskon), ("PPN 11%", ppn), ("TOTAL", total), ("Bayar", bayar), ("Kembali", bayar - total)]:
            print(f"{label:<24}{rp(v):>10}")

toko = Toko([Produk("KP1", "Kopi Gayo", 85_000, 5), Produk("GL1", "Gula aren", 32_500, 2), Produk("SS1", "Susu oat", 29_900, 10)])
k = Keranjang()
for sku, qty in [("KP1", 2), ("GL1", 3), ("GL1", 2), ("SS1", 1)]:
    try: toko.tambah(k, sku, qty); print(f"+ {qty} {sku}")
    except StokTidakCukup as e: print("ditolak:", e)
for v in ["DISKON99", "HEMAT10"]:
    k.voucher = v
    try: toko.hitung(k); print("voucher dipakai:", v); break
    except VoucherTidakBerlaku as e: print("voucher ditolak:", e)
toko.checkout(k, 300_000)
print("-" * 34)
print("sisa stok:", {s: p.stok for s, p in toko.produk.items()}, "| transaksi hari ini:", len(toko.log))
'''

JADWAL = r'''# Penjadwal ujian tanpa bentrok: graph coloring dengan heuristik DSatur + backtracking jika slot terbatas
ambil = {  # mahasiswa -> mata kuliah yang diambil
    "M01": ["Algoritma", "Basis Data", "Statistika"], "M02": ["Algoritma", "Jaringan"], "M03": ["Basis Data", "Jaringan", "Etika"],
    "M04": ["Statistika", "Etika"], "M05": ["Algoritma", "Basis Data"], "M06": ["Jaringan", "Statistika"],
    "M07": ["Kalkulus", "Algoritma"], "M08": ["Kalkulus", "Etika", "Basis Data"],
}
# 1. bangun graph konflik: dua matkul bertetangga jika ada mahasiswa yang mengambil keduanya
konflik = {}
for mk in ambil.values():
    for a in mk:
        konflik.setdefault(a, set())
        for b in mk:
            if a != b: konflik[a].add(b)
print("derajat konflik:", {m: len(v) for m, v in sorted(konflik.items(), key=lambda x: -len(x[1]))})

# 2. DSatur: pilih matkul dengan warna tetangga paling beragam, beri slot terkecil yang aman
def dsatur(g):
    slot = {}
    while len(slot) < len(g):
        sisa = [v for v in g if v not in slot]
        v = max(sisa, key=lambda v: (len({slot[u] for u in g[v] if u in slot}), len(g[v]), v))
        dipakai = {slot[u] for u in g[v] if u in slot}
        slot[v] = next(s for s in range(len(g)) if s not in dipakai)
    return slot

# 3. backtracking: apakah bisa dengan k slot saja?
def bisa(g, k):
    urut = sorted(g, key=lambda v: -len(g[v])); slot = {}
    def coba(i):
        if i == len(urut): return True
        v = urut[i]
        for s in range(k):
            if all(slot.get(u) != s for u in g[v]):
                slot[v] = s
                if coba(i + 1): return True
                del slot[v]
        return False
    return dict(slot) if coba(0) else None

hasil = dsatur(konflik)
JAM = ["Sen 08:00", "Sen 13:00", "Sel 08:00", "Sel 13:00", "Rab 08:00"]
print(f"DSatur memakai {max(hasil.values()) + 1} slot:")
for s in sorted(set(hasil.values())):
    print(f"  {JAM[s]}: {sorted(m for m, x in hasil.items() if x == s)}")
for k in range(2, 5):
    print(f"bisa dengan {k} slot?", "ya" if bisa(konflik, k) else "tidak")
bentrok = [(a, b) for a in konflik for b in konflik[a] if hasil[a] == hasil[b]]
print("verifikasi bentrok:", len(bentrok))
'''

RUTE = r'''import heapq, itertools, math

# Kurir mengantar 6 paket dari gudang. Langkah 1: jarak terpendek antar titik di peta jalan (Dijkstra).
jalan = {"Gudang": {"A": 4, "B": 2}, "A": {"Gudang": 4, "B": 1, "C": 5}, "B": {"Gudang": 2, "A": 1, "D": 8, "E": 10},
         "C": {"A": 5, "D": 2, "F": 6}, "D": {"B": 8, "C": 2, "E": 3, "F": 4}, "E": {"B": 10, "D": 3, "F": 2}, "F": {"C": 6, "D": 4, "E": 2}}

def dijkstra(src):
    dist, pq = {src: 0}, [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in jalan[u].items():
            if d + w < dist.get(v, math.inf): dist[v] = d + w; heapq.heappush(pq, (d + w, v))
    return dist

titik = list(jalan)
D = {a: dijkstra(a) for a in titik}                  # matriks jarak semua pasangan (km)
tujuan = ["A", "B", "C", "D", "E", "F"]

def panjang(rute): return sum(D[a][b] for a, b in zip(rute, rute[1:]))

# Langkah 2a: heuristik nearest neighbor (cepat, O(n²), belum tentu optimal)
rute, sisa = ["Gudang"], set(tujuan)
while sisa:
    nxt = min(sisa, key=lambda t: (D[rute[-1]][t], t)); rute.append(nxt); sisa.remove(nxt)
rute.append("Gudang")
print("nearest neighbor:", " -> ".join(rute), f"= {panjang(rute)} km")

# Langkah 2b: perbaikan 2-opt (balik segmen jika memperpendek)
def dua_opt(r):
    membaik = True
    while membaik:
        membaik = False
        for i in range(1, len(r) - 2):
            for j in range(i + 1, len(r) - 1):
                baru = r[:i] + r[i:j + 1][::-1] + r[j + 1:]
                if panjang(baru) < panjang(r): r, membaik = baru, True
    return r
r2 = dua_opt(rute)
print("setelah 2-opt   :", " -> ".join(r2), f"= {panjang(r2)} km")

# Langkah 3: brute force untuk membuktikan optimal (6! = 720 urutan; tidak mungkin untuk 50 titik)
terbaik = min((["Gudang", *p, "Gudang"] for p in itertools.permutations(tujuan)), key=panjang)
print("optimal (brute) :", " -> ".join(terbaik), f"= {panjang(terbaik)} km")
print(f"jumlah urutan untuk 15 titik: {math.factorial(15):,}".replace(",", "."))
'''

LOG = r'''import re, statistics
from collections import Counter, deque
from itertools import islice

# Generator log akses (di produksi: for baris in open("access.log"))
def sumber_log():
    import random
    rng = random.Random(42)
    endpoint = ["/", "/produk", "/produk/7", "/keranjang", "/checkout", "/login"]
    for detik in range(0, 600):                       # 10 menit
        n = 3 if not 300 <= detik < 330 else 25       # lonjakan di menit ke-5
        for _ in range(rng.randint(n - 2, n + 2)):
            ip = f"10.0.{rng.randint(0, 3)}.{rng.randint(1, 40)}" if detik < 300 or detik >= 330 else "203.0.113.9"
            ep = rng.choice(endpoint) if ip != "203.0.113.9" else "/login"
            status = 401 if ep == "/login" and ip == "203.0.113.9" else rng.choice([200] * 18 + [404, 500])
            yield f'{ip} - - [19/Nov/2026:10:{detik // 60:02d}:{detik % 60:02d} +0700] "GET {ep} HTTP/1.1" {status} {rng.randint(200, 5000)} {rng.randint(20, 300)}'

POLA = re.compile(r'(?P<ip>\S+) .*?:(?P<m>\d{2}):(?P<s>\d{2}) .*?"(?P<met>\w+) (?P<ep>\S+) .*?" (?P<st>\d{3}) (?P<b>\d+) (?P<ms>\d+)')

def parse(baris):
    for b in baris:
        m = POLA.match(b)
        if m: yield m["ip"], int(m["m"]) * 60 + int(m["s"]), m["ep"], int(m["st"]), int(m["ms"])

per_status, per_ep, durasi = Counter(), Counter(), []
gagal_login_ip, jendela, lonjakan = Counter(), deque(), []
for ip, t, ep, st, ms in parse(sumber_log()):
    per_status[st // 100 * 100] += 1; per_ep[ep] += 1; durasi.append(ms)
    if ep == "/login" and st == 401: gagal_login_ip[ip] += 1
    jendela.append(t)
    while jendela[0] <= t - 10: jendela.popleft()          # sliding window 10 detik
    if len(jendela) > 150 and (not lonjakan or t - lonjakan[-1] > 30): lonjakan.append(t)

total = sum(per_status.values())
print(f"{total:,} request dalam 10 menit".replace(",", "."))
print("status:", {f"{k // 100}xx": f"{v / total:.1%}".replace(".", ",") for k, v in sorted(per_status.items())})
print("endpoint teratas:", per_ep.most_common(3))
q = statistics.quantiles(durasi, n=100)
print(f"latensi p50 {q[49]:.0f} ms, p95 {q[94]:.0f} ms, p99 {q[98]:.0f} ms")
for t in lonjakan: print(f"ALERT lonjakan trafik mulai 10:{t // 60:02d}:{t % 60:02d}")
for ip, n in gagal_login_ip.items():
    if n >= 20: print(f"ALERT brute force login dari {ip}: {n} kali 401 -> blokir sementara di WAF")
'''

CARI = r'''# Pencarian produk toleran salah ketik: trie untuk autocomplete + edit distance (DP) untuk koreksi
PRODUK = {"kopi gayo arabika": 950, "kopi toraja": 610, "kopi susu literan": 1200, "kopiah hitam": 80, "teh melati": 430,
          "teh tarik": 520, "gula aren cair": 700, "susu oat": 390, "keripik singkong": 860, "kerupuk udang": 300}

class Trie:
    def __init__(self): self.anak, self.skor = {}, None
    def tambah(self, kata, skor):
        n = self
        for c in kata: n = n.anak.setdefault(c, Trie())
        n.skor = skor
    def awalan(self, p, k=3):
        n = self
        for c in p:
            if c not in n.anak: return []
            n = n.anak[c]
        hasil, st = [], [(n, p)]
        while st:
            x, s = st.pop()
            if x.skor is not None: hasil.append((-x.skor, s))
            st.extend((a, s + c) for c, a in x.anak.items())
        return [s for _, s in sorted(hasil)[:k]]

def jarak_edit(a, b):                          # Damerau-Levenshtein (OSA): DP O(len(a) x len(b))
    d = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + 1)          # tukar dua huruf bersebelahan
    return d[-1][-1]

KATA = sorted({w for nama in PRODUK for w in nama.split()})
def koreksi(w):
    if w in KATA: return w
    batas = 1 if len(w) <= 4 else 2
    kandidat = sorted((jarak_edit(w, k), k) for k in KATA)
    d, k = kandidat[0]
    return k if d <= batas else None

trie = Trie()
for nama, skor in PRODUK.items(): trie.tambah(nama, skor)

def cari(teks):
    kata = teks.lower().split()
    benar = [koreksi(w) or w for w in kata]
    hasil = [n for n in sorted(PRODUK, key=lambda n: -PRODUK[n]) if all(w in n.split() for w in benar)]
    saran = f" (maksud Anda: '{' '.join(benar)}'?)" if benar != kata else ""
    return hasil[:3], saran

for awal in ["ko", "kopi s", "te", "ke"]:
    print(f"autocomplete {awal!r:<9} -> {trie.awalan(awal)}")
for q in ["kopi", "kpoi toraja", "teh mleati", "sus oat", "kripik", "laptop"]:
    hasil, saran = cari(q)
    print(f"cari {q!r:<14} -> {hasil or 'tidak ditemukan'}{saran}")
'''

LG_MINI = [
MINI(1, 'Validator dan normalisasi data pelanggan',
  'Admin toko mengimpor ribuan baris pelanggan dari formulir dan Excel. Nama berantakan, nomor HP berbeda format, NIK kurang digit, tanggal lahir mustahil, dan ada NIK ganda. Data kotor ini membuat pengiriman WhatsApp gagal dan laporan salah.',
  ['Normalisasi nama (spasi, huruf kapital) dan nomor HP ke format 62xxx', 'Validasi NIK 16 digit, email, dan tanggal lahir (format ganda, tanggal mustahil, umur minimal 17)', 'Tolak NIK duplikat', 'Satu baris rusak tidak menghentikan impor; semua alasan penolakan dicatat per nomor baris', 'Tampilkan NIK yang di-masking pada laporan'],
  ['Buat satu fungsi norm_* per kolom yang mengembalikan nilai bersih atau melempar BarisTidakValid.', 'Pakai regex untuk pola dan datetime.date untuk menolak tanggal seperti 30 Februari; hitung umur dari tanggal acuan.', 'Simpan NIK yang sudah diterima di set agar pengecekan duplikat O(1).', 'Bungkus pemrosesan tiap baris dengan try/except dan kumpulkan (nomor baris, alasan).', 'Masking dengan slicing: tampilkan 4 digit terakhir saja.'],
  VALIDATOR, 'python', run=True,
  kunci='baca berkas CSV sungguhan dengan argparse, tulis bersih.csv dan ditolak.csv, lalu tambahkan test pytest untuk setiap fungsi norm_*.',
  cek=q('Kenapa setiap baris dibungkus try/except, bukan seluruh impor sekaligus?', ['Agar satu baris rusak tidak menggagalkan ribuan baris lain, dan setiap alasan penolakan tercatat', 'Karena try/except membuat kode lebih cepat', 'Karena Python mewajibkannya'], 0, 'Error ditangani per unit kerja.')),
MINI(2, 'Kasir toko dengan stok, voucher, dan PPN',
  'Toko kopi kecil butuh kasir sederhana yang tidak menjual barang melebihi stok, menolak voucher yang tidak memenuhi syarat, menghitung PPN dengan benar, dan baru mengurangi stok saat pembayaran berhasil.',
  ['Model Produk dan Keranjang dengan dataclass', 'Menolak penambahan yang melebihi stok, termasuk yang sudah ada di keranjang', 'Voucher persen dan potongan tetap dengan minimum belanja', 'PPN 11% dihitung dari harga setelah diskon dengan Decimal', 'Struk rapi dan stok berkurang hanya setelah checkout berhasil'],
  ['Pisahkan data (dataclass) dari aturan (kelas Toko).', 'Hitung sisa efektif = stok - qty di keranjang; lempar StokTidakCukup jika kurang.', 'Simpan aturan voucher sebagai data (jenis, nilai, minimum) dan lempar VoucherTidakBerlaku.', 'Gunakan Decimal dan ROUND_HALF_UP untuk PPN agar pembulatan sesuai kebiasaan akuntansi.', 'Kurangi stok di dalam checkout setelah validasi pembayaran; cetak struk dengan format specifier.'],
  KASIR, 'python', run=True,
  kunci='simpan produk dan transaksi ke SQLite, tambahkan laporan penjualan harian, dan buat antarmuka CLI dengan menu do-while.',
  cek=q('Kenapa stok baru dikurangi di checkout, bukan saat barang dimasukkan ke keranjang?', ['Keranjang bisa dibatalkan; jika stok dikurangi lebih awal, stok terlihat habis padahal barang tidak terjual', 'Agar perhitungan PPN lebih mudah', 'Karena dataclass tidak bisa diubah'], 0, 'Efek samping terjadi saat transaksi pasti.')),
MINI(3, 'Penjadwal ujian tanpa bentrok (graph coloring)',
  'Bagian akademik menyusun jadwal ujian secara manual dan selalu ada mahasiswa yang dua ujiannya bentrok. Mereka butuh jadwal otomatis dengan jumlah slot sesedikit mungkin.',
  ['Bangun graph konflik dari data pengambilan mata kuliah', 'Beri slot dengan heuristik DSatur', 'Uji dengan backtracking apakah jumlah slot bisa dikurangi', 'Verifikasi tidak ada pasangan bentrok', 'Tampilkan jadwal per slot waktu'],
  ['Untuk setiap mahasiswa, hubungkan setiap pasangan mata kuliahnya (adjacency set).', 'DSatur: pilih simpul dengan saturasi (jumlah warna tetangga berbeda) tertinggi, beri warna terkecil yang aman.', 'Backtracking: coba warna 0..k-1 berurutan, mundur saat buntu; urutkan simpul dari derajat terbesar untuk pruning.', 'Periksa semua sisi: kedua ujung tidak boleh memiliki slot sama.', 'Petakan nomor warna ke label hari dan jam.'],
  JADWAL, 'python', run=True,
  kunci='tambahkan kapasitas ruang per slot dan aturan "maksimal 2 ujian per hari per mahasiswa", lalu ekspor ke CSV.',
  cek=q('Kenapa graph coloring cocok untuk penjadwalan ujian?', ['Mata kuliah yang berbagi mahasiswa dihubungkan, dan "warna" yang berbeda berarti slot berbeda, sehingga tidak ada bentrok', 'Karena warna membuat jadwal lebih menarik', 'Karena graph selalu lebih cepat dari list'], 0, 'Pemodelan masalah sebagai graph.')),
MINI(4, 'Rute kurir: Dijkstra, nearest neighbor, dan 2-opt',
  'Kurir UMKM harus mengantar 6 paket lalu kembali ke gudang. Rute dipilih berdasarkan perasaan, sehingga bensin dan waktu terbuang. Pemilik ingin rute yang mendekati optimal tanpa perangkat lunak mahal.',
  ['Hitung jarak terpendek antar semua titik dengan Dijkstra', 'Susun rute awal dengan nearest neighbor', 'Perbaiki rute dengan 2-opt', 'Bandingkan dengan solusi optimal brute force untuk data kecil', 'Jelaskan kenapa brute force tidak bisa dipakai untuk banyak titik'],
  ['Jalankan Dijkstra dari setiap titik untuk mendapat matriks jarak (peta jalan tidak langsung lengkap).', 'Nearest neighbor: dari posisi sekarang selalu ke tujuan terdekat yang belum dikunjungi.', '2-opt: coba balik setiap segmen; ulangi selama ada perbaikan.', 'Brute force dengan itertools.permutations untuk memastikan kualitas heuristik.', 'Hitung n! untuk menunjukkan ledakan kombinasi (TSP adalah NP-hard).'],
  RUTE, 'python', run=True,
  kunci='tambahkan jendela waktu pengantaran dan kapasitas motor, lalu bandingkan dengan pustaka OR-Tools.',
  cek=q('Kenapa memakai heuristik (nearest neighbor + 2-opt) dan bukan brute force untuk 50 titik?', ['50! urutan terlalu banyak untuk dihitung; heuristik memberi rute bagus dalam waktu singkat', 'Karena brute force selalu salah', 'Karena Dijkstra tidak bisa dipakai untuk 50 titik'], 0, 'Masalah NP-hard butuh heuristik.')),
MINI(5, 'Analisis log server dan deteksi anomali',
  'Toko daring mendadak lambat dan tim tidak tahu penyebabnya. File access log berukuran besar harus dianalisis tanpa memuat semuanya ke memori, lalu lonjakan trafik dan percobaan brute force login harus terdeteksi otomatis.',
  ['Baca log secara streaming dengan generator', 'Parsing baris dengan regex bernama', 'Ringkasan status, endpoint teratas, dan latensi p50/p95/p99', 'Deteksi lonjakan dengan sliding window 10 detik', 'Deteksi IP dengan banyak login gagal'],
  ['Generator sumber_log dan parse membentuk pipeline yang memproses satu baris setiap kali.', 'Regex dengan named group menghasilkan field yang jelas; baris tak cocok dilewati.', 'Counter untuk agregasi; statistics.quantiles untuk persentil latensi.', 'deque menyimpan waktu request di jendela; buang yang lebih tua dari 10 detik; alert jika melewati ambang.', 'Hitung 401 per IP di /login; beri rekomendasi blokir di WAF.'],
  LOG, 'python', run=True,
  kunci='baca log Nginx sungguhan, kirim alert ke Telegram/Slack lewat webhook, dan simpan ringkasan per menit ke SQLite.',
  cek=q('Kenapa log dibaca dengan generator, bukan readlines()?', ['Generator memproses satu baris setiap kali sehingga file berukuran GB tidak memenuhi memori', 'Karena readlines() tidak bisa membaca log', 'Agar regex lebih cepat'], 0, 'Streaming hemat memori.')),
MINI(6, 'Pencarian produk dengan autocomplete dan koreksi salah ketik',
  'Pengguna aplikasi sering salah ketik ("kpoi", "mleati") dan tidak menemukan produk, sehingga penjualan hilang. Toko butuh kotak pencarian dengan saran otomatis dan koreksi ejaan tanpa layanan pihak ketiga.',
  ['Autocomplete berbasis trie, diurutkan dari produk terpopuler', 'Koreksi salah ketik dengan edit distance (Damerau-Levenshtein: hapus, sisip, ganti, tukar huruf)', 'Batas toleransi sesuai panjang kata', 'Pencarian multi-kata dengan saran "maksud Anda"', 'Hasil kosong ditangani dengan jelas'],
  ['Masukkan setiap nama produk ke trie beserta skor popularitas.', 'Untuk awalan, turun ke simpul awalan lalu kumpulkan semua kata di bawahnya, urutkan skor menurun.', 'Edit distance dengan tabel DP O(m x n); tukar dua huruf bersebelahan (kpoi -> kopi) dihitung satu langkah.', 'Kata pendek hanya boleh salah 1 huruf, kata panjang 2, agar tidak terlalu longgar.', 'Cocokkan semua kata hasil koreksi ke nama produk; tampilkan saran jika ada kata yang dikoreksi.'],
  CARI, 'python', run=True,
  kunci='tambahkan sinonim (susu = milk), pembobotan BM25, dan ukur waktu pencarian untuk 100.000 produk.',
  cek=q('Apa fungsi edit distance pada fitur pencarian?', ['Mengukur berapa huruf yang perlu diubah agar kata pengguna sama dengan kata di katalog, sehingga salah ketik bisa dikoreksi', 'Mengurutkan produk berdasarkan harga', 'Mengompresi teks'], 0, 'Levenshtein untuk toleransi typo.')),
]

# ---------------------------------------------------------------- BESAR
CATAT = r'''# Paket "catatku": pencatat keuangan UMKM yang siap rilis ke PyPI
# Struktur repositori
#   pyproject.toml   src/catatku/{__init__,model,repo,laporan,cli}.py   tests/   .github/workflows/ci.yml

# ---- pyproject.toml
[project]
name = "catatku"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = ["typer>=0.12", "pydantic>=2.7", "rich>=13"]
[project.scripts]
catatku = "catatku.cli:app"
[project.optional-dependencies]
dev = ["pytest>=8", "pytest-cov", "ruff", "mypy"]

# ---- src/catatku/model.py
from datetime import date
from decimal import Decimal
from enum import StrEnum
from pydantic import BaseModel, Field

class Jenis(StrEnum):
    MASUK = "masuk"
    KELUAR = "keluar"

class Transaksi(BaseModel):
    tanggal: date
    jenis: Jenis
    kategori: str = Field(min_length=2, max_length=40)
    jumlah: Decimal = Field(gt=0, decimal_places=0)
    catatan: str = ""

# ---- src/catatku/repo.py
import sqlite3
from contextlib import contextmanager
SKEMA = """CREATE TABLE IF NOT EXISTS transaksi (id INTEGER PRIMARY KEY, tanggal TEXT NOT NULL,
  jenis TEXT CHECK (jenis IN ('masuk','keluar')), kategori TEXT NOT NULL, jumlah INTEGER CHECK (jumlah > 0), catatan TEXT);
CREATE INDEX IF NOT EXISTS ix_tanggal ON transaksi(tanggal);"""

class Repo:
    def __init__(self, path):
        self.db = sqlite3.connect(path); self.db.executescript(SKEMA)
    @contextmanager
    def tx(self):
        with self.db: yield self.db                      # commit/rollback otomatis
    def tambah(self, t: Transaksi) -> int:
        with self.tx() as c:
            return c.execute("INSERT INTO transaksi (tanggal, jenis, kategori, jumlah, catatan) VALUES (?,?,?,?,?)",
                             (t.tanggal.isoformat(), t.jenis, t.kategori.lower(), int(t.jumlah), t.catatan)).lastrowid
    def per_bulan(self, tahun: int):
        return self.db.execute("""SELECT substr(tanggal,1,7) bln, SUM(CASE jenis WHEN 'masuk' THEN jumlah ELSE 0 END),
                                  SUM(CASE jenis WHEN 'keluar' THEN jumlah ELSE 0 END) FROM transaksi
                                  WHERE tanggal LIKE ? GROUP BY bln ORDER BY bln""", (f"{tahun}-%",)).fetchall()

# ---- src/catatku/laporan.py
PPH_FINAL_UMKM = Decimal("0.005")          # PP 55/2022: 0,5% dari omzet bruto, omzet s.d. Rp500 juta/tahun tidak dikenai
def pajak_tahunan(omzet_per_bulan: list[int]) -> list[tuple[int, int]]:
    kumulatif, hasil = 0, []
    for omzet in omzet_per_bulan:
        kena = max(0, min(omzet, kumulatif + omzet - 500_000_000))
        kumulatif += omzet
        hasil.append((omzet, int(Decimal(kena) * PPH_FINAL_UMKM)))
    return hasil

# ---- src/catatku/cli.py
import typer
from rich.table import Table
from rich.console import Console
app = typer.Typer(help="Pencatat keuangan UMKM")
@app.command()
def tambah(jenis: Jenis, kategori: str, jumlah: int, tanggal: str = typer.Option(date.today().isoformat())):
    t = Transaksi(tanggal=tanggal, jenis=jenis, kategori=kategori, jumlah=jumlah)
    typer.echo(f"tersimpan #{Repo('catatku.db').tambah(t)}")
@app.command()
def laporan(tahun: int):
    tabel = Table("Bulan", "Masuk", "Keluar", "Laba", "PPh final")
    rows = Repo("catatku.db").per_bulan(tahun)
    for (bln, m, k), (_, pph) in zip(rows, pajak_tahunan([m for _, m, _ in rows])):
        tabel.add_row(bln, f"{m:,}", f"{k:,}", f"{m - k:,}", f"{pph:,}")
    Console().print(tabel)

# ---- tests/test_laporan.py
def test_omzet_di_bawah_500_juta_tidak_kena_pajak():
    assert all(p == 0 for _, p in pajak_tahunan([40_000_000] * 12))
def test_hanya_kelebihan_500_juta_yang_kena():
    hasil = pajak_tahunan([100_000_000] * 6)
    assert [p for _, p in hasil] == [0, 0, 0, 0, 0, 500_000]
def test_transaksi_negatif_ditolak():
    with pytest.raises(ValidationError): Transaksi(tanggal="2026-01-01", jenis="masuk", kategori="jual", jumlah=-5)

# ---- .github/workflows/ci.yml
# jobs: test (matrix 3.11/3.12/3.13) -> ruff check -> mypy --strict src -> pytest --cov=catatku --cov-fail-under=85
#       release (tag v*) -> python -m build -> pypa/gh-action-pypi-publish (trusted publishing, tanpa token)'''

SEARCH = r'''# Mesin pencarian produk: inverted index + BM25 + koreksi typo, disajikan lewat FastAPI async dengan cache dan rate limit
# ---- app/index.py
import math, re, unicodedata
from collections import Counter, defaultdict

def token(teks: str) -> list[str]:
    teks = unicodedata.normalize("NFKD", teks.lower())
    return [t for t in re.findall(r"[a-z0-9]+", teks) if t not in STOPWORDS]
STOPWORDS = {"dan", "yang", "untuk", "di", "dengan", "isi"}
SINONIM = {"hp": "ponsel", "handphone": "ponsel", "milk": "susu"}

class Indeks:
    def __init__(self, k1=1.2, b=0.75):
        self.post = defaultdict(dict)          # token -> {doc_id: tf}
        self.panjang, self.doc, self.k1, self.b = {}, {}, k1, b
    def tambah(self, doc_id: int, judul: str, deskripsi: str, popularitas: float):
        tok = [SINONIM.get(t, t) for t in token(judul) * 3 + token(deskripsi)]   # judul diberi bobot 3x
        for t, tf in Counter(tok).items(): self.post[t][doc_id] = tf
        self.panjang[doc_id] = len(tok); self.doc[doc_id] = (judul, popularitas)
    def cari(self, q: str, k: int = 20) -> list[tuple[int, float]]:
        N, avg = len(self.doc), sum(self.panjang.values()) / len(self.doc)
        skor = Counter()
        for t in (SINONIM.get(x, x) for x in token(q)):
            t = t if t in self.post else koreksi(t, self.post.keys())
            if not t: continue
            df = len(self.post[t]); idf = math.log(1 + (N - df + 0.5) / (df + 0.5))
            for d, tf in self.post[t].items():
                skor[d] += idf * tf * (self.k1 + 1) / (tf + self.k1 * (1 - self.b + self.b * self.panjang[d] / avg))
        for d in skor: skor[d] *= 1 + 0.1 * math.log1p(self.doc[d][1])        # sedikit dorongan popularitas
        return skor.most_common(k)

# koreksi(): Levenshtein dibatasi 1-2 edit + kandidat dari BK-tree agar tidak membandingkan semua token

# ---- app/main.py
import asyncio, time
from fastapi import FastAPI, Query, Request, HTTPException
from cachetools import TTLCache

app = FastAPI(title="Search API")
INDEKS = Indeks(); CACHE = TTLCache(maxsize=10_000, ttl=60); EMBER: dict[str, list[float]] = {}

@app.on_event("startup")
async def muat():
    async for p in stream_produk_dari_db():            # batch 5.000 baris, tidak memuat semua sekaligus
        INDEKS.tambah(p.id, p.nama, p.deskripsi, p.terjual_30h)

def rate_limit(ip: str, maks=30, per=10.0):            # token bucket per IP
    sisa, t = EMBER.get(ip, [maks, time.monotonic()])
    sekarang = time.monotonic(); sisa = min(maks, sisa + (sekarang - t) * maks / per)
    if sisa < 1: raise HTTPException(429, "terlalu banyak permintaan")
    EMBER[ip] = [sisa - 1, sekarang]

@app.get("/cari")
async def cari(request: Request, q: str = Query(min_length=1, max_length=80), hal: int = Query(1, ge=1, le=50)):
    rate_limit(request.client.host)
    kunci = (q.lower().strip(), hal)
    if kunci not in CACHE:
        hasil = await asyncio.to_thread(INDEKS.cari, q, hal * 20)     # CPU-bound keluar dari event loop
        CACHE[kunci] = hasil[(hal - 1) * 20: hal * 20]
    return {"q": q, "hasil": [{"id": d, "judul": INDEKS.doc[d][0], "skor": round(s, 3)} for d, s in CACHE[kunci]]}

# ---- evaluasi kualitas (offline), dijalankan di CI setiap perubahan ranking
# 300 kueri nyata dari log + jawaban relevan berlabel -> NDCG@10, MRR, recall@20; gagal jika NDCG turun > 2 poin
# ---- beban: k6 200 VU, target p95 < 120 ms pada 500.000 produk; profil dengan py-spy bila melambat'''

PANGAN = r'''# Pipeline pemantau harga pangan harian: ambil -> validasi -> simpan -> deteksi anomali -> laporan
# Dijalankan terjadwal (cron/GitHub Actions/Airflow) pukul 10.00 WIB
# ---- pipeline/ambil.py
import asyncio, random
import httpx
from pydantic import BaseModel, Field, field_validator

class Harga(BaseModel):
    tanggal: str
    provinsi: str
    komoditas: str
    harga: int = Field(gt=0, lt=1_000_000)
    @field_validator("komoditas")
    @classmethod
    def kenal(cls, v):
        if v not in KOMODITAS: raise ValueError(f"komoditas tidak dikenal: {v}")
        return v

KOMODITAS = {"beras medium", "beras premium", "cabai merah", "bawang merah", "telur ayam", "minyak goreng", "gula pasir"}
SEM = asyncio.Semaphore(5)                                  # sopan ke server sumber

async def ambil(client: httpx.AsyncClient, prov: str, tanggal: str, coba=5) -> list[Harga]:
    for i in range(coba):
        try:
            async with SEM:
                r = await client.get(f"{SUMBER_API}/harga", params={"prov": prov, "tgl": tanggal}, timeout=15)
            if r.status_code == 429 or r.status_code >= 500: raise httpx.HTTPStatusError("retry", request=r.request, response=r)
            r.raise_for_status()
            return [Harga(**x) for x in r.json()["data"]]
        except (httpx.TransportError, httpx.HTTPStatusError):
            await asyncio.sleep(min(60, 2 ** i) + random.random())     # exponential backoff + jitter
    raise RuntimeError(f"gagal ambil {prov} setelah {coba} percobaan")

async def ambil_semua(tanggal):
    async with httpx.AsyncClient(headers={"User-Agent": "pemantau-harga/1.0"}) as c:
        hasil = await asyncio.gather(*(ambil(c, p, tanggal) for p in PROVINSI), return_exceptions=True)
    gagal = [p for p, h in zip(PROVINSI, hasil) if isinstance(h, Exception)]
    return [x for h in hasil if not isinstance(h, Exception) for x in h], gagal

# ---- pipeline/anomali.py
from statistics import median
def anomali(riwayat: list[int], hari_ini: int, k=3.5):
    """Modified z-score berbasis median & MAD: tahan outlier, cocok untuk harga yang melonjak musiman."""
    med = median(riwayat); mad = median(abs(x - med) for x in riwayat) or 1
    z = 0.6745 * (hari_ini - med) / mad
    return z if abs(z) > k else None

# ---- pipeline/dag.py  (urutan tugas = topological sort; tugas gagal menghentikan turunannya saja)
TUGAS = {"ambil": [], "validasi": ["ambil"], "simpan": ["validasi"], "anomali": ["simpan"],
         "laporan_pdf": ["anomali"], "notifikasi": ["anomali"], "dashboard": ["simpan"]}

# ---- pipeline/simpan.py: upsert idempoten (aman dijalankan ulang untuk tanggal yang sama)
UPSERT = """INSERT INTO harga (tanggal, provinsi, komoditas, harga) VALUES (?, ?, ?, ?)
            ON CONFLICT (tanggal, provinsi, komoditas) DO UPDATE SET harga = excluded.harga"""

# ---- keluaran
# 1. tabel harga per provinsi + perubahan vs minggu lalu, 2. daftar anomali (cabai merah Papua +38%, z=5.1)
# 3. notifikasi ke kanal tim jika ada anomali atau provinsi gagal diambil
# 4. data quality report: baris ditolak validasi, provinsi hilang, freshness (data terakhir < 26 jam)
# Etika & legal: patuhi robots.txt dan ketentuan sumber data, cantumkan atribusi, jangan membebani server.'''

FRAUD = r'''# Mesin deteksi fraud transaksi real-time untuk dompet digital
# Kafka topic "transaksi" -> konsumen Python (aiokafka) -> rule engine + fitur streaming -> skor -> keputusan < 50 ms
# ---- fraud/fitur.py : fitur streaming dengan sliding window per pengguna (disimpan di Redis di produksi)
from collections import deque, defaultdict
from dataclasses import dataclass

@dataclass(frozen=True)
class Trx:
    id: str; user: str; device: str; ip: str; jumlah: int; merchant: str; ts: float; lat: float; lon: float

class Jendela:
    def __init__(self, detik): self.detik, self.q = detik, defaultdict(deque)
    def tambah(self, kunci, t: Trx):
        q = self.q[kunci]; q.append(t)
        while q and q[0].ts <= t.ts - self.detik: q.popleft()
        return q

J5M, J24J = Jendela(300), Jendela(86_400)

# ---- fraud/graf.py : akun yang berbagi device/IP digabung dengan Union-Find (deteksi sindikat/akun ternak)
class UnionFind:
    def __init__(self): self.p, self.uk = {}, {}
    def cari(self, x):
        self.p.setdefault(x, x); self.uk.setdefault(x, 1)
        while self.p[x] != x: self.p[x] = self.p[self.p[x]]; x = self.p[x]     # path compression
        return x
    def gabung(self, a, b):
        a, b = self.cari(a), self.cari(b)
        if a == b: return
        if self.uk[a] < self.uk[b]: a, b = b, a
        self.p[b] = a; self.uk[a] += self.uk[b]
UF = UnionFind()

# ---- fraud/aturan.py : aturan sebagai data agar tim risk bisa mengubah tanpa deploy ulang
ATURAN = [
    ("VELOCITY", lambda t, f: f["n5m"] >= 5, 30),                         # >= 5 transaksi dalam 5 menit
    ("NOMINAL_TIDAK_WAJAR", lambda t, f: t.jumlah > 5 * max(f["median24j"], 50_000), 25),
    ("IMPOSSIBLE_TRAVEL", lambda t, f: f["kecepatan_kmh"] > 900, 40),       # pindah kota lebih cepat dari pesawat
    ("DEVICE_BARU_NOMINAL_BESAR", lambda t, f: f["device_baru"] and t.jumlah > 2_000_000, 25),
    ("SINDIKAT", lambda t, f: f["ukuran_cluster"] >= 10, 35),
]

def skor(t: Trx, f: dict) -> tuple[int, list[str]]:
    kena = [(n, b) for n, cek, b in ATURAN if cek(t, f)]
    return min(100, sum(b for _, b in kena)), [n for n, _ in kena]

def putuskan(s):                    # ambang dikalibrasi mingguan dari data berlabel (chargeback, laporan pengguna)
    return "TOLAK" if s >= 70 else "VERIFIKASI_OTP" if s >= 40 else "SETUJU"

# ---- fraud/antrean.py : kasus untuk analis diurutkan dengan heap (skor tertinggi, nominal terbesar dulu)
import heapq
ANTREAN: list[tuple[int, int, str]] = []
def ke_analis(t, s): heapq.heappush(ANTREAN, (-s, -t.jumlah, t.id))

# ---- evaluasi
# Data berlabel 90 hari: precision, recall, false positive rate per aturan; biaya = fraud lolos + pelanggan baik terganggu
# Shadow mode 2 minggu sebelum aturan baru aktif; A/B ambang; audit log setiap keputusan (siapa, aturan apa, skor)
# Kepatuhan: data pribadi diminimalkan (hash device/IP), retensi sesuai kebijakan, penjelasan keputusan bisa diaudit'''

LG_BESAR = [
BESAR(1, 'Paket CLI pencatat keuangan UMKM yang siap rilis',
  'Jutaan UMKM masih mencatat keuangan di buku tulis sehingga tidak tahu laba bulanan dan kewajiban PPh final 0,5%. Dibutuhkan alat baris perintah yang sederhana, datanya aman di laptop sendiri, dan dirilis sebagai paket Python profesional.',
  ['Model transaksi tervalidasi dengan Pydantic (tidak ada nominal negatif atau kategori kosong)', 'Penyimpanan SQLite dengan transaksi atomik dan indeks tanggal', 'Laporan bulanan: pemasukan, pengeluaran, laba, dan PPh final sesuai ambang omzet Rp500 juta', 'CLI dengan Typer dan tabel Rich; dapat dipasang dengan pip install', 'Test, linting, type check, dan rilis otomatis ke PyPI lewat CI'],
  'Python 3.12, Typer, Pydantic v2, SQLite, Rich, pytest, ruff, mypy, GitHub Actions, PyPI trusted publishing',
  [('Struktur', 'src layout, pyproject.toml (PEP 621), entry point catatku'), ('Domain', 'model.py (Pydantic), laporan.py (perhitungan pajak murni, mudah diuji)'),
   ('Data', 'repo.py: SQLite + context manager transaksi; migrasi skema berversi'), ('Antarmuka', 'cli.py: Typer, keluaran Rich, ekspor CSV'),
   ('Kualitas', 'pytest + coverage 85%, ruff, mypy --strict, pre-commit'), ('Rilis', 'tag versi -> build -> PyPI; semantic versioning dan CHANGELOG')],
  ['Tulis user story dan contoh perintah yang diinginkan pemilik UMKM.', 'Rancang model dan fungsi laporan sebagai fungsi murni, lalu tulis test lebih dulu untuk aturan pajak.', 'Bangun repositori SQLite dengan transaksi dan indeks; uji dengan basis data sementara.', 'Bangun CLI, uji alur dari awal sampai laporan, tambahkan ekspor CSV.', 'Siapkan CI, dokumentasi README, lalu rilis versi 1.0.0 ke PyPI.'],
  CATAT, 'python', standar='struktur paket standar (src layout, pyproject), logika bisnis berupa fungsi murni yang teruji, validasi input, transaksi database atomik, type check ketat, CI dan rilis otomatis yang dapat diulang',
  cek=q('Kenapa perhitungan pajak ditulis sebagai fungsi murni terpisah dari CLI dan database?', ['Agar mudah diuji dengan banyak kasus tanpa menyiapkan database atau terminal, dan bisa dipakai ulang di antarmuka lain', 'Karena Typer tidak bisa menghitung', 'Agar kodenya lebih panjang'], 0, 'Pisahkan logika murni dari I/O.')),
BESAR(2, 'Mesin pencarian produk dengan BM25 sebagai API',
  'Marketplace lokal dengan 500.000 produk memakai pencarian LIKE di database: lambat, tidak toleran typo, dan hasilnya tidak relevan. Tim butuh layanan pencarian sendiri yang cepat dan kualitasnya bisa diukur.',
  ['Inverted index dengan tokenisasi, stopword, dan sinonim', 'Ranking BM25 dengan bobot judul dan dorongan popularitas', 'Koreksi typo dengan edit distance yang dibatasi', 'API FastAPI async dengan cache TTL dan rate limit token bucket', 'Evaluasi offline NDCG/MRR di CI dan uji beban p95 < 120 ms'],
  'Python 3.12, FastAPI, Uvicorn, Pydantic, cachetools, PostgreSQL (sumber), k6, py-spy',
  [('Indeks', 'posting list token -> {doc: tf}; dibangun streaming dari database saat startup, dibangun ulang tiap malam'), ('Ranking', 'BM25 (k1=1,2, b=0,75), judul bobot 3x, log popularitas'),
   ('Toleransi', 'normalisasi Unicode, sinonim, Levenshtein <= 2 dengan BK-tree'), ('API', '/cari dengan validasi query, pagination, cache 60 detik, 429 saat melewati limit'),
   ('Kualitas', 'set kueri berlabel; NDCG@10, MRR, recall@20 sebagai gate CI'), ('Kinerja', 'CPU-bound dipindah ke thread, profil py-spy, target p95')],
  ['Kumpulkan 300 kueri nyata dari log dan beri label hasil yang relevan.', 'Bangun inverted index dan BM25; ukur NDCG sebagai baseline.', 'Tambahkan sinonim, bobot judul, koreksi typo; pertahankan hanya yang menaikkan metrik.', 'Bungkus sebagai API dengan cache dan rate limit; uji beban dengan k6.', 'Rilis bertahap (10% trafik) dan bandingkan konversi dengan pencarian lama.'],
  SEARCH, 'python', standar='relevansi diukur dengan metrik offline yang menjadi gerbang CI, latensi p95 terukur di bawah target, API terlindungi rate limit, perubahan ranking dirilis bertahap dengan A/B',
  cek=q('Kenapa perubahan ranking diuji dengan NDCG pada kueri berlabel sebelum dirilis?', ['Agar perbaikan untuk satu kueri tidak diam-diam merusak relevansi kueri lain; metrik memberi bukti objektif', 'Karena FastAPI mewajibkannya', 'Agar indeks lebih kecil'], 0, 'Kualitas pencarian harus terukur.')),
BESAR(3, 'Pipeline pemantau harga pangan harian',
  'Dinas ketahanan pangan dan pedagang butuh peringatan dini saat harga cabai, bawang, atau beras melonjak di suatu provinsi. Data tersebar di banyak sumber, sering terlambat, dan pengambilan manual memakan waktu berjam-jam.',
  ['Pengambilan data paralel yang sopan (semaphore) dengan retry, exponential backoff, dan jitter', 'Validasi setiap baris dengan Pydantic; baris rusak dilaporkan, bukan disimpan', 'Penyimpanan idempoten (upsert) agar aman dijalankan ulang', 'Deteksi anomali dengan modified z-score berbasis median', 'Orkestrasi berbentuk DAG, laporan harian, notifikasi, dan data quality report'],
  'Python 3.12, asyncio, httpx, Pydantic, PostgreSQL/SQLite, Airflow atau GitHub Actions cron, Metabase',
  [('Ingest', 'httpx AsyncClient, Semaphore(5), backoff + jitter, User-Agent jelas'), ('Validasi', 'Pydantic: komoditas dikenal, rentang harga wajar, tanggal valid'),
   ('Storage', 'tabel harga dengan kunci unik (tanggal, provinsi, komoditas), upsert'), ('Analitik', 'median & MAD 30 hari, modified z-score > 3,5 = anomali'),
   ('Orkestrasi', 'DAG: ambil -> validasi -> simpan -> anomali -> laporan/notifikasi/dashboard'), ('Observability', 'freshness, jumlah baris, provinsi gagal, durasi tiap tugas')],
  ['Petakan sumber data, ketentuan penggunaannya, dan jadwal pembaruannya.', 'Bangun pengambil async dengan retry; uji dengan server tiruan yang sengaja gagal.', 'Tambahkan validasi dan upsert; jalankan dua kali untuk membuktikan idempoten.', 'Kalibrasi ambang anomali dengan data historis bersama ahli pangan.', 'Jadwalkan pipeline, buat dashboard dan notifikasi, lalu pantau kualitas datanya.'],
  PANGAN, 'python', standar='pengambilan data sopan dan legal, idempoten, validasi eksplisit, anomali dengan statistik yang tahan outlier, observability kualitas data, dan dokumentasi sumber',
  cek=q('Kenapa penyimpanan dibuat idempoten dengan upsert?', ['Agar pipeline bisa dijalankan ulang untuk tanggal yang sama setelah gagal tanpa membuat data ganda', 'Agar query lebih cepat', 'Karena SQLite tidak mendukung INSERT biasa'], 0, 'Idempotensi membuat pemulihan aman.')),
BESAR(4, 'Mesin deteksi fraud transaksi real-time',
  'Dompet digital kehilangan ratusan juta rupiah per bulan karena akun curian, akun ternak promo, dan transaksi tidak wajar. Keputusan setuju/tolak harus diambil dalam puluhan milidetik tanpa mengganggu pengguna jujur.',
  ['Fitur streaming per pengguna dengan sliding window (5 menit, 24 jam)', 'Deteksi sindikat akun yang berbagi device/IP dengan Union-Find', 'Rule engine berbasis data dengan skor dan keputusan bertingkat (setuju, OTP, tolak)', 'Antrean kasus untuk analis dengan priority queue', 'Evaluasi precision/recall, shadow mode, dan audit log'],
  'Python 3.12, aiokafka, Redis, PostgreSQL, Prometheus/Grafana, pandas untuk evaluasi offline',
  [('Streaming', 'konsumen Kafka async; state jendela di Redis dengan TTL'), ('Fitur', 'velocity, median nominal 24 jam, kecepatan perpindahan lokasi, device baru'),
   ('Graph', 'Union-Find dengan path compression dan union by size untuk cluster akun'), ('Aturan', 'daftar aturan sebagai data, bobot skor, ambang dikalibrasi mingguan'),
   ('Operasional', 'heap kasus untuk analis, SLA tinjauan, umpan balik label ke evaluasi'), ('Tata kelola', 'shadow mode, A/B ambang, audit log, minimisasi data pribadi')],
  ['Kumpulkan data berlabel (chargeback, laporan pengguna) dan definisikan biaya salah tolak vs fraud lolos.', 'Bangun fitur jendela dan Union-Find; uji dengan data replay.', 'Tulis aturan awal bersama tim risk, ukur precision/recall per aturan.', 'Jalankan shadow mode dua minggu, kalibrasi ambang, lalu aktifkan bertahap.', 'Pantau metrik harian, tinjau kasus, dan perbarui aturan dari temuan analis.'],
  FRAUD, 'python', standar='latensi keputusan di bawah target, setiap keputusan dapat dijelaskan dan diaudit, aturan diukur dengan data berlabel, rilis lewat shadow mode, dan data pribadi diminimalkan',
  cek=q('Kenapa aturan fraud baru dijalankan dalam shadow mode sebelum aktif?', ['Untuk mengukur berapa transaksi jujur yang akan ikut ditolak dan berapa fraud yang tertangkap, tanpa mengganggu pengguna', 'Agar aturan lebih cepat', 'Karena Kafka mewajibkannya'], 0, 'Ukur dampak sebelum memblokir.')),
]

PJ_LOGIKA = JALUR_M('Logika, Python & Algoritma', 'Menengah',
  'Enam proyek mini Python yang dijalankan (validator data pelanggan, kasir dengan stok dan PPN, penjadwal ujian graph coloring, rute kurir Dijkstra + 2-opt, analisis log dan deteksi anomali, pencarian dengan autocomplete dan koreksi typo) dan empat proyek besar berskala industri 2026-2027 (paket CLI keuangan UMKM yang dirilis ke PyPI, mesin pencarian BM25 sebagai API, pipeline pemantau harga pangan, mesin deteksi fraud real-time), lengkap dengan penyelesaiannya.',
  ['Validasi data', 'OOP & exception', 'Graph & DSA', 'Generator & streaming', 'Paket & API'], LG_MINI, LG_BESAR)
