"""Pendalaman jalur Jetpack Compose & Android: istilah dunia kerja dan contoh kode tambahan."""
K = 'compose'


def X(t, code, b=None, lang='kotlin'):
    return dict(t=t, b=b, code=code, lang=lang, run=False)


D = {
'UI deklaratif dengan Compose': dict(
  ist=[('Declarative UI', 'UI = fungsi(state); kamu menjelaskan tampilan, bukan langkah mengubahnya.'),
       ('@Composable', 'Fungsi yang menghasilkan UI.'),
       ('Recomposition', 'Compose memanggil ulang composable yang state-nya berubah.'),
       ('@Preview', 'Pratinjau composable di Android Studio tanpa menjalankan aplikasi.')],
  cx=[X('Composable dengan beberapa pratinjau', '@Composable\nfun SapaPengguna(nama: String, poin: Int) {\n    Text("Halo, $nama! Kamu punya $poin poin", style = MaterialTheme.typography.titleMedium)\n}\n\n@Preview(name = "Terang", showBackground = true)\n@Preview(name = "Gelap", uiMode = Configuration.UI_MODE_NIGHT_YES)\n@Preview(name = "Huruf besar", fontScale = 1.5f)\n@Composable\nfun SapaPenggunaPreview() = TokoTheme { SapaPengguna("Sari", 1200) }')]),
'Column, Row, Box, dan Modifier': dict(
  ist=[('Modifier', 'Rantai pengubah tampilan dan perilaku: ukuran, jarak, klik, latar.'),
       ('Modifier order', 'Urutan penting: padding lalu background berbeda hasilnya dengan sebaliknya.'),
       ('Arrangement / Alignment', 'Pengaturan jarak di sumbu utama dan perataan di sumbu silang.'),
       ('weight', 'Membagi sisa ruang di Row/Column (setara Expanded).')],
  cx=[X('Baris produk yang tidak meluber', '@Composable\nfun BarisProduk(p: Produk, onTambah: () -> Unit) {\n    Row(\n        modifier = Modifier.fillMaxWidth().clickable { }.padding(horizontal = 16.dp, vertical = 12.dp),\n        verticalAlignment = Alignment.CenterVertically,\n        horizontalArrangement = Arrangement.spacedBy(12.dp),\n    ) {\n        AsyncImage(model = p.foto, contentDescription = null, modifier = Modifier.size(56.dp).clip(RoundedCornerShape(8.dp)))\n        Column(Modifier.weight(1f)) {\n            Text(p.nama, maxLines = 2, overflow = TextOverflow.Ellipsis)\n            Text(p.harga.rupiah(), fontWeight = FontWeight.Bold)\n        }\n        IconButton(onClick = onTambah) { Icon(Icons.Default.AddShoppingCart, contentDescription = "Tambah ${p.nama}") }\n    }\n}')]),
'State dengan remember dan mutableStateOf': dict(
  ist=[('State hoisting', 'Mengangkat state ke pemanggil: composable menerima value dan onValueChange.'),
       ('remember vs rememberSaveable', 'rememberSaveable bertahan saat layar diputar atau proses dimatikan.'),
       ('Stateless composable', 'Composable tanpa state sendiri; mudah dipakai ulang dan diuji.'),
       ('derivedStateOf', 'State turunan yang hanya memicu recomposition saat hasilnya berubah.')],
  cx=[X('State hoisting pada pemilih jumlah', '@Composable\nfun PemilihQty(qty: Int, onQtyChange: (Int) -> Unit, maks: Int = 10) {\n    Row(verticalAlignment = Alignment.CenterVertically) {\n        IconButton(onClick = { onQtyChange(qty - 1) }, enabled = qty > 1) { Icon(Icons.Default.Remove, "Kurangi") }\n        Text("$qty", style = MaterialTheme.typography.titleMedium)\n        IconButton(onClick = { onQtyChange(qty + 1) }, enabled = qty < maks) { Icon(Icons.Default.Add, "Tambah") }\n    }\n}\n\n@Composable\nfun LayarProduk() {\n    var qty by rememberSaveable { mutableIntStateOf(1) } // bertahan saat rotasi\n    PemilihQty(qty = qty, onQtyChange = { qty = it })\n}')]),
'LazyColumn dan TextField': dict(
  ist=[('LazyColumn', 'Daftar yang hanya membuat item yang terlihat.'),
       ('key', 'Identitas item agar animasi dan state tetap benar saat urutan berubah.'),
       ('contentType', 'Membantu Compose memakai ulang item berjenis sama.'),
       ('KeyboardOptions / KeyboardActions', 'Jenis keyboard dan aksi tombol enter.')],
  cx=[X('Pencarian dengan daftar yang tersaring', '@Composable\nfun CariProduk(semua: List<Produk>) {\n    var kata by rememberSaveable { mutableStateOf("") }\n    val hasil by remember(semua) { derivedStateOf { semua.filter { it.nama.contains(kata, ignoreCase = true) } } }\n    Column {\n        OutlinedTextField(\n            value = kata, onValueChange = { kata = it },\n            label = { Text("Cari produk") }, singleLine = true,\n            keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search),\n            modifier = Modifier.fillMaxWidth().padding(16.dp),\n        )\n        LazyColumn {\n            items(hasil, key = { it.id }) { p -> ListItem(headlineContent = { Text(p.nama) }, supportingContent = { Text(p.harga.rupiah()) }) }\n        }\n    }\n}')]),
'Material 3, Scaffold, dan navigasi': dict(
  ist=[('Scaffold', 'Kerangka layar: topBar, bottomBar, FAB, snackbar.'),
       ('Navigation Compose', 'Navigasi antar layar; versi baru mendukung rute bertipe (type-safe).'),
       ('Back stack', 'Tumpukan layar yang bisa dikembalikan.'),
       ('Edge-to-edge', 'Konten sampai ke tepi layar; wajib di Android 15. Atur padding insets.')],
  cx=[X('Rute bertipe dengan kotlinx.serialization', '@Serializable object Beranda\n@Serializable data class DetailProduk(val id: Long)\n\n@Composable\nfun NavUtama() {\n    val nav = rememberNavController()\n    NavHost(nav, startDestination = Beranda) {\n        composable<Beranda> { LayarBeranda(onBuka = { id -> nav.navigate(DetailProduk(id)) }) }\n        composable<DetailProduk> { entry ->\n            val args = entry.toRoute<DetailProduk>()\n            LayarDetail(id = args.id, onKembali = { nav.popBackStack() })\n        }\n    }\n}')]),
'ViewModel, StateFlow, dan data dari API': dict(
  ist=[('ViewModel', 'Penyimpan state layar yang bertahan saat rotasi.'),
       ('UDF (Unidirectional Data Flow)', 'Event naik ke ViewModel, state turun ke UI.'),
       ('viewModelScope', 'Scope coroutine yang otomatis batal saat ViewModel dihancurkan.'),
       ('stateIn / WhileSubscribed', 'Mengubah Flow menjadi StateFlow yang berhenti saat tidak ada yang melihat.')],
  cx=[X('ViewModel dengan UiState', 'data class ProdukUiState(val memuat: Boolean = true, val produk: List<Produk> = emptyList(), val error: String? = null)\n\n@HiltViewModel\nclass ProdukViewModel @Inject constructor(private val repo: ProdukRepository) : ViewModel() {\n    private val _state = MutableStateFlow(ProdukUiState())\n    val state: StateFlow<ProdukUiState> = _state.asStateFlow()\n\n    init { muat() }\n\n    fun muat() = viewModelScope.launch {\n        _state.update { it.copy(memuat = true, error = null) }\n        repo.daftar()\n            .onSuccess { ps -> _state.update { it.copy(memuat = false, produk = ps) } }\n            .onFailure { e -> _state.update { it.copy(memuat = false, error = e.message ?: "Gagal memuat") } }\n    }\n}\n\n// di layar:\n// val state by vm.state.collectAsStateWithLifecycle()')]),
'Tema Material 3 dan mode gelap': dict(
  ist=[('ColorScheme', 'Palet peran warna: primary, onPrimary, surface, error, dan lainnya.'),
       ('Dynamic color', 'Warna dari wallpaper pengguna (Android 12+).'),
       ('Typography & Shapes', 'Skala huruf dan bentuk sudut yang konsisten.'),
       ('Semantic color', 'Gunakan peran (colorScheme.error) bukan nilai hex langsung.')],
  cx=[X('Tema dengan dynamic color dan cadangan warna merek', '@Composable\nfun TokoTheme(gelap: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {\n    val ctx = LocalContext.current\n    val skema = when {\n        Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> if (gelap) dynamicDarkColorScheme(ctx) else dynamicLightColorScheme(ctx)\n        gelap -> darkColorScheme(primary = Color(0xFFE6B89C))\n        else -> lightColorScheme(primary = Color(0xFF6B3E26))\n    }\n    MaterialTheme(colorScheme = skema, typography = TokoTypography, content = content)\n}')]),
'Animasi di Compose': dict(
  ist=[('animate*AsState', 'Animasi nilai sederhana (warna, ukuran, alpha).'),
       ('AnimatedVisibility', 'Animasi muncul/hilang.'),
       ('AnimatedContent', 'Animasi saat konten berganti (misalnya angka keranjang).'),
       ('Shared element transition', 'Elemen yang "terbang" antar layar (foto produk).')],
  cx=[X('Badge keranjang yang beranimasi saat jumlah berubah', '@Composable\nfun BadgeKeranjang(jumlah: Int) {\n    AnimatedContent(\n        targetState = jumlah,\n        transitionSpec = { (slideInVertically { -it } + fadeIn()) togetherWith (slideOutVertically { it } + fadeOut()) },\n        label = "jumlah",\n    ) { n -> Text("$n", style = MaterialTheme.typography.labelLarge) }\n}')]),
'Side effect: LaunchedEffect dan rememberCoroutineScope': dict(
  ist=[('Side effect', 'Pekerjaan di luar menggambar UI: panggil API, tampilkan snackbar, log analytics.'),
       ('LaunchedEffect(key)', 'Coroutine yang berjalan saat masuk komposisi dan diulang saat key berubah.'),
       ('rememberCoroutineScope', 'Scope untuk memulai coroutine dari event klik.'),
       ('DisposableEffect', 'Efek dengan pembersihan (lepas listener) saat keluar komposisi.')],
  cx=[X('Snackbar dari event satu kali', '@Composable\nfun LayarCheckout(vm: CheckoutViewModel, snackbar: SnackbarHostState) {\n    LaunchedEffect(Unit) {\n        vm.event.collect { e ->\n            when (e) {\n                is CheckoutEvent.Sukses -> snackbar.showSnackbar("Pesanan ${e.nomor} dibuat")\n                is CheckoutEvent.Gagal -> snackbar.showSnackbar(e.pesan, actionLabel = "Coba lagi")\n            }\n        }\n    }\n    val scope = rememberCoroutineScope()\n    Button(onClick = { scope.launch { vm.bayar() } }) { Text("Bayar sekarang") }\n}')]),
'Room: database lokal': dict(
  ist=[('Entity / DAO / Database', 'Tiga bagian Room: tabel, query, dan kelas database.'),
       ('Flow dari Room', 'Query yang mengembalikan Flow otomatis memancarkan data baru saat tabel berubah.'),
       ('Migration', 'Perubahan skema antar versi; uji dengan MigrationTestHelper.'),
       ('Single source of truth', 'UI selalu membaca dari database lokal; jaringan hanya memperbarui database.')],
  cx=[X('Entity dan DAO dengan Flow', '@Entity(tableName = "catatan")\ndata class Catatan(\n    @PrimaryKey(autoGenerate = true) val id: Long = 0,\n    val judul: String,\n    val isi: String,\n    val diubah: Long = System.currentTimeMillis(),\n)\n\n@Dao\ninterface CatatanDao {\n    @Query("SELECT * FROM catatan ORDER BY diubah DESC")\n    fun semua(): Flow<List<Catatan>>\n\n    @Upsert\n    suspend fun simpan(c: Catatan)\n\n    @Delete\n    suspend fun hapus(c: Catatan)\n}')]),
'DataStore untuk pengaturan': dict(
  ist=[('Preferences DataStore', 'Pengganti SharedPreferences yang asinkron dan aman.'),
       ('Proto DataStore', 'Versi bertipe dengan skema Protocol Buffers.'),
       ('ANR', 'Application Not Responding; SharedPreferences sinkron bisa memicunya.'),
       ('Onboarding flag', 'Penanda pengguna sudah melewati layar pengenalan.')],
  cx=[X('Menyimpan pilihan tema', 'private val Context.dataStore by preferencesDataStore("pengaturan")\nprivate val TEMA = stringPreferencesKey("tema")\n\nclass PengaturanRepo(private val ctx: Context) {\n    val tema: Flow<String> = ctx.dataStore.data.map { it[TEMA] ?: "sistem" }\n    suspend fun setTema(t: String) = ctx.dataStore.edit { it[TEMA] = t }\n}')]),
'Peta library Android yang sering dipakai': dict(
  ist=[('Jetpack', 'Kumpulan pustaka resmi Google: Compose, Navigation, Room, WorkManager, Paging.'),
       ('Retrofit + OkHttp', 'Klien HTTP standar industri Android.'),
       ('Coil', 'Pemuat gambar berbasis coroutine untuk Compose.'),
       ('BOM (Bill of Materials)', 'Satu versi Compose BOM menyelaraskan semua pustaka Compose.')],
  cx=[X('Dependensi umum di build.gradle.kts', 'dependencies {\n    implementation(platform(libs.androidx.compose.bom))\n    implementation(libs.androidx.compose.material3)\n    implementation(libs.androidx.navigation.compose)\n    implementation(libs.androidx.lifecycle.viewmodel.compose)\n    implementation(libs.hilt.android); ksp(libs.hilt.compiler)\n    implementation(libs.androidx.room.ktx); ksp(libs.androidx.room.compiler)\n    implementation(libs.retrofit); implementation(libs.okhttp.logging)\n    implementation(libs.coil.compose)\n    testImplementation(libs.mockk); testImplementation(libs.turbine)\n}')]),
'Pengujian UI Compose': dict(
  ist=[('ComposeTestRule', 'Aturan tes untuk memasang composable dan berinteraksi dengannya.'),
       ('Semantics tree', 'Pohon makna UI yang dipakai tes dan pembaca layar.'),
       ('testTag', 'Penanda khusus untuk menemukan elemen di tes.'),
       ('Screenshot test', 'Membandingkan tangkapan layar dengan acuan (Paparazzi, Roborazzi).')],
  cx=[X('Tes tombol tambah nonaktif di batas maksimum', 'class PemilihQtyTest {\n    @get:Rule val rule = createComposeRule()\n\n    @Test\n    fun tombolTambahNonaktifDiMaks() {\n        rule.setContent { var q by remember { mutableIntStateOf(2) }; PemilihQty(q, { q = it }, maks = 3) }\n        rule.onNodeWithContentDescription("Tambah").performClick()\n        rule.onNodeWithText("3").assertIsDisplayed()\n        rule.onNodeWithContentDescription("Tambah").assertIsNotEnabled()\n    }\n}')]),
'Proyek: aplikasi catatan': dict(
  ist=[('Offline-first', 'Bisa dipakai tanpa internet, karena semua data disimpan lokal dulu.'),
       ('Auto-save', 'Simpan otomatis saat mengetik (dengan debounce) tanpa tombol simpan.'),
       ('Empty state', 'Tampilan saat belum ada catatan, dengan ajakan membuat yang pertama.'),
       ('Swipe to delete + undo', 'Pola hapus yang aman tanpa dialog.')],
  cx=[X('Auto-save dengan debounce di ViewModel', 'class EditorViewModel(private val dao: CatatanDao, id: Long) : ViewModel() {\n    private val teks = MutableStateFlow("")\n    init {\n        viewModelScope.launch {\n            teks.drop(1).debounce(600).distinctUntilChanged().collect { isi ->\n                dao.simpan(Catatan(id = id, judul = isi.lineSequence().first().take(40), isi = isi))\n            }\n        }\n    }\n    fun ketik(isi: String) { teks.value = isi }\n}')]),
'Activity, lifecycle, dan manifest': dict(
  ist=[('Activity lifecycle', 'onCreate, onStart, onResume, onPause, onStop, onDestroy.'),
       ('Configuration change', 'Rotasi, ganti bahasa, mode gelap; Activity dibuat ulang.'),
       ('Process death', 'Sistem mematikan aplikasi di latar; state harus dipulihkan (SavedStateHandle).'),
       ('AndroidManifest.xml', 'Deklarasi komponen, izin, dan intent filter aplikasi.')],
  cx=[X('Manifest dengan deep link dan izin', '<manifest xmlns:android="http://schemas.android.com/apk/res/android">\n    <uses-permission android:name="android.permission.INTERNET" />\n    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />\n    <application android:label="@string/app_name" android:theme="@style/Theme.Toko">\n        <activity android:name=".MainActivity" android:exported="true">\n            <intent-filter>\n                <action android:name="android.intent.action.MAIN" />\n                <category android:name="android.intent.category.LAUNCHER" />\n            </intent-filter>\n            <intent-filter android:autoVerify="true">\n                <action android:name="android.intent.action.VIEW" />\n                <category android:name="android.intent.category.DEFAULT" />\n                <category android:name="android.intent.category.BROWSABLE" />\n                <data android:scheme="https" android:host="tokokopi.id" android:pathPrefix="/produk" />\n            </intent-filter>\n        </activity>\n    </application>\n</manifest>', lang='xml')]),
'Intent, izin runtime, dan komponen aplikasi': dict(
  ist=[('Intent', 'Pesan untuk membuka Activity lain atau aplikasi lain (berbagi, telepon, peta).'),
       ('Activity Result API', 'Cara modern meminta izin dan menerima hasil (rememberLauncherForActivityResult).'),
       ('Service / BroadcastReceiver / ContentProvider', 'Tiga komponen aplikasi selain Activity.'),
       ('Photo Picker', 'Pemilih foto sistem yang tidak butuh izin penyimpanan.')],
  cx=[X('Meminta izin notifikasi (Android 13+)', '@Composable\nfun TombolAktifkanNotifikasi() {\n    val launcher = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { diizinkan ->\n        if (!diizinkan) { /* tampilkan penjelasan dan tautan ke Pengaturan */ }\n    }\n    Button(onClick = {\n        if (Build.VERSION.SDK_INT >= 33) launcher.launch(Manifest.permission.POST_NOTIFICATIONS)\n    }) { Text("Aktifkan notifikasi status pesanan") }\n}')]),
'WorkManager untuk tugas latar': dict(
  ist=[('WorkManager', 'Penjadwal tugas latar yang tetap berjalan meski aplikasi ditutup atau HP restart.'),
       ('Constraints', 'Syarat tugas: ada internet, sedang mengisi daya, baterai tidak lemah.'),
       ('Periodic work', 'Tugas berulang, minimal setiap 15 menit.'),
       ('Doze mode', 'Mode hemat baterai Android yang menunda tugas latar.')],
  cx=[X('Sinkron catatan saat ada internet', 'class SinkronWorker(ctx: Context, params: WorkerParameters, private val repo: CatatanRepo) : CoroutineWorker(ctx, params) {\n    override suspend fun doWork(): Result = try {\n        repo.sinkron()\n        Result.success()\n    } catch (e: IOException) {\n        if (runAttemptCount < 5) Result.retry() else Result.failure()\n    }\n}\n\nval kerja = PeriodicWorkRequestBuilder<SinkronWorker>(6, TimeUnit.HOURS)\n    .setConstraints(Constraints(requiredNetworkType = NetworkType.CONNECTED, requiresBatteryNotLow = true))\n    .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)\n    .build()\nWorkManager.getInstance(ctx).enqueueUniquePeriodicWork("sinkron", ExistingPeriodicWorkPolicy.KEEP, kerja)')]),
'Dependency injection dengan Hilt': dict(
  ist=[('Hilt', 'Kerangka DI resmi Android di atas Dagger.'),
       ('@Module / @Provides / @Binds', 'Cara memberi tahu Hilt cara membuat dependensi.'),
       ('Scope (@Singleton)', 'Umur objek: satu untuk seluruh aplikasi, per Activity, atau per ViewModel.'),
       ('Test double', 'Mengganti implementasi asli dengan palsu saat pengujian (@TestInstallIn).')],
  cx=[X('Modul jaringan Hilt', '@Module\n@InstallIn(SingletonComponent::class)\nobject JaringanModule {\n    @Provides @Singleton\n    fun okHttp(auth: AuthInterceptor): OkHttpClient = OkHttpClient.Builder()\n        .addInterceptor(auth)\n        .connectTimeout(10, TimeUnit.SECONDS)\n        .build()\n\n    @Provides @Singleton\n    fun api(client: OkHttpClient): TokoApi = Retrofit.Builder()\n        .baseUrl("https://api.tokokopi.id/v1/")\n        .client(client)\n        .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))\n        .build().create(TokoApi::class.java)\n}\n\n@Module @InstallIn(SingletonComponent::class)\nabstract class RepoModule { @Binds abstract fun produkRepo(impl: ProdukRepositoryImpl): ProdukRepository }')]),
'Retrofit, repository, dan offline-first': dict(
  ist=[('Retrofit interface', 'Deklarasi endpoint API sebagai fungsi suspend beranotasi.'),
       ('Network-bound resource', 'Tampilkan cache dulu, ambil dari jaringan, simpan, lalu tampilkan data baru.'),
       ('Stale-while-revalidate', 'Data lama ditampilkan sambil memuat data terbaru.'),
       ('HTTP caching', 'Cache-Control dan ETag agar tidak mengunduh ulang data yang sama.')],
  cx=[X('Repository offline-first: Room sebagai sumber kebenaran', 'interface TokoApi {\n    @GET("produk") suspend fun produk(@Query("halaman") halaman: Int = 1): List<ProdukDto>\n}\n\nclass ProdukRepositoryImpl @Inject constructor(private val api: TokoApi, private val dao: ProdukDao) : ProdukRepository {\n    override fun pantau(): Flow<List<Produk>> = dao.semua().map { it.map(ProdukEntity::keDomain) }\n\n    override suspend fun segarkan(): Result<Unit> = runCatching {\n        val dto = api.produk()\n        dao.gantiSemua(dto.map(ProdukDto::keEntity)) // UI otomatis ikut berubah lewat Flow\n    }\n}')]),
'Paging 3 untuk daftar panjang': dict(
  ist=[('PagingSource', 'Sumber data per halaman (API atau database).'),
       ('RemoteMediator', 'Menggabungkan halaman dari API ke Room untuk paging offline.'),
       ('LoadState', 'Status memuat: refresh, append, prepend (loading/error/not loading).'),
       ('Cursor vs offset pagination', 'Cursor lebih stabil saat data bertambah di tengah.')],
  cx=[X('PagingSource berbasis halaman API', 'class ProdukPagingSource(private val api: TokoApi) : PagingSource<Int, ProdukDto>() {\n    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, ProdukDto> = try {\n        val hal = params.key ?: 1\n        val data = api.produk(halaman = hal)\n        LoadResult.Page(data, prevKey = if (hal == 1) null else hal - 1, nextKey = if (data.isEmpty()) null else hal + 1)\n    } catch (e: IOException) {\n        LoadResult.Error(e)\n    }\n    override fun getRefreshKey(state: PagingState<Int, ProdukDto>) = state.anchorPosition?.let { state.closestPageToPosition(it)?.prevKey?.plus(1) }\n}\n\n// UI: val item = vm.produk.collectAsLazyPagingItems(); LazyColumn { items(item.itemCount) { i -> item[i]?.let { BarisProduk(it) } } }')]),
'Signing, R8, dan App Bundle': dict(
  ist=[('Android App Bundle (AAB)', 'Format unggah wajib Play Store; Play membuat APK sesuai perangkat.'),
       ('Play App Signing', 'Google menyimpan kunci tanda tangan aplikasi; kamu memakai upload key.'),
       ('R8', 'Pengecil dan pengacak kode (minify, obfuscate) untuk build rilis.'),
       ('ProGuard rules / keep', 'Aturan agar kelas yang dipakai lewat refleksi tidak dihapus R8.')],
  cx=[X('Konfigurasi build rilis', 'android {\n    signingConfigs {\n        create("rilis") {\n            storeFile = file(System.getenv("KEYSTORE_PATH") ?: "upload.jks")\n            storePassword = System.getenv("KEYSTORE_PASS")\n            keyAlias = "upload"\n            keyPassword = System.getenv("KEY_PASS")\n        }\n    }\n    buildTypes {\n        release {\n            isMinifyEnabled = true\n            isShrinkResources = true\n            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")\n            signingConfig = signingConfigs.getByName("rilis")\n        }\n    }\n}\n// ./gradlew bundleRelease -> app/build/outputs/bundle/release/app-release.aab')]),
'Play Console, jalur rilis, dan pemantauan': dict(
  ist=[('Release track', 'Internal testing → closed → open → production.'),
       ('Staged rollout', 'Rilis bertahap ke persentase pengguna; bisa dihentikan bila ada masalah.'),
       ('Android vitals', 'Metrik crash rate, ANR rate, dan startup; di atas ambang membuat aplikasi diturunkan peringkatnya.'),
       ('Target API level', 'Play mewajibkan targetSdk terbaru setiap tahun.')],
  cx=[X('Unggah otomatis ke jalur internal dengan Gradle Play Publisher', 'plugins { id("com.github.triplet.play") version "3.12.1" }\n\nplay {\n    serviceAccountCredentials.set(file(System.getenv("PLAY_SA_JSON") ?: "play.json"))\n    track.set("internal")\n    defaultToAppBundles.set(true)\n    userFraction.set(0.1) // saat dipromosikan ke production: mulai 10%\n}\n// ./gradlew publishReleaseBundle')]),
}
