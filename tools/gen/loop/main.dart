void main() {
  // 1. for: jumlah putaran sudah pasti
  for (var i = 1; i <= 3; i++) {
    print('for: i = $i');
  }

  // 2. while: kondisi dicek DULU, bisa 0 kali
  var n = 3;
  while (n > 0) {
    print('while: n = $n');
    n--;
  }

  // 3. do-while: badan jalan DULU, kondisi dicek di akhir
  var x = 10;
  do {
    print('do-while: x = $x (tetap jalan sekali)');
    x++;
  } while (x < 5);

  // 4. for-in: menelusuri isi list tanpa indeks
  final buah = ['apel', 'jeruk', 'mangga'];
  for (final b in buah) {
    print('for-each: $b');
  }

  // 5. bersarang: loop di dalam loop
  for (var baris = 1; baris <= 2; baris++) {
    final isi = <int>[];
    for (var kolom = 1; kolom <= 3; kolom++) {
      isi.add(baris * kolom);
    }
    print('nested: ${isi.join(' ')}');
  }

  // 6. break: keluar dari loop lebih awal
  var hasil = <int>[];
  for (var i = 1; i <= 10; i++) {
    if (i == 4) break;
    hasil.add(i);
  }
  print('break: ${hasil.join(' ')}');

  // 7. continue: lewati sisa badan untuk putaran ini saja
  hasil = [];
  for (var i = 1; i <= 6; i++) {
    if (i % 2 == 0) continue;
    hasil.add(i);
  }
  print('continue: ${hasil.join(' ')}');
}
