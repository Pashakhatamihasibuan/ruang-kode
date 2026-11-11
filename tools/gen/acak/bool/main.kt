fun main() {
    // 1. Hasil perbandingan selalu boolean: true atau false
    val nilai = 82
    val hadir = 70
    val nilaiCukup = nilai >= 75
    val hadirCukup = hadir >= 80
    println("nilaiCukup = $nilaiCukup")
    println("hadirCukup = $hadirCukup")

    // 2. AND (&&), OR (||), NOT (!)
    println("AND: lulus = ${nilaiCukup && hadirCukup}")
    println("OR : remedial = ${!nilaiCukup || !hadirCukup}")
    println("NOT: !hadirCukup = ${!hadirCukup}")

    // 3. Tabel kebenaran semua kombinasi p dan q
    val tf = listOf(true, false)
    fun kol(v: Boolean) = v.toString().padEnd(6)
    println("p     q     AND   OR    XOR")
    for (p in tf) {
        for (q in tf) {
            println(kol(p) + kol(q) + kol(p && q) + kol(p || q) + (p xor q))
        }
    }

    // 4. Hukum De Morgan, dicek untuk semua kombinasi
    var hukum1 = true
    var hukum2 = true
    for (p in tf) {
        for (q in tf) {
            if (!(p && q) != (!p || !q)) hukum1 = false
            if (!(p || q) != (!p && !q)) hukum2 = false
        }
    }
    println("De Morgan 1: !(p && q) == !p || !q -> $hukum1")
    println("De Morgan 2: !(p || q) == !p && !q -> $hukum2")

    // 5. Urutan: ! dulu, lalu &&, baru ||
    println("true || false && false = ${true || false && false}")

    // 6. Short-circuit: sisi kanan tidak dihitung jika hasil sudah pasti
    var pembagi = 0
    if (pembagi != 0 && 10 / pembagi > 1) {
        println("hasil bagi besar")
    } else {
        println("short-circuit: 10 / 0 tidak pernah dihitung")
    }
}
