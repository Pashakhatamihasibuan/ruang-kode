"""Jalur JavaScript lengkap (mengikuti roadmap.sh/javascript).
Keluaran setiap contoh dan soal dihitung saat generate dengan menjalankan kodenya di Node 22,
jadi yang tampil di pelajaran selalu cocok dengan hasil sebenarnya."""
import pathlib, subprocess, tempfile
from mobile_lib import C, M, q
from mobile_dart_x import S

_CACHE = {}


def node(code, cjs=False, files=None):
    """Jalankan kode JS. ESM (main.mjs, otomatis strict) atau CommonJS (main.cjs, sloppy) jika cjs=True.
    files = {nama: isi} untuk contoh modul dengan beberapa file."""
    key = (code, cjs, tuple(sorted((files or {}).items())))
    if key in _CACHE:
        return _CACHE[key]
    with tempfile.TemporaryDirectory() as d:
        for nama, isi in (files or {}).items():
            p = pathlib.Path(d) / nama
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(isi)
        main = 'main.cjs' if cjs else 'main.mjs'
        (pathlib.Path(d) / main).write_text(code)
        # stderr digabung agar console.warn/error/assert ikut tampil sesuai urutan
        r = subprocess.run(['node', '--no-warnings', main], cwd=d, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=60)
        if r.returncode != 0:
            raise RuntimeError(f'JS gagal:\n{r.stdout}\n---\n{code}')
        _CACHE[key] = r.stdout.rstrip('\n')
    return _CACHE[key]


def J(t, b, code, tb=None, pts=None, qs=None, so=None, nodes=None, viz=None, cjs=False, files=None):
    """Pelajaran JS yang bisa dijalankan; keluaran berasal dari Node."""
    d = C(t, b, code, None, 'js', tb, pts, qs, so, nodes, viz)
    d['out'] = node(code, cjs, files)
    return d


def JT(t, b, code, lang='js', out=None, tb=None, pts=None, qs=None, so=None, nodes=None):
    """Pelajaran konsep: contoh tidak dijalankan (kode khusus browser, perintah terminal)."""
    return C(t, b, code, out, lang, tb, pts, qs, so, nodes)


def SX(soal, petunjuk, jawab, cjs=False):
    """Soal latihan JS: jawabannya dijalankan untuk mendapatkan keluaran."""
    return S(soal, petunjuk, jawab, node(jawab, cjs), lang='js')


def SN(soal, petunjuk, jawab, lang='js'):
    """Soal latihan tanpa keluaran (kode browser)."""
    return S(soal, petunjuk, jawab, None, lang=lang)


JS1 = [
M('Pengenalan JavaScript', 'Pemula',
  'Apa itu JavaScript, sejarahnya, versi ECMAScript, dan cara menjalankan kode di browser maupun Node.js.',
  ['Introduction to JavaScript', 'What is JavaScript?', 'History of JavaScript', 'JavaScript Versions', 'How to run JavaScript'], [
  J('Apa itu JavaScript',
    ['<b>JavaScript</b> (JS) adalah bahasa pemrograman yang membuat halaman web hidup: merespons klik, memvalidasi formulir, memuat data tanpa memuat ulang halaman, sampai menjalankan game. Bersama HTML (struktur) dan CSS (tampilan), JS adalah satu dari tiga bahasa inti web dan satu-satunya bahasa yang berjalan bawaan di semua browser.',
     'Hari ini JS juga berjalan di luar browser: <b>Node.js</b>, <b>Deno</b>, dan <b>Bun</b> untuk server dan alat baris perintah, <b>React Native</b> untuk aplikasi mobile, <b>Electron</b> untuk aplikasi desktop (VS Code, Slack, Discord), bahkan perangkat IoT. Survei Stack Overflow menempatkan JS sebagai bahasa paling banyak dipakai lebih dari sepuluh tahun berturut-turut.',
     'Ciri bahasanya: <b>dinamis</b> (tipe ditentukan saat berjalan), <b>multi-paradigma</b> (prosedural, berorientasi objek berbasis prototype, dan fungsional), <b>single-threaded</b> dengan <b>event loop</b> untuk pekerjaan asinkron, serta dijalankan oleh <b>engine</b> seperti V8 (Chrome, Node, Edge), SpiderMonkey (Firefox), dan JavaScriptCore (Safari) yang memakai kompilasi JIT agar cepat.',
     'Jangan tertukar dengan Java: namanya mirip karena alasan pemasaran tahun 1995, tetapi bahasanya berbeda jauh.'],
    "// Program pertama: jalankan, lalu coba ubah isinya\nconst nama = 'Rina';\nconst kota = 'Bandung';\nconsole.log(`Halo, ${nama} dari ${kota}!`);\nconsole.log('Tahun ini JavaScript berumur', 2026 - 1995, 'tahun');\nconsole.log(typeof nama, typeof 2026);",
    tb=[{'c': 'Di mana JavaScript berjalan', 'h': ['Lingkungan', 'Engine', 'Contoh pemakaian'], 'r': [
      ['Chrome, Edge, Opera', 'V8', 'Situs dan aplikasi web'], ['Firefox', 'SpiderMonkey', 'Situs dan aplikasi web'], ['Safari', 'JavaScriptCore', 'Situs, termasuk semua browser di iOS'],
      ['Node.js', 'V8', 'API server, CLI, build tools (Vite, ESLint)'], ['Deno, Bun', 'V8, JavaScriptCore', 'Server modern dengan TypeScript bawaan'], ['React Native, Electron', 'Hermes, V8', 'Aplikasi mobile dan desktop']]}],
    pts=['JS adalah bahasa bawaan browser dan kini juga berjalan di server, mobile, dan desktop.', 'Dinamis, multi-paradigma, single-threaded dengan event loop.', 'Engine (V8, SpiderMonkey, JavaScriptCore) mengeksekusi kode dengan JIT.'],
    qs=[q('Engine JavaScript yang dipakai Chrome dan Node.js?', ['V8', 'SpiderMonkey', 'JavaScriptCore'], 0, 'Keduanya memakai V8 buatan Google.'),
        q('Pernyataan yang benar tentang Java dan JavaScript?', ['Dua bahasa berbeda, hanya namanya mirip', 'JavaScript adalah versi ringan Java', 'Java berjalan bawaan di semua browser'], 0, 'Nama JavaScript dipilih karena tren pemasaran Java tahun 1995.')],
    so=[SX('Cetak kartu nama tiga baris: nama, pekerjaan impian, dan kota. Gunakan template literal minimal sekali.', 'Template literal memakai backtick dan ${...}.',
           "const nama = 'Budi Santoso';\nconst cita = 'Frontend Developer';\nconst kota = 'Surabaya';\nconsole.log(`Nama   : ${nama}`);\nconsole.log(`Impian : ${cita}`);\nconsole.log(`Kota   : ${kota}`);")]),
  J('Sejarah dan versi ECMAScript',
    ['Tahun 1995 <b>Brendan Eich</b> di Netscape membuat bahasa ini dalam sekitar 10 hari dengan nama Mocha, lalu LiveScript, lalu JavaScript. Agar tidak dikuasai satu perusahaan, bahasa ini distandarkan oleh <b>Ecma International</b> dengan nama <b>ECMAScript</b> (spesifikasi ECMA-262). "JavaScript" adalah implementasi paling populer dari standar itu.',
     'Standar dikembangkan oleh komite <b>TC39</b>. Setiap fitur baru melalui <b>stage 0 sampai 4</b>; fitur yang mencapai stage 4 masuk ke rilis tahunan berikutnya. Sejak <b>ES2015 (ES6)</b>, yang membawa <code>let</code>/<code>const</code>, arrow function, class, modul, Promise, dan template literal, ECMAScript dirilis setiap Juni dengan nama tahun: ES2016, ES2017, dan seterusnya.',
     'Di dunia kerja kamu akan mendengar istilah <b>"ES6+"</b> atau <b>"modern JavaScript"</b>, yang berarti kode memakai fitur sejak ES2015. Untuk browser lama, alat seperti <b>Babel</b>, <b>esbuild</b>, atau <b>SWC</b> melakukan <b>transpile</b> ke sintaks lama, dan <b>polyfill</b> (misalnya core-js) menambahkan fungsi yang belum ada. Situs <b>caniuse.com</b> dan tabel kompatibilitas MDN dipakai untuk mengecek dukungan.'],
    "// Beberapa fitur dari versi yang berbeda, semua didukung Node 22\nconst nilai = [70, 85, 92];                      // ES2015: const, array\nconst [pertama, ...sisa] = nilai;                 // ES2015: destructuring, rest\nconsole.log(pertama, sisa);\nconsole.log(nilai.includes(85));                  // ES2016: includes\nconsole.log(Object.entries({ a: 1, b: 2 }));       // ES2017: Object.entries\nconst cfg = { tema: null };\nconsole.log(cfg.tema ?? 'terang');                // ES2020: nullish coalescing\nconsole.log(cfg.user?.nama);                      // ES2020: optional chaining\nconsole.log(nilai.at(-1));                        // ES2022: at()\nconsole.log(nilai.toSorted((a, b) => b - a), nilai); // ES2023: toSorted tidak mengubah asli\nconsole.log(Object.groupBy([1, 2, 3, 4], n => n % 2 ? 'ganjil' : 'genap')); // ES2024",
    tb=[{'c': 'Tonggak versi ECMAScript', 'h': ['Versi', 'Tahun', 'Fitur penting'], 'r': [
      ['ES1', '1997', 'Standar pertama'], ['ES3', '1999', 'Regex, try/catch'], ['ES5', '2009', 'Strict mode, JSON, Array.forEach/map/filter'],
      ['ES2015 (ES6)', '2015', 'let/const, arrow, class, modul, Promise, Map/Set, template literal, destructuring'],
      ['ES2017', '2017', 'async/await, Object.entries/values'], ['ES2018', '2018', 'Rest/spread objek, Promise.finally, for await'],
      ['ES2020', '2020', 'BigInt, ?? dan ?., Promise.allSettled, globalThis, import() dinamis'],
      ['ES2022', '2022', 'Field privat #, top-level await, at(), Error cause'], ['ES2023', '2023', 'toSorted, toReversed, with, findLast'],
      ['ES2024', '2024', 'Object.groupBy, Promise.withResolvers, ArrayBuffer resizable'], ['ES2025', '2025', 'Iterator helpers, metode Set (union, intersection), RegExp.escape, import JSON']]}],
    pts=['ECMAScript adalah standar, JavaScript implementasinya.', 'TC39 mengelola fitur lewat stage 0 sampai 4.', 'ES2015 adalah lompatan terbesar; sejak itu rilis tahunan.', 'Babel/esbuild untuk transpile, polyfill untuk API yang belum ada.'],
    qs=[q('Nama standar resmi bahasa JavaScript?', ['ECMAScript', 'JScript', 'TypeScript'], 0, 'Distandarkan Ecma International sebagai ECMA-262.'),
        q('Fitur yang hadir di ES2015?', ['let, const, arrow function, dan class', 'async/await', 'Optional chaining'], 0, 'async/await di ES2017, ?. di ES2020.'),
        q('Fungsi transpiler seperti Babel?', ['Mengubah sintaks baru menjadi sintaks lama yang dimengerti browser lama', 'Menjalankan JS di server', 'Mengompres gambar'], 0, 'Transpile = terjemahan antar versi bahasa.')]),
  JT('Cara menjalankan JavaScript',
    ['<b>1. Konsol browser.</b> Tekan F12 (atau Ctrl+Shift+J / Cmd+Option+J), buka tab <b>Console</b>, ketik kode, lalu Enter. Cocok untuk mencoba potongan kecil dan memeriksa halaman yang sedang terbuka.',
     '<b>2. Di halaman HTML.</b> Tulis kode di file terpisah dan muat dengan tag script di akhir body, atau di head dengan atribut <code>defer</code> agar HTML selesai dibaca dulu. Atribut <code>type="module"</code> mengaktifkan import/export dan strict mode, serta otomatis bersifat defer.',
     '<b>3. Node.js.</b> Pasang Node versi LTS dari nodejs.org (atau lewat nvm/fnm), lalu jalankan <code>node app.js</code>. Ketik <code>node</code> saja untuk masuk <b>REPL</b> (Read-Eval-Print Loop). File berakhiran <code>.mjs</code> atau proyek dengan <code>"type": "module"</code> di package.json memakai modul ES.',
     '<b>4. Playground online</b> seperti CodePen, JSFiddle, StackBlitz, atau tombol <b>Jalankan</b> di Ruang Kode. Di dunia kerja, editor yang umum adalah VS Code dengan ekstensi ESLint dan Prettier.'],
    "<!-- index.html -->\n<!doctype html>\n<html lang=\"id\">\n<head>\n  <meta charset=\"utf-8\">\n  <title>Belajar JS</title>\n  <script src=\"app.js\" defer></script>        <!-- skrip biasa, jalan setelah HTML siap -->\n  <script type=\"module\" src=\"main.js\"></script> <!-- modul ES -->\n</head>\n<body>\n  <h1 id=\"judul\">Halo</h1>\n</body>\n</html>\n\n// app.js\ndocument.querySelector('#judul').textContent = 'Halo dari JavaScript!';\nconsole.log('Halaman siap');\n\n# terminal\n$ node --version\nv22.22.0\n$ node app-server.js\n$ node                # masuk REPL, keluar dengan .exit atau Ctrl+D\n> 2 ** 10\n1024",
    'html',
    tb=[{'c': 'Cara memuat skrip di HTML', 'h': ['Cara', 'Kapan dijalankan', 'Urutan antar skrip'], 'r': [
      ['script biasa di head', 'Segera, menghentikan parsing HTML', 'Sesuai urutan'], ['script di akhir body', 'Setelah HTML di atasnya terbaca', 'Sesuai urutan'],
      ['defer', 'Setelah HTML selesai diparse', 'Sesuai urutan'], ['async', 'Begitu selesai diunduh', 'Tidak dijamin (cocok untuk analytics)'], ['type="module"', 'Seperti defer, mode strict, mendukung import', 'Sesuai urutan']]}],
    pts=['Konsol DevTools untuk eksperimen cepat.', 'Di HTML: pakai defer atau type="module".', 'Node.js menjalankan JS di terminal; REPL untuk mencoba.', 'VS Code + ESLint + Prettier adalah setelan umum.'],
    qs=[q('Atribut script yang menunda eksekusi sampai HTML selesai diparse dan tetap menjaga urutan?', ['defer', 'async', 'lazy'], 0, 'async tidak menjamin urutan.'),
        q('Perintah untuk menjalankan file app.js dengan Node?', ['node app.js', 'npm app.js', 'js run app.js'], 0, 'node diikuti nama file.')]),
]),

M('Variabel, hoisting, dan scope', 'Pemula',
  'var, let, const, aturan penamaan, hoisting dan Temporal Dead Zone, serta block, function, dan global scope.',
  ['Variables', 'Variable Declarations', 'var', 'let', 'const', 'Hoisting', 'Variable Naming Rules', 'Variable Scopes', 'Block Scope', 'Function Scope', 'Global Scope'], [
  J('var, let, dan const',
    ['Variabel adalah nama untuk sebuah nilai. JS punya tiga kata kunci: <code>const</code> untuk nama yang <b>tidak akan di-assign ulang</b>, <code>let</code> untuk nilai yang akan berubah, dan <code>var</code> (gaya lama sebelum ES2015).',
     'Aturan praktis tim profesional (dan aturan ESLint <code>prefer-const</code>, <code>no-var</code>): <b>pakai const secara bawaan</b>, ganti ke let hanya jika memang perlu di-assign ulang, dan jangan memakai var di kode baru.',
     'Penting: <code>const</code> mengunci <b>ikatan (binding)</b>, bukan isinya. Objek atau array yang disimpan di const tetap bisa diubah isinya (<b>mutasi</b>). Untuk membekukan objek, pakai <code>Object.freeze()</code> (dangkal, hanya satu tingkat).'],
    "const PPN = 0.11;\nlet saldo = 100000;\nsaldo -= 25000;              // let boleh di-assign ulang\nconsole.log('Saldo:', saldo);\n\ntry {\n  PPN = 0.12;                 // const tidak boleh\n} catch (e) {\n  console.log(e.name + ':', e.message);\n}\n\nconst keranjang = ['kopi'];\nkeranjang.push('teh');       // mutasi isi tetap boleh\nconsole.log(keranjang);\n\nconst cfg = Object.freeze({ tema: 'gelap' });\ntry {\n  cfg.tema = 'terang';       // modul ES = strict mode: TypeError\n} catch (e) { console.log(e.name); }\nconsole.log(cfg.tema, Object.isFrozen(cfg));",
    tb=[{'c': 'Perbandingan var, let, const', 'h': ['Sifat', 'var', 'let', 'const'], 'r': [
      ['Scope', 'Function', 'Block', 'Block'], ['Hoisting', 'Ya, diisi undefined', 'Ya, tetapi TDZ', 'Ya, tetapi TDZ'], ['Assign ulang', 'Boleh', 'Boleh', 'Tidak'],
      ['Deklarasi ulang di scope sama', 'Boleh', 'SyntaxError', 'SyntaxError'], ['Wajib diberi nilai awal', 'Tidak', 'Tidak', 'Ya'], ['Jadi properti window (global)', 'Ya', 'Tidak', 'Tidak']]}],
    pts=['Bawaan const, let jika perlu berubah, hindari var.', 'const mengunci binding, bukan isi objek.', 'Object.freeze membekukan satu tingkat.'],
    qs=[q('Hasil const daftar = [1]; daftar.push(2);?', ['Berhasil, daftar menjadi [1, 2]', 'TypeError karena const', 'SyntaxError'], 0, 'Mutasi isi diizinkan; yang dilarang assign ulang.'),
        q('Kata kunci yang dianjurkan untuk penghitung di perulangan for?', ['let', 'const', 'var'], 0, 'Nilainya berubah setiap putaran.')],
    so=[SX('Buat <code>const harga = 45000</code> dan <code>let jumlah = 2</code>. Tambah jumlah menjadi 3, lalu cetak total. Coba juga meng-assign ulang harga dan tangkap errornya.', 'Bungkus assign ulang const dengan try/catch dan cetak e.name.',
           "const harga = 45000;\nlet jumlah = 2;\njumlah = 3;\nconsole.log('Total:', harga * jumlah);\ntry {\n  harga = 50000;\n} catch (e) {\n  console.log('Gagal:', e.name);\n}")]),
  J('Aturan penamaan variabel',
    ['Nama variabel (<b>identifier</b>) boleh berisi huruf, angka, <code>_</code>, dan <code>$</code>, tetapi <b>tidak boleh diawali angka</b> dan tidak boleh berupa kata kunci (<b>reserved word</b>) seperti <code>class</code>, <code>return</code>, <code>new</code>, <code>let</code>. JS <b>case-sensitive</b>: <code>nama</code> dan <code>Nama</code> adalah dua variabel berbeda.',
     'Konvensi industri: <b>camelCase</b> untuk variabel dan fungsi (<code>totalHarga</code>), <b>PascalCase</b> untuk class dan komponen (<code>KeranjangBelanja</code>), <b>UPPER_SNAKE_CASE</b> untuk konstanta konfigurasi (<code>MAX_RETRY</code>), awalan <code>is</code>/<code>has</code>/<code>can</code> untuk boolean (<code>isAktif</code>), dan awalan <code>#</code> untuk field privat class.',
     'Nama yang baik menjelaskan <b>maksud</b>, bukan tipe: <code>hariSejakLogin</code> lebih jelas dari <code>d</code> atau <code>angka1</code>. Satu huruf hanya wajar untuk indeks perulangan pendek (<code>i</code>, <code>j</code>). Di tim, pilih satu bahasa penamaan (Indonesia atau Inggris) dan konsisten.'],
    "const totalHarga = 125000;        // camelCase\nconst MAX_PERCOBAAN = 3;          // konstanta konfigurasi\nconst isMember = true;            // boolean dengan awalan is\nconst $tombol = 'elemen DOM';     // $ boleh (sering dipakai untuk elemen)\nconst _internal = 'hanya modul';  // _ menandai internal (konvensi)\n\nlet nama = 'rina', Nama = 'RINA';\nconsole.log(nama === Nama);       // case-sensitive\n\n// const 2tahun = 2;   SyntaxError: tidak boleh diawali angka\n// const class = 'A';  SyntaxError: kata kunci\nconst hariSejakLogin = 4;\nconsole.log(`${totalHarga} ${MAX_PERCOBAAN} ${isMember} ${hariSejakLogin}`);",
    tb=[{'c': 'Konvensi penamaan', 'h': ['Gaya', 'Dipakai untuk', 'Contoh'], 'r': [
      ['camelCase', 'Variabel, fungsi, metode', 'hitungOngkir, jumlahItem'], ['PascalCase', 'Class, komponen React, tipe', 'Pesanan, KartuProduk'],
      ['UPPER_SNAKE_CASE', 'Konstanta konfigurasi', 'API_URL, BATAS_UNGGAH_MB'], ['isX / hasX / canX', 'Boolean', 'isLogin, hasDiskon'], ['#nama', 'Field privat class', '#saldo'], ['kebab-case', 'Nama file, bukan variabel', 'kartu-produk.js']]}],
    pts=['Huruf, angka, _, $; tidak diawali angka; bukan kata kunci.', 'Case-sensitive.', 'camelCase, PascalCase, UPPER_SNAKE_CASE sesuai peran.', 'Nama menjelaskan maksud.'],
    qs=[q('Nama variabel yang valid?', ['_jumlah2', '2jumlah', 'jumlah-item'], 0, 'Tanda minus dibaca sebagai operator; tidak boleh diawali angka.'),
        q('Gaya penamaan untuk class?', ['PascalCase', 'camelCase', 'snake_case'], 0, 'Contoh: class KeranjangBelanja.')]),
  J('Hoisting dan Temporal Dead Zone',
    ['Sebelum kode dijalankan, engine membuat <b>execution context</b> dan mendaftarkan semua deklarasi di scope itu. Efek ini disebut <b>hoisting</b> (seolah deklarasi "diangkat" ke atas).',
     '<b>Deklarasi fungsi</b> di-hoist lengkap, jadi bisa dipanggil sebelum ditulis. <b>var</b> di-hoist dan langsung diisi <code>undefined</code>, sehingga membacanya sebelum baris deklarasi tidak error tetapi menghasilkan undefined (sumber bug klasik).',
     '<b>let, const, dan class</b> juga di-hoist tetapi tidak diinisialisasi. Rentang dari awal scope sampai baris deklarasinya disebut <b>Temporal Dead Zone (TDZ)</b>; mengaksesnya di sana melempar <code>ReferenceError</code>. TDZ justru membantu: error yang jelas lebih baik daripada undefined diam-diam.',
     'Function expression dan arrow function mengikuti aturan variabelnya: <code>const f = () =&gt; {}</code> tidak bisa dipanggil sebelum barisnya.'],
    "console.log(sapa('Andi'));        // deklarasi fungsi: hoist penuh\nfunction sapa(n) { return 'Halo ' + n; }\n\nconsole.log(kota);                // var: undefined, bukan error\nvar kota = 'Medan';\n\ntry {\n  console.log(umur);              // let di TDZ\n} catch (e) { console.log(e.name, '-', e.message); }\nlet umur = 20;\n\ntry {\n  hitung();                       // const + arrow: masih TDZ\n} catch (e) { console.log(e.name, '-', e.message); }\nconst hitung = () => 42;\n\nconsole.log(typeof belumAda);     // typeof aman untuk nama yang tidak ada",
    tb=[{'c': 'Perilaku hoisting', 'h': ['Deklarasi', 'Di-hoist?', 'Nilai sebelum baris deklarasi'], 'r': [
      ['function f() {}', 'Ya, lengkap', 'Fungsi siap dipanggil'], ['var x', 'Ya', 'undefined'], ['let x / const x', 'Ya (TDZ)', 'ReferenceError'],
      ['class A {}', 'Ya (TDZ)', 'ReferenceError'], ['const f = function () {}', 'Mengikuti const', 'ReferenceError'], ['import', 'Ya, paling awal', 'Binding modul siap']]}],
    pts=['Hoisting: deklarasi didaftarkan sebelum eksekusi.', 'Deklarasi fungsi bisa dipanggil sebelum ditulis.', 'var berisi undefined; let/const/class kena TDZ.', 'Tulis deklarasi di atas sebelum dipakai agar mudah dibaca.'],
    qs=[q('Output console.log(x); var x = 5;?', ['undefined', '5', 'ReferenceError'], 0, 'var di-hoist dan diisi undefined.'),
        q('Output console.log(y); let y = 5;?', ['ReferenceError', 'undefined', '5'], 0, 'y berada di Temporal Dead Zone.')],
    so=[SX('Tunjukkan perbedaan deklarasi fungsi dan function expression: panggil keduanya sebelum barisnya, tangkap error untuk yang gagal.', 'Deklarasi fungsi lolos; const dengan function expression melempar ReferenceError.',
           "console.log(luas(3));\ntry {\n  console.log(keliling(3));\n} catch (e) {\n  console.log('Error:', e.name);\n}\nfunction luas(s) { return s * s; }\nconst keliling = function (s) { return 4 * s; };")]),
  J('Block, function, dan global scope',
    ['<b>Scope</b> menentukan dari mana sebuah variabel bisa diakses. <b>Global scope</b>: dideklarasikan di luar fungsi atau blok; bisa diakses di mana saja. Di browser, <code>var</code> global dan deklarasi fungsi global menjadi properti <code>window</code>; di modul ES, variabel tingkat atas hanya berlaku di modul itu (<b>module scope</b>).',
     '<b>Function scope</b>: variabel di dalam fungsi hanya terlihat di dalam fungsi itu. <b>Block scope</b>: <code>let</code> dan <code>const</code> di dalam kurung kurawal (if, for, atau blok biasa) hanya terlihat di blok itu. <code>var</code> mengabaikan blok dan "bocor" ke fungsi pembungkusnya.',
     'Scope bersarang membentuk <b>scope chain</b>: saat mencari nama, engine melihat scope saat ini, lalu scope luarnya, sampai global. Variabel dalam yang bernama sama dengan variabel luar disebut <b>shadowing</b>. Minimalkan variabel global karena rawan bentrok antar skrip dan sulit dilacak.'],
    "const aplikasi = 'Ruang Kode';            // global (module scope di file ini)\n\nfunction hitungDiskon(harga) {\n  const persen = 10;                      // function scope\n  if (harga > 100000) {\n    let bonus = 5000;                     // block scope\n    var catatan = 'harga besar';          // var bocor ke seluruh fungsi\n    console.log('di blok:', bonus, catatan);\n  }\n  console.log('di fungsi:', typeof bonus, catatan);\n  return harga - harga * persen / 100;\n}\nconsole.log(hitungDiskon(200000));\nconsole.log(typeof persen);               // tidak terlihat di luar fungsi\n\nconst nilai = 'luar';\n{\n  const nilai = 'dalam';                  // shadowing\n  console.log(nilai, '-', aplikasi);      // scope chain sampai global\n}\nconsole.log(nilai);\n\nfor (var i = 0; i < 3; i++) {}\nconsole.log('var i setelah loop:', i);",
    tb=[{'c': 'Jenis scope', 'h': ['Scope', 'Dibuat oleh', 'Berlaku untuk'], 'r': [
      ['Global', 'Kode tingkat atas skrip biasa', 'var, let, const, function'], ['Module', 'Kode tingkat atas modul ES', 'Semua deklarasi di modul'],
      ['Function', 'Setiap fungsi', 'var, let, const, parameter'], ['Block', 'Kurung kurawal: if, for, while, try, blok', 'let, const, class'], ['Lexical (scope chain)', 'Posisi kode saat ditulis', 'Pencarian nama ke luar']]}],
    pts=['Global, module, function, dan block scope.', 'var tidak mengenal block scope.', 'Scope chain mencari nama dari dalam ke luar.', 'Shadowing: nama dalam menutupi nama luar.'],
    qs=[q('Output: if (true) { let a = 1; } console.log(typeof a);', ['undefined', 'number', 'ReferenceError'], 0, 'a hanya ada di blok if; typeof nama tak dikenal menghasilkan "undefined".'),
        q('Kenapa var di dalam for bisa dibaca setelah loop?', ['var berscope fungsi, bukan blok', 'var selalu global', 'Karena hoisting let'], 0, 'var mengabaikan blok.')],
    so=[SX('Buat fungsi <code>buatSalam(jam)</code>: di dalam blok if/else deklarasikan <code>const salam</code> sesuai jam (pagi di bawah 11, siang di bawah 15, sisanya sore). Kembalikan salam itu dengan benar walaupun const ada di dalam blok.', 'Deklarasikan let hasil di function scope, isi di blok, lalu return.',
           "function buatSalam(jam) {\n  let hasil;\n  if (jam < 11) {\n    const salam = 'Selamat pagi';\n    hasil = salam;\n  } else if (jam < 15) {\n    const salam = 'Selamat siang';\n    hasil = salam;\n  } else {\n    const salam = 'Selamat sore';\n    hasil = salam;\n  }\n  return hasil;\n}\nconsole.log(buatSalam(8));\nconsole.log(buatSalam(13));\nconsole.log(buatSalam(17));")]),
]),
]
