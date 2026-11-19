"""Pendalaman jalur Python (bagian 2: file & error, modul, OOP, Python idiomatik). Contoh dijalankan dengan CPython 3.13."""
K = 'python'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Pemrosesan File': dict(
  ist=[('File mode', "'r' baca, 'w' tulis (menimpa), 'a' tambah di akhir, 'x' buat baru dan gagal jika sudah ada, 'b' biner."),
       ('Encoding', 'Selalu tulis encoding="utf-8" agar file sama di Windows, macOS, dan Linux.'),
       ('CSV', 'Format tabel teks; modul csv menangani koma di dalam tanda kutip dengan benar.'),
       ('Atomic write', 'Menulis ke file sementara lalu mengganti nama, agar file tidak setengah jadi saat program gagal.')],
  cx=[P('Menulis dan membaca CSV laporan penjualan', '''
import csv, os, tempfile
with tempfile.TemporaryDirectory() as d:
    path = os.path.join(d, "penjualan.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["tanggal", "produk", "qty", "harga"])
        w.writerows([["2026-11-01", "Kopi, gula aren", 3, 22000], ["2026-11-01", "Teh", 5, 12000],
                     ["2026-11-02", "Kopi, gula aren", 4, 22000]])
    with open(path, encoding="utf-8") as f:
        baris = list(csv.DictReader(f))
    total = sum(int(b["qty"]) * int(b["harga"]) for b in baris)
    print(len(baris), "baris; produk pertama:", baris[0]["produk"])
    print(f"omzet: Rp{total:,}".replace(",", "."))

    tmp = path + ".tmp"                                   # atomic write
    with open(tmp, "w", encoding="utf-8") as f: f.write("ringkasan siap\\n")
    os.replace(tmp, os.path.join(d, "ringkasan.txt"))
    print(sorted(os.listdir(d)))
''', '"Kopi, gula aren" mengandung koma. Memecah baris dengan split(",") akan merusak kolomnya, sedangkan modul csv menanganinya dengan benar.')]),

'Membaca file baris demi baris': dict(
  ist=[('Streaming', 'Memproses file per baris tanpa memuat seluruhnya ke memori; wajib untuk file log berukuran GB.'),
       ('Lazy iteration', 'Objek file adalah iterator; for baris in f membaca satu baris setiap kali.'),
       ('rstrip("\\n")', 'Membuang karakter baris baru di akhir setiap baris.'),
       ('Log parsing', 'Mengambil informasi (waktu, level, pesan) dari baris log untuk dihitung.')],
  cx=[P('Menghitung status HTTP dari access log tanpa memuat semua', '''
import io
from collections import Counter
LOG = io.StringIO("""10.0.0.1 - - [19/Nov/2026:10:00:01] "GET /produk HTTP/1.1" 200 512
10.0.0.2 - - [19/Nov/2026:10:00:02] "POST /checkout HTTP/1.1" 500 87
10.0.0.1 - - [19/Nov/2026:10:00:05] "GET /produk/7 HTTP/1.1" 404 12
10.0.0.3 - - [19/Nov/2026:10:00:09] "GET /produk HTTP/1.1" 200 498
10.0.0.2 - - [19/Nov/2026:10:00:11] "POST /checkout HTTP/1.1" 500 91
""")
status, error_path = Counter(), Counter()
for no, baris in enumerate(LOG, 1):        # di file nyata: with open("access.log") as LOG
    bagian = baris.rstrip("\\n").split()
    kode, path = int(bagian[-2]), bagian[5]
    status[kode] += 1
    if kode >= 500: error_path[path] += 1
print("status:", dict(status))
print("endpoint error 5xx:", error_path.most_common())
''', 'io.StringIO meniru file di memori. Kodenya sama persis untuk file sungguhan karena keduanya bisa dibaca per baris.')]),

'Menangani error (exception)': dict(
  ist=[('Exception', 'Objek yang dilempar saat terjadi kesalahan; jika tidak ditangkap, program berhenti dengan traceback.'),
       ('Specific except', 'Tangkap jenis error yang spesifik (ValueError, KeyError), bukan except: kosong.'),
       ('EAFP', '"Easier to Ask Forgiveness than Permission": coba dulu, tangani error. Gaya umum di Python.'),
       ('Traceback', 'Jejak pemanggilan fungsi sampai titik error; dibaca dari bawah ke atas.')],
  cx=[P('Impor data dengan error yang ditangani per baris', '''
data = ["12500", "8.000", "", "abc", "15000", None]
valid, ditolak = [], []
for i, x in enumerate(data, 1):
    try:
        valid.append(int(x))
    except ValueError as e:
        ditolak.append((i, f"format salah: {e}"))
    except TypeError:
        ditolak.append((i, "nilai kosong (None)"))
print("valid:", valid)
for i, alasan in ditolak: print(f"  baris {i}: {alasan}")

harga = {"kopi": 18000}
try:
    print(harga["teh"])
except KeyError as e:
    print("produk tidak ada:", e)
''', 'Satu baris rusak tidak boleh menggagalkan impor ribuan baris. Baris yang ditolak dicatat beserta alasannya untuk diperbaiki.')]),

'raise, exception buatan sendiri & else/finally': dict(
  ist=[('Custom exception', 'Kelas error milik domain sendiri, misalnya SaldoTidakCukup, turunan dari Exception.'),
       ('Exception hierarchy', 'Error domain diturunkan dari satu kelas dasar agar bisa ditangkap bersama.'),
       ('raise ... from', 'Merangkai error asli sebagai penyebab (__cause__) agar jejaknya tidak hilang.'),
       ('try/except/else/finally', 'else jalan jika tidak ada error; finally selalu jalan, untuk membersihkan sumber daya.')],
  cx=[P('Error domain untuk dompet digital', '''
class DompetError(Exception): pass
class SaldoTidakCukup(DompetError):
    def __init__(self, saldo, diminta):
        super().__init__(f"saldo {saldo:,} kurang dari {diminta:,}".replace(",", "."))
        self.kurang = diminta - saldo
class AkunDibekukan(DompetError): pass

def bayar(akun, jumlah):
    if akun["beku"]: raise AkunDibekukan(akun["id"])
    if akun["saldo"] < jumlah: raise SaldoTidakCukup(akun["saldo"], jumlah)
    akun["saldo"] -= jumlah

for akun, jml in [({"id": "A1", "saldo": 50_000, "beku": False}, 20_000),
                  ({"id": "A2", "saldo": 10_000, "beku": False}, 35_000),
                  ({"id": "A3", "saldo": 99_000, "beku": True}, 1_000)]:
    try:
        bayar(akun, jml)
    except SaldoTidakCukup as e:
        print(akun["id"], "gagal:", e, "| kurang", e.kurang)
    except DompetError as e:
        print(akun["id"], "ditolak:", type(e).__name__)
    else:
        print(akun["id"], "berhasil, sisa", akun["saldo"])
    finally:
        print("   (audit log ditulis)")

try:
    try: int("x")
    except ValueError as e: raise DompetError("format nominal salah") from e
except DompetError as e:
    print("penyebab asli:", repr(e.__cause__))
''')]),

'Context manager: with': dict(
  ist=[('Context manager', 'Objek dengan __enter__ dan __exit__ yang menjamin sumber daya dibersihkan.'),
       ('Resource leak', 'File, koneksi, atau lock yang tidak ditutup sehingga menumpuk dan membuat sistem gagal.'),
       ('contextlib.contextmanager', 'Membuat context manager dari fungsi generator dengan satu yield.'),
       ('Transaction', 'Pola with: commit jika berhasil, rollback jika ada error.')],
  cx=[P('Transaksi database dan pengukur waktu dengan with', '''
import sqlite3, time
from contextlib import contextmanager

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE rekening (id TEXT PRIMARY KEY, saldo INT CHECK (saldo >= 0))")
db.executemany("INSERT INTO rekening VALUES (?, ?)", [("A", 100), ("B", 50)]); db.commit()

def transfer(dari, ke, n):
    try:
        with db:                      # commit jika sukses, rollback jika error
            db.execute("UPDATE rekening SET saldo = saldo + ? WHERE id = ?", (n, ke))
            db.execute("UPDATE rekening SET saldo = saldo - ? WHERE id = ?", (n, dari))
        print(f"transfer {n} {dari}->{ke} OK")
    except sqlite3.IntegrityError:
        print(f"transfer {n} {dari}->{ke} DIBATALKAN (saldo tidak cukup)")

transfer("A", "B", 30); transfer("B", "A", 500)
print(db.execute("SELECT * FROM rekening").fetchall())

@contextmanager
def ukur(nama):
    t0 = time.perf_counter()
    try: yield
    finally: print(f"{nama} selesai ({'<1' if time.perf_counter() - t0 < 1 else '>=1'} detik)")
with ukur("laporan"):
    sum(range(100_000))
''', 'Pada transfer kedua, B sudah ditambah 500 sebelum A gagal dikurangi. Rollback dari with membatalkan keduanya sehingga uang tidak tercipta dari udara.')]),

'pathlib & modul glob': dict(
  ist=[('pathlib.Path', 'Objek path lintas OS; operator / menggabungkan path.'),
       ('glob / rglob', 'Mencari file dengan pola: *.csv di satu folder, **/*.csv rekursif.'),
       ('stem / suffix', 'Nama file tanpa ekstensi dan ekstensinya.'),
       ('Path traversal', 'Serangan memakai ../ untuk keluar dari folder yang diizinkan; periksa dengan resolve() dan is_relative_to().')],
  cx=[P('Merapikan folder unduhan dan mencegah path traversal', '''
import tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    for n in ["laporan_jan.csv", "laporan_feb.csv", "foto.JPG", "catatan.txt", "arsip/2025/laporan_des.csv"]:
        (root / n).parent.mkdir(parents=True, exist_ok=True); (root / n).write_text("x")
    print("csv di root   :", sorted(p.name for p in root.glob("*.csv")))
    print("csv rekursif  :", sorted(str(p.relative_to(root)) for p in root.rglob("*.csv")))
    print("per ekstensi  :", sorted({p.suffix.lower() for p in root.rglob("*") if p.is_file()}))

    unggahan = root / "unggahan"; unggahan.mkdir()
    for nama in ["cv.pdf", "../../etc/passwd"]:
        tujuan = (unggahan / nama).resolve()
        print(f"{nama:<18} aman: {tujuan.is_relative_to(unggahan.resolve())}")
''', 'Nama file dari pengguna tidak boleh langsung dipakai sebagai path. Selalu resolve() lalu pastikan masih di dalam folder unggahan.')]),

'Import & modul buatan sendiri': dict(
  ist=[('Module', 'Satu berkas .py yang bisa diimpor.'),
       ('Package', 'Folder berisi modul, biasanya dengan __init__.py.'),
       ('Absolute vs relative import', 'from toko.harga import ppn vs from .harga import ppn di dalam paket.'),
       ('Circular import', 'Dua modul saling mengimpor sehingga salah satunya belum selesai dimuat; atasi dengan memindah kode bersama.')],
  cx=[P('Membuat paket kecil lalu mengimpornya', '''
import sys, tempfile, importlib
from pathlib import Path
d = Path(tempfile.mkdtemp())
(d / "toko").mkdir()
(d / "toko/__init__.py").write_text('from .harga import total_ppn\\n__all__ = ["total_ppn"]\\n')
(d / "toko/harga.py").write_text('PPN = 0.11\\ndef total_ppn(x):\\n    return round(x * (1 + PPN))\\n')
sys.path.insert(0, str(d))
import toko
from toko.harga import PPN
print("total:", toko.total_ppn(100_000), "| PPN:", PPN)
print("toko adalah paket:", hasattr(toko, "__path__"), "| modul dimuat sekali:", "toko.harga" in sys.modules)
sys.path.remove(str(d))
''', 'Struktur nyata: folder src/toko/ dengan __init__.py, lalu dipasang dengan pip install -e . agar import bekerja dari mana saja.')]),

'Modul bawaan yang sering dipakai': dict(
  ist=[('Standard library', '"Batteries included": ratusan modul bawaan tanpa perlu pip install.'),
       ('datetime / zoneinfo', 'Tanggal, waktu, dan zona waktu (Asia/Jakarta, Asia/Makassar, Asia/Jayapura).'),
       ('json', 'Serialisasi data ke teks JSON untuk API dan konfigurasi.'),
       ('statistics', 'Rata-rata, median, simpangan baku tanpa pustaka tambahan.')],
  cx=[P('Zona waktu Indonesia, JSON, dan statistik', '''
import json, statistics
from datetime import datetime
from zoneinfo import ZoneInfo
rapat = datetime(2026, 11, 19, 9, 0, tzinfo=ZoneInfo("Asia/Jakarta"))
for kota, zona in [("Jakarta", "Asia/Jakarta"), ("Makassar", "Asia/Makassar"), ("Jayapura", "Asia/Jayapura")]:
    print(f"{kota:<9} {rapat.astimezone(ZoneInfo(zona)):%H:%M %Z}")

pesanan = {"id": 17, "total": 125000, "dibuat": rapat.isoformat()}
teks = json.dumps(pesanan); print("JSON:", teks)
print("kembali:", json.loads(teks)["total"])

waktu_respon = [120, 135, 128, 900, 131, 125]
print("mean", round(statistics.mean(waktu_respon)), "| median", statistics.median(waktu_respon))
''', 'Median lebih jujur daripada rata-rata untuk waktu respons karena satu request lambat (900 ms) tidak menyeret nilainya.')]),

'pip, PyPI & virtual environment': dict(
  ist=[('PyPI', 'Python Package Index: gudang paket publik yang dipasang dengan pip.'),
       ('Virtual environment', 'Folder Python terisolasi per proyek (python -m venv .venv) agar versi paket tidak bentrok.'),
       ('Pinning', 'Mengunci versi persis (requests==2.32.3) agar build bisa diulang.'),
       ('Supply chain attack', 'Paket palsu atau typosquatting (reqeusts) yang berisi malware; periksa nama dan sumber paket.')],
  cx=[T('Alur kerja harian dengan venv dan pip', '''
$ python -m venv .venv                 # buat lingkungan terisolasi
$ source .venv/bin/activate            # Windows: .venv\\Scripts\\activate
(.venv) $ pip install "requests>=2.32,<3" pandas
(.venv) $ pip freeze > requirements.txt   # kunci versi persis
(.venv) $ pip list --outdated            # cek paket yang perlu diperbarui
(.venv) $ pip-audit                      # cek kerentanan keamanan (CVE)
(.venv) $ deactivate

# di komputer/server lain
$ python -m venv .venv && source .venv/bin/activate
(.venv) $ pip install -r requirements.txt

# .gitignore
.venv/'''),
     P('Membaca versi paket yang terpasang dari kode', '''
from importlib.metadata import version, PackageNotFoundError
for paket in ["pip", "paket-yang-tidak-ada"]:
    try:
        print(paket, "terpasang:", bool(version(paket)))
    except PackageNotFoundError:
        print(paket, "belum terpasang -> pip install", paket)
''')]),

'pyproject.toml, Poetry, pipenv, PDM, Conda, pyenv': dict(
  ist=[('pyproject.toml', 'Berkas standar (PEP 518/621) untuk metadata proyek, dependensi, dan konfigurasi alat.'),
       ('Lock file', 'Daftar versi persis seluruh dependensi termasuk turunan (poetry.lock, uv.lock) agar build identik.'),
       ('uv', 'Pengelola paket dan proyek berbasis Rust yang sangat cepat; makin banyak dipakai sejak 2024.'),
       ('pyenv / Conda', 'pyenv mengelola banyak versi Python; Conda juga mengelola pustaka non-Python (umum di data science).')],
  cx=[P('Membaca pyproject.toml dengan tomllib', '''
import tomllib
teks = """
[project]
name = "kasir-toko"
version = "1.4.0"
requires-python = ">=3.11"
dependencies = ["fastapi>=0.115", "sqlalchemy>=2.0", "pydantic>=2.7"]

[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.6", "mypy>=1.11"]

[tool.ruff]
line-length = 100
"""
cfg = tomllib.loads(teks)
p = cfg["project"]
print(p["name"], p["version"], "| Python", p["requires-python"])
print("runtime:", [d.split(">")[0] for d in p["dependencies"]])
print("dev    :", [d.split(">")[0] for d in p["optional-dependencies"]["dev"]])
print("ruff line-length:", cfg["tool"]["ruff"]["line-length"])
''', 'Satu pyproject.toml menggantikan setup.py, requirements-dev.txt, dan berbagai berkas konfigurasi alat.'),
     T('Perbandingan singkat alat 2026', '''
Alat     Kelola paket  Lock file    Kelola versi Python  Cocok untuk
pip+venv ya            manual       tidak                skrip sederhana, belajar
uv       ya            uv.lock      ya                   proyek baru, CI cepat
Poetry   ya            poetry.lock  tidak                aplikasi dan library
PDM      ya            pdm.lock     tidak                proyek berbasis standar PEP
pipenv   ya            Pipfile.lock tidak                proyek lama
Conda    ya (+non-Py)  environment  ya                   data science, CUDA, GDAL
pyenv    tidak         -            ya                   banyak versi Python di satu laptop''')]),

'Kelas & Objek': dict(
  ist=[('Class', 'Cetak biru yang mendefinisikan data (atribut) dan perilaku (method).'),
       ('Instance', 'Objek nyata hasil kelas; setiap instance punya datanya sendiri.'),
       ('Domain model', 'Kelas yang mewakili konsep bisnis: Pesanan, Pelanggan, Produk.'),
       ('Cohesion', 'Data dan perilaku yang berhubungan dikumpulkan di kelas yang sama.')],
  cx=[P('Model domain keranjang belanja', '''
class Keranjang:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.item = {}

    def tambah(self, sku, harga, qty=1):
        h, q = self.item.get(sku, (harga, 0))
        self.item[sku] = (harga, q + qty)

    def total(self):
        return sum(h * q for h, q in self.item.values())

a, b = Keranjang("Sari"), Keranjang("Doni")
a.tambah("KOPI-250", 45_000, 2); a.tambah("KOPI-250", 45_000); a.tambah("GULA-1", 18_000)
b.tambah("TEH-100", 22_000)
print(a.pelanggan, a.item, a.total())
print(b.pelanggan, b.total(), "| objek terpisah:", a.item is not b.item)
''')]),

'Kelas, konstruktor, objek': dict(
  ist=[('__init__', 'Method yang dijalankan saat objek dibuat; mengisi atribut awal.'),
       ('self', 'Referensi ke objek itu sendiri, parameter pertama setiap method instance.'),
       ('Class attribute', 'Atribut milik kelas, dipakai bersama semua instance.'),
       ('Alternative constructor', '@classmethod seperti dari_csv() atau dari_dict() sebagai cara lain membuat objek.')],
  cx=[P('Konstruktor dengan validasi dan alternative constructor', '''
class Produk:
    jumlah_dibuat = 0                         # atribut kelas

    def __init__(self, sku, nama, harga):
        if harga <= 0: raise ValueError("harga harus positif")
        self.sku, self.nama, self.harga = sku, nama, harga
        Produk.jumlah_dibuat += 1

    @classmethod
    def dari_csv(cls, baris):
        sku, nama, harga = baris.split(";")
        return cls(sku, nama.strip(), int(harga))

p1 = Produk("KP-01", "Kopi Gayo", 85_000)
p2 = Produk.dari_csv("TH-02; Teh Melati ;24000")
print(p1.nama, p1.harga, "|", p2.nama, p2.harga)
try:
    Produk("X", "Gratis", 0)
except ValueError as e:
    print("ditolak:", e)
print("produk dibuat:", Produk.jumlah_dibuat)
''', 'Validasi di konstruktor menjamin tidak pernah ada objek Produk dengan harga tidak sah di mana pun di sistem.')]),

'Method & enkapsulasi': dict(
  ist=[('Encapsulation', 'Menyembunyikan detail internal; pengguna objek hanya memakai method publik.'),
       ('_protected / __private', 'Konvensi: satu garis bawah = internal; dua garis bawah = name mangling.'),
       ('Invariant', 'Aturan yang harus selalu benar pada objek, misalnya saldo tidak negatif.'),
       ('Tell, don\'t ask', 'Suruh objek melakukan sesuatu (rek.tarik(50)) daripada mengambil datanya lalu mengubah dari luar.')],
  cx=[P('Rekening yang menjaga invariant-nya sendiri', '''
class Rekening:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self._saldo = saldo
        self._riwayat = []

    def setor(self, n):
        if n <= 0: raise ValueError("setoran harus positif")
        self._saldo += n; self._riwayat.append(("setor", n))

    def tarik(self, n):
        if n > self._saldo: raise ValueError("saldo tidak cukup")
        self._saldo -= n; self._riwayat.append(("tarik", n))

    def saldo(self):
        return self._saldo

    def mutasi(self):
        return list(self._riwayat)              # salinan, bukan list internal

r = Rekening("Rina", 100_000)
r.setor(50_000); r.tarik(30_000)
try: r.tarik(1_000_000)
except ValueError as e: print("ditolak:", e)
m = r.mutasi(); m.clear()                       # tidak merusak riwayat asli
print("saldo:", r.saldo(), "| riwayat:", r.mutasi())
''')]),

'Enkapsulasi: property & dataclass': dict(
  ist=[('@property', 'Method yang diakses seperti atribut; bisa diberi setter dengan validasi.'),
       ('@dataclass', 'Membuat __init__, __repr__, __eq__ otomatis untuk kelas yang terutama menyimpan data.'),
       ('frozen=True', 'Dataclass immutable; cocok untuk value object seperti Uang atau Alamat.'),
       ('Value object', 'Objek yang dibandingkan dari nilainya, bukan identitasnya.')],
  cx=[P('Value object Uang dan property dengan validasi', '''
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Uang:
    nilai: int
    mata_uang: str = "IDR"
    def __add__(self, o):
        if o.mata_uang != self.mata_uang: raise ValueError("mata uang berbeda")
        return Uang(self.nilai + o.nilai, self.mata_uang)

@dataclass
class Karyawan:
    nama: str
    _gaji: int = field(repr=False)
    @property
    def gaji(self): return self._gaji
    @gaji.setter
    def gaji(self, v):
        if v < 3_500_000: raise ValueError("di bawah UMK")
        self._gaji = v

print(Uang(10_000) + Uang(2_500), "| sama nilai:", Uang(5) == Uang(5))
k = Karyawan("Agus", 5_000_000); print(k)
try: k.gaji = 2_000_000
except ValueError as e: print("ditolak:", e)
try: Uang(1).nilai = 2
except Exception as e: print("frozen:", type(e).__name__)
''')]),

'Dunder method: membuat objek terasa bawaan': dict(
  ist=[('Dunder (double underscore)', 'Method khusus seperti __len__, __eq__, __lt__ yang dipanggil oleh sintaks bawaan.'),
       ('__repr__ vs __str__', '__repr__ untuk developer (debug, jelas), __str__ untuk pengguna (rapi).'),
       ('Data model', 'Protokol Python yang membuat objek sendiri bisa dipakai dengan len, in, for, sorted, +.'),
       ('functools.total_ordering', 'Cukup definisikan __eq__ dan __lt__; perbandingan lain dibuat otomatis.')],
  cx=[P('Kelas Playlist yang terasa seperti tipe bawaan', '''
from functools import total_ordering

@total_ordering
class Lagu:
    def __init__(self, judul, detik): self.judul, self.detik = judul, detik
    def __repr__(self): return f"Lagu({self.judul!r}, {self.detik})"
    def __str__(self): return f"{self.judul} ({self.detik // 60}:{self.detik % 60:02d})"
    def __eq__(self, o): return self.detik == o.detik
    def __lt__(self, o): return self.detik < o.detik

class Playlist:
    def __init__(self, *lagu): self._lagu = list(lagu)
    def __len__(self): return len(self._lagu)
    def __iter__(self): return iter(self._lagu)
    def __contains__(self, judul): return any(l.judul == judul for l in self._lagu)
    def __add__(self, o): return Playlist(*self._lagu, *o._lagu)

a = Playlist(Lagu("Pagi", 215), Lagu("Senja", 187))
b = Playlist(Lagu("Hujan", 242))
semua = a + b
print(len(semua), "lagu |", "Senja" in semua, "|", [str(l) for l in sorted(semua)])
print(repr(max(semua)), "| Lagu A >= Lagu B:", Lagu("A", 200) >= Lagu("B", 100))
''')]),

'Pewarisan & Kelas Abstrak': dict(
  ist=[('Inheritance', 'Kelas anak mewarisi atribut dan method kelas induk.'),
       ('ABC / @abstractmethod', 'Kelas abstrak mendefinisikan kontrak yang wajib diimplementasikan anak.'),
       ('Template method pattern', 'Induk mengatur alur, anak mengisi langkah tertentu.'),
       ('Composition over inheritance', 'Sering lebih fleksibel memasukkan objek lain sebagai atribut daripada menurunkan kelas.')],
  cx=[P('Kontrak metode pembayaran dengan ABC', '''
from abc import ABC, abstractmethod

class MetodeBayar(ABC):
    def proses(self, jumlah):                   # template method
        if jumlah <= 0: return "nominal tidak valid"
        return f"{type(self).__name__}: {self._bayar(jumlah)} (biaya {self.biaya(jumlah):,})".replace(",", ".")
    @abstractmethod
    def _bayar(self, jumlah): ...
    def biaya(self, jumlah): return 0

class QRIS(MetodeBayar):
    def _bayar(self, j): return f"scan QR Rp{j:,}"
    def biaya(self, j): return round(j * 0.007)          # MDR 0,7%

class VirtualAccount(MetodeBayar):
    def _bayar(self, j): return "VA 8808 0812 3456 78"
    def biaya(self, j): return 4_000

for m in [QRIS(), VirtualAccount()]: print(m.proses(250_000))
try: MetodeBayar()
except TypeError as e: print("kelas abstrak tidak bisa dibuat:", "abstract" in str(e))
''')]),

'Pewarisan & override': dict(
  ist=[('Override', 'Kelas anak mengganti implementasi method induk.'),
       ('super()', 'Memanggil method induk dari kelas anak, misalnya untuk menambah perilaku.'),
       ('MRO', 'Method Resolution Order: urutan pencarian method pada pewarisan berganda (Kelas.__mro__).'),
       ('Liskov Substitution', 'Objek anak harus bisa menggantikan induk tanpa merusak program.')],
  cx=[P('Perhitungan gaji per jenis karyawan', '''
class Karyawan:
    def __init__(self, nama, pokok): self.nama, self.pokok = nama, pokok
    def gaji(self): return self.pokok
    def __str__(self): return f"{self.nama:<6} {type(self).__name__:<10} {self.gaji():>11,}".replace(",", ".")

class Sales(Karyawan):
    def __init__(self, nama, pokok, omzet):
        super().__init__(nama, pokok); self.omzet = omzet
    def gaji(self): return super().gaji() + round(self.omzet * 0.02)

class Manajer(Karyawan):
    def gaji(self): return super().gaji() + 2_500_000      # tunjangan jabatan

for k in [Karyawan("Rudi", 5_000_000), Sales("Mira", 4_000_000, 150_000_000), Manajer("Bayu", 12_000_000)]:
    print(k)
print("MRO Sales:", [c.__name__ for c in Sales.__mro__])
''')]),

'Duck typing (kontrak tanpa interface)': dict(
  ist=[('Duck typing', '"Jika berjalan dan bersuara seperti bebek, ia bebek": yang penting method-nya ada, bukan kelasnya.'),
       ('Protocol', 'typing.Protocol mendeskripsikan kontrak struktural yang bisa diperiksa type checker.'),
       ('Structural subtyping', 'Kecocokan tipe berdasarkan bentuk (method yang dimiliki), bukan pewarisan.'),
       ('Adapter', 'Pembungkus agar objek dengan antarmuka berbeda bisa dipakai dengan kontrak yang sama.')],
  cx=[P('Pengirim notifikasi tanpa kelas induk bersama', '''
from typing import Protocol, runtime_checkable

@runtime_checkable
class Pengirim(Protocol):
    def kirim(self, ke: str, pesan: str) -> str: ...

class Email:
    def kirim(self, ke, pesan): return f"email ke {ke}: {pesan}"
class WhatsApp:
    def kirim(self, ke, pesan): return f"WA ke {ke}: {pesan[:20]}..."
class SmsLama:                                   # pustaka pihak ketiga, nama method beda
    def send_sms(self, nomor, teks): return f"SMS {nomor}: {teks[:15]}"
class SmsAdapter:
    def __init__(self, sms): self.sms = sms
    def kirim(self, ke, pesan): return self.sms.send_sms(ke, pesan)

def broadcast(kanal, ke, pesan):
    for k in kanal: print(" ", k.kirim(ke, pesan))

broadcast([Email(), WhatsApp(), SmsAdapter(SmsLama())], "0812xxxx", "Pesanan INV-0042 sudah dikirim kurir")
print("SmsLama memenuhi Protocol:", isinstance(SmsLama(), Pengirim), "| adapter:", isinstance(SmsAdapter(None), Pengirim))
''')]),

'Paradigma: prosedural, OOP, fungsional': dict(
  ist=[('Procedural', 'Program sebagai urutan langkah dan fungsi yang mengubah data.'),
       ('Object-oriented', 'Program sebagai objek yang menyatukan data dan perilaku.'),
       ('Functional', 'Program sebagai komposisi fungsi murni tanpa mengubah state.'),
       ('Multi-paradigm', 'Python mendukung ketiganya; pilih yang paling jelas untuk tiap bagian.')],
  cx=[P('Satu tugas, tiga paradigma: total pesanan lunas', '''
pesanan = [{"id": 1, "total": 120_000, "lunas": True}, {"id": 2, "total": 75_000, "lunas": False},
           {"id": 3, "total": 310_000, "lunas": True}]

def total_prosedural(data):
    t = 0
    for p in data:
        if p["lunas"]: t += p["total"]
    return t

class Buku:
    def __init__(self, data): self.data = data
    def lunas(self): return [p for p in self.data if p["lunas"]]
    def total_lunas(self): return sum(p["total"] for p in self.lunas())

from functools import reduce
total_fungsional = reduce(lambda acc, p: acc + p["total"], filter(lambda p: p["lunas"], pesanan), 0)

print(total_prosedural(pesanan), Buku(pesanan).total_lunas(), total_fungsional)
''', 'Ketiganya benar. Di tim, pilihan biasanya: OOP untuk model domain, fungsi murni untuk perhitungan, prosedural untuk skrip.')]),

'List, dict & set comprehension': dict(
  ist=[('Comprehension', 'Sintaks ringkas membangun list/dict/set dari iterable: [f(x) for x in data if kondisi].'),
       ('Generator expression', 'Seperti comprehension tetapi dengan ( ); menghasilkan nilai satu per satu, hemat memori.'),
       ('Readability limit', 'Jika comprehension butuh lebih dari satu if atau dua for, tulis sebagai loop biasa.'),
       ('Dict inversion', '{v: k for k, v in d.items()} membalik kunci dan nilai.')],
  cx=[P('Transformasi data API dengan comprehension', '''
respons = [{"sku": "A1", "nama": "Kopi", "stok": 12, "aktif": True}, {"sku": "B2", "nama": "Teh", "stok": 0, "aktif": True},
           {"sku": "C3", "nama": "Susu", "stok": 7, "aktif": False}, {"sku": "D4", "nama": "Gula", "stok": 30, "aktif": True}]
tersedia = [p["nama"] for p in respons if p["aktif"] and p["stok"] > 0]
indeks = {p["sku"]: p for p in respons}
kategori_stok = {("habis" if p["stok"] == 0 else "ada") for p in respons}
print(tersedia)
print(indeks["D4"]["stok"], "|", sorted(kategori_stok))
print("total stok aktif:", sum(p["stok"] for p in respons if p["aktif"]))     # generator expression
print({v: k for k, v in {"MDN": "Medan", "BDG": "Bandung"}.items()})
''')]),

'Iterator & generator': dict(
  ist=[('Iterator', 'Objek yang memberi elemen satu per satu lewat next(); habis setelah dipakai.'),
       ('Generator', 'Fungsi dengan yield yang menghasilkan nilai sesuai permintaan (lazy).'),
       ('Pipeline', 'Rangkaian generator yang memproses data mengalir tanpa memuat semuanya.'),
       ('itertools', 'Modul alat iterator: islice, chain, groupby, batched (3.12+).')],
  cx=[P('Pipeline generator dan pengiriman data per batch', '''
from itertools import islice, batched

def baca_baris():                          # misalnya membaca file 10 juta baris
    for i in range(1, 10_000_001):
        yield f"{i},{'PAID' if i % 3 else 'FAILED'},{i * 1000}"

def parse(baris):
    for b in baris:
        id_, status, jml = b.split(",")
        yield int(id_), status, int(jml)

def gagal(rows):
    return (r for r in rows if r[1] == "FAILED")

pipa = gagal(parse(baca_baris()))
print("5 transaksi gagal pertama:", [r[0] for r in islice(pipa, 5)])
for kel in islice(batched(range(1, 11), 4), 3):
    print("kirim batch ke API:", kel)
''', 'Meski sumbernya 10 juta baris, hanya baris yang dibutuhkan yang benar-benar dibuat. Itulah sebabnya contoh ini selesai seketika.')]),

'Pemrograman Fungsional': dict(
  ist=[('Pure function', 'Tanpa efek samping dan selalu memberi hasil sama untuk input sama.'),
       ('Immutability', 'Data tidak diubah di tempat; perubahan menghasilkan data baru.'),
       ('Higher-order function', 'Fungsi yang menerima atau mengembalikan fungsi.'),
       ('functools.partial', 'Membuat fungsi baru dengan sebagian argumen sudah diisi.')],
  cx=[P('Aturan harga sebagai komposisi fungsi murni', '''
from functools import partial, reduce

def diskon_persen(p, harga): return harga * (1 - p)
def potongan(n, harga): return max(harga - n, 0)
def bulatkan(harga): return int(round(harga, -2))

def susun(*fungsi):
    return lambda x: reduce(lambda acc, f: f(acc), fungsi, x)

promo_member = susun(partial(diskon_persen, 0.10), partial(potongan, 5_000), bulatkan)
promo_flash = susun(partial(diskon_persen, 0.25), bulatkan)
for harga in [48_750, 120_000]:
    print(harga, "-> member", promo_member(harga), "| flash", promo_flash(harga))
''', 'Setiap aturan diuji sendiri, lalu tim marketing bisa menyusun promo baru dari aturan yang sudah ada.')]),

'Lambda': dict(
  ist=[('Lambda', 'Fungsi anonim satu ekspresi: lambda x: x * 2.'),
       ('Key function', 'Penggunaan lambda paling umum: sorted(data, key=lambda x: x["harga"]).'),
       ('operator module', 'itemgetter dan attrgetter sering lebih cepat dan jelas daripada lambda.'),
       ('Late binding closure', 'Lambda di dalam loop menangkap variabel, bukan nilainya; gunakan argumen default.')],
  cx=[P('Lambda sebagai key, itemgetter, dan jebakan late binding', '''
from operator import itemgetter
produk = [("Kopi", 85_000, 4.8), ("Teh", 24_000, 4.6), ("Cokelat", 60_000, 4.8)]
print(sorted(produk, key=lambda p: (-p[2], p[1])))      # rating tinggi dulu, lalu termurah
print(sorted(produk, key=itemgetter(1)))

salah = [lambda: i for i in range(3)]
benar = [lambda i=i: i for i in range(3)]
print("late binding:", [f() for f in salah], "| diperbaiki:", [f() for f in benar])
''')]),

'filter, map, reduce': dict(
  ist=[('map', 'Menerapkan fungsi ke setiap elemen; hasilnya iterator.'),
       ('filter', 'Menyaring elemen yang membuat fungsi bernilai benar.'),
       ('reduce', 'Melipat semua elemen menjadi satu nilai (functools.reduce).'),
       ('MapReduce', 'Pola komputasi terdistribusi (Hadoop, Spark) yang berasal dari ide map dan reduce.')],
  cx=[P('Word count gaya MapReduce', '''
from functools import reduce
from collections import Counter
ulasan = ["kopi enak pengiriman cepat", "kopi pahit pengiriman lambat", "enak dan murah", "pengiriman cepat"]
STOP = {"dan"}
kata = map(str.split, ulasan)                                   # map
rata = (k for daftar in kata for k in daftar)
bersih = filter(lambda k: k not in STOP, rata)                  # filter
hitung = reduce(lambda acc, k: acc + Counter({k: 1}), bersih, Counter())   # reduce
print(hitung.most_common(3))
print("versi idiomatik:", Counter(k for u in ulasan for k in u.split() if k not in STOP).most_common(3))
''', 'Di Python sehari-hari, comprehension dan Counter lebih umum. Pola map-filter-reduce tetap penting saat memakai Spark atau pandas.')]),

'Decorator': dict(
  ist=[('Decorator', 'Fungsi yang membungkus fungsi lain untuk menambah perilaku tanpa mengubah kodenya.'),
       ('functools.wraps', 'Menjaga nama dan docstring fungsi asli setelah dibungkus.'),
       ('Cross-cutting concern', 'Kebutuhan yang muncul di banyak tempat: logging, caching, retry, otorisasi.'),
       ('lru_cache', 'Decorator bawaan untuk memoization (menyimpan hasil pemanggilan).')],
  cx=[P('Decorator retry, otorisasi, dan cache', '''
import functools

def retry(kali):
    def dekor(f):
        @functools.wraps(f)
        def bungkus(*a, **k):
            for i in range(1, kali + 1):
                try: return f(*a, **k)
                except ConnectionError as e: print(f"  percobaan {i} gagal: {e}")
            raise ConnectionError("menyerah")
        return bungkus
    return dekor

def butuh_peran(peran):
    def dekor(f):
        @functools.wraps(f)
        def bungkus(user, *a):
            if peran not in user["peran"]: return f"403: {user['nama']} bukan {peran}"
            return f(user, *a)
        return bungkus
    return dekor

hit = {"n": 0}
@retry(3)
def ambil_kurs():
    hit["n"] += 1
    if hit["n"] < 3: raise ConnectionError("timeout")
    return 16_250

@butuh_peran("admin")
def hapus_produk(user, sku): return f"{sku} dihapus oleh {user['nama']}"

@functools.lru_cache(maxsize=128)
def ongkir(asal, tujuan): hit["n"] += 100; return 12_000

print("kurs:", ambil_kurs(), "| nama tetap:", ambil_kurs.__name__)
print(hapus_produk({"nama": "Tia", "peran": ["staf"]}, "A1"))
print(hapus_produk({"nama": "Ari", "peran": ["admin"]}, "A1"))
ongkir("JKT", "BDG"); ongkir("JKT", "BDG"); print(ongkir.cache_info())
''')]),

'Regular expression (modul re)': dict(
  ist=[('Regex', 'Bahasa pola untuk mencari dan memvalidasi teks.'),
       ('Raw string r""', 'Menulis pola tanpa menggandakan backslash: r"\\d+".'),
       ('Named group', '(?P<nama>...) memberi nama bagian yang ditangkap.'),
       ('ReDoS', 'Pola yang bisa sangat lambat pada input tertentu (backtracking berlebihan); hindari kuantifier bersarang.')],
  cx=[P('Ekstraksi dan validasi data Indonesia', '''
import re
teks = """Pesanan INV-2026-00042 dari budi@contoh.id, HP 0812-3456-7890 / +62 857 1111 2222.
Kirim ke Jl. Merdeka No. 10, Bandung 40115. Total Rp1.250.000 dibayar 19/11/2026."""

print("invoice :", re.findall(r"INV-\\d{4}-\\d{5}", teks))
print("email   :", re.findall(r"[\\w.+-]+@[\\w-]+\\.[\\w.]+", teks))
hp = [re.sub(r"\\D", "", h) for h in re.findall(r"(?:\\+62\\s?|0)8[\\d\\s-]{8,14}\\d", teks)]
print("HP norm.:", ["62" + h[1:] if h.startswith("0") else h for h in hp])
m = re.search(r"Rp(?P<angka>[\\d.]+)", teks); print("total   :", int(m["angka"].replace(".", "")))
tgl = re.search(r"(?P<d>\\d{2})/(?P<m>\\d{2})/(?P<y>\\d{4})", teks); print("ISO date:", f"{tgl['y']}-{tgl['m']}-{tgl['d']}")
print("kode pos:", re.findall(r"(?<![\\d-])\\d{5}\\b", teks))
NIK = re.compile(r"^\\d{16}$")
print("NIK valid:", [bool(NIK.match(n)) for n in ["3201123456780001", "32011234", "320112345678000A"]])
''', 'Regex cocok untuk ekstraksi pola sederhana. Untuk email, validasi akhirnya tetap dengan mengirim tautan konfirmasi.')]),
}
