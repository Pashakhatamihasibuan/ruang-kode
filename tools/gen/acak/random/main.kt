import kotlin.random.Random

fun main() {
    // 1. Desimal acak: 0.0 sampai KURANG DARI 1.0
    val r = Random.nextDouble()
    println("desimal: " + "%.4f".format(r))

    // 2. Dadu 1..6: (1..6).random() memasukkan kedua batas
    print("5 dadu :")
    repeat(5) { print(" " + (1..6).random()) }
    println()

    // 3. Rentang bebas: nextInt(dari, sampai) TIDAK memasukkan batas atas
    val bawah = 10
    val atas = 20
    println("10..20 : " + Random.nextInt(bawah, atas + 1))

    // 4. Lempar dadu sampai keluar angka 6
    var lemparan = 0
    var hasil = 0
    while (hasil != 6) {
        hasil = (1..6).random()
        lemparan++
    }
    println("dapat 6 setelah $lemparan lemparan")

    // 5. Memilih satu isi list dan mengocok list
    val menu = listOf("soto", "bakso", "gado-gado", "nasi goreng")
    println("menu   : " + menu.random())
    val kartu = listOf(1, 2, 3, 4, 5).shuffled()
    println("kocok  : $kartu")

    // 6. Seed sama menghasilkan urutan yang sama (berguna untuk pengujian)
    val a = Random(42)
    val b = Random(42)
    val sama = (1..5).all { a.nextInt(100) == b.nextInt(100) }
    println("seed 42 dua kali, urutan sama: $sama")
}
