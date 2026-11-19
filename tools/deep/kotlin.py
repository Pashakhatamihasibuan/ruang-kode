"""Pendalaman jalur Kotlin: istilah dunia kerja dan contoh tambahan."""
K = 'kotlin'


def X(t, code, out=None, b=None, lang='kotlin'):
    return dict(t=t, b=b, code=code, lang=lang, run=False, out=out)


D = {
'Program Kotlin pertama': dict(
  ist=[('Kotlin/JVM', 'Kotlin dikompilasi ke bytecode JVM; bisa memakai semua pustaka Java.'),
       ('Android first-class language', 'Google menjadikan Kotlin bahasa utama Android sejak 2019.'),
       ('K2 compiler', 'Compiler Kotlin 2.x yang jauh lebih cepat.'),
       ('Interop', 'Kotlin dan Java bisa saling memanggil dalam satu proyek.')],
  cx=[X('main dengan argumen', 'fun main(args: Array<String>) {\n    val nama = args.firstOrNull() ?: "Dunia"\n    println("Halo, $nama!")\n    println("Kotlin ${KotlinVersion.CURRENT.major}.x")\n}', "Halo, Dunia!\nKotlin 2.x")]),
'val, var, tipe data, dan null safety': dict(
  ist=[('val vs var', 'val tidak bisa diganti (utamakan), var bisa diganti.'),
       ('Nullable type', 'String? boleh null; String tidak.'),
       ('Elvis operator', '?: memberi nilai cadangan saat null.'),
       ('!! (not-null assertion)', 'Memaksa non-null; melempar NPE jika ternyata null. Hindari.')],
  cx=[X('Safe call, Elvis, dan smart cast', 'fun panjangNama(nama: String?): Int = nama?.trim()?.length ?: 0\n\nfun main() {\n    println(panjangNama("  Sari "))\n    println(panjangNama(null))\n    val kota: String? = "Medan"\n    if (kota != null) println(kota.uppercase()) // smart cast ke String\n}', "4\n0\nMEDAN")]),
'String template dan format keluaran': dict(
  ist=[('String template', '"Halo, $nama" dan "${ekspresi}".'),
       ('Raw string', 'Teks multi-baris dengan """ dan trimIndent().'),
       ('String.format / NumberFormat', 'Format angka sesuai locale.'),
       ('buildString', 'Menyusun teks efisien dengan StringBuilder di dalamnya.')],
  cx=[X('Format rupiah dengan Locale Indonesia', 'import java.text.NumberFormat\nimport java.util.Locale\n\nfun main() {\n    val id = Locale.forLanguageTag("id-ID")\n    println(String.format(id, "%,d", 1_250_000))\n    println(NumberFormat.getCurrencyInstance(id).format(85_000))\n    val struk = buildString {\n        appendLine("Kopi Gayo".padEnd(12) + "x2")\n        append("Total".padEnd(12) + "170.000")\n    }\n    println(struk)\n}', "1.250.000\nRp85.000,00\nKopi Gayo   x2\nTotal       170.000")]),
'if dan when sebagai ekspresi, range dan loop': dict(
  ist=[('Expression vs statement', 'if dan when menghasilkan nilai di Kotlin.'),
       ('when', 'Pengganti switch yang lebih kuat: bisa range, tipe, dan kondisi bebas.'),
       ('Range', '1..10, 1 until 10, 10 downTo 1 step 2.'),
       ('Exhaustive when', 'when atas sealed class/enum wajib lengkap jika dipakai sebagai ekspresi.')],
  cx=[X('Tarif ongkir dengan when dan range', 'fun ongkir(gram: Int): String = when (gram) {\n    in 1..1000 -> "Rp9.000"\n    in 1001..3000 -> "Rp15.000"\n    in 3001..10_000 -> "Rp22.000"\n    else -> if (gram <= 0) "berat tidak valid" else "kargo"\n}\n\nfun main() {\n    for (g in listOf(800, 1000, 2500, 12000, 0)) println("$g g -> ${ongkir(g)}")\n}', "800 g -> Rp9.000\n1000 g -> Rp9.000\n2500 g -> Rp15.000\n12000 g -> kargo\n0 g -> berat tidak valid")]),
'Latihan algoritma: Fibonacci, bubble sort, prima': dict(
  ist=[('Sequence', 'Koleksi malas Kotlin; elemen dihitung saat dibutuhkan.'),
       ('generateSequence', 'Membuat deret tak terbatas dari nilai awal dan rumus.'),
       ('Idiomatic Kotlin', 'Gaya penulisan khas Kotlin: ringkas, ekspresif, memakai fungsi koleksi.'),
       ('Complexity', 'Selalu sebutkan Big-O solusimu saat wawancara.')],
  cx=[X('Fibonacci dengan Sequence dan prima dengan filter', 'fun main() {\n    val fib = generateSequence(0 to 1) { (a, b) -> b to a + b }.map { it.first }\n    println(fib.take(10).toList())\n    val prima = (2..50).filter { n -> (2..Math.sqrt(n.toDouble()).toInt()).none { n % it == 0 } }\n    println(prima)\n}', "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]")]),
'Fungsi, lambda, dan koleksi': dict(
  ist=[('Default & named argument', 'Parameter bawaan dan pemanggilan bernama: kirim(ke = "a", prioritas = true).'),
       ('Trailing lambda', 'Lambda terakhir boleh di luar kurung: list.filter { it > 0 }.'),
       ('it', 'Nama bawaan parameter tunggal lambda.'),
       ('Immutable collection', 'listOf/mapOf tidak bisa diubah; mutableListOf bisa.')],
  cx=[X('Ringkasan penjualan dengan fungsi koleksi', 'data class Jual(val kota: String, val nilai: Int)\n\nfun main() {\n    val data = listOf(Jual("Medan", 170), Jual("Jakarta", 210), Jual("Medan", 105), Jual("Bandung", 90))\n    println(data.groupBy { it.kota }.mapValues { (_, v) -> v.sumOf { it.nilai } })\n    println(data.maxBy { it.nilai })\n    println(data.filter { it.nilai >= 100 }.joinToString { it.kota })\n}', "{Medan=275, Jakarta=210, Bandung=90}\nJual(kota=Jakarta, nilai=210)\nMedan, Jakarta, Medan")]),
'Semua jenis perulangan: for, while, do-while, for-each, break, continue': dict(
  ist=[('forEachIndexed / withIndex', 'Menelusuri dengan indeks.'),
       ('Labeled break', 'break@luar keluar dari loop bersarang.'),
       ('repeat(n)', 'Mengulang blok n kali.'),
       ('return@forEach', 'Lompat ke elemen berikutnya di dalam lambda forEach.')],
  cx=[X('withIndex dan break berlabel', 'fun main() {\n    val antrean = listOf("A001", "A002", "BATAL", "A004")\n    for ((i, no) in antrean.withIndex()) {\n        if (no == "BATAL") continue\n        println("${i + 1}. $no")\n    }\n    luar@ for (r in 1..3) for (k in 1..3) {\n        if (r * k == 4) { println("ketemu di $r x $k"); break@luar }\n    }\n}', "1. A001\n2. A002\n4. A004\nketemu di 2 x 2")]),
'Boolean logic: AND, OR, NOT, tabel kebenaran, dan De Morgan': dict(
  ist=[('&& / || / !', 'AND, OR, NOT dengan short-circuit.'),
       ('and / or / xor (infix)', 'Versi tanpa short-circuit; jarang dipakai.'),
       ('Predicate function', 'Fungsi (T) -> Boolean, misalnya dipakai di filter.'),
       ('De Morgan', '!(a && b) == !a || !b.')],
  cx=[X('Tabel kebenaran De Morgan', 'fun main() {\n    for (a in listOf(true, false)) for (b in listOf(true, false)) {\n        println("$a $b -> ${!(a && b) == (!a || !b)}")\n    }\n}', "true true -> true\ntrue false -> true\nfalse true -> true\nfalse false -> true")]),
'Random number: bilangan acak, rentang, seed, dan mengocok': dict(
  ist=[('Random.nextInt(a, b)', 'Bilangan acak a sampai b−1.'),
       ('Random(seed)', 'Deret yang bisa diulang untuk pengujian.'),
       ('shuffled / random()', 'Mengacak list dan mengambil satu elemen acak.'),
       ('SecureRandom', 'Untuk OTP, token, dan kunci; dari java.security.')],
  cx=[X('Kode voucher acak dengan karakter yang mudah dibaca', 'import java.security.SecureRandom\n\nconst val HURUF = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789" // tanpa O, 0, I, 1 agar tidak tertukar\n\nfun voucher(panjang: Int = 8): String {\n    val r = SecureRandom()\n    return (1..panjang).map { HURUF[r.nextInt(HURUF.length)] }.joinToString("")\n}\n\nfun main() {\n    val v = voucher()\n    println("Panjang: ${v.length}, valid: ${v.all { it in HURUF }}")\n}', "Panjang: 8, valid: true")]),
'Class, data class, dan sealed class': dict(
  ist=[('data class', 'Kelas data dengan equals, hashCode, toString, copy otomatis.'),
       ('sealed class / interface', 'Hierarki tertutup; when atasnya wajib lengkap.'),
       ('UI state', 'Pola sealed interface UiState { Loading, Success, Error } di Android.'),
       ('Primary constructor', 'Konstruktor di baris deklarasi kelas.')],
  cx=[X('UI state dengan sealed interface', 'sealed interface UiState {\n    data object Loading : UiState\n    data class Success(val produk: List<String>) : UiState\n    data class Error(val pesan: String) : UiState\n}\n\nfun render(s: UiState) = when (s) {\n    UiState.Loading -> "Memuat..."\n    is UiState.Success -> "${s.produk.size} produk"\n    is UiState.Error -> "Error: ${s.pesan}"\n}\n\nfun main() {\n    listOf(UiState.Loading, UiState.Success(listOf("Kopi", "Teh")), UiState.Error("timeout")).forEach { println(render(it)) }\n}', "Memuat...\n2 produk\nError: timeout")]),
'Extension function dan scope function': dict(
  ist=[('Extension function', 'Menambah fungsi ke kelas yang sudah ada: fun Int.rupiah().'),
       ('let / run / apply / also / with', 'Scope function untuk null check, konfigurasi objek, dan efek samping.'),
       ('apply', 'Mengonfigurasi objek lalu mengembalikan objek itu sendiri.'),
       ('also', 'Melakukan efek samping (log) tanpa mengubah alur.')],
  cx=[X('Extension rupiah dan apply untuk konfigurasi', 'fun Long.rupiah(): String = "Rp" + "%,d".format(this).replace(\',\', \'.\')\n\ndata class Permintaan(var url: String = "", var timeoutDetik: Int = 10, val header: MutableMap<String, String> = mutableMapOf())\n\nfun main() {\n    println(1_250_000L.rupiah())\n    val req = Permintaan().apply {\n        url = "https://api.tokokopi.id/produk"\n        timeoutDetik = 15\n        header["Accept"] = "application/json"\n    }.also { println("Kirim ke ${it.url}") }\n    println(req.timeoutDetik)\n}', "Rp1.250.000\nKirim ke https://api.tokokopi.id/produk\n15")]),
'Coroutines: kode asinkron yang mudah dibaca': dict(
  ist=[('suspend function', 'Fungsi yang bisa ditunda tanpa memblokir thread.'),
       ('Structured concurrency', 'Coroutine anak terikat ke scope induk; batal bersama, tidak bocor.'),
       ('Dispatchers.IO / Main / Default', 'Tempat coroutine berjalan: I/O, UI, kerja CPU.'),
       ('async / await', 'Menjalankan beberapa tugas paralel dan menunggu hasilnya.')],
  cx=[X('Memuat dua data paralel dengan async', 'import kotlinx.coroutines.*\nimport kotlin.system.measureTimeMillis\n\nsuspend fun profil(): String { delay(300); return "Sari" }\nsuspend fun saldo(): Long { delay(200); return 150_000 }\n\nfun main() = runBlocking {\n    val waktu = measureTimeMillis {\n        val p = async { profil() }\n        val s = async { saldo() }\n        println("${p.await()} punya saldo ${s.await()}")\n    }\n    println("Paralel (< 400 ms): ${waktu < 400}")\n}', "Sari punya saldo 150000\nParalel (< 400 ms): true")]),
'Build tool dan library Kotlin populer': dict(
  ist=[('Gradle Kotlin DSL', 'build.gradle.kts: konfigurasi build ditulis dalam Kotlin.'),
       ('Version catalog', 'gradle/libs.versions.toml: satu tempat mengatur versi semua pustaka.'),
       ('KSP', 'Kotlin Symbol Processing untuk generator kode (Room, Hilt, Moshi).'),
       ('kotlinx', 'Pustaka resmi: coroutines, serialization, datetime.')],
  cx=[X('Version catalog', '[versions]\nkotlin = "2.0.21"\ncoroutines = "1.9.0"\nktor = "3.0.1"\n\n[libraries]\nkotlinx-coroutines-core = { module = "org.jetbrains.kotlinx:kotlinx-coroutines-core", version.ref = "coroutines" }\nktor-client-core = { module = "io.ktor:ktor-client-core", version.ref = "ktor" }\n\n[plugins]\nkotlin-jvm = { id = "org.jetbrains.kotlin.jvm", version.ref = "kotlin" }\n\n# build.gradle.kts\n# dependencies { implementation(libs.kotlinx.coroutines.core) }', lang='text')]),
'Exception, require, dan Result': dict(
  ist=[('require / check', 'Validasi argumen (IllegalArgumentException) dan state (IllegalStateException).'),
       ('runCatching / Result', 'Membungkus hasil yang bisa gagal tanpa try-catch bertebaran.'),
       ('No checked exception', 'Kotlin tidak mewajibkan menangkap exception seperti Java.'),
       ('Error boundary', 'Satu tempat menangani error per lapisan (repository mengubah exception menjadi Result).')],
  cx=[X('require dan runCatching', 'fun tarik(saldo: Long, jumlah: Long): Long {\n    require(jumlah > 0) { "jumlah harus positif" }\n    check(saldo >= jumlah) { "saldo tidak cukup" }\n    return saldo - jumlah\n}\n\nfun main() {\n    for (j in listOf(50_000L, -1L, 500_000L)) {\n        val hasil = runCatching { tarik(100_000, j) }\n        println(hasil.fold({ "sisa $it" }, { "gagal: ${it.message}" }))\n    }\n}', "sisa 50000\ngagal: jumlah harus positif\ngagal: saldo tidak cukup")]),
'Generics, enum class, dan object': dict(
  ist=[('object', 'Singleton bawaan bahasa.'),
       ('companion object', 'Anggota "statis" sebuah kelas, misalnya factory.'),
       ('enum class dengan properti', 'Enum yang membawa data dan fungsi.'),
       ('Variance (in / out)', 'Aturan generic untuk tipe yang hanya dibaca (out) atau ditulis (in).')],
  cx=[X('Enum dengan properti dan companion factory', 'enum class Kurir(val kode: String, val estimasiHari: IntRange) {\n    JNE("jne", 2..3), SICEPAT("sicepat", 1..2), POS("pos", 3..5);\n\n    companion object {\n        fun dariKode(k: String) = entries.firstOrNull { it.kode == k } ?: error("kurir tidak dikenal: $k")\n    }\n}\n\nfun main() {\n    val k = Kurir.dariKode("sicepat")\n    println("$k tiba ${k.estimasiHari.first}-${k.estimasiHari.last} hari")\n    println(Kurir.entries.minBy { it.estimasiHari.last })\n}', "SICEPAT tiba 1-2 hari\nSICEPAT")]),
'Flow: aliran data asinkron': dict(
  ist=[('Cold flow', 'Flow yang baru berjalan saat dikumpulkan (collect).'),
       ('StateFlow / SharedFlow', 'Hot flow untuk state UI dan event.'),
       ('Operator', 'map, filter, debounce, combine, flatMapLatest.'),
       ('collectAsStateWithLifecycle', 'Mengumpulkan flow di Compose dengan aman terhadap lifecycle.')],
  cx=[X('Flow harga dengan operator', 'import kotlinx.coroutines.flow.*\nimport kotlinx.coroutines.runBlocking\n\nfun main() = runBlocking {\n    flowOf(85_000, 87_000, 86_000, 90_000)\n        .filter { it >= 86_000 }\n        .map { "Rp$it" }\n        .collect { println(it) }\n}', "Rp87000\nRp86000\nRp90000")]),
'Proyek: struk kasir': dict(
  ist=[('Domain model', 'data class Item, Keranjang dengan perilaku sendiri.'),
       ('BigDecimal', 'Perhitungan uang yang presisi; di Kotlin bisa memakai operator + dan *.'),
       ('Pure function', 'Fungsi hitung tanpa efek samping, mudah diuji.'),
       ('Receipt formatting', 'Merapikan kolom struk dengan padStart/padEnd.')],
  cx=[X('Hitung struk dengan BigDecimal', 'import java.math.BigDecimal\nimport java.math.RoundingMode\n\ndata class Item(val nama: String, val harga: BigDecimal, val qty: Int) {\n    val subtotal get() = harga * qty.toBigDecimal()\n}\n\nfun main() {\n    val items = listOf(Item("Kopi Gayo", "85000".toBigDecimal(), 2), Item("Gula Aren", "28000".toBigDecimal(), 1))\n    val sub = items.sumOf { it.subtotal }\n    val ppn = (sub * "0.12".toBigDecimal()).setScale(0, RoundingMode.HALF_UP)\n    items.forEach { println(it.nama.padEnd(12) + it.subtotal.toString().padStart(8)) }\n    println("PPN 12%".padEnd(12) + ppn.toString().padStart(8))\n    println("TOTAL".padEnd(12) + (sub + ppn).toString().padStart(8))\n}', "Kopi Gayo     170000\nGula Aren      28000\nPPN 12%        23760\nTOTAL         221760")]),
'Pewarisan, interface, dan visibility': dict(
  ist=[('open', 'Kelas dan fungsi Kotlin final secara bawaan; harus open agar bisa diwarisi.'),
       ('internal', 'Terlihat hanya dalam satu modul Gradle.'),
       ('Interface dengan implementasi bawaan', 'Interface boleh punya fungsi berisi.'),
       ('override', 'Kata kunci wajib saat menimpa anggota induk.')],
  cx=[X('Interface pembayaran', 'interface Pembayaran {\n    val nama: String\n    fun biaya(nominal: Long): Long = 0\n    fun ringkas(nominal: Long) = "$nama: total ${nominal + biaya(nominal)}"\n}\n\nclass Qris : Pembayaran { override val nama = "QRIS"; override fun biaya(nominal: Long) = nominal * 7 / 1000 }\nclass Cod : Pembayaran { override val nama = "COD"; override fun biaya(nominal: Long) = 5_000L }\nclass Transfer : Pembayaran { override val nama = "Transfer" }\n\nfun main() {\n    listOf(Qris(), Cod(), Transfer()).forEach { println(it.ringkas(200_000)) }\n}', "QRIS: total 201400\nCOD: total 205000\nTransfer: total 200000")]),
'Delegation: by lazy, observable, dan class delegation': dict(
  ist=[('by lazy', 'Nilai dihitung sekali saat pertama dipakai.'),
       ('Delegates.observable', 'Menjalankan kode setiap kali properti berubah.'),
       ('Class delegation (by)', 'Meneruskan implementasi interface ke objek lain; alternatif pewarisan.'),
       ('Property delegate', 'Mekanisme di balik by viewModels(), by remember di Android.')],
  cx=[X('lazy dan observable', 'import kotlin.properties.Delegates\n\nclass Pengaturan {\n    val konfigurasiBerat: String by lazy { println("memuat konfigurasi..."); "siap" }\n    var tema: String by Delegates.observable("terang") { _, lama, baru -> println("tema $lama -> $baru") }\n}\n\nfun main() {\n    val p = Pengaturan()\n    println("objek dibuat")\n    println(p.konfigurasiBerat)\n    println(p.konfigurasiBerat)\n    p.tema = "gelap"\n}', "objek dibuat\nmemuat konfigurasi...\nsiap\nsiap\ntema terang -> gelap")]),
'Destructuring, operator overloading, dan infix': dict(
  ist=[('componentN', 'Fungsi yang memungkinkan destructuring: val (a, b) = pasangan.'),
       ('operator fun', 'Mendefinisikan arti +, -, *, [], in untuk kelas sendiri.'),
       ('infix', 'Pemanggilan tanpa titik dan kurung: 1 to "satu".'),
       ('Value class', 'Pembungkus tipe tanpa biaya runtime: @JvmInline value class Rupiah(val v: Long).')],
  cx=[X('Kelas Uang dengan operator plus dan times', 'data class Uang(val rupiah: Long) {\n    operator fun plus(lain: Uang) = Uang(rupiah + lain.rupiah)\n    operator fun times(n: Int) = Uang(rupiah * n)\n    override fun toString() = "Rp$rupiah"\n}\n\ninfix fun Int.kali(u: Uang) = u * this\n\nfun main() {\n    val kopi = Uang(85_000)\n    val total = kopi * 2 + Uang(28_000)\n    println(total)\n    println(3 kali kopi)\n    val (nilai) = total\n    println(nilai)\n}', "Rp198000\nRp255000\n198000")]),
'Higher-order function, inline, dan reified': dict(
  ist=[('Higher-order function', 'Fungsi yang menerima atau mengembalikan fungsi.'),
       ('inline', 'Badan fungsi disalin ke pemanggil; menghindari biaya objek lambda.'),
       ('reified', 'Tipe generic bisa dibaca saat runtime pada fungsi inline.'),
       ('Function type', '(Int) -> String sebagai tipe parameter.')],
  cx=[X('Pengukur waktu dan filter berdasarkan tipe', 'inline fun <T> ukur(label: String, blok: () -> T): T {\n    val mulai = System.nanoTime()\n    return blok().also { println("$label selesai: ${(System.nanoTime() - mulai) >= 0}") }\n}\n\ninline fun <reified T> List<Any>.hanya(): List<T> = filterIsInstance<T>()\n\nfun main() {\n    val total = ukur("hitung") { (1..1_000).sum() }\n    println(total)\n    println(listOf(1, "dua", 3.0, "empat").hanya<String>())\n}', "hitung selesai: true\n500500\n[dua, empat]")]),
'Type-safe builder (DSL)': dict(
  ist=[('DSL', 'Domain-Specific Language: sintaks khusus yang terbaca seperti konfigurasi.'),
       ('Lambda with receiver', 'T.() -> Unit; dasar DSL Kotlin, Gradle KTS, dan Compose.'),
       ('@DslMarker', 'Mencegah salah akses ke scope luar di DSL bersarang.'),
       ('Builder pattern', 'Menyusun objek kompleks langkah demi langkah.')],
  cx=[X('DSL kecil untuk membuat email', 'class Email { var ke = ""; var subjek = ""; private val isi = StringBuilder()\n    fun baris(t: String) { isi.appendLine(t) }\n    override fun toString() = "Ke: $ke\\nSubjek: $subjek\\n$isi".trimEnd()\n}\n\nfun email(atur: Email.() -> Unit) = Email().apply(atur)\n\nfun main() {\n    println(email {\n        ke = "sari@contoh.id"\n        subjek = "Pesanan INV-7 dikirim"\n        baris("Halo Sari,")\n        baris("Paketmu sedang dalam perjalanan.")\n    })\n}', "Ke: sari@contoh.id\nSubjek: Pesanan INV-7 dikirim\nHalo Sari,\nPaketmu sedang dalam perjalanan.")]),
'Pengujian Kotlin: JUnit 5, kotest, dan MockK': dict(
  ist=[('MockK', 'Pustaka mocking khas Kotlin (mendukung coroutine dan object).'),
       ('kotest', 'Kerangka tes Kotlin dengan gaya spesifikasi dan property-based testing.'),
       ('runTest', 'Menguji coroutine dengan waktu virtual (delay tidak benar-benar menunggu).'),
       ('Turbine', 'Pustaka untuk menguji Flow.')],
  cx=[X('Tes ViewModel dengan MockK dan runTest', 'class KeranjangViewModelTest {\n    private val repo = mockk<KeranjangRepository>()\n\n    @Test\n    fun `checkout sukses mengosongkan keranjang`() = runTest {\n        coEvery { repo.checkout(any()) } returns Result.success("INV-7")\n        val vm = KeranjangViewModel(repo)\n        vm.tambah(Produk(1, "Kopi", 85_000))\n\n        vm.checkout()\n        advanceUntilIdle()\n\n        assertEquals(0, vm.state.value.item.size)\n        coVerify(exactly = 1) { repo.checkout(any()) }\n    }\n}')]),
}
