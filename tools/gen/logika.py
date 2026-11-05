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

_OLD = [
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


# ---------- Pseudocode: 6 modul x 6 pelajaran (+1 pelajaran perbandingan loop) ----------
# Pelajaran lama dipakai ulang lewat R() agar isinya tidak hilang.
_O = {l['t']: l for m in _OLD for l in m['lessons']}
def R(old, t, **kw):
    d = dict(_O[old]); d['t'] = t
    d.update(kw)
    return d

P_IO = fc('SapaPengguna', [D('nama', 'String'), D('umur', 'Integer'), O('"Siapa namamu?"'), I('nama'), O('"Berapa umurmu?"'), I('umur'),
    O('"Halo " & nama & ", tahun depan umurmu " & (umur + 1)')], ['Rina', '19'])
P_DETIK = fc('KonversiDetik', [D('total, jam, menit, detik', 'Integer'), I('total'), A('jam', 'Int(total / 3600)'), A('menit', 'Int((total mod 3600) / 60)'), A('detik', 'total mod 60'),
    O('jam & " jam " & menit & " menit " & detik & " detik"')], ['7384'])
P_STRUK = fc('StrukBelanja', [D('harga, jumlah, subtotal', 'Integer'), D('pajak, total', 'Real'), I('harga'), I('jumlah'), A('subtotal', 'harga * jumlah'),
    A('pajak', 'subtotal * 11 / 100'), A('total', 'subtotal + pajak'), O('"Subtotal: " & subtotal'), O('"PPN 11%: " & pajak'), O('"Total: " & total')], ['15000', '4'])
P_ONGKIR = fc('GratisOngkir', [D('belanja, ongkir', 'Integer'), I('belanja'), A('ongkir', '15000'),
    IF('belanja >= 100000', [A('ongkir', '0'), O('"Selamat, gratis ongkir!"')]), O('"Total bayar: " & (belanja + ongkir)')], ['120000'])
P_MENU3 = fc('PilihMinuman', [D('kode, harga', 'Integer'), D('menu', 'String'), I('kode'),
    IF('kode = 1', [A('menu', '"Kopi susu"'), A('harga', '18000')], [IF('kode = 2', [A('menu', '"Teh tarik"'), A('harga', '15000')], [IF('kode = 3', [A('menu', '"Jus jeruk"'), A('harga', '20000')], [A('menu', '"Tidak ada"'), A('harga', '0')])])]),
    O('menu & ": Rp" & harga')], ['2'])
P_GUARD = fc('ValidasiNilai', [D('nilai', 'Integer'), I('nilai'),
    IF('nilai < 0 or nilai > 100', [O('"Error: nilai harus 0 sampai 100"')], [IF('nilai >= 75', [O('"Lulus"')], [O('"Remedial"')])])], ['120'])
P_BEDA = fc('TigaLoop', [D('i, n', 'Integer'), I('n'),
    O('"FOR:"'), F('i', 'n', '5', [O('i')]),
    O('"WHILE:"'), A('i', 'n'), W('i <= 5', [O('i'), A('i', 'i + 1')]),
    O('"DO-WHILE:"'), A('i', 'n'), DO('i <= 5', [O('i'), A('i', 'i + 1')], 'i > 5')], ['1'])
P_DIGIT = fc('HitungDigit', [D('n, digit', 'Integer'), I('n'), A('digit', '0'), W('n > 0', [A('n', 'Int(n / 10)'), A('digit', 'digit + 1')]), O('"Banyak digit: " & digit')], ['40271'])
P_AKUM = fc('RekapNilai', [D('i, x, total, lulus, maks', 'Integer'), D('rata', 'Real'), A('total', '0'), A('lulus', '0'), A('maks', '0'),
    F('i', '1', '5', [I('x'), A('total', 'total + x'), IF('x >= 75', [A('lulus', 'lulus + 1')]), IF('i = 1 or x > maks', [A('maks', 'x')])]),
    A('rata', 'total / 5'), O('"Total: " & total'), O('"Rata-rata: " & rata'), O('"Lulus: " & lulus & " orang"'), O('"Tertinggi: " & maks')], ['80', '65', '92', '75', '58'])
P_UPDATE = fc('NaikkanHarga', [D('harga', 'Integer', 5), A('harga', '[12000, 8000, 15000, 5000, 20000]'), D('i', 'Integer'),
    F('i', '0', '4', [A('harga[i]', 'harga[i] + Int(harga[i] * 10 / 100)')]), O('"Harga baru: " & harga'),
    F('i', '4', '0', [O('"Indeks " & i & ": " & harga[i]')], '-1')])
P_MATRIX = fc('NilaiPerSiswa', [D('nilai', 'Integer', '3, 4'), A('nilai', '[[80, 75, 90, 85], [60, 70, 65, 80], [95, 88, 92, 90]]'), D('b, k, total', 'Integer'),
    F('b', '0', '2', [A('total', '0'), F('k', '0', '3', [A('total', 'total + nilai[b][k]')]), O('"Siswa " & (b + 1) & ": total " & total & ", rata-rata " & total / 4')])])
P_BINARY = fc('BinarySearch', [D('data', 'Integer', 8), A('data', '[3, 8, 12, 17, 23, 31, 40, 52]'), D('cari, kiri, kanan, tengah, posisi', 'Integer'), I('cari'),
    A('kiri', '0'), A('kanan', '7'), A('posisi', '-1'),
    W('kiri <= kanan and posisi = -1', [A('tengah', 'Int((kiri + kanan) / 2)'),
        IF('data[tengah] = cari', [A('posisi', 'tengah')], [IF('data[tengah] < cari', [A('kiri', 'tengah + 1')], [A('kanan', 'tengah - 1')])])]),
    IF('posisi = -1', [O('cari & " tidak ditemukan"')], [O('cari & " ada di indeks " & posisi')])], ['31'])
P_INSERT = fc('InsertionSort', [D('a', 'Integer', 5), A('a', '[29, 10, 14, 37, 13]'), D('i, j, kunci', 'Integer'),
    F('i', '1', '4', [A('kunci', 'a[i]'), A('j', 'i - 1'), W('j >= 0 and a[j] > kunci', [A('a[j + 1]', 'a[j]'), A('j', 'j - 1')]), A('a[j + 1]', 'kunci')]),
    O('"Terurut: " & a')])
P_OBO = fc('TotalNilaiBug', [D('nilai', 'Integer', 5), A('nilai', '[70, 85, 62, 91, 78]'), D('i, total', 'Integer'), A('total', '0'),
    F('i', '0', '5', [A('total', 'total + nilai[i]')]), O('"Total: " & total')])
P_LANGKAH = fc('HitungLangkah', [D('n, i, j, langkah', 'Integer'), I('n'), A('langkah', '0'),
    F('i', '1', 'n', [F('j', '1', 'n', [A('langkah', 'langkah + 1')])]), O('"n = " & n & ", langkah = " & langkah')], ['4'])

PSEUDO = [
{'t': 'Konstruksi logika inti', 'lvl': 'Pemula', 'd': 'Tujuan pseudocode yang tidak terikat bahasa, kata kunci standar, variabel dan tipe data, input-output, operator aritmetika, dan algoritma sekuensial pertama.', 'nodes': ['Algoritma', 'Pseudocode'], 'lessons': [
 R('Algoritma dan pseudocode', 'Tujuan pseudocode yang tidak terikat bahasa', b=_O['Algoritma dan pseudocode']['b'][:2] + [
   '<b>Pseudocode</b> adalah cara menulis algoritma dengan bahasa yang mirip kode program, tetapi <b>tidak terikat bahasa tertentu</b> (language-agnostic). Tujuannya: memikirkan <b>logika</b> dulu sebelum memikirkan titik koma, kurung kurawal, atau aturan Java dan Python. Pseudocode yang baik bisa diterjemahkan ke bahasa apa pun oleh siapa pun.',
   'Kenapa ini penting? Pertama, <b>komunikasi</b>: dosen, rekan satu tim, dan pewawancara kerja bisa membaca pseudocode tanpa tahu bahasa favoritmu. Kedua, <b>fokus</b>: kesalahan logika lebih mudah terlihat tanpa gangguan error sintaks. Ketiga, <b>tahan lama</b>: bahasa pemrograman datang dan pergi, tetapi algoritma tetap sama.',
   'Visual di bawah menunjukkan satu algoritma dalam dua bentuk: <b>flowchart</b> (gambar) dan <b>pseudocode</b> (teks). Tekan Berikutnya dan perhatikan baris yang aktif di keduanya berjalan bersamaan. Ganti inputnya, lalu jalankan lagi.']),
 R('Aturan menulis pseudocode', 'Kata kunci standar dan gaya penulisan', b=_O['Aturan menulis pseudocode']['b'] + [
   'Ada dua <b>gaya penulisan</b> yang sering dipakai. <b>Gaya terstruktur</b> (seperti di Ruang Kode dan kurikulum Cambridge) memakai kata kunci huruf besar dan penutup blok (<code>ENDIF</code>). <b>Gaya ringkas</b> (sering di buku algoritma dan wawancara kerja) mirip Python: tanpa penutup blok, cukup indentasi. Pilih satu gaya dan konsisten dalam satu dokumen.']),
 R('Variabel, tipe data, dan operator', 'Variabel, tipe data, dan pengisian nilai', b=[
   '<b>Variabel</b> adalah kotak bernama untuk menyimpan nilai. Sebelum dipakai, variabel dideklarasikan beserta <b>tipe</b>-nya, agar jelas jenis isi yang boleh masuk: <code>DECLARE umur : INTEGER</code>. Tipe dasar: <code>INTEGER</code> (bilangan bulat), <code>REAL</code> (bilangan pecahan), <code>STRING</code> (teks), <code>BOOLEAN</code> (benar/salah), dan <code>CHAR</code> (satu huruf).',
   '<b>Pengisian nilai</b> (assignment) ditulis dengan panah: <code>umur ← 19</code>. Bacanya dari kanan ke kiri: hitung nilai di kanan, lalu simpan ke variabel di kiri. Nilai lama di dalam kotak <b>tertimpa</b> dan hilang. Itulah sebabnya <code>x ← x + 1</code> masuk akal: ambil x lama, tambah 1, simpan lagi ke x.',
   'Beri nama variabel yang <b>bermakna</b>: <code>hargaSatuan</code> lebih jelas daripada <code>h</code>. Nama tidak boleh diawali angka dan tidak boleh berisi spasi. Variabel yang belum diisi nilainya tidak boleh dibaca, karena isinya belum jelas.',
   'Contoh visual mengubah suhu Celcius ke Fahrenheit dengan tipe <code>REAL</code>, karena hasilnya bisa pecahan. Perhatikan kolom variabel: <code>fahrenheit</code> masih kosong sampai baris pengisian dijalankan. Coba input 100 atau -40.'],
   tb=[_O['Variabel, tipe data, dan operator']['tb'][0], {'c': 'Pengisian nilai langkah demi langkah', 'h': ['Baris', 'a', 'b', 'Keterangan'], 'r': [['a ← 5', '5', '—', 'a diisi 5'], ['b ← a * 2', '5', '10', 'b dihitung dari a'], ['a ← a + b', '15', '10', 'nilai lama a (5) tertimpa'], ['b ← 0', '15', '0', 'a tidak ikut berubah']]}],
   pts=['Deklarasikan variabel dengan tipenya.', '← mengisi nilai: hitung kanan, simpan ke kiri, nilai lama tertimpa.', 'Nama variabel harus bermakna.'],
   q=quiz(['Tipe yang tepat untuk menyimpan IPK 3.75?', ['INTEGER', 'REAL', 'BOOLEAN'], 1, 'IPK berupa bilangan pecahan.'],
          ['a ← 4, lalu a ← a * 3. Berapa a sekarang?', ['4', '7', '12'], 2, 'Hitung 4 × 3 = 12, lalu simpan ke a.'],
          ['Nama variabel mana yang sah dan bermakna?', ['2nilai', 'total harga', 'totalHarga'], 2, 'Tidak diawali angka dan tanpa spasi.'])),
 L('Input dan output dasar', [
   'Hampir semua program mengikuti pola <b>IPO</b>: <b>Input</b> (terima data), <b>Proses</b> (olah data), <b>Output</b> (tampilkan hasil). <code>INPUT nama</code> berarti program berhenti sejenak, menunggu pengguna mengetik, lalu menyimpan ketikan itu ke variabel <code>nama</code>.',
   '<code>OUTPUT</code> menampilkan teks atau isi variabel. Teks ditulis di antara tanda kutip, variabel tanpa kutip: <code>OUTPUT "Halo ", nama</code>. Perbedaan ini penting: <code>OUTPUT "nama"</code> menampilkan tulisan nama, sedangkan <code>OUTPUT nama</code> menampilkan isinya, misalnya Rina.',
   'Program yang ramah selalu menampilkan <b>prompt</b> (pertanyaan) sebelum INPUT, agar pengguna tahu apa yang harus diketik. Di Flowgorithm dan di visual ini, teks dan variabel digabung dengan tanda <code>&amp;</code>.',
   'Jalankan visual. Ganti input nama dan umur, lalu lihat outputnya berubah tanpa mengubah satu baris pun algoritmanya.'],
   P_IO,
   tb=[{'c': 'INPUT dan OUTPUT di beberapa bahasa', 'h': ['Pseudocode', 'Python', 'Java', 'JavaScript'], 'r': [
     ['INPUT nama', 'nama = input()', 'nama = sc.nextLine();', 'nama = prompt()'], ['INPUT umur (angka)', 'umur = int(input())', 'umur = sc.nextInt();', 'umur = Number(prompt())'],
     ['OUTPUT "Halo ", nama', 'print("Halo", nama)', 'System.out.println("Halo " + nama);', 'console.log("Halo " + nama)']]}],
   pts=['Pola IPO: Input, Proses, Output.', 'Teks pakai kutip, variabel tanpa kutip.', 'Tampilkan prompt sebelum INPUT.'],
   q=quiz(['nama berisi "Budi". Apa hasil OUTPUT "nama"?', ['Budi', 'nama', 'Error'], 1, 'Teks di dalam kutip ditampilkan apa adanya.'],
          ['Kenapa sebaiknya ada OUTPUT pertanyaan sebelum INPUT?', ['Wajib secara aturan', 'Agar pengguna tahu apa yang harus diketik', 'Agar lebih cepat'], 1, 'Prompt membuat program ramah pengguna.'])),
 L('Operasi aritmetika dan urutan operator', [
   '<b>Operator aritmetika</b>: <code>+ - * /</code>, ditambah <code>MOD</code> (sisa bagi, 17 MOD 5 = 2) dan <code>DIV</code> atau <code>Int(a / b)</code> (hasil bagi bulat, 17 DIV 5 = 3). MOD dan DIV sangat sering dipakai: mengecek genap-ganjil, memecah detik menjadi jam, dan mengambil digit terakhir angka.',
   '<b>Urutan operator</b> (precedence) mengikuti matematika: <b>kurung</b> dulu, lalu <b>kali, bagi, MOD, DIV</b>, lalu <b>tambah dan kurang</b>. Operator dengan tingkat sama dihitung dari kiri ke kanan. Jadi <code>2 + 3 * 4</code> = 14, bukan 20, dan <code>(2 + 3) * 4</code> = 20.',
   'Jebakan klasik: rata-rata tiga nilai ditulis <code>a + b + c / 3</code>. Yang dibagi 3 hanya c! Yang benar <code>(a + b + c) / 3</code>. Saat ragu, pakai kurung agar pembaca dan komputer tidak salah tafsir.',
   'Visual mengubah total detik menjadi jam, menit, dan detik. 7384 detik = 2 jam (7200), sisa 184 detik = 3 menit (180), sisa 4 detik. Coba 3661 dan 59.'],
   P_DETIK,
   tb=[_O['Variabel, tipe data, dan operator']['tb'][1], {'c': 'Urutan operator (atas lebih dulu)', 'h': ['Tingkat', 'Operator', 'Contoh'], 'r': [['1', '( )', '(2 + 3) * 4 = 20'], ['2', '* / MOD DIV', '2 + 3 * 4 = 14'], ['3', '+ -', '10 - 4 + 1 = 7 (kiri ke kanan)'], ['4', '= <> < > <= >=', '2 + 3 > 4 → benar'], ['5', 'NOT, lalu AND, lalu OR', 'benar OR salah AND salah → benar']]}],
   pts=['MOD = sisa bagi, DIV = hasil bagi bulat.', 'Kurung, lalu kali-bagi, lalu tambah-kurang.', 'Rata-rata: (a + b + c) / 3, bukan a + b + c / 3.'],
   q=quiz(['Berapa 23 MOD 4?', ['5', '3', '5.75'], 1, '23 = 4 × 5 + 3, sisanya 3.'], ['Berapa 10 - 2 * 3?', ['24', '4', '16'], 1, 'Kali dulu: 2 × 3 = 6, lalu 10 - 6 = 4.'],
          ['Berapa 125 DIV 60?', ['2', '5', '2.08'], 0, 'Hasil bagi bulat: 60 masuk 2 kali.'])),
 L('Algoritma sekuensial pertamamu', [
   'Algoritma <b>sekuensial</b> (runtunan) adalah algoritma yang langkahnya dijalankan berurutan dari atas ke bawah, tepat sekali, tanpa percabangan dan tanpa perulangan. Ini bentuk paling dasar, dan setiap algoritma yang lebih rumit tersusun dari runtunan kecil seperti ini.',
   'Cara menyusunnya: (1) tulis <b>masalahnya</b> dalam satu kalimat, (2) tentukan <b>input</b> dan <b>output</b>, (3) tulis <b>rumus</b> prosesnya, (4) deklarasikan variabel, (5) susun langkahnya, dan (6) <b>uji</b> dengan data yang hasilnya sudah kamu hitung manual.',
   'Urutan langkah menentukan hasil. Jika <code>total ← subtotal + pajak</code> ditulis sebelum <code>pajak</code> dihitung, total akan salah karena pajak belum punya nilai. Itulah inti algoritma sekuensial: setiap langkah hanya boleh memakai nilai yang <b>sudah</b> dihitung di atasnya.',
   'Contoh: struk belanja dengan PPN 11%. Masalah: hitung total bayar. Input: harga dan jumlah. Output: subtotal, PPN, dan total. Hitung manual dulu: 15.000 × 4 = 60.000, PPN 6.600, total 66.600. Lalu jalankan visual dan cocokkan.'],
   P_STRUK,
   tb=[{'c': 'Lembar perencanaan algoritma', 'h': ['Langkah', 'Isi untuk struk belanja'], 'r': [['Masalah', 'Hitung total bayar termasuk PPN 11%'], ['Input', 'harga (INTEGER), jumlah (INTEGER)'], ['Output', 'subtotal, pajak, total'], ['Rumus', 'subtotal = harga × jumlah; pajak = subtotal × 11 / 100; total = subtotal + pajak'], ['Uji manual', '15000 dan 4 → 60000, 6600, 66600']]}],
   pts=['Runtunan: langkah berurutan, masing-masing sekali.', 'Rencanakan masalah, input, output, rumus, lalu uji.', 'Langkah hanya boleh memakai nilai yang sudah dihitung.'],
   q=quiz(['Apa yang terjadi jika total dihitung sebelum pajak?', ['Hasilnya tetap benar', 'Total salah karena pajak belum ada nilainya', 'Program lebih cepat'], 1, 'Urutan langkah menentukan hasil.'],
          ['Kapan sebaiknya menghitung hasil secara manual?', ['Tidak perlu', 'Sebelum menjalankan, untuk mencocokkan', 'Setelah program dipakai pengguna'], 1, 'Tanpa jawaban manual, kamu tidak tahu programnya benar atau tidak.'])),
]},
{'t': 'Percabangan kondisional', 'lvl': 'Pemula', 'd': 'Ekspresi Boolean, IF satu cabang, IF-ELSE, CASE, percabangan bersarang, dan guard clause untuk menangani kesalahan.', 'nodes': ['Percabangan'], 'lessons': [
 R('Operator logika: and, or, not', 'Ekspresi Boolean dan operator logika', b=[
   'Setiap percabangan bergantung pada <b>ekspresi Boolean</b>: ekspresi yang hasilnya hanya <b>benar</b> atau <b>salah</b>. Contoh: <code>nilai &gt;= 75</code>, <code>stok = 0</code>, <code>password &lt;&gt; ""</code>. Hasilnya bisa langsung dipakai di IF atau disimpan dulu di variabel BOOLEAN.'] + _O['Operator logika: and, or, not']['b']),
 L('IF satu cabang', [
   'Bentuk percabangan paling sederhana hanya punya <b>satu jalur</b>: <code>IF kondisi THEN ... ENDIF</code>. Jika kondisi benar, langkah di dalamnya dijalankan. Jika salah, langkah itu <b>dilewati</b> begitu saja dan program lanjut ke baris setelah <code>ENDIF</code>.',
   'Pakai IF satu cabang saat ada langkah <b>tambahan</b> yang hanya terjadi pada kondisi tertentu, sedangkan selain itu tidak ada yang perlu dilakukan. Contoh: memberi bonus, menampilkan peringatan stok menipis, atau menghapus ongkir.',
   'Pola yang sering dipakai: isi <b>nilai bawaan</b> dulu, lalu ubah dengan IF. Pada contoh, <code>ongkir ← 15000</code> sebagai bawaan; hanya jika belanja minimal 100 ribu, ongkir diubah menjadi 0. Cara ini menghindari ELSE dan memastikan variabel selalu punya nilai.',
   'Jalankan dengan 120000, lalu 80000. Perhatikan baris di dalam IF dilewati pada input kedua.'],
   P_ONGKIR,
   pts=['IF tanpa ELSE: jika salah, langkahnya dilewati.', 'Cocok untuk langkah tambahan pada kondisi tertentu.', 'Pola nilai bawaan lalu diubah oleh IF.'],
   q=quiz(['Belanja 80000 pada contoh. Berapa total bayar?', ['80000', '95000', '15000'], 1, 'Ongkir bawaan 15000 tidak diubah.'],
          ['Kapan IF satu cabang paling cocok?', ['Ada langkah tambahan hanya pada kondisi tertentu', 'Harus memilih satu dari dua hasil', 'Ada lima pilihan'], 0, 'Selain kondisi itu, tidak ada yang dilakukan.'])),
 R('IF dan ELSE', 'IF-ELSE: dua jalur'),
 L('CASE: memilih banyak jalur', [
   'Jika pilihan bergantung pada <b>satu nilai yang tepat</b>, misalnya kode menu 1, 2, 3, pakai <code>CASE OF variabel ... OTHERWISE ... ENDCASE</code>. Lebih rapi daripada IF bertingkat yang panjang, karena setiap pilihan berdiri di satu baris.',
   'Bagian <code>OTHERWISE</code> menangani nilai yang tidak terdaftar, misalnya pengguna mengetik 9. <b>Selalu sediakan OTHERWISE</b>: pengguna pasti suatu saat mengetik sesuatu yang tidak kamu duga.',
   'CASE di bahasa nyata: <code>switch</code> di Java, JavaScript, dan Dart; <code>match</code> di Python 3.10+; <code>when</code> di Kotlin. Hati-hati di Java dan JavaScript: setiap <code>case</code> butuh <code>break</code>, jika tidak, eksekusi "jatuh" ke case berikutnya.',
   'Visual di bawah menjalankan logika yang sama dengan IF bertingkat (simulator belum punya simbol CASE). Bandingkan dengan pseudocode CASE di bagian contoh. Coba kode 1, 3, lalu 9.'],
   P_MENU3,
   code='DECLARE kode, harga : INTEGER\nDECLARE menu : STRING\nINPUT kode\nCASE OF kode\n    1 : menu ← "Kopi susu"\n        harga ← 18000\n    2 : menu ← "Teh tarik"\n        harga ← 15000\n    3 : menu ← "Jus jeruk"\n        harga ← 20000\n    OTHERWISE : menu ← "Tidak ada"\n                harga ← 0\nENDCASE\nOUTPUT menu, ": Rp", harga', out='Teh tarik: Rp15000', run=False,
   tb=[{'c': 'CASE atau IF bertingkat?', 'h': ['Situasi', 'Pilihan', 'Alasan'], 'r': [['Kode menu 1, 2, 3', 'CASE', 'Mencocokkan nilai tepat'], ['Nama hari dari angka 1 sampai 7', 'CASE', 'Nilai tepat, banyak pilihan'], ['Nilai 85 ke atas A, 70 ke atas B', 'IF bertingkat', 'Berupa rentang nilai'], ['Dua syarat digabung (hadir dan lunas)', 'IF dengan AND', 'Kondisi gabungan']]}],
   pts=['CASE untuk mencocokkan satu nilai tepat dengan banyak pilihan.', 'Selalu sediakan OTHERWISE.', 'Rentang nilai lebih cocok dengan IF bertingkat.'],
   q=quiz(['Pengguna mengetik 9 pada menu 1 sampai 3. Bagian mana yang jalan?', ['Pilihan 1', 'OTHERWISE', 'Tidak ada'], 1, 'OTHERWISE menangkap nilai yang tidak terdaftar.'],
          ['Menentukan nilai huruf dari angka 0 sampai 100 lebih cocok memakai?', ['CASE', 'IF bertingkat'], 1, 'Berupa rentang, bukan nilai tepat.'])),
 R('Percabangan bertingkat', 'Percabangan bersarang', b=[
   'Jika pilihannya lebih dari dua, kita bisa menaruh IF <b>di dalam</b> IF lain. Ini disebut <b>percabangan bersarang</b> (nested conditional). Ada dua bentuk: <b>berantai</b> (IF di dalam ELSE, seperti nilai huruf A, B, C, D) dan <b>bersarang sungguhan</b> (IF di dalam THEN, misalnya "jika member, cek lagi apakah belanja di atas 200 ribu").',
   'Pada bentuk berantai, kondisi dicek dari atas ke bawah, dan begitu satu kondisi benar, sisanya tidak dicek lagi. Urutan kondisi sangat penting. Jika kita mengecek <code>nilai &gt;= 55</code> lebih dulu, nilai 90 akan mendapat C, karena 90 juga ≥ 55. Aturannya: <b>mulai dari kondisi paling ketat</b> ke yang paling longgar.',
   'Sarang yang terlalu dalam (lebih dari 3 tingkat) sulit dibaca. Tanda bahaya: indentasi terus bergeser ke kanan. Solusinya: gabungkan kondisi dengan AND, pakai CASE, atau pakai <b>guard clause</b> di pelajaran berikutnya.',
   'Uji visual dengan 85, 84, 70, 55, dan 40. Kelima angka itu mencakup setiap jalur dan setiap batas.']),
 L('Guard clause untuk menangani kesalahan', [
   '<b>Guard clause</b> (klausa penjaga) adalah pemeriksaan di <b>awal</b> algoritma yang langsung menolak data yang tidak sah, sebelum logika utama dijalankan. Daripada membungkus seluruh logika di dalam IF yang dalam, kita tangani kasus buruk dulu, lalu keluar.',
   'Contoh: nilai ujian harus 0 sampai 100. Tanpa penjaga, input 120 akan dianggap "Lulus", padahal datanya salah. Dengan penjaga, input di luar rentang langsung dijawab dengan pesan error yang jelas.',
   'Di dalam fungsi, guard clause biasanya memakai <code>RETURN</code> lebih awal, sehingga logika utama tidak perlu menjorok ke dalam. Lihat pseudocode di bagian contoh: setiap penjaga berdiri sendiri, dan logika utama tetap rata kiri.',
   'Kasus yang perlu dijaga: angka di luar rentang, teks kosong, pembagian dengan nol, stok tidak cukup, dan data yang belum diisi. Jalankan visual dengan 120, -5, 80, dan 60.'],
   P_GUARD,
   code='FUNCTION StatusNilai(nilai : INTEGER) RETURNS STRING\n    // penjaga: tolak data tidak sah lebih dulu\n    IF nilai < 0 OR nilai > 100 THEN\n        RETURN "Error: nilai harus 0 sampai 100"\n    ENDIF\n    // logika utama\n    IF nilai >= 75 THEN\n        RETURN "Lulus"\n    ENDIF\n    RETURN "Remedial"\nENDFUNCTION\n\nFUNCTION BagiAman(a : REAL, b : REAL) RETURNS REAL\n    IF b = 0 THEN\n        OUTPUT "Tidak bisa membagi dengan nol"\n        RETURN 0\n    ENDIF\n    RETURN a / b\nENDFUNCTION', out='StatusNilai(120) → Error: nilai harus 0 sampai 100\nStatusNilai(80)  → Lulus\nBagiAman(10, 0)  → Tidak bisa membagi dengan nol', run=False,
   pts=['Tolak data tidak sah di awal.', 'Pesan error harus jelas: apa yang salah dan apa yang benar.', 'Guard clause membuat logika utama tidak menjorok terlalu dalam.'],
   q=quiz(['Tanpa penjaga, nilai 150 pada contoh menghasilkan?', ['Error', 'Lulus', 'Remedial'], 1, '150 >= 75 benar, padahal datanya tidak sah.'],
          ['Di mana guard clause diletakkan?', ['Di akhir algoritma', 'Di awal, sebelum logika utama', 'Di dalam loop terdalam'], 1, 'Tangani kasus buruk dulu.'])),
]},
{'t': 'Proses perulangan', 'lvl': 'Pemula', 'd': 'FOR, WHILE, REPEAT-UNTIL, perbandingan ketiganya dengan contoh sederhana, penghentian loop, loop bersarang, dan pola akumulator.', 'nodes': ['Perulangan'], 'lessons': [
 R('FOR: jumlah putaran sudah diketahui', 'FOR: perulangan pasti', b=[
   'Jika kita tahu persis berapa kali sesuatu harus diulang, pakai <code>FOR i ← awal TO akhir DO ... ENDFOR</code>. Ini disebut <b>perulangan pasti</b> (definite iteration). Variabel <code>i</code> (penghitung) otomatis bertambah 1 setiap putaran sampai melewati nilai akhir.',
   'Contoh paling sederhana, mencetak 1 sampai 5:<br><code>FOR i ← 1 TO 5 DO</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;OUTPUT i</code><br><code>ENDFOR</code><br>Hasilnya 1, 2, 3, 4, 5. Kita tidak perlu menulis <code>i ← i + 1</code>, karena FOR melakukannya sendiri.',
   'Contoh berikutnya: menjumlahkan 1 sampai n. Kita butuh variabel <b>akumulator</b> <code>total</code> yang diisi 0 sebelum loop, lalu ditambah <code>i</code> di setiap putaran. FOR juga bisa mundur atau melompat dengan <code>STEP</code>, misalnya <code>FOR i ← 10 TO 0 STEP -2</code>.',
   'Jalankan visual dan perhatikan kolom variabel: <code>i</code> dan <code>total</code> berubah bersama setiap putaran.']),
 R('WHILE: ulangi selama kondisi benar', 'WHILE: perulangan bersyarat', b=[
   '<code>WHILE kondisi DO ... ENDWHILE</code> memeriksa kondisi <b>sebelum</b> setiap putaran. Selama kondisinya benar, badan loop dijalankan. Pakai WHILE jika jumlah putaran <b>belum diketahui</b>, yang diketahui hanya kapan harus berhenti.',
   'Contoh sederhana, mencetak 1 sampai 5 dengan WHILE:<br><code>i ← 1</code><br><code>WHILE i &lt;= 5 DO</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;OUTPUT i</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;i ← i + 1</code><br><code>ENDWHILE</code><br>Berbeda dengan FOR, di sini kita sendiri yang mengisi nilai awal <code>i</code> dan menaikkannya. Lupa <code>i ← i + 1</code> membuat loop berputar selamanya.',
   'Jika kondisinya sudah salah sejak awal, badan WHILE <b>tidak dijalankan sama sekali</b>. Ini beda penting dengan REPEAT-UNTIL di pelajaran berikutnya.',
   'Visual: menabung 30 ribu per minggu sampai saldo minimal 100 ribu. Berapa minggu? Kita tidak tahu di awal, jadi WHILE yang tepat.']),
 R('REPEAT-UNTIL: jalan minimal sekali', 'REPEAT-UNTIL: dicek di akhir', b=[
   '<code>REPEAT ... UNTIL kondisi</code> menjalankan badan loop <b>dulu</b>, baru memeriksa kondisi di akhir. Loop berhenti saat kondisinya <b>benar</b>. Karena dicek di akhir, badannya pasti jalan <b>minimal sekali</b>. Di Java, JavaScript, C, dan Flowgorithm bentuk ini disebut <b>do-while</b>.',
   'Contoh sederhana, mencetak 1 sampai 5:<br><code>i ← 1</code><br><code>REPEAT</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;OUTPUT i</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;i ← i + 1</code><br><code>UNTIL i &gt; 5</code><br>Perhatikan kondisinya: WHILE memakai <code>i &lt;= 5</code> (syarat lanjut), REPEAT-UNTIL memakai <code>i &gt; 5</code> (syarat berhenti).',
   'Contoh paling tepat: <b>validasi input</b>. Kita harus meminta PIN dulu sebelum bisa memeriksanya. Dengan WHILE, kita terpaksa meminta PIN dua kali (sebelum loop dan di dalam loop). Do-while di Java dan JavaScript <b>lanjut</b> saat kondisi benar (<code>while (pin != 2468)</code>), REPEAT-UNTIL <b>berhenti</b> saat kondisi benar. Keduanya sama, hanya kondisinya dibalik.',
   'Input di visual adalah tiga percobaan: 1111, 1234, lalu 2468. Ubah urutannya, misalnya langsung 2468, dan lihat badan loop tetap jalan sekali.']),
 L('FOR, WHILE, dan DO-WHILE: contoh sederhana dan bedanya', [
   'Ketiga loop bisa menyelesaikan tugas yang sama. Bedanya ada pada <b>kapan kondisi diperiksa</b> dan <b>siapa yang mengurus penghitung</b>. Contoh di bawah mencetak 1 sampai 5 dengan ketiganya, dan hasilnya identik: 1 2 3 4 5.',
   '<b>FOR</b>: penghitung diurus otomatis, cocok jika jumlah putaran pasti (cetak 10 baris, proses 30 mahasiswa). <b>WHILE</b>: kondisi dicek <b>di awal</b>, jadi bisa jalan 0 kali; cocok jika jumlah putaran belum diketahui (menabung sampai target, membaca data sampai habis). <b>DO-WHILE / REPEAT-UNTIL</b>: kondisi dicek <b>di akhir</b>, jadi pasti jalan minimal 1 kali; cocok untuk menu dan validasi input.',
   'Perbedaan paling terasa muncul saat kondisi <b>sudah salah sejak awal</b>. Visual di bawah menjalankan ketiga loop dengan nilai awal <code>n</code>. Jalankan dengan n = 1: ketiganya mencetak 1 sampai 5. Lalu ganti n = <b>10</b>: FOR dan WHILE tidak mencetak apa pun, sedangkan DO-WHILE tetap mencetak 10 satu kali, karena badannya jalan dulu sebelum kondisi diperiksa.',
   'Cara memilih cepat: tanyakan "apakah aku tahu berapa kali?" Jika ya, FOR. Jika tidak, tanyakan "apakah badannya harus jalan minimal sekali?" Jika ya, DO-WHILE; jika tidak, WHILE.'],
   P_BEDA,
   code='// 1) FOR: penghitung otomatis\nFOR i ← 1 TO 5 DO\n    OUTPUT i\nENDFOR\n\n// 2) WHILE: cek di awal, bisa 0 kali\ni ← 1\nWHILE i <= 5 DO\n    OUTPUT i\n    i ← i + 1\nENDWHILE\n\n// 3) DO-WHILE (REPEAT-UNTIL): cek di akhir, minimal 1 kali\ni ← 1\nREPEAT\n    OUTPUT i\n    i ← i + 1\nUNTIL i > 5', out='Ketiganya mencetak:\n1\n2\n3\n4\n5', run=False,
   tb=[{'c': 'Perbandingan FOR, WHILE, dan DO-WHILE', 'h': ['Aspek', 'FOR', 'WHILE', 'DO-WHILE / REPEAT-UNTIL'], 'r': [
     ['Jumlah putaran', 'Sudah diketahui', 'Belum diketahui', 'Belum diketahui'], ['Kondisi dicek', 'Di awal (otomatis)', 'Di awal', 'Di akhir'],
     ['Minimal jalan', '0 kali', '0 kali', '1 kali'], ['Penghitung', 'Diurus otomatis', 'Diurus sendiri', 'Diurus sendiri'],
     ['Risiko umum', 'Batas salah (off-by-one)', 'Lupa mengubah kondisi', 'Kondisi terbalik'], ['Contoh pemakaian', 'Cetak tabel perkalian', 'Menabung sampai target', 'Menu dan validasi PIN']]},
     {'c': 'Cetak 1 sampai 5 di tiga bahasa', 'h': ['Loop', 'Python', 'Java', 'JavaScript'], 'r': [
     ['FOR', 'for i in range(1, 6): print(i)', 'for (int i = 1; i <= 5; i++) System.out.println(i);', 'for (let i = 1; i <= 5; i++) console.log(i)'],
     ['WHILE', 'i = 1\nwhile i <= 5: print(i); i += 1', 'int i = 1; while (i <= 5) { System.out.println(i); i++; }', 'let i = 1; while (i <= 5) { console.log(i); i++ }'],
     ['DO-WHILE', 'i = 1\nwhile True: print(i); i += 1; if i > 5: break', 'int i = 1; do { System.out.println(i); i++; } while (i <= 5);', 'let i = 1; do { console.log(i); i++ } while (i <= 5)']]},
     {'c': 'Jika nilai awal sudah melewati batas (n = 10)', 'h': ['Loop', 'Yang tercetak', 'Alasan'], 'r': [['FOR i ← 10 TO 5', 'Tidak ada', '10 sudah melewati 5'], ['WHILE i <= 5', 'Tidak ada', 'Kondisi salah sejak awal'], ['REPEAT ... UNTIL i > 5', '10', 'Badan jalan dulu, baru dicek']]}],
   pts=['Ketiga loop bisa mengerjakan tugas yang sama.', 'FOR: jumlah pasti. WHILE: cek di awal, bisa 0 kali. DO-WHILE: cek di akhir, minimal 1 kali.', 'Python tidak punya do-while; pakai while True dengan break.'],
   q=quiz(['i ← 10, lalu WHILE i <= 5 DO OUTPUT i. Berapa kali OUTPUT jalan?', ['0', '1', '5'], 0, 'Kondisi dicek di awal dan langsung salah.'],
          ['i ← 10, lalu REPEAT OUTPUT i ... UNTIL i > 5. Berapa kali OUTPUT jalan?', ['0', '1', '5'], 1, 'Badan jalan dulu, baru kondisi dicek.'],
          ['Mencetak daftar 40 mahasiswa paling cocok memakai?', ['FOR', 'WHILE', 'DO-WHILE'], 0, 'Jumlahnya sudah diketahui.'],
          ['Meminta password sampai benar paling cocok memakai?', ['FOR', 'DO-WHILE'], 1, 'Harus meminta minimal sekali, jumlah percobaan belum diketahui.'])),
 L('Penghentian loop dan infinite loop', [
   'Setiap loop harus punya <b>kondisi berhenti</b> yang pasti tercapai. Tiga syaratnya: (1) variabel kondisi <b>diberi nilai awal</b>, (2) variabel itu <b>berubah</b> di dalam badan loop, dan (3) perubahannya <b>menuju</b> kondisi berhenti. Jika salah satunya hilang, terjadi <b>infinite loop</b>: program berputar selamanya dan tampak "hang".',
   'Contoh infinite loop: <code>i ← 1; WHILE i &lt;= 5 DO OUTPUT i ENDWHILE</code> (lupa menaikkan i). Atau <code>i ← 1; WHILE i &lt;&gt; 10 DO i ← i + 2 ENDWHILE</code>: i bernilai 1, 3, 5, 7, 9, 11, ... dan tidak pernah tepat 10. Pakai <code>&lt;</code> atau <code>&lt;=</code> daripada <code>&lt;&gt;</code> untuk kondisi berhenti.',
   'Cara lain menghentikan loop: <b>sentinel</b> (nilai khusus seperti 0 atau -1 yang berarti "selesai"), <b>flag</b> (variabel BOOLEAN <code>ketemu</code> yang diubah menjadi benar), dan <b>batas pengaman</b> (maksimal 3 kali percobaan PIN). Banyak bahasa juga punya <code>break</code> untuk keluar paksa.',
   'Visual menghitung banyak digit: n dibagi 10 terus sampai habis. Loop ini pasti berhenti karena n selalu mengecil dan suatu saat menjadi 0. Coba 7, 1000, dan 0.'],
   P_DIGIT,
   tb=[{'c': 'Mencari penyebab infinite loop', 'h': ['Kode', 'Masalah', 'Perbaikan'], 'r': [['WHILE i <= 5 DO OUTPUT i', 'i tidak pernah berubah', 'Tambahkan i ← i + 1'], ['WHILE i <> 10 DO i ← i + 2', 'i melompati 10', 'Pakai WHILE i < 10'], ['WHILE i > 0 DO i ← i + 1', 'i menjauhi kondisi berhenti', 'Pakai i ← i - 1'], ['REPEAT ... UNTIL x > 5 tanpa mengubah x', 'Kondisi tidak pernah berubah', 'Ubah x di badan loop']]}],
   pts=['Nilai awal, berubah, dan menuju kondisi berhenti.', 'Hindari <> sebagai kondisi berhenti angka.', 'Sentinel, flag, dan batas pengaman.'],
   q=quiz(['i ← 0; WHILE i <> 7 DO i ← i + 2. Apa yang terjadi?', ['Berhenti di 7', 'Infinite loop', 'Tidak jalan sama sekali'], 1, 'i: 0, 2, 4, 6, 8, ... tidak pernah tepat 7.'],
          ['Apa itu nilai sentinel?', ['Nilai khusus penanda akhir input', 'Nilai terbesar', 'Batas memori'], 0, 'Contoh: ketik 0 untuk selesai.'])),
 _O['Loop bersarang'],
 L('Pola akumulator', [
   '<b>Akumulator</b> adalah variabel yang <b>mengumpulkan</b> hasil selama loop berjalan. Polanya selalu sama: (1) beri nilai awal <b>sebelum</b> loop, (2) perbarui <b>di dalam</b> loop, (3) pakai hasilnya <b>setelah</b> loop.',
   'Empat akumulator yang paling sering: <b>penjumlah</b> (<code>total ← 0</code>, lalu <code>total ← total + x</code>), <b>penghitung</b> (<code>lulus ← 0</code>, lalu <code>lulus ← lulus + 1</code> jika syarat terpenuhi), <b>pengali</b> (<code>hasil ← 1</code>, lalu <code>hasil ← hasil * x</code>, misalnya faktorial), dan <b>pencari ekstrem</b> (maksimum atau minimum).',
   'Nilai awal harus sesuai jenisnya: penjumlah dan penghitung mulai dari <b>0</b>, pengali mulai dari <b>1</b> (jika 0, hasilnya selalu 0). Untuk maksimum, ambil data <b>pertama</b> sebagai nilai awal; pada contoh dipakai kondisi <code>i = 1 OR x &gt; maks</code> agar data pertama langsung menjadi maks.',
   'Visual membaca 5 nilai dan menghitung empat hal sekaligus dalam satu loop. Coba ganti nilai-nilainya dan prediksi hasilnya sebelum menekan Jalankan.'],
   P_AKUM,
   tb=[{'c': 'Jenis akumulator', 'h': ['Jenis', 'Nilai awal', 'Di dalam loop', 'Contoh'], 'r': [['Penjumlah', '0', 'total ← total + x', 'Total belanja'], ['Penghitung', '0', 'IF syarat THEN n ← n + 1', 'Jumlah yang lulus'], ['Pengali', '1', 'hasil ← hasil * x', 'Faktorial, pangkat'], ['Maksimum', 'Data pertama', 'IF x > maks THEN maks ← x', 'Nilai tertinggi'], ['Penggabung teks', '""', 's ← s & x', 'Membuat baris bintang']]}],
   pts=['Nilai awal sebelum loop, perbarui di dalam, pakai setelahnya.', 'Penjumlah 0, pengali 1, maksimum dari data pertama.', 'Satu loop bisa mengurus beberapa akumulator.'],
   q=quiz(['Nilai awal yang benar untuk menghitung faktorial?', ['0', '1', 'n'], 1, 'Jika 0, hasil perkalian selalu 0.'],
          ['Nilai 80, 65, 92, 75, 58. Berapa yang lulus (≥ 75)?', ['2', '3', '4'], 1, '80, 92, dan 75.'])),
]},
{'t': 'Desain modular', 'lvl': 'Menengah', 'd': 'Dekomposisi top-down, fungsi dan nilai kembali, prosedur, parameter by value dan by reference, ruang lingkup variabel, dan rekursi.', 'nodes': ['Fungsi', 'Rekursi'], 'lessons': [
 L('Dekomposisi top-down', [
   '<b>Dekomposisi top-down</b> adalah memecah masalah besar menjadi sub-masalah yang lebih kecil, lalu memecahnya lagi sampai setiap bagian cukup sederhana untuk ditulis langsung. Mulai dari gambaran besar ("buat kasir"), turun ke langkah utama ("baca belanjaan, hitung diskon, hitung kembalian"), lalu ke detail.',
   'Setiap sub-masalah menjadi satu <b>modul</b> (prosedur atau fungsi) dengan satu tugas jelas. Program utama cukup memanggil modul-modul itu, sehingga terbaca seperti daftar isi. Modul bisa dikerjakan, diuji, dan diperbaiki terpisah, bahkan oleh orang yang berbeda.',
   'Visual menjalankan kasir dalam satu blok panjang. Bagian contoh menunjukkan kasir yang sama setelah didekomposisi: program utama hanya empat baris, dan detailnya ada di fungsi masing-masing. Logikanya identik, tetapi jauh lebih mudah dibaca dan diubah.',
   'Jalankan visual dengan input bawaan: 2 kopi seharga 25.000, 3 roti seharga 18.000, selesai (0), lalu bayar 150.000.'],
   P_KASIR,
   code='// Program utama: terbaca seperti daftar isi\nSTART\n    total ← BacaBelanjaan()\n    total ← TerapkanDiskon(total)\n    OUTPUT "Total: ", total\n    CALL ProsesPembayaran(total)\nEND\n\nFUNCTION BacaBelanjaan() RETURNS INTEGER\n    DECLARE harga, jumlah, total : INTEGER\n    total ← 0\n    REPEAT\n        INPUT harga\n        IF harga > 0 THEN\n            INPUT jumlah\n            total ← total + harga * jumlah\n        ENDIF\n    UNTIL harga = 0\n    RETURN total\nENDFUNCTION\n\nFUNCTION TerapkanDiskon(total : INTEGER) RETURNS INTEGER\n    IF total > 100000 THEN\n        RETURN total - total * 10 DIV 100\n    ENDIF\n    RETURN total\nENDFUNCTION\n\nPROCEDURE ProsesPembayaran(total : INTEGER)\n    DECLARE bayar : INTEGER\n    INPUT bayar\n    IF bayar >= total THEN\n        OUTPUT "Kembalian: ", bayar - total\n    ELSE\n        OUTPUT "Uang kurang ", total - bayar\n    ENDIF\nENDPROCEDURE', out='Total: 93600\nKembalian: 56400', run=False,
   tb=[{'c': 'Pohon dekomposisi kasir', 'h': ['Tingkat', 'Modul', 'Tugas'], 'r': [['0', 'Kasir', 'Seluruh transaksi'], ['1', 'BacaBelanjaan', 'Ulangi baca harga dan jumlah sampai 0'], ['1', 'TerapkanDiskon', 'Potong 10% jika total > 100 ribu'], ['1', 'ProsesPembayaran', 'Terima uang, hitung kembalian atau kekurangan']]}],
   pts=['Pecah masalah besar menjadi sub-masalah kecil.', 'Satu modul, satu tugas.', 'Program utama terbaca seperti daftar isi.'],
   q=quiz(['Apa langkah pertama dekomposisi top-down?', ['Menulis detail terkecil', 'Menentukan gambaran besar lalu langkah utamanya', 'Memilih bahasa pemrograman'], 1, 'Dari atas ke bawah.'],
          ['Keuntungan memecah kasir menjadi modul?', ['Program pasti lebih cepat', 'Setiap bagian bisa diuji dan diubah terpisah', 'Tidak butuh variabel'], 1, 'Satu modul, satu tugas.'])),
 R('Prosedur dan fungsi', 'Fungsi dan nilai kembali', b=[
   '<b>Fungsi</b> adalah modul yang menerima input lewat <b>parameter</b>, menghitung, lalu <b>mengembalikan satu nilai</b> dengan <code>RETURN</code>. Bentuknya: <code>FUNCTION Nama(parameter : TIPE) RETURNS TIPE ... ENDFUNCTION</code>.',
   'Nilai kembali bisa langsung dipakai di ekspresi: <code>luas ← Luas(8, 5)</code>, <code>OUTPUT Luas(3, 4) + 10</code>, atau <code>IF Luas(p, l) &gt; 100 THEN</code>. Begitu <code>RETURN</code> dijalankan, fungsi <b>langsung selesai</b>; baris di bawahnya tidak dijalankan.',
   'Fungsi yang baik itu <b>murni</b>: hasilnya hanya bergantung pada parameternya, dan ia tidak menampilkan apa pun atau mengubah variabel di luar. Fungsi murni mudah diuji: <code>Luas(8, 5)</code> selalu 40. Jika ingin menampilkan sesuatu, serahkan ke pemanggilnya atau ke prosedur.'],
   code='FUNCTION Luas(p : INTEGER, l : INTEGER) RETURNS INTEGER\n    RETURN p * l\nENDFUNCTION\n\nFUNCTION HargaSetelahDiskon(harga : REAL, persen : REAL) RETURNS REAL\n    RETURN harga - harga * persen / 100\nENDFUNCTION\n\nSTART\n    OUTPUT Luas(8, 5)\n    OUTPUT Luas(3, 4) + 10\n    OUTPUT HargaSetelahDiskon(200000, 15)\nEND', out='40\n22\n170000',
   tb=[{'c': 'Anatomi fungsi', 'h': ['Bagian', 'Contoh', 'Arti'], 'r': [['Nama', 'Luas', 'Kata kerja atau kata benda yang jelas'], ['Parameter', 'p : INTEGER, l : INTEGER', 'Data yang diterima'], ['Tipe kembali', 'RETURNS INTEGER', 'Jenis nilai yang dikembalikan'], ['RETURN', 'RETURN p * l', 'Mengirim hasil dan mengakhiri fungsi'], ['Pemanggilan', 'x ← Luas(8, 5)', 'Argumen 8 dan 5 masuk ke p dan l']]}],
   pts=['Fungsi mengembalikan satu nilai dengan RETURN.', 'RETURN langsung mengakhiri fungsi.', 'Fungsi murni mudah diuji.'],
   q=quiz(['Apa yang dicetak OUTPUT Luas(2, 3) * 2?', ['6', '12', '23'], 1, 'Luas(2, 3) = 6, lalu × 2.'],
          ['Baris setelah RETURN di dalam fungsi yang sama...', ['Tetap dijalankan', 'Tidak dijalankan', 'Dijalankan dua kali'], 1, 'RETURN mengakhiri fungsi.'])),
 L('Prosedur untuk efek samping', [
   '<b>Prosedur</b> adalah modul yang <b>tidak mengembalikan nilai</b>. Ia dipanggil karena <b>efek samping</b>-nya: menampilkan sesuatu ke layar, mencetak struk, menyimpan data, atau mengubah isi variabel yang dikirim kepadanya. Dipanggil dengan <code>CALL NamaProsedur(argumen)</code>.',
   'Bedanya dengan fungsi: fungsi <b>menjawab pertanyaan</b> ("berapa luasnya?"), prosedur <b>melakukan pekerjaan</b> ("cetak garis sepanjang 20"). Karena tidak ada nilai kembali, prosedur tidak bisa dipakai di dalam ekspresi: <code>x ← CetakGaris(3)</code> salah.',
   'Pisahkan perhitungan dari tampilan. Hitung dengan fungsi, tampilkan dengan prosedur. Contoh: <code>total ← HitungTotal(...)</code> lalu <code>CALL CetakStruk(total)</code>. Dengan begitu, fungsi perhitungan bisa dipakai ulang di aplikasi web, mobile, maupun konsol.'],
   code='PROCEDURE CetakGaris(n : INTEGER)\n    DECLARE i : INTEGER\n    DECLARE s : STRING\n    s ← ""\n    FOR i ← 1 TO n DO\n        s ← s & "-"\n    ENDFOR\n    OUTPUT s\nENDPROCEDURE\n\nPROCEDURE CetakStruk(nama : STRING, total : INTEGER)\n    CALL CetakGaris(20)\n    OUTPUT "Pelanggan: ", nama\n    OUTPUT "Total    : Rp", total\n    CALL CetakGaris(20)\nENDPROCEDURE\n\nSTART\n    CALL CetakStruk("Rina", 66600)\nEND', out='--------------------\nPelanggan: Rina\nTotal    : Rp66600\n--------------------', run=False,
   tb=[_O['Prosedur dan fungsi']['tb'][0]],
   pts=['Prosedur dipanggil karena efek sampingnya.', 'Prosedur tidak bisa dipakai di dalam ekspresi.', 'Hitung dengan fungsi, tampilkan dengan prosedur.'],
   q=quiz(['Mencetak kop surat lebih cocok dibuat sebagai?', ['Fungsi', 'Prosedur'], 1, 'Pekerjaannya menampilkan, tidak mengembalikan nilai.'],
          ['Mana pemanggilan yang SALAH?', ['CALL CetakGaris(5)', 'x ← CetakGaris(5)', 'CALL CetakStruk("Andi", 1000)'], 1, 'Prosedur tidak punya nilai kembali.'])),
 L('Parameter by value dan by reference', [
   'Ada dua cara mengirim data ke modul. <b>By value</b> (BYVAL): modul menerima <b>salinan</b> nilai. Mengubah parameter di dalam modul tidak mengubah variabel asli di pemanggil. Ini cara bawaan dan paling aman.',
   '<b>By reference</b> (BYREF): modul menerima <b>alamat</b> variabel asli. Mengubah parameter berarti mengubah variabel pemanggil. Dipakai saat modul memang harus mengubah data pemanggil, misalnya prosedur <code>Tukar(a, b)</code> yang menukar isi dua variabel.',
   'Analogi: by value seperti memberi <b>fotokopi</b> dokumen, coretan di fotokopi tidak mengubah aslinya. By reference seperti meminjamkan <b>dokumen asli</b>.',
   'Di bahasa nyata: Java dan Python mengirim tipe dasar (int, float) secara by value. Objek dan list dikirim sebagai <b>salinan referensi</b>, sehingga isi list bisa diubah dari dalam fungsi. C++ dan C# punya penanda eksplisit (<code>&amp;</code>, <code>ref</code>).'],
   code='PROCEDURE NaikkanByVal(BYVAL x : INTEGER)\n    x ← x + 10\n    OUTPUT "Di dalam: ", x\nENDPROCEDURE\n\nPROCEDURE NaikkanByRef(BYREF x : INTEGER)\n    x ← x + 10\nENDPROCEDURE\n\nPROCEDURE Tukar(BYREF a : INTEGER, BYREF b : INTEGER)\n    DECLARE t : INTEGER\n    t ← a\n    a ← b\n    b ← t\nENDPROCEDURE\n\nSTART\n    nilai ← 5\n    CALL NaikkanByVal(nilai)\n    OUTPUT "Setelah ByVal: ", nilai\n    CALL NaikkanByRef(nilai)\n    OUTPUT "Setelah ByRef: ", nilai\n    p ← 1\n    q ← 2\n    CALL Tukar(p, q)\n    OUTPUT p, " ", q\nEND', out='Di dalam: 15\nSetelah ByVal: 5\nSetelah ByRef: 15\n2 1', run=False,
   tb=[{'c': 'By value vs by reference', 'h': ['Aspek', 'BYVAL', 'BYREF'], 'r': [['Yang dikirim', 'Salinan nilai', 'Alamat variabel asli'], ['Variabel pemanggil', 'Tidak berubah', 'Ikut berubah'], ['Keamanan', 'Aman dari perubahan tak sengaja', 'Harus hati-hati'], ['Contoh', 'Luas(p, l)', 'Tukar(a, b)']]}],
   pts=['BYVAL mengirim salinan, aslinya aman.', 'BYREF mengirim alamat, aslinya ikut berubah.', 'Pakai BYREF hanya jika modul memang harus mengubah data pemanggil.'],
   q=quiz(['x ← 3; CALL Gandakan(x) dengan BYVAL, di dalamnya x ← x * 2. Berapa x setelahnya?', ['3', '6'], 0, 'Yang diubah hanya salinannya.'],
          ['Prosedur Tukar(a, b) harus memakai?', ['BYVAL', 'BYREF'], 1, 'Tujuannya memang mengubah variabel pemanggil.'])),
 L('Ruang lingkup variabel dan enkapsulasi state', [
   '<b>Ruang lingkup</b> (scope) menentukan di mana sebuah variabel bisa dipakai. Variabel <b>lokal</b> dideklarasikan di dalam modul dan hanya hidup selama modul itu berjalan; setelah modul selesai, variabelnya hilang. Variabel <b>global</b> dideklarasikan di luar semua modul dan bisa dibaca serta diubah dari mana saja.',
   'Variabel global terlihat praktis, tetapi berbahaya: jika ada bug, <b>modul mana pun</b> bisa menjadi penyebabnya. Aturan praktis: pakai variabel lokal dan parameter, kirim data masuk lewat parameter dan keluar lewat RETURN.',
   'Dua modul boleh punya variabel lokal dengan <b>nama sama</b> tanpa saling mengganggu. <code>i</code> di prosedur A dan <code>i</code> di prosedur B adalah dua kotak berbeda.',
   '<b>Enkapsulasi state</b> berarti menyembunyikan data di balik modul, dan hanya mengizinkan perubahan lewat modul itu. Contoh: saldo rekening hanya boleh berubah lewat <code>Setor</code> dan <code>Tarik</code>, yang memeriksa aturan (penarikan tidak boleh melebihi saldo). Inilah benih dari konsep <b>class</b> dan <b>object</b> di Java, Kotlin, Dart, dan Python.'],
   code='DECLARE saldo : INTEGER          // state, hanya diubah lewat Setor dan Tarik\nsaldo ← 0\n\nPROCEDURE Setor(jumlah : INTEGER)\n    IF jumlah <= 0 THEN\n        OUTPUT "Jumlah setoran tidak sah"\n    ELSE\n        saldo ← saldo + jumlah\n    ENDIF\nENDPROCEDURE\n\nPROCEDURE Tarik(jumlah : INTEGER)\n    IF jumlah > saldo THEN\n        OUTPUT "Saldo tidak cukup"\n    ELSE\n        saldo ← saldo - jumlah\n    ENDIF\nENDPROCEDURE\n\nFUNCTION Hitung() RETURNS INTEGER\n    DECLARE i, total : INTEGER   // lokal: hilang setelah fungsi selesai\n    total ← 0\n    FOR i ← 1 TO 3 DO\n        total ← total + i\n    ENDFOR\n    RETURN total\nENDFUNCTION\n\nSTART\n    CALL Setor(50000)\n    CALL Tarik(80000)\n    CALL Tarik(20000)\n    OUTPUT "Saldo: ", saldo\n    OUTPUT Hitung()\nEND', out='Saldo tidak cukup\nSaldo: 30000\n6', run=False,
   tb=[{'c': 'Lokal vs global', 'h': ['Aspek', 'Lokal', 'Global'], 'r': [['Dideklarasikan', 'Di dalam modul', 'Di luar semua modul'], ['Bisa dipakai', 'Hanya di modul itu', 'Di mana saja'], ['Umur', 'Selama modul berjalan', 'Selama program berjalan'], ['Risiko', 'Rendah', 'Bug sulit dilacak']]}],
   pts=['Variabel lokal hanya hidup di modulnya.', 'Hindari global; pakai parameter dan RETURN.', 'Enkapsulasi: state hanya diubah lewat modul yang memeriksa aturan.'],
   q=quiz(['Variabel total di dalam fungsi Hitung bisa dibaca dari program utama?', ['Ya', 'Tidak'], 1, 'total adalah variabel lokal.'],
          ['Kenapa saldo hanya boleh diubah lewat Setor dan Tarik?', ['Agar aturan seperti saldo cukup selalu diperiksa', 'Agar lebih cepat', 'Aturan bahasa'], 0, 'Inilah enkapsulasi.'])),
 L('Rekursi dan base case', [
   '<b>Rekursi</b> adalah fungsi yang <b>memanggil dirinya sendiri</b> dengan masalah yang lebih kecil. Contoh: faktorial. 5! = 5 × 4!, 4! = 4 × 3!, dan seterusnya sampai 1! = 1.',
   'Setiap fungsi rekursif wajib punya dua bagian. <b>Base case</b> (kasus dasar): kondisi berhenti yang dijawab langsung tanpa memanggil diri sendiri, misalnya <code>IF n &lt;= 1 THEN RETURN 1</code>. <b>Recursive case</b>: memanggil diri sendiri dengan input yang <b>mendekati</b> base case, misalnya <code>RETURN n * Faktorial(n - 1)</code>.',
   'Tanpa base case, atau jika inputnya tidak mendekati base case, fungsi memanggil dirinya terus sampai memori tumpukan (call stack) habis: <b>stack overflow</b>. Ini versi rekursi dari infinite loop.',
   'Rekursi cocok untuk masalah yang bentuknya berulang ke dalam: struktur folder, pohon menu, binary search, dan Menara Hanoi. Untuk hitungan sederhana, versi loop biasanya lebih hemat memori. Visual di bawah menghitung faktorial dengan loop; bandingkan dengan versi rekursif di bagian contoh.'],
   P_FAKT,
   code='FUNCTION Faktorial(n : INTEGER) RETURNS INTEGER\n    IF n <= 1 THEN            // base case\n        RETURN 1\n    ENDIF\n    RETURN n * Faktorial(n - 1)   // recursive case\nENDFUNCTION\n\nFUNCTION Pangkat(a : INTEGER, b : INTEGER) RETURNS INTEGER\n    IF b = 0 THEN\n        RETURN 1\n    ENDIF\n    RETURN a * Pangkat(a, b - 1)\nENDFUNCTION\n\nSTART\n    OUTPUT Faktorial(5)\n    OUTPUT Pangkat(2, 10)\nEND', out='120\n1024', run=False,
   tb=[{'c': 'Jejak Faktorial(4)', 'h': ['Panggilan', 'Menunggu', 'Kembali'], 'r': [['Faktorial(4)', '4 × Faktorial(3)', '24'], ['Faktorial(3)', '3 × Faktorial(2)', '6'], ['Faktorial(2)', '2 × Faktorial(1)', '2'], ['Faktorial(1)', 'base case', '1']]}],
   pts=['Rekursi: fungsi memanggil dirinya dengan masalah lebih kecil.', 'Wajib ada base case.', 'Input harus mendekati base case, jika tidak terjadi stack overflow.'],
   q=quiz(['Apa base case pada Pangkat(a, b)?', ['b = 0', 'a = 0', 'b = 1'], 0, 'a pangkat 0 = 1.'],
          ['Fungsi rekursif tanpa base case akan...', ['Mengembalikan 0', 'Memanggil dirinya terus sampai stack overflow', 'Berhenti sendiri'], 1, 'Tidak ada kondisi berhenti.'])),
]},
{'t': 'Koleksi data', 'lvl': 'Menengah', 'd': 'Array satu dimensi, indeks dan traversal, array multidimensi, record, linear dan binary search, bubble sort dan insertion sort.', 'nodes': ['Array', 'Searching', 'Sorting'], 'lessons': [
 R('Array: banyak nilai dalam satu nama', 'Array satu dimensi'),
 L('Indeks, traversal, dan memperbarui array', [
   '<b>Indeks</b> adalah nomor kotak di array. Di kebanyakan bahasa, indeks dimulai dari 0, sehingga array berisi n data punya indeks 0 sampai n - 1. <code>harga[2]</code> berarti kotak <b>ketiga</b>. Beberapa buku pseudocode memakai indeks mulai 1; selalu periksa konvensi yang dipakai.',
   '<b>Traversal</b> berarti mengunjungi setiap isi array satu per satu, biasanya dengan FOR. Maju: <code>FOR i ← 0 TO n - 1</code>. Mundur: <code>FOR i ← n - 1 TO 0 STEP -1</code>. Hampir semua algoritma array (jumlah, cari, hitung, urutkan) adalah traversal ditambah sedikit logika.',
   '<b>Memperbarui</b> isi array sama seperti mengisi variabel, tetapi dengan indeks: <code>harga[i] ← harga[i] + 1000</code>. Di dalam traversal, kita bisa memperbarui setiap isi sekaligus, misalnya menaikkan semua harga 10%.',
   'Visual menaikkan lima harga sebesar 10%, lalu menampilkannya dari indeks terakhir ke indeks pertama (traversal mundur).'],
   P_UPDATE,
   tb=[{'c': 'Pola traversal', 'h': ['Tujuan', 'Pseudocode'], 'r': [['Maju semua', 'FOR i ← 0 TO n - 1'], ['Mundur semua', 'FOR i ← n - 1 TO 0 STEP -1'], ['Indeks genap saja', 'FOR i ← 0 TO n - 1 STEP 2'], ['Mulai dari kedua', 'FOR i ← 1 TO n - 1'], ['Pasangan bersebelahan', 'FOR i ← 0 TO n - 2 (pakai a[i] dan a[i + 1])']]}],
   pts=['Indeks 0 sampai n - 1.', 'Traversal: kunjungi setiap isi dengan FOR.', 'Perbarui isi dengan a[i] ← ...'],
   q=quiz(['Array 8 data. Traversal mundur dimulai dari indeks?', ['8', '7', '0'], 1, 'Indeks terakhir = n - 1.'],
          ['Untuk membandingkan a[i] dengan a[i + 1], batas akhir FOR adalah?', ['n - 1', 'n - 2', 'n'], 1, 'Agar a[i + 1] tidak keluar dari array.'])),
 L('Array multidimensi', [
   '<b>Array dua dimensi</b> (matriks) menyimpan data dalam bentuk <b>tabel</b>: baris dan kolom. Contoh: nilai 3 siswa untuk 4 mata pelajaran, <code>DECLARE nilai : ARRAY[0..2, 0..3] OF INTEGER</code>. Satu isi diakses dengan dua indeks: <code>nilai[baris][kolom]</code> atau <code>nilai[baris, kolom]</code>.',
   'Traversal matriks memakai <b>loop bersarang</b>: loop luar untuk baris, loop dalam untuk kolom. Total isi = jumlah baris × jumlah kolom. Pada contoh 3 × 4 = 12 nilai.',
   'Pemakaian nyata: papan permainan (catur, tic-tac-toe), kursi bioskop, peta grid, gambar (setiap piksel), dan spreadsheet. Array tiga dimensi juga ada (misalnya nilai per siswa, per mapel, per semester), tetapi jarang dipakai.',
   'Visual menghitung total dan rata-rata setiap siswa (setiap baris). Perhatikan <code>total</code> diisi 0 lagi di <b>awal setiap baris</b>, bukan sekali di awal program.'],
   P_MATRIX,
   tb=[{'c': 'Matriks nilai[3][4]', 'h': ['', 'Kolom 0', 'Kolom 1', 'Kolom 2', 'Kolom 3'], 'r': [['Baris 0', '80', '75', '90', '85'], ['Baris 1', '60', '70', '65', '80'], ['Baris 2', '95', '88', '92', '90']]}],
   pts=['Matriks = baris × kolom, akses dengan dua indeks.', 'Traversal dengan loop bersarang.', 'Reset akumulator per baris jika menghitung per baris.'],
   q=quiz(['Pada tabel di atas, nilai[1][3] adalah?', ['85', '80', '65'], 1, 'Baris 1 (kedua), kolom 3 (keempat).'],
          ['Matriks 5 baris × 6 kolom berisi berapa data?', ['11', '30', '56'], 1, '5 × 6 = 30.'])),
 L('Struktur record', [
   'Array menyimpan banyak data <b>sejenis</b>. <b>Record</b> (struct) menyimpan beberapa data <b>berbeda jenis</b> yang menjadi satu kesatuan. Contoh: satu mahasiswa punya NIM (STRING), nama (STRING), IPK (REAL), dan status aktif (BOOLEAN).',
   'Record didefinisikan sebagai <b>tipe baru</b>: <code>TYPE Mahasiswa ... ENDTYPE</code>. Setiap bagian disebut <b>field</b>, diakses dengan titik: <code>mhs.nama</code>, <code>mhs.ipk</code>.',
   'Kekuatan sebenarnya muncul saat record digabung dengan array: <code>ARRAY[0..29] OF Mahasiswa</code> menyimpan data satu kelas. Tanpa record, kita butuh empat array terpisah (nim[], nama[], ipk[], aktif[]) yang harus dijaga agar indeksnya selalu sejajar, dan itu rawan salah.',
   'Record adalah cikal bakal <code>class</code> di Java dan Kotlin, <code>data class</code> di Kotlin, <code>dataclass</code> di Python, <code>interface</code> atau object di TypeScript, dan baris tabel di SQL.'],
   code='TYPE Mahasiswa\n    nim   : STRING\n    nama  : STRING\n    ipk   : REAL\n    aktif : BOOLEAN\nENDTYPE\n\nDECLARE kelas : ARRAY[0..2] OF Mahasiswa\nDECLARE i : INTEGER\nDECLARE terbaik : Mahasiswa\n\nkelas[0] ← Mahasiswa("2301", "Rina", 3.62, TRUE)\nkelas[1] ← Mahasiswa("2302", "Budi", 3.15, TRUE)\nkelas[2] ← Mahasiswa("2303", "Sari", 3.88, FALSE)\n\nterbaik ← kelas[0]\nFOR i ← 1 TO 2 DO\n    IF kelas[i].ipk > terbaik.ipk THEN\n        terbaik ← kelas[i]\n    ENDIF\nENDFOR\nOUTPUT "IPK tertinggi: ", terbaik.nama, " (", terbaik.ipk, ")"', out='IPK tertinggi: Sari (3.88)', run=False,
   tb=[{'c': 'Record di beberapa bahasa', 'h': ['Bahasa', 'Bentuk'], 'r': [['Pseudocode', 'TYPE Mahasiswa ... ENDTYPE'], ['Python', '@dataclass class Mahasiswa'], ['Java', 'record Mahasiswa(String nim, ...)'], ['Kotlin', 'data class Mahasiswa(val nim: String, ...)'], ['TypeScript', 'type Mahasiswa = { nim: string; ... }'], ['SQL', 'Satu baris di tabel mahasiswa']]}],
   pts=['Record = beberapa field berbeda jenis dalam satu kesatuan.', 'Akses field dengan titik: mhs.nama.', 'Array of record lebih aman daripada beberapa array sejajar.'],
   q=quiz(['Cara mengambil IPK mahasiswa ke-2 dari array kelas?', ['kelas.ipk[1]', 'kelas[1].ipk', 'ipk[kelas]'], 1, 'Indeks array dulu, lalu field.'],
          ['Kenapa array of record lebih baik dari 4 array sejajar?', ['Data satu orang selalu tetap bersama', 'Lebih sedikit memori', 'Wajib di semua bahasa'], 0, 'Tidak ada risiko indeks tidak sejajar.'])),
 R('Linear search: mencari satu per satu', 'Linear search dan binary search', b=[
   '<b>Linear search</b> memeriksa isi array satu per satu dari depan sampai data ditemukan atau array habis. Cara ini bekerja untuk data apa pun, terurut atau tidak. Kita pakai WHILE dengan dua syarat: masih ada data <b>dan</b> belum ketemu. Nilai -1 menjadi tanda "belum ditemukan", karena tidak ada indeks negatif.',
   '<b>Binary search</b> jauh lebih cepat, tetapi <b>datanya harus terurut</b>. Caranya seperti mencari kata di kamus: buka bagian <b>tengah</b>. Jika yang dicari lebih besar, buang separuh kiri; jika lebih kecil, buang separuh kanan. Ulangi sampai ketemu atau tidak ada data tersisa (<code>kiri &gt; kanan</code>).',
   'Bedanya sangat besar untuk data banyak. 1.000.000 data: linear search butuh sampai 1.000.000 pemeriksaan, binary search paling banyak sekitar <b>20</b>, karena setiap langkah membuang separuh data.',
   'Visual menjalankan binary search pada 8 data terurut. Cari 31 (ketemu di langkah kedua), lalu 3, 52, dan 20 (tidak ada). Perhatikan <code>kiri</code>, <code>kanan</code>, dan <code>tengah</code> bergerak. Versi linear search ada di bagian contoh.'],
   fc=P_BINARY,
   code='// Linear search: data boleh tidak terurut\ni ← 0\nposisi ← -1\nWHILE i < n AND posisi = -1 DO\n    IF data[i] = cari THEN\n        posisi ← i\n    ENDIF\n    i ← i + 1\nENDWHILE\n\n// Binary search: data WAJIB terurut\nkiri ← 0\nkanan ← n - 1\nposisi ← -1\nWHILE kiri <= kanan AND posisi = -1 DO\n    tengah ← (kiri + kanan) DIV 2\n    IF data[tengah] = cari THEN\n        posisi ← tengah\n    ELSE IF data[tengah] < cari THEN\n        kiri ← tengah + 1\n    ELSE\n        kanan ← tengah - 1\n    ENDIF\nENDWHILE', run=False,
   tb=[{'c': 'Linear vs binary search', 'h': ['Aspek', 'Linear', 'Binary'], 'r': [['Syarat data', 'Bebas', 'Harus terurut'], ['Cara', 'Satu per satu dari depan', 'Cek tengah, buang separuh'], ['Langkah terburuk, 1.000 data', '1.000', '10'], ['Langkah terburuk, 1.000.000 data', '1.000.000', '20'], ['Kompleksitas', 'O(n)', 'O(log n)']]}],
   pts=['Linear: bebas syarat, satu per satu.', 'Binary: data terurut, buang separuh setiap langkah.', '-1 sebagai tanda belum ditemukan.'],
   q=quiz(['Syarat wajib binary search?', ['Data berjumlah genap', 'Data terurut', 'Data berupa angka positif'], 1, 'Tanpa urutan, kita tidak tahu separuh mana yang dibuang.'],
          ['Data [3, 8, 12, 17, 23, 31, 40, 52], cari 31. Indeks tengah pertama?', ['3', '4', '5'], 0, '(0 + 7) DIV 2 = 3, berisi 17.'],
          ['Berapa langkah terburuk linear search untuk 100 data?', ['7', '50', '100'], 2, 'Jika data di akhir atau tidak ada, semua diperiksa.'])),
 R('Bubble sort dalam pseudocode', 'Bubble sort dan insertion sort', b=[
   '<b>Bubble sort</b> mengurutkan dengan membandingkan pasangan <b>bersebelahan</b> dan menukarnya jika salah urutan. Setelah putaran pertama, angka terbesar sudah di ujung kanan, seperti gelembung yang naik. Menukar butuh variabel bantu <code>t</code>: <code>t ← a[j]</code>, <code>a[j] ← a[j + 1]</code>, <code>a[j + 1] ← t</code>.',
   '<b>Insertion sort</b> bekerja seperti merapikan kartu di tangan. Ambil satu kartu (<code>kunci</code>), geser kartu-kartu di kirinya yang lebih besar satu langkah ke kanan, lalu <b>sisipkan</b> kunci di celah yang terbuka. Bagian kiri array selalu sudah terurut.',
   'Keduanya butuh sekitar n² langkah untuk data acak, jadi lambat untuk data besar. Tetapi insertion sort <b>sangat cepat</b> untuk data yang hampir terurut, karena hampir tidak ada yang perlu digeser. Itulah sebabnya Python dan Java memakai insertion sort untuk potongan kecil di dalam algoritma sort bawaannya.',
   'Visual menjalankan insertion sort pada [29, 10, 14, 37, 13]. Perhatikan <code>kunci</code> dan <code>j</code>, lalu lihat isi array berubah. Versi bubble sort ada di bagian contoh.'],
   fc=P_INSERT,
   code='// Bubble sort\nFOR i ← 0 TO n - 2 DO\n    FOR j ← 0 TO n - 2 - i DO\n        IF a[j] > a[j + 1] THEN\n            t ← a[j]\n            a[j] ← a[j + 1]\n            a[j + 1] ← t\n        ENDIF\n    ENDFOR\nENDFOR\n\n// Insertion sort\nFOR i ← 1 TO n - 1 DO\n    kunci ← a[i]\n    j ← i - 1\n    WHILE j >= 0 AND a[j] > kunci DO\n        a[j + 1] ← a[j]\n        j ← j - 1\n    ENDWHILE\n    a[j + 1] ← kunci\nENDFOR', out='[29, 10, 14, 37, 13] → [10, 13, 14, 29, 37]', run=False,
   tb=[{'c': 'Bubble vs insertion sort', 'h': ['Aspek', 'Bubble', 'Insertion'], 'r': [['Ide', 'Tukar pasangan bersebelahan', 'Sisipkan ke bagian kiri yang terurut'], ['Data acak', 'Sekitar n² langkah', 'Sekitar n² langkah'], ['Data hampir terurut', 'Tetap lambat (tanpa optimasi)', 'Sangat cepat'], ['Pemakaian nyata', 'Belajar konsep', 'Data kecil, bagian dari sort bawaan']]},
       {'c': 'Jejak insertion sort', 'h': ['i', 'kunci', 'Array setelahnya'], 'r': [['awal', '—', '[29, 10, 14, 37, 13]'], ['1', '10', '[10, 29, 14, 37, 13]'], ['2', '14', '[10, 14, 29, 37, 13]'], ['3', '37', '[10, 14, 29, 37, 13]'], ['4', '13', '[10, 13, 14, 29, 37]']]}],
   pts=['Bubble: tukar pasangan bersebelahan.', 'Insertion: sisipkan kunci ke bagian kiri yang sudah terurut.', 'Insertion sort unggul untuk data hampir terurut.'],
   q=quiz(['Kenapa menukar nilai butuh variabel t?', ['Agar nilai lama tidak hilang tertimpa', 'Agar lebih cepat', 'Aturan pseudocode'], 0, 'Seperti menukar isi dua gelas.'],
          ['Pada insertion sort, apa yang selalu benar tentang bagian kiri array?', ['Kosong', 'Sudah terurut', 'Berisi nilai terbesar'], 1, 'Setiap kunci disisipkan ke bagian yang sudah terurut.'])),
]},
{'t': 'Verifikasi dan translasi', 'lvl': 'Menengah', 'd': 'Trace table, off-by-one dan kesalahan logika, kompleksitas waktu dan ruang, menerjemahkan ke Python, adaptasi ke bahasa bertipe kuat, dan standar dokumentasi.', 'nodes': ['Verifikasi', 'Translasi'], 'lessons': [
 L('Trace table', [
   '<b>Trace table</b> (tabel jejak) adalah cara menjalankan algoritma <b>di atas kertas</b>, baris demi baris, sambil mencatat nilai setiap variabel. Setiap kolom satu variabel (ditambah kolom kondisi dan output), setiap baris satu langkah yang mengubah nilai.',
   'Trace table dipakai untuk tiga hal: (1) <b>memahami</b> algoritma orang lain, (2) <b>menemukan bug</b> dengan membandingkan isi tabel dengan yang seharusnya, dan (3) menjawab soal ujian "apa output algoritma berikut?". Ini keterampilan wajib di ujian algoritma kampus dan tes masuk kerja.',
   'Tipsnya: tulis hanya saat nilai <b>berubah</b>, catat hasil kondisi (benar/salah) di setiap pengecekan loop, dan jangan melompati langkah walaupun terasa jelas. Kesalahan biasanya bersembunyi di langkah yang kita anggap jelas.',
   'Kolom variabel di visual adalah trace table otomatis. Isi tabel di bawah dengan tanganmu dulu untuk n = 5, baru jalankan visual dan cocokkan langkah demi langkah.'],
   P_FAKT,
   tb=[{'c': 'Trace table Faktorial, n = 5', 'h': ['Langkah', 'i', 'i <= n?', 'hasil', 'Output'], 'r': [['awal', '—', '—', '1', ''], ['1', '2', 'benar', '2', ''], ['2', '3', 'benar', '6', ''], ['3', '4', 'benar', '24', ''], ['4', '5', 'benar', '120', ''], ['5', '6', 'salah', '120', '5! = 120']]}],
   pts=['Satu kolom per variabel, satu baris per perubahan.', 'Catat hasil setiap kondisi.', 'Jangan melompati langkah yang terasa jelas.'],
   q=quiz(['Pada trace di atas, berapa nilai hasil saat i = 4 selesai diproses?', ['6', '24', '120'], 1, '6 × 4 = 24.'],
          ['Apa fungsi utama trace table?', ['Mempercepat program', 'Menjalankan algoritma di kertas untuk memahami dan mencari bug', 'Menggambar flowchart'], 1, 'Kita menjadi komputernya.'])),
 L('Off-by-one dan kesalahan logika', [
   '<b>Kesalahan sintaks</b> ditangkap oleh compiler. <b>Kesalahan logika</b> tidak: program berjalan, tetapi hasilnya salah. Jenis paling terkenal adalah <b>off-by-one</b> (meleset satu): loop berjalan satu kali terlalu banyak atau terlalu sedikit.',
   'Visual di bawah sengaja berisi bug: array 5 data (indeks 0 sampai 4) diproses dengan <code>FOR i ← 0 TO 5</code>. Pada putaran terakhir, <code>nilai[5]</code> tidak ada. Simulator menampilkan hasilnya sebagai NaN (bukan angka); Java akan berhenti dengan <code>ArrayIndexOutOfBoundsException</code>, Python dengan <code>IndexError</code>. Perbaikannya: <code>TO 4</code>, atau umumnya <code>TO n - 1</code>.',
   'Kesalahan logika lain yang sering: <code>&gt;</code> tertukar dengan <code>&gt;=</code> (nilai tepat 75 tidak lulus), akumulator tidak diisi nilai awal atau diisi di dalam loop, urutan IF bertingkat terbalik, <code>AND</code> tertukar dengan <code>OR</code>, dan pembagian bulat yang tidak disengaja (7 / 2 menjadi 3).',
   'Cara melawannya: uji <b>kasus batas</b> (nilai minimum, maksimum, tepat di batas, data kosong, satu data), buat trace table, dan bandingkan dengan hasil hitungan manual.'],
   P_OBO,
   tb=[{'c': 'Kesalahan logika yang sering', 'h': ['Gejala', 'Penyebab', 'Perbaikan'], 'r': [['Error indeks di akhir loop', 'FOR i ← 0 TO n', 'FOR i ← 0 TO n - 1'], ['Data pertama terlewat', 'FOR i ← 1 TO n - 1 padahal indeks mulai 0', 'Mulai dari 0'], ['Nilai tepat 75 tidak lulus', 'nilai > 75', 'nilai >= 75'], ['Total hanya berisi data terakhir', 'total ← 0 di dalam loop', 'Pindahkan ke sebelum loop'], ['Nilai 90 dapat C', 'Urutan IF bertingkat terbalik', 'Cek kondisi paling ketat dulu'], ['Rata-rata 7 / 2 = 3', 'Pembagian antar-integer', 'Pakai REAL']]},
       {'c': 'Kasus batas yang wajib diuji', 'h': ['Kasus', 'Contoh untuk "nilai 0 sampai 100, lulus ≥ 75"'], 'r': [['Tepat di batas', '75 dan 74'], ['Minimum dan maksimum', '0 dan 100'], ['Di luar rentang', '-1 dan 101'], ['Data kosong', 'Tidak ada mahasiswa'], ['Satu data', 'Hanya satu mahasiswa']]}],
   pts=['Kesalahan logika tidak ditangkap compiler.', 'Off-by-one: batas loop meleset satu.', 'Selalu uji kasus batas.'],
   q=quiz(['Array 10 data, indeks mulai 0. Batas FOR yang benar?', ['0 TO 10', '0 TO 9', '1 TO 10'], 1, 'Indeks 0 sampai n - 1.'],
          ['total ← 0 ditaruh di dalam loop. Akibatnya?', ['Total benar', 'Total hanya berisi data terakhir', 'Infinite loop'], 1, 'Total di-reset setiap putaran.'])),
 L('Kompleksitas waktu dan ruang', [
   '<b>Kompleksitas waktu</b> mengukur bagaimana <b>jumlah langkah</b> bertambah saat data bertambah. Kita tidak mengukur detik (karena bergantung komputer), melainkan pertumbuhannya, ditulis dengan notasi <b>Big-O</b>.',
   'Yang paling sering: <b>O(1)</b> konstan, tidak bergantung jumlah data (mengakses <code>a[5]</code>). <b>O(log n)</b> logaritmik, membuang separuh setiap langkah (binary search). <b>O(n)</b> linear, satu loop (linear search, menjumlah array). <b>O(n²)</b> kuadratik, dua loop bersarang (bubble sort). Aturan cepat: hitung loop bersarang yang bergantung pada n.',
   '<b>Kompleksitas ruang</b> mengukur <b>memori tambahan</b> yang dipakai. Menjumlah array cukup satu variabel <code>total</code>: O(1). Menyalin array ke array baru: O(n). Matriks n × n: O(n²). Rekursi juga memakai ruang untuk setiap panggilan di call stack.',
   'Visual menghitung berapa kali badan loop bersarang dijalankan. Coba n = 4, 8, lalu 16. Saat n dua kali lipat, langkahnya menjadi <b>empat</b> kali lipat: itulah ciri O(n²).'],
   P_LANGKAH,
   tb=[{'c': 'Pertumbuhan jumlah langkah', 'h': ['n', 'O(1)', 'O(log n)', 'O(n)', 'O(n²)'], 'r': [['10', '1', '4', '10', '100'], ['100', '1', '7', '100', '10.000'], ['1.000', '1', '10', '1.000', '1.000.000'], ['1.000.000', '1', '20', '1.000.000', '1.000.000.000.000']]},
       {'c': 'Kompleksitas algoritma di jalur ini', 'h': ['Algoritma', 'Waktu', 'Ruang tambahan'], 'r': [['Akses a[i]', 'O(1)', 'O(1)'], ['Jumlah, maksimum, linear search', 'O(n)', 'O(1)'], ['Binary search (loop)', 'O(log n)', 'O(1)'], ['Bubble sort, insertion sort', 'O(n²)', 'O(1)'], ['Faktorial rekursif', 'O(n)', 'O(n), call stack'], ['Traversal matriks n × n', 'O(n²)', 'O(1)']]}],
   pts=['Big-O mengukur pertumbuhan, bukan detik.', 'Satu loop O(n), dua loop bersarang O(n²), membuang separuh O(log n).', 'Ruang: memori tambahan, termasuk call stack.'],
   q=quiz(['Kompleksitas waktu bubble sort?', ['O(n)', 'O(log n)', 'O(n²)'], 2, 'Dua loop bersarang.'],
          ['Algoritma O(n²) butuh 1 detik untuk 1.000 data. Kira-kira berapa untuk 2.000 data?', ['2 detik', '4 detik', '1 detik'], 1, 'n dua kali lipat, langkah empat kali lipat.'])),
 R('Menerjemahkan pseudocode ke bahasa pemrograman', 'Menerjemahkan pseudocode ke Python', b=[
   'Setelah logikanya benar di pseudocode, menulis kode tinggal menerjemahkan baris demi baris. Struktur IF, WHILE, FOR tidak berubah; yang berubah hanya cara penulisannya. Python paling dekat dengan pseudocode: tanpa deklarasi tipe, tanpa titik koma, dan blok ditandai indentasi.',
   'Jebakan saat menerjemahkan ke Python. Pertama, <code>=</code> pembanding menjadi <code>==</code>, dan <code>←</code> menjadi <code>=</code>. Kedua, <code>FOR i ← 1 TO n</code> menjadi <code>range(1, n + 1)</code>, karena batas akhir range tidak ikut. Ketiga, <code>DIV</code> menjadi <code>//</code> dan <code>MOD</code> menjadi <code>%</code>. Keempat, <code>INPUT</code> selalu menghasilkan teks, jadi angka harus diubah dengan <code>int()</code> atau <code>float()</code>.',
   'Python tidak punya REPEAT-UNTIL atau do-while. Polanya: <code>while True:</code>, badan loop, lalu <code>if kondisi_berhenti: break</code>. CASE menjadi <code>match</code> (Python 3.10+) atau <code>if/elif/else</code>.',
   'Kode Python di bawah adalah terjemahan langsung program "jumlah 1 sampai n" dari modul perulangan. Ubah nilai <code>n</code>, lalu jalankan.']),
 L('Adaptasi ke bahasa bertipe kuat', [
   'Bahasa <b>bertipe statis dan kuat</b> seperti Java, Kotlin, Dart, C#, dan TypeScript memeriksa tipe data <b>sebelum</b> program dijalankan. Kabar baiknya: pseudocode kita sudah punya <code>DECLARE x : INTEGER</code>, jadi informasi tipenya sudah ada. Tinggal dipetakan ke tipe bahasa tujuan.',
   'Hal yang perlu diperhatikan. Pertama, <b>pilih tipe angka</b>: INTEGER menjadi <code>int</code> (atau <code>long</code> untuk angka besar seperti rupiah triliunan), REAL menjadi <code>double</code>. Kedua, <b>pembagian</b>: di Java, <code>7 / 2</code> antar-int menghasilkan 3; agar 3.5, salah satunya harus double. Ketiga, <b>INPUT</b> harus diubah ke tipe yang tepat (<code>sc.nextInt()</code>, <code>readln().toInt()</code>).',
   'Keempat, <b>fungsi</b> menulis tipe parameter dan tipe kembali secara eksplisit: <code>FUNCTION Luas(p : INTEGER, l : INTEGER) RETURNS INTEGER</code> menjadi <code>static int luas(int p, int l)</code> di Java. Kelima, perbandingan <b>STRING</b> di Java memakai <code>.equals()</code>, bukan <code>==</code>.',
   'Contoh di bawah menerjemahkan algoritma rekap nilai (pola akumulator) ke Java. Bandingkan baris demi baris dengan pseudocodenya.'],
   lang='java', code='import java.util.Scanner;\n\npublic class RekapNilai {\n    // FUNCTION RataRata(total : INTEGER, n : INTEGER) RETURNS REAL\n    static double rataRata(int total, int n) {\n        return (double) total / n;   // cegah pembagian bulat\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int total = 0, lulus = 0, maks = 0;      // DECLARE ... : INTEGER\n        for (int i = 1; i <= 5; i++) {           // FOR i <- 1 TO 5\n            int x = sc.nextInt();                // INPUT x\n            total += x;\n            if (x >= 75) lulus++;\n            if (i == 1 || x > maks) maks = x;\n        }\n        System.out.println("Total: " + total);\n        System.out.println("Rata-rata: " + rataRata(total, 5));\n        System.out.println("Lulus: " + lulus + " orang");\n        System.out.println("Tertinggi: " + maks);\n    }\n}', out='Input: 80 65 92 75 58\nTotal: 370\nRata-rata: 74.0\nLulus: 3 orang\nTertinggi: 92', run=False,
   tb=[{'c': 'Pemetaan tipe data', 'h': ['Pseudocode', 'Java', 'Kotlin', 'Dart', 'TypeScript'], 'r': [
     ['INTEGER', 'int / long', 'Int / Long', 'int', 'number'], ['REAL', 'double', 'Double', 'double', 'number'], ['STRING', 'String', 'String', 'String', 'string'],
     ['BOOLEAN', 'boolean', 'Boolean', 'bool', 'boolean'], ['CHAR', 'char', 'Char', 'String (1 huruf)', 'string'],
     ['ARRAY[0..4] OF INTEGER', 'int[] a = new int[5]', 'IntArray(5)', 'List<int>.filled(5, 0)', 'number[]'], ['TYPE Mahasiswa', 'record / class', 'data class', 'class', 'type / interface']]},
       {'c': 'Jebakan saat pindah ke bahasa bertipe kuat', 'h': ['Pseudocode', 'Jebakan', 'Solusi di Java'], 'r': [['rata ← total / n', '370 / 5 aman, 7 / 2 menjadi 3', '(double) total / n'], ['IF nama = "Rina"', '== membandingkan alamat objek', 'nama.equals("Rina")'], ['INPUT x', 'Hasil teks atau token', 'sc.nextInt(), Integer.parseInt()'], ['total ← total + harga', 'int meluap di atas 2,1 miliar', 'Pakai long']]}],
   pts=['Tipe di DECLARE dipetakan ke tipe bahasa tujuan.', 'Waspadai pembagian bulat dan batas int.', 'Tulis tipe parameter dan tipe kembali fungsi.'],
   q=quiz(['Di Java, 7 / 2 dengan keduanya int menghasilkan?', ['3.5', '3', '4'], 1, 'Pembagian antar-int dibulatkan ke bawah.'],
          ['REAL di pseudocode menjadi apa di Kotlin?', ['Int', 'Double', 'String'], 1, 'Bilangan pecahan.'],
          ['Membandingkan dua String di Java sebaiknya memakai?', ['==', '.equals()', '='], 1, '== membandingkan alamat objek.'])),
 L('Standar dokumentasi dan keterbacaan', [
   'Pseudocode ditulis untuk <b>dibaca manusia</b>: dosen, rekan tim, atau dirimu sendiri enam bulan lagi. Algoritma yang benar tetapi sulit dibaca tetap merepotkan saat perlu diperbaiki.',
   'Standar yang dipakai di dunia kerja dan kampus. (1) <b>Kepala algoritma</b>: nama, tujuan, input, output, dan penulis. (2) <b>Nama bermakna</b>: <code>hargaSatuan</code>, bukan <code>h</code>; fungsi diawali kata kerja (<code>HitungPajak</code>). (3) <b>Konsisten</b>: satu gaya kata kunci, satu gaya penamaan (camelCase atau snake_case), indentasi 4 spasi. (4) <b>Konstanta bernama</b>: <code>CONSTANT PPN ← 0.11</code>, bukan angka 0.11 yang muncul tiba-tiba (magic number).',
   '(5) <b>Komentar</b> menjelaskan <b>kenapa</b>, bukan <b>apa</b>. <code>// tambah 1 ke i</code> tidak berguna; <code>// indeks mulai 0, jadi batas n - 1</code> berguna. (6) <b>Satu modul satu tugas</b>, dan modul cukup pendek untuk dibaca dalam satu layar. (7) Sertakan <b>contoh uji</b> beserta hasil yang diharapkan.',
   'Bandingkan versi sulit dibaca dan versi terdokumentasi di bagian contoh. Keduanya menghasilkan angka yang sama.'],
   code='// ===== Sulit dibaca =====\nINPUT a\nINPUT b\nc ← a * b\nd ← c * 0.11\nOUTPUT c + d\n\n// ===== Terdokumentasi =====\n// Nama    : HitungTotalBayar\n// Tujuan  : menghitung total belanja termasuk PPN\n// Input   : hargaSatuan (INTEGER), jumlah (INTEGER)\n// Output  : totalBayar (REAL)\n// Uji     : 15000, 4 -> 66600\nCONSTANT TARIF_PPN ← 0.11      // PPN 11% sejak April 2022\n\nDECLARE hargaSatuan, jumlah, subtotal : INTEGER\nDECLARE pajak, totalBayar : REAL\n\nINPUT hargaSatuan\nINPUT jumlah\nsubtotal ← hargaSatuan * jumlah\npajak ← subtotal * TARIF_PPN\ntotalBayar ← subtotal + pajak\nOUTPUT "Total bayar: ", totalBayar', out='Masukan 15000 dan 4 → Total bayar: 66600', run=False,
   tb=[{'c': 'Daftar periksa keterbacaan', 'h': ['Periksa', 'Contoh baik'], 'r': [['Ada kepala algoritma', 'Nama, tujuan, input, output, contoh uji'], ['Nama variabel bermakna', 'totalBayar, jumlahLulus'], ['Fungsi diawali kata kerja', 'HitungPajak, CetakStruk'], ['Tanpa magic number', 'CONSTANT TARIF_PPN ← 0.11'], ['Indentasi konsisten', '4 spasi per tingkat'], ['Komentar menjelaskan alasan', '// batas n - 1 karena indeks mulai 0'], ['Modul pendek dan satu tugas', 'Muat dalam satu layar']]}],
   pts=['Tulis untuk manusia: kepala algoritma, nama bermakna, konsisten.', 'Konstanta bernama menggantikan magic number.', 'Komentar menjelaskan kenapa, bukan apa.'],
   q=quiz(['Komentar mana yang paling berguna?', ['// i ditambah 1', '// batas n - 1 karena indeks mulai dari 0', '// loop'], 1, 'Menjelaskan alasan, bukan mengulang kode.'],
          ['Apa itu magic number?', ['Angka acak', 'Angka penting yang muncul tanpa nama atau penjelasan', 'Angka yang sangat besar'], 1, 'Ganti dengan konstanta bernama.'])),
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
