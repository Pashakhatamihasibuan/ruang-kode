"""Pendalaman jalur Flutter: istilah dunia kerja dan contoh kode tambahan."""
K = 'flutter'


def X(t, code, b=None, lang='dart', out=None):
    return dict(t=t, b=b, code=code, lang=lang, run=False, out=out)


D = {
'Apa itu Flutter': dict(
  ist=[('Cross-platform', 'Satu basis kode untuk Android, iOS, web, dan desktop.'),
       ('Impeller', 'Mesin render Flutter terbaru yang menggantikan Skia di iOS dan Android; animasi lebih mulus.'),
       ('Widget tree', 'Seluruh UI Flutter adalah pohon widget.'),
       ('Time-to-market', 'Waktu sampai produk rilis; alasan bisnis utama memilih Flutter.')],
  cx=[X('Aplikasi Flutter paling kecil', "import 'package:flutter/material.dart';\n\nvoid main() => runApp(const MaterialApp(\n      home: Scaffold(body: Center(child: Text('Halo, Ruang Kode!'))),\n    ));")]),
'Memasang Flutter dan membuat proyek': dict(
  ist=[('flutter doctor', 'Perintah pemeriksa kelengkapan alat (Android SDK, Xcode, lisensi).'),
       ('FVM', 'Flutter Version Management: mengunci versi Flutter per proyek agar tim seragam.'),
       ('Emulator / simulator', 'Perangkat virtual Android / iOS untuk menguji aplikasi.'),
       ('Bundle ID / applicationId', 'Identitas unik aplikasi di toko aplikasi, misalnya id.tokokopi.app.')],
  cx=[X('Membuat proyek dengan organisasi dan platform tertentu', "flutter create --org id.tokokopi --platforms android,ios toko_kopi\ncd toko_kopi\nflutter doctor -v\nflutter run -d emulator-5554", lang='bash')]),
'StatelessWidget dan StatefulWidget': dict(
  ist=[('setState', 'Memberi tahu Flutter bahwa state berubah sehingga widget digambar ulang.'),
       ('const constructor', 'Widget const tidak dibangun ulang; menghemat kerja render.'),
       ('Lifecycle', 'initState, didUpdateWidget, dispose pada State.'),
       ('dispose', 'Melepas controller dan listener; lupa dispose menyebabkan memory leak.')],
  cx=[X('Counter dengan lifecycle yang benar', "class PenghitungQty extends StatefulWidget {\n  const PenghitungQty({super.key, this.maks = 10});\n  final int maks;\n  @override\n  State<PenghitungQty> createState() => _PenghitungQtyState();\n}\n\nclass _PenghitungQtyState extends State<PenghitungQty> {\n  int qty = 1;\n\n  @override\n  Widget build(BuildContext context) => Row(mainAxisSize: MainAxisSize.min, children: [\n        IconButton(onPressed: qty > 1 ? () => setState(() => qty--) : null, icon: const Icon(Icons.remove)),\n        Text('$qty', style: Theme.of(context).textTheme.titleMedium),\n        IconButton(onPressed: qty < widget.maks ? () => setState(() => qty++) : null, icon: const Icon(Icons.add)),\n      ]);\n}", 'onPressed: null otomatis membuat tombol tampil nonaktif. Ini cara Flutter menangani batas minimum dan maksimum.')]),
'Row, Column, Container, dan Expanded': dict(
  ist=[('Main axis / cross axis', 'Sumbu utama (arah susunan) dan sumbu silang.'),
       ('Constraints go down, sizes go up', 'Aturan layout Flutter: induk memberi batas, anak memilih ukuran, induk menentukan posisi.'),
       ('RenderFlex overflowed', 'Error garis kuning-hitam saat isi Row/Column melebihi ruang.'),
       ('Flexible / Expanded', 'Membagi sisa ruang secara proporsional.')],
  cx=[X('Baris produk yang tidak overflow pada nama panjang', "Row(children: [\n  ClipRRect(borderRadius: BorderRadius.circular(8), child: Image.asset('assets/gayo.jpg', width: 56, height: 56, fit: BoxFit.cover)),\n  const SizedBox(width: 12),\n  Expanded( // tanpa Expanded, nama panjang membuat overflow\n    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [\n      Text(produk.nama, maxLines: 2, overflow: TextOverflow.ellipsis),\n      Text(rupiah(produk.harga), style: const TextStyle(fontWeight: FontWeight.w700)),\n    ]),\n  ),\n  IconButton(onPressed: tambah, icon: const Icon(Icons.add_shopping_cart)),\n])")]),
'ListView, gambar, dan aset': dict(
  ist=[('ListView.builder', 'Membangun item hanya yang terlihat; wajib untuk daftar panjang.'),
       ('Lazy loading / infinite scroll', 'Memuat halaman berikutnya saat pengguna mendekati akhir daftar.'),
       ('Image caching', 'Menyimpan gambar jaringan agar tidak diunduh ulang (cached_network_image).'),
       ('Placeholder & error widget', 'Tampilan saat gambar memuat atau gagal.')],
  cx=[X('Daftar panjang dengan muat halaman berikutnya', "ListView.builder(\n  itemCount: produk.length + (masihAda ? 1 : 0),\n  itemBuilder: (context, i) {\n    if (i == produk.length) {\n      muatBerikutnya(); // panggil sekali, jaga dengan flag sedangMemuat\n      return const Padding(padding: EdgeInsets.all(16), child: Center(child: CircularProgressIndicator()));\n    }\n    final p = produk[i];\n    return ListTile(\n      leading: CachedNetworkImage(imageUrl: p.foto, width: 48, placeholder: (_, __) => const ColoredBox(color: Colors.black12)),\n      title: Text(p.nama),\n      subtitle: Text(rupiah(p.harga)),\n    );\n  },\n)")]),
'Form dan validasi input': dict(
  ist=[('GlobalKey<FormState>', 'Kunci untuk memvalidasi dan menyimpan seluruh form.'),
       ('autovalidateMode', 'Kapan validasi berjalan: saat submit atau saat pengguna mengetik.'),
       ('TextInputType / textInputAction', 'Jenis keyboard (email, angka) dan tombol aksi (next, done).'),
       ('Inline error message', 'Pesan error di bawah field yang menjelaskan cara memperbaiki.')],
  cx=[X('Validasi nomor HP Indonesia', "final formKey = GlobalKey<FormState>();\n\nForm(\n  key: formKey,\n  autovalidateMode: AutovalidateMode.onUserInteraction,\n  child: TextFormField(\n    decoration: const InputDecoration(labelText: 'Nomor HP', prefixText: '+62 ', hintText: '812 3456 7890'),\n    keyboardType: TextInputType.phone,\n    textInputAction: TextInputAction.done,\n    validator: (v) {\n      final angka = (v ?? '').replaceAll(RegExp(r'\\D'), '');\n      if (angka.isEmpty) return 'Nomor HP wajib diisi';\n      if (!RegExp(r'^8\\d{8,11}$').hasMatch(angka)) return 'Mulai dengan 8, 9 sampai 12 digit';\n      return null;\n    },\n  ),\n)\n// tombol: if (formKey.currentState!.validate()) kirim();")]),
'Navigasi dengan go_router': dict(
  ist=[('Declarative routing', 'Rute ditentukan dari state/URL, bukan tumpukan push manual.'),
       ('Deep link', 'Tautan yang membuka halaman tertentu di aplikasi (tokokopi.id/produk/12).'),
       ('Redirect / guard', 'Mengalihkan pengguna yang belum login.'),
       ('ShellRoute', 'Rute yang berbagi kerangka, misalnya bottom navigation.')],
  cx=[X('Rute dengan parameter dan guard login', "final router = GoRouter(\n  initialLocation: '/',\n  refreshListenable: auth, // ChangeNotifier status login\n  redirect: (context, state) {\n    final butuhLogin = state.matchedLocation.startsWith('/keranjang');\n    if (butuhLogin && !auth.masuk) return '/masuk?lanjut=${state.matchedLocation}';\n    return null;\n  },\n  routes: [\n    GoRoute(path: '/', builder: (_, __) => const BerandaPage()),\n    GoRoute(path: '/produk/:id', builder: (_, s) => ProdukPage(id: int.parse(s.pathParameters['id']!))),\n    GoRoute(path: '/keranjang', builder: (_, __) => const KeranjangPage()),\n    GoRoute(path: '/masuk', builder: (_, s) => MasukPage(lanjut: s.uri.queryParameters['lanjut'])),\n  ],\n);")]),
'State management dengan Provider': dict(
  ist=[('State management', 'Cara menyimpan dan membagikan data yang berubah ke banyak widget.'),
       ('ChangeNotifier', 'Kelas yang memberi tahu pendengar saat datanya berubah.'),
       ('Lifting state up', 'Memindahkan state ke induk bersama agar bisa dipakai banyak anak.'),
       ('context.watch / read / select', 'Dengarkan perubahan / baca sekali / dengarkan sebagian kecil saja.')],
  cx=[X('Keranjang dengan ChangeNotifier', "class Keranjang extends ChangeNotifier {\n  final Map<int, int> _qty = {};\n  int get jumlahItem => _qty.values.fold(0, (a, b) => a + b);\n  void tambah(int produkId) {\n    _qty.update(produkId, (q) => q + 1, ifAbsent: () => 1);\n    notifyListeners();\n  }\n}\n\n// di main: ChangeNotifierProvider(create: (_) => Keranjang(), child: const App())\n// badge hanya dibangun ulang saat jumlahItem berubah:\nfinal n = context.select<Keranjang, int>((k) => k.jumlahItem);\nBadge(label: Text('$n'), child: const Icon(Icons.shopping_bag));")]),
'Riverpod dan BLoC/Cubit': dict(
  ist=[('Riverpod', 'State management tanpa BuildContext, aman tipe, mudah diuji; populer untuk proyek baru.'),
       ('BLoC / Cubit', 'Pola event → state yang ketat; banyak dipakai perusahaan besar dan bank.'),
       ('AsyncValue', 'Status data asinkron di Riverpod: loading, data, error.'),
       ('Unidirectional data flow', 'Data mengalir satu arah: aksi → state → UI.')],
  cx=[X('Riverpod: daftar produk dengan loading dan error', "@riverpod\nFuture<List<Produk>> daftarProduk(Ref ref) async {\n  final api = ref.watch(apiProvider);\n  return api.produk();\n}\n\nclass HalamanProduk extends ConsumerWidget {\n  const HalamanProduk({super.key});\n  @override\n  Widget build(BuildContext context, WidgetRef ref) {\n    final hasil = ref.watch(daftarProdukProvider);\n    return hasil.when(\n      loading: () => const Center(child: CircularProgressIndicator()),\n      error: (e, _) => PesanError(pesan: 'Gagal memuat produk', onCobaLagi: () => ref.invalidate(daftarProdukProvider)),\n      data: (ps) => ListView(children: [for (final p in ps) ListTile(title: Text(p.nama))]),\n    );\n  }\n}")]),
'Mengambil data API dengan http dan dio': dict(
  ist=[('REST client', 'Klien HTTP untuk memanggil API backend.'),
       ('Interceptor', 'Kode yang menyisipkan token, mencatat log, atau me-refresh token di setiap request (dio).'),
       ('Timeout & retry', 'Batas waktu dan percobaan ulang; wajib untuk jaringan seluler yang tidak stabil.'),
       ('Serialization', 'Mengubah JSON menjadi objek Dart dan sebaliknya.')],
  cx=[X('Dio dengan token dan refresh otomatis', "final dio = Dio(BaseOptions(\n  baseUrl: 'https://api.tokokopi.id/v1',\n  connectTimeout: const Duration(seconds: 10),\n  receiveTimeout: const Duration(seconds: 15),\n));\n\ndio.interceptors.add(InterceptorsWrapper(\n  onRequest: (o, h) async {\n    o.headers['Authorization'] = 'Bearer ${await penyimpanan.tokenAkses()}';\n    h.next(o);\n  },\n  onError: (e, h) async {\n    if (e.response?.statusCode == 401 && await auth.refresh()) {\n      return h.resolve(await dio.fetch(e.requestOptions)); // ulangi request dengan token baru\n    }\n    h.next(e);\n  },\n));")]),
'Penyimpanan lokal dan Firebase': dict(
  ist=[('shared_preferences', 'Penyimpanan key-value kecil (tema, bahasa, onboarding selesai).'),
       ('flutter_secure_storage', 'Penyimpanan terenkripsi (Keychain/Keystore) untuk token.'),
       ('Firestore', 'Database dokumen real-time dari Firebase.'),
       ('Security Rules', 'Aturan akses Firestore di server; wajib ditulis, jangan biarkan terbuka.')],
  cx=[X('Aturan keamanan Firestore: pengguna hanya bisa membaca pesanannya sendiri', "rules_version = '2';\nservice cloud.firestore {\n  match /databases/{db}/documents {\n    match /pesanan/{id} {\n      allow read: if request.auth != null && resource.data.uid == request.auth.uid;\n      allow create: if request.auth != null && request.resource.data.uid == request.auth.uid\n                    && request.resource.data.total is int && request.resource.data.total > 0;\n      allow update, delete: if false; // perubahan status hanya lewat Cloud Functions\n    }\n  }\n}", lang='text')]),
'Pengujian dan rilis aplikasi': dict(
  ist=[('Widget test', 'Menguji widget tanpa perangkat: pumpWidget, tap, expect.'),
       ('Integration test', 'Menguji alur lengkap di perangkat/emulator.'),
       ('App signing', 'Tanda tangan aplikasi (keystore Android, sertifikat iOS); jangan sampai hilang.'),
       ('Staged rollout', 'Merilis bertahap (10% → 50% → 100%) di Play Console.')],
  cx=[X('Widget test tombol tambah keranjang', "testWidgets('menekan + menambah qty', (tester) async {\n  await tester.pumpWidget(const MaterialApp(home: Scaffold(body: PenghitungQty(maks: 3))));\n  expect(find.text('1'), findsOneWidget);\n  await tester.tap(find.byIcon(Icons.add));\n  await tester.pump();\n  expect(find.text('2'), findsOneWidget);\n  await tester.tap(find.byIcon(Icons.add));\n  await tester.tap(find.byIcon(Icons.add)); // sudah maks, tombol nonaktif\n  await tester.pump();\n  expect(find.text('3'), findsOneWidget);\n});")]),
'Tema Material 3 dan mode gelap': dict(
  ist=[('ColorScheme.fromSeed', 'Membuat seluruh palet Material 3 dari satu warna merek.'),
       ('ThemeExtension', 'Menambah token desain sendiri (misalnya warna status) ke tema.'),
       ('Dynamic color', 'Warna mengikuti wallpaper pengguna (Android 12+).'),
       ('Design token', 'Nilai desain bernama (warna, jarak, radius) yang dipakai konsisten.')],
  cx=[X('Tema terang dan gelap dari warna merek', "final merek = const Color(0xFF6B3E26); // cokelat kopi\n\nMaterialApp(\n  theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: merek), useMaterial3: true),\n  darkTheme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: merek, brightness: Brightness.dark), useMaterial3: true),\n  themeMode: ThemeMode.system,\n  home: const BerandaPage(),\n);\n// di widget: Theme.of(context).colorScheme.primary, bukan Color(0xFF6B3E26) langsung")]),
'Animasi implisit dan Hero': dict(
  ist=[('Implicit animation', 'Widget Animated* yang beranimasi otomatis saat nilainya berubah.'),
       ('Explicit animation', 'AnimationController untuk kontrol penuh (ulang, balik, urutan).'),
       ('Hero', 'Animasi elemen bersama saat berpindah halaman (foto produk membesar).'),
       ('Reduce motion', 'Hormati pengaturan aksesibilitas pengguna yang mengurangi animasi.')],
  cx=[X('Tombol favorit beranimasi dan foto Hero', "AnimatedScale(\n  scale: favorit ? 1.2 : 1.0,\n  duration: const Duration(milliseconds: 200),\n  curve: Curves.easeOutBack,\n  child: IconButton(\n    onPressed: () => setState(() => favorit = !favorit),\n    icon: Icon(favorit ? Icons.favorite : Icons.favorite_border, color: favorit ? Colors.red : null),\n  ),\n)\n\n// daftar dan halaman detail memakai tag yang sama\nHero(tag: 'foto-${produk.id}', child: Image.network(produk.foto))")]),
'Layout responsif: LayoutBuilder dan MediaQuery': dict(
  ist=[('Breakpoint', 'Batas lebar untuk mengganti tata letak: compact < 600, medium < 840, expanded ≥ 840 (Material 3).'),
       ('Adaptive layout', 'Tata letak berubah sesuai perangkat: NavigationBar di ponsel, NavigationRail di tablet.'),
       ('MediaQuery.sizeOf', 'Membaca ukuran layar tanpa membangun ulang karena perubahan lain.'),
       ('Foldable', 'Ponsel lipat; uji di emulator foldable.')],
  cx=[X('Grid yang jumlah kolomnya mengikuti lebar', "LayoutBuilder(builder: (context, c) {\n  final kolom = c.maxWidth < 600 ? 2 : c.maxWidth < 840 ? 3 : 5;\n  return GridView.builder(\n    gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: kolom, childAspectRatio: 3 / 4, mainAxisSpacing: 12, crossAxisSpacing: 12),\n    itemCount: produk.length,\n    itemBuilder: (_, i) => KartuProduk(produk[i]),\n  );\n})")]),
'Peta library yang sering dipakai': dict(
  ist=[('Ekosistem pub.dev', 'Ribuan paket; pilih yang aktif dirawat, pub points tinggi, dan berlabel Flutter Favorite.'),
       ('Dependency hell', 'Konflik versi antar paket; kurangi dependensi yang tidak perlu.'),
       ('Lock-in', 'Ketergantungan pada satu paket/layanan; bungkus dengan lapisan sendiri.'),
       ('Audit dependensi', 'flutter pub outdated dan pemeriksaan lisensi sebelum rilis.')],
  cx=[X('Paket standar industri per kebutuhan', "# Navigasi        : go_router\n# State           : flutter_riverpod / flutter_bloc\n# HTTP            : dio (+ retrofit untuk klien bertipe)\n# Model & JSON    : freezed + json_serializable\n# Penyimpanan     : shared_preferences, flutter_secure_storage, drift\n# Gambar          : cached_network_image\n# Firebase        : firebase_core, firebase_auth, cloud_firestore, firebase_messaging, firebase_crashlytics\n# Pengujian       : mocktail, golden_toolkit / alchemist\n# Lainnya         : intl (format), permission_handler, url_launcher, image_picker\nflutter pub outdated", lang='bash')]),
'Model data dengan freezed dan json_serializable': dict(
  ist=[('Code generation', 'Kode dibuat otomatis oleh build_runner dari anotasi.'),
       ('Union type', 'Satu tipe dengan beberapa bentuk (Loading | Data | Error) di freezed.'),
       ('Value equality', 'Dua objek dengan isi sama dianggap sama (==).'),
       ('@JsonKey', 'Memetakan nama field JSON (snake_case) ke Dart (camelCase).')],
  cx=[X('Model Produk dengan freezed', "@freezed\nclass Produk with _$Produk {\n  const factory Produk({\n    required int id,\n    required String nama,\n    required int harga,\n    @JsonKey(name: 'url_foto') String? foto,\n    @Default(0) int stok,\n  }) = _Produk;\n\n  factory Produk.fromJson(Map<String, dynamic> json) => _$ProdukFromJson(json);\n}\n// dart run build_runner build --delete-conflicting-outputs\n// gratis: copyWith, ==, hashCode, toString, toJson")]),
'Database lokal: sqflite, drift, Hive, dan Isar': dict(
  ist=[('Offline-first', 'Aplikasi tetap bisa dipakai tanpa internet; sinkron saat online.'),
       ('ORM / query builder', 'drift: SQL bertipe dengan query yang dicek saat kompilasi.'),
       ('Migration', 'Perubahan skema antar versi aplikasi; wajib diuji agar data pengguna tidak hilang.'),
       ('Sync conflict', 'Data diubah di dua tempat saat offline; perlu aturan siapa yang menang.')],
  cx=[X('Tabel dan query drift', "class Catatan extends Table {\n  IntColumn get id => integer().autoIncrement()();\n  TextColumn get judul => text().withLength(min: 1, max: 80)();\n  BoolColumn get tersinkron => boolean().withDefault(const Constant(false))();\n  DateTimeColumn get diubah => dateTime()();\n}\n\n@DriftDatabase(tables: [Catatan])\nclass Db extends _$Db {\n  Db(super.e);\n  @override\n  int get schemaVersion => 2;\n\n  Stream<List<CatatanData>> pantauBelumSinkron() =>\n      (select(catatan)..where((c) => c.tersinkron.equals(false))).watch();\n}")]),
'Fitur perangkat: kamera, izin, lokasi, dan tautan': dict(
  ist=[('Runtime permission', 'Izin diminta saat dibutuhkan, dengan penjelasan alasannya.'),
       ('Permission rationale', 'Layar penjelasan sebelum dialog izin sistem; menaikkan persetujuan.'),
       ('Permanently denied', 'Izin ditolak permanen; arahkan ke Pengaturan aplikasi.'),
       ('Privacy manifest', 'Pernyataan penggunaan data yang diwajibkan App Store.')],
  cx=[X('Meminta izin kamera dengan benar', "Future<void> ambilFotoKtp(BuildContext context) async {\n  var status = await Permission.camera.status;\n  if (status.isDenied) {\n    final setuju = await tampilkanAlasan(context, 'Kamera dipakai untuk memotret KTP saat verifikasi akun.');\n    if (!setuju) return;\n    status = await Permission.camera.request();\n  }\n  if (status.isPermanentlyDenied) {\n    await openAppSettings();\n    return;\n  }\n  if (status.isGranted) {\n    final foto = await ImagePicker().pickImage(source: ImageSource.camera, imageQuality: 70, maxWidth: 1600);\n    if (foto != null) unggah(foto);\n  }\n}")]),
'Arsitektur berlapis dan dependency injection': dict(
  ist=[('Clean Architecture', 'Lapisan presentation → domain → data; aturan bisnis tidak bergantung pada Flutter.'),
       ('Repository pattern', 'Satu pintu akses data yang menyembunyikan sumbernya (API, cache, DB lokal).'),
       ('Dependency injection', 'Dependensi diberikan dari luar (Riverpod, get_it) agar mudah diganti saat tes.'),
       ('Feature-first folder', 'Struktur folder per fitur: lib/fitur/keranjang/{data,domain,presentation}.')],
  cx=[X('Repository dengan cache lokal dan API', "abstract interface class ProdukRepository {\n  Future<List<Produk>> daftar({bool paksaSegarkan = false});\n}\n\nclass ProdukRepositoryImpl implements ProdukRepository {\n  ProdukRepositoryImpl(this._api, this._db);\n  final ProdukApi _api;\n  final ProdukDao _db;\n\n  @override\n  Future<List<Produk>> daftar({bool paksaSegarkan = false}) async {\n    if (!paksaSegarkan) {\n      final lokal = await _db.semua();\n      if (lokal.isNotEmpty) return lokal;\n    }\n    final segar = await _api.produk();\n    await _db.simpanSemua(segar);\n    return segar;\n  }\n}\n\nfinal produkRepoProvider = Provider<ProdukRepository>((ref) => ProdukRepositoryImpl(ref.watch(apiProvider), ref.watch(daoProvider)));\n// di tes: ProviderScope(overrides: [produkRepoProvider.overrideWithValue(RepoPalsu())])")]),
'Proyek: aplikasi daftar tugas (Todo)': dict(
  ist=[('MVP', 'Minimum Viable Product: fitur paling kecil yang sudah berguna.'),
       ('CRUD', 'Create, Read, Update, Delete.'),
       ('Empty state', 'Tampilan saat belum ada data, mengajak pengguna bertindak.'),
       ('Undo snackbar', 'Membatalkan hapus lewat SnackBar; lebih ramah daripada dialog konfirmasi.')],
  cx=[X('Hapus dengan geser dan undo', "Dismissible(\n  key: ValueKey(tugas.id),\n  direction: DismissDirection.endToStart,\n  background: Container(color: Theme.of(context).colorScheme.errorContainer, alignment: Alignment.centerRight,\n      padding: const EdgeInsets.only(right: 16), child: const Icon(Icons.delete)),\n  onDismissed: (_) {\n    ref.read(tugasProvider.notifier).hapus(tugas.id);\n    ScaffoldMessenger.of(context).showSnackBar(SnackBar(\n      content: Text('\"${tugas.judul}\" dihapus'),\n      action: SnackBarAction(label: 'Batalkan', onPressed: () => ref.read(tugasProvider.notifier).pulihkan(tugas)),\n    ));\n  },\n  child: CheckboxListTile(value: tugas.selesai, title: Text(tugas.judul), onChanged: (_) => ref.read(tugasProvider.notifier).toggle(tugas.id)),\n)")]),
'Widget, Element, RenderObject, dan Key': dict(
  ist=[('Three trees', 'Widget (konfigurasi), Element (instance di pohon), RenderObject (layout & gambar).'),
       ('Rebuild vs relayout vs repaint', 'Membangun ulang widget murah; relayout dan repaint lebih mahal.'),
       ('Key', 'Penanda identitas widget saat urutan daftar berubah: ValueKey, ObjectKey, GlobalKey.'),
       ('Element reuse', 'Flutter memakai ulang Element jika tipe dan key sama.')],
  cx=[X('Kenapa daftar yang bisa diurutkan butuh Key', "ReorderableListView(\n  onReorder: (lama, baru) => ref.read(tugasProvider.notifier).pindah(lama, baru),\n  children: [\n    for (final t in tugas)\n      // tanpa key unik, state (misalnya checkbox) bisa \"tertinggal\" di posisi lama\n      ListTile(key: ValueKey(t.id), title: Text(t.judul), trailing: const Icon(Icons.drag_handle)),\n  ],\n)")]),
'Future, Stream, dan isolate': dict(
  ist=[('Isolate', 'Thread terpisah dengan memori sendiri di Dart; untuk kerja berat CPU.'),
       ('Jank', 'Patah-patah karena frame lebih dari 16 ms (60 fps) atau 8 ms (120 fps).'),
       ('compute / Isolate.run', 'Menjalankan fungsi di isolate lain dengan mudah.'),
       ('StreamBuilder / FutureBuilder', 'Widget yang membangun UI dari Stream/Future.')],
  cx=[X('Parsing JSON besar di isolate agar UI tidak patah', "Future<List<Produk>> parseProduk(String body) =>\n    Isolate.run(() => (jsonDecode(body) as List).map((e) => Produk.fromJson(e as Map<String, dynamic>)).toList());\n\n// 20.000 produk: di thread UI bisa membekukan layar ~300 ms, di isolate UI tetap 60 fps")]),
'Platform channel dan plugin': dict(
  ist=[('MethodChannel', 'Jalur komunikasi Dart ↔ kode native (Kotlin/Swift).'),
       ('Pigeon', 'Generator kode channel yang aman tipe.'),
       ('Federated plugin', 'Plugin yang dipecah per platform (android, ios, web).'),
       ('FFI', 'Memanggil pustaka C langsung dari Dart.')],
  cx=[X('Membaca level baterai lewat MethodChannel', "// Dart\nconst _ch = MethodChannel('id.tokokopi/baterai');\nFuture<int?> levelBaterai() => _ch.invokeMethod<int>('level');\n\n// Android (MainActivity.kt)\n// MethodChannel(flutterEngine.dartExecutor.binaryMessenger, \"id.tokokopi/baterai\").setMethodCallHandler { call, result ->\n//   if (call.method == \"level\") {\n//     val bm = getSystemService(BATTERY_SERVICE) as BatteryManager\n//     result.success(bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY))\n//   } else result.notImplemented()\n// }")]),
'DevTools dan performa': dict(
  ist=[('Profile mode', 'Mode build untuk mengukur performa; jangan ukur di debug mode.'),
       ('Rebuild stats', 'Statistik widget yang paling sering dibangun ulang.'),
       ('Raster vs UI thread', 'Dua thread utama; grafik merah di DevTools menunjukkan frame lambat.'),
       ('App size analysis', 'flutter build apk --analyze-size untuk melihat apa yang membuat aplikasi besar.')],
  cx=[X('Perintah analisis performa dan ukuran', "flutter run --profile\nflutter build appbundle --release --analyze-size --target-platform android-arm64\nflutter build apk --split-per-abi   # APK lebih kecil per arsitektur", lang='bash')]),
'Notifikasi push, Analytics, dan Crashlytics': dict(
  ist=[('FCM', 'Firebase Cloud Messaging: layanan notifikasi push.'),
       ('Topic / token', 'Kirim ke semua pelanggan topik "promo" atau ke satu perangkat lewat token.'),
       ('Crash-free users', 'Persentase pengguna tanpa crash; target umum di atas 99,5%.'),
       ('Event tracking', 'Mencatat aksi penting (add_to_cart, purchase) untuk analisis funnel.')],
  cx=[X('Inisialisasi Crashlytics dan event pembelian', "Future<void> main() async {\n  WidgetsFlutterBinding.ensureInitialized();\n  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);\n  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterFatalError;\n  PlatformDispatcher.instance.onError = (e, s) { FirebaseCrashlytics.instance.recordError(e, s, fatal: true); return true; };\n  runApp(const App());\n}\n\nawait FirebaseAnalytics.instance.logPurchase(currency: 'IDR', value: 221760, transactionId: 'INV-7');")]),
'Flavor dan CI/CD': dict(
  ist=[('Flavor', 'Varian aplikasi: dev, staging, prod dengan API dan nama berbeda.'),
       ('--dart-define', 'Menyuntikkan konfigurasi saat build.'),
       ('Fastlane / Codemagic', 'Alat otomasi build, tanda tangan, dan unggah ke toko aplikasi.'),
       ('Internal testing track', 'Jalur rilis uji internal di Play Console / TestFlight.')],
  cx=[dict(t='GitHub Actions: analisis, tes, dan build appbundle', lang='yaml', run=False, code="name: flutter-ci\non: [pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: subosito/flutter-action@v2\n        with: { channel: stable, cache: true }\n      - run: flutter pub get\n      - run: dart format --set-exit-if-changed .\n      - run: flutter analyze\n      - run: flutter test --coverage\n      - run: flutter build appbundle --flavor staging --dart-define=API_URL=https://staging.api.tokokopi.id")]),
}
