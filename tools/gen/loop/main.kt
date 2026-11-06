fun main() {
    // 1. for dengan range: jumlah putaran sudah pasti
    for (i in 1..3) {
        println("for: i = $i")
    }

    // 2. while: kondisi dicek DULU, bisa 0 kali
    var n = 3
    while (n > 0) {
        println("while: n = $n")
        n--
    }

    // 3. do-while: badan jalan DULU, kondisi dicek di akhir
    var x = 10
    do {
        println("do-while: x = $x (tetap jalan sekali)")
        x++
    } while (x < 5)

    // 4. for-each: menelusuri isi list tanpa indeks
    val buah = listOf("apel", "jeruk", "mangga")
    for (b in buah) {
        println("for-each: $b")
    }

    // 5. bersarang: loop di dalam loop
    for (baris in 1..2) {
        val isi = (1..3).map { kolom -> baris * kolom }
        println("nested: ${isi.joinToString(" ")}")
    }

    // 6. break: keluar dari loop lebih awal
    var hasil = mutableListOf<Int>()
    for (i in 1..10) {
        if (i == 4) break
        hasil.add(i)
    }
    println("break: ${hasil.joinToString(" ")}")

    // 7. continue: lewati sisa badan untuk putaran ini saja
    hasil = mutableListOf()
    for (i in 1..6) {
        if (i % 2 == 0) continue
        hasil.add(i)
    }
    println("continue: ${hasil.joinToString(" ")}")
}
