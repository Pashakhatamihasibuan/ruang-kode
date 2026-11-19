"""Pendalaman jalur Tailwind CSS: istilah dunia kerja, markup siap pakai, dan perhitungan yang dijalankan dengan Node."""
K = 'tw'


def H(t, code, b=None, lang='html'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def J(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='js')


D = {
'Utility-first dan cara memasang': dict(
  ist=[('Utility-first', 'Gaya disusun dari kelas kecil satu fungsi (p-4, flex, text-lg) langsung di markup.'),
       ('JIT / on-demand', 'Tailwind hanya menghasilkan CSS untuk kelas yang benar-benar dipakai.'),
       ('Content detection', 'Tailwind v4 memindai file proyek otomatis untuk menemukan kelas.'),
       ('@import "tailwindcss"', 'Satu baris CSS untuk memuat Tailwind v4.'),
       ('Arbitrary value', 'Nilai bebas dalam kurung siku: w-[342px], bg-[#0f766e].')],
  cx=[H('Memasang Tailwind v4 dengan Vite', r'''
npm create vite@latest landing -- --template vanilla
cd landing && npm install tailwindcss @tailwindcss/vite

// vite.config.js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
export default defineConfig({ plugins: [tailwindcss()] });

/* src/style.css */
@import "tailwindcss";

<!-- index.html -->
<button class="rounded-lg bg-emerald-600 px-4 py-2 font-semibold text-white hover:bg-emerald-700">
  Daftar sekarang
</button>''', lang='bash'),
      J('Kenapa CSS akhirnya kecil: hanya kelas yang dipakai', r'''
const html = `<div class="flex items-center gap-4 p-6">
  <img class="size-12 rounded-full">
  <h2 class="text-lg font-semibold text-slate-900">Rina</h2>
  <button class="ml-auto rounded-lg bg-emerald-600 px-4 py-2 text-white hover:bg-emerald-700">Ikuti</button>
</div>`;
const kelas = new Set(html.match(/class="([^"]+)"/g).flatMap((c) => c.slice(7, -1).split(/\s+/)));
const totalKelasTersedia = 22_000;           // perkiraan kombinasi utilitas bawaan
console.log(`${kelas.size} kelas dipakai dari ~${totalKelasTersedia.toLocaleString("id-ID")} yang mungkin:`);
console.log([...kelas].join(" "));
console.log(`Perkiraan CSS hasil: ~${(kelas.size * 70 / 1024).toFixed(1)} KB, bukan ~3 MB jika semua kelas dibuat`);
''')]),

'Jarak, ukuran, dan warna': dict(
  ist=[('Spacing scale', 'Satu unit = 0,25rem (4px): p-4 = 16px, mt-8 = 32px.'),
       ('size-*', 'Mengatur width dan height sekaligus: size-10.'),
       ('max-w-*', 'Membatasi lebar konten: max-w-prose (~65 karakter), max-w-screen-lg.'),
       ('Color palette 50-950', 'Skala warna dari terang ke gelap; v4 memakai ruang warna OKLCH.'),
       ('Opacity modifier', 'bg-black/50 untuk transparansi 50%.')],
  cx=[H('Kartu harga dengan skala spasi konsisten', r'''
<div class="mx-auto max-w-sm rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
  <p class="text-sm font-medium text-emerald-700">Paling populer</p>
  <h3 class="mt-2 text-2xl font-bold text-slate-900">Kelas Frontend</h3>
  <p class="mt-4 flex items-baseline gap-1">
    <span class="text-4xl font-extrabold">Rp499rb</span><span class="text-slate-500">/bulan</span>
  </p>
  <ul class="mt-6 space-y-3 text-slate-700">
    <li>✓ 120 video materi</li><li>✓ Review proyek mingguan</li><li>✓ Sertifikat</li>
  </ul>
  <a href="#" class="mt-8 block rounded-lg bg-emerald-600 px-4 py-3 text-center font-semibold text-white">Mulai belajar</a>
</div>'''),
      J('Tabel konversi spacing Tailwind', r'''
const kelas = [0.5, 1, 2, 3, 4, 5, 6, 8, 12, 16, 24];
console.log("kelas   rem      px");
for (const k of kelas) console.log(`p-${String(k).padEnd(4)} ${(k * 0.25).toString().padEnd(6)}rem ${String(k * 4).padStart(4)}px`);
const desain = [18, 20, 30];
for (const px of desain) {
  const terdekat = kelas.reduce((a, b) => (Math.abs(b * 4 - px) < Math.abs(a * 4 - px) ? b : a));
  console.log(`desain ${px}px -> pakai p-${terdekat} (${terdekat * 4}px)${terdekat * 4 === px ? "" : ` atau p-[${px}px] bila harus persis`}`);
}
''')]),

'Tipografi': dict(
  ist=[('Font size scale', 'text-xs sampai text-9xl; setiap ukuran sudah membawa line-height.'),
       ('font-weight', 'font-normal (400), font-semibold (600), font-bold (700).'),
       ('leading / tracking', 'Jarak baris (leading-relaxed) dan jarak huruf (tracking-wide).'),
       ('@tailwindcss/typography', 'Kelas prose untuk menata konten panjang dari Markdown/CMS.'),
       ('text-balance / text-pretty', 'Pemenggalan judul seimbang dan paragraf tanpa yatim.')],
  cx=[H('Artikel blog dengan prose dan judul responsif', r'''
<!-- @plugin "@tailwindcss/typography"; di style.css -->
<article class="mx-auto max-w-prose px-4 py-12">
  <p class="text-sm font-semibold uppercase tracking-wider text-emerald-700">Tutorial</p>
  <h1 class="mt-2 text-3xl font-extrabold leading-tight text-balance text-slate-900 sm:text-5xl">
    Membuat landing page responsif dengan Tailwind dalam satu sore
  </h1>
  <p class="mt-4 text-lg leading-relaxed text-pretty text-slate-600">Ringkasan artikel di sini.</p>
  <div class="prose prose-slate prose-a:text-emerald-700 mt-10 lg:prose-lg dark:prose-invert">
    <!-- HTML hasil Markdown dari CMS -->
  </div>
</article>'''),
      J('Skala tipografi modular untuk desain sistem', r'''
const dasar = 16, rasio = 1.25;   // major third
const nama = ["sm", "base", "lg", "xl", "2xl", "3xl", "4xl"];
nama.forEach((n, i) => {
  const px = dasar * rasio ** (i - 1);
  console.log(`text-${n.padEnd(5)} ${px.toFixed(1).padStart(5)}px  ${(px / 16).toFixed(3)}rem`);
});
console.log("(token kustom di @theme; bawaan Tailwind: sm 14px, base 16px, lg 18px, xl 20px, 2xl 24px)");
const karakterPerBaris = (lebarPx, ukuranPx) => Math.round(lebarPx / (ukuranPx * 0.5));
console.log("max-w-prose (65ch) di 16px ≈", karakterPerBaris(65 * 8, 16), "karakter per baris");
''')]),

'Flexbox dan Grid': dict(
  ist=[('flex / items-center / justify-between', 'Tata letak satu dimensi dan perataan.'),
       ('grid / grid-cols-* / gap-*', 'Tata letak dua dimensi dengan jarak konsisten.'),
       ('col-span-* / row-span-*', 'Elemen yang mengambil beberapa kolom atau baris.'),
       ('grid-cols-[repeat(auto-fill,minmax(14rem,1fr))]', 'Grid otomatis tanpa media query lewat arbitrary value.'),
       ('Subgrid', 'grid-rows-subgrid agar isi kartu sejajar antar-kartu.')],
  cx=[H('Navbar flex dan galeri grid bento', r'''
<header class="flex items-center justify-between gap-4 border-b px-6 py-4">
  <a href="/" class="text-xl font-black">RuangKopi</a>
  <nav class="hidden gap-6 md:flex"><a href="#menu">Menu</a><a href="#lokasi">Lokasi</a></nav>
  <a href="#pesan" class="rounded-full bg-amber-700 px-4 py-2 text-white">Pesan</a>
</header>

<section class="grid auto-rows-[12rem] grid-cols-2 gap-4 p-6 md:grid-cols-4">
  <div class="col-span-2 row-span-2 rounded-2xl bg-amber-100">Menu andalan</div>
  <div class="rounded-2xl bg-stone-200">Espresso</div>
  <div class="rounded-2xl bg-stone-200">V60</div>
  <div class="col-span-2 rounded-2xl bg-emerald-100">Promo pagi</div>
</section>

<ul class="grid grid-cols-[repeat(auto-fill,minmax(14rem,1fr))] gap-6">
  <li class="grid grid-rows-subgrid row-span-3 rounded-xl border p-4">
    <img class="aspect-square rounded-lg object-cover" src="..." alt="...">
    <h3>Nama produk yang bisa panjang sekali</h3>
    <p class="self-end font-bold">Rp45.000</p>
  </li>
</ul>''')]),

'Desain responsif': dict(
  ist=[('Mobile-first', 'Kelas tanpa prefiks berlaku di semua ukuran; sm: md: lg: menimpa di layar lebih lebar.'),
       ('Breakpoint', 'sm 40rem (640px), md 48rem (768px), lg 64rem (1024px), xl 80rem, 2xl 96rem.'),
       ('Container query', '@container dan @md: menyesuaikan dengan lebar induk, bukan layar.'),
       ('max-* variant', 'max-md:hidden untuk gaya yang hanya berlaku di bawah breakpoint.')],
  cx=[H('Hero dua kolom yang menumpuk di ponsel', r'''
<section class="mx-auto grid max-w-6xl items-center gap-10 px-4 py-12 md:grid-cols-2 md:py-24">
  <div class="order-2 md:order-1">
    <h1 class="text-3xl font-extrabold sm:text-4xl lg:text-6xl">Belajar coding dari nol sampai kerja</h1>
    <p class="mt-4 text-slate-600 md:text-lg">Kurikulum industri, mentor praktisi.</p>
    <div class="mt-8 flex flex-col gap-3 sm:flex-row">
      <a class="rounded-lg bg-emerald-600 px-6 py-3 text-center text-white">Mulai gratis</a>
      <a class="rounded-lg border px-6 py-3 text-center">Lihat kurikulum</a>
    </div>
  </div>
  <img class="order-1 w-full rounded-3xl md:order-2" src="hero.webp" alt="Siswa belajar" width="800" height="600">
</section>

<!-- Container query: kartu menyesuaikan lebar kolom tempat ia berada -->
<div class="@container">
  <article class="flex flex-col gap-4 @md:flex-row">...</article>
</div>'''),
      J('Kelas mana yang aktif di tiap lebar layar', r'''
const bp = { sm: 640, md: 768, lg: 1024, xl: 1280 };
const kelas = "text-3xl sm:text-4xl lg:text-6xl grid-cols-1 md:grid-cols-2 xl:grid-cols-3".split(" ");
function aktif(lebar) {
  const hasil = {};
  for (const k of kelas) {
    const [pref, util] = k.includes(":") ? k.split(":") : [null, k];
    if (pref && lebar < bp[pref]) continue;
    hasil[util.replace(/-\w+$/, "")] = util;             // yang belakangan menimpa
  }
  return Object.values(hasil).join(" ");
}
for (const w of [360, 640, 800, 1100, 1440]) console.log(`${String(w).padStart(4)}px -> ${aktif(w)}`);
''')]),

'Hover, focus, dan mode gelap': dict(
  ist=[('State variant', 'hover:, focus-visible:, active:, disabled:, aria-*: untuk gaya per keadaan.'),
       ('group / peer', 'Gaya anak berdasarkan hover induk (group-hover:) atau keadaan saudara (peer-invalid:).'),
       ('dark:', 'Gaya mode gelap; default mengikuti prefers-color-scheme.'),
       ('@custom-variant dark', 'Tailwind v4: mengubah dark: agar mengikuti kelas .dark atau data-theme.'),
       ('focus-visible', 'Cincin fokus hanya untuk pengguna keyboard; jangan hapus outline tanpa pengganti.')],
  cx=[H('Kartu interaktif, input dengan peer, dan tema gelap', r'''
/* style.css: dark mode via atribut data-theme */
@import "tailwindcss";
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));

<a href="/kelas/react" class="group block rounded-2xl border bg-white p-6 transition hover:-translate-y-1 hover:shadow-lg
   focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-600
   dark:border-slate-700 dark:bg-slate-900">
  <h3 class="font-bold text-slate-900 group-hover:text-emerald-700 dark:text-white">React untuk Pemula</h3>
  <span class="text-sm text-slate-500 group-hover:underline">Lihat silabus →</span>
</a>

<label class="block">
  <input type="email" required placeholder=" " class="peer w-full rounded-lg border px-3 py-2 invalid:[&:not(:placeholder-shown)]:border-red-500">
  <span class="mt-1 hidden text-sm text-red-600 peer-[&:invalid:not(:placeholder-shown)]:block">Format email belum benar</span>
</label>

<button aria-pressed="false" class="rounded-lg px-3 py-2 aria-pressed:bg-emerald-600 aria-pressed:text-white disabled:opacity-50">Filter</button>'''),
      J('Memeriksa kontras pasangan warna terang dan gelap', r'''
const hex = { "slate-900": "#0f172a", "slate-500": "#64748b", "slate-400": "#94a3b8", white: "#ffffff", "emerald-600": "#059669", "emerald-400": "#34d399" };
const L = (h) => { const [r, g, b] = h.match(/\w\w/g).map((x) => parseInt(x, 16) / 255).map((c) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4)); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const kontras = (a, b) => { const [x, y] = [L(hex[a]), L(hex[b])].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
const pasangan = [["slate-900", "white", "judul, terang"], ["slate-500", "white", "teks sekunder, terang"], ["slate-400", "slate-900", "teks sekunder, gelap"], ["emerald-600", "white", "tautan, terang"], ["emerald-400", "slate-900", "tautan, gelap"]];
for (const [fg, bg, ket] of pasangan) {
  const k = kontras(fg, bg);
  console.log(`text-${fg.padEnd(12)} di bg-${bg.padEnd(10)} ${k.toFixed(2).padStart(5)}:1  ${k >= 4.5 ? "AA" : k >= 3 ? "hanya teks besar" : "GAGAL"}  (${ket})`);
}
''')]),

'Form yang rapi': dict(
  ist=[('@tailwindcss/forms', 'Plugin yang menormalkan tampilan input, select, checkbox antar browser.'),
       ('accent-*', 'Warna checkbox, radio, dan range bawaan browser.'),
       ('Label + helper + error', 'Tiga teks wajib di setiap field form profesional.'),
       ('Touch target', 'Tinggi input minimal 44px (h-11) agar nyaman disentuh di ponsel.')],
  cx=[H('Form pendaftaran yang rapi dan aksesibel', r'''
<form class="mx-auto max-w-md space-y-5 rounded-2xl bg-white p-6 shadow">
  <div>
    <label for="nama" class="block text-sm font-medium text-slate-700">Nama lengkap</label>
    <input id="nama" name="nama" autocomplete="name" required
           class="mt-1 h-11 w-full rounded-lg border-slate-300 px-3 focus:border-emerald-600 focus:ring-emerald-600">
  </div>
  <div>
    <label for="hp" class="block text-sm font-medium text-slate-700">Nomor WhatsApp</label>
    <input id="hp" name="hp" type="tel" inputmode="tel" aria-describedby="hp-bantu hp-error" aria-invalid="true"
           class="mt-1 h-11 w-full rounded-lg border-red-500 px-3 aria-invalid:ring-1 aria-invalid:ring-red-500">
    <p id="hp-bantu" class="mt-1 text-xs text-slate-500">Contoh: 081234567890</p>
    <p id="hp-error" class="mt-1 text-sm text-red-600">Nomor harus diawali 08 atau +628</p>
  </div>
  <fieldset>
    <legend class="text-sm font-medium text-slate-700">Jadwal kelas</legend>
    <div class="mt-2 grid grid-cols-2 gap-3">
      <label class="flex items-center gap-2 rounded-lg border p-3 has-[:checked]:border-emerald-600 has-[:checked]:bg-emerald-50">
        <input type="radio" name="jadwal" value="pagi" class="accent-emerald-600"> Pagi
      </label>
      <label class="flex items-center gap-2 rounded-lg border p-3 has-[:checked]:border-emerald-600 has-[:checked]:bg-emerald-50">
        <input type="radio" name="jadwal" value="malam" class="accent-emerald-600"> Malam
      </label>
    </div>
  </fieldset>
  <button class="h-11 w-full rounded-lg bg-emerald-600 font-semibold text-white hover:bg-emerald-700 disabled:opacity-50">Daftar</button>
</form>''')]),

'Komponen dan @apply': dict(
  ist=[('Component extraction', 'Cara utama menghindari pengulangan kelas: jadikan komponen (React/Vue/Blade), bukan @apply.'),
       ('@apply', 'Menggabungkan utilitas ke kelas CSS sendiri; pakai hemat untuk elemen yang tidak bisa dijadikan komponen.'),
       ('@layer components', 'Tempat kelas komponen kustom agar urutan prioritas benar.'),
       ('tailwind-merge', 'Menggabungkan kelas tanpa konflik (p-2 + p-4 menjadi p-4).'),
       ('Prettier plugin', 'prettier-plugin-tailwindcss mengurutkan kelas otomatis.')],
  cx=[H('Kapan @apply dan kapan komponen', r'''
/* style.css: cocok untuk konten dari CMS yang tidak bisa diberi kelas satu per satu */
@layer components {
  .btn { @apply inline-flex h-11 items-center gap-2 rounded-lg px-4 font-semibold transition; }
  .btn-utama { @apply bg-emerald-600 text-white hover:bg-emerald-700; }
  .konten-cms a { @apply text-emerald-700 underline underline-offset-2; }
}

// Tombol.tsx: cara yang lebih disukai di proyek berbasis komponen
import { twMerge } from "tailwind-merge";
export function Tombol({ className, ...p }) {
  return <button className={twMerge("h-11 rounded-lg bg-emerald-600 px-4 font-semibold text-white", className)} {...p} />;
}
<Tombol className="px-8 bg-rose-600">Hapus</Tombol>   // px-8 & bg-rose-600 menimpa tanpa konflik''', lang='css'),
      J('Cara tailwind-merge menyelesaikan konflik kelas', r'''
const grup = [
  [/^p-/, "padding"], [/^px-/, "padding-x"], [/^py-/, "padding-y"], [/^bg-/, "bg"],
  [/^text-(xs|sm|base|lg|xl|\dxl)$/, "font-size"], [/^text-/, "text-color"], [/^rounded/, "radius"], [/^h-/, "height"],
];
function twMerge(...daftar) {
  const hasil = new Map();
  for (const k of daftar.join(" ").split(/\s+/).filter(Boolean)) {
    const [, nama] = grup.find(([re]) => re.test(k.replace(/^\w+:/, ""))) ?? [null, k];
    const varian = k.includes(":") ? k.split(":")[0] + ":" : "";
    hasil.delete(varian + nama); hasil.set(varian + nama, k);
  }
  return [...hasil.values()].join(" ");
}
const dasar = "h-11 rounded-lg bg-emerald-600 px-4 text-sm text-white hover:bg-emerald-700";
console.log(twMerge(dasar, "bg-rose-600 px-8 text-lg hover:bg-rose-700"));
''')]),

'Tema dan konfigurasi': dict(
  ist=[('@theme', 'Tailwind v4: mendefinisikan design token sebagai variabel CSS yang otomatis menjadi utilitas.'),
       ('Design token', 'Nilai bernama (warna merek, font, radius) yang dipakai konsisten di seluruh produk.'),
       ('CSS variables at runtime', 'Token v4 tersedia sebagai var(--color-merek-500) untuk JavaScript atau tema dinamis.'),
       ('tailwind.config.js (v3)', 'Cara lama mengatur tema; v4 memindahkannya ke CSS.')],
  cx=[H('Token merek dengan @theme', r'''
/* style.css (Tailwind v4) */
@import "tailwindcss";

@theme {
  --font-sans: "Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
  --color-merek-50:  oklch(0.97 0.02 165);
  --color-merek-500: oklch(0.65 0.15 165);
  --color-merek-700: oklch(0.48 0.12 165);
  --radius-kartu: 1.25rem;
  --breakpoint-3xl: 120rem;
  --animate-muncul: muncul 0.3s ease-out;
  @keyframes muncul { from { opacity: 0; translate: 0 8px; } }
}

/* Hasilnya langsung tersedia: */
<div class="rounded-kartu bg-merek-50 font-sans text-merek-700 animate-muncul 3xl:p-12">...</div>

/* Tema per pelanggan (white-label) cukup menimpa variabel */
[data-brand="kopi"] { --color-merek-500: oklch(0.55 0.12 50); }''', lang='css'),
      J('Membuat skala warna 50-900 dari satu warna merek', r'''
// skala lightness OKLCH yang mendekati palet bawaan Tailwind
const langkah = { 50: 0.97, 100: 0.94, 200: 0.88, 300: 0.8, 400: 0.71, 500: 0.62, 600: 0.53, 700: 0.45, 800: 0.38, 900: 0.31 };
const chroma = (l) => +(0.16 * Math.sin(Math.PI * Math.min(1, (1 - l) / 0.75))).toFixed(3);
const hue = 165;   // hijau tosca merek
for (const [k, l] of Object.entries(langkah))
  console.log(`--color-merek-${k.padEnd(3)}: oklch(${l} ${chroma(l)} ${hue});`);
''')]),

'Proyek: landing page responsif': dict(
  ist=[('Landing page', 'Halaman tunggal untuk satu tujuan konversi (daftar, beli, unduh).'),
       ('Above the fold', 'Bagian yang terlihat tanpa scroll: judul, nilai utama, CTA.'),
       ('Social proof', 'Testimoni, logo klien, jumlah pengguna untuk membangun kepercayaan.'),
       ('Conversion rate', 'Persentase pengunjung yang melakukan aksi tujuan.')],
  cx=[H('Kerangka landing page kursus', r'''
<body class="bg-white text-slate-800 antialiased dark:bg-slate-950 dark:text-slate-200">
  <header class="sticky top-0 z-40 border-b bg-white/80 backdrop-blur dark:bg-slate-950/80">...</header>
  <main>
    <section class="mx-auto max-w-6xl px-4 py-16 text-center md:py-28">
      <p class="mx-auto w-fit rounded-full bg-emerald-50 px-3 py-1 text-sm text-emerald-700">Angkatan Januari 2027 dibuka</p>
      <h1 class="mt-6 text-4xl font-extrabold text-balance md:text-6xl">Jadi Frontend Developer dalam 16 minggu</h1>
      <p class="mx-auto mt-4 max-w-2xl text-lg text-slate-600">Belajar HTML sampai React dengan proyek nyata dan mentor praktisi.</p>
      <a href="#daftar" class="mt-8 inline-flex h-12 items-center rounded-lg bg-emerald-600 px-8 font-semibold text-white">Daftar sekarang</a>
    </section>
    <section aria-label="Dipercaya oleh" class="flex flex-wrap justify-center gap-8 opacity-70 grayscale">...</section>
    <section id="fitur" class="mx-auto grid max-w-6xl gap-6 px-4 py-16 sm:grid-cols-2 lg:grid-cols-3">...</section>
    <section id="testimoni" class="bg-slate-50 py-16 dark:bg-slate-900">...</section>
    <section id="harga" class="mx-auto grid max-w-5xl gap-6 px-4 py-16 md:grid-cols-3">...</section>
    <section id="faq" class="mx-auto max-w-3xl px-4 py-16"><details class="group border-b py-4">...</details></section>
  </main>
  <footer class="border-t py-10 text-center text-sm text-slate-500">© 2026 RuangKode</footer>
</body>'''),
      J('Menghitung konversi dan dampak perbaikan', r'''
const funnel = [["Kunjungan", 12_400], ["Scroll ke harga", 5_580], ["Klik daftar", 1_240], ["Bayar", 186]];
funnel.forEach(([n, v], i) => {
  const dariSebelum = i ? ((v / funnel[i - 1][1]) * 100).toFixed(1) + "%" : "";
  console.log(`${n.padEnd(16)} ${v.toLocaleString("id-ID").padStart(7)}  ${dariSebelum.padStart(6)}`);
});
const konversi = funnel.at(-1)[1] / funnel[0][1];
console.log(`Conversion rate: ${(konversi * 100).toFixed(2)}%`);
const naik = 0.2;   // misal hero baru menaikkan klik daftar 20%
console.log(`Jika klik daftar naik ${naik * 100}%: ~${Math.round(funnel.at(-1)[1] * (1 + naik))} pembayaran (+${Math.round(funnel.at(-1)[1] * naik)} siswa)`);
''')]),

'Posisi, z-index, dan overflow': dict(
  ist=[('relative / absolute / fixed / sticky', 'Mode posisi; absolute mengacu ke induk relative terdekat.'),
       ('inset-* / top-* / right-*', 'Utilitas jarak posisi; inset-0 menutupi seluruh induk.'),
       ('z-index scale', 'z-10 sampai z-50; tetapkan skala lapisan tim (dropdown < sticky < modal < toast).'),
       ('Stacking context', 'Lapisan baru dibuat oleh transform, opacity < 1, isolation; sering penyebab z-index "tidak jalan".'),
       ('overflow-x-auto', 'Wadah scroll untuk tabel lebar agar halaman tidak melebar.')],
  cx=[H('Badge, header sticky, dan tabel yang bisa digulir', r'''
<div class="relative w-fit">
  <img src="keranjang.svg" class="size-8" alt="Keranjang">
  <span class="absolute -right-2 -top-2 grid size-5 place-items-center rounded-full bg-rose-600 text-xs text-white">3</span>
</div>

<header class="sticky top-0 z-30 bg-white/90 backdrop-blur">...</header>

<div class="relative isolate">
  <img src="hero.webp" class="absolute inset-0 -z-10 size-full object-cover" alt="">
  <div class="absolute inset-0 -z-10 bg-gradient-to-t from-black/70"></div>
  <h1 class="p-8 text-white">Teks di atas gambar</h1>
</div>

<div class="overflow-x-auto rounded-lg border">
  <table class="min-w-[640px] w-full text-left text-sm">...</table>
</div>''')]),

'Transform, transisi, dan animasi': dict(
  ist=[('transition / duration / ease', 'Animasi perubahan properti saat hover/focus; 150-300 ms untuk UI.'),
       ('transform utilities', 'scale-*, rotate-*, translate-*; murah karena tidak memicu layout.'),
       ('animate-*', 'animate-spin, animate-pulse (skeleton), animate-bounce, atau animasi kustom.'),
       ('motion-safe / motion-reduce', 'Hormati pengguna yang mematikan animasi di sistem operasi.'),
       ('starting:', 'Varian v4 untuk animasi saat elemen pertama kali muncul (@starting-style).')],
  cx=[H('Kartu hover, skeleton, dan animasi masuk', r'''
<article class="rounded-2xl border p-6 transition duration-200 ease-out motion-safe:hover:-translate-y-1 motion-safe:hover:shadow-xl">...</article>

<!-- Skeleton loading -->
<div class="space-y-3" aria-busy="true">
  <div class="h-40 rounded-xl bg-slate-200 motion-safe:animate-pulse"></div>
  <div class="h-4 w-3/4 rounded bg-slate-200 motion-safe:animate-pulse"></div>
</div>

<!-- Toast yang meluncur masuk (Tailwind v4) -->
<div popover id="toast" class="translate-y-0 opacity-100 transition-all duration-300 starting:translate-y-4 starting:opacity-0">
  Tersimpan ✓
</div>'''),
      J('Kurva easing: kenapa ease-out terasa responsif', r'''
const bezier = (p1, p2) => (t) => { const u = 1 - t; return 3 * u * u * t * p1 + 3 * u * t * t * p2 + t ** 3; };
const kurva = { linear: (t) => t, "ease-in": bezier(0, 0.4), "ease-out": bezier(0.6, 1), "ease-in-out": bezier(0, 1) };
console.log("progres pada 50ms dari durasi 200ms (25% waktu):");
for (const [n, f] of Object.entries(kurva)) console.log(`  ${n.padEnd(12)} ${(f(0.25) * 100).toFixed(0).padStart(3)}%  ${"█".repeat(Math.round(f(0.25) * 30))}`);
''', 'ease-out bergerak cepat di awal sehingga pengguna langsung melihat respons, cocok untuk elemen yang muncul. ease-in cocok untuk elemen yang keluar.')]),

'Menu ponsel dengan sedikit JavaScript': dict(
  ist=[('Hamburger menu', 'Tombol yang membuka navigasi di layar kecil.'),
       ('aria-expanded / aria-controls', 'Memberi tahu pembaca layar status menu.'),
       ('Escape & focus management', 'Esc menutup menu, fokus kembali ke tombol.'),
       ('Popover API', 'Atribut popover HTML untuk menu/tooltip tanpa JavaScript.')],
  cx=[H('Navbar responsif dengan JavaScript minimal', r'''
<header class="flex items-center justify-between px-4 py-3">
  <a href="/" class="font-black">RuangKode</a>
  <button id="tombol-menu" aria-expanded="false" aria-controls="menu" class="md:hidden size-11 grid place-items-center rounded-lg">
    <span class="sr-only">Buka menu</span>☰
  </button>
  <nav id="menu" class="absolute inset-x-0 top-full hidden flex-col gap-1 bg-white p-4 shadow-lg data-[buka=true]:flex
                         md:static md:flex md:flex-row md:gap-6 md:p-0 md:shadow-none">
    <a href="#kelas" class="rounded-lg p-3 hover:bg-slate-100 md:p-0">Kelas</a>
    <a href="#harga" class="rounded-lg p-3 hover:bg-slate-100 md:p-0">Harga</a>
  </nav>
</header>
<script>
  const t = document.querySelector("#tombol-menu"), m = document.querySelector("#menu");
  const atur = (buka) => { m.dataset.buka = buka; t.setAttribute("aria-expanded", buka); if (!buka) t.focus(); };
  t.addEventListener("click", () => atur(m.dataset.buka !== "true"));
  document.addEventListener("keydown", (e) => e.key === "Escape" && m.dataset.buka === "true" && atur(false));
  m.addEventListener("click", (e) => e.target.closest("a") && atur(false));
</script>'''),
      J('State machine menu diuji di Node', r'''
function buatMenu() {
  const s = { buka: false, fokus: "body", log: [] };
  const atur = (b, alasan) => { s.buka = b; if (!b) s.fokus = "tombol-menu"; s.log.push(`${alasan.padEnd(14)} -> ${b ? "terbuka" : "tertutup"}, aria-expanded=${b}, fokus=${s.fokus}`); };
  return {
    s,
    klikTombol: () => atur(!s.buka, "klik tombol"),
    tekan: (k) => k === "Escape" && s.buka && atur(false, "tekan Escape"),
    klikTautan: () => s.buka && atur(false, "klik tautan"),
  };
}
const m = buatMenu();
m.klikTombol(); m.tekan("Escape"); m.klikTombol(); m.klikTautan(); m.tekan("Escape");
console.log(m.s.log.join("\n"));
''')]),

'Tailwind v4: apa yang baru dan cara migrasi': dict(
  ist=[('CSS-first configuration', 'Konfigurasi pindah dari tailwind.config.js ke @theme di CSS.'),
       ('Oxide engine', 'Mesin baru berbasis Rust; build penuh hingga 5x dan incremental 100x lebih cepat.'),
       ('Automatic content detection', 'Tidak perlu lagi daftar content: [...].'),
       ('@tailwindcss/upgrade', 'Alat resmi untuk migrasi otomatis dari v3.'),
       ('Modern CSS', 'Memakai cascade layers, @property, color-mix(), dan OKLCH; butuh Safari 16.4+, Chrome 111+.')],
  cx=[H('Perbandingan v3 dan v4', r'''
/* ===== v3 ===== */
// tailwind.config.js
module.exports = {
  content: ["./src/**/*.{html,js,tsx}"],
  darkMode: "class",
  theme: { extend: { colors: { merek: "#0f766e" } } },
  plugins: [require("@tailwindcss/forms")],
};
/* style.css */
@tailwind base; @tailwind components; @tailwind utilities;

/* ===== v4 ===== */
/* style.css (tanpa tailwind.config.js) */
@import "tailwindcss";
@plugin "@tailwindcss/forms";
@custom-variant dark (&:where(.dark, .dark *));
@theme { --color-merek: #0f766e; }

# Migrasi otomatis
npx @tailwindcss/upgrade

# Perubahan nama kelas yang perlu dicek
shadow-sm -> shadow-xs, shadow -> shadow-sm
rounded-sm -> rounded-xs, rounded -> rounded-sm
outline-none -> outline-hidden, ring -> ring-3
bg-opacity-50 -> bg-black/50''', lang='css'),
      J('Skrip migrasi nama kelas sederhana', r'''
const peta = { "shadow-sm": "shadow-xs", shadow: "shadow-sm", "rounded-sm": "rounded-xs", rounded: "rounded-sm", "outline-none": "outline-hidden", ring: "ring-3", "flex-grow": "grow", "flex-shrink-0": "shrink-0" };
const html = `<button class="rounded shadow ring flex-shrink-0 outline-none hover:shadow-sm">Kirim</button>
<div class="rounded-sm shadow-sm bg-black bg-opacity-50 flex-grow">...</div>`;
let jumlah = 0;
const baru = html.replace(/class="([^"]+)"/g, (_, k) => 'class="' + k.split(/\s+/).map((c) => {
  const [v, u] = c.includes(":") ? c.split(":") : ["", c];
  if (peta[u]) { jumlah++; return (v ? v + ":" : "") + peta[u]; }
  return c;
}).join(" ") + '"');
console.log(baru);
console.log(`${jumlah} kelas diganti; bg-opacity-50 perlu diubah manual menjadi bg-black/50`);
''')]),
}
