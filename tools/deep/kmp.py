"""Pendalaman jalur Kotlin Multiplatform."""
K = 'kmp'


def X(t, code, b=None, lang='kotlin'):
    return dict(t=t, b=b, code=code, lang=lang, run=False)


D = {
'Apa itu Kotlin Multiplatform': dict(
  ist=[('Shared business logic', 'Logika bisnis, jaringan, dan database ditulis sekali untuk Android dan iOS.'),
       ('Native UI option', 'UI tetap boleh native (Compose di Android, SwiftUI di iOS).'),
       ('Stable sejak 2023', 'KMP dinyatakan stabil; dipakai Netflix, McDonald\'s, Cash App, dan lainnya.'),
       ('Incremental adoption', 'Bisa dimulai dari satu modul kecil di aplikasi yang sudah ada.')],
  cx=[X('Satu fungsi validasi untuk kedua platform', '// commonMain\nobject Validasi {\n    private val polaHp = Regex("^(\\\\+62|0)8\\\\d{8,11}$")\n    fun nomorHp(input: String): Boolean = polaHp.matches(input.replace(" ", "").replace("-", ""))\n}\n// Android: Validasi.nomorHp(teks)\n// iOS (Swift): Validasi.shared.nomorHp(input: teks)')]),
'Struktur proyek dan expect/actual': dict(
  ist=[('Source set', 'commonMain, androidMain, iosMain, plus versi test-nya.'),
       ('expect / actual', 'Deklarasi di kode bersama, implementasi per platform.'),
       ('Hierarchical project structure', 'Source set bertingkat, misalnya iosMain dipakai bersama iosArm64 dan iosSimulatorArm64.'),
       ('Interface + DI', 'Alternatif expect/actual yang lebih mudah diuji.')],
  cx=[X('Informasi platform dengan expect/actual', '// commonMain\nexpect fun namaPlatform(): String\nfun sapaan() = "Halo dari ${namaPlatform()}"\n\n// androidMain\nactual fun namaPlatform() = "Android ${android.os.Build.VERSION.SDK_INT}"\n\n// iosMain\nactual fun namaPlatform() = platform.UIKit.UIDevice.currentDevice.let { "${it.systemName()} ${it.systemVersion}" }')]),
'Ktor dan kotlinx.serialization di kode bersama': dict(
  ist=[('Ktor client', 'Klien HTTP multiplatform dengan engine per platform (OkHttp, Darwin).'),
       ('ContentNegotiation', 'Plugin Ktor untuk JSON otomatis.'),
       ('@Serializable', 'Anotasi kotlinx.serialization untuk mengubah JSON ↔ objek.'),
       ('ignoreUnknownKeys', 'Abaikan field JSON baru agar aplikasi lama tidak crash.')],
  cx=[X('Klien kurs bersama', '@Serializable\ndata class KursResponse(val base: String, val rates: Map<String, Double>)\n\nclass KursApi(private val client: HttpClient = HttpClient {\n    install(ContentNegotiation) { json(Json { ignoreUnknownKeys = true }) }\n    install(HttpTimeout) { requestTimeoutMillis = 10_000 }\n}) {\n    suspend fun kurs(dasar: String = "IDR"): KursResponse =\n        client.get("https://api.contoh-kurs.id/latest") { parameter("base", dasar) }.body()\n}')]),
'Compose Multiplatform: satu tampilan untuk semua': dict(
  ist=[('Compose Multiplatform', 'UI Compose untuk Android, iOS, desktop, dan web dari JetBrains; iOS stabil sejak 2025.'),
       ('Resources', 'Gambar, string, dan font bersama lewat compose.components.resources.'),
       ('Platform look & feel', 'Pertimbangkan pola navigasi dan gestur khas iOS.'),
       ('Interop', 'Menyisipkan view native (peta, kamera) ke Compose dan sebaliknya.')],
  cx=[X('Layar kurs yang sama di Android dan iOS', '@Composable\nfun LayarKurs(state: KursState, onSegarkan: () -> Unit) {\n    Scaffold(topBar = { TopAppBar(title = { Text(stringResource(Res.string.judul_kurs)) }) }) { pad ->\n        LazyColumn(contentPadding = pad) {\n            items(state.daftar, key = { it.kode }) { k ->\n                ListItem(headlineContent = { Text(k.kode) }, trailingContent = { Text(k.nilaiRupiah) })\n            }\n        }\n    }\n}')]),
'Menyiapkan proyek dengan KMP wizard': dict(
  ist=[('KMP wizard', 'Pembuat proyek di kmp.jetbrains.com / IntelliJ untuk memilih target dan UI.'),
       ('Xcode project', 'Folder iosApp yang dibuka di Xcode untuk menjalankan di simulator.'),
       ('Kotlin/Native', 'Compiler Kotlin ke kode mesin iOS.'),
       ('Gradle sync', 'Proses membaca konfigurasi build; pertama kali bisa lama.')],
  cx=[X('Target di build.gradle.kts modul shared', 'kotlin {\n    androidTarget()\n    listOf(iosX64(), iosArm64(), iosSimulatorArm64()).forEach {\n        it.binaries.framework { baseName = "Shared"; isStatic = true }\n    }\n    sourceSets {\n        commonMain.dependencies {\n            implementation(libs.ktor.client.core)\n            implementation(libs.kotlinx.coroutines.core)\n        }\n        androidMain.dependencies { implementation(libs.ktor.client.okhttp) }\n        iosMain.dependencies { implementation(libs.ktor.client.darwin) }\n    }\n}')]),
'Koin untuk dependency injection': dict(
  ist=[('Koin', 'Kerangka DI ringan berbasis DSL Kotlin, mendukung multiplatform.'),
       ('module { single { } factory { } }', 'single: satu instance; factory: instance baru tiap diminta.'),
       ('koinViewModel()', 'Mengambil ViewModel dari Koin di Compose.'),
       ('Service locator', 'Pola dasar Koin; berbeda dengan Hilt yang berbasis generator kode.')],
  cx=[X('Modul Koin bersama', 'val modulBersama = module {\n    single { KursApi() }\n    single<KursRepository> { KursRepositoryImpl(get(), get()) }\n    factory { KursViewModel(get()) }\n}\n\nfun initKoin(tambahan: Module = module { }) = startKoin { modules(modulBersama, tambahan) }\n// Android: di Application.onCreate(); iOS: dipanggil dari iOSApp.init')]),
'Database bersama: SQLDelight dan Room KMP': dict(
  ist=[('SQLDelight', 'Menulis SQL murni dan menghasilkan API Kotlin bertipe.'),
       ('Room KMP', 'Room kini mendukung multiplatform (Android, iOS, desktop).'),
       ('Driver', 'Implementasi database per platform (AndroidSqliteDriver, NativeSqliteDriver).'),
       ('Offline cache', 'Menyimpan kurs terakhir agar aplikasi tetap berguna tanpa internet.')],
  cx=[X('Query SQLDelight', '-- src/commonMain/sqldelight/id/kurs/Kurs.sq\nCREATE TABLE kurs (\n  kode TEXT PRIMARY KEY NOT NULL,\n  nilai REAL NOT NULL,\n  diperbarui INTEGER NOT NULL\n);\n\nsemua:\nSELECT * FROM kurs ORDER BY kode;\n\nsimpan:\nINSERT OR REPLACE INTO kurs VALUES (?, ?, ?);\n\n-- Kotlin: db.kursQueries.semua().asFlow().mapToList(Dispatchers.IO)', lang='sql')]),
'Memanggil kode Kotlin dari Swift (iOS)': dict(
  ist=[('Objective-C header', 'Kotlin/Native mengekspor API lewat header Objective-C yang dibaca Swift.'),
       ('SKIE', 'Alat dari Touchlab agar suspend function dan Flow terasa alami di Swift (async/await, AsyncSequence).'),
       ('Swift Export', 'Ekspor langsung ke Swift yang sedang dikembangkan JetBrains.'),
       ('Framework', 'Hasil build modul shared yang ditautkan ke proyek Xcode.')],
  cx=[X('SwiftUI memakai ViewModel Kotlin (dengan SKIE)', 'import SwiftUI\nimport Shared\n\nstruct KursView: View {\n    @State private var daftar: [Kurs] = []\n    let vm = KursViewModel()\n\n    var body: some View {\n        List(daftar, id: \\.kode) { k in\n            HStack { Text(k.kode); Spacer(); Text(k.nilaiRupiah) }\n        }\n        .task {\n            for await state in vm.state { daftar = state.daftar } // Flow -> AsyncSequence\n        }\n        .refreshable { try? await vm.segarkan() }               // suspend -> async\n    }\n}', lang='swift')]),
'Proyek: aplikasi kurs mata uang': dict(
  ist=[('Shared ViewModel', 'Logika layar dipakai bersama; UI Android dan iOS hanya menampilkan state.'),
       ('Cache-first', 'Tampilkan kurs tersimpan, lalu perbarui dari jaringan.'),
       ('Rate limit API', 'Batas panggilan API gratis; hemat dengan cache dan interval.'),
       ('Common tests', 'Tes di commonTest berjalan untuk semua platform.')],
  cx=[X('Tes logika konversi di commonTest', 'class KonversiTest {\n    @Test\n    fun konversiDuaArah() {\n        val k = Konverter(mapOf("USD" to 0.0000625, "SGD" to 0.0000842)) // 1 IDR = ...\n        assertEquals(62.5, k.dariRupiah(1_000_000, "USD"), 0.001)\n        assertEquals(1_000_000.0, k.keRupiah(62.5, "USD"), 0.5)\n    }\n}')]),
}
