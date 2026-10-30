/* ===================== KODE PEMULA VS KODE RAPI =====================
   Perbandingan cara pemula dan cara yang lebih rapi (best practice), termasuk trik yang
   jarang diketahui. Ditempel ke pelajaran berdasarkan judulnya: l.pro = [{t,why,a,b,out,lang}].
   Setiap pasangan kode sudah dijalankan dan menghasilkan keluaran yang sama. */
(()=>{
const PRO={
"java:Tipe data primitif & type casting": [
{
"t": "Angka besar lebih mudah dibaca dengan garis bawah",
"tag": "Trik jarang diketahui",
"why": "Sejak Java 7, garis bawah boleh ditulis di antara digit: <code>1_000_000</code>. Compiler mengabaikannya, nilainya tetap sama, tetapi mata manusia langsung tahu itu satu juta, bukan seratus ribu.",
"lang": "java",
"a": "long harga = 1000000;\nlong ongkir = 25000;\nSystem.out.println(harga + ongkir);",
"b": "long harga = 1_000_000;\nlong ongkir = 25_000;\nSystem.out.println(harga + ongkir);",
"out": "1025000"
},
{
"t": "Hasil perkalian int bisa meluap tanpa peringatan",
"tag": "Lebih aman",
"why": "Perkalian dua <code>int</code> tetap bertipe <code>int</code>, walaupun hasilnya disimpan ke <code>long</code>. Kalau melewati ±2,1 miliar, angkanya berputar menjadi negatif. Ubah salah satu operand menjadi <code>long</code> (akhiran <code>L</code>) sebelum dikalikan, atau pakai <code>Math.multiplyExact</code> agar luapan langsung jadi error.",
"lang": "java",
"a": "int hargaSatuan = 2_500_000;\nint jumlah = 1_000;\nlong total = hargaSatuan * jumlah;\nSystem.out.println(total);",
"b": "int hargaSatuan = 2_500_000;\nint jumlah = 1_000;\nlong total = (long) hargaSatuan * jumlah;\nSystem.out.println(total);",
"outA": "-1794967296",
"outB": "2500000000"
}
],
"java:Method String & StringBuilder": [
{
"t": "Menggabungkan isi array dengan pemisah",
"tag": "Lebih singkat",
"why": "Menyambung string di dalam loop membuat objek baru setiap putaran dan butuh logika tambahan agar koma terakhir tidak ikut. <code>String.join</code> melakukan semuanya dalam satu baris.",
"lang": "java",
"a": "String[] buah = {\"apel\", \"jeruk\", \"mangga\"};\nString hasil = \"\";\nfor (int i = 0; i < buah.length; i++) {\n    hasil = hasil + buah[i];\n    if (i < buah.length - 1) {\n        hasil = hasil + \", \";\n    }\n}\nSystem.out.println(hasil);",
"b": "String[] buah = {\"apel\", \"jeruk\", \"mangga\"};\nSystem.out.println(String.join(\", \", buah));",
"out": "apel, jeruk, mangga"
},
{
"t": "Teks beberapa baris dengan text block",
"tag": "Trik jarang diketahui",
"why": "Text block (Java 15) diapit tiga tanda kutip. Tidak perlu <code>\\n</code> dan tanda <code>+</code> di setiap baris, dan indentasi di kiri dibuang otomatis.",
"lang": "java",
"a": "String pesan = \"Halo Sari,\\n\" +\n        \"Pesananmu sudah dikirim.\\n\" +\n        \"Terima kasih!\";\nSystem.out.println(pesan);",
"b": "String pesan = \"\"\"\n        Halo Sari,\n        Pesananmu sudah dikirim.\n        Terima kasih!\"\"\";\nSystem.out.println(pesan);",
"out": "Halo Sari,\nPesananmu sudah dikirim.\nTerima kasih!"
}
],
"java:switch & operator ternary": [
{
"t": "switch dengan panah tidak butuh break",
"tag": "Lebih aman",
"why": "Lupa menulis <code>break</code> adalah bug klasik: eksekusi \"jatuh\" ke case berikutnya. Switch expression dengan <code>-&gt;</code> (Java 14) tidak pernah jatuh, bisa menggabungkan beberapa nilai dengan koma, dan langsung mengembalikan nilai.",
"lang": "java",
"a": "int hari = 6;\nString jenis;\nswitch (hari) {\n    case 6:\n    case 7:\n        jenis = \"Akhir pekan\";\n        break;\n    default:\n        jenis = \"Hari kerja\";\n}\nSystem.out.println(jenis);",
"b": "int hari = 6;\nString jenis = switch (hari) {\n    case 6, 7 -> \"Akhir pekan\";\n    default -> \"Hari kerja\";\n};\nSystem.out.println(jenis);",
"out": "Akhir pekan"
}
],
"java:Kelas Arrays & array dua dimensi": [
{
"t": "Mencetak dan mengurutkan array",
"tag": "Lebih singkat",
"why": "Kelas <code>Arrays</code> sudah punya <code>sort</code> dan <code>toString</code>. Tidak perlu menulis algoritma pengurutan dan loop pencetak sendiri, kecuali sedang belajar algoritmanya.",
"lang": "java",
"a": "int[] nilai = {78, 92, 65};\nfor (int i = 0; i < nilai.length; i++)\n    for (int j = 0; j < nilai.length - 1 - i; j++)\n        if (nilai[j] > nilai[j + 1]) {\n            int t = nilai[j]; nilai[j] = nilai[j + 1]; nilai[j + 1] = t;\n        }\nSystem.out.print(\"[\");\nfor (int i = 0; i < nilai.length; i++) {\n    System.out.print(nilai[i]);\n    if (i < nilai.length - 1) System.out.print(\", \");\n}\nSystem.out.println(\"]\");",
"b": "int[] nilai = {78, 92, 65};\nArrays.sort(nilai);\nSystem.out.println(Arrays.toString(nilai));",
"out": "[65, 78, 92]"
}
],
"java:Enum & record": [
{
"t": "Kelas data cukup ditulis sebagai record",
"tag": "Lebih singkat",
"why": "Kelas yang hanya membawa data biasanya butuh field, konstruktor, getter, <code>equals</code>, <code>hashCode</code>, dan <code>toString</code>. <code>record</code> (Java 16) membuat semuanya otomatis dan nilainya tidak bisa diubah.",
"lang": "java",
"a": "class Produk {\n    private final String nama;\n    private final int harga;\n    Produk(String nama, int harga) { this.nama = nama; this.harga = harga; }\n    String nama() { return nama; }\n    int harga() { return harga; }\n    @Override public String toString() { return \"Produk[nama=\" + nama + \", harga=\" + harga + \"]\"; }\n}\nProduk p = new Produk(\"Kopi Gayo\", 85_000);\nSystem.out.println(p);\nSystem.out.println(p.harga());",
"b": "record Produk(String nama, int harga) {}\nProduk p = new Produk(\"Kopi Gayo\", 85_000);\nSystem.out.println(p);\nSystem.out.println(p.harga());",
"out": "Produk[nama=Kopi Gayo, harga=85000]\n85000"
}
],
"java:Array lawan ArrayList": [
{
"t": "Daftar tetap cukup dengan List.of",
"tag": "Lebih singkat",
"why": "<code>List.of</code> (Java 9) membuat daftar dalam satu baris. Daftarnya tidak bisa diubah, sehingga aman dibagikan ke bagian program lain. Kalau perlu menambah isi, bungkus dengan <code>new ArrayList&lt;&gt;(List.of(...))</code>.",
"lang": "java",
"a": "ArrayList<String> kota = new ArrayList<String>();\nkota.add(\"Medan\");\nkota.add(\"Bandung\");\nkota.add(\"Makassar\");\nSystem.out.println(kota);",
"b": "var kota = List.of(\"Medan\", \"Bandung\", \"Makassar\");\nSystem.out.println(kota);",
"out": "[Medan, Bandung, Makassar]"
}
],
"java:Generics: kode yang aman tipe": [
{
"t": "Menghitung kemunculan dengan merge",
"tag": "Trik jarang diketahui",
"why": "Pola \"kalau kunci sudah ada tambah satu, kalau belum isi satu\" bisa diganti <code>Map.merge</code>. Diamond <code>&lt;&gt;</code> juga membuat tipe tidak perlu ditulis dua kali.",
"lang": "java",
"a": "String[] belanja = {\"kopi\", \"teh\", \"kopi\", \"gula\", \"kopi\"};\nTreeMap<String, Integer> hitung = new TreeMap<String, Integer>();\nfor (String b : belanja) {\n    if (hitung.containsKey(b)) {\n        hitung.put(b, hitung.get(b) + 1);\n    } else {\n        hitung.put(b, 1);\n    }\n}\nSystem.out.println(hitung);",
"b": "String[] belanja = {\"kopi\", \"teh\", \"kopi\", \"gula\", \"kopi\"};\nMap<String, Integer> hitung = new TreeMap<>();\nfor (String b : belanja) hitung.merge(b, 1, Integer::sum);\nSystem.out.println(hitung);",
"out": "{gula=1, kopi=3, teh=1}"
}
],
"java:Deque & Iterator": [
{
"t": "Menghapus isi list sambil melooping",
"tag": "Lebih aman",
"why": "Menghapus elemen di dalam for-each membuat iterator bingung dan Java melempar <code>ConcurrentModificationException</code>. <code>removeIf</code> menghapus dengan aman dalam satu baris.",
"lang": "java",
"a": "List<Integer> stok = new ArrayList<>(List.of(5, 0, 12, 0, 7));\nfor (Integer s : stok) {\n    if (s == 0) stok.remove(s);\n}\nSystem.out.println(stok);",
"b": "List<Integer> stok = new ArrayList<>(List.of(5, 0, 12, 0, 7));\nstok.removeIf(s -> s == 0);\nSystem.out.println(stok);",
"outA": "Exception in thread \"main\" java.util.ConcurrentModificationException",
"outB": "[5, 12, 7]"
}
],
"java:Stream API & method chaining": [
{
"t": "Menyaring dan menjumlah dengan stream",
"tag": "Lebih singkat",
"why": "Loop dengan variabel penampung dan if bisa ditulis sebagai rangkaian langkah yang terbaca seperti kalimat: saring, ubah, jumlahkan.",
"lang": "java",
"a": "int[] harga = {12_000, 45_000, 8_000, 30_000};\nint total = 0;\nfor (int i = 0; i < harga.length; i++) {\n    if (harga[i] >= 10_000) {\n        total = total + harga[i] * 2;\n    }\n}\nSystem.out.println(total);",
"b": "int[] harga = {12_000, 45_000, 8_000, 30_000};\nint total = Arrays.stream(harga)\n        .filter(h -> h >= 10_000)\n        .map(h -> h * 2)\n        .sum();\nSystem.out.println(total);",
"out": "174000"
}
],
"java:Optional: mengganti null dengan aman": [
{
"t": "Nilai cadangan untuk null",
"tag": "Trik jarang diketahui",
"why": "<code>Objects.requireNonNullElse</code> (Java 9) mengembalikan nilai cadangan kalau nilainya null. Satu baris, tanpa if-else.",
"lang": "java",
"a": "String nama = null;\nString sapaan;\nif (nama != null) {\n    sapaan = nama;\n} else {\n    sapaan = \"Tamu\";\n}\nSystem.out.println(\"Halo, \" + sapaan);",
"b": "String nama = null;\nSystem.out.println(\"Halo, \" + Objects.requireNonNullElse(nama, \"Tamu\"));",
"out": "Halo, Tamu"
}
],
"java:Checked, unchecked & exception buatan sendiri": [
{
"t": "Menutup sumber daya otomatis",
"tag": "Lebih aman",
"why": "Try-with-resources menutup reader, file, atau koneksi database secara otomatis, juga saat terjadi exception. Tidak perlu blok <code>finally</code> dan tidak ada risiko lupa memanggil <code>close()</code>.",
"lang": "java",
"a": "BufferedReader r = new BufferedReader(new StringReader(\"baris pertama\"));\ntry {\n    System.out.println(r.readLine());\n} finally {\n    r.close();\n}",
"b": "try (var r = new BufferedReader(new StringReader(\"baris pertama\"))) {\n    System.out.println(r.readLine());\n}",
"out": "baris pertama"
}
],
"python:Tipe data & typecasting": [
{
"t": "Angka besar lebih mudah dibaca dengan garis bawah",
"tag": "Trik jarang diketahui",
"why": "Python (3.6+) mengizinkan garis bawah di antara digit. <code>1_000_000</code> sama persis dengan <code>1000000</code>, tetapi jauh lebih mudah dibaca orang lain.",
"lang": "python",
"a": "harga = 1000000\nongkir = 25000\nprint(harga + ongkir)",
"b": "harga = 1_000_000\nongkir = 25_000\nprint(harga + ongkir)",
"out": "1025000"
},
{
"t": "Format rupiah tanpa loop",
"tag": "Lebih singkat",
"why": "Format spec <code>:,</code> di f-string menambahkan pemisah ribuan. Ganti koma menjadi titik untuk gaya Indonesia.",
"lang": "python",
"a": "harga = 1250000\ns = str(harga)\nhasil = \"\"\nwhile len(s) > 3:\n    hasil = \".\" + s[-3:] + hasil\n    s = s[:-3]\nprint(\"Rp\" + s + hasil)",
"b": "harga = 1_250_000\nprint(f\"Rp{harga:,}\".replace(\",\", \".\"))",
"out": "Rp1.250.000"
}
],
"python:Operator lengkap: //, **, walrus, dan @": [
{
"t": "Perbandingan berantai",
"tag": "Trik jarang diketahui",
"why": "Python membaca <code>0 &lt;= nilai &lt;= 100</code> seperti matematika. Lebih pendek dan nilai di tengah hanya dihitung sekali.",
"lang": "python",
"a": "nilai = 87\nif nilai >= 0 and nilai <= 100:\n    print(\"valid\")",
"b": "nilai = 87\nif 0 <= nilai <= 100:\n    print(\"valid\")",
"out": "valid"
}
],
"python:f-string, slicing & method string": [
{
"t": "Mencetak nama variabel dan nilainya sekaligus",
"tag": "Trik jarang diketahui",
"why": "Tanda <code>=</code> di akhir f-string (Python 3.8) mencetak ekspresinya beserta nilainya. Sangat praktis untuk debugging cepat.",
"lang": "python",
"a": "harga = 85000\njumlah = 3\nprint(\"harga=\" + str(harga) + \", jumlah=\" + str(jumlah))",
"b": "harga = 85_000\njumlah = 3\nprint(f\"{harga=}, {jumlah=}\")",
"out": "harga=85000, jumlah=3"
},
{
"t": "Membalik teks",
"tag": "Lebih singkat",
"why": "Slicing dengan langkah <code>-1</code> membaca teks dari belakang.",
"lang": "python",
"a": "kata = \"katak\"\nbalik = \"\"\nfor huruf in kata:\n    balik = huruf + balik\nprint(balik == kata)",
"b": "kata = \"katak\"\nprint(kata[::-1] == kata)",
"out": "True"
}
],
"python:enumerate, zip, break, continue, else": [
{
"t": "Nomor urut tanpa range(len())",
"tag": "Lebih mudah dibaca",
"why": "<code>enumerate</code> memberi nomor dan isinya sekaligus, dan bisa dimulai dari 1. <code>zip</code> berjalan di beberapa list bersamaan.",
"lang": "python",
"a": "nama = [\"Sari\", \"Budi\", \"Rina\"]\nnilai = [90, 78, 85]\nfor i in range(len(nama)):\n    print(str(i + 1) + \". \" + nama[i] + \": \" + str(nilai[i]))",
"b": "nama = [\"Sari\", \"Budi\", \"Rina\"]\nnilai = [90, 78, 85]\nfor no, (n, v) in enumerate(zip(nama, nilai), start=1):\n    print(f\"{no}. {n}: {v}\")",
"out": "1. Sari: 90\n2. Budi: 78\n3. Rina: 85"
}
],
"python:Tuple & unpacking": [
{
"t": "Menukar dua variabel",
"tag": "Lebih singkat",
"why": "Python bisa membongkar tuple di sisi kiri, jadi menukar nilai tidak perlu variabel sementara. Tanda <code>*</code> menampung sisanya.",
"lang": "python",
"a": "a = 5\nb = 9\nsementara = a\na = b\nb = sementara\nantrean = [\"Sari\", \"Budi\", \"Rina\", \"Dewi\"]\npertama = antrean[0]\nsisa = antrean[1:]\nprint(a, b, pertama, sisa)",
"b": "a, b = 5, 9\na, b = b, a\npertama, *sisa = [\"Sari\", \"Budi\", \"Rina\", \"Dewi\"]\nprint(a, b, pertama, sisa)",
"out": "9 5 Sari ['Budi', 'Rina', 'Dewi']"
}
],
"python:Dictionary lanjutan & operasi set": [
{
"t": "Menghitung kemunculan",
"tag": "Lebih singkat",
"why": "<code>collections.Counter</code> menghitung isi list dalam satu baris dan bisa langsung memberi yang paling sering muncul.",
"lang": "python",
"a": "belanja = [\"kopi\", \"teh\", \"kopi\", \"gula\", \"kopi\", \"teh\"]\nhitung = {}\nfor b in belanja:\n    if b in hitung:\n        hitung[b] = hitung[b] + 1\n    else:\n        hitung[b] = 1\nprint(hitung)",
"b": "from collections import Counter\nbelanja = [\"kopi\", \"teh\", \"kopi\", \"gula\", \"kopi\", \"teh\"]\nhitung = Counter(belanja)\nprint(dict(hitung))",
"out": "{'kopi': 3, 'teh': 2, 'gula': 1}"
},
{
"t": "Membuang duplikat tanpa mengacak urutan",
"tag": "Trik jarang diketahui",
"why": "<code>set</code> membuang duplikat tetapi urutannya tidak terjamin. <code>dict.fromkeys</code> juga membuang duplikat dan tetap menjaga urutan kemunculan pertama.",
"lang": "python",
"a": "kota = [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"]\nunik = []\nfor k in kota:\n    if k not in unik:\n        unik.append(k)\nprint(unik)",
"b": "kota = [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"]\nprint(list(dict.fromkeys(kota)))",
"out": "['Medan', 'Bandung', 'Ambon']"
}
],
"python:List, dict & set comprehension": [
{
"t": "Membuat list baru dari list lain",
"tag": "Lebih singkat",
"why": "Pola \"buat list kosong, loop, if, append\" bisa ditulis sebagai comprehension. Lebih pendek dan biasanya lebih cepat.",
"lang": "python",
"a": "harga = [12000, 45000, 8000, 30000]\nmahal = []\nfor h in harga:\n    if h >= 10000:\n        mahal.append(h * 2)\nprint(mahal)",
"b": "harga = [12_000, 45_000, 8_000, 30_000]\nmahal = [h * 2 for h in harga if h >= 10_000]\nprint(mahal)",
"out": "[24000, 90000, 60000]"
}
],
"python:Context manager: with": [
{
"t": "Membuka file dengan with",
"tag": "Lebih aman",
"why": "Kalau terjadi error sebelum <code>close()</code>, file tetap terbuka. Blok <code>with</code> menutup file otomatis dalam keadaan apa pun.",
"lang": "python",
"a": "f = open(\"catatan.txt\", \"w\")\nf.write(\"belajar Python\")\nf.close()\nf = open(\"catatan.txt\")\nprint(f.read())\nf.close()",
"b": "with open(\"catatan.txt\", \"w\") as f:\n    f.write(\"belajar Python\")\nwith open(\"catatan.txt\") as f:\n    print(f.read())",
"out": "belajar Python"
}
],
"python:Modul bawaan yang sering dipakai": [
{
"t": "Memeriksa \"ada yang\" dan \"semuanya\"",
"tag": "Lebih singkat",
"why": "<code>any</code> dan <code>all</code> menggantikan loop dengan variabel penanda. Keduanya berhenti begitu jawabannya sudah pasti.",
"lang": "python",
"a": "stok = [5, 0, 12, 7]\nada_habis = False\nfor s in stok:\n    if s == 0:\n        ada_habis = True\n        break\nprint(ada_habis)",
"b": "stok = [5, 0, 12, 7]\nprint(any(s == 0 for s in stok))",
"out": "True"
}
],
"python:Argumen default, keyword, *args, **kwargs": [
{
"t": "Jangan pakai list sebagai nilai default",
"tag": "Lebih aman",
"why": "Nilai default dibuat sekali saja saat fungsi didefinisikan. List default akhirnya dipakai bersama oleh setiap panggilan, sehingga isi keranjang pembeli sebelumnya ikut terbawa. Pakai <code>None</code> lalu buat list baru di dalam fungsi.",
"lang": "python",
"a": "def tambah(barang, keranjang=[]):\n    keranjang.append(barang)\n    return keranjang\n\nprint(tambah(\"kopi\"))\nprint(tambah(\"teh\"))",
"b": "def tambah(barang, keranjang=None):\n    if keranjang is None:\n        keranjang = []\n    keranjang.append(barang)\n    return keranjang\n\nprint(tambah(\"kopi\"))\nprint(tambah(\"teh\"))",
"outA": "['kopi']\n['kopi', 'teh']",
"outB": "['kopi']\n['teh']"
}
],
"python:Enkapsulasi: property & dataclass": [
{
"t": "Kelas data dengan @dataclass",
"tag": "Lebih singkat",
"why": "<code>@dataclass</code> membuat <code>__init__</code>, <code>__repr__</code>, dan <code>__eq__</code> otomatis dari daftar field.",
"lang": "python",
"a": "class Produk:\n    def __init__(self, nama, harga):\n        self.nama = nama\n        self.harga = harga\n\n    def __repr__(self):\n        return f\"Produk(nama={self.nama!r}, harga={self.harga!r})\"\n\nprint(Produk(\"Kopi Gayo\", 85000))",
"b": "from dataclasses import dataclass\n\n@dataclass\nclass Produk:\n    nama: str\n    harga: int\n\nprint(Produk(\"Kopi Gayo\", 85_000))",
"out": "Produk(nama='Kopi Gayo', harga=85000)"
}
],
"python:Iterator & generator": [
{
"t": "Menjumlah tanpa membuat list",
"tag": "Lebih hemat memori",
"why": "Tanda kurung siku membuat seluruh list di memori dulu. Tanpa kurung siku, generator menghasilkan angka satu per satu, sehingga hemat memori untuk data besar.",
"lang": "python",
"a": "total = sum([x * x for x in range(1_000_000)])\nprint(total)",
"b": "total = sum(x * x for x in range(1_000_000))\nprint(total)",
"out": "333332833333500000"
}
],
"python:raise, exception buatan sendiri & else/finally": [
{
"t": "Tangkap error yang spesifik",
"tag": "Lebih aman",
"why": "<code>except:</code> tanpa nama menangkap semua hal, termasuk salah ketik nama variabel dan Ctrl+C, sehingga bug tersembunyi. Sebutkan jenis error yang memang kamu harapkan.",
"lang": "python",
"a": "teks = \"12a\"\ntry:\n    jumlah = int(teks)\nexcept:\n    jumlah = 0\nprint(jumlah)",
"b": "teks = \"12a\"\ntry:\n    jumlah = int(teks)\nexcept ValueError:\n    jumlah = 0\nprint(jumlah)",
"out": "0"
}
],
"sql:WHERE: menyaring baris": [
{
"t": "Rentang dan daftar nilai",
"tag": "Lebih mudah dibaca",
"why": "<code>BETWEEN</code> mencakup kedua batas, dan <code>IN</code> menggantikan rangkaian <code>OR</code>. Hasilnya sama, tetapi maksud query langsung terbaca.",
"lang": "sql",
"a": "SELECT nama, kategori, harga\nFROM produk\nWHERE harga >= 10000 AND harga <= 30000\n  AND (kategori = 'Camilan' OR kategori = 'Minuman')\nORDER BY harga;",
"b": "SELECT nama, kategori, harga\nFROM produk\nWHERE harga BETWEEN 10000 AND 30000\n  AND kategori IN ('Camilan', 'Minuman')\nORDER BY harga;",
"out": "nama             | kategori | harga\n-----------------+----------+------\nKeripik Singkong | Camilan  | 15000\nKerupuk Udang    | Camilan  | 20000\nTeh Melati       | Minuman  | 25000"
}
],
"sql:SELECT & FROM": [
{
"t": "Sebutkan kolom yang dibutuhkan",
"tag": "Best practice",
"why": "<code>SELECT *</code> praktis saat menjelajah, tetapi di aplikasi sebaiknya kolom disebutkan. Data yang dikirim lebih sedikit, dan query tidak berubah perilaku diam-diam saat tabel mendapat kolom baru.",
"lang": "sql",
"a": "SELECT * FROM produk ORDER BY harga DESC LIMIT 3;",
"b": "SELECT nama, harga FROM produk ORDER BY harga DESC LIMIT 3;",
"outA": "id | nama           | kategori | harga  | stok\n---+----------------+----------+--------+-----\n6  | Madu Hutan     | Minuman  | 120000 | 15\n1  | Kopi Gayo      | Minuman  | 85000  | 40\n7  | Rendang Kaleng | Makanan  | 75000  | 0",
"outB": "nama           | harga\n---------------+-------\nMadu Hutan     | 120000\nKopi Gayo      | 85000\nRendang Kaleng | 75000"
}
],
"sql:HAVING": [
{
"t": "Menyaring hasil kelompok dengan HAVING",
"tag": "Lebih singkat",
"why": "Menyaring hasil <code>GROUP BY</code> tidak perlu subquery. <code>HAVING</code> bekerja setelah pengelompokan, sedangkan <code>WHERE</code> sebelum pengelompokan.",
"lang": "sql",
"a": "SELECT * FROM (\n  SELECT kategori, COUNT(*) AS jumlah\n  FROM produk\n  GROUP BY kategori\n) AS r\nWHERE jumlah >= 3\nORDER BY kategori;",
"b": "SELECT kategori, COUNT(*) AS jumlah\nFROM produk\nGROUP BY kategori\nHAVING COUNT(*) >= 3\nORDER BY kategori;",
"out": "kategori | jumlah\n---------+-------\nCamilan  | 3\nMinuman  | 3"
}
],
"sql:CASE, COALESCE & NULLIF": [
{
"t": "Nilai cadangan untuk NULL",
"tag": "Lebih singkat",
"why": "<code>COALESCE</code> mengambil nilai pertama yang tidak NULL. Lebih pendek dari <code>CASE WHEN ... IS NULL</code>.",
"lang": "sql",
"a": "SELECT nama,\n       CASE WHEN kota IS NULL THEN 'Belum diisi' ELSE kota END AS kota\nFROM pelanggan\nORDER BY id\nLIMIT 4;",
"b": "SELECT nama, COALESCE(kota, 'Belum diisi') AS kota\nFROM pelanggan\nORDER BY id\nLIMIT 4;",
"out": "nama  | kota\n------+---------\nAndi  | Jakarta\nBudi  | Bandung\nCitra | Surabaya\nDewi  | Jakarta"
}
],
"sql:CTE: WITH": [
{
"t": "Beri nama pada subquery dengan WITH",
"tag": "Lebih mudah dibaca",
"why": "Subquery bertingkat dibaca dari dalam ke luar. CTE dibaca dari atas ke bawah seperti langkah-langkah, dan setiap langkah punya nama.",
"lang": "sql",
"a": "SELECT p.nama, t.total\nFROM (\n  SELECT pelanggan_id, COUNT(*) AS total\n  FROM pesanan\n  GROUP BY pelanggan_id\n) AS t\nJOIN pelanggan p ON p.id = t.pelanggan_id\nWHERE t.total >= 2\nORDER BY t.total DESC, p.nama;",
"b": "WITH jumlah_pesanan AS (\n  SELECT pelanggan_id, COUNT(*) AS total\n  FROM pesanan\n  GROUP BY pelanggan_id\n)\nSELECT p.nama, j.total\nFROM jumlah_pesanan j\nJOIN pelanggan p ON p.id = j.pelanggan_id\nWHERE j.total >= 2\nORDER BY j.total DESC, p.nama;",
"out": "nama | total\n-----+------\nAndi | 3\nBudi | 2"
}
],
"sql:Window function: ROW_NUMBER, RANK, DENSE_RANK": [
{
"t": "Peringkat tanpa subquery berkorelasi",
"tag": "Lebih cepat",
"why": "Subquery berkorelasi dijalankan ulang untuk setiap baris. Window function menghitung peringkat semua baris dalam satu kali jalan.",
"lang": "sql",
"a": "SELECT nama, harga,\n       (SELECT COUNT(*) FROM produk p2 WHERE p2.harga > p1.harga) + 1 AS peringkat\nFROM produk p1\nORDER BY peringkat\nLIMIT 4;",
"b": "SELECT nama, harga,\n       RANK() OVER (ORDER BY harga DESC) AS peringkat\nFROM produk\nORDER BY peringkat\nLIMIT 4;",
"out": "nama           | harga  | peringkat\n---------------+--------+----------\nMadu Hutan     | 120000 | 1\nKopi Gayo      | 85000  | 2\nRendang Kaleng | 75000  | 3\nKacang Mete    | 60000  | 4"
}
],
"sql:Correlated subquery & EXISTS": [
{
"t": "Cek keberadaan dengan EXISTS",
"tag": "Lebih cepat",
"why": "<code>EXISTS</code> berhenti begitu satu baris cocok ditemukan, sedangkan <code>COUNT(*) &gt; 0</code> menghitung semuanya dulu.",
"lang": "sql",
"a": "SELECT nama FROM pelanggan c\nWHERE (SELECT COUNT(*) FROM pesanan o WHERE o.pelanggan_id = c.id) > 0\nORDER BY nama\nLIMIT 5;",
"b": "SELECT nama FROM pelanggan c\nWHERE EXISTS (SELECT 1 FROM pesanan o WHERE o.pelanggan_id = c.id)\nORDER BY nama\nLIMIT 5;",
"out": "nama\n-----\nAndi\nBudi\nCitra\nDewi\nEko"
}
],
"ts:Primitif, array & tuple": [
{
"t": "Pemisah angka di TypeScript dan JavaScript",
"tag": "Trik jarang diketahui",
"why": "Sama seperti Java dan Python, JavaScript modern (ES2021) dan TypeScript menerima <code>1_000_000</code>. Nilainya tetap angka biasa.",
"lang": "ts",
"a": "const harga: number = 1000000;\nconst ongkir: number = 25000;\nconsole.log(harga + ongkir);",
"b": "const harga = 1_000_000;\nconst ongkir = 25_000;\nconsole.log(harga + ongkir);",
"out": "1025000"
}
],
"ts:Objek, literal & enum": [
{
"t": "Union string sebagai pengganti enum",
"tag": "Best practice",
"why": "<code>enum</code> menghasilkan kode JavaScript tambahan. Union literal seperti <code>\"baru\" | \"dikirim\"</code> sama amannya, tanpa kode tambahan, dan nilainya bisa langsung dibandingkan dengan string dari API.",
"lang": "ts",
"a": "enum Status { Baru = \"baru\", Dikirim = \"dikirim\", Selesai = \"selesai\" }\nfunction label(s: Status): string {\n  return s === Status.Dikirim ? \"Dalam perjalanan\" : \"Lainnya\";\n}\nconsole.log(label(Status.Dikirim));",
"b": "type Status = \"baru\" | \"dikirim\" | \"selesai\";\nfunction label(s: Status): string {\n  return s === \"dikirim\" ? \"Dalam perjalanan\" : \"Lainnya\";\n}\nconsole.log(label(\"dikirim\"));",
"out": "Dalam perjalanan"
}
],
"ts:Type alias, union & intersection": [
{
"t": "Optional chaining dan ?? untuk data bersarang",
"tag": "Lebih singkat",
"why": "<code>?.</code> berhenti dengan <code>undefined</code> begitu ada bagian yang kosong, dan <code>??</code> memberi nilai cadangan. Tidak perlu rangkaian <code>&amp;&amp;</code>.",
"lang": "ts",
"a": "type Pelanggan = { nama: string; alamat?: { kota?: string } };\nconst p: Pelanggan = { nama: \"Sari\" };\nlet kota: string;\nif (p && p.alamat && p.alamat.kota) {\n  kota = p.alamat.kota;\n} else {\n  kota = \"-\";\n}\nconsole.log(kota);",
"b": "type Pelanggan = { nama: string; alamat?: { kota?: string } };\nconst p: Pelanggan = { nama: \"Sari\" };\nconsole.log(p.alamat?.kota ?? \"-\");",
"out": "-"
}
],
"ts:any, unknown, never & void": [
{
"t": "Pakai unknown, bukan any",
"tag": "Lebih aman",
"why": "<code>any</code> mematikan pemeriksaan tipe, sehingga salah ketik baru ketahuan saat program jalan. <code>unknown</code> memaksa kamu memeriksa tipenya dulu, lalu TypeScript membantumu sepenuhnya.",
"lang": "ts",
"a": "const data: any = JSON.parse('{\"harga\": 85000}');\nconsole.log(data.hargaa * 2);",
"b": "const data: unknown = JSON.parse('{\"harga\": 85000}');\nif (typeof data === \"object\" && data !== null && \"harga\" in data && typeof data.harga === \"number\") {\n  console.log(data.harga * 2);\n}",
"outA": "NaN",
"outB": "170000"
}
],
"fe0:Operator & percabangan": [
{
"t": "|| dan ?? berbeda saat nilainya 0",
"tag": "Lebih aman",
"why": "<code>||</code> menganggap <code>0</code> dan <code>\"\"</code> sebagai kosong, sehingga stok 0 malah diganti 10. <code>??</code> hanya mengganti <code>null</code> dan <code>undefined</code>. Gunakan juga <code>===</code>, bukan <code>==</code>, agar <code>0 == \"\"</code> tidak dianggap sama.",
"lang": "js",
"a": "const stok = 0;\nconst tampil = stok || 10;\nconsole.log(tampil);\nconsole.log(0 == \"\");",
"b": "const stok = 0;\nconst tampil = stok ?? 10;\nconsole.log(tampil);\nconsole.log(0 === \"\");",
"outA": "10\ntrue",
"outB": "0\nfalse"
}
],
"fe0:Variabel & tipe data": [
{
"t": "Template literal untuk menyusun teks",
"tag": "Lebih mudah dibaca",
"why": "Backtick dan <code>${...}</code> menyisipkan nilai langsung ke teks, tanpa tanda <code>+</code> dan tanda kutip yang mudah tertukar. <code>toLocaleString(\"id-ID\")</code> memberi pemisah ribuan gaya Indonesia.",
"lang": "js",
"a": "var nama = \"Sari\";\nvar total = 1250000;\nconsole.log(\"Halo \" + nama + \", totalmu Rp\" + total + \".\");",
"b": "const nama = \"Sari\";\nconst total = 1_250_000;\nconsole.log(`Halo ${nama}, totalmu Rp${total.toLocaleString(\"id-ID\")}.`);",
"outA": "Halo Sari, totalmu Rp1250000.",
"outB": "Halo Sari, totalmu Rp1.250.000."
}
],
"fe0:Array & objek": [
{
"t": "map, filter, dan reduce",
"tag": "Lebih singkat",
"why": "Ketiga method ini mengganti loop dengan variabel penampung. Kodenya terbaca sebagai langkah: saring, ubah, jumlahkan.",
"lang": "js",
"a": "const keranjang = [{ nama: \"Kopi\", harga: 85000, qty: 1 }, { nama: \"Teh\", harga: 25000, qty: 0 }, { nama: \"Gula\", harga: 18000, qty: 2 }];\nlet total = 0;\nfor (let i = 0; i < keranjang.length; i++) {\n  if (keranjang[i].qty > 0) {\n    total = total + keranjang[i].harga * keranjang[i].qty;\n  }\n}\nconsole.log(total);",
"b": "const keranjang = [{ nama: \"Kopi\", harga: 85_000, qty: 1 }, { nama: \"Teh\", harga: 25_000, qty: 0 }, { nama: \"Gula\", harga: 18_000, qty: 2 }];\nconst total = keranjang\n  .filter((b) => b.qty > 0)\n  .reduce((jml, b) => jml + b.harga * b.qty, 0);\nconsole.log(total);",
"out": "121000"
},
{
"t": "Destructuring dan spread",
"tag": "Trik jarang diketahui",
"why": "Destructuring mengambil beberapa properti sekaligus, dan spread <code>...</code> menyalin objek sambil mengubah sebagian isinya tanpa mengubah aslinya.",
"lang": "js",
"a": "const produk = { nama: \"Kopi\", harga: 85000, stok: 40 };\nconst nama = produk.nama;\nconst harga = produk.harga;\nconst baru = { nama: produk.nama, harga: produk.harga, stok: 39 };\nconsole.log(nama, harga, baru, produk.stok);",
"b": "const produk = { nama: \"Kopi\", harga: 85_000, stok: 40 };\nconst { nama, harga } = produk;\nconst baru = { ...produk, stok: 39 };\nconsole.log(nama, harga, baru, produk.stok);",
"out": "Kopi 85000 { nama: 'Kopi', harga: 85000, stok: 39 } 40"
}
],
"fe0:Mengambil data: fetch, JSON & async": [
{
"t": "async/await lebih mudah dibaca dari rantai then",
"tag": "Lebih mudah dibaca",
"why": "Kedua versi melakukan hal yang sama. Dengan <code>async</code>/<code>await</code>, kode asinkron dibaca dari atas ke bawah dan error ditangkap dengan <code>try/catch</code> biasa. Di sini <code>ambil</code> meniru <code>fetch</code> agar bisa dijalankan tanpa internet.",
"lang": "js",
"a": "const ambil = () => Promise.resolve({ json: () => Promise.resolve({ nama: \"Kopi Gayo\" }) });\nambil()\n  .then((res) => res.json())\n  .then((data) => console.log(data.nama))\n  .catch((err) => console.log(\"Gagal:\", err.message));",
"b": "const ambil = () => Promise.resolve({ json: () => Promise.resolve({ nama: \"Kopi Gayo\" }) });\nasync function tampilkan() {\n  try {\n    const res = await ambil();\n    const data = await res.json();\n    console.log(data.nama);\n  } catch (err) {\n    console.log(\"Gagal:\", err.message);\n  }\n}\ntampilkan();",
"out": "Kopi Gayo"
}
],
"fe:Event loop JavaScript": [
{
"t": "Jalankan permintaan bersamaan dengan Promise.all",
"tag": "Lebih cepat",
"why": "Tiga <code>await</code> berturut-turut menunggu satu per satu. Kalau permintaannya tidak saling bergantung, <code>Promise.all</code> menjalankannya bersamaan, sehingga waktu tunggunya hanya selama permintaan terlama.",
"lang": "js",
"a": "const tunda = (ms, v) => new Promise((r) => setTimeout(() => r(v), ms));\n(async () => {\n  const mulai = Date.now();\n  const produk = await tunda(300, \"produk\");\n  const ulasan = await tunda(300, \"ulasan\");\n  const stok = await tunda(300, \"stok\");\n  console.log(produk, ulasan, stok);\n  console.log(\"±\" + Math.round((Date.now() - mulai) / 100) * 100 + \" ms\");\n})();",
"b": "const tunda = (ms, v) => new Promise((r) => setTimeout(() => r(v), ms));\n(async () => {\n  const mulai = Date.now();\n  const [produk, ulasan, stok] = await Promise.all([\n    tunda(300, \"produk\"), tunda(300, \"ulasan\"), tunda(300, \"stok\"),\n  ]);\n  console.log(produk, ulasan, stok);\n  console.log(\"±\" + Math.round((Date.now() - mulai) / 100) * 100 + \" ms\");\n})();",
"outA": "produk ulasan stok\n±900 ms",
"outB": "produk ulasan stok\n±300 ms"
}
],
"fe:Web API: storage, observer & lainnya": [
{
"t": "Salin objek bersarang dengan structuredClone",
"tag": "Trik jarang diketahui",
"why": "Spread hanya menyalin lapisan teratas, sehingga objek di dalamnya masih dipakai bersama. <code>structuredClone</code> (bawaan browser dan Node 17+) menyalin seluruh isi, termasuk tanggal dan Map.",
"lang": "js",
"a": "const asli = { nama: \"Sari\", alamat: { kota: \"Medan\" } };\nconst salinan = { ...asli };\nsalinan.alamat.kota = \"Bandung\";\nconsole.log(asli.alamat.kota);",
"b": "const asli = { nama: \"Sari\", alamat: { kota: \"Medan\" } };\nconst salinan = structuredClone(asli);\nsalinan.alamat.kota = \"Bandung\";\nconsole.log(asli.alamat.kota);",
"outA": "Bandung",
"outB": "Medan"
}
],
"react:State dengan useState": [
{
"t": "Perbarui state dari nilai sebelumnya",
"tag": "Lebih aman",
"why": "<code>jumlah</code> di dalam satu render adalah nilai tetap. Memanggil <code>setJumlah(jumlah + 1)</code> dua kali tetap menghasilkan +1. Fungsi pembaru <code>j =&gt; j + 1</code> selalu menerima nilai terbaru, sehingga hasilnya +2.",
"lang": "jsx",
"a": "function Keranjang() {\n  const [jumlah, setJumlah] = useState(0);\n  function tambahDua() {\n    setJumlah(jumlah + 1);\n    setJumlah(jumlah + 1); // hasil akhir tetap 1\n  }\n  return <button onClick={tambahDua}>{jumlah}</button>;\n}",
"b": "function Keranjang() {\n  const [jumlah, setJumlah] = useState(0);\n  function tambahDua() {\n    setJumlah((j) => j + 1);\n    setJumlah((j) => j + 1); // hasil akhir 2\n  }\n  return <button onClick={tambahDua}>{jumlah}</button>;\n}"
}
],
"react:Event, percabangan & daftar": [
{
"t": "Gunakan id sebagai key, bukan index",
"tag": "Lebih aman",
"why": "Kalau daftar diurutkan ulang atau ada yang dihapus, key berbasis index membuat React memasangkan state ke baris yang salah, misalnya isi input pindah ke produk lain. Pakai id yang unik dan stabil.",
"lang": "jsx",
"a": "{produk.map((p, i) => (\n  <li key={i}>{p.nama}</li>\n))}",
"b": "{produk.map((p) => (\n  <li key={p.id}>{p.nama}</li>\n))}"
}
],
"react:useEffect & siklus hidup": [
{
"t": "Nilai turunan tidak perlu state dan effect",
"tag": "Lebih singkat",
"why": "Total yang bisa dihitung dari state lain cukup dihitung saat render. Menyimpannya di state lalu menyinkronkan dengan <code>useEffect</code> menambah satu render ekstra dan rawan tidak sinkron.",
"lang": "jsx",
"a": "const [keranjang, setKeranjang] = useState([]);\nconst [total, setTotal] = useState(0);\nuseEffect(() => {\n  setTotal(keranjang.reduce((t, b) => t + b.harga, 0));\n}, [keranjang]);",
"b": "const [keranjang, setKeranjang] = useState([]);\nconst total = keranjang.reduce((t, b) => t + b.harga, 0);"
}
],
"html:Form, label & input": [
{
"t": "Label sungguhan, bukan placeholder",
"tag": "Aksesibilitas",
"why": "Placeholder hilang saat pengguna mulai mengetik dan sering tidak dibacakan pembaca layar. <code>&lt;label&gt;</code> yang terhubung membuat area klik lebih luas, dan <code>autocomplete</code> serta <code>inputmode</code> membuat HP menampilkan keyboard yang tepat.",
"lang": "html",
"a": "<input type=\"text\" placeholder=\"Nomor HP\">",
"b": "<label for=\"hp\">Nomor HP</label>\n<input id=\"hp\" name=\"hp\" type=\"tel\" inputmode=\"tel\" autocomplete=\"tel\" placeholder=\"08xx xxxx xxxx\">"
}
],
"html:Gambar & figure": [
{
"t": "Gambar yang cepat dan tidak membuat halaman bergeser",
"tag": "Lebih cepat",
"why": "Ukuran <code>width</code> dan <code>height</code> membuat browser menyiapkan ruang sebelum gambar selesai diunduh, sehingga tata letak tidak meloncat. <code>loading=\"lazy\"</code> menunda gambar di bawah layar, dan <code>alt</code> wajib untuk pembaca layar.",
"lang": "html",
"a": "<img src=\"kopi.jpg\">",
"b": "<img src=\"kopi.jpg\" alt=\"Secangkir kopi Gayo di meja kayu\"\n     width=\"800\" height=\"600\" loading=\"lazy\" decoding=\"async\">"
}
],
"html:Elemen semantik": [
{
"t": "Tombol sungguhan, bukan div yang diberi onclick",
"tag": "Aksesibilitas",
"why": "<code>&lt;div&gt;</code> tidak bisa difokus dengan Tab, tidak bisa ditekan dengan Enter atau spasi, dan tidak diumumkan sebagai tombol oleh pembaca layar. <code>&lt;button&gt;</code> memberi semua itu tanpa kode tambahan.",
"lang": "html",
"a": "<div class=\"tombol\" onclick=\"beli()\">Beli</div>",
"b": "<button type=\"button\" class=\"tombol\" onclick=\"beli()\">Beli</button>"
}
],
"css:Box model": [
{
"t": "box-sizing: border-box untuk semua elemen",
"tag": "Best practice",
"why": "Secara bawaan, padding dan border ditambahkan di luar <code>width</code>, sehingga kotak 300px dengan padding 20px menjadi 342px. Dengan <code>border-box</code>, lebar yang ditulis adalah lebar akhirnya.",
"lang": "css",
"a": ".kartu {\n  width: 258px; /* 300 - 2x20 padding - 2x1 border, dihitung manual */\n  padding: 20px;\n  border: 1px solid #ccc;\n}",
"b": "*, *::before, *::after { box-sizing: border-box; }\n.kartu {\n  width: 300px;\n  padding: 20px;\n  border: 1px solid #ccc;\n}"
}
],
"css:Grid": [
{
"t": "Menengahkan isi dalam dua baris",
"tag": "Trik jarang diketahui",
"why": "Trik lama memakai <code>position</code> dan <code>transform</code>. Grid dengan <code>place-items: center</code> menengahkan isi secara horizontal dan vertikal.",
"lang": "css",
"a": ".wadah { position: relative; height: 300px; }\n.isi {\n  position: absolute;\n  top: 50%;\n  left: 50%;\n  transform: translate(-50%, -50%);\n}",
"b": ".wadah {\n  display: grid;\n  place-items: center;\n  height: 300px;\n}"
}
],
"css:Media query & mobile-first": [
{
"t": "Ukuran huruf yang ikut lebar layar dengan clamp()",
"tag": "Trik jarang diketahui",
"why": "<code>clamp(min, ideal, maks)</code> membuat judul membesar mulus mengikuti lebar layar dan tidak pernah lebih kecil atau lebih besar dari batasnya. Tidak perlu tiga media query.",
"lang": "css",
"a": "h1 { font-size: 24px; }\n@media (min-width: 600px) { h1 { font-size: 32px; } }\n@media (min-width: 1000px) { h1 { font-size: 44px; } }",
"b": "h1 { font-size: clamp(1.5rem, 1rem + 2.5vw, 2.75rem); }"
}
],
"css:Variabel CSS & tema": [
{
"t": "Warna disimpan di satu tempat",
"tag": "Best practice",
"why": "Kode warna yang diulang di banyak tempat sulit diganti dan mudah berbeda sedikit. Custom property menyimpannya sekali, dan tema gelap cukup mengganti nilainya.",
"lang": "css",
"a": ".tombol { background: #255DA2; }\n.tautan { color: #255DA2; }\n.badge  { border-color: #255da2; }",
"b": ":root { --warna-utama: #255DA2; }\n@media (prefers-color-scheme: dark) { :root { --warna-utama: #79ACEE; } }\n.tombol { background: var(--warna-utama); }\n.tautan { color: var(--warna-utama); }\n.badge  { border-color: var(--warna-utama); }"
}
],
"css:Selector sederhana": [
{
"t": "Satu selector untuk beberapa keadaan dengan :is()",
"tag": "Lebih singkat",
"why": "<code>:is()</code> menggabungkan daftar selector yang berulang. <code>:focus-visible</code> menampilkan garis fokus hanya untuk pengguna keyboard, bukan saat diklik dengan mouse.",
"lang": "css",
"a": ".menu a:hover, .menu a:focus, .footer a:hover, .footer a:focus {\n  text-decoration: underline;\n}",
"b": ":is(.menu, .footer) a:is(:hover, :focus-visible) {\n  text-decoration: underline;\n}"
}
],
"git:init, add, commit": [
{
"t": "Commit kecil dengan pesan yang jelas",
"tag": "Best practice",
"why": "<code>git add .</code> dengan pesan \"update\" mencampur banyak perubahan dalam satu commit yang tidak bisa dijelaskan. <code>git add -p</code> memilih bagian per bagian, dan pesan berformat <i>jenis: ringkasan</i> (Conventional Commits) membuat riwayat mudah dicari.",
"lang": "bash",
"a": "git add .\ngit commit -m \"update\"",
"b": "git add -p\ngit commit -m \"fix: total keranjang salah saat diskon 0%\""
}
],
"git:Remote, push & pull": [
{
"t": "Push paksa yang tidak menimpa kerja teman",
"tag": "Lebih aman",
"why": "<code>--force</code> menimpa remote tanpa melihat, sehingga commit teman yang baru di-push bisa hilang. <code>--force-with-lease</code> menolak push kalau remote sudah berubah sejak terakhir kamu ambil.",
"lang": "bash",
"a": "git push --force",
"b": "git push --force-with-lease"
}
],
"git:Membatalkan perubahan": [
{
"t": "Membatalkan commit yang sudah di-push",
"tag": "Lebih aman",
"why": "<code>reset --hard</code> menghapus commit dari riwayat dan membuat repositori teman tidak sinkron. Untuk commit yang sudah dibagikan, <code>revert</code> membuat commit baru yang membalikkan perubahan tanpa mengubah riwayat.",
"lang": "bash",
"a": "git reset --hard HEAD~1\ngit push --force",
"b": "git revert HEAD\ngit push"
}
],
"git:Riwayat & perbedaan: log dan diff": [
{
"t": "Riwayat ringkas dalam bentuk grafik",
"tag": "Trik jarang diketahui",
"why": "<code>--oneline --graph --all</code> menampilkan satu baris per commit beserta percabangannya. <code>git log -S kata</code> mencari commit yang menambah atau menghapus teks tertentu.",
"lang": "bash",
"a": "git log",
"b": "git log --oneline --graph --all -n 15\ngit log -S \"hitungDiskon\" --oneline"
}
],
"pda:Series & DataFrame": [
{
"t": "Kolom baru tanpa loop baris",
"tag": "Lebih cepat",
"why": "<code>iterrows</code> memproses baris satu per satu dengan Python biasa. Operasi kolom (vektor) dikerjakan pandas sekaligus dan bisa ratusan kali lebih cepat untuk data besar.",
"lang": "python",
"a": "import pandas as pd\ndf = pd.DataFrame({\"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"], \"produk\": [\"Kopi\", \"Teh\", \"Teh\", \"Kopi\", \"Kopi\"], \"harga\": [85000, 25000, 25000, 85000, 85000], \"qty\": [2, 4, 1, 3, 1]})\n\ntotal = []\nfor i, baris in df.iterrows():\n    total.append(baris[\"harga\"] * baris[\"qty\"])\ndf[\"total\"] = total\nprint(df[\"total\"].tolist())",
"b": "import pandas as pd\ndf = pd.DataFrame({\"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"], \"produk\": [\"Kopi\", \"Teh\", \"Teh\", \"Kopi\", \"Kopi\"], \"harga\": [85000, 25000, 25000, 85000, 85000], \"qty\": [2, 4, 1, 3, 1]})\n\ndf[\"total\"] = df[\"harga\"] * df[\"qty\"]\nprint(df[\"total\"].tolist())",
"out": "[170000, 100000, 25000, 255000, 85000]"
}
],
"pda:groupby & agregasi": [
{
"t": "Agregasi bernama dalam satu groupby",
"tag": "Lebih singkat",
"why": "Daripada melooping setiap kota lalu menyaring, <code>groupby</code> dengan <code>agg</code> bernama menghitung beberapa ringkasan sekaligus dan langsung memberi nama kolomnya.",
"lang": "python",
"a": "import pandas as pd\ndf = pd.DataFrame({\"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"], \"produk\": [\"Kopi\", \"Teh\", \"Teh\", \"Kopi\", \"Kopi\"], \"harga\": [85000, 25000, 25000, 85000, 85000], \"qty\": [2, 4, 1, 3, 1]})\n\ndf[\"total\"] = df[\"harga\"] * df[\"qty\"]\nfor kota in sorted(df[\"kota\"].unique()):\n    bagian = df[df[\"kota\"] == kota]\n    print(kota, bagian[\"total\"].sum(), len(bagian))",
"b": "import pandas as pd\ndf = pd.DataFrame({\"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"], \"produk\": [\"Kopi\", \"Teh\", \"Teh\", \"Kopi\", \"Kopi\"], \"harga\": [85000, 25000, 25000, 85000, 85000], \"qty\": [2, 4, 1, 3, 1]})\n\ndf[\"total\"] = df[\"harga\"] * df[\"qty\"]\nringkas = df.groupby(\"kota\").agg(omzet=(\"total\", \"sum\"), transaksi=(\"total\", \"size\"))\nfor kota, r in ringkas.iterrows():\n    print(kota, r[\"omzet\"], r[\"transaksi\"])",
"out": "Ambon 255000 1\nBandung 185000 2\nMedan 195000 2"
}
],
"pda:Memilih & menyaring: loc, iloc, query": [
{
"t": "Mengubah sebagian baris dengan .loc",
"tag": "Lebih aman",
"why": "Pengindeksan berantai <code>df[syarat][\"kolom\"] = ...</code> mengubah salinan sementara, bukan tabel aslinya, sehingga perubahannya hilang begitu saja. <code>.loc[syarat, \"kolom\"]</code> mengubah tabel aslinya dalam satu langkah.",
"lang": "python",
"a": "import pandas as pd\ndf = pd.DataFrame({\"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"], \"produk\": [\"Kopi\", \"Teh\", \"Teh\", \"Kopi\", \"Kopi\"], \"harga\": [85000, 25000, 25000, 85000, 85000], \"qty\": [2, 4, 1, 3, 1]})\n\nimport warnings; warnings.simplefilter(\"ignore\")\ndf[df[\"kota\"] == \"Ambon\"][\"harga\"] = 90000\nprint(df.loc[3, \"harga\"])",
"b": "import pandas as pd\ndf = pd.DataFrame({\"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\"], \"produk\": [\"Kopi\", \"Teh\", \"Teh\", \"Kopi\", \"Kopi\"], \"harga\": [85000, 25000, 25000, 85000, 85000], \"qty\": [2, 4, 1, 3, 1]})\n\ndf.loc[df[\"kota\"] == \"Ambon\", \"harga\"] = 90_000\nprint(df.loc[3, \"harga\"])",
"outA": "85000",
"outB": "90000"
}
],
"pda:Teks, tanggal & tipe data": [
{
"t": "Method .str untuk seluruh kolom teks",
"tag": "Lebih singkat",
"why": "Aksesor <code>.str</code> menjalankan method teks untuk seluruh kolom tanpa <code>apply</code> dan lambda, dan tidak error saat ada nilai kosong.",
"lang": "python",
"a": "import pandas as pd\nnama = pd.Series([\"  sari \", \"BUDI\", \"rina  \"])\nrapi = nama.apply(lambda s: s.strip().title())\nprint(rapi.tolist())",
"b": "import pandas as pd\nnama = pd.Series([\"  sari \", \"BUDI\", \"rina  \"])\nprint(nama.str.strip().str.title().tolist())",
"out": "['Sari', 'Budi', 'Rina']"
}
],
"da:Lookup & pivot table": [
{
"t": "XLOOKUP menggantikan VLOOKUP",
"tag": "Trik jarang diketahui",
"why": "VLOOKUP memakai nomor kolom yang rusak saat ada kolom disisipkan, hanya bisa mencari ke kanan, dan bawaannya mencocokkan perkiraan. XLOOKUP (Excel 365 dan Google Sheets) menunjuk kolom langsung, bisa ke kiri, dan punya nilai cadangan bila tidak ditemukan.",
"lang": "text",
"a": "=VLOOKUP(A2; Produk!A:D; 4; FALSE)",
"b": "=XLOOKUP(A2; Produk!A:A; Produk!D:D; \"Tidak ada\")"
}
],
"da:Fungsi dasar: SUM, AVERAGE, COUNT, IF": [
{
"t": "IFS menggantikan IF bersarang",
"tag": "Lebih mudah dibaca",
"why": "IF di dalam IF di dalam IF sulit dibaca dan mudah salah tutup kurung. IFS menuliskan setiap syarat dan hasilnya berpasangan dari atas ke bawah.",
"lang": "text",
"a": "=IF(B2>=85; \"A\"; IF(B2>=70; \"B\"; IF(B2>=55; \"C\"; \"D\")))",
"b": "=IFS(B2>=85; \"A\"; B2>=70; \"B\"; B2>=55; \"C\"; TRUE; \"D\")"
}
],
"bi:Pertumbuhan, margin & kontribusi": [
{
"t": "Hindari pembagian dengan nol memakai NULLIF",
"tag": "Lebih aman",
"why": "Kalau penyebutnya 0, sebagian database menghentikan query dengan error. <code>NULLIF(x, 0)</code> mengubah 0 menjadi NULL, sehingga hasil baginya NULL dan query tetap berjalan.",
"lang": "sql",
"a": "SELECT nama, stok, harga / stok AS harga_per_stok\nFROM produk\nWHERE kategori = 'Minuman'\nORDER BY nama;",
"b": "SELECT nama, stok, harga / NULLIF(stok, 0) AS harga_per_stok\nFROM produk\nWHERE kategori = 'Minuman'\nORDER BY nama;",
"out": "nama       | stok | harga_per_stok\n-----------+------+-------------------\nKopi Gayo  | 40   | 2125\nMadu Hutan | 15   | 8000\nTeh Melati | 120  | 208.33333333333334"
}
],
"de:Idempotensi & upsert": [
{
"t": "Upsert agar pipeline aman dijalankan ulang",
"tag": "Best practice",
"why": "Pipeline yang gagal di tengah sering dijalankan ulang. <code>INSERT</code> biasa menghasilkan baris ganda, sedangkan <code>INSERT ... ON CONFLICT DO UPDATE</code> (PostgreSQL, SQLite) memperbarui baris yang sudah ada, sehingga hasilnya sama berapa kali pun dijalankan.",
"lang": "python",
"a": "import sqlite3\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"CREATE TABLE stok (sku TEXT, jumlah INT)\")\nfor _ in range(2):  # pipeline dijalankan dua kali\n    db.execute(\"INSERT INTO stok VALUES ('KOPI-01', 40)\")\nprint(db.execute(\"SELECT * FROM stok\").fetchall())",
"b": "import sqlite3\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"CREATE TABLE stok (sku TEXT PRIMARY KEY, jumlah INT)\")\nfor _ in range(2):  # pipeline dijalankan dua kali\n    db.execute(\"\"\"INSERT INTO stok VALUES ('KOPI-01', 40)\n                  ON CONFLICT(sku) DO UPDATE SET jumlah = excluded.jumlah\"\"\")\nprint(db.execute(\"SELECT * FROM stok\").fetchall())",
"outA": "[('KOPI-01', 40), ('KOPI-01', 40)]",
"outB": "[('KOPI-01', 40)]"
}
],
"de:Linux & shell untuk data": [
{
"t": "Satu perintah lebih baik dari rantai cat",
"tag": "Lebih singkat",
"why": "<code>grep</code> bisa membaca file sendiri dan menghitung baris yang cocok dengan <code>-c</code>, jadi <code>cat</code> dan <code>wc</code> tidak perlu. <code>awk</code> bisa menjumlah kolom CSV tanpa membuka spreadsheet.",
"lang": "bash",
"a": "cat penjualan.csv | grep Medan | wc -l",
"b": "grep -c Medan penjualan.csv\nawk -F, '$2 == \"Medan\" { total += $3 } END { print total }' penjualan.csv",
"outA": "3",
"outB": "3\n195000"
}
],
"ux:Kurangi beban: default, sedikit pilihan, aksi jelas": [
{
"t": "Label tombol yang menyebut aksinya",
"tag": "UX writing",
"why": "\"Submit\" dan \"OK\" tidak memberi tahu apa yang terjadi setelah ditekan. Kata kerja yang spesifik mengurangi ragu, terutama untuk aksi yang tidak bisa dibatalkan.",
"lang": "html",
"a": "<p>Yakin?</p>\n<button>OK</button> <button>Batal</button>",
"b": "<p>Hapus alamat \"Rumah\"? Alamat ini tidak bisa dikembalikan.</p>\n<button>Hapus alamat</button> <button>Simpan alamat</button>"
}
],
"ds:Token: primitif, semantik, komponen": [
{
"t": "Komponen memakai token semantik, bukan kode warna",
"tag": "Best practice",
"why": "Kode heksa di dalam komponen harus dicari satu per satu saat brand berganti warna. Token semantik menyebut perannya, sehingga perubahan cukup di satu tempat dan mode gelap tinggal mengganti nilai token.",
"lang": "css",
"a": ".tombol-utama { background: #2563EB; color: #FFFFFF; }\n.tombol-utama:hover { background: #1D4ED8; }",
"b": ":root {\n  --blue-600: #2563EB;  /* primitif */\n  --blue-700: #1D4ED8;\n  --color-action-primary: var(--blue-600);        /* semantik */\n  --color-action-primary-hover: var(--blue-700);\n  --color-on-action: #FFFFFF;\n}\n.tombol-utama { background: var(--color-action-primary); color: var(--color-on-action); }\n.tombol-utama:hover { background: var(--color-action-primary-hover); }"
}
],
"ds:Warna fungsional & kontras": [
{
"t": "Error tidak boleh hanya ditandai warna merah",
"tag": "Aksesibilitas",
"why": "Sekitar 1 dari 12 laki-laki mengalami buta warna, dan pembaca layar tidak membaca warna. Pesan error perlu teks yang jelas, terhubung ke field-nya dengan <code>aria-describedby</code>, dan ditandai <code>aria-invalid</code>.",
"lang": "html",
"a": "<input type=\"email\" style=\"border-color: red\">",
"b": "<label for=\"email\">Email</label>\n<input id=\"email\" type=\"email\" aria-invalid=\"true\" aria-describedby=\"email-err\">\n<p id=\"email-err\" class=\"error\">⚠ Format email belum benar, contoh: nama@contoh.com</p>"
}
]
};
const M={java:JAVA_MODULES,python:PY_MODULES,sql:SQL_MODULES,html:HTML_MODULES,css:CSS_MODULES,fe0:FE0_MODULES,fe:FE_MODULES,react:REACT_MODULES,ts:TS_MODULES,git:GIT_MODULES,pda:PDA_MODULES,da:DA_MODULES,bi:BI_MODULES,de:DE_MODULES,ux:UX_MODULES,ds:DS_MODULES};
for(const [key,list] of Object.entries(PRO)){const i=key.indexOf(':'),mods=M[key.slice(0,i)],ti=key.slice(i+1);
  const l=mods&&mods.flatMap(m=>m.lessons).find(x=>x.t===ti);if(!l)throw new Error('tips: pelajaran tidak ditemukan: '+key);l.pro=(l.pro||[]).concat(list)}
})();
