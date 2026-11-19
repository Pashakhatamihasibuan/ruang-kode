"""Pendalaman jalur Slicing Mobile (Figma ke Flutter/Compose)."""
K = 'slm'


def X(t, code, b=None, lang='dart'):
    return dict(t=t, b=b, code=code, lang=lang, run=False)


D = {
'Membaca desain mobile': dict(
  ist=[('Dev Mode', 'Mode Figma untuk developer: ukuran, jarak, warna, dan kode.'),
       ('dp / pt', 'Satuan independen kepadatan layar: dp (Android), pt (iOS), logical pixel (Flutter).'),
       ('Frame 360×800 / 393×852', 'Ukuran frame acuan umum Android dan iPhone.'),
       ('Redline / spec', 'Anotasi jarak dan ukuran di desain.')],
  cx=[X('Catatan spesifikasi sebelum menulis kode', "// Layar: Masuk (frame 393x852)\n// Grid: margin 24, gutter 16\n// Judul: Plus Jakarta Sans 28/36 SemiBold, onSurface\n// Field: tinggi 56, radius 12, border 1 outline, jarak antar field 16\n// Tombol utama: tinggi 52, radius 12, primary, teks labelLarge\n// State: default, fokus, error, nonaktif, memuat", lang='text')]),
'Ekspor aset dan ikon': dict(
  ist=[('Density bucket', 'mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi (Android); @1x @2x @3x (iOS/Flutter).'),
       ('Vector asset', 'SVG/Vector Drawable yang tajam di semua ukuran dan kecil ukurannya.'),
       ('Adaptive icon', 'Ikon Android dengan lapisan depan dan latar yang dipotong sesuai bentuk perangkat.'),
       ('WebP / AVIF', 'Format gambar modern yang lebih kecil dari PNG/JPEG.')],
  cx=[X('Struktur aset Flutter dengan resolusi', "assets/\n  images/\n    kopi.webp          # 1x\n    2.0x/kopi.webp     # 2x\n    3.0x/kopi.webp     # 3x\n  icons/\n    keranjang.svg      # pakai flutter_svg\n\n# pubspec.yaml\nflutter:\n  assets:\n    - assets/images/\n    - assets/icons/", lang='text')]),
'Token desain ke ThemeData dan MaterialTheme': dict(
  ist=[('Design token', 'Nilai desain bernama: color.primary, space.md, radius.lg.'),
       ('Figma Variables', 'Fitur Figma untuk menyimpan token dan mode (terang/gelap).'),
       ('Single source of truth', 'Token di satu tempat, dipakai desain dan kode.'),
       ('Semantic vs primitive token', 'brown-700 (primitif) vs color.action.primary (semantik).')],
  cx=[X('Token jarak dan radius sebagai ThemeExtension', "@immutable\nclass Jarak extends ThemeExtension<Jarak> {\n  const Jarak({this.xs = 4, this.sm = 8, this.md = 16, this.lg = 24});\n  final double xs, sm, md, lg;\n  @override\n  Jarak copyWith({double? xs, double? sm, double? md, double? lg}) => Jarak(xs: xs ?? this.xs, sm: sm ?? this.sm, md: md ?? this.md, lg: lg ?? this.lg);\n  @override\n  Jarak lerp(Jarak? o, double t) => this;\n}\n\n// pakai: final j = Theme.of(context).extension<Jarak>()!;  Padding(padding: EdgeInsets.all(j.md))")]),
'Memetakan auto layout ke Row dan Column': dict(
  ist=[('Auto layout', 'Fitur Figma setara Row/Column: arah, jarak, padding, perataan.'),
       ('Hug / Fill / Fixed', 'Ukuran mengikuti isi / mengisi ruang (Expanded) / tetap.'),
       ('Spacing between items', 'Setara SizedBox antar anak atau Arrangement.spacedBy.'),
       ('Absolute position', 'Elemen menimpa; setara Stack/Box + Positioned/align.')],
  cx=[X('Auto layout ke Flutter: hug, fill, spacing', "// Figma: horizontal, spacing 12, padding 16, item kedua 'Fill container'\nPadding(\n  padding: const EdgeInsets.all(16),\n  child: Row(children: [\n    const Icon(Icons.local_cafe),          // Hug\n    const SizedBox(width: 12),              // spacing\n    const Expanded(child: Text('Kopi Gayo')), // Fill\n    const SizedBox(width: 12),\n    Text('Rp85.000'),                       // Hug\n  ]),\n)\n// Flutter 3.27+: Row(spacing: 12, children: [...])")]),
'Layar login di Flutter': dict(
  ist=[('SafeArea', 'Menghindari notch, status bar, dan gesture bar.'),
       ('Keyboard avoidance', 'Konten bergeser/scroll saat keyboard muncul.'),
       ('AutofillHints', 'Mengizinkan pengelola kata sandi mengisi email dan password.'),
       ('Obscure toggle', 'Tombol lihat/sembunyikan kata sandi.')],
  cx=[X('Field email dan kata sandi dengan autofill', "AutofillGroup(\n  child: Column(children: [\n    TextFormField(\n      decoration: const InputDecoration(labelText: 'Email'),\n      keyboardType: TextInputType.emailAddress,\n      autofillHints: const [AutofillHints.email],\n      textInputAction: TextInputAction.next,\n    ),\n    const SizedBox(height: 16),\n    TextFormField(\n      decoration: InputDecoration(\n        labelText: 'Kata sandi',\n        suffixIcon: IconButton(icon: Icon(lihat ? Icons.visibility_off : Icons.visibility), onPressed: () => setState(() => lihat = !lihat)),\n      ),\n      obscureText: !lihat,\n      autofillHints: const [AutofillHints.password],\n      onFieldSubmitted: (_) => masuk(),\n    ),\n  ]),\n)")]),
'Layar login di Jetpack Compose': dict(
  ist=[('imePadding', 'Modifier agar konten naik di atas keyboard.'),
       ('VisualTransformation', 'Menyembunyikan karakter kata sandi.'),
       ('ContentType autofill', 'Petunjuk autofill di Compose (semantics contentType).'),
       ('FocusRequester', 'Memindahkan fokus ke field berikutnya.')],
  cx=[X('Field kata sandi dengan toggle', '@Composable\nfun FieldSandi(nilai: String, onUbah: (String) -> Unit) {\n    var lihat by rememberSaveable { mutableStateOf(false) }\n    OutlinedTextField(\n        value = nilai, onValueChange = onUbah, label = { Text("Kata sandi") }, singleLine = true,\n        visualTransformation = if (lihat) VisualTransformation.None else PasswordVisualTransformation(),\n        keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Password, imeAction = ImeAction.Done),\n        trailingIcon = { IconButton(onClick = { lihat = !lihat }) { Icon(if (lihat) Icons.Default.VisibilityOff else Icons.Default.Visibility, if (lihat) "Sembunyikan" else "Tampilkan") } },\n        modifier = Modifier.fillMaxWidth(),\n    )\n}', lang='kotlin')]),
'Kartu produk dan grid di Flutter': dict(
  ist=[('Card / elevation', 'Kartu dengan bayangan atau garis tepi sesuai desain.'),
       ('Aspect ratio', 'Rasio gambar tetap (1:1, 4:3) agar grid rapi.'),
       ('SliverGrid', 'Grid di dalam CustomScrollView bersama header yang ikut tergulir.'),
       ('Ink / InkWell', 'Efek riak saat disentuh.')],
  cx=[X('Kartu produk dengan rasio gambar tetap', "class KartuProduk extends StatelessWidget {\n  const KartuProduk(this.p, {super.key});\n  final Produk p;\n  @override\n  Widget build(BuildContext context) => Card(\n        clipBehavior: Clip.antiAlias,\n        child: InkWell(\n          onTap: () => context.push('/produk/${p.id}'),\n          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [\n            AspectRatio(aspectRatio: 1, child: Image.network(p.foto, fit: BoxFit.cover)),\n            Padding(\n              padding: const EdgeInsets.all(12),\n              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [\n                Text(p.nama, maxLines: 2, overflow: TextOverflow.ellipsis),\n                const SizedBox(height: 4),\n                Text(rupiah(p.harga), style: Theme.of(context).textTheme.titleSmall),\n              ]),\n            ),\n          ]),\n        ),\n      );\n}")]),
'Kartu produk dan LazyVerticalGrid di Compose': dict(
  ist=[('GridCells.Adaptive', 'Jumlah kolom menyesuaikan lebar minimum item.'),
       ('span', 'Item yang mengambil beberapa kolom (header, banner).'),
       ('ElevatedCard / OutlinedCard', 'Varian kartu Material 3.'),
       ('contentPadding', 'Jarak tepi grid yang tetap ikut tergulir.')],
  cx=[X('Grid adaptif dengan header selebar penuh', 'LazyVerticalGrid(\n    columns = GridCells.Adaptive(minSize = 160.dp),\n    contentPadding = PaddingValues(16.dp),\n    horizontalArrangement = Arrangement.spacedBy(12.dp),\n    verticalArrangement = Arrangement.spacedBy(12.dp),\n) {\n    item(span = { GridItemSpan(maxLineSpan) }) { Text("Kopi pilihan minggu ini", style = MaterialTheme.typography.titleLarge) }\n    items(produk, key = { it.id }) { p -> KartuProduk(p) }\n}', lang='kotlin')]),
'Bottom navigation dan top app bar': dict(
  ist=[('NavigationBar', 'Navigasi bawah Material 3 untuk 3–5 tujuan utama.'),
       ('Top app bar scroll behavior', 'App bar yang mengecil/menghilang saat menggulir.'),
       ('Badge', 'Penanda angka/titik pada ikon (keranjang, notifikasi).'),
       ('Navigation state preservation', 'Setiap tab mempertahankan posisi gulir dan tumpukannya.')],
  cx=[X('NavigationBar dengan badge keranjang (Flutter)', "NavigationBar(\n  selectedIndex: indeks,\n  onDestinationSelected: (i) => setState(() => indeks = i),\n  destinations: [\n    const NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'Beranda'),\n    const NavigationDestination(icon: Icon(Icons.search), label: 'Cari'),\n    NavigationDestination(icon: Badge(label: Text('$jumlahKeranjang'), isLabelVisible: jumlahKeranjang > 0, child: const Icon(Icons.shopping_bag_outlined)), label: 'Keranjang'),\n    const NavigationDestination(icon: Icon(Icons.person_outline), label: 'Akun'),\n  ],\n)")]),
'Layar berbagai ukuran': dict(
  ist=[('Window size class', 'Compact, medium, expanded: kategori lebar layar Material 3.'),
       ('Text scaling', 'Pengguna bisa memperbesar huruf hingga 200%; layout tidak boleh pecah.'),
       ('Landscape', 'Orientasi mendatar; uji minimal layar utama.'),
       ('Small device', 'Uji di layar kecil (320–360 dp lebar) yang masih banyak di Indonesia.')],
  cx=[X('Membatasi lebar konten di tablet', "Center(\n  child: ConstrainedBox(\n    constraints: const BoxConstraints(maxWidth: 480), // form tidak melebar penuh di tablet\n    child: const FormMasuk(),\n  ),\n)")]),
'Pixel-perfect dan golden test': dict(
  ist=[('Pixel-perfect', 'Hasil build sama dengan desain dalam toleransi yang disepakati.'),
       ('Golden test', 'Tes tangkapan layar yang dibandingkan dengan gambar acuan.'),
       ('Design QA', 'Pemeriksaan hasil oleh desainer sebelum rilis.'),
       ('Overlay comparison', 'Menumpuk screenshot dan desain dengan transparansi untuk mencari selisih.')],
  cx=[X('Golden test kartu produk di dua tema', "testWidgets('golden kartu produk', (tester) async {\n  for (final mode in [ThemeMode.light, ThemeMode.dark]) {\n    await tester.pumpWidget(MaterialApp(\n      theme: temaTerang, darkTheme: temaGelap, themeMode: mode,\n      home: const Center(child: SizedBox(width: 180, child: KartuProduk(produkContoh))),\n    ));\n    await expectLater(find.byType(KartuProduk), matchesGoldenFile('goldens/kartu_${mode.name}.png'));\n  }\n});\n// perbarui acuan: flutter test --update-goldens")]),
'Proyek: slicing aplikasi kedai kopi': dict(
  ist=[('Screen inventory', 'Daftar semua layar dan state yang harus dibuat.'),
       ('Component-first', 'Bangun komponen kecil (kartu, tombol) dulu, baru rakit layar.'),
       ('Mock data', 'Data contoh realistis untuk slicing sebelum API siap.'),
       ('Handoff checklist', 'Daftar periksa serah terima: state, aksesibilitas, mode gelap.')],
  cx=[X('Inventaris layar dan komponen', "Layar: Splash, Onboarding (3), Masuk, Daftar, Beranda, Detail Produk, Keranjang, Checkout, Status Pesanan, Profil\nState tiap layar: memuat, kosong, error, sukses, offline\nKomponen: TombolUtama, FieldTeks, KartuProduk, ChipKategori, PemilihQty, BarisKeranjang, BannerPromo\nUrutan kerja: token → komponen + golden test → layar → navigasi → data palsu → API", lang='text')]),
'Contoh desain: layar Masuk': dict(
  ist=[('Hierarki visual', 'Urutan perhatian: judul → field → tombol utama → tautan sekunder.'),
       ('Primary action', 'Satu tombol utama per layar.'),
       ('Error state', 'Tampilan saat input salah atau server menolak.'),
       ('Social login', 'Masuk dengan Google/Apple; wajib menyediakan Apple jika ada login pihak ketiga di iOS.')],
  cx=[X('Spesifikasi layar Masuk', "Judul       : 'Selamat datang kembali' (headlineSmall)\nSubjudul    : 'Masuk untuk melanjutkan pesananmu' (bodyMedium, onSurfaceVariant)\nField       : Email, Kata sandi (dengan tombol lihat)\nTautan      : 'Lupa kata sandi?' rata kanan\nTombol      : 'Masuk' (filled, lebar penuh, 52 tinggi)\nPemisah     : 'atau'\nTombol      : 'Masuk dengan Google' (outlined)\nBawah       : 'Belum punya akun? Daftar'", lang='text')]),
'Langkah 1: membaca spesifikasi dan memecah layar': dict(
  ist=[('Component breakdown', 'Memecah layar menjadi komponen dari besar ke kecil.'),
       ('Widget tree sketch', 'Sketsa pohon widget sebelum menulis kode.'),
       ('Reusable vs one-off', 'Menentukan komponen mana yang dipakai ulang.'),
       ('Acceptance criteria', 'Syarat layar dianggap selesai.')],
  cx=[X('Sketsa pohon widget layar Masuk', "Scaffold\n└─ SafeArea\n   └─ SingleChildScrollView (padding 24)\n      └─ Column\n         ├─ Judul + Subjudul\n         ├─ FieldTeks(email)\n         ├─ FieldTeks(sandi, rahasia: true)\n         ├─ TautanLupaSandi (Align kanan)\n         ├─ TombolUtama('Masuk', memuat: state.memuat)\n         ├─ PemisahAtau\n         ├─ TombolGoogle\n         └─ BarisDaftar", lang='text')]),
'Langkah 2: token menjadi tema': dict(
  ist=[('Color role mapping', 'Memetakan warna Figma ke peran ColorScheme.'),
       ('Text style mapping', 'Memetakan gaya teks Figma ke TextTheme (headlineSmall, bodyMedium).'),
       ('Font licensing', 'Pastikan font boleh dipakai di aplikasi (Google Fonts umumnya OFL).'),
       ('google_fonts package', 'Memuat font dari Google Fonts; bundel untuk produksi agar tidak mengunduh.')],
  cx=[X('ThemeData dari token', "final skema = ColorScheme.fromSeed(seedColor: const Color(0xFF6B3E26)).copyWith(\n  primary: const Color(0xFF6B3E26),\n  error: const Color(0xFFB3261E),\n);\nfinal tema = ThemeData(\n  colorScheme: skema,\n  textTheme: GoogleFonts.plusJakartaSansTextTheme(),\n  inputDecorationTheme: InputDecorationTheme(\n    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),\n    contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 18),\n  ),\n  filledButtonTheme: FilledButtonThemeData(style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(52), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)))),\n);")]),
'Langkah 3: kerangka layar, safe area, dan scroll': dict(
  ist=[('SingleChildScrollView', 'Agar layar tetap bisa digulir saat keyboard muncul atau huruf diperbesar.'),
       ('resizeToAvoidBottomInset', 'Scaffold menyusut saat keyboard muncul (bawaan true).'),
       ('Dismiss keyboard', 'Menutup keyboard saat menyentuh area kosong.'),
       ('Edge-to-edge', 'Konten sampai tepi layar dengan padding insets yang benar.')],
  cx=[X('Kerangka yang aman keyboard', "Scaffold(\n  body: GestureDetector(\n    onTap: () => FocusScope.of(context).unfocus(),\n    child: SafeArea(\n      child: SingleChildScrollView(\n        padding: const EdgeInsets.all(24),\n        keyboardDismissBehavior: ScrollViewKeyboardDismissBehavior.onDrag,\n        child: const FormMasuk(),\n      ),\n    ),\n  ),\n)")]),
'Langkah 4: komponen form sesuai spesifikasi': dict(
  ist=[('Reusable component', 'Satu FieldTeks dipakai di semua form agar konsisten.'),
       ('Touch target', 'Minimal 48×48 dp untuk semua elemen yang bisa disentuh.'),
       ('Semantics label', 'Label untuk pembaca layar (TalkBack, VoiceOver).'),
       ('Error text', 'Pesan error spesifik di bawah field.')],
  cx=[X('Tombol utama dengan state memuat', "class TombolUtama extends StatelessWidget {\n  const TombolUtama({super.key, required this.label, required this.onPressed, this.memuat = false});\n  final String label;\n  final VoidCallback? onPressed;\n  final bool memuat;\n  @override\n  Widget build(BuildContext context) => FilledButton(\n        onPressed: memuat ? null : onPressed,\n        child: memuat\n            ? Semantics(label: 'Sedang memproses', child: const SizedBox.square(dimension: 20, child: CircularProgressIndicator(strokeWidth: 2)))\n            : Text(label),\n      );\n}")]),
'Langkah 5: state, validasi, dan memuat': dict(
  ist=[('Form state', 'Status form: idle, submitting, success, error.'),
       ('Double submit', 'Tombol ditekan dua kali; cegah dengan menonaktifkan saat memuat.'),
       ('Server error mapping', 'Mengubah kode error API menjadi pesan yang dipahami pengguna.'),
       ('Rate limiting UX', 'Pesan ramah saat terlalu banyak percobaan masuk.')],
  cx=[X('Memetakan error server ke pesan', "String pesanError(Object e) => switch (e) {\n  DioException(response: Response(statusCode: 401)) => 'Email atau kata sandi salah',\n  DioException(response: Response(statusCode: 429)) => 'Terlalu banyak percobaan. Coba lagi dalam 1 menit',\n  DioException(type: DioExceptionType.connectionError) => 'Tidak ada koneksi internet',\n  _ => 'Terjadi kesalahan. Coba lagi',\n};")]),
'Langkah 6: QA dengan desain dan serah terima': dict(
  ist=[('Visual QA', 'Membandingkan build dengan desain di perangkat nyata.'),
       ('Accessibility check', 'Kontras, ukuran huruf besar, pembaca layar, target sentuh.'),
       ('Device matrix', 'Daftar perangkat uji: layar kecil, besar, Android lama, iPhone.'),
       ('Release notes', 'Catatan perubahan untuk tim dan pengguna.')],
  cx=[X('Checklist QA layar Masuk', "[ ] Jarak dan ukuran sesuai spec (toleransi 2 dp)\n[ ] Mode gelap terbaca, kontras teks >= 4.5:1\n[ ] Huruf 200%: tidak terpotong, bisa digulir\n[ ] TalkBack/VoiceOver membaca label field dan tombol\n[ ] Keyboard: next pindah field, done menekan Masuk\n[ ] Autofill password manager bekerja\n[ ] State: memuat, salah sandi, tanpa internet, 429\n[ ] Golden test diperbarui dan lolos di CI", lang='text')]),
}
