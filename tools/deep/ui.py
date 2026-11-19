"""Pendalaman jalur UI Design: istilah dunia kerja dan contoh (perhitungan warna/tipografi dijalankan; CSS sebagai rujukan)."""
K = 'ui'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def C(t, code, b=None, lang='css'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


KONTRAS = '''def lum(hexw):
    r, g, b = (int(hexw.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def kontras(a, b):
    l1, l2 = sorted((lum(a), lum(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)
'''

D = {
'Hierarki visual': dict(
  ist=[('Visual weight', 'Seberapa kuat elemen menarik mata: ukuran, bobot huruf, warna, kontras.'),
       ('Squint test', 'Menyipitkan mata melihat layar; elemen yang masih terlihat adalah yang paling dominan.'),
       ('Emphasis budget', 'Hanya satu atau dua hal yang boleh paling menonjol per layar.'),
       ('Scannability', 'Kemudahan dipindai: judul jelas, paragraf pendek, angka penting menonjol.')],
  cx=[C('Satu kartu tagihan dengan tiga tingkat hierarki', '''
.tagihan        { padding: 16px; border-radius: 12px; background: var(--surface); }
.tagihan .label { font: 500 13px/1.4 var(--font); color: var(--text-muted); }          /* tingkat 3 */
.tagihan .jumlah{ font: 700 28px/1.2 var(--font); color: var(--text); margin: 4px 0; } /* tingkat 1 */
.tagihan .tempo { font: 500 14px/1.4 var(--font); color: var(--danger); }              /* tingkat 2 */
.tagihan .aksi  { margin-top: 16px; width: 100%; min-height: 48px; }                   /* aksi utama */

/* HTML: <p class="label">Tagihan listrik November</p>
         <p class="jumlah">Rp 487.500</p>
         <p class="tempo">Jatuh tempo 20 Nov · 1 hari lagi</p>
         <button class="aksi btn-primary">Bayar sekarang</button> */
''')]),

'Prinsip Gestalt': dict(
  ist=[('Proximity', 'Elemen yang berdekatan dianggap satu kelompok; jarak dalam kelompok harus lebih kecil dari jarak antarkelompok.'),
       ('Similarity', 'Elemen yang mirip (warna/bentuk) dianggap berfungsi sama.'),
       ('Common region', 'Elemen dalam satu bidang (kartu, latar) dianggap satu kelompok.'),
       ('Continuity & closure', 'Mata mengikuti garis dan melengkapi bentuk yang tidak utuh.')],
  cx=[P('Memeriksa aturan proximity: jarak dalam grup < jarak antargrup', '''
grup = {  # jarak vertikal (px) di form alamat
    "label-ke-input": 4, "antar-field dalam grup": 12, "antar-grup (Data diri -> Alamat)": 32,
}
ok = grup["label-ke-input"] < grup["antar-field dalam grup"] < grup["antar-grup (Data diri -> Alamat)"]
for k, v in grup.items():
    print(f"{k:34} {v:>3}px")
print("Proximity terjaga" if ok else "Kelompok ambigu: perbesar jarak antargrup")
''')]),

'Grid 8 poin': dict(
  ist=[('8pt grid', 'Semua ukuran dan jarak kelipatan 8 (dengan 4 untuk detail kecil) agar konsisten dan mudah dihitung.'),
       ('Spacing scale', 'Daftar jarak resmi: 4, 8, 12, 16, 24, 32, 48, 64.'),
       ('Baseline grid', 'Grid horizontal untuk menyelaraskan baris teks; line-height kelipatan 4.'),
       ('Column grid', 'Kolom dan gutter: misalnya 4 kolom di HP, 12 kolom di desktop.')],
  cx=[P('Membulatkan nilai liar ke skala 4/8', '''
SKALA = [0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80]
def ke_skala(px):
    return min(SKALA, key=lambda s: (abs(s - px), s))
liar = {"padding kartu": 15, "gap ikon-teks": 7, "margin section": 45, "radius": 10, "tinggi tombol": 46}
for nama, v in liar.items():
    print(f"{nama:15} {v:>3}px -> {ke_skala(v)}px")
print("Lebar kolom 360px, margin 16, 4 kolom, gutter 16:", (360 - 2 * 16 - 3 * 16) / 4, "px per kolom")
''')]),

'Perataan dan keseimbangan': dict(
  ist=[('Alignment', 'Menyelaraskan tepi atau pusat elemen; rata kiri paling mudah dibaca untuk teks Indonesia/Latin.'),
       ('Optical alignment', 'Penyesuaian kecil agar terlihat sejajar oleh mata (ikon play digeser sedikit).'),
       ('Symmetry vs asymmetry', 'Simetris terasa formal dan stabil; asimetris terasa dinamis.'),
       ('Tabular numbers', 'Angka berlebar sama (font-variant-numeric: tabular-nums) agar kolom nominal sejajar.')],
  cx=[C('Angka rupiah sejajar dengan tabular-nums dan rata kanan', '''
.mutasi td.nominal {
  text-align: right;
  font-variant-numeric: tabular-nums;     /* 1 dan 8 selebar yang sama */
  white-space: nowrap;
}
.mutasi td.keterangan { text-align: left; }
.ikon-play { transform: translateX(2px); } /* koreksi optik: segitiga terlihat lebih ke kiri */
''')]),

'Jarak untuk kepadatan dan keterbacaan': dict(
  ist=[('Density', 'Kepadatan informasi: compact (dashboard), comfortable (aplikasi umum), spacious (marketing).'),
       ('Breathing room', 'Ruang di sekitar elemen penting agar tidak terasa sesak.'),
       ('Internal ≤ external rule', 'Padding di dalam komponen tidak lebih besar dari jarak ke komponen lain.'),
       ('Density token', 'Token yang mengubah jarak sekaligus, misalnya density-compact untuk tabel admin.')],
  cx=[C('Satu tabel, tiga tingkat kepadatan lewat token', '''
:root            { --row-y: 12px; --row-x: 16px; --row-font: 14px; }
[data-density="compact"]  { --row-y: 6px;  --row-x: 12px; --row-font: 13px; }
[data-density="spacious"] { --row-y: 16px; --row-x: 20px; --row-font: 15px; }

.tabel td { padding: var(--row-y) var(--row-x); font-size: var(--row-font); }
/* Admin gudang memilih compact (lebih banyak baris terlihat), pengguna umum tetap default. */
''')]),

'Memilih typeface': dict(
  ist=[('Typeface vs font', 'Typeface = keluarga desain (Inter); font = satu berkas/varian (Inter Bold 16).'),
       ('Variable font', 'Satu berkas berisi banyak bobot/lebar; hemat ukuran unduhan.'),
       ('x-height', 'Tinggi huruf kecil; x-height besar lebih terbaca di ukuran kecil layar.'),
       ('Font pairing', 'Kombinasi maksimal dua keluarga, misalnya serif untuk judul dan sans untuk isi.')],
  cx=[C('Memuat font dengan aman dan cepat', '''
/* Google Fonts: hanya bobot yang dipakai, display=swap agar teks langsung tampil */
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap");

:root {
  --font-sans: "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "JetBrains Mono", Menlo, monospace;
}
body { font-family: var(--font-sans); }
/* Plus Jakarta Sans: dirancang di Indonesia, x-height cukup tinggi, lisensi OFL (bebas komersial). */
''')]),

'Skala tipe modular': dict(
  ist=[('Modular scale', 'Ukuran huruf dari rasio tetap: 1.125 (major second), 1.2 (minor third), 1.25 (major third).'),
       ('Base size', 'Ukuran dasar teks isi, biasanya 16px di web.'),
       ('Type ramp', 'Daftar ukuran resmi yang boleh dipakai: caption, body, title, headline, display.'),
       ('Rounding', 'Hasil skala dibulatkan ke angka genap/kelipatan 2 agar rapi di grid.')],
  cx=[P('Membangkitkan skala tipe dengan dua rasio', '''
base = 16
nama = ["caption", "body", "title-sm", "title", "headline", "display"]
for rasio in (1.2, 1.25):
    ukuran = [base * rasio ** i for i in range(-1, len(nama) - 1)]
    print(f"rasio {rasio}:", ", ".join(f"{n}={round(u / 2) * 2}px" for n, u in zip(nama, ukuran)))
print("Mobile biasanya memakai rasio lebih kecil (1.2), desktop lebih besar (1.25-1.333).")
''')]),

'Line height, tracking, dan panjang baris': dict(
  ist=[('Line height (leading)', 'Jarak antarbaris; 1.4-1.6 untuk isi, 1.1-1.3 untuk judul besar.'),
       ('Tracking / letter-spacing', 'Jarak antarhuruf; perlebar sedikit untuk huruf kapital kecil, rapatkan untuk display besar.'),
       ('Measure', 'Panjang baris ideal 45-80 karakter; gunakan max-width: 65ch.'),
       ('Widow / orphan', 'Kata tunggal yang tertinggal di baris terakhir; text-wrap: pretty membantu.')],
  cx=[C('Pengaturan teks artikel yang nyaman dibaca', '''
.artikel p {
  font-size: 1rem;
  line-height: 1.6;
  max-width: 65ch;              /* ± 65 karakter per baris */
  text-wrap: pretty;            /* kurangi kata yatim di akhir paragraf */
}
.artikel h1 { font-size: clamp(1.75rem, 4vw, 2.5rem); line-height: 1.15; letter-spacing: -0.02em; text-wrap: balance; }
.eyebrow    { font-size: .75rem; text-transform: uppercase; letter-spacing: .08em; }
''')]),

'Peran tipografi semantik': dict(
  ist=[('Semantic type token', 'Nama berdasarkan peran (title-lg, body-md, label-sm), bukan ukuran (font-24).'),
       ('Type role', 'Display, headline, title, body, label: lima peran di Material 3.'),
       ('Heading level vs visual size', 'h2 boleh tampil kecil; tingkat heading untuk struktur, ukuran untuk visual.'),
       ('Text style', 'Gabungan font, ukuran, bobot, line-height, dan tracking yang disimpan sebagai satu gaya di Figma.')],
  cx=[C('Token tipografi semantik dipakai di CSS', '''
:root {
  --type-headline-md: 700 1.75rem/1.25 var(--font-sans);
  --type-title-md:    600 1.125rem/1.4 var(--font-sans);
  --type-body-md:     400 1rem/1.6 var(--font-sans);
  --type-label-sm:    600 .75rem/1.3 var(--font-sans);
}
.judul-halaman { font: var(--type-headline-md); }
.kartu h3      { font: var(--type-title-md); }   /* h3 secara struktur, title secara visual */
.badge         { font: var(--type-label-sm); letter-spacing: .04em; }
''')]),

'Tipografi responsif': dict(
  ist=[('Fluid typography', 'Ukuran huruf tumbuh mulus antara batas minimum dan maksimum dengan clamp().'),
       ('rem vs px', 'rem mengikuti pengaturan ukuran huruf pengguna; px tidak. Gunakan rem untuk aksesibilitas.'),
       ('Dynamic Type', 'Pengaturan ukuran huruf sistem di iOS (dan font scale di Android) yang harus dihormati aplikasi.'),
       ('Reflow (WCAG 1.4.10)', 'Konten tetap bisa dibaca tanpa scroll horizontal di lebar 320 CSS px atau zoom 400%.')],
  cx=[P('Menghitung clamp() dari ukuran di dua lebar layar', '''
def fluid(min_px, max_px, vw_min=360, vw_max=1280, root=16):
    kemiringan = (max_px - min_px) / (vw_max - vw_min)
    potong = min_px - kemiringan * vw_min
    return f"clamp({min_px / root:.3f}rem, {potong / root:.3f}rem + {kemiringan * 100:.3f}vw, {max_px / root:.3f}rem)"
for nama, a, b in [("display", 32, 56), ("headline", 24, 36), ("body", 16, 18)]:
    print(f"--fs-{nama}: {fluid(a, b)};")
''')]),

'Properti warna dan model warna layar': dict(
  ist=[('HEX / RGB', 'Model warna layar berbasis merah-hijau-biru.'),
       ('HSL', 'Hue, saturation, lightness; mudah dibaca manusia tetapi lightness-nya tidak seragam secara persepsi.'),
       ('OKLCH', 'Model warna perseptual modern di CSS: lightness yang sama terlihat sama terang di semua hue.'),
       ('Display P3', 'Ruang warna lebih luas dari sRGB pada layar modern (iPhone, MacBook).')],
  cx=[P('HEX ke RGB dan HSL dengan colorsys', '''
import colorsys
warna = {"Hijau brand": "#0F766E", "Oranye aksen": "#EA580C", "Abu teks": "#334155"}
for nama, h in warna.items():
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    hh, ll, ss = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    print(f"{nama:13} {h}  rgb({r}, {g}, {b})  hsl({hh * 360:.0f}, {ss:.0%}, {ll:.0%})")
print("CSS modern: color: oklch(51% 0.09 185); /* setara kira-kira hijau brand */")
''')]),

'Kontras WCAG': dict(
  ist=[('Contrast ratio', 'Perbandingan luminans dua warna, dari 1:1 sampai 21:1.'),
       ('AA normal text 4.5:1', 'Syarat minimum teks biasa; teks besar (≥ 24px atau ≥ 18,66px tebal) cukup 3:1.'),
       ('Non-text contrast 3:1', 'Batas komponen UI (border input, ikon penting, fokus) minimal 3:1 terhadap sekitarnya.'),
       ('APCA', 'Metode kontras baru yang dikembangkan untuk WCAG 3; belum menjadi standar resmi.')],
  cx=[P('Menghitung rasio kontras dan status AA', KONTRAS + '''
pasangan = [("#FFFFFF", "#0F766E", "teks putih di tombol hijau"), ("#FFFFFF", "#14B8A6", "teks putih di hijau muda"),
            ("#64748B", "#FFFFFF", "teks abu di putih"), ("#94A3B8", "#FFFFFF", "placeholder abu muda"),
            ("#CBD5E1", "#FFFFFF", "border input")]
for fg, bg, ket in pasangan:
    r = kontras(fg, bg)
    status = "AA teks" if r >= 4.5 else "AA teks besar/UI" if r >= 3 else "GAGAL"
    print(f"{r:5.2f}:1  {status:17} {ket}")
''')]),

'Palet tint dan shade': dict(
  ist=[('Tint / shade', 'Warna dicampur putih (lebih terang) atau hitam (lebih gelap).'),
       ('Tonal palette', 'Skala 50-950 atau 0-100 dari satu hue, dipakai untuk latar, border, teks, state.'),
       ('Perceptual uniformity', 'Langkah antartingkat terlihat sama besar; lebih mudah dicapai di OKLCH dari HSL.'),
       ('color-mix()', 'Fungsi CSS untuk mencampur warna langsung di browser.')],
  cx=[P('Membangkitkan skala tonal dari satu warna brand', KONTRAS + '''
def campur(h, target, t):
    a = [int(h[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(target[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(a, b))

brand = "#0F766E"
skala = {50: campur(brand, "#FFFFFF", .92), 100: campur(brand, "#FFFFFF", .82), 300: campur(brand, "#FFFFFF", .5),
         500: campur(brand, "#FFFFFF", .15), 600: brand, 700: campur(brand, "#000000", .2), 900: campur(brand, "#000000", .5)}
for k, v in skala.items():
    print(f"teal-{k:<3} {v}  kontras vs putih {kontras(v, '#FFFFFF'):5.2f}  vs hitam {kontras(v, '#000000'):5.2f}")
''')]),

'Warna semantik untuk state': dict(
  ist=[('Semantic color', 'Warna berdasarkan makna: success, warning, danger, info.'),
       ('Don\'t rely on color alone (WCAG 1.4.1)', 'Status juga ditandai ikon dan teks, bukan warna saja.'),
       ('Container color', 'Latar lembut untuk pesan status (danger-container) dengan teks yang tetap kontras.'),
       ('Color blindness', 'Sekitar 8% laki-laki memiliki defisiensi warna merah-hijau; uji dengan simulator.')],
  cx=[C('Banner status: warna + ikon + teks', '''
:root {
  --success: #15803D; --success-container: #DCFCE7;
  --warning: #A16207; --warning-container: #FEF9C3;
  --danger:  #B91C1C; --danger-container:  #FEE2E2;
}
.banner { display: flex; gap: 8px; padding: 12px 16px; border-radius: 8px; border-left: 4px solid; }
.banner.danger  { background: var(--danger-container);  color: var(--danger);  border-color: var(--danger); }
.banner.success { background: var(--success-container); color: var(--success); border-color: var(--success); }
/* <div class="banner danger" role="alert"><svg aria-hidden="true">…</svg>
     <span><b>Pembayaran gagal.</b> Saldo tidak cukup. Isi saldo lalu coba lagi.</span></div> */
''')]),

'Dark mode': dict(
  ist=[('Elevation by lightness', 'Di mode gelap, permukaan yang lebih tinggi dibuat sedikit lebih terang, bukan memakai bayangan.'),
       ('Desaturated accent', 'Warna aksen jenuh terlalu menyilaukan di latar gelap; turunkan saturasi/naikkan lightness.'),
       ('prefers-color-scheme', 'Media query untuk mengikuti pengaturan sistem pengguna.'),
       ('Avoid pure black', 'Latar #121212 atau sejenis lebih nyaman dari #000 murni dan mengurangi efek smearing di OLED.')],
  cx=[C('Token terang/gelap dengan pilihan manual', '''
:root {
  --bg: #FFFFFF; --surface: #F8FAFC; --text: #0F172A; --muted: #475569; --accent: #0F766E;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0B1220; --surface: #131C2E; --text: #E2E8F0; --muted: #94A3B8; --accent: #2DD4BF;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #0B1220; --surface: #131C2E; --text: #E2E8F0; --muted: #94A3B8; --accent: #2DD4BF;
  color-scheme: dark;
}
body { background: var(--bg); color: var(--text); }
''')]),

'Anatomi input form': dict(
  ist=[('Label', 'Teks di atas field yang selalu terlihat; placeholder bukan pengganti label.'),
       ('Helper text', 'Petunjuk format di bawah field ("Contoh: 0812 3456 7890").'),
       ('Error message', 'Pesan spesifik yang menempel pada field dan diumumkan pembaca layar (aria-describedby).'),
       ('Input mode', 'inputmode/type yang memunculkan keyboard tepat (tel, numeric, email).')],
  cx=[C('Field nomor HP yang lengkap dan aksesibel', '''
<div class="field">
  <label for="hp">Nomor HP</label>
  <input id="hp" name="hp" type="tel" inputmode="tel" autocomplete="tel"
         aria-describedby="hp-bantu hp-galat" aria-invalid="true" value="0812">
  <p id="hp-bantu" class="helper">Diawali 08 atau +62, 10-13 digit</p>
  <p id="hp-galat" class="error">Nomor HP terlalu pendek. Tambahkan 6 digit lagi.</p>
</div>
''', lang='html')]),

'State dan hierarki tombol': dict(
  ist=[('Button hierarchy', 'Primary (satu per layar), secondary, tertiary/text, destructive.'),
       ('Interactive states', 'Default, hover, focus-visible, pressed, disabled, loading.'),
       ('Focus visible', 'Cincin fokus jelas untuk pengguna keyboard; jangan dihapus dengan outline: none tanpa pengganti.'),
       ('Loading state', 'Tombol menampilkan spinner dan mencegah klik ganda saat proses berjalan.')],
  cx=[C('Semua state tombol primer', '''
.btn-primary { min-height: 48px; padding: 0 20px; border-radius: 10px; border: 0;
               background: var(--accent); color: #fff; font-weight: 600; cursor: pointer; }
.btn-primary:hover          { background: color-mix(in oklch, var(--accent), black 12%); }
.btn-primary:active         { transform: translateY(1px); }
.btn-primary:focus-visible  { outline: 3px solid color-mix(in oklch, var(--accent), white 40%); outline-offset: 2px; }
.btn-primary:disabled,
.btn-primary[aria-disabled="true"] { background: var(--disabled-bg); color: var(--disabled-fg); cursor: not-allowed; }
.btn-primary[aria-busy="true"]     { pointer-events: none; }
.btn-primary[aria-busy="true"]::before { content: ""; width: 16px; height: 16px; margin-right: 8px;
  border: 2px solid currentColor; border-right-color: transparent; border-radius: 50%; display: inline-block;
  animation: putar .8s linear infinite; }
@keyframes putar { to { transform: rotate(1turn); } }
@media (prefers-reduced-motion: reduce) { .btn-primary[aria-busy="true"]::before { animation: none; } }
''')]),

'Kartu': dict(
  ist=[('Card', 'Wadah berisi satu topik: gambar, judul, ringkasan, aksi.'),
       ('Whole-card link', 'Seluruh kartu bisa diklik dengan teknik pseudo-element pada link utama, tanpa membungkus semua dengan <a>.'),
       ('Media aspect ratio', 'aspect-ratio menjaga gambar tidak melompat saat dimuat (mengurangi CLS).'),
       ('Elevation', 'Kesan ketinggian lewat bayangan atau border; jangan berlebihan.')],
  cx=[C('Kartu produk yang seluruhnya bisa diklik', '''
.kartu { position: relative; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; background: var(--surface); }
.kartu img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; display: block; }
.kartu .isi { padding: 12px; display: grid; gap: 4px; }
.kartu a.judul::after { content: ""; position: absolute; inset: 0; }   /* area klik = seluruh kartu */
.kartu a.judul:focus-visible { outline: none; }
.kartu:has(a.judul:focus-visible) { outline: 3px solid var(--accent); outline-offset: 2px; }
.kartu .harga { font-weight: 700; font-variant-numeric: tabular-nums; }
''')]),

'Modal, sheet, dan popover': dict(
  ist=[('Modal dialog', 'Menghentikan alur utama sampai pengguna merespons; untuk keputusan penting saja.'),
       ('Bottom sheet', 'Panel dari bawah di mobile; lebih mudah dijangkau jempol.'),
       ('Popover API', 'Atribut popover di HTML untuk menu/tooltip tanpa JavaScript tambahan.'),
       ('Focus trap & restore', 'Fokus tetap di dalam modal saat terbuka dan kembali ke tombol pemicu saat ditutup; <dialog> menanganinya.')],
  cx=[C('Dialog konfirmasi dengan elemen <dialog> bawaan', '''
<button id="hapus" class="btn-danger">Hapus alamat</button>

<dialog id="konfirmasi" aria-labelledby="judul-k">
  <h2 id="judul-k">Hapus alamat "Rumah"?</h2>
  <p>Alamat ini tidak bisa dipulihkan. Pesanan yang sedang berjalan tidak terpengaruh.</p>
  <form method="dialog" class="aksi">
    <button value="batal" autofocus>Batal</button>
    <button value="hapus" class="btn-danger">Hapus</button>
  </form>
</dialog>

<script>
  const d = document.getElementById("konfirmasi");
  document.getElementById("hapus").onclick = () => d.showModal();   // fokus terkunci + Esc menutup
  d.addEventListener("close", () => { if (d.returnValue === "hapus") hapusAlamat(); });
</script>
''', lang='html')]),

'Auto layout dan batasan tata letak dinamis': dict(
  ist=[('Auto layout (Figma)', 'Frame yang menyusun anaknya otomatis seperti flexbox: arah, gap, padding, alignment.'),
       ('Hug / Fill / Fixed', 'Ukuran mengikuti isi, memenuhi ruang, atau tetap; padanan CSS: fit-content, flex:1, width tetap.'),
       ('Constraints', 'Aturan posisi elemen saat frame induk berubah ukuran.'),
       ('Min/max width', 'Batas agar komponen tidak terlalu sempit atau terlalu lebar.')],
  cx=[C('Padanan auto layout Figma di CSS', '''
/* Figma: Auto layout horizontal, gap 12, padding 16, align center
   - avatar: Fixed 40x40
   - teks  : Fill container
   - badge : Hug contents                                            */
.baris-chat { display: flex; align-items: center; gap: 12px; padding: 16px; }
.baris-chat .avatar { flex: none; width: 40px; height: 40px; border-radius: 50%; }
.baris-chat .teks   { flex: 1; min-width: 0; }           /* Fill + izinkan teks terpotong */
.baris-chat .teks p { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.baris-chat .badge  { flex: none; width: fit-content; }   /* Hug */
''')]),

'Fondasi design token': dict(
  ist=[('Design token', 'Nilai desain bernama (warna, jarak, radius, bayangan, durasi) yang dipakai desain dan kode.'),
       ('Figma Variables', 'Fitur Figma untuk menyimpan token dengan mode (light/dark, brand).'),
       ('Style Dictionary', 'Alat yang mengubah token JSON menjadi CSS, Swift, Kotlin, dan format lain.'),
       ('Hard-coded value', 'Nilai langsung (#0F766E, 16px) di komponen; sulit diubah serentak.')],
  cx=[P('Mengubah token JSON menjadi CSS variables', '''
import json
token = json.loads("""{
  "color": {"brand": {"600": "#0F766E"}, "text": {"default": "{color.neutral.900}"}, "neutral": {"900": "#0F172A"}},
  "space": {"2": "8px", "4": "16px"},
  "radius": {"md": "10px"}
}""")
def ratakan(d, awal=""):
    for k, v in d.items():
        nama = f"{awal}-{k}" if awal else k
        yield from ratakan(v, nama) if isinstance(v, dict) else [(nama, v)]
def css_nilai(v):
    return f"var(--{v[1:-1].replace('.', '-')})" if v.startswith("{") else v
print(":root {")
for nama, v in ratakan(token):
    print(f"  --{nama}: {css_nilai(v)};")
print("}")
''')]),

'Penamaan token global dan alias': dict(
  ist=[('Global / primitive token', 'Nilai mentah: blue-600, space-4.'),
       ('Alias / semantic token', 'Nama peran yang merujuk primitive: color.action.primary → blue-600.'),
       ('Component token', 'Token khusus komponen: button.primary.bg → color.action.primary.'),
       ('Naming convention', 'Pola konsisten, misalnya kategori.peran.varian.state (color.text.danger.hover).')],
  cx=[P('Menyelesaikan rantai alias tiga lapis', '''
token = {
    "blue.600": "#2563EB", "teal.600": "#0F766E",
    "color.action.primary": "{teal.600}",            # semantic
    "button.primary.bg": "{color.action.primary}",   # component
    "link.color": "{color.action.primary}",
}
def resolve(nama, jejak=None):
    jejak = (jejak or []) + [nama]
    v = token[nama]
    return resolve(v[1:-1], jejak) if v.startswith("{") else (v, jejak)
for k in ("button.primary.bg", "link.color"):
    nilai, jejak = resolve(k)
    print(" -> ".join(jejak), "=", nilai)
token["teal.600"] = "#0D9488"                         # rebrand: ubah satu primitive
print("setelah rebrand:", resolve("button.primary.bg")[0], resolve("link.color")[0])
''')]),

'Varian dan properti komponen': dict(
  ist=[('Variant', 'Versi komponen berdasarkan properti: size=sm/md/lg, hierarchy=primary/secondary.'),
       ('Component property', 'Properti di Figma: boolean (ada ikon?), text (label), instance swap (ganti ikon).'),
       ('Combinatorial explosion', 'Jumlah varian meledak bila semua kombinasi digambar; gunakan properti, bukan varian, untuk hal sederhana.'),
       ('Prop API parity', 'Nama properti di Figma sama dengan props di kode (size, variant, iconStart).')],
  cx=[P('Menghitung ledakan varian dan cara menekannya', '''
from itertools import product
dimensi = {"hierarchy": ["primary", "secondary", "tertiary", "danger"], "size": ["sm", "md", "lg"],
           "state": ["default", "hover", "focus", "pressed", "disabled", "loading"], "icon": ["none", "start", "end", "only"]}
semua = list(product(*dimensi.values()))
print("varian jika semua digambar:", len(semua))
varian = len(dimensi["hierarchy"]) * len(dimensi["size"]) * len(dimensi["state"])
print("ikon jadi boolean + instance swap (bukan varian):", varian)
print("state hover/pressed diserahkan ke prototipe interaktif:", len(dimensi["hierarchy"]) * len(dimensi["size"]) * 4)
''')]),

'Set ikon dan aset': dict(
  ist=[('Icon grid', 'Kanvas ikon tetap (24x24) dengan area aman (2px) agar semua ikon seimbang.'),
       ('Stroke consistency', 'Ketebalan garis sama (1.5 atau 2px) di semua ikon.'),
       ('SVG sprite / icon component', 'Cara menyajikan ikon di kode tanpa banyak request.'),
       ('Export settings', 'Ekspor aset: SVG untuk ikon, WebP/AVIF untuk foto, 1x/2x/3x untuk mobile.')],
  cx=[C('Ikon SVG yang mewarisi warna teks dan aksesibel', '''
<!-- ikon dekoratif: disembunyikan dari pembaca layar -->
<button class="btn-ikon" aria-label="Tambah ke keranjang">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
       stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/>
    <path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h8.6a2 2 0 0 0 2-1.6L22 7H6"/>
  </svg>
</button>
<style>.btn-ikon { width: 48px; height: 48px; display: grid; place-items: center; color: var(--text); }</style>
''', lang='html')]),

'Dokumentasi pedoman pola': dict(
  ist=[('Usage guideline', 'Kapan memakai dan kapan tidak memakai komponen/pola.'),
       ('Do / Don\'t', 'Contoh benar dan salah berdampingan; cara paling cepat dipahami.'),
       ('Pattern', 'Gabungan komponen untuk masalah berulang: form multi-langkah, empty state, pencarian.'),
       ('Content guideline', 'Aturan teks: sapaan, kapitalisasi, panjang label tombol.')],
  cx=[C('Template halaman pedoman komponen (Markdown)', '''
# Toast

Pesan singkat yang muncul sementara untuk mengonfirmasi aksi yang **berhasil**.

## Kapan dipakai
- Konfirmasi aksi yang bisa diurungkan: "Alamat dihapus · Urungkan"
- Status yang tidak butuh tindakan

## Jangan dipakai
- Error yang harus diperbaiki pengguna → gunakan pesan inline di field
- Informasi penting yang harus dibaca → gunakan banner

## Do / Don't
| Do                                   | Don't                                  |
|--------------------------------------|----------------------------------------|
| "Disimpan" (1-2 kata kerja)          | "Data Anda telah berhasil disimpan!"   |
| Tampil 4-6 detik, berhenti saat hover | Hilang 1 detik sebelum terbaca         |

## Aksesibilitas
`role="status"` + `aria-live="polite"`; tombol Urungkan bisa dijangkau keyboard.
''', lang='markdown')]),

'Breakpoint fluid dan aturan container': dict(
  ist=[('Breakpoint', 'Lebar tempat tata letak berubah, misalnya 600, 905, 1240 px (Material) atau 640/768/1024/1280 (Tailwind).'),
       ('Content-out breakpoint', 'Breakpoint ditentukan saat konten mulai rusak, bukan dari ukuran perangkat populer.'),
       ('Container query', 'Gaya komponen berubah berdasarkan lebar wadahnya, bukan lebar layar.'),
       ('Max content width', 'Batas lebar konten (misal 1200px) agar baris tidak terlalu panjang di layar lebar.')],
  cx=[C('Kartu yang berubah tata letak berdasarkan wadahnya', '''
.daftar { container-type: inline-size; }

.kartu-produk { display: grid; gap: 12px; }
@container (min-width: 520px) {
  .kartu-produk { grid-template-columns: 160px 1fr; align-items: center; }
}
.halaman { width: min(100% - 32px, 1200px); margin-inline: auto; }  /* gutter 16px + batas 1200px */
''')]),

'Pola navigasi mobile': dict(
  ist=[('Bottom navigation bar', '3-5 tujuan utama di bawah layar, selalu dengan label.'),
       ('Tab bar vs navigation drawer', 'Tab untuk tujuan sejajar yang sering dipakai; drawer untuk banyak tujuan jarang.'),
       ('Back behavior', 'Tombol kembali Android/gesture iOS harus kembali ke layar sebelumnya secara logis.'),
       ('Predictive back', 'Animasi pratinjau tujuan saat gesture kembali di Android 14+.')],
  cx=[P('Memilih pola navigasi dari jumlah dan frekuensi tujuan', '''
def pilih(tujuan):
    sering = [t for t, f in tujuan if f == "sering"]
    if 3 <= len(sering) <= 5:
        return f"Bottom nav: {', '.join(sering)}" + (f" + menu 'Lainnya' untuk {len(tujuan) - len(sering)} tujuan" if len(tujuan) > len(sering) else "")
    if len(sering) < 3:
        return "Satu layar utama + tombol/tautan; bottom nav berlebihan"
    return "Navigation drawer / rail; kelompokkan tujuan"
app_bank = [("Beranda", "sering"), ("Transfer", "sering"), ("Riwayat", "sering"), ("Profil", "sering"),
            ("Kartu", "jarang"), ("Investasi", "jarang"), ("Bantuan", "jarang")]
app_kalkulator = [("Kalkulator", "sering"), ("Riwayat", "jarang")]
print("Bank      :", pilih(app_bank))
print("Kalkulator:", pilih(app_kalkulator))
''')]),

'Layout dashboard desktop': dict(
  ist=[('KPI card', 'Kartu angka utama dengan pembanding (vs minggu lalu) dan arah tren.'),
       ('F-layout dashboard', 'KPI terpenting di kiri atas, detail di bawah.'),
       ('Data density', 'Dashboard boleh padat, tetapi tetap ada hierarki dan ruang kosong.'),
       ('Responsive table', 'Tabel lebar di layar kecil: scroll horizontal dengan kolom pertama sticky, atau berubah jadi kartu.')],
  cx=[C('Grid dashboard: sidebar, KPI, grafik, tabel', '''
.dasbor {
  display: grid; gap: 16px; min-height: 100dvh;
  grid-template-columns: 240px 1fr;
  grid-template-areas: "nav kpi" "nav grafik" "nav tabel";
}
.kpi    { grid-area: kpi; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }
.grafik { grid-area: grafik; min-height: 320px; }
.tabel  { grid-area: tabel; overflow-x: auto; }
.tabel th:first-child, .tabel td:first-child { position: sticky; left: 0; background: var(--surface); }
@media (max-width: 900px) {
  .dasbor { grid-template-columns: 1fr; grid-template-areas: "kpi" "grafik" "tabel"; }
  nav { display: none; } /* diganti bottom nav / drawer */
}
''')]),

'Redlining dan spesifikasi': dict(
  ist=[('Redline', 'Anotasi ukuran, jarak, warna, dan font di atas desain untuk developer.'),
       ('Dev Mode', 'Mode Figma untuk developer: inspeksi token, kode CSS/iOS/Android, status "ready for dev".'),
       ('Annotation', 'Catatan perilaku: validasi, animasi, batas karakter, state kosong.'),
       ('Spec drift', 'Perbedaan desain dan hasil implementasi yang menumpuk; dicegah dengan token dan design QA.')],
  cx=[C('Spesifikasi komponen yang bisa langsung dipakai developer', '''
KOMPONEN   : Kartu tagihan (BillCard)
UKURAN     : lebar fill, padding space.4 (16), radius radius.lg (12), gap space.1 (4)
WARNA      : bg color.surface.raised · label color.text.muted · jumlah color.text.default
TIPOGRAFI  : label type.label.md · jumlah type.headline.sm (tabular-nums) · tempo type.body.sm
STATE      : normal | jatuh tempo ≤ 3 hari → tempo color.text.danger + ikon jam
             lunas → badge "Lunas" color.success, tombol diganti "Lihat struk"
             memuat → skeleton 3 baris
PERILAKU   : jumlah > 12 digit → turunkan ke type.title.lg; nama tagihan maks 2 baris lalu ellipsis
AKSESIBEL  : seluruh kartu satu tautan; label pembaca layar "Tagihan listrik, Rp487.500, jatuh tempo besok"
''', lang='text')]),

'Sesi handoff kolaboratif': dict(
  ist=[('Handoff', 'Serah terima desain ke developer; idealnya kolaborasi berkelanjutan, bukan sekali lempar.'),
       ('Design QA', 'Desainer memeriksa hasil build di perangkat nyata sebelum rilis.'),
       ('Ready for dev', 'Status di Figma yang menandai bagian desain sudah final untuk dikerjakan.'),
       ('Definition of ready', 'Syarat desain siap: semua state, copy final, token, aksesibilitas, edge case.')],
  cx=[P('Checklist definition of ready otomatis', '''
desain = {
    "semua state (kosong, memuat, error, sukses)": True, "copy final disetujui": True, "memakai token, tanpa nilai liar": False,
    "target sentuh >= 44/48": True, "kontras AA dicek": True, "layout 360px dan 1280px": False,
    "anotasi perilaku & validasi": True, "aset diekspor": True,
}
belum = [k for k, v in desain.items() if not v]
print(f"siap: {len(desain) - len(belum)}/{len(desain)}")
for k in belum:
    print("  BELUM:", k)
print("Status:", "Ready for dev" if not belum else "Belum siap diserahkan")
''')]),

'Langkah 1: brief, masalah, dan target': dict(
  ist=[('Design brief', 'Dokumen singkat: latar belakang, masalah, pengguna, tujuan, batasan, jadwal.'),
       ('Problem statement', '"[Pengguna] kesulitan [apa] karena [penyebab], sehingga [dampak]."'),
       ('Success metric', 'Ukuran keberhasilan yang disepakati sebelum mendesain.'),
       ('Constraint', 'Batasan teknis, waktu, brand, regulasi.')],
  cx=[C('Brief satu halaman: aplikasi antrean puskesmas', '''
PROYEK      Aplikasi antrean online Puskesmas Kota (Android, web)
MASALAH     Pasien lansia antre 2-3 jam sejak subuh karena tidak tahu kapan gilirannya,
            sehingga ruang tunggu penuh dan risiko penularan naik.
PENGGUNA    Pasien umum & BPJS (banyak lansia, HP entry-level), petugas loket
TUJUAN      Waktu tunggu di lokasi turun dari ± 150 ke ≤ 45 menit
METRIK      % pasien datang ≤ 30 menit sebelum giliran · SUS ≥ 70 · keluhan loket turun
BATASAN     4 minggu, 1 developer Flutter, wajib bisa via WhatsApp/SMS untuk yang tanpa smartphone
''', lang='text')]),

'Langkah 2: riset cepat, benchmark, dan moodboard': dict(
  ist=[('Guerrilla research', 'Riset cepat dan murah: wawancara singkat di lokasi nyata.'),
       ('Benchmark', 'Membandingkan alur produk sejenis untuk mencari pola dan celah.'),
       ('Moodboard', 'Kumpulan referensi visual untuk menyepakati nuansa (tenang, ramah, terpercaya).'),
       ('Insight', 'Temuan yang menjelaskan kenapa, bukan hanya apa.')],
  cx=[P('Merangkum catatan riset cepat menjadi tema', '''
from collections import Counter
catatan = ["takut kelewatan dipanggil", "tidak paham aplikasi", "datang subuh biar dapat nomor", "anak yang daftarkan",
           "takut kelewatan dipanggil", "ingin tahu estimasi jam", "HP sering habis kuota", "anak yang daftarkan",
           "ingin tahu estimasi jam", "takut kelewatan dipanggil"]
tema = {"takut kelewatan dipanggil": "Kecemasan giliran", "ingin tahu estimasi jam": "Kecemasan giliran",
        "datang subuh biar dapat nomor": "Kecemasan giliran", "anak yang daftarkan": "Didampingi keluarga",
        "tidak paham aplikasi": "Literasi digital", "HP sering habis kuota": "Akses terbatas"}
for t, n in Counter(tema[c] for c in catatan).most_common():
    print(f"{n:>2}x {t}")
print("Insight: pasien datang subuh bukan karena suka, tetapi karena tidak ada kepastian jam giliran.")
''')]),

'Langkah 3: user flow dan wireframe': dict(
  ist=[('User flow', 'Diagram langkah pengguna dari titik masuk sampai tujuan, termasuk cabang dan error.'),
       ('Happy path & edge case', 'Jalur normal dan kasus tepi (nomor habis, sesi kedaluwarsa).'),
       ('Low-fi wireframe', 'Kerangka abu-abu untuk membahas struktur, bukan warna.'),
       ('Entry point', 'Cara pengguna masuk ke alur: notifikasi, tautan WhatsApp, beranda.')],
  cx=[C('User flow ambil antrean dalam notasi teks', '''
[Buka aplikasi / tautan WA]
      |
      v
<Sudah login?> --tidak--> [Masuk dengan nomor HP + OTP] --gagal 3x--> [Bantuan via loket]
      | ya
      v
[Pilih poli] --> <Kuota hari ini habis?> --ya--> [Tawarkan jadwal besok + pengingat]
      | tidak
      v
[Pilih pasien: diri sendiri / keluarga] --> [Konfirmasi] --> [Nomor A-027 · estimasi 10.40]
      |
      v
[Notifikasi 30 menit sebelum giliran] --> [Check-in di lokasi via QR]
''', lang='text')]),

'Langkah 4: style guide (warna, tipografi, jarak)': dict(
  ist=[('Style guide', 'Ringkasan fondasi visual: palet, skala tipe, jarak, radius, ikon, nada visual.'),
       ('Brand color vs UI color', 'Warna brand untuk identitas; warna UI untuk fungsi (aksi, status).'),
       ('Accessibility check', 'Semua pasangan teks-latar di style guide sudah lolos kontras AA.'),
       ('Tokens first', 'Style guide ditulis sebagai token agar langsung bisa dipakai developer.')],
  cx=[P('Memvalidasi semua pasangan warna style guide', KONTRAS + '''
palet = {"bg": "#FFFFFF", "surface": "#F1F5F9", "text": "#0F172A", "muted": "#475569",
         "primary": "#0F766E", "on_primary": "#FFFFFF", "danger": "#B91C1C"}
pasangan = [("text", "bg"), ("muted", "bg"), ("muted", "surface"), ("on_primary", "primary"), ("danger", "bg"), ("primary", "surface")]
for fg, bg in pasangan:
    r = kontras(palet[fg], palet[bg])
    print(f"{fg:>10} di {bg:<8} {r:5.2f}:1  {'lolos AA' if r >= 4.5 else 'cek ulang'}")
''')]),

'Langkah 5: komponen, varian, dan auto layout': dict(
  ist=[('Component inventory', 'Daftar komponen yang dibutuhkan dari semua layar wireframe.'),
       ('Atomic design', 'Atom (tombol), molekul (field), organisme (form), template, halaman.'),
       ('Instance', 'Salinan komponen di layar; berubah otomatis saat komponen induk diubah.'),
       ('Slot', 'Area fleksibel di komponen yang bisa diisi konten lain (properti slot di Figma).')],
  cx=[P('Inventaris komponen dari daftar layar', '''
layar = {
    "Login": ["AppBar", "TextField", "Button", "Link"],
    "Pilih poli": ["AppBar", "SearchField", "ListItem", "Chip", "BottomNav"],
    "Konfirmasi": ["AppBar", "Card", "RadioGroup", "Button"],
    "Tiket antrean": ["AppBar", "Card", "QRCode", "Button", "Banner", "BottomNav"],
    "Riwayat": ["AppBar", "ListItem", "EmptyState", "BottomNav"],
}
from collections import Counter
hitung = Counter(k for ks in layar.values() for k in ks)
print("Komponen (dipakai di berapa layar):")
for k, n in hitung.most_common():
    print(f"  {k:12} {n}")
print("Bangun dulu yang dipakai >= 3 layar:", [k for k, n in hitung.items() if n >= 3])
''')]),

'Langkah 6: desain hi-fi, state layar, dan prototipe': dict(
  ist=[('High-fidelity', 'Desain final dengan warna, tipografi, konten asli, dan semua state.'),
       ('Screen states', 'Ideal, kosong, memuat, sebagian, error, offline, konten sangat panjang.'),
       ('Prototype interaction', 'Transisi dan animasi mikro yang menjelaskan perubahan (150-300 ms).'),
       ('Realistic content', 'Nama, angka, dan teks asli Indonesia, bukan lorem ipsum.')],
  cx=[P('Matriks state yang wajib ada per layar', '''
STATE = ["ideal", "kosong", "memuat", "error", "offline", "teks panjang"]
punya = {
    "Pilih poli": {"ideal", "memuat", "error", "teks panjang"},
    "Tiket antrean": {"ideal", "memuat", "offline"},
    "Riwayat": {"ideal", "kosong", "memuat"},
}
print(f"{'Layar':14}" + "".join(f"{s[:7]:>9}" for s in STATE))
for l, s in punya.items():
    print(f"{l:14}" + "".join(f"{'v' if x in s else '-':>9}" for x in STATE))
kurang = sum(len(STATE) - len(s) for s in punya.values())
print(f"{kurang} state belum didesain")
''')]),

'Langkah 7: handoff ke developer': dict(
  ist=[('Handoff package', 'Tautan Figma (Dev Mode), token, aset, anotasi, prototipe, dan daftar edge case.'),
       ('Acceptance criteria', 'Kriteria yang bisa diuji QA untuk menyatakan layar selesai.'),
       ('Walkthrough', 'Sesi menjelaskan desain kepada developer dan QA, termasuk alasan keputusan.'),
       ('Changelog desain', 'Catatan perubahan setelah handoff agar developer tahu apa yang berubah.')],
  cx=[C('Isi tiket handoff yang lengkap', '''
JUDUL     [Antrean] Layar tiket antrean
FIGMA     https://www.figma.com/design/xxxx?node-id=12-345 (Ready for dev)
TOKEN     tokens/antrean.json v1.3 (sudah di repo)
STATE     ideal · memuat · offline (tampilkan tiket tersimpan + jam terakhir sinkron)
EDGE      nomor > 999 → format "A-1.024" · nama poli > 30 karakter → 2 baris
AKSES     estimasi diumumkan aria-live saat berubah; kontras QR ≥ 3:1
KRITERIA  Given tiket aktif, When offline, Then tiket & QR tetap tampil dengan label "Terakhir diperbarui 10.12"
''', lang='text')]),

'Struktur studi kasus yang dibaca perekrut': dict(
  ist=[('Skimmability', 'Perekrut rata-rata memindai portofolio beberapa menit; ringkasan harus di atas.'),
       ('Before / after', 'Perbandingan desain lama dan baru dengan alasan perubahannya.'),
       ('Role clarity', 'Jelaskan bagianmu sendiri dalam proyek tim.'),
       ('Process vs outcome', 'Tunjukkan proses secukupnya; fokus pada keputusan dan hasil.')],
  cx=[C('Struktur halaman studi kasus UI', '''
1. Hero: judul hasil ("Antrean puskesmas: waktu tunggu 150 → 40 menit"), peran, durasi, alat
2. Masalah & konteks (3-4 kalimat + 1 foto lokasi/kutipan pengguna)
3. Sorotan keputusan desain (3 kartu): sebelum/sesudah + alasan
4. Sistem visual: palet, tipografi, komponen kunci
5. Layar final (mobile mockup) + state penting
6. Hasil: angka, kutipan, apa yang dipelajari
7. Tautan prototipe Figma
''', lang='text')]),

'Mendesain halaman portofolio': dict(
  ist=[('Personal brand', 'Kesan konsisten dari nama, nada tulisan, dan gaya visual.'),
       ('Case study card', 'Kartu proyek di beranda: gambar kuat, judul hasil, tag peran.'),
       ('Performance', 'Gambar besar dikompres (WebP/AVIF), lazy loading; portofolio lambat memberi kesan buruk.'),
       ('Accessible portfolio', 'Portofolio desainer juga dinilai dari aksesibilitasnya sendiri.')],
  cx=[C('Grid kartu studi kasus yang ringan', '''
.proyek { display: grid; gap: 24px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr)); }
.proyek img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; border-radius: 12px; }
/* <img src="antrean.avif" alt="Layar tiket antrean puskesmas di ponsel" loading="lazy"
        width="1280" height="800" decoding="async"> */
.proyek h3 { font: 600 1.25rem/1.3 var(--font-sans); margin: 12px 0 4px; }
.proyek .tag { font: 500 .8125rem/1 var(--font-sans); color: var(--muted); }
''')]),

'Platform, presentasi, dan kesalahan umum': dict(
  ist=[('Behance / Dribbble / situs pribadi', 'Behance untuk studi kasus panjang, Dribbble untuk visual, situs pribadi untuk kendali penuh.'),
       ('Read.cv / Framer / Notion', 'Alternatif cepat membuat portofolio tanpa koding.'),
       ('Dribbble shot syndrome', 'Portofolio berisi visual cantik tanpa masalah nyata dan proses.'),
       ('Concept project', 'Proyek fiktif boleh, asal diberi label jujur dan tetap berbasis riset.')],
  cx=[P('Cek cepat kesalahan umum portofolio', '''
cek = {
    "ada ringkasan hasil di atas setiap studi kasus": True,
    "peran pribadi dijelaskan": True,
    "minimal 1 proyek dengan riset pengguna nyata": False,
    "proyek konsep diberi label 'konsep'": True,
    "gambar < 500 KB dan berformat modern": False,
    "kontras teks lolos AA": True,
    "tautan prototipe berfungsi": True,
}
skor = sum(cek.values())
print(f"Skor {skor}/{len(cek)}")
for k, v in cek.items():
    if not v:
        print("  Perbaiki:", k)
''')]),
}
