"""Pendalaman jalur Design System: istilah dunia kerja dan contoh (perhitungan dijalankan; CSS/JSON sebagai rujukan)."""
K = 'ds'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def C(t, code, b=None, lang='css'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Design system, pustaka komponen & atomic design': dict(
  ist=[('Design system', 'Produk internal berisi prinsip, token, komponen, pola, dokumentasi, dan proses tata kelolanya.'),
       ('Component library', 'Hanya bagian komponen (di Figma dan di kode); belum tentu design system utuh.'),
       ('Atomic design', 'Atom → molekul → organisme → template → halaman (Brad Frost).'),
       ('Style guide vs pattern library', 'Style guide: fondasi visual. Pattern library: solusi berulang (form, pencarian, empty state).')],
  cx=[P('Memetakan komponen ke tingkat atomic design', '''
peta = {
    "atom": ["Button", "Icon", "Badge", "Input", "Avatar"],
    "molekul": ["SearchField (Input + Icon + Button)", "FormField (Label + Input + Helper)", "ListItem (Avatar + teks + Badge)"],
    "organisme": ["Header (Logo + SearchField + Avatar)", "CheckoutForm (beberapa FormField + Button)"],
    "template": ["Halaman daftar: Header + filter + grid kartu + pagination"],
    "halaman": ["Hasil pencarian 'beras 5 kg' dengan data asli"],
}
for tingkat, isi in peta.items():
    print(f"{tingkat.upper():10} {len(isi)} | " + "; ".join(isi))
''')]),

'Kapan tim butuh design system?': dict(
  ist=[('Scale signal', 'Tanda butuh: banyak tim/produk, inkonsistensi naik, waktu desain ulang komponen tinggi.'),
       ('ROI design system', 'Penghematan jam desain & development dibanding biaya membangun dan merawat.'),
       ('Centralized vs federated', 'Dikelola satu tim inti, atau kontribusi dari banyak tim produk.'),
       ('Premature system', 'Membangun design system besar sebelum produk menemukan pola stabil; boros.')],
  cx=[P('Estimasi ROI sederhana design system', '''
tim = 6                 # tim produk
komponen_per_bulan = 10 # komponen yang dibuat ulang per tim per bulan
jam_per_komponen = 8    # desain + kode + QA
hemat = 0.6             # 60% kerja ulang hilang dengan design system
biaya_bangun_jam = 1_200
biaya_rawat_jam_bulan = 120
hemat_bulan = tim * komponen_per_bulan * jam_per_komponen * hemat
bersih = hemat_bulan - biaya_rawat_jam_bulan
print(f"hemat kotor  : {hemat_bulan:.0f} jam/bulan")
print(f"bersih       : {bersih:.0f} jam/bulan")
print(f"balik modal  : {biaya_bangun_jam / bersih:.1f} bulan")
print("Dengan 1 tim saja:", round(1 * 10 * 8 * 0.6 - 120), "jam/bulan -> belum layak, cukup UI kit sederhana")
''')]),

'Audit visual & pilot': dict(
  ist=[('Interface inventory', 'Tangkapan layar semua variasi komponen dari produk yang ada, dikelompokkan per jenis.'),
       ('Visual audit', 'Menghitung variasi warna, ukuran huruf, jarak, radius yang benar-benar dipakai.'),
       ('Pilot', 'Menerapkan design system awal ke satu fitur/tim untuk membuktikan manfaat.'),
       ('Consolidation', 'Menyatukan variasi yang mirip menjadi satu token/komponen.')],
  cx=[P('Audit warna dari berkas CSS yang ada', '''
import re
from collections import Counter
css = """
.btn{background:#2563EB}.btn:hover{background:#1D4ED8}.link{color:#2563eb}.badge{background:#2563EA}
.alert{color:#DC2626}.err{color:#dc2626}.danger{color:#E11D48}.text{color:#111827}.muted{color:#6B7280}
.title{color:#111827}.sub{color:#6b7280}.card{border-color:#E5E7EB}.divider{background:#e5e7eb}.x{color:#6B7281}
"""
warna = Counter(w.upper() for w in re.findall(r"#[0-9a-fA-F]{6}", css))
print(f"{sum(warna.values())} pemakaian, {len(warna)} warna unik")
for w, n in warna.most_common():
    print(f"  {w} x{n}")
def dekat(a, b):
    return sum(abs(int(a[i:i + 2], 16) - int(b[i:i + 2], 16)) for i in (1, 3, 5)) <= 6
pasangan = [(a, b) for a in warna for b in warna if a < b and dekat(a, b)]
print("hampir sama (satukan):", pasangan)
''')]),

'Prinsip desain & tone of voice': dict(
  ist=[('Design principles', '3-5 prinsip spesifik yang membantu memutuskan saat ada dua pilihan bagus.'),
       ('Tone of voice', 'Kepribadian bahasa produk: misalnya hangat, jelas, tidak menggurui.'),
       ('Voice vs tone', 'Voice tetap; tone menyesuaikan situasi (error lebih tenang, sukses lebih ceria).'),
       ('Microcopy', 'Teks kecil di UI: label tombol, pesan error, empty state.')],
  cx=[C('Tone yang berubah menurut situasi (voice tetap)', '''
SITUASI          TONE            CONTOH
---------------  --------------  ---------------------------------------------------------------
Sukses kecil     ringan          "Tersimpan."
Sukses besar     merayakan       "Target Celengan Liburan tercapai! Rp3.000.000 siap dipakai."
Error pengguna   tenang, jelas   "Nomor HP belum lengkap. Masukkan 10-13 digit."
Error sistem     bertanggung     "Maaf, server kami sedang bermasalah. Saldo kamu aman. Coba lagi
                 jawab           dalam beberapa menit."
Aksi berisiko    serius          "Tutup rekening? Sisa saldo Rp125.000 akan dikirim ke rekening utama."

PRINSIP: 1) Jelas lebih penting dari lucu  2) Sapa dengan "kamu"  3) Angka selalu lengkap dengan Rp
''', lang='text')]),

'Ikon, ilustrasi & motion yang konsisten': dict(
  ist=[('Icon style', 'Outline vs filled, ketebalan stroke, sudut; satu gaya untuk seluruh produk.'),
       ('Illustration system', 'Aturan karakter, palet, dan komposisi ilustrasi (empty state, onboarding).'),
       ('Motion token', 'Durasi dan easing bernama: duration.short = 150ms, easing.standard.'),
       ('Reduced motion', 'Hormati prefers-reduced-motion; ganti animasi gerak dengan fade atau tanpa animasi.')],
  cx=[C('Token motion dan penggunaannya', '''
:root {
  --duration-short: 150ms;   /* hover, toggle */
  --duration-medium: 250ms;  /* expand, sheet */
  --duration-long: 400ms;    /* transisi halaman */
  --easing-standard: cubic-bezier(.2, 0, 0, 1);
  --easing-emphasized-decelerate: cubic-bezier(.05, .7, .1, 1);
}
.sheet { transition: transform var(--duration-medium) var(--easing-emphasized-decelerate); }
.toggle { transition: background-color var(--duration-short) var(--easing-standard); }
@media (prefers-reduced-motion: reduce) {
  :root { --duration-short: 0ms; --duration-medium: 0ms; --duration-long: 0ms; }
}
''')]),

'Token: primitif, semantik, komponen': dict(
  ist=[('Primitive / reference token', 'Nilai mentah tanpa makna: teal.600, space.4.'),
       ('Semantic / system token', 'Makna penggunaan: color.bg.brand, color.text.on-brand.'),
       ('Component token', 'Spesifik komponen: button.primary.bg; opsional, dipakai saat butuh kontrol per komponen.'),
       ('Token tier rule', 'Komponen hanya merujuk token semantik atau komponen, tidak pernah primitif langsung.')],
  cx=[P('Linter: komponen tidak boleh memakai token primitif', '''
import re
primitif = {"teal.600", "slate.900", "red.700", "space.4"}
komponen = {
    "Button": {"bg": "color.action.primary", "fg": "color.text.on-action", "pad": "space.inset.md"},
    "Alert":  {"bg": "red.700", "fg": "color.text.on-danger", "pad": "space.4"},
    "Card":   {"bg": "color.surface.raised", "fg": "color.text.default", "pad": "space.inset.lg"},
}
for nama, props in komponen.items():
    salah = {k: v for k, v in props.items() if v in primitif}
    print(f"{nama:7} {'OK' if not salah else 'LANGGAR: ' + str(salah)}")
''')]),

'Warna fungsional & kontras': dict(
  ist=[('Functional color', 'Warna dengan fungsi: aksi, tautan, fokus, status, latar, teks, border.'),
       ('On-color', 'Warna teks/ikon di atas warna tertentu (on-primary, on-danger) yang dijamin kontras.'),
       ('Contrast matrix', 'Tabel semua pasangan foreground-background yang diizinkan beserta rasio kontrasnya.'),
       ('Focus color', 'Warna cincin fokus yang kontras ≥ 3:1 terhadap latar di semua tema.')],
  cx=[P('Matriks kontras untuk pasangan yang diizinkan', '''
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def r(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)
fg = {"text.default": "#0F172A", "text.muted": "#475569", "text.on-action": "#FFFFFF", "text.link": "#0E7490"}
bg = {"bg.default": "#FFFFFF", "bg.subtle": "#F1F5F9", "action.primary": "#0F766E"}
print(f"{'':16}" + "".join(f"{b:>16}" for b in bg))
for nf, vf in fg.items():
    print(f"{nf:16}" + "".join(f"{r(vf, vb):>13.2f}{'  ' if r(vf, vb) >= 4.5 else ' x'} " for vb in bg.values()))
print("x = di bawah 4.5:1, pasangan ini tidak boleh dipakai untuk teks biasa")
''')]),

'Skala tipografi & jarak': dict(
  ist=[('Type scale token', 'Ukuran huruf resmi sebagai token: font.size.100 ... font.size.900.'),
       ('Spacing scale', 'Skala jarak 4-based: 0, 2, 4, 8, 12, 16, 24, 32, 48, 64.'),
       ('Inset / stack / inline', 'Jenis jarak: padding dalam (inset), vertikal antar elemen (stack), horizontal (inline).'),
       ('Responsive token', 'Nilai token berbeda per breakpoint, misalnya space.section 32px di HP, 64px di desktop.')],
  cx=[P('Membangkitkan token jarak dan tipe sebagai JSON DTCG', '''
import json
jarak = {str(k): {"$type": "dimension", "$value": {"value": v, "unit": "px"}} for k, v in
         {"0": 0, "1": 4, "2": 8, "3": 12, "4": 16, "6": 24, "8": 32, "12": 48}.items()}
dasar, rasio = 16, 1.2
tipe = {str(100 * (i + 1)): {"$type": "dimension", "$value": {"value": round(dasar * rasio ** (i - 1)), "unit": "px"}} for i in range(6)}
for grup, isi in (("space", jarak), ("font-size", tipe)):
    for k, v in list(isi.items())[:3]:
        print(f'"{grup}.{k}":', json.dumps(v))
print("ukuran tipe:", [t["$value"]["value"] for t in tipe.values()])
''')]),

'Mode gelap dengan token CSS': dict(
  ist=[('Theme mode', 'Kumpulan nilai token untuk satu tema (light, dark, high-contrast).'),
       ('Mode switching', 'Mengganti tema dengan atribut data-theme atau mengikuti sistem.'),
       ('light-dark()', 'Fungsi CSS baru yang memilih nilai berdasarkan color-scheme aktif.'),
       ('Image & illustration adaptation', 'Gambar/ilustrasi juga disesuaikan (atau diberi latar) agar tidak menyilaukan di mode gelap.')],
  cx=[C('Satu deklarasi untuk dua tema dengan light-dark()', '''
:root { color-scheme: light dark; }
:root[data-theme="light"] { color-scheme: light; }
:root[data-theme="dark"]  { color-scheme: dark; }

:root {
  --color-bg:         light-dark(#FFFFFF, #0B1220);
  --color-surface:    light-dark(#F8FAFC, #131C2E);
  --color-text:       light-dark(#0F172A, #E2E8F0);
  --color-action:     light-dark(#0F766E, #2DD4BF);
  --color-on-action:  light-dark(#FFFFFF, #042F2E);
}
/* Fallback browser lama: definisikan ulang dengan @media (prefers-color-scheme: dark). */
''')]),

'Token lintas platform: format DTCG': dict(
  ist=[('DTCG', 'Design Tokens Community Group (W3C Community Group); spesifikasi stabil pertama 2025.10 dirilis Oktober 2025.'),
       ('$value / $type / $description', 'Properti standar token DTCG; alias ditulis {grup.token}.'),
       ('Style Dictionary / Tokens Studio', 'Alat yang membaca DTCG dan menghasilkan CSS, Swift, Kotlin/Compose, Flutter.'),
       ('Multi-brand', 'Satu set token semantik dengan beberapa set primitif per brand.')],
  cx=[P('Mengubah token DTCG menjadi CSS, Kotlin, dan Swift', '''
import json
dtcg = json.loads("""{
 "color": {
  "teal": {"600": {"$type": "color", "$value": "#0F766E"}},
  "action": {"primary": {"$type": "color", "$value": "{color.teal.600}", "$description": "Tombol utama"}}
 },
 "radius": {"md": {"$type": "dimension", "$value": {"value": 10, "unit": "px"}}}
}""")
def daun(d, jalur=()):
    for k, v in d.items():
        if isinstance(v, dict) and "$value" in v: yield jalur + (k,), v
        elif isinstance(v, dict): yield from daun(v, jalur + (k,))
semua = dict(daun(dtcg))
def nilai(v):
    x = v["$value"]
    if isinstance(x, str) and x.startswith("{"): return nilai(semua[tuple(x[1:-1].split("."))])
    return x
for jalur, v in semua.items():
    x = nilai(v)
    if v["$type"] == "color":
        print(f"CSS    --{'-'.join(jalur)}: {x};")
        print(f"Kotlin val {''.join(p.title() for p in jalur)} = Color(0xFF{x[1:]})")
        print(f"Swift  static let {jalur[0]}{''.join(p.title() for p in jalur[1:])} = Color(hex: 0x{x[1:]})")
    else:
        print(f"CSS    --{'-'.join(jalur)}: {x['value']}{x['unit']};   Kotlin {x['value']}.dp   Swift {x['value']}")
''')]),

'Komponen tombol lengkap dengan state': dict(
  ist=[('Button API', 'Props yang konsisten: variant, size, iconStart, iconEnd, loading, disabled, fullWidth.'),
       ('aria-disabled vs disabled', 'disabled menghapus tombol dari urutan fokus; aria-disabled tetap fokus dan bisa memberi penjelasan.'),
       ('Touch target', 'Area sentuh minimal 44-48px walau tampilan tombol kecil.'),
       ('Visual regression test', 'Tes tangkapan layar otomatis setiap state agar perubahan tak sengaja terdeteksi.')],
  cx=[C('Komponen Button React dengan API design system', '''
type Props = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary" | "ghost" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
  iconStart?: React.ReactNode;
};

export function Button({ variant = "primary", size = "md", loading = false, iconStart, children, disabled, ...rest }: Props) {
  return (
    <button
      {...rest}
      className={`ds-btn ds-btn--${variant} ds-btn--${size}`}
      aria-disabled={disabled || loading || undefined}
      aria-busy={loading || undefined}
      onClick={disabled || loading ? (e) => e.preventDefault() : rest.onClick}
    >
      {loading ? <Spinner aria-hidden /> : iconStart}
      <span>{children}</span>
    </button>
  );
}
// <Button variant="danger" loading={menghapus}>Hapus alamat</Button>
''', lang='tsx')]),

'Anatomi komponen form & umpan balik': dict(
  ist=[('Inline validation', 'Validasi saat field kehilangan fokus (blur), bukan setiap ketikan pertama.'),
       ('Error summary', 'Ringkasan error di atas form setelah submit, berisi tautan ke field yang salah.'),
       ('Required indicator', 'Tandai field wajib atau opsional secara konsisten (lebih sedikit yang ditandai lebih baik).'),
       ('Accessible name & description', 'Label sebagai nama, helper/error sebagai deskripsi (aria-describedby).')],
  cx=[P('Aturan kapan validasi ditampilkan', '''
def tampilkan_error(field):
    if field["dikirim"]:
        return True                       # setelah submit: tampilkan semua
    if field["pernah_blur"] and field["isi"]:
        return True                       # sudah diisi lalu ditinggalkan
    return False                          # sedang mengetik pertama kali: jangan ganggu

kasus = [
    {"nama": "email sedang diketik", "dikirim": False, "pernah_blur": False, "isi": "rina@"},
    {"nama": "email ditinggalkan", "dikirim": False, "pernah_blur": True, "isi": "rina@"},
    {"nama": "field kosong dilewati", "dikirim": False, "pernah_blur": True, "isi": ""},
    {"nama": "submit dengan field kosong", "dikirim": True, "pernah_blur": False, "isi": ""},
]
for k in kasus:
    print(f"{k['nama']:28} -> {'tampilkan error' if tampilkan_error(k) else 'tahan dulu'}")
''')]),

'Memilih komponen umpan balik: toast, banner, modal': dict(
  ist=[('Toast / snackbar', 'Pesan singkat sementara untuk konfirmasi; jangan untuk error penting.'),
       ('Banner', 'Pesan menetap di atas konten untuk status sistem atau peringatan.'),
       ('Modal', 'Menghentikan alur untuk keputusan penting atau berisiko.'),
       ('Interruption level', 'Seberapa mengganggu umpan balik; pilih yang paling rendah yang masih efektif.')],
  cx=[P('Pohon keputusan komponen umpan balik', '''
def pilih(terkait_field, penting, menghalangi, sementara):
    if menghalangi:
        return "Modal (keputusan berisiko, harus dijawab)"
    if terkait_field:
        return "Pesan inline di field terkait"
    if penting and not sementara:
        return "Banner (menetap sampai keadaan berubah)"
    if sementara:
        return "Toast (hilang sendiri, opsi Urungkan)"
    return "Teks status di halaman"
for situasi, arg in [("Alamat disimpan", (False, False, False, True)),
                     ("Saldo tidak cukup saat checkout", (False, True, False, False)),
                     ("Hapus akun permanen", (False, True, True, False)),
                     ("Format nomor HP salah", (True, True, False, False)),
                     ("Koneksi terputus, mode offline", (False, True, False, False))]:
    print(f"{situasi:33} -> {pilih(*arg)}")
''')]),

'Dokumentasi & katalog komponen': dict(
  ist=[('Storybook', 'Alat katalog komponen kode dengan stories per state, dokumentasi, dan tes.'),
       ('Zeroheight / Supernova', 'Situs dokumentasi design system yang menyatukan Figma dan kode.'),
       ('Living documentation', 'Dokumentasi yang dibangkitkan dari kode/token sehingga tidak basi.'),
       ('Code Connect', 'Fitur Figma yang menampilkan cuplikan kode komponen asli di Dev Mode.')],
  cx=[C('Story Storybook untuk semua state tombol', '''
// Button.stories.tsx
import type { Meta, StoryObj } from "@storybook/react";
import { Button } from "./Button";

const meta: Meta<typeof Button> = {
  title: "Komponen/Button",
  component: Button,
  args: { children: "Simpan perubahan" },
  argTypes: { variant: { control: "inline-radio", options: ["primary", "secondary", "ghost", "danger"] } },
  parameters: { docs: { description: { component: "Satu tombol primary per layar. Label kata kerja spesifik." } } },
};
export default meta;
type S = StoryObj<typeof Button>;

export const Primary: S = {};
export const Memuat: S = { args: { loading: true } };
export const Nonaktif: S = { args: { disabled: true } };
export const Bahaya: S = { args: { variant: "danger", children: "Hapus alamat" } };
export const LabelPanjang: S = { args: { children: "Lanjutkan ke pembayaran dengan virtual account" } };
''', lang='tsx')]),

'Versi, kontribusi & metrik adopsi': dict(
  ist=[('Semantic versioning', 'MAJOR.MINOR.PATCH: major untuk perubahan yang merusak, minor fitur baru, patch perbaikan.'),
       ('Deprecation policy', 'Komponen lama diberi peringatan dan masa transisi sebelum dihapus.'),
       ('Contribution model', 'Alur tim produk mengusulkan komponen: proposal → review → build → rilis.'),
       ('Adoption metric', 'Persentase komponen di produk yang berasal dari design system.')],
  cx=[P('Mengukur adopsi dari pemindaian kode', '''
import re
from collections import Counter
kode = """
import { Button, Card } from "@celengan/ds";
<Button>Simpan</Button> <Card/> <button class="btn-lama">Batal</button>
<Button variant="ghost">Lewati</Button> <div class="card-custom"></div> <Card/>
<button class="btn-lama">Kirim</button> <Modal/> <Button>OK</Button>
"""
ds = Counter(re.findall(r"<(Button|Card|Modal)\\b", kode))
lokal = Counter(re.findall(r'class="(btn-lama|card-custom)"', kode))
total_ds, total_lokal = sum(ds.values()), sum(lokal.values())
print("komponen DS   :", dict(ds))
print("komponen lokal:", dict(lokal))
print(f"adopsi: {total_ds / (total_ds + total_lokal):.0%}")
versi = "2.4.1"
major, minor, patch = map(int, versi.split("."))
print("ubah API props Button ->", f"{major + 1}.0.0", "| tambah varian baru ->", f"{major}.{minor + 1}.0", "| perbaiki warna fokus ->", f"{major}.{minor}.{patch + 1}")
''')]),

'Aksesibilitas bawaan komponen (WCAG 2.2)': dict(
  ist=[('Accessible by default', 'Komponen sudah benar aksesibilitasnya sehingga tim produk tidak perlu mengingat setiap aturan.'),
       ('2.4.11 Focus Not Obscured', 'Elemen yang fokus tidak boleh tertutup total oleh header lengket, banner cookie, atau bottom bar.'),
       ('2.5.8 Target Size (Minimum)', 'Target pointer minimal 24x24 CSS px atau berjarak cukup (AA).'),
       ('3.3.8 Accessible Authentication', 'Login tanpa tes kognitif; izinkan paste, password manager, passkey.')],
  cx=[C('Mencegah fokus tertutup header lengket (2.4.11)', '''
:root { --tinggi-header: 64px; --tinggi-bottom-nav: 72px; }
html {
  scroll-padding-top: calc(var(--tinggi-header) + 8px);      /* elemen fokus tidak tersembunyi di bawah header */
  scroll-padding-bottom: calc(var(--tinggi-bottom-nav) + 8px);
}
.ds-icon-btn { min-width: 44px; min-height: 44px; }             /* melampaui 24x24 minimum AA */
.ds-input[type="password"] { /* jangan blokir paste: tidak ada onpaste="return false" */ }
''')]),

'Design system mini "Celengan"': dict(
  ist=[('MVP design system', 'Versi awal: token dasar + 8-12 komponen paling sering dipakai.'),
       ('Release notes', 'Catatan rilis untuk setiap versi: apa yang baru, berubah, dan perlu migrasi.'),
       ('Governance', 'Siapa memutuskan perubahan, bagaimana proses review, dan jadwal rilis.'),
       ('Health metric', 'Adopsi, detach rate Figma, waktu respons kontribusi, jumlah bug aksesibilitas.')],
  cx=[P('Rencana rilis MVP design system Celengan', '''
backlog = [
    ("Token warna, tipe, jarak, radius", "fondasi", 3), ("Button", "komponen", 2), ("TextField", "komponen", 3),
    ("Card", "komponen", 1), ("ListItem", "komponen", 2), ("BottomNav", "komponen", 2), ("Toast", "komponen", 1),
    ("Dialog", "komponen", 2), ("ProgressBar celengan", "komponen", 1), ("Dokumentasi + Storybook", "dokumentasi", 3),
]
kapasitas_per_sprint = 8
sprint, beban = 1, 0
for item, jenis, poin in backlog:
    if beban + poin > kapasitas_per_sprint:
        sprint, beban = sprint + 1, 0
    beban += poin
    print(f"Sprint {sprint}: {item:32} ({jenis}, {poin} poin)")
print(f"Rilis v1.0.0 setelah {sprint} sprint")
''')]),
}
