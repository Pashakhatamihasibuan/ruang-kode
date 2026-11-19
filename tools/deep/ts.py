"""Pendalaman jalur TypeScript: istilah dunia kerja dan contoh TypeScript yang dijalankan dengan Node."""
K = 'ts'


def T(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='ts')


def X(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Kenapa TypeScript?': dict(
  ist=[('Static typing', 'Tipe diperiksa saat kompilasi, sebelum kode dijalankan pengguna.'),
       ('Superset JavaScript', 'Semua JavaScript valid adalah TypeScript valid; TS hanya menambah anotasi tipe.'),
       ('Type erasure', 'Anotasi tipe dihapus saat kompilasi; di runtime yang berjalan tetap JavaScript biasa.'),
       ('DX (developer experience)', 'Autocomplete, rename aman, dan navigasi kode yang akurat di editor.')],
  cx=[T('Bug yang ditangkap sebelum produksi', r'''
type Produk = { nama: string; harga: number; stok: number };

function totalNilaiStok(daftar: Produk[]): number {
  return daftar.reduce((jml, p) => jml + p.harga * p.stok, 0);
}

const gudang: Produk[] = [
  { nama: "Kopi 250g", harga: 45000, stok: 12 },
  { nama: "Teh hijau", harga: 28000, stok: 30 },
];
// gudang.push({ nama: "Gula", harga: "15000", stok: 5 });
//   ^ error TS2322: Type 'string' is not assignable to type 'number'.
//   Di JavaScript murni data ini lolos, lalu kode lain seperti s + p.harga
//   menyambung teks ("73000" + "15000" = "7300015000"), bukan menjumlah angka.
const rp = (n: number) => "Rp" + n.toLocaleString("id-ID");
console.log("Nilai stok:", rp(totalNilaiStok(gudang)));
''', 'Baris yang dikomentari adalah contoh yang akan ditolak compiler. Tipe membuat kontrak data terlihat jelas bagi rekan setim.')]),

'Memasang & menjalankan': dict(
  ist=[('tsc', 'TypeScript compiler: memeriksa tipe dan menghasilkan file .js.'),
       ('tsconfig.json', 'Konfigurasi proyek: target, module, strict, paths, outDir.'),
       ('strict mode', 'Kumpulan pemeriksaan ketat (strictNullChecks, noImplicitAny, dll.); wajib di proyek baru.'),
       ('Type stripping', 'Node 22.6+ dan Bun/Deno bisa menjalankan .ts langsung dengan membuang anotasi tipe.'),
       ('tsx / ts-node', 'Alat untuk menjalankan TypeScript langsung saat pengembangan.')],
  cx=[X('Memulai proyek TypeScript', r'''
npm init -y
npm install -D typescript @types/node
npx tsc --init                 # membuat tsconfig.json

# tsconfig.json minimal yang direkomendasikan 2026
{
  "compilerOptions": {
    "target": "ES2023",
    "module": "NodeNext",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "outDir": "dist",
    "skipLibCheck": true
  },
  "include": ["src"]
}

npx tsc --noEmit               # hanya periksa tipe (dipakai di CI)
npx tsc                        # periksa + hasilkan dist/*.js
node --experimental-strip-types src/main.ts   # Node 22: jalankan .ts langsung''', lang='bash'),
      T('Program pertama yang dijalankan', r'''
const sapa = (nama: string, jam: number): string =>
  jam < 11 ? `Selamat pagi, ${nama}` : jam < 15 ? `Selamat siang, ${nama}` : `Selamat sore, ${nama}`;

for (const jam of [8, 13, 17]) console.log(jam.toString().padStart(2, "0") + ":00", sapa("Rina", jam));
''')]),

'Primitif, array & tuple': dict(
  ist=[('Primitive type', 'string, number, boolean, bigint, symbol, null, undefined.'),
       ('Type inference', 'TS menebak tipe dari nilai awal; anotasi tidak selalu perlu.'),
       ('Tuple', 'Array dengan panjang dan tipe per posisi yang tetap, misalnya [string, number].'),
       ('readonly array', 'readonly number[] mencegah push/pop; cocok untuk data konfigurasi.')],
  cx=[T('Tuple untuk koordinat dan hasil fungsi', r'''
type Koordinat = [lat: number, lng: number];
const kantor: Koordinat = [-6.2088, 106.8456];

function minMax(nilai: readonly number[]): [min: number, max: number] {
  return [Math.min(...nilai), Math.max(...nilai)];
}
const suhu = [27.5, 31.2, 29.8, 33.1, 26.4] as const;
const [rendah, tinggi] = minMax(suhu);
console.log(`Kantor di ${kantor[0]}, ${kantor[1]}`);
console.log(`Suhu minggu ini: ${rendah}°C sampai ${tinggi}°C`);
const besar: bigint = 2n ** 64n;
console.log("2^64 =", besar.toString());
''')]),

'Objek, literal & enum': dict(
  ist=[('Object type', 'Bentuk objek ditulis sebagai { kunci: tipe }.'),
       ('Optional property', 'kunci?: tipe berarti boleh tidak ada (bernilai undefined).'),
       ('Literal type', 'Tipe yang hanya menerima nilai tertentu, misalnya "pending" | "lunas".'),
       ('enum vs union literal', 'Tim modern lebih memilih union literal karena tidak menghasilkan kode runtime.')],
  cx=[T('Union literal vs enum untuk status pesanan', r'''
type Status = "baru" | "dibayar" | "dikirim" | "selesai";
enum Prioritas { Rendah = 1, Normal = 2, Tinggi = 3 }

interface Pesanan { id: string; status: Status; prioritas: Prioritas; catatan?: string }

const daftar: Pesanan[] = [
  { id: "INV-001", status: "dikirim", prioritas: Prioritas.Normal },
  { id: "INV-002", status: "baru", prioritas: Prioritas.Tinggi, catatan: "kirim pagi" },
];
for (const p of daftar) {
  console.log(p.id, p.status.padEnd(8), Prioritas[p.prioritas], p.catatan ?? "-");
}
// const salah: Status = "batal";   // error: "batal" bukan bagian dari Status
''', 'Enum menghasilkan objek di runtime (Prioritas[3] menjadi "Tinggi"), sedangkan union literal hilang total setelah kompilasi.')]),

'any, unknown, never & void': dict(
  ist=[('any', 'Mematikan pemeriksaan tipe; hindari, ia "menular" ke kode lain.'),
       ('unknown', 'Versi aman dari any: wajib dipersempit (narrowing) sebelum dipakai.'),
       ('never', 'Tipe untuk nilai yang tidak mungkin terjadi; dipakai untuk exhaustive check.'),
       ('void', 'Fungsi yang tidak mengembalikan nilai bermakna.')],
  cx=[T('unknown dari JSON.parse dan exhaustive check dengan never', r'''
function bacaUmur(json: string): number {
  const data: unknown = JSON.parse(json);
  if (typeof data === "object" && data !== null && "umur" in data && typeof data.umur === "number") {
    return data.umur;
  }
  throw new Error("format tidak valid");
}

type Bentuk = { jenis: "persegi"; sisi: number } | { jenis: "lingkaran"; r: number };
function luas(b: Bentuk): number {
  switch (b.jenis) {
    case "persegi": return b.sisi ** 2;
    case "lingkaran": return Math.PI * b.r ** 2;
    default: { const mustahil: never = b; return mustahil; }  // error jika ada jenis baru belum ditangani
  }
}
const log = (pesan: string): void => console.log("[log]", pesan);

console.log(bacaUmur('{"umur": 24}'));
try { bacaUmur('{"umur": "24"}'); } catch (e) { log((e as Error).message); }
console.log(luas({ jenis: "lingkaran", r: 2 }).toFixed(2));
''')]),

'Menulis tipe fungsi': dict(
  ist=[('Parameter type & return type', 'Anotasi pada parameter dan hasil fungsi.'),
       ('Optional & default parameter', 'diskon?: number atau diskon = 0.'),
       ('Rest parameter', '...angka: number[] untuk jumlah argumen bebas.'),
       ('Function type', 'Tipe untuk variabel berisi fungsi: (a: number) => string.')],
  cx=[T('Fungsi harga dengan default, optional, dan rest', r'''
type Formatter = (n: number) => string;
const rupiah: Formatter = (n) => "Rp" + Math.round(n).toLocaleString("id-ID");

function hargaAkhir(harga: number, diskonPersen = 0, ongkir?: number): number {
  return harga * (1 - diskonPersen / 100) + (ongkir ?? 0);
}
function totalBelanja(...item: number[]): number {
  return item.reduce((a, b) => a + b, 0);
}

console.log(rupiah(hargaAkhir(150000)));
console.log(rupiah(hargaAkhir(150000, 10)));
console.log(rupiah(hargaAkhir(150000, 10, 12000)));
console.log("Total keranjang:", rupiah(totalBelanja(45000, 28000, 15500)));
''')]),

'Overload fungsi': dict(
  ist=[('Function overload', 'Beberapa tanda tangan (signature) untuk satu implementasi.'),
       ('Overload signature vs implementation signature', 'Hanya signature overload yang terlihat oleh pemanggil.'),
       ('Union parameter', 'Alternatif yang lebih sederhana bila tipe hasil tidak bergantung pada input.')],
  cx=[T('Satu fungsi, hasil berbeda sesuai input', r'''
function format(nilai: number): string;
function format(nilai: Date): string;
function format(nilai: number | Date): string {
  if (typeof nilai === "number") return nilai.toLocaleString("id-ID");
  const p = (x: number) => String(x).padStart(2, "0");
  return `${p(nilai.getDate())}/${p(nilai.getMonth() + 1)}/${nilai.getFullYear()}`;
}

function ambil(id: number): { id: number; nama: string };
function ambil(id: number[]): { id: number; nama: string }[];
function ambil(id: number | number[]) {
  const db: Record<number, string> = { 1: "Andi", 2: "Sari", 3: "Budi" };
  return Array.isArray(id) ? id.map((i) => ({ id: i, nama: db[i] })) : { id, nama: db[id] };
}

console.log(format(1250000));
console.log(format(new Date(2026, 7, 17)));
console.log(ambil(2).nama);
console.log(ambil([1, 3]).map((u) => u.nama).join(", "));
''')]),

'Fungsi orde tinggi & callback bertipe': dict(
  ist=[('Higher-order function', 'Fungsi yang menerima atau mengembalikan fungsi.'),
       ('Callback', 'Fungsi yang diberikan untuk dipanggil nanti, misalnya di map/filter.'),
       ('Closure', 'Fungsi yang mengingat variabel dari lingkup tempat ia dibuat.'),
       ('Debounce', 'Menunda eksekusi sampai input berhenti; dipakai di kolom pencarian.')],
  cx=[T('Membuat middleware, memoize, dan debounce bertipe', r'''
function memoize<A extends string | number, R>(fn: (a: A) => R): (a: A) => R {
  const cache = new Map<A, R>();
  return (a) => {
    if (!cache.has(a)) { console.log("  hitung", a); cache.set(a, fn(a)); }
    return cache.get(a)!;
  };
}
const ongkir = memoize((kota: string) => ({ Jakarta: 9000, Bandung: 12000 } as Record<string, number>)[kota] ?? 25000);
console.log(ongkir("Bandung"), ongkir("Bandung"), ongkir("Medan"));

function debounce<T extends unknown[]>(fn: (...a: T) => void, ms: number) {
  let t: ReturnType<typeof setTimeout> | undefined;
  return (...a: T) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
}
const cari = debounce((q: string) => console.log("cari ke server:", q), 50);
for (const q of ["l", "la", "lap", "lapt", "laptop"]) cari(q);   // hanya "laptop" yang dikirim
''')]),

'Interface & extends': dict(
  ist=[('interface', 'Mendeskripsikan bentuk objek; bisa di-extend dan digabung (declaration merging).'),
       ('extends', 'Mewarisi properti interface lain.'),
       ('implements', 'Kelas berjanji memenuhi bentuk sebuah interface.'),
       ('Index signature', '{ [kunci: string]: number } untuk objek dengan kunci dinamis.')],
  cx=[T('Hierarki pengguna: Pengguna, Pelanggan, Admin', r'''
interface Pengguna { id: number; nama: string; email: string }
interface Pelanggan extends Pengguna { poin: number; alamat?: string }
interface Admin extends Pengguna { hak: ("baca" | "tulis" | "hapus")[] }

const ana: Pelanggan = { id: 1, nama: "Ana", email: "ana@contoh.id", poin: 1200 };
const dodi: Admin = { id: 2, nama: "Dodi", email: "dodi@contoh.id", hak: ["baca", "tulis"] };

const bolehHapus = (u: Pengguna | Admin) => "hak" in u && u.hak.includes("hapus");
interface StokGudang { [sku: string]: number }
const stok: StokGudang = { "KP-250": 12, "TH-100": 30 };

console.log(ana.nama, "poin", ana.poin);
console.log(dodi.nama, "boleh hapus?", bolehHapus(dodi));
console.log("SKU:", Object.keys(stok).join(", "));
''')]),

'Type alias, union & intersection': dict(
  ist=[('type alias', 'Nama untuk tipe apa pun: objek, union, tuple, fungsi.'),
       ('Union (A | B)', 'Nilai salah satu dari beberapa tipe.'),
       ('Intersection (A & B)', 'Gabungan semua properti dari beberapa tipe.'),
       ('interface vs type', 'Konvensi umum: interface untuk bentuk objek publik, type untuk union dan komposisi.')],
  cx=[T('Menyusun tipe respons API dengan union dan intersection', r'''
type Timestamp = { dibuat: string; diubah: string };
type Artikel = { id: number; judul: string } & Timestamp;

type Sukses<T> = { ok: true; data: T };
type Gagal = { ok: false; kode: number; pesan: string };
type Respons<T> = Sukses<T> | Gagal;

function tampil(r: Respons<Artikel[]>) {
  if (r.ok) r.data.forEach((a) => console.log(`#${a.id} ${a.judul} (diubah ${a.diubah})`));
  else console.log(`Gagal ${r.kode}: ${r.pesan}`);
}
tampil({ ok: true, data: [{ id: 7, judul: "Belajar TypeScript", dibuat: "2026-01-02", diubah: "2026-03-10" }] });
tampil({ ok: false, kode: 503, pesan: "server sedang pemeliharaan" });
''')]),

'Type guard & discriminated union': dict(
  ist=[('Narrowing', 'TS mempersempit tipe setelah pengecekan typeof, instanceof, in, atau ===.'),
       ('Type guard', 'Pengecekan yang membuat tipe menyempit di dalam blok if.'),
       ('Discriminated union', 'Union dengan properti penanda (tag) yang sama, misalnya type atau kind.'),
       ('State machine', 'Status UI (idle, loading, success, error) dimodelkan dengan discriminated union.')],
  cx=[T('State pemuatan data seperti di aplikasi React', r'''
type State<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: string };

function render(s: State<string[]>): string {
  switch (s.status) {
    case "idle": return "Tekan tombol untuk memuat";
    case "loading": return "Memuat...";
    case "success": return `${s.data.length} produk: ${s.data.join(", ")}`;
    case "error": return `Terjadi kesalahan: ${s.error}`;
  }
}
const urutan: State<string[]>[] = [
  { status: "idle" }, { status: "loading" },
  { status: "success", data: ["Kopi", "Teh"] }, { status: "error", error: "timeout 5s" },
];
urutan.forEach((s) => console.log(render(s)));
''', 'Dengan pola ini tidak mungkin ada data dan error sekaligus, sehingga UI tidak pernah berada di keadaan yang mustahil.')]),

'as, as const, ! & satisfies': dict(
  ist=[('Type assertion (as)', 'Memberi tahu compiler "percaya saya"; tidak ada pengecekan runtime.'),
       ('as const', 'Membuat nilai readonly dan bertipe literal paling sempit.'),
       ('Non-null assertion (!)', 'Menyatakan nilai pasti bukan null/undefined; pakai seperlunya.'),
       ('satisfies', 'Memeriksa nilai cocok dengan tipe tanpa kehilangan tipe literalnya (TS 4.9+).')],
  cx=[T('Konfigurasi rute dengan as const dan satisfies', r'''
type Rute = { path: string; auth: boolean };

const RUTE = {
  beranda: { path: "/", auth: false },
  profil: { path: "/profil", auth: true },
  admin: { path: "/admin", auth: true },
} satisfies Record<string, Rute>;
// kunci tetap terbaca persis: "beranda" | "profil" | "admin"
type NamaRute = keyof typeof RUTE;

const PERAN = ["tamu", "anggota", "admin"] as const;
type Peran = (typeof PERAN)[number];   // "tamu" | "anggota" | "admin"

const peta = new Map<NamaRute, Peran>([["admin", "admin"], ["profil", "anggota"]]);
const butuh = peta.get("admin")!;      // kita tahu kuncinya ada
for (const n of Object.keys(RUTE) as NamaRute[]) {
  console.log(n.padEnd(8), RUTE[n].path.padEnd(8), RUTE[n].auth ? "login" : "publik");
}
console.log("peran untuk /admin:", butuh, "| semua peran:", PERAN.join(", "));
''')]),

'Validasi data dari API dengan type predicate': dict(
  ist=[('Type predicate', 'Fungsi dengan hasil x is T yang mempersempit tipe di pemanggil.'),
       ('Runtime validation', 'Tipe TS hilang saat runtime; data dari luar harus divalidasi.'),
       ('Zod / Valibot', 'Pustaka skema populer: satu skema menghasilkan validator dan tipe TS sekaligus.'),
       ('Parse, don\'t validate', 'Ubah data mentah menjadi tipe yang sudah pasti benar di batas sistem.')],
  cx=[T('Memvalidasi respons API tanpa pustaka', r'''
interface Produk { sku: string; nama: string; harga: number }

function isProduk(x: unknown): x is Produk {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return typeof o.sku === "string" && typeof o.nama === "string"
    && typeof o.harga === "number" && o.harga >= 0;
}

const mentah: unknown = JSON.parse(`[
  {"sku":"KP-250","nama":"Kopi","harga":45000},
  {"sku":"TH-100","nama":"Teh","harga":"28000"},
  {"sku":"GL-1K","nama":"Gula","harga":16500},
  null
]`);
const daftar = Array.isArray(mentah) ? mentah : [];
const valid = daftar.filter(isProduk);              // bertipe Produk[]
const ditolak = daftar.length - valid.length;
valid.forEach((p) => console.log(p.sku, p.nama, p.harga.toLocaleString("id-ID")));
console.log(`${ditolak} baris ditolak dan dicatat ke log`);
'''),
      X('Versi produksi dengan Zod', r'''
import { z } from "zod";

const ProdukSchema = z.object({
  sku: z.string().regex(/^[A-Z]{2}-\w+$/),
  nama: z.string().min(1),
  harga: z.number().int().nonnegative(),
});
type Produk = z.infer<typeof ProdukSchema>;   // tipe otomatis dari skema

const hasil = ProdukSchema.array().safeParse(await res.json());
if (!hasil.success) console.error(hasil.error.issues);
else render(hasil.data);''', lang='ts')]),

'Kelas & modifier akses': dict(
  ist=[('public / private / protected', 'Mengatur siapa yang boleh mengakses anggota kelas.'),
       ('#private field', 'Private asli JavaScript yang tetap tersembunyi di runtime.'),
       ('readonly', 'Properti hanya boleh diisi saat konstruksi.'),
       ('Parameter property', 'constructor(private saldo: number) sekaligus mendeklarasikan dan mengisi properti.')],
  cx=[T('Rekening dengan saldo yang terlindungi', r'''
class Rekening {
  static jumlahDibuat = 0;
  #riwayat: string[] = [];
  constructor(public readonly nomor: string, private saldo: number = 0) { Rekening.jumlahDibuat++; }

  setor(n: number) { this.saldo += n; this.#riwayat.push(`+${n}`); return this; }
  tarik(n: number) {
    if (n > this.saldo) throw new Error(`saldo kurang ${(n - this.saldo).toLocaleString("id-ID")}`);
    this.saldo -= n; this.#riwayat.push(`-${n}`); return this;
  }
  get ringkasan() { return `${this.nomor}: Rp${this.saldo.toLocaleString("id-ID")} [${this.#riwayat.join(" ")}]`; }
}

const r = new Rekening("1234-5678", 100000).setor(50000).tarik(30000);
console.log(r.ringkasan);
try { r.tarik(500000); } catch (e) { console.log("Ditolak:", (e as Error).message); }
// r.saldo = 1e9;   // error: 'saldo' is private
console.log("Rekening dibuat:", Rekening.jumlahDibuat);
''')]),

'Kelas abstrak & polimorfisme': dict(
  ist=[('abstract class', 'Kelas dasar yang tidak bisa dibuat langsung; berisi kerangka.'),
       ('abstract method', 'Metode tanpa isi yang wajib diimplementasikan kelas turunan.'),
       ('Polimorfisme', 'Satu antarmuka, banyak perilaku: kode memanggil metode yang sama di objek berbeda.'),
       ('Strategy pattern', 'Memilih algoritma (misalnya metode pembayaran) saat runtime.')],
  cx=[T('Metode pembayaran dengan strategy pattern', r'''
abstract class Pembayaran {
  constructor(protected jumlah: number) {}
  abstract biaya(): number;
  abstract get nama(): string;
  total() { return this.jumlah + this.biaya(); }
  struk() { return `${this.nama.padEnd(16)} biaya ${String(this.biaya()).padStart(5)}  total ${this.total().toLocaleString("id-ID")}`; }
}
class TransferVA extends Pembayaran { get nama() { return "Virtual Account"; } biaya() { return 4000; } }
class QRIS extends Pembayaran { get nama() { return "QRIS"; } biaya() { return Math.round(this.jumlah * 0.007); } }
class KartuKredit extends Pembayaran { get nama() { return "Kartu kredit"; } biaya() { return Math.round(this.jumlah * 0.029) + 2000; } }

const belanja = 250000;
const opsi: Pembayaran[] = [new TransferVA(belanja), new QRIS(belanja), new KartuKredit(belanja)];
opsi.forEach((p) => console.log(p.struk()));
const termurah = opsi.reduce((a, b) => (b.total() < a.total() ? b : a));
console.log("Termurah:", termurah.nama);
''')]),

'Fungsi & tipe generik': dict(
  ist=[('Generic', 'Parameter tipe <T> agar fungsi/tipe bekerja untuk banyak tipe tanpa kehilangan informasi.'),
       ('Type argument inference', 'T biasanya ditebak dari argumen; tidak perlu ditulis manual.'),
       ('Generic type', 'Tipe dengan parameter, misalnya Respons<T> atau Paginasi<T>.')],
  cx=[T('Paginasi dan groupBy generik', r'''
type Halaman<T> = { item: T[]; halaman: number; totalHalaman: number };

function paginasi<T>(data: T[], halaman: number, perHalaman: number): Halaman<T> {
  const mulai = (halaman - 1) * perHalaman;
  return { item: data.slice(mulai, mulai + perHalaman), halaman, totalHalaman: Math.ceil(data.length / perHalaman) };
}
function kelompokkan<T, K extends string>(data: T[], kunci: (x: T) => K): Record<K, T[]> {
  return data.reduce((acc, x) => { (acc[kunci(x)] ??= []).push(x); return acc; }, {} as Record<K, T[]>);
}

const siswa = ["Ani", "Bayu", "Citra", "Dewi", "Eka", "Fajar", "Gita"];
const h2 = paginasi(siswa, 2, 3);
console.log(`Halaman ${h2.halaman}/${h2.totalHalaman}:`, h2.item.join(", "));

const nilai = [{ n: "Ani", skor: 88 }, { n: "Bayu", skor: 72 }, { n: "Citra", skor: 95 }, { n: "Dewi", skor: 64 }];
const grup = kelompokkan(nilai, (x) => (x.skor >= 85 ? "A" : x.skor >= 70 ? "B" : "C"));
for (const [g, isi] of Object.entries(grup)) console.log(g, isi.map((x) => x.n).join(", "));
''')]),

'Constraint generik & tipe bawaan': dict(
  ist=[('Constraint (extends)', '<T extends { id: number }> membatasi T agar punya properti tertentu.'),
       ('keyof constraint', '<K extends keyof T> memastikan kunci benar-benar ada di T.'),
       ('Default type parameter', '<T = string> memberi tipe bawaan bila tidak ditentukan.'),
       ('Promise<T>, Map<K, V>, Set<T>', 'Tipe generik bawaan yang paling sering dipakai.')],
  cx=[T('Repository generik untuk entitas apa pun yang punya id', r'''
interface Entitas { id: number }

class Repo<T extends Entitas> {
  private data = new Map<number, T>();
  simpan(x: T) { this.data.set(x.id, x); return x; }
  cari(id: number): T | undefined { return this.data.get(id); }
  urutkan<K extends keyof T>(kunci: K): T[] {
    return [...this.data.values()].sort((a, b) => (a[kunci] < b[kunci] ? -1 : 1));
  }
}
interface Buku extends Entitas { judul: string; tahun: number }
const repo = new Repo<Buku>();
repo.simpan({ id: 3, judul: "Laskar Pelangi", tahun: 2005 });
repo.simpan({ id: 1, judul: "Bumi Manusia", tahun: 1980 });
repo.simpan({ id: 2, judul: "Cantik Itu Luka", tahun: 2002 });

console.log(repo.cari(2)?.judul);
console.log(repo.urutkan("tahun").map((b) => `${b.tahun} ${b.judul}`).join(" | "));
// repo.urutkan("penulis");   // error: "penulis" bukan keyof Buku

async function ambil<T = string>(nilai: T): Promise<T> { return nilai; }
ambil(42).then((n) => console.log("Promise<number> selesai:", n + 1));
''')]),

'Partial, Pick, Omit, Readonly & Record': dict(
  ist=[('Partial<T>', 'Semua properti menjadi opsional; cocok untuk data update (PATCH).'),
       ('Pick<T, K> / Omit<T, K>', 'Ambil atau buang sebagian properti; misalnya Omit<User, "password">.'),
       ('Readonly<T>', 'Semua properti tidak bisa diubah.'),
       ('Record<K, V>', 'Objek dengan kunci K dan nilai V.'),
       ('DTO', 'Data Transfer Object: bentuk data yang dikirim antar lapisan/ke API.')],
  cx=[T('Tipe DTO untuk API pengguna', r'''
interface User { id: number; nama: string; email: string; password: string; peran: "user" | "admin" }

type UserPublik = Omit<User, "password">;
type BuatUser = Omit<User, "id">;
type UbahUser = Partial<Pick<User, "nama" | "email">>;
type Izin = Record<User["peran"], readonly string[]>;

const izin: Readonly<Izin> = { user: ["baca"], admin: ["baca", "tulis", "hapus"] };

let db: User = { id: 1, nama: "Rina", email: "rina@contoh.id", password: "hash$2b$...", peran: "user" };
function ubah(id: number, patch: UbahUser): UserPublik {
  db = { ...db, ...patch };
  const { password, ...publik } = db;
  return publik;
}
const baru: BuatUser = { nama: "Joko", email: "joko@contoh.id", password: "x", peran: "admin" };
console.log(ubah(1, { email: "rina.w@contoh.id" }));
console.log("izin admin:", izin[baru.peran].join(", "));
''')]),

'Exclude, Extract, ReturnType & lainnya': dict(
  ist=[('Exclude<U, X> / Extract<U, X>', 'Buang atau ambil anggota union.'),
       ('NonNullable<T>', 'Buang null dan undefined.'),
       ('ReturnType<F> / Parameters<F>', 'Ambil tipe hasil atau parameter dari fungsi.'),
       ('Awaited<T>', 'Tipe isi Promise setelah di-await.')],
  cx=[T('Menurunkan tipe dari kode yang sudah ada', r'''
type Event = "klik" | "scroll" | "beli" | "daftar" | null;
type EventBisnis = Extract<Event, "beli" | "daftar">;
type EventUI = Exclude<NonNullable<Event>, EventBisnis>;

function buatPesanan(sku: string, qty: number, kupon?: string) {
  return { id: "ORD-" + sku + "-" + qty, total: qty * 45000, kupon: kupon ?? null };
}
type Pesanan = ReturnType<typeof buatPesanan>;
type Arg = Parameters<typeof buatPesanan>;

async function muatProfil() { return { nama: "Sari", level: 3 }; }
type Profil = Awaited<ReturnType<typeof muatProfil>>;

const ui: EventUI[] = ["klik", "scroll"];
const bisnis: EventBisnis = "beli";
const arg: Arg = ["KP-250", 2];
const p: Pesanan = buatPesanan(...arg);
muatProfil().then((pr: Profil) => console.log(ui.join("/"), bisnis, p.id, p.total, pr.nama));
''')]),

'keyof, mapped & conditional types': dict(
  ist=[('keyof', 'Union dari semua nama kunci sebuah tipe.'),
       ('Indexed access', 'T["kunci"] mengambil tipe satu properti.'),
       ('Mapped type', '{ [K in keyof T]: ... } membuat tipe baru dengan mengubah tiap properti.'),
       ('Conditional type', 'T extends U ? X : Y; dengan infer untuk mengambil bagian tipe.')],
  cx=[T('Membuat tipe form otomatis dari model data', r'''
interface Pendaftaran { nama: string; umur: number; setuju: boolean }

type Error_<T> = { [K in keyof T]?: string };
type Getter<T> = { [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K] };
type IsiArray<T> = T extends (infer U)[] ? U : T;

function validasi(f: Pendaftaran): Error_<Pendaftaran> {
  const e: Error_<Pendaftaran> = {};
  if (f.nama.trim().length < 3) e.nama = "Nama minimal 3 huruf";
  if (f.umur < 17) e.umur = "Umur minimal 17 tahun";
  if (!f.setuju) e.setuju = "Centang persetujuan data";
  return e;
}
const form: Pendaftaran = { nama: "Al", umur: 16, setuju: false };
for (const [k, pesan] of Object.entries(validasi(form))) console.log(k.padEnd(7), pesan);

const g: Getter<Pendaftaran> = { getNama: () => form.nama, getUmur: () => form.umur, getSetuju: () => form.setuju };
const x: IsiArray<string[]> = "elemen array bertipe string";
console.log(g.getNama(), g.getUmur(), "|", x);
''')]),

'Template literal & tipe rekursif': dict(
  ist=[('Template literal type', 'Tipe string berpola, misalnya `/api/${string}` atau `${Sumbu}-${Ukuran}`.'),
       ('Recursive type', 'Tipe yang merujuk dirinya sendiri: pohon menu, JSON, komentar bersarang.'),
       ('Intrinsic string types', 'Uppercase, Lowercase, Capitalize, Uncapitalize.')],
  cx=[T('Kelas utilitas spacing dan menu bersarang', r'''
type Sisi = "t" | "b" | "l" | "r" | "x" | "y";
type Ukuran = 0 | 1 | 2 | 4 | 8;
type KelasSpasi = `${"m" | "p"}${Sisi}-${Ukuran}`;     // 2 x 6 x 5 = 60 kombinasi valid
const k: KelasSpasi[] = ["mt-4", "px-2", "py-8"];
// const salah: KelasSpasi = "mt-3";   // error: 3 bukan Ukuran

type Menu = { label: string; href?: string; anak?: Menu[] };
const menu: Menu[] = [
  { label: "Beranda", href: "/" },
  { label: "Produk", anak: [
    { label: "Elektronik", anak: [{ label: "Laptop", href: "/p/laptop" }, { label: "Ponsel", href: "/p/ponsel" }] },
    { label: "Buku", href: "/p/buku" } ] },
];
function cetak(m: Menu[], lvl = 0): void {
  for (const x of m) { console.log("  ".repeat(lvl) + "- " + x.label + (x.href ? ` (${x.href})` : "")); if (x.anak) cetak(x.anak, lvl + 1); }
}
console.log(k.join(" "));
cetak(menu);
''')]),

'Modul, deklarasi & augmentasi': dict(
  ist=[('ES module', 'import/export; satu file satu modul.'),
       ('import type', 'Mengimpor hanya tipe sehingga hilang total di hasil JS.'),
       ('Declaration file (.d.ts)', 'Berisi tipe saja untuk pustaka JavaScript; paket @types/*.'),
       ('Module augmentation', 'Menambah tipe ke modul lain, misalnya properti user di Request Express.')],
  cx=[X('Struktur modul dan file deklarasi', r'''
// src/tipe.ts
export interface Produk { sku: string; harga: number }

// src/harga.ts
import type { Produk } from "./tipe.js";
export const totalHarga = (p: Produk[]) => p.reduce((a, b) => a + b.harga, 0);

// src/types/pustaka-lama.d.ts  -> memberi tipe untuk pustaka JS tanpa tipe
declare module "pustaka-lama" {
  export function hitung(a: number, b: number): number;
}

// src/types/express.d.ts  -> module augmentation
import "express";
declare module "express-serve-static-core" {
  interface Request { user?: { id: number; peran: "user" | "admin" } }
}

// Variabel global dari script lain (misalnya analytics)
declare global {
  interface Window { dataLayer: unknown[] }
}''', lang='ts'),
      T('Namespace dan declaration merging dalam satu file', r'''
interface Konfigurasi { apiUrl: string }
interface Konfigurasi { timeoutMs: number }        // digabung otomatis (declaration merging)

const conf: Konfigurasi = { apiUrl: "https://api.contoh.id", timeoutMs: 5000 };

namespace Validasi {
  export const email = (s: string) => /^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(s);
  export const telepon = (s: string) => /^(\+62|0)8\d{8,11}$/.test(s);
}
console.log(conf.apiUrl, conf.timeoutMs + "ms");
console.log(Validasi.email("dina@contoh.id"), Validasi.telepon("+6281234567890"), Validasi.telepon("021555"));
''')]),

'Decorator & alat ekosistem': dict(
  ist=[('Decorator', 'Fungsi yang membungkus kelas/metode; standar ECMAScript sejak TS 5.0.'),
       ('Angular & NestJS', 'Framework yang memakai decorator secara intensif (@Component, @Controller).'),
       ('ESLint + typescript-eslint', 'Linter dengan aturan yang memahami tipe.'),
       ('Vite, tsup, Biome', 'Alat build dan lint cepat yang umum di 2026.')],
  cx=[X('Decorator standar TS 5 untuk logging durasi', r'''
function ukurWaktu<This, Args extends unknown[], R>(
  target: (this: This, ...args: Args) => R,
  ctx: ClassMethodDecoratorContext,
) {
  return function (this: This, ...args: Args): R {
    const t0 = performance.now();
    const hasil = target.apply(this, args);
    console.log(`${String(ctx.name)} selesai ${(performance.now() - t0).toFixed(1)} ms`);
    return hasil;
  };
}

class Laporan {
  @ukurWaktu
  hitungOmzet(transaksi: number[]) { return transaksi.reduce((a, b) => a + b, 0); }
}''', 'Decorator butuh langkah kompilasi tsc/Vite/esbuild, jadi contoh ini tidak dijalankan langsung oleh Node.', lang='ts'),
      T('Prinsip yang sama tanpa sintaks decorator', r'''
function ukurWaktu<A extends unknown[], R>(nama: string, fn: (...a: A) => R) {
  return (...a: A): R => {
    const t0 = performance.now();
    const r = fn(...a);
    console.log(`${nama} selesai dalam ${(performance.now() - t0) < 50 ? "< 50" : "> 50"} ms`);
    return r;
  };
}
const hitungOmzet = ukurWaktu("hitungOmzet", (t: number[]) => t.reduce((a, b) => a + b, 0));
console.log("Omzet:", hitungOmzet([150000, 87500, 230000]).toLocaleString("id-ID"));
'''),
      X('Konfigurasi lint dan build yang umum', r'''
// eslint.config.mjs (flat config)
import tseslint from "typescript-eslint";
export default tseslint.config(
  ...tseslint.configs.strictTypeChecked,
  { languageOptions: { parserOptions: { projectService: true } } },
  { rules: { "@typescript-eslint/no-floating-promises": "error" } },
);

// package.json scripts
"scripts": {
  "dev": "vite",
  "typecheck": "tsc --noEmit",
  "lint": "eslint .",
  "build": "tsc --noEmit && vite build"
}''', lang='ts')]),

'Pustaka keranjang belanja bertipe': dict(
  ist=[('Domain model', 'Tipe yang mencerminkan konsep bisnis: Produk, Item, Kupon, Keranjang.'),
       ('Immutability', 'Operasi mengembalikan keranjang baru, bukan mengubah yang lama; aman untuk React.'),
       ('Branded type', 'Tipe number/string "bermerek" agar Rupiah tidak tertukar dengan jumlah barang.'),
       ('Public API', 'Fungsi yang diekspor dan dijamin stabil bagi pengguna pustaka.')],
  cx=[T('Keranjang immutable dengan kupon dan branded type', r'''
type Rupiah = number & { readonly __brand: "Rupiah" };
const rp = (n: number) => Math.round(n) as Rupiah;
const fmt = (n: Rupiah) => "Rp" + n.toLocaleString("id-ID");

interface Produk { sku: string; nama: string; harga: Rupiah }
interface Item { produk: Produk; qty: number }
type Kupon = { kode: string; jenis: "persen"; nilai: number; maks: Rupiah } | { kode: string; jenis: "potong"; nilai: Rupiah; minBelanja: Rupiah };
interface Keranjang { readonly item: readonly Item[]; readonly kupon?: Kupon }

const kosong: Keranjang = { item: [] };
const tambah = (k: Keranjang, p: Produk, qty = 1): Keranjang => {
  const ada = k.item.find((i) => i.produk.sku === p.sku);
  return { ...k, item: ada ? k.item.map((i) => (i === ada ? { ...i, qty: i.qty + qty } : i)) : [...k.item, { produk: p, qty }] };
};
const pakaiKupon = (k: Keranjang, kupon: Kupon): Keranjang => ({ ...k, kupon });
const subtotal = (k: Keranjang) => rp(k.item.reduce((a, i) => a + i.produk.harga * i.qty, 0));
function diskon(k: Keranjang): Rupiah {
  const s = subtotal(k), c = k.kupon;
  if (!c) return rp(0);
  if (c.jenis === "persen") return rp(Math.min(s * c.nilai / 100, c.maks));
  return s >= c.minBelanja ? c.nilai : rp(0);
}

const kopi: Produk = { sku: "KP-250", nama: "Kopi 250g", harga: rp(45000) };
const teh: Produk = { sku: "TH-100", nama: "Teh hijau", harga: rp(28000) };
let k = tambah(tambah(tambah(kosong, kopi, 2), teh), kopi);
k = pakaiKupon(k, { kode: "HEMAT10", jenis: "persen", nilai: 10, maks: rp(15000) });
for (const i of k.item) console.log(`${i.produk.nama.padEnd(10)} x${i.qty}  ${fmt(rp(i.produk.harga * i.qty))}`);
console.log("Subtotal ", fmt(subtotal(k)));
console.log("Diskon   ", fmt(diskon(k)), `(${k.kupon?.kode})`);
console.log("Total    ", fmt(rp(subtotal(k) - diskon(k))));
console.log("Keranjang awal tetap kosong:", kosong.item.length === 0);
''')]),

'Format specifier: merapikan keluaran': dict(
  ist=[('padStart / padEnd', 'Setara format lebar kolom; meratakan teks ke kanan atau kiri.'),
       ('toFixed', 'Jumlah angka di belakang koma.'),
       ('Intl.NumberFormat', 'Format angka dan mata uang sesuai lokal (id-ID, en-US).'),
       ('Intl.DateTimeFormat', 'Format tanggal lokal tanpa pustaka tambahan.')],
  cx=[T('Struk rapi dengan Intl dan padStart', r'''
const idr = new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 });
const persen = new Intl.NumberFormat("id-ID", { style: "percent", maximumFractionDigits: 1 });
const tgl = new Intl.DateTimeFormat("id-ID", { dateStyle: "long", timeZone: "Asia/Jakarta" });

const item: [string, number, number][] = [["Nasi goreng", 2, 25000], ["Es teh", 3, 5000], ["Kerupuk", 4, 2000]];
const L = 36;
console.log("WARUNG SEDERHANA".padStart((L + 16) / 2));
console.log(tgl.format(new Date(Date.UTC(2026, 10, 19, 5))));
console.log("-".repeat(L));
let total = 0;
for (const [nama, q, h] of item) {
  total += q * h;
  console.log(nama.padEnd(14) + String(q).padStart(3) + idr.format(q * h).padStart(L - 17));
}
console.log("-".repeat(L));
console.log("TOTAL".padEnd(17) + idr.format(total).padStart(L - 17));
console.log("PPN 11%".padEnd(17) + idr.format(total * 0.11).padStart(L - 17));
console.log("Porsi minuman:", persen.format(15000 / total), "| pi =", Math.PI.toFixed(3));
''')]),

'Kapan for, kapan while, kapan do-while': dict(
  ist=[('for', 'Jumlah perulangan sudah diketahui atau mengiterasi koleksi.'),
       ('while', 'Berulang selama kondisi benar, jumlahnya belum diketahui.'),
       ('do...while', 'Badan loop dijalankan minimal sekali, baru kondisi dicek.'),
       ('for...of vs for...in', 'for...of mengambil nilai (array), for...in mengambil kunci (objek).')],
  cx=[T('Tiga bentuk loop untuk tiga kebutuhan', r'''
// for: cicilan 6 bulan sudah pasti
const pokok = 3_000_000, bunga = 0.015;
for (let bulan = 1; bulan <= 6; bulan++) {
  const sisa = pokok * (1 + bunga) ** bulan;
  if (bulan % 2 === 0) console.log(`bulan ${bulan}: utang Rp${Math.round(sisa).toLocaleString("id-ID")}`);
}

// while: berapa tahun tabungan berlipat dua? (jumlah belum diketahui)
let saldo = 10_000_000, tahun = 0;
while (saldo < 20_000_000) { saldo *= 1.06; tahun++; }
console.log(`berlipat dua setelah ${tahun} tahun`);

// do...while: menu tampil minimal sekali
const pilihan = ["2", "1", "0"][Symbol.iterator]();
let p: string;
do {
  p = pilihan.next().value ?? "0";
  console.log("menu -> dipilih", p);
} while (p !== "0");

for (const k in { nama: "Ani", kota: "Solo" }) console.log("kunci:", k);
''')]),

'Bilangan Fibonacci: for dan while': dict(
  ist=[('Deret Fibonacci', 'F(n) = F(n-1) + F(n-2), dengan F(0)=0 dan F(1)=1.'),
       ('Iteratif vs rekursif', 'Versi loop O(n); rekursi naif O(2^n) sangat lambat.'),
       ('BigInt', 'Tipe bilangan bulat tanpa batas; Number aman hanya sampai 2^53 - 1.'),
       ('Generator', 'function* menghasilkan nilai satu per satu (lazy).')],
  cx=[T('Fibonacci dengan for, while, generator, dan BigInt', r'''
function fibFor(n: number): number[] {
  const f = [0, 1];
  for (let i = 2; i < n; i++) f.push(f[i - 1] + f[i - 2]);
  return f.slice(0, n);
}
function fibKurangDari(batas: number): number[] {
  const hasil: number[] = [];
  let [a, b] = [0, 1];
  while (a < batas) { hasil.push(a); [a, b] = [b, a + b]; }
  return hasil;
}
function* fibBig(): Generator<bigint> { let [a, b] = [0n, 1n]; while (true) { yield a; [a, b] = [b, a + b]; } }

console.log("10 pertama :", fibFor(10).join(" "));
console.log("< 100      :", fibKurangDari(100).join(" "));
const g = fibBig(); let f100 = 0n;
for (let i = 0; i <= 100; i++) f100 = g.next().value;
console.log("F(100)     :", f100.toString());
console.log("Number aman?", Number.isSafeInteger(Number(f100)));
''')]),

'Bubble sort: loop di dalam loop': dict(
  ist=[('Nested loop', 'Loop di dalam loop; total langkah sering O(n^2).'),
       ('Swap', 'Menukar dua elemen: [a[i], a[j]] = [a[j], a[i]].'),
       ('Early exit', 'Berhenti jika satu putaran tidak ada pertukaran (data sudah urut).'),
       ('Array.prototype.sort', 'Di produksi pakai sort bawaan (TimSort, O(n log n)) dengan comparator.')],
  cx=[T('Bubble sort generik dengan penghitung langkah', r'''
function bubbleSort<T>(data: readonly T[], banding: (a: T, b: T) => number) {
  const a = [...data];
  let banding_ = 0, tukar = 0;
  for (let i = 0; i < a.length - 1; i++) {
    let adaTukar = false;
    for (let j = 0; j < a.length - 1 - i; j++) {
      banding_++;
      if (banding(a[j], a[j + 1]) > 0) { [a[j], a[j + 1]] = [a[j + 1], a[j]]; tukar++; adaTukar = true; }
    }
    if (!adaTukar) break;
  }
  return { hasil: a, banding: banding_, tukar };
}
const harga = [45000, 12000, 87000, 30000, 5000, 61000];
const r = bubbleSort(harga, (x, y) => x - y);
console.log(r.hasil.join(" "), `| ${r.banding} perbandingan, ${r.tukar} pertukaran`);
const urut = bubbleSort(r.hasil, (x, y) => x - y);
console.log("data sudah urut:", urut.banding, "perbandingan (early exit)");
const nama = bubbleSort(["Sari", "andi", "Budi"], (x, y) => x.localeCompare(y, "id"));
console.log(nama.hasil.join(", "));
''')]),

'FizzBuzz dan bilangan prima: break dan loop bersarang': dict(
  ist=[('Modulo (%)', 'Sisa bagi; dasar cek kelipatan.'),
       ('break / continue', 'Keluar dari loop atau lompat ke iterasi berikutnya.'),
       ('Labeled break', 'break luar; keluar dari loop bersarang sekaligus.'),
       ('Saringan Eratosthenes', 'Algoritma cepat mencari semua prima sampai n.')],
  cx=[T('FizzBuzz, cek prima, dan labeled break', r'''
const fizz = Array.from({ length: 15 }, (_, i) => i + 1)
  .map((n) => (n % 15 === 0 ? "FizzBuzz" : n % 3 === 0 ? "Fizz" : n % 5 === 0 ? "Buzz" : String(n)));
console.log(fizz.join(" "));

function prima(n: number): boolean {
  if (n < 2) return false;
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return false;
  return true;
}
function saringan(n: number): number[] {
  const p = new Array<boolean>(n + 1).fill(true); p[0] = p[1] = false;
  for (let i = 2; i * i <= n; i++) if (p[i]) for (let j = i * i; j <= n; j += i) p[j] = false;
  return p.flatMap((ok, i) => (ok ? [i] : []));
}
console.log("prima < 50:", saringan(50).join(" "));
console.log("97 prima?", prima(97), "| 91 prima?", prima(91));

let pasangan = "";
luar: for (let a = 2; a < 50; a++) {
  for (let b = a; b < 50; b++) {
    if (prima(a) && prima(b) && a + b === 40) { pasangan = `${a} + ${b}`; break luar; }
  }
}
console.log("Goldbach 40 =", pasangan);
''')]),

'Faktorial, jumlah digit, dan palindrom': dict(
  ist=[('Faktorial', 'n! = 1 x 2 x ... x n; tumbuh sangat cepat, perlu BigInt di atas 18!.'),
       ('Digit sum', 'Ambil digit dengan % 10 lalu bagi 10, atau ubah ke string.'),
       ('Palindrom', 'Sama dibaca maju dan mundur setelah dinormalisasi.'),
       ('Two pointers', 'Dua indeks dari ujung kiri dan kanan bergerak ke tengah.')],
  cx=[T('Tiga latihan klasik dalam TypeScript', r'''
const faktorial = (n: bigint): bigint => (n <= 1n ? 1n : n * faktorial(n - 1n));
function jumlahDigit(n: number): number {
  let s = 0;
  for (n = Math.abs(n); n > 0; n = Math.floor(n / 10)) s += n % 10;
  return s;
}
function palindrom(teks: string): boolean {
  const s = teks.toLowerCase().replace(/[^a-z0-9]/g, "");
  for (let i = 0, j = s.length - 1; i < j; i++, j--) if (s[i] !== s[j]) return false;
  return true;
}
for (const n of [5n, 10n, 20n, 25n]) console.log(`${n}! =`, faktorial(n).toString());
console.log("jumlah digit 2026 =", jumlahDigit(2026), "| digit 25! =", [...faktorial(25n).toString()].reduce((a, c) => a + +c, 0));
for (const t of ["Kasur ini rusak", "Malam", "Ruang Kode"]) console.log(`"${t}" palindrom?`, palindrom(t));
''')]),

'Binary search: membagi dua sampai ketemu': dict(
  ist=[('Binary search', 'Mencari di data terurut dengan membuang separuh ruang tiap langkah; O(log n).'),
       ('Invarian', 'Kondisi yang selalu benar selama loop, misalnya target ada di [lo, hi].'),
       ('Lower bound', 'Indeks pertama yang >= target; dipakai untuk menyisipkan data terurut.'),
       ('Off-by-one', 'Kesalahan batas indeks yang paling sering terjadi di binary search.')],
  cx=[T('Binary search dan lower bound dengan pencatat langkah', r'''
function cariBiner(a: readonly number[], target: number): { indeks: number; langkah: number } {
  let lo = 0, hi = a.length - 1, langkah = 0;
  while (lo <= hi) {
    langkah++;
    const mid = lo + ((hi - lo) >> 1);
    if (a[mid] === target) return { indeks: mid, langkah };
    if (a[mid] < target) lo = mid + 1; else hi = mid - 1;
  }
  return { indeks: -1, langkah };
}
function lowerBound(a: readonly number[], x: number): number {
  let lo = 0, hi = a.length;
  while (lo < hi) { const m = (lo + hi) >> 1; if (a[m] < x) lo = m + 1; else hi = m; }
  return lo;
}
const data = Array.from({ length: 1_000_000 }, (_, i) => i * 3);
for (const t of [0, 1_499_997, 2_999_997, 1_000_001]) {
  const r = cariBiner(data, t);
  console.log(`cari ${String(t).padStart(9)} -> indeks ${String(r.indeks).padStart(7)} dalam ${r.langkah} langkah`);
}
const harga = [5000, 12000, 30000, 45000, 87000];
console.log("sisipkan 31000 di indeks", lowerBound(harga, 31000));
console.log("maks langkah untuk 1 juta data:", Math.ceil(Math.log2(1_000_000)));
''')]),
}
