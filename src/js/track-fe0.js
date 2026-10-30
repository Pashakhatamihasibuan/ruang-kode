/* ===================== JALUR FRONTEND PEMULA =====================
   Mengikuti roadmap.sh/frontend-beginner. Banyak pelajaran dipinjam dari jalur lain
   lewat {k:'see', ref:'jalur:Judul pelajaran'}; progresnya ikut tersimpan di pelajaran asal.
   Pelajaran JavaScript dasar ada di sini dan dipinjam jalur Frontend. */
const FE0_MODULES=[
{t:'Mulai dari sini',lvl:'Pemula',d:'Gambaran kerja frontend developer dan cara web sampai ke layar.',nodes:['HTML','CSS','JavaScript'],
 lessons:[
  {k:'c',t:'Apa kerja frontend developer?',nodes:['HTML','CSS','JavaScript'],
   b:['Frontend developer membangun bagian situs atau aplikasi yang dilihat dan disentuh pengguna. Tiga bahan utamanya: <b>HTML</b> untuk struktur dan isi, <b>CSS</b> untuk tampilan, dan <b>JavaScript</b> untuk perilaku (apa yang terjadi saat tombol ditekan).',
      'Di atas tiga bahan itu ada alat kerja: <b>Git dan GitHub</b> untuk menyimpan riwayat kode dan bekerja sama, <b>npm</b> untuk memasang pustaka, framework seperti <b>React</b> untuk membangun antarmuka yang rumit, dan <b>Tailwind</b> untuk menata gaya lebih cepat.',
      'Jalur ini mengikuti urutan roadmap frontend pemula: HTML, CSS, JavaScript, Git, GitHub, npm, Tailwind, React, lalu Vitest untuk pengujian. Di akhir, kamu membangun dan menerbitkan satu proyek sendiri.'],
   pts:['HTML = struktur, CSS = tampilan, JavaScript = perilaku.','Git dan GitHub untuk riwayat kode dan kolaborasi.','npm memasang pustaka; React membangun UI; Tailwind menata gaya.','Belajar paling cepat dengan membuat proyek kecil.'],
   q:[['Bagian yang mengatur apa yang terjadi saat tombol ditekan?',['JavaScript','HTML','CSS'],0,'JavaScript menangani perilaku dan interaksi.']]},
  {k:'see',ref:'html:Cara web bekerja'}
 ]},
{t:'HTML',lvl:'Pemula',d:'Struktur halaman, teks, link, gambar, daftar, form, dan elemen semantik.',nodes:['HTML'],
 lessons:[
  {k:'see',ref:'html:Struktur dokumen HTML'},{k:'see',ref:'html:Tag, atribut & elemen'},{k:'see',ref:'html:Judul & paragraf'},
  {k:'see',ref:'html:Link'},{k:'see',ref:'html:Gambar & figure'},{k:'see',ref:'html:Daftar'},
  {k:'see',ref:'html:Form, label & input'},{k:'see',ref:'html:Elemen semantik'}
 ]},
{t:'CSS',lvl:'Pemula',d:'Selector, box model, warna, tipografi, flexbox, grid, dan tampilan responsif.',nodes:['CSS'],
 lessons:[
  {k:'see',ref:'css:Aturan, selector & deklarasi'},{k:'see',ref:'css:Selector sederhana'},{k:'see',ref:'css:Box model'},
  {k:'see',ref:'css:Warna & latar'},{k:'see',ref:'css:Tipografi'},{k:'see',ref:'css:Flexbox'},{k:'see',ref:'css:Grid'},
  {k:'see',ref:'css:Media query & mobile-first'}
 ]},
{t:'JavaScript dasar',lvl:'Pemula',d:'Variabel, kondisi, fungsi, array, objek, DOM, event, dan mengambil data dari server.',nodes:['JavaScript'],
 lessons:[
  {k:'w',t:'Variabel & tipe data',nodes:['JavaScript'],console:true,
   b:['JavaScript adalah bahasa pemrograman yang berjalan di browser. Variabel dibuat dengan <code>const</code> (nilainya tidak akan diganti) atau <code>let</code> (boleh diganti). Hindari <code>var</code> yang sudah usang.',
      'Tipe dasarnya: <b>string</b> (teks), <b>number</b> (bilangan bulat dan pecahan sama-sama number), <b>boolean</b>, <b>null</b> (sengaja kosong), <b>undefined</b> (belum diberi nilai), serta object dan array. Operator <code>typeof</code> menunjukkan tipenya.',
      'Template literal memakai backtick dan <code>${...}</code> untuk menyisipkan nilai. <code>console.log</code> mencetak ke panel konsol di bawah pratinjau.'],
   html:`<p>Lihat panel Konsol di bawah.</p>`,
   js:`const nama = "Sinta";
let saldo = 50000;
saldo = saldo - 12000;          // let boleh diganti
const aktif = true;

console.log(\`Halo, \${nama}! Saldo: \${saldo}\`);
console.log(typeof nama, typeof saldo, typeof aktif);
console.log(0.1 + 0.2);          // pecahan biner tidak selalu tepat
console.log("5" + 3, "5" - 3);   // + menyambung string, - mengubah ke angka`,
   task:{q:'Buat variabel <code>kota</code> berisi "Bandung" lalu cetak dengan console.log.',test:`(window.__logs||[]).some(l=>/Bandung/.test(l))`,hint:'const kota = "Bandung"; console.log(kota);'},
   pts:['const untuk nilai tetap, let untuk nilai yang berubah.','typeof memeriksa tipe.','Template literal: `Halo ${nama}`.','"5" + 3 menghasilkan "53"; hati-hati dengan konversi otomatis.'],
   q:[['Hasil "5" + 3 di JavaScript?',['"53"','8','Error'],0,'+ dengan string menjadi penyambungan.'],
      ['Kapan memakai const?',['Saat variabel tidak akan diberi nilai baru','Untuk angka saja','Tidak pernah'],0,'Default-lah ke const, pakai let bila perlu.']]},
  {k:'w',t:'Operator & percabangan',nodes:['JavaScript'],console:true,
   b:['Bandingkan nilai dengan <code>===</code> (sama nilai dan tipe) dan <code>!==</code>. Hindari <code>==</code> karena mengubah tipe diam-diam: <code>"0" == 0</code> bernilai true.',
      'Percabangan memakai <code>if / else if / else</code>, atau operator ternary <code>kondisi ? a : b</code> untuk pilihan singkat. Operator logika: <code>&amp;&amp;</code> (dan), <code>||</code> (atau), <code>!</code> (tidak). Operator <code>??</code> memberi nilai cadangan hanya jika nilainya null atau undefined.'],
   html:`<p>Lihat panel Konsol.</p>`,
   js:`const total = 135000;
const member = true;

let ongkir;
if (total >= 100000) {
  ongkir = 0;
} else if (member) {
  ongkir = 5000;
} else {
  ongkir = 15000;
}
console.log("Ongkir:", ongkir);

const label = total > 200000 ? "besar" : "biasa";
console.log("Pesanan", label);

console.log("0" == 0, "0" === 0);
const kupon = null;
console.log(kupon ?? "tanpa kupon");`,
   task:{q:'Ubah total menjadi 80000 dan pastikan konsol mencetak "Ongkir: 5000".',test:`(window.__logs||[]).some(l=>/Ongkir: 5000/.test(l))`,hint:'Ganti const total = 80000;'},
   pts:['Pakai === dan !==, hindari ==.','Ternary untuk pilihan singkat.','?? memberi cadangan untuk null/undefined.'],
   q:[['"0" === 0 bernilai?',['false','true','Error'],0,'=== juga membandingkan tipe.']]},
  {k:'w',t:'Fungsi',nodes:['JavaScript'],console:true,
   b:['Fungsi membungkus langkah agar bisa dipakai ulang. Ada dua bentuk umum: deklarasi <code>function hitung(a, b) { ... }</code> dan <b>arrow function</b> <code>const hitung = (a, b) =&gt; a + b</code>.',
      'Parameter bisa punya nilai bawaan: <code>(harga, diskon = 0) =&gt; ...</code>. Fungsi adalah nilai biasa, jadi bisa dikirim ke fungsi lain (callback), misalnya ke <code>setTimeout</code> atau <code>addEventListener</code>.'],
   html:`<p>Lihat panel Konsol.</p>`,
   js:`function rupiah(n) {
  return "Rp" + n.toLocaleString("id-ID");
}
const hargaAkhir = (harga, diskon = 0) => harga - harga * diskon;

console.log(rupiah(85000));
console.log(rupiah(hargaAkhir(85000, 0.2)));
console.log(rupiah(hargaAkhir(25000)));

// fungsi sebagai argumen (callback)
setTimeout(() => console.log("Pesan ini muncul 1 detik kemudian"), 1000);`,
   task:{q:'Buat fungsi <code>pajak(n)</code> yang mengembalikan 11% dari n, lalu cetak <code>pajak(100000)</code> (hasilnya 11000).',test:`(window.__logs||[]).some(l=>/^11000$/.test(l.trim()))`,hint:'const pajak = n => n * 0.11; console.log(pajak(100000));'},
   pts:['function deklarasi dan arrow function.','Parameter bawaan: (x = 0).','Fungsi bisa dikirim sebagai callback.'],
   q:[['Bentuk arrow function yang benar?',['const f = (a, b) => a + b','const f = a, b => a + b','function => (a, b)'],0,'Parameter lebih dari satu dalam kurung.']]},
  {k:'w',t:'Array & objek',nodes:['JavaScript'],console:true,
   b:['<b>Array</b> menyimpan daftar berurutan: <code>["kopi", "teh"]</code>. <b>Objek</b> menyimpan pasangan kunci-nilai: <code>{ nama: "Kopi", harga: 85000 }</code>. Data dari server hampir selalu berbentuk array berisi objek.',
      'Metode array yang paling sering dipakai: <code>map</code> (ubah setiap elemen), <code>filter</code> (saring), <code>reduce</code> (ringkas jadi satu nilai), <code>find</code>, dan <code>sort</code>. Destructuring <code>const { nama } = produk</code> dan spread <code>[...a, x]</code> membuat kode ringkas.'],
   html:`<p>Lihat panel Konsol.</p>`,
   js:`const produk = [
  { nama: "Kopi Gayo", harga: 85000, stok: 40 },
  { nama: "Teh Melati", harga: 25000, stok: 120 },
  { nama: "Rendang Kaleng", harga: 75000, stok: 0 },
];

const tersedia = produk.filter(p => p.stok > 0);
const nama = tersedia.map(p => p.nama);
const totalStok = produk.reduce((jml, p) => jml + p.stok, 0);

console.log(nama);
console.log("Total stok:", totalStok);

const { harga } = produk[0];
const baru = [...produk, { nama: "Madu", harga: 120000, stok: 15 }];
console.log(harga, baru.length);`,
   task:{q:'Cetak array harga semua produk memakai <code>map</code>.',test:`(window.__logs||[]).some(l=>/85000.*25000.*75000/.test(l))`,hint:'console.log(produk.map(p => p.harga));'},
   pts:['Array berurutan, objek kunci-nilai.','map, filter, reduce, find adalah alat utama.','Destructuring dan spread meringkas kode.'],
   q:[['Metode untuk menyaring elemen yang memenuhi syarat?',['filter','map','reduce'],0,'filter mengembalikan array baru yang lolos syarat.']]},
  {k:'w',t:'DOM & event',nodes:['JavaScript'],
   b:['<b>DOM</b> (Document Object Model) adalah HTML dalam bentuk objek yang bisa diubah JavaScript. Ambil elemen dengan <code>document.querySelector(".kelas")</code>, ubah teksnya dengan <code>textContent</code>, dan ubah gaya dengan <code>classList.add/remove/toggle</code>.',
      '<b>Event</b> adalah kejadian seperti klik, ketikan, atau kirim form. Daftarkan pendengarnya dengan <code>elemen.addEventListener("click", fungsi)</code>. Buat elemen baru dengan <code>document.createElement</code> lalu <code>append</code>.'],
   html:`<h3>Daftar belanja</h3>
<form id="f"><input id="isi" placeholder="Contoh: Kopi Gayo" aria-label="Barang"> <button>Tambah</button></form>
<ul id="daftar"></ul>
<p id="jumlah">0 barang</p>`,
   css:`li{cursor:pointer}li.selesai{text-decoration:line-through;color:#999}body{font:14px sans-serif}`,
   js:`const form = document.querySelector("#f");
const daftar = document.querySelector("#daftar");

form.addEventListener("submit", e => {
  e.preventDefault();                       // jangan muat ulang halaman
  const isi = document.querySelector("#isi");
  if (!isi.value.trim()) return;
  const li = document.createElement("li");
  li.textContent = isi.value;
  li.addEventListener("click", () => li.classList.toggle("selesai"));
  daftar.append(li);
  isi.value = "";
  document.querySelector("#jumlah").textContent = daftar.children.length + " barang";
});`,
   task:{q:'Tambahkan tiga barang lewat form, lalu klik salah satunya hingga tercoret.',test:`document.querySelectorAll('#daftar li').length>=3&&!!document.querySelector('#daftar li.selesai')`,hint:'Ketik di input, tekan Tambah tiga kali, lalu klik satu barang.'},
   pts:['querySelector mengambil elemen.','textContent dan classList mengubah isi dan gaya.','addEventListener mendaftarkan event.','preventDefault mencegah form memuat ulang halaman.'],
   q:[['Cara aman mengisi teks dari input pengguna ke halaman?',['textContent','innerHTML','eval'],0,'innerHTML bisa menjalankan HTML/script yang disisipkan.']]},
  {k:'w',t:'Mengambil data: fetch, JSON & async',nodes:['JavaScript'],console:true,
   b:['Data dari server biasanya berbentuk <b>JSON</b>, teks yang mirip objek JavaScript. <code>JSON.parse</code> mengubah teks menjadi objek, <code>JSON.stringify</code> sebaliknya.',
      '<code>fetch(url)</code> meminta data dan mengembalikan <b>Promise</b>, janji hasil yang datang nanti. Dengan <code>async/await</code>, kode menunggu hasil tanpa membekukan halaman. Bungkus dengan <code>try/catch</code> untuk menangani gagal jaringan.',
      'Contoh di bawah memakai server tiruan agar bisa berjalan di mana saja; polanya sama persis dengan fetch sungguhan.'],
   html:`<button id="muat">Muat produk</button><ul id="hasil"></ul>`,
   js:`// server tiruan: membalas setelah 600 ms
const fetchTiruan = () => new Promise(res => setTimeout(() =>
  res({ ok: true, json: async () => JSON.parse('[{"nama":"Kopi Gayo","harga":85000},{"nama":"Teh Melati","harga":25000}]') }), 600));

async function muatProduk() {
  console.log("Meminta data...");
  try {
    const res = await fetchTiruan("/api/produk");
    if (!res.ok) throw new Error("Gagal memuat");
    const data = await res.json();
    console.log("Diterima", data.length, "produk");
    document.querySelector("#hasil").innerHTML = "";
    data.forEach(p => {
      const li = document.createElement("li");
      li.textContent = p.nama + " - Rp" + p.harga.toLocaleString("id-ID");
      document.querySelector("#hasil").append(li);
    });
  } catch (err) {
    console.log("Error:", err.message);
  }
}
document.querySelector("#muat").addEventListener("click", muatProduk);
console.log("Kode di bawah fetch tetap jalan duluan.");`,
   task:{q:'Klik tombol "Muat produk" sampai daftar terisi.',test:`document.querySelectorAll('#hasil li').length>=2`,hint:'Tekan tombol di pratinjau dan tunggu sebentar.'},
   pts:['JSON adalah format tukar data.','fetch mengembalikan Promise.','async/await membuat kode asinkron terbaca berurutan.','Selalu tangani error dengan try/catch.'],
   q:[['Apa yang dikembalikan fetch?',['Promise','Data JSON langsung','String HTML'],0,'Hasilnya ditunggu dengan await atau .then().']]}
 ]},
{t:'Git & GitHub',lvl:'Pemula',d:'Simpan riwayat kode dan bagikan proyek di GitHub.',nodes:['Git','GitHub'],
 lessons:[
  {k:'see',ref:'git:Apa itu version control & Git?'},{k:'see',ref:'git:init, add, commit'},{k:'see',ref:'git:Branch & merge'},
  {k:'see',ref:'git:Remote, push & pull'},{k:'see',ref:'git:Fork & pull request'}
 ]},
{t:'npm, Tailwind & React',lvl:'Menengah',d:'Pasang pustaka, tata gaya dengan utility class, dan mulai membangun komponen.',nodes:['npm','Tailwind CSS','React'],
 lessons:[
  {k:'c',t:'npm & package.json',nodes:['npm'],lang:'bash',run:false,
   b:['<b>npm</b> (Node Package Manager) memasang pustaka buatan orang lain ke proyekmu. Pustaka tercatat di <code>package.json</code>, file daftar isi proyek, dan disimpan di folder <code>node_modules</code> yang tidak perlu ikut di-commit.',
      '<code>npm install nama</code> memasang pustaka, <code>npm install -D nama</code> untuk alat pengembangan saja, dan <code>npm run dev</code> menjalankan skrip yang ditulis di bagian <code>scripts</code>. File <code>package-lock.json</code> mengunci versi persis agar semua anggota tim mendapat versi yang sama.',
      'Untuk memulai proyek frontend modern, perintah <code>npm create vite@latest</code> menyiapkan kerangka lengkap dalam hitungan detik.'],
   code:`$ npm create vite@latest toko-nusantara -- --template react
$ cd toko-nusantara
$ npm install
$ npm install -D vitest
$ npm run dev
  VITE ready in 312 ms
  ➜  Local:   http://localhost:5173/`,
   pts:['package.json mencatat pustaka dan skrip.','node_modules tidak di-commit.','-D untuk alat pengembangan.','package-lock.json mengunci versi.'],
   q:[['Folder yang sebaiknya dimasukkan ke .gitignore?',['node_modules','src','public'],0,'Bisa dibuat ulang dengan npm install.']]},
  {k:'w',t:'Tailwind CSS',nodes:['Tailwind CSS'],
   b:['Tailwind adalah kumpulan <b>utility class</b>: class kecil yang masing-masing melakukan satu hal, misalnya <code>p-4</code> (padding), <code>rounded-xl</code>, <code>text-sm</code>, <code>flex</code>, <code>gap-2</code>. Kamu menata langsung di HTML tanpa berpindah file.',
      'Prefix responsif seperti <code>md:</code> berlaku mulai lebar tertentu, dan <code>hover:</code> untuk keadaan. Saat build, Tailwind hanya menyertakan class yang benar-benar kamu pakai, jadi CSS akhirnya kecil.',
      'Pratinjau ini memakai potongan CSS buatan sendiri yang meniru beberapa class Tailwind agar bisa berjalan tanpa internet.'],
   html:`<div class="p-4 rounded-xl border flex gap-3 items-center">
  <div class="w-12 h-12 rounded-full bg-aksen"></div>
  <div>
    <p class="font-semibold">Kopi Gayo</p>
    <p class="text-sm text-redup">Rp85.000</p>
  </div>
  <button class="ml-auto px-3 py-1 rounded-full bg-gelap text-putih hover-naik">Beli</button>
</div>`,
   css:`/* tiruan kecil dari class Tailwind */
body{font-family:system-ui,sans-serif}
.p-4{padding:1rem}.px-3{padding-left:.75rem;padding-right:.75rem}.py-1{padding-top:.25rem;padding-bottom:.25rem}
.rounded-xl{border-radius:.75rem}.rounded-full{border-radius:999px}.border{border:1px solid #e5e5e5}
.flex{display:flex}.gap-3{gap:.75rem}.items-center{align-items:center}.ml-auto{margin-left:auto}
.w-12{width:3rem}.h-12{height:3rem}.bg-aksen{background:#B4532A}.bg-gelap{background:#1C1B19}.text-putih{color:#fff}
.font-semibold{font-weight:600}.text-sm{font-size:.875rem}.text-redup{color:#6E6B64}
.hover-naik{border:0;transition:transform .2s}.hover-naik:hover{transform:translateY(-2px)}`,
   pts:['Utility class: satu class, satu tugas.','md: untuk responsif, hover: untuk keadaan.','Build hanya menyertakan class yang dipakai.'],
   q:[['Class Tailwind untuk padding 1rem di semua sisi?',['p-4','pad-1','padding-4'],0,'Skala 4 = 1rem.']]},
  {k:'see',ref:'react:Komponen & JSX'},{k:'see',ref:'react:Props'},{k:'see',ref:'react:State dengan useState'}
 ]},
{t:'Pengujian & terbit',lvl:'Menengah',d:'Uji fungsi dengan Vitest dan terbitkan situs ke internet.',nodes:['Vitest'],
 lessons:[
  {k:'c',t:'Menguji kode dengan Vitest',nodes:['Vitest'],lang:'js',run:false,
   b:['Tes otomatis memeriksa bahwa kodemu bekerja, dan terus bekerja setelah diubah. <b>Vitest</b> adalah test runner yang cepat dan menyatu dengan Vite.',
      'Tes ditulis di file <code>*.test.js</code>: <code>describe</code> mengelompokkan, <code>it</code> atau <code>test</code> menulis satu kasus, dan <code>expect(nilai).toBe(harapan)</code> memeriksa hasil. Jalankan dengan <code>npx vitest</code>.'],
   code:`// harga.js
export const hargaAkhir = (harga, diskon = 0) => harga - harga * diskon;

// harga.test.js
import { describe, it, expect } from "vitest";
import { hargaAkhir } from "./harga.js";

describe("hargaAkhir", () => {
  it("tanpa diskon harga tetap", () => {
    expect(hargaAkhir(85000)).toBe(85000);
  });
  it("diskon 20%", () => {
    expect(hargaAkhir(85000, 0.2)).toBe(68000);
  });
});

/* $ npx vitest run
 ✓ harga.test.js (2 tests) 3ms
 Test Files  1 passed (1)
      Tests  2 passed (2) */`,
   pts:['Tes mencegah bug lama muncul lagi.','describe, it, expect adalah pola dasar.','Jalankan tes sebelum push.'],
   q:[['Fungsi untuk memeriksa hasil di Vitest?',['expect','assert.print','check'],0,'expect(x).toBe(y).']]},
  {k:'c',t:'Menerbitkan situs',nodes:['GitHub'],lang:'bash',run:false,
   b:['Situs statis (HTML, CSS, JS) bisa diterbitkan gratis. <b>GitHub Pages</b> menerbitkan langsung dari repositori. <b>Vercel</b>, <b>Netlify</b>, dan <b>Cloudflare Pages</b> terhubung ke GitHub dan otomatis membangun ulang setiap kali kamu push.',
      'Untuk proyek Vite, perintah <code>npm run build</code> menghasilkan folder <code>dist</code> berisi file siap terbit. Ruang Kode yang sedang kamu pakai diterbitkan dengan cara ini: push ke GitHub, Vercel membangun dan menerbitkan otomatis.'],
   code:`$ npm run build
  dist/index.html          0.46 kB
  dist/assets/index.js   143.21 kB
$ git add .
$ git commit -m "Siap terbit"
$ git push
# Vercel mendeteksi push lalu menerbitkan ke https://toko-nusantara.vercel.app`,
   pts:['GitHub Pages, Vercel, Netlify gratis untuk situs statis.','npm run build menghasilkan folder dist.','Deploy otomatis setiap push.'],
   q:[['Perintah yang menyiapkan file siap terbit di proyek Vite?',['npm run build','npm start','git build'],0,'Hasilnya di folder dist.']]}
 ]},
{t:'Proyek akhir Frontend Pemula',lvl:'Menengah',d:'Bangun dan terbitkan aplikasi kecil dengan HTML, CSS, dan JavaScript.',nodes:[],
 lessons:[
  {k:'proj',t:'Aplikasi daftar belanja',stack:'HTML + CSS + JavaScript',
   brief:'Buat aplikasi daftar belanja yang menyimpan data di localStorage, lalu terbitkan ke GitHub Pages atau Vercel.',
   feats:['Form tambah barang dengan label dan validasi tidak boleh kosong','Daftar barang; klik untuk menandai sudah dibeli','Tombol hapus per barang dan tombol hapus yang sudah dibeli','Jumlah barang tersisa diperbarui otomatis','Data tetap ada setelah halaman dimuat ulang (localStorage)','Tampilan rapi di ponsel 360px','Kode di GitHub dengan minimal 5 commit yang pesannya jelas','Situs sudah terbit dan bisa dibuka orang lain'],
   steps:['Tulis HTML: form dan ul kosong.','Tambahkan JavaScript: tambah, tandai, hapus.','Simpan dan muat dari localStorage.','Tata dengan CSS, lalu push dan terbitkan.'],
   files:[['index.html','html',`<!DOCTYPE html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daftar Belanja</title>
<style>
body{font:16px system-ui,sans-serif;max-width:420px;margin:24px auto;padding:0 16px}
form{display:flex;gap:8px}input{flex:1;padding:8px;border:1px solid #ccc;border-radius:8px}
button{padding:8px 12px;border:0;border-radius:8px;background:#1C1B19;color:#fff}
li{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #eee;cursor:pointer}
li.beli span{text-decoration:line-through;color:#999}
</style></head>
<body>
<h1>Daftar belanja</h1>
<form id="f"><label for="isi" hidden>Barang</label><input id="isi" required placeholder="Tambah barang"><button>Tambah</button></form>
<ul id="daftar"></ul>
<p id="sisa"></p>
<button id="bersih">Hapus yang sudah dibeli</button>
<script>
let data = JSON.parse(localStorage.getItem("belanja") || "[]");
const simpan = () => localStorage.setItem("belanja", JSON.stringify(data));
function tampil() {
  const ul = document.getElementById("daftar");
  ul.innerHTML = "";
  data.forEach((b, i) => {
    const li = document.createElement("li");
    li.className = b.beli ? "beli" : "";
    const s = document.createElement("span"); s.textContent = b.nama;
    const x = document.createElement("button"); x.textContent = "Hapus";
    x.onclick = e => { e.stopPropagation(); data.splice(i, 1); simpan(); tampil(); };
    li.onclick = () => { b.beli = !b.beli; simpan(); tampil(); };
    li.append(s, x); ul.append(li);
  });
  document.getElementById("sisa").textContent = data.filter(b => !b.beli).length + " barang belum dibeli";
}
document.getElementById("f").onsubmit = e => {
  e.preventDefault();
  const isi = document.getElementById("isi");
  data.push({ nama: isi.value.trim(), beli: false });
  isi.value = ""; simpan(); tampil();
};
document.getElementById("bersih").onclick = () => { data = data.filter(b => !b.beli); simpan(); tampil(); };
tampil();
<\/script>
</body></html>`]],
   preview:true}
 ]}
];
