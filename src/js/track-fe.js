/* ===================== JALUR FRONTEND =====================
   Mengikuti roadmap.sh/frontend (versi lengkap). Dasar dipinjam dari jalur HTML, CSS,
   Frontend Pemula, Git, dan React; materi lanjutan ditulis di sini. */
const FE_MODULES=[
{t:'Internet & browser',lvl:'Pemula',d:'Cara internet bekerja, HTTP, cache, dan apa yang dilakukan browser sampai halaman tampil.',
 nodes:['Internet','How Does The Internet Work','What is HTTP?','Domain Name','Hosting','DNS','Browsers','HTTPS','Cache-Control'],
 lessons:[
  {k:'see',ref:'html:Cara web bekerja'},
  {k:'c',t:'HTTP, HTTPS & cache',nodes:['What is HTTP?','HTTPS','Cache-Control'],lang:'text',run:false,
   b:['Setiap permintaan HTTP punya <b>metode</b> (GET untuk membaca, POST untuk mengirim, PUT/PATCH untuk mengubah, DELETE untuk menghapus), <b>header</b> (informasi tambahan), dan kadang <b>body</b>. Respons membawa kode status: 2xx berhasil, 3xx pengalihan, 4xx kesalahan dari sisi klien, 5xx kesalahan server.',
      '<b>HTTPS</b> mengenkripsi lalu lintas dengan TLS, sehingga kata sandi dan data pembayaran tidak bisa dibaca di jaringan Wi-Fi publik. Browser modern menandai situs non-HTTPS sebagai tidak aman.',
      'Header <code>Cache-Control</code> memberi tahu browser berapa lama file boleh disimpan. File dengan nama ber-hash (<code>app.3f9a1c.js</code>) aman di-cache setahun karena namanya berubah setiap isinya berubah; dokumen HTML biasanya <code>no-cache</code> agar selalu diperiksa ulang.'],
   code:`GET /assets/app.3f9a1c.js HTTP/2
Host: tokonusantara.id

HTTP/2 200
content-type: text/javascript
cache-control: public, max-age=31536000, immutable

GET / HTTP/2
HTTP/2 200
content-type: text/html
cache-control: no-cache`,
   pts:['Metode: GET, POST, PUT/PATCH, DELETE.','Status: 2xx sukses, 3xx pengalihan, 4xx salah klien, 5xx salah server.','HTTPS = HTTP + enkripsi TLS.','Aset ber-hash di-cache lama; HTML diperiksa ulang.'],
   q:[['Kode 401 masuk kelompok?',['Kesalahan klien (belum login)','Sukses','Kesalahan server'],0,'4xx adalah kesalahan di sisi permintaan.'],
      ['Kenapa file app.3f9a1c.js boleh di-cache setahun?',['Namanya berubah setiap isinya berubah','Karena JS tidak pernah berubah','Karena HTTPS'],0,'Ini disebut cache busting.']]},
  {k:'c',t:'Cara browser menggambar halaman',nodes:['Browsers'],viz:'render',
   b:['Setelah HTML diterima, browser membangun <b>DOM</b> dari HTML dan <b>CSSOM</b> dari CSS, menggabungkannya menjadi <b>render tree</b>, menghitung ukuran dan posisi setiap kotak (<b>layout</b>), mewarnainya (<b>paint</b>), lalu menyusun lapisan (<b>composite</b>).',
      'CSS menghambat tampilan dan script biasa menghambat pembacaan HTML. Karena itu CSS penting dimuat lebih awal dan script diberi defer.',
      'Saat JavaScript mengubah lebar atau posisi elemen, browser mengulang layout dan paint (mahal). Mengubah transform dan opacity cukup mengulang composite (murah), itulah alasan animasi sebaiknya memakai keduanya.'],
   pts:['HTML → DOM, CSS → CSSOM, lalu render tree.','Layout menghitung posisi, paint mewarnai, composite menyusun lapisan.','Ubah transform/opacity untuk animasi yang mulus.'],
   q:[['Mengubah width elemen memicu?',['Layout, paint, composite','Hanya composite','Tidak ada apa-apa'],0,'Ukuran berubah sehingga posisi harus dihitung ulang.']]}
 ]},
{t:'HTML & CSS',lvl:'Pemula',d:'Fondasi struktur dan tampilan, dipinjam dari jalur HTML dan CSS.',nodes:['HTML','CSS'],
 lessons:[
  {k:'see',ref:'html:Struktur dokumen HTML'},{k:'see',ref:'html:Elemen semantik'},{k:'see',ref:'html:Form, label & input'},{k:'see',ref:'html:Aksesibilitas dasar'},{k:'see',ref:'html:Meta tag & SEO dasar'},
  {k:'see',ref:'css:Box model'},{k:'see',ref:'css:Flexbox'},{k:'see',ref:'css:Grid'},{k:'see',ref:'css:Media query & mobile-first'},{k:'see',ref:'css:Variabel CSS & tema'}
 ]},
{t:'JavaScript',lvl:'Pemula',d:'Dasar bahasa ditambah modul, event loop, dan Web API.',nodes:['JavaScript','Web APIs'],
 lessons:[
  {k:'see',ref:'fe0:Variabel & tipe data'},{k:'see',ref:'fe0:Operator & percabangan'},{k:'see',ref:'fe0:Fungsi'},{k:'see',ref:'fe0:Array & objek'},{k:'see',ref:'fe0:DOM & event'},{k:'see',ref:'fe0:Mengambil data: fetch, JSON & async'},
  {k:'w',t:'Event loop JavaScript',nodes:['JavaScript'],console:true,viz:'jsloop',
   b:['JavaScript di browser berjalan di <b>satu thread</b>. Agar halaman tidak membeku saat menunggu jaringan atau timer, pekerjaan yang menunggu diserahkan ke browser, lalu callback-nya diantrekan.',
      'Ada dua antrean: <b>microtask</b> (Promise, await) dan <b>macrotask</b> (setTimeout, event klik). Setelah kode sinkron selesai, semua microtask dijalankan dulu, baru satu macrotask, dan seterusnya. Tebak urutan keluaran sebelum menjalankan.'],
   html:`<p>Lihat panel Konsol.</p>`,
   js:`console.log("1. mulai");
setTimeout(() => console.log("4. setTimeout (macrotask)"), 0);
Promise.resolve().then(() => console.log("3. promise (microtask)"));
console.log("2. selesai kode sinkron");`,
   pts:['Satu thread, tidak memblokir lewat antrean callback.','Urutan: sinkron, semua microtask, lalu macrotask.','setTimeout 0 tetap menunggu kode sinkron dan microtask.'],
   q:[['Mana yang jalan lebih dulu: Promise.then atau setTimeout 0?',['Promise.then','setTimeout 0','Acak'],0,'Microtask didahulukan.']]},
  {k:'c',t:'Modul ES',nodes:['JavaScript'],lang:'js',run:false,
   b:['Kode besar dipecah menjadi <b>modul</b>: satu file satu tanggung jawab. <code>export</code> membagikan fungsi atau nilai, <code>import</code> memakainya. Ada named export (bisa banyak) dan default export (satu per file).',
      'Di browser, pakai <code>&lt;script type="module"&gt;</code>. Modul otomatis memakai mode ketat dan bersifat defer. <code>import()</code> dinamis memuat modul hanya saat dibutuhkan, cara dasar code splitting.'],
   code:`// format.js
export const rupiah = n => "Rp" + n.toLocaleString("id-ID");
export default function judul(s) { return s[0].toUpperCase() + s.slice(1); }

// main.js
import judul, { rupiah } from "./format.js";
console.log(judul("kopi"), rupiah(85000));   // Kopi Rp85.000

// muat grafik hanya saat tombol diklik
document.querySelector("#lihat").onclick = async () => {
  const { gambarGrafik } = await import("./grafik.js");
  gambarGrafik();
};`,
   pts:['export/import untuk membagi kode.','Named export banyak, default export satu.','type="module" di browser.','import() dinamis untuk memuat saat perlu.'],
   q:[['Sintaks memakai named export rupiah?',['import { rupiah } from "./format.js"','import rupiah from "./format.js"','require rupiah'],0,'Named export memakai kurung kurawal.']]},
  {k:'w',t:'Web API: storage, observer & lainnya',nodes:['Web APIs'],
   b:['Browser menyediakan banyak <b>Web API</b>: <code>localStorage</code> menyimpan data kecil yang bertahan setelah browser ditutup, <code>IntersectionObserver</code> memberi tahu saat elemen masuk layar (untuk lazy load atau animasi muncul), <code>Clipboard</code>, <code>Geolocation</code>, <code>Notification</code>, dan lainnya.',
      'Selalu periksa ketersediaan API dan bungkus akses storage dengan try/catch, karena bisa ditolak di mode privat.'],
   html:`<p>Kunjungan ke pratinjau ini: <b id="n">?</b></p>
<div style="height:220px;overflow:auto;border:1px solid #ddd" id="area">
  <div style="height:300px"></div>
  <p id="target" class="kotak">Saya muncul saat terlihat</p>
  <div style="height:60px"></div>
</div>`,
   css:`body{font:14px system-ui,sans-serif}.kotak{opacity:0;transform:translateY(20px);transition:all .5s;background:#E9EFF5;padding:10px;border-radius:8px}.kotak.tampak{opacity:1;transform:none}`,
   js:`try {
  const n = Number(localStorage.getItem("kunjungan") || 0) + 1;
  localStorage.setItem("kunjungan", n);
  document.getElementById("n").textContent = n;
} catch (e) { document.getElementById("n").textContent = "storage tidak tersedia"; }

const io = new IntersectionObserver(es => es.forEach(en => {
  if (en.isIntersecting) en.target.classList.add("tampak");
}), { root: document.getElementById("area") });
io.observe(document.getElementById("target"));`,
   task:{q:'Gulir kotak di pratinjau sampai teks "Saya muncul saat terlihat" tampak.',test:`document.getElementById('target').classList.contains('tampak')`,hint:'Gulir di dalam kotak bergaris.'},
   pts:['localStorage untuk data kecil yang bertahan.','IntersectionObserver untuk mendeteksi elemen terlihat.','Bungkus akses storage dengan try/catch.'],
   q:[['API yang tepat untuk lazy load saat elemen terlihat?',['IntersectionObserver','setInterval yang memeriksa scroll','localStorage'],0,'Lebih hemat daripada memantau scroll terus-menerus.']]}
 ]},
{t:'Git & hosting repositori',lvl:'Pemula',d:'Version control dan kerja tim dengan GitHub atau GitLab.',nodes:['Version Control Systems','Git','Repo Hosting Services','GitHub','GitLab'],
 lessons:[{k:'see',ref:'git:Apa itu version control & Git?'},{k:'see',ref:'git:init, add, commit'},{k:'see',ref:'git:Branch & merge'},{k:'see',ref:'git:Remote, push & pull'},{k:'see',ref:'git:Fork & pull request'}]},
{t:'Package manager & build tools',lvl:'Menengah',d:'npm, pnpm, yarn, bun, bundler, linter, dan formatter.',
 nodes:['Package Managers','npm','pnpm','Yarn','Bun','Module Bundlers','Vite','esbuild','Rollup','Rolldown','Parcel','SWC (Speedy Web Compiler)','Linters formatters','ESLint','Prettier','Biome'],
 lessons:[
  {k:'see',ref:'fe0:npm & package.json'},
  {k:'c',t:'Bundler & Vite',nodes:['Module Bundlers','Vite','esbuild','Rollup','Rolldown','Parcel','SWC (Speedy Web Compiler)','pnpm','Yarn','Bun'],lang:'js',run:false,
   b:['Kode modern terdiri dari ratusan modul, JSX, dan TypeScript yang tidak bisa langsung dijalankan browser lama. <b>Bundler</b> menggabungkan dan mengoptimasi semuanya: menghapus kode yang tidak dipakai (tree shaking), memecah file (code splitting), dan mengecilkan ukuran (minify).',
      '<b>Vite</b> kini menjadi pilihan utama: saat pengembangan ia menyajikan modul ES langsung sehingga sangat cepat, dan saat build ia memakai Rollup (atau Rolldown). <b>esbuild</b> dan <b>SWC</b> adalah kompiler super cepat yang ditulis dengan Go dan Rust.',
      'Selain npm, ada <b>pnpm</b> (hemat ruang disk), <b>Yarn</b>, dan <b>Bun</b> (runtime sekaligus package manager yang sangat cepat).'],
   code:`// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    sourcemap: true,
    rollupOptions: { output: { manualChunks: { react: ["react", "react-dom"] } } },
  },
});
// $ npm run build
// dist/assets/react-8f2c.js   142 kB │ gzip: 45 kB
// dist/assets/index-1b7d.js    18 kB │ gzip:  6 kB`,
   pts:['Bundler: gabung, tree shaking, code splitting, minify.','Vite cepat saat dev, Rollup/Rolldown saat build.','esbuild dan SWC adalah kompiler cepat.','pnpm, Yarn, Bun alternatif npm.'],
   q:[['Tree shaking berarti?',['Membuang kode yang tidak dipakai','Mengurutkan file','Mengompres gambar'],0,'Hanya kode yang di-import yang ikut.']]},
  {k:'c',t:'Linter & formatter',nodes:['Linters formatters','ESLint','Prettier','Biome'],lang:'json',run:false,
   b:['<b>Formatter</b> seperti Prettier merapikan gaya penulisan otomatis (spasi, tanda kutip, panjang baris), sehingga tim tidak berdebat soal gaya. <b>Linter</b> seperti ESLint mencari pola kode yang berpotensi bug, misalnya variabel tidak dipakai atau dependensi useEffect yang terlewat.',
      '<b>Biome</b> menggabungkan keduanya dalam satu alat yang sangat cepat. Jalankan otomatis saat menyimpan file dan sebelum commit.'],
   code:`// package.json
{
  "scripts": {
    "lint": "eslint .",
    "format": "prettier --write ."
  }
}
// $ npm run lint
// src/App.jsx
//   12:9  warning  'total' is assigned a value but never used   no-unused-vars
//   20:6  warning  React Hook useEffect has a missing dependency: 'id'   react-hooks/exhaustive-deps`,
   pts:['Formatter: gaya seragam otomatis.','Linter: deteksi pola rawan bug.','Biome menggabungkan keduanya.'],
   q:[['Alat yang mendeteksi variabel tidak terpakai?',['Linter (ESLint)','Formatter (Prettier)','Bundler'],0,'Linter menganalisis makna kode.']]}
 ]},
{t:'CSS modern & framework',lvl:'Menengah',d:'Tailwind, CSS modern, dan memilih framework JavaScript.',nodes:['Modern CSS','Tailwind CSS','Pick a Framework','React','Vue.js','Angular','Svelte','SolidJS'],
 lessons:[
  {k:'see',ref:'fe0:Tailwind CSS'},{k:'see',ref:'css:Container query'},
  {k:'c',t:'Memilih framework',nodes:['Pick a Framework','React','Vue.js','Angular','Svelte','SolidJS'],
   b:['Framework membantu membangun antarmuka yang rumit dengan komponen dan state. <b>React</b> paling banyak dipakai dan ekosistemnya paling besar. <b>Vue</b> ramah pemula dengan template mirip HTML. <b>Angular</b> lengkap dan kaku, populer di perusahaan besar. <b>Svelte</b> dan <b>SolidJS</b> mengompilasi komponen menjadi kode yang sangat ringan.',
      'Untuk karier di Indonesia, React dan Vue paling banyak diminta lowongan. Konsep intinya sama: komponen, props, state, dan reaktivitas. Kuasai satu dengan baik, framework lain jadi mudah dipelajari.'],
   code:`// React
function Sapa({ nama }) { return <p>Halo, {nama}</p>; }

<!-- Vue -->
<template><p>Halo, {{ nama }}</p></template>
<script setup>defineProps(["nama"])</script>

<!-- Svelte -->
<script>export let nama;</script>
<p>Halo, {nama}</p>`,lang:'jsx',run:false,
   pts:['React: ekosistem terbesar.','Vue: ramah pemula.','Angular: lengkap, populer di enterprise.','Svelte/Solid: hasil kompilasi ringan.'],
   q:[['Konsep yang sama di semua framework modern?',['Komponen dan state','Kelas Java','SQL'],0,'Karena itu pindah framework relatif mudah.']]},
  {k:'see',ref:'react:Komponen & JSX'},{k:'see',ref:'react:State dengan useState'},{k:'see',ref:'react:useEffect & siklus hidup'}
 ]},
{t:'Pengujian',lvl:'Menengah',d:'Unit test, tes komponen, dan tes end-to-end.',nodes:['Testing your apps','Vitest','Jest','Playwright','Cypress'],
 lessons:[
  {k:'see',ref:'fe0:Menguji kode dengan Vitest'},{k:'see',ref:'react:Menguji komponen'},
  {k:'c',t:'Tes end-to-end dengan Playwright',nodes:['Playwright','Cypress'],lang:'ts',run:false,
   b:['Tes end-to-end (E2E) menjalankan browser sungguhan dan meniru pengguna: membuka halaman, mengetik, mengklik, lalu memeriksa hasil. Tes ini paling lambat tapi paling meyakinkan, jadi tulis untuk alur terpenting saja, seperti login dan checkout.',
      '<b>Playwright</b> mendukung Chromium, Firefox, dan WebKit sekaligus, serta menunggu elemen siap secara otomatis. <b>Cypress</b> adalah alternatif populer dengan antarmuka interaktif.'],
   code:`import { test, expect } from "@playwright/test";

test("pembeli bisa menambah produk ke keranjang", async ({ page }) => {
  await page.goto("https://tokonusantara.id");
  await page.getByRole("searchbox", { name: "Cari produk" }).fill("kopi");
  await page.getByRole("button", { name: "Tambah Kopi Gayo" }).click();
  await expect(page.getByText("1 barang di keranjang")).toBeVisible();
});
// $ npx playwright test
//   ✓ pembeli bisa menambah produk ke keranjang (1.2s)`,
   pts:['Piramida tes: banyak unit, sedikit E2E.','Playwright: lintas browser, auto-wait.','Tulis E2E untuk alur paling penting.'],
   q:[['Tes paling lambat tapi paling mirip pengguna asli?',['End-to-end','Unit','Lint'],0,'E2E menjalankan aplikasi utuh di browser.']]}
 ]},
{t:'Keamanan web',lvl:'Lanjutan',d:'HTTPS, CORS, CSP, risiko OWASP, dan strategi autentikasi.',nodes:['Web Security Knowledge','HTTPS','CORS','Content Security Policy','OWASP Security Risks','Authentication Strategies'],
 lessons:[
  {k:'c',t:'CORS & CSP',nodes:['CORS','Content Security Policy','HTTPS'],lang:'text',run:false,
   b:['Browser menerapkan <b>same-origin policy</b>: JavaScript dari tokonusantara.id tidak boleh membaca respons dari api.lain.com kecuali server itu mengizinkan lewat header <b>CORS</b> (<code>Access-Control-Allow-Origin</code>). Error CORS diperbaiki di server, bukan di frontend.',
      '<b>Content Security Policy</b> membatasi sumber script, gaya, dan gambar. Jika penyerang berhasil menyisipkan <code>&lt;script&gt;</code> lewat komentar, CSP yang ketat mencegahnya berjalan.'],
   code:`# Browser (dari https://tokonusantara.id) meminta:
GET https://api.tokonusantara.id/produk
Origin: https://tokonusantara.id

# Server mengizinkan:
Access-Control-Allow-Origin: https://tokonusantara.id
Content-Security-Policy: default-src 'self'; script-src 'self'; img-src 'self' https://cdn.tokonusantara.id`,
   pts:['Same-origin policy membatasi baca lintas domain.','CORS diatur di server lewat header.','CSP membatasi sumber script dan konten.'],
   q:[['Error CORS diperbaiki di mana?',['Server API (header CORS)','Kode React','CSS'],0,'Server yang menentukan origin mana yang boleh.']]},
  {k:'w',t:'XSS & risiko OWASP',nodes:['OWASP Security Risks','Web Security Knowledge'],
   b:['<b>OWASP Top 10</b> adalah daftar risiko keamanan web paling umum: kontrol akses yang rusak, kegagalan kriptografi, injeksi (SQL injection, XSS), desain tidak aman, konfigurasi salah, komponen usang, autentikasi lemah, dan lainnya.',
      'Di frontend, risiko paling sering adalah <b>XSS</b> (cross-site scripting): input pengguna ditampilkan sebagai HTML sehingga script penyerang ikut berjalan. Lawannya: tampilkan input dengan <code>textContent</code>, bukan <code>innerHTML</code>, dan sanitasi HTML jika benar-benar perlu.'],
   html:`<label>Komentar: <input id="k" value="&lt;img src=x onerror=&quot;document.body.style.background='#B23A2E'&quot;&gt;"></label>
<button id="a">Tampilkan (innerHTML)</button> <button id="b">Tampilkan (textContent)</button>
<div id="out" style="margin-top:8px;padding:8px;border:1px solid #ddd"></div>`,
   js:`const out = document.getElementById("out"), k = document.getElementById("k");
document.getElementById("a").onclick = () => { out.innerHTML = k.value; };      // berbahaya
document.getElementById("b").onclick = () => { out.textContent = k.value; };    // aman`,
   pts:['Kenali OWASP Top 10.','XSS terjadi saat input pengguna dirender sebagai HTML.','Pakai textContent; sanitasi bila harus menampilkan HTML.','React otomatis meng-escape teks di JSX.'],
   q:[['Cara aman menampilkan komentar pengguna?',['textContent','innerHTML','eval'],0,'Teks tidak diurai sebagai HTML.']]},
  {k:'c',t:'Strategi autentikasi',nodes:['Authentication Strategies'],lang:'text',run:false,
   b:['<b>Session cookie</b>: server menyimpan sesi dan browser menyimpan id-nya di cookie <code>HttpOnly; Secure; SameSite</code> yang tidak bisa dibaca JavaScript. Cara paling aman untuk aplikasi web biasa.',
      '<b>Token (JWT)</b>: server memberi token bertanda tangan yang dikirim di header Authorization. Cocok untuk API dan aplikasi mobile, tapi jangan simpan di localStorage jika situs rentan XSS. <b>OAuth / OpenID Connect</b> untuk "Masuk dengan Google". <b>Passkey</b> menggantikan kata sandi dengan kunci di perangkat.'],
   code:`# Login berhasil, server mengirim cookie sesi:
Set-Cookie: sid=8f2c1e...; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=86400

# Permintaan berikutnya otomatis membawa cookie:
GET /akun
Cookie: sid=8f2c1e...

# Alternatif token untuk API:
GET /api/pesanan
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...`,
   pts:['Cookie HttpOnly + Secure + SameSite untuk sesi web.','JWT untuk API/mobile; hati-hati tempat penyimpanannya.','OAuth/OIDC untuk login pihak ketiga.','Passkey: tanpa kata sandi.'],
   q:[['Flag cookie yang mencegah JavaScript membacanya?',['HttpOnly','Secure','Path'],0,'Melindungi sesi dari XSS.']]}
 ]},
{t:'Performa & aksesibilitas',lvl:'Lanjutan',d:'Mengukur dan mempercepat situs, serta memastikan semua orang bisa memakainya.',nodes:['Performance','Lighthouse','DevTools Usage','Accessibility'],
 lessons:[
  {k:'c',t:'Core Web Vitals & Lighthouse',nodes:['Performance','Lighthouse','DevTools Usage'],viz:'vitals',
   b:['Google mengukur pengalaman pengguna dengan <b>Core Web Vitals</b>: <b>LCP</b> (Largest Contentful Paint, kapan konten utama tampil, target di bawah 2,5 detik), <b>INP</b> (Interaction to Next Paint, seberapa cepat halaman merespons klik, di bawah 200 ms), dan <b>CLS</b> (Cumulative Layout Shift, seberapa banyak tata letak melompat, di bawah 0,1).',
      '<b>Lighthouse</b> di Chrome DevTools mengaudit performa, aksesibilitas, SEO, dan praktik terbaik, lalu memberi saran konkret. Tab Network dan Performance di DevTools menunjukkan file mana yang lambat.',
      'Cara cepat memperbaiki: kompres gambar (WebP/AVIF) dan beri ukuran, lazy load gambar di bawah, kurangi JavaScript, pakai code splitting, dan muat font dengan <code>font-display: swap</code>.'],
   pts:['LCP < 2,5 s, INP < 200 ms, CLS < 0,1.','Lighthouse memberi skor dan saran.','Gambar dan JavaScript adalah penyebab paling umum situs lambat.'],
   q:[['Gambar tanpa width/height paling memengaruhi metrik?',['CLS','LCP','INP'],0,'Tata letak melompat saat gambar selesai dimuat.']]},
  {k:'see',ref:'html:Aksesibilitas dasar'}
 ]},
{t:'Web API lanjutan',lvl:'Lanjutan',d:'Web Components, Shadow DOM, PWA, dan service worker.',nodes:['Web Components','Custom Elements','HTML Templates','Shadow DOM','Progressive Web Apps','Service Workers'],
 lessons:[
  {k:'w',t:'Web Components & Shadow DOM',nodes:['Web Components','Custom Elements','HTML Templates','Shadow DOM'],
   b:['<b>Web Components</b> adalah komponen bawaan browser tanpa framework. <b>Custom element</b> mendefinisikan tag sendiri seperti <code>&lt;kartu-produk&gt;</code>. <b>Shadow DOM</b> membungkus HTML dan CSS-nya sehingga tidak bocor ke luar dan tidak terganggu gaya luar. <b>&lt;template&gt;</b> menyimpan potongan HTML yang belum dirender.',
      'Web Components bisa dipakai di React, Vue, atau HTML biasa, cocok untuk design system lintas framework.'],
   html:`<kartu-produk nama="Kopi Gayo" harga="85000"></kartu-produk>
<kartu-produk nama="Teh Melati" harga="25000"></kartu-produk>
<p class="kartu">Paragraf luar dengan class kartu tidak terpengaruh gaya di dalam komponen.</p>`,
   js:`class KartuProduk extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: "open" });
    const harga = Number(this.getAttribute("harga")).toLocaleString("id-ID");
    root.innerHTML = \`
      <style>.kartu{border:1px solid #2E5E8C;border-radius:10px;padding:8px 12px;margin:6px 0;font:14px sans-serif}
             b{color:#2E5E8C}</style>
      <div class="kartu"><b>\${this.getAttribute("nama")}</b> · Rp\${harga}</div>\`;
  }
}
customElements.define("kartu-produk", KartuProduk);`,
   task:{q:'Tambahkan satu &lt;kartu-produk&gt; lagi untuk "Madu Hutan" seharga 120000.',test:`[...document.querySelectorAll('kartu-produk')].some(e=>/Madu/.test(e.getAttribute('nama')||''))`,hint:'<kartu-produk nama="Madu Hutan" harga="120000"></kartu-produk>'},
   pts:['customElements.define membuat tag baru (wajib ada tanda hubung).','Shadow DOM mengisolasi HTML dan CSS.','Bisa dipakai di framework mana pun.'],
   q:[['Syarat nama custom element?',['Mengandung tanda hubung','Diawali huruf kapital','Maksimal 5 huruf'],0,'Contoh: kartu-produk.']]},
  {k:'c',t:'PWA & service worker',nodes:['Progressive Web Apps','Service Workers'],lang:'js',run:false,
   b:['<b>Progressive Web App</b> adalah situs yang bisa dipasang di layar utama, bekerja offline, dan mengirim notifikasi. Syaratnya: HTTPS, file <code>manifest.webmanifest</code> (nama, ikon, warna), dan <b>service worker</b>.',
      'Service worker adalah script yang berjalan di latar belakang dan bisa mencegat permintaan jaringan. Dengan itu, halaman dan aset bisa diambil dari cache saat sinyal hilang, hal yang penting di daerah dengan koneksi tidak stabil.'],
   code:`// sw.js — cache dulu, jaringan kemudian
const CACHE = "toko-v1";
self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(["/", "/app.js", "/gaya.css", "/offline.html"])));
});
self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(hit => hit || fetch(e.request).catch(() => caches.match("/offline.html")))
  );
});

// main.js
if ("serviceWorker" in navigator) navigator.serviceWorker.register("/sw.js");`,
   pts:['PWA: HTTPS + manifest + service worker.','Service worker mencegat request dan memakai cache.','Penting untuk pengguna dengan koneksi tidak stabil.'],
   q:[['Komponen PWA yang memungkinkan offline?',['Service worker','Manifest','Favicon'],0,'Ia menyajikan dari cache saat offline.']]}
 ]},
{t:'Rendering, SSR & deploy',lvl:'Profesional',d:'CSR, SSR, SSG, framework meta, GraphQL, dan tempat menerbitkan aplikasi.',nodes:['Server-side rendering','Static Site Generators','Next.js','Nuxt.js','SvelteKit','Astro','Eleventy','Vuepress','Tanstack Start','Graphql','Apollo','Relay Modern','Deployment','Vercel','Netlify','Cloudflare','Render','Railway','GitHub Pages'],
 lessons:[
  {k:'c',t:'CSR, SSR & SSG',nodes:['Server-side rendering','Static Site Generators','Next.js','Nuxt.js','SvelteKit','Astro','Eleventy','Vuepress','Tanstack Start'],viz:'ssr',
   b:['<b>CSR</b> (client-side rendering): server mengirim HTML hampir kosong, JavaScript membangun halaman di browser. Interaktif setelah JS dimuat, tapi tampilan pertama lebih lambat dan kurang ramah SEO.',
      '<b>SSR</b> (server-side rendering): HTML dibuat di server untuk setiap permintaan, lalu JavaScript "menghidupkannya" (hydration). <b>SSG</b> (static site generation): HTML dibuat sekali saat build, sangat cepat dan murah.',
      'Framework meta seperti <b>Next.js</b> (React), <b>Nuxt</b> (Vue), <b>SvelteKit</b>, dan <b>Astro</b> bisa mencampur ketiganya per halaman. Situs dokumentasi atau blog cocok dengan SSG; dashboard pribadi cocok dengan CSR; toko online cocok dengan SSR/SSG campuran.'],
   pts:['CSR: dirender di browser.','SSR: dirender di server per permintaan.','SSG: dirender saat build.','Framework meta mencampur per halaman.'],
   q:[['Blog yang jarang berubah paling cocok dengan?',['SSG','CSR','SSR per permintaan'],0,'HTML sudah jadi sejak build.']]},
  {k:'c',t:'GraphQL',nodes:['Graphql','Apollo','Relay Modern'],lang:'text',run:false,
   b:['Di REST, setiap sumber data punya alamat sendiri (<code>/produk</code>, <code>/produk/1/ulasan</code>). Di <b>GraphQL</b>, ada satu endpoint dan klien menulis <b>query</b> yang menyebut persis kolom yang dibutuhkan. Tidak ada data berlebih, dan data bertingkat diambil sekali jalan.',
      'Klien seperti Apollo dan Relay mengelola cache hasil query di frontend.'],
   code:`# query dari klien
query {
  produk(id: 1) {
    nama
    harga
    ulasan(terbaru: 2) { bintang komentar }
  }
}

# respons server: bentuknya sama dengan query
{ "data": { "produk": { "nama": "Kopi Gayo", "harga": 85000,
  "ulasan": [ { "bintang": 5, "komentar": "Wangi!" }, { "bintang": 4, "komentar": "Mantap" } ] } } }`,
   pts:['Satu endpoint, klien menentukan bentuk data.','Tidak ada over-fetching.','Apollo/Relay mengelola cache.'],
   q:[['Keunggulan utama GraphQL?',['Klien meminta tepat kolom yang dibutuhkan','Tidak butuh server','Lebih aman otomatis'],0,'Bentuk respons mengikuti query.']]},
  {k:'see',ref:'fe0:Menerbitkan situs'}
 ]},
{t:'AI untuk frontend developer',lvl:'Profesional',d:'Cara kerja LLM, prompt engineering, asisten coding, dan membangun fitur AI.',nodes:['AI vs. Traditional Software Development','How LLMs Work','Prompt Engineering','AI-Assisted Coding','Claude Code','GitHub Copilot','Cursor','AI-Powered Code Reviews','Refactoring with AI','Documentation Generation with AI','Implementing AI','Generative AI for Frontend Development','AI Applications in Frontend Development','OpenAI','Anthropic','Gemini','Streamed Responses','Model Context Protocol (MCP)','AI Agents','Skills','Antigravity'],
 lessons:[
  {k:'c',t:'LLM & asisten coding',nodes:['AI vs. Traditional Software Development','How LLMs Work','Prompt Engineering','AI-Assisted Coding','Claude Code','GitHub Copilot','Cursor','AI-Powered Code Reviews','Refactoring with AI','Documentation Generation with AI','AI Agents','Skills','Antigravity','Model Context Protocol (MCP)'],
   b:['<b>Large Language Model</b> (LLM) dilatih memprediksi kata berikutnya dari teks dalam jumlah sangat besar. Hasilnya model yang bisa menjelaskan, menulis, dan memperbaiki kode, tetapi juga bisa keliru dengan percaya diri. Karena itu, hasilnya selalu perlu kamu baca dan uji.',
      'Asisten coding seperti <b>Claude Code</b>, <b>GitHub Copilot</b>, dan <b>Cursor</b> membantu menulis kode, refactor, membuat tes dan dokumentasi, serta meninjau pull request. <b>Agen</b> AI bisa menjalankan perintah dan mengubah banyak file; <b>MCP</b> (Model Context Protocol) menghubungkan AI dengan alat dan data lain.',
      'Prompt yang baik memberi konteks (proyek, teknologi), tugas yang jelas, batasan (gaya kode, pustaka yang boleh), dan contoh hasil yang diinginkan.'],
   code:`Konteks: proyek React + TypeScript + Tailwind, komponen di src/components.
Tugas: buat komponen KartuProduk yang menampilkan nama, harga (format Rupiah),
dan tombol "Tambah ke keranjang".
Batasan: tanpa pustaka tambahan, aksesibel (button asli, alt pada gambar),
tulis juga satu tes Vitest + Testing Library.
Contoh pemakaian: <KartuProduk nama="Kopi Gayo" harga={85000} onTambah={...} />`,lang:'text',run:false,
   pts:['LLM memprediksi teks; bisa salah dengan yakin.','Selalu baca, jalankan, dan uji kode hasil AI.','Prompt: konteks, tugas, batasan, contoh.','Agen dan MCP memperluas kemampuan AI.'],
   q:[['Sikap yang benar terhadap kode buatan AI?',['Baca dan uji seperti kode dari rekan kerja','Langsung deploy','Tidak boleh dipakai sama sekali'],0,'Kamu tetap bertanggung jawab atas kodenya.']]},
  {k:'c',t:'Membangun fitur AI di frontend',nodes:['Implementing AI','Generative AI for Frontend Development','AI Applications in Frontend Development','OpenAI','Anthropic','Gemini','Streamed Responses'],lang:'js',run:false,
   b:['Fitur AI di aplikasi (chatbot, ringkasan, pencarian semantik) memanggil API model dari penyedia seperti Anthropic, OpenAI, atau Google. <b>Kunci API tidak boleh ada di kode frontend</b>; panggil lewat server atau fungsi serverless milikmu.',
      'Jawaban model dikirim bertahap (<b>streaming</b>) agar pengguna langsung melihat teks muncul, bukan menunggu jawaban utuh. Di frontend, baca stream dengan <code>response.body.getReader()</code>.'],
   code:`// Frontend: membaca jawaban yang di-stream dari server kita sendiri
async function tanya(pertanyaan, tulis) {
  const res = await fetch("/api/tanya", { method: "POST", body: JSON.stringify({ pertanyaan }) });
  const reader = res.body.getReader();
  const dec = new TextDecoder();
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    tulis(dec.decode(value, { stream: true }));   // tampilkan potongan teks segera
  }
}
// Server (/api/tanya) yang memegang kunci API dan meneruskan stream dari penyedia model.`,
   pts:['Kunci API selalu di server.','Streaming membuat jawaban terasa cepat.','Tampilkan status, tangani error, dan beri tahu bahwa jawaban bisa keliru.'],
   q:[['Di mana kunci API model AI disimpan?',['Di server/fungsi serverless','Di kode React','Di localStorage'],0,'Kode frontend bisa dibaca siapa pun.']]}
 ]},
{t:'Proyek akhir Frontend',lvl:'Profesional',d:'Aplikasi web lengkap: cepat, aman, teruji, dan terbit.',nodes:[],
 lessons:[
  {k:'proj',t:'Dashboard cuaca & kualitas udara',stack:'React + Vite + TypeScript',
   brief:'Bangun aplikasi yang menampilkan cuaca dan kualitas udara beberapa kota Indonesia dari API publik, lengkap dengan pencarian, favorit, mode gelap, dan dukungan offline sederhana.',
   feats:['Proyek Vite + React + TypeScript dengan ESLint dan Prettier','Pencarian kota dengan debounce dan keadaan loading/error','Data diambil dengan TanStack Query (cache dan retry)','Kota favorit tersimpan di localStorage','Mode gelap dengan variabel CSS dan prefers-color-scheme','Skor Lighthouse performa dan aksesibilitas minimal 90','Minimal 3 unit test (Vitest) dan 1 tes E2E (Playwright)','Kunci API (jika ada) tidak bocor ke kode frontend','Terbit di Vercel/Netlify dengan deploy otomatis dari GitHub'],
   steps:['Rancang tampilan di kertas atau Figma.','Bangun komponen dengan data tiruan.','Sambungkan API dan tangani semua keadaan.','Ukur dengan Lighthouse, tulis tes, lalu terbitkan.'],
   files:[['src/hooks/useCuaca.ts','ts',`import { useQuery } from "@tanstack/react-query";

export type Cuaca = { kota: string; suhu: number; kondisi: string };

export function useCuaca(lat: number, lon: number) {
  return useQuery({
    queryKey: ["cuaca", lat, lon],
    queryFn: async (): Promise<Cuaca> => {
      const url = \`https://api.open-meteo.com/v1/forecast?latitude=\${lat}&longitude=\${lon}&current=temperature_2m,weather_code\`;
      const res = await fetch(url);
      if (!res.ok) throw new Error("Gagal memuat cuaca");
      const j = await res.json();
      return { kota: \`\${lat},\${lon}\`, suhu: j.current.temperature_2m, kondisi: String(j.current.weather_code) };
    },
    staleTime: 10 * 60 * 1000,
  });
}`]]}
 ]}
];
