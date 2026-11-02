"""Tambahan jalur Dart: soal latihan per pelajaran, kuis tambahan, dan modul lanjutan."""
from mobile_lib import C, q, M


def S(soal, petunjuk, jawab, out=None, lang=None):
    d = {'q': soal, 'h': petunjuk, 'a': jawab}
    if out is not None: d['out'] = out
    if lang: d['lang'] = lang
    return d


# ---------- soal latihan untuk pelajaran yang sudah ada (kunci = judul pelajaran) ----------
DART_SO = {
'Program Dart pertama': [
  S('Cetak biodata tiga baris: nama, program studi, dan kota asalmu.', 'Panggil print() tiga kali di dalam main().',
    "void main() {\n  print('Nama: Rina Siregar');\n  print('Prodi: Teknik Informatika');\n  print('Kota: Medan');\n}",
    'Nama: Rina Siregar\nProdi: Teknik Informatika\nKota: Medan'),
  S("Cetak kalimat <code>It's Dart time</code> yang mengandung tanda kutip satu.", "Pakai tanda kutip dua untuk string, atau tulis \\' di dalam kutip satu.",
    "void main() {\n  print(\"It's Dart time\");\n  print('It\\'s Dart time');\n}",
    "It's Dart time\nIt's Dart time"),
],
'Variabel, tipe data, dan null safety': [
  S('Hitung luas lingkaran berjari-jari 7 dengan <code>const pi = 3.141592653589793</code>, tampilkan 2 desimal.', 'Luas = pi × r × r, lalu toStringAsFixed(2).',
    "void main() {\n  const pi = 3.141592653589793;\n  final r = 7;\n  final luas = pi * r * r;\n  print('Luas: ${luas.toStringAsFixed(2)}');\n}",
    'Luas: 153.94'),
  S('Variabel <code>String? nama</code> belum diisi. Tampilkan panjang nama, atau 0 jika null, tanpa memakai if.', 'Gabungkan ?. dan ??.',
    "void main() {\n  String? nama;\n  print('Panjang: ${nama?.length ?? 0}');\n  nama = 'Budi';\n  print('Panjang: ${nama?.length ?? 0}');\n}",
    'Panjang: 0\nPanjang: 4'),
],
'String, interpolasi, dan format keluaran': [
  S('Buat tabel nilai rata kiri-kanan untuk Andi 85.5, Budi 90, Citra 78.4. Nama lebar 10, nilai lebar 6 dengan 1 desimal.', 'nama.padRight(10) dan nilai.toStringAsFixed(1).padLeft(6).',
    "void main() {\n  final nilai = {'Andi': 85.5, 'Budi': 90.0, 'Citra': 78.4};\n  print('${'Nama'.padRight(10)}${'Nilai'.padLeft(6)}');\n  nilai.forEach((n, v) {\n    print('${n.padRight(10)}${v.toStringAsFixed(1).padLeft(6)}');\n  });\n}",
    'Nama       Nilai\nAndi        85.5\nBudi        90.0\nCitra       78.4'),
  S('Ubah daftar nomor <code>[7, 42, 315]</code> menjadi kode faktur INV-0007, INV-0042, INV-0315.', "toString().padLeft(4, '0').",
    "void main() {\n  for (final n in [7, 42, 315]) {\n    print('INV-${n.toString().padLeft(4, '0')}');\n  }\n}",
    'INV-0007\nINV-0042\nINV-0315'),
],
'Percabangan dan perulangan': [
  S('FizzBuzz 1 sampai 15: cetak Fizz untuk kelipatan 3, Buzz untuk kelipatan 5, FizzBuzz untuk keduanya.', 'Periksa kelipatan 15 lebih dulu.',
    "void main() {\n  for (var i = 1; i <= 15; i++) {\n    if (i % 15 == 0) {\n      print('FizzBuzz');\n    } else if (i % 3 == 0) {\n      print('Fizz');\n    } else if (i % 5 == 0) {\n      print('Buzz');\n    } else {\n      print(i);\n    }\n  }\n}",
    '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz'),
  S('Jumlahkan bilangan genap dari 1 sampai 100 memakai <code>continue</code> untuk melewati bilangan ganjil.', 'Jika i % 2 != 0, continue.',
    "void main() {\n  var total = 0;\n  for (var i = 1; i <= 100; i++) {\n    if (i % 2 != 0) continue;\n    total += i;\n  }\n  print('Jumlah genap: $total');\n}",
    'Jumlah genap: 2550'),
  S('Cetak segitiga bintang 4 baris (baris ke-i berisi i bintang).', "Operator * pada String mengulang teks: '*' * i.",
    "void main() {\n  for (var i = 1; i <= 4; i++) {\n    print('*' * i);\n  }\n}",
    '*\n**\n***\n****'),
],
'Latihan algoritma: Fibonacci, bubble sort, prima': [
  S('Hitung faktorial 10 dengan for.', 'Mulai dari hasil = 1, kalikan dengan i dari 1 sampai 10.',
    "void main() {\n  var hasil = 1;\n  for (var i = 1; i <= 10; i++) {\n    hasil *= i;\n  }\n  print('10! = $hasil');\n}",
    '10! = 3628800'),
  S('Cari FPB 48 dan 36 dengan algoritma Euclid.', 'Selama b != 0: (a, b) = (b, a % b). Jawabannya a.',
    "void main() {\n  var a = 48, b = 36;\n  while (b != 0) {\n    (a, b) = (b, a % b);\n  }\n  print('FPB: $a');\n}",
    'FPB: 12'),
  S('Cari angka terbesar di <code>[12, 45, 7, 89, 23]</code> tanpa method bawaan.', 'Anggap elemen pertama terbesar, lalu bandingkan satu per satu.',
    "void main() {\n  final data = [12, 45, 7, 89, 23];\n  var maks = data[0];\n  for (final x in data) {\n    if (x > maks) maks = x;\n  }\n  print('Terbesar: $maks');\n}",
    'Terbesar: 89'),
],
'Fungsi, parameter bernama, dan arrow function': [
  S('Buat fungsi <code>luas({required double p, required double l})</code> dengan arrow, lalu panggil untuk p=5, l=3.', 'double luas({required double p, required double l}) => p * l;',
    "double luas({required double p, required double l}) => p * l;\n\nvoid main() {\n  print(luas(p: 5, l: 3));\n}",
    '15.0'),
  S('Buat fungsi <code>sapa(String nama, [String? gelar])</code> dengan parameter posisi opsional.', 'Parameter opsional posisi ditulis dalam kurung siku.',
    "String sapa(String nama, [String? gelar]) =>\n    gelar == null ? 'Halo, $nama' : 'Halo, $gelar $nama';\n\nvoid main() {\n  print(sapa('Rina'));\n  print(sapa('Budi', 'Dr.'));\n}",
    'Halo, Rina\nHalo, Dr. Budi'),
],
'List, Map, Set dan operasi koleksi': [
  S('Dari nilai <code>[70, 85, 90, 60, 95]</code>, hitung rata-rata, nilai tertinggi, dan jumlah yang lulus (≥ 75).', 'fold untuk jumlah, reduce untuk maksimum, where(...).length untuk yang lulus.',
    "void main() {\n  final nilai = [70, 85, 90, 60, 95];\n  final rata = nilai.fold(0, (a, b) => a + b) / nilai.length;\n  final maks = nilai.reduce((a, b) => a > b ? a : b);\n  final lulus = nilai.where((n) => n >= 75).length;\n  print('Rata-rata: $rata');\n  print('Tertinggi: $maks');\n  print('Lulus: $lulus');\n}",
    'Rata-rata: 80.0\nTertinggi: 95\nLulus: 3'),
  S("Hitung frekuensi setiap huruf di kata <code>'banana'</code> memakai Map.", 'f[c] = (f[c] ?? 0) + 1 untuk setiap huruf.',
    "void main() {\n  final f = <String, int>{};\n  for (final c in 'banana'.split('')) {\n    f[c] = (f[c] ?? 0) + 1;\n  }\n  print(f);\n}",
    '{b: 1, a: 3, n: 2}'),
],
'Class, constructor, dan getter': [
  S('Buat class <code>Rekening</code> dengan saldo privat <code>_saldo</code>, method <code>setor</code> dan <code>tarik</code> (tolak jika saldo kurang), dan getter <code>saldo</code>.', 'Nama berawalan _ bersifat privat di file itu.',
    "class Rekening {\n  int _saldo = 0;\n  int get saldo => _saldo;\n\n  void setor(int n) => _saldo += n;\n\n  bool tarik(int n) {\n    if (n > _saldo) return false;\n    _saldo -= n;\n    return true;\n  }\n}\n\nvoid main() {\n  final r = Rekening();\n  r.setor(100000);\n  print('Tarik 30000: ${r.tarik(30000)}');\n  print('Tarik 90000: ${r.tarik(90000)}');\n  print('Saldo: ${r.saldo}');\n}",
    'Tarik 30000: true\nTarik 90000: false\nSaldo: 70000'),
  S('Tambahkan named constructor <code>Mahasiswa.baru(nama)</code> yang mengisi semester 1, dan override <code>toString</code>.', 'Named constructor bisa memanggil constructor utama dengan : this(...).',
    "class Mahasiswa {\n  final String nama;\n  final int semester;\n  Mahasiswa(this.nama, this.semester);\n  Mahasiswa.baru(String nama) : this(nama, 1);\n\n  @override\n  String toString() => '$nama (semester $semester)';\n}\n\nvoid main() {\n  print(Mahasiswa('Rina', 5));\n  print(Mahasiswa.baru('Budi'));\n}",
    'Rina (semester 5)\nBudi (semester 1)'),
],
'Inheritance, abstract class, dan mixin': [
  S('Buat <code>abstract class Bentuk</code> dengan method <code>luas()</code>, lalu turunan Lingkaran(r) dan Persegi(s). Cetak luas keduanya dengan 2 desimal.', 'Lingkaran: 3.14159 × r × r. Override di setiap turunan.',
    "abstract class Bentuk {\n  double luas();\n}\n\nclass Lingkaran extends Bentuk {\n  final double r;\n  Lingkaran(this.r);\n  @override\n  double luas() => 3.14159 * r * r;\n}\n\nclass Persegi extends Bentuk {\n  final double s;\n  Persegi(this.s);\n  @override\n  double luas() => s * s;\n}\n\nvoid main() {\n  final daftar = <Bentuk>[Lingkaran(2), Persegi(3)];\n  for (final b in daftar) {\n    print('${b.runtimeType}: ${b.luas().toStringAsFixed(2)}');\n  }\n}",
    'Lingkaran: 12.57\nPersegi: 9.00'),
  S('Buat mixin <code>Logger</code> dengan method <code>log(pesan)</code>, lalu pakai di class <code>Pesanan</code>.', 'mixin Logger { ... } lalu class Pesanan with Logger.',
    "mixin Logger {\n  void log(String m) => print('[LOG] $m');\n}\n\nclass Pesanan with Logger {\n  void bayar() {\n    log('Pesanan dibayar');\n  }\n}\n\nvoid main() {\n  Pesanan().bayar();\n}",
    '[LOG] Pesanan dibayar'),
],
'Future, async, dan await': [
  S('Simulasikan mengunduh tiga file secara berurutan (masing-masing 300 ms), lalu cetak "Semua selesai".', 'Pakai for dan await Future.delayed di dalam main yang async.',
    "Future<void> unduh(String f) async {\n  await Future.delayed(const Duration(milliseconds: 300));\n  print('$f selesai');\n}\n\nFuture<void> main() async {\n  for (final f in ['a.pdf', 'b.pdf', 'c.pdf']) {\n    await unduh(f);\n  }\n  print('Semua selesai');\n}",
    'a.pdf selesai\nb.pdf selesai\nc.pdf selesai\nSemua selesai'),
  S('Jalankan dua permintaan sekaligus dengan <code>Future.wait</code>, dan tangkap error dari fungsi yang melempar <code>Exception(\'Server sibuk\')</code>.', 'Future.wait menunggu semua; error ditangkap try/catch.',
    "Future<int> stok() async => 12;\nFuture<int> harga() async => throw Exception('Server sibuk');\n\nFuture<void> main() async {\n  final hasil = await Future.wait([stok(), stok()]);\n  print('Stok: $hasil');\n  try {\n    await harga();\n  } catch (e) {\n    print('Gagal: $e');\n  }\n}",
    'Stok: [12, 12]\nGagal: Exception: Server sibuk'),
],
'Stream: data yang datang terus-menerus': [
  S('Dari Stream angka 1–6, ambil yang genap lalu kuadratkan.', 'Stream.fromIterable, lalu where dan map seperti pada List.',
    "Future<void> main() async {\n  final s = Stream.fromIterable([1, 2, 3, 4, 5, 6])\n      .where((x) => x.isEven)\n      .map((x) => x * x);\n  await for (final x in s) {\n    print(x);\n  }\n}",
    '4\n16\n36'),
  S('Buat fungsi <code>async*</code> yang menghasilkan nama hari kerja satu per satu.', 'Pakai for-in di dalam async* lalu yield.',
    "Stream<String> hariKerja() async* {\n  for (final h in ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']) {\n    yield h;\n  }\n}\n\nFuture<void> main() async {\n  final semua = await hariKerja().toList();\n  print(semua.join(', '));\n}",
    'Senin, Selasa, Rabu, Kamis, Jumat'),
],
'Package dari pub.dev dan struktur proyek': [
  S('Tulis perintah terminal untuk menambahkan package <b>http</b> dan <b>intl</b>, serta <b>lints</b> sebagai dev dependency.', 'dart pub add, dengan --dev untuk dev dependency.',
    'dart pub add http intl\ndart pub add --dev lints', lang='bash'),
  S('Pakai package intl untuk menampilkan 7500000 sebagai Rupiah.', "NumberFormat.currency(locale: 'id_ID', symbol: 'Rp', decimalDigits: 0).",
    "import 'package:intl/intl.dart';\n\nvoid main() {\n  final rp = NumberFormat.currency(locale: 'id_ID', symbol: 'Rp', decimalDigits: 0);\n  print(rp.format(7500000));\n}",
    'Rp7.500.000'),
],
}

DART_QX = {
'Fungsi, parameter bernama, dan arrow function': [q('Parameter opsional posisi ditulis dengan?', ['{ }', '[ ]', '( )'], 1, 'Kurung siku untuk opsional posisi, kurawal untuk bernama.')],
'Class, constructor, dan getter': [q('Field berawalan garis bawah (_saldo) berarti?', ['Privat di dalam file (library) itu', 'Konstanta', 'Static'], 0, 'Dart tidak punya kata kunci private; awalan _ yang menandainya.')],
'Inheritance, abstract class, dan mixin': [q('Bisakah objek dibuat langsung dari abstract class?', ['Bisa', 'Tidak bisa', 'Hanya dengan const'], 1, 'Abstract class harus diturunkan dulu.')],
'Future, async, dan await': [q('Future.wait([a, b]) mengembalikan?', ['Hasil a saja', 'List berisi hasil a dan b', 'Stream'], 1, 'Menunggu semua lalu mengembalikan list hasilnya.')],
'Stream: data yang datang terus-menerus': [q('Kata kunci untuk mengirim nilai dari fungsi async*?', ['return', 'yield', 'emit'], 1, 'yield mengirim satu nilai ke Stream.')],
}

# ---------- modul tambahan ----------
DART_MORE = [
M('Dart lanjutan', 'Menengah', 'Menangani error, enum, generics, extension method, records, dan pattern matching Dart 3.', ['Exceptions', 'Generics', 'Records', 'Patterns'], [
 C('Exception: try, catch, finally, dan throw', [
   'Program yang baik tidak tertutup saat input salah. Kode yang berisiko dibungkus <code>try</code>. Error ditangkap dengan <code>on TipeError catch (e)</code> untuk jenis tertentu, atau <code>catch (e)</code> untuk semua. Blok <code>finally</code> selalu dijalankan, berhasil atau gagal.',
   'Kamu bisa melempar error sendiri dengan <code>throw</code>. Untuk aturan bisnis, buat class exception sendiri yang <code>implements Exception</code>, misalnya <code>SaldoKurang</code>. Pesan error jadi jelas dan bisa ditangkap secara khusus.',
   'Untuk input angka dari pengguna, <code>int.tryParse(s)</code> lebih aman daripada <code>int.parse(s)</code>: hasilnya <code>null</code> jika teks bukan angka, sehingga tidak perlu try/catch.'],
   "class SaldoKurang implements Exception {\n  final int kurang;\n  SaldoKurang(this.kurang);\n  @override\n  String toString() => 'Saldo kurang Rp$kurang';\n}\n\nvoid tarik(int saldo, int jumlah) {\n  if (jumlah > saldo) throw SaldoKurang(jumlah - saldo);\n  print('Tarik $jumlah berhasil');\n}\n\nvoid main() {\n  try {\n    final n = int.parse('12a');\n    print(n);\n  } on FormatException {\n    print('Format salah, masukkan angka saja');\n  } finally {\n    print('Selesai memeriksa input');\n  }\n\n  try {\n    tarik(50000, 80000);\n  } on SaldoKurang catch (e) {\n    print(e);\n  }\n\n  final angka = int.tryParse('99x') ?? 0;\n  print('tryParse: $angka');\n}",
   'Format salah, masukkan angka saja\nSelesai memeriksa input\nSaldo kurang Rp30000\ntryParse: 0',
   tb=[{'c': 'Pola menangani error', 'h': ['Tulisan', 'Arti'], 'r': [['try { } catch (e) { }', 'Tangkap semua error'], ['on FormatException catch (e)', 'Tangkap jenis tertentu saja'], ['finally { }', 'Selalu dijalankan'], ['throw X()', 'Lempar error'], ['rethrow', 'Lempar ulang error yang sedang ditangkap'], ['int.tryParse(s)', 'null jika bukan angka, tanpa error']]}],
   so=[S("Buat fungsi <code>bagi(a, b)</code> yang melempar <code>Exception('Pembagi nol')</code> jika b = 0. Tangkap errornya di main.", 'if (b == 0) throw Exception(...); lalu try/catch di pemanggil.',
         "double bagi(int a, int b) {\n  if (b == 0) throw Exception('Pembagi nol');\n  return a / b;\n}\n\nvoid main() {\n  print(bagi(10, 4));\n  try {\n    print(bagi(5, 0));\n  } catch (e) {\n    print('Gagal: $e');\n  }\n}",
         '2.5\nGagal: Exception: Pembagi nol'),
       S("Validasi daftar input umur <code>['20', 'abc', '-5', '17']</code>: cetak 'valid', 'bukan angka', atau 'tidak boleh negatif'.", 'int.tryParse lalu periksa null dan < 0.',
         "void main() {\n  for (final s in ['20', 'abc', '-5', '17']) {\n    final n = int.tryParse(s);\n    if (n == null) {\n      print('$s: bukan angka');\n    } else if (n < 0) {\n      print('$s: tidak boleh negatif');\n    } else {\n      print('$s: valid');\n    }\n  }\n}",
         '20: valid\nabc: bukan angka\n-5: tidak boleh negatif\n17: valid')],
   pts=['try/on/catch/finally.', 'Exception sendiri dengan implements Exception.', 'tryParse untuk input pengguna.'],
   qs=[q('Blok yang selalu dijalankan, ada error atau tidak?', ['catch', 'finally', 'on'], 1, 'finally cocok untuk menutup koneksi atau mematikan loading.'),
       q("Hasil int.tryParse('abc')?", ['0', 'null', 'Error'], 1, 'tryParse mengembalikan null jika gagal.')]),
 C('Enum, generics, dan extension method', [
   '<b>Enum</b> mendaftar pilihan yang pasti, misalnya status pesanan. Dart mendukung <b>enhanced enum</b>: enum boleh punya field dan constructor, seperti ukuran gelas yang menyimpan volume ml.',
   '<b>Generics</b> membuat class atau fungsi yang bekerja untuk berbagai tipe tanpa kehilangan keamanan tipe. <code>List&lt;int&gt;</code> adalah contoh yang sudah kamu pakai. Kamu bisa membuat sendiri, misalnya <code>Kotak&lt;T&gt;</code> atau <code>Hasil&lt;T&gt;</code> untuk respons API.',
   '<b>Extension method</b> menambah method ke tipe yang sudah ada tanpa mengubah aslinya. Contoh: <code>1250000.rp</code> menghasilkan teks Rupiah. Banyak package Flutter memakai extension, misalnya <code>context.go()</code> dari go_router.'],
   "enum Status { menunggu, dikirim, selesai }\n\nenum Ukuran {\n  kecil(250), sedang(350), besar(500);\n  final int ml;\n  const Ukuran(this.ml);\n}\n\nclass Kotak<T> {\n  final T isi;\n  Kotak(this.isi);\n  String info() => 'Kotak berisi $isi ($T)';\n}\n\nextension Rupiah on int {\n  String get rp {\n    final s = toString();\n    final b = StringBuffer();\n    for (var i = 0; i < s.length; i++) {\n      if (i > 0 && (s.length - i) % 3 == 0) b.write('.');\n      b.write(s[i]);\n    }\n    return 'Rp$b';\n  }\n}\n\nvoid main() {\n  final s = Status.dikirim;\n  print('${s.name} indeks ${s.index}');\n  for (final u in Ukuran.values) {\n    print('${u.name}: ${u.ml} ml');\n  }\n  print(Kotak<int>(7).info());\n  print(Kotak('kopi').info());\n  print(1250000.rp);\n}",
   'dikirim indeks 1\nkecil: 250 ml\nsedang: 350 ml\nbesar: 500 ml\nKotak berisi 7 (int)\nKotak berisi kopi (String)\nRp1.250.000',
   so=[S("Buat extension <code>judul</code> pada String yang mengubah 'belajar dart itu seru' menjadi 'Belajar Dart Itu Seru'.", "split(' '), ubah huruf pertama setiap kata dengan toUpperCase, lalu join(' ').",
         "extension Judul on String {\n  String get judul => split(' ')\n      .map((k) => k.isEmpty ? k : k[0].toUpperCase() + k.substring(1))\n      .join(' ');\n}\n\nvoid main() {\n  print('belajar dart itu seru'.judul);\n}",
         'Belajar Dart Itu Seru'),
       S('Buat fungsi generik <code>terbesar&lt;T extends Comparable&lt;T&gt;&gt;(List&lt;T&gt; xs)</code> dan uji dengan angka dan teks.', 'Bandingkan dengan compareTo; > 0 berarti lebih besar.',
         "T terbesar<T extends Comparable<T>>(List<T> xs) {\n  var m = xs.first;\n  for (final x in xs) {\n    if (x.compareTo(m) > 0) m = x;\n  }\n  return m;\n}\n\nvoid main() {\n  print(terbesar([3, 9, 2]));\n  print(terbesar(['apel', 'zaitun', 'mangga']));\n}",
         '9\nzaitun'),
       S('Buat enum <code>Status</code> dengan field <code>label</code> berbahasa Indonesia, lalu cetak label semua status.', 'Enhanced enum: menunggu(\'Menunggu bayar\'), ...; final String label; const Status(this.label);',
         "enum Status {\n  menunggu('Menunggu bayar'),\n  dikirim('Sedang dikirim'),\n  selesai('Sudah diterima');\n\n  final String label;\n  const Status(this.label);\n}\n\nvoid main() {\n  for (final s in Status.values) {\n    print('${s.index + 1}. ${s.label}');\n  }\n}",
         '1. Menunggu bayar\n2. Sedang dikirim\n3. Sudah diterima')],
   pts=['Enhanced enum boleh punya field.', 'Generics <T> menjaga keamanan tipe.', 'Extension menambah method ke tipe yang ada.'],
   qs=[q('Apa arti T pada class Kotak<T>?', ['Tipe yang ditentukan saat dipakai', 'Teks', 'Waktu'], 0, 'T diganti tipe nyata, misalnya Kotak<int>.'),
       q('Extension method mengubah class aslinya?', ['Ya', 'Tidak, hanya menambah method saat dipakai', 'Hanya untuk int'], 1, 'Class asli tidak berubah.')]),
 C('Records dan pattern matching (Dart 3)', [
   '<b>Record</b> mengelompokkan beberapa nilai tanpa membuat class: <code>(double, double)</code> atau dengan nama <code>({String nama, int umur})</code>. Cocok untuk fungsi yang mengembalikan lebih dari satu nilai.',
   '<b>Pattern</b> membongkar data: <code>final (lo, hi) = minMax(data);</code>. Dengan <code>if (json case {...})</code> kamu bisa memeriksa bentuk JSON sekaligus mengambil nilainya, tanpa casting manual.',
   '<code>switch</code> pada <b>sealed class</b> memeriksa semua kemungkinan. Jika ada turunan baru yang lupa ditangani, Dart memberi error saat kompilasi. Pola ini sangat dipakai untuk status layar Flutter: Memuat, Sukses, Gagal.'],
   "(double, double) minMax(List<double> xs) {\n  var lo = xs.first, hi = xs.first;\n  for (final x in xs) {\n    if (x < lo) lo = x;\n    if (x > hi) hi = x;\n  }\n  return (lo, hi);\n}\n\nsealed class Bentuk {}\nclass Lingkaran extends Bentuk {\n  final double r;\n  Lingkaran(this.r);\n}\nclass Persegi extends Bentuk {\n  final double s;\n  Persegi(this.s);\n}\n\ndouble luas(Bentuk b) => switch (b) {\n      Lingkaran(r: final r) => 3.14 * r * r,\n      Persegi(s: final s) => s * s,\n    };\n\nvoid main() {\n  final (lo, hi) = minMax([3.5, 1.2, 9.8]);\n  print('min $lo, max $hi');\n\n  final user = (nama: 'Rina', umur: 20);\n  print('${user.nama} ${user.umur}');\n\n  final json = {'nama': 'Budi', 'nilai': [80, 90]};\n  if (json case {'nama': String n, 'nilai': [int a, int b]}) {\n    print('$n rata-rata ${(a + b) / 2}');\n  }\n\n  print(luas(Lingkaran(2)));\n  print(luas(Persegi(3)));\n}",
   'min 1.2, max 9.8\nRina 20\nBudi rata-rata 85.0\n12.56\n9.0',
   so=[S('Buat fungsi yang mengembalikan record <code>(int jumlah, double rata)</code> dari <code>[4, 8, 6]</code>, lalu bongkar hasilnya.', 'return (total, total / xs.length); lalu final (j, r) = ringkas(...).',
         "(int, double) ringkas(List<int> xs) {\n  final total = xs.fold(0, (a, b) => a + b);\n  return (total, total / xs.length);\n}\n\nvoid main() {\n  final (j, r) = ringkas([4, 8, 6]);\n  print('Jumlah $j, rata-rata $r');\n}",
         'Jumlah 18, rata-rata 6.0'),
       S('Kelompokkan umur <code>[8, 15, 30]</code> menjadi anak (&lt; 13), remaja (13–17), dewasa, memakai switch expression dengan relational pattern.', 'Kasus: < 13 =>, >= 13 && < 18 =>, _ =>.',
         "String kategori(int u) => switch (u) {\n      < 13 => 'anak',\n      >= 13 && < 18 => 'remaja',\n      _ => 'dewasa',\n    };\n\nvoid main() {\n  for (final u in [8, 15, 30]) {\n    print('$u: ${kategori(u)}');\n  }\n}",
         '8: anak\n15: remaja\n30: dewasa')],
   pts=['Record (a, b) untuk banyak nilai kembalian.', 'Pattern membongkar record, list, map, dan objek.', 'switch + sealed class memeriksa semua kasus.'],
   qs=[q('Keuntungan sealed class pada switch?', ['Lebih cepat', 'Dart memastikan semua turunan ditangani', 'Bisa diubah saat runtime'], 1, 'Exhaustiveness checking saat kompilasi.')]),
]),
M('Proyek konsol Dart', 'Menengah', 'Menggabungkan class, koleksi, format, dan logika dalam satu program kasir.', ['Project'], [
 C('Proyek: struk kasir', [
   'Proyek ini menggabungkan semua yang sudah dipelajari: class <code>Item</code> dengan getter <code>subtotal</code>, list sebagai keranjang, loop untuk menjumlahkan, operator ternary untuk diskon, dan <code>padLeft</code>/<code>padRight</code> untuk struk yang rapi.',
   'Fungsi <code>rp()</code> menambahkan titik pemisah ribuan tanpa package. Di aplikasi Flutter sungguhan, pakai <code>NumberFormat</code> dari package intl.',
   'Jalankan di dartpad.dev, lalu kerjakan tantangan di bawah untuk mengembangkannya.'],
   "class Item {\n  final String nama;\n  final int harga;\n  final int qty;\n  const Item(this.nama, this.harga, this.qty);\n  int get subtotal => harga * qty;\n}\n\nString rp(int n) {\n  final s = n.toString();\n  final b = StringBuffer();\n  for (var i = 0; i < s.length; i++) {\n    if (i > 0 && (s.length - i) % 3 == 0) b.write('.');\n    b.write(s[i]);\n  }\n  return b.toString();\n}\n\nvoid main() {\n  const keranjang = [\n    Item('Kopi susu', 18000, 2),\n    Item('Roti bakar', 22500, 1),\n    Item('Air mineral', 5000, 3),\n  ];\n  print('${'Barang'.padRight(14)}${'Qty'.padLeft(4)}${'Subtotal'.padLeft(10)}');\n  print('-' * 28);\n  var total = 0;\n  for (final it in keranjang) {\n    print('${it.nama.padRight(14)}${it.qty.toString().padLeft(4)}${rp(it.subtotal).padLeft(10)}');\n    total += it.subtotal;\n  }\n  final diskon = total >= 50000 ? total ~/ 10 : 0;\n  print('-' * 28);\n  print('${'Total'.padRight(18)}${rp(total).padLeft(10)}');\n  print('${'Diskon 10%'.padRight(18)}${rp(diskon).padLeft(10)}');\n  print('${'Bayar'.padRight(18)}${rp(total - diskon).padLeft(10)}');\n}",
   'Barang         Qty  Subtotal\n----------------------------\nKopi susu        2    36.000\nRoti bakar       1    22.500\nAir mineral      3    15.000\n----------------------------\nTotal                 73.500\nDiskon 10%             7.350\nBayar                 66.150',
   so=[S('Tambahkan PPN 11% (dibulatkan) yang dihitung dari harga setelah diskon, lalu tampilkan total akhir.', 'ppn = (setelahDiskon * 11 / 100).round(). round() membulatkan .5 ke atas.',
         "  final setelahDiskon = total - diskon;\n  final ppn = (setelahDiskon * 11 / 100).round();\n  print('${'PPN 11%'.padRight(18)}${rp(ppn).padLeft(10)}');\n  print('${'Total akhir'.padRight(18)}${rp(setelahDiskon + ppn).padLeft(10)}');",
         'PPN 11%                7.277\nTotal akhir           73.427'),
       S('Cetak barang diurutkan dari subtotal terbesar.', 'Salin list dulu ([...keranjang]) karena list const tidak bisa diurutkan, lalu sort dengan compareTo terbalik.',
         "  final urut = [...keranjang]..sort((a, b) => b.subtotal.compareTo(a.subtotal));\n  for (final it in urut) {\n    print('${it.nama}: ${rp(it.subtotal)}');\n  }",
         'Kopi susu: 36.000\nRoti bakar: 22.500\nAir mineral: 15.000'),
       S('Ubah diskon menjadi bertingkat: 15% jika total ≥ 100.000, 10% jika ≥ 50.000, selain itu 0. Pakai switch expression.', 'switch (total) { >= 100000 => total * 15 ~/ 100, >= 50000 => total ~/ 10, _ => 0 }',
         "  final diskon = switch (total) {\n    >= 100000 => total * 15 ~/ 100,\n    >= 50000 => total ~/ 10,\n    _ => 0,\n  };")],
   pts=['Class + getter untuk data barang.', 'Loop + akumulator untuk total.', 'padLeft/padRight untuk struk berkolom.'],
   qs=[q('Kenapa keranjang const tidak bisa langsung di-sort?', ['List const tidak bisa diubah', 'sort hanya untuk Set', 'Karena berisi objek'], 0, 'Salin dulu dengan [...keranjang].')]),
]),
]
