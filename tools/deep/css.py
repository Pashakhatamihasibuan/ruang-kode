"""Pendalaman jalur CSS: istilah dunia kerja dan contoh CSS siap pakai (beberapa perhitungan dijalankan dengan Node)."""
K = 'css'


def C(t, code, b=None, lang='css'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def J(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='js')


D = {
'Aturan, selector & deklarasi': dict(
  ist=[('Rule set', 'Selector + blok deklarasi { properti: nilai; }.'),
       ('Shorthand property', 'Satu properti yang mengisi beberapa sekaligus: margin, padding, font, border, inset.'),
       ('Logical properties', 'margin-inline, padding-block, inset-inline-start: mengikuti arah tulisan (penting untuk RTL).'),
       ('Stylelint', 'Linter CSS untuk menangkap kesalahan dan menegakkan konvensi tim.')],
  cx=[C('Shorthand dan logical properties', '''
.kartu {
  /* longhand */
  margin-top: 16px; margin-right: 0; margin-bottom: 16px; margin-left: 0;
  /* shorthand setara */
  margin: 16px 0;
  /* logical: otomatis benar untuk bahasa kanan-ke-kiri (Arab) */
  padding-block: 1rem;          /* atas & bawah */
  padding-inline: 1.25rem;      /* awal & akhir baris */
  border-inline-start: 4px solid var(--warna-aksen);
  font: 600 1rem/1.5 "Inter", system-ui, sans-serif;   /* weight size/line-height family */
}''')]),

'Selector sederhana': dict(
  ist=[('Type, class, id selector', 'p, .kartu, #utama; kelas adalah pilihan utama untuk gaya.'),
       ('Attribute selector', '[type="email"], [href^="https"], [data-status="lunas"].'),
       ('Universal selector', '* memilih semua; dipakai untuk reset box-sizing.'),
       ('Selector performance', 'Browser modern cepat; yang lebih penting adalah keterbacaan dan specificity rendah.')],
  cx=[C('Selector atribut untuk status data', '''
*, *::before, *::after { box-sizing: border-box; }

.lencana { padding: .125rem .5rem; border-radius: 999px; font-size: .75rem; }
.lencana[data-status="lunas"]   { background: #e6f4ea; color: #1e6b34; }
.lencana[data-status="pending"] { background: #fff4e5; color: #8a4b00; }
.lencana[data-status="gagal"]   { background: #fdecea; color: #a1281e; }

a[href^="http"]:not([href*="tokokopi.id"])::after { content: " ↗"; }   /* tanda link eksternal */
a[href$=".pdf"]::after { content: " (PDF)"; }
input[type="number"] { font-variant-numeric: tabular-nums; }''')]),

'Cascade & specificity': dict(
  ist=[('Cascade', 'Urutan penentuan gaya: origin & !important, cascade layer, specificity, lalu urutan muncul.'),
       ('Specificity (a,b,c)', 'id = (1,0,0), kelas/atribut/pseudo-class = (0,1,0), elemen = (0,0,1).'),
       ('@layer', 'Cascade layers: mengatur prioritas kelompok CSS (reset, framework, komponen, utilitas) tanpa perang specificity.'),
       ('!important', 'Pengecualian terakhir; jika sering dipakai, tanda arsitektur CSS bermasalah.')],
  cx=[J('Menghitung specificity seperti browser', '''
function specificity(sel) {
  const s = sel.replace(/:not\\(([^)]*)\\)/g, " $1 ");       // :not() dihitung dari isinya
  const a = (s.match(/#[\\w-]+/g) || []).length;
  const b = (s.match(/\\.[\\w-]+|\\[[^\\]]+\\]|(?<!:):(?!:)[\\w-]+/g) || []).length;
  const c = (s.replace(/#[\\w-]+|\\.[\\w-]+|\\[[^\\]]+\\]|:{1,2}[\\w-]+/g, " ").match(/(^|[\\s>+~])[a-z][\\w-]*/gi) || []).length
          + (s.match(/::[\\w-]+/g) || []).length;
  return [a, b, c];
}
const daftar = ["p", ".tombol", "nav a:hover", "#header .menu li", "button.tombol.utama:not(.nonaktif)", "a::before"];
for (const sel of daftar) console.log(sel.padEnd(38), specificity(sel).join(","));
const menang = daftar.reduce((x, y) => (specificity(y).join() > specificity(x).join() ? y : x));
console.log("paling kuat:", menang);
'''),
     C('@layer: prioritas ditentukan urutan layer, bukan specificity', '''
@layer reset, framework, komponen, utilitas;

@layer framework {
  #app .btn.btn-primary { background: blue; }      /* specificity tinggi */
}
@layer komponen {
  .tombol { background: var(--hijau); }             /* menang: layer belakangan */
}
@layer utilitas {
  .sembunyi { display: none; }
}''', 'Gaya di layer yang dideklarasikan belakangan selalu menang atas layer sebelumnya, berapa pun specificity-nya.')]),

'Box model': dict(
  ist=[('content / padding / border / margin', 'Empat lapisan kotak setiap elemen.'),
       ('box-sizing: border-box', 'Lebar sudah termasuk padding dan border; standar hampir semua proyek.'),
       ('Margin collapsing', 'Margin vertikal dua blok bersebelahan bergabung menjadi yang terbesar, bukan dijumlah.'),
       ('DevTools box model', 'Panel di Inspect Element untuk melihat ukuran tiap lapisan.')],
  cx=[J('Berapa lebar sebenarnya? content-box vs border-box', '''
const kotak = { width: 300, padding: 24, border: 2, margin: 16 };
const contentBox = kotak.width + 2 * kotak.padding + 2 * kotak.border;
const borderBox = kotak.width;
console.log("content-box: lebar terlihat", contentBox, "px, ruang terpakai", contentBox + 2 * kotak.margin, "px");
console.log("border-box : lebar terlihat", borderBox, "px, isi tersisa", borderBox - 2 * kotak.padding - 2 * kotak.border, "px");
const margin = [32, 24];
console.log("dua margin vertikal", margin.join(" & "), "-> jarak", Math.max(...margin), "px (collapse), bukan", margin[0] + margin[1]);
''')]),

'Unit ukuran': dict(
  ist=[('rem / em', 'rem relatif ke font root (aman dan konsisten); em relatif ke font elemen induk.'),
       ('Viewport units', 'vw, vh, dvh (dynamic viewport, memperhitungkan bilah browser ponsel), svh, lvh.'),
       ('clamp()', 'clamp(min, ideal, max) untuk tipografi dan spasi yang fluid tanpa media query.'),
       ('ch', 'Lebar karakter "0"; max-width: 65ch membatasi panjang baris yang nyaman dibaca.')],
  cx=[C('Tipografi fluid dan tinggi layar ponsel yang benar', '''
:root { font-size: 100%; }                       /* hormati pengaturan font pengguna (biasanya 16px) */
h1 { font-size: clamp(1.75rem, 1.2rem + 2.5vw, 3rem); }   /* 28px di ponsel -> 48px di desktop */
.konten { max-width: 65ch; margin-inline: auto; padding-inline: clamp(1rem, 4vw, 3rem); }
.hero { min-height: 100dvh; }                     /* 100vh di ponsel tertutup bilah alamat; dvh tidak */
.ikon { inline-size: 1.25em; block-size: 1.25em; }   /* ikut besar teks di sekitarnya */
@media (min-width: 48rem) { .grid { gap: 2rem; } }  /* breakpoint dalam rem ikut zoom pengguna */'''),
     J('Menghitung clamp() di beberapa lebar layar', '''
const clamp = (min, ideal, max) => Math.min(Math.max(min, ideal), max);
for (const vw of [360, 768, 1280, 1920]) {
  const px = clamp(28, 1.2 * 16 + 0.025 * vw, 48);
  console.log(`${String(vw).padStart(4)}px layar -> h1 ${px.toFixed(1)}px`);
}
''')]),

'Warna & latar': dict(
  ist=[('Contrast ratio', 'WCAG AA: teks normal minimal 4,5:1, teks besar dan komponen UI minimal 3:1.'),
       ('Relative luminance', 'Kecerahan warna yang dihitung dari nilai RGB linear; dasar rumus kontras.'),
       ('background shorthand', 'Gambar, posisi, ukuran, repeat, dan warna dalam satu deklarasi; bisa berlapis.'),
       ('Gradient', 'linear-gradient, radial-gradient, conic-gradient sebagai gambar latar.')],
  cx=[J('Menghitung rasio kontras WCAG untuk palet merek', '''
const lum = (hex) => {
  const [r, g, b] = hex.match(/\\w\\w/g).map((x) => parseInt(x, 16) / 255)
    .map((c) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};
const kontras = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
const pasang = [["#ffffff", "#16a34a", "teks putih di tombol hijau"], ["#ffffff", "#15803d", "putih di hijau lebih gelap"],
                ["#6b7280", "#ffffff", "abu-abu di putih"], ["#111827", "#fbbf24", "hitam di kuning"]];
for (const [fg, bg, ket] of pasang) {
  const r = kontras(fg, bg);
  console.log(`${ket.padEnd(28)} ${r.toFixed(2)}:1  ${r >= 4.5 ? "lulus AA" : r >= 3 ? "hanya teks besar" : "GAGAL"}`);
}
''', 'Hijau cerah populer untuk tombol, tetapi teks putih di atasnya sering gagal AA. Menggelapkan satu tingkat biasanya cukup.')]),

'Tipografi': dict(
  ist=[('Type scale', 'Skala ukuran font dengan rasio tetap (misalnya 1,25) agar hierarki konsisten.'),
       ('line-height', '1,4-1,6 untuk paragraf; judul besar lebih rapat (1,1-1,2).'),
       ('Variable font', 'Satu berkas font dengan banyak ketebalan; hemat unduhan.'),
       ('font-display: swap', 'Teks tampil dengan font cadangan sambil menunggu font web, menghindari teks tak terlihat.')],
  cx=[C('Sistem tipografi dengan font variabel', '''
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-var.woff2") format("woff2-variations");
  font-weight: 100 900;
  font-display: swap;
}
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --step-0: 1rem; --step-1: 1.25rem; --step-2: 1.563rem; --step-3: 1.953rem; --step-4: 2.441rem;  /* rasio 1,25 */
}
body { font-family: var(--font-sans); font-size: var(--step-0); line-height: 1.6; text-wrap: pretty; }
h1, h2, h3 { line-height: 1.15; text-wrap: balance; letter-spacing: -0.01em; }
h1 { font-size: var(--step-4); font-weight: 750; }
.harga { font-variant-numeric: tabular-nums; }    /* angka sama lebar agar kolom rata */''')]),

'Warna modern: oklch, color-mix & light-dark': dict(
  ist=[('OKLCH', 'Ruang warna perseptual (Lightness, Chroma, Hue); mengubah L memberi perubahan terang yang terasa seragam.'),
       ('color-mix()', 'Mencampur dua warna di ruang warna tertentu, misalnya untuk hover atau transparansi.'),
       ('light-dark()', 'Memilih warna sesuai color-scheme terang atau gelap dalam satu deklarasi.'),
       ('Wide gamut (P3)', 'Layar modern bisa menampilkan warna lebih jenuh daripada sRGB; OKLCH bisa menjangkaunya.')],
  cx=[C('Palet merek dari satu hue dengan oklch', '''
:root {
  color-scheme: light dark;
  --hue: 150;                                         /* hijau merek */
  --hijau-50:  oklch(97% 0.03 var(--hue));
  --hijau-500: oklch(62% 0.17 var(--hue));
  --hijau-700: oklch(48% 0.14 var(--hue));
  --permukaan: light-dark(#ffffff, oklch(20% 0.01 var(--hue)));
  --teks:      light-dark(oklch(22% 0.02 var(--hue)), oklch(95% 0.01 var(--hue)));
}
.tombol { background: var(--hijau-700); color: white; }
.tombol:hover { background: color-mix(in oklch, var(--hijau-700), black 12%); }
.sorot { background: color-mix(in srgb, var(--hijau-500) 15%, transparent); }''', 'Mengganti --hue saja sudah menghasilkan palet merek baru dengan tingkat terang yang sama.')]),

'Display & alur normal': dict(
  ist=[('Normal flow', 'Tata letak bawaan: blok bertumpuk vertikal, inline mengalir dalam baris.'),
       ('block / inline / inline-block', 'Menentukan apakah elemen mengambil satu baris penuh, mengalir di teks, atau keduanya.'),
       ('display: none vs visibility: hidden', 'none menghapus dari layout dan aksesibilitas; hidden menyisakan ruang.'),
       ('Visually hidden', 'Pola .sr-only menyembunyikan teks dari mata tetapi tetap dibaca pembaca layar.')],
  cx=[C('Menyembunyikan dengan benar sesuai tujuan', '''
/* tidak terlihat dan tidak dibaca pembaca layar */
[hidden] { display: none !important; }

/* tidak terlihat tetapi tetap dibaca pembaca layar (label tombol ikon, "membuka tab baru") */
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0;
}
/* skip link: tersembunyi sampai difokus keyboard */
.skip-link { position: absolute; inset-inline-start: 1rem; translate: 0 -200%; }
.skip-link:focus { translate: 0 1rem; }

/* display: contents membuat pembungkus "hilang" dari layout tetapi anaknya tetap ikut grid */
.grup-kartu { display: contents; }''')]),

'Position & z-index': dict(
  ist=[('relative / absolute / fixed / sticky', 'Cara memosisikan elemen relatif terhadap dirinya, induk berposisi, viewport, atau saat menggulir.'),
       ('Containing block', 'Elemen acuan untuk position: absolute; induk terdekat yang punya position selain static.'),
       ('Stacking context', 'Kelompok lapisan; z-index hanya bersaing di dalam stacking context yang sama.'),
       ('z-index scale', 'Skala token (dropdown 100, sticky 200, modal 1000, toast 1100) agar tidak ada z-index: 99999.')],
  cx=[C('Header sticky, lencana absolut, dan skala z-index', '''
:root { --z-dropdown: 100; --z-sticky: 200; --z-overlay: 900; --z-modal: 1000; --z-toast: 1100; }

.header { position: sticky; top: 0; z-index: var(--z-sticky); background: var(--permukaan); }
.ikon-keranjang { position: relative; }
.ikon-keranjang .jumlah {
  position: absolute; inset-block-start: -6px; inset-inline-end: -8px;
  min-width: 1.25rem; padding-inline: .25rem; border-radius: 999px;
}
/* jebakan: transform/opacity < 1/filter membuat stacking context baru,
   sehingga z-index anak tidak bisa "keluar" melewati elemen lain di luar induknya */
.kartu:hover { transform: translateY(-2px); }''')]),

'Flexbox': dict(
  ist=[('Main axis / cross axis', 'Sumbu utama (flex-direction) dan sumbu silang; justify-content vs align-items.'),
       ('flex: 1 1 0', 'grow, shrink, basis; flex: 1 membagi ruang rata.'),
       ('gap', 'Jarak antaritem tanpa margin; didukung semua browser modern.'),
       ('min-width: 0', 'Item flex tidak menyusut di bawah isi terpanjangnya kecuali diberi min-width: 0; sumber overflow teks panjang.')],
  cx=[C('Pola flexbox sehari-hari', '''
/* navbar: logo kiri, menu kanan */
.nav { display: flex; align-items: center; gap: 1rem; }
.nav .spasi { margin-inline-start: auto; }

/* baris item keranjang: teks panjang tidak mendorong harga keluar layar */
.item { display: flex; gap: .75rem; align-items: center; }
.item__nama { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.item__harga { flex-shrink: 0; font-variant-numeric: tabular-nums; }

/* tag yang turun baris otomatis */
.tag-list { display: flex; flex-wrap: wrap; gap: .5rem; }

/* footer kartu selalu di bawah walau isi kartu beda tinggi */
.kartu { display: flex; flex-direction: column; }
.kartu__aksi { margin-block-start: auto; }''')]),

'Grid': dict(
  ist=[('Grid template', 'grid-template-columns/rows dan areas untuk tata letak dua dimensi.'),
       ('fr unit', 'Bagian dari ruang sisa; 1fr 2fr membagi 1:2.'),
       ('auto-fill / auto-fit + minmax()', 'Kolom responsif tanpa media query: repeat(auto-fill, minmax(220px, 1fr)).'),
       ('Subgrid', 'Anak grid memakai garis kolom/baris induk agar isi kartu sejajar antar kartu.')],
  cx=[C('Katalog responsif tanpa media query dan layout halaman dengan area', '''
.katalog { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(220px, 100%), 1fr)); gap: 1.5rem; }

/* subgrid: judul, harga, dan tombol sejajar di semua kartu */
.kartu { display: grid; grid-row: span 3; grid-template-rows: subgrid; gap: .5rem; }

.halaman {
  display: grid; min-height: 100dvh;
  grid-template: "header" auto "utama" 1fr "footer" auto / 1fr;
}
@media (min-width: 64rem) {
  .halaman { grid-template: "header header" auto "sisi utama" 1fr "footer footer" auto / 260px 1fr; }
}
.halaman > header { grid-area: header; } .halaman > aside { grid-area: sisi; }
.halaman > main { grid-area: utama; }   .halaman > footer { grid-area: footer; }'''),
     J('Berapa kolom yang muncul dengan auto-fill minmax(220px, 1fr)?', '''
const kolom = (lebar, min = 220, gap = 24) => Math.max(1, Math.floor((lebar + gap) / (min + gap)));
for (const w of [328, 720, 1024, 1232]) {
  const n = kolom(w); const lebarKolom = (w - (n - 1) * 24) / n;
  console.log(`kontainer ${w}px -> ${n} kolom @ ${lebarKolom.toFixed(0)}px`);
}
''')]),

'Media query & mobile-first': dict(
  ist=[('Mobile-first', 'Gaya dasar untuk layar kecil, lalu tambah dengan min-width; CSS lebih sederhana dan ringan di ponsel.'),
       ('Breakpoint', 'Titik lebar tempat tata letak berubah; tentukan dari konten, bukan model perangkat.'),
       ('Media features', 'prefers-color-scheme, prefers-reduced-motion, hover, pointer: coarse.'),
       ('Range syntax', '@media (48rem <= width < 64rem) lebih mudah dibaca daripada min/max.')],
  cx=[C('Mobile-first plus preferensi pengguna', '''
.produk { display: grid; gap: 1rem; }                       /* 1 kolom: ponsel */
@media (width >= 40rem) { .produk { grid-template-columns: 1fr 1fr; } }
@media (width >= 64rem) { .produk { grid-template-columns: 2fr 1fr; } }

@media (hover: hover) { .kartu:hover { box-shadow: var(--bayangan-2); } }   /* hover hanya untuk mouse */
@media (pointer: coarse) { .tombol { min-block-size: 48px; } }             /* target sentuh besar */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
@media print { nav, .tombol { display: none; } a::after { content: " (" attr(href) ")"; } }''')]),

'Container query': dict(
  ist=[('Container query', 'Gaya berdasarkan ukuran kontainer, bukan viewport; komponen menyesuaikan di mana pun ia diletakkan.'),
       ('container-type: inline-size', 'Menjadikan elemen kontainer yang bisa diquery lebarnya.'),
       ('cqi / cqw', 'Unit relatif ke ukuran kontainer.'),
       ('Intrinsic design', 'Komponen yang responsif sendiri tanpa tahu tata letak halaman.')],
  cx=[C('Kartu produk yang menyesuaikan lebar slotnya', '''
.slot-kartu { container: kartu / inline-size; }

.kartu { display: grid; gap: .75rem; }
.kartu__judul { font-size: clamp(1rem, 4cqi, 1.375rem); }

@container kartu (width >= 28rem) {          /* slot lebar: gambar di samping */
  .kartu { grid-template-columns: 160px 1fr; align-items: center; }
}
@container kartu (width < 16rem) {           /* slot sangat sempit (sidebar): sembunyikan deskripsi */
  .kartu__deskripsi { display: none; }
}''', 'Kartu yang sama tampil vertikal di grid tiga kolom, horizontal di daftar lebar, dan ringkas di sidebar, tanpa kelas tambahan.')]),

'Gambar responsif, aspect-ratio & object-fit': dict(
  ist=[('aspect-ratio', 'Menjaga rasio kotak (16/9, 1/1) bahkan sebelum gambar dimuat; mencegah layout shift.'),
       ('object-fit: cover / contain', 'Mengisi kotak dengan memotong, atau memuat seluruh gambar dengan ruang kosong.'),
       ('object-position', 'Menentukan bagian gambar yang tetap terlihat saat dipotong.'),
       ('max-width: 100%', 'Mencegah gambar lebih lebar dari kontainernya.')],
  cx=[C('Thumbnail seragam dari foto berbagai ukuran', '''
img, video { max-width: 100%; height: auto; display: block; }

.thumb {
  aspect-ratio: 1;                 /* kotak sempurna */
  width: 100%;
  object-fit: cover;               /* isi penuh, potong bagian berlebih */
  object-position: 50% 30%;        /* utamakan bagian atas-tengah (wajah, label produk) */
  border-radius: .75rem;
  background: var(--abu-100);      /* placeholder saat memuat */
}
.logo-mitra { aspect-ratio: 3 / 1; object-fit: contain; }   /* logo jangan terpotong */
.video-embed { aspect-ratio: 16 / 9; width: 100%; }''')]),

'Combinator & pseudo': dict(
  ist=[('Combinator', 'Spasi (keturunan), > (anak langsung), + (saudara berikutnya), ~ (saudara setelahnya).'),
       ('Pseudo-class', 'Status elemen: :hover, :focus-visible, :checked, :nth-child(), :empty, :is(), :where().'),
       ('Pseudo-element', 'Bagian virtual: ::before, ::after, ::placeholder, ::marker, ::selection.'),
       (':focus-visible', 'Cincin fokus hanya untuk navigasi keyboard, bukan klik mouse.')],
  cx=[C('Pola umum dengan combinator dan pseudo', '''
.tumpuk > * + * { margin-block-start: 1rem; }               /* "lobotomized owl": jarak antar anak */
.tabel tbody tr:nth-child(even) { background: var(--abu-50); }
.daftar li:not(:last-child) { border-block-end: 1px solid var(--garis); }
:is(h1, h2, h3):where(.artikel *) { scroll-margin-top: 5rem; }   /* :where = specificity 0 */

.tombol:focus-visible { outline: 3px solid var(--fokus); outline-offset: 2px; }
.input:placeholder-shown + .label { opacity: .6; }
.kotak:empty::before { content: "Belum ada data"; color: var(--teks-lembut); }
.wajib::after { content: " *"; color: var(--merah-700); }
input[type="checkbox"]:checked + label { text-decoration: line-through; }''')]),

'Transform, transisi & animasi': dict(
  ist=[('Composited properties', 'transform dan opacity dianimasikan GPU tanpa layout ulang; murah dan mulus.'),
       ('transition', 'Perubahan halus antar dua state; tentukan properti, durasi, dan easing.'),
       ('@keyframes', 'Animasi multi-langkah yang bisa berulang.'),
       ('View Transitions', 'API untuk animasi perpindahan halaman/state (startViewTransition dan @view-transition).')],
  cx=[C('Animasi yang mulus dan menghormati preferensi pengguna', '''
.kartu { transition: transform 200ms cubic-bezier(.2,.8,.2,1), box-shadow 200ms; }
.kartu:hover { transform: translateY(-4px); }

@keyframes kerangka { from { background-position: 200% 0; } to { background-position: -200% 0; } }
.skeleton {
  background: linear-gradient(90deg, var(--abu-100) 25%, var(--abu-200) 50%, var(--abu-100) 75%);
  background-size: 200% 100%; animation: kerangka 1.4s linear infinite;
}
/* hindari menganimasikan width/height/top/left: memicu layout setiap frame */
.toast { translate: 0 120%; transition: translate 250ms ease-out; }
.toast.tampil { translate: 0 0; }

@view-transition { navigation: auto; }        /* transisi halus antar halaman MPA */
@media (prefers-reduced-motion: reduce) { .skeleton { animation: none; } }''')]),

':has(): selector induk & nesting': dict(
  ist=[(':has()', 'Memilih elemen berdasarkan isi atau saudaranya; "parent selector" yang lama ditunggu.'),
       ('Native CSS nesting', 'Menulis aturan bersarang langsung di CSS (& untuk induk), tanpa Sass.'),
       ('Form state styling', 'form:has(:user-invalid) untuk menandai form yang masih punya error.'),
       ('Progressive enhancement', 'Fitur baru dipakai sebagai peningkatan; halaman tetap berfungsi di browser lama.')],
  cx=[C(':has() dan nesting tanpa JavaScript', '''
.kartu {
  padding: 1rem;
  &:has(img) { padding-block-start: 0; }                 /* kartu bergambar */
  &:has(.lencana--habis) { opacity: .6; }                 /* produk habis tampak redup */
  & .judul { font-weight: 600; }
  &:hover .judul { text-decoration: underline; }
  @media (width >= 40rem) { padding: 1.5rem; }
}
.field:has(input:user-invalid) label { color: var(--merah-700); }
form:has(:user-invalid) button[type="submit"] { opacity: .5; }
body:has(dialog[open]) { overflow: hidden; }              /* kunci gulir saat modal terbuka */
.galeri:has(> :nth-child(5)) { grid-template-columns: repeat(3, 1fr); }  /* 5+ foto: 3 kolom */''')]),

'Variabel CSS & tema': dict(
  ist=[('Custom property', '--nama: nilai; dibaca dengan var(--nama, cadangan); bisa diubah saat runtime.'),
       ('Design token tiers', 'Primitive (--hijau-700) -> semantic (--warna-aksi) -> component (--tombol-latar).'),
       ('Theming', 'Mengganti nilai token di [data-theme="gelap"] atau media query, tanpa menyentuh komponen.'),
       ('@property', 'Mendaftarkan tipe custom property agar bisa dianimasikan.')],
  cx=[C('Token tiga lapis dan tema gelap', '''
:root {
  /* primitive */
  --hijau-600: oklch(55% 0.15 150); --hijau-700: oklch(48% 0.14 150);
  --abu-50: oklch(98% 0 0); --abu-900: oklch(20% 0.01 150);
  /* semantic */
  --warna-latar: var(--abu-50); --warna-teks: var(--abu-900); --warna-aksi: var(--hijau-700);
  /* component */
  --tombol-latar: var(--warna-aksi); --tombol-teks: white; --radius: .75rem;
}
[data-theme="gelap"] { --warna-latar: var(--abu-900); --warna-teks: var(--abu-50); --warna-aksi: var(--hijau-600); }
@media (prefers-color-scheme: dark) { :root:not([data-theme="terang"]) { --warna-latar: var(--abu-900); --warna-teks: var(--abu-50); } }

body { background: var(--warna-latar); color: var(--warna-teks); }
.tombol { background: var(--tombol-latar); color: var(--tombol-teks); border-radius: var(--radius); }

@property --progres { syntax: "<percentage>"; inherits: false; initial-value: 0%; }
.bar { background: linear-gradient(90deg, var(--warna-aksi) var(--progres), transparent 0); transition: --progres .4s; }''')]),

'BEM, Sass, CSS Modules & performa': dict(
  ist=[('BEM', 'Block__Element--Modifier: konvensi nama kelas yang menghindari bentrok (kartu__judul--besar).'),
       ('Sass', 'Preprocessor dengan variabel, mixin, dan partial; sebagian fiturnya kini ada di CSS asli.'),
       ('CSS Modules', 'Nama kelas diberi hash otomatis per komponen sehingga tidak bentrok antar berkas.'),
       ('Unused CSS', 'CSS yang tidak terpakai memperlambat render; ukur di DevTools Coverage dan hapus.')],
  cx=[C('Satu komponen dalam tiga gaya penulisan', '''
/* BEM (CSS biasa) */
.kartu { … }  .kartu__judul { … }  .kartu--unggulan { … }

/* Sass: mixin dan partial */
@use "token" as t;
@mixin fokus { outline: 3px solid t.$fokus; outline-offset: 2px; }
.tombol { &:focus-visible { @include fokus; } }

/* CSS Modules: Kartu.module.css */
.judul { font-weight: 600; }
/* Kartu.jsx */
/* import s from "./Kartu.module.css";  <h3 className={s.judul}>  ->  class="Kartu_judul__x7a2q" */'''),
     J('Mengukur CSS yang tidak terpakai (simulasi panel Coverage)', '''
const aturan = [".kartu", ".kartu__judul", ".tombol", ".tombol--besar", ".modal", ".carousel", ".carousel__slide", ".lencana"];
const dipakaiDiHalaman = new Set([".kartu", ".kartu__judul", ".tombol", ".lencana"]);
const tidak = aturan.filter((a) => !dipakaiDiHalaman.has(a));
console.log(`${tidak.length}/${aturan.length} aturan tidak terpakai (${Math.round(100 * tidak.length / aturan.length)}%):`, tidak.join(" "));
console.log("tindakan: pecah CSS per halaman/komponen, atau muat .modal dan .carousel saat dibutuhkan");
''')]),

'Landing page toko responsif': dict(
  ist=[('Above the fold', 'Bagian yang terlihat tanpa menggulir; berisi proposisi nilai dan satu ajakan utama.'),
       ('Call to action (CTA)', 'Tombol utama ("Pesan sekarang") yang kontras dan konsisten.'),
       ('Core Web Vitals', 'LCP < 2,5 s, INP < 200 ms, CLS < 0,1 sebagai target kualitas halaman.'),
       ('Visual regression test', 'Membandingkan tangkapan layar sebelum dan sesudah perubahan CSS untuk menangkap kerusakan tampilan.')],
  cx=[C('Kerangka CSS landing page yang cepat', '''
@layer reset, token, layout, komponen;
@layer layout {
  .wadah { max-width: 72rem; margin-inline: auto; padding-inline: clamp(1rem, 4vw, 2rem); }
  .hero { display: grid; gap: 2rem; align-items: center; min-height: min(80dvh, 44rem); }
  @media (width >= 56rem) { .hero { grid-template-columns: 1.1fr 1fr; } }
  .fitur { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(min(16rem, 100%), 1fr)); }
}
@layer komponen {
  .cta { display: inline-flex; align-items: center; gap: .5rem; min-block-size: 48px; padding-inline: 1.5rem;
         background: var(--warna-aksi); color: white; border-radius: var(--radius); font-weight: 600; }
  .hero img { aspect-ratio: 4 / 3; width: 100%; object-fit: cover; border-radius: 1.5rem; }
  .testimoni { border-inline-start: 4px solid var(--warna-aksi); padding-inline-start: 1rem; }
}
/* Checklist sebelum rilis: 360px tanpa gulir samping, kontras AA, fokus terlihat, Lighthouse >= 90 */''')]),
}
