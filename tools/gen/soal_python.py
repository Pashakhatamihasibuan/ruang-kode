"""Soal latihan tambahan untuk pelajaran konsep (k:'c') di jalur Python."""
from mobile_dart_x import S


def P(q, h, a, out=None): return S(q, h, a, out, lang='python')
def Tx(q, h, a): return S(q, h, a, lang='text')
def Bs(q, h, a): return S(q, h, a, lang='bash')
def Tm(q, h, a): return S(q, h, a, lang='toml')


PY = {
'Tipe data & typecasting': [
  P('Input dari pengguna selalu string. Ubah "18000" dan "2" menjadi angka, hitung total, lalu tampilkan tipe tiap nilai.', 'int() dan type().',
    'harga = "18000"\njumlah = "2"\nprint(harga + jumlah)            # string digabung\ntotal = int(harga) * int(jumlah)\nprint(total, type(total).__name__)\nprint(float("2.5"), bool(""), bool("0"))', '180002\n36000 int\n2.5 False True'),
  P('Apa hasil <code>int(3.99)</code>, <code>round(2.5)</code>, <code>round(3.5)</code>, dan <code>int("  42 ")</code>?', 'int memotong desimal. round memakai pembulatan ke genap terdekat (banker\'s rounding).',
    'print(int(3.99))\nprint(round(2.5))\nprint(round(3.5))\nprint(int("  42 "))', '3\n2\n4\n42'),
],
'Operator lengkap: //, **, walrus, dan @': [
  P('Ubah 135 menit menjadi jam dan sisa menit memakai <code>//</code> dan <code>%</code>, lalu hitung 2 pangkat 10.', 'divmod(a, b) memberi keduanya sekaligus.',
    'menit = 135\nprint(menit // 60, "jam", menit % 60, "menit")\nprint(divmod(menit, 60))\nprint(2 ** 10)\nprint(-7 // 2)       # dibulatkan ke bawah', '2 jam 15 menit\n(2, 15)\n1024\n-4'),
  P('Pakai walrus <code>:=</code> untuk membaca data dari list sampai menemukan nilai 0, sambil mencetak setiap nilai.', 'while (x := ...) != 0: menyimpan sekaligus memeriksa.',
    'data = iter([5, 3, 8, 0, 9])\nwhile (x := next(data)) != 0:\n    print(x)', '5\n3\n8'),
],
'Argumen default, keyword, *args, **kwargs': [
  P('Buat fungsi <code>total(*harga, diskon=0)</code> yang menjumlahkan semua harga lalu mengurangi diskon persen.', '*harga menampung banyak argumen posisi sebagai tuple.',
    'def total(*harga, diskon=0):\n    jumlah = sum(harga)\n    return jumlah - jumlah * diskon // 100\n\nprint(total(10000, 20000))\nprint(total(10000, 20000, 30000, diskon=10))', '30000\n54000'),
  P('Kenapa <code>def tambah(x, daftar=[])</code> berbahaya? Tunjukkan bug-nya lalu perbaiki.', 'Nilai default dibuat sekali saat fungsi didefinisikan. Pakai None.',
    'def tambah_salah(x, daftar=[]):\n    daftar.append(x)\n    return daftar\n\nprint(tambah_salah(1))\nprint(tambah_salah(2))      # list yang sama terpakai lagi\n\ndef tambah(x, daftar=None):\n    if daftar is None:\n        daftar = []\n    daftar.append(x)\n    return daftar\n\nprint(tambah(1))\nprint(tambah(2))', '[1]\n[1, 2]\n[1]\n[2]'),
  P('Buat fungsi <code>profil(nama, **info)</code> yang mencetak nama lalu setiap pasangan kunci dan nilai.', '**info menampung argumen keyword sebagai dict.',
    'def profil(nama, **info):\n    print(nama)\n    for k, v in info.items():\n        print(f"  {k}: {v}")\n\nprofil("Rina", kota="Medan", umur=21)', 'Rina\n  kota: Medan\n  umur: 21'),
],
'Scope variabel: aturan LEGB': [
  P('Kenapa kode ini error <code>UnboundLocalError</code>? Perbaiki dengan <code>global</code>, lalu dengan cara yang lebih baik.<br><code>hitung = 0<br>def klik():<br>&nbsp;&nbsp;hitung += 1</code>', 'Mengisi variabel di dalam fungsi membuatnya lokal. Lebih baik kembalikan nilai baru.',
    'hitung = 0\n\ndef klik():\n    global hitung\n    hitung += 1\n\nklik(); klik()\nprint(hitung)\n\n# lebih baik: tanpa variabel global\ndef klik_murni(n):\n    return n + 1\n\nprint(klik_murni(klik_murni(0)))', '2\n2'),
  P('Buat fungsi pembuat penghitung (closure) memakai <code>nonlocal</code>.', 'Fungsi dalam bisa mengubah variabel fungsi luar jika ditandai nonlocal.',
    'def buat_penghitung():\n    n = 0\n    def tambah():\n        nonlocal n\n        n += 1\n        return n\n    return tambah\n\nc = buat_penghitung()\nc(); c()\nprint(c())', '3'),
],
'f-string, slicing & method string': [
  P('Cetak struk dengan f-string: nama rata kiri 10 karakter, harga rata kanan 9 karakter dengan pemisah ribuan.', 'f"{nama:<10}{harga:>9,}" lalu ganti koma dengan titik.',
    'belanja = [("Kopi", 18000), ("Roti bakar", 125000)]\nfor nama, harga in belanja:\n    print(f"{nama:<10}{harga:>9,}".replace(",", "."))\nprint(f"{\'Total\':<10}{sum(h for _, h in belanja):>9,}".replace(",", "."))', 'Kopi         18.000\nRoti bakar  125.000\nTotal       143.000'),
  P('Dari "ruangkode", ambil 4 huruf pertama, 4 huruf terakhir, setiap huruf kedua, dan versi terbaliknya.', 's[:4], s[-4:], s[::2], s[::-1]',
    's = "ruangkode"\nprint(s[:4])\nprint(s[-4:])\nprint(s[::2])\nprint(s[::-1])', 'ruan\nkode\nragoe\nedokgnaur'),
  P('Rapikan "  rina SIREGAR  " menjadi "Rina Siregar", hitung huruf a, dan ganti spasi dengan tanda hubung.', 'strip, title, count, replace.',
    'nama = "  rina SIREGAR  ".strip().title()\nprint(nama)\nprint(nama.lower().count("a"))\nprint(nama.replace(" ", "-").lower())', 'Rina Siregar\n2\nrina-siregar'),
],
'match-case & ekspresi kondisional': [
  P('Pakai match-case untuk perintah teks: "tambah X", "hapus X", "daftar", dan lainnya "tidak dikenal".', 'Pola list: case ["tambah", barang]:',
    'def proses(perintah):\n    match perintah.split():\n        case ["tambah", barang]:\n            return f"Menambah {barang}"\n        case ["hapus", barang]:\n            return f"Menghapus {barang}"\n        case ["daftar"]:\n            return "Menampilkan daftar"\n        case _:\n            return "Perintah tidak dikenal"\n\nfor p in ["tambah kopi", "daftar", "lompat"]:\n    print(proses(p))', 'Menambah kopi\nMenampilkan daftar\nPerintah tidak dikenal'),
  P('Tulis ekspresi kondisional satu baris: status "dewasa" jika umur &gt;= 17, selain itu "anak".', 'nilai_a if kondisi else nilai_b',
    'for umur in (12, 17, 30):\n    status = "dewasa" if umur >= 17 else "anak"\n    print(umur, status)', '12 anak\n17 dewasa\n30 dewasa'),
],
'enumerate, zip, break, continue, else': [
  P('Cetak daftar juara bernomor mulai 1 memakai enumerate, dan pasangkan nama dengan nilai memakai zip.', 'enumerate(daftar, start=1), zip(a, b).',
    'nama = ["Rina", "Sandi", "Tari"]\nnilai = [92, 88, 85]\nfor i, (n, v) in enumerate(zip(nama, nilai), start=1):\n    print(f"{i}. {n} {v}")', '1. Rina 92\n2. Sandi 88\n3. Tari 85'),
  P('Cari bilangan prima pertama yang lebih besar dari 90 memakai for-else untuk memeriksa pembagi.', 'Blok else pada for jalan jika loop selesai tanpa break.',
    'n = 91\nwhile True:\n    for d in range(2, int(n ** 0.5) + 1):\n        if n % d == 0:\n            break\n    else:\n        print(n)\n        break\n    n += 1', '97'),
  P('Jumlahkan angka 1 sampai 20, lewati kelipatan 3 dengan continue, dan berhenti jika jumlah sudah melewati 100.', 'continue melompat ke putaran berikutnya, break keluar dari loop.',
    'total = 0\nfor i in range(1, 21):\n    if i % 3 == 0:\n        continue\n    total += i\n    if total > 100:\n        print("berhenti di", i)\n        break\nprint(total)', 'berhenti di 17\n108'),
],
'Tuple & unpacking': [
  P('Fungsi <code>statistik(data)</code> mengembalikan min, maks, dan rata-rata sekaligus. Bongkar hasilnya ke tiga variabel.', 'return a, b, c membuat tuple.',
    'def statistik(data):\n    return min(data), max(data), sum(data) / len(data)\n\nterkecil, terbesar, rata = statistik([70, 85, 90, 65])\nprint(terkecil, terbesar, rata)', '65 90 77.5'),
  P('Pakai unpacking bintang untuk memisahkan juara pertama dan sisanya, lalu tukar dua variabel tanpa variabel bantu.', 'pertama, *sisa = daftar; a, b = b, a',
    'pertama, *sisa = ["Rina", "Sandi", "Tari", "Dewi"]\nprint(pertama)\nprint(sisa)\na, b = 1, 2\na, b = b, a\nprint(a, b)', 'Rina\n[\'Sandi\', \'Tari\', \'Dewi\']\n2 1'),
],
'Dictionary lanjutan & operasi set': [
  P('Hitung frekuensi kata dalam kalimat "kopi susu kopi teh kopi susu" dengan <code>dict.get</code>, lalu dengan <code>Counter</code>.', 'freq[k] = freq.get(k, 0) + 1; Counter(...).most_common(1).',
    'from collections import Counter\n\nkata = "kopi susu kopi teh kopi susu".split()\nfreq = {}\nfor k in kata:\n    freq[k] = freq.get(k, 0) + 1\nprint(freq)\nprint(Counter(kata).most_common(1))', "{'kopi': 3, 'susu': 2, 'teh': 1}\n[('kopi', 3)]"),
  P('Kelas A diikuti {Rina, Sandi, Tari}, kelas B diikuti {Sandi, Dewi, Tari}. Siapa ikut keduanya, salah satu saja, dan semua peserta?', 'Irisan &, selisih simetris ^, gabungan |.',
    'a = {"Rina", "Sandi", "Tari"}\nb = {"Sandi", "Dewi", "Tari"}\nprint(sorted(a & b))\nprint(sorted(a ^ b))\nprint(len(a | b))', "['Sandi', 'Tari']\n['Dewi', 'Rina']\n4"),
  P('Kelompokkan nama berdasarkan huruf awal memakai <code>defaultdict(list)</code>.', 'defaultdict otomatis membuat list kosong untuk kunci baru.',
    'from collections import defaultdict\n\ngrup = defaultdict(list)\nfor n in ["Rina", "Sandi", "Rio", "Tari"]:\n    grup[n[0]].append(n)\nprint(dict(grup))', "{'R': ['Rina', 'Rio'], 'S': ['Sandi'], 'T': ['Tari']}"),
],
'raise, exception buatan sendiri & else/finally': [
  P('Buat exception <code>StokHabis</code>. Fungsi <code>beli(stok, n)</code> melemparnya jika n melebihi stok. Tunjukkan urutan blok try, except, else, finally.', 'else jalan jika tidak ada exception; finally selalu jalan.',
    'class StokHabis(Exception):\n    pass\n\ndef beli(stok, n):\n    if n > stok:\n        raise StokHabis(f"stok hanya {stok}")\n    return stok - n\n\nfor n in (2, 9):\n    try:\n        sisa = beli(5, n)\n    except StokHabis as e:\n        print("Gagal:", e)\n    else:\n        print("Sisa", sisa)\n    finally:\n        print("selesai")', 'Sisa 3\nselesai\nGagal: stok hanya 5\nselesai'),
  P('Minta umur dari daftar input <code>["abc", "-5", "21"]</code>: lewati yang bukan angka (ValueError) atau negatif, cetak yang valid.', 'raise ValueError sendiri untuk angka negatif agar ditangani di except yang sama.',
    'for teks in ["abc", "-5", "21"]:\n    try:\n        umur = int(teks)\n        if umur < 0:\n            raise ValueError("umur negatif")\n    except ValueError as e:\n        print("Ditolak:", teks, "-", e)\n    else:\n        print("Umur valid:", umur)', "Ditolak: abc - invalid literal for int() with base 10: 'abc'\nDitolak: -5 - umur negatif\nUmur valid: 21"),
],
'Context manager: with': [
  P('Tulis dua baris ke file lalu baca kembali memakai <code>with</code>. Kenapa with lebih aman daripada open/close biasa?', 'with menutup file otomatis, bahkan jika terjadi exception.',
    'with open("catatan.txt", "w", encoding="utf-8") as f:\n    f.write("beli kopi\\nbayar listrik\\n")\n\nwith open("catatan.txt", encoding="utf-8") as f:\n    for baris in f:\n        print(baris.strip())', 'beli kopi\nbayar listrik'),
  P('Buat context manager <code>pengukur_waktu</code> dengan <code>@contextmanager</code> yang mencetak "mulai" dan "selesai".', 'Kode sebelum yield jalan saat masuk, setelah yield jalan saat keluar. Pakai try/finally.',
    'from contextlib import contextmanager\n\n@contextmanager\ndef pengukur_waktu(nama):\n    print("mulai", nama)\n    try:\n        yield\n    finally:\n        print("selesai", nama)\n\nwith pengukur_waktu("impor"):\n    print("bekerja...")', 'mulai impor\nbekerja...\nselesai impor'),
],
'pathlib & modul glob': [
  P('Dari path <code>laporan/2026/penjualan.csv</code>, ambil nama file, ekstensi, nama tanpa ekstensi, dan folder induknya.', 'Path(...).name, .suffix, .stem, .parent',
    'from pathlib import Path\n\np = Path("laporan/2026/penjualan.csv")\nprint(p.name)\nprint(p.suffix)\nprint(p.stem)\nprint(p.parent.as_posix())\nprint((p.parent / "ringkas.txt").as_posix())', 'penjualan.csv\n.csv\npenjualan\nlaporan/2026\nlaporan/2026/ringkas.txt'),
  P('Buat folder <code>data</code> berisi a.csv, b.csv, dan c.txt, lalu daftar semua file .csv yang terurut.', 'mkdir(exist_ok=True), touch(), glob("*.csv").',
    'from pathlib import Path\n\nd = Path("data")\nd.mkdir(exist_ok=True)\nfor n in ["a.csv", "b.csv", "c.txt"]:\n    (d / n).touch()\nprint(sorted(f.name for f in d.glob("*.csv")))', "['a.csv', 'b.csv']"),
],
'Import & modul buatan sendiri': [
  Tx('Kamu punya file <code>hitung.py</code> berisi fungsi <code>pajak()</code>. Tulis tiga cara mengimpornya di <code>main.py</code>.', 'import modul, from modul import nama, import modul as alias.',
     'import hitung\nhitung.pajak(100000)\n\nfrom hitung import pajak\npajak(100000)\n\nimport hitung as h\nh.pajak(100000)'),
  P('Apa gunanya <code>if __name__ == "__main__":</code>? Tulis contohnya.', 'Kode di dalam blok itu hanya jalan saat file dijalankan langsung, bukan saat diimpor.',
    'def pajak(harga):\n    return harga * 11 // 100\n\nif __name__ == "__main__":\n    # hanya jalan saat: python hitung.py\n    print(pajak(100000))', '11000'),
],
'Modul bawaan yang sering dipakai': [
  P('Pakai modul bawaan: hitung akar 144 (math), rata-rata dan median [3, 7, 8, 10] (statistics), dan buat data JSON dari dict.', 'math.sqrt, statistics.mean, statistics.median, json.dumps.',
    'import json, math, statistics\n\nprint(math.sqrt(144))\nprint(statistics.mean([3, 7, 8, 10]))\nprint(statistics.median([3, 7, 8, 10]))\nprint(json.dumps({"nama": "Rina", "nilai": 92}))', '12.0\n7\n7.5\n{"nama": "Rina", "nilai": 92}'),
  P('Hitung tanggal jatuh tempo 30 hari setelah 15 Oktober 2026 dan format menjadi "14-11-2026".', 'datetime.date, timedelta, strftime("%d-%m-%Y").',
    'from datetime import date, timedelta\n\ntempo = date(2026, 10, 15) + timedelta(days=30)\nprint(tempo.strftime("%d-%m-%Y"))\nprint((date(2026, 12, 25) - date(2026, 10, 15)).days)', '14-11-2026\n71'),
],
'pip, PyPI & virtual environment': [
  Bs('Buat virtual environment, aktifkan, pasang requests, lalu simpan daftar paket ke requirements.txt.', 'python -m venv .venv; source (Linux/macOS) atau Scripts\\activate (Windows).',
     'python -m venv .venv\nsource .venv/bin/activate        # Windows: .venv\\Scripts\\activate\npip install requests\npip freeze > requirements.txt\n\n# di komputer lain\npip install -r requirements.txt'),
  Tx('Kenapa setiap proyek sebaiknya punya virtual environment sendiri?', 'Bayangkan proyek A butuh Django 4 dan proyek B butuh Django 5.',
     'Setiap proyek bisa memakai versi paket berbeda tanpa saling bentrok.\nPaket tidak mengotori Python sistem.\nDaftar dependensi bisa dicatat dan dipasang ulang persis di komputer lain.'),
],
'pyproject.toml, Poetry, pipenv, PDM, Conda, pyenv': [
  Tm('Tulis <code>pyproject.toml</code> minimal untuk proyek "kasir" versi 0.1.0, Python 3.11 ke atas, dengan dependensi requests.', 'Bagian [project] dengan name, version, requires-python, dependencies.',
     '[project]\nname = "kasir"\nversion = "0.1.0"\nrequires-python = ">=3.11"\ndependencies = [\n    "requests>=2.31",\n]\n\n[build-system]\nrequires = ["hatchling"]\nbuild-backend = "hatchling.build"'),
  Bs('Dengan Poetry: buat proyek baru, tambah pandas, tambah pytest sebagai dependensi pengembangan, lalu jalankan test.', 'poetry new, poetry add, poetry add --group dev, poetry run.',
     'poetry new kasir\ncd kasir\npoetry add pandas\npoetry add --group dev pytest\npoetry run pytest'),
],
'Enkapsulasi: property & dataclass': [
  P('Buat kelas <code>Produk</code> dengan property <code>harga</code> yang menolak nilai negatif.', '@property untuk getter, @harga.setter untuk setter. Simpan di _harga.',
    'class Produk:\n    def __init__(self, nama, harga):\n        self.nama = nama\n        self.harga = harga        # lewat setter\n\n    @property\n    def harga(self):\n        return self._harga\n\n    @harga.setter\n    def harga(self, nilai):\n        if nilai < 0:\n            raise ValueError("harga tidak boleh negatif")\n        self._harga = nilai\n\np = Produk("Kopi", 18000)\ntry:\n    p.harga = -5\nexcept ValueError as e:\n    print(e)\nprint(p.harga)', 'harga tidak boleh negatif\n18000'),
  P('Ubah kelas di atas menjadi <code>@dataclass</code> dengan field stok bawaan 0, lalu cetak objek dan bandingkan dua objek yang sama.', 'dataclass otomatis membuat __init__, __repr__, dan __eq__.',
    'from dataclasses import dataclass\n\n@dataclass\nclass Produk:\n    nama: str\n    harga: int\n    stok: int = 0\n\na = Produk("Kopi", 18000)\nb = Produk("Kopi", 18000)\nprint(a)\nprint(a == b)', "Produk(nama='Kopi', harga=18000, stok=0)\nTrue"),
],
'Dunder method: membuat objek terasa bawaan': [
  P('Buat kelas <code>Uang</code> yang bisa dijumlahkan dengan <code>+</code>, dibandingkan dengan <code>&lt;</code>, dan dicetak sebagai "Rp18.000".', '__add__, __lt__, __str__.',
    'class Uang:\n    def __init__(self, n):\n        self.n = n\n    def __add__(self, lain):\n        return Uang(self.n + lain.n)\n    def __lt__(self, lain):\n        return self.n < lain.n\n    def __str__(self):\n        return "Rp" + f"{self.n:,}".replace(",", ".")\n\na, b = Uang(18000), Uang(12500)\nprint(a + b)\nprint(b < a)\nprint(min(a, b))', 'Rp30.500\nTrue\nRp12.500'),
  P('Buat kelas <code>Keranjang</code> yang mendukung <code>len()</code>, <code>in</code>, dan perulangan for.', '__len__, __contains__, __iter__.',
    'class Keranjang:\n    def __init__(self):\n        self._isi = []\n    def tambah(self, x):\n        self._isi.append(x)\n    def __len__(self):\n        return len(self._isi)\n    def __contains__(self, x):\n        return x in self._isi\n    def __iter__(self):\n        return iter(self._isi)\n\nk = Keranjang()\nk.tambah("kopi"); k.tambah("roti")\nprint(len(k), "kopi" in k)\nfor x in k:\n    print(x)', '2 True\nkopi\nroti'),
],
'Paradigma: prosedural, OOP, fungsional': [
  P('Hitung total belanja di atas 10.000 dengan tiga gaya: prosedural (loop), fungsional (filter/sum), dan OOP (kelas Keranjang).', 'Hasilnya harus sama; yang berbeda cara menyusun kodenya.',
    'harga = [18000, 9000, 25000, 5000]\n\n# prosedural\ntotal = 0\nfor h in harga:\n    if h > 10000:\n        total += h\nprint(total)\n\n# fungsional\nprint(sum(filter(lambda h: h > 10000, harga)))\n\n# OOP\nclass Keranjang:\n    def __init__(self, isi):\n        self.isi = isi\n    def total_mahal(self, batas):\n        return sum(h for h in self.isi if h > batas)\n\nprint(Keranjang(harga).total_mahal(10000))', '43000\n43000\n43000'),
  P('Pakai <code>functools.reduce</code> untuk mengalikan semua angka [1, 2, 3, 4, 5] dan <code>map</code> untuk mengkuadratkan.', 'reduce(lambda a, b: a * b, data).',
    'from functools import reduce\n\ndata = [1, 2, 3, 4, 5]\nprint(reduce(lambda a, b: a * b, data))\nprint(list(map(lambda x: x * x, data)))', '120\n[1, 4, 9, 16, 25]'),
],
'List, dict & set comprehension': [
  P('Dari angka 1 sampai 20, buat list kuadrat bilangan genap, dict angka ke kuadratnya untuk 1 sampai 5, dan set sisa bagi 3.', '[x*x for x in ... if ...], {x: x*x for ...}, {x % 3 for ...}',
    'print([x * x for x in range(1, 21) if x % 2 == 0][:5])\nprint({x: x * x for x in range(1, 6)})\nprint({x % 3 for x in range(1, 21)})', '[4, 16, 36, 64, 100]\n{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n{0, 1, 2}'),
  P('Ratakan matriks <code>[[1, 2], [3, 4], [5, 6]]</code> menjadi satu list, dan balik dict <code>{"a": 1, "b": 2}</code>.', 'Comprehension bersarang: [x for baris in m for x in baris].',
    'm = [[1, 2], [3, 4], [5, 6]]\nprint([x for baris in m for x in baris])\nd = {"a": 1, "b": 2}\nprint({v: k for k, v in d.items()})', "[1, 2, 3, 4, 5, 6]\n{1: 'a', 2: 'b'}"),
],
'Iterator & generator': [
  P('Buat generator <code>fibonacci()</code> tanpa batas, lalu ambil 10 angka pertama memakai <code>itertools.islice</code>.', 'yield mengembalikan nilai satu per satu dan melanjutkan dari tempat terakhir.',
    'from itertools import islice\n\ndef fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n\nprint(list(islice(fibonacci(), 10)))', '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'),
  P('Bandingkan memori list comprehension dan generator expression untuk satu juta angka.', 'sys.getsizeof. Generator tidak menyimpan semua nilai.',
    'import sys\n\ndaftar = [x for x in range(1_000_000)]\ngen = (x for x in range(1_000_000))\nprint(sys.getsizeof(daftar) > 1_000_000)\nprint(sys.getsizeof(gen) < 1_000)\nprint(sum(gen))', 'True\nTrue\n499999500000'),
],
'Decorator': [
  P('Buat decorator <code>log</code> yang mencetak nama fungsi dan argumennya sebelum fungsi dipanggil.', 'def log(f): def bungkus(*args, **kwargs): ...; return bungkus. Pakai functools.wraps.',
    'from functools import wraps\n\ndef log(f):\n    @wraps(f)\n    def bungkus(*args, **kwargs):\n        print(f"memanggil {f.__name__}{args}")\n        return f(*args, **kwargs)\n    return bungkus\n\n@log\ndef tambah(a, b):\n    return a + b\n\nprint(tambah(2, 3))\nprint(tambah.__name__)', 'memanggil tambah(2, 3)\n5\ntambah'),
  P('Buat decorator berparameter <code>ulangi(n)</code> yang menjalankan fungsi n kali.', 'Tiga lapis fungsi: ulangi(n) -> decorator(f) -> bungkus(*args).',
    'def ulangi(n):\n    def decorator(f):\n        def bungkus(*args, **kwargs):\n            for _ in range(n):\n                f(*args, **kwargs)\n        return bungkus\n    return decorator\n\n@ulangi(3)\ndef sapa(nama):\n    print("Halo", nama)\n\nsapa("Rina")', 'Halo Rina\nHalo Rina\nHalo Rina'),
  P('Pakai <code>@lru_cache</code> agar fibonacci rekursif ke-80 dihitung cepat.', 'from functools import lru_cache. Hasil yang sudah dihitung disimpan.',
    'from functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    return n if n < 2 else fib(n - 1) + fib(n - 2)\n\nprint(fib(80))', '23416728348467685'),
],
'Regular expression (modul re)': [
  P('Ambil semua alamat email dari teks: "Hubungi rina@mail.id atau sandi.p@kantor.co.id, bukan @salah".', 're.findall dengan pola [\\w.]+@[\\w.]+\\w',
    'import re\n\nteks = "Hubungi rina@mail.id atau sandi.p@kantor.co.id, bukan @salah"\nprint(re.findall(r"[\\w.]+@[\\w.]+\\w", teks))', "['rina@mail.id', 'sandi.p@kantor.co.id']"),
  P('Validasi nomor HP Indonesia (08 atau +628, lalu 8 sampai 11 digit) dan ubah format "0812-3456-7890" menjadi angka saja.', 're.fullmatch untuk validasi, re.sub(r"\\D", "", s) untuk membuang selain angka.',
    'import re\n\npola = r"(\\+62|0)8\\d{8,11}"\nfor hp in ["081234567890", "+62812345678", "0712345"]:\n    print(hp, bool(re.fullmatch(pola, hp)))\nprint(re.sub(r"\\D", "", "0812-3456-7890"))', '081234567890 True\n+62812345678 True\n0712345 False\n081234567890'),
  P('Pakai grup bernama untuk mengambil hari, bulan, dan tahun dari "Tanggal: 17/08/2026".', '(?P&lt;nama&gt;...) lalu m.group("nama") atau m.groupdict().',
    'import re\n\nm = re.search(r"(?P<hari>\\d{2})/(?P<bulan>\\d{2})/(?P<tahun>\\d{4})", "Tanggal: 17/08/2026")\nprint(m.groupdict())', "{'hari': '17', 'bulan': '08', 'tahun': '2026'}"),
],
'deque, heapq & bisect: struktur data siap pakai': [
  P('Simpan hanya 3 riwayat pencarian terakhir memakai <code>deque(maxlen=3)</code>.', 'Saat penuh, elemen paling lama otomatis terbuang.',
    'from collections import deque\n\nriwayat = deque(maxlen=3)\nfor q in ["kopi", "teh", "roti", "susu"]:\n    riwayat.append(q)\nprint(list(riwayat))', "['teh', 'roti', 'susu']"),
  P('Ambil 3 produk termahal dengan <code>heapq.nlargest</code>, dan tentukan nilai huruf dari skor memakai <code>bisect</code>.', 'bisect_right(batas, skor) memberi indeks kelompok.',
    'import heapq\nfrom bisect import bisect_right\n\nharga = {"kopi": 18000, "teh": 8000, "roti": 12000, "kue": 25000}\nprint(heapq.nlargest(3, harga, key=harga.get))\n\nbatas = [60, 70, 80, 90]\nhuruf = "EDCBA"\nfor skor in (55, 75, 90):\n    print(skor, huruf[bisect_right(batas, skor)])', "['kue', 'kopi', 'roti']\n55 E\n75 C\n90 A"),
],
'Anotasi tipe & modul typing': [
  P('Beri anotasi tipe pada fungsi <code>rata(data)</code> yang menerima list angka dan mengembalikan float atau None jika list kosong.', 'list[float] dan float | None (Python 3.10+).',
    'def rata(data: list[float]) -> float | None:\n    if not data:\n        return None\n    return sum(data) / len(data)\n\nprint(rata([80, 90]))\nprint(rata([]))', '85.0\nNone'),
  P('Buat <code>TypedDict</code> untuk data pengguna dan <code>Literal</code> untuk status pesanan.', 'from typing import TypedDict, Literal.',
    'from typing import Literal, TypedDict\n\nclass Pengguna(TypedDict):\n    nama: str\n    umur: int\n\nStatus = Literal["baru", "dikirim", "selesai"]\n\ndef ubah(status: Status) -> str:\n    return f"Status: {status}"\n\nu: Pengguna = {"nama": "Rina", "umur": 21}\nprint(u["nama"], ubah("dikirim"))', 'Rina Status: dikirim'),
],
'Pemeriksa tipe: mypy, pyright, pyrefly': [
  P('Kode ini jalan tanpa error di Python, tapi mypy menolaknya. Apa pesan kesalahannya kira-kira, dan bagaimana memperbaikinya?<br><code>def pajak(harga: int) -&gt; int: return harga * 11 // 100<br>pajak("18000")</code>', 'Pemeriksa tipe membaca anotasi tanpa menjalankan program.',
    '# mypy: error: Argument 1 to "pajak" has incompatible type "str"; expected "int"\ndef pajak(harga: int) -> int:\n    return harga * 11 // 100\n\nprint(pajak(int("18000")))', '1980'),
  Bs('Pasang dan jalankan mypy dalam mode ketat untuk folder src.', 'pip install mypy; mypy --strict src',
     'pip install mypy\nmypy --strict src\n\n# atau pyright\npip install pyright\npyright src'),
],
'Validasi data dengan Pydantic': [
  P('Buat model Pydantic <code>Pesanan</code> (produk: str, jumlah: int lebih dari 0, email). Apa yang terjadi jika data dari JSON berisi jumlah "3" (string)?', 'Field(gt=0). Pydantic mengubah "3" menjadi 3 (mode lax), tapi menolak "tiga".',
    'from pydantic import BaseModel, Field, ValidationError\n\nclass Pesanan(BaseModel):\n    produk: str\n    jumlah: int = Field(gt=0)\n\nprint(Pesanan(produk="Kopi", jumlah="3"))\ntry:\n    Pesanan(produk="Kopi", jumlah=0)\nexcept ValidationError as e:\n    print(e.error_count(), "kesalahan")', "produk='Kopi' jumlah=3\n1 kesalahan"),
  P('Ubah objek Pydantic menjadi dict dan JSON.', 'model_dump() dan model_dump_json() di Pydantic v2.',
    'from pydantic import BaseModel\n\nclass Produk(BaseModel):\n    nama: str\n    harga: int\n\np = Produk(nama="Kopi", harga=18000)\nprint(p.model_dump())\nprint(p.model_dump_json())', '{\'nama\': \'Kopi\', \'harga\': 18000}\n{"nama":"Kopi","harga":18000}'),
],
'Formatter & linter: black, ruff, yapf': [
  Bs('Jalankan ruff untuk memeriksa dan memperbaiki otomatis, lalu format kode dengan ruff format atau black.', 'ruff check --fix, ruff format, black .',
     'pip install ruff black\nruff check . --fix     # cari dan perbaiki masalah (import tak terpakai, dll.)\nruff format .          # format gaya kode\nblack .                # alternatif formatter'),
  Tm('Atur ruff di pyproject.toml: panjang baris 100, aktifkan aturan pycodestyle (E), pyflakes (F), dan isort (I).', 'Bagian [tool.ruff] dan [tool.ruff.lint].',
     '[tool.ruff]\nline-length = 100\n\n[tool.ruff.lint]\nselect = ["E", "F", "I"]'),
],
'Docstring, komentar & Sphinx': [
  P('Tulis docstring gaya Google untuk fungsi <code>cicilan(pokok, bunga_tahunan, bulan)</code>, lalu tampilkan dengan <code>help</code> atau <code>__doc__</code>.', 'Bagian Args, Returns, Raises.',
    'def cicilan(pokok: int, bunga_tahunan: float, bulan: int) -> int:\n    """Menghitung cicilan bulanan dengan bunga flat.\n\n    Args:\n        pokok: Jumlah pinjaman dalam rupiah.\n        bunga_tahunan: Bunga per tahun dalam persen.\n        bulan: Lama cicilan dalam bulan.\n\n    Returns:\n        Cicilan per bulan dalam rupiah.\n\n    Raises:\n        ValueError: Jika bulan tidak positif.\n    """\n    if bulan <= 0:\n        raise ValueError("bulan harus positif")\n    bunga = pokok * bunga_tahunan / 100 * bulan / 12\n    return round((pokok + bunga) / bulan)\n\nprint(cicilan.__doc__.splitlines()[0])\nprint(cicilan(12_000_000, 12, 12))', 'Menghitung cicilan bulanan dengan bunga flat.\n1120000'),
  Tx('Mana komentar yang berguna dan mana yang tidak?<br>(a) <code>i += 1  # tambah i dengan 1</code><br>(b) <code># API membatasi 100 permintaan per menit, jadi tunggu 0,6 detik</code>', 'Komentar yang baik menjelaskan alasan, bukan mengulang kode.',
     '(a) tidak berguna: hanya mengulang apa yang sudah jelas dari kode.\n(b) berguna: menjelaskan ALASAN (batas API) yang tidak terlihat dari kode.'),
],
'Testing dengan pytest': [
  P('Tulis test pytest untuk <code>diskon(harga, persen)</code>: kasus normal, dan persen di atas 100 harus melempar ValueError.', 'Fungsi diawali test_, assert biasa, pytest.raises.',
    'import pytest\n\ndef diskon(harga, persen):\n    if not 0 <= persen <= 100:\n        raise ValueError("persen tidak valid")\n    return harga - harga * persen // 100\n\ndef test_diskon_normal():\n    assert diskon(100_000, 10) == 90_000\n\ndef test_persen_tidak_valid():\n    with pytest.raises(ValueError):\n        diskon(10_000, 120)'),
  P('Ubah beberapa kasus uji menjadi satu test dengan <code>@pytest.mark.parametrize</code>.', 'Daftar tuple (masukan, harapan).',
    'import pytest\n\n@pytest.mark.parametrize("harga, persen, harapan", [\n    (100_000, 10, 90_000),\n    (50_000, 0, 50_000),\n    (20_000, 100, 0),\n])\ndef test_diskon(harga, persen, harapan):\n    assert diskon(harga, persen) == harapan'),
],
'unittest, doctest & tox': [
  P('Tulis doctest di docstring fungsi <code>kuadrat</code>, lalu jalankan dengan <code>doctest.testmod()</code>.', 'Baris diawali &gt;&gt;&gt; diikuti hasil yang diharapkan.',
    'def kuadrat(x):\n    """Mengembalikan x pangkat dua.\n\n    >>> kuadrat(3)\n    9\n    >>> kuadrat(-4)\n    16\n    """\n    return x * x\n\nimport doctest\nprint(doctest.testmod())', 'TestResults(failed=0, attempted=2)'),
  P('Tulis test yang sama memakai unittest (kelas TestCase).', 'class ... (unittest.TestCase), method test_..., self.assertEqual.',
    'import unittest\n\ndef kuadrat(x):\n    return x * x\n\nclass TestKuadrat(unittest.TestCase):\n    def test_positif(self):\n        self.assertEqual(kuadrat(3), 9)\n\n    def test_negatif(self):\n        self.assertEqual(kuadrat(-4), 16)\n\nif __name__ == "__main__":\n    unittest.main()'),
],
'Threading & GIL': [
  P('Unduh 5 halaman (disimulasikan dengan <code>time.sleep(1)</code>) memakai ThreadPoolExecutor. Kenapa hasilnya sekitar 1 detik, bukan 5?', 'Saat thread menunggu I/O, GIL dilepas sehingga thread lain bisa jalan.',
    'import time\nfrom concurrent.futures import ThreadPoolExecutor\n\ndef unduh(n):\n    time.sleep(1)          # pura-pura menunggu jaringan\n    return f"halaman {n}"\n\nmulai = time.perf_counter()\nwith ThreadPoolExecutor(max_workers=5) as ex:\n    hasil = list(ex.map(unduh, range(1, 6)))\nprint(hasil[-1])\nprint(round(time.perf_counter() - mulai))', 'halaman 5\n1'),
  P('Dua thread menambah penghitung bersama 100.000 kali. Lindungi dengan Lock agar hasilnya pasti 200.000.', 'with kunci: hitung += 1',
    'import threading\n\nhitung = 0\nkunci = threading.Lock()\n\ndef kerja():\n    global hitung\n    for _ in range(100_000):\n        with kunci:\n            hitung += 1\n\nt = [threading.Thread(target=kerja) for _ in range(2)]\nfor x in t: x.start()\nfor x in t: x.join()\nprint(hitung)', '200000'),
],
'Multiprocessing': [
  P('Hitung jumlah bilangan prima di bawah 50.000 untuk empat rentang secara paralel memakai ProcessPoolExecutor.', 'Pekerjaan berat CPU butuh proses terpisah karena GIL. Wajib di dalam if __name__ == "__main__".',
    'from concurrent.futures import ProcessPoolExecutor\n\ndef hitung_prima(rentang):\n    a, b = rentang\n    return sum(1 for n in range(max(a, 2), b)\n               if all(n % d for d in range(2, int(n ** 0.5) + 1)))\n\nif __name__ == "__main__":\n    bagian = [(0, 12500), (12500, 25000), (25000, 37500), (37500, 50000)]\n    with ProcessPoolExecutor() as ex:\n        print(sum(ex.map(hitung_prima, bagian)))', '5133'),
  Tx('Pilih threading, multiprocessing, atau asyncio untuk: (a) mengunduh 1.000 halaman web, (b) mengubah ukuran 1.000 foto, (c) server chat dengan ribuan koneksi.', 'I/O-bound atau CPU-bound?',
     '(a) threading atau asyncio: kebanyakan waktu menunggu jaringan (I/O-bound).\n(b) multiprocessing: pengolahan gambar berat di CPU (CPU-bound).\n(c) asyncio: ribuan koneksi yang sering menunggu, ringan di memori.'),
],
'asyncio, async/await & gevent': [
  P('Jalankan tiga tugas async yang masing-masing menunggu 1 detik secara bersamaan memakai <code>asyncio.gather</code>.', 'await asyncio.sleep, bukan time.sleep.',
    'import asyncio, time\n\nasync def ambil(n):\n    await asyncio.sleep(1)\n    return n * 10\n\nasync def main():\n    mulai = time.perf_counter()\n    hasil = await asyncio.gather(ambil(1), ambil(2), ambil(3))\n    print(hasil)\n    print(round(time.perf_counter() - mulai))\n\nasyncio.run(main())', '[10, 20, 30]\n1'),
  P('Batasi tugas async yang terlalu lama dengan <code>asyncio.wait_for</code> (batas 0,5 detik).', 'TimeoutError dilempar jika waktu habis.',
    'import asyncio\n\nasync def lambat():\n    await asyncio.sleep(2)\n    return "selesai"\n\nasync def main():\n    try:\n        print(await asyncio.wait_for(lambat(), timeout=0.5))\n    except TimeoutError:\n        print("kelamaan, dibatalkan")\n\nasyncio.run(main())', 'kelamaan, dibatalkan'),
],
'Peta framework web Python': [
  Tx('Pilih framework: (a) API cepat dengan validasi otomatis dan dokumentasi, (b) situs lengkap dengan admin dan ORM bawaan, (c) aplikasi kecil yang ingin serba manual.', 'FastAPI, Django, Flask.',
     '(a) FastAPI: berbasis type hint dan Pydantic, dokumentasi /docs otomatis.\n(b) Django: "baterai lengkap" (ORM, admin, auth, migrasi).\n(c) Flask: mikro dan fleksibel, pilih sendiri pustaka tambahannya.'),
  Tx('Apa beda WSGI dan ASGI, dan framework mana memakai yang mana?', 'Sinkron atau asinkron?',
     'WSGI: standar server sinkron, satu permintaan per worker (Flask, Django klasik; server Gunicorn).\nASGI: standar asinkron, mendukung async/await dan WebSocket (FastAPI, Starlette, Django async; server Uvicorn).'),
],
'Membuat REST API: Flask & FastAPI': [
  P('Buat API FastAPI dengan <code>GET /produk/{id}</code> yang mengembalikan 404 jika produk tidak ada, dan <code>POST /produk</code> dengan model Pydantic.', 'HTTPException(status_code=404), parameter path bertipe int.',
    'from fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel\n\napp = FastAPI()\nPRODUK = {1: {"nama": "Kopi", "harga": 18000}}\n\nclass ProdukBaru(BaseModel):\n    nama: str\n    harga: int\n\n@app.get("/produk/{id}")\ndef ambil(id: int):\n    if id not in PRODUK:\n        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")\n    return PRODUK[id]\n\n@app.post("/produk", status_code=201)\ndef tambah(p: ProdukBaru):\n    baru = max(PRODUK) + 1\n    PRODUK[baru] = p.model_dump()\n    return {"id": baru, **PRODUK[baru]}\n\n# jalankan: uvicorn main:app --reload'),
  P('Tulis endpoint yang sama di Flask.', '@app.get, jsonify, abort(404), request.get_json().',
    'from flask import Flask, abort, jsonify, request\n\napp = Flask(__name__)\nPRODUK = {1: {"nama": "Kopi", "harga": 18000}}\n\n@app.get("/produk/<int:id>")\ndef ambil(id):\n    if id not in PRODUK:\n        abort(404)\n    return jsonify(PRODUK[id])\n\n@app.post("/produk")\ndef tambah():\n    data = request.get_json()\n    baru = max(PRODUK) + 1\n    PRODUK[baru] = data\n    return jsonify({"id": baru, **data}), 201'),
],
'Django: aplikasi web lengkap': [
  P('Buat model Django <code>Produk</code> (nama, harga, dibuat otomatis) lalu tulis query untuk produk di bawah 20.000 urut dari termurah.', 'models.Model, CharField, IntegerField, DateTimeField(auto_now_add=True), objects.filter(harga__lt=...).',
    'from django.db import models\n\nclass Produk(models.Model):\n    nama = models.CharField(max_length=100)\n    harga = models.IntegerField()\n    dibuat = models.DateTimeField(auto_now_add=True)\n\n    def __str__(self):\n        return self.nama\n\n# query\nmurah = Produk.objects.filter(harga__lt=20000).order_by("harga")'),
  Bs('Urutan perintah: buat proyek "toko", aplikasi "katalog", buat migrasi, terapkan, buat admin, lalu jalankan server.', 'django-admin startproject, manage.py startapp, makemigrations, migrate, createsuperuser, runserver.',
     'django-admin startproject toko\ncd toko\npython manage.py startapp katalog\n# tambahkan "katalog" ke INSTALLED_APPS\npython manage.py makemigrations\npython manage.py migrate\npython manage.py createsuperuser\npython manage.py runserver'),
],
}

SOAL = {'PY_MODULES': PY}
