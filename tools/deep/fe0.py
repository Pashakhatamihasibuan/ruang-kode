"""Pendalaman jalur Frontend Pemula. Contoh JavaScript dijalankan dengan Node 22 (ESM)."""
K = 'fe0'


def J(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='js')


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Apa kerja frontend developer?': dict(
  ist=[('Frontend', 'Bagian aplikasi yang dilihat dan dipakai pengguna di browser: tampilan, interaksi, dan pemanggilan API.'),
       ('Design handoff', 'Serah terima desain dari desainer (Figma) ke developer, berisi ukuran, token warna, dan state komponen.'),
       ('Sprint', 'Siklus kerja 1-2 minggu dalam Scrum; frontend mengambil tiket dari backlog lalu demo di akhir sprint.'),
       ('Definition of Done', 'Daftar syarat sebuah tiket dianggap selesai: lolos review, ada test, responsif, aksesibel, sudah di staging.')],
  cx=[T('Satu hari kerja frontend developer', '''
09.00  Daily stand-up 15 menit: kemarin, hari ini, hambatan
09.20  Ambil tiket FE-231 "Form checkout menampilkan error per field"
       - baca acceptance criteria, buka desain di Figma (state default, error, loading, sukses)
       - git switch -c feat/FE-231-checkout-error
10.00  Koding komponen + panggilan API, cek di 360px, 768px, 1280px
13.00  Tulis test (Vitest) untuk validasi, jalankan Lighthouse aksesibilitas
14.30  Buka pull request: deskripsi, tangkapan layar, cara menguji
15.00  Review PR rekan, balas komentar reviewer di PR sendiri
16.30  PR di-merge -> CI deploy otomatis ke staging -> QA menguji
       Tiket pindah ke kolom "Ready for QA"'''),
     J('Kontrak data yang dibicarakan frontend dan backend', '''
// Contoh respons API yang disepakati di awal sprint (kontrak)
const respons = { data: [{ id: 7, nama: "Kopi Gayo", harga: 85000, stok: 3 }], meta: { halaman: 1, total: 42 } };
for (const p of respons.data) {
  const label = p.stok === 0 ? "Habis" : p.stok < 5 ? `Sisa ${p.stok}` : "Tersedia";
  console.log(`${p.nama} - Rp${p.harga.toLocaleString("id-ID")} - ${label}`);
}
console.log(`Halaman ${respons.meta.halaman} dari ${Math.ceil(respons.meta.total / 20)}`);
''', 'Frontend mengubah data mentah dari API menjadi teks yang ramah pengguna: format rupiah, label stok, dan paginasi.')]),

'Variabel & tipe data': dict(
  ist=[('let / const', 'const untuk nilai yang tidak diikat ulang (default), let jika memang berubah; hindari var.'),
       ('Primitive types', 'string, number, bigint, boolean, undefined, null, symbol.'),
       ('typeof', 'Operator untuk memeriksa tipe; typeof null menghasilkan "object" (bug historis).'),
       ('Number precision', 'number adalah float 64-bit; bilangan bulat aman hanya sampai Number.MAX_SAFE_INTEGER.')],
  cx=[J('Tipe data dan jebakan angka besar', '''
const nama = "Sari";
let saldo = 150000;
saldo += 25000;
console.log(typeof nama, typeof saldo, typeof true, typeof undefined, typeof null);
console.log("0.1 + 0.2 =", 0.1 + 0.2);
console.log("batas aman:", Number.MAX_SAFE_INTEGER);
const idTransaksi = 9007199254740993;           // lebih dari batas aman
console.log("id rusak  :", idTransaksi, "| BigInt:", 9007199254740993n);
console.log("uang dalam sen:", (1999 + 1) / 100, "=> simpan rupiah/sen sebagai bilangan bulat");
''', 'ID dari database berukuran 64-bit sering dikirim sebagai string di JSON agar tidak rusak di JavaScript.')]),

'Operator & percabangan': dict(
  ist=[('Strict equality ===', 'Membandingkan nilai dan tipe tanpa konversi; == melakukan konversi yang membingungkan.'),
       ('Truthy / falsy', 'Nilai falsy: false, 0, -0, 0n, "", null, undefined, NaN.'),
       ('Nullish coalescing ??', 'Memberi default hanya jika nilai null/undefined; berbeda dengan || yang juga mengganti 0 dan "".'),
       ('Optional chaining ?.', 'Mengakses properti bersarang tanpa error jika ada yang null/undefined.')],
  cx=[J('?? vs || dan optional chaining pada data API', '''
console.log("0 == '0':", 0 == "0", "| 0 === '0':", 0 === "0", "| null == undefined:", null == undefined);
const pengaturan = { diskon: 0, catatan: "", alamat: null };
console.log("diskon || 10 :", pengaturan.diskon || 10, "<- 0 yang sah hilang");
console.log("diskon ?? 10 :", pengaturan.diskon ?? 10);
console.log("kota:", pengaturan.alamat?.kota ?? "(belum diisi)");
const nilai = 78;
const status = nilai >= 85 ? "A" : nilai >= 75 ? "B" : nilai >= 60 ? "C" : "D";
console.log("nilai", nilai, "=>", status);
''')]),

'Fungsi': dict(
  ist=[('Function declaration vs arrow function', 'function f(){} di-hoist; const f = () => {} lebih ringkas dan tidak punya this sendiri.'),
       ('Default parameter', 'Nilai bawaan parameter: function f(x = 1).'),
       ('Pure function', 'Tanpa efek samping; input sama selalu memberi output sama.'),
       ('Higher-order function', 'Fungsi yang menerima atau mengembalikan fungsi: map, filter, addEventListener.')],
  cx=[J('Fungsi kecil yang bisa digabung', '''
const rupiah = (n) => "Rp" + n.toLocaleString("id-ID");
const denganPpn = (n, tarif = 0.11) => Math.round(n * (1 + tarif));
const diskon = (persen) => (n) => n - Math.round(n * persen / 100);   // fungsi yang mengembalikan fungsi
const member = diskon(10);

const harga = [45000, 120000, 18500];
console.log(harga.map(member).map((x) => denganPpn(x)).map(rupiah));
function sapa(nama = "Tamu") { return `Halo, ${nama}!`; }
console.log(sapa(), sapa("Rina"));
''')]),

'Array & objek': dict(
  ist=[('Array methods', 'map, filter, reduce, find, some, every, sort; sebagian besar tidak mengubah array asli.'),
       ('Destructuring', 'Mengambil nilai dari array/objek ke variabel: const { nama, harga } = produk.'),
       ('Spread ...', 'Menyalin atau menggabungkan: [...a, ...b], { ...obj, harga: 10 }.'),
       ('Immutability', 'Membuat salinan baru alih-alih mengubah data lama; wajib di React state.')],
  cx=[J('Mengolah keranjang belanja tanpa mengubah data asli', '''
const keranjang = [
  { sku: "KP1", nama: "Kopi Gayo", harga: 85000, qty: 2 },
  { sku: "GL1", nama: "Gula aren", harga: 32500, qty: 1 },
  { sku: "SS1", nama: "Susu oat", harga: 29900, qty: 3 },
];
const total = keranjang.reduce((t, { harga, qty }) => t + harga * qty, 0);
const mahal = keranjang.filter((i) => i.harga > 30000).map((i) => i.nama);
const diperbarui = keranjang.map((i) => (i.sku === "GL1" ? { ...i, qty: i.qty + 1 } : i));
console.log("total:", total, "| di atas 30rb:", mahal);
console.log("qty gula asli:", keranjang[1].qty, "| versi baru:", diperbarui[1].qty);
const urut = [...keranjang].sort((a, b) => b.harga * b.qty - a.harga * a.qty).map((i) => i.sku);
console.log("urut subtotal:", urut, "| ada yang habis?", keranjang.some((i) => i.qty === 0));
''')]),

'DOM & event': dict(
  ist=[('DOM', 'Document Object Model: representasi pohon halaman HTML yang bisa diubah JavaScript.'),
       ('querySelector', 'Memilih elemen dengan selector CSS.'),
       ('Event delegation', 'Satu listener di elemen induk untuk banyak anak, memanfaatkan event bubbling.'),
       ('textContent vs innerHTML', 'textContent aman dari XSS; innerHTML menafsirkan HTML sehingga berbahaya untuk data pengguna.')],
  cx=[T('Event delegation untuk daftar yang dinamis', '''
<ul id="daftar">
  <li data-id="1">Kopi <button data-aksi="hapus">Hapus</button></li>
  <li data-id="2">Teh <button data-aksi="hapus">Hapus</button></li>
</ul>
<script>
  const daftar = document.querySelector("#daftar");
  // satu listener untuk semua tombol, termasuk item yang ditambahkan nanti
  daftar.addEventListener("click", (e) => {
    const tombol = e.target.closest("[data-aksi='hapus']");
    if (!tombol) return;
    const li = tombol.closest("li");
    console.log("hapus id", li.dataset.id);
    li.remove();
  });
  const baru = document.createElement("li");
  baru.dataset.id = "3";
  baru.textContent = "Susu ";                 // aman: teks, bukan HTML
  daftar.append(baru);
</script>''', lang='html'),
     J('Kenapa innerHTML berbahaya untuk data pengguna', '''
const komentar = '<img src=x onerror="alert(document.cookie)">';
const viaInnerHTML = `<p>${komentar}</p>`;                       // browser akan menjalankan onerror
const escape = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
console.log("berbahaya:", viaInnerHTML);
console.log("aman     :", `<p>${escape(komentar)}</p>`);
''', 'Di browser, gunakan textContent untuk teks dari pengguna. Fungsi escape di sini hanya untuk menunjukkan apa yang dilakukan browser.')]),

'Mengambil data: fetch, JSON & async': dict(
  ist=[('Promise', 'Objek yang mewakili hasil operasi asinkron: pending, fulfilled, atau rejected.'),
       ('async / await', 'Sintaks untuk menulis kode asinkron seperti kode berurutan.'),
       ('response.ok', 'fetch tidak melempar error untuk 404/500; periksa response.ok atau status.'),
       ('AbortController', 'Membatalkan request, misalnya saat pengguna pindah halaman atau timeout.')],
  cx=[J('fetch dengan timeout, cek status, dan Promise.all', '''
import http from "node:http";
const server = http.createServer((req, res) => {
  const data = { "/produk": [{ id: 1, nama: "Kopi" }], "/stok": { 1: 12 } }[req.url];
  if (req.url === "/lambat") return setTimeout(() => res.end("{}"), 2000);
  res.writeHead(data ? 200 : 404, { "Content-Type": "application/json" });
  res.end(JSON.stringify(data ?? { error: "tidak ada" }));
}).listen(0);
const base = `http://localhost:${server.address().port}`;

async function ambil(path, ms = 500) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), ms);
  try {
    const res = await fetch(base + path, { signal: ctrl.signal });
    if (!res.ok) throw new Error(`HTTP ${res.status} untuk ${path}`);
    return await res.json();
  } finally { clearTimeout(t); }
}
const [produk, stok] = await Promise.all([ambil("/produk"), ambil("/stok")]);
console.log(produk[0].nama, "stok", stok[produk[0].id]);
for (const p of ["/tidak-ada", "/lambat"]) {
  try { await ambil(p); } catch (e) { console.log("gagal:", e.name === "AbortError" ? `timeout ${p}` : e.message); }
}
server.close(); server.closeAllConnections();
''', 'Contoh ini membuat server kecil di Node agar fetch benar-benar berjalan. Di browser kodenya sama persis.')]),

'Perulangan: for, for...of & while': dict(
  ist=[('for...of', 'Mengulang nilai dari iterable (array, string, Map); pilihan utama untuk array.'),
       ('for...in', 'Mengulang kunci objek; jangan dipakai untuk array.'),
       ('entries()', 'Mendapat indeks dan nilai sekaligus: for (const [i, x] of arr.entries()).'),
       ('Infinite loop', 'Loop yang tidak berhenti dan membekukan tab browser; pastikan kondisi berubah.')],
  cx=[J('for...of, for...in, dan entries', '''
const nilai = [88, 72, 95];
for (const [i, n] of nilai.entries()) console.log(`siswa ${i + 1}: ${n}`);
const stok = { kopi: 12, teh: 0, gula: 5 };
for (const nama in stok) if (stok[nama] === 0) console.log("habis:", nama);
for (const [nama, n] of Object.entries(stok)) if (n > 0 && n < 10) console.log("menipis:", nama, n);
let tabungan = 0, bulan = 0;
while (tabungan < 1_000_000) { tabungan += 150_000; bulan++; }
console.log(`target tercapai dalam ${bulan} bulan`);
''')]),

'Menangani error dengan try...catch': dict(
  ist=[('Error object', 'Objek berisi name, message, dan stack; bisa dibuat dengan new Error("pesan").'),
       ('Custom error', 'class ValidasiError extends Error untuk membedakan jenis error.'),
       ('finally', 'Blok yang selalu jalan, misalnya mematikan indikator loading.'),
       ('Error boundary / global handler', 'Penangkap error tingkat aplikasi (window.onerror, React error boundary) untuk dilaporkan ke Sentry.')],
  cx=[J('Error kustom dan pesan yang ramah pengguna', '''
class ValidasiError extends Error {
  constructor(field, pesan) { super(pesan); this.name = "ValidasiError"; this.field = field; }
}
function validasi(form) {
  if (!form.email.includes("@")) throw new ValidasiError("email", "Format email belum benar");
  if (form.sandi.length < 8) throw new ValidasiError("sandi", "Kata sandi minimal 8 karakter");
  return true;
}
for (const form of [{ email: "sari@x.id", sandi: "rahasia123" }, { email: "sari", sandi: "x" }, null]) {
  let loading = true;
  try { validasi(form); console.log("terkirim"); }
  catch (e) {
    if (e instanceof ValidasiError) console.log(`tampilkan di field ${e.field}: ${e.message}`);
    else console.log("error tak terduga, laporkan ke monitoring:", e.name);
  } finally { loading = false; }
}
''')]),

'Modul: import & export': dict(
  ist=[('ES Modules', 'Sistem modul standar JavaScript: import dan export, didukung browser dan Node.'),
       ('Named vs default export', 'export const a (bisa banyak) vs export default (satu per berkas).'),
       ('Tree shaking', 'Bundler membuang kode yang tidak diimpor sehingga berkas akhir lebih kecil.'),
       ('Dynamic import()', 'Memuat modul saat dibutuhkan (code splitting), misalnya halaman admin.')],
  cx=[J('Modul nyata: menulis berkas, lalu import statis dan dinamis', '''
import { writeFile, mkdtemp } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
const dir = await mkdtemp(join(tmpdir(), "modul-"));
await writeFile(join(dir, "format.mjs"), `
export const rupiah = (n) => "Rp" + n.toLocaleString("id-ID");
export const tanggal = (d) => d.toISOString().slice(0, 10);
export default function ringkas(teks, n = 20) { return teks.length > n ? teks.slice(0, n - 1) + "…" : teks; }
`);
const { rupiah, default: ringkas } = await import(join(dir, "format.mjs"));   // dynamic import
console.log(rupiah(1250000), "|", ringkas("Kopi Gayo Arabika Premium 250 gram"));
''', 'Di proyek nyata cukup tulis import ringkas, { rupiah } from "./format.js" di bagian atas berkas.')]),

'Semua jenis perulangan: for, while, do-while, for-each, break, continue': dict(
  ist=[('do...while', 'Badan loop jalan minimal sekali sebelum kondisi diperiksa.'),
       ('forEach', 'Method array yang tidak bisa dihentikan dengan break; gunakan for...of jika perlu berhenti.'),
       ('Labeled break', 'break luar untuk keluar dari loop bersarang sekaligus.'),
       ('Array.from / some / find', 'Alternatif deklaratif yang sering menggantikan loop manual.')],
  cx=[J('Lima gaya perulangan dan kapan berhenti', '''
const data = [12, 7, 0, 25, 3];
let total = 0;
for (let i = 0; i < data.length; i++) total += data[i];
console.log("for klasik:", total);
total = 0; data.forEach((x) => (total += x)); console.log("forEach   :", total);
let i = 0; do { i++; } while (i < 0); console.log("do-while jalan", i, "kali walau kondisi salah");
for (const x of data) { if (x === 0) continue; if (x > 20) { console.log("berhenti di", x); break; } }
cari: for (const a of [1, 2, 3]) for (const b of [4, 5, 6]) if (a * b === 10) { console.log("ketemu", a, b); break cari; }
console.log("find:", data.find((x) => x > 10), "| some negatif:", data.some((x) => x < 0));
''')]),

'Boolean logic: AND, OR, NOT, tabel kebenaran, dan De Morgan': dict(
  ist=[('Logical operators', '&&, ||, ! mengembalikan salah satu operand, bukan selalu true/false.'),
       ('De Morgan', '!(a && b) === (!a || !b) dan !(a || b) === (!a && !b).'),
       ('Short-circuit', 'user && user.nama tidak mengevaluasi kanan jika user falsy.'),
       ('Feature flag', 'Kondisi boolean yang menyalakan fitur untuk sebagian pengguna.')],
  cx=[J('Tabel kebenaran dan aturan tombol checkout', '''
console.log("a     b     !(a&&b) !a||!b");
for (const a of [false, true]) for (const b of [false, true])
  console.log(String(a).padEnd(5), String(b).padEnd(5), String(!(a && b)).padEnd(7), !a || !b);
const bisaCheckout = ({ login, keranjang, alamat }) => login && keranjang > 0 && Boolean(alamat);
const nonaktif = ({ login, keranjang, alamat }) => !login || keranjang === 0 || !alamat;   // De Morgan
const kasus = [{ login: true, keranjang: 2, alamat: "Bandung" }, { login: true, keranjang: 0, alamat: "Medan" }, { login: false, keranjang: 1, alamat: "" }];
console.log(kasus.map((k) => [bisaCheckout(k), nonaktif(k)]));
''')]),

'Random number: bilangan acak, rentang, seed, dan mengocok': dict(
  ist=[('Math.random', 'Angka acak 0 sampai <1; tidak aman untuk keamanan.'),
       ('crypto.getRandomValues / randomUUID', 'Keacakan kriptografis untuk token, ID, dan OTP.'),
       ('Fisher-Yates shuffle', 'Algoritma mengocok yang adil; sort(() => Math.random() - 0.5) bias.'),
       ('Seeded PRNG', 'Generator dengan seed (misalnya mulberry32) agar hasil bisa diulang dalam test.')],
  cx=[J('Acak yang bisa diulang, mengocok adil, dan ID aman', '''
function mulberry32(seed) {
  return () => { seed |= 0; seed = (seed + 0x6d2b79f5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}
const rnd = mulberry32(2026);
const antara = (a, b) => a + Math.floor(rnd() * (b - a + 1));
console.log("dadu:", Array.from({ length: 6 }, () => antara(1, 6)));
function kocok(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
console.log("urutan presentasi:", kocok(["Ani", "Budi", "Citra", "Dedi"]));
console.log("UUID v4 valid:", /^[0-9a-f-]{36}$/.test(crypto.randomUUID()));
''')]),

'npm & package.json': dict(
  ist=[('npm', 'Node Package Manager: memasang pustaka dari registry npmjs.com.'),
       ('dependencies vs devDependencies', 'Pustaka yang ikut ke produksi vs alat pengembangan (Vite, Vitest, ESLint).'),
       ('Semantic versioning', 'MAJOR.MINOR.PATCH; ^1.4.2 menerima 1.x terbaru, ~1.4.2 hanya patch.'),
       ('Lockfile', 'package-lock.json mengunci versi persis; selalu di-commit dan pakai npm ci di CI.')],
  cx=[J('Membaca package.json dan memahami rentang versi', '''
const pkg = {
  name: "toko-kopi", version: "1.2.0", type: "module",
  scripts: { dev: "vite", build: "vite build", test: "vitest run", lint: "eslint ." },
  dependencies: { react: "^19.0.0", "react-dom": "^19.0.0" },
  devDependencies: { vite: "^6.0.0", vitest: "^3.0.0", eslint: "~9.17.0" },
};
const cocok = (rentang, versi) => {
  const [maj, min, pat] = versi.split(".").map(Number);
  const [, op, r] = rentang.match(/^([\\^~]?)(.*)$/); const [M, m, p] = r.split(".").map(Number);
  if (op === "^") return maj === M && (min > m || (min === m && pat >= p));
  if (op === "~") return maj === M && min === m && pat >= p;
  return versi === r;
};
for (const [rentang, v] of [["^19.0.0", "19.2.1"], ["^19.0.0", "20.0.0"], ["~9.17.0", "9.17.3"], ["~9.17.0", "9.18.0"]])
  console.log(`${rentang} menerima ${v}?`, cocok(rentang, v));
console.log("skrip:", Object.keys(pkg.scripts).map((s) => `npm run ${s}`).join(", "));
''', 'Versi MAJOR baru boleh merusak API lama. Karena itu ^ tidak pernah menaikkan MAJOR secara otomatis.')]),

'Tailwind CSS': dict(
  ist=[('Utility-first', 'Gaya dibangun dari kelas kecil satu tujuan (p-4, text-lg, flex) langsung di HTML.'),
       ('Design token', 'Skala spasi, warna, dan ukuran font yang konsisten; dikonfigurasi di tema Tailwind.'),
       ('Responsive prefix', 'sm:, md:, lg: menerapkan kelas mulai lebar layar tertentu (mobile-first).'),
       ('State variant', 'hover:, focus-visible:, disabled:, dark: untuk gaya per state.')],
  cx=[T('Kartu produk dengan Tailwind v4: responsif, state, dan dark mode', '''
<article class="rounded-2xl border border-zinc-200 bg-white p-4 shadow-sm transition
                hover:shadow-md dark:border-zinc-700 dark:bg-zinc-900 sm:p-6">
  <img src="kopi.webp" alt="Kopi Gayo 250 gram" class="aspect-square w-full rounded-xl object-cover" loading="lazy">
  <h3 class="mt-3 text-base font-semibold text-zinc-900 dark:text-zinc-50 sm:text-lg">Kopi Gayo</h3>
  <p class="text-sm text-zinc-500">Arabika, 250 g</p>
  <div class="mt-4 flex items-center justify-between gap-3">
    <span class="text-lg font-bold text-emerald-700 dark:text-emerald-400">Rp85.000</span>
    <button class="rounded-lg bg-emerald-600 px-4 py-2 text-sm font-medium text-white
                   hover:bg-emerald-700 focus-visible:outline focus-visible:outline-2
                   focus-visible:outline-offset-2 disabled:cursor-not-allowed disabled:opacity-50">
      Tambah
    </button>
  </div>
</article>
<!-- Tailwind v4: cukup @import "tailwindcss"; di CSS, kelas yang dipakai dipindai otomatis -->''', lang='html')]),

'Menguji kode dengan Vitest': dict(
  ist=[('Unit test', 'Menguji satu fungsi atau komponen secara terisolasi.'),
       ('Arrange-Act-Assert', 'Pola menulis test: siapkan data, jalankan, periksa hasil.'),
       ('Mock', 'Mengganti dependensi (fetch, waktu) dengan tiruan agar test cepat dan stabil.'),
       ('Watch mode', 'Vitest menjalankan ulang test terkait setiap kali berkas disimpan.')],
  cx=[T('Berkas test Vitest', '''
// src/keranjang.test.js
import { describe, it, expect, vi } from "vitest";
import { hitungTotal, ambilProduk } from "./keranjang.js";

describe("hitungTotal", () => {
  it("menjumlah harga x qty", () => {
    expect(hitungTotal([{ harga: 10000, qty: 2 }, { harga: 5000, qty: 1 }])).toBe(25000);
  });
  it("keranjang kosong bernilai 0", () => expect(hitungTotal([])).toBe(0));
  it("menolak qty negatif", () => expect(() => hitungTotal([{ harga: 1, qty: -1 }])).toThrow("qty"));
});

it("ambilProduk memanggil API yang benar", async () => {
  globalThis.fetch = vi.fn().mockResolvedValue({ ok: true, json: async () => [{ id: 1 }] });
  await ambilProduk();
  expect(fetch).toHaveBeenCalledWith("/api/produk");
});

$ npx vitest run
 ✓ src/keranjang.test.js (4 tests) 6ms
 Test Files  1 passed (1)
      Tests  4 passed (4)''', lang='js'),
     J('Inti test runner: describe, it, expect (dijalankan dengan node:test)', '''
import { test } from "node:test";
import assert from "node:assert/strict";
const hitungTotal = (items) => items.reduce((t, { harga, qty }) => {
  if (qty < 0) throw new Error("qty tidak boleh negatif");
  return t + harga * qty;
}, 0);
const hasil = [];
const uji = (nama, fn) => { try { fn(); hasil.push(`✓ ${nama}`); } catch (e) { hasil.push(`✗ ${nama}: ${e.message}`); } };
uji("menjumlah harga x qty", () => assert.equal(hitungTotal([{ harga: 10000, qty: 2 }, { harga: 5000, qty: 1 }]), 25000));
uji("keranjang kosong bernilai 0", () => assert.equal(hitungTotal([]), 0));
uji("menolak qty negatif", () => assert.throws(() => hitungTotal([{ harga: 1, qty: -1 }]), /qty/));
console.log(hasil.join("\\n"));
console.log(`${hasil.filter((h) => h.startsWith("✓")).length} lulus`);
''')]),

'Menerbitkan situs': dict(
  ist=[('Static hosting', 'Layanan yang menyajikan berkas HTML/CSS/JS hasil build: Vercel, Netlify, Cloudflare Pages, GitHub Pages.'),
       ('Build artifact', 'Folder hasil npm run build (dist/) yang diunggah ke hosting.'),
       ('Preview deployment', 'URL sementara untuk setiap pull request agar bisa dicek sebelum merge.'),
       ('Custom domain & HTTPS', 'Menghubungkan domain sendiri lewat DNS (CNAME/A) dan sertifikat TLS otomatis.')],
  cx=[T('Alur terbit dari laptop ke internet', '''
$ npm run build                    # vite build -> dist/index.html, dist/assets/*.js (nama ber-hash)
$ npx serve dist                   # cek hasil build secara lokal

# GitHub + Vercel/Netlify/Cloudflare Pages
git push origin main  ──>  hosting menjalankan build  ──>  https://toko-kopi.vercel.app
pull request #12      ──>  preview: https://toko-kopi-git-fitur-promo.vercel.app

# Domain sendiri
DNS  www.tokokopi.id  CNAME  cname.vercel-dns.com
Sertifikat HTTPS dibuat otomatis (Let's Encrypt)

# Cek setelah terbit
- Lighthouse: Performance, Accessibility, Best Practices, SEO
- Halaman 404 kustom, favicon, meta description, Open Graph untuk dibagikan di WhatsApp''')]),

'Aplikasi daftar belanja': dict(
  ist=[('State', 'Data yang menentukan tampilan (daftar item, filter); tampilan dirender ulang dari state.'),
       ('Single source of truth', 'Satu tempat menyimpan state; DOM hanya cerminannya.'),
       ('localStorage', 'Penyimpanan kunci-nilai di browser agar data tetap ada setelah halaman ditutup.'),
       ('CRUD', 'Create, Read, Update, Delete: empat operasi dasar aplikasi data.')],
  cx=[J('Logika daftar belanja dipisah dari DOM (bisa diuji)', '''
function buatToko(awal = []) {
  let state = { item: awal, filter: "semua" };
  const dengar = new Set();
  const ubah = (fn) => { state = fn(state); dengar.forEach((f) => f(state)); };
  return {
    tambah: (nama, qty = 1) => ubah((s) => ({ ...s, item: [...s.item, { id: s.item.length + 1, nama: nama.trim(), qty, beli: false }] })),
    centang: (id) => ubah((s) => ({ ...s, item: s.item.map((i) => (i.id === id ? { ...i, beli: !i.beli } : i)) })),
    hapus: (id) => ubah((s) => ({ ...s, item: s.item.filter((i) => i.id !== id) })),
    saring: (filter) => ubah((s) => ({ ...s, filter })),
    terlihat: () => state.item.filter((i) => state.filter === "semua" || (state.filter === "belum" ? !i.beli : i.beli)),
    pantau: (f) => dengar.add(f),
  };
}
const toko = buatToko();
toko.pantau((s) => console.log(`render: ${s.item.length} item, ${s.item.filter((i) => i.beli).length} dibeli`)); // di browser: render DOM + localStorage
toko.tambah("Beras 5 kg"); toko.tambah("Telur", 2); toko.tambah("  Minyak goreng ");
toko.centang(2); toko.saring("belum");
console.log("belum dibeli:", toko.terlihat().map((i) => i.nama));
''')]),

'Format specifier: merapikan keluaran': dict(
  ist=[('Intl.NumberFormat', 'API format angka sesuai lokal: mata uang, persen, ribuan.'),
       ('Intl.DateTimeFormat', 'Format tanggal sesuai lokal dan zona waktu.'),
       ('padStart / padEnd', 'Menambah karakter di kiri/kanan agar kolom rata.'),
       ('toFixed', 'Membulatkan ke n digit desimal dan mengembalikan string.')],
  cx=[J('Struk dan laporan dengan Intl', '''
const rp = new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 });
const pct = new Intl.NumberFormat("id-ID", { style: "percent", maximumFractionDigits: 1 });
const tgl = new Intl.DateTimeFormat("id-ID", { dateStyle: "full", timeStyle: "short", timeZone: "Asia/Jakarta" });
const item = [["Kopi Gayo", 2, 85000], ["Gula aren", 1, 32500], ["Susu oat", 3, 29900]];
for (const [n, q, h] of item) console.log(n.padEnd(12), String(q).padStart(2), "x", rp.format(h).padStart(10), rp.format(q * h).padStart(12));
console.log("diskon member", pct.format(0.075), "| rata-rata", (247.3456).toFixed(2));
console.log(tgl.format(new Date("2026-11-19T02:30:00Z")).replace(/\\u202f/g, " "));
''')]),

'Kapan for, kapan while, kapan do-while': dict(
  ist=[('Known iterations', 'for/for...of jika jumlah elemen atau putaran diketahui.'),
       ('Unknown iterations', 'while jika berhenti bergantung kondisi (polling, retry).'),
       ('Run at least once', 'do...while untuk menu atau validasi yang harus tampil minimal sekali.'),
       ('Polling with backoff', 'Mengecek status berkala dengan jeda yang makin panjang dan batas maksimum.')],
  cx=[J('Polling status pembayaran dengan backoff', '''
const statusDariServer = ["PENDING", "PENDING", "PENDING", "PAID"];
let cek = 0, jeda = 500, status;
const sleep = (ms) => new Promise((r) => setTimeout(r, Math.min(ms, 5) /* dipercepat untuk contoh */));
while (cek < 8) {
  status = statusDariServer[Math.min(cek, statusDariServer.length - 1)];
  cek++;
  console.log(`cek ke-${cek}: ${status}${status === "PENDING" ? `, tunggu ${jeda} ms` : ""}`);
  if (status !== "PENDING") break;
  await sleep(jeda); jeda = Math.min(jeda * 2, 8000);
}
console.log(status === "PAID" ? "tampilkan halaman sukses" : "tampilkan 'cek lagi nanti'");
''')]),

'Bilangan Fibonacci: for dan while': dict(
  ist=[('Iterative solution', 'Menyimpan dua nilai terakhir; O(n) waktu dan O(1) memori.'),
       ('BigInt', 'Tipe bilangan bulat tak terbatas di JavaScript (akhiran n); number kehilangan presisi setelah F(78).'),
       ('Generator function', 'function* menghasilkan deret tanpa batas secara lazy.'),
       ('Memoization', 'Menyimpan hasil agar tidak dihitung ulang.')],
  cx=[J('Fibonacci dengan for, while, generator, dan BigInt', '''
function fib(n) { let a = 0, b = 1; for (let i = 0; i < n; i++) [a, b] = [b, a + b]; return a; }
function fibBig(n) { let a = 0n, b = 1n; for (let i = 0; i < n; i++) [a, b] = [b, a + b]; return a; }
function* deret() { let [a, b] = [0, 1]; while (true) { yield a; [a, b] = [b, a + b]; } }
const sepuluh = []; for (const x of deret()) { if (sepuluh.length === 10) break; sepuluh.push(x); }
console.log(sepuluh.join(" "));
console.log("F(80) number:", fib(80), "| BigInt:", fibBig(80).toString(), "| sama?", BigInt(fib(80)) === fibBig(80));
''')]),

'Bubble sort: loop di dalam loop': dict(
  ist=[('Bubble sort', 'Menukar pasangan bersebelahan yang salah urut; O(n²).'),
       ('Comparator', 'Fungsi (a, b) => a - b yang menentukan urutan di Array.prototype.sort.'),
       ('Default sort pitfall', '[10, 9, 1].sort() mengurutkan sebagai string: [1, 10, 9].'),
       ('localeCompare', 'Membandingkan string sesuai aturan bahasa, termasuk huruf beraksen.')],
  cx=[J('Bubble sort manual vs sort bawaan dan jebakannya', '''
function bubble(a) {
  a = [...a]; let tukar = true, putaran = 0;
  while (tukar) { tukar = false; putaran++;
    for (let i = 0; i < a.length - putaran; i++) if (a[i] > a[i + 1]) { [a[i], a[i + 1]] = [a[i + 1], a[i]]; tukar = true; } }
  return [a, putaran];
}
console.log(bubble([5, 1, 4, 2, 8]));
console.log("sort() tanpa comparator:", [10, 9, 1, 100].sort());
console.log("sort((a,b)=>a-b)       :", [10, 9, 1, 100].sort((a, b) => a - b));
console.log("nama:", ["Zaki", "ani", "Émil", "Budi"].sort((a, b) => a.localeCompare(b, "id", { sensitivity: "base" })));
''')]),

'FizzBuzz dan bilangan prima: break dan loop bersarang': dict(
  ist=[('Modulo %', 'Sisa bagi; inti FizzBuzz dan cek kelipatan.'),
       ('Early exit', 'break/return begitu jawaban diketahui.'),
       ('Sieve of Eratosthenes', 'Mencari semua prima sampai n dengan mencoret kelipatan.'),
       ('Typed array', 'Uint8Array hemat memori untuk tanda boolean dalam jumlah besar.')],
  cx=[J('FizzBuzz berbasis aturan dan saringan prima dengan Uint8Array', '''
const aturan = [[3, "Fizz"], [5, "Buzz"]];
console.log(Array.from({ length: 15 }, (_, i) => aturan.map(([d, k]) => ((i + 1) % d ? "" : k)).join("") || i + 1).join(" "));
function prima(n) {
  const coret = new Uint8Array(n + 1);
  for (let i = 2; i * i <= n; i++) if (!coret[i]) for (let j = i * i; j <= n; j += i) coret[j] = 1;
  const hasil = []; for (let i = 2; i <= n; i++) if (!coret[i]) hasil.push(i);
  return hasil;
}
console.log("prima < 40:", prima(40).join(", "));
console.log("jumlah prima < 1 juta:", prima(1_000_000).length);
''')]),

'Faktorial, jumlah digit, dan palindrom': dict(
  ist=[('Factorial', 'n! = 1 x 2 x ... x n; gunakan BigInt di atas 18!.'),
       ('String reversal', '[...s].reverse().join("") aman untuk emoji dan aksen.'),
       ('Normalization', 'Menghapus spasi, tanda baca, dan huruf besar sebelum membandingkan.'),
       ('Luhn checksum', 'Validasi nomor kartu dengan menjumlah digit berbobot.')],
  cx=[J('Palindrom, jumlah digit faktorial, dan Luhn', '''
const palindrom = (s) => { const t = s.toLowerCase().replace(/[^a-z0-9]/g, ""); return t === [...t].reverse().join(""); };
console.log(["Kasur ini rusak", "Malam", "Ada apa"].map(palindrom));
let f = 1n; for (let i = 1n; i <= 50n; i++) f *= i;
console.log("50! punya", f.toString().length, "digit, jumlah digit", [...f.toString()].reduce((t, d) => t + Number(d), 0));
const luhn = (no) => [...no.replace(/\\D/g, "")].reverse().reduce((t, d, i) => { let x = +d; if (i % 2) { x *= 2; if (x > 9) x -= 9; } return t + x; }, 0) % 10 === 0;
console.log("4111 1111 1111 1111:", luhn("4111 1111 1111 1111"), "| ...1112:", luhn("4111 1111 1111 1112"));
''')]),

'Binary search: membagi dua sampai ketemu': dict(
  ist=[('Binary search', 'Mencari di array terurut dengan membagi dua ruang pencarian: O(log n).'),
       ('Sorted precondition', 'Data harus terurut; jika tidak, hasil salah tanpa error.'),
       ('Lower bound', 'Indeks pertama dengan nilai >= target; berguna untuk rentang harga.'),
       ('Math.floor((lo + hi) / 2)', 'Titik tengah; pakai >>> 1 atau lo + ((hi - lo) >> 1) untuk menghindari overflow di bahasa lain.')],
  cx=[J('Binary search dan lower bound untuk filter harga', '''
const harga = [5000, 12000, 18000, 25000, 40000, 55000, 90000];
function cari(a, x) {
  let lo = 0, hi = a.length - 1, langkah = 0;
  while (lo <= hi) { const mid = (lo + hi) >>> 1; langkah++;
    if (a[mid] === x) return [mid, langkah]; if (a[mid] < x) lo = mid + 1; else hi = mid - 1; }
  return [-1, langkah];
}
function lowerBound(a, x) { let lo = 0, hi = a.length; while (lo < hi) { const m = (lo + hi) >>> 1; if (a[m] < x) lo = m + 1; else hi = m; } return lo; }
console.log("cari 40000:", cari(harga, 40000), "| cari 41000:", cari(harga, 41000));
const [min, max] = [15000, 50000];
console.log("produk Rp15rb-50rb:", harga.slice(lowerBound(harga, min), lowerBound(harga, max + 1)));
console.log("1 juta data butuh paling banyak", Math.ceil(Math.log2(1_000_001)), "langkah");
''')]),
}
