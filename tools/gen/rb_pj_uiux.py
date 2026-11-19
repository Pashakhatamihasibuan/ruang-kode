"""Proyek UI/UX berpenyelesaian: 6 mini (Python, dijalankan saat generate) + 4 besar berskala industri 2026-2027."""
from rb_pj_lib import MINI, BESAR, JALUR_M, q

# ---------------------------------------------------------------- MINI
KONTRAS = '''# Linter kontras WCAG 2.2 untuk token warna tema terang & gelap
def lum(hexwarna):
    h = hexwarna.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def rasio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)

TEMA = {
    "terang": {"bg": "#FFFFFF", "surface": "#F4F6F8", "text": "#1B1F24", "muted": "#8A94A0",
               "primary": "#0B6BCB", "on-primary": "#FFFFFF", "danger": "#E5484D", "border": "#D0D7DE"},
    "gelap":  {"bg": "#0E1116", "surface": "#161B22", "text": "#E6EDF3", "muted": "#7D8590",
               "primary": "#4493F8", "on-primary": "#0E1116", "danger": "#F85149", "border": "#30363D"},
}
# (teks/komponen, latar, jenis) -> jenis menentukan ambang: teks 4.5, besar/UI 3.0
PASANGAN = [("text", "bg", "teks"), ("text", "surface", "teks"), ("muted", "bg", "teks"),
            ("on-primary", "primary", "teks"), ("primary", "bg", "teks"), ("danger", "bg", "teks"),
            ("border", "bg", "ui")]
AMBANG = {"teks": 4.5, "ui": 3.0}

gagal = 0
for nama, t in TEMA.items():
    print(f"TEMA {nama}")
    for fg, bg, jenis in PASANGAN:
        r = rasio(t[fg], t[bg])
        ok = r >= AMBANG[jenis]
        gagal += not ok
        print(f"  {'LULUS' if ok else 'GAGAL'}  {fg:<10} di {bg:<8} {r:5.2f}:1  (min {AMBANG[jenis]})")
print(f"{gagal} pasangan gagal -> perbaiki token sebelum handoff" if gagal else "semua lulus")
'''

TOKEN = '''import json

# Token format DTCG (Design Tokens Community Group 2025.10): primitive -> semantic -> component
SUMBER = json.loads("""{
  "primitive": {
    "blue":  {"500": {"$type": "color", "$value": "#0B6BCB"}, "300": {"$type": "color", "$value": "#4493F8"}},
    "gray":  {"0":   {"$type": "color", "$value": "#FFFFFF"}, "950": {"$type": "color", "$value": "#0E1116"},
              "900": {"$type": "color", "$value": "#1B1F24"}, "100": {"$type": "color", "$value": "#E6EDF3"}},
    "space": {"2": {"$type": "dimension", "$value": "8px"}, "4": {"$type": "dimension", "$value": "16px"}},
    "radius":{"md": {"$type": "dimension", "$value": "8px"}}
  },
  "semantic": {
    "color": {
      "bg":      {"$value": {"light": "{primitive.gray.0}",   "dark": "{primitive.gray.950}"}},
      "text":    {"$value": {"light": "{primitive.gray.900}", "dark": "{primitive.gray.100}"}},
      "action":  {"$value": {"light": "{primitive.blue.500}", "dark": "{primitive.blue.300}"}}
    }
  },
  "component": {
    "button": {
      "primary-bg": {"$value": "{semantic.color.action}"},
      "padding-x":  {"$value": "{primitive.space.4}"},
      "radius":     {"$value": "{primitive.radius.md}"}
    }
  }
}""")

def ambil(jalur):
    node = SUMBER
    for k in jalur.split("."):
        node = node[k]
    return node["$value"]

def selesaikan(nilai, mode):
    if isinstance(nilai, dict):
        nilai = nilai[mode]
    while isinstance(nilai, str) and nilai.startswith("{"):
        nilai = ambil(nilai[1:-1])
        if isinstance(nilai, dict):
            nilai = nilai[mode]
    return nilai

def ratakan(node, awal=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        jalur = f"{awal}.{k}" if awal else k
        if "$value" in v:
            yield jalur, v["$value"]
        else:
            yield from ratakan(v, jalur)

def css(mode):
    baris = []
    for lapis in ("semantic", "component"):
        for jalur, nilai in ratakan(SUMBER[lapis], lapis):
            nama = "--" + jalur.split(".", 1)[1].replace(".", "-")
            baris.append(f"  {nama}: {selesaikan(nilai, mode)};")
    return baris

# Aturan arsitektur: komponen tidak boleh merujuk primitive warna langsung
WARNA_PRIMITIVE = ("{primitive.blue", "{primitive.gray")
pelanggaran = [j for j, v in ratakan(SUMBER["component"], "component")
               if isinstance(v, str) and v.startswith(WARNA_PRIMITIVE)]
print(":root {"); print("\\n".join(css("light"))); print("}")
print('[data-theme="dark"] {'); print("\\n".join(l for l in css("dark") if "color" in l or "primary-bg" in l)); print("}")
print("pelanggaran lapisan:", pelanggaran or "tidak ada")
'''

SKALA = '''# Type scale modular + cek panjang baris dan tinggi baris untuk handoff
DASAR, RASIO = 16, 1.25          # Major Third
LANGKAH = {"caption": -1, "body": 0, "h4": 1, "h3": 2, "h2": 3, "h1": 4, "display": 5}

def bulat4(px):                  # jaga grid 4pt
    return int(round(px / 4) * 4) if px >= 20 else round(px)

print(f"{'token':<9}{'px':>5}{'rem':>8}{'line-height':>13}")
for nama, n in LANGKAH.items():
    px = bulat4(DASAR * RASIO ** n)
    lh = 1.6 if px <= 18 else 1.4 if px <= 28 else 1.2
    tinggi = bulat4(px * lh)
    print(f"{nama:<9}{px:>5}{px/16:>8.3f}{tinggi:>9}px ({tinggi/px:.2f})")

# Panjang baris: rata-rata lebar karakter Inter ~0,5em
print()
for wadah in (320, 600, 720, 960):
    ch = wadah / (DASAR * 0.5)
    status = "nyaman" if 45 <= ch <= 80 else "pendek, wajar di HP (cukup >= 35)" if ch < 45 else "terlalu panjang -> batasi max-width: 65ch"
    print(f"wadah {wadah:>4}px ~ {ch:>4.0f} karakter/baris : {status}")
'''

SUS = '''import statistics as st

# Hasil usability test aplikasi bank digital: 8 partisipan, 3 tugas, + kuesioner SUS (10 butir, skala 1-5)
SUS = [
    [4, 2, 4, 1, 4, 2, 5, 2, 4, 2], [5, 1, 4, 2, 5, 1, 4, 1, 5, 2], [3, 3, 3, 3, 3, 3, 3, 2, 3, 3],
    [4, 2, 5, 1, 4, 2, 4, 2, 4, 1], [2, 4, 2, 4, 3, 4, 2, 4, 2, 4], [4, 1, 4, 2, 4, 2, 5, 1, 4, 2],
    [5, 2, 4, 1, 4, 1, 4, 2, 5, 1], [3, 2, 4, 2, 3, 2, 4, 3, 3, 2],
]
def skor_sus(j):
    ganjil = sum(j[i] - 1 for i in range(0, 10, 2))
    genap = sum(5 - j[i] for i in range(1, 10, 2))
    return (ganjil + genap) * 2.5

skor = [skor_sus(j) for j in SUS]
rata = st.mean(skor)
grade = "A" if rata >= 80.3 else "B" if rata >= 74 else "C" if rata >= 68 else "D" if rata >= 51 else "F"
print("SUS per partisipan:", skor)
print(f"SUS rata-rata {rata:.1f} (grade {grade}; rata-rata industri 68)")

# Tugas: (nama, berhasil dari 8, median detik, SEQ rata-rata 1-7)
TUGAS = [("Transfer ke rekening baru", 7, 74, 5.9), ("Bayar QRIS", 8, 21, 6.6), ("Ubah limit kartu", 4, 168, 3.4)]
print()
for nama, ok, dtk, seq in TUGAS:
    print(f"{nama:<27} sukses {ok}/8 ({ok/8:>4.0%})  median {dtk:>3}s  SEQ {seq}")

# Temuan diprioritaskan: severity Nielsen (0-4) x frekuensi
TEMUAN = [("Menu limit kartu tersembunyi di Profil > Keamanan", 4, 4), ("Label 'Rekening tujuan' vs 'Penerima' tidak konsisten", 2, 3),
          ("Tombol konfirmasi transfer di bawah lipatan pada HP 360px", 3, 5), ("Ikon QRIS tanpa label", 1, 2)]
print("\\nPRIORITAS PERBAIKAN")
for t, sev, frek in sorted(TEMUAN, key=lambda x: -(x[1] * x[2])):
    print(f"  skor {sev * frek:>2}  sev {sev}  {frek}/8 partisipan  {t}")
'''

AUDIT = '''from html.parser import HTMLParser
import re

HTML = """
<header><img src="logo.svg"><nav><a href="/">Beranda</a><a href="/promo"><img src="ikon-promo.svg"></a></nav></header>
<main>
  <h1>Pesan tiket kereta</h1>
  <h3>Pilih jadwal</h3>
  <label for="asal">Stasiun asal</label><input id="asal">
  <input id="tujuan" placeholder="Stasiun tujuan">
  <button style="width:20px;height:20px">x</button>
  <button aria-label="Tukar asal dan tujuan" style="width:44px;height:44px"></button>
  <div onclick="pesan()">Pesan sekarang</div>
  <img src="kereta.jpg" alt="">
</main>
"""

class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.masalah = []; self.label = set(); self.input = []
        self.heading = 0; self.tumpuk = []; self.teks = ""; self.landmark = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("header", "nav", "main", "footer"): self.landmark.add(tag)
        if tag == "img" and "alt" not in a:
            self.masalah.append(("1.1.1 A", f"img {a.get('src')} tanpa atribut alt"))
        if tag == "label": self.label.add(a.get("for"))
        if tag == "input": self.input.append(a)
        if re.fullmatch(r"h[1-6]", tag):
            n = int(tag[1])
            if self.heading and n > self.heading + 1:
                self.masalah.append(("1.3.1 A", f"heading lompat h{self.heading} -> h{n}"))
            self.heading = n
        if tag in ("div", "span") and "onclick" in a and "role" not in a:
            self.masalah.append(("2.1.1 A", f"<{tag} onclick> tidak bisa dijangkau keyboard; pakai <button>"))
        if tag == "button":
            gaya = dict(re.findall(r"(width|height):(\\d+)px", a.get("style", "")))
            if gaya and min(int(v) for v in gaya.values()) < 24:
                self.masalah.append(("2.5.8 AA", f"target {gaya['width']}x{gaya['height']}px < 24x24"))
            self.tumpuk.append(a); self.teks = ""
        if tag == "a": self.tumpuk.append({"a": 1, **a}); self.teks = ""
    def handle_data(self, d): self.teks += d.strip()
    def handle_endtag(self, tag):
        if tag in ("button", "a") and self.tumpuk:
            a = self.tumpuk.pop()
            if not self.teks and "aria-label" not in a and tag == "button":
                self.masalah.append(("4.1.2 A", "button tanpa nama aksesibel"))
            if tag == "a" and not self.teks:
                self.masalah.append(("2.4.4 A", f"tautan {a.get('href')} hanya berisi gambar tanpa alt"))

au = Audit(); au.feed(HTML)
for i in au.input:
    if i.get("id") not in au.label and "aria-label" not in i:
        au.masalah.append(("3.3.2 A", f"input #{i.get('id')} hanya punya placeholder, tanpa label"))
if "footer" not in au.landmark: au.masalah.append(("info", "landmark footer tidak ada"))
for kriteria, pesan in sorted(au.masalah):
    print(f"[{kriteria:<8}] {pesan}")
print(f"total {len(au.masalah)} temuan otomatis. Cek manual tetap wajib: urutan fokus, screen reader, zoom 200%.")
'''

CARDSORT = '''from itertools import combinations
from collections import Counter

# Open card sorting 6 partisipan untuk menu aplikasi koperasi simpan pinjam
HASIL = [
    {"Simpanan": ["Setor", "Tarik", "Saldo"], "Pinjaman": ["Ajukan", "Angsuran", "Simulasi"], "Akun": ["Profil", "Kata sandi"]},
    {"Uang saya": ["Saldo", "Setor", "Tarik", "Angsuran"], "Pinjam": ["Ajukan", "Simulasi"], "Pengaturan": ["Profil", "Kata sandi"]},
    {"Tabungan": ["Setor", "Tarik", "Saldo"], "Kredit": ["Ajukan", "Simulasi", "Angsuran"], "Saya": ["Profil", "Kata sandi"]},
    {"Transaksi": ["Setor", "Tarik", "Angsuran"], "Info": ["Saldo", "Simulasi"], "Layanan": ["Ajukan", "Profil", "Kata sandi"]},
    {"Simpanan": ["Setor", "Tarik", "Saldo"], "Pinjaman": ["Ajukan", "Simulasi", "Angsuran"], "Akun": ["Profil", "Kata sandi"]},
    {"Simpan": ["Saldo", "Setor", "Tarik"], "Pinjam": ["Ajukan", "Angsuran", "Simulasi"], "Profil": ["Profil", "Kata sandi"]},
]
kartu = sorted({k for h in HASIL for g in h.values() for k in g})
pasang = Counter()
for h in HASIL:
    for grup in h.values():
        for a, b in combinations(sorted(grup), 2):
            pasang[(a, b)] += 1

print("Matriks kemiripan (% partisipan yang mengelompokkan bersama)")
print(" " * 11 + "".join(f"{k[:6]:>7}" for k in kartu))
for a in kartu:
    sel = []
    for b in kartu:
        if a == b: sel.append("    -  ")
        else: sel.append(f"{pasang[tuple(sorted((a, b)))] / len(HASIL):>6.0%} ")
    print(f"{a:<11}" + "".join(sel))

# Klaster sederhana: gabungkan pasangan dengan kesepakatan >= 66%
grup = {k: {k} for k in kartu}
for (a, b), n in pasang.most_common():
    if n / len(HASIL) >= 0.66 and grup[a] is not grup[b]:
        gabung = grup[a] | grup[b]
        for k in gabung: grup[k] = gabung
klaster = {frozenset(g) for g in grup.values()}
print("\\nUsulan kelompok menu (kesepakatan >= 66%):")
for g in sorted(klaster, key=len, reverse=True):
    print("  -", ", ".join(sorted(g)))
label = Counter(n for h in HASIL for n in h)
print("Label paling sering:", label.most_common(4))
print("Kartu ambigu (cek dengan tree testing): Angsuran")
'''

UX_MINI = [
MINI(1, 'Linter kontras token warna (WCAG 2.2)',
  'Tim desain punya palet tema terang dan gelap, tetapi developer sering menemukan teks abu-abu yang sulit dibaca setelah build. Kamu diminta membuat pemeriksa otomatis untuk semua pasangan warna token sebelum handoff.',
  ['Hitung luminans relatif dan rasio kontras sesuai rumus WCAG', 'Periksa setiap pasangan token teks/latar di kedua tema', 'Ambang berbeda: teks 4,5:1, komponen UI dan teks besar 3:1', 'Laporan LULUS/GAGAL dan jumlah pasangan yang harus diperbaiki'],
  ['Ubah hex ke RGB 0-1, linierkan (gamma sRGB), lalu bobot 0,2126/0,7152/0,0722.', 'Rasio = (L terang + 0,05) / (L gelap + 0,05).', 'Simpan pasangan sebagai data (fg, bg, jenis) agar mudah ditambah.', 'Cetak tabel per tema dan ringkasan akhir untuk dipakai di CI.'],
  KONTRAS, 'python', run=True,
  kunci='baca token dari file JSON Figma Variables, sarankan warna pengganti terdekat yang lulus, dan jalankan di GitHub Actions setiap kali token berubah.',
  cek=q('Berapa rasio kontras minimum WCAG 2.2 AA untuk teks berukuran normal?', ['4,5:1', '3:1', '7:1'], 0, '3:1 untuk teks besar dan komponen UI; 7:1 untuk AAA.')),

MINI(2, 'Generator design token DTCG ke CSS (terang & gelap)',
  'Design system startup masih menyalin warna hex manual dari Figma ke kode. Buat pipeline kecil yang mengubah token format DTCG tiga lapis (primitive, semantic, component) menjadi CSS variables untuk dua tema.',
  ['Membaca token DTCG dengan $type dan $value', 'Menyelesaikan alias berantai seperti {semantic.color.action}', 'Mode terang/gelap dari satu sumber', 'Menolak komponen yang merujuk warna primitive langsung'],
  ['Simpan token sebagai JSON; lapisan semantic menyimpan nilai per mode.', 'Tulis fungsi ambil(jalur) dan selesaikan(nilai, mode) yang mengikuti alias sampai nilai akhir.', 'Ratakan pohon token menjadi nama variabel --lapis-nama.', 'Cetak :root dan [data-theme="dark"], lalu jalankan aturan arsitektur.'],
  TOKEN, 'python', run=True,
  kunci='ganti dengan Style Dictionary v4 atau Terrazzo, tambahkan keluaran Android XML dan Swift, dan publikasikan paket npm @perusahaan/tokens dengan changelog.',
  cek=q('Kenapa komponen sebaiknya merujuk token semantic, bukan primitive?', ['Agar ganti tema atau brand cukup mengubah pemetaan semantic tanpa menyentuh komponen', 'Agar file JSON lebih pendek', 'Karena primitive tidak boleh berisi warna'], 0, 'Lapisan semantic memberi makna peran.')),

MINI(3, 'Type scale modular dan aturan panjang baris',
  'Setiap halaman di produk memakai ukuran huruf berbeda (13, 15, 17, 22, 27px). Buat skala tipografi yang konsisten pada grid 4pt beserta aturan tinggi baris dan panjang baris untuk dokumentasi handoff.',
  ['Skala modular dengan rasio yang bisa diganti', 'Pembulatan ke grid 4pt dan nilai rem', 'Tinggi baris menurun untuk ukuran besar', 'Cek 45-80 karakter per baris di beberapa lebar wadah'],
  ['Hitung ukuran = dasar × rasio^langkah untuk setiap peran teks.', 'Bulatkan ke kelipatan 4 untuk ukuran ≥ 20px agar ritme vertikal rapi.', 'Pilih line-height 1,6 untuk body dan 1,2 untuk display.', 'Perkirakan karakter per baris dari lebar wadah dan lebar rata-rata huruf.'],
  SKALA, 'python', run=True,
  kunci='tambahkan fluid typography dengan clamp() antara 360px dan 1440px, dan uji dengan teks berbahasa Jerman yang 30% lebih panjang.',
  cek=q('Panjang baris yang nyaman untuk teks isi berada di kisaran berapa karakter?', ['45-80 karakter', '10-20 karakter', '120-160 karakter'], 0, 'Sering dibatasi dengan max-width: 65ch.')),

MINI(4, 'Analisis usability test: SUS, task success, dan prioritas temuan',
  'Kamu baru selesai menjalankan usability test aplikasi bank digital dengan 8 partisipan. Stakeholder ingin ringkasan angka yang jelas dan daftar perbaikan yang diprioritaskan, bukan sekadar catatan.',
  ['Skor SUS per partisipan dan rata-rata dengan grade', 'Task success rate, median waktu, dan SEQ per tugas', 'Prioritas temuan berdasarkan severity Nielsen × frekuensi', 'Keluaran siap ditempel ke laporan'],
  ['SUS: butir ganjil (skor-1), butir genap (5-skor), jumlahkan lalu kali 2,5.', 'Bandingkan rata-rata dengan patokan 68 dan grade kurva Sauro-Lewis.', 'Hitung sukses/8, median waktu, dan rata-rata SEQ untuk tiap tugas.', 'Urutkan temuan dengan skor severity × frekuensi dan tulis rekomendasinya.'],
  SUS, 'python', run=True,
  kunci='tambahkan interval kepercayaan (adjusted Wald) untuk task success, dan buat grafik before-after setelah redesign.',
  cek=q('Dengan 8 partisipan, apa keterbatasan angka task success 4/8 (50%)?', ['Interval kepercayaannya lebar, jadi angka itu menunjukkan masalah serius tetapi bukan estimasi persis untuk seluruh pengguna', 'Angkanya pasti 50% untuk semua pengguna', 'Tidak bisa dihitung sama sekali'], 0, 'Sampel kecil cocok untuk menemukan masalah, bukan mengukur presisi.')),

MINI(5, 'Audit aksesibilitas otomatis hasil slicing',
  'Halaman pemesanan tiket hasil slicing akan dirilis minggu depan. Buat pemeriksa kecil yang menandai pelanggaran WCAG yang paling sering muncul dan menyebut nomor kriterianya, agar developer tahu harus memperbaiki apa.',
  ['Gambar tanpa alt dan tautan berisi gambar tanpa teks', 'Input tanpa label (hanya placeholder)', 'Heading yang melompat level', 'Elemen klik non-semantik dan target sentuh < 24×24px', 'Laporan dengan nomor kriteria WCAG'],
  ['Turunkan HTMLParser dan simpan status (label, input, heading terakhir).', 'Periksa atribut di handle_starttag dan teks di handle_endtag.', 'Cocokkan input dengan label for setelah semua HTML terbaca.', 'Urutkan temuan per kriteria dan ingatkan bahwa cek manual tetap perlu.'],
  AUDIT, 'python', run=True,
  kunci='jalankan axe-core lewat Playwright pada halaman asli, gabungkan hasilnya, dan gagalkan CI jika ada pelanggaran level A/AA.',
  cek=q('Kenapa <div onclick> untuk tombol dianggap masalah aksesibilitas?', ['Tidak bisa difokus dan diaktifkan dengan keyboard serta tidak diumumkan sebagai tombol oleh screen reader', 'Warnanya salah', 'Div tidak bisa diberi teks'], 0, 'Gunakan elemen <button> asli.')),

MINI(6, 'Card sorting untuk menyusun information architecture',
  'Koperasi simpan pinjam ingin menyusun ulang menu aplikasinya. Enam anggota sudah mengikuti open card sorting. Olah hasilnya menjadi matriks kemiripan dan usulan kelompok menu.',
  ['Matriks kemiripan antar kartu dalam persen', 'Pengelompokan berdasarkan ambang kesepakatan', 'Label kelompok yang paling sering dipakai partisipan', 'Daftar kartu ambigu untuk divalidasi dengan tree testing'],
  ['Hitung setiap pasangan kartu yang berada di grup yang sama (combinations).', 'Bagi dengan jumlah partisipan untuk persentase kesepakatan.', 'Gabungkan pasangan dengan kesepakatan ≥ 66% menjadi klaster.', 'Hitung frekuensi nama grup untuk memilih label menu dengan bahasa pengguna.'],
  CARDSORT, 'python', run=True,
  kunci='gunakan hierarchical clustering (scipy) dan dendrogram, lalu rancang tree test dengan 8 tugas untuk memvalidasi struktur baru.',
  cek=q('Kapan tree testing dilakukan dibanding card sorting?', ['Setelah struktur menu diusulkan, untuk menguji apakah pengguna bisa menemukan item di struktur itu', 'Sebelum ada kartu sama sekali', 'Hanya setelah aplikasi dirilis'], 0, 'Card sorting membangun, tree testing memvalidasi.')),
]

# ---------------------------------------------------------------- BESAR
DS = r'''// tokens/semantic/color.json (DTCG 2025.10) — satu sumber untuk 3 brand x 2 mode
{
  "color": {
    "action": {
      "primary": { "$type": "color", "$value": "{brand.primary.600}",
                   "$extensions": { "mode": { "dark": "{brand.primary.300}" } } }
    },
    "text": { "default": { "$type": "color", "$value": "{neutral.900}", "$extensions": { "mode": { "dark": "{neutral.50}" } } } }
  }
}

// style-dictionary.config.mjs — keluaran web, Android, iOS
export default {
  source: ['tokens/primitive/**/*.json', `tokens/brand/${process.env.BRAND}.json`, 'tokens/semantic/**/*.json'],
  platforms: {
    css:     { transformGroup: 'css',     buildPath: `dist/${process.env.BRAND}/`, files: [{ destination: 'tokens.css', format: 'css/variables' }] },
    android: { transformGroup: 'android', buildPath: 'dist/android/', files: [{ destination: 'colors.xml', format: 'android/colors' }] },
    ios:     { transformGroup: 'ios-swift', buildPath: 'dist/ios/',   files: [{ destination: 'Tokens.swift', format: 'ios-swift/class' }] },
  },
};

// packages/ui/src/Button.tsx — komponen hanya memakai token semantic/component
export function Button({ variant = 'primary', size = 'md', loading = false, children, ...rest }) {
  return (
    <button className={cx('btn', `btn--${variant}`, `btn--${size}`)} aria-busy={loading || undefined}
            disabled={rest.disabled || loading} {...rest}>
      {loading ? <Spinner aria-hidden /> : null}
      <span className={loading ? 'sr-only' : undefined}>{children}</span>
    </button>
  );
}

// packages/ui/src/Button.stories.tsx — setiap state terdokumentasi dan diuji visual
export default { title: 'Aksi/Button', component: Button, tags: ['autodocs'] };
export const Semua = () => (['primary', 'secondary', 'danger'] as const).map(v =>
  <div key={v}><Button variant={v}>Simpan</Button><Button variant={v} disabled>Simpan</Button><Button variant={v} loading>Simpan</Button></div>);

// .github/workflows/ds.yml — PR: build token, lint kontras, tes a11y, visual regression
//  - npm run tokens:build && node scripts/lint-kontras.mjs      (gagal jika < 4.5:1)
//  - npx test-storybook --coverage                             (interaction + axe per story)
//  - npx chromatic --exit-zero-on-changes=false                (perubahan visual wajib di-approve)
//  - npx changeset version                                     (semver + changelog otomatis)'''

CHECKOUT = r'''<!-- checkout/pembayaran.html — hasil redesign: satu tujuan per layar, error spesifik, aman di HP 360px -->
<main class="checkout" aria-labelledby="judul">
  <ol class="langkah" aria-label="Langkah checkout">
    <li aria-current="false">Alamat</li><li aria-current="step">Pembayaran</li><li>Konfirmasi</li>
  </ol>
  <h1 id="judul">Pilih metode pembayaran</h1>

  <form id="bayar" novalidate>
    <fieldset>
      <legend>Metode yang paling sering dipakai</legend>
      <label class="opsi"><input type="radio" name="metode" value="qris" checked> QRIS <small>Semua e-wallet & m-banking</small></label>
      <label class="opsi"><input type="radio" name="metode" value="va"> Transfer virtual account <small>BCA, BRI, Mandiri, BNI</small></label>
      <label class="opsi"><input type="radio" name="metode" value="cod"> Bayar di tempat (COD) <small>Biaya Rp5.000</small></label>
    </fieldset>

    <label for="voucher">Kode voucher <span class="opsional">(opsional)</span></label>
    <div class="baris">
      <input id="voucher" name="voucher" autocomplete="off" aria-describedby="voucher-pesan" inputmode="text">
      <button type="button" id="pakai">Pakai</button>
    </div>
    <p id="voucher-pesan" role="status" aria-live="polite"></p>

    <section class="ringkasan" aria-label="Ringkasan biaya">
      <dl><dt>Subtotal</dt><dd>Rp1.249.000</dd><dt>Ongkir</dt><dd>Rp18.000</dd><dt>Total</dt><dd><strong>Rp1.267.000</strong></dd></dl>
      <p class="aman">Pembayaran diproses oleh penyedia berizin Bank Indonesia.</p>
    </section>

    <!-- tombol utama menempel di bawah pada HP agar selalu terlihat (temuan usability: tombol di bawah lipatan) -->
    <div class="aksi-tempel"><button type="submit" class="btn-utama">Bayar Rp1.267.000</button></div>
  </form>
</main>

<style>
.aksi-tempel { position: sticky; bottom: 0; padding: 12px 16px calc(12px + env(safe-area-inset-bottom)); background: var(--surface); }
.btn-utama { inline-size: 100%; min-block-size: 48px; font: var(--type-label-lg); }
.opsi { display: grid; grid-template-columns: auto 1fr; gap: 4px 12px; min-block-size: 56px; align-items: center; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; scroll-margin-bottom: 96px; } /* WCAG 2.4.11: fokus tidak tertutup bar tempel */
</style>

<script>
// analitik eksperimen: varian B (redesign) vs A, metrik utama = konversi checkout, guardrail = refund & tiket CS
document.getElementById('bayar').addEventListener('submit', e => {
  e.preventDefault();
  track('checkout_submit', { varian: window.EXP?.checkout ?? 'A', metode: new FormData(e.target).get('metode') });
});
</script>'''

PUBLIK = r'''// tests/a11y.spec.ts — Playwright + axe: setiap halaman layanan diuji WCAG 2.2 AA di CI
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

const HALAMAN = ['/', '/layanan/ktp', '/layanan/ktp/formulir', '/antrean', '/status', '/bantuan'];

for (const url of HALAMAN) {
  test(`a11y ${url}`, async ({ page }) => {
    await page.goto(url);
    const hasil = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
    expect(hasil.violations, JSON.stringify(hasil.violations.map(v => v.id))).toEqual([]);
  });
}

test('formulir bisa diselesaikan hanya dengan keyboard', async ({ page }) => {
  await page.goto('/layanan/ktp/formulir');
  await page.keyboard.press('Tab');                                  // skip link muncul pertama
  await expect(page.getByRole('link', { name: 'Langsung ke isi' })).toBeFocused();
  await page.getByLabel('NIK').fill('3201234567890001');
  await page.getByLabel('Nomor HP').fill('081234567890');
  await page.getByRole('button', { name: 'Lanjut' }).press('Enter');
  await expect(page.getByRole('heading', { name: 'Unggah dokumen' })).toBeVisible();
});

test('pesan error terhubung ke field dan diumumkan', async ({ page }) => {
  await page.goto('/layanan/ktp/formulir');
  await page.getByRole('button', { name: 'Lanjut' }).click();
  const nik = page.getByLabel('NIK');
  await expect(nik).toHaveAttribute('aria-invalid', 'true');
  await expect(nik).toHaveAccessibleDescription('NIK harus 16 angka. Lihat di KTP lama atau Kartu Keluarga.');
});

test('zoom 200% dan lebar 320px tanpa scroll horizontal (1.4.10 Reflow)', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 640 });
  await page.goto('/layanan/ktp');
  const lebar = await page.evaluate(() => document.documentElement.scrollWidth);
  expect(lebar).toBeLessThanOrEqual(320);
});

test('login tanpa tes kognitif (3.3.8): OTP bisa ditempel', async ({ page }) => {
  await page.goto('/masuk');
  const otp = page.getByLabel('Kode OTP');
  await expect(otp).toHaveAttribute('autocomplete', 'one-time-code');
  await expect(otp).not.toHaveAttribute('onpaste', /.+/);
});'''

AI = r'''// components/AsistenJawaban.tsx — pola UX fitur AI di aplikasi bank (transparansi, kontrol, human-in-the-loop)
type Sumber = { judul: string; url: string };
type Jawaban = { teks: string; sumber: Sumber[]; yakin: 'tinggi' | 'sedang' | 'rendah'; aksi?: AksiUsulan };
type AksiUsulan = { jenis: 'transfer' | 'blokir_kartu'; ringkasan: string; payload: unknown };

export function AsistenJawaban({ j, onUmpanBalik, onEskalasi }: Props) {
  return (
    <article className="jawaban-ai" aria-live="polite">
      <header className="label-ai">
        <IkonAI aria-hidden /> Dibuat oleh AI · bisa keliru · <a href="/bantuan/asisten">Cara kerja asisten</a>
      </header>

      <Markdown>{j.teks}</Markdown>

      {j.sumber.length > 0 && (
        <details open={j.yakin !== 'tinggi'}>
          <summary>Sumber ({j.sumber.length})</summary>
          <ul>{j.sumber.map(s => <li key={s.url}><a href={s.url}>{s.judul}</a></li>)}</ul>
        </details>
      )}

      {j.yakin === 'rendah' && (
        <p className="peringatan">Asisten belum yakin. <button onClick={onEskalasi}>Hubungi petugas</button></p>
      )}

      {j.aksi && <PratinjauAksi aksi={j.aksi} />}

      <footer className="umpan-balik">
        <span id="ub">Apakah jawaban ini membantu?</span>
        <button aria-describedby="ub" onClick={() => onUmpanBalik('ya')}>Ya</button>
        <button aria-describedby="ub" onClick={() => onUmpanBalik('tidak')}>Tidak</button>
      </footer>
    </article>
  );
}

// Aksi berisiko tidak pernah dieksekusi otomatis: pratinjau -> konfirmasi eksplisit -> PIN/biometrik -> bisa dibatalkan
function PratinjauAksi({ aksi }: { aksi: AksiUsulan }) {
  const [tahap, setTahap] = useState<'pratinjau' | 'verifikasi' | 'selesai'>('pratinjau');
  if (tahap === 'pratinjau') return (
    <section className="pratinjau" aria-label="Usulan tindakan">
      <h3>Periksa sebelum dijalankan</h3>
      <p>{aksi.ringkasan}</p>
      <button className="utama" onClick={() => setTahap('verifikasi')}>Lanjutkan</button>
      <button onClick={() => track('ai_aksi_ditolak', { jenis: aksi.jenis })}>Batalkan</button>
    </section>
  );
  if (tahap === 'verifikasi') return <VerifikasiPIN onSukses={() => setTahap('selesai')} />;
  return <p role="status">Selesai. <a href="/riwayat">Lihat di riwayat</a></p>;
}

// Persetujuan data (UU PDP + peraturan pelaksana): terpisah dari S&K, tidak dicentang otomatis, bisa ditarik
export function PersetujuanAI() {
  return (
    <fieldset>
      <legend>Izin penggunaan data untuk asisten</legend>
      <label><input type="checkbox" name="riwayat_transaksi" /> Pakai riwayat transaksi 90 hari untuk menjawab pertanyaan saya</label>
      <label><input type="checkbox" name="perbaikan_model" /> Izinkan percakapan saya (tanpa nama & nomor) dipakai memperbaiki layanan</label>
      <p>Izin bisa dicabut kapan saja di <a href="/profil/privasi">Profil &gt; Privasi</a>.</p>
    </fieldset>
  );
}'''

UX_BESAR = [
BESAR(1, 'Design system multi-brand dengan token DTCG dan visual regression',
  'Grup ritel punya 3 brand (supermarket, apotek, elektronik) dengan aplikasi web dan mobile terpisah. Tombol saja ada 27 versi, tema gelap tidak konsisten, dan setiap rebranding butuh 3 bulan kerja developer.',
  ['Token tiga lapis (primitive → semantic → component) format DTCG, 3 brand × 2 mode', 'Pipeline token ke CSS, Android, dan iOS dari satu sumber', 'Pustaka komponen React dengan semua state (default, hover, focus, disabled, loading, error)', 'Dokumentasi Storybook dengan panduan kapan dipakai dan contoh salah/benar', 'CI: lint kontras, tes aksesibilitas per story, visual regression, semver + changelog'],
  'Figma Variables, Tokens Studio, DTCG 2025.10, Style Dictionary v4, React + TypeScript, Storybook 9, Chromatic/Playwright, Changesets, GitHub Actions',
  [('Token', 'primitive (skala warna 50-950, spacing 4pt) → semantic (peran per mode) → component (button, input, card)'), ('Distribusi', 'paket @grup/tokens dan @grup/ui di registry internal, versi semver'),
   ('Komponen', 'atomic: atom (Button, Input) → molekul (FormField) → organisme (Header, ProductCard)'), ('Kualitas', 'kontras ≥ 4,5:1 di semua brand/mode, axe 0 pelanggaran, visual diff wajib di-approve'),
   ('Tata kelola', 'RFC untuk komponen baru, office hour mingguan, kontribusi lewat PR dengan template'), ('Metrik adopsi', '% layar memakai komponen DS, jumlah komponen lokal yang dihapus, waktu rebranding')],
  ['Audit inventaris UI: tangkap semua varian tombol, warna, dan jarak dari produk yang berjalan.', 'Definisikan token primitive dan semantic bersama tim brand; uji kontras otomatis.', 'Bangun komponen inti (Button, Input, Select, Dialog, Toast) dengan semua state dan dokumentasi.', 'Siapkan pipeline token + Storybook + Chromatic di CI dan rilis versi 1.0.', 'Migrasikan satu alur per brand (checkout) sebagai bukti, ukur adopsi, lalu lanjutkan bertahap.'],
  DS, 'tsx', standar='satu sumber token untuk semua platform, setiap komponen punya semua state dan dokumentasi, aksesibilitas diuji otomatis, perubahan visual direview, rilis bersemver dengan changelog',
  cek=q('Apa fungsi visual regression testing (misalnya Chromatic) di design system?', ['Mendeteksi perubahan tampilan komponen yang tidak disengaja dengan membandingkan tangkapan layar tiap PR', 'Mengecilkan ukuran bundle', 'Menerjemahkan teks komponen'], 0, 'Perubahan visual harus disetujui manusia.')),

BESAR(2, 'Redesign checkout e-commerce berbasis riset dan A/B test',
  'Marketplace fashion lokal punya tingkat abandon checkout 71% di mobile. Tim bisnis ingin langsung mengganti warna tombol. Kamu diminta memimpin redesign yang dibuktikan dengan data: dari riset sampai eksperimen.',
  ['Analisis funnel dan session recording untuk menemukan titik drop-off', 'Usability test 5-8 pengguna Android entry-level dengan koneksi lambat', 'Flow baru: guest checkout, alamat tersimpan, metode bayar lokal (QRIS, VA, COD) di depan', 'Desain dan slicing responsif dengan error spesifik dan tombol utama selalu terlihat', 'A/B test dengan metrik utama, guardrail, dan ukuran sampel yang dihitung sebelumnya'],
  'Figma, Maze/Lookback, GA4/Amplitude, Hotjar/Clarity, HTML/CSS/JS atau React, GrowthBook/Statsig, Looker Studio',
  [('Riset', 'funnel per langkah, 20 session recording, 6 usability test, survei exit 300 responden'), ('Hipotesis', 'drop-off terbesar di langkah pembayaran karena ongkir muncul terlambat dan tombol tertutup keyboard'),
   ('Desain', '3 langkah dengan progress, ongkir di keranjang, metode terakhir dipilih otomatis, sticky CTA'), ('Eksperimen', '50/50, MDE 2 poin persen, α 0,05, power 0,8, durasi minimal 2 siklus mingguan'),
   ('Guardrail', 'tingkat refund, tiket CS terkait pembayaran, waktu muat halaman'), ('Handoff', 'spesifikasi state, anotasi error, acceptance criteria, design QA di perangkat nyata')],
  ['Petakan funnel dan pilih satu langkah dengan drop-off terbesar sebagai fokus.', 'Jalankan usability test dan sintesis temuan dengan affinity mapping.', 'Rancang 2-3 alternatif, uji prototype, pilih satu dengan alasan dan data.', 'Slicing responsif + aksesibel, instrumentasi event analitik.', 'Hitung ukuran sampel, jalankan A/B test, baca hasil termasuk guardrail, dan dokumentasikan pembelajaran.'],
  CHECKOUT, 'html', standar='keputusan didukung riset, satu tujuan per layar, metode bayar lokal jelas, error spesifik, eksperimen dengan ukuran sampel dan guardrail, hasil didokumentasikan termasuk jika gagal',
  cek=q('Kenapa guardrail metric (misalnya tingkat refund) diperlukan dalam A/B test checkout?', ['Agar kenaikan konversi tidak dibayar dengan masalah lain seperti pesanan salah atau keluhan yang naik', 'Agar eksperimen selesai lebih cepat', 'Karena metrik utama tidak bisa diukur'], 0, 'Optimasi satu angka bisa merusak angka lain.')),

BESAR(3, 'Portal layanan publik yang aksesibel (WCAG 2.2 AA) untuk semua warga',
  'Pemerintah daerah meluncurkan portal layanan kependudukan (KTP, KK, akta). Penggunanya beragam: lansia, penyandang disabilitas netra, warga di daerah 3G, dan pengguna HP 2 GB RAM. Versi lama gagal audit aksesibilitas dan antrean di kantor tetap panjang.',
  ['Riset kontekstual di kantor layanan dan wawancara kelompok rentan (lansia, netra, literasi rendah)', 'Bahasa sederhana, ikon berlabel, bantuan konsisten di setiap halaman (3.2.6)', 'Formulir bertahap dengan simpan otomatis, tanpa input ulang (3.3.7), error terhubung ke field', 'Login dengan OTP yang bisa ditempel atau passkey (3.3.8), tanpa CAPTCHA teka-teki', 'Tes otomatis axe + keyboard + reflow 320px di CI, plus uji manual dengan screen reader'],
  'Figma, GOV-style design pattern, HTML semantik + progressive enhancement, Next.js atau Astro (SSR, JS minimal), Playwright + axe-core, NVDA/TalkBack/VoiceOver, Lighthouse CI',
  [('Prinsip', 'mulai dari kebutuhan warga, satu hal per halaman, bekerja tanpa JavaScript, hemat data'), ('Konten', 'tingkat keterbacaan setara kelas 6 SD, istilah dijelaskan, contoh isian (NIK 16 angka)'),
   ('Aksesibilitas', 'WCAG 2.2 AA; fokus tidak tertutup header tempel (2.4.11), target ≥ 24px dan praktiknya 48px'), ('Kinerja', 'halaman < 200 KB, LCP < 2,5 s di 3G, berfungsi di Android 9+'),
   ('Privasi', 'data minimum, persetujuan terpisah, penjelasan tujuan per data (UU PDP)'), ('Pengukuran', 'completion rate online, waktu layanan, antrean fisik, CSAT, laporan aksesibilitas publik')],
  ['Lakukan riset di 3 kantor layanan dan rekrut partisipan dari kelompok rentan.', 'Susun service blueprint dari warga sampai petugas back-office.', 'Rancang dan uji formulir bertahap dengan bahasa sederhana; ulangi tiap 2 minggu.', 'Bangun dengan HTML semantik dan tes otomatis aksesibilitas di setiap PR.', 'Audit manual dengan screen reader, terbitkan pernyataan aksesibilitas, dan pantau metrik layanan.'],
  PUBLIK, 'ts', standar='WCAG 2.2 AA lulus otomatis dan manual, bisa dipakai dengan keyboard dan screen reader, berfungsi di jaringan lambat dan HP murah, bahasa sederhana, pernyataan aksesibilitas publik',
  cek=q('Apa tuntutan kriteria WCAG 2.2 3.3.8 Accessible Authentication (Minimum)?', ['Login tidak boleh bergantung pada tes kognitif seperti mengingat atau menyalin karakter tanpa alternatif; izinkan paste, password manager, OTP, atau passkey', 'Password wajib minimal 20 karakter', 'Setiap halaman wajib punya CAPTCHA'], 0, 'Kriteria baru di WCAG 2.2.')),

BESAR(4, 'UX fitur asisten AI di aplikasi perbankan',
  'Bank digital menambahkan asisten AI yang bisa menjawab pertanyaan produk, menjelaskan transaksi, dan mengusulkan tindakan (blokir kartu, transfer rutin). Risikonya besar: jawaban keliru, kepercayaan berlebihan, dan aksi keuangan yang tidak diinginkan.',
  ['Batas kemampuan AI dijelaskan sejak awal; jawaban diberi label AI dan sumber', 'Tingkat keyakinan memengaruhi tampilan; keyakinan rendah menawarkan eskalasi ke petugas', 'Aksi berisiko melalui pratinjau, konfirmasi eksplisit, dan verifikasi PIN/biometrik', 'Persetujuan data terpisah, tidak dicentang otomatis, dan bisa ditarik (UU PDP)', 'Umpan balik per jawaban dan evaluasi kualitas berkala dengan skenario uji'],
  'Figma, prototyping percakapan (Voiceflow/Figma), React/React Native, Claude API dengan tool use, analitik event, Google PAIR Guidebook, Microsoft HAX Toolkit',
  [('Ekspektasi', 'onboarding singkat: apa yang bisa dan tidak bisa, contoh pertanyaan, tautan cara kerja'), ('Transparansi', 'label AI, sumber per jawaban, keyakinan memengaruhi apakah sumber dibuka otomatis'),
   ('Kontrol', 'terima/edit/tolak usulan, batalkan, riwayat tindakan, eskalasi ke manusia selalu tersedia'), ('Keamanan', 'AI hanya mengusulkan; eksekusi tetap lewat alur transaksi biasa dengan verifikasi'),
   ('Privasi', 'izin granular, data minimum, retensi percakapan dijelaskan, log persetujuan'), ('Evaluasi', 'golden set 200 pertanyaan, rasio jawaban dengan sumber benar, tingkat eskalasi, CSAT, insiden aksi salah = 0')],
  ['Petakan pertanyaan nasabah dari data CS dan pilih kasus di mana AI benar-benar menambah nilai.', 'Rancang pola percakapan, label, dan state (memuat, tidak yakin, gagal, offline).', 'Uji prototype dengan nasabah termasuk skenario jawaban salah untuk mengukur kepercayaan berlebihan.', 'Rancang alur aksi berisiko dengan pratinjau dan verifikasi; review bersama tim risiko dan legal.', 'Rilis bertahap ke 5% pengguna, pantau metrik kualitas dan keselamatan, iterasi.'],
  AI, 'tsx', standar='pengguna tahu sedang berinteraksi dengan AI, jawaban bersumber, aksi keuangan selalu dikonfirmasi manusia, persetujuan data sesuai UU PDP, kualitas dan keselamatan diukur sebelum dan sesudah rilis',
  cek=q('Kenapa asisten AI di aplikasi bank sebaiknya hanya mengusulkan transfer, bukan langsung mengeksekusinya?', ['Karena aksi keuangan sulit dibatalkan; pengguna harus melihat pratinjau dan mengonfirmasi dengan verifikasi agar kesalahan AI tidak merugikan', 'Karena AI tidak bisa memanggil API', 'Agar aplikasi terlihat lebih lambat'], 0, 'Human-in-the-loop untuk aksi berisiko.')),
]

PJ_UIUX = JALUR_M('UI/UX Designer', 'Menengah',
  'Enam proyek mini Python yang dijalankan (linter kontras WCAG, generator token DTCG, type scale, analisis usability test SUS, audit aksesibilitas HTML, card sorting untuk IA) dan empat proyek besar berskala industri 2026-2027 (design system multi-brand, redesign checkout berbasis A/B test, portal layanan publik WCAG 2.2 AA, UX fitur asisten AI perbankan), lengkap dengan penyelesaiannya.',
  ['UX research', 'Design tokens', 'Accessibility', 'Design system', 'AI UX'], UX_MINI, UX_BESAR)
