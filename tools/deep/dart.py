"""Pendalaman jalur Dart: istilah dunia kerja dan contoh tambahan (keluaran ditulis dari program yang deterministik)."""
K = 'dart'


def X(t, code, out=None, b=None):
    return dict(t=t, b=b, code=code, lang='dart', run=False, out=out)


D = {
'Program Dart pertama': dict(
  ist=[('Dart SDK', 'Paket alat Dart: compiler, VM, formatter (dart format), analyzer (dart analyze).'),
       ('JIT vs AOT', 'JIT saat pengembangan (hot reload cepat), AOT saat rilis (aplikasi cepat dan kecil).'),
       ('Hot reload', 'Memuat ulang kode tanpa kehilangan state aplikasi; andalan produktivitas Flutter.'),
       ('Linter', 'Pemeriksa gaya otomatis; di Dart diatur lewat analysis_options.yaml (flutter_lints).')],
  cx=[X('Membaca argumen baris perintah', "void main(List<String> args) {\n  final nama = args.isEmpty ? 'Dunia' : args.first;\n  print('Halo, $nama!');\n  print('Jumlah argumen: ${args.length}');\n}\n// dart run halo.dart Sari", "Halo, Sari!\nJumlah argumen: 1")]),
'Variabel, tipe data, dan null safety': dict(
  ist=[('Sound null safety', 'Tipe tidak boleh null kecuali ditandai ?; dicek compiler.'),
       ('final vs const', 'final diisi sekali saat runtime; const ditentukan saat kompilasi.'),
       ('Null-aware operator', '?. (akses aman), ?? (nilai cadangan), ??= (isi jika null).'),
       ('late', 'Variabel non-null yang diisi belakangan; error jika dibaca sebelum diisi.')],
  cx=[X('Operator null-aware pada profil pengguna', "void main() {\n  String? kota;            // boleh null\n  final nama = 'Sari';\n  print(kota?.toUpperCase());       // tidak error, hasil null\n  print(kota ?? 'Kota belum diisi');\n  kota ??= 'Medan';\n  print('$nama tinggal di $kota (${kota.length} huruf)');\n}",
        "null\nKota belum diisi\nSari tinggal di Medan (5 huruf)", 'Setelah kota ??= \'Medan\', compiler tahu kota tidak null lagi (type promotion), jadi kota.length aman.')]),
'String, interpolasi, dan format keluaran': dict(
  ist=[('Interpolation', 'Menyisipkan nilai ke teks: \'$nama\' atau \'${ekspresi}\'.'),
       ('Raw string', "r'C:\\data' — garis miring terbalik tidak diproses."),
       ('padLeft / padRight', 'Merapikan kolom teks.'),
       ('intl package', 'Pustaka resmi format angka, tanggal, dan mata uang per locale.')],
  cx=[X('Format rupiah tanpa pustaka tambahan', "String rupiah(int n) {\n  final s = n.toString();\n  final buf = StringBuffer();\n  for (var i = 0; i < s.length; i++) {\n    if (i > 0 && (s.length - i) % 3 == 0) buf.write('.');\n    buf.write(s[i]);\n  }\n  return 'Rp$buf';\n}\n\nvoid main() {\n  print(rupiah(1250000));\n  print('Kopi'.padRight(8) + rupiah(85000).padLeft(10));\n}",
        "Rp1.250.000\nKopi      Rp85.000", "Di aplikasi nyata gunakan NumberFormat.currency(locale: 'id_ID', symbol: 'Rp') dari paket intl.")]),
'Percabangan dan perulangan': dict(
  ist=[('Switch expression', 'switch yang menghasilkan nilai dengan => (Dart 3).'),
       ('Collection if / for', 'if dan for di dalam literal list: [if (login) \'Profil\', for (x in xs) x * 2].'),
       ('Guard clause', 'Keluar lebih awal untuk kasus tidak valid.'),
       ('Exhaustiveness', 'Compiler memastikan semua kasus enum/sealed tertangani.')],
  cx=[X('Collection if dan for untuk menu aplikasi', "void main() {\n  final sudahLogin = true;\n  final kategori = ['Kopi', 'Teh'];\n  final menu = [\n    'Beranda',\n    for (final k in kategori) 'Kategori $k',\n    if (sudahLogin) 'Profil' else 'Masuk',\n  ];\n  print(menu);\n}",
        "[Beranda, Kategori Kopi, Kategori Teh, Profil]", 'Pola ini sangat sering dipakai di Flutter untuk menyusun daftar widget secara kondisional.')]),
'Latihan algoritma: Fibonacci, bubble sort, prima': dict(
  ist=[('Generator (sync*)', 'Fungsi yang menghasilkan deret nilai satu per satu dengan yield.'),
       ('Lazy evaluation', 'Nilai dihitung hanya saat dibutuhkan; take(10) berhenti di 10.'),
       ('Algorithmic thinking', 'Kemampuan memecah masalah menjadi langkah; diuji di wawancara.'),
       ('Edge case', 'Kasus pinggir seperti n = 0, 1, atau angka negatif.')],
  cx=[X('Fibonacci sebagai generator malas', "Iterable<int> fibonacci() sync* {\n  var a = 0, b = 1;\n  while (true) {\n    yield a;\n    (a, b) = (b, a + b);\n  }\n}\n\nvoid main() {\n  print(fibonacci().take(10).toList());\n  print(fibonacci().firstWhere((x) => x > 1000));\n}",
        "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n1597")]),
'Fungsi, parameter bernama, dan arrow function': dict(
  ist=[('Named parameter', 'Parameter dengan nama: kirim(ke: ..., isi: ...); bisa required.'),
       ('Optional positional', 'Parameter opsional dalam kurung siku [ ].'),
       ('Arrow function', 'Fungsi satu ekspresi: int dobel(int x) => x * 2;'),
       ('First-class function', 'Fungsi bisa disimpan di variabel dan dikirim sebagai argumen (callback).')],
  cx=[X('Parameter bernama dengan nilai bawaan', "int hitungOngkir({required int beratGram, String layanan = 'reguler', bool asuransi = false}) {\n  final perKg = layanan == 'kilat' ? 18000 : 9000;\n  final kg = (beratGram / 1000).ceil();\n  return kg * perKg + (asuransi ? 2500 : 0);\n}\n\nvoid main() {\n  print(hitungOngkir(beratGram: 1200));\n  print(hitungOngkir(beratGram: 800, layanan: 'kilat', asuransi: true));\n}",
        "18000\n20500", 'Parameter bernama membuat pemanggilan terbaca jelas. Ini alasan konstruktor widget Flutter memakainya.')]),
'Semua jenis perulangan: for, while, do-while, for-each, break, continue': dict(
  ist=[('for-in', 'Menelusuri setiap elemen Iterable.'),
       ('forEach', 'Method koleksi untuk menjalankan fungsi per elemen; tidak bisa break.'),
       ('Labeled break', 'Keluar dari loop luar dengan nama label.'),
       ('Iterable vs List', 'Iterable bisa malas; List punya indeks dan panjang tetap terhitung.')],
  cx=[X('Mencari kursi kosong pertama dengan labeled break', "void main() {\n  final kursi = [\n    [1, 1, 1],\n    [1, 0, 1],\n    [0, 0, 1],\n  ];\n  String? hasil;\n  luar:\n  for (var b = 0; b < kursi.length; b++) {\n    for (var k = 0; k < kursi[b].length; k++) {\n      if (kursi[b][k] == 0) {\n        hasil = 'baris ${b + 1}, kursi ${k + 1}';\n        break luar;\n      }\n    }\n  }\n  print(hasil ?? 'penuh');\n}", "baris 2, kursi 2")]),
'Boolean logic: AND, OR, NOT, tabel kebenaran, dan De Morgan': dict(
  ist=[('Short-circuit', '&& dan || berhenti lebih awal jika hasil sudah pasti.'),
       ('Feature flag', 'Saklar boolean untuk menyalakan fitur bagi sebagian pengguna (Remote Config).'),
       ('De Morgan', '!(a && b) sama dengan !a || !b.'),
       ('Predicate', 'Fungsi yang mengembalikan bool, misalnya where((x) => x.aktif).')],
  cx=[X('Syarat tombol Bayar aktif', "bool tombolBayarAktif({required bool login, required int item, required bool alamatLengkap, required bool sedangMemuat}) =>\n    login && item > 0 && alamatLengkap && !sedangMemuat;\n\nvoid main() {\n  print(tombolBayarAktif(login: true, item: 2, alamatLengkap: true, sedangMemuat: false));\n  print(tombolBayarAktif(login: true, item: 0, alamatLengkap: true, sedangMemuat: false));\n  // De Morgan: alasan tombol mati\n  final mati = !true || 2 <= 0 || !false || true;\n  print(mati);\n}", "true\nfalse\ntrue")]),
'Random number: bilangan acak, rentang, seed, dan mengocok': dict(
  ist=[('Random(seed)', 'Deret acak yang bisa diulang; berguna untuk tes.'),
       ('Random.secure()', 'Acak kriptografis untuk token dan OTP.'),
       ('nextInt(n)', 'Bilangan 0 sampai n−1.'),
       ('shuffle', 'Mengacak urutan list di tempat.')],
  cx=[X('Kode OTP 6 digit yang aman', "import 'dart:math';\n\nString buatOtp() {\n  final r = Random.secure();\n  return List.generate(6, (_) => r.nextInt(10)).join();\n}\n\nvoid main() {\n  final otp = buatOtp();\n  print('Panjang OTP: ${otp.length}');\n  print('Semua digit: ${RegExp(r'^\\d{6}$').hasMatch(otp)}');\n}", "Panjang OTP: 6\nSemua digit: true",
        'Nilai OTP sendiri berbeda setiap dijalankan, jadi yang dicetak hanya pemeriksaannya.')]),
'List, Map, Set dan operasi koleksi': dict(
  ist=[('where / map / fold', 'Saring, ubah, dan lipat koleksi (setara filter, map, reduce).'),
       ('Spread operator', '...list untuk menyisipkan isi list ke list lain.'),
       ('Unmodifiable', 'List.unmodifiable atau const list agar tidak bisa diubah.'),
       ('groupBy', 'Mengelompokkan elemen; tersedia di paket collection.')],
  cx=[X('Total keranjang dan kategori unik', "void main() {\n  final keranjang = [\n    {'nama': 'Kopi Gayo', 'kategori': 'Kopi', 'harga': 85000, 'qty': 2},\n    {'nama': 'Teh Melati', 'kategori': 'Teh', 'harga': 35000, 'qty': 1},\n    {'nama': 'Kopi Toraja', 'kategori': 'Kopi', 'harga': 92000, 'qty': 1},\n  ];\n  final total = keranjang.fold<int>(0, (s, i) => s + (i['harga'] as int) * (i['qty'] as int));\n  final kategori = keranjang.map((i) => i['kategori']).toSet();\n  final mahal = keranjang.where((i) => (i['harga'] as int) > 50000).map((i) => i['nama']).toList();\n  print('Total: $total');\n  print('Kategori: $kategori');\n  print('Di atas 50rb: $mahal');\n}",
        "Total: 297000\nKategori: {Kopi, Teh}\nDi atas 50rb: [Kopi Gayo, Kopi Toraja]", 'Di proyek nyata, Map seperti ini diganti class model (lihat freezed) agar aman tipe.')]),
'Class, constructor, dan getter': dict(
  ist=[('Named constructor', 'Konstruktor bernama, misalnya Produk.fromJson(map).'),
       ('Factory constructor', 'Konstruktor yang boleh mengembalikan instance yang sudah ada atau subtipe.'),
       ('Initializer list', 'Mengisi field final sebelum badan konstruktor: : assert(harga > 0).'),
       ('Immutable model', 'Semua field final + copyWith; standar state di Flutter.')],
  cx=[X('Model immutable dengan fromJson dan copyWith', "class Produk {\n  final String nama;\n  final int harga;\n  const Produk({required this.nama, required this.harga}) : assert(harga > 0);\n\n  factory Produk.fromJson(Map<String, dynamic> j) => Produk(nama: j['nama'] as String, harga: j['harga'] as int);\n\n  Produk copyWith({String? nama, int? harga}) => Produk(nama: nama ?? this.nama, harga: harga ?? this.harga);\n\n  String get labelHarga => 'Rp$harga';\n\n  @override\n  String toString() => 'Produk($nama, $labelHarga)';\n}\n\nvoid main() {\n  final p = Produk.fromJson({'nama': 'Kopi Gayo', 'harga': 85000});\n  final diskon = p.copyWith(harga: 76500);\n  print(p);\n  print(diskon);\n}", "Produk(Kopi Gayo, Rp85000)\nProduk(Kopi Gayo, Rp76500)")]),
'Inheritance, abstract class, dan mixin': dict(
  ist=[('Mixin', 'Kumpulan perilaku yang bisa "dicampur" ke banyak kelas dengan with.'),
       ('Interface implisit', 'Setiap kelas Dart otomatis bisa dipakai sebagai interface (implements).'),
       ('Sealed class', 'Kelas dengan subtipe tertutup; switch atasnya wajib lengkap (Dart 3).'),
       ('Composition over inheritance', 'Menyusun objek lebih lentur daripada pewarisan bertingkat.')],
  cx=[X('Sealed class untuk hasil pemanggilan API', "sealed class Hasil<T> {}\nclass Sukses<T> extends Hasil<T> { final T data; Sukses(this.data); }\nclass Gagal<T> extends Hasil<T> { final String pesan; Gagal(this.pesan); }\nclass Memuat<T> extends Hasil<T> {}\n\nString tampilkan(Hasil<List<String>> h) => switch (h) {\n  Memuat() => 'Memuat...',\n  Sukses(:final data) => '${data.length} produk',\n  Gagal(:final pesan) => 'Error: $pesan',\n};\n\nvoid main() {\n  print(tampilkan(Memuat()));\n  print(tampilkan(Sukses(['Kopi', 'Teh'])));\n  print(tampilkan(Gagal('tidak ada koneksi')));\n}",
        "Memuat...\n2 produk\nError: tidak ada koneksi", 'Jika kelak ada subtipe baru, compiler menandai setiap switch yang belum menanganinya.')]),
'Future, async, dan await': dict(
  ist=[('Future', 'Nilai yang akan tersedia nanti (hasil HTTP, baca berkas).'),
       ('Event loop', 'Dart menjalankan satu thread dengan antrean event; await tidak memblokir UI.'),
       ('Future.wait', 'Menjalankan beberapa Future bersamaan dan menunggu semuanya.'),
       ('Timeout', 'Batas waktu menunggu: future.timeout(Duration(seconds: 10)).')],
  cx=[X('Memuat tiga data paralel dengan Future.wait', "Future<String> ambil(String nama, int ms) async {\n  await Future.delayed(Duration(milliseconds: ms));\n  return nama;\n}\n\nFuture<void> main() async {\n  final sw = Stopwatch()..start();\n  final hasil = await Future.wait([ambil('profil', 300), ambil('saldo', 200), ambil('promo', 250)]);\n  print(hasil);\n  print('Selesai kurang dari 400 ms: ${sw.elapsedMilliseconds < 400}');\n}",
        "[profil, saldo, promo]\nSelesai kurang dari 400 ms: true", 'Jika ditunggu satu per satu, totalnya sekitar 750 ms. Dengan Future.wait, waktunya mengikuti yang paling lama (sekitar 300 ms).')]),
'Stream: data yang datang terus-menerus': dict(
  ist=[('Stream', 'Rangkaian event asinkron: lokasi GPS, chat, harga saham.'),
       ('Single-subscription vs broadcast', 'Satu pendengar saja vs banyak pendengar.'),
       ('StreamController', 'Pembuat stream manual.'),
       ('Debounce', 'Menunggu jeda input sebelum memproses (kolom pencarian).')],
  cx=[X('Stream harga dengan transformasi', "Stream<int> hargaKopi() async* {\n  for (final h in [85000, 87000, 86000, 90000]) {\n    await Future.delayed(Duration(milliseconds: 10));\n    yield h;\n  }\n}\n\nFuture<void> main() async {\n  await for (final h in hargaKopi().where((h) => h >= 86000).map((h) => 'Rp$h')) {\n    print(h);\n  }\n  print('Stream selesai');\n}", "Rp87000\nRp86000\nRp90000\nStream selesai")]),
'Package dari pub.dev dan struktur proyek': dict(
  ist=[('pubspec.yaml', 'Berkas manifes: nama, versi, dependensi, aset.'),
       ('Semantic versioning & caret', '^1.2.0 berarti boleh 1.x terbaru yang kompatibel.'),
       ('pubspec.lock', 'Mengunci versi persis; di-commit untuk aplikasi.'),
       ('Pub points / likes', 'Indikator kualitas dan popularitas paket di pub.dev.')],
  cx=[dict(t='pubspec.yaml aplikasi', lang='yaml', run=False, code="name: toko_kopi\ndescription: Aplikasi pemesanan kopi\nversion: 1.4.0+23   # versi+nomor build\nenvironment:\n  sdk: ^3.5.0\ndependencies:\n  flutter:\n    sdk: flutter\n  dio: ^5.7.0\n  flutter_riverpod: ^2.6.1\n  go_router: ^14.6.0\ndev_dependencies:\n  flutter_test:\n    sdk: flutter\n  flutter_lints: ^5.0.0\n  build_runner: ^2.4.13")]),
'Exception: try, catch, finally, dan throw': dict(
  ist=[('Exception vs Error', 'Exception untuk kondisi yang bisa ditangani; Error untuk bug program.'),
       ('on Type catch', 'Menangkap jenis exception tertentu.'),
       ('rethrow', 'Melempar ulang setelah mencatat, tanpa kehilangan stack trace.'),
       ('Error reporting', 'Mengirim error ke Crashlytics/Sentry di produksi.')],
  cx=[X('Menangani beberapa jenis exception', "class SaldoKurang implements Exception {\n  final int kurang;\n  SaldoKurang(this.kurang);\n  @override\n  String toString() => 'Saldo kurang Rp$kurang';\n}\n\nvoid bayar(int saldo, String input) {\n  try {\n    final tagihan = int.parse(input);\n    if (tagihan > saldo) throw SaldoKurang(tagihan - saldo);\n    print('Berhasil bayar $tagihan');\n  } on FormatException {\n    print('Input bukan angka: $input');\n  } on SaldoKurang catch (e) {\n    print(e);\n  } finally {\n    print('-- selesai --');\n  }\n}\n\nvoid main() {\n  bayar(100000, '75000');\n  bayar(100000, 'abc');\n  bayar(100000, '150000');\n}",
        "Berhasil bayar 75000\n-- selesai --\nInput bukan angka: abc\n-- selesai --\nSaldo kurang Rp50000\n-- selesai --")]),
'Enum, generics, dan extension method': dict(
  ist=[('Enhanced enum', 'Enum dengan field, konstruktor, dan method (Dart 2.17+).'),
       ('Extension method', 'Menambah method ke tipe yang sudah ada tanpa mewarisinya.'),
       ('Generic class', 'Kelas dengan parameter tipe: Cache<K, V>.'),
       ('Type safety', 'Kesalahan tipe ditangkap saat kompilasi, bukan saat aplikasi berjalan.')],
  cx=[X('Enhanced enum dan extension', "enum StatusPesanan {\n  baru('Menunggu bayar', false),\n  dibayar('Disiapkan', true),\n  dikirim('Dalam perjalanan', false);\n\n  const StatusPesanan(this.label, this.bisaDibatalkan);\n  final String label;\n  final bool bisaDibatalkan;\n}\n\nextension Rupiah on int {\n  String get rp => 'Rp${toString().replaceAllMapped(RegExp(r'\\B(?=(\\d{3})+(?!\\d))'), (m) => '.')}';\n}\n\nvoid main() {\n  for (final s in StatusPesanan.values) {\n    print('${s.name}: ${s.label}, batal? ${s.bisaDibatalkan}');\n  }\n  print(1250000.rp);\n}",
        "baru: Menunggu bayar, batal? false\ndibayar: Disiapkan, batal? true\ndikirim: Dalam perjalanan, batal? false\nRp1.250.000")]),
'Records dan pattern matching (Dart 3)': dict(
  ist=[('Record', 'Kumpulan nilai ringan tanpa membuat kelas: (int, String) atau (lat: .., lng: ..).'),
       ('Destructuring', 'Membongkar record/list/objek ke variabel: final (a, b) = hasil;'),
       ('Pattern', 'Bentuk yang dicocokkan di switch, if-case, dan deklarasi.'),
       ('Guard clause (when)', 'Syarat tambahan pada case: case int n when n > 100.')],
  cx=[X('Mengembalikan dua nilai dan switch dengan guard', "(int, String) cekNilai(int n) => (n, switch (n) {\n  >= 85 => 'A',\n  >= 70 => 'B',\n  >= 55 => 'C',\n  _ => 'D',\n});\n\nvoid main() {\n  final (nilai, huruf) = cekNilai(78);\n  print('$nilai -> $huruf');\n  final lokasi = (lat: 3.5952, lng: 98.6722);\n  print('Medan: ${lokasi.lat}, ${lokasi.lng}');\n  final json = {'status': 'ok', 'data': [1, 2, 3]};\n  if (json case {'status': 'ok', 'data': List data}) print('Isi data: ${data.length}');\n}",
        "78 -> B\nMedan: 3.5952, 98.6722\nIsi data: 3")]),
'Proyek: struk kasir': dict(
  ist=[('CLI app', 'Aplikasi baris perintah; cocok untuk alat internal dan otomasi.'),
       ('Separation of concerns', 'Pisahkan model, logika hitung, dan tampilan.'),
       ('Unit test (package:test)', 'Tes otomatis untuk fungsi hitung total dan pajak.'),
       ('dart compile exe', 'Mengompilasi menjadi berkas eksekusi native.')],
  cx=[X('Logika struk yang bisa diuji', "class Item {\n  final String nama;\n  final int harga, qty;\n  const Item(this.nama, this.harga, this.qty);\n  int get subtotal => harga * qty;\n}\n\n({int subtotal, int ppn, int total}) hitung(List<Item> items, {double tarifPpn = 0.12}) {\n  final sub = items.fold(0, (s, i) => s + i.subtotal);\n  final ppn = (sub * tarifPpn).round();\n  return (subtotal: sub, ppn: ppn, total: sub + ppn);\n}\n\nvoid main() {\n  final h = hitung([Item('Kopi Gayo', 85000, 2), Item('Gula Aren', 28000, 1)]);\n  print('Subtotal ${h.subtotal}, PPN ${h.ppn}, Total ${h.total}');\n}\n\n// test/struk_test.dart\n// test('PPN 12% dibulatkan', () => expect(hitung([Item('x', 1001, 1)]).ppn, 120));",
        "Subtotal 198000, PPN 23760, Total 221760")]),
}
