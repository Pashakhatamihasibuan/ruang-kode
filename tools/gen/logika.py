"""Membuat src/js/track-logika.js: jalur Pseudocode dan Flowgorithm.
Setiap program fc dijalankan oleh simulator di viz-fc.js (flowchart + pseudocode + variabel).
Jalankan: python3 tools/gen/logika.py"""
import json, pathlib

def D(v, ty, arr=None):
    d = {'t': 'dec', 'v': v, 'ty': ty}
    if arr: d['arr'] = str(arr)
    return d
def I(v): return {'t': 'in', 'v': v}
def A(v, e): return {'t': 'asg', 'v': v, 'e': e}
def O(e): return {'t': 'out', 'e': e}
def IF(c, y, n=None): return {'t': 'if', 'c': c, 'y': y, 'n': n or []}
def W(c, b): return {'t': 'while', 'c': c, 'b': b}
def F(v, a, z, b, s=None):
    d = {'t': 'for', 'v': v, 'a': a, 'z': z, 'b': b}
    if s: d['s'] = s
    return d
def DO(c, b, u): return {'t': 'do', 'c': c, 'b': b, 'u': u}
def fc(name, p, inp=None):
    d = {'name': name, 'p': p}
    if inp: d['in'] = inp
    return d
def L(t, b, fcp=None, tb=None, pts=None, q=None, nodes=None, **kw):
    d = {'k': 'c', 't': t, 'nodes': nodes or [], 'lang': 'text', 'b': b}
    if fcp: d['viz'] = 'fc'; d['fc'] = fcp
    if tb: d['tb'] = tb
    if pts: d['pts'] = pts
    if q: d['q'] = q
    d.update(kw)
    return d

# ---------- program contoh (dipakai bersama) ----------
P_LUAS = fc('LuasPersegiPanjang', [D('panjang, lebar, luas', 'Integer'), I('panjang'), I('lebar'), A('luas', 'panjang * lebar'), O('"Luas = " & luas')], ['8', '5'])
P_RATA = fc('RataRataTiga', [D('a, b, c', 'Integer'), D('rata', 'Real'), I('a'), I('b'), I('c'), A('rata', '(a + b + c) / 3'), O('"Rata-rata: " & rata')], ['80', '75', '90'])
P_SUHU = fc('KonversiSuhu', [D('celcius, fahrenheit', 'Real'), I('celcius'), A('fahrenheit', 'celcius * 9 / 5 + 32'), O('celcius & " C = " & fahrenheit & " F"')], ['37'])
P_LULUS = fc('CekKelulusan', [D('nilai', 'Integer'), I('nilai'), IF('nilai >= 75', [O('"Lulus"')], [O('"Belum lulus, ikut remedial"')])], ['68'])
P_HURUF = fc('NilaiHuruf', [D('nilai', 'Integer'), D('huruf', 'String'), I('nilai'),
    IF('nilai >= 85', [A('huruf', '"A"')], [IF('nilai >= 70', [A('huruf', '"B"')], [IF('nilai >= 55', [A('huruf', '"C"')], [A('huruf', '"D"')])])]),
    O('"Nilai huruf: " & huruf')], ['78'])
P_KABISAT = fc('TahunKabisat', [D('tahun', 'Integer'), D('kabisat', 'Boolean'), I('tahun'),
    A('kabisat', '(tahun mod 4 = 0 and tahun mod 100 <> 0) or tahun mod 400 = 0'),
    IF('kabisat', [O('tahun & " adalah tahun kabisat"')], [O('tahun & " bukan tahun kabisat"')])], ['2024'])
P_JUMLAH = fc('Jumlah1SampaiN', [D('n, i, total', 'Integer'), I('n'), A('total', '0'), F('i', '1', 'n', [A('total', 'total + i')]), O('"Jumlah 1 sampai " & n & " = " & total')], ['5'])
P_TABUNG = fc('TargetTabungan', [D('saldo, minggu', 'Integer'), A('saldo', '0'), A('minggu', '0'), W('saldo < 100000', [A('saldo', 'saldo + 30000'), A('minggu', 'minggu + 1')]), O('"Tercapai di minggu ke-" & minggu & ", saldo " & saldo')])
P_PIN = fc('ValidasiPIN', [D('pin', 'String'), D('coba', 'Integer'), A('coba', '0'),
    DO('pin <> "2468"', [I('pin'), A('coba', 'coba + 1'), IF('pin <> "2468"', [O('"PIN salah"')])], 'pin = "2468"'), O('"PIN benar setelah " & coba & " kali"')], ['1111', '1234', '2468'])
P_SEGI = fc('SegitigaBintang', [D('n, i, j', 'Integer'), D('baris', 'String'), I('n'),
    F('i', '1', 'n', [A('baris', '""'), F('j', '1', 'i', [A('baris', 'baris & "*"')]), O('baris')])], ['4'])
P_ARR = fc('NilaiTertinggi', [D('nilai', 'Integer', 5), D('i, maks, total', 'Integer'), D('rata', 'Real'),
    F('i', '0', '4', [I('nilai[i]')]), A('maks', 'nilai[0]'), A('total', '0'),
    F('i', '0', '4', [A('total', 'total + nilai[i]'), IF('nilai[i] > maks', [A('maks', 'nilai[i]')])]),
    A('rata', 'total / 5'), O('"Tertinggi: " & maks'), O('"Rata-rata: " & rata')], ['70', '85', '62', '91', '78'])
P_LINEAR = fc('LinearSearch', [D('data', 'Integer', 6), A('data', '[12, 7, 30, 18, 25, 9]'), D('cari, i, posisi', 'Integer'), I('cari'), A('posisi', '-1'), A('i', '0'),
    W('i < 6 and posisi = -1', [IF('data[i] = cari', [A('posisi', 'i')]), A('i', 'i + 1')]),
    IF('posisi = -1', [O('cari & " tidak ditemukan"')], [O('cari & " ada di indeks " & posisi')])], ['18'])
P_BUBBLE = fc('BubbleSort', [D('a', 'Integer', 5), A('a', '[29, 10, 14, 37, 13]'), D('i, j, t', 'Integer'),
    F('i', '0', '3', [F('j', '0', '3 - i', [IF('a[j] > a[j + 1]', [A('t', 'a[j]'), A('a[j]', 'a[j + 1]'), A('a[j + 1]', 't')])])]), O('"Terurut: " & a')])
P_KASIR = fc('KasirSederhana', [D('harga, jumlah, total, bayar, kembali', 'Integer'), A('total', '0'),
    DO('harga > 0', [I('harga'), IF('harga > 0', [I('jumlah'), A('total', 'total + harga * jumlah')])], 'harga = 0'),
    IF('total > 100000', [A('total', 'total - Int(total * 10 / 100)'), O('"Diskon 10% diberikan"')]),
    O('"Total: " & total'), I('bayar'),
    IF('bayar >= total', [A('kembali', 'bayar - total'), O('"Kembalian: " & kembali')], [O('"Uang kurang " & (total - bayar)')])],
    ['25000', '2', '18000', '3', '0', '150000'])
P_HELLO = fc('HaloDunia', [O('"Halo, Ruang Kode!"')])
P_LINGKAR = fc('LuasLingkaran', [D('r, luas, keliling', 'Real'), I('r'), A('luas', '3.14159 * r * r'), A('keliling', '2 * 3.14159 * r'), O('"Luas: " & luas'), O('"Keliling: " & keliling')], ['7'])
P_DISKON = fc('HitungDiskon', [D('harga, persen, potongan, bayar', 'Real'), I('harga'), I('persen'), A('potongan', 'harga * persen / 100'), A('bayar', 'harga - potongan'),
    O('"Potongan: " & potongan'), O('"Harus dibayar: " & bayar')], ['250000', '15'])
P_GANJIL = fc('GanjilGenap', [D('x', 'Integer'), I('x'), IF('x mod 2 = 0', [O('x & " genap"')], [O('x & " ganjil"')])], ['17'])
P_KALI = fc('TabelPerkalian', [D('n, i', 'Integer'), I('n'), F('i', '1', '5', [O('n & " x " & i & " = " & n * i')])], ['7'])
P_TEBAK = fc('TebakAngka', [D('rahasia, tebakan, kali', 'Integer'), A('rahasia', '42'), A('kali', '0'), A('tebakan', '0'),
    W('tebakan <> rahasia', [I('tebakan'), A('kali', 'kali + 1'), IF('tebakan < rahasia', [O('"Terlalu kecil"')], [IF('tebakan > rahasia', [O('"Terlalu besar"')], [O('"Benar!"')])])]),
    O('"Ditebak dalam " & kali & " kali"')], ['50', '30', '42'])
P_MENU = fc('MenuKasir', [D('pilih, saldo', 'Integer'), A('saldo', '50000'),
    DO('pilih <> 0', [O('"1 Cek saldo  2 Isi 10000  0 Keluar"'), I('pilih'),
        IF('pilih = 1', [O('"Saldo: " & saldo')], [IF('pilih = 2', [A('saldo', 'saldo + 10000'), O('"Saldo bertambah"')])])], 'pilih = 0'), O('"Terima kasih"')], ['1', '2', '1', '0'])
P_FIB = fc('Fibonacci', [D('n, i, a, b, c', 'Integer'), I('n'), A('a', '0'), A('b', '1'), F('i', '1', 'n', [O('a'), A('c', 'a + b'), A('a', 'b'), A('b', 'c')])], ['8'])
P_FAKT = fc('Faktorial', [D('n, i, hasil', 'Integer'), I('n'), A('hasil', '1'), F('i', '2', 'n', [A('hasil', 'hasil * i')]), O('n & "! = " & hasil')], ['5'])
P_MUNDUR = fc('HitungMundur', [D('i', 'Integer'), F('i', '5', '1', [O('i')], '-1'), O('"Meluncur!"')])

def quiz(*q): return list(q)

PSEUDO = [
{'t': 'Berpikir algoritma', 'lvl': 'Pemula', 'd': 'Apa itu algoritma dan pseudocode, aturan menulis, variabel, tipe data, dan operator.', 'nodes': ['Algoritma', 'Pseudocode'], 'lessons': [
 L('Algoritma dan pseudocode', [
   '<b>Algoritma</b> adalah urutan langkah yang jelas dan terbatas untuk menyelesaikan masalah. Resep masakan, petunjuk arah ke kampus, dan cara menghitung nilai rapor adalah algoritma. Komputer hanya bisa menjalankan algoritma yang ditulis sangat jelas, tanpa langkah yang ambigu.',
   'Algoritma yang baik punya lima ciri: ada <b>input</b> (data yang diterima), ada <b>output</b> (hasil), setiap langkah <b>jelas</b> (tidak bisa ditafsirkan ganda), <b>berhenti</b> setelah jumlah langkah terbatas, dan <b>efektif</b> (setiap langkah benar-benar bisa dikerjakan).',
   '<b>Pseudocode</b> adalah cara menulis algoritma dengan bahasa yang mirip kode program, tetapi tidak terikat aturan bahasa tertentu. Tujuannya: memikirkan <b>logika</b> dulu sebelum memikirkan titik koma, kurung kurawal, atau aturan Java dan Python. Pseudocode yang baik bisa diterjemahkan ke bahasa apa pun.',
   'Visual di bawah menunjukkan satu algoritma dalam dua bentuk: <b>flowchart</b> (gambar) dan <b>pseudocode</b> (teks). Tekan Berikutnya dan perhatikan baris yang aktif di keduanya berjalan bersamaan. Ganti inputnya, lalu jalankan lagi.'],
   P_LUAS,
   tb=[{'c': 'Tiga cara menyajikan algoritma', 'h': ['Bentuk', 'Kelebihan', 'Kekurangan'], 'r': [
     ['Kalimat biasa', 'Mudah dipahami siapa saja', 'Sering ambigu dan panjang'],
     ['Flowchart', 'Alur dan percabangan terlihat jelas', 'Repot digambar untuk program besar'],
     ['Pseudocode', 'Ringkas, dekat ke kode program', 'Perlu belajar kata kunci dasar']]}],
   pts=['Algoritma: langkah jelas, terbatas, untuk menyelesaikan masalah.', 'Ciri: input, output, jelas, berhenti, efektif.', 'Pseudocode memisahkan logika dari aturan bahasa pemrograman.'],
   q=quiz(['Mana yang BUKAN ciri algoritma yang baik?', ['Berhenti setelah langkah terbatas', 'Langkahnya boleh ditafsirkan berbeda', 'Punya output'], 1, 'Setiap langkah harus jelas dan tidak ambigu.'],
          ['Apa tujuan utama menulis pseudocode?', ['Agar program lebih cepat', 'Memikirkan logika tanpa terikat aturan bahasa', 'Menggantikan bahasa pemrograman'], 1, 'Logika dulu, sintaks belakangan.'])),
 L('Aturan menulis pseudocode', [
   'Tidak ada satu standar resmi, tetapi buku dan kampus di Indonesia memakai kata kunci yang mirip. Di Ruang Kode kita memakai kata kunci berhuruf besar: <code>DECLARE</code>, <code>INPUT</code>, <code>OUTPUT</code>, <code>IF</code>, <code>WHILE</code>, <code>FOR</code>, dan tanda panah <code>←</code> untuk mengisi nilai ke variabel.',
   'Tiga aturan penting. Pertama, <b>satu baris satu langkah</b>. Kedua, <b>indentasi</b> (menjorok ke dalam) menunjukkan langkah mana yang ada di dalam IF atau loop. Ketiga, setiap blok ditutup dengan pasangannya: <code>IF</code> dengan <code>ENDIF</code>, <code>WHILE</code> dengan <code>ENDWHILE</code>.',
   'Kenapa memakai <code>←</code> dan bukan <code>=</code>? Karena <code>total ← total + 5</code> berarti "hitung total + 5, lalu simpan ke total". Ini <b>perintah</b>, bukan persamaan matematika. Tanda <code>=</code> kita pakai untuk <b>membandingkan</b>, misalnya <code>IF nilai = 100</code>.',
   'Di kampus, kamu mungkin melihat versi berbahasa Indonesia (<code>BACA</code>, <code>TULIS</code>, <code>JIKA ... MAKA</code>). Artinya sama persis; tabel di bawah memetakan keduanya.'],
   P_RATA,
   tb=[{'c': 'Kata kunci pseudocode', 'h': ['Kata kunci', 'Versi Indonesia', 'Arti'], 'r': [
     ['DECLARE x : INTEGER', 'DEKLARASI x : integer', 'Menyiapkan variabel'], ['INPUT x', 'BACA(x)', 'Menerima data dari pengguna'],
     ['OUTPUT x', 'TULIS(x)', 'Menampilkan hasil'], ['x ← 5', 'x ← 5', 'Mengisi nilai ke variabel'],
     ['IF ... THEN ... ELSE ... ENDIF', 'JIKA ... MAKA ... SELAIN ITU ... AKHIR JIKA', 'Percabangan'],
     ['WHILE ... DO ... ENDWHILE', 'SELAMA ... LAKUKAN ... AKHIR SELAMA', 'Ulangi selama kondisi benar'],
     ['FOR i ← 1 TO n DO ... ENDFOR', 'UNTUK i ← 1 SAMPAI n LAKUKAN ...', 'Ulangi sebanyak n kali'],
     ['REPEAT ... UNTIL kondisi', 'ULANGI ... SAMPAI kondisi', 'Ulangi sampai kondisi benar']]}],
   pts=['Satu baris satu langkah, indentasi menunjukkan blok.', '← mengisi nilai, = membandingkan.', 'Setiap blok punya penutup (ENDIF, ENDWHILE, ENDFOR).'],
   q=quiz(['Apa arti baris skor ← skor + 10?', ['skor sama dengan skor + 10', 'Hitung skor + 10 lalu simpan ke skor', 'Bandingkan skor dengan 10'], 1, '← adalah perintah mengisi nilai.'],
          ['Penutup yang benar untuk WHILE adalah?', ['END', 'ENDWHILE', 'STOP'], 1, 'Setiap blok ditutup dengan pasangannya.'])),
 L('Variabel, tipe data, dan operator', [
   '<b>Variabel</b> adalah kotak bernama untuk menyimpan nilai. Sebelum dipakai, variabel dideklarasikan beserta <b>tipe</b>-nya, agar jelas jenis isi yang boleh masuk. Tipe dasar: <code>INTEGER</code> (bilangan bulat), <code>REAL</code> (bilangan pecahan), <code>STRING</code> (teks), <code>BOOLEAN</code> (benar/salah), dan <code>CHAR</code> (satu huruf).',
   '<b>Operator aritmetika</b>: <code>+ - * /</code>, ditambah <code>mod</code> (sisa bagi, 17 mod 5 = 2) dan <code>div</code> atau <code>Int(a / b)</code> (hasil bagi bulat, 17 div 5 = 3). <b>Operator perbandingan</b>: <code>= &lt;&gt; &lt; &gt; &lt;= &gt;=</code>, hasilnya selalu benar atau salah. <b>Operator logika</b>: <code>and</code>, <code>or</code>, <code>not</code>.',
   'Urutan hitung mengikuti matematika: kurung dulu, lalu kali-bagi, lalu tambah-kurang. <code>celcius * 9 / 5 + 32</code> dihitung dari kiri: kali 9, bagi 5, baru tambah 32. Saat ragu, pakai kurung agar pembaca tidak salah tafsir.',
   'Contoh visual mengubah suhu Celcius ke Fahrenheit dengan tipe <code>REAL</code>, karena hasilnya bisa pecahan. Coba input 100 atau -40.'],
   P_SUHU,
   tb=[{'c': 'Tipe data dasar', 'h': ['Tipe', 'Isi', 'Contoh'], 'r': [['INTEGER', 'Bilangan bulat', 'umur ← 19'], ['REAL', 'Bilangan pecahan', 'ipk ← 3.45'], ['STRING', 'Teks', 'nama ← "Rina"'], ['BOOLEAN', 'Benar atau salah', 'lulus ← true'], ['CHAR', 'Satu karakter', 'grade ← \'A\'']]},
       {'c': 'Operator', 'h': ['Operator', 'Arti', 'Contoh dan hasil'], 'r': [['mod', 'Sisa bagi', '17 mod 5 = 2'], ['div / Int(a / b)', 'Hasil bagi bulat', '17 div 5 = 3'], ['=', 'Sama dengan', '5 = 5 → benar'], ['<>', 'Tidak sama dengan', '5 <> 3 → benar'], ['and', 'Keduanya benar', 'benar and salah → salah'], ['or', 'Salah satu benar', 'benar or salah → benar'], ['not', 'Kebalikan', 'not benar → salah']]}],
   pts=['Deklarasikan variabel dengan tipenya.', 'mod = sisa bagi, div = hasil bagi bulat.', 'Kurung membuat urutan hitung jelas.'],
   q=quiz(['Berapa 23 mod 4?', ['5', '3', '5.75'], 1, '23 = 4 × 5 + 3, sisanya 3.'], ['Tipe yang tepat untuk menyimpan IPK 3.75?', ['INTEGER', 'REAL', 'BOOLEAN'], 1, 'IPK berupa bilangan pecahan.'],
          ['Hasil (5 > 3) and (2 > 4)?', ['benar', 'salah'], 1, 'and butuh keduanya benar; 2 > 4 salah.'])),
]},
{'t': 'Percabangan', 'lvl': 'Pemula', 'd': 'IF, IF-ELSE, percabangan bertingkat, dan operator logika.', 'nodes': ['Percabangan'], 'lessons': [
 L('IF dan ELSE', [
   'Program sering harus <b>memilih</b>: lulus atau remedial, stok cukup atau habis, password benar atau salah. Pilihan ini ditulis dengan <code>IF kondisi THEN ... ELSE ... ENDIF</code>. Kondisi adalah ekspresi yang hasilnya benar atau salah.',
   'Jika kondisi benar, langkah di bawah <code>THEN</code> dijalankan. Jika salah, langkah di bawah <code>ELSE</code> yang dijalankan. Hanya <b>satu</b> jalur yang dipilih, tidak pernah keduanya. Bagian <code>ELSE</code> boleh tidak ada jika tidak ada yang perlu dilakukan saat kondisi salah.',
   'Di flowchart, percabangan digambar sebagai <b>belah ketupat</b> dengan dua jalur keluar: Benar dan Salah. Kedua jalur bertemu lagi di satu titik sebelum program berlanjut.',
   'Coba jalankan visual dengan nilai 68, lalu ganti menjadi 75. Perhatikan jalur mana yang dilewati. Nilai 75 adalah <b>kasus batas</b>: selalu uji nilai tepat di batas kondisi, karena di situlah kesalahan <code>&gt;</code> versus <code>&gt;=</code> sering terjadi.'],
   P_LULUS, pts=['IF memilih satu dari dua jalur.', 'ELSE opsional.', 'Selalu uji nilai tepat di batas kondisi.'],
   q=quiz(['Jika kondisinya nilai > 75 dan nilai = 75, hasilnya?', ['Masuk jalur Benar', 'Masuk jalur Salah'], 1, '75 > 75 salah. Jika 75 harus lulus, pakai >=.'],
          ['Simbol flowchart untuk percabangan?', ['Persegi panjang', 'Belah ketupat', 'Jajar genjang'], 1, 'Belah ketupat punya dua jalur keluar.'])),
 L('Percabangan bertingkat', [
   'Jika pilihannya lebih dari dua, misalnya nilai huruf A, B, C, D, kita menaruh IF di dalam ELSE. Ini disebut <b>percabangan bertingkat</b> (nested IF). Kondisi dicek dari atas ke bawah, dan begitu satu kondisi benar, sisanya tidak dicek lagi.',
   'Urutan kondisi sangat penting. Jika kita mengecek <code>nilai &gt;= 55</code> lebih dulu, nilai 90 akan mendapat C, karena 90 juga ≥ 55. Aturannya: <b>mulai dari kondisi paling ketat</b> (nilai tertinggi) ke yang paling longgar.',
   'Banyak bahasa punya <code>CASE</code> atau <code>switch</code> untuk memilih berdasarkan satu nilai tepat, misalnya kode menu 1, 2, 3. Untuk rentang nilai seperti 70 sampai 84, IF bertingkat lebih cocok.',
   'Uji visual dengan 85, 84, 70, 55, dan 40. Kelima angka itu mencakup setiap jalur dan setiap batas.'],
   P_HURUF,
   tb=[{'c': 'Kasus uji nilai huruf', 'h': ['Input', 'Jalur yang dilewati', 'Hasil'], 'r': [['85', 'nilai >= 85 benar', 'A'], ['84', '>= 85 salah, >= 70 benar', 'B'], ['55', '>= 85, >= 70 salah, >= 55 benar', 'C'], ['40', 'semua salah', 'D']]}],
   pts=['IF bertingkat untuk lebih dari dua pilihan.', 'Cek kondisi paling ketat lebih dulu.', 'Uji setiap jalur dan setiap batas.'],
   q=quiz(['Jika urutan cek dibalik (>= 55 dulu), nilai 90 mendapat?', ['A', 'C', 'D'], 1, '90 >= 55 sudah benar, jadi berhenti di C.'],
          ['Berapa kasus uji minimal untuk menguji 4 jalur nilai huruf?', ['1', '2', '4'], 2, 'Setiap jalur butuh minimal satu kasus.'])),
 L('Operator logika: and, or, not', [
   'Kondisi nyata sering gabungan. "Boleh ikut ujian jika hadir minimal 75% <b>dan</b> sudah bayar". "Gratis ongkir jika belanja di atas 100 ribu <b>atau</b> member premium". Operator <code>and</code> butuh <b>semua</b> bagian benar; <code>or</code> cukup <b>salah satu</b>.',
   'Contoh klasik: <b>tahun kabisat</b>. Aturannya: habis dibagi 4 tetapi tidak habis dibagi 100, <b>atau</b> habis dibagi 400. Jadi 2024 kabisat, 1900 bukan, 2000 kabisat. Satu kondisi gabungan menggantikan tiga IF bertingkat.',
   'Saat mencampur <code>and</code> dan <code>or</code>, pakai <b>kurung</b>. Tanpa kurung, pembaca dan komputer bisa menafsirkan urutan yang berbeda.',
   'Pada visual, hasil kondisi gabungan disimpan dulu di variabel Boolean <code>kabisat</code>, lalu IF cukup mengecek variabel itu. Memberi nama pada kondisi panjang membuat algoritma lebih mudah dibaca. Uji dengan 2024, 1900, 2000, dan 2023.'],
   P_KABISAT,
   tb=[{'c': 'Tabel kebenaran', 'h': ['A', 'B', 'A and B', 'A or B', 'not A'], 'r': [['benar', 'benar', 'benar', 'benar', 'salah'], ['benar', 'salah', 'salah', 'benar', 'salah'], ['salah', 'benar', 'salah', 'benar', 'benar'], ['salah', 'salah', 'salah', 'salah', 'benar']]}],
   pts=['and: semua benar. or: salah satu benar. not: kebalikan.', 'Pakai kurung saat mencampur and dan or.'],
   q=quiz(['Apakah 1900 tahun kabisat?', ['Ya', 'Tidak'], 1, 'Habis dibagi 100 tetapi tidak habis dibagi 400.'],
          ['"Diskon jika member ATAU belanja > 200 ribu". Bukan member, belanja 250 ribu. Dapat diskon?', ['Ya', 'Tidak'], 0, 'or cukup satu bagian benar.'])),
]},
{'t': 'Perulangan', 'lvl': 'Pemula', 'd': 'FOR, WHILE, REPEAT-UNTIL, dan loop bersarang, serta kapan memakai masing-masing.', 'nodes': ['Perulangan'], 'lessons': [
 L('FOR: jumlah putaran sudah diketahui', [
   'Jika kita tahu persis berapa kali sesuatu harus diulang, pakai <code>FOR i ← awal TO akhir DO ... ENDFOR</code>. Variabel <code>i</code> (penghitung) otomatis bertambah 1 setiap putaran sampai melewati nilai akhir.',
   'Contoh: menjumlahkan 1 sampai n. Kita butuh variabel <b>akumulator</b> <code>total</code> yang diisi 0 sebelum loop, lalu ditambah <code>i</code> di setiap putaran. Lupa mengisi 0 di awal adalah kesalahan pemula yang paling umum.',
   'FOR juga bisa mundur atau melompat dengan <code>STEP</code>, misalnya <code>FOR i ← 10 TO 0 STEP -2</code>. Di flowchart Flowgorithm, FOR digambar sebagai segi enam.',
   'Jalankan visual dan perhatikan kolom variabel: <code>i</code> dan <code>total</code> berubah bersama setiap putaran.'],
   P_JUMLAH, pts=['FOR untuk jumlah putaran yang pasti.', 'Akumulator diisi nilai awal sebelum loop.', 'STEP mengatur arah dan besar langkah.'],
   q=quiz(['Berapa kali FOR i ← 3 TO 7 berputar?', ['4', '5', '7'], 1, '3, 4, 5, 6, 7: lima kali.'], ['Jika total tidak diisi 0 di awal, apa akibatnya?', ['Tidak ada', 'Isinya tidak jelas sehingga hasilnya salah', 'Program lebih cepat'], 1, 'Akumulator harus punya nilai awal.'])),
 L('WHILE: ulangi selama kondisi benar', [
   '<code>WHILE kondisi DO ... ENDWHILE</code> memeriksa kondisi <b>sebelum</b> setiap putaran. Selama kondisinya benar, badan loop dijalankan. Pakai WHILE jika jumlah putaran <b>belum diketahui</b>, yang diketahui hanya kapan harus berhenti.',
   'Badan loop harus mengubah sesuatu yang membuat kondisi akhirnya salah. Jika tidak, terjadi <b>loop tak berhingga</b> (infinite loop): program berputar selamanya. Pada contoh, <code>saldo</code> terus bertambah sehingga suatu saat ≥ 100000.',
   'Jika kondisinya sudah salah sejak awal, badan WHILE <b>tidak dijalankan sama sekali</b>. Ini beda penting dengan REPEAT-UNTIL di pelajaran berikutnya.',
   'Simulator di bawah akan berhenti dan memberi peringatan jika sebuah loop berputar lebih dari 1.500 langkah.'],
   P_TABUNG, pts=['WHILE untuk jumlah putaran yang belum diketahui.', 'Kondisi dicek sebelum setiap putaran.', 'Badan loop harus menggerakkan kondisi ke arah berhenti.'],
   q=quiz(['WHILE x < 0 dengan x = 5 di awal. Berapa kali badan loop jalan?', ['0', '1', 'Tak hingga'], 0, 'Kondisi salah sejak awal.'], ['Penyebab infinite loop?', ['Kondisi tidak pernah menjadi salah', 'Memakai FOR', 'Variabel bertipe REAL'], 0, 'Badan loop tidak mengubah kondisi.'])),
 L('REPEAT-UNTIL: jalan minimal sekali', [
   '<code>REPEAT ... UNTIL kondisi</code> menjalankan badan loop <b>dulu</b>, baru memeriksa kondisi di akhir. Loop berhenti saat kondisinya <b>benar</b>. Karena dicek di akhir, badannya pasti jalan <b>minimal sekali</b>.',
   'Contoh paling tepat: <b>validasi input</b>. Kita harus meminta PIN dulu sebelum bisa memeriksanya. Dengan WHILE, kita terpaksa meminta PIN dua kali (sebelum loop dan di dalam loop).',
   'Hati-hati dengan arah kondisi. REPEAT-UNTIL berhenti saat kondisi <b>benar</b> (UNTIL pin = "2468"). Do-while di Java, JavaScript, dan Flowgorithm justru <b>lanjut</b> saat kondisi benar (while pin &lt;&gt; "2468"). Keduanya sama, hanya kondisinya dibalik.',
   'Input di visual adalah tiga percobaan: 1111, 1234, lalu 2468. Ubah urutannya, misalnya langsung 2468, dan lihat badan loop tetap jalan sekali.'],
   P_PIN,
   tb=[{'c': 'WHILE vs REPEAT-UNTIL', 'h': ['Aspek', 'WHILE', 'REPEAT-UNTIL'], 'r': [['Cek kondisi', 'Di awal', 'Di akhir'], ['Minimal jalan', '0 kali', '1 kali'], ['Berhenti saat', 'Kondisi salah', 'Kondisi benar'], ['Cocok untuk', 'Menunggu target tercapai', 'Menu dan validasi input']]}],
   pts=['REPEAT-UNTIL jalan minimal sekali.', 'Berhenti saat kondisi UNTIL benar.', 'Do-while = REPEAT-UNTIL dengan kondisi dibalik.'],
   q=quiz(['Loop yang paling cocok untuk menampilkan menu sampai pengguna memilih Keluar?', ['FOR', 'REPEAT-UNTIL', 'Tidak perlu loop'], 1, 'Menu harus tampil minimal sekali.'], ['REPEAT ... UNTIL x > 10 berhenti saat?', ['x > 10 benar', 'x > 10 salah'], 0, 'UNTIL berhenti saat kondisinya benar.'])),
 L('Loop bersarang', [
   'Loop di dalam loop disebut <b>loop bersarang</b>. Untuk setiap satu putaran loop luar, loop dalam berjalan penuh. Jika loop luar 4 kali dan dalam 5 kali, badan loop dalam berjalan 4 × 5 = 20 kali.',
   'Pola segitiga bintang adalah latihan klasik. Loop luar <code>i</code> menentukan <b>baris</b>, loop dalam <code>j</code> menentukan <b>banyak bintang</b> di baris itu. Karena batas loop dalam adalah <code>i</code>, baris ke-1 punya 1 bintang, baris ke-4 punya 4.',
   'Loop bersarang dipakai untuk tabel (baris × kolom), membandingkan setiap pasangan data, dan sorting. Ingat: makin dalam sarangnya, makin banyak langkahnya, sehingga program bisa lambat untuk data besar.',
   'Jalankan visual dengan input 4, lalu coba 6.'],
   P_SEGI, pts=['Loop dalam berjalan penuh untuk setiap putaran loop luar.', 'Total langkah = putaran luar × putaran dalam.', 'Batas loop dalam boleh bergantung pada loop luar.'],
   q=quiz(['Loop luar 1 sampai 3, loop dalam 1 sampai 4. Berapa kali badan dalam dijalankan?', ['7', '12', '4'], 1, '3 × 4 = 12.'], ['Pada segitiga bintang n = 5, baris ke-3 berisi?', ['***', '*****', '*'], 0, 'Banyak bintang = nomor baris.'])),
]},
{'t': 'Array dan algoritma klasik', 'lvl': 'Menengah', 'd': 'Array, nilai tertinggi dan rata-rata, linear search, dan bubble sort.', 'nodes': ['Array', 'Searching', 'Sorting'], 'lessons': [
 L('Array: banyak nilai dalam satu nama', [
   '<b>Array</b> menyimpan banyak nilai sejenis dalam satu nama, misalnya 5 nilai ujian di <code>nilai[0]</code> sampai <code>nilai[4]</code>. Angka di dalam kurung siku disebut <b>indeks</b> dan dimulai dari 0 di kebanyakan bahasa (Java, Python, JavaScript, Flowgorithm).',
   'Array hampir selalu diproses dengan <b>FOR</b>, karena jumlah isinya diketahui. Pola dasarnya: <code>FOR i ← 0 TO n - 1</code>. Kesalahan klasik adalah menulis <code>TO n</code>, yang mengakses satu kotak di luar array.',
   'Mencari <b>nilai tertinggi</b>: anggap isi pertama sebagai yang tertinggi (<code>maks ← nilai[0]</code>), lalu bandingkan dengan setiap isi berikutnya. Jangan mulai dari <code>maks ← 0</code>, karena akan salah jika semua nilai negatif.',
   'Visual meminta 5 input nilai. Ganti dengan angka lain dan prediksi hasilnya.'],
   P_ARR, pts=['Indeks array dimulai dari 0.', 'Proses array dengan FOR 0 sampai n - 1.', 'Nilai maksimum dimulai dari isi pertama, bukan 0.'],
   q=quiz(['Array berisi 5 nilai. Indeks terakhirnya?', ['5', '4', '6'], 1, 'Indeks 0 sampai 4.'], ['Kenapa maks ← nilai[0], bukan maks ← 0?', ['Agar lebih cepat', 'Agar benar walau semua nilai negatif', 'Aturan bahasa'], 1, 'Jika semua negatif, 0 akan keliru dianggap maksimum.'])),
 L('Linear search: mencari satu per satu', [
   '<b>Linear search</b> memeriksa isi array satu per satu dari depan sampai data ditemukan atau array habis. Cara ini bekerja untuk data apa pun, terurut atau tidak.',
   'Kita pakai <b>WHILE</b> dengan dua syarat: masih ada data (<code>i &lt; 6</code>) <b>dan</b> belum ketemu (<code>posisi = -1</code>). Nilai -1 adalah tanda "belum ditemukan", karena tidak ada indeks negatif.',
   'Jika data ada di depan, pencarian cepat. Jika di belakang atau tidak ada, semua data harus diperiksa. Untuk data besar yang terurut, binary search jauh lebih cepat (dibahas di modul latihan algoritma tiap bahasa).',
   'Coba cari 18, 12, lalu 99 (tidak ada).'],
   P_LINEAR, pts=['Linear search memeriksa satu per satu.', '-1 sebagai tanda belum ditemukan.', 'Berhenti saat ketemu atau data habis.'],
   q=quiz(['Berapa langkah terburuk linear search untuk 100 data?', ['10', '50', '100'], 2, 'Jika data di akhir atau tidak ada, semua diperiksa.'], ['Kenapa memakai -1 sebagai nilai awal posisi?', ['Karena indeks tidak pernah negatif', 'Agar loop lebih cepat', 'Wajib di semua bahasa'], 0, '-1 tidak mungkin menjadi indeks yang sah.'])),
 L('Bubble sort dalam pseudocode', [
   'Bubble sort mengurutkan dengan membandingkan pasangan <b>bersebelahan</b> dan menukarnya jika salah urutan. Setelah putaran pertama, angka terbesar sudah di ujung kanan.',
   'Menukar dua nilai butuh <b>variabel bantu</b> <code>t</code>: <code>t ← a[j]</code>, <code>a[j] ← a[j + 1]</code>, <code>a[j + 1] ← t</code>. Tanpa <code>t</code>, nilai <code>a[j]</code> hilang tertimpa. Bayangkan menukar isi dua gelas: kamu butuh gelas ketiga.',
   'Versi ini memakai dua FOR: luar <code>i</code> dari 0 sampai 3 (n - 2 untuk 5 data), dalam <code>j</code> dari 0 sampai <code>3 - i</code>. Batas dalam mengecil karena bagian kanan sudah terurut.',
   'Jalankan visual dan perhatikan isi array di kolom variabel berubah setiap kali terjadi pertukaran.'],
   P_BUBBLE, pts=['Bandingkan dan tukar pasangan bersebelahan.', 'Menukar butuh variabel bantu.', 'Batas loop dalam mengecil setiap putaran.'],
   q=quiz(['Kenapa menukar nilai butuh variabel t?', ['Agar nilai lama tidak hilang tertimpa', 'Agar lebih cepat', 'Aturan pseudocode'], 0, 'Seperti menukar isi dua gelas.'], ['Setelah putaran pertama, apa yang pasti?', ['Array sudah terurut', 'Nilai terbesar di ujung kanan', 'Nilai terkecil di kanan'], 1, 'Nilai terbesar terbawa ke kanan.'])),
]},
{'t': 'Dari pseudocode ke kode program', 'lvl': 'Menengah', 'd': 'Menerjemahkan pseudocode ke Python, Java, dan JavaScript, prosedur dan fungsi, serta proyek mini kasir.', 'nodes': ['Translasi'], 'lessons': [
 L('Menerjemahkan pseudocode ke bahasa pemrograman', [
   'Setelah logikanya benar di pseudocode, menulis kode tinggal menerjemahkan baris demi baris. Struktur IF, WHILE, FOR tidak berubah; yang berubah hanya cara penulisannya. Inilah alasan pseudocode diajarkan sebelum bahasa pemrograman.',
   'Perhatikan tiga jebakan saat menerjemahkan. Pertama, <code>=</code> pembanding di pseudocode menjadi <code>==</code> di Python, Java, dan JavaScript. Kedua, <code>FOR i ← 1 TO n</code> menjadi <code>range(1, n + 1)</code> di Python, karena batas akhir range tidak ikut. Ketiga, pembagian bulat: <code>//</code> di Python, <code>/</code> antar-int di Java, dan <code>Math.floor(a / b)</code> di JavaScript.',
   'Kode Python di bawah adalah terjemahan langsung program "jumlah 1 sampai n" dari modul perulangan. Ubah nilai <code>n</code>, lalu jalankan.'],
   lang='python', code='# Terjemahan pseudocode: Jumlah1SampaiN\nn = 5\ntotal = 0\nfor i in range(1, n + 1):   # FOR i <- 1 TO n\n    total = total + i\nprint(f"Jumlah 1 sampai {n} = {total}")', out='Jumlah 1 sampai 5 = 15',
   tb=[{'c': 'Kamus terjemahan', 'h': ['Pseudocode', 'Python', 'Java', 'JavaScript'], 'r': [
     ['DECLARE x : INTEGER', 'x = 0', 'int x;', 'let x;'], ['INPUT x', 'x = int(input())', 'x = sc.nextInt();', 'x = Number(prompt())'],
     ['OUTPUT x', 'print(x)', 'System.out.println(x);', 'console.log(x)'], ['x ← x + 1', 'x += 1', 'x++;', 'x++'],
     ['IF a = b THEN', 'if a == b:', 'if (a == b) {', 'if (a === b) {'], ['a <> b', 'a != b', 'a != b', 'a !== b'], ['a mod b', 'a % b', 'a % b', 'a % b'],
     ['WHILE c DO', 'while c:', 'while (c) {', 'while (c) {'], ['FOR i ← 1 TO n', 'for i in range(1, n + 1):', 'for (int i = 1; i <= n; i++)', 'for (let i = 1; i <= n; i++)'],
     ['REPEAT ... UNTIL c', 'while True: ... if c: break', 'do { ... } while (!c);', 'do { ... } while (!c);'], ['a and b, not a', 'a and b, not a', 'a && b, !a', 'a && b, !a']]}],
   pts=['Struktur logika tetap, hanya penulisannya berubah.', '= pembanding menjadi ==.', 'range(1, n + 1) untuk FOR 1 TO n di Python.'],
   q=quiz(['FOR i ← 1 TO 10 di Python ditulis?', ['range(1, 10)', 'range(1, 11)', 'range(10)'], 1, 'Batas akhir range tidak ikut.'], ['IF x = 5 THEN di Java ditulis?', ['if (x = 5)', 'if (x == 5)', 'if x == 5:'], 1, '= di Java adalah pengisian nilai.'])),
 L('Prosedur dan fungsi', [
   'Saat algoritma makin panjang, kita memecahnya menjadi bagian kecil yang punya nama. <b>Prosedur</b> menjalankan serangkaian langkah tanpa mengembalikan nilai, misalnya <code>PROCEDURE CetakGaris(n)</code>. <b>Fungsi</b> mengembalikan satu nilai, misalnya <code>FUNCTION Luas(p, l) RETURNS INTEGER</code>.',
   'Nilai yang dikirim ke prosedur atau fungsi disebut <b>parameter</b>. Dengan parameter, satu fungsi bisa dipakai berkali-kali untuk data berbeda: <code>Luas(8, 5)</code> dan <code>Luas(3, 4)</code> memakai langkah yang sama.',
   'Keuntungannya: kode tidak diulang-ulang, lebih mudah diuji per bagian, dan lebih mudah dibaca. Prinsip ini sama di semua bahasa dan juga ada di Flowgorithm (simbol Call).'],
   code='FUNCTION Luas(p : INTEGER, l : INTEGER) RETURNS INTEGER\n    RETURN p * l\nENDFUNCTION\n\nPROCEDURE CetakGaris(n : INTEGER)\n    DECLARE i : INTEGER\n    FOR i <- 1 TO n DO\n        OUTPUT "-"\n    ENDFOR\nENDPROCEDURE\n\nSTART\n    OUTPUT Luas(8, 5)\n    CALL CetakGaris(3)\nEND', out='40\n-\n-\n-', run=False,
   tb=[{'c': 'Prosedur vs fungsi', 'h': ['Aspek', 'Prosedur', 'Fungsi'], 'r': [['Mengembalikan nilai', 'Tidak', 'Ya, dengan RETURN'], ['Cara memanggil', 'CALL CetakGaris(3)', 'x ← Luas(8, 5)'], ['Contoh', 'Mencetak struk', 'Menghitung pajak']]}],
   pts=['Prosedur menjalankan langkah, fungsi mengembalikan nilai.', 'Parameter membuat satu fungsi bisa dipakai ulang.'],
   q=quiz(['Hitung diskon lalu dipakai di rumus lain. Lebih cocok prosedur atau fungsi?', ['Prosedur', 'Fungsi'], 1, 'Butuh nilai kembali.'], ['Apa keuntungan memecah program menjadi fungsi?', ['Program pasti lebih cepat', 'Tidak mengulang kode dan mudah diuji', 'Tidak perlu variabel'], 1, 'Satu bagian, satu tugas.'])),
 L('Proyek mini: kasir sederhana', [
   'Saatnya menggabungkan semuanya. Kasir menerima harga dan jumlah barang berulang kali sampai kasir mengetik harga 0 (<b>REPEAT-UNTIL</b>), menjumlahkan total (<b>akumulator</b>), memberi diskon 10% jika total di atas 100 ribu (<b>IF</b>), lalu menghitung kembalian (<b>IF-ELSE</b>).',
   'Nilai 0 sebagai tanda selesai disebut <b>sentinel</b>. Teknik ini umum saat jumlah data tidak diketahui sebelumnya.',
   'Jalankan visual dengan input bawaan: 2 kopi seharga 25.000, 3 roti seharga 18.000, selesai, lalu bayar 150.000. Kemudian ubah inputnya agar total di bawah 100 ribu, atau uang bayarnya kurang.',
   '<b>Tantangan</b>: tulis ulang algoritma ini di bahasa yang sedang kamu pelajari, lalu tambahkan pajak 11% setelah diskon.'],
   P_KASIR, pts=['Sentinel (misalnya 0) menandai akhir input.', 'Gabungkan loop, akumulator, dan percabangan.', 'Uji juga kasus uang kurang.'],
   q=quiz(['Kenapa loop kasir memakai REPEAT-UNTIL?', ['Harga harus diminta minimal sekali', 'Jumlah barang selalu 5', 'Agar lebih cepat'], 0, 'Kita belum tahu jumlah barang, tetapi minimal sekali harus bertanya.'], ['Apa itu nilai sentinel?', ['Nilai khusus penanda akhir input', 'Nilai terbesar', 'Variabel global'], 0, 'Contoh: harga 0 berarti selesai.'])),
]},
]

FLOWG = [
{'t': 'Mengenal Flowgorithm', 'lvl': 'Pemula', 'd': 'Flowchart, simbol-simbol Flowgorithm, memasang aplikasi, tipe data, dan aturan ekspresi.', 'nodes': ['Flowchart', 'Flowgorithm'], 'lessons': [
 L('Flowchart dan Flowgorithm', [
   '<b>Flowchart</b> (diagram alir) menggambarkan algoritma dengan simbol dan panah. Setiap simbol punya arti tetap, sehingga siapa pun bisa membaca alurnya tanpa tahu bahasa pemrograman.',
   '<b>Flowgorithm</b> adalah aplikasi gratis untuk membuat flowchart yang <b>bisa dijalankan</b>. Kamu menyusun simbol, menekan Run, dan program benar-benar berjalan: meminta input, menghitung, dan menampilkan output. Kesalahan logika langsung terlihat.',
   'Flowgorithm juga bisa menerjemahkan flowchart menjadi kode di banyak bahasa (Python, Java, JavaScript, C++, C#, dan lainnya) lewat jendela <b>Source Code Viewer</b>. Ini jembatan yang bagus dari logika ke kode.',
   'Visual di Ruang Kode meniru cara kerja Flowgorithm: simbol aktif disorot, variabel ditampilkan, dan keluaran muncul di layar. Program pertama ini hanya punya satu simbol Output.'],
   P_HELLO,
   tb=[{'c': 'Simbol Flowgorithm', 'h': ['Simbol', 'Bentuk', 'Fungsi'], 'r': [
     ['Main / End', 'Lonjong', 'Awal dan akhir program'], ['Declare', 'Persegi dengan garis di sisi', 'Menyiapkan variabel'], ['Assign', 'Persegi panjang', 'Mengisi atau menghitung nilai'],
     ['Input', 'Jajar genjang', 'Menerima data dari pengguna'], ['Output', 'Jajar genjang', 'Menampilkan hasil'], ['If', 'Belah ketupat', 'Percabangan Benar/Salah'],
     ['While', 'Belah ketupat', 'Ulangi selama kondisi benar'], ['For', 'Segi enam', 'Ulangi dengan penghitung'], ['Do', 'Belah ketupat di bawah', 'Ulangi, cek di akhir'], ['Call', 'Persegi bergaris ganda', 'Memanggil fungsi']]}],
   pts=['Flowchart: algoritma dalam bentuk gambar.', 'Flowgorithm membuat flowchart bisa dijalankan.', 'Source Code Viewer menerjemahkan ke banyak bahasa.'],
   q=quiz(['Simbol untuk menerima data dari pengguna?', ['Persegi panjang', 'Jajar genjang', 'Segi enam'], 1, 'Input dan Output memakai jajar genjang.'], ['Simbol segi enam di Flowgorithm adalah?', ['If', 'For', 'Declare'], 1, 'For digambar sebagai segi enam.'])),
 L('Memasang dan memakai Flowgorithm', [
   'Unduh Flowgorithm dari situs resminya, <b>flowgorithm.org</b>. Aplikasinya gratis dan dibuat untuk Windows. Di macOS atau Linux, sebagian pengguna menjalankannya lewat Wine; kamu juga bisa berlatih dengan simulator di Ruang Kode.',
   'Saat membuat program baru, sudah ada simbol <b>Main</b> dan <b>End</b>. Untuk menambah simbol, <b>klik panah</b> di antara dua simbol, lalu pilih jenis simbol dari daftar. <b>Klik dua kali</b> sebuah simbol untuk mengisi isinya, misalnya nama variabel atau ekspresi.',
   'Tekan tombol <b>Run</b> untuk menjalankan. Jendela <b>Console</b> menampilkan input dan output. Gunakan juga jendela <b>Variable Watch</b> untuk melihat isi setiap variabel saat program berjalan, dan jalankan <b>langkah demi langkah</b> untuk mencari kesalahan logika. Kecepatan eksekusi bisa diatur agar alur mudah diikuti.',
   'Kebiasaan baik: simpan file (.fprg) sesering mungkin, beri nama variabel yang bermakna, dan tambahkan simbol <b>Comment</b> untuk menjelaskan bagian yang rumit.'],
   P_LUAS,
   tb=[{'c': 'Langkah membuat program pertama', 'h': ['Langkah', 'Yang dilakukan'], 'r': [['1', 'File → New, muncul Main dan End'], ['2', 'Klik panah, tambah Declare: panjang, lebar, luas bertipe Integer'], ['3', 'Tambah Input panjang, lalu Input lebar'], ['4', 'Tambah Assign: luas = panjang * lebar'], ['5', 'Tambah Output: "Luas = " & luas'], ['6', 'Tekan Run, isi input di Console']]}],
   pts=['Klik panah untuk menambah simbol, klik dua kali untuk mengisi.', 'Variable Watch dan jalan langkah demi langkah membantu mencari kesalahan.', 'Simpan sering dan beri nama yang bermakna.'],
   q=quiz(['Cara menambah simbol baru di Flowgorithm?', ['Klik panah di antara simbol', 'Ketik kode', 'Seret dari menu File'], 0, 'Panah adalah titik sisip.'], ['Jendela untuk melihat isi variabel saat program berjalan?', ['Console', 'Variable Watch', 'Source Code Viewer'], 1, 'Variable Watch menampilkan nilai terkini.'])),
 L('Tipe data, Declare, dan aturan ekspresi', [
   'Flowgorithm mewajibkan setiap variabel di-<b>Declare</b> dulu dengan tipe: <code>Integer</code> (bulat), <code>Real</code> (pecahan), <code>String</code> (teks), atau <code>Boolean</code> (true/false). Centang <b>Array</b> dan isi ukurannya untuk membuat array.',
   'Aturan ekspresinya berbeda sedikit dari bahasa lain: <code>=</code> dipakai untuk <b>membandingkan</b> di If dan While, <code>&lt;&gt;</code> atau <code>!=</code> untuk tidak sama, <code>mod</code> atau <code>%</code> untuk sisa bagi, <code>and</code> <code>or</code> <code>not</code> untuk logika, dan <code>&amp;</code> untuk <b>menggabungkan teks</b>: <code>"Halo " &amp; nama</code>.',
   'Fungsi bawaan yang sering dipakai: <code>Int(x)</code> membuang desimal, <code>Sqrt(x)</code> akar, <code>Abs(x)</code> nilai mutlak, <code>Len(s)</code> panjang teks, <code>Random(n)</code> angka acak 0 sampai n - 1, <code>ToString(x)</code> dan <code>ToInteger(s)</code> untuk konversi.',
   'Jika hasil bagi harus bulat, bungkus dengan <code>Int()</code>, misalnya <code>Int(angka / 10)</code>. Jika hasilnya boleh pecahan, seperti rata-rata pada contoh, simpan di variabel <code>Real</code>.'],
   P_RATA,
   tb=[{'c': 'Operator dan fungsi Flowgorithm', 'h': ['Tulis', 'Arti', 'Contoh'], 'r': [['=', 'Sama dengan (di kondisi)', 'x = 5'], ['<> atau !=', 'Tidak sama dengan', 'x <> 0'], ['mod atau %', 'Sisa bagi', '17 mod 5 → 2'], ['&', 'Gabung teks', '"Nilai: " & x'], ['and, or, not', 'Logika', 'x > 0 and x < 10'], ['^', 'Pangkat', '2 ^ 3 → 8'], ['Int(x)', 'Bulatkan ke bawah (buang desimal)', 'Int(7.8) → 7'], ['Len(s)', 'Panjang teks', 'Len("kode") → 4']]}],
   pts=['Declare dulu dengan tipe yang tepat.', '& untuk gabung teks, = untuk membandingkan.', 'Int() mengubah pecahan menjadi bulat.'],
   q=quiz(['Cara menampilkan "Halo Rina" jika nama berisi "Rina"?', ['"Halo " + nama', '"Halo " & nama', '"Halo " , nama'], 1, 'Flowgorithm memakai & untuk menggabungkan teks.'], ['Hasil Int(9.99)?', ['10', '9', '9.9'], 1, 'Int membuang bagian desimal.'])),
]},
{'t': 'Input, proses, output', 'lvl': 'Pemula', 'd': 'Program lurus tanpa percabangan: menghitung luas lingkaran dan diskon belanja.', 'nodes': ['IPO'], 'lessons': [
 L('Luas dan keliling lingkaran', [
   'Program paling dasar mengikuti pola <b>Input → Proses → Output</b>. Terima jari-jari dari pengguna, hitung luas dan keliling, lalu tampilkan.',
   'Karena jari-jari dan hasilnya bisa pecahan, semua variabel bertipe <code>Real</code>. Rumusnya: luas = π × r × r dan keliling = 2 × π × r, dengan π ≈ 3.14159.',
   'Di Flowgorithm, satu simbol Assign berisi satu perhitungan. Memecah rumus menjadi beberapa Assign membuat flowchart lebih mudah dibaca dan diperiksa.',
   'Jalankan dengan r = 7, lalu coba r = 10 dan r = 0.5.'],
   P_LINGKAR, pts=['Pola dasar: Input → Proses → Output.', 'Pakai Real untuk nilai pecahan.', 'Satu Assign, satu perhitungan.'],
   q=quiz(['Tipe yang tepat untuk jari-jari 2.5?', ['Integer', 'Real', 'String'], 1, '2.5 adalah pecahan.'], ['Urutan simbol yang benar?', ['Output, Input, Assign', 'Declare, Input, Assign, Output', 'Assign, Declare, Output'], 1, 'Variabel disiapkan, data diterima, dihitung, lalu ditampilkan.'])),
 L('Menghitung diskon belanja', [
   'Toko memberi diskon dalam persen. Program menerima harga dan persen diskon, menghitung potongan (<code>harga * persen / 100</code>), lalu harga yang harus dibayar.',
   'Perhatikan urutan: <code>potongan</code> harus dihitung <b>sebelum</b> <code>bayar</code>, karena <code>bayar</code> memakai nilai potongan. Komputer menjalankan simbol dari atas ke bawah, tidak bisa "melihat ke depan".',
   'Coba input harga 250000 dengan diskon 15, lalu diskon 0 dan 100. Nilai ekstrem seperti 0 dan 100 membantu memastikan rumusnya benar.'],
   P_DISKON, pts=['Simbol dijalankan berurutan dari atas ke bawah.', 'Nilai yang dipakai harus sudah dihitung lebih dulu.', 'Uji dengan nilai ekstrem.'],
   q=quiz(['Harga 200000, diskon 25%. Berapa yang dibayar?', ['50000', '150000', '175000'], 1, 'Potongan 50000, bayar 150000.'], ['Jika Assign bayar diletakkan sebelum Assign potongan, apa yang terjadi?', ['Tidak ada bedanya', 'Bayar dihitung dengan potongan yang belum ada', 'Program lebih cepat'], 1, 'Urutan simbol menentukan hasil.'])),
]},
{'t': 'Percabangan di Flowgorithm', 'lvl': 'Pemula', 'd': 'Simbol If, ganjil-genap, dan If bersarang untuk nilai huruf.', 'nodes': ['If'], 'lessons': [
 L('Simbol If: ganjil atau genap', [
   'Simbol <b>If</b> berbentuk belah ketupat dengan dua cabang: <b>True</b> di kanan dan <b>False</b> di kiri. Isi kondisinya dengan ekspresi yang hasilnya benar atau salah, misalnya <code>x mod 2 = 0</code>.',
   'Bilangan genap habis dibagi 2, sehingga sisa baginya 0. Jika kondisi benar, cabang kanan menampilkan "genap"; jika salah, cabang kiri menampilkan "ganjil". Kedua cabang bertemu lagi di titik bulat di bawah.',
   'Di Flowgorithm, kamu bisa menaruh beberapa simbol di setiap cabang, atau membiarkan satu cabang kosong.',
   'Coba input 17, 0, dan -4.'],
   P_GANJIL, pts=['If punya cabang True (kanan) dan False (kiri).', 'mod 2 = 0 berarti genap.', 'Kedua cabang bertemu kembali.'],
   q=quiz(['Kondisi untuk "x habis dibagi 3"?', ['x / 3 = 0', 'x mod 3 = 0', 'x & 3 = 0'], 1, 'Sisa bagi 0 berarti habis dibagi.'], ['Apakah 0 genap menurut program ini?', ['Ya', 'Tidak'], 0, '0 mod 2 = 0.'])),
 L('If bersarang: nilai huruf', [
   'Untuk lebih dari dua kemungkinan, taruh If baru di cabang False. Setiap tingkat memeriksa satu batas, dari yang tertinggi ke yang terendah.',
   'Flowchart If bersarang bisa melebar ke samping. Di Flowgorithm, ini normal. Kuncinya: cek urutan batas dan uji setiap jalur.',
   'Uji dengan 90, 78, 60, dan 30 untuk melewati keempat jalur.'],
   P_HURUF, pts=['If bersarang ditaruh di cabang False.', 'Cek batas tertinggi lebih dulu.', 'Uji setiap jalur.'],
   q=quiz(['Nilai 70 mendapat huruf apa di program ini?', ['A', 'B', 'C'], 1, '70 >= 70 benar.'], ['Berapa simbol If yang dibutuhkan untuk 4 nilai huruf?', ['2', '3', '4'], 1, 'Pilihan terakhir (D) adalah sisa ketika semua kondisi salah.'])),
]},
{'t': 'Perulangan di Flowgorithm', 'lvl': 'Pemula', 'd': 'Simbol For, While, dan Do: tabel perkalian, Fibonacci, faktorial, tebak angka, dan menu.', 'nodes': ['For', 'While', 'Do'], 'lessons': [
 L('Simbol For: tabel perkalian dan hitung mundur', [
   'Simbol <b>For</b> (segi enam) berisi variabel penghitung, nilai awal, nilai akhir, arah (naik atau turun), dan besar langkah. Variabelnya harus sudah di-Declare sebagai Integer.',
   'Tabel perkalian adalah contoh klasik For: kita tahu persis ada 5 baris. Untuk hitung mundur, pilih arah <b>Decreasing</b> dengan langkah 1, atau di pseudocode tulis <code>STEP -1</code>.',
   'Jalankan tabel perkalian dengan input 7, lalu coba 9. Perhatikan bahwa simbol For mengecek batas sebelum setiap putaran.'],
   P_KALI, pts=['For: penghitung, awal, akhir, arah, langkah.', 'Variabel For harus di-Declare.', 'Arah Decreasing untuk hitung mundur.'],
   q=quiz(['For i dari 1 sampai 10 langkah 3 menghasilkan?', ['1 4 7 10', '1 3 6 9', '3 6 9'], 0, 'Mulai 1, tambah 3: 1, 4, 7, 10.'], ['Loop yang tepat untuk mencetak 100 baris?', ['For', 'Do', 'If'], 0, 'Jumlah putaran pasti.'])),
 L('Deret Fibonacci dan faktorial', [
   'Fibonacci di Flowgorithm butuh tiga variabel: <code>a</code>, <code>b</code>, dan <code>c</code> sebagai penampung sementara. Setiap putaran: tampilkan <code>a</code>, hitung <code>c = a + b</code>, lalu geser <code>a = b</code> dan <code>b = c</code>.',
   'Faktorial memakai akumulator perkalian: <code>hasil</code> diisi <b>1</b>, bukan 0, karena 0 dikali apa pun hasilnya 0. Ini jebakan yang sering muncul di ujian.',
   'Jalankan Fibonacci dengan n = 8, lalu coba n = 12. Perhatikan bagaimana a, b, c bergeser di Variable Watch.'],
   P_FIB, pts=['Fibonacci: tampilkan, jumlahkan, geser.', 'Akumulator perkalian dimulai dari 1.'],
   q=quiz(['Nilai awal hasil untuk menghitung faktorial?', ['0', '1', 'n'], 1, 'Perkalian dengan 0 selalu 0.'], ['Fibonacci n = 6 menampilkan?', ['0 1 1 2 3 5', '1 1 2 3 5 8', '0 1 2 3 4 5'], 0, 'Mulai dari 0 dan 1.'])),
 L('Simbol While: tebak angka', [
   'Simbol <b>While</b> memeriksa kondisi di awal. Selama benar, simbol-simbol di dalamnya dijalankan, lalu kembali ke atas. Pakai While saat jumlah putaran tidak diketahui.',
   'Pada permainan tebak angka, kita tidak tahu berapa kali pengguna akan menebak. Loop berjalan selama <code>tebakan &lt;&gt; rahasia</code>. Agar kondisi bisa dicek pertama kali, <code>tebakan</code> diisi 0 lebih dulu.',
   'Input bawaan adalah tiga tebakan: 50, 30, 42. Ubah urutannya dan perhatikan jumlah percobaan berubah.'],
   P_TEBAK, pts=['While cek di awal; bisa 0 kali.', 'Variabel di kondisi harus punya nilai sebelum loop.', 'Badan loop harus bisa membuat kondisi salah.'],
   q=quiz(['Kenapa tebakan diisi 0 sebelum While?', ['Agar kondisi bisa dicek pada putaran pertama', 'Agar lebih cepat', 'Tidak ada alasan'], 0, 'Variabel tanpa nilai tidak bisa dibandingkan.'], ['Rahasia 42, tebakan pertama 42. Berapa kali badan loop jalan?', ['0', '1', '2'], 1, 'Kondisi awal 0 <> 42 benar, jadi masuk sekali, lalu tebakan benar.'])),
 L('Simbol Do: menu yang berulang', [
   'Simbol <b>Do</b> menjalankan isi loop dulu, baru memeriksa kondisi di bawah. Loop <b>lanjut</b> selama kondisi benar. Cocok untuk menu, karena menu harus tampil minimal sekali.',
   'Pada contoh, menu tampil, pengguna memilih, program memproses, lalu kondisi <code>pilih &lt;&gt; 0</code> dicek. Pilihan 0 menghentikan loop.',
   'Input bawaan: 1 (cek saldo), 2 (isi saldo), 1 (cek lagi), 0 (keluar).'],
   P_MENU, pts=['Do menjalankan isi dulu, cek di akhir.', 'Lanjut selama kondisi benar.', 'Ideal untuk menu dan validasi input.'],
   q=quiz(['Beda utama Do dan While?', ['Do cek kondisi di akhir, jadi minimal jalan sekali', 'Do lebih cepat', 'While tidak bisa memakai kondisi'], 0, 'Posisi pengecekan yang berbeda.'], ['Pada menu ini, input pertama 0. Apakah menu sempat tampil?', ['Ya, sekali', 'Tidak'], 0, 'Isi Do selalu jalan minimal sekali.'])),
]},
{'t': 'Array, fungsi, dan proyek', 'lvl': 'Menengah', 'd': 'Array dengan input, fungsi (Call), proyek kasir, dan mengekspor flowchart menjadi kode.', 'nodes': ['Array', 'Function'], 'lessons': [
 L('Array dengan input', [
   'Untuk membuat array di Flowgorithm, centang <b>Array?</b> pada simbol Declare dan isi ukurannya. Indeks dimulai dari 0, jadi array berukuran 5 punya indeks 0 sampai 4.',
   'Input ke array memakai For: <code>Input nilai[i]</code> untuk i dari 0 sampai 4. Setelah semua terisi, For kedua menghitung total dan mencari nilai tertinggi.',
   'Memisahkan "mengisi data" dan "mengolah data" ke dua loop membuat flowchart lebih jelas dan mudah diperiksa.'],
   P_ARR, pts=['Centang Array? dan isi ukurannya.', 'Indeks dari 0 sampai ukuran - 1.', 'Pisahkan loop pengisian dan loop pengolahan.'],
   q=quiz(['Array ukuran 10, For yang benar untuk mengisinya?', ['i = 1 to 10', 'i = 0 to 9', 'i = 0 to 10'], 1, 'Indeks 0 sampai 9.'], ['Akses nilai[5] pada array ukuran 5 akan?', ['Mengambil nilai terakhir', 'Error karena di luar batas', 'Mengambil 0'], 1, 'Indeks terakhir adalah 4.'])),
 L('Fungsi dan simbol Call', [
   'Flowgorithm mendukung <b>fungsi</b>. Buat fungsi baru lewat <b>Function Manager</b> (daftar fungsi di toolbar), lalu isi nama, parameter, dan tipe nilai kembali. Fungsi punya flowchart sendiri dengan simbol awal dan akhir.',
   'Fungsi dipanggil di dalam ekspresi, misalnya <code>luas = HitungLuas(p, l)</code>. Fungsi yang tidak mengembalikan nilai (prosedur) dipanggil dengan simbol <b>Call</b>.',
   'Gunakan fungsi saat langkah yang sama dipakai di beberapa tempat, atau saat flowchart utama terlalu panjang. Satu fungsi sebaiknya punya satu tugas yang jelas.'],
   code='Function HitungLuas (Integer p, Integer l) → Integer\n    Declare Integer hasil\n    Assign hasil = p * l\nReturn hasil\n\nMain\n    Declare Integer luas\n    Assign luas = HitungLuas(8, 5)\n    Output "Luas: " & luas\n    Call CetakGaris(3)\nEnd', out='Luas: 40\n---', run=False,
   tb=[{'c': 'Bagian fungsi di Flowgorithm', 'h': ['Bagian', 'Isi'], 'r': [['Nama', 'HitungLuas'], ['Parameter', 'Integer p, Integer l'], ['Return type', 'Integer (atau None untuk prosedur)'], ['Return variable', 'hasil'], ['Cara memanggil', 'Di ekspresi Assign, atau simbol Call untuk prosedur']]}],
   pts=['Fungsi punya flowchart sendiri.', 'Fungsi dengan nilai kembali dipanggil di ekspresi.', 'Prosedur (tanpa nilai kembali) dipanggil dengan Call.'],
   q=quiz(['Simbol untuk memanggil prosedur?', ['Assign', 'Call', 'Output'], 1, 'Call menjalankan fungsi tanpa nilai kembali.'], ['Kapan sebaiknya membuat fungsi?', ['Saat langkah sama dipakai berulang', 'Setiap ada satu simbol', 'Tidak pernah'], 0, 'Hindari mengulang langkah yang sama.'])),
 L('Proyek: kasir dengan diskon', [
   'Proyek ini menggabungkan Do (input barang sampai harga 0), akumulator, If untuk diskon, dan If-Else untuk kembalian. Bangun ulang di aplikasi Flowgorithm, simbol demi simbol, lalu bandingkan dengan simulator ini.',
   'Saat membangun di Flowgorithm, jalankan setiap kali menambah 2 sampai 3 simbol. Menguji sedikit-sedikit jauh lebih mudah daripada mencari kesalahan di flowchart yang sudah besar.',
   '<b>Tantangan</b>: tambahkan pajak 11% setelah diskon, dan tampilkan jumlah barang yang dibeli.'],
   P_KASIR, pts=['Gabungkan Do, akumulator, dan If.', 'Uji setiap beberapa simbol.', 'Uji juga kasus uang kurang dan total di bawah batas diskon.'],
   q=quiz(['Kenapa jumlah barang tidak diminta saat harga 0?', ['Karena 0 adalah tanda selesai', 'Karena error', 'Karena wajib'], 0, 'If di dalam Do melewati input jumlah saat sentinel muncul.'], ['Total 120000 mendapat diskon 10%. Total baru?', ['108000', '110000', '12000'], 0, '120000 - 12000 = 108000.'])),
 L('Dari flowchart ke kode: Source Code Viewer', [
   'Setelah flowchart berjalan benar, buka jendela <b>Source Code Viewer</b> di Flowgorithm (dari menu Tools). Pilih bahasa (Python, Java, JavaScript, C++, C#, dan lainnya), dan Flowgorithm menuliskan kode yang setara. Klik sebuah simbol dan baris kode yang sesuai ikut tersorot.',
   'Gunakan fitur ini untuk <b>belajar membaca kode</b>, bukan untuk menyalin tugas. Bandingkan setiap simbol dengan baris kodenya: Declare menjadi deklarasi variabel, While menjadi <code>while</code>, Output menjadi <code>print</code> atau <code>System.out.println</code>.',
   'Kode Python di bawah setara dengan flowchart tabel perkalian. Ubah nilai <code>n</code> lalu jalankan. Setelah itu, lanjutkan ke jalur Python, Java, atau JavaScript di Ruang Kode, termasuk modul latihan algoritma di masing-masing jalur.'],
   lang='python', code='# Setara dengan flowchart TabelPerkalian\nn = 7\nfor i in range(1, 6):\n    print(f"{n} x {i} = {n * i}")', out='7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35',
   tb=[{'c': 'Simbol Flowgorithm ke kode', 'h': ['Simbol', 'Python', 'Java', 'JavaScript'], 'r': [['Declare Integer x', 'x = 0', 'int x;', 'let x;'], ['Input x', 'x = int(input())', 'x = input.nextInt();', 'x = Number(prompt())'], ['Output x', 'print(x)', 'System.out.println(x);', 'console.log(x)'], ['Assign x = x + 1', 'x = x + 1', 'x = x + 1;', 'x = x + 1'], ['If', 'if ...:', 'if (...) { }', 'if (...) { }'], ['While', 'while ...:', 'while (...) { }', 'while (...) { }'], ['For', 'for i in range(...):', 'for (int i = ...; ...; i++)', 'for (let i = ...; ...; i++)'], ['Do', 'while True: ... break', 'do { } while (...);', 'do { } while (...);']]}],
   pts=['Source Code Viewer menerjemahkan flowchart ke banyak bahasa.', 'Pakai untuk belajar membaca kode, bukan menyalin.', 'Setiap simbol punya padanan baris kode.'],
   q=quiz(['Simbol Output di Python menjadi?', ['input()', 'print()', 'return'], 1, 'Output menampilkan ke layar.'], ['Manfaat utama Source Code Viewer bagi pemula?', ['Melihat padanan setiap simbol dalam kode', 'Mempercepat komputer', 'Mengganti Python'], 0, 'Jembatan dari logika ke sintaks.'])),
]},
]

root = pathlib.Path(__file__).resolve().parents[2]
js = ('/* ===================== JALUR PSEUDOCODE & FLOWGORITHM =====================\n'
      '   Dibuat oleh tools/gen/logika.py. Program fc dijalankan oleh simulator viz-fc.js. */\n'
      'const PSEUDO_MODULES=' + json.dumps(PSEUDO, ensure_ascii=False) + ';\n'
      'const FLOWG_MODULES=' + json.dumps(FLOWG, ensure_ascii=False) + ';\n')
(root / 'src/js/track-logika.js').write_text(js)
print('lessons', sum(len(m['lessons']) for m in PSEUDO), sum(len(m['lessons']) for m in FLOWG), len(js))
