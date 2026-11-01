/* ===================== JALUR PYTHON =====================
   Mengikuti roadmap.sh/python. Format pelajaran sama dengan jalur Java. */
const PY_MODULES=[
{t:'Fondasi Python',lvl:'Pemula',d:'Cara Python menjalankan kode, variabel, tipe data, operator, dan input.',
 nodes:['Basic Syntax','Variables','Typecasting','Operators','@ operator'],
 lessons:[
  {k:'lab',n:1,nodes:['Basic Syntax']},
  {k:'topic',ref:'1.0',nodes:['Basic Syntax']},
  {k:'topic',ref:'2.0',nodes:['Variables']},
  {k:'c',t:'Tipe data & typecasting',nodes:['Typecasting','Variables'],viz:'casting',
   b:['Python bertipe <b>dinamis</b>: kamu tidak menulis tipe saat membuat variabel, dan satu nama boleh menunjuk nilai bertipe berbeda di waktu lain. Tipe dasar yang paling sering dipakai: <code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>, dan <code>None</code> untuk "tidak ada nilai". Cek tipe dengan <code>type(x)</code>.',
      'Meski dinamis, Python bertipe <b>kuat</b>: <code>"5" + 3</code> menghasilkan error, bukan "53" atau 8. Kamu harus mengubah tipe secara eksplisit dengan <code>int()</code>, <code>float()</code>, <code>str()</code>, atau <code>bool()</code>. Ini disebut <b>typecasting</b>.',
      'Hati-hati: <code>int(3.9)</code> memotong menjadi 3, bukan membulatkan. <code>int("3.9")</code> malah error karena teksnya bukan bilangan bulat. Untuk pembulatan pakai <code>round()</code>. Nilai yang dianggap salah oleh <code>bool()</code>: 0, 0.0, string kosong, list kosong, dan None.'],
   code:R`umur = "17"
print(type(umur))
umur = int(umur)            # str -> int
print(umur + 1)

harga = 9.99
print(int(harga))           # potong pecahan
print(round(harga))         # bulatkan
print(float("3.5") * 2)
print(str(2024) + " tahun")

print(bool(0), bool(""), bool([]), bool("0"), bool(None))

try:
    print("5" + 3)
except TypeError as e:
    print("TypeError:", e)

print(int("ff", 16))        # dari heksadesimal`,
   out:`<class 'str'>
18
9
10
7.0
2024 tahun
False False False True False
TypeError: can only concatenate str (not "int") to str
255
`,
   pts:['Dinamis: tipe melekat pada nilai, bukan pada nama variabel.','Kuat: tipe berbeda tidak dicampur diam-diam.','<code>int()</code> memotong, <code>round()</code> membulatkan.','<code>input()</code> selalu menghasilkan str; ubah dulu sebelum dihitung.'],
   q:[['Hasil <code>int(7.8)</code>?',['7','8','7.8'],0,'int() membuang pecahan.'],
      ['Apa yang terjadi pada <code>"10" + 5</code>?',['"105"','15','TypeError'],2,'Python tidak mengubah tipe secara diam-diam.']]},
  {k:'topic',ref:'2.1',nodes:['Operators']},
  {k:'c',t:'Operator lengkap: //, **, walrus, dan @',nodes:['Operators','@ operator'],
   b:['Selain <code>+ - * /</code>, Python punya <code>//</code> (pembagian bulat ke bawah), <code>%</code> (sisa bagi), dan <code>**</code> (pangkat). Ingat, <code>/</code> di Python 3 selalu menghasilkan float: <code>7 / 2</code> = 3.5.',
      'Operator perbandingan bisa dirangkai seperti di matematika: <code>0 &lt;= nilai &lt;= 100</code>. Operator identitas <code>is</code> memeriksa apakah dua nama menunjuk objek yang sama, sedangkan <code>==</code> memeriksa isinya. Pakai <code>is</code> hanya untuk <code>None</code>. Operator keanggotaan <code>in</code> memeriksa apakah elemen ada di dalam koleksi.',
      'Operator <b>walrus</b> <code>:=</code> (Python 3.8) memberi nilai sekaligus memakainya dalam ekspresi. Operator <b>@</b> adalah perkalian matriks, dipakai pustaka seperti NumPy; kelas buatanmu bisa mendukungnya dengan method <code>__matmul__</code>.'],
   code:R`print(7 / 2, 7 // 2, 7 % 2, 2 ** 10)
print(-7 // 2)              # dibulatkan ke bawah, bukan ke nol

nilai = 85
print(0 <= nilai <= 100)
print("a" in "kata", 3 in [1, 2, 3])

data = None
print(data is None)

skor = [70, 95, 88]
if (n := len(skor)) > 2:
    print(f"ada {n} skor")

class Matriks:
    def __init__(self, baris):
        self.b = baris
    def __matmul__(self, lain):
        return Matriks([[sum(a * b for a, b in zip(r, k)) for k in zip(*lain.b)] for r in self.b])

A = Matriks([[1, 2], [3, 4]])
B = Matriks([[5, 6], [7, 8]])
print((A @ B).b)`,
   out:`3.5 3 1 1024
-4
True
True True
True
ada 3 skor
[[19, 22], [43, 50]]
`,
   pts:['<code>/</code> selalu float, <code>//</code> bulat ke bawah.','Perbandingan berantai: <code>a &lt; b &lt; c</code>.','<code>is</code> untuk None, <code>==</code> untuk isi.','<code>@</code> = perkalian matriks lewat <code>__matmul__</code>.'],
   q:[['Hasil <code>17 // 5</code>?',['3.4','3','2'],1,'Pembagian bulat ke bawah.'],
      ['Cara benar memeriksa variabel kosong (None)?',['x == None','x is None','x = None'],1,'None adalah objek tunggal, jadi gunakan is.']]},
  {k:'topic',ref:'3.2',nodes:['Basic Syntax']}
 ]},
{t:'Fungsi & string',lvl:'Pemula',d:'Membuat fungsi yang bisa dipakai ulang, scope variabel, dan mengolah teks.',
 nodes:['Functions','Variable Scope','Working with Strings'],
 lessons:[
  {k:'topic',ref:'1.1',nodes:['Functions']},
  {k:'topic',ref:'3.0',nodes:['Functions']},
  {k:'c',t:'Argumen default, keyword, *args, **kwargs',nodes:['Functions'],
   b:['Fungsi Python sangat fleksibel dalam menerima argumen. <b>Parameter default</b> punya nilai bawaan jika pemanggil tidak mengisinya. <b>Keyword argument</b> menyebut nama parameter saat memanggil, sehingga urutannya bebas dan kode lebih mudah dibaca.',
      '<code>*args</code> mengumpulkan sejumlah argumen posisi menjadi tuple, dan <code>**kwargs</code> mengumpulkan argumen bernama menjadi dict. Ini berguna untuk fungsi yang jumlah masukannya tidak pasti.',
      'Jebakan klasik: jangan memakai list atau dict sebagai nilai default (<code>def f(x=[])</code>), karena objek default hanya dibuat sekali dan dipakai bersama semua pemanggilan. Pakai <code>None</code> lalu buat list baru di dalam fungsi.'],
   code:R`def sapa(nama, salam="Halo", tanda="!"):
    return f"{salam}, {nama}{tanda}"

print(sapa("Rina"))
print(sapa("Budi", tanda="?"))
print(sapa(salam="Selamat pagi", nama="Citra"))

def total(*harga, diskon=0):
    return sum(harga) * (100 - diskon) // 100

print(total(10000, 25000, 5000))
print(total(10000, 25000, diskon=10))

def profil(**data):
    return ", ".join(f"{k}={v}" for k, v in data.items())

print(profil(nama="Eko", kota="Medan"))

def tambah(item, wadah=None):
    if wadah is None:
        wadah = []
    wadah.append(item)
    return wadah

print(tambah(1), tambah(2))`,
   out:`Halo, Rina!
Halo, Budi?
Selamat pagi, Citra!
40000
31500
nama=Eko, kota=Medan
[1] [2]
`,
   pts:['Parameter default ditulis setelah parameter wajib.','Keyword argument membuat pemanggilan jelas.','<code>*args</code> → tuple, <code>**kwargs</code> → dict.','Hindari default yang bisa diubah (list/dict).'],
   q:[['<code>def f(*args)</code>, isi args saat <code>f(1, 2, 3)</code>?',['[1, 2, 3]','(1, 2, 3)','{1, 2, 3}'],1,'*args dikumpulkan menjadi tuple.'],
      ['Kenapa <code>def f(x=[])</code> berbahaya?',['Error sintaks','List default dipakai bersama semua pemanggilan','Lambat'],1,'Default dievaluasi sekali saat fungsi didefinisikan.']]},
  {k:'c',t:'Scope variabel: aturan LEGB',nodes:['Variable Scope'],
   b:['Saat Python mencari sebuah nama, ia memeriksa empat tempat secara berurutan: <b>L</b>ocal (di dalam fungsi), <b>E</b>nclosing (fungsi luar yang membungkus), <b>G</b>lobal (tingkat file), lalu <b>B</b>uilt-in (seperti <code>print</code>, <code>len</code>). Urutan ini disebut aturan LEGB.',
      'Memberi nilai pada sebuah nama di dalam fungsi otomatis membuatnya variabel lokal. Jadi jika kamu ingin mengubah variabel global, tulis <code>global nama</code>; untuk variabel fungsi luar, tulis <code>nonlocal nama</code>. Gunakan keduanya seperlunya, karena variabel global membuat program sulit dilacak.',
      'Fungsi di dalam fungsi yang mengingat variabel luarnya disebut <b>closure</b>. Ini dasar dari decorator yang akan kamu pelajari nanti.'],
   code:R`pajak = 0.11                     # global

def harga_akhir(harga):
    diskon = 0.05                # local
    return harga * (1 - diskon) * (1 + pajak)

print(round(harga_akhir(100000)))

hitungan = 0
def klik():
    global hitungan
    hitungan += 1

klik(); klik()
print(hitungan)

def buat_penghitung():
    n = 0                        # enclosing
    def tambah():
        nonlocal n
        n += 1
        return n
    return tambah

c = buat_penghitung()
c(); c()
print(c())

def rusak():
    try:
        hitungan += 1            # dianggap lokal, belum ada nilainya
    except UnboundLocalError as e:
        print("UnboundLocalError")

rusak()`,
   out:`105450
2
3
UnboundLocalError
`,
   pts:['Urutan pencarian nama: Local → Enclosing → Global → Built-in.','Assignment di dalam fungsi membuat variabel lokal.','<code>global</code>/<code>nonlocal</code> untuk mengubah variabel di luar.','Closure: fungsi dalam yang mengingat variabel fungsi luar.'],
   q:[['Python mencari nama di mana terlebih dahulu?',['Global','Local','Built-in'],1,'L di LEGB adalah yang pertama.'],
      ['Kata kunci untuk mengubah variabel fungsi luar dari fungsi dalam?',['global','nonlocal','outer'],1,'nonlocal merujuk scope enclosing.']]},
  {k:'topic',ref:'3.1',nodes:['Working with Strings']},
  {k:'c',t:'f-string, slicing & method string',nodes:['Working with Strings'],
   b:['<b>f-string</b> adalah cara paling nyaman menyusun teks: tulis <code>f</code> sebelum kutip, lalu ekspresi di dalam kurung kurawal. Kamu juga bisa mengatur format: <code>{harga:,}</code> memberi pemisah ribuan, <code>{x:.2f}</code> dua angka di belakang koma, <code>{nama:&gt;10}</code> rata kanan selebar 10.',
      '<b>Slicing</b> mengambil potongan string dengan <code>s[awal:akhir:langkah]</code>. Indeks negatif dihitung dari belakang: <code>s[-1]</code> huruf terakhir, <code>s[::-1]</code> membalik string.',
      'String immutable, jadi method seperti <code>upper</code>, <code>strip</code>, <code>replace</code> mengembalikan string baru. Method yang paling sering dipakai: <code>split</code> dan <code>join</code> untuk memecah dan menggabung, <code>startswith</code>, <code>find</code>, serta <code>count</code>.'],
   code:R`nama = "  budi santoso "
rapi = nama.strip().title()
print(rapi)
print(rapi[:4], rapi[-7:], rapi[::-1])

harga = 1250000
print(f"Harga: Rp{harga:,}".replace(",", "."))
print(f"Rata-rata: {85.666:.2f}")
print(f"[{'kopi':>8}] [{'teh':<6}] [{7:03d}]")

kalimat = "saya belajar python dan sql"
kata = kalimat.split()
print(len(kata), kata[2])
print("-".join(kata))
print(kalimat.count("a"), kalimat.find("python"))
print(kalimat.startswith("saya"), "SQL" in kalimat.upper())`,
   out:`Budi Santoso
Budi Santoso osotnaS iduB
Harga: Rp1.250.000
Rata-rata: 85.67
[    kopi] [teh   ] [007]
5 python
saya-belajar-python-dan-sql
5 13
True True
`,
   pts:['f-string: <code>f"{ekspresi:format}"</code>.','Slicing <code>[a:b]</code> mengambil a sampai sebelum b.','<code>s[::-1]</code> membalik string.','<code>"pemisah".join(list)</code> kebalikan dari <code>split</code>.'],
   q:[['Hasil <code>"python"[1:4]</code>?',['"pyt"','"yth"','"ytho"'],1,'Indeks 1 sampai sebelum 4.'],
      ['Format f-string untuk dua desimal?',['{x:2}','{x:.2f}','{x,2}'],1,'.2f = float dengan dua angka di belakang koma.']]}
 ]},
{t:'Percabangan & perulangan',lvl:'Pemula',d:'if, match, for, while, dan trik perulangan khas Python.',
 nodes:['Conditionals','Loops'],
 lessons:[
  {k:'lab',n:4,nodes:['Conditionals']},
  {k:'topic',ref:'4.0',nodes:['Conditionals']},
  {k:'c',t:'match-case & ekspresi kondisional',nodes:['Conditionals'],
   b:['Python 3.10 memperkenalkan <code>match</code>, mirip switch di bahasa lain tetapi lebih kuat karena bisa mencocokkan <b>pola</b>: nilai tetap, beberapa pilihan dengan <code>|</code>, bentuk tuple atau list, bahkan menangkap bagian data ke variabel.',
      'Kasus <code>case _:</code> adalah penangkap sisa, seperti <code>else</code>. Tambahkan <code>if</code> setelah pola (disebut guard) untuk syarat tambahan.',
      'Untuk pilihan dua nilai yang singkat, Python punya ekspresi kondisional: <code>a if kondisi else b</code>. Urutannya dibaca seperti kalimat: "a jika kondisi, kalau tidak b".'],
   code:R`def jenis_hari(h):
    match h:
        case "sabtu" | "minggu":
            return "akhir pekan"
        case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
            return "hari kerja"
        case _:
            return "tidak dikenal"

print(jenis_hari("sabtu"), "/", jenis_hari("rabu"))

def arah(perintah):
    match perintah.split():
        case ["jalan", tujuan]:
            return f"berjalan ke {tujuan}"
        case ["ambil", benda, *sisa] if sisa:
            return f"ambil {benda} dan {len(sisa)} barang lain"
        case ["ambil", benda]:
            return f"ambil {benda}"
        case _:
            return "perintah tidak dikenal"

print(arah("jalan utara"))
print(arah("ambil kunci peta senter"))
print(arah("ambil kunci"))

umur = 16
print("dewasa" if umur >= 17 else "remaja")`,
   out:`akhir pekan / hari kerja
berjalan ke utara
ambil kunci dan 2 barang lain
ambil kunci
remaja
`,
   pts:['<code>case a | b:</code> untuk beberapa pilihan.','<code>case _:</code> menangkap semua sisa.','Pola bisa menangkap bagian data ke variabel.','Ekspresi kondisional: <code>x if syarat else y</code>.'],
   q:[['Pola untuk "semua kasus lainnya" di match?',['case else:','case _:','default:'],1,'Garis bawah adalah wildcard.'],
      ['Hasil <code>"A" if 3 > 5 else "B"</code>?',['"A"','"B"','None'],1,'Kondisinya salah, jadi nilai setelah else dipilih.']]},
  {k:'topic',ref:'4.1',nodes:['Conditionals','Loops']},
  {k:'lab',n:2,nodes:['Loops']},
  {k:'topic',ref:'2.2',nodes:['Loops']},
  {k:'topic',ref:'2.3',nodes:['Loops']},
  {k:'lab',n:5,nodes:['Loops']},
  {k:'topic',ref:'5.0',nodes:['Loops']},
  {k:'topic',ref:'5.1',nodes:['Conditionals']},
  {k:'topic',ref:'5.2',nodes:['Loops']},
  {k:'c',t:'enumerate, zip, break, continue, else',nodes:['Loops'],
   b:['Python mendorong loop yang langsung berjalan di atas data, bukan di atas indeks. Jika kamu butuh indeks sekaligus nilainya, pakai <code>enumerate</code>. Jika ingin berjalan di atas dua list sekaligus, pakai <code>zip</code>.',
      '<code>break</code> menghentikan loop seketika, sedangkan <code>continue</code> melompat ke putaran berikutnya. Loop di Python juga boleh punya blok <code>else</code>, yang dijalankan hanya jika loop selesai <i>tanpa</i> break. Ini rapi untuk pola "cari, dan kalau tidak ketemu lakukan sesuatu".',
      '<code>range(awal, akhir, langkah)</code> menghasilkan deret angka tanpa menyimpannya semua di memori. <code>reversed</code> dan <code>sorted</code> membantu berjalan terbalik atau berurutan tanpa mengubah data asli.'],
   code:R`buah = ["apel", "jeruk", "mangga"]
for i, b in enumerate(buah, start=1):
    print(i, b)

harga = [12000, 8000, 15000]
for b, h in zip(buah, harga):
    print(f"{b}: {h}")

ganjil = []
for n in range(1, 10):
    if n % 2 == 0:
        continue
    if n > 7:
        break
    ganjil.append(n)
print(ganjil)

target = "durian"
for b in buah:
    if b == target:
        print("ketemu")
        break
else:
    print(target, "tidak ada")

print(list(range(10, 0, -3)), list(reversed(buah)))`,
   out:`1 apel
2 jeruk
3 mangga
apel: 12000
jeruk: 8000
mangga: 15000
[1, 3, 5, 7]
durian tidak ada
[10, 7, 4, 1] ['mangga', 'jeruk', 'apel']
`,
   pts:['<code>enumerate</code> memberi pasangan (indeks, nilai).','<code>zip</code> berjalan di atas beberapa koleksi sekaligus.','<code>for ... else</code>: else jalan jika tidak ada break.','<code>range</code> hemat memori.'],
   q:[['Kapan blok <code>else</code> pada for dijalankan?',['Selalu','Jika loop selesai tanpa break','Jika terjadi error'],1,'Break melewati blok else.'],
      ['Fungsi untuk mendapat indeks dan nilai sekaligus?',['zip','enumerate','range'],1,'enumerate menghasilkan pasangan indeks dan nilai.']]}
 ]},
{t:'Struktur data bawaan',lvl:'Pemula',d:'List, tuple, set, dan dictionary: empat wadah data andalan Python.',
 nodes:['Lists','Tuples','Sets','Dictionaries'],
 lessons:[
  {k:'lab',n:7,nodes:['Lists']},
  {k:'topic',ref:'7.0',nodes:['Lists']},
  {k:'topic',ref:'7.1',nodes:['Lists']},
  {k:'topic',ref:'7.2',nodes:['Lists']},
  {k:'lab',n:10,nodes:['Lists']},
  {k:'topic',ref:'10.0',nodes:['Lists']},
  {k:'topic',ref:'10.1',nodes:['Lists']},
  {k:'c',t:'Tuple & unpacking',nodes:['Tuples'],
   b:['<b>Tuple</b> mirip list, tetapi <b>immutable</b>: setelah dibuat isinya tidak bisa diubah. Ditulis dengan kurung biasa: <code>(3, 4)</code>. Tuple cocok untuk data yang memang satu paket dan tetap, seperti koordinat, tanggal, atau satu baris hasil database.',
      'Karena immutable, tuple bisa dipakai sebagai kunci dictionary dan anggota set, sedangkan list tidak bisa.',
      '<b>Unpacking</b> membongkar isi tuple ke beberapa variabel sekaligus: <code>x, y = titik</code>. Fungsi bisa mengembalikan beberapa nilai sebagai tuple. Tanda bintang menangkap sisanya: <code>pertama, *sisa = data</code>. Trik terkenal: menukar dua variabel cukup dengan <code>a, b = b, a</code>.'],
   code:R`titik = (3, 4)
x, y = titik
print(x, y)

def statistik(data):
    return min(data), max(data), sum(data) / len(data)

lo, hi, rata = statistik([70, 85, 90, 65])
print(lo, hi, rata)

pertama, *tengah, terakhir = [1, 2, 3, 4, 5]
print(pertama, tengah, terakhir)

a, b = 10, 20
a, b = b, a
print(a, b)

jarak = {("Jakarta", "Bandung"): 150, ("Jakarta", "Bogor"): 60}
print(jarak[("Jakarta", "Bogor")])

try:
    titik[0] = 9
except TypeError:
    print("tuple tidak bisa diubah")

satu = (5,)
print(type(satu).__name__, type((5)).__name__)`,
   out:`3 4
65 90 77.5
1 [2, 3, 4] 5
20 10
60
tuple tidak bisa diubah
tuple int
`,
   pts:['Tuple immutable, list mutable.','Tuple bisa menjadi kunci dict.','Unpacking: <code>a, b = pasangan</code>; bintang menangkap sisa.','Tuple satu elemen butuh koma: <code>(5,)</code>.'],
   q:[['Mana yang bisa menjadi kunci dictionary?',['[1, 2]','(1, 2)','{1, 2}'],1,'Kunci dict harus immutable (hashable).'],
      ['Cara menukar nilai a dan b?',['a = b; b = a','a, b = b, a','swap(a, b)'],1,'Unpacking tuple menukar keduanya sekaligus.']]},
  {k:'lab',n:11,nodes:['Sets','Dictionaries']},
  {k:'topic',ref:'11.0',nodes:['Sets']},
  {k:'topic',ref:'11.1',nodes:['Dictionaries']},
  {k:'c',t:'Dictionary lanjutan & operasi set',nodes:['Dictionaries','Sets'],
   b:['Dictionary menyimpan pasangan kunci dan nilai, dan sejak Python 3.7 urutan penyisipan terjaga. Ambil nilai dengan aman memakai <code>d.get(k, cadangan)</code> agar tidak muncul KeyError. <code>setdefault</code> dan <code>collections.defaultdict</code> memudahkan pola "kelompokkan".',
      'Telusuri dictionary dengan <code>items()</code> untuk mendapat kunci dan nilai sekaligus. Gabungkan dua dictionary dengan operator <code>|</code> (Python 3.9). <code>collections.Counter</code> adalah dictionary khusus untuk menghitung.',
      'Set punya operasi himpunan seperti di matematika: <code>|</code> gabungan, <code>&amp;</code> irisan, <code>-</code> selisih, dan <code>^</code> beda simetris. Ini sangat cepat untuk pertanyaan seperti "siapa yang ikut kelas A tapi tidak ikut kelas B?".'],
   code:R`from collections import Counter, defaultdict

stok = {"kopi": 40, "teh": 120}
print(stok.get("madu", 0))
stok |= {"madu": 15}
for nama, jml in stok.items():
    print(f"{nama:5} {jml}")

pesanan = ["kopi", "teh", "kopi", "madu", "kopi"]
print(Counter(pesanan).most_common(2))

per_kota = defaultdict(list)
for nama, kota in [("Andi", "Jakarta"), ("Budi", "Bandung"), ("Dewi", "Jakarta")]:
    per_kota[kota].append(nama)
print(dict(per_kota))

kelas_a = {"Andi", "Budi", "Citra"}
kelas_b = {"Budi", "Dewi"}
print(sorted(kelas_a & kelas_b), sorted(kelas_a - kelas_b), sorted(kelas_a | kelas_b))`,
   out:`0
kopi  40
teh   120
madu  15
[('kopi', 3), ('teh', 1)]
{'Jakarta': ['Andi', 'Dewi'], 'Bandung': ['Budi']}
['Budi'] ['Andi', 'Citra'] ['Andi', 'Budi', 'Citra', 'Dewi']
`,
   pts:['<code>get(k, default)</code> mencegah KeyError.','<code>items()</code> untuk loop kunci dan nilai.','Counter untuk menghitung, defaultdict untuk mengelompokkan.','Set: <code>&amp;</code> irisan, <code>|</code> gabungan, <code>-</code> selisih.'],
   q:[['<code>{"a":1}.get("b", 0)</code> menghasilkan?',['KeyError','None','0'],2,'Nilai cadangan dikembalikan jika kunci tidak ada.'],
      ['Operator set untuk anggota yang ada di kedua himpunan?',['|','&','-'],1,'& adalah irisan.']]}
 ]},
{t:'Error & file',lvl:'Menengah',d:'Menangani exception, membuat exception sendiri, context manager, dan bekerja dengan file serta folder.',
 nodes:['Exceptions','Error Handling','File Handling','Context Manager','Glob Module'],
 lessons:[
  {k:'lab',n:6,nodes:['File Handling']},
  {k:'topic',ref:'6.0',nodes:['File Handling']},
  {k:'topic',ref:'6.1',nodes:['Exceptions','Error Handling']},
  {k:'c',t:'raise, exception buatan sendiri & else/finally',nodes:['Exceptions','Error Handling'],viz:'unwind',
   b:['Kamu bisa melempar exception sendiri dengan <code>raise</code> ketika fungsi menerima data yang tidak masuk akal. Buat kelas exception khusus dengan menurunkan <code>Exception</code>, supaya pemanggil bisa menangkap jenis kesalahan yang spesifik.',
      'Exception yang tidak ditangkap akan "naik" ke fungsi pemanggil, lalu pemanggilnya, dan seterusnya, sampai ada <code>except</code> yang cocok. Kalau tidak ada sama sekali, program berhenti dan menampilkan <i>traceback</i>: jejak lengkap pemanggilan dari bawah ke atas.',
      'Struktur lengkapnya: <code>try</code> (kode yang mungkin gagal), <code>except</code> (penanganan), <code>else</code> (jalan jika tidak ada error), dan <code>finally</code> (selalu jalan). Tangkap exception yang spesifik; <code>except:</code> kosong bisa menyembunyikan bug.'],
   code:R`class SaldoKurang(Exception):
    def __init__(self, kurang):
        super().__init__(f"saldo kurang Rp{kurang:,}")
        self.kurang = kurang

saldo = 50_000

def tarik(jumlah):
    global saldo
    if jumlah <= 0:
        raise ValueError("jumlah harus positif")
    if jumlah > saldo:
        raise SaldoKurang(jumlah - saldo)
    saldo -= jumlah

def layani(jumlah):
    print("memproses", jumlah)
    tarik(jumlah)
    print("berhasil")

for j in [20_000, 80_000, -5]:
    try:
        layani(j)
    except SaldoKurang as e:
        print("gagal:", e)
    except ValueError as e:
        print("input salah:", e)
    else:
        print("transaksi tercatat")
    finally:
        print("sisa", saldo)`,
   out:`memproses 20000
berhasil
transaksi tercatat
sisa 30000
memproses 80000
gagal: saldo kurang Rp50,000
sisa 30000
memproses -5
input salah: jumlah harus positif
sisa 30000
`,
   pts:['<code>raise</code> melempar exception.','Exception buatan sendiri: <code>class NamaError(Exception)</code>.','else jalan jika tidak ada error, finally selalu jalan.','Tangkap jenis exception yang spesifik.'],
   q:[['Blok yang dijalankan hanya jika try sukses?',['except','else','finally'],1,'else melengkapi try saat tidak ada exception.'],
      ['Exception yang tidak ditangkap di fungsi akan?',['Diabaikan','Naik ke pemanggil','Mengulang fungsi'],1,'Ia naik terus sampai ada except yang cocok.']]},
  {k:'c',t:'Context manager: with',nodes:['Context Manager','File Handling'],
   b:['Sumber daya seperti file, koneksi database, atau kunci (lock) harus selalu ditutup, bahkan ketika terjadi error. Pernyataan <code>with</code> menjamin hal itu: saat blok selesai, dengan cara apa pun, sumber daya dibereskan otomatis.',
      'Objek yang bisa dipakai dengan <code>with</code> disebut <b>context manager</b>. Ia punya method <code>__enter__</code> (dijalankan saat masuk) dan <code>__exit__</code> (dijalankan saat keluar). Cara lebih singkat untuk membuatnya adalah dekorator <code>@contextmanager</code> dari modul <code>contextlib</code>: kode sebelum <code>yield</code> adalah persiapan, sesudahnya adalah pembersihan.',
      'Kamu bisa membuka beberapa context manager sekaligus dalam satu <code>with</code>, misalnya membaca satu file dan menulis ke file lain.'],
   code:R`from contextlib import contextmanager
import time

with open("catatan.txt", "w") as f:
    f.write("baris 1\nbaris 2\n")
print(f.closed)

with open("catatan.txt") as sumber, open("salinan.txt", "w") as tujuan:
    for baris in sumber:
        tujuan.write(baris.upper())
print(open("salinan.txt").read().strip())

@contextmanager
def stopwatch(label):
    mulai = time.perf_counter()
    print(f"[{label}] mulai")
    try:
        yield
    finally:
        print(f"[{label}] selesai")

with stopwatch("hitung"):
    total = sum(range(1_000_000))
print(total)

class Kunci:
    def __enter__(self):
        print("kunci dipasang"); return self
    def __exit__(self, tipe, nilai, jejak):
        print("kunci dilepas", tipe.__name__ if tipe else "tanpa error")
        return True                          # telan exception

with Kunci():
    1 / 0
print("program lanjut")`,
   out:`True
BARIS 1
BARIS 2
[hitung] mulai
[hitung] selesai
499999500000
kunci dipasang
kunci dilepas ZeroDivisionError
program lanjut
`,
   pts:['<code>with</code> menjamin pembersihan meski ada error.','Context manager = <code>__enter__</code> + <code>__exit__</code>.','<code>@contextmanager</code>: persiapan → yield → pembersihan.','<code>__exit__</code> yang mengembalikan True menelan exception.'],
   q:[['Setelah blok <code>with open(...) as f</code> selesai, file?',['Masih terbuka','Tertutup otomatis','Terhapus'],1,'Itulah tujuan with.'],
      ['Method yang dipanggil saat keluar dari with?',['__enter__','__exit__','__close__'],1,'__exit__ menerima info exception jika ada.']]},
  {k:'c',t:'pathlib & modul glob',nodes:['Glob Module','File Handling'],
   b:['Modul <code>pathlib</code> menyediakan objek <code>Path</code> untuk mengelola lokasi file dengan cara yang rapi dan lintas sistem operasi. Gabungkan path dengan operator <code>/</code>, ambil nama file dengan <code>.name</code>, ekstensi dengan <code>.suffix</code>, dan baca tulis dengan <code>read_text</code>/<code>write_text</code>.',
      'Untuk mencari banyak file sekaligus dengan pola, pakai <b>glob</b>. Tanda <code>*</code> cocok dengan apa saja, <code>?</code> satu karakter, dan <code>**</code> masuk ke semua subfolder. Tersedia sebagai modul <code>glob</code> dan juga method <code>Path.glob</code>/<code>rglob</code>.',
      'Contoh kebutuhan nyata: mengumpulkan semua laporan CSV di folder bulanan, mengganti nama foto secara massal, atau menghapus file sementara.'],
   code:R`from pathlib import Path
import glob

folder = Path("laporan")
folder.mkdir(exist_ok=True)
for bulan in ["jan", "feb", "mar"]:
    (folder / f"penjualan_{bulan}.csv").write_text("produk,jumlah\nkopi,10\n")
(folder / "catatan.txt").write_text("rahasia")

csv = sorted(folder.glob("*.csv"))
print([p.name for p in csv])
print(csv[0].stem, csv[0].suffix)

print(sorted(glob.glob("laporan/penjualan_?a?.csv")))

total = sum(len(p.read_text().splitlines()) - 1 for p in csv)
print("total baris data:", total)

for p in folder.iterdir():
    p.unlink()
folder.rmdir()
print(folder.exists())`,
   out:`['penjualan_feb.csv', 'penjualan_jan.csv', 'penjualan_mar.csv']
penjualan_feb .csv
['laporan/penjualan_jan.csv', 'laporan/penjualan_mar.csv']
total baris data: 3
False
`,
   pts:['<code>Path("a") / "b.txt"</code> menggabung path.','<code>.name</code>, <code>.stem</code>, <code>.suffix</code> untuk bagian nama.','Pola glob: <code>*</code>, <code>?</code>, <code>**</code>.','<code>rglob</code> mencari di semua subfolder.'],
   q:[['Pola glob untuk semua file CSV?',['*.csv','%.csv','csv*'],0,'Bintang cocok dengan nama apa pun.'],
      ['<code>Path("data/laporan.csv").suffix</code>?',['"laporan"','".csv"','"data"'],1,'suffix adalah ekstensi termasuk titiknya.']]}
 ]},
{t:'Modul, paket & lingkungan',lvl:'Menengah',d:'Import, pustaka standar, pip, PyPI, virtual environment, dan alat pengelola proyek modern.',
 nodes:['Modules','Builtin Modules','Custom Modules','Common Packages and Modules','Package Managers','Pip','PyPI','Conda','Poetry','pipenv','PDM','uv','virtualenv','pyenv','pyproject.toml'],
 lessons:[
  {k:'c',t:'Import & modul buatan sendiri',nodes:['Modules','Custom Modules'],
   b:['Setiap file <code>.py</code> adalah <b>modul</b>. Kamu bisa memakai fungsi dari file lain dengan <code>import</code>. Folder berisi beberapa modul disebut <b>paket</b> (package). Memecah program ke beberapa modul membuat kode lebih teratur dan bisa dipakai ulang.',
      'Ada beberapa gaya import: <code>import math</code> (pakai sebagai <code>math.sqrt</code>), <code>from math import sqrt</code> (langsung <code>sqrt</code>), dan <code>import numpy as np</code> (dengan nama alias). Hindari <code>from x import *</code> karena nama-nama bisa bertabrakan diam-diam.',
      'Setiap modul punya variabel <code>__name__</code>. Nilainya <code>"__main__"</code> jika file dijalankan langsung, dan nama modulnya jika diimpor. Itu sebabnya kode uji coba ditaruh di dalam <code>if __name__ == "__main__":</code>.'],
   code:R`# File: toko/harga.py
PAJAK = 0.11

def dengan_pajak(harga):
    return round(harga * (1 + PAJAK))

def rupiah(n):
    return f"Rp{n:,}".replace(",", ".")

if __name__ == "__main__":
    print("uji:", rupiah(dengan_pajak(10000)))   # hanya saat dijalankan langsung

# File: toko/__init__.py   (boleh kosong, menandai folder sebagai paket)

# File: main.py
from toko.harga import dengan_pajak, rupiah
import toko.harga as h

print(rupiah(dengan_pajak(85000)))
print(h.PAJAK)
# Keluaran:
# Rp94.350
# 0.11`,
   out:null,
   pts:['Satu file = satu modul, satu folder = paket.','<code>import x as y</code> memberi alias.','Blok <code>if __name__ == "__main__":</code> tidak jalan saat diimpor.','Python mencari modul di folder kerja, lalu di site-packages.'],
   q:[['Nilai <code>__name__</code> saat file dijalankan langsung?',['Nama file','"__main__"','None'],1,'Itulah kenapa pola if __name__ == "__main__" bekerja.'],
      ['Kenapa <code>from x import *</code> sebaiknya dihindari?',['Lambat','Nama bisa bertabrakan tanpa ketahuan','Tidak didukung'],1,'Sumber setiap nama jadi tidak jelas.']]},
  {k:'c',t:'Modul bawaan yang sering dipakai',nodes:['Builtin Modules','Common Packages and Modules'],
   b:['Python dijuluki "batteries included" karena pustaka standarnya sangat lengkap. Sebelum memasang paket dari luar, cek dulu apakah modul bawaan sudah cukup.',
      'Yang paling sering dipakai: <code>math</code> (fungsi matematika), <code>random</code> (angka dan pilihan acak), <code>datetime</code> (tanggal dan waktu), <code>json</code> (membaca dan menulis JSON), <code>os</code> dan <code>sys</code> (sistem operasi dan interpreter), <code>collections</code> (Counter, deque, defaultdict), <code>itertools</code> (kombinasi dan permutasi), <code>statistics</code>, serta <code>csv</code>.',
      'Paket pihak ketiga yang populer: <b>requests</b> (HTTP), <b>pandas</b> (analisis data), <b>numpy</b> (komputasi angka), <b>matplotlib</b> (grafik), dan <b>pytest</b> (testing). Semuanya dipasang dengan pip.'],
   code:R`import math, random, json, statistics, itertools
from datetime import date, timedelta

print(math.sqrt(144), math.pi.__round__(4), math.factorial(5))

random.seed(42)
print(random.randint(1, 6), random.choice(["kopi", "teh", "jus"]))

hari_ini = date(2024, 10, 28)
print(hari_ini + timedelta(days=5), hari_ini.strftime("%d/%m/%Y"))

data = {"nama": "Rina", "nilai": [80, 92]}
teks = json.dumps(data)
print(teks, json.loads(teks)["nilai"][1])

print(statistics.mean([80, 92, 75]), statistics.median([80, 92, 75]))
print(list(itertools.combinations("ABC", 2)))`,
   out:`12.0 3.1416 120
6 kopi
2024-11-02 28/10/2024
{"nama": "Rina", "nilai": [80, 92]} 92
82.33333333333333 80
[('A', 'B'), ('A', 'C'), ('B', 'C')]
`,
   pts:['Cek pustaka standar sebelum memasang paket.','<code>json.dumps</code>/<code>loads</code>: dict ↔ teks JSON.','<code>random.seed</code> membuat hasil acak bisa diulang.','<code>datetime.timedelta</code> untuk menambah hari.'],
   q:[['Modul untuk mengubah dict menjadi teks JSON?',['pickle','json','csv'],1,'json.dumps menghasilkan string JSON.'],
      ['Fungsi agar hasil random sama setiap kali dijalankan?',['random.fix()','random.seed()','random.same()'],1,'Seed menetapkan titik awal generator.']]},
  {k:'c',t:'pip, PyPI & virtual environment',nodes:['Package Managers','Pip','PyPI','virtualenv','uv'],
   b:['<b>PyPI</b> (Python Package Index) adalah gudang ratusan ribu paket Python. <b>pip</b> adalah alat bawaan untuk memasangnya: <code>pip install requests</code>. Daftar dependensi proyek biasanya dicatat di <code>requirements.txt</code>.',
      'Masalahnya, jika semua proyek memasang paket ke tempat yang sama, versi bisa bentrok: proyek A butuh Django 4, proyek B butuh Django 5. <b>Virtual environment</b> (venv) memberi setiap proyek folder paketnya sendiri yang terisolasi. Aktifkan sebelum memasang paket.',
      '<b>uv</b> adalah pengelola paket modern yang ditulis dengan Rust dan jauh lebih cepat dari pip. Ia bisa membuat venv, memasang paket, bahkan memasang versi Python sendiri. <b>virtualenv</b> adalah pendahulu venv yang masih banyak dipakai.'],
   code:R`# 1. Buat dan aktifkan virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. Pasang paket dari PyPI
pip install requests==2.32.3
pip list
pip freeze > requirements.txt      # catat versi persis

# 3. Di komputer lain / server
pip install -r requirements.txt

# Cara modern dengan uv (jauh lebih cepat)
uv venv
uv pip install requests
uv add pandas                      # tambah ke pyproject.toml
uv run main.py

deactivate                         # keluar dari venv`,
   out:null,lang:'text',
   pts:['Satu proyek = satu virtual environment.','<code>requirements.txt</code> mencatat dependensi.','Jangan commit folder <code>.venv</code> ke Git.','uv: alternatif pip yang sangat cepat.'],
   q:[['Kenapa memakai virtual environment?',['Agar Python lebih cepat','Agar paket tiap proyek tidak bentrok','Wajib untuk pip'],1,'Setiap proyek punya versi paketnya sendiri.'],
      ['Perintah memasang semua paket dari requirements.txt?',['pip install requirements.txt','pip install -r requirements.txt','pip get -all'],1,'-r membaca daftar dari file.']]},
  {k:'c',t:'pyproject.toml, Poetry, pipenv, PDM, Conda, pyenv',nodes:['pyproject.toml','Poetry','pipenv','PDM','Conda','pyenv'],
   b:['<code>pyproject.toml</code> adalah standar modern untuk mendeskripsikan proyek Python dalam satu file: nama, versi, dependensi, dan konfigurasi alat seperti ruff atau pytest. Hampir semua alat baru membaca file ini.',
      '<b>Poetry</b>, <b>PDM</b>, dan <b>pipenv</b> adalah pengelola proyek yang menggabungkan virtual environment, pemasangan paket, dan <i>lock file</i> (daftar versi persis semua paket termasuk turunannya) agar hasil instalasi sama di semua komputer.',
      '<b>Conda</b> populer di dunia data science karena juga bisa memasang pustaka non-Python seperti CUDA. <b>pyenv</b> berbeda fungsinya: ia mengelola banyak versi Python di satu komputer, misalnya 3.11 untuk proyek lama dan 3.13 untuk proyek baru.'],
   code:R`# pyproject.toml
[project]
name = "toko-nusantara"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.32",
    "pydantic>=2.7",
]

[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.5"]

[tool.ruff]
line-length = 100

# Perintah setara di beberapa alat
poetry add requests          # Poetry
pdm add requests             # PDM
pipenv install requests      # pipenv
conda install pandas         # Conda
pyenv install 3.13.0         # pasang versi Python
pyenv local 3.13.0           # pakai versi ini di folder proyek`,
   out:null,lang:'text',
   pts:['pyproject.toml = satu file konfigurasi proyek.','Lock file menjamin versi paket identik.','Conda untuk data science dengan pustaka non-Python.','pyenv mengelola versi Python, bukan paket.'],
   q:[['Alat untuk berpindah antar versi Python?',['pip','pyenv','Poetry'],1,'pyenv memasang dan memilih versi interpreter.'],
      ['Fungsi lock file?',['Mengunci file agar tidak dibaca','Mencatat versi persis semua paket','Mempercepat Python'],1,'Instalasi jadi bisa diulang dengan hasil sama.']]}
 ]},
{t:'OOP di Python',lvl:'Menengah',d:'Kelas, objek, pewarisan, enkapsulasi, dunder method, dan paradigma pemrograman.',
 nodes:['OOP','Classes','Inheritance','Encapsulation','Methods and Dunder Methods','Paradigms'],
 lessons:[
  {k:'lab',n:8,nodes:['OOP','Classes']},
  {k:'topic',ref:'8.0',nodes:['Classes']},
  {k:'topic',ref:'8.1',nodes:['Encapsulation']},
  {k:'c',t:'Enkapsulasi: property & dataclass',nodes:['Encapsulation','Classes'],
   b:['Python tidak punya kata kunci <code>private</code>. Konvensinya: nama yang diawali satu garis bawah (<code>_saldo</code>) berarti "internal, jangan disentuh dari luar". Dua garis bawah (<code>__pin</code>) membuat Python mengganti namanya (name mangling) sehingga lebih sulit diakses tanpa sengaja.',
      '<b>@property</b> membuat method bisa diakses seperti atribut, sekaligus memberi tempat untuk validasi. Pengguna kelas menulis <code>akun.saldo</code>, tetapi di balik layar ada logika yang menjaga aturan.',
      '<b>@dataclass</b> menulis otomatis <code>__init__</code>, <code>__repr__</code>, dan <code>__eq__</code> untuk kelas pembawa data. Tambahkan <code>frozen=True</code> agar objeknya tidak bisa diubah (immutable).'],
   code:R`from dataclasses import dataclass, field

class Rekening:
    def __init__(self, pemilik):
        self.pemilik = pemilik
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            raise ValueError("saldo tidak boleh negatif")
        self._saldo = nilai

r = Rekening("Andi")
r.saldo = 75_000
print(r.saldo)
try:
    r.saldo = -1
except ValueError as e:
    print(e)

@dataclass
class Produk:
    nama: str
    harga: int
    tag: list = field(default_factory=list)

@dataclass(frozen=True)
class Titik:
    x: int
    y: int

p = Produk("Kopi Gayo", 85000)
print(p)
print(p == Produk("Kopi Gayo", 85000))
t = Titik(1, 2)
try:
    t.x = 5
except Exception as e:
    print(type(e).__name__)`,
   out:`75000
saldo tidak boleh negatif
Produk(nama='Kopi Gayo', harga=85000, tag=[])
True
FrozenInstanceError
`,
   pts:['<code>_nama</code> = konvensi internal.','<code>@property</code> + setter untuk validasi.','<code>@dataclass</code> mengurangi kode boilerplate.','<code>frozen=True</code> membuat objek immutable.'],
   q:[['Apa yang dibuat otomatis oleh @dataclass?',['__init__, __repr__, __eq__','Database','Koneksi internet'],0,'Ketiganya dibuat dari anotasi field.'],
      ['Arti garis bawah di depan nama atribut (<code>_saldo</code>)?',['Error','Konvensi: internal, jangan diakses dari luar','Atribut statis'],1,'Python mengandalkan kesepakatan.']]},
  {k:'c',t:'Dunder method: membuat objek terasa bawaan',nodes:['Methods and Dunder Methods'],
   b:['<b>Dunder method</b> (double underscore) adalah method khusus dengan nama diapit dua garis bawah, seperti <code>__init__</code>. Python memanggilnya secara otomatis untuk operasi tertentu. Dengan mengisinya, objek buatanmu bisa dipakai seperti tipe bawaan.',
      '<code>__str__</code> menentukan tampilan untuk <code>print</code>, <code>__repr__</code> untuk tampilan debug. <code>__len__</code> membuat <code>len(obj)</code> bekerja, <code>__getitem__</code> membuat <code>obj[i]</code> bekerja, dan <code>__iter__</code> membuat objek bisa dipakai di for.',
      'Operator juga punya dunder: <code>__add__</code> untuk +, <code>__eq__</code> untuk ==, <code>__lt__</code> untuk &lt; (yang juga membuat <code>sorted</code> bekerja). Teknik ini disebut <i>operator overloading</i>.'],
   code:R`class Uang:
    def __init__(self, rupiah):
        self.rupiah = rupiah
    def __str__(self):
        return f"Rp{self.rupiah:,}".replace(",", ".")
    def __repr__(self):
        return f"Uang({self.rupiah})"
    def __add__(self, lain):
        return Uang(self.rupiah + lain.rupiah)
    def __eq__(self, lain):
        return self.rupiah == lain.rupiah
    def __lt__(self, lain):
        return self.rupiah < lain.rupiah

class Keranjang:
    def __init__(self):
        self.isi = []
    def tambah(self, nama, harga):
        self.isi.append((nama, Uang(harga)))
    def __len__(self):
        return len(self.isi)
    def __getitem__(self, i):
        return self.isi[i]
    def __iter__(self):
        return iter(self.isi)

k = Keranjang()
k.tambah("kopi", 85000)
k.tambah("teh", 25000)
print(len(k), k[1][0])
total = Uang(0)
for nama, harga in k:
    total = total + harga
print(total)
print(sorted([Uang(5), Uang(2), Uang(9)]))
print(Uang(100) == Uang(100))`,
   out:`2 teh
Rp110.000
[Uang(2), Uang(5), Uang(9)]
True
`,
   pts:['<code>__str__</code> untuk pengguna, <code>__repr__</code> untuk programmer.','<code>__len__</code>, <code>__getitem__</code>, <code>__iter__</code> membuat objek mirip koleksi.','<code>__add__</code>, <code>__eq__</code>, <code>__lt__</code> untuk operator.','Jangan memanggil dunder langsung; biarkan Python yang memanggil.'],
   q:[['Dunder yang dipanggil oleh <code>len(obj)</code>?',['__size__','__len__','__count__'],1,'len() memanggil obj.__len__().'],
      ['Supaya <code>sorted</code> bisa mengurutkan objekmu, minimal isi?',['__lt__','__add__','__str__'],0,'sorted membandingkan dengan operator <.']]},
  {k:'lab',n:9,nodes:['Inheritance']},
  {k:'topic',ref:'9.0',nodes:['Inheritance']},
  {k:'topic',ref:'9.1',nodes:['Inheritance']},
  {k:'c',t:'Paradigma: prosedural, OOP, fungsional',nodes:['Paradigms'],
   b:['<b>Paradigma</b> adalah gaya berpikir dalam menyusun program. Python mendukung beberapa paradigma sekaligus, dan programmer berpengalaman memilih yang paling cocok untuk masalahnya.',
      '<b>Prosedural</b>: program adalah urutan langkah dan fungsi yang mengolah data. Cocok untuk skrip dan otomasi. <b>Berorientasi objek</b>: data dan perilakunya dibungkus dalam objek. Cocok untuk sistem dengan banyak entitas seperti toko, game, atau aplikasi bank. <b>Fungsional</b>: program dibangun dari fungsi murni tanpa efek samping, memakai map, filter, dan komposisi. Cocok untuk transformasi data.',
      'Masalah yang sama bisa diselesaikan dengan ketiga gaya. Perhatikan contoh di bawah: ketiganya menghitung total belanja barang yang harganya di atas 20 ribu.'],
   code:R`belanja = [("kopi", 85000), ("keripik", 15000), ("madu", 120000)]

# 1. Prosedural
total = 0
for nama, harga in belanja:
    if harga > 20000:
        total += harga
print("prosedural:", total)

# 2. Berorientasi objek
class Keranjang:
    def __init__(self, isi):
        self.isi = isi
    def total_di_atas(self, batas):
        return sum(h for _, h in self.isi if h > batas)
print("OOP:", Keranjang(belanja).total_di_atas(20000))

# 3. Fungsional
from functools import reduce
mahal = filter(lambda b: b[1] > 20000, belanja)
print("fungsional:", reduce(lambda a, b: a + b, map(lambda b: b[1], mahal), 0))`,
   out:`prosedural: 205000
OOP: 205000
fungsional: 205000
`,
   pts:['Prosedural: langkah demi langkah.','OOP: data + perilaku dalam objek.','Fungsional: fungsi murni dan transformasi data.','Python multi-paradigma: campur sesuai kebutuhan.'],
   q:[['Paradigma yang menekankan fungsi tanpa efek samping?',['Prosedural','OOP','Fungsional'],2,'Fungsi murni hanya bergantung pada input.'],
      ['Untuk sistem dengan banyak entitas yang punya data dan perilaku, gaya yang cocok?',['OOP','Assembly','Prosedural saja'],0,'Objek memodelkan entitas.']]}
 ]},
{t:'Python idiomatik',lvl:'Menengah',d:'Comprehension, iterator, generator, lambda, decorator, dan regex.',
 nodes:['List Comprehensions','Iterators','Generator Expressions','Lambdas','Decorators','Regular Expressions'],
 lessons:[
  {k:'c',t:'List, dict & set comprehension',nodes:['List Comprehensions'],viz:'stream',
   b:['<b>Comprehension</b> adalah cara Pythonic membuat koleksi baru dari koleksi lain dalam satu baris: <code>[ekspresi for item in data if syarat]</code>. Bacanya seperti kalimat: "ambil ekspresi untuk setiap item di data, jika syarat terpenuhi".',
      'Bentuk yang sama tersedia untuk dictionary <code>{k: v for ...}</code> dan set <code>{x for ...}</code>. Comprehension biasanya lebih cepat dan lebih mudah dibaca daripada loop dengan <code>append</code>.',
      'Tapi jangan berlebihan. Jika comprehension butuh dua loop bersarang dan beberapa syarat, tulis ulang sebagai loop biasa demi keterbacaan.'],
   code:R`harga = {"kopi": 85000, "teh": 25000, "keripik": 15000, "madu": 120000}

kuadrat = [n * n for n in range(1, 6)]
print(kuadrat)

mahal = [nama for nama, h in harga.items() if h > 50000]
print(mahal)

diskon = {nama: h * 9 // 10 for nama, h in harga.items()}
print(diskon["kopi"])

huruf_awal = {nama[0] for nama in harga}
print(sorted(huruf_awal))

label = ["genap" if n % 2 == 0 else "ganjil" for n in range(4)]
print(label)

matriks = [[1, 2, 3], [4, 5, 6]]
print([x for baris in matriks for x in baris])`,
   out:`[1, 4, 9, 16, 25]
['kopi', 'madu']
76500
['k', 'm', 't']
['genap', 'ganjil', 'genap', 'ganjil']
[1, 2, 3, 4, 5, 6]
`,
   pts:['<code>[f(x) for x in data if syarat(x)]</code>.','Dict comprehension: <code>{k: v for ...}</code>.','if di akhir = saring; if-else di depan = pilih nilai.','Utamakan keterbacaan.'],
   q:[['Hasil <code>[x*2 for x in [1,2,3] if x != 2]</code>?',['[2, 4, 6]','[2, 6]','[1, 3]'],1,'2 disaring, lalu 1 dan 3 dikali dua.'],
      ['Kurung untuk set comprehension?',['[ ]','{ } tanpa titik dua','( )'],1,'Kurung kurawal tanpa pasangan kunci:nilai.']]},
  {k:'c',t:'Iterator & generator',nodes:['Iterators','Generator Expressions'],viz:'stream',
   b:['<b>Iterator</b> adalah objek yang memberikan elemen satu per satu lewat <code>next()</code>, dan melempar <code>StopIteration</code> jika habis. Loop for bekerja di atas protokol ini: ia memanggil <code>iter()</code> sekali lalu <code>next()</code> berulang kali.',
      '<b>Generator</b> adalah cara termudah membuat iterator: fungsi biasa yang memakai <code>yield</code> alih-alih return. Setiap kali <code>next()</code> dipanggil, fungsi berjalan sampai <code>yield</code> berikutnya, menyerahkan nilai, lalu <b>berhenti sejenak</b> sambil mengingat posisinya.',
      'Generator bersifat malas (lazy): nilai dibuat hanya saat diminta. Karena itu generator bisa mewakili deret tak hingga atau file berukuran gigabyte tanpa menghabiskan memori. <b>Generator expression</b> ditulis seperti list comprehension tetapi dengan kurung biasa: <code>(x*x for x in data)</code>.'],
   code:R`import sys

def hitung_mundur(n):
    print("mulai")
    while n > 0:
        yield n
        n -= 1
    print("habis")

g = hitung_mundur(3)
print(next(g))
print(next(g))
for x in g:
    print("loop", x)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(8)])

daftar = [x * x for x in range(100_000)]
gen = (x * x for x in range(100_000))
print(sys.getsizeof(daftar) > 100_000, sys.getsizeof(gen) < 1000)
print(sum(gen))`,
   out:`mulai
3
2
loop 1
habis
[0, 1, 1, 2, 3, 5, 8, 13]
True True
333328333350000
`,
   pts:['Iterator: <code>iter()</code> lalu <code>next()</code> sampai StopIteration.','<code>yield</code> menyerahkan nilai dan menjeda fungsi.','Generator hemat memori karena lazy.','Generator hanya bisa dilalui sekali.'],
   q:[['Apa yang dilakukan <code>yield</code>?',['Mengakhiri fungsi','Menyerahkan nilai lalu menjeda fungsi','Mencetak nilai'],1,'Fungsi melanjutkan dari titik yang sama saat next() berikutnya.'],
      ['Keunggulan generator dibanding list?',['Bisa diakses dengan indeks','Hemat memori karena nilai dibuat saat dibutuhkan','Bisa diulang berkali-kali'],1,'Nilai tidak disimpan semuanya sekaligus.']]},
  {k:'lab',n:19,nodes:['Lambdas']},
  {k:'topic',ref:'19.0',nodes:['Lambdas']},
  {k:'topic',ref:'19.1',nodes:['Lambdas']},
  {k:'c',t:'Decorator',nodes:['Decorators'],viz:'decorator',
   b:['<b>Decorator</b> adalah fungsi yang menerima fungsi lain lalu mengembalikan versi yang "dibungkus" dengan perilaku tambahan, tanpa mengubah kode aslinya. Contoh kegunaannya: mencatat log, mengukur waktu, memeriksa login, atau menyimpan hasil (cache).',
      'Menulis <code>@catat</code> di atas <code>def bayar</code> sama artinya dengan <code>bayar = catat(bayar)</code>. Decorator bekerja berkat dua sifat Python: fungsi adalah objek yang bisa dioper, dan closure yang mengingat fungsi asli.',
      'Gunakan <code>functools.wraps</code> di dalam decorator agar nama dan dokumentasi fungsi asli tetap terjaga. Pustaka standar juga punya decorator siap pakai seperti <code>@functools.lru_cache</code> untuk menyimpan hasil pemanggilan.'],
   code:R`import functools, time

def catat(fungsi):
    @functools.wraps(fungsi)
    def pembungkus(*args, **kwargs):
        print(f"-> {fungsi.__name__}{args}")
        hasil = fungsi(*args, **kwargs)
        print(f"<- {hasil}")
        return hasil
    return pembungkus

def ulangi(n):                      # decorator dengan parameter
    def dekor(fungsi):
        @functools.wraps(fungsi)
        def pembungkus(*args):
            return [fungsi(*args) for _ in range(n)]
        return pembungkus
    return dekor

@catat
def bayar(harga, diskon=0):
    return harga - diskon

bayar(85000, 5000)
print(bayar.__name__)

@ulangi(3)
def sapa(nama):
    return f"hai {nama}"
print(sapa("Rina"))

@functools.lru_cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(80))`,
   out:`-> bayar(85000, 5000)
<- 80000
bayar
['hai Rina', 'hai Rina', 'hai Rina']
23416728348467685
`,
   pts:['<code>@d</code> di atas fungsi = <code>f = d(f)</code>.','Decorator mengembalikan fungsi pembungkus.','<code>functools.wraps</code> menjaga nama fungsi asli.','<code>lru_cache</code> mempercepat fungsi rekursif yang berulang.'],
   q:[['<code>@catat</code> di atas <code>def f</code> setara dengan?',['catat()','f = catat(f)','f.catat()'],1,'Decorator hanyalah gula sintaks.'],
      ['Decorator bawaan untuk menyimpan hasil pemanggilan fungsi?',['@property','@lru_cache','@staticmethod'],1,'lru_cache adalah memoization siap pakai.']]},
  {k:'c',t:'Regular expression (modul re)',nodes:['Regular Expressions'],
   b:['<b>Regular expression</b> adalah bahasa mini untuk mencari pola di teks. Modul <code>re</code> menyediakan fungsi utama: <code>re.search</code> (cari kecocokan pertama), <code>re.findall</code> (ambil semua), <code>re.sub</code> (ganti), <code>re.fullmatch</code> (seluruh teks harus cocok), dan <code>re.split</code>.',
      'Simbol dasar: <code>\\d</code> angka, <code>\\w</code> huruf/angka/garis bawah, <code>\\s</code> spasi, <code>+</code> satu atau lebih, <code>*</code> nol atau lebih, <code>{n}</code> tepat n kali, <code>[...]</code> salah satu karakter, <code>^</code> awal, <code>$</code> akhir. Kurung <code>( )</code> membuat grup yang bisa diambil.',
      'Tulis pola sebagai <b>raw string</b> <code>r"..."</code> agar garis miring terbalik tidak perlu digandakan. Grup bernama <code>(?P&lt;nama&gt;...)</code> membuat hasil lebih mudah dibaca.'],
   code:R`import re

teks = "Hubungi 0812-3456-7890 atau 0857-1111-2222 sebelum 28/10/2024"
print(re.findall(r"\d{4}-\d{4}-\d{4}", teks))

m = re.search(r"(?P<tgl>\d{2})/(?P<bln>\d{2})/(?P<thn>\d{4})", teks)
print(m.group("thn"), m.group("bln"))

print(re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", teks)[-10:])

email = "rina@kampus.ac.id"
print(bool(re.fullmatch(r"[\w.]+@[\w.]+\.[a-z]{2,}", email)))

print(re.split(r"\s*[,;]\s*", "kopi , teh;madu"))`,
   out:`['0812-3456-7890', '0857-1111-2222']
2024 10
2024-10-28
True
['kopi', 'teh', 'madu']
`,
   pts:['Selalu tulis pola sebagai raw string <code>r"..."</code>.','<code>findall</code> untuk semua kecocokan, <code>search</code> untuk yang pertama.','<code>re.sub</code> bisa memakai grup <code>\\1</code>, <code>\\2</code>.','Grup bernama membuat hasil mudah dibaca.'],
   q:[['Fungsi untuk mengambil semua kecocokan?',['re.search','re.findall','re.match'],1,'findall mengembalikan list semua kecocokan.'],
      ['Kenapa pola ditulis <code>r"..."</code>?',['Lebih cepat','Agar backslash tidak perlu digandakan','Wajib di Python 3'],1,'Raw string tidak memproses escape.']]}
 ]},
{t:'Rekursi & algoritma',lvl:'Menengah',d:'Berpikir rekursif, mencari, mengurutkan, dan Big-O.',
 nodes:['Recursion','Sorting Algorithms','Data Structures and Algorithms'],
 lessons:[
  {k:'lab',n:12,nodes:['Recursion']},{k:'topic',ref:'12.0',nodes:['Recursion']},{k:'topic',ref:'12.1',nodes:['Recursion']},
  {k:'lab',n:13,nodes:['Sorting Algorithms']},{k:'topic',ref:'13.0',nodes:['Data Structures and Algorithms']},{k:'topic',ref:'13.1',nodes:['Sorting Algorithms']},{k:'topic',ref:'13.2',nodes:['Data Structures and Algorithms']}
 ]},
{t:'Struktur data & algoritma',lvl:'Lanjutan',d:'Stack, queue, linked list, pohon biner, hash map, dan heap, dibangun sendiri lalu dipakai dari pustaka.',
 nodes:['Data Structures and Algorithms','Arrays and Linked lists','Hash Tables','Heaps, Stacks and Queues','Binary Search Trees'],
 lessons:[
  {k:'lab',n:14,nodes:['Heaps, Stacks and Queues']},{k:'topic',ref:'14.0',nodes:['Heaps, Stacks and Queues']},{k:'topic',ref:'14.1',nodes:['Heaps, Stacks and Queues']},
  {k:'lab',n:15,nodes:['Arrays and Linked lists']},{k:'topic',ref:'15.0'},{k:'topic',ref:'15.1'},
  {k:'lab',n:16,nodes:['Arrays and Linked lists']},{k:'topic',ref:'16.0',nodes:['Arrays and Linked lists']},{k:'topic',ref:'16.1',nodes:['Arrays and Linked lists']},
  {k:'lab',n:17,nodes:['Binary Search Trees']},{k:'topic',ref:'17.0',nodes:['Binary Search Trees']},{k:'topic',ref:'17.1',nodes:['Binary Search Trees']},
  {k:'lab',n:18,nodes:['Hash Tables','Heaps, Stacks and Queues']},{k:'topic',ref:'18.0',nodes:['Hash Tables']},{k:'topic',ref:'18.1',nodes:['Heaps, Stacks and Queues']},
  {k:'c',t:'deque, heapq & bisect: struktur data siap pakai',nodes:['Heaps, Stacks and Queues','Data Structures and Algorithms'],
   b:['Setelah memahami cara kerja struktur data dari nol, saatnya memakai versi siap pakai yang cepat dari pustaka standar. <code>collections.deque</code> adalah antrean dua ujung dengan operasi tambah dan ambil di ujung mana pun dalam waktu O(1). Jangan memakai <code>list.pop(0)</code> untuk antrean karena O(n).',
      '<code>heapq</code> mengubah list biasa menjadi <b>min-heap</b>: elemen terkecil selalu di indeks 0. Cocok untuk priority queue, misalnya memproses pesanan paling mendesak atau mencari k nilai terbesar dengan <code>nlargest</code>.',
      '<code>bisect</code> melakukan binary search pada list yang sudah urut, untuk mencari posisi sisip atau menyisipkan sambil menjaga urutan.'],
   code:R`from collections import deque
import heapq, bisect

antre = deque(["Ani", "Bayu"])
antre.append("Citra")
antre.appendleft("VIP")
print(antre.popleft(), list(antre))

riwayat = deque(maxlen=3)
for hal in ["beranda", "produk", "keranjang", "bayar"]:
    riwayat.append(hal)
print(list(riwayat))

tugas = []
heapq.heappush(tugas, (2, "balas email"))
heapq.heappush(tugas, (1, "server mati"))
heapq.heappush(tugas, (3, "rapat"))
print(heapq.heappop(tugas))
print(heapq.nlargest(2, [70, 95, 88, 60, 91]))

nilai = [55, 70, 85, 90]
print(bisect.bisect_left(nilai, 80))
bisect.insort(nilai, 80)
print(nilai)`,
   out:`VIP ['Ani', 'Bayu', 'Citra']
['produk', 'keranjang', 'bayar']
(1, 'server mati')
[95, 91]
2
[55, 70, 80, 85, 90]
`,
   pts:['<code>deque</code> untuk antrean, bukan <code>list.pop(0)</code>.','<code>deque(maxlen=n)</code> menyimpan n item terakhir.','<code>heapq</code> = min-heap; simpan tuple (prioritas, data).','<code>bisect</code> = binary search pada list urut.'],
   q:[['Kenapa <code>list.pop(0)</code> lambat untuk antrean besar?',['Semua elemen digeser: O(n)','Karena list immutable','Tidak lambat'],0,'deque.popleft() O(1).'],
      ['<code>heapq.heappop</code> mengambil elemen?',['Terbesar','Terkecil','Terakhir masuk'],1,'heapq adalah min-heap.']]}
 ]},
{t:'Type hints',lvl:'Lanjutan',d:'Anotasi tipe, pemeriksa tipe statis, dan validasi data dengan Pydantic.',
 nodes:['Static Typing','Typing','Type Annotations','mypy','pyright','pyrefly','Pydantic'],
 lessons:[
  {k:'c',t:'Anotasi tipe & modul typing',nodes:['Static Typing','Typing','Type Annotations'],
   b:['Python tetap dinamis, tetapi sejak 3.5 kamu bisa menambahkan <b>anotasi tipe</b>: <code>def total(harga: list[int]) -&gt; int</code>. Anotasi tidak memengaruhi cara program berjalan. Gunanya sebagai dokumentasi, membantu IDE memberi saran, dan dibaca oleh pemeriksa tipe untuk menemukan bug sebelum program dijalankan.',
      'Tipe bawaan bisa langsung dipakai: <code>int</code>, <code>str</code>, <code>list[str]</code>, <code>dict[str, int]</code>, <code>tuple[int, int]</code>. Nilai yang mungkin None ditulis <code>str | None</code>. Modul <code>typing</code> menambah alat seperti <code>Callable</code>, <code>TypedDict</code>, <code>Literal</code>, <code>Protocol</code>, dan <code>TypeVar</code> untuk fungsi generik.',
      'Mulailah dari tanda tangan fungsi publik. Tidak perlu menganotasi setiap variabel lokal, karena pemeriksa tipe bisa menebaknya.'],
   code:R`from typing import Callable, Literal, TypedDict, TypeVar

T = TypeVar("T")

class Produk(TypedDict):
    nama: str
    harga: int

Status = Literal["baru", "dikirim", "selesai"]

def termahal(data: list[Produk]) -> Produk | None:
    return max(data, key=lambda p: p["harga"]) if data else None

def terapkan(f: Callable[[int], int], nilai: list[int]) -> list[int]:
    return [f(x) for x in nilai]

def pertama(xs: list[T]) -> T:
    return xs[0]

def ubah_status(s: Status) -> str:
    return s.upper()

katalog: list[Produk] = [{"nama": "Kopi", "harga": 85000}, {"nama": "Teh", "harga": 25000}]
print(termahal(katalog))
print(terapkan(lambda x: x * 2, [1, 2, 3]))
print(pertama(["a", "b"]), ubah_status("dikirim"))
print(termahal.__annotations__["return"])`,
   out:`{'nama': 'Kopi', 'harga': 85000}
[2, 4, 6]
a DIKIRIM
__main__.Produk | None
`,
   pts:['Anotasi tidak dicek saat runtime; alat statis yang memeriksanya.','<code>X | None</code> untuk nilai opsional.','<code>TypedDict</code> untuk dict berstruktur tetap.','<code>TypeVar</code> untuk fungsi generik.'],
   q:[['Apakah Python menolak <code>f("a")</code> jika parameternya beranotasi int?',['Ya, saat runtime','Tidak, hanya pemeriksa tipe yang memperingatkan','Ya, saat import'],1,'Anotasi hanyalah informasi.'],
      ['Penulisan tipe "string atau None"?',['str?','str | None','Optional str'],1,'Sintaks union sejak Python 3.10.']]},
  {k:'c',t:'Pemeriksa tipe: mypy, pyright, pyrefly',nodes:['mypy','pyright','pyrefly'],
   b:['<b>Pemeriksa tipe statis</b> membaca kode tanpa menjalankannya, lalu melaporkan pemakaian tipe yang tidak cocok. Bug seperti mengirim string ke fungsi yang butuh angka, atau lupa menangani kemungkinan None, ketahuan sebelum sampai ke pengguna.',
      '<b>mypy</b> adalah pemeriksa tipe tertua dan menjadi acuan. <b>pyright</b> dari Microsoft sangat cepat dan menjadi mesin di balik fitur Pylance di VS Code. <b>pyrefly</b> dari Meta adalah pemeriksa baru berbasis Rust yang fokus pada kecepatan untuk proyek raksasa.',
      'Biasanya pemeriksa tipe dijalankan otomatis di editor dan di pipeline CI, berdampingan dengan linter dan tes. Mode <code>--strict</code> mewajibkan semua fungsi beranotasi.'],
   code:R`# toko.py
def diskon(harga: int, persen: int) -> int:
    return harga - harga * persen // 100

def cari_harga(nama: str) -> int | None:
    katalog = {"kopi": 85000}
    return katalog.get(nama)

total = diskon("85000", 10)          # salah tipe
h = cari_harga("teh")
print(h + 1000)                       # h bisa None

# $ mypy toko.py
# toko.py:8: error: Argument 1 to "diskon" has incompatible type "str"; expected "int"
# toko.py:10: error: Unsupported operand types for + ("None" and "int")
# Found 2 errors in 1 file (checked 1 source file)

# $ pyright toko.py      -> laporan serupa
# $ pyrefly check toko.py`,
   out:null,
   pts:['Pemeriksa tipe menemukan bug tanpa menjalankan program.','mypy = acuan, pyright = cepat dan terintegrasi VS Code, pyrefly = baru dan sangat cepat.','Tangani None secara eksplisit: <code>if h is not None</code>.','Jalankan di CI agar kode baru selalu diperiksa.'],
   q:[['Kapan mypy menemukan kesalahan tipe?',['Saat program dijalankan','Saat membaca kode, sebelum dijalankan','Saat pip install'],1,'Itu arti statis.'],
      ['Mesin di balik Pylance di VS Code?',['mypy','pyright','pyrefly'],1,'Pylance dibangun di atas pyright.']]},
  {k:'c',t:'Validasi data dengan Pydantic',nodes:['Pydantic'],
   b:['Anotasi tipe biasa tidak memeriksa data saat program berjalan. Padahal data dari luar (form, API, file JSON) sering berantakan. <b>Pydantic</b> memakai anotasi tipe untuk <b>memvalidasi dan mengonversi</b> data saat runtime.',
      'Kamu mendefinisikan model sebagai kelas turunan <code>BaseModel</code>. Saat membuat objek, Pydantic memeriksa setiap field: mengubah <code>"85000"</code> menjadi int jika memungkinkan, dan melempar <code>ValidationError</code> yang jelas jika tidak. Aturan tambahan ditulis dengan <code>Field(gt=0)</code> atau validator.',
      'Pydantic menjadi fondasi FastAPI: setiap request JSON otomatis divalidasi berdasarkan model, dan dokumentasi API dibuat dari model yang sama.'],
   code:R`from pydantic import BaseModel, Field, ValidationError

class Produk(BaseModel):
    nama: str = Field(min_length=2)
    harga: int = Field(gt=0)
    tag: list[str] = []

p = Produk(nama="Kopi Gayo", harga="85000")   # string diubah jadi int
print(p.harga + 1, p.model_dump())

try:
    Produk(nama="K", harga=-5)
except ValidationError as e:
    for err in e.errors():
        print(err["loc"][0], "->", err["msg"])

# Keluaran:
# 85001 {'nama': 'Kopi Gayo', 'harga': 85000, 'tag': []}
# nama -> String should have at least 2 characters
# harga -> Input should be greater than 0`,
   out:null,
   pts:['Pydantic memvalidasi data saat runtime berdasarkan anotasi.','Konversi otomatis jika aman ("85000" → 85000).','<code>Field(...)</code> untuk aturan tambahan.','<code>model_dump()</code> mengubah model menjadi dict.'],
   q:[['Perbedaan utama Pydantic dengan anotasi biasa?',['Pydantic memeriksa data saat program berjalan','Pydantic hanya dokumentasi','Tidak ada'],0,'Itu alasan Pydantic populer untuk data dari luar.'],
      ['Framework web yang dibangun di atas Pydantic?',['Django','FastAPI','Flask'],1,'FastAPI memakai model Pydantic untuk request dan response.']]}
 ]},
{t:'Kualitas kode & testing',lvl:'Profesional',d:'Formatter, linter, docstring, dan tes otomatis dengan pytest, unittest, doctest, dan tox.',
 nodes:['Code Formatting','black','ruff','yapf','Docstrings and Comments','sphinx','Testing','pytest','PyUnit/Unittest','Doctest','Tox'],
 lessons:[
  {k:'c',t:'Formatter & linter: black, ruff, yapf',nodes:['Code Formatting','black','ruff','yapf'],
   b:['Tim profesional tidak berdebat soal spasi atau tanda kutip. Mereka memakai <b>formatter</b> yang merapikan kode secara otomatis dengan aturan seragam, biasanya mengikuti panduan gaya <b>PEP 8</b>.',
      '<b>black</b> adalah formatter "tanpa kompromi" dengan sedikit pilihan konfigurasi, sehingga semua kode terlihat sama. <b>yapf</b> dari Google lebih bisa diatur. <b>ruff</b> adalah linter dan formatter super cepat berbasis Rust: ia menemukan masalah seperti import tak terpakai, variabel tidak didefinisikan, dan pola rawan bug, sekaligus bisa memformat seperti black.',
      'Jalankan alat ini otomatis lewat <i>pre-commit hook</i> atau di CI, supaya kode yang masuk repositori selalu rapi.'],
   code:R`# sebelum
import os,sys
def hitung( harga,diskon = 0 ):
  total=harga-harga*diskon/100
  return  total

# $ ruff check toko.py
# toko.py:1:8: F401 [*] 'os' imported but unused
# toko.py:1:11: F401 [*] 'sys' imported but unused
# $ ruff check --fix toko.py && ruff format toko.py     (atau: black toko.py)

# sesudah
def hitung(harga, diskon=0):
    total = harga - harga * diskon / 100
    return total`,
   out:null,lang:'python',
   pts:['PEP 8 = panduan gaya resmi Python.','Formatter merapikan, linter mencari masalah.','ruff sangat cepat dan bisa menggantikan banyak alat.','Otomatiskan dengan pre-commit dan CI.'],
   q:[['Alat yang memformat kode tanpa banyak pilihan konfigurasi?',['black','yapf','pip'],0,'black sengaja dibuat "opinionated".'],
      ['Kode F401 dari ruff berarti?',['Sintaks salah','Import tidak dipakai','Tes gagal'],1,'F401: module imported but unused.']]},
  {k:'c',t:'Docstring, komentar & Sphinx',nodes:['Docstrings and Comments','sphinx'],
   b:['<b>Komentar</b> (<code>#</code>) menjelaskan <i>kenapa</i> sebuah kode ditulis begitu. <b>Docstring</b> adalah string di baris pertama fungsi, kelas, atau modul yang menjelaskan <i>apa</i> kegunaannya dan cara memakainya. Docstring bisa dibaca saat program berjalan lewat <code>help(fungsi)</code> atau <code>fungsi.__doc__</code>.',
      'Ada beberapa gaya penulisan docstring yang populer: gaya Google, NumPy, dan reStructuredText. Pilih satu dan konsisten. Isi minimal: ringkasan satu baris, penjelasan parameter, nilai kembali, dan exception yang mungkin dilempar.',
      '<b>Sphinx</b> mengubah docstring menjadi situs dokumentasi lengkap, seperti dokumentasi resmi Python dan banyak pustaka besar. Ekstensi <code>autodoc</code> mengambil docstring langsung dari kodemu.'],
   code:R`def hitung_ongkir(berat_kg: float, kota: str) -> int:
    """Menghitung ongkos kirim dalam rupiah.

    Tarif dasar Rp10.000 per kg, ditambah biaya luar Jawa.

    Args:
        berat_kg: Berat paket dalam kilogram, harus lebih dari 0.
        kota: Kota tujuan.

    Returns:
        Ongkos kirim yang dibulatkan ke atas per kilogram.

    Raises:
        ValueError: Jika berat tidak positif.
    """
    if berat_kg <= 0:
        raise ValueError("berat harus positif")
    # dibulatkan ke atas karena kurir menghitung per kg penuh
    kg = -(-berat_kg // 1)
    tambahan = 15000 if kota not in {"Jakarta", "Bandung", "Surabaya"} else 0
    return int(kg * 10000 + tambahan)

print(hitung_ongkir(2.3, "Medan"))
print(hitung_ongkir.__doc__.splitlines()[0])`,
   out:`45000
Menghitung ongkos kirim dalam rupiah.
`,
   pts:['Komentar = kenapa; docstring = apa dan bagaimana memakai.','Docstring diakses lewat <code>help()</code> atau <code>__doc__</code>.','Pilih satu gaya: Google, NumPy, atau reST.','Sphinx + autodoc = situs dokumentasi dari docstring.'],
   q:[['Di mana docstring ditulis?',['Di akhir fungsi','Sebagai string pertama di badan fungsi','Di file terpisah'],1,'Baris pertama setelah def.'],
      ['Alat untuk membuat situs dokumentasi dari docstring?',['Sphinx','black','pytest'],0,'Sphinx dengan ekstensi autodoc.']]},
  {k:'c',t:'Testing dengan pytest',nodes:['Testing','pytest'],
   b:['<b>pytest</b> adalah framework tes paling populer di Python. Tes ditulis sebagai fungsi biasa yang namanya diawali <code>test_</code>, di file yang namanya diawali <code>test_</code>. Pemeriksaan cukup memakai <code>assert</code> biasa, dan pytest menampilkan detail nilai yang berbeda saat gagal.',
      '<code>pytest.raises</code> memeriksa bahwa sebuah exception dilempar. <code>@pytest.mark.parametrize</code> menjalankan satu tes dengan banyak data. <b>Fixture</b> menyiapkan data atau sumber daya yang dipakai bersama beberapa tes, misalnya database sementara.',
      'Jalankan semua tes dengan perintah <code>pytest</code> di folder proyek. Tambahkan <code>-v</code> untuk melihat nama setiap tes, dan pasang <code>pytest-cov</code> untuk mengukur seberapa banyak kode yang teruji.'],
   code:R`# toko.py
def diskon(harga, persen):
    if not 0 <= persen <= 100:
        raise ValueError("persen harus 0..100")
    return harga - harga * persen // 100

# test_toko.py
import pytest
from toko import diskon

def test_diskon_sepuluh_persen():
    assert diskon(50_000, 10) == 45_000

def test_persen_salah():
    with pytest.raises(ValueError):
        diskon(1000, 150)

@pytest.mark.parametrize("harga, persen, harapan", [
    (100_000, 0, 100_000),
    (100_000, 100, 0),
    (80_000, 25, 60_000),
])
def test_banyak_kasus(harga, persen, harapan):
    assert diskon(harga, persen) == harapan

@pytest.fixture
def keranjang():
    return [("kopi", 85_000), ("teh", 25_000)]

def test_total(keranjang):
    assert sum(h for _, h in keranjang) == 110_000

# $ pytest -v
# test_toko.py::test_diskon_sepuluh_persen PASSED
# test_toko.py::test_persen_salah PASSED
# test_toko.py::test_banyak_kasus[100000-0-100000] PASSED   ... (3 kasus)
# test_toko.py::test_total PASSED
# ===== 6 passed in 0.02s =====`,
   out:null,
   pts:['File dan fungsi tes diawali <code>test_</code>.','Cukup <code>assert</code> biasa.','<code>parametrize</code> untuk banyak data, <code>fixture</code> untuk persiapan bersama.','<code>pytest-cov</code> untuk mengukur cakupan tes.'],
   q:[['Cara pytest mengenali fungsi tes?',['Anotasi @Test','Nama diawali test_','Kelas TestCase'],1,'Konvensi nama test_.'],
      ['Fitur untuk menyiapkan data yang dipakai banyak tes?',['fixture','mock','assert'],0,'Fixture disuntikkan lewat nama parameter.']]},
  {k:'c',t:'unittest, doctest & tox',nodes:['PyUnit/Unittest','Doctest','Tox'],
   b:['<b>unittest</b> (PyUnit) adalah framework tes bawaan Python, bergaya kelas seperti JUnit. Tes ditulis sebagai method di kelas turunan <code>unittest.TestCase</code> dan memakai method seperti <code>assertEqual</code>. pytest juga bisa menjalankan tes unittest, jadi keduanya bisa hidup berdampingan.',
      '<b>doctest</b> menjalankan contoh yang ditulis di dalam docstring dengan format sesi interaktif (<code>&gt;&gt;&gt;</code>). Ini menjaga contoh di dokumentasi selalu benar.',
      '<b>tox</b> menjalankan rangkaian tes di beberapa lingkungan sekaligus, misalnya Python 3.11, 3.12, dan 3.13, masing-masing dalam virtual environment sendiri. Pustaka yang dipakai banyak orang memakai tox atau nox untuk memastikan kompatibilitas.'],
   code:R`import unittest

def rupiah(n):
    """Format angka menjadi rupiah.

    >>> rupiah(1500000)
    'Rp1.500.000'
    >>> rupiah(0)
    'Rp0'
    """
    return f"Rp{n:,}".replace(",", ".")

class TesRupiah(unittest.TestCase):
    def test_ribuan(self):
        self.assertEqual(rupiah(85000), "Rp85.000")
    def test_tipe(self):
        self.assertIsInstance(rupiah(1), str)

if __name__ == "__main__":
    import doctest, io, contextlib
    hasil = doctest.testmod()
    print("doctest gagal:", hasil.failed, "dari", hasil.attempted)
    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        r = unittest.main(exit=False).result
    print("unittest jalan:", r.testsRun, "gagal:", len(r.failures))`,
   out:`doctest gagal: 0 dari 2
unittest jalan: 2 gagal: 0
`,
   pts:['unittest: bawaan, berbasis kelas TestCase.','doctest: contoh di docstring ikut diuji.','tox: menguji di banyak versi Python.','pytest bisa menjalankan tes unittest dan doctest.'],
   q:[['Tanda yang dipakai doctest untuk contoh di docstring?',['>>>','$','#'],0,'Format sesi interaktif Python.'],
      ['Kegunaan tox?',['Format kode','Menguji di beberapa versi Python sekaligus','Memasang paket'],1,'Setiap versi punya venv sendiri.']]}
 ]},
{t:'Konkurensi',lvl:'Profesional',d:'Threading dan GIL, multiprocessing, asyncio, dan gevent.',
 nodes:['Concurrency','Threading','GIL','Multiprocessing','Asynchrony','gevent'],
 lessons:[
  {k:'c',t:'Threading & GIL',nodes:['Threading','GIL','Concurrency'],viz:'race',
   b:['<b>Thread</b> memungkinkan beberapa pekerjaan berjalan bergantian dalam satu proses. Di CPython ada <b>GIL</b> (Global Interpreter Lock): hanya satu thread yang boleh menjalankan bytecode Python pada satu waktu. Akibatnya, thread tidak mempercepat pekerjaan berat di CPU.',
      'Namun thread tetap sangat berguna untuk pekerjaan yang banyak <b>menunggu</b> (I/O): mengunduh file, memanggil API, membaca database. Saat satu thread menunggu jaringan, GIL dilepas dan thread lain bisa bekerja.',
      'Meski ada GIL, race condition tetap bisa terjadi, karena <code>n += 1</code> terdiri dari beberapa langkah bytecode dan thread bisa berganti di antaranya. Lindungi data bersama dengan <code>threading.Lock</code>. Catatan: Python 3.13 mulai menyediakan build eksperimental tanpa GIL (free-threaded).'],
   code:R`import threading, time
from concurrent.futures import ThreadPoolExecutor

def unduh(nama):
    time.sleep(0.5)                  # pura-pura menunggu jaringan
    return f"{nama} selesai"

mulai = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as ex:
    hasil = list(ex.map(unduh, ["a.jpg", "b.jpg", "c.jpg", "d.jpg", "e.jpg"]))
print(hasil[0], "| 5 unduhan dalam", round(time.perf_counter() - mulai, 1), "detik")

saldo = 0
kunci = threading.Lock()
def setor():
    global saldo
    for _ in range(100_000):
        with kunci:                  # bagian kritis
            saldo += 1

ts = [threading.Thread(target=setor) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
print("saldo:", saldo)`,
   out:`a.jpg selesai | 5 unduhan dalam 0.5 detik
saldo: 400000
`,
   pts:['GIL: satu thread menjalankan bytecode Python pada satu waktu.','Thread cocok untuk tugas I/O, bukan hitungan berat.','<code>ThreadPoolExecutor</code> untuk menjalankan banyak tugas.','Pakai <code>Lock</code> untuk data yang diubah bersama.'],
   q:[['Kenapa thread tidak mempercepat hitungan berat di CPython?',['Karena GIL','Karena thread lambat','Karena butuh internet'],0,'Hanya satu thread yang menjalankan bytecode.'],
      ['Pekerjaan yang paling cocok untuk thread?',['Menghitung bilangan prima','Mengunduh banyak file','Mengurutkan list'],1,'Thread lain bekerja saat satu thread menunggu.']]},
  {k:'c',t:'Multiprocessing',nodes:['Multiprocessing','Concurrency'],
   b:['Untuk pekerjaan berat di CPU, seperti memproses gambar atau menghitung statistik besar, gunakan <b>multiprocessing</b>. Setiap proses punya interpreter Python dan GIL-nya sendiri, sehingga benar-benar berjalan paralel di beberapa inti CPU.',
      'Cara termudah adalah <code>ProcessPoolExecutor</code> atau <code>multiprocessing.Pool</code>: berikan fungsi dan daftar data, lalu tugas dibagi ke beberapa proses.',
      'Proses tidak berbagi memori seperti thread. Data dikirim antarproses dengan cara diserialisasi (pickle), jadi ada biaya tambahan. Selalu bungkus kode utama dengan <code>if __name__ == "__main__":</code>, karena di Windows dan macOS proses baru mengimpor ulang file utamamu.'],
   code:R`from concurrent.futures import ProcessPoolExecutor
import math, os

def jumlah_prima(batas):
    return sum(1 for n in range(2, batas) if all(n % d for d in range(2, int(math.isqrt(n)) + 1)))

if __name__ == "__main__":
    tugas = [50_000, 60_000, 70_000, 80_000]
    with ProcessPoolExecutor() as ex:
        hasil = list(ex.map(jumlah_prima, tugas))
    print(hasil)
    print("inti CPU tersedia:", os.cpu_count() is not None)`,
   out:`[5133, 6057, 6935, 7837]
inti CPU tersedia: True
`,
   pts:['Multiprocessing = paralel sungguhan, melewati GIL.','Cocok untuk tugas berat CPU.','Data antarproses dikirim lewat pickle.','Wajib <code>if __name__ == "__main__":</code>.'],
   q:[['Untuk memproses 1000 foto (berat CPU), pilih?',['threading','multiprocessing','asyncio'],1,'Setiap proses memakai inti CPU sendiri.'],
      ['Apakah proses berbagi variabel global?',['Ya','Tidak, masing-masing punya memori sendiri','Hanya list'],1,'Butuh Queue, Pipe, atau shared memory untuk berbagi.']]},
  {k:'c',t:'asyncio, async/await & gevent',nodes:['Asynchrony','gevent','Concurrency'],viz:'eventloop',
   b:['<b>asyncio</b> menjalankan banyak tugas I/O secara bergantian dalam <b>satu thread</b>, dikendalikan oleh <b>event loop</b>. Fungsi yang ditulis dengan <code>async def</code> disebut coroutine. Di dalamnya, <code>await</code> berarti "tunggu hasil ini, dan selama menunggu, silakan jalankan tugas lain".',
      '<code>asyncio.gather</code> menjalankan beberapa coroutine bersamaan dan mengumpulkan hasilnya. Karena hanya satu thread, tidak ada race condition di antara titik <code>await</code>. Ini membuat asyncio sangat efisien untuk server yang melayani ribuan koneksi.',
      'Syaratnya, pustaka yang dipakai juga harus mendukung async, misalnya <code>httpx</code> atau <code>aiohttp</code> untuk HTTP. <b>gevent</b> adalah pendekatan lama: ia "menambal" pustaka standar agar kode sinkron biasa otomatis bergantian seperti async (greenlet).'],
   code:R`import asyncio, time

async def ambil(nama, detik):
    print(f"mulai {nama}")
    await asyncio.sleep(detik)        # menunggu tanpa memblokir
    print(f"selesai {nama}")
    return f"{nama}:{detik}s"

async def main():
    mulai = time.perf_counter()
    hasil = await asyncio.gather(
        ambil("cuaca", 0.3),
        ambil("kurs", 0.1),
        ambil("berita", 0.2),
    )
    print(hasil)
    print("total sekitar", round(time.perf_counter() - mulai, 1), "detik")

asyncio.run(main())`,
   out:`mulai cuaca
mulai kurs
mulai berita
selesai kurs
selesai berita
selesai cuaca
['cuaca:0.3s', 'kurs:0.1s', 'berita:0.2s']
total sekitar 0.3 detik
`,
   pts:['<code>async def</code> membuat coroutine; <code>await</code> menyerahkan giliran.','Event loop menjalankan tugas bergantian dalam satu thread.','<code>asyncio.gather</code> untuk menjalankan bersamaan.','Ringkasan: CPU berat → multiprocessing; I/O banyak → asyncio atau thread.'],
   q:[['Total waktu tiga tugas 0.3, 0.1, 0.2 detik dengan gather?',['0.6 detik','Sekitar 0.3 detik','0.1 detik'],1,'Semua menunggu bersamaan; total = yang paling lama.'],
      ['Apa yang terjadi saat coroutine bertemu <code>await asyncio.sleep(1)</code>?',['Seluruh program diam 1 detik','Event loop menjalankan tugas lain dulu','Error'],1,'Itulah inti asyncio.']]}
 ]},
{t:'Framework web',lvl:'Profesional',d:'Memilih dan memakai framework web Python: Django, Flask, FastAPI, dan lainnya.',
 nodes:['Python Frameworks','Django','Flask','FastAPI','Pyramid','Sanic','Tornado','AIOHTTP','Plotly Dash'],
 lessons:[
  {k:'c',t:'Peta framework web Python',nodes:['Python Frameworks','Pyramid','Sanic','Tornado','AIOHTTP','Plotly Dash'],
   b:['Framework web menangani pekerjaan berulang: menerima request HTTP, mencocokkan URL ke fungsi, membaca data form atau JSON, dan mengirim response. Python punya banyak pilihan dengan filosofi berbeda.',
      '<b>Django</b>: "batteries included", lengkap dengan ORM, panel admin, autentikasi, dan template. <b>Flask</b>: mikro dan fleksibel, kamu memilih sendiri komponennya. <b>FastAPI</b>: modern, async, berbasis type hint dan Pydantic, dengan dokumentasi API otomatis. <b>Pyramid</b>: bisa mulai kecil dan tumbuh besar.',
      'Untuk performa async tinggi ada <b>Sanic</b>, <b>Tornado</b>, dan <b>AIOHTTP</b>. <b>Plotly Dash</b> khusus membuat dashboard data interaktif hanya dengan Python. Panduan cepat: aplikasi web lengkap dengan admin → Django; REST API modern → FastAPI; layanan kecil atau belajar → Flask.'],
   code:R`# Dash: dashboard interaktif dalam satu file
from dash import Dash, html, dcc
import plotly.express as px

data = {"bulan": ["Jan", "Feb", "Mar"], "penjualan": [120, 150, 170]}
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Penjualan Toko Nusantara"),
    dcc.Graph(figure=px.bar(data, x="bulan", y="penjualan")),
])

if __name__ == "__main__":
    app.run(debug=True)          # buka http://127.0.0.1:8050`,
   out:null,
   pts:['Django: lengkap, cocok untuk aplikasi web penuh.','Flask: minimalis dan fleksibel.','FastAPI: API modern, async, validasi otomatis.','Sanic/Tornado/AIOHTTP: async; Dash: dashboard data.'],
   q:[['Framework dengan panel admin bawaan?',['Flask','Django','FastAPI'],1,'Django admin dibuat otomatis dari model.'],
      ['Framework untuk dashboard data interaktif tanpa JavaScript?',['Plotly Dash','Tornado','Pyramid'],0,'Dash dibangun di atas Plotly dan React.']]},
  {k:'c',t:'Membuat REST API: Flask & FastAPI',nodes:['Flask','FastAPI'],
   b:['<b>Flask</b> menghubungkan URL ke fungsi dengan decorator <code>@app.route</code> (atau <code>@app.get</code> di versi baru). Fungsi mengembalikan dict, dan Flask mengubahnya menjadi JSON.',
      '<b>FastAPI</b> tampak mirip, tetapi memanfaatkan type hint secara penuh. Parameter <code>id: int</code> di fungsi otomatis divalidasi dari URL. Body request dideklarasikan sebagai model Pydantic. FastAPI juga membuat dokumentasi interaktif di <code>/docs</code> secara otomatis.',
      'FastAPI mendukung <code>async def</code> sehingga satu server bisa melayani banyak request yang sedang menunggu database atau API lain. Jalankan dengan server ASGI seperti <code>uvicorn</code>.'],
   code:R`# ===== Flask =====
from flask import Flask
app = Flask(__name__)
PRODUK = {1: {"nama": "Kopi Gayo", "harga": 85000}}

@app.get("/produk/<int:pid>")
def detail(pid):
    p = PRODUK.get(pid)
    return p if p else ({"error": "tidak ada"}, 404)
# flask --app app run

# ===== FastAPI =====
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

api = FastAPI()

class ProdukBaru(BaseModel):
    nama: str
    harga: int

@api.get("/produk/{pid}")
async def ambil(pid: int):
    if pid not in PRODUK:
        raise HTTPException(status_code=404, detail="tidak ada")
    return PRODUK[pid]

@api.post("/produk", status_code=201)
async def tambah(p: ProdukBaru):
    pid = max(PRODUK) + 1
    PRODUK[pid] = p.model_dump()
    return {"id": pid, **PRODUK[pid]}
# uvicorn app:api --reload   -> dokumentasi di http://127.0.0.1:8000/docs`,
   out:null,
   pts:['Route = pasangan method HTTP + URL → fungsi.','FastAPI memvalidasi parameter dari type hint.','Body request = model Pydantic.','Kode status: 200 OK, 201 Created, 404 Not Found.'],
   q:[['Di FastAPI, apa yang terjadi jika <code>/produk/abc</code> dipanggil padahal <code>pid: int</code>?',['Crash','Respons 422 berisi pesan validasi','Mengembalikan semua produk'],1,'Validasi otomatis dari type hint.'],
      ['Server untuk menjalankan aplikasi FastAPI?',['uvicorn','gunicorn saja','nginx saja'],0,'uvicorn adalah server ASGI.']]},
  {k:'c',t:'Django: aplikasi web lengkap',nodes:['Django'],
   b:['<b>Django</b> memakai pola <b>MTV</b>: <i>Model</i> (struktur data dan tabel database), <i>Template</i> (tampilan HTML), dan <i>View</i> (logika yang menerima request dan mengembalikan response). URL dipetakan ke view lewat file <code>urls.py</code>.',
      'Model Django adalah ORM: kelas Python yang otomatis menjadi tabel. Perintah <code>makemigrations</code> dan <code>migrate</code> membuat dan memperbarui tabel sesuai model. Query ditulis dengan gaya Python: <code>Produk.objects.filter(harga__gt=50000)</code>.',
      'Daftarkan model di <code>admin.py</code>, dan kamu langsung mendapat panel admin untuk menambah, mengubah, dan menghapus data. Untuk REST API, tim biasanya menambahkan Django REST Framework.'],
   code:R`# models.py
from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    kategori = models.CharField(max_length=50)
    harga = models.PositiveIntegerField()

    def __str__(self):
        return self.nama

# views.py
from django.shortcuts import render
from .models import Produk

def daftar_mahal(request):
    produk = Produk.objects.filter(harga__gt=50000).order_by("-harga")
    return render(request, "toko/daftar.html", {"produk": produk})

# urls.py
from django.urls import path
from . import views
urlpatterns = [path("mahal/", views.daftar_mahal)]

# admin.py
from django.contrib import admin
admin.site.register(Produk)

# Terminal
# django-admin startproject toko_site
# python manage.py makemigrations && python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver      -> http://127.0.0.1:8000/admin`,
   out:null,
   pts:['MTV: Model, Template, View.','ORM: <code>Model.objects.filter(...)</code>.','Migrasi menjaga tabel sesuai model.','Panel admin otomatis dari model.'],
   q:[['Perintah untuk menerapkan perubahan model ke database?',['runserver','migrate','startapp'],1,'makemigrations membuat rencana, migrate menjalankannya.'],
      ['<code>harga__gt=50000</code> berarti?',['harga = 50000','harga > 50000','harga < 50000'],1,'gt = greater than.']]}
 ]}
];
