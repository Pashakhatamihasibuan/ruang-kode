"""Soal latihan tambahan untuk jalur Pseudocode, Flowgorithm, dan Git & GitHub."""
from mobile_dart_x import S


def P(soal, petunjuk, jawab, out=None):
    return S(soal, petunjuk, jawab, out, lang='text')


def B(soal, petunjuk, jawab, out=None):
    return S(soal, petunjuk, jawab, out, lang='bash')


PSEUDO = {
'Algoritma dan pseudocode': [
  P('Tulis algoritma (langkah bernomor) untuk membuat teh manis.', 'Pastikan urutannya jelas, setiap langkah satu tindakan, dan ada kondisi selesai.',
    '1. Siapkan gelas, kantong teh, gula, dan air panas.\n2. Masukkan kantong teh ke gelas.\n3. Tuang air panas sampai 3/4 gelas.\n4. Tunggu 3 menit, lalu angkat kantong teh.\n5. Masukkan 2 sendok gula.\n6. Aduk sampai gula larut.\n7. Selesai: teh siap diminum.'),
  P('Tulis pseudocode yang menerima dua angka lalu menampilkan jumlahnya.', 'Pola input, proses, output: INPUT a, INPUT b, total ← a + b, OUTPUT total.',
    'DECLARE a, b, total : INTEGER\nINPUT a\nINPUT b\ntotal ← a + b\nOUTPUT "Jumlah = ", total', 'Masukan 7 dan 5 → Jumlah = 12'),
],
'Aturan menulis pseudocode': [
  P('Perbaiki pseudocode berikut agar mengikuti aturan:<br><code>input umur; if umur>=17 output boleh else output belum</code>', 'Satu baris satu langkah, kata kunci huruf besar, indentasi, dan setiap IF ditutup ENDIF.',
    'DECLARE umur : INTEGER\nINPUT umur\nIF umur >= 17 THEN\n    OUTPUT "Boleh membuat KTP"\nELSE\n    OUTPUT "Belum boleh"\nENDIF'),
  P('Apa bedanya <code>x ← x + 1</code> dan <code>x = x + 1</code> di pseudocode?', '← adalah perintah mengisi nilai, = adalah perbandingan.',
    'x ← x + 1  : hitung x + 1, lalu simpan ke x (x bertambah 1)\nx = x + 1  : pertanyaan "apakah x sama dengan x + 1?"\n             hasilnya selalu FALSE'),
],
'Variabel, tipe data, dan operator': [
  P('Ubah 135 menit menjadi jam dan menit memakai DIV dan MOD.', 'DIV memberi hasil bagi bulat, MOD memberi sisa.',
    'DECLARE total, jam, menit : INTEGER\ntotal ← 135\njam ← total DIV 60\nmenit ← total MOD 60\nOUTPUT jam, " jam ", menit, " menit"', '2 jam 15 menit'),
  P('Tukar isi variabel a = 3 dan b = 8 lalu tampilkan keduanya.', 'Butuh variabel bantu t agar nilai a tidak hilang.',
    'DECLARE a, b, t : INTEGER\na ← 3\nb ← 8\nt ← a\na ← b\nb ← t\nOUTPUT "a = ", a, ", b = ", b', 'a = 8, b = 3'),
  P('Hitung rata-rata tiga nilai 80, 75, 92 dan tampilkan dengan tipe yang tepat.', 'Rata-rata bisa pecahan, jadi pakai REAL.',
    'DECLARE n1, n2, n3 : INTEGER\nDECLARE rata : REAL\nn1 ← 80\nn2 ← 75\nn3 ← 92\nrata ← (n1 + n2 + n3) / 3\nOUTPUT "Rata-rata: ", rata', 'Rata-rata: 82.333...'),
],
'IF dan ELSE': [
  P('Tentukan apakah sebuah bilangan positif, negatif, atau nol.', 'Pakai IF, ELSE IF, ELSE.',
    'DECLARE n : INTEGER\nINPUT n\nIF n > 0 THEN\n    OUTPUT "Positif"\nELSE IF n < 0 THEN\n    OUTPUT "Negatif"\nELSE\n    OUTPUT "Nol"\nENDIF', 'Masukan -4 → Negatif'),
  P('Ongkir gratis jika belanja minimal 100000, selain itu ongkir 15000. Tampilkan total bayar.', 'Hitung ongkir dengan IF, lalu total ← belanja + ongkir.',
    'DECLARE belanja, ongkir : INTEGER\nINPUT belanja\nIF belanja >= 100000 THEN\n    ongkir ← 0\nELSE\n    ongkir ← 15000\nENDIF\nOUTPUT "Total: ", belanja + ongkir', 'Masukan 85000 → Total: 100000'),
],
'Percabangan bertingkat': [
  P('Ubah nilai angka menjadi huruf: ≥ 85 A, ≥ 70 B, ≥ 55 C, ≥ 40 D, selain itu E.', 'Urutkan dari batas terbesar agar setiap cabang cukup memeriksa satu batas.',
    'DECLARE nilai : INTEGER\nINPUT nilai\nIF nilai >= 85 THEN\n    OUTPUT "A"\nELSE IF nilai >= 70 THEN\n    OUTPUT "B"\nELSE IF nilai >= 55 THEN\n    OUTPUT "C"\nELSE IF nilai >= 40 THEN\n    OUTPUT "D"\nELSE\n    OUTPUT "E"\nENDIF', 'Masukan 72 → B'),
  P('Tarif parkir: motor Rp2.000, mobil Rp5.000, lainnya Rp10.000. Tulis dengan CASE.', 'CASE OF jenis ... OTHERWISE ... ENDCASE.',
    'DECLARE jenis : STRING\nINPUT jenis\nCASE OF jenis\n    "motor" : OUTPUT 2000\n    "mobil" : OUTPUT 5000\n    OTHERWISE : OUTPUT 10000\nENDCASE', 'Masukan "mobil" → 5000'),
],
'Operator logika: and, or, not': [
  P('Tentukan tahun kabisat: habis dibagi 4 dan tidak habis dibagi 100, atau habis dibagi 400.', '(t MOD 4 = 0 AND t MOD 100 <> 0) OR t MOD 400 = 0.',
    'DECLARE t : INTEGER\nINPUT t\nIF (t MOD 4 = 0 AND t MOD 100 <> 0) OR t MOD 400 = 0 THEN\n    OUTPUT t, " kabisat"\nELSE\n    OUTPUT t, " bukan kabisat"\nENDIF', '2024 kabisat · 1900 bukan kabisat · 2000 kabisat'),
  P('Mahasiswa boleh ikut ujian jika kehadiran ≥ 75% dan tidak punya tunggakan. Tulis kondisinya.', 'Gabungkan dengan AND dan NOT.',
    'DECLARE hadir : INTEGER\nDECLARE tunggakan : BOOLEAN\nINPUT hadir\nINPUT tunggakan\nIF hadir >= 75 AND NOT tunggakan THEN\n    OUTPUT "Boleh ikut ujian"\nELSE\n    OUTPUT "Tidak boleh ikut ujian"\nENDIF'),
],
'FOR: jumlah putaran sudah diketahui': [
  P('Tampilkan bilangan kelipatan 3 dari 3 sampai 30 dan jumlahnya.', 'FOR dengan STEP 3, dan akumulator total yang diisi 0 di awal.',
    'DECLARE i, total : INTEGER\ntotal ← 0\nFOR i ← 3 TO 30 STEP 3 DO\n    OUTPUT i\n    total ← total + i\nENDFOR\nOUTPUT "Jumlah = ", total', '3 6 9 12 15 18 21 24 27 30\nJumlah = 165'),
  P('Hitung faktorial n (n! = 1 × 2 × ... × n). Uji dengan n = 6.', 'Akumulator perkalian dimulai dari 1, bukan 0.',
    'DECLARE n, i, hasil : INTEGER\nINPUT n\nhasil ← 1\nFOR i ← 1 TO n DO\n    hasil ← hasil * i\nENDFOR\nOUTPUT n, "! = ", hasil', '6! = 720'),
],
'WHILE: ulangi selama kondisi benar': [
  P('Tabungan awal 100.000 bertambah 10% setiap tahun. Berapa tahun sampai tabungan mencapai 200.000?', 'Jumlah tahun belum diketahui, jadi WHILE saldo < 200000.',
    'DECLARE saldo : REAL\nDECLARE tahun : INTEGER\nsaldo ← 100000\ntahun ← 0\nWHILE saldo < 200000 DO\n    saldo ← saldo * 1.1\n    tahun ← tahun + 1\nENDWHILE\nOUTPUT "Butuh ", tahun, " tahun"', 'Butuh 8 tahun'),
  P('Hitung banyaknya digit sebuah bilangan bulat positif (contoh 40271 punya 5 digit).', 'Bagi dengan 10 (DIV) berulang selama angka > 0, sambil menghitung.',
    'DECLARE n, digit : INTEGER\nINPUT n\ndigit ← 0\nWHILE n > 0 DO\n    n ← n DIV 10\n    digit ← digit + 1\nENDWHILE\nOUTPUT digit, " digit"', 'Masukan 40271 → 5 digit'),
],
'REPEAT-UNTIL: jalan minimal sekali': [
  P('Minta pengguna memasukkan nilai 0–100. Ulangi permintaan selama nilainya di luar rentang.', 'REPEAT INPUT ... UNTIL nilai >= 0 AND nilai <= 100.',
    'DECLARE nilai : INTEGER\nREPEAT\n    OUTPUT "Masukkan nilai (0-100): "\n    INPUT nilai\nUNTIL nilai >= 0 AND nilai <= 100\nOUTPUT "Nilai diterima: ", nilai'),
  P('Jumlahkan angka yang dimasukkan sampai pengguna mengetik 0, lalu tampilkan totalnya.', 'Angka 0 ikut dijumlahkan tidak masalah karena tidak mengubah total.',
    'DECLARE x, total : INTEGER\ntotal ← 0\nREPEAT\n    INPUT x\n    total ← total + x\nUNTIL x = 0\nOUTPUT "Total: ", total', 'Masukan 5, 8, 2, 0 → Total: 15'),
],
'Loop bersarang': [
  P('Cetak segitiga angka 4 baris:<br>1<br>1 2<br>1 2 3<br>1 2 3 4', 'Loop luar i untuk baris, loop dalam j dari 1 sampai i.',
    'DECLARE i, j : INTEGER\nFOR i ← 1 TO 4 DO\n    FOR j ← 1 TO i DO\n        OUTPUT j, " "   // tanpa pindah baris\n    ENDFOR\n    OUTPUT ""           // pindah baris\nENDFOR', '1\n1 2\n1 2 3\n1 2 3 4'),
  P('Berapa kali baris OUTPUT dijalankan pada FOR i ← 1 TO 5 berisi FOR j ← 1 TO 3? Tuliskan juga pseudocode untuk menghitungnya.', 'Jumlah putaran loop bersarang = putaran luar × putaran dalam.',
    'DECLARE i, j, hitung : INTEGER\nhitung ← 0\nFOR i ← 1 TO 5 DO\n    FOR j ← 1 TO 3 DO\n        hitung ← hitung + 1\n    ENDFOR\nENDFOR\nOUTPUT hitung', '15'),
],
'Array: banyak nilai dalam satu nama': [
  P('Array suhu berisi 7 nilai seminggu: 31, 29, 33, 30, 28, 32, 34. Hitung rata-rata dan suhu terendah.', 'Satu FOR cukup: jumlahkan sambil membandingkan dengan min ← suhu[0].',
    'DECLARE suhu : ARRAY[0..6] OF INTEGER\nDECLARE i, total, minim : INTEGER\nsuhu ← [31, 29, 33, 30, 28, 32, 34]\ntotal ← 0\nminim ← suhu[0]\nFOR i ← 0 TO 6 DO\n    total ← total + suhu[i]\n    IF suhu[i] < minim THEN\n        minim ← suhu[i]\n    ENDIF\nENDFOR\nOUTPUT "Rata-rata: ", total / 7\nOUTPUT "Terendah: ", minim', 'Rata-rata: 31\nTerendah: 28'),
  P('Balik urutan isi array [1, 2, 3, 4, 5] menjadi [5, 4, 3, 2, 1] tanpa array baru.', 'Tukar a[i] dengan a[n-1-i] untuk i dari 0 sampai n DIV 2 - 1.',
    'DECLARE a : ARRAY[0..4] OF INTEGER\nDECLARE i, t, n : INTEGER\na ← [1, 2, 3, 4, 5]\nn ← 5\nFOR i ← 0 TO n DIV 2 - 1 DO\n    t ← a[i]\n    a[i] ← a[n - 1 - i]\n    a[n - 1 - i] ← t\nENDFOR\nOUTPUT a', '[5, 4, 3, 2, 1]'),
],
'Linear search: mencari satu per satu': [
  P('Hitung berapa kali angka 7 muncul di array [7, 3, 7, 1, 7, 9].', 'Jangan berhenti saat ketemu; teruskan sampai akhir sambil menghitung.',
    'DECLARE a : ARRAY[0..5] OF INTEGER\nDECLARE i, jumlah : INTEGER\na ← [7, 3, 7, 1, 7, 9]\njumlah ← 0\nFOR i ← 0 TO 5 DO\n    IF a[i] = 7 THEN\n        jumlah ← jumlah + 1\n    ENDIF\nENDFOR\nOUTPUT "Muncul ", jumlah, " kali"', 'Muncul 3 kali'),
  P('Cari posisi nama "Budi" di daftar nama dan berhenti begitu ketemu. Tampilkan -1 jika tidak ada.', 'WHILE dengan dua syarat: indeks masih di dalam array AND belum ketemu.',
    'DECLARE nama : ARRAY[0..3] OF STRING\nDECLARE i, posisi : INTEGER\nnama ← ["Andi", "Budi", "Citra", "Dewi"]\ni ← 0\nposisi ← -1\nWHILE i <= 3 AND posisi = -1 DO\n    IF nama[i] = "Budi" THEN\n        posisi ← i\n    ENDIF\n    i ← i + 1\nENDWHILE\nOUTPUT posisi', '1'),
],
'Bubble sort dalam pseudocode': [
  P('Ubah bubble sort agar mengurutkan dari terbesar ke terkecil.', 'Cukup balik tanda perbandingan: tukar jika a[j] < a[j + 1].',
    'FOR i ← 0 TO n - 2 DO\n    FOR j ← 0 TO n - 2 - i DO\n        IF a[j] < a[j + 1] THEN\n            t ← a[j]\n            a[j] ← a[j + 1]\n            a[j + 1] ← t\n        ENDIF\n    ENDFOR\nENDFOR', '[5, 1, 4, 2] → [5, 4, 2, 1]'),
  P('Tuliskan isi array [5, 1, 4, 2] setelah putaran luar pertama bubble sort menaik.', 'Bandingkan pasangan bersebelahan dari kiri: (5,1) tukar, (5,4) tukar, (5,2) tukar.',
    'Awal      : [5, 1, 4, 2]\nj = 0     : [1, 5, 4, 2]\nj = 1     : [1, 4, 5, 2]\nj = 2     : [1, 4, 2, 5]\nSetelah putaran 1, angka terbesar (5) sudah di ujung.'),
],
'Menerjemahkan pseudocode ke bahasa pemrograman': [
  S('Terjemahkan ke Python:<br><code>FOR i ← 1 TO 5 DO OUTPUT i * i ENDFOR</code>', 'FOR i ← 1 TO 5 menjadi range(1, 6) karena batas akhir range tidak ikut.',
    'for i in range(1, 6):\n    print(i * i)', '1\n4\n9\n16\n25', lang='python'),
  S('Terjemahkan ke Java: REPEAT INPUT pin UNTIL pin = "2468".', 'REPEAT-UNTIL menjadi do-while dengan kondisi dibalik.',
    'Scanner in = new Scanner(System.in);\nString pin;\ndo {\n    pin = in.nextLine();\n} while (!pin.equals("2468"));', lang='java'),
],
'Prosedur dan fungsi': [
  P('Buat FUNCTION Maks(a, b) yang mengembalikan nilai terbesar, lalu pakai untuk mencari terbesar dari tiga angka.', 'Maks(Maks(x, y), z).',
    'FUNCTION Maks(a : INTEGER, b : INTEGER) RETURNS INTEGER\n    IF a > b THEN\n        RETURN a\n    ELSE\n        RETURN b\n    ENDIF\nENDFUNCTION\n\nOUTPUT Maks(Maks(12, 45), 30)', '45'),
  P('Buat FUNCTION IsPrima(n) yang mengembalikan TRUE jika n bilangan prima.', 'Periksa pembagi dari 2 selama d * d <= n.',
    'FUNCTION IsPrima(n : INTEGER) RETURNS BOOLEAN\n    DECLARE d : INTEGER\n    IF n < 2 THEN\n        RETURN FALSE\n    ENDIF\n    d ← 2\n    WHILE d * d <= n DO\n        IF n MOD d = 0 THEN\n            RETURN FALSE\n        ENDIF\n        d ← d + 1\n    ENDWHILE\n    RETURN TRUE\nENDFUNCTION', 'IsPrima(29) → TRUE · IsPrima(21) → FALSE'),
],
'Proyek mini: kasir sederhana': [
  P('Tambahkan pajak 11% yang dihitung dari total setelah diskon.', 'pajak ← bayar * 0.11, lalu bayar ← bayar + pajak.',
    'bayar ← total - diskon\npajak ← bayar * 0.11\nbayar ← bayar + pajak\nOUTPUT "Pajak: ", pajak\nOUTPUT "Bayar: ", bayar'),
  P('Hitung kembalian. Jika uang pembeli kurang, minta masukan lagi.', 'REPEAT INPUT uang UNTIL uang >= bayar, lalu kembali ← uang - bayar.',
    'REPEAT\n    OUTPUT "Uang pembeli: "\n    INPUT uang\n    IF uang < bayar THEN\n        OUTPUT "Uang kurang ", bayar - uang\n    ENDIF\nUNTIL uang >= bayar\nOUTPUT "Kembalian: ", uang - bayar'),
],
}

FLOWG = {
'Flowchart dan Flowgorithm': [
  P('Sebutkan simbol flowchart yang dipakai untuk: menerima input, menghitung, memilih, dan menampilkan hasil.', 'Ingat bentuknya: jajaran genjang, persegi panjang, belah ketupat.',
    'Input  → jajaran genjang (Input)\nHitung → persegi panjang (Assign)\nPilih  → belah ketupat (If)\nTampil → jajaran genjang (Output)\nMulai/selesai → oval (Main / End)'),
  P('Gambarkan (dalam bentuk daftar simbol) flowchart untuk menghitung luas persegi panjang.', 'Urutannya: Main, Declare, Input, Input, Assign, Output, End.',
    'Main\n→ Declare panjang, lebar, luas : Integer\n→ Input panjang\n→ Input lebar\n→ Assign luas = panjang * lebar\n→ Output "Luas = " & luas\n→ End'),
],
'Memasang dan memakai Flowgorithm': [
  P('Program Flowgorithm-mu tidak mau jalan dan muncul pesan "variable not declared". Apa penyebab dan perbaikannya?', 'Flowgorithm mewajibkan setiap variabel dideklarasikan dulu.',
    'Penyebab: variabel dipakai (di Input atau Assign) sebelum ada simbol Declare.\nPerbaikan: tambahkan simbol Declare di awal program,\nisi nama variabel dan tipe datanya (Integer, Real, String, Boolean).'),
  P('Tuliskan langkah menyimpan program dan melihat versi kodenya dalam Python.', 'Menu File untuk menyimpan, Tools untuk Source Code Viewer.',
    '1. File → Save As, beri nama misalnya luas.fprg\n2. Tools → Source Code Viewer\n3. Pilih bahasa Python di daftar bahasa\n4. Salin kodenya jika ingin dijalankan di VS Code'),
],
'Tipe data, Declare, dan aturan ekspresi': [
  P('Tentukan tipe data yang tepat: umur, IPK, nama, sudah lulus.', 'Bilangan bulat, pecahan, teks, benar/salah.',
    'umur       : Integer\nipk        : Real\nnama       : String\nsudahLulus : Boolean'),
  P('Berapa hasil ekspresi Flowgorithm berikut: <code>7 / 2</code>, <code>7 % 2</code>, <code>"Nilai: " & 80</code>?', 'Operator / di Flowgorithm selalu memberi hasil pecahan, % adalah sisa bagi, dan & menyambung teks.',
    '7 / 2         → 3.5 (Flowgorithm memberi hasil pecahan)\n7 % 2         → 1   (sisa bagi)\n"Nilai: " & 80 → Nilai: 80'),
],
'Luas dan keliling lingkaran': [
  P('Buat flowchart menghitung luas dan keliling persegi panjang dari input panjang dan lebar.', 'Dua Assign: luas = p * l dan keliling = 2 * (p + l).',
    'Declare p, l, luas, keliling : Real\nInput p\nInput l\nAssign luas = p * l\nAssign keliling = 2 * (p + l)\nOutput "Luas = " & luas\nOutput "Keliling = " & keliling', 'p = 8, l = 5 → Luas = 40, Keliling = 26'),
  P('Konversi suhu Celsius ke Fahrenheit (F = C × 9 / 5 + 32).', 'Pakai tipe Real agar pecahan tidak hilang.',
    'Declare c, f : Real\nInput c\nAssign f = c * 9 / 5 + 32\nOutput c & " C = " & f & " F"', '30 C = 86 F'),
],
'Menghitung diskon belanja': [
  P('Hitung harga setelah diskon persen yang dimasukkan pengguna.', 'potongan = harga * persen / 100.',
    'Declare harga, persen, potongan, bayar : Real\nInput harga\nInput persen\nAssign potongan = harga * persen / 100\nAssign bayar = harga - potongan\nOutput "Bayar: " & bayar', 'harga 250000, persen 20 → Bayar: 200000'),
  P('Hitung total belanja 3 barang dengan jumlah berbeda (harga × qty), lalu tambahkan ongkir 10000.', 'Tiga pasang input harga dan qty, lalu satu Assign untuk total.',
    'Declare h1, h2, h3, q1, q2, q3, total : Integer\nInput h1\nInput q1\nInput h2\nInput q2\nInput h3\nInput q3\nAssign total = h1*q1 + h2*q2 + h3*q3 + 10000\nOutput "Total: " & total'),
],
'Simbol If: ganjil atau genap': [
  P('Buat flowchart yang memeriksa apakah sebuah angka habis dibagi 5.', 'If n % 5 == 0.',
    'Declare n : Integer\nInput n\nIf n % 5 == 0\n    True : Output n & " habis dibagi 5"\n    False: Output n & " tidak habis dibagi 5"', '35 habis dibagi 5'),
  P('Tampilkan angka yang lebih besar dari dua input, atau "sama" jika keduanya sama.', 'If bersarang: cek a == b dulu, lalu a > b.',
    'Declare a, b : Integer\nInput a\nInput b\nIf a == b\n    True : Output "sama"\n    False: If a > b\n               True : Output a\n               False: Output b'),
],
'If bersarang: nilai huruf': [
  P('Tentukan kategori BMI: < 18.5 kurus, < 25 normal, < 30 gemuk, selain itu obesitas. BMI = berat / (tinggi × tinggi), tinggi dalam meter.', 'Hitung BMI dulu dengan Assign, lalu If bersarang dari batas terkecil.',
    'Declare berat, tinggi, bmi : Real\nInput berat\nInput tinggi\nAssign bmi = berat / (tinggi * tinggi)\nIf bmi < 18.5 → Output "Kurus"\nElse If bmi < 25 → Output "Normal"\nElse If bmi < 30 → Output "Gemuk"\nElse → Output "Obesitas"', 'berat 60, tinggi 1.65 → BMI 22.04 → Normal'),
  P('Tarif listrik: pemakaian ≤ 100 kWh Rp1.000/kWh, di atas itu Rp1.500/kWh untuk kelebihannya. Hitung tagihan.', 'Jika lebih dari 100: 100 × 1000 + (kwh − 100) × 1500.',
    'Declare kwh, tagihan : Integer\nInput kwh\nIf kwh <= 100\n    True : Assign tagihan = kwh * 1000\n    False: Assign tagihan = 100 * 1000 + (kwh - 100) * 1500\nOutput "Tagihan: Rp" & tagihan', '150 kWh → Tagihan: Rp175000'),
],
'Simbol For: tabel perkalian dan hitung mundur': [
  P('Tampilkan semua bilangan ganjil dari 1 sampai 19 dengan For (step 2).', 'For i dari 1 sampai 19, langkah 2.',
    'Declare i : Integer\nFor i = 1 to 19 step 2\n    Output i', '1 3 5 7 9 11 13 15 17 19'),
  P('Hitung jumlah 1 + 2 + ... + n untuk n dari input.', 'Akumulator total = 0 sebelum For, total = total + i di dalamnya.',
    'Declare n, i, total : Integer\nInput n\nAssign total = 0\nFor i = 1 to n\n    Assign total = total + i\nOutput "Jumlah = " & total', 'n = 100 → Jumlah = 5050'),
],
'Deret Fibonacci dan faktorial': [
  P('Tampilkan 12 suku pertama Fibonacci dan jumlah semuanya.', 'Tiga variabel a, b, c; tambahkan a ke total di setiap putaran.',
    'Declare a, b, c, i, total : Integer\nAssign a = 0\nAssign b = 1\nAssign total = 0\nFor i = 1 to 12\n    Output a\n    Assign total = total + a\n    Assign c = a + b\n    Assign a = b\n    Assign b = c\nOutput "Jumlah = " & total', '0 1 1 2 3 5 8 13 21 34 55 89\nJumlah = 232'),
  P('Hitung pangkat a^b dengan perulangan (tanpa operator ^). Uji 2^10.', 'Mulai hasil = 1, kalikan dengan a sebanyak b kali.',
    'Declare a, b, i, hasil : Integer\nInput a\nInput b\nAssign hasil = 1\nFor i = 1 to b\n    Assign hasil = hasil * a\nOutput hasil', '1024'),
],
'Simbol While: tebak angka': [
  P('Hitung berapa kali sebuah angka bisa dibagi 2 sampai menjadi 1 (contoh 64 → 6 kali).', 'While n > 1: n = Int(n / 2), lalu hitung bertambah 1. Int() membuang bagian pecahan.',
    'Declare n, hitung : Integer\nInput n\nAssign hitung = 0\nWhile n > 1\n    Assign n = Int(n / 2)\n    Assign hitung = hitung + 1\nOutput hitung & " kali"', '64 → 6 kali'),
  P('Batasi tebak angka menjadi paling banyak 5 kesempatan.', 'Tambahkan syarat kesempatan < 5 pada kondisi While dengan and.',
    'Declare rahasia, tebakan, kesempatan : Integer\nAssign rahasia = Random(10) + 1\nAssign tebakan = 0\nAssign kesempatan = 0\nWhile tebakan != rahasia and kesempatan < 5\n    Input tebakan\n    Assign kesempatan = kesempatan + 1\nIf tebakan == rahasia\n    True : Output "Benar!"\n    False: Output "Kesempatan habis. Jawabannya " & rahasia'),
],
'Simbol Do: menu yang berulang': [
  P('Buat menu kalkulator: 1 Tambah, 2 Kurang, 0 Keluar, yang terus tampil sampai pengguna memilih 0.', 'Do ... loop while pilihan != 0; di dalamnya If untuk setiap pilihan.',
    'Declare pilih, a, b : Integer\nDo\n    Output "1 Tambah, 2 Kurang, 0 Keluar"\n    Input pilih\n    If pilih == 1 → Input a, Input b, Output a + b\n    If pilih == 2 → Input a, Input b, Output a - b\nLoop while pilih != 0\nOutput "Sampai jumpa"'),
  P('Minta PIN sampai benar (1234), lalu tampilkan berapa kali mencoba.', 'Do ... while pin != 1234, hitung percobaan di dalam loop.',
    'Declare pin, coba : Integer\nAssign coba = 0\nDo\n    Input pin\n    Assign coba = coba + 1\nLoop while pin != 1234\nOutput "Berhasil setelah " & coba & " kali"'),
],
'Array dengan input': [
  P('Masukkan 5 nilai ke array, lalu tampilkan berapa yang lulus (≥ 75).', 'Satu For untuk input, satu For untuk menghitung.',
    'Declare nilai : Integer array[5]\nDeclare i, lulus : Integer\nFor i = 0 to 4\n    Input nilai[i]\nAssign lulus = 0\nFor i = 0 to 4\n    If nilai[i] >= 75 → Assign lulus = lulus + 1\nOutput lulus & " mahasiswa lulus"', '80 60 90 75 50 → 3 mahasiswa lulus'),
  P('Tampilkan isi array dari belakang ke depan.', 'For i dari 4 turun ke 0 (step -1).',
    'For i = 4 to 0 step -1\n    Output nilai[i]'),
],
'Fungsi dan simbol Call': [
  P('Buat fungsi Luas(p, l) yang mengembalikan luas, lalu panggil dari Main untuk dua persegi panjang.', 'Fungsi punya Return Type Integer dan variabel return.',
    'Function Luas(Integer p, Integer l) → Integer hasil\n    Assign hasil = p * l\nEnd\n\nMain\n    Output "Luas A = " & Luas(4, 5)\n    Output "Luas B = " & Luas(7, 3)', 'Luas A = 20\nLuas B = 21'),
  P('Buat prosedur (tanpa return) CetakBintang(n) yang mencetak n bintang dalam satu baris, lalu Call untuk n = 1 sampai 3.', 'Return Type: None. Dipanggil dengan simbol Call.',
    'Function CetakBintang(Integer n) → None\n    Declare i : Integer\n    Declare s : String\n    Assign s = ""\n    For i = 1 to n\n        Assign s = s & "*"\n    Output s\nEnd\n\nMain\n    For k = 1 to 3\n        Call CetakBintang(k)', '*\n**\n***'),
],
'Proyek: kasir dengan diskon': [
  P('Tambahkan pilihan metode bayar: 1 tunai (tanpa biaya), 2 kartu (biaya 2%).', 'If pilihan == 2 maka bayar = bayar + bayar * 0.02.',
    'Input metode\nIf metode == 2\n    True: Assign bayar = bayar + bayar * 0.02\nOutput "Total bayar: " & bayar'),
  P('Hitung jumlah barang yang dibeli dan harga rata-rata per barang.', 'Tambahkan penghitung jumlahBarang di dalam loop input harga.',
    'Assign jumlahBarang = jumlahBarang + 1   // di dalam loop\n...\nOutput "Rata-rata harga: " & total / jumlahBarang'),
],
'Dari flowchart ke kode: Source Code Viewer': [
  S('Terjemahkan flowchart "jumlah 1 sampai n" ke Java sesuai hasil Source Code Viewer.', 'For di Flowgorithm menjadi for (i = 1; i <= n; i++).',
    'Scanner input = new Scanner(System.in);\nint n = input.nextInt();\nint total = 0;\nfor (int i = 1; i <= n; i++) {\n    total = total + i;\n}\nSystem.out.println("Jumlah = " + total);', lang='java'),
  S('Terjemahkan flowchart ganjil/genap ke Python.', 'If menjadi if/else, % tetap sama.',
    'n = int(input())\nif n % 2 == 0:\n    print(n, "genap")\nelse:\n    print(n, "ganjil")', lang='python'),
],
}

GIT = {
'Apa itu version control & Git?': [
  B('Tulis perintah untuk memeriksa versi Git dan mengatur nama serta email sekali untuk semua repositori.', 'git --version, lalu git config --global.',
    'git --version\ngit config --global user.name "Rina Siregar"\ngit config --global user.email "rina@mail.com"\ngit config --global init.defaultBranch main\ngit config --list'),
  B('Kamu punya file laporan_final.docx, laporan_final2.docx, laporan_final_fix.docx. Jelaskan dengan perintah Git bagaimana version control menyelesaikan masalah ini.', 'Satu file, banyak commit; riwayat dilihat dengan git log.',
    '# cukup satu file: laporan.md\ngit add laporan.md\ngit commit -m "Draf bab 1"\n# ... ubah lagi ...\ngit commit -am "Perbaiki bab 1 sesuai masukan dosen"\n# lihat semua versi\ngit log --oneline\n# kembali melihat versi lama\ngit show HEAD~1:laporan.md'),
],
'Membaca status repositori': [
  B('Setelah mengubah index.html dan membuat file baru gaya.css, apa yang ditampilkan git status, dan bagaimana membuat keduanya siap di-commit?', 'File baru = untracked, file lama yang diubah = modified.',
    'git status\n# Changes not staged: modified: index.html\n# Untracked files: gaya.css\ngit add index.html gaya.css\ngit status\n# Changes to be committed: modified index.html, new file gaya.css'),
  B('Tampilkan status dalam format ringkas dan jelaskan arti kode M, A, dan ??.', 'git status -s.',
    'git status -s\n#  M index.html   diubah, belum di-stage\n# A  gaya.css     file baru, sudah di-stage\n# ?? catatan.txt  belum dilacak Git'),
],
'init, add, commit': [
  B('Buat repositori baru bernama portofolio, tambahkan README.md, lalu buat commit pertama.', 'mkdir, cd, git init, buat file, add, commit.',
    'mkdir portofolio && cd portofolio\ngit init\necho "# Portofolio Rina" > README.md\ngit add README.md\ngit commit -m "Tambah README"\ngit log --oneline'),
  B('Kamu salah menulis pesan commit terakhir (belum di-push). Perbaiki pesannya.', 'git commit --amend.',
    'git commit --amend -m "Tambah halaman kontak"'),
],
'Riwayat & perbedaan: log dan diff': [
  B('Tampilkan 5 commit terakhir dalam satu baris per commit beserta grafik cabangnya.', 'git log dengan --oneline, --graph, dan -n.',
    'git log --oneline --graph --all -n 5'),
  B('Lihat perubahan yang sudah di-stage (akan masuk commit) dan yang belum.', 'git diff untuk yang belum, git diff --staged untuk yang sudah.',
    'git diff            # perubahan belum di-stage\ngit diff --staged   # perubahan yang akan di-commit\ngit diff HEAD~1 -- index.html   # dibanding commit sebelumnya'),
],
'.gitignore': [
  B('Tulis .gitignore untuk proyek Node.js yang mengabaikan node_modules, file .env, folder dist, dan file log.', 'Satu pola per baris; folder diakhiri garis miring.',
    'node_modules/\ndist/\n.env\n*.log\n.DS_Store'),
  B('File .env sudah terlanjur di-commit. Hentikan pelacakannya tanpa menghapus file di laptopmu.', 'git rm --cached, lalu tambahkan ke .gitignore. Ganti juga semua rahasia di dalamnya karena sudah tersimpan di riwayat.',
    'echo ".env" >> .gitignore\ngit rm --cached .env\ngit commit -m "Berhenti melacak .env"\n# penting: ganti password/API key yang ada di .env'),
],
'Membatalkan perubahan': [
  B('Kamu mengubah index.html tapi ingin kembali ke versi commit terakhir.', 'git restore nama_file (perubahan yang belum di-commit akan hilang).',
    'git restore index.html'),
  B('Commit terakhir sudah di-push dan ternyata salah. Batalkan dengan aman tanpa menulis ulang riwayat.', 'git revert membuat commit baru yang membalik perubahan.',
    'git revert HEAD\ngit push'),
  B('Kamu tidak sengaja git add file besar video.mp4. Keluarkan dari staging.', 'git restore --staged.',
    'git restore --staged video.mp4'),
],
'Branch & merge': [
  B('Buat cabang fitur-kontak, pindah ke sana, commit perubahan, lalu gabungkan ke main.', 'git switch -c, commit, kembali ke main, git merge.',
    'git switch -c fitur-kontak\n# ... edit kontak.html ...\ngit add kontak.html\ngit commit -m "Tambah halaman kontak"\ngit switch main\ngit merge fitur-kontak\ngit branch -d fitur-kontak'),
  B('Tampilkan semua cabang lokal dan remote, serta cabang mana yang sudah digabung ke main.', 'git branch -a dan git branch --merged.',
    'git branch -a\ngit branch --merged main'),
],
'Menyelesaikan konflik merge': [
  B('Tuliskan isi file setelah konflik diselesaikan dengan memakai kedua perubahan:<br><code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD<br>Harga: 15000<br>=======<br>Harga: 18000<br>&gt;&gt;&gt;&gt;&gt;&gt;&gt; fitur-harga</code>', 'Hapus semua penanda konflik, putuskan isi akhirnya, lalu add dan commit.',
    '# isi akhir file (penanda konflik dihapus)\nHarga normal: 15000\nHarga promo: 18000\n\n# lalu\ngit add harga.txt\ngit commit -m "Selesaikan konflik harga"'),
  B('Konfliknya terlalu rumit dan kamu ingin membatalkan merge.', 'git merge --abort mengembalikan keadaan sebelum merge.',
    'git merge --abort\ngit status'),
],
'Stash & rebase': [
  B('Kamu sedang mengedit di cabang fitur, lalu harus memperbaiki bug di main sekarang. Simpan pekerjaan sementara dan kembalikan setelahnya.', 'git stash, pindah cabang, kembali, git stash pop.',
    'git stash push -m "setengah jadi: form kontak"\ngit switch main\n# ... perbaiki bug, commit ...\ngit switch fitur\ngit stash pop'),
  B('Perbarui cabang fitur dengan commit terbaru dari main memakai rebase.', 'git fetch, lalu git rebase origin/main. Jangan rebase cabang yang sudah dipakai orang lain.',
    'git switch fitur\ngit fetch origin\ngit rebase origin/main\n# jika ada konflik: perbaiki, git add, git rebase --continue\ngit push --force-with-lease'),
],
'Remote, push & pull': [
  B('Hubungkan repositori lokal ke GitHub dan push cabang main untuk pertama kali.', 'git remote add origin, lalu git push -u.',
    'git remote add origin https://github.com/rina/portofolio.git\ngit branch -M main\ngit push -u origin main'),
  B('Push ditolak dengan pesan "Updates were rejected because the remote contains work that you do not have". Apa yang harus dilakukan?', 'Ambil dulu perubahan dari remote dengan pull, selesaikan konflik jika ada, lalu push lagi.',
    'git pull --rebase origin main\n# selesaikan konflik jika ada\ngit push'),
],
'Fork & pull request': [
  B('Tulis alur lengkap berkontribusi ke proyek orang lain lewat fork.', 'Fork di GitHub, clone fork-mu, tambah upstream, buat cabang, push, buka PR.',
    '# 1. klik Fork di GitHub\ngit clone https://github.com/rina/proyek.git\ncd proyek\ngit remote add upstream https://github.com/pemilik/proyek.git\ngit switch -c perbaiki-typo\n# ... edit ...\ngit commit -am "Perbaiki salah ketik di README"\ngit push -u origin perbaiki-typo\n# 2. buka Pull Request dari GitHub'),
  B('Sinkronkan fork-mu dengan proyek asli (upstream) yang sudah maju.', 'fetch upstream, merge ke main, push ke fork.',
    'git switch main\ngit fetch upstream\ngit merge upstream/main\ngit push origin main'),
],
'Issue, label & project board': [
  B('Tulis isi issue laporan bug yang baik untuk tombol "Simpan" yang tidak berfungsi di Safari.', 'Judul spesifik, langkah reproduksi, hasil yang diharapkan vs yang terjadi, lingkungan.',
    'Judul: Tombol "Simpan" di halaman profil tidak merespons di Safari 17\n\nLangkah:\n1. Buka /profil di Safari 17 (macOS 14)\n2. Ubah nama\n3. Klik "Simpan"\n\nDiharapkan: muncul pesan "Profil tersimpan"\nYang terjadi: tidak ada respons, konsol menampilkan TypeError\n\nLabel: bug, prioritas-tinggi'),
  B('Tulis pesan commit yang otomatis menutup issue #42 saat PR digabung.', 'Kata kunci closes, fixes, atau resolves diikuti nomor issue.',
    'git commit -m "Perbaiki tombol simpan di Safari (fixes #42)"'),
],
'README & Markdown': [
  S('Tulis README singkat untuk proyek "Toko Kopi": judul, deskripsi, cara menjalankan, dan lisensi.', 'Pakai #, ##, daftar, dan blok kode.',
    '# Toko Kopi\n\nAplikasi katalog kopi Nusantara.\n\n## Fitur\n- Daftar produk\n- Keranjang belanja\n\n## Cara menjalankan\n```bash\nnpm install\nnpm run dev\n```\n\n## Lisensi\nMIT', lang='markdown'),
  S('Tulis tabel Markdown berisi tiga bahasa pemrograman dan kegunaannya.', 'Baris kedua berisi --- sebagai pemisah kepala tabel.',
    '| Bahasa | Kegunaan |\n|---|---|\n| Python | Data dan otomasi |\n| Kotlin | Aplikasi Android |\n| Dart | Aplikasi Flutter |', lang='markdown'),
],
'GitHub Pages & Actions': [
  S('Tulis workflow GitHub Actions yang menjalankan npm test setiap ada push dan pull request.', 'File di .github/workflows/test.yml; on: [push, pull_request].',
    'name: Tes\non: [push, pull_request]\njobs:\n  tes:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-node@v4\n        with:\n          node-version: 20\n      - run: npm ci\n      - run: npm test', lang='yaml'),
  B('Sebutkan langkah mengaktifkan GitHub Pages untuk repositori portofolio statis.', 'Settings → Pages → pilih branch main dan folder root.',
    '# di GitHub: Settings → Pages\n# Source: Deploy from a branch\n# Branch: main, folder: / (root) → Save\n# situs tayang di https://<username>.github.io/portofolio/'),
],
'Keamanan & aturan cabang': [
  B('Kamu tidak sengaja push API key ke GitHub. Apa langkah yang benar?', 'Hapus dari kode saja tidak cukup karena masih ada di riwayat. Cabut kuncinya dulu.',
    '# 1. Cabut (revoke) API key di dasbor penyedia, buat kunci baru\n# 2. Pindahkan kunci ke .env dan masukkan .env ke .gitignore\ngit rm --cached .env\ngit commit -m "Pindahkan rahasia ke .env"\n# 3. Simpan kunci untuk CI di Settings → Secrets and variables → Actions\n# 4. Aktifkan Secret scanning dan Push protection'),
  B('Atur agar cabang main tidak bisa di-push langsung dan setiap PR butuh 1 persetujuan serta tes yang lulus.', 'Settings → Branches (atau Rules → Rulesets).',
    '# Settings → Rules → Rulesets → New branch ruleset\n# Target: main\n# Centang: Restrict deletions, Block force pushes\n# Require a pull request before merging (1 approval)\n# Require status checks to pass: "Tes"'),
],
}

SOAL = {'PSEUDO_MODULES': PSEUDO, 'FLOWG_MODULES': FLOWG, 'GIT_MODULES': GIT}
