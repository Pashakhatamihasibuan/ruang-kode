"""Proyek Mobile berpenyelesaian: 6 mini (Flutter, Kotlin/Compose, KMP) + 4 besar berskala industri 2026-2027."""
from rb_pj_lib import MINI, BESAR, JALUR_M, q

# ---------------------------------------------------------------- MINI
DOMPET = r'''// lib/model/transaksi.dart
enum Jenis { masuk, keluar }

class Transaksi {
  final String id;
  final String judul;
  final int nominal;            // rupiah, selalu bilangan bulat
  final Jenis jenis;
  final String kategori;
  final DateTime tanggal;
  const Transaksi({required this.id, required this.judul, required this.nominal,
      required this.jenis, required this.kategori, required this.tanggal});

  Map<String, Object> toMap() => {'id': id, 'judul': judul, 'nominal': nominal,
      'jenis': jenis.name, 'kategori': kategori, 'tanggal': tanggal.millisecondsSinceEpoch};
  factory Transaksi.fromMap(Map<String, Object?> m) => Transaksi(
      id: m['id'] as String, judul: m['judul'] as String, nominal: m['nominal'] as int,
      jenis: Jenis.values.byName(m['jenis'] as String), kategori: m['kategori'] as String,
      tanggal: DateTime.fromMillisecondsSinceEpoch(m['tanggal'] as int));
}

// lib/data/transaksi_repo.dart  (sqflite, tersimpan offline)
class TransaksiRepo {
  TransaksiRepo(this._db);
  final Database _db;

  Future<List<Transaksi>> bulan(DateTime b) async {
    final awal = DateTime(b.year, b.month), akhir = DateTime(b.year, b.month + 1);
    final rows = await _db.query('transaksi',
        where: 'tanggal >= ? AND tanggal < ?',
        whereArgs: [awal.millisecondsSinceEpoch, akhir.millisecondsSinceEpoch],
        orderBy: 'tanggal DESC');
    return rows.map(Transaksi.fromMap).toList();
  }

  Future<void> simpan(Transaksi t) =>
      _db.insert('transaksi', t.toMap(), conflictAlgorithm: ConflictAlgorithm.replace);
  Future<void> hapus(String id) => _db.delete('transaksi', where: 'id = ?', whereArgs: [id]);
}

// lib/state/dompet_notifier.dart  (Riverpod 2/3)
class Ringkasan {
  final int masuk, keluar;
  final Map<String, int> perKategori;
  const Ringkasan(this.masuk, this.keluar, this.perKategori);
  int get saldo => masuk - keluar;
}

Ringkasan hitungRingkasan(List<Transaksi> list) {
  var masuk = 0, keluar = 0;
  final kat = <String, int>{};
  for (final t in list) {
    if (t.jenis == Jenis.masuk) {
      masuk += t.nominal;
    } else {
      keluar += t.nominal;
      kat.update(t.kategori, (v) => v + t.nominal, ifAbsent: () => t.nominal);
    }
  }
  return Ringkasan(masuk, keluar, kat);
}

final repoProvider = Provider<TransaksiRepo>((ref) => throw UnimplementedError()); // di-override di main()

class DompetNotifier extends AsyncNotifier<List<Transaksi>> {
  DateTime _bulan = DateTime.now();

  @override
  Future<List<Transaksi>> build() => ref.read(repoProvider).bulan(_bulan);

  Future<void> tambah(Transaksi t) async {
    await ref.read(repoProvider).simpan(t);
    state = await AsyncValue.guard(() => ref.read(repoProvider).bulan(_bulan));
  }

  Future<void> hapus(Transaksi t) async {
    final sebelum = state.value ?? [];
    state = AsyncData(sebelum.where((x) => x.id != t.id).toList());   // optimistic update
    try {
      await ref.read(repoProvider).hapus(t.id);
    } catch (_) {
      state = AsyncData(sebelum);                                      // rollback
    }
  }

  Future<void> gantiBulan(DateTime b) async {
    _bulan = b;
    ref.invalidateSelf();
  }
}

final dompetProvider = AsyncNotifierProvider<DompetNotifier, List<Transaksi>>(DompetNotifier.new);
final ringkasanProvider = Provider((ref) => hitungRingkasan(ref.watch(dompetProvider).value ?? []));

// lib/ui/beranda.dart
class Beranda extends ConsumerWidget {
  const Beranda({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final data = ref.watch(dompetProvider);
    final r = ref.watch(ringkasanProvider);
    return Scaffold(
      appBar: AppBar(title: const Text('Dompetku')),
      body: data.when(
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (e, _) => Center(child: Text('Gagal memuat: $e')),
        data: (list) => list.isEmpty
            ? const Center(child: Text('Belum ada transaksi bulan ini.\nTekan + untuk mencatat.', textAlign: TextAlign.center))
            : ListView(children: [
                KartuSaldo(saldo: r.saldo, masuk: r.masuk, keluar: r.keluar),
                for (final t in list)
                  Dismissible(
                    key: ValueKey(t.id),
                    onDismissed: (_) => ref.read(dompetProvider.notifier).hapus(t),
                    child: ListTile(title: Text(t.judul), subtitle: Text(t.kategori),
                        trailing: Text((t.jenis == Jenis.masuk ? '+' : '-') + rupiah(t.nominal))),
                  ),
              ]),
      ),
      floatingActionButton: FloatingActionButton(
          onPressed: () => context.push('/tambah'), child: const Icon(Icons.add)),
    );
  }
}

// test/ringkasan_test.dart
void main() {
  test('saldo dan pengeluaran per kategori', () {
    final t = DateTime(2026, 11, 1);
    final r = hitungRingkasan([
      Transaksi(id: '1', judul: 'Gaji', nominal: 6500000, jenis: Jenis.masuk, kategori: 'Gaji', tanggal: t),
      Transaksi(id: '2', judul: 'Kos', nominal: 1500000, jenis: Jenis.keluar, kategori: 'Tempat tinggal', tanggal: t),
      Transaksi(id: '3', judul: 'Makan siang', nominal: 25000, jenis: Jenis.keluar, kategori: 'Makan', tanggal: t),
      Transaksi(id: '4', judul: 'Kopi', nominal: 18000, jenis: Jenis.keluar, kategori: 'Makan', tanggal: t),
    ]);
    expect(r.saldo, 4957000);
    expect(r.perKategori['Makan'], 43000);
  });
}'''

KATALOG = r'''// lib/data/produk_api.dart  (Dio)
class ProdukApi {
  ProdukApi(this._dio);
  final Dio _dio;

  Future<Halaman<Produk>> cari({required String kata, required int halaman, CancelToken? batal}) async {
    final res = await _dio.get('/v1/produk',
        queryParameters: {'q': kata, 'page': halaman, 'size': 20}, cancelToken: batal);
    final items = (res.data['items'] as List).map((e) => Produk.fromJson(e)).toList();
    return Halaman(items, adaLagi: res.data['hasNext'] as bool);
  }
}

// lib/state/katalog_state.dart  (sealed class: setiap state ditangani UI)
sealed class KatalogState { const KatalogState(); }
class Memuat extends KatalogState { const Memuat(); }
class Kosong extends KatalogState { const Kosong(this.kata); final String kata; }
class Gagal extends KatalogState { const Gagal(this.pesan); final String pesan; }
class Tampil extends KatalogState {
  const Tampil(this.items, {required this.adaLagi, this.memuatLagi = false});
  final List<Produk> items; final bool adaLagi, memuatLagi;
}

// lib/state/katalog_cubit.dart  (flutter_bloc)
class KatalogCubit extends Cubit<KatalogState> {
  KatalogCubit(this._api) : super(const Memuat());
  final ProdukApi _api;
  Timer? _debounce;
  CancelToken? _batal;
  String _kata = '';
  int _halaman = 1;

  void ketik(String kata) {
    _debounce?.cancel();
    _debounce = Timer(const Duration(milliseconds: 400), () => _muatAwal(kata.trim()));
  }

  Future<void> _muatAwal(String kata) async {
    _batal?.cancel('kata berubah');            // request lama tidak boleh menimpa hasil baru
    _batal = CancelToken();
    _kata = kata; _halaman = 1;
    emit(const Memuat());
    try {
      final h = await _api.cari(kata: kata, halaman: 1, batal: _batal);
      emit(h.items.isEmpty ? Kosong(kata) : Tampil(h.items, adaLagi: h.adaLagi));
    } on DioException catch (e) {
      if (CancelToken.isCancel(e)) return;
      emit(Gagal(e.type == DioExceptionType.connectionError
          ? 'Tidak ada koneksi. Periksa internet lalu coba lagi.'
          : 'Server sedang bermasalah. Coba beberapa saat lagi.'));
    }
  }

  Future<void> muatBerikutnya() async {
    final s = state;
    if (s is! Tampil || !s.adaLagi || s.memuatLagi) return;   // cegah request ganda saat scroll
    emit(Tampil(s.items, adaLagi: true, memuatLagi: true));
    try {
      final h = await _api.cari(kata: _kata, halaman: ++_halaman, batal: _batal);
      emit(Tampil([...s.items, ...h.items], adaLagi: h.adaLagi));
    } on DioException {
      _halaman--;
      emit(Tampil(s.items, adaLagi: true));
    }
  }

  void cobaLagi() => _muatAwal(_kata);

  @override
  Future<void> close() { _debounce?.cancel(); return super.close(); }
}

// lib/ui/katalog_page.dart
class DaftarProduk extends StatelessWidget {
  const DaftarProduk({super.key});
  @override
  Widget build(BuildContext context) {
    return BlocBuilder<KatalogCubit, KatalogState>(builder: (context, s) => switch (s) {
      Memuat() => const SkeletonGrid(),
      Kosong(:final kata) => Center(child: Text('Tidak ada hasil untuk "$kata". Coba kata lain.')),
      Gagal(:final pesan) => PesanError(pesan: pesan, onCobaLagi: context.read<KatalogCubit>().cobaLagi),
      Tampil(:final items, :final memuatLagi) => NotificationListener<ScrollNotification>(
          onNotification: (n) {
            if (n.metrics.extentAfter < 600) context.read<KatalogCubit>().muatBerikutnya();
            return false;
          },
          child: GridView.builder(
            gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(maxCrossAxisExtent: 220, childAspectRatio: .66),
            itemCount: items.length + (memuatLagi ? 1 : 0),
            itemBuilder: (_, i) => i == items.length
                ? const Center(child: CircularProgressIndicator())
                : KartuProduk(produk: items[i]),
          ),
        ),
    });
  }
}'''

OBAT = r'''// data/Jadwal.kt  (Room)
@Entity(tableName = "jadwal")
data class Jadwal(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val namaObat: String,
    val dosis: String,
    val jam: Int, val menit: Int,
    val aktif: Boolean = true,
)

@Dao
interface JadwalDao {
    @Query("SELECT * FROM jadwal ORDER BY jam, menit") fun semua(): Flow<List<Jadwal>>
    @Upsert suspend fun simpan(j: Jadwal): Long
    @Delete suspend fun hapus(j: Jadwal)
}

// kerja/PengingatScheduler.kt  (WorkManager: tetap jalan setelah aplikasi ditutup/HP restart)
class PengingatScheduler(private val wm: WorkManager, private val clock: Clock = Clock.systemDefaultZone()) {
    fun jadwalkan(j: Jadwal) {
        val sekarang = LocalDateTime.now(clock)
        var target = sekarang.withHour(j.jam).withMinute(j.menit).withSecond(0).withNano(0)
        if (!target.isAfter(sekarang)) target = target.plusDays(1)
        val tunda = Duration.between(sekarang, target)

        val kerja = PeriodicWorkRequestBuilder<PengingatWorker>(1, TimeUnit.DAYS)
            .setInitialDelay(tunda)
            .setInputData(workDataOf("id" to j.id, "obat" to j.namaObat, "dosis" to j.dosis))
            .build()
        wm.enqueueUniquePeriodicWork("obat-${j.id}", ExistingPeriodicWorkPolicy.UPDATE, kerja)
    }
    fun batalkan(id: Long) = wm.cancelUniqueWork("obat-$id")
}

class PengingatWorker(ctx: Context, params: WorkerParameters) : CoroutineWorker(ctx, params) {
    override suspend fun doWork(): Result {
        val obat = inputData.getString("obat") ?: return Result.failure()
        val dosis = inputData.getString("dosis").orEmpty()
        if (ContextCompat.checkSelfPermission(applicationContext, Manifest.permission.POST_NOTIFICATIONS)
            != PackageManager.PERMISSION_GRANTED) return Result.success()      // Android 13+: izin bisa ditolak
        val notif = NotificationCompat.Builder(applicationContext, KANAL_OBAT)
            .setSmallIcon(R.drawable.ic_pil)
            .setContentTitle("Waktunya minum $obat")
            .setContentText(dosis)
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            .setAutoCancel(true)
            .build()
        NotificationManagerCompat.from(applicationContext).notify(inputData.getLong("id", 0).toInt(), notif)
        return Result.success()
    }
}

// ui/JadwalViewModel.kt
class JadwalViewModel(private val dao: JadwalDao, private val scheduler: PengingatScheduler) : ViewModel() {
    val jadwal: StateFlow<List<Jadwal>> = dao.semua()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), emptyList())

    fun simpan(nama: String, dosis: String, jam: Int, menit: Int) = viewModelScope.launch {
        require(nama.isNotBlank()) { "Nama obat wajib diisi" }
        val id = dao.simpan(Jadwal(namaObat = nama.trim(), dosis = dosis.trim(), jam = jam, menit = menit))
        scheduler.jadwalkan(Jadwal(id, nama, dosis, jam, menit))
    }
    fun hapus(j: Jadwal) = viewModelScope.launch { dao.hapus(j); scheduler.batalkan(j.id) }
}

// ui/JadwalScreen.kt
@Composable
fun JadwalScreen(vm: JadwalViewModel = koinViewModel()) {
    val daftar by vm.jadwal.collectAsStateWithLifecycle()
    val izin = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { }
    LaunchedEffect(Unit) {
        if (Build.VERSION.SDK_INT >= 33) izin.launch(Manifest.permission.POST_NOTIFICATIONS)
    }
    LazyColumn(contentPadding = PaddingValues(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
        items(daftar, key = { it.id }) { j ->
            ElevatedCard(Modifier.fillMaxWidth()) {
                ListItem(
                    headlineContent = { Text(j.namaObat) },
                    supportingContent = { Text("${"%02d:%02d".format(j.jam, j.menit)} · ${j.dosis}") },
                    trailingContent = { IconButton(onClick = { vm.hapus(j) }) { Icon(Icons.Default.Delete, "Hapus ${j.namaObat}") } },
                )
            }
        }
    }
}

// test: PengingatSchedulerTest.kt — Clock.fixed jam 21:00, jadwal 07:00 -> tunda 10 jam (besok pagi)'''

FORM = r'''// FormDaftarState.kt  (state tunggal yang tidak bisa diubah langsung oleh UI)
data class FormDaftar(
    val langkah: Int = 0,                         // 0 data diri, 1 alamat, 2 konfirmasi
    val nama: String = "", val hp: String = "", val email: String = "",
    val provinsi: String = "", val kota: String = "", val alamat: String = "",
    val setujuData: Boolean = false,              // UU PDP: terpisah dari setuju S&K
    val setujuSk: Boolean = false,
    val galat: Map<String, String> = emptyMap(),
    val mengirim: Boolean = false,
)

object Validasi {
    private val polaHp = Regex("^(\\+62|0)8\\d{8,11}$")
    private val polaEmail = Regex("^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$")

    fun langkah(f: FormDaftar): Map<String, String> = buildMap {
        when (f.langkah) {
            0 -> {
                if (f.nama.trim().length < 3) put("nama", "Nama minimal 3 huruf")
                if (!polaHp.matches(f.hp.replace(" ", "").replace("-", ""))) put("hp", "Nomor HP diawali 08 atau +628, 10-13 digit")
                if (!polaEmail.matches(f.email.trim())) put("email", "Format email belum benar, contoh: nama@domain.com")
            }
            1 -> {
                if (f.provinsi.isBlank()) put("provinsi", "Pilih provinsi")
                if (f.kota.isBlank()) put("kota", "Pilih kabupaten/kota")
                if (f.alamat.trim().length < 10) put("alamat", "Tulis alamat lengkap (jalan, nomor, RT/RW)")
            }
            2 -> if (!f.setujuSk) put("setujuSk", "Setujui syarat dan ketentuan untuk melanjutkan")
        }
    }
}

// FormDaftarViewModel.kt  (draf otomatis tersimpan di DataStore agar tidak hilang saat app ditutup)
class FormDaftarViewModel(private val draf: DataStore<Preferences>, private val api: AkunApi) : ViewModel() {
    private val _state = MutableStateFlow(FormDaftar())
    val state = _state.asStateFlow()

    init {
        viewModelScope.launch {
            val p = draf.data.first()
            _state.update { it.copy(nama = p[K_NAMA].orEmpty(), hp = p[K_HP].orEmpty(), email = p[K_EMAIL].orEmpty()) }
        }
        viewModelScope.launch {
            _state.map { Triple(it.nama, it.hp, it.email) }.distinctUntilChanged().debounce(500)
                .collect { (n, h, e) -> draf.edit { it[K_NAMA] = n; it[K_HP] = h; it[K_EMAIL] = e } }
        }
    }

    fun ubah(transform: FormDaftar.() -> FormDaftar) = _state.update { it.transform().copy(galat = emptyMap()) }

    fun lanjut() {
        val g = Validasi.langkah(_state.value)
        if (g.isNotEmpty()) { _state.update { it.copy(galat = g) }; return }
        if (_state.value.langkah < 2) _state.update { it.copy(langkah = it.langkah + 1) } else kirim()
    }

    fun kembali() = _state.update { it.copy(langkah = (it.langkah - 1).coerceAtLeast(0), galat = emptyMap()) }

    private fun kirim() = viewModelScope.launch {
        _state.update { it.copy(mengirim = true) }
        runCatching { api.daftar(_state.value) }
            .onSuccess { draf.edit { it.clear() } }
            .onFailure { e -> _state.update { it.copy(galat = mapOf("umum" to "Gagal mengirim: ${e.message}")) } }
        _state.update { it.copy(mengirim = false) }
    }

    companion object {
        val K_NAMA = stringPreferencesKey("nama"); val K_HP = stringPreferencesKey("hp"); val K_EMAIL = stringPreferencesKey("email")
    }
}

// LangkahDataDiri.kt  (state hoisting: composable hanya menerima nilai dan callback)
@Composable
fun LangkahDataDiri(f: FormDaftar, onUbah: (FormDaftar.() -> FormDaftar) -> Unit) {
    Column(verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Isian("Nama lengkap", f.nama, f.galat["nama"]) { v -> onUbah { copy(nama = v) } }
        Isian("Nomor HP", f.hp, f.galat["hp"], KeyboardType.Phone) { v -> onUbah { copy(hp = v) } }
        Isian("Email", f.email, f.galat["email"], KeyboardType.Email) { v -> onUbah { copy(email = v) } }
    }
}

@Composable
fun Isian(label: String, nilai: String, galat: String?, tipe: KeyboardType = KeyboardType.Text, onUbah: (String) -> Unit) {
    OutlinedTextField(
        value = nilai, onValueChange = onUbah, label = { Text(label) },
        isError = galat != null,
        supportingText = { galat?.let { Text(it) } },        // pesan error menempel di field-nya
        keyboardOptions = KeyboardOptions(keyboardType = tipe, imeAction = ImeAction.Next),
        singleLine = true, modifier = Modifier.fillMaxWidth(),
    )
}

// ValidasiTest.kt
class ValidasiTest {
    @Test fun nomorHpIndonesia() {
        val f = FormDaftar(nama = "Rina", email = "rina@mail.id")
        assertTrue(Validasi.langkah(f.copy(hp = "0812-3456-7890")).isEmpty())
        assertTrue(Validasi.langkah(f.copy(hp = "+6281234567890")).isEmpty())
        assertEquals("Nomor HP diawali 08 atau +628, 10-13 digit", Validasi.langkah(f.copy(hp = "021555777"))["hp"])
    }
}'''

RESEP = r'''// lib/router.dart  (go_router + deep link: https://resepku.id/resep/rendang)
final router = GoRouter(
  initialLocation: '/',
  routes: [
    StatefulShellRoute.indexedStack(
      builder: (context, state, shell) => KerangkaNavigasi(shell: shell),   // NavigationBar bawah
      branches: [
        StatefulShellBranch(routes: [
          GoRoute(path: '/', builder: (_, __) => const BerandaResep(), routes: [
            GoRoute(path: 'resep/:slug', builder: (_, s) => DetailResep(slug: s.pathParameters['slug']!)),
          ]),
        ]),
        StatefulShellBranch(routes: [
          GoRoute(path: '/favorit', builder: (_, __) => const HalamanFavorit()),
        ]),
      ],
    ),
  ],
  errorBuilder: (_, s) => HalamanTidakDitemukan(path: s.uri.toString()),
);

// lib/data/favorit_store.dart  (shared_preferences; cukup untuk daftar id)
class FavoritStore extends ChangeNotifier {
  FavoritStore(this._prefs) : _ids = (_prefs.getStringList(_kunci) ?? []).toSet();
  static const _kunci = 'favorit_v1';
  final SharedPreferences _prefs;
  final Set<String> _ids;

  bool ada(String slug) => _ids.contains(slug);
  Set<String> get semua => Set.unmodifiable(_ids);

  Future<void> toggle(String slug) async {
    _ids.contains(slug) ? _ids.remove(slug) : _ids.add(slug);
    notifyListeners();                                   // UI langsung berubah
    await _prefs.setStringList(_kunci, _ids.toList());
  }
}

// lib/ui/detail_resep.dart
class DetailResep extends StatelessWidget {
  const DetailResep({super.key, required this.slug});
  final String slug;

  @override
  Widget build(BuildContext context) {
    final fav = context.watch<FavoritStore>();
    return FutureBuilder<Resep>(
      future: context.read<ResepRepo>().ambil(slug),
      builder: (context, snap) {
        if (snap.hasError) return const PesanError(pesan: 'Resep tidak bisa dimuat.');
        if (!snap.hasData) return const Center(child: CircularProgressIndicator());
        final r = snap.data!;
        return Scaffold(
          body: CustomScrollView(slivers: [
            SliverAppBar.large(
              title: Text(r.judul),
              actions: [
                IconButton(
                  tooltip: fav.ada(slug) ? 'Hapus dari favorit' : 'Simpan ke favorit',
                  icon: Icon(fav.ada(slug) ? Icons.favorite : Icons.favorite_border),
                  onPressed: () => fav.toggle(slug),
                ),
                IconButton(tooltip: 'Bagikan', icon: const Icon(Icons.share),
                    onPressed: () => SharePlus.instance.share(ShareParams(uri: Uri.parse('https://resepku.id/resep/$slug')))),
              ],
            ),
            SliverToBoxAdapter(child: Hero(tag: 'foto-$slug', child: CachedNetworkImage(imageUrl: r.foto, height: 220, fit: BoxFit.cover))),
            SliverPadding(padding: const EdgeInsets.all(16), sliver: SliverList.list(children: [
              Text('${r.porsi} porsi · ${r.menit} menit', style: Theme.of(context).textTheme.labelLarge),
              const SizedBox(height: 12),
              Text('Bahan', style: Theme.of(context).textTheme.titleMedium),
              for (final b in r.bahan) CheckboxListTile(value: false, onChanged: (_) {}, title: Text(b)),
              Text('Langkah', style: Theme.of(context).textTheme.titleMedium),
              for (final (i, l) in r.langkah.indexed) ListTile(leading: CircleAvatar(child: Text('${i + 1}')), title: Text(l)),
            ])),
          ]),
        );
      },
    );
  }
}

// android/app/src/main/AndroidManifest.xml (App Links)
// <intent-filter android:autoVerify="true">
//   <action android:name="android.intent.action.VIEW"/>
//   <category android:name="android.intent.category.DEFAULT"/><category android:name="android.intent.category.BROWSABLE"/>
//   <data android:scheme="https" android:host="resepku.id" android:pathPrefix="/resep"/>
// </intent-filter>
// iOS: Associated Domains "applinks:resepku.id" + apple-app-site-association di server'''

KURS = r'''// shared/src/commonMain/kotlin/Konverter.kt
class Konverter(private val perIdr: Map<String, Double>) {          // 1 IDR = x mata uang asing
    fun dariRupiah(rupiah: Long, kode: String): Double =
        rupiah * (perIdr[kode] ?: error("Kurs $kode tidak tersedia"))
    fun keRupiah(nilai: Double, kode: String): Double =
        nilai / (perIdr[kode] ?: error("Kurs $kode tidak tersedia"))
}

fun formatRupiah(n: Long): String {
    val s = kotlin.math.abs(n).toString().reversed().chunked(3).joinToString(".").reversed()
    return (if (n < 0) "-Rp" else "Rp") + s
}

// shared/src/commonMain/kotlin/KursRepository.kt  (cache-first: tampil dulu dari DB, lalu segarkan)
class KursRepository(
    private val api: KursApi,
    private val db: KursDatabase,
    private val jam: () -> Long = { Clock.System.now().toEpochMilliseconds() },
) {
    private val umurMaks = 60 * 60 * 1000L                         // API gratis: hemat kuota, maks 1x per jam

    fun pantau(): Flow<List<Kurs>> = db.kursQueries.semua().asFlow().mapToList(Dispatchers.Default)
        .map { rows -> rows.map { Kurs(it.kode, it.nilai, it.diperbarui) } }

    suspend fun segarkan(paksa: Boolean = false): Result<Unit> = runCatching {
        val terakhir = db.kursQueries.terakhirDiperbarui().executeAsOneOrNull()?.max ?: 0L
        if (!paksa && jam() - terakhir < umurMaks) return@runCatching
        val res = api.kurs("IDR")
        db.transaction { res.rates.forEach { (k, v) -> db.kursQueries.simpan(k, v, jam()) } }
    }
}

// shared/src/commonMain/kotlin/KursViewModel.kt  (dipakai Android & iOS)
data class KursUi(val daftar: List<Kurs> = emptyList(), val memuat: Boolean = false, val pesan: String? = null, val offline: Boolean = false)

class KursViewModel(private val repo: KursRepository) : ViewModel() {
    private val status = MutableStateFlow(KursUi())
    val state: StateFlow<KursUi> = combine(repo.pantau(), status) { d, s -> s.copy(daftar = d) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), KursUi())

    init { segarkan() }

    fun segarkan(paksa: Boolean = false) = viewModelScope.launch {
        status.update { it.copy(memuat = true, pesan = null) }
        repo.segarkan(paksa)
            .onSuccess { status.update { it.copy(memuat = false, offline = false) } }
            .onFailure { status.update { it.copy(memuat = false, offline = true, pesan = "Offline: menampilkan kurs tersimpan") } }
    }
}

// shared/src/commonTest/kotlin/KonverterTest.kt  (jalan di JVM, Android, dan iOS simulator)
class KonverterTest {
    private val k = Konverter(mapOf("USD" to 0.0000625, "SGD" to 0.0000842))
    @Test fun dariRupiah() = assertEquals(62.5, k.dariRupiah(1_000_000, "USD"), 0.0001)
    @Test fun keRupiah() = assertEquals(1_000_000.0, k.keRupiah(62.5, "USD"), 0.5)
    @Test fun formatNegatif() = assertEquals("-Rp1.250.000", formatRupiah(-1_250_000))
    @Test fun kodeTakDikenal() { assertFailsWith<IllegalStateException> { k.dariRupiah(1, "XYZ") } }
    @Test fun cacheMasihSegar() = runTest {
        val api = ApiPalsu(); val repo = KursRepository(api, dbMemori(), jam = { 10_000L })
        repo.segarkan(); repo.segarkan()
        assertEquals(1, api.jumlahPanggilan)                       // panggilan kedua memakai cache
    }
}'''

ABSEN = r'''// lib/presensi/presensi_service.dart  (Flutter: QR + lokasi + anti fake GPS)
class HasilPresensi {
  const HasilPresensi.ok(this.pesan) : berhasil = true;
  const HasilPresensi.gagal(this.pesan) : berhasil = false;
  final bool berhasil; final String pesan;
}

class PresensiService {
  PresensiService(this._api, this._jam);
  final PresensiApi _api;
  final DateTime Function() _jam;
  static const radiusMeter = 100.0;

  /// Isi QR dibuat server: "kantorId|kadaluarsaEpochDetik|tandaTanganHmac" dan berganti tiap 30 detik.
  Future<HasilPresensi> presensi(String isiQr, Position pos) async {
    final bagian = isiQr.split('|');
    if (bagian.length != 3) return const HasilPresensi.gagal('QR tidak dikenali.');
    final kadaluarsa = DateTime.fromMillisecondsSinceEpoch(int.parse(bagian[1]) * 1000);
    if (_jam().isAfter(kadaluarsa)) return const HasilPresensi.gagal('QR sudah kedaluwarsa, pindai QR terbaru di layar.');
    if (pos.isMocked) return const HasilPresensi.gagal('Lokasi palsu terdeteksi. Matikan aplikasi fake GPS.');

    final kantor = await _api.kantor(bagian[0]);
    final jarak = Geolocator.distanceBetween(pos.latitude, pos.longitude, kantor.lat, kantor.lng);
    if (jarak > radiusMeter) {
      return HasilPresensi.gagal('Anda berada ${jarak.round()} m dari kantor (maks ${radiusMeter.round()} m).');
    }
    // Server memverifikasi ulang HMAC, waktu, dan jarak: aplikasi klien tidak dipercaya penuh.
    final r = await _api.kirim(isiQr: isiQr, lat: pos.latitude, lng: pos.longitude, akurasi: pos.accuracy);
    return r.terlambat
        ? HasilPresensi.ok('Tercatat ${r.jam} (terlambat ${r.menitTerlambat} menit)')
        : HasilPresensi.ok('Tercatat ${r.jam}. Selamat bekerja!');
  }
}

// lib/presensi/pindai_page.dart  (mobile_scanner)
class PindaiPage extends StatefulWidget { const PindaiPage({super.key}); @override State<PindaiPage> createState() => _PindaiPageState(); }

class _PindaiPageState extends State<PindaiPage> {
  final _kamera = MobileScannerController(detectionSpeed: DetectionSpeed.noDuplicates);
  bool _proses = false;

  Future<void> _terdeteksi(BarcodeCapture c) async {
    final isi = c.barcodes.firstOrNull?.rawValue;
    if (isi == null || _proses) return;
    setState(() => _proses = true);
    try {
      final izin = await Geolocator.requestPermission();
      if (izin == LocationPermission.denied || izin == LocationPermission.deniedForever) {
        _tampil(const HasilPresensi.gagal('Izin lokasi diperlukan untuk presensi.'));
        return;
      }
      final pos = await Geolocator.getCurrentPosition(
          locationSettings: const LocationSettings(accuracy: LocationAccuracy.high, timeLimit: Duration(seconds: 10)));
      _tampil(await context.read<PresensiService>().presensi(isi, pos));
    } finally {
      if (mounted) setState(() => _proses = false);
    }
  }

  void _tampil(HasilPresensi h) => ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content: Text(h.pesan), backgroundColor: h.berhasil ? Colors.green.shade700 : Theme.of(context).colorScheme.error));

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: const Text('Presensi')),
        body: Stack(children: [
          MobileScanner(controller: _kamera, onDetect: _terdeteksi),
          if (_proses) const ColoredBox(color: Colors.black54, child: Center(child: CircularProgressIndicator())),
        ]),
      );

  @override
  void dispose() { _kamera.dispose(); super.dispose(); }
}

// test/presensi_service_test.dart (potongan)
//   QR kedaluwarsa       -> gagal "QR sudah kedaluwarsa..."
//   isMocked = true      -> gagal "Lokasi palsu terdeteksi..."
//   jarak 250 m          -> gagal "Anda berada 250 m dari kantor (maks 100 m)."
//   jarak 40 m, 08.05    -> ok "Tercatat 08:05 (terlambat 5 menit)"'''

MB_MINI = [
MINI(1, 'Dompet pribadi offline dengan Flutter dan Riverpod',
  'Mahasiswa di Yogyakarta ingin mencatat pemasukan dan pengeluaran tanpa internet, melihat saldo bulan berjalan, dan tahu kategori yang paling boros. Data tidak boleh hilang saat aplikasi ditutup.',
  ['Model transaksi dengan nominal bilangan bulat (rupiah)', 'Penyimpanan lokal SQLite (sqflite) dengan query per bulan', 'State management Riverpod <code>AsyncNotifier</code>: loading, error, data', 'Hapus dengan geser (optimistic update + rollback bila gagal)', 'Ringkasan saldo dan pengeluaran per kategori, lengkap dengan unit test'],
  ['Tulis <code>Transaksi</code> dengan <code>toMap/fromMap</code>; nominal <code>int</code>, bukan <code>double</code>.', 'Repo memakai <code>where tanggal &gt;= awal AND &lt; akhir</code> agar akurat di pergantian bulan.', '<code>AsyncNotifierProvider</code>; UI memakai <code>data.when(loading, error, data)</code> sehingga tiga state wajib ditangani.', 'Simpan daftar lama, ubah state dulu, kembalikan di blok <code>catch</code>.', '<code>hitungRingkasan</code> fungsi murni sehingga mudah dites tanpa widget.'],
  DOMPET, 'dart',
  kunci='tambahkan anggaran bulanan per kategori dengan peringatan 80%, grafik donat (fl_chart), dan ekspor CSV.',
  cek=q('Kenapa hitungRingkasan dibuat sebagai fungsi murni terpisah dari widget?', ['Bisa diuji dengan unit test biasa tanpa menjalankan UI, dan dipakai ulang di layar lain', 'Agar aplikasi lebih berat', 'Karena Riverpod melarang logika di widget'], 0, 'Pisahkan logika dari tampilan.')),

MINI(2, 'Katalog UMKM dengan pencarian, debounce, dan infinite scroll',
  'Koperasi UMKM punya 8.000 produk. Pencarian lama dan sering menampilkan hasil yang salah karena respons lama datang setelah respons baru. Di sinyal lemah, aplikasi hanya menampilkan layar putih.',
  ['Pencarian dengan debounce 400 ms', 'Request lama dibatalkan saat kata kunci berubah (tidak ada race condition)', 'Pagination 20 item per halaman saat scroll mendekati bawah', 'Empat state jelas: memuat (skeleton), kosong, gagal (dengan tombol coba lagi), tampil', 'Pesan error yang membedakan tidak ada koneksi dan server bermasalah'],
  ['<code>Timer</code> yang dibatalkan setiap ketikan baru.', '<code>CancelToken</code> Dio; abaikan <code>DioException</code> bertipe cancel.', '<code>NotificationListener</code> + <code>extentAfter &lt; 600</code>; flag <code>memuatLagi</code> mencegah request ganda.', '<code>sealed class KatalogState</code> + <code>switch</code> exhaustive: compiler memaksa semua state ditangani.', 'Periksa <code>DioExceptionType.connectionError</code> untuk pesan offline.'],
  KATALOG, 'dart',
  kunci='tambahkan filter kategori dan harga, simpan 5 pencarian terakhir, dan cache halaman pertama untuk dibuka offline.',
  cek=q('Masalah apa yang dicegah dengan membatalkan request lama saat kata kunci berubah?', ['Hasil pencarian lama yang datang terlambat menimpa hasil pencarian terbaru', 'Aplikasi kehabisan baterai', 'Server menolak semua request'], 0, 'Race condition pada respons jaringan.')),

MINI(3, 'Pengingat minum obat dengan Room dan WorkManager',
  'Keluarga dengan orang tua lansia di Surabaya sering lupa jadwal obat. Mereka butuh aplikasi Android sederhana yang tetap mengingatkan walau aplikasi ditutup atau HP baru dinyalakan ulang.',
  ['Simpan jadwal obat di Room dan tampilkan reaktif dengan Flow', 'Notifikasi harian tepat jam via WorkManager (bertahan setelah reboot)', 'Minta izin notifikasi Android 13+ dan tetap aman bila ditolak', 'Compose UI dengan target sentuh besar dan label aksesibel', 'Perhitungan waktu tunda bisa diuji dengan Clock tetap'],
  ['<code>@Entity Jadwal</code>, DAO dengan <code>Flow&lt;List&lt;Jadwal&gt;&gt;</code> dan <code>@Upsert</code>.', '<code>PeriodicWorkRequest</code> 1 hari + <code>setInitialDelay</code> ke jam target; nama unik per jadwal.', '<code>RequestPermission</code> launcher; worker mengecek izin sebelum <code>notify</code>.', '<code>IconButton</code> dengan <code>contentDescription</code> "Hapus {obat}"; kartu dengan teks besar.', 'Suntikkan <code>Clock</code>; tes jam 21:00 untuk jadwal 07:00 harus menghasilkan tunda 10 jam.'],
  OBAT, 'kotlin',
  kunci='tambahkan tombol "Sudah diminum" di notifikasi, riwayat kepatuhan mingguan, dan mode pendamping yang mengirim laporan ke anggota keluarga.',
  cek=q('Kenapa WorkManager dipilih untuk pengingat ini, bukan coroutine biasa di ViewModel?', ['WorkManager tetap menjalankan tugas walau aplikasi ditutup atau HP restart; coroutine ViewModel ikut mati bersama layar', 'Coroutine tidak bisa menunda', 'WorkManager lebih cepat dari coroutine'], 0, 'Pekerjaan latar yang harus terjamin berjalan.')),

MINI(4, 'Formulir pendaftaran multi-langkah dengan validasi dan draf otomatis',
  'Aplikasi koperasi simpan pinjam kehilangan banyak calon anggota di formulir pendaftaran: pesan error membingungkan, dan isian hilang saat pengguna berpindah aplikasi untuk mencari data.',
  ['Tiga langkah: data diri, alamat, konfirmasi dengan indikator progres', 'Validasi per langkah dengan pesan spesifik yang menempel di field', 'Format lokal: nomor HP 08/+628, alamat sampai RT/RW', 'Draf tersimpan otomatis ke DataStore (debounce 500 ms)', 'Persetujuan data pribadi terpisah dari S&K, tidak tercentang otomatis (UU PDP)'],
  ['<code>data class FormDaftar</code> sebagai satu sumber kebenaran; UI hanya mengirim perubahan.', '<code>Validasi.langkah()</code> mengembalikan peta field → pesan; tampil lewat <code>supportingText</code>.', 'Regex <code>^(\\+62|0)8\\d{8,11}$</code> setelah spasi dan tanda hubung dibuang.', '<code>distinctUntilChanged().debounce(500)</code> lalu <code>DataStore.edit</code>; hapus draf setelah sukses.', 'Dua <code>Checkbox</code> terpisah; hanya S&K yang wajib untuk lanjut, persetujuan pemasaran opsional.'],
  FORM, 'kotlin',
  kunci='tambahkan pilihan provinsi/kota bertingkat dari API wilayah, unggah foto KTP dengan kompresi, dan uji UI dengan Compose testing.',
  cek=q('Di mana sebaiknya pesan error validasi ditampilkan?', ['Menempel di field yang bermasalah, menjelaskan cara memperbaikinya', 'Di dialog pop-up setelah semua isian dikirim', 'Hanya dengan mengubah warna field menjadi merah'], 0, 'Error spesifik dan dekat dengan sumbernya.')),

MINI(5, 'Aplikasi resep dengan navigasi, deep link, dan favorit',
  'Blog resep populer ingin punya aplikasi. Tautan resep yang dibagikan di WhatsApp harus langsung membuka halaman resep di aplikasi, dan pengguna bisa menyimpan favorit tanpa login.',
  ['Navigasi bawah dua tab yang mempertahankan posisi scroll (StatefulShellRoute)', 'Deep link https://resepku.id/resep/{slug} untuk Android App Links dan iOS Universal Links', 'Favorit tersimpan lokal dan langsung memperbarui UI', 'Halaman detail dengan SliverAppBar, Hero image, dan tombol bagikan', 'Halaman 404 untuk tautan yang tidak dikenal'],
  ['<code>StatefulShellRoute.indexedStack</code> dengan dua <code>StatefulShellBranch</code>.', '<code>GoRoute(path: \'resep/:slug\')</code> + intent-filter <code>autoVerify</code> + Associated Domains.', '<code>FavoritStore extends ChangeNotifier</code>; <code>notifyListeners()</code> sebelum menulis ke disk.', '<code>CustomScrollView</code> + <code>SliverAppBar.large</code>; <code>CachedNetworkImage</code> untuk hemat kuota.', '<code>errorBuilder</code> di GoRouter.'],
  RESEP, 'dart',
  kunci='tambahkan mode memasak (layar tidak mati, langkah besar satu per satu), pengatur porsi yang menghitung ulang bahan, dan pencarian berdasarkan bahan di kulkas.',
  cek=q('Apa fungsi android:autoVerify="true" pada intent-filter App Links?', ['Android memverifikasi domain lewat assetlinks.json sehingga tautan langsung membuka aplikasi tanpa dialog pilihan', 'Mempercepat build', 'Memaksa pengguna login'], 0, 'Verifikasi kepemilikan domain.')),

MINI(6, 'Konverter kurs lintas platform dengan Kotlin Multiplatform',
  'Agen perjalanan umrah dan wisata butuh konverter kurs untuk Android dan iOS yang tetap jalan di pesawat (offline), memakai API gratis dengan kuota terbatas, dan logika yang sama persis di kedua platform.',
  ['Logika konversi dan format rupiah di <code>commonMain</code>', 'Cache-first: tampilkan kurs tersimpan (SQLDelight), segarkan maksimal 1x per jam', 'Status offline yang jelas kepada pengguna', 'ViewModel bersama untuk Android (Compose) dan iOS (SwiftUI)', 'Tes di <code>commonTest</code> yang berjalan di semua target'],
  ['<code>Konverter</code> menyimpan peta 1 IDR = x mata uang; error jelas untuk kode tak dikenal.', '<code>pantau()</code> mengalirkan data DB; <code>segarkan()</code> mengecek umur cache sebelum memanggil API.', 'Gagal jaringan → <code>offline = true</code> dan pesan "menampilkan kurs tersimpan".', '<code>combine(repo.pantau(), status)</code> menjadi satu <code>StateFlow&lt;KursUi&gt;</code>.', 'Jam disuntikkan sebagai fungsi agar tes cache tidak bergantung waktu nyata.'],
  KURS, 'kotlin',
  kunci='tambahkan widget layar utama Android (Glance) dan iOS (WidgetKit) yang menampilkan 3 kurs favorit.',
  cek=q('Kenapa repository memeriksa umur cache sebelum memanggil API?', ['Menghemat kuota API gratis dan data pengguna; kurs tidak berubah tiap detik', 'Agar aplikasi selalu offline', 'Karena SQLDelight mewajibkannya'], 0, 'Cache-first dan rate limit API.')),
]

# ---------------------------------------------------------------- BESAR
OJEK = r'''// lib/features/lacak/domain/lacak_pesanan.dart  (Clean Architecture: domain tidak tahu Flutter)
sealed class StatusPesanan { const StatusPesanan(); }
class MencariDriver extends StatusPesanan { const MencariDriver(); }
class DriverMenuju extends StatusPesanan { const DriverMenuju(this.driver, this.posisi, this.etaMenit); final Driver driver; final LatLng posisi; final int etaMenit; }
class DalamPerjalanan extends StatusPesanan { const DalamPerjalanan(this.posisi, this.etaMenit); final LatLng posisi; final int etaMenit; }
class Selesai extends StatusPesanan { const Selesai(this.tarif); final int tarif; }
class Dibatalkan extends StatusPesanan { const Dibatalkan(this.alasan); final String alasan; }

abstract interface class LacakRepository {
  Stream<StatusPesanan> pantau(String pesananId);
}

// lib/features/lacak/data/lacak_repository_ws.dart  (WebSocket + reconnect + fallback polling)
class LacakRepositoryWs implements LacakRepository {
  LacakRepositoryWs(this._ws, this._api);
  final WebSocketFactory _ws; final PesananApi _api;

  @override
  Stream<StatusPesanan> pantau(String id) async* {
    var percobaan = 0;
    while (true) {
      try {
        final kanal = _ws.sambung('wss://rt.ojekita.id/v1/pesanan/$id');
        percobaan = 0;
        await for (final pesan in kanal.stream) {
          final s = StatusMapper.dariJson(jsonDecode(pesan as String));
          yield s;
          if (s is Selesai || s is Dibatalkan) return;
        }
      } catch (_) {
        yield await _api.statusTerakhir(id);                            // fallback: ambil sekali via REST
      }
      final jeda = Duration(seconds: min(30, 1 << percobaan++));        // exponential backoff 1,2,4,...30 s
      await Future.delayed(jeda);
    }
  }
}

// lib/features/lacak/presentation/lacak_controller.dart
@riverpod
Stream<StatusPesanan> statusPesanan(Ref ref, String id) => ref.watch(lacakRepoProvider).pantau(id);

// lib/features/lacak/presentation/lacak_page.dart
class LacakPage extends ConsumerWidget {
  const LacakPage({super.key, required this.id});
  final String id;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final status = ref.watch(statusPesananProvider(id));
    return Scaffold(
      body: Stack(children: [
        PetaRute(status: status.value),                                 // google_maps_flutter / flutter_map
        Align(
          alignment: Alignment.bottomCenter,
          child: KartuStatus(child: switch (status) {
            AsyncData(value: MencariDriver()) => const Text('Mencari driver terdekat...'),
            AsyncData(value: DriverMenuju(:final driver, :final etaMenit)) =>
                InfoDriver(driver: driver, keterangan: 'Tiba dalam $etaMenit menit'),
            AsyncData(value: DalamPerjalanan(:final etaMenit)) => Text('Sampai tujuan sekitar $etaMenit menit lagi'),
            AsyncData(value: Selesai(:final tarif)) => RatingDriver(tarif: tarif),
            AsyncData(value: Dibatalkan(:final alasan)) => Text('Pesanan dibatalkan: $alasan'),
            AsyncError() => const Text('Koneksi terputus. Menyambung ulang...'),
            _ => const LinearProgressIndicator(),
          }),
        ),
      ]),
    );
  }
}

// .github/workflows/mobile.yml (potongan)
// - flutter analyze && flutter test --coverage
// - patrol test (E2E di emulator) untuk alur pesan -> lacak -> selesai
// - fastlane: build appbundle + upload ke Play internal track; build ipa + TestFlight'''

TOKO = r'''// settings.gradle.kts — modularisasi
include(":app", ":core:model", ":core:network", ":core:database", ":core:designsystem",
        ":feature:katalog", ":feature:keranjang", ":feature:checkout", ":feature:akun")

// core/database/ProdukRemoteMediator.kt  (Paging 3: offline-first, Room sebagai sumber kebenaran)
@OptIn(ExperimentalPagingApi::class)
class ProdukRemoteMediator(
    private val query: String, private val api: TokoApi, private val db: TokoDatabase,
) : RemoteMediator<Int, ProdukEntity>() {
    override suspend fun load(loadType: LoadType, state: PagingState<Int, ProdukEntity>): MediatorResult {
        val halaman = when (loadType) {
            LoadType.REFRESH -> 1
            LoadType.PREPEND -> return MediatorResult.Success(endOfPaginationReached = true)
            LoadType.APPEND -> db.kunciDao().untuk(query)?.berikutnya ?: return MediatorResult.Success(true)
        }
        return try {
            val res = api.produk(query, halaman, state.config.pageSize)
            db.withTransaction {
                if (loadType == LoadType.REFRESH) { db.produkDao().hapusQuery(query); db.kunciDao().hapus(query) }
                db.kunciDao().simpan(KunciHalaman(query, if (res.hasNext) halaman + 1 else null))
                db.produkDao().simpanSemua(res.items.map { it.keEntity(query) })
            }
            MediatorResult.Success(endOfPaginationReached = !res.hasNext)
        } catch (e: IOException) { MediatorResult.Error(e) } catch (e: HttpException) { MediatorResult.Error(e) }
    }
}

// feature/checkout/CheckoutViewModel.kt  (Hilt + UDF)
@HiltViewModel
class CheckoutViewModel @Inject constructor(
    private val keranjang: KeranjangRepository,
    private val bayar: PembayaranRepository,
    private val analitik: Analitik,
) : ViewModel() {
    private val _ui = MutableStateFlow<CheckoutUi>(CheckoutUi.Memuat)
    val ui = _ui.asStateFlow()
    private val idempotencyKey = UUID.randomUUID().toString()     // satu kunci per sesi checkout

    fun bayar(metode: MetodeBayar) = viewModelScope.launch {
        _ui.value = CheckoutUi.Memproses
        analitik.catat("checkout_bayar", mapOf("metode" to metode.kode))
        bayar.buatTransaksi(keranjang.snapshot(), metode, idempotencyKey)
            .onSuccess { _ui.value = CheckoutUi.LanjutBayar(it.snapToken) }       // buka Snap/SDK gateway
            .onFailure { _ui.value = CheckoutUi.Gagal(it.pesanUntukPengguna()) }
    }

    fun hasilGateway(status: StatusGateway) {
        // Status final TIDAK dipercaya dari klien: aplikasi menunggu webhook server lewat endpoint status pesanan.
        viewModelScope.launch { _ui.value = CheckoutUi.MenungguKonfirmasi(bayar.pantauStatus(status.orderId)) }
    }
}

// feature/katalog/KatalogScreen.kt
@Composable
fun KatalogScreen(vm: KatalogViewModel = hiltViewModel(), onProduk: (String) -> Unit) {
    val produk = vm.produk.collectAsLazyPagingItems()
    LazyVerticalGrid(columns = GridCells.Adaptive(160.dp), contentPadding = PaddingValues(16.dp)) {
        items(produk.itemCount, key = produk.itemKey { it.id }) { i ->
            produk[i]?.let { KartuProduk(it, onClick = { onProduk(it.id) }) } ?: KartuProdukPlaceholder()
        }
        if (produk.loadState.append is LoadState.Error)
            item(span = { GridItemSpan(maxLineSpan) }) { TombolCobaLagi(onClick = produk::retry) }
    }
}

// app/build.gradle.kts (potongan kualitas rilis)
// android { buildTypes { release { isMinifyEnabled = true; isShrinkResources = true } } }
// dependencies { baselineProfile(project(":baselineprofile")); implementation(libs.androidx.profileinstaller) }
// Play Integrity API diperiksa di server sebelum promo/voucher besar diberikan'''

KLINIK = r'''// shared/src/commonMain/kotlin/domain/Slot.kt
data class Slot(val id: String, val dokterId: String, val mulai: Instant, val sisa: Int)
sealed interface HasilBooking {
    data class Berhasil(val kodeAntrian: String, val estimasi: Instant) : HasilBooking
    data object SlotPenuh : HasilBooking
    data class Gagal(val pesan: String) : HasilBooking
}

// shared/src/commonMain/kotlin/data/BookingRepository.kt
class BookingRepository(private val api: KlinikApi, private val db: KlinikDb, private val antre: AntreanOffline) {
    fun slot(dokterId: String, tanggal: LocalDate): Flow<List<Slot>> = flow {
        emit(db.slotQueries.untuk(dokterId, tanggal.toString()).executeAsList().map { it.keDomain() })   // cache dulu
        val segar = api.slot(dokterId, tanggal)
        db.transaction { segar.forEach { db.slotQueries.simpan(it.keRow()) } }
        emit(segar)
    }

    suspend fun pesan(slotId: String, pasienId: String): HasilBooking {
        val kunci = "$pasienId:$slotId"                              // idempotency: tekan dua kali tetap satu booking
        return try {
            when (val r = api.pesan(slotId, pasienId, idempotencyKey = kunci)) {
                is ApiBooking.Ok -> HasilBooking.Berhasil(r.kode, r.estimasi).also { db.bookingQueries.simpan(r.keRow()) }
                ApiBooking.Penuh -> HasilBooking.SlotPenuh
            }
        } catch (e: IOException) {
            antre.tambah(kunci, slotId, pasienId)                   // dikirim ulang saat online (WorkManager / BGTaskScheduler)
            HasilBooking.Gagal("Tidak ada koneksi. Permintaan disimpan dan akan dikirim otomatis.")
        }
    }
}

// shared/src/commonMain/kotlin/ui/BookingScreen.kt  (Compose Multiplatform: Android & iOS)
@Composable
fun BookingScreen(vm: BookingViewModel = koinViewModel()) {
    val ui by vm.ui.collectAsStateWithLifecycle()
    Scaffold(topBar = { TopAppBar(title = { Text(stringResource(Res.string.pilih_jadwal)) }) }) { pad ->
        Column(Modifier.padding(pad).padding(16.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            PemilihTanggal(ui.tanggal, onPilih = vm::pilihTanggal)
            when {
                ui.memuat && ui.slot.isEmpty() -> SlotSkeleton()
                ui.slot.isEmpty() -> Text("Jadwal dokter penuh di tanggal ini. Coba tanggal lain.")
                else -> FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    ui.slot.forEach { s ->
                        FilterChip(
                            selected = s.id == ui.dipilih, enabled = s.sisa > 0, onClick = { vm.pilihSlot(s.id) },
                            label = { Text("${s.mulai.jamLokal()} · sisa ${s.sisa}") },
                        )
                    }
                }
            }
            Button(onClick = vm::konfirmasi, enabled = ui.dipilih != null && !ui.mengirim,
                   modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)) { Text("Konfirmasi booking") }
        }
    }
}

// iosApp/iosApp/iOSApp.swift
@main struct iOSApp: App {
    init() { KoinKt.doInitKoin() }
    var body: some Scene { WindowGroup { ComposeView().ignoresSafeArea(.keyboard) } }
}

// Keamanan data kesehatan: token di Keystore/Keychain, SQLCipher untuk DB lokal, sertifikat TLS di-pin,
// log tanpa data pasien, dan persetujuan UU PDP untuk data sensitif (kesehatan) dicatat beserta waktunya.'''

AI = r'''// lib/ai/asisten_router.dart  (AI on-device dulu, cloud bila perlu dan diizinkan)
enum Jalur { perangkat, cloud, aturan }

class AsistenRouter {
  AsistenRouter(this._lokal, this._cloud, this._izin, this._jaringan);
  final ModelLokal _lokal;            // model kecil (misal Gemma) via MediaPipe/LiteRT
  final ModelCloud _cloud;            // Gemini lewat Firebase AI Logic (App Check aktif)
  final IzinPengguna _izin;
  final StatusJaringan _jaringan;

  Future<Jawaban> tanya(String teks, List<Transaksi> konteks) async {
    final aman = Pii.samarkan(teks);                                      // nomor rekening, NIK, HP disamarkan
    final ringkas = Ringkas.transaksi(konteks, maksBaris: 40);          // grounding: angka dari data, bukan tebakan

    if (Intent.adalahHitungan(aman)) {                                    // "total jajan minggu ini" -> dihitung, bukan ditebak
      return Jawaban(Kalkulator.jawab(aman, konteks), jalur: Jalur.aturan);
    }
    if (_lokal.tersedia && aman.length < 600) {
      final r = await _lokal.hasilkan(Prompt.keuangan(aman, ringkas)).timeout(const Duration(seconds: 8), onTimeout: () => '');
      if (r.isNotEmpty) return Jawaban(r, jalur: Jalur.perangkat);
    }
    if (_izin.bolehCloud && await _jaringan.online) {
      final r = await _cloud.hasilkan(Prompt.keuangan(aman, ringkas));
      return Jawaban(r, jalur: Jalur.cloud);
    }
    return const Jawaban('Saya belum bisa menjawab tanpa koneksi. Coba pertanyaan yang lebih singkat.', jalur: Jalur.aturan);
  }
}

// lib/ai/kategorisasi.dart  (klasifikasi transaksi on-device: cepat, gratis, privat)
class Kategorisasi {
  Kategorisasi(this._model);
  final ModelTeksKecil _model;                                          // TFLite/LiteRT, < 5 MB
  static const ambang = 0.7;

  Future<String> tebak(String keterangan) async {
    final aturan = AturanKataKunci.cocok(keterangan);                   // "GOPAY", "PLN", "INDOMARET"
    if (aturan != null) return aturan;
    final (label, skor) = await _model.klasifikasi(keterangan);
    return skor >= ambang ? label : 'Perlu dicek';                     // skor rendah -> minta konfirmasi pengguna
  }
}

// lib/ui/chat_page.dart (potongan)
//  - Setiap jawaban menampilkan lencana jalur: "Diproses di perangkat" / "Diproses di cloud".
//  - Tombol 👍/👎 + alasan -> disimpan anonim untuk evaluasi.
//  - Sakelar "Izinkan pemrosesan cloud" mati secara default; penjelasan data apa yang dikirim.
//  - Saran investasi/pinjaman diblokir dan diarahkan ke penjelasan umum + disclaimer.

// test/eval/asisten_eval_test.dart  (evaluasi otomatis sebelum rilis)
void main() {
  final kasus = muatJsonl('test/eval/kasus_keuangan.jsonl');            // 150 pertanyaan + jawaban acuan
  test('akurasi angka 100% untuk pertanyaan hitungan', () async {
    for (final k in kasus.where((k) => k.jenis == 'hitungan')) {
      final j = await routerUji.tanya(k.pertanyaan, k.transaksi);
      expect(j.jalur, Jalur.aturan);
      expect(j.teks, contains(k.angkaAcuan));
    }
  });
  test('tidak ada PII yang keluar ke cloud', () async {
    for (final k in kasus) {
      await routerUji.tanya(k.pertanyaan, k.transaksi);
      expect(cloudPalsu.promptTerkirim.any(Pii.mengandung), isFalse);
    }
  });
}'''

MB_BESAR = [
BESAR(1, 'Aplikasi ojek dan pesan antar dengan pelacakan real-time (Flutter)',
  'Startup logistik lokal di Makassar ingin menyaingi aplikasi besar dengan fokus kota lapis kedua. Pelanggan harus bisa memesan, melihat driver bergerak di peta secara langsung, dan aplikasi harus tetap bisa dipakai di sinyal naik-turun.',
  ['Clean Architecture per fitur (domain, data, presentation) dengan Riverpod', 'Pelacakan real-time lewat WebSocket dengan reconnect exponential backoff dan fallback REST', 'Peta dan rute (google_maps_flutter atau flutter_map), estimasi waktu tiba', 'Push notification FCM untuk perubahan status pesanan', 'E2E test alur utama dengan Patrol, CI/CD fastlane ke Play internal track dan TestFlight'],
  'Flutter 3.3x, Dart 3, Riverpod (riverpod_generator), go_router, Dio, web_socket_channel, Firebase (FCM, Crashlytics, Remote Config), Patrol, fastlane, GitHub Actions',
  [('Struktur', 'lib/features/{auth,pesan,lacak,riwayat}/{domain,data,presentation}; lib/core untuk network, theme, error'), ('State', 'Riverpod: StreamProvider untuk status real-time, AsyncNotifier untuk aksi (pesan, batal)'),
   ('Real-time', 'WebSocket per pesanan; backoff 1-30 detik; status final menutup stream'), ('Offline', 'Riwayat pesanan di cache lokal (drift/isar); antrean aksi saat offline'),
   ('Observabilitas', 'Crashlytics + analytics event funnel (buka → pesan → driver ditemukan → selesai)'), ('Rilis', 'Flavor dev/staging/prod, Remote Config untuk feature flag, staged rollout 10% → 100%')],
  ['Petakan status pesanan menjadi <code>sealed class</code>; UI wajib menangani semua kasus.', 'Bangun repository WebSocket dengan reconnect dan uji dengan server palsu.', 'Hubungkan peta: marker driver dianimasikan antar-posisi agar tidak melompat.', 'Integrasikan FCM: notifikasi membuka layar lacak lewat deep link.', 'Siapkan flavor, Crashlytics, dan pipeline CI yang menjalankan analyze, test, dan Patrol sebelum rilis.'],
  OJEK, 'dart', standar='arsitektur berlapis yang bisa dites, real-time tahan putus koneksi, crash-free users ≥ 99,5%, cold start &lt; 2 detik di HP entry-level, rilis bertahap dengan feature flag',
  cek=q('Kenapa status pesanan dimodelkan sebagai sealed class?', ['Compiler memastikan setiap status ditangani di UI sehingga tidak ada layar kosong untuk status yang terlupa', 'Agar aplikasi lebih kecil', 'Karena WebSocket hanya bisa mengirim sealed class'], 0, 'Exhaustive switch.')),

BESAR(2, 'Aplikasi e-commerce Android native dengan Compose dan arsitektur modular',
  'Brand fesyen lokal dengan 200 ribu pengguna aktif ingin aplikasi Android yang cepat di HP entry-level, tetap bisa menjelajah katalog saat offline, dan checkout aman dengan payment gateway Indonesia.',
  ['Modularisasi per fitur dan core (build lebih cepat, tim paralel)', 'Katalog offline-first: Paging 3 + RemoteMediator + Room', 'Checkout dengan idempotency key dan status final dari webhook server, bukan dari klien', 'Hilt untuk DI, Compose + Material 3, navigasi type-safe', 'Performa: Baseline Profiles, R8, pengukuran dengan Macrobenchmark'],
  'Kotlin 2.x, Jetpack Compose, Material 3, Hilt, Room, Paging 3, Retrofit/OkHttp + kotlinx.serialization, Navigation Compose, Coil, Midtrans/Xendit SDK, Firebase, Macrobenchmark',
  [('Modul', ':app, :core:{model,network,database,designsystem}, :feature:{katalog,keranjang,checkout,akun}'), ('Data', 'Room sebagai single source of truth; jaringan hanya mengisi DB'),
   ('Pembayaran', 'Server membuat transaksi gateway; aplikasi membuka Snap/SDK; status lunas dari webhook'), ('Keamanan', 'Play Integrity, token di EncryptedSharedPreferences/DataStore + Keystore, R8 obfuscation'),
   ('Kualitas', 'Unit test ViewModel (Turbine), Compose UI test, screenshot test (Roborazzi), Macrobenchmark startup'), ('Rilis', 'App Bundle, Play internal → closed → produksi bertahap; Android vitals dipantau')],
  ['Buat modul core dan design system (warna, tipografi, komponen) lebih dulu.', 'Implementasikan katalog dengan <code>RemoteMediator</code>; uji mode pesawat.', 'Bangun keranjang (Room) dan checkout dengan <code>idempotencyKey</code> per sesi.', 'Integrasi payment gateway; tampilkan "menunggu konfirmasi" sampai server menerima webhook.', 'Buat Baseline Profile dan ukur startup sebelum/sesudah dengan Macrobenchmark.'],
  TOKO, 'kotlin', standar='offline-first, modular, checkout idempoten dan tidak memercayai status dari klien, startup diukur dan dioptimasi, ANR rate &lt; 0,47% dan crash rate &lt; 1,09% (ambang Android vitals)',
  cek=q('Kenapa status pembayaran lunas tidak diambil dari callback SDK di aplikasi?', ['Callback di klien bisa dimanipulasi atau hilang; sumber kebenaran adalah webhook gateway ke server', 'Karena SDK tidak punya callback', 'Agar pembayaran lebih cepat'], 0, 'Jangan percaya klien untuk uang.')),

BESAR(3, 'Reservasi klinik Android dan iOS dengan Compose Multiplatform',
  'Jaringan klinik pratama di Jawa Barat ingin satu aplikasi untuk Android dan iOS: pilih dokter, booking slot, antrean digital, dan pengingat. Tim hanya 3 developer, jadi kode harus dibagi sebanyak mungkin tanpa mengorbankan rasa native.',
  ['Logika, data, dan UI bersama dengan Kotlin Multiplatform + Compose Multiplatform', 'Booking idempoten; slot penuh ditangani dengan jelas', 'Cache slot dan antrean booking offline yang dikirim ulang otomatis', 'Interop native: notifikasi lokal, kalender, dan login biometrik per platform', 'Keamanan data kesehatan: enkripsi lokal, TLS pinning, persetujuan data sensitif'],
  'Kotlin Multiplatform, Compose Multiplatform, Ktor client, kotlinx.serialization, SQLDelight (+SQLCipher), Koin, kotlinx-datetime, Swift/SwiftUI interop, Xcode Cloud / GitHub Actions',
  [('Source set', 'commonMain (domain, data, UI), androidMain/iosMain (notifikasi, biometrik, driver DB)'), ('Data', 'Ktor + SQLDelight; repository cache-first dengan Flow'),
   ('UI', 'Compose Multiplatform dengan resources bersama; komponen kecil disesuaikan per platform (expect/actual)'), ('Sinkronisasi', 'Antrean aksi offline; WorkManager (Android) dan BGTaskScheduler (iOS)'),
   ('Keamanan', 'Keystore/Keychain, SQLCipher, certificate pinning, log tanpa data pasien'), ('Kualitas', 'commonTest untuk domain/data, UI test per platform, crash reporting')],
  ['Mulai dari wizard KMP dengan target Android dan iOS; jalankan di kedua simulator di hari pertama.', 'Tulis domain dan repository di <code>commonMain</code>, lengkap dengan tes.', 'Bangun layar booking dengan Compose Multiplatform; uji gestur kembali iOS.', 'Tambahkan <code>expect/actual</code> untuk notifikasi, biometrik, dan kalender.', 'Lakukan audit keamanan dan alur persetujuan sebelum uji coba di satu klinik.'],
  KLINIK, 'kotlin', standar='≥ 70% kode bersama, perilaku native terjaga di iOS, booking idempoten, offline queue, data kesehatan terenkripsi dan sesuai UU PDP',
  cek=q('Apa fungsi idempotency key "$pasienId:$slotId" saat booking?', ['Jika permintaan terkirim dua kali (tekan ganda atau retry), server hanya membuat satu booking', 'Mengenkripsi data pasien', 'Mempercepat pencarian slot'], 0, 'Retry aman.')),

BESAR(4, 'Asisten keuangan dengan AI on-device dan cloud (Flutter)',
  'Fintech tabungan mikro ingin fitur "tanya keuanganmu": pengguna bertanya dalam bahasa sehari-hari tentang pengeluarannya. Data keuangan sensitif, banyak pengguna berkuota terbatas, dan jawaban angka tidak boleh salah.',
  ['Router AI: aturan/kalkulator untuk hitungan, model on-device untuk teks pendek, cloud hanya dengan izin', 'Kategorisasi transaksi on-device dengan ambang keyakinan dan konfirmasi pengguna', 'PII disamarkan sebelum meninggalkan perangkat; sakelar cloud mati secara default', 'Transparansi: lencana sumber jawaban, umpan balik 👍/👎, disclaimer saran keuangan', 'Evaluasi otomatis (akurasi angka, kebocoran PII) di CI sebelum rilis'],
  'Flutter, Riverpod, MediaPipe LLM Inference / LiteRT (model kecil on-device), Firebase AI Logic (Gemini) + App Check, drift (SQLite terenkripsi), Remote Config, GitHub Actions',
  [('Jalur jawaban', 'aturan (angka pasti) → on-device (privat, gratis) → cloud (izin + online)'), ('Model', 'model teks kecil terkuantisasi diunduh setelah instalasi lewat Wi-Fi; versi dikontrol Remote Config'),
   ('Privasi', 'PII masking, data mentah tidak dikirim, hanya ringkasan; persetujuan terpisah (UU PDP)'), ('Keandalan', 'timeout 8 detik, fallback, jawaban "tidak tahu" lebih baik dari mengarang'),
   ('Evaluasi', '150 kasus uji JSONL: akurasi angka 100%, nol PII ke cloud, skor relevansi dinilai manusia per rilis'), ('Biaya', 'kuota cloud per pengguna per hari, cache jawaban umum, pemantauan token')],
  ['Kumpulkan 150 pertanyaan nyata dan jawaban acuan sebelum menulis kode AI.', 'Bangun kalkulator berbasis aturan untuk semua pertanyaan hitungan.', 'Integrasikan model on-device; ukur ukuran unduhan, RAM, dan latensi di HP 4 GB.', 'Tambahkan jalur cloud dengan App Check, PII masking, dan sakelar izin.', 'Jalankan evaluasi otomatis di CI; rilis bertahap dengan Remote Config.'],
  AI, 'dart', standar='angka selalu dari perhitungan, privasi by design, transparansi sumber jawaban, evaluasi otomatis sebelum rilis, fallback offline, biaya cloud terkendali',
  cek=q('Kenapa pertanyaan "berapa total jajan minggu ini" dijawab kalkulator, bukan model bahasa?', ['Model bahasa bisa salah menghitung; angka keuangan harus pasti dari data', 'Model bahasa tidak bisa membaca bahasa Indonesia', 'Kalkulator lebih mahal'], 0, 'Gunakan alat yang tepat untuk angka.')),
]

PJ_MOBILE = JALUR_M('Mobile Developer', 'Menengah',
  'Enam proyek mini (dompet offline, katalog dengan infinite scroll, pengingat obat, formulir multi-langkah, resep dengan deep link, konverter kurs KMP) dan empat proyek besar berskala industri 2026-2027 (ojek real-time, e-commerce Android modular, reservasi klinik Compose Multiplatform, asisten keuangan AI on-device), lengkap dengan kode penyelesaiannya di Flutter, Kotlin, dan KMP.',
  ['Flutter', 'Jetpack Compose', 'Kotlin Multiplatform', 'Offline-first', 'AI on-device'], MB_MINI, MB_BESAR)
