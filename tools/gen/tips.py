"""Membuat src/js/tips.js: perbandingan "kode pemula" dan "kode rapi" per pelajaran.

Setiap pasangan kode yang bisa dijalankan (Java, Python, TypeScript, JavaScript, SQL, Bash)
dijalankan di sini, lalu keluarannya ditulis apa adanya. Jalankan dari akar repo:
    python3 tools/gen/tips.py
"""
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).parent

J_PRE = "import java.util.*;\nimport java.util.stream.*;\nimport java.io.*;\n\npublic class Main {\n  public static void main(String[] args) throws Exception {\n"


def run_java(code):
    with tempfile.TemporaryDirectory() as d:
        Path(d, "Main.java").write_text(J_PRE + code + "\n  }\n}\n")
        c = subprocess.run(["javac", "Main.java"], cwd=d, capture_output=True, text=True)
        if c.returncode:
            raise SystemExit("javac gagal:\n" + c.stderr + "\n" + code)
        r = subprocess.run(["java", "Main"], cwd=d, capture_output=True, text=True)
        err = "\n".join(x for x in r.stderr.splitlines() if not x.startswith(("\tat ", "Picked up")) and x.strip())
        return r.stdout + err


def run_py(code):
    with tempfile.TemporaryDirectory() as d:
        r = subprocess.run(["python3", "-c", code], cwd=d, capture_output=True, text=True)
        err = r.stderr.strip().splitlines()
        return r.stdout + (err[-1] if err else "")


def run_ts(code):
    with tempfile.TemporaryDirectory() as d:
        Path(d, "main.ts").write_text(code)
        c = subprocess.run(["tsc", "--strict", "--target", "es2022", "--module", "commonjs", "main.ts"], cwd=d, capture_output=True, text=True)
        if c.returncode:
            raise SystemExit("tsc gagal:\n" + c.stdout + "\n" + code)
        return subprocess.run(["node", "main.js"], cwd=d, capture_output=True, text=True).stdout


def run_js(code):
    r = subprocess.run(["node", "-e", code], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("node gagal:\n" + r.stderr + "\n" + code)
    return r.stdout


def run_sql(code, db="toko"):
    r = subprocess.run(["node", str(HERE / "sqlrun.js")], input=json.dumps({"db": db, "sql": code}), capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("sql gagal:\n" + r.stderr + "\n" + code)
    return r.stdout


def run_bash(code):
    with tempfile.TemporaryDirectory() as d:
        Path(d, "penjualan.csv").write_text("tanggal,kota,total\n2024-01-02,Medan,120000\n2024-01-02,Jakarta,90000\n"
                                            "2024-01-03,Medan,45000\n2024-01-03,Bandung,70000\n2024-01-04,Medan,30000\n")
        r = subprocess.run(["bash", "-c", code], cwd=d, capture_output=True, text=True)
        return r.stdout


RUN = {"java": run_java, "python": run_py, "ts": run_ts, "js": run_js, "sql": run_sql, "bash": run_bash}

# track, judul pelajaran, judul tip, label, penjelasan (HTML), bahasa, kode pemula, kode rapi
T = []


def tip(track, lesson, t, tag, why, lang, a, b, run=True, db="toko"):
    T.append(dict(track=track, lesson=lesson, t=t, tag=tag, why=why, lang=lang, a=a.strip("\n"), b=b.strip("\n"), run=run, db=db))


# ============================================================== JAVA
tip("java", "Tipe data primitif & type casting", "Angka besar lebih mudah dibaca dengan garis bawah", "Trik jarang diketahui",
    "Sejak Java 7, garis bawah boleh ditulis di antara digit: <code>1_000_000</code>. Compiler mengabaikannya, nilainya tetap sama, tetapi mata manusia langsung tahu itu satu juta, bukan seratus ribu.",
    "java", """
long harga = 1000000;
long ongkir = 25000;
System.out.println(harga + ongkir);
""", """
long harga = 1_000_000;
long ongkir = 25_000;
System.out.println(harga + ongkir);
""")
tip("java", "Tipe data primitif & type casting", "Hasil perkalian int bisa meluap tanpa peringatan", "Lebih aman",
    "Perkalian dua <code>int</code> tetap bertipe <code>int</code>, walaupun hasilnya disimpan ke <code>long</code>. Kalau melewati ±2,1 miliar, angkanya berputar menjadi negatif. Ubah salah satu operand menjadi <code>long</code> (akhiran <code>L</code>) sebelum dikalikan, atau pakai <code>Math.multiplyExact</code> agar luapan langsung jadi error.",
    "java", """
int hargaSatuan = 2_500_000;
int jumlah = 1_000;
long total = hargaSatuan * jumlah;
System.out.println(total);
""", """
int hargaSatuan = 2_500_000;
int jumlah = 1_000;
long total = (long) hargaSatuan * jumlah;
System.out.println(total);
""")
tip("java", "Method String & StringBuilder", "Menggabungkan isi array dengan pemisah", "Lebih singkat",
    "Menyambung string di dalam loop membuat objek baru setiap putaran dan butuh logika tambahan agar koma terakhir tidak ikut. <code>String.join</code> melakukan semuanya dalam satu baris.",
    "java", """
String[] buah = {"apel", "jeruk", "mangga"};
String hasil = "";
for (int i = 0; i < buah.length; i++) {
    hasil = hasil + buah[i];
    if (i < buah.length - 1) {
        hasil = hasil + ", ";
    }
}
System.out.println(hasil);
""", """
String[] buah = {"apel", "jeruk", "mangga"};
System.out.println(String.join(", ", buah));
""")
tip("java", "Method String & StringBuilder", "Teks beberapa baris dengan text block", "Trik jarang diketahui",
    "Text block (Java 15) diapit tiga tanda kutip. Tidak perlu <code>\\n</code> dan tanda <code>+</code> di setiap baris, dan indentasi di kiri dibuang otomatis.",
    "java", '''
String pesan = "Halo Sari,\\n" +
        "Pesananmu sudah dikirim.\\n" +
        "Terima kasih!";
System.out.println(pesan);
''', '''
String pesan = """
        Halo Sari,
        Pesananmu sudah dikirim.
        Terima kasih!""";
System.out.println(pesan);
''')
tip("java", "switch & operator ternary", "switch dengan panah tidak butuh break", "Lebih aman",
    "Lupa menulis <code>break</code> adalah bug klasik: eksekusi \"jatuh\" ke case berikutnya. Switch expression dengan <code>-&gt;</code> (Java 14) tidak pernah jatuh, bisa menggabungkan beberapa nilai dengan koma, dan langsung mengembalikan nilai.",
    "java", """
int hari = 6;
String jenis;
switch (hari) {
    case 6:
    case 7:
        jenis = "Akhir pekan";
        break;
    default:
        jenis = "Hari kerja";
}
System.out.println(jenis);
""", """
int hari = 6;
String jenis = switch (hari) {
    case 6, 7 -> "Akhir pekan";
    default -> "Hari kerja";
};
System.out.println(jenis);
""")
tip("java", "Kelas Arrays & array dua dimensi", "Mencetak dan mengurutkan array", "Lebih singkat",
    "Kelas <code>Arrays</code> sudah punya <code>sort</code> dan <code>toString</code>. Tidak perlu menulis algoritma pengurutan dan loop pencetak sendiri, kecuali sedang belajar algoritmanya.",
    "java", """
int[] nilai = {78, 92, 65};
for (int i = 0; i < nilai.length; i++)
    for (int j = 0; j < nilai.length - 1 - i; j++)
        if (nilai[j] > nilai[j + 1]) {
            int t = nilai[j]; nilai[j] = nilai[j + 1]; nilai[j + 1] = t;
        }
System.out.print("[");
for (int i = 0; i < nilai.length; i++) {
    System.out.print(nilai[i]);
    if (i < nilai.length - 1) System.out.print(", ");
}
System.out.println("]");
""", """
int[] nilai = {78, 92, 65};
Arrays.sort(nilai);
System.out.println(Arrays.toString(nilai));
""")
tip("java", "Enum & record", "Kelas data cukup ditulis sebagai record", "Lebih singkat",
    "Kelas yang hanya membawa data biasanya butuh field, konstruktor, getter, <code>equals</code>, <code>hashCode</code>, dan <code>toString</code>. <code>record</code> (Java 16) membuat semuanya otomatis dan nilainya tidak bisa diubah.",
    "java", """
class Produk {
    private final String nama;
    private final int harga;
    Produk(String nama, int harga) { this.nama = nama; this.harga = harga; }
    String nama() { return nama; }
    int harga() { return harga; }
    @Override public String toString() { return "Produk[nama=" + nama + ", harga=" + harga + "]"; }
}
Produk p = new Produk("Kopi Gayo", 85_000);
System.out.println(p);
System.out.println(p.harga());
""", """
record Produk(String nama, int harga) {}
Produk p = new Produk("Kopi Gayo", 85_000);
System.out.println(p);
System.out.println(p.harga());
""")
tip("java", "Array lawan ArrayList", "Daftar tetap cukup dengan List.of", "Lebih singkat",
    "<code>List.of</code> (Java 9) membuat daftar dalam satu baris. Daftarnya tidak bisa diubah, sehingga aman dibagikan ke bagian program lain. Kalau perlu menambah isi, bungkus dengan <code>new ArrayList&lt;&gt;(List.of(...))</code>.",
    "java", """
ArrayList<String> kota = new ArrayList<String>();
kota.add("Medan");
kota.add("Bandung");
kota.add("Makassar");
System.out.println(kota);
""", """
var kota = List.of("Medan", "Bandung", "Makassar");
System.out.println(kota);
""")
tip("java", "Generics: kode yang aman tipe", "Menghitung kemunculan dengan merge", "Trik jarang diketahui",
    "Pola \"kalau kunci sudah ada tambah satu, kalau belum isi satu\" bisa diganti <code>Map.merge</code>. Diamond <code>&lt;&gt;</code> juga membuat tipe tidak perlu ditulis dua kali.",
    "java", """
String[] belanja = {"kopi", "teh", "kopi", "gula", "kopi"};
TreeMap<String, Integer> hitung = new TreeMap<String, Integer>();
for (String b : belanja) {
    if (hitung.containsKey(b)) {
        hitung.put(b, hitung.get(b) + 1);
    } else {
        hitung.put(b, 1);
    }
}
System.out.println(hitung);
""", """
String[] belanja = {"kopi", "teh", "kopi", "gula", "kopi"};
Map<String, Integer> hitung = new TreeMap<>();
for (String b : belanja) hitung.merge(b, 1, Integer::sum);
System.out.println(hitung);
""")
tip("java", "Deque & Iterator", "Menghapus isi list sambil melooping", "Lebih aman",
    "Menghapus elemen di dalam for-each membuat iterator bingung dan Java melempar <code>ConcurrentModificationException</code>. <code>removeIf</code> menghapus dengan aman dalam satu baris.",
    "java", """
List<Integer> stok = new ArrayList<>(List.of(5, 0, 12, 0, 7));
for (Integer s : stok) {
    if (s == 0) stok.remove(s);
}
System.out.println(stok);
""", """
List<Integer> stok = new ArrayList<>(List.of(5, 0, 12, 0, 7));
stok.removeIf(s -> s == 0);
System.out.println(stok);
""")
tip("java", "Stream API & method chaining", "Menyaring dan menjumlah dengan stream", "Lebih singkat",
    "Loop dengan variabel penampung dan if bisa ditulis sebagai rangkaian langkah yang terbaca seperti kalimat: saring, ubah, jumlahkan.",
    "java", """
int[] harga = {12_000, 45_000, 8_000, 30_000};
int total = 0;
for (int i = 0; i < harga.length; i++) {
    if (harga[i] >= 10_000) {
        total = total + harga[i] * 2;
    }
}
System.out.println(total);
""", """
int[] harga = {12_000, 45_000, 8_000, 30_000};
int total = Arrays.stream(harga)
        .filter(h -> h >= 10_000)
        .map(h -> h * 2)
        .sum();
System.out.println(total);
""")
tip("java", "Optional: mengganti null dengan aman", "Nilai cadangan untuk null", "Trik jarang diketahui",
    "<code>Objects.requireNonNullElse</code> (Java 9) mengembalikan nilai cadangan kalau nilainya null. Satu baris, tanpa if-else.",
    "java", """
String nama = null;
String sapaan;
if (nama != null) {
    sapaan = nama;
} else {
    sapaan = "Tamu";
}
System.out.println("Halo, " + sapaan);
""", """
String nama = null;
System.out.println("Halo, " + Objects.requireNonNullElse(nama, "Tamu"));
""")
tip("java", "Checked, unchecked & exception buatan sendiri", "Menutup sumber daya otomatis", "Lebih aman",
    "Try-with-resources menutup reader, file, atau koneksi database secara otomatis, juga saat terjadi exception. Tidak perlu blok <code>finally</code> dan tidak ada risiko lupa memanggil <code>close()</code>.",
    "java", """
BufferedReader r = new BufferedReader(new StringReader("baris pertama"));
try {
    System.out.println(r.readLine());
} finally {
    r.close();
}
""", """
try (var r = new BufferedReader(new StringReader("baris pertama"))) {
    System.out.println(r.readLine());
}
""")

# ============================================================== PYTHON
tip("python", "Tipe data & typecasting", "Angka besar lebih mudah dibaca dengan garis bawah", "Trik jarang diketahui",
    "Python (3.6+) mengizinkan garis bawah di antara digit. <code>1_000_000</code> sama persis dengan <code>1000000</code>, tetapi jauh lebih mudah dibaca orang lain.",
    "python", """
harga = 1000000
ongkir = 25000
print(harga + ongkir)
""", """
harga = 1_000_000
ongkir = 25_000
print(harga + ongkir)
""")
tip("python", "Tipe data & typecasting", "Format rupiah tanpa loop", "Lebih singkat",
    "Format spec <code>:,</code> di f-string menambahkan pemisah ribuan. Ganti koma menjadi titik untuk gaya Indonesia.",
    "python", """
harga = 1250000
s = str(harga)
hasil = ""
while len(s) > 3:
    hasil = "." + s[-3:] + hasil
    s = s[:-3]
print("Rp" + s + hasil)
""", """
harga = 1_250_000
print(f"Rp{harga:,}".replace(",", "."))
""")
tip("python", "Operator lengkap: //, **, walrus, dan @", "Perbandingan berantai", "Trik jarang diketahui",
    "Python membaca <code>0 &lt;= nilai &lt;= 100</code> seperti matematika. Lebih pendek dan nilai di tengah hanya dihitung sekali.",
    "python", """
nilai = 87
if nilai >= 0 and nilai <= 100:
    print("valid")
""", """
nilai = 87
if 0 <= nilai <= 100:
    print("valid")
""")
tip("python", "f-string, slicing & method string", "Mencetak nama variabel dan nilainya sekaligus", "Trik jarang diketahui",
    "Tanda <code>=</code> di akhir f-string (Python 3.8) mencetak ekspresinya beserta nilainya. Sangat praktis untuk debugging cepat.",
    "python", """
harga = 85000
jumlah = 3
print("harga=" + str(harga) + ", jumlah=" + str(jumlah))
""", """
harga = 85_000
jumlah = 3
print(f"{harga=}, {jumlah=}")
""")
tip("python", "f-string, slicing & method string", "Membalik teks", "Lebih singkat",
    "Slicing dengan langkah <code>-1</code> membaca teks dari belakang.",
    "python", """
kata = "katak"
balik = ""
for huruf in kata:
    balik = huruf + balik
print(balik == kata)
""", """
kata = "katak"
print(kata[::-1] == kata)
""")
tip("python", "enumerate, zip, break, continue, else", "Nomor urut tanpa range(len())", "Lebih mudah dibaca",
    "<code>enumerate</code> memberi nomor dan isinya sekaligus, dan bisa dimulai dari 1. <code>zip</code> berjalan di beberapa list bersamaan.",
    "python", """
nama = ["Sari", "Budi", "Rina"]
nilai = [90, 78, 85]
for i in range(len(nama)):
    print(str(i + 1) + ". " + nama[i] + ": " + str(nilai[i]))
""", """
nama = ["Sari", "Budi", "Rina"]
nilai = [90, 78, 85]
for no, (n, v) in enumerate(zip(nama, nilai), start=1):
    print(f"{no}. {n}: {v}")
""")
tip("python", "Tuple & unpacking", "Menukar dua variabel", "Lebih singkat",
    "Python bisa membongkar tuple di sisi kiri, jadi menukar nilai tidak perlu variabel sementara. Tanda <code>*</code> menampung sisanya.",
    "python", """
a = 5
b = 9
sementara = a
a = b
b = sementara
antrean = ["Sari", "Budi", "Rina", "Dewi"]
pertama = antrean[0]
sisa = antrean[1:]
print(a, b, pertama, sisa)
""", """
a, b = 5, 9
a, b = b, a
pertama, *sisa = ["Sari", "Budi", "Rina", "Dewi"]
print(a, b, pertama, sisa)
""")
tip("python", "Dictionary lanjutan & operasi set", "Menghitung kemunculan", "Lebih singkat",
    "<code>collections.Counter</code> menghitung isi list dalam satu baris dan bisa langsung memberi yang paling sering muncul.",
    "python", """
belanja = ["kopi", "teh", "kopi", "gula", "kopi", "teh"]
hitung = {}
for b in belanja:
    if b in hitung:
        hitung[b] = hitung[b] + 1
    else:
        hitung[b] = 1
print(hitung)
""", """
from collections import Counter
belanja = ["kopi", "teh", "kopi", "gula", "kopi", "teh"]
hitung = Counter(belanja)
print(dict(hitung))
""")
tip("python", "Dictionary lanjutan & operasi set", "Membuang duplikat tanpa mengacak urutan", "Trik jarang diketahui",
    "<code>set</code> membuang duplikat tetapi urutannya tidak terjamin. <code>dict.fromkeys</code> juga membuang duplikat dan tetap menjaga urutan kemunculan pertama.",
    "python", """
kota = ["Medan", "Bandung", "Medan", "Ambon", "Bandung"]
unik = []
for k in kota:
    if k not in unik:
        unik.append(k)
print(unik)
""", """
kota = ["Medan", "Bandung", "Medan", "Ambon", "Bandung"]
print(list(dict.fromkeys(kota)))
""")
tip("python", "List, dict & set comprehension", "Membuat list baru dari list lain", "Lebih singkat",
    "Pola \"buat list kosong, loop, if, append\" bisa ditulis sebagai comprehension. Lebih pendek dan biasanya lebih cepat.",
    "python", """
harga = [12000, 45000, 8000, 30000]
mahal = []
for h in harga:
    if h >= 10000:
        mahal.append(h * 2)
print(mahal)
""", """
harga = [12_000, 45_000, 8_000, 30_000]
mahal = [h * 2 for h in harga if h >= 10_000]
print(mahal)
""")
tip("python", "Context manager: with", "Membuka file dengan with", "Lebih aman",
    "Kalau terjadi error sebelum <code>close()</code>, file tetap terbuka. Blok <code>with</code> menutup file otomatis dalam keadaan apa pun.",
    "python", """
f = open("catatan.txt", "w")
f.write("belajar Python")
f.close()
f = open("catatan.txt")
print(f.read())
f.close()
""", """
with open("catatan.txt", "w") as f:
    f.write("belajar Python")
with open("catatan.txt") as f:
    print(f.read())
""")
tip("python", "Modul bawaan yang sering dipakai", "Memeriksa \"ada yang\" dan \"semuanya\"", "Lebih singkat",
    "<code>any</code> dan <code>all</code> menggantikan loop dengan variabel penanda. Keduanya berhenti begitu jawabannya sudah pasti.",
    "python", """
stok = [5, 0, 12, 7]
ada_habis = False
for s in stok:
    if s == 0:
        ada_habis = True
        break
print(ada_habis)
""", """
stok = [5, 0, 12, 7]
print(any(s == 0 for s in stok))
""")
tip("python", "Argumen default, keyword, *args, **kwargs", "Jangan pakai list sebagai nilai default", "Lebih aman",
    "Nilai default dibuat sekali saja saat fungsi didefinisikan. List default akhirnya dipakai bersama oleh setiap panggilan, sehingga isi keranjang pembeli sebelumnya ikut terbawa. Pakai <code>None</code> lalu buat list baru di dalam fungsi.",
    "python", """
def tambah(barang, keranjang=[]):
    keranjang.append(barang)
    return keranjang

print(tambah("kopi"))
print(tambah("teh"))
""", """
def tambah(barang, keranjang=None):
    if keranjang is None:
        keranjang = []
    keranjang.append(barang)
    return keranjang

print(tambah("kopi"))
print(tambah("teh"))
""")
tip("python", "Enkapsulasi: property & dataclass", "Kelas data dengan @dataclass", "Lebih singkat",
    "<code>@dataclass</code> membuat <code>__init__</code>, <code>__repr__</code>, dan <code>__eq__</code> otomatis dari daftar field.",
    "python", """
class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __repr__(self):
        return f"Produk(nama={self.nama!r}, harga={self.harga!r})"

print(Produk("Kopi Gayo", 85000))
""", """
from dataclasses import dataclass

@dataclass
class Produk:
    nama: str
    harga: int

print(Produk("Kopi Gayo", 85_000))
""")
tip("python", "Iterator & generator", "Menjumlah tanpa membuat list", "Lebih hemat memori",
    "Tanda kurung siku membuat seluruh list di memori dulu. Tanpa kurung siku, generator menghasilkan angka satu per satu, sehingga hemat memori untuk data besar.",
    "python", """
total = sum([x * x for x in range(1_000_000)])
print(total)
""", """
total = sum(x * x for x in range(1_000_000))
print(total)
""")
tip("python", "raise, exception buatan sendiri & else/finally", "Tangkap error yang spesifik", "Lebih aman",
    "<code>except:</code> tanpa nama menangkap semua hal, termasuk salah ketik nama variabel dan Ctrl+C, sehingga bug tersembunyi. Sebutkan jenis error yang memang kamu harapkan.",
    "python", """
teks = "12a"
try:
    jumlah = int(teks)
except:
    jumlah = 0
print(jumlah)
""", """
teks = "12a"
try:
    jumlah = int(teks)
except ValueError:
    jumlah = 0
print(jumlah)
""")

# ============================================================== SQL
tip("sql", "WHERE: menyaring baris", "Rentang dan daftar nilai", "Lebih mudah dibaca",
    "<code>BETWEEN</code> mencakup kedua batas, dan <code>IN</code> menggantikan rangkaian <code>OR</code>. Hasilnya sama, tetapi maksud query langsung terbaca.",
    "sql", """
SELECT nama, kategori, harga
FROM produk
WHERE harga >= 10000 AND harga <= 30000
  AND (kategori = 'Camilan' OR kategori = 'Minuman')
ORDER BY harga;
""", """
SELECT nama, kategori, harga
FROM produk
WHERE harga BETWEEN 10000 AND 30000
  AND kategori IN ('Camilan', 'Minuman')
ORDER BY harga;
""")
tip("sql", "SELECT & FROM", "Sebutkan kolom yang dibutuhkan", "Best practice",
    "<code>SELECT *</code> praktis saat menjelajah, tetapi di aplikasi sebaiknya kolom disebutkan. Data yang dikirim lebih sedikit, dan query tidak berubah perilaku diam-diam saat tabel mendapat kolom baru.",
    "sql", """
SELECT * FROM produk ORDER BY harga DESC LIMIT 3;
""", """
SELECT nama, harga FROM produk ORDER BY harga DESC LIMIT 3;
""")
tip("sql", "HAVING", "Menyaring hasil kelompok dengan HAVING", "Lebih singkat",
    "Menyaring hasil <code>GROUP BY</code> tidak perlu subquery. <code>HAVING</code> bekerja setelah pengelompokan, sedangkan <code>WHERE</code> sebelum pengelompokan.",
    "sql", """
SELECT * FROM (
  SELECT kategori, COUNT(*) AS jumlah
  FROM produk
  GROUP BY kategori
) AS r
WHERE jumlah >= 3
ORDER BY kategori;
""", """
SELECT kategori, COUNT(*) AS jumlah
FROM produk
GROUP BY kategori
HAVING COUNT(*) >= 3
ORDER BY kategori;
""")
tip("sql", "CASE, COALESCE & NULLIF", "Nilai cadangan untuk NULL", "Lebih singkat",
    "<code>COALESCE</code> mengambil nilai pertama yang tidak NULL. Lebih pendek dari <code>CASE WHEN ... IS NULL</code>.",
    "sql", """
SELECT nama,
       CASE WHEN kota IS NULL THEN 'Belum diisi' ELSE kota END AS kota
FROM pelanggan
ORDER BY id
LIMIT 4;
""", """
SELECT nama, COALESCE(kota, 'Belum diisi') AS kota
FROM pelanggan
ORDER BY id
LIMIT 4;
""")
tip("sql", "CTE: WITH", "Beri nama pada subquery dengan WITH", "Lebih mudah dibaca",
    "Subquery bertingkat dibaca dari dalam ke luar. CTE dibaca dari atas ke bawah seperti langkah-langkah, dan setiap langkah punya nama.",
    "sql", """
SELECT p.nama, t.total
FROM (
  SELECT pelanggan_id, COUNT(*) AS total
  FROM pesanan
  GROUP BY pelanggan_id
) AS t
JOIN pelanggan p ON p.id = t.pelanggan_id
WHERE t.total >= 2
ORDER BY t.total DESC, p.nama;
""", """
WITH jumlah_pesanan AS (
  SELECT pelanggan_id, COUNT(*) AS total
  FROM pesanan
  GROUP BY pelanggan_id
)
SELECT p.nama, j.total
FROM jumlah_pesanan j
JOIN pelanggan p ON p.id = j.pelanggan_id
WHERE j.total >= 2
ORDER BY j.total DESC, p.nama;
""")
tip("sql", "Window function: ROW_NUMBER, RANK, DENSE_RANK", "Peringkat tanpa subquery berkorelasi", "Lebih cepat",
    "Subquery berkorelasi dijalankan ulang untuk setiap baris. Window function menghitung peringkat semua baris dalam satu kali jalan.",
    "sql", """
SELECT nama, harga,
       (SELECT COUNT(*) FROM produk p2 WHERE p2.harga > p1.harga) + 1 AS peringkat
FROM produk p1
ORDER BY peringkat
LIMIT 4;
""", """
SELECT nama, harga,
       RANK() OVER (ORDER BY harga DESC) AS peringkat
FROM produk
ORDER BY peringkat
LIMIT 4;
""")
tip("sql", "Correlated subquery & EXISTS", "Cek keberadaan dengan EXISTS", "Lebih cepat",
    "<code>EXISTS</code> berhenti begitu satu baris cocok ditemukan, sedangkan <code>COUNT(*) &gt; 0</code> menghitung semuanya dulu.",
    "sql", """
SELECT nama FROM pelanggan c
WHERE (SELECT COUNT(*) FROM pesanan o WHERE o.pelanggan_id = c.id) > 0
ORDER BY nama
LIMIT 5;
""", """
SELECT nama FROM pelanggan c
WHERE EXISTS (SELECT 1 FROM pesanan o WHERE o.pelanggan_id = c.id)
ORDER BY nama
LIMIT 5;
""")

# ============================================================== TYPESCRIPT
tip("ts", "Primitif, array & tuple", "Pemisah angka di TypeScript dan JavaScript", "Trik jarang diketahui",
    "Sama seperti Java dan Python, JavaScript modern (ES2021) dan TypeScript menerima <code>1_000_000</code>. Nilainya tetap angka biasa.",
    "ts", """
const harga: number = 1000000;
const ongkir: number = 25000;
console.log(harga + ongkir);
""", """
const harga = 1_000_000;
const ongkir = 25_000;
console.log(harga + ongkir);
""")
tip("ts", "Objek, literal & enum", "Union string sebagai pengganti enum", "Best practice",
    "<code>enum</code> menghasilkan kode JavaScript tambahan. Union literal seperti <code>\"baru\" | \"dikirim\"</code> sama amannya, tanpa kode tambahan, dan nilainya bisa langsung dibandingkan dengan string dari API.",
    "ts", """
enum Status { Baru = "baru", Dikirim = "dikirim", Selesai = "selesai" }
function label(s: Status): string {
  return s === Status.Dikirim ? "Dalam perjalanan" : "Lainnya";
}
console.log(label(Status.Dikirim));
""", """
type Status = "baru" | "dikirim" | "selesai";
function label(s: Status): string {
  return s === "dikirim" ? "Dalam perjalanan" : "Lainnya";
}
console.log(label("dikirim"));
""")
tip("ts", "Type alias, union & intersection", "Optional chaining dan ?? untuk data bersarang", "Lebih singkat",
    "<code>?.</code> berhenti dengan <code>undefined</code> begitu ada bagian yang kosong, dan <code>??</code> memberi nilai cadangan. Tidak perlu rangkaian <code>&amp;&amp;</code>.",
    "ts", """
type Pelanggan = { nama: string; alamat?: { kota?: string } };
const p: Pelanggan = { nama: "Sari" };
let kota: string;
if (p && p.alamat && p.alamat.kota) {
  kota = p.alamat.kota;
} else {
  kota = "-";
}
console.log(kota);
""", """
type Pelanggan = { nama: string; alamat?: { kota?: string } };
const p: Pelanggan = { nama: "Sari" };
console.log(p.alamat?.kota ?? "-");
""")
tip("ts", "any, unknown, never & void", "Pakai unknown, bukan any", "Lebih aman",
    "<code>any</code> mematikan pemeriksaan tipe, sehingga salah ketik baru ketahuan saat program jalan. <code>unknown</code> memaksa kamu memeriksa tipenya dulu, lalu TypeScript membantumu sepenuhnya.",
    "ts", """
const data: any = JSON.parse('{"harga": 85000}');
console.log(data.hargaa * 2);
""", """
const data: unknown = JSON.parse('{"harga": 85000}');
if (typeof data === "object" && data !== null && "harga" in data && typeof data.harga === "number") {
  console.log(data.harga * 2);
}
""")

# ============================================================== FRONTEND PEMULA (JavaScript)
tip("fe0", "Operator & percabangan", "|| dan ?? berbeda saat nilainya 0", "Lebih aman",
    "<code>||</code> menganggap <code>0</code> dan <code>\"\"</code> sebagai kosong, sehingga stok 0 malah diganti 10. <code>??</code> hanya mengganti <code>null</code> dan <code>undefined</code>. Gunakan juga <code>===</code>, bukan <code>==</code>, agar <code>0 == \"\"</code> tidak dianggap sama.",
    "js", """
const stok = 0;
const tampil = stok || 10;
console.log(tampil);
console.log(0 == "");
""", """
const stok = 0;
const tampil = stok ?? 10;
console.log(tampil);
console.log(0 === "");
""")
tip("fe0", "Variabel & tipe data", "Template literal untuk menyusun teks", "Lebih mudah dibaca",
    "Backtick dan <code>${...}</code> menyisipkan nilai langsung ke teks, tanpa tanda <code>+</code> dan tanda kutip yang mudah tertukar. <code>toLocaleString(\"id-ID\")</code> memberi pemisah ribuan gaya Indonesia.",
    "js", """
var nama = "Sari";
var total = 1250000;
console.log("Halo " + nama + ", totalmu Rp" + total + ".");
""", """
const nama = "Sari";
const total = 1_250_000;
console.log(`Halo ${nama}, totalmu Rp${total.toLocaleString("id-ID")}.`);
""")
tip("fe0", "Array & objek", "map, filter, dan reduce", "Lebih singkat",
    "Ketiga method ini mengganti loop dengan variabel penampung. Kodenya terbaca sebagai langkah: saring, ubah, jumlahkan.",
    "js", """
const keranjang = [{ nama: "Kopi", harga: 85000, qty: 1 }, { nama: "Teh", harga: 25000, qty: 0 }, { nama: "Gula", harga: 18000, qty: 2 }];
let total = 0;
for (let i = 0; i < keranjang.length; i++) {
  if (keranjang[i].qty > 0) {
    total = total + keranjang[i].harga * keranjang[i].qty;
  }
}
console.log(total);
""", """
const keranjang = [{ nama: "Kopi", harga: 85_000, qty: 1 }, { nama: "Teh", harga: 25_000, qty: 0 }, { nama: "Gula", harga: 18_000, qty: 2 }];
const total = keranjang
  .filter((b) => b.qty > 0)
  .reduce((jml, b) => jml + b.harga * b.qty, 0);
console.log(total);
""")
tip("fe0", "Array & objek", "Destructuring dan spread", "Trik jarang diketahui",
    "Destructuring mengambil beberapa properti sekaligus, dan spread <code>...</code> menyalin objek sambil mengubah sebagian isinya tanpa mengubah aslinya.",
    "js", """
const produk = { nama: "Kopi", harga: 85000, stok: 40 };
const nama = produk.nama;
const harga = produk.harga;
const baru = { nama: produk.nama, harga: produk.harga, stok: 39 };
console.log(nama, harga, baru, produk.stok);
""", """
const produk = { nama: "Kopi", harga: 85_000, stok: 40 };
const { nama, harga } = produk;
const baru = { ...produk, stok: 39 };
console.log(nama, harga, baru, produk.stok);
""")
tip("fe0", "Mengambil data: fetch, JSON & async", "async/await lebih mudah dibaca dari rantai then", "Lebih mudah dibaca",
    "Kedua versi melakukan hal yang sama. Dengan <code>async</code>/<code>await</code>, kode asinkron dibaca dari atas ke bawah dan error ditangkap dengan <code>try/catch</code> biasa. Di sini <code>ambil</code> meniru <code>fetch</code> agar bisa dijalankan tanpa internet.",
    "js", """
const ambil = () => Promise.resolve({ json: () => Promise.resolve({ nama: "Kopi Gayo" }) });
ambil()
  .then((res) => res.json())
  .then((data) => console.log(data.nama))
  .catch((err) => console.log("Gagal:", err.message));
""", """
const ambil = () => Promise.resolve({ json: () => Promise.resolve({ nama: "Kopi Gayo" }) });
async function tampilkan() {
  try {
    const res = await ambil();
    const data = await res.json();
    console.log(data.nama);
  } catch (err) {
    console.log("Gagal:", err.message);
  }
}
tampilkan();
""")

# ============================================================== FRONTEND
tip("fe", "Event loop JavaScript", "Jalankan permintaan bersamaan dengan Promise.all", "Lebih cepat",
    "Tiga <code>await</code> berturut-turut menunggu satu per satu. Kalau permintaannya tidak saling bergantung, <code>Promise.all</code> menjalankannya bersamaan, sehingga waktu tunggunya hanya selama permintaan terlama.",
    "js", """
const tunda = (ms, v) => new Promise((r) => setTimeout(() => r(v), ms));
(async () => {
  const mulai = Date.now();
  const produk = await tunda(300, "produk");
  const ulasan = await tunda(300, "ulasan");
  const stok = await tunda(300, "stok");
  console.log(produk, ulasan, stok);
  console.log("±" + Math.round((Date.now() - mulai) / 100) * 100 + " ms");
})();
""", """
const tunda = (ms, v) => new Promise((r) => setTimeout(() => r(v), ms));
(async () => {
  const mulai = Date.now();
  const [produk, ulasan, stok] = await Promise.all([
    tunda(300, "produk"), tunda(300, "ulasan"), tunda(300, "stok"),
  ]);
  console.log(produk, ulasan, stok);
  console.log("±" + Math.round((Date.now() - mulai) / 100) * 100 + " ms");
})();
""")
tip("fe", "Web API: storage, observer & lainnya", "Salin objek bersarang dengan structuredClone", "Trik jarang diketahui",
    "Spread hanya menyalin lapisan teratas, sehingga objek di dalamnya masih dipakai bersama. <code>structuredClone</code> (bawaan browser dan Node 17+) menyalin seluruh isi, termasuk tanggal dan Map.",
    "js", """
const asli = { nama: "Sari", alamat: { kota: "Medan" } };
const salinan = { ...asli };
salinan.alamat.kota = "Bandung";
console.log(asli.alamat.kota);
""", """
const asli = { nama: "Sari", alamat: { kota: "Medan" } };
const salinan = structuredClone(asli);
salinan.alamat.kota = "Bandung";
console.log(asli.alamat.kota);
""")

# ============================================================== REACT (tidak dijalankan di sini)
tip("react", "State dengan useState", "Perbarui state dari nilai sebelumnya", "Lebih aman",
    "<code>jumlah</code> di dalam satu render adalah nilai tetap. Memanggil <code>setJumlah(jumlah + 1)</code> dua kali tetap menghasilkan +1. Fungsi pembaru <code>j =&gt; j + 1</code> selalu menerima nilai terbaru, sehingga hasilnya +2.",
    "jsx", """
function Keranjang() {
  const [jumlah, setJumlah] = useState(0);
  function tambahDua() {
    setJumlah(jumlah + 1);
    setJumlah(jumlah + 1); // hasil akhir tetap 1
  }
  return <button onClick={tambahDua}>{jumlah}</button>;
}
""", """
function Keranjang() {
  const [jumlah, setJumlah] = useState(0);
  function tambahDua() {
    setJumlah((j) => j + 1);
    setJumlah((j) => j + 1); // hasil akhir 2
  }
  return <button onClick={tambahDua}>{jumlah}</button>;
}
""", run=False)
tip("react", "Event, percabangan & daftar", "Gunakan id sebagai key, bukan index", "Lebih aman",
    "Kalau daftar diurutkan ulang atau ada yang dihapus, key berbasis index membuat React memasangkan state ke baris yang salah, misalnya isi input pindah ke produk lain. Pakai id yang unik dan stabil.",
    "jsx", """
{produk.map((p, i) => (
  <li key={i}>{p.nama}</li>
))}
""", """
{produk.map((p) => (
  <li key={p.id}>{p.nama}</li>
))}
""", run=False)
tip("react", "useEffect & siklus hidup", "Nilai turunan tidak perlu state dan effect", "Lebih singkat",
    "Total yang bisa dihitung dari state lain cukup dihitung saat render. Menyimpannya di state lalu menyinkronkan dengan <code>useEffect</code> menambah satu render ekstra dan rawan tidak sinkron.",
    "jsx", """
const [keranjang, setKeranjang] = useState([]);
const [total, setTotal] = useState(0);
useEffect(() => {
  setTotal(keranjang.reduce((t, b) => t + b.harga, 0));
}, [keranjang]);
""", """
const [keranjang, setKeranjang] = useState([]);
const total = keranjang.reduce((t, b) => t + b.harga, 0);
""", run=False)

# ============================================================== HTML & CSS
tip("html", "Form, label & input", "Label sungguhan, bukan placeholder", "Aksesibilitas",
    "Placeholder hilang saat pengguna mulai mengetik dan sering tidak dibacakan pembaca layar. <code>&lt;label&gt;</code> yang terhubung membuat area klik lebih luas, dan <code>autocomplete</code> serta <code>inputmode</code> membuat HP menampilkan keyboard yang tepat.",
    "html", """
<input type="text" placeholder="Nomor HP">
""", """
<label for="hp">Nomor HP</label>
<input id="hp" name="hp" type="tel" inputmode="tel" autocomplete="tel" placeholder="08xx xxxx xxxx">
""", run=False)
tip("html", "Gambar & figure", "Gambar yang cepat dan tidak membuat halaman bergeser", "Lebih cepat",
    "Ukuran <code>width</code> dan <code>height</code> membuat browser menyiapkan ruang sebelum gambar selesai diunduh, sehingga tata letak tidak meloncat. <code>loading=\"lazy\"</code> menunda gambar di bawah layar, dan <code>alt</code> wajib untuk pembaca layar.",
    "html", """
<img src="kopi.jpg">
""", """
<img src="kopi.jpg" alt="Secangkir kopi Gayo di meja kayu"
     width="800" height="600" loading="lazy" decoding="async">
""", run=False)
tip("html", "Elemen semantik", "Tombol sungguhan, bukan div yang diberi onclick", "Aksesibilitas",
    "<code>&lt;div&gt;</code> tidak bisa difokus dengan Tab, tidak bisa ditekan dengan Enter atau spasi, dan tidak diumumkan sebagai tombol oleh pembaca layar. <code>&lt;button&gt;</code> memberi semua itu tanpa kode tambahan.",
    "html", """
<div class="tombol" onclick="beli()">Beli</div>
""", """
<button type="button" class="tombol" onclick="beli()">Beli</button>
""", run=False)
tip("css", "Box model", "box-sizing: border-box untuk semua elemen", "Best practice",
    "Secara bawaan, padding dan border ditambahkan di luar <code>width</code>, sehingga kotak 300px dengan padding 20px menjadi 342px. Dengan <code>border-box</code>, lebar yang ditulis adalah lebar akhirnya.",
    "css", """
.kartu {
  width: 258px; /* 300 - 2x20 padding - 2x1 border, dihitung manual */
  padding: 20px;
  border: 1px solid #ccc;
}
""", """
*, *::before, *::after { box-sizing: border-box; }
.kartu {
  width: 300px;
  padding: 20px;
  border: 1px solid #ccc;
}
""", run=False)
tip("css", "Grid", "Menengahkan isi dalam dua baris", "Trik jarang diketahui",
    "Trik lama memakai <code>position</code> dan <code>transform</code>. Grid dengan <code>place-items: center</code> menengahkan isi secara horizontal dan vertikal.",
    "css", """
.wadah { position: relative; height: 300px; }
.isi {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
""", """
.wadah {
  display: grid;
  place-items: center;
  height: 300px;
}
""", run=False)
tip("css", "Media query & mobile-first", "Ukuran huruf yang ikut lebar layar dengan clamp()", "Trik jarang diketahui",
    "<code>clamp(min, ideal, maks)</code> membuat judul membesar mulus mengikuti lebar layar dan tidak pernah lebih kecil atau lebih besar dari batasnya. Tidak perlu tiga media query.",
    "css", """
h1 { font-size: 24px; }
@media (min-width: 600px) { h1 { font-size: 32px; } }
@media (min-width: 1000px) { h1 { font-size: 44px; } }
""", """
h1 { font-size: clamp(1.5rem, 1rem + 2.5vw, 2.75rem); }
""", run=False)
tip("css", "Variabel CSS & tema", "Warna disimpan di satu tempat", "Best practice",
    "Kode warna yang diulang di banyak tempat sulit diganti dan mudah berbeda sedikit. Custom property menyimpannya sekali, dan tema gelap cukup mengganti nilainya.",
    "css", """
.tombol { background: #255DA2; }
.tautan { color: #255DA2; }
.badge  { border-color: #255da2; }
""", """
:root { --warna-utama: #255DA2; }
@media (prefers-color-scheme: dark) { :root { --warna-utama: #79ACEE; } }
.tombol { background: var(--warna-utama); }
.tautan { color: var(--warna-utama); }
.badge  { border-color: var(--warna-utama); }
""", run=False)
tip("css", "Selector sederhana", "Satu selector untuk beberapa keadaan dengan :is()", "Lebih singkat",
    "<code>:is()</code> menggabungkan daftar selector yang berulang. <code>:focus-visible</code> menampilkan garis fokus hanya untuk pengguna keyboard, bukan saat diklik dengan mouse.",
    "css", """
.menu a:hover, .menu a:focus, .footer a:hover, .footer a:focus {
  text-decoration: underline;
}
""", """
:is(.menu, .footer) a:is(:hover, :focus-visible) {
  text-decoration: underline;
}
""", run=False)

# ============================================================== GIT
tip("git", "init, add, commit", "Commit kecil dengan pesan yang jelas", "Best practice",
    "<code>git add .</code> dengan pesan \"update\" mencampur banyak perubahan dalam satu commit yang tidak bisa dijelaskan. <code>git add -p</code> memilih bagian per bagian, dan pesan berformat <i>jenis: ringkasan</i> (Conventional Commits) membuat riwayat mudah dicari.",
    "bash", """
git add .
git commit -m "update"
""", """
git add -p
git commit -m "fix: total keranjang salah saat diskon 0%"
""", run=False)
tip("git", "Remote, push & pull", "Push paksa yang tidak menimpa kerja teman", "Lebih aman",
    "<code>--force</code> menimpa remote tanpa melihat, sehingga commit teman yang baru di-push bisa hilang. <code>--force-with-lease</code> menolak push kalau remote sudah berubah sejak terakhir kamu ambil.",
    "bash", """
git push --force
""", """
git push --force-with-lease
""", run=False)
tip("git", "Membatalkan perubahan", "Membatalkan commit yang sudah di-push", "Lebih aman",
    "<code>reset --hard</code> menghapus commit dari riwayat dan membuat repositori teman tidak sinkron. Untuk commit yang sudah dibagikan, <code>revert</code> membuat commit baru yang membalikkan perubahan tanpa mengubah riwayat.",
    "bash", """
git reset --hard HEAD~1
git push --force
""", """
git revert HEAD
git push
""", run=False)
tip("git", "Riwayat & perbedaan: log dan diff", "Riwayat ringkas dalam bentuk grafik", "Trik jarang diketahui",
    "<code>--oneline --graph --all</code> menampilkan satu baris per commit beserta percabangannya. <code>git log -S kata</code> mencari commit yang menambah atau menghapus teks tertentu.",
    "bash", """
git log
""", """
git log --oneline --graph --all -n 15
git log -S "hitungDiskon" --oneline
""", run=False)

# ============================================================== DATA (Python/pandas)
PD_DATA = 'import pandas as pd\ndf = pd.DataFrame({"kota": ["Medan", "Bandung", "Medan", "Ambon", "Bandung"], "produk": ["Kopi", "Teh", "Teh", "Kopi", "Kopi"], "harga": [85000, 25000, 25000, 85000, 85000], "qty": [2, 4, 1, 3, 1]})\n'
tip("pda", "Series & DataFrame", "Kolom baru tanpa loop baris", "Lebih cepat",
    "<code>iterrows</code> memproses baris satu per satu dengan Python biasa. Operasi kolom (vektor) dikerjakan pandas sekaligus dan bisa ratusan kali lebih cepat untuk data besar.",
    "python", PD_DATA + """
total = []
for i, baris in df.iterrows():
    total.append(baris["harga"] * baris["qty"])
df["total"] = total
print(df["total"].tolist())
""", PD_DATA + """
df["total"] = df["harga"] * df["qty"]
print(df["total"].tolist())
""")
tip("pda", "groupby & agregasi", "Agregasi bernama dalam satu groupby", "Lebih singkat",
    "Daripada melooping setiap kota lalu menyaring, <code>groupby</code> dengan <code>agg</code> bernama menghitung beberapa ringkasan sekaligus dan langsung memberi nama kolomnya.",
    "python", PD_DATA + """
df["total"] = df["harga"] * df["qty"]
for kota in sorted(df["kota"].unique()):
    bagian = df[df["kota"] == kota]
    print(kota, bagian["total"].sum(), len(bagian))
""", PD_DATA + """
df["total"] = df["harga"] * df["qty"]
ringkas = df.groupby("kota").agg(omzet=("total", "sum"), transaksi=("total", "size"))
for kota, r in ringkas.iterrows():
    print(kota, r["omzet"], r["transaksi"])
""")
tip("pda", "Memilih & menyaring: loc, iloc, query", "Mengubah sebagian baris dengan .loc", "Lebih aman",
    "Pengindeksan berantai <code>df[syarat][\"kolom\"] = ...</code> mengubah salinan sementara, bukan tabel aslinya, sehingga perubahannya hilang begitu saja. <code>.loc[syarat, \"kolom\"]</code> mengubah tabel aslinya dalam satu langkah.",
    "python", PD_DATA + """
import warnings; warnings.simplefilter("ignore")
df[df["kota"] == "Ambon"]["harga"] = 90000
print(df.loc[3, "harga"])
""", PD_DATA + """
df.loc[df["kota"] == "Ambon", "harga"] = 90_000
print(df.loc[3, "harga"])
""")
tip("pda", "Teks, tanggal & tipe data", "Method .str untuk seluruh kolom teks", "Lebih singkat",
    "Aksesor <code>.str</code> menjalankan method teks untuk seluruh kolom tanpa <code>apply</code> dan lambda, dan tidak error saat ada nilai kosong.",
    "python", """
import pandas as pd
nama = pd.Series(["  sari ", "BUDI", "rina  "])
rapi = nama.apply(lambda s: s.strip().title())
print(rapi.tolist())
""", """
import pandas as pd
nama = pd.Series(["  sari ", "BUDI", "rina  "])
print(nama.str.strip().str.title().tolist())
""")
tip("da", "Lookup & pivot table", "XLOOKUP menggantikan VLOOKUP", "Trik jarang diketahui",
    "VLOOKUP memakai nomor kolom yang rusak saat ada kolom disisipkan, hanya bisa mencari ke kanan, dan bawaannya mencocokkan perkiraan. XLOOKUP (Excel 365 dan Google Sheets) menunjuk kolom langsung, bisa ke kiri, dan punya nilai cadangan bila tidak ditemukan.",
    "text", """
=VLOOKUP(A2; Produk!A:D; 4; FALSE)
""", """
=XLOOKUP(A2; Produk!A:A; Produk!D:D; "Tidak ada")
""", run=False)
tip("da", "Fungsi dasar: SUM, AVERAGE, COUNT, IF", "IFS menggantikan IF bersarang", "Lebih mudah dibaca",
    "IF di dalam IF di dalam IF sulit dibaca dan mudah salah tutup kurung. IFS menuliskan setiap syarat dan hasilnya berpasangan dari atas ke bawah.",
    "text", """
=IF(B2>=85; "A"; IF(B2>=70; "B"; IF(B2>=55; "C"; "D")))
""", """
=IFS(B2>=85; "A"; B2>=70; "B"; B2>=55; "C"; TRUE; "D")
""", run=False)
tip("bi", "Pertumbuhan, margin & kontribusi", "Hindari pembagian dengan nol memakai NULLIF", "Lebih aman",
    "Kalau penyebutnya 0, sebagian database menghentikan query dengan error. <code>NULLIF(x, 0)</code> mengubah 0 menjadi NULL, sehingga hasil baginya NULL dan query tetap berjalan.",
    "sql", """
SELECT nama, stok, harga / stok AS harga_per_stok
FROM produk
WHERE kategori = 'Minuman'
ORDER BY nama;
""", """
SELECT nama, stok, harga / NULLIF(stok, 0) AS harga_per_stok
FROM produk
WHERE kategori = 'Minuman'
ORDER BY nama;
""")
tip("de", "Idempotensi & upsert", "Upsert agar pipeline aman dijalankan ulang", "Best practice",
    "Pipeline yang gagal di tengah sering dijalankan ulang. <code>INSERT</code> biasa menghasilkan baris ganda, sedangkan <code>INSERT ... ON CONFLICT DO UPDATE</code> (PostgreSQL, SQLite) memperbarui baris yang sudah ada, sehingga hasilnya sama berapa kali pun dijalankan.",
    "python", """
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE stok (sku TEXT, jumlah INT)")
for _ in range(2):  # pipeline dijalankan dua kali
    db.execute("INSERT INTO stok VALUES ('KOPI-01', 40)")
print(db.execute("SELECT * FROM stok").fetchall())
""", """
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE stok (sku TEXT PRIMARY KEY, jumlah INT)")
for _ in range(2):  # pipeline dijalankan dua kali
    db.execute(\"\"\"INSERT INTO stok VALUES ('KOPI-01', 40)
                  ON CONFLICT(sku) DO UPDATE SET jumlah = excluded.jumlah\"\"\")
print(db.execute("SELECT * FROM stok").fetchall())
""")
tip("de", "Linux & shell untuk data", "Satu perintah lebih baik dari rantai cat", "Lebih singkat",
    "<code>grep</code> bisa membaca file sendiri dan menghitung baris yang cocok dengan <code>-c</code>, jadi <code>cat</code> dan <code>wc</code> tidak perlu. <code>awk</code> bisa menjumlah kolom CSV tanpa membuka spreadsheet.",
    "bash", """
cat penjualan.csv | grep Medan | wc -l
""", """
grep -c Medan penjualan.csv
awk -F, '$2 == "Medan" { total += $3 } END { print total }' penjualan.csv
""")

# ============================================================== DESAIN
tip("ux", "Kurangi beban: default, sedikit pilihan, aksi jelas", "Label tombol yang menyebut aksinya", "UX writing",
    "\"Submit\" dan \"OK\" tidak memberi tahu apa yang terjadi setelah ditekan. Kata kerja yang spesifik mengurangi ragu, terutama untuk aksi yang tidak bisa dibatalkan.",
    "html", """
<p>Yakin?</p>
<button>OK</button> <button>Batal</button>
""", """
<p>Hapus alamat "Rumah"? Alamat ini tidak bisa dikembalikan.</p>
<button>Hapus alamat</button> <button>Simpan alamat</button>
""", run=False)
tip("ds", "Token: primitif, semantik, komponen", "Komponen memakai token semantik, bukan kode warna", "Best practice",
    "Kode heksa di dalam komponen harus dicari satu per satu saat brand berganti warna. Token semantik menyebut perannya, sehingga perubahan cukup di satu tempat dan mode gelap tinggal mengganti nilai token.",
    "css", """
.tombol-utama { background: #2563EB; color: #FFFFFF; }
.tombol-utama:hover { background: #1D4ED8; }
""", """
:root {
  --blue-600: #2563EB;  /* primitif */
  --blue-700: #1D4ED8;
  --color-action-primary: var(--blue-600);        /* semantik */
  --color-action-primary-hover: var(--blue-700);
  --color-on-action: #FFFFFF;
}
.tombol-utama { background: var(--color-action-primary); color: var(--color-on-action); }
.tombol-utama:hover { background: var(--color-action-primary-hover); }
""", run=False)
tip("ds", "Warna fungsional & kontras", "Error tidak boleh hanya ditandai warna merah", "Aksesibilitas",
    "Sekitar 1 dari 12 laki-laki mengalami buta warna, dan pembaca layar tidak membaca warna. Pesan error perlu teks yang jelas, terhubung ke field-nya dengan <code>aria-describedby</code>, dan ditandai <code>aria-invalid</code>.",
    "html", """
<input type="email" style="border-color: red">
""", """
<label for="email">Email</label>
<input id="email" type="email" aria-invalid="true" aria-describedby="email-err">
<p id="email-err" class="error">⚠ Format email belum benar, contoh: nama@contoh.com</p>
""", run=False)


def main():
    out = {}
    for x in T:
        item = {"t": x["t"], "tag": x["tag"], "why": x["why"], "lang": x["lang"], "a": x["a"], "b": x["b"]}
        if x["run"]:
            f = RUN[x["lang"]]
            oa = f(x["a"], x["db"]) if x["lang"] == "sql" else f(x["a"])
            ob = f(x["b"], x["db"]) if x["lang"] == "sql" else f(x["b"])
            oa, ob = oa.rstrip("\n"), ob.rstrip("\n")
            if oa == ob:
                item["out"] = oa
            else:
                item["outA"], item["outB"] = oa, ob
        out.setdefault(f"{x['track']}:{x['lesson']}", []).append(item)
        print(("=" if "out" in item else "≠" if "outA" in item else "·"), x["track"], "|", x["t"])
    js = (Path(__file__).parent / "tips.tpl.js").read_text().replace("%PRO%", json.dumps(out, ensure_ascii=False, indent=0))
    (ROOT / "src/js/tips.js").write_text(js)
    print(len(T), "tip ditulis ke src/js/tips.js")


if __name__ == "__main__":
    main()
