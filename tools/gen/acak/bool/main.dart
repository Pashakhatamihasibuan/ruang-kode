void main() {
  // 1. Hasil perbandingan selalu boolean: true atau false
  const nilai = 82, hadir = 70;
  final nilaiCukup = nilai >= 75;
  final hadirCukup = hadir >= 80;
  print('nilaiCukup = $nilaiCukup');
  print('hadirCukup = $hadirCukup');

  // 2. AND (&&), OR (||), NOT (!)
  print('AND: lulus = ${nilaiCukup && hadirCukup}');
  print('OR : remedial = ${!nilaiCukup || !hadirCukup}');
  print('NOT: !hadirCukup = ${!hadirCukup}');

  // 3. Tabel kebenaran semua kombinasi p dan q
  const tf = [true, false];
  String kol(bool v) => '$v'.padRight(6);
  print('p     q     AND   OR    XOR');
  for (final p in tf) {
    for (final q in tf) {
      print(kol(p) + kol(q) + kol(p && q) + kol(p || q) + '${p ^ q}');
    }
  }

  // 4. Hukum De Morgan, dicek untuk semua kombinasi
  var hukum1 = true, hukum2 = true;
  for (final p in tf) {
    for (final q in tf) {
      if (!(p && q) != (!p || !q)) hukum1 = false;
      if (!(p || q) != (!p && !q)) hukum2 = false;
    }
  }
  print('De Morgan 1: !(p && q) == !p || !q -> $hukum1');
  print('De Morgan 2: !(p || q) == !p && !q -> $hukum2');

  // 5. Urutan: ! dulu, lalu &&, baru ||
  print('true || false && false = ${true || false && false}');

  // 6. Short-circuit: sisi kanan tidak dihitung jika hasil sudah pasti
  var pembagi = 0;
  if (pembagi != 0 && 10 ~/ pembagi > 1) {
    print('hasil bagi besar');
  } else {
    print('short-circuit: 10 / 0 tidak pernah dihitung');
  }
}
