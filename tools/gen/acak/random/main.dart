import 'dart:math';

void main() {
  final acak = Random();

  // 1. Desimal acak: 0.0 sampai KURANG DARI 1.0
  final r = acak.nextDouble();
  print('desimal: ${r.toStringAsFixed(4)}');

  // 2. Dadu 1..6: nextInt(6) memberi 0..5, lalu ditambah 1
  final dadu = StringBuffer('5 dadu :');
  for (var i = 0; i < 5; i++) {
    dadu.write(' ${acak.nextInt(6) + 1}');
  }
  print(dadu);

  // 3. Rentang bebas bawah..atas (kedua batas ikut)
  const bawah = 10, atas = 20;
  print('10..20 : ${acak.nextInt(atas - bawah + 1) + bawah}');

  // 4. Lempar dadu sampai keluar angka 6
  var lemparan = 0, hasil = 0;
  while (hasil != 6) {
    hasil = acak.nextInt(6) + 1;
    lemparan++;
  }
  print('dapat 6 setelah $lemparan lemparan');

  // 5. Memilih satu isi list dan mengocok list
  final menu = ['soto', 'bakso', 'gado-gado', 'nasi goreng'];
  print('menu   : ${menu[acak.nextInt(menu.length)]}');
  final kartu = [1, 2, 3, 4, 5]..shuffle(acak);
  print('kocok  : $kartu');

  // 6. Seed sama menghasilkan urutan yang sama (berguna untuk pengujian)
  final a = Random(42), b = Random(42);
  var sama = true;
  for (var i = 0; i < 5; i++) {
    if (a.nextInt(100) != b.nextInt(100)) sama = false;
  }
  print('seed 42 dua kali, urutan sama: $sama');
}
