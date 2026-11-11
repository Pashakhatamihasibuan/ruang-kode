"""Membuat src/js/track-acak.js: pelajaran "Boolean logic" dan "Random number" yang ditaruh di AKHIR
modul percabangan & perulangan tiap jalur bahasa pemrograman, sehingga alamat pelajaran lama tidak bergeser.
Kode Java, Python, dan JavaScript dijalankan dulu dan keluarannya dipakai apa adanya.
Kode Dart dan Kotlin ditulis setara baris demi baris dengan kode Java:
- Boolean: keluarannya deterministik dan sama persis dengan Java (true/false huruf kecil).
- Random: keluarannya contoh satu kali jalan (angka acak memang berbeda setiap dijalankan).
Jalankan: python3 tools/gen/acak/gen.py"""
import json, subprocess
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parents[2]


def jalan(topik):
    d = here / topik
    run = lambda cmd: subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=d).stdout.rstrip('\n')
    o = {'python': run(['python3', 'main.py']), 'js': run(['node', 'main.js']), 'java': run(['java', 'Main.java'])}
    o['dart'] = o['kotlin'] = o['java']
    return o


baca = lambda topik, f: (here / topik / f).read_text().rstrip('\n')
BERKAS = {'java': 'Main.java', 'python': 'main.py', 'js': 'main.js', 'dart': 'main.dart', 'kotlin': 'main.kt'}

# ---------------------------------------------------------------- Boolean logic
B_TB = [{'c': 'Operator logika di tiap bahasa', 'h': ['Operator', 'Java, JS, Dart, Kotlin', 'Python', 'Bernilai true jika', 'Contoh'], 'r': [
    ['AND', '<code>&&</code>', '<code>and</code>', 'kedua sisi true', 'nilai ≥ 75 <b>dan</b> hadir ≥ 80'],
    ['OR', '<code>||</code>', '<code>or</code>', 'minimal satu sisi true', 'hari Sabtu <b>atau</b> Minggu'],
    ['NOT', '<code>!</code>', '<code>not</code>', 'nilainya false (dibalik)', '<b>belum</b> login'],
    ['XOR', '<code>^</code> (Kotlin <code>xor</code>, JS <code>!==</code>)', '<code>^</code> atau <code>!=</code>', 'kedua sisi berbeda', 'tepat satu lampu menyala']]},
    {'c': 'Tabel kebenaran (p dan q)', 'h': ['p', 'q', 'p AND q', 'p OR q', 'NOT p', 'p XOR q'], 'r': [
        ['true', 'true', 'true', 'true', 'false', 'false'],
        ['true', 'false', 'false', 'true', 'false', 'true'],
        ['false', 'true', 'false', 'true', 'true', 'true'],
        ['false', 'false', 'false', 'false', 'true', 'false']]}]

B_UMUM = [
    '<b>Boolean</b> adalah tipe data yang hanya punya dua nilai: <b>true</b> (benar) dan <b>false</b> (salah). Namanya diambil dari George Boole, matematikawan yang merumuskan aljabar logika. Setiap kondisi di <code>if</code> dan <code>while</code> pada akhirnya menghasilkan satu nilai boolean.',
    'Operator perbandingan (<code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>) selalu menghasilkan boolean. Hasilnya bisa disimpan di variabel dengan nama yang jelas, misalnya <code>nilaiCukup</code> atau <code>sudahLogin</code>, sehingga kondisi panjang menjadi mudah dibaca.',
    '<b>AND</b> bernilai true hanya jika <b>kedua</b> sisi true. <b>OR</b> bernilai true jika <b>minimal satu</b> sisi true. <b>NOT</b> membalik nilai. <b>XOR</b> bernilai true jika kedua sisi <b>berbeda</b>. Tabel kebenaran mendaftar semua kombinasi masukan: dua masukan berarti 2 × 2 = 4 baris.',
    'Urutan pengerjaan: <b>NOT</b> dulu, lalu <b>AND</b>, baru <b>OR</b>. Karena itu <code>true || false &amp;&amp; false</code> hasilnya true: bagian <code>false &amp;&amp; false</code> dikerjakan lebih dulu. Agar tidak salah baca, pakai tanda kurung.',
    '<b>Hukum De Morgan</b>: membalik AND menjadi OR dari kebalikannya, dan sebaliknya. <code>!(a &amp;&amp; b)</code> sama dengan <code>!a || !b</code>, dan <code>!(a || b)</code> sama dengan <code>!a &amp;&amp; !b</code>. Contoh sehari-hari: "tidak (nilai cukup dan hadir cukup)" sama artinya dengan "nilai kurang atau hadir kurang".',
    '<b>Short-circuit</b>: AND berhenti jika sisi kiri sudah false, dan OR berhenti jika sisi kiri sudah true, karena hasilnya sudah pasti. Ini dipakai sebagai pengaman, misalnya <code>pembagi != 0 &amp;&amp; 10 / pembagi &gt; 1</code> tidak pernah membagi dengan nol. Buka visual 3D di bawah, lalu ubah p, q, dan operatornya di panel Eksperimen.']

B_CAT = {
    'java': 'Catatan Java: <code>&amp;&amp;</code> dan <code>||</code> memakai short-circuit, sedangkan <code>&amp;</code> dan <code>|</code> pada boolean tetap menghitung kedua sisi. Boolean di Java tidak bisa diubah menjadi angka: <code>if (1)</code> adalah error.',
    'python': 'Catatan Python: operator ditulis dengan kata (<code>and</code>, <code>or</code>, <code>not</code>), dan nilainya <code>True</code>/<code>False</code> berhuruf besar. Nilai seperti <code>0</code>, <code>""</code>, <code>[]</code>, dan <code>None</code> dianggap salah (falsy). <code>and</code>/<code>or</code> mengembalikan salah satu operandnya, misalnya <code>nama or "tamu"</code>. Python juga mendukung perbandingan berantai <code>0 &lt; x &lt; 10</code>.',
    'js': 'Catatan JavaScript: ada nilai falsy (<code>false</code>, <code>0</code>, <code>""</code>, <code>null</code>, <code>undefined</code>, <code>NaN</code>); selain itu truthy. <code>&amp;&amp;</code> dan <code>||</code> mengembalikan salah satu operandnya, bukan selalu boolean. <code>!!x</code> mengubah nilai apa pun menjadi boolean. Untuk nilai bawaan, <code>??</code> lebih aman daripada <code>||</code> karena tidak menganggap 0 sebagai kosong.',
    'dart': 'Catatan Dart: tidak ada truthy/falsy. Kondisi harus benar-benar bertipe <code>bool</code>, jadi tulis <code>if (daftar.isNotEmpty)</code>, bukan <code>if (daftar.length)</code>. Operator <code>^</code> bisa dipakai pada bool sebagai XOR.',
    'kotlin': 'Catatan Kotlin: <code>&amp;&amp;</code> dan <code>||</code> memakai short-circuit, sedangkan fungsi infix <code>and</code>, <code>or</code>, dan <code>xor</code> selalu menghitung kedua sisi. Seperti Java, angka tidak bisa dipakai sebagai kondisi.'}

B_PTS = ['AND true jika keduanya true; OR true jika salah satu true; NOT membalik.',
         'Urutan pengerjaan: NOT, lalu AND, lalu OR. Pakai kurung agar jelas.',
         'De Morgan: !(a && b) sama dengan !a || !b.',
         'Short-circuit melewati sisi kanan jika hasilnya sudah pasti.']
B_Q = [['p = true dan q = false. Berapa nilai p && q?', ['false', 'true', 'error'], 0, 'AND butuh kedua sisi true.'],
       ['Hasil dari true || false && false adalah…', ['true', 'false', 'error'], 0, '&& dikerjakan dulu: false && false = false, lalu true || false = true.'],
       ['Menurut De Morgan, !(a && b) sama dengan…', ['!a || !b', '!a && !b', 'a || b'], 0, 'AND yang dibalik menjadi OR dari kebalikan masing-masing.'],
       ['Mengapa x != 0 && 10 / x > 1 aman saat x = 0?', ['Sisi kanan tidak dihitung karena sisi kiri sudah false', 'Pembagian dengan nol menghasilkan 0', 'Compiler melewati baris itu'], 0, 'Short-circuit: hasil AND sudah pasti false.']]

# ---------------------------------------------------------------- Random number
R_TB = [{'c': 'Fungsi acak di tiap bahasa', 'h': ['Bahasa', 'Desimal 0 sampai &lt; 1', 'Bulat a sampai b (b ikut)', 'Pilih acak', 'Kocok', 'Untuk keamanan'], 'r': [
    ['Java', '<code>Math.random()</code>', '<code>r.nextInt(b - a + 1) + a</code>', '<code>xs[r.nextInt(xs.length)]</code>', '<code>Collections.shuffle(list)</code>', '<code>SecureRandom</code>'],
    ['Python', '<code>random.random()</code>', '<code>random.randint(a, b)</code>', '<code>random.choice(xs)</code>', '<code>random.shuffle(xs)</code>', 'modul <code>secrets</code>'],
    ['JavaScript', '<code>Math.random()</code>', '<code>Math.floor(Math.random() * (b - a + 1)) + a</code>', 'indeks acak 0..panjang−1', 'Fisher-Yates', '<code>crypto.getRandomValues()</code>'],
    ['Dart', '<code>Random().nextDouble()</code>', '<code>r.nextInt(b - a + 1) + a</code>', '<code>xs[r.nextInt(xs.length)]</code>', '<code>xs.shuffle()</code>', '<code>Random.secure()</code>'],
    ['Kotlin', '<code>Random.nextDouble()</code>', '<code>(a..b).random()</code>', '<code>xs.random()</code>', '<code>xs.shuffled()</code>', '<code>SecureRandom</code>']]}]

R_UMUM = [
    'Komputer tidak benar-benar melempar dadu. Ia memakai <b>rumus</b> yang menghasilkan deret angka yang terlihat acak, dimulai dari angka awal yang disebut <b>seed</b>. Karena itu namanya <b>acak semu</b> (pseudo-random). Bilangan acak dipakai untuk game, simulasi, mengambil sampel data, dan mengocok urutan soal kuis.',
    'Hampir semua bahasa punya fungsi dasar yang menghasilkan <b>desimal dari 0 sampai kurang dari 1</b> (0 ≤ r &lt; 1). Angka 0 bisa keluar, tetapi angka 1 <b>tidak pernah</b> keluar.',
    'Rumus bilangan bulat dari <i>bawah</i> sampai <i>atas</i>: <code>floor(r × (atas − bawah + 1)) + bawah</code>. Contoh dadu: r × 6 memberi 0 sampai 5,99…, floor membulatkan ke bawah menjadi 0 sampai 5, lalu +1 menjadi 1 sampai 6. Jika "+1" pada lebar rentang lupa ditulis, angka 6 tidak akan pernah keluar. Ini kesalahan off-by-one yang paling sering.',
    'Setiap bahasa berbeda soal <b>batas atas ikut atau tidak</b>. <code>randint(1, 6)</code> di Python memasukkan 6, <code>nextInt(6)</code> di Java dan Dart memberi 0 sampai 5, sedangkan <code>Random.nextInt(1, 7)</code> di Kotlin tidak memasukkan 7. Selalu cek dokumentasinya.',
    'Dengan <b>seed yang sama</b>, urutan angka acak selalu sama. Ini berguna untuk pengujian, mencari bug, dan memutar ulang permainan. Tanpa seed, biasanya seed diambil dari jam komputer sehingga hasilnya berbeda setiap kali dijalankan.',
    'Memilih isi list secara acak sama dengan mengambil <b>indeks acak</b> dari 0 sampai panjang − 1. Mengocok list memakai algoritma <b>Fisher-Yates</b>. Untuk password, token, atau kode OTP, jangan memakai fungsi acak biasa; pakai generator kriptografis. <b>Keluaran di bawah adalah contoh satu kali jalan</b>, jadi angkamu akan berbeda. Coba juga visual 3D dan ubah rentang serta seed-nya.']

R_CAT = {
    'java': 'Catatan Java: <code>new Random().nextInt(n)</code> memberi 0 sampai n − 1. Sejak Java 17 ada <code>random.nextInt(a, b)</code> (b tidak ikut). Di program banyak thread, pakai <code>ThreadLocalRandom.current()</code>. Untuk token keamanan, pakai <code>java.security.SecureRandom</code>.',
    'python': 'Catatan Python: <code>randint(a, b)</code> memasukkan b, tetapi <code>randrange(a, b)</code> tidak. <code>random.shuffle(xs)</code> mengubah list itu sendiri dan mengembalikan <code>None</code>. <code>random.sample(xs, k)</code> memilih k isi tanpa pengulangan. Untuk keamanan, pakai modul <code>secrets</code>, misalnya <code>secrets.token_hex()</code>.',
    'js': 'Catatan JavaScript: tidak ada fungsi bawaan untuk bilangan bulat acak, jadi rumus <code>Math.floor(Math.random() * (b - a + 1)) + a</code> ditulis sendiri. <code>Math.random()</code> juga tidak bisa diberi seed. Untuk keamanan, pakai <code>crypto.getRandomValues()</code> atau <code>crypto.randomUUID()</code>. Jangan mengocok dengan <code>sort(() =&gt; Math.random() - 0.5)</code> karena hasilnya tidak merata.',
    'dart': 'Catatan Dart: impor <code>dart:math</code>. <code>Random(42)</code> memakai seed, <code>Random.secure()</code> untuk keamanan. <code>list.shuffle()</code> mengubah list itu sendiri.',
    'kotlin': 'Catatan Kotlin: <code>(1..6).random()</code> memasukkan kedua batas, sedangkan <code>Random.nextInt(dari, sampai)</code> tidak memasukkan batas atas. <code>shuffled()</code> mengembalikan list baru, sedangkan <code>shuffle()</code> mengubah MutableList itu sendiri.'}

R_PTS = ['Fungsi dasar memberi desimal 0 ≤ r < 1; angka 1 tidak pernah keluar.',
         'Bulat bawah..atas: floor(r × (atas − bawah + 1)) + bawah.',
         'Seed sama menghasilkan urutan sama; berguna untuk pengujian.',
         'Untuk password dan token, pakai generator kriptografis.']
R_Q = [['Rumus bilangan bulat acak 1 sampai 6 dari r (0 ≤ r < 1) adalah…', ['floor(r × 6) + 1', 'floor(r × 6)', 'floor(r × 7)'], 0, 'r × 6 memberi 0..5,99, floor menjadi 0..5, lalu +1.'],
       ['Bisakah Math.random() atau random.random() menghasilkan tepat 1.0?', ['Tidak, selalu kurang dari 1', 'Ya, kadang-kadang', 'Hanya jika seed-nya 1'], 0, 'Rentangnya 0 ≤ r < 1.'],
       ['Apa gunanya seed?', ['Agar urutan angka acak bisa diulang persis', 'Agar angkanya lebih acak', 'Agar program lebih cepat'], 0, 'Seed sama, urutan sama.'],
       ['Untuk membuat token reset password, sebaiknya memakai…', ['Generator kriptografis seperti SecureRandom atau secrets', 'Math.random()', 'Random dengan seed tetap'], 0, 'Fungsi acak biasa bisa ditebak.']]

JALUR = [('JAVA_MODULES', 'Percabangan & perulangan', 'java'),
         ('PY_MODULES', 'Percabangan & perulangan', 'python'),
         ('FE0_MODULES', 'JavaScript dasar', 'js'),
         ('DART_MODULES', 'Alur program dan fungsi', 'dart'),
         ('KOTLIN_MODULES', 'Alur program, fungsi, dan koleksi', 'kotlin')]

out_b, out_r = jalan('bool'), jalan('random')
js = ['/* ===================== BOOLEAN LOGIC DAN RANDOM NUMBER =====================',
      '   Dibuat oleh tools/gen/acak/gen.py. Pelajaran ditambahkan di akhir modul percabangan & perulangan tiap jalur.',
      '   Dimuat sesudah track-loop.js agar alamat pelajaran "Semua jenis perulangan" tidak bergeser. */',
      '(()=>{const tambah=(mods,judul,l)=>{const m=mods.find(x=>x.t===judul);if(m&&!m.lessons.some(x=>x.t===l.t))m.lessons.push(l)};']
for const, modul, lang in JALUR:
    f = BERKAS[lang]
    lb = {'k': 'c', 't': 'Boolean logic: AND, OR, NOT, tabel kebenaran, dan De Morgan', 'nodes': ['Operators', 'Conditionals'], 'lang': lang,
          'b': B_UMUM + [B_CAT[lang]], 'code': baca('bool', f), 'out': out_b[lang], 'run': False, 'tb': B_TB, 'pts': B_PTS, 'q': B_Q}
    lr = {'k': 'c', 't': 'Random number: bilangan acak, rentang, seed, dan mengocok', 'nodes': ['Math Operations'], 'lang': lang,
          'b': R_UMUM + [R_CAT[lang]], 'code': baca('random', f), 'out': out_r[lang], 'run': False, 'tb': R_TB, 'pts': R_PTS, 'q': R_Q}
    for l in (lb, lr):
        js.append(f'if(typeof {const}!=="undefined")tambah({const},{json.dumps(modul, ensure_ascii=False)},{json.dumps(l, ensure_ascii=False)});')
js.append('})();\n')
(root / 'src/js/track-acak.js').write_text('\n'.join(js))
print('ok', len(JALUR), 'jalur x 2 pelajaran')
