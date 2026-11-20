"""Jalur JavaScript bagian 5: JavaScript asinkron, event loop, Promise, async/await, dan bekerja dengan API."""
from rb_js import J, JT, SX, SN
from mobile_lib import M, q

SERVER = r"""import http from 'node:http';
// server API kecil di proses yang sama, supaya contoh fetch bisa dijalankan tanpa internet
const produk = [{ id: 1, nama: 'Kopi Gayo', harga: 85000 }, { id: 2, nama: 'Teh Melati', harga: 22000 }];
const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://x');
  const kirim = (status, data) => { res.writeHead(status, { 'Content-Type': 'application/json' }); res.end(JSON.stringify(data)); };
  if (req.method === 'GET' && url.pathname === '/api/produk') return kirim(200, produk);
  if (req.method === 'GET' && url.pathname.startsWith('/api/produk/')) {
    const p = produk.find(x => x.id === Number(url.pathname.split('/').pop()));
    return p ? kirim(200, p) : kirim(404, { error: 'Produk tidak ditemukan' });
  }
  if (req.method === 'POST' && url.pathname === '/api/pesanan') {
    let body = '';
    for await (const potong of req) body += potong;
    const data = JSON.parse(body);
    if (req.headers.authorization !== 'Bearer token-demo') return kirim(401, { error: 'Belum login' });
    return kirim(201, { id: 501, ...data, status: 'dibuat' });
  }
  if (url.pathname === '/api/lambat') return setTimeout(() => kirim(200, { ok: true }), 500);
  kirim(404, { error: 'Rute tidak ada' });
});
await new Promise(r => server.listen(0, r));
const BASE = `http://localhost:${server.address().port}`;
"""

JS5 = [
M('JavaScript asinkron', 'Menengah',
  'Event loop, setTimeout dan setInterval, callback dan callback hell, Promise, async/await, serta penanganan error asinkron.',
  ['Asynchronous JavaScript', 'Event Loop', 'setTimeout', 'setInterval', 'Callbacks', 'Callback Hell', 'Promises', 'async/await'], [
  J('Event loop: cara JS menangani hal asinkron',
    ['JS menjalankan kode di <b>satu thread</b> dengan satu <b>call stack</b>. Pekerjaan yang lama (timer, jaringan, membaca file) diserahkan ke lingkungan (<b>Web API</b> di browser, <b>libuv</b> di Node). Saat selesai, callback-nya dimasukkan ke antrean dan dijalankan oleh <b>event loop</b> ketika call stack kosong. Karena itu JS bisa <b>non-blocking</b> walau single-threaded.',
     'Ada dua antrean utama: <b>microtask queue</b> (callback Promise <code>then/catch/finally</code>, <code>await</code>, <code>queueMicrotask</code>, MutationObserver) dan <b>macrotask/task queue</b> (setTimeout, setInterval, event I/O, event klik). Aturannya: jalankan kode sinkron sampai habis, lalu <b>kosongkan semua microtask</b>, lalu ambil <b>satu</b> macrotask, kosongkan microtask lagi, (browser bisa render), dan ulangi.',
     'Konsekuensi praktis: <code>setTimeout(fn, 0)</code> tidak langsung jalan, melainkan setelah kode sinkron dan semua microtask. Kode sinkron yang berat (loop jutaan iterasi) <b>memblokir</b> event loop sehingga halaman macet dan tidak bisa diklik; pecah pekerjaannya atau pindahkan ke <b>Web Worker</b>. Di Node, <code>process.nextTick</code> berjalan bahkan sebelum microtask Promise (contoh ini dijalankan sebagai skrip CommonJS; di modul ES urutan nextTick bisa berbeda karena modul dievaluasi secara asinkron).'],
    "console.log('1. sinkron: mulai');\nsetTimeout(() => console.log('6. macrotask: setTimeout 0'), 0);\nsetTimeout(() => console.log('7. macrotask: setTimeout 10'), 10);\nPromise.resolve().then(() => console.log('4. microtask: then'));\nqueueMicrotask(() => console.log('5. microtask: queueMicrotask'));\nprocess.nextTick(() => console.log('3. nextTick (khusus Node)'));\n(async () => {\n  console.log('2. sinkron: isi async sebelum await');\n  await null;\n  console.log('5b. microtask: setelah await');\n})();\nconsole.log('2b. sinkron: selesai');\n\nsetTimeout(() => {\n  console.log('8. macrotask A');\n  Promise.resolve().then(() => console.log('9. microtask dari A, sebelum macrotask B'));\n}, 20);\nsetTimeout(() => console.log('10. macrotask B'), 20);",
    cjs=True,
    tb=[{'c': 'Antrean di event loop', 'h': ['Antrean', 'Isinya', 'Kapan dijalankan'], 'r': [
      ['Call stack', 'Kode sinkron', 'Sekarang, sampai habis'], ['process.nextTick (Node)', 'Callback nextTick', 'Setelah operasi saat ini, sebelum Promise'],
      ['Microtask', 'then/catch/finally, await, queueMicrotask', 'Semua dikosongkan setelah setiap task'], ['Macrotask (task)', 'setTimeout, setInterval, I/O, event UI', 'Satu per putaran loop'],
      ['Rendering (browser)', 'requestAnimationFrame, layout, paint', 'Di antara task, sekitar 60 kali per detik']]}],
    pts=['Single-threaded + event loop = non-blocking.', 'Urutan: sinkron, semua microtask, satu macrotask, ulangi.', 'Promise (microtask) mendahului setTimeout 0 (macrotask).', 'Kode sinkron berat memblokir UI.'],
    qs=[q("Urutan: setTimeout(()=>log('A')); Promise.resolve().then(()=>log('B')); log('C')", ['C B A', 'A B C', 'C A B'], 0, 'Sinkron, lalu microtask, lalu macrotask.'),
        q('Kenapa loop berat membuat tombol tidak bisa diklik?', ['Call stack tidak kosong sehingga event klik tidak diproses', 'Browser mematikan JS', 'Karena microtask terlalu banyak saja'], 0, 'Event loop menunggu stack kosong.')],
    so=[SX('Tebak lalu buktikan urutan keluaran: log "a", setTimeout log "b", Promise then log "c", lalu then berantai log "d", log "e".', 'Sinkron a, e; microtask c, d; macrotask b.',
           "console.log('a');\nsetTimeout(() => console.log('b'));\nPromise.resolve().then(() => console.log('c')).then(() => console.log('d'));\nconsole.log('e');")]),
  J('setTimeout dan setInterval',
    ['<code>setTimeout(fn, ms, ...args)</code> menjadwalkan fn <b>sekali</b> setelah <b>minimal</b> ms milidetik (bisa lebih lambat jika thread sibuk). <code>setInterval(fn, ms)</code> menjalankannya <b>berulang</b>. Keduanya mengembalikan ID yang dipakai untuk membatalkan dengan <code>clearTimeout</code>/<code>clearInterval</code>.',
     'Browser membatasi timer: tab di latar belakang dibatasi sekitar sekali per detik, dan timer bersarang lebih dari 5 tingkat minimal 4 ms. Untuk animasi gunakan <code>requestAnimationFrame</code>, bukan setInterval. Untuk polling yang memanggil server, <b>setTimeout rekursif</b> lebih aman daripada setInterval karena panggilan berikutnya baru dijadwalkan setelah yang sebelumnya selesai.',
     'Dua pola wajib di frontend memakai timer dan closure: <b>debounce</b> (tunggu sampai pengguna berhenti mengetik, misalnya pencarian) dan <b>throttle</b> (batasi frekuensi, misalnya event scroll). Selalu bersihkan timer saat komponen dilepas (misalnya di cleanup useEffect) agar tidak bocor.'],
    "const mulai = Date.now();\nconst t = () => `${Math.round((Date.now() - mulai) / 100) * 100}ms`;\n\nsetTimeout((nama) => console.log(`[${t()}] halo ${nama}`), 100, 'Dina');\nconst batal = setTimeout(() => console.log('tidak pernah muncul'), 150);\nclearTimeout(batal);\n\nlet ke = 0;\nconst id = setInterval(() => {\n  ke++;\n  console.log(`[${t()}] interval ke-${ke}`);\n  if (ke === 3) { clearInterval(id); console.log('interval dihentikan'); }\n}, 200);\n\nfunction debounce(fn, tunggu) {\n  let timer;\n  return (...args) => {\n    clearTimeout(timer);\n    timer = setTimeout(() => fn(...args), tunggu);\n  };\n}\nconst cari = debounce(q => console.log(`[${t()}] cari ke server: \"${q}\"`), 320);\n['k', 'ko', 'kop', 'kopi'].forEach((q, i) => setTimeout(() => cari(q), i * 50));   // mengetik cepat\n\nfunction throttle(fn, jeda) {\n  let terakhir = 0;\n  return (...args) => {\n    const now = Date.now();\n    if (now - terakhir >= jeda) { terakhir = now; fn(...args); }\n  };\n}\nconst onScroll = throttle(i => console.log('scroll diproses', i), 1000);\nfor (let i = 1; i <= 5; i++) onScroll(i);   // hanya yang pertama diproses",
    tb=[{'c': 'Debounce vs throttle', 'h': ['Aspek', 'Debounce', 'Throttle'], 'r': [
      ['Perilaku', 'Jalan sekali setelah jeda tenang', 'Paling banyak sekali per interval'], ['Contoh', 'Pencarian saat mengetik, autosave', 'Scroll, resize, mousemove'],
      ['Event cepat 10 kali dalam 1 detik', 'Satu panggilan di akhir', 'Beberapa panggilan merata']]}],
    pts=['setTimeout sekali, setInterval berulang; batalkan dengan clear*.', 'Jeda adalah waktu minimal, bukan pasti.', 'requestAnimationFrame untuk animasi; setTimeout rekursif untuk polling.', 'Debounce dan throttle dibangun dari timer + closure.'],
    qs=[q('Pola untuk memanggil API pencarian hanya setelah pengguna berhenti mengetik?', ['Debounce', 'Throttle', 'setInterval'], 0, 'Debounce menunggu jeda tenang.'),
        q('Apakah setTimeout(fn, 100) dijamin tepat 100 ms?', ['Tidak, minimal 100 ms', 'Ya, selalu', 'Ya jika di Node'], 0, 'Menunggu call stack kosong.')],
    so=[SX('Buat hitung mundur 3, 2, 1, "Mulai!" dengan jeda 100 ms memakai setTimeout rekursif (bukan setInterval).', 'Fungsi hitung(n) mencetak n lalu menjadwalkan hitung(n - 1).',
           "function hitung(n) {\n  if (n === 0) return console.log('Mulai!');\n  console.log(n);\n  setTimeout(() => hitung(n - 1), 100);\n}\nhitung(3);")]),
  J('Callback dan callback hell',
    ['<b>Callback</b> adalah fungsi yang dikirim ke fungsi lain untuk dipanggil nanti, misalnya saat data siap. Konvensi lama Node adalah <b>error-first callback</b>: <code>callback(err, hasil)</code>, di mana argumen pertama berisi error atau null.',
     'Saat beberapa operasi asinkron bergantung satu sama lain, callback bersarang semakin dalam membentuk <b>callback hell</b> atau <b>pyramid of doom</b>: sulit dibaca, error harus ditangani di setiap tingkat, dan alur sulit diikuti. Masalah lain adalah <b>inversion of control</b>: kita menyerahkan kendali ke kode lain yang mungkin memanggil callback dua kali atau tidak sama sekali.',
     'Solusinya adalah <b>Promise</b> dan <b>async/await</b>. API lama berbasis callback bisa diubah menjadi Promise (<b>promisify</b>), misalnya dengan <code>util.promisify</code> di Node atau membungkusnya dengan <code>new Promise</code>.'],
    "function ambilUser(id, cb) {\n  setTimeout(() => (id > 0 ? cb(null, { id, nama: 'Rina' }) : cb(new Error('id tidak valid'))), 30);\n}\nfunction ambilPesanan(user, cb) { setTimeout(() => cb(null, [{ no: 'INV-7', total: 150000 }]), 30); }\nfunction ambilPengiriman(pesanan, cb) { setTimeout(() => cb(null, { resi: 'JNE123', status: 'dikirim' }), 30); }\n\n// callback hell: setiap langkah bersarang dan error dicek di setiap tingkat\nambilUser(1, (err, user) => {\n  if (err) return console.log('gagal user', err.message);\n  ambilPesanan(user, (err, pesanan) => {\n    if (err) return console.log('gagal pesanan');\n    ambilPengiriman(pesanan[0], (err, kirim) => {\n      if (err) return console.log('gagal kirim');\n      console.log(`[callback] ${user.nama} - ${pesanan[0].no} - ${kirim.status}`);\n    });\n  });\n});\n\n// promisify lalu tulis datar dengan async/await\nconst jadiPromise = fn => (...args) => new Promise((ok, gagal) => fn(...args, (err, v) => (err ? gagal(err) : ok(v))));\nconst [userP, pesananP, kirimP] = [ambilUser, ambilPesanan, ambilPengiriman].map(jadiPromise);\nsetTimeout(async () => {\n  try {\n    const user = await userP(1);\n    const pesanan = await pesananP(user);\n    const kirim = await kirimP(pesanan[0]);\n    console.log(`[async] ${user.nama} - ${pesanan[0].no} - ${kirim.status}`);\n    await userP(-1);\n  } catch (e) {\n    console.log('[async] satu catch untuk semua:', e.message);\n  }\n}, 200);",
    pts=['Callback = fungsi yang dipanggil nanti.', 'Error-first callback: cb(err, hasil).', 'Callback hell: bersarang, error berulang, inversion of control.', 'Promisify lalu pakai async/await.'],
    qs=[q('Argumen pertama pada error-first callback?', ['Error atau null', 'Hasil', 'Callback berikutnya'], 0, 'Konvensi Node.'),
        q('Masalah utama callback hell?', ['Kode bersarang sulit dibaca dan error ditangani berulang', 'Lebih lambat dari Promise', 'Tidak bisa di browser'], 0, 'Masalahnya keterbacaan dan alur kontrol.')]),
  J('Promise',
    ['<b>Promise</b> adalah object yang mewakili hasil operasi asinkron di masa depan. Statusnya <b>pending</b>, lalu berubah sekali menjadi <b>fulfilled</b> (berhasil, dengan nilai) atau <b>rejected</b> (gagal, dengan alasan/error); keduanya disebut <b>settled</b> dan tidak bisa berubah lagi.',
     'Konsumsi dengan <code>.then(onSukses)</code>, <code>.catch(onGagal)</code>, dan <code>.finally(onSelesai)</code>. Setiap then mengembalikan Promise baru sehingga bisa <b>dirantai</b>; nilai yang di-return diteruskan ke then berikutnya, dan error melompat ke catch terdekat. Selalu return Promise di dalam then agar rantai menunggu, dan selalu akhiri dengan catch.',
     'Kombinator: <code>Promise.all</code> (paralel, gagal jika satu gagal), <code>Promise.allSettled</code> (tunggu semua, laporkan status masing-masing), <code>Promise.race</code> (yang pertama settled, cocok untuk timeout), <code>Promise.any</code> (yang pertama sukses, AggregateError jika semua gagal). <code>Promise.withResolvers()</code> (ES2024) memberi promise beserta fungsi resolve/reject-nya.'],
    "const tunda = (ms, nilai, gagal = false) =>\n  new Promise((resolve, reject) => setTimeout(() => (gagal ? reject(new Error(nilai)) : resolve(nilai)), ms));\n\nconst p = tunda(50, 'data siap');\nconsole.log(p);                                   // masih pending\np.then(v => { console.log('then:', v); return v.length; })\n .then(n => console.log('panjang:', n))\n .finally(() => console.log('finally: selesai'));\n\ntunda(60, 'server error', true)\n  .then(() => console.log('tidak dijalankan'))\n  .catch(e => { console.log('catch:', e.message); return 'nilai cadangan'; })\n  .then(v => console.log('lanjut dengan', v));\n\nconst stok = () => tunda(80, { stok: 12 });\nconst harga = () => tunda(40, { harga: 85000 });\nconst ulasan = () => tunda(60, 'layanan ulasan mati', true);\n\nsetTimeout(async () => {\n  console.log('all:', await Promise.all([stok(), harga()]));\n  const hasil = await Promise.allSettled([stok(), ulasan()]);\n  console.log('allSettled:', hasil.map(h => h.status));\n  console.log('race:', await Promise.race([tunda(100, 'lambat'), tunda(10, 'cepat')]));\n  console.log('any:', await Promise.any([ulasan(), harga()]));\n  try { await Promise.all([stok(), ulasan()]); } catch (e) { console.log('all gagal:', e.message); }\n  try { await Promise.any([ulasan(), ulasan()]); } catch (e) { console.log(e.name, e.errors.length); }\n  const { promise, resolve } = Promise.withResolvers();\n  setTimeout(() => resolve('diselesaikan dari luar'), 10);\n  console.log(await promise);\n}, 150);",
    tb=[{'c': 'Kombinator Promise', 'h': ['Metode', 'Selesai saat', 'Hasil', 'Contoh pemakaian'], 'r': [
      ['Promise.all', 'Semua sukses atau satu gagal', 'Array nilai / error pertama', 'Muat beberapa data wajib paralel'],
      ['Promise.allSettled', 'Semua settled', 'Array {status, value/reason}', 'Dashboard dengan widget independen'],
      ['Promise.race', 'Yang pertama settled', 'Nilai/error pertama', 'Timeout permintaan'], ['Promise.any', 'Yang pertama sukses', 'Nilai / AggregateError', 'Server cermin (mirror) tercepat']]}],
    pts=['Status: pending lalu fulfilled atau rejected, sekali saja.', 'then berantai; return nilai/Promise; akhiri dengan catch.', 'all, allSettled, race, any untuk banyak Promise.', 'Promise.all menjalankan secara paralel.'],
    qs=[q('Kombinator yang tetap memberi semua hasil walau sebagian gagal?', ['Promise.allSettled', 'Promise.all', 'Promise.race'], 0, 'allSettled melaporkan status setiap Promise.'),
        q('Apa yang terjadi pada nilai yang di-return di dalam then?', ['Diteruskan ke then berikutnya', 'Dibuang', 'Menjadi error'], 0, 'then mengembalikan Promise baru.')],
    so=[SX('Buat fungsi <code>denganTimeout(promise, ms)</code> memakai Promise.race yang menolak dengan Error "timeout" jika promise lebih lambat dari ms. Uji dengan proses 50 ms (batas 100) dan 200 ms (batas 100).', 'Race antara promise asli dan promise yang reject setelah ms.',
           "const tunda = (ms, v) => new Promise(r => setTimeout(() => r(v), ms));\nfunction denganTimeout(p, ms) {\n  const batas = new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), ms));\n  return Promise.race([p, batas]);\n}\ndenganTimeout(tunda(50, 'cepat selesai'), 100).then(console.log, e => console.log(e.message));\ndenganTimeout(tunda(200, 'lambat'), 100).then(console.log, e => console.log('gagal:', e.message));")]),
  J('async dan await',
    ['<code>async function</code> selalu mengembalikan Promise. Di dalamnya, <code>await promise</code> menjeda fungsi itu (bukan seluruh program) sampai Promise settled, lalu menghasilkan nilainya atau melempar error-nya. Hasilnya kode asinkron yang terbaca seperti kode sinkron, dan error ditangani dengan try/catch biasa.',
     'Jebakan performa: <code>await</code> berurutan untuk operasi yang <b>tidak saling bergantung</b> membuatnya berjalan serial. Mulai semua dulu, lalu tunggu bersama dengan <code>await Promise.all([...])</code>. Sebaliknya, jangan pakai <code>forEach(async ...)</code> karena forEach tidak menunggu; gunakan <code>for...of</code> dengan await (serial) atau <code>Promise.all(arr.map(async ...))</code> (paralel).',
     '<b>Top-level await</b> (ES2022) boleh dipakai langsung di modul ES. Promise yang ditolak tanpa catch memicu <b>unhandled rejection</b> (di Node modern, proses berhenti), jadi selalu tangani error. Untuk membatalkan operasi seperti fetch, gunakan <code>AbortController</code>.'],
    "const tunda = (ms, v) => new Promise(r => setTimeout(() => r(v), ms));\nconst waktu = async (label, fn) => { const t0 = Date.now(); const h = await fn(); console.log(label, h, `~${Math.round((Date.now() - t0) / 100) * 100}ms`); };\n\nasync function profil() { return { nama: 'Wulan' }; }\nconsole.log(profil() instanceof Promise);\n\nawait waktu('serial  :', async () => {\n  const a = await tunda(200, 'user');\n  const b = await tunda(200, 'notifikasi');\n  return [a, b];\n});\nawait waktu('paralel :', async () => {\n  const [a, b] = await Promise.all([tunda(200, 'user'), tunda(200, 'notifikasi')]);\n  return [a, b];\n});\n\nconst ids = [3, 1, 2];\nconst hasil = [];\nids.forEach(async id => { await tunda(id * 10); hasil.push(id); });\nconsole.log('forEach tidak menunggu:', hasil);\nconst urut = [];\nfor (const id of ids) { await tunda(id * 10); urut.push(id); }\nconsole.log('for...of menunggu    :', urut);\nconsole.log('map + Promise.all    :', await Promise.all(ids.map(async id => (await tunda(id * 10), id * 100))));\n\nasync function bayar(nominal) {\n  if (nominal <= 0) throw new Error('nominal harus positif');\n  await tunda(20);\n  return `dibayar ${nominal}`;\n}\ntry {\n  console.log(await bayar(50000));\n  console.log(await bayar(0));\n} catch (e) {\n  console.log('tertangkap:', e.message);\n}",
    tb=[{'c': 'Pola async yang benar dan salah', 'h': ['Kebutuhan', 'Salah', 'Benar'], 'r': [
      ['Dua permintaan independen', 'await a(); await b();', 'await Promise.all([a(), b()])'], ['Proses array satu per satu', 'arr.forEach(async x => ...)', 'for (const x of arr) await f(x)'],
      ['Proses array paralel', 'arr.forEach(async ...)', 'await Promise.all(arr.map(f))'], ['Tangani error', 'Tanpa catch', 'try/catch di sekitar await'], ['Kembalikan nilai', 'return di callback then yang lupa di-return', 'return await atau return promise']]}],
    pts=['async selalu mengembalikan Promise.', 'await hanya menjeda fungsi async itu.', 'Operasi independen: Promise.all, bukan await berurutan.', 'forEach tidak menunggu async; pakai for...of atau map + Promise.all.', 'Top-level await di modul ES.'],
    qs=[q('Nilai kembali async function f() { return 5 }?', ['Promise yang fulfilled dengan 5', '5', 'undefined'], 0, 'async selalu membungkus dengan Promise.'),
        q('Cara tercepat menunggu tiga fetch yang independen?', ['await Promise.all([f1(), f2(), f3()])', 'Tiga await berurutan', 'forEach dengan async'], 0, 'Berjalan paralel.')],
    so=[SX('Simulasikan unggah 3 file (durasi 30, 10, 20 ms) secara paralel dengan async/await dan Promise.all; cetak tiap file saat selesai lalu "semua terunggah".', 'Fungsi unggah(nama, ms) yang await tunda lalu console.log.',
           "const tunda = ms => new Promise(r => setTimeout(r, ms));\nasync function unggah(nama, ms) {\n  await tunda(ms);\n  console.log(`${nama} selesai`);\n  return nama;\n}\nconst hasil = await Promise.all([unggah('a.jpg', 30), unggah('b.pdf', 10), unggah('c.png', 20)]);\nconsole.log('semua terunggah:', hasil);")]),
]),

M('Bekerja dengan API', 'Menengah',
  'Fetch API, metode HTTP, header dan body JSON, penanganan status error, AbortController, serta XMLHttpRequest.',
  ['Working with APIs', 'Fetch', 'XMLHttpRequest'], [
  J('Fetch API: GET dan menangani respons',
    ['<code>fetch(url, opsi)</code> adalah API standar untuk permintaan HTTP di browser dan Node 18+. Ia mengembalikan Promise berisi object <code>Response</code>. Isi respons dibaca dengan metode yang juga mengembalikan Promise: <code>res.json()</code>, <code>res.text()</code>, <code>res.blob()</code>, <code>res.arrayBuffer()</code>, <code>res.formData()</code>; body hanya bisa dibaca sekali.',
     'Jebakan terpenting: fetch <b>hanya menolak (reject) saat gagal jaringan</b> (offline, DNS, CORS diblok). Status <b>404 atau 500 tetap fulfilled</b>. Selalu cek <code>res.ok</code> (true untuk status 200 sampai 299) atau <code>res.status</code>, lalu lempar error sendiri.',
     'Di proyek nyata, buat <b>wrapper</b> kecil (misalnya <code>api.get</code>) yang menambahkan base URL, header, pengecekan status, dan parsing JSON di satu tempat. Banyak tim memakai pustaka seperti <b>TanStack Query</b> atau SWR di atas fetch untuk cache, retry, dan status loading. Contoh di bawah menjalankan server API kecil di proses yang sama agar fetch benar-benar terjadi.'],
    SERVER + r"""
// 1. GET daftar produk
const res = await fetch(`${BASE}/api/produk`);
console.log(res.status, res.ok, res.headers.get('content-type'));
const daftar = await res.json();
console.log(daftar.map(p => p.nama));

// 2. 404 tidak membuat fetch reject
const r404 = await fetch(`${BASE}/api/produk/99`);
console.log('404 ->', r404.ok, r404.status, await r404.json());

// 3. wrapper yang mengecek status
async function ambilJSON(path) {
  const r = await fetch(BASE + path);
  if (!r.ok) {
    const body = await r.json().catch(() => ({}));
    throw new Error(`HTTP ${r.status}: ${body.error ?? r.statusText}`);
  }
  return r.json();
}
console.log(await ambilJSON('/api/produk/2'));
try { await ambilJSON('/api/produk/42'); } catch (e) { console.log('ditangkap:', e.message); }

// 4. kegagalan jaringan memang reject
try { await fetch('http://localhost:1/tidak-ada'); } catch (e) { console.log('jaringan gagal:', e.name, e.message); }
server.close();""",
    tb=[{'c': 'Kode status HTTP yang sering ditemui', 'h': ['Status', 'Arti', 'Tindakan di frontend'], 'r': [
      ['200 OK', 'Berhasil', 'Tampilkan data'], ['201 Created', 'Data dibuat', 'Tampilkan sukses, perbarui daftar'], ['204 No Content', 'Berhasil tanpa body', 'Jangan panggil res.json()'],
      ['400 Bad Request', 'Input salah', 'Tampilkan pesan validasi'], ['401 Unauthorized', 'Belum login atau token habis', 'Arahkan ke login / refresh token'], ['403 Forbidden', 'Tidak punya izin', 'Sembunyikan aksi'],
      ['404 Not Found', 'Tidak ada', 'Halaman atau pesan tidak ditemukan'], ['429 Too Many Requests', 'Kena rate limit', 'Tunggu lalu coba lagi'], ['500 / 503', 'Server error / sibuk', 'Pesan ramah + retry']]}],
    pts=['fetch mengembalikan Promise<Response>; baca body dengan res.json().', 'fetch tidak reject untuk 404/500: cek res.ok.', 'Body hanya bisa dibaca sekali.', 'Buat wrapper API terpusat.'],
    qs=[q('Apa yang terjadi jika fetch menerima status 500?', ['Promise tetap fulfilled, res.ok bernilai false', 'Promise reject', 'fetch mengulang otomatis'], 0, 'Reject hanya untuk kegagalan jaringan.'),
        q('res.ok bernilai true untuk status?', ['200 sampai 299', 'Semua di bawah 500', 'Hanya 200'], 0, 'Rentang sukses HTTP.')]),
  J('POST JSON, header, dan AbortController',
    ['Untuk mengirim data, isi opsi fetch: <code>method</code> (POST, PUT, PATCH, DELETE), <code>headers</code> (misalnya <code>Content-Type: application/json</code> dan <code>Authorization: Bearer token</code>), dan <code>body</code> berupa <code>JSON.stringify(data)</code>. Untuk unggah file, kirim <code>FormData</code> dan <b>jangan</b> set Content-Type manual (browser mengisi boundary). Query string disusun dengan <code>URLSearchParams</code>.',
     '<b>AbortController</b> membatalkan permintaan: kirim <code>signal</code> ke fetch, lalu panggil <code>controller.abort()</code>; fetch menolak dengan <code>AbortError</code>. Untuk batas waktu ada jalan pintas <code>AbortSignal.timeout(ms)</code> (menolak dengan <code>TimeoutError</code>). Pola ini penting untuk pencarian saat mengetik (batalkan permintaan lama) dan cleanup di useEffect React.',
     'Opsi lain yang perlu dikenal: <code>credentials: "include"</code> untuk mengirim cookie lintas origin, <code>cache</code>, <code>mode</code>, dan <code>keepalive</code>. Permintaan lintas domain di browser tunduk pada <b>CORS</b>: server harus mengirim header <code>Access-Control-Allow-Origin</code>; error CORS tidak bisa diperbaiki dari sisi frontend.'],
    SERVER + r"""
async function buatPesanan(data, token) {
  const r = await fetch(`${BASE}/api/pesanan`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...(token && { Authorization: `Bearer ${token}` }) },
    body: JSON.stringify(data),
  });
  const body = await r.json();
  return `${r.status} ${JSON.stringify(body)}`;
}
console.log(await buatPesanan({ produkId: 1, qty: 2 }));
console.log(await buatPesanan({ produkId: 1, qty: 2 }, 'token-demo'));

const params = new URLSearchParams({ q: 'kopi susu', urut: 'termurah', hal: 1 });
console.log('query:', params.toString());

const ctrl = new AbortController();
const janji = fetch(`${BASE}/api/lambat`, { signal: ctrl.signal });
setTimeout(() => ctrl.abort(), 50);
try { await janji; } catch (e) { console.log('dibatalkan:', e.name); }

try {
  await fetch(`${BASE}/api/lambat`, { signal: AbortSignal.timeout(100) });
} catch (e) { console.log('kelamaan:', e.name); }
const cepat = await fetch(`${BASE}/api/lambat`, { signal: AbortSignal.timeout(2000) });
console.log('cukup waktu:', await cepat.json());
server.close();""",
    tb=[{'c': 'Metode HTTP', 'h': ['Metode', 'Fungsi', 'Body?', 'Idempoten?'], 'r': [
      ['GET', 'Ambil data', 'Tidak', 'Ya'], ['POST', 'Buat data / aksi', 'Ya', 'Tidak'], ['PUT', 'Ganti seluruh data', 'Ya', 'Ya'],
      ['PATCH', 'Ubah sebagian', 'Ya', 'Tidak selalu'], ['DELETE', 'Hapus', 'Biasanya tidak', 'Ya']]}],
    pts=['POST JSON: method, Content-Type, body JSON.stringify.', 'FormData untuk file, tanpa set Content-Type.', 'AbortController dan AbortSignal.timeout untuk membatalkan.', 'CORS diatur server, bukan frontend.'],
    qs=[q('Header wajib saat mengirim body JSON?', ["'Content-Type': 'application/json'", "'Accept': 'text/html'", "'Cache-Control': 'no-cache'"], 0, 'Agar server tahu formatnya.'),
        q('Nama error saat fetch dibatalkan dengan controller.abort()?', ['AbortError', 'TypeError', 'TimeoutError'], 0, 'TimeoutError hanya dari AbortSignal.timeout.')],
    so=[SN('Tulis fungsi pencarian di browser yang membatalkan permintaan sebelumnya setiap kali pengguna mengetik huruf baru.', 'Simpan controller di luar fungsi; abort yang lama sebelum fetch baru; abaikan AbortError.',
           "let ctrl;\nasync function cari(q) {\n  ctrl?.abort();\n  ctrl = new AbortController();\n  try {\n    const r = await fetch(`/api/cari?${new URLSearchParams({ q })}`, { signal: ctrl.signal });\n    if (!r.ok) throw new Error(`HTTP ${r.status}`);\n    tampilkan(await r.json());\n  } catch (e) {\n    if (e.name !== 'AbortError') tampilkanError(e);\n  }\n}\ninput.addEventListener('input', e => cari(e.target.value));")]),
  JT('XMLHttpRequest dan perbandingannya dengan fetch',
    ['<b>XMLHttpRequest</b> (XHR) adalah API lama (sejak awal 2000-an) yang memungkinkan <b>AJAX</b>: memuat data tanpa memuat ulang halaman, teknologi di balik Gmail dan Google Maps generasi awal. Walau namanya XML, XHR bisa mengambil JSON, teks, dan biner.',
     'XHR berbasis event dan callback (<code>onload</code>, <code>onerror</code>, <code>onprogress</code>), bukan Promise, sehingga lebih bertele-tele. Kelebihan yang masih membuatnya dipakai: event <code>upload.onprogress</code> untuk <b>progress bar unggah</b> yang belum ada padanannya yang sederhana di fetch. Pustaka <b>Axios</b> di browser juga memakai XHR di baliknya.',
     'Untuk kode baru, gunakan fetch. Kenali XHR karena masih ada di kode lama, plugin jQuery (<code>$.ajax</code>), dan pertanyaan wawancara. API ini hanya ada di browser, jadi contoh di bawah tidak dijalankan di Node.'],
    "// GET dengan XMLHttpRequest\nconst xhr = new XMLHttpRequest();\nxhr.open('GET', '/api/produk');\nxhr.responseType = 'json';\nxhr.onload = () => {\n  if (xhr.status >= 200 && xhr.status < 300) console.log('data', xhr.response);\n  else console.error('HTTP', xhr.status);\n};\nxhr.onerror = () => console.error('jaringan gagal');\nxhr.send();\n\n// unggah file dengan progress bar\nfunction unggah(file, onPersen) {\n  return new Promise((resolve, reject) => {\n    const x = new XMLHttpRequest();\n    x.open('POST', '/api/unggah');\n    x.upload.onprogress = e => e.lengthComputable && onPersen(Math.round(e.loaded / e.total * 100));\n    x.onload = () => (x.status < 300 ? resolve(x.response) : reject(new Error(`HTTP ${x.status}`)));\n    x.onerror = () => reject(new Error('jaringan gagal'));\n    const fd = new FormData();\n    fd.append('berkas', file);\n    x.send(fd);\n  });\n}\nawait unggah(inputFile.files[0], p => (progress.value = p));\n\n// padanannya dengan fetch (tanpa progress unggah)\nconst res = await fetch('/api/produk');\nif (!res.ok) throw new Error(`HTTP ${res.status}`);\nconsole.log(await res.json());",
    'js',
    tb=[{'c': 'XMLHttpRequest vs fetch vs Axios', 'h': ['Aspek', 'XMLHttpRequest', 'fetch', 'Axios'], 'r': [
      ['Gaya', 'Event/callback', 'Promise', 'Promise'], ['Tolak saat 4xx/5xx', 'Tidak (cek status)', 'Tidak (cek res.ok)', 'Ya'], ['Parse JSON', 'responseType', 'res.json()', 'Otomatis'],
      ['Progress unggah', 'Ya', 'Belum sederhana', 'Ya (lewat XHR)'], ['Batalkan', 'xhr.abort()', 'AbortController', 'AbortController'], ['Tersedia di Node', 'Tidak', 'Ya (18+)', 'Ya (pustaka)']]}],
    pts=['XHR adalah API AJAX lama berbasis event.', 'Kelebihan XHR: progress unggah.', 'Kode baru: fetch.', 'Axios memakai XHR di browser.'],
    qs=[q('Kenapa XHR masih dipakai untuk unggah file besar?', ['Punya event upload.onprogress untuk progress bar', 'Lebih aman dari fetch', 'Satu-satunya cara mengirim FormData'], 0, 'fetch belum punya progress unggah yang sederhana.')]),
]),
]
