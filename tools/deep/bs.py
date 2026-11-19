"""Pendalaman jalur Bootstrap 5: istilah dunia kerja, markup siap pakai, dan perhitungan yang dijalankan dengan Node."""
K = 'bs'


def H(t, code, b=None, lang='html'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def J(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='js')


D = {
'Memasang Bootstrap 5': dict(
  ist=[('CDN', 'Memuat CSS/JS dari jsDelivr; cepat untuk prototipe.'),
       ('npm + bundler', 'Cara produksi: npm i bootstrap, impor Sass dan hanya JS yang diperlukan.'),
       ('bootstrap.bundle.js', 'Berisi Popper.js untuk dropdown, tooltip, dan popover.'),
       ('SRI (integrity)', 'Hash yang memastikan file dari CDN tidak diubah pihak lain.'),
       ('Bootstrap Icons', 'Pustaka 2.000+ ikon SVG resmi.')],
  cx=[H('Templat awal dengan CDN', r'''
<!doctype html>
<html lang="id" data-bs-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kursus Coding</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
</head>
<body>
  <main class="container py-5">
    <h1 class="display-5 fw-bold">Halo, Bootstrap!</h1>
    <button class="btn btn-primary"><i class="bi bi-rocket-takeoff"></i> Mulai</button>
  </main>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>'''),
      H('Instalasi produksi dengan Vite dan Sass', r'''
npm i bootstrap @popperjs/core && npm i -D sass

// src/main.js: impor hanya komponen JS yang dipakai
import "./style.scss";
import Modal from "bootstrap/js/dist/modal";
import Collapse from "bootstrap/js/dist/collapse";

// src/style.scss: impor hanya bagian Sass yang dipakai
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/maps";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/root";
@import "bootstrap/scss/reboot";
@import "bootstrap/scss/grid";
@import "bootstrap/scss/buttons";
@import "bootstrap/scss/utilities/api";''', lang='bash'),
      J('Membuat hash SRI untuk file sendiri', r'''
import { createHash } from "node:crypto";
const isi = "/* app.css */ .kartu{border-radius:12px}";
const sri = "sha384-" + createHash("sha384").update(isi).digest("base64");
console.log(`<link rel="stylesheet" href="https://cdn.contoh.id/app.css" integrity="${sri}" crossorigin="anonymous">`);
const diubah = isi.replace("12px", "0");
console.log("file diubah penyerang -> hash cocok?", sri === "sha384-" + createHash("sha384").update(diubah).digest("base64"), "(browser menolak memuat)");
''')]),

'Sistem grid 12 kolom': dict(
  ist=[('container / container-fluid', 'Pembungkus dengan lebar maksimum per breakpoint atau penuh.'),
       ('row & col', 'Baris flex berisi kolom; total 12 bagian per baris.'),
       ('Breakpoint', 'sm 576, md 768, lg 992, xl 1200, xxl 1400 px.'),
       ('Gutter (g-*)', 'Jarak antar kolom: g-0 sampai g-5, gx-* dan gy-*.'),
       ('row-cols-*', 'Menentukan jumlah kolom per baris tanpa menulis col-* di setiap anak.')],
  cx=[H('Tata letak blog dan galeri kartu', r'''
<div class="container py-4">
  <div class="row g-4">
    <main class="col-lg-8">Artikel</main>
    <aside class="col-lg-4">Sidebar</aside>             <!-- menumpuk di bawah lg -->
  </div>

  <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-3 mt-2">
    <div class="col"><div class="card h-100">...</div></div>
    <div class="col"><div class="card h-100">...</div></div>
    <div class="col"><div class="card h-100">...</div></div>
    <div class="col"><div class="card h-100">...</div></div>
  </div>

  <div class="row">
    <div class="col-md-6 offset-md-3 text-center">Konten di tengah</div>
    <div class="col-6 col-md-4 order-md-2">A</div>
    <div class="col-6 col-md-8 order-md-1">B</div>
  </div>
</div>'''),
      J('Menghitung lebar kolom di setiap breakpoint', r'''
const container = { xs: null, sm: 540, md: 720, lg: 960, xl: 1140, xxl: 1320 };
const bp = { xs: 0, sm: 576, md: 768, lg: 992, xl: 1200, xxl: 1400 };
const gutter = 24;
function lebarKolom(layar, kelas) {
  const aktif = Object.keys(bp).filter((k) => layar >= bp[k]).at(-1);
  const wadah = container[aktif] ?? layar;
  let span = 12;
  for (const k of Object.keys(bp)) {
    if (layar < bp[k]) break;
    const m = kelas.match(new RegExp(`col-${k === "xs" ? "" : k + "-"}(\\d+)`));
    if (m) span = +m[1];
  }
  return { aktif, wadah, span, px: Math.round((wadah * span) / 12 - gutter) };
}
for (const w of [375, 800, 1024, 1440]) {
  const a = lebarKolom(w, "col-12 col-md-6 col-lg-4"), b = lebarKolom(w, "col-12 col-lg-8");
  console.log(`${String(w).padStart(4)}px [${a.aktif.padEnd(3)}] wadah ${String(a.wadah).padStart(4)} | kartu col-${a.span} ~${a.px}px | artikel col-${b.span} ~${b.px}px`);
}
''')]),

'Utilitas, tipografi, dan warna': dict(
  ist=[('Spacing utility', 'm/p + sisi (t, b, s, e, x, y) + ukuran 0-5: mt-3, px-4, mx-auto.'),
       ('Display & flex utility', 'd-none d-md-block, d-flex justify-content-between align-items-center.'),
       ('Typography', 'display-1 sampai 6, lead, fw-bold, text-truncate, text-body-secondary.'),
       ('Theme colors', 'primary, secondary, success, danger, warning, info, light, dark.'),
       ('Subtle & emphasis', 'bg-success-subtle, text-success-emphasis (5.3) untuk latar lembut.')],
  cx=[H('Header bagian dengan utilitas', r'''
<section class="py-5 bg-body-tertiary">
  <div class="container">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 mb-4">
      <div>
        <span class="badge rounded-pill bg-success-subtle text-success-emphasis">Baru</span>
        <h2 class="fw-bold mt-2 mb-1">Kelas Data Analyst</h2>
        <p class="lead text-body-secondary mb-0">SQL, Excel, Python, dan dashboard.</p>
      </div>
      <a href="#" class="btn btn-outline-primary px-4">Lihat semua <i class="bi bi-arrow-right"></i></a>
    </div>
    <p class="text-truncate" style="max-width: 320px">Judul sangat panjang yang akan dipotong dengan elipsis bila tidak muat</p>
    <p class="small text-uppercase fw-semibold text-primary">Label kecil</p>
  </div>
</section>'''),
      J('Arti nilai spacing Bootstrap', r'''
const spacer = 16;   // $spacer = 1rem
const skala = { 0: 0, 1: 0.25, 2: 0.5, 3: 1, 4: 1.5, 5: 3 };
for (const [k, f] of Object.entries(skala)) console.log(`m-${k} / p-${k} = ${String(f).padEnd(4)}rem = ${spacer * f}px`);
const kelas = "mt-3 px-4 mb-md-5 mx-auto";
const arti = { m: "margin", p: "padding" }, sisi = { t: "-top", b: "-bottom", s: "-left (start)", e: "-right (end)", x: " kiri & kanan", y: " atas & bawah", "": "" };
for (const c of kelas.split(" ")) {
  const [, prop, s, bp, n] = c.match(/^([mp])([tbsexy]?)-(?:(sm|md|lg|xl|xxl)-)?(\d|auto)$/);
  console.log(`${c.padEnd(10)} -> ${arti[prop]}${sisi[s]} = ${n === "auto" ? "auto" : spacer * skala[n] + "px"}${bp ? ` mulai layar ${bp}` : ""}`);
}
''')]),

'Tombol, kartu, alert, dan badge': dict(
  ist=[('btn varian', 'btn-primary, btn-outline-*, btn-link; ukuran btn-sm/btn-lg.'),
       ('card', 'Wadah dengan card-header, card-body, card-footer, card-img-top.'),
       ('alert', 'Pesan kontekstual; alert-dismissible untuk tombol tutup.'),
       ('badge', 'Label kecil untuk status atau jumlah.'),
       ('stretched-link', 'Membuat seluruh kartu dapat diklik lewat satu tautan.')],
  cx=[H('Kartu kursus lengkap', r'''
<div class="card h-100 shadow-sm position-relative">
  <img src="react.webp" class="card-img-top" alt="Kelas React" width="400" height="225">
  <div class="card-body">
    <div class="d-flex gap-2 mb-2">
      <span class="badge text-bg-primary">Frontend</span>
      <span class="badge text-bg-warning">Terlaris</span>
    </div>
    <h5 class="card-title"><a href="/kelas/react" class="stretched-link text-decoration-none text-reset">React dari Nol</a></h5>
    <p class="card-text text-body-secondary">24 materi · 18 jam · proyek toko online</p>
  </div>
  <div class="card-footer bg-transparent d-flex justify-content-between align-items-center">
    <span><del class="text-body-secondary small">Rp599.000</del> <strong>Rp399.000</strong></span>
    <span class="text-warning">★ 4,8</span>
  </div>
</div>

<div class="alert alert-success alert-dismissible fade show d-flex gap-2" role="alert">
  <i class="bi bi-check-circle-fill"></i>
  <div>Pembayaran diterima. Akses kelas sudah aktif.</div>
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Tutup"></button>
</div>

<button class="btn btn-primary" disabled>
  <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
  <span role="status">Memproses...</span>
</button>'''),
      J('Menghitung persentase diskon untuk badge', r'''
const kelas = [["React dari Nol", 599000, 399000], ["Python Data", 450000, 450000], ["UI/UX Figma", 750000, 299000]];
for (const [nama, normal, promo] of kelas) {
  const pct = Math.round((1 - promo / normal) * 100);
  const badge = pct >= 50 ? "text-bg-danger" : pct > 0 ? "text-bg-warning" : null;
  console.log(`${nama.padEnd(16)} Rp${promo.toLocaleString("id-ID").padStart(7)}  ${badge ? `<span class="badge ${badge}">-${pct}%</span>` : "(tanpa badge)"}`);
}
''')]),

'Navbar yang bisa dilipat': dict(
  ist=[('navbar-expand-*', 'Breakpoint saat navbar berubah dari menu lipat menjadi horizontal.'),
       ('navbar-toggler', 'Tombol hamburger yang membuka collapse.'),
       ('collapse', 'Komponen JS untuk menampilkan/menyembunyikan konten.'),
       ('sticky-top / fixed-top', 'Navbar tetap terlihat saat scroll.'),
       ('aria-current="page"', 'Menandai tautan halaman aktif untuk pembaca layar.')],
  cx=[H('Navbar responsif dengan pencarian', r'''
<nav class="navbar navbar-expand-lg bg-body-tertiary sticky-top border-bottom">
  <div class="container">
    <a class="navbar-brand fw-bold" href="/"><i class="bi bi-code-slash"></i> RuangKode</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navUtama"
            aria-controls="navUtama" aria-expanded="false" aria-label="Buka navigasi">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navUtama">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item"><a class="nav-link active" aria-current="page" href="/">Beranda</a></li>
        <li class="nav-item"><a class="nav-link" href="/kelas">Kelas</a></li>
        <li class="nav-item"><a class="nav-link" href="/harga">Harga</a></li>
      </ul>
      <form class="d-flex gap-2" role="search">
        <input class="form-control" type="search" placeholder="Cari kelas" aria-label="Cari kelas">
        <button class="btn btn-outline-success" type="submit">Cari</button>
      </form>
    </div>
  </div>
</nav>''')]),

'Form dan validasi': dict(
  ist=[('form-control / form-select', 'Gaya input dan dropdown standar.'),
       ('form-floating', 'Label mengambang di dalam input.'),
       ('Validation classes', 'is-valid / is-invalid dan invalid-feedback untuk pesan.'),
       ('needs-validation + novalidate', 'Pola validasi Bootstrap dengan Constraint Validation API browser.'),
       ('input-group', 'Input dengan awalan/akhiran seperti "Rp" atau tombol.')],
  cx=[H('Form checkout dengan validasi Bootstrap', r'''
<form class="row g-3 needs-validation" novalidate>
  <div class="col-md-6 form-floating">
    <input type="text" class="form-control" id="nama" placeholder="Nama" required minlength="3">
    <label for="nama">Nama penerima</label>
    <div class="invalid-feedback">Nama minimal 3 huruf.</div>
  </div>
  <div class="col-md-6">
    <label for="hp" class="form-label">Nomor HP</label>
    <div class="input-group has-validation">
      <span class="input-group-text">+62</span>
      <input type="tel" class="form-control" id="hp" pattern="8[0-9]{8,11}" required aria-describedby="hpBantu">
      <div class="invalid-feedback">Masukkan nomor tanpa 0 di depan, contoh 81234567890.</div>
    </div>
    <div id="hpBantu" class="form-text">Untuk konfirmasi pengiriman via WhatsApp.</div>
  </div>
  <div class="col-md-4">
    <label for="kodepos" class="form-label">Kode pos</label>
    <input class="form-control" id="kodepos" inputmode="numeric" pattern="[0-9]{5}" required>
    <div class="invalid-feedback">Kode pos 5 digit.</div>
  </div>
  <div class="col-12 form-check">
    <input class="form-check-input" type="checkbox" id="setuju" required>
    <label class="form-check-label" for="setuju">Saya setuju data dipakai untuk pengiriman</label>
  </div>
  <div class="col-12"><button class="btn btn-primary w-100 btn-lg">Bayar</button></div>
</form>
<script>
  document.querySelectorAll(".needs-validation").forEach((f) =>
    f.addEventListener("submit", (e) => {
      if (!f.checkValidity()) { e.preventDefault(); e.stopPropagation(); f.querySelector(":invalid")?.focus(); }
      f.classList.add("was-validated");
    }));
</script>'''),
      J('Pola validasi HTML yang sama diuji di Node', r'''
const aturan = { nama: { minlength: 3 }, hp: { pattern: "8[0-9]{8,11}" }, kodepos: { pattern: "[0-9]{5}" } };
const cek = (nilai, a) => {
  if (!nilai) return "valueMissing";
  if (a.minlength && nilai.length < a.minlength) return "tooShort";
  if (a.pattern && !new RegExp(`^(?:${a.pattern})$`).test(nilai)) return "patternMismatch";
  return "valid";
};
const isian = [{ nama: "Al", hp: "081234567890", kodepos: "4011" }, { nama: "Alya", hp: "81234567890", kodepos: "40115" }];
for (const d of isian) console.log(Object.entries(aturan).map(([k, a]) => `${k}=${cek(d[k], a)}`).join("  "));
''', 'Atribut pattern di HTML otomatis diberi jangkar ^ dan $, jadi "081234567890" gagal karena diawali 0.')]),

'Modal dan komponen JavaScript': dict(
  ist=[('Data API', 'Mengaktifkan komponen lewat atribut data-bs-toggle tanpa menulis JS.'),
       ('JavaScript API', 'new bootstrap.Modal(el) dan method show(), hide(), toggle().'),
       ('Event', 'show.bs.modal, shown.bs.modal, hidden.bs.modal untuk mengaitkan logika.'),
       ('getOrCreateInstance', 'Mengambil instance yang ada atau membuat baru; hindari instance ganda.'),
       ('Focus trap', 'Modal mengunci fokus keyboard di dalamnya dan mengembalikannya saat ditutup.')],
  cx=[H('Modal konfirmasi hapus dengan data dinamis', r'''
<button class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#modalHapus" data-nama="Kelas React" data-id="12">Hapus</button>

<div class="modal fade" id="modalHapus" tabindex="-1" aria-labelledby="judulHapus" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="judulHapus">Hapus kelas?</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button>
      </div>
      <div class="modal-body">Kelas <strong id="namaHapus"></strong> akan dihapus permanen.</div>
      <div class="modal-footer">
        <button class="btn btn-secondary" data-bs-dismiss="modal">Batal</button>
        <button class="btn btn-danger" id="konfirmasiHapus">Ya, hapus</button>
      </div>
    </div>
  </div>
</div>
<script>
  const el = document.getElementById("modalHapus");
  let idDipilih = null;
  el.addEventListener("show.bs.modal", (e) => {
    idDipilih = e.relatedTarget.dataset.id;
    el.querySelector("#namaHapus").textContent = e.relatedTarget.dataset.nama;   // textContent: aman dari XSS
  });
  document.getElementById("konfirmasiHapus").addEventListener("click", async () => {
    await fetch(`/api/kelas/${idDipilih}`, { method: "DELETE" });
    bootstrap.Modal.getOrCreateInstance(el).hide();
  });
</script>''')]),

'Variabel CSS, Sass, dan mode gelap': dict(
  ist=[('Sass variables', '$primary, $border-radius, $font-family-base diubah sebelum impor Bootstrap.'),
       ('CSS custom properties', '--bs-primary, --bs-body-bg dapat diubah saat runtime.'),
       ('data-bs-theme', 'Atribut "light" / "dark" untuk mode warna (Bootstrap 5.3+).'),
       ('Utility API', 'Membuat utilitas sendiri dari map Sass.'),
       ('Theming / white-label', 'Satu basis kode, banyak merek dengan variabel berbeda.')],
  cx=[H('Kustomisasi merek dan tombol tema', r'''
// custom.scss
$primary: #0f766e;
$border-radius: .75rem;
$font-family-sans-serif: "Plus Jakarta Sans", system-ui, sans-serif;
$enable-shadows: true;
@import "bootstrap/scss/bootstrap";

// Utilitas baru: .opacity-15
$utilities: map-merge($utilities, ("opacity": (property: opacity, values: (15: .15, 50: .5, 100: 1))));

/* Ubah saat runtime tanpa compile ulang */
.tema-kopi { --bs-primary: #92400e; --bs-primary-rgb: 146, 64, 14; }

<!-- Tombol mode gelap -->
<button class="btn btn-outline-secondary" id="tombolTema" aria-pressed="false"><i class="bi bi-moon"></i> Mode gelap</button>
<script>
  const simpan = (() => { try { return localStorage.getItem("tema"); } catch { return null; } })();
  const awal = simpan ?? (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  const terapkan = (t) => { document.documentElement.dataset.bsTheme = t; tombolTema.setAttribute("aria-pressed", t === "dark"); };
  terapkan(awal);
  tombolTema.onclick = () => { const t = document.documentElement.dataset.bsTheme === "dark" ? "light" : "dark"; terapkan(t); try { localStorage.setItem("tema", t); } catch {} };
</script>''', lang='scss'),
      J('Menurunkan warna hover dan subtle seperti fungsi Sass Bootstrap', r'''
const hexKeRgb = (h) => h.match(/\w\w/g).map((x) => parseInt(x, 16));
const rgbKeHex = (a) => "#" + a.map((x) => Math.round(x).toString(16).padStart(2, "0")).join("");
const campur = (a, b, persenA) => rgbKeHex(hexKeRgb(a).map((v, i) => v * persenA + hexKeRgb(b)[i] * (1 - persenA)));
const shade = (h, p) => campur("#000000", h, p), tint = (h, p) => campur("#ffffff", h, p);
const primary = "#0f766e";
const baris = (k, v) => console.log(k.padEnd(22), v);
baris("primary", primary);
baris("hover (shade 15%)", shade(primary, 0.15));
baris("active (shade 20%)", shade(primary, 0.2));
baris("subtle bg (tint 80%)", tint(primary, 0.8));
baris("--bs-primary-rgb", hexKeRgb(primary).join(", "));
''')]),

'Proyek: halaman kursus': dict(
  ist=[('Landing kursus', 'Hero, silabus, mentor, testimoni, harga, FAQ, CTA.'),
       ('Accordion silabus', 'Menampilkan modul secara ringkas, dapat dibuka satu per satu.'),
       ('Schema.org Course', 'Data terstruktur agar kursus tampil kaya di hasil Google.'),
       ('Lighthouse 90+', 'Target skor performa, aksesibilitas, praktik terbaik, dan SEO.')],
  cx=[H('Kerangka halaman kursus', r'''
<nav class="navbar navbar-expand-lg sticky-top bg-body border-bottom">...</nav>
<header class="py-5 bg-body-tertiary">
  <div class="container"><div class="row align-items-center g-5">
    <div class="col-lg-6">
      <span class="badge text-bg-success mb-3">Batch 12 · Mulai 6 Januari 2027</span>
      <h1 class="display-5 fw-bold">Bootcamp Frontend 16 Minggu</h1>
      <p class="lead">HTML, CSS, JavaScript, React, dan proyek portofolio dengan mentor industri.</p>
      <div class="d-grid d-sm-flex gap-2"><a class="btn btn-primary btn-lg" href="#harga">Daftar</a><a class="btn btn-outline-secondary btn-lg" href="#silabus">Lihat silabus</a></div>
    </div>
    <div class="col-lg-6"><img class="img-fluid rounded-4" src="hero.webp" alt="Siswa bootcamp" width="720" height="480"></div>
  </div></div>
</header>
<section id="silabus" class="container py-5">
  <div class="accordion" id="silabusAcc">
    <div class="accordion-item">
      <h2 class="accordion-header"><button class="accordion-button" data-bs-toggle="collapse" data-bs-target="#m1">Minggu 1-3 · HTML & CSS</button></h2>
      <div id="m1" class="accordion-collapse collapse show" data-bs-parent="#silabusAcc"><div class="accordion-body">Semantik, flexbox, grid, responsif.</div></div>
    </div>
  </div>
</section>
<script type="application/ld+json">
{ "@context": "https://schema.org", "@type": "Course", "name": "Bootcamp Frontend 16 Minggu",
  "description": "HTML sampai React dengan proyek portofolio.", "provider": { "@type": "Organization", "name": "RuangKode" },
  "offers": { "@type": "Offer", "price": "4500000", "priceCurrency": "IDR" } }
</script>'''),
      J('Membuat data silabus dan JSON-LD dari satu sumber', r'''
const modul = [["HTML & CSS", 3], ["JavaScript", 4], ["Git & tooling", 1], ["React", 5], ["Proyek akhir", 3]];
let minggu = 1;
for (const [nama, durasi] of modul) {
  const rentang = durasi === 1 ? String(minggu) : `${minggu}-${minggu + durasi - 1}`;
  console.log(`Minggu ${rentang.padEnd(5)} · ${nama}`);
  minggu += durasi;
}
const jsonld = { "@context": "https://schema.org", "@type": "Course", name: "Bootcamp Frontend 16 Minggu",
  hasCourseInstance: { "@type": "CourseInstance", courseMode: "online", courseWorkload: `P${minggu - 1}W` },
  offers: { "@type": "Offer", price: "4500000", priceCurrency: "IDR" } };
console.log(`total ${minggu - 1} minggu`);
console.log(JSON.stringify(jsonld));
''')]),

'Dropdown, tab, dan accordion': dict(
  ist=[('dropdown', 'Menu pilihan yang diposisikan Popper; dropdown-menu-end untuk rata kanan.'),
       ('nav-tabs / nav-pills', 'Navigasi tab dengan tab-pane sebagai isi.'),
       ('accordion', 'Panel lipat; data-bs-parent agar hanya satu terbuka.'),
       ('Keyboard support', 'Panah atas/bawah di dropdown, Esc menutup; sudah ditangani Bootstrap.')],
  cx=[H('Dropdown akun, tab detail produk, dan FAQ', r'''
<div class="dropdown">
  <button class="btn btn-light dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    <img src="avatar.webp" class="rounded-circle" width="28" height="28" alt=""> Rina
  </button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="/akun"><i class="bi bi-person"></i> Profil</a></li>
    <li><a class="dropdown-item" href="/kelas-saya">Kelas saya</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><button class="dropdown-item text-danger">Keluar</button></li>
  </ul>
</div>

<ul class="nav nav-tabs" role="tablist">
  <li class="nav-item" role="presentation"><button class="nav-link active" data-bs-toggle="tab" data-bs-target="#desk" role="tab">Deskripsi</button></li>
  <li class="nav-item" role="presentation"><button class="nav-link" data-bs-toggle="tab" data-bs-target="#ulasan" role="tab">Ulasan <span class="badge text-bg-secondary">128</span></button></li>
</ul>
<div class="tab-content border border-top-0 p-3">
  <div class="tab-pane fade show active" id="desk" role="tabpanel">...</div>
  <div class="tab-pane fade" id="ulasan" role="tabpanel">...</div>
</div>

<div class="accordion accordion-flush" id="faq">
  <div class="accordion-item">
    <h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q1">Apakah ada sertifikat?</button></h2>
    <div id="q1" class="accordion-collapse collapse" data-bs-parent="#faq"><div class="accordion-body">Ya, setelah lulus proyek akhir.</div></div>
  </div>
</div>''')]),

'Offcanvas, toast, dan tooltip': dict(
  ist=[('offcanvas', 'Panel samping yang meluncur; cocok untuk filter atau keranjang di ponsel.'),
       ('toast', 'Notifikasi singkat yang hilang sendiri; letakkan dalam toast-container.'),
       ('tooltip / popover', 'Info tambahan saat hover/focus; wajib diinisialisasi dengan JS.'),
       ('aria-live', 'Agar pembaca layar mengumumkan toast.')],
  cx=[H('Keranjang offcanvas, toast, dan tooltip', r'''
<button class="btn btn-primary position-relative" data-bs-toggle="offcanvas" data-bs-target="#keranjang">
  <i class="bi bi-cart"></i><span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">2</span>
</button>
<div class="offcanvas offcanvas-end" tabindex="-1" id="keranjang" aria-labelledby="judulKeranjang">
  <div class="offcanvas-header"><h5 id="judulKeranjang">Keranjang</h5><button class="btn-close" data-bs-dismiss="offcanvas" aria-label="Tutup"></button></div>
  <div class="offcanvas-body">...</div>
</div>

<div class="toast-container position-fixed bottom-0 end-0 p-3">
  <div id="toastSimpan" class="toast" role="status" aria-live="polite" aria-atomic="true" data-bs-delay="3000">
    <div class="toast-body d-flex justify-content-between">Kelas ditambahkan ke keranjang <button class="btn-close" data-bs-dismiss="toast"></button></div>
  </div>
</div>

<span class="text-decoration-underline" data-bs-toggle="tooltip" data-bs-title="Pajak Pertambahan Nilai 11%" tabindex="0">PPN</span>

<script>
  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((el) => new bootstrap.Tooltip(el));
  const toast = bootstrap.Toast.getOrCreateInstance(document.getElementById("toastSimpan"));
  document.querySelectorAll(".tambah-keranjang").forEach((b) => b.addEventListener("click", () => toast.show()));
</script>''')]),

'Tabel, list group, dan pagination': dict(
  ist=[('table-striped / table-hover', 'Gaya tabel standar; table-responsive untuk scroll horizontal.'),
       ('list-group', 'Daftar dengan item aktif, badge, dan aksi.'),
       ('pagination', 'Navigasi halaman; tandai halaman aktif dengan aria-current.'),
       ('Server-side pagination', 'Hanya mengambil satu halaman data per request (LIMIT/OFFSET atau cursor).')],
  cx=[H('Tabel transaksi dengan pagination', r'''
<div class="table-responsive">
  <table class="table table-striped table-hover align-middle">
    <caption>Transaksi November 2026</caption>
    <thead class="table-light"><tr><th scope="col">No. invoice</th><th scope="col">Siswa</th><th scope="col" class="text-end">Total</th><th scope="col">Status</th></tr></thead>
    <tbody>
      <tr><td>INV-0412</td><td>Rina W.</td><td class="text-end">Rp399.000</td><td><span class="badge text-bg-success">Lunas</span></td></tr>
      <tr><td>INV-0413</td><td>Budi S.</td><td class="text-end">Rp450.000</td><td><span class="badge text-bg-warning">Menunggu</span></td></tr>
    </tbody>
  </table>
</div>
<nav aria-label="Navigasi halaman transaksi">
  <ul class="pagination justify-content-center">
    <li class="page-item disabled"><span class="page-link">«</span></li>
    <li class="page-item active" aria-current="page"><span class="page-link">1</span></li>
    <li class="page-item"><a class="page-link" href="?hal=2">2</a></li>
    <li class="page-item"><a class="page-link" href="?hal=3">3</a></li>
    <li class="page-item"><a class="page-link" href="?hal=2">»</a></li>
  </ul>
</nav>'''),
      J('Membuat nomor halaman dengan elipsis', r'''
function halaman(aktif, total, sekitar = 1) {
  const h = new Set([1, total]);
  for (let i = aktif - sekitar; i <= aktif + sekitar; i++) if (i > 1 && i < total) h.add(i);
  const urut = [...h].sort((a, b) => a - b), hasil = [];
  urut.forEach((n, i) => { if (i && n - urut[i - 1] > 1) hasil.push("…"); hasil.push(n === aktif ? `[${n}]` : String(n)); });
  return hasil.join(" ");
}
const totalData = 487, perHalaman = 20, total = Math.ceil(totalData / perHalaman);
for (const a of [1, 5, 13, total]) console.log(`hal ${String(a).padStart(2)}/${total}: « ${halaman(a, total)} »   OFFSET ${(a - 1) * perHalaman} LIMIT ${perHalaman}`);
''')]),

'Utilitas lanjutan: stack, posisi, dan rasio': dict(
  ist=[('vstack / hstack', 'Pembungkus flex vertikal/horizontal dengan gap; ringkas untuk tata letak cepat.'),
       ('Position utilities', 'position-absolute top-0 start-100 translate-middle untuk badge di sudut.'),
       ('ratio', 'Wadah berasio tetap (ratio-16x9) untuk video atau peta.'),
       ('object-fit-*', 'object-fit-cover agar gambar memenuhi wadah tanpa gepeng.'),
       ('visually-hidden', 'Teks hanya untuk pembaca layar.')],
  cx=[H('Profil mentor, video, dan tombol ikon', r'''
<div class="hstack gap-3 align-items-start">
  <div class="position-relative flex-shrink-0">
    <img src="mentor.webp" class="rounded-circle object-fit-cover" width="64" height="64" alt="Dimas, mentor React">
    <span class="position-absolute bottom-0 end-0 p-2 bg-success border border-light rounded-circle">
      <span class="visually-hidden">Sedang online</span>
    </span>
  </div>
  <div class="vstack gap-1">
    <strong>Dimas Pratama</strong>
    <span class="text-body-secondary small">Senior Frontend Engineer · 8 tahun</span>
  </div>
  <button class="btn btn-light ms-auto"><i class="bi bi-chat-dots"></i><span class="visually-hidden">Kirim pesan</span></button>
</div>

<div class="ratio ratio-16x9 rounded-3 overflow-hidden mt-4">
  <video controls preload="metadata" poster="cuplikan.webp"><source src="cuplikan.mp4" type="video/mp4"></video>
</div>'''),
      J('Menghitung tinggi wadah rasio di berbagai lebar', r'''
const rasio = { "1x1": [1, 1], "4x3": [4, 3], "16x9": [16, 9], "21x9": [21, 9] };
for (const lebar of [360, 768, 1140]) {
  console.log(`lebar ${lebar}px: ` + Object.entries(rasio).map(([k, [w, h]]) => `${k} -> ${Math.round((lebar * h) / w)}px`).join(" | "));
}
console.log("padding-top trik lama untuk 16x9:", ((9 / 16) * 100).toFixed(2) + "%", "| kini cukup aspect-ratio: 16 / 9");
''')]),
}
