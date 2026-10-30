/* ===================== JALUR TYPESCRIPT =====================
   Mengikuti roadmap.sh/typescript. Contoh kode dengan out sudah dijalankan dengan Node 22
   (--experimental-transform-types). Contoh error tipe ditandai run:false. */
const TS_MODULES=[
{t:'Pengantar TypeScript',lvl:'Pemula',d:'Apa itu TypeScript, bedanya dengan JavaScript, dan cara menjalankannya.',
 nodes:['Introduction to TypeScript','TypeScript vs JavaScript','TS and JS Interoperability','Installation and Configuration','tsconfig.json','Compiler Options','Running TypeScript','tsc','ts-node','TS Playground'],
 lessons:[
  {k:'c',t:'Kenapa TypeScript?',nodes:['Introduction to TypeScript','TypeScript vs JavaScript','TS and JS Interoperability'],lang:'ts',
   b:['<b>TypeScript</b> adalah JavaScript ditambah <b>tipe</b>. Kamu menulis anotasi seperti <code>harga: number</code>, lalu kompiler memeriksa kesalahan <b>sebelum</b> program dijalankan: salah ketik nama properti, lupa menangani null, atau mengirim string ke fungsi yang butuh angka.',
      'Tipe dihapus saat kompilasi, sehingga hasilnya JavaScript biasa yang berjalan di browser atau Node. Semua JavaScript valid juga TypeScript valid, jadi proyek bisa dipindahkan bertahap.',
      'Bonus terbesar sehari-hari: editor tahu bentuk setiap data, sehingga autocomplete dan refactor menjadi akurat.'],
   code:`function totalHarga(harga: number, jumlah: number): number {
  return harga * jumlah;
}

const produk = { nama: "Kopi Gayo", harga: 85000 };
console.log(totalHarga(produk.harga, 2));
// totalHarga("85000", 2);   // error: Argument of type 'string' is not assignable to parameter of type 'number'.`,
   out:`170000`,
   pts:['TypeScript = JavaScript + tipe.','Kesalahan tertangkap sebelum program jalan.','Tipe dihapus saat kompilasi.','Bisa diadopsi bertahap.'],
   q:[['Kapan TypeScript menemukan kesalahan tipe?',['Saat kompilasi, sebelum dijalankan','Hanya saat program crash','Tidak pernah'],0,'Itu keunggulan utamanya.']]},
  {k:'c',t:'Memasang & menjalankan',nodes:['Installation and Configuration','tsconfig.json','Compiler Options','Running TypeScript','tsc','ts-node','TS Playground'],lang:'bash',run:false,
   b:['Pasang TypeScript per proyek: <code>npm install -D typescript</code>, lalu buat <code>tsconfig.json</code> dengan <code>npx tsc --init</code>. Opsi terpenting: <code>"strict": true</code> (aktifkan semua pemeriksaan ketat), <code>target</code> (versi JavaScript keluaran), dan <code>module</code>.',
      '<code>npx tsc</code> memeriksa tipe dan menghasilkan file .js. Untuk menjalankan langsung, pakai <code>tsx</code> atau <code>ts-node</code>, atau Node 22 ke atas yang bisa membuang anotasi tipe sendiri. Untuk mencoba cepat tanpa instalasi, ada TypeScript Playground di situs resmi.'],
   code:`$ npm install -D typescript
$ npx tsc --init
# tsconfig.json (potongan)
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "strict": true,
    "outDir": "dist"
  }
}
$ npx tsc            # periksa tipe + hasilkan dist/*.js
$ npx tsx main.ts    # jalankan langsung
$ node main.ts       # Node 23+ (Node 22 dengan --experimental-strip-types)`,
   pts:['typescript dipasang sebagai devDependency.','Selalu nyalakan "strict": true.','tsc memeriksa dan mengompilasi; tsx/ts-node menjalankan langsung.'],
   q:[['Opsi tsconfig yang menyalakan semua pemeriksaan ketat?',['"strict": true','"check": "all"','"noJS": true'],0,'Sangat disarankan untuk proyek baru.']]}
 ]},
{t:'Tipe dasar',lvl:'Pemula',d:'Primitif, array, tuple, objek, literal, enum, dan tipe khusus any, unknown, never, void.',
 nodes:['TypeScript Types','Boolean Type in TypeScript','Number Type in TypeScript','String','Null Type in TypeScript','undefined','Array','Tuple','Object Types in TypeScript','Literal Types','Enum','any','Unknown Type','Never Type','Void Type','Type Inference'],
 lessons:[
  {k:'c',t:'Primitif, array & tuple',nodes:['Boolean Type in TypeScript','Number Type in TypeScript','String','Null Type in TypeScript','undefined','Array','Tuple','Type Inference'],lang:'ts',
   b:['Tipe primitif: <code>string</code>, <code>number</code>, <code>boolean</code>, <code>null</code>, <code>undefined</code>, <code>bigint</code>, <code>symbol</code>. Seringkali kamu tidak perlu menulis tipe karena TypeScript <b>menebaknya</b> (type inference): <code>let stok = 40</code> sudah bertipe number.',
      'Array ditulis <code>string[]</code> atau <code>Array&lt;string&gt;</code>. <b>Tuple</b> adalah array dengan panjang dan tipe per posisi tetap: <code>[string, number]</code>, cocok untuk pasangan seperti nama dan harga.'],
   code:`let stok = 40;                      // ditebak: number
const nama: string = "Kopi Gayo";
const aktif: boolean = true;
const kategori: string[] = ["Minuman", "Camilan"];
const item: [string, number] = ["Teh Melati", 25000];

const [n, h] = item;
console.log(nama, stok, aktif);
console.log(kategori.length, n, h);
// stok = "banyak";   // error: Type 'string' is not assignable to type 'number'.`,
   out:`Kopi Gayo 40 true
2 Teh Melati 25000`,
   pts:['Biarkan TypeScript menebak tipe jika jelas.','Array: T[] atau Array<T>.','Tuple: panjang dan tipe per posisi tetap.'],
   q:[['Tipe let x = "a" menurut inferensi?',['string','any','unknown'],0,'Nilai awal string.']]},
  {k:'c',t:'Objek, literal & enum',nodes:['Object Types in TypeScript','Literal Types','Enum'],lang:'ts',
   b:['Tipe objek menyebut setiap properti: <code>{ nama: string; harga: number; promo?: boolean }</code>. Tanda <code>?</code> berarti opsional, dan <code>readonly</code> berarti tidak boleh diubah.',
      '<b>Literal type</b> membatasi nilai ke beberapa pilihan: <code>"baru" | "dikirim" | "selesai"</code>. Ini sering lebih disukai daripada <b>enum</b>, yang menghasilkan objek di JavaScript. Enum tetap berguna untuk kumpulan konstanta bernama.'],
   code:`type Status = "baru" | "dikirim" | "selesai";

const pesanan: { id: number; status: Status; catatan?: string } = {
  id: 101,
  status: "dikirim",
};

enum Kurir { JNE = "jne", JNT = "jnt", SiCepat = "sicepat" }

console.log(pesanan.id, pesanan.status, pesanan.catatan ?? "tanpa catatan");
console.log(Kurir.SiCepat, Object.keys(Kurir).length);
// pesanan.status = "hilang";  // error: Type '"hilang"' is not assignable to type 'Status'.`,
   out:`101 dikirim tanpa catatan
sicepat 3`,
   pts:['? untuk properti opsional, readonly untuk tidak bisa diubah.','Literal union membatasi nilai yang sah.','Enum membuat objek di JavaScript; literal union tidak.'],
   q:[['Tipe "a" | "b" disebut?',['Union literal type','Enum','Tuple'],0,'Gabungan beberapa nilai literal.']]},
  {k:'c',t:'any, unknown, never & void',nodes:['any','Unknown Type','Never Type','Void Type'],lang:'ts',
   b:['<code>any</code> mematikan pemeriksaan tipe; hindari karena menghilangkan manfaat TypeScript. <code>unknown</code> adalah versi aman: nilainya bisa apa saja, tapi kamu wajib memeriksa tipenya sebelum memakai.',
      '<code>void</code> untuk fungsi yang tidak mengembalikan nilai. <code>never</code> untuk nilai yang mustahil terjadi, misalnya fungsi yang selalu melempar error, atau cabang yang seharusnya tidak pernah tercapai.'],
   code:`function cetak(pesan: string): void {
  console.log("LOG:", pesan);
}

function gagal(pesan: string): never {
  throw new Error(pesan);
}

function panjang(x: unknown): number {
  if (typeof x === "string") return x.length;     // aman setelah diperiksa
  if (Array.isArray(x)) return x.length;
  return 0;
}

cetak("mulai");
console.log(panjang("halo"), panjang([1, 2, 3]), panjang(42));
try { gagal("stok habis"); } catch (e) { console.log((e as Error).message); }`,
   out:`LOG: mulai
4 3 0
stok habis`,
   pts:['Hindari any.','unknown wajib diperiksa sebelum dipakai.','void: tidak mengembalikan nilai.','never: tidak mungkin terjadi.'],
   q:[['Data JSON dari luar sebaiknya diberi tipe awal?',['unknown','any','never'],0,'Paksa pemeriksaan sebelum dipakai.']]}
 ]},
{t:'Fungsi',lvl:'Pemula',d:'Memberi tipe pada parameter, nilai kembali, callback, dan overload.',nodes:['TypeScript Functions','Typing Functions','Function Overloading'],
 lessons:[
  {k:'c',t:'Menulis tipe fungsi',nodes:['TypeScript Functions','Typing Functions'],lang:'ts',
   b:['Tulis tipe setiap parameter; tipe kembalian biasanya bisa ditebak, tapi menuliskannya membuat maksudmu jelas. Parameter opsional memakai <code>?</code>, parameter bawaan memakai <code>=</code>, dan rest parameter memakai <code>...nama: T[]</code>.',
      'Tipe fungsi juga bisa dijadikan alias: <code>type Diskon = (harga: number) =&gt; number</code>, berguna untuk callback.'],
   code:`type Diskon = (harga: number) => number;

const potong10: Diskon = h => h * 0.9;
const potong20: Diskon = h => h * 0.8;

function bayar(harga: number, diskon?: Diskon, ongkir = 15000): number {
  const setelah = diskon ? diskon(harga) : harga;
  return setelah + ongkir;
}

function jumlahkan(...angka: number[]): number {
  return angka.reduce((a, b) => a + b, 0);
}

console.log(bayar(100000));
console.log(bayar(100000, potong20, 0));
console.log(jumlahkan(85000, 25000, 15000));`,
   out:`115000
80000
125000`,
   pts:['Selalu beri tipe parameter.','? opsional, = nilai bawaan, ... rest.','Alias tipe fungsi untuk callback.'],
   q:[['Tipe untuk "fungsi menerima number, mengembalikan number"?',['(n: number) => number','function<number>','number => number tanpa nama'],0,'Parameter harus diberi nama di tipe fungsi.']]},
  {k:'c',t:'Overload fungsi',nodes:['Function Overloading'],lang:'ts',
   b:['<b>Overload</b> menulis beberapa tanda tangan untuk satu fungsi, sehingga tipe kembalian bisa berbeda tergantung argumennya. Tulis tanda tangan overload dulu, lalu satu implementasi yang menangani semuanya.',
      'Sering kali union type atau generics sudah cukup; pakai overload jika hubungan input-output tidak bisa diungkapkan dengan cara lain.'],
   code:`function format(nilai: number): string;
function format(nilai: Date): string;
function format(nilai: number | Date): string {
  if (typeof nilai === "number") return "Rp" + nilai.toLocaleString("id-ID");
  return nilai.toISOString().slice(0, 10);
}

console.log(format(85000));
console.log(format(new Date("2024-10-01T00:00:00Z")));`,
   out:`Rp85.000
2024-10-01`,
   pts:['Beberapa tanda tangan, satu implementasi.','Implementasi tidak terlihat dari luar.','Utamakan union atau generics jika cukup.'],
   q:[['Berapa implementasi untuk sekelompok overload?',['Satu','Sebanyak tanda tangan','Nol'],0,'Satu badan fungsi menangani semua kasus.']]}
 ]},
{t:'Interface & type alias',lvl:'Menengah',d:'Mendefinisikan bentuk data, mewarisi, dan menggabungkan tipe.',nodes:['TypeScript Interfaces','Interface Declaration','Interface','Extending Interfaces','Hybrid Types','Type Aliases','Types vs Interfaces','Combining Types','Union Types','Intersection Types','Type Compatibility'],
 lessons:[
  {k:'c',t:'Interface & extends',nodes:['TypeScript Interfaces','Interface Declaration','Interface','Extending Interfaces','Hybrid Types'],lang:'ts',
   b:['<b>Interface</b> mendefinisikan bentuk objek. Ia bisa <code>extends</code> interface lain untuk menambah properti, dan bisa berisi method.',
      'TypeScript memakai <b>structural typing</b>: objek cocok dengan interface jika bentuknya cocok, tanpa perlu menyatakan "implements". Ini berbeda dengan Java.'],
   code:`interface Produk {
  id: number;
  nama: string;
  harga: number;
}

interface ProdukDigital extends Produk {
  urlUnduh: string;
  hitungDiskon(persen: number): number;
}

const ebook: ProdukDigital = {
  id: 9, nama: "E-book Resep Kopi", harga: 49000, urlUnduh: "https://contoh.id/resep.pdf",
  hitungDiskon(p) { return this.harga * (1 - p / 100); },
};

function label(p: Produk): string {        // ProdukDigital juga diterima
  return \`#\${p.id} \${p.nama}\`;
}
console.log(label(ebook), ebook.hitungDiskon(10));`,
   out:`#9 E-book Resep Kopi 44100`,
   pts:['interface untuk bentuk objek.','extends menambah properti.','Structural typing: cocok jika bentuknya cocok.'],
   q:[['Bolehkah objek ProdukDigital dikirim ke fungsi yang meminta Produk?',['Boleh, karena punya semua properti Produk','Tidak boleh','Hanya dengan as any'],0,'Structural typing.']]},
  {k:'c',t:'Type alias, union & intersection',nodes:['Type Aliases','Types vs Interfaces','Combining Types','Union Types','Intersection Types','Type Compatibility'],lang:'ts',
   b:['<code>type</code> memberi nama untuk tipe apa saja: objek, union, tuple, atau fungsi. <b>Union</b> <code>A | B</code> berarti "salah satu", <b>intersection</b> <code>A &amp; B</code> berarti "keduanya sekaligus".',
      'Kapan interface dan kapan type? Keduanya hampir setara untuk objek. Pakai interface untuk bentuk objek yang bisa diperluas, dan type untuk union, tuple, atau tipe turunan.'],
   code:`type Id = number | string;
type Bertanggal = { dibuat: string };
type Pelanggan = { id: Id; nama: string } & Bertanggal;

const a: Pelanggan = { id: 1, nama: "Andi", dibuat: "2023-01-15" };
const b: Pelanggan = { id: "PLG-008", nama: "Hadi", dibuat: "2024-09-03" };

function tampil(id: Id): string {
  return typeof id === "number" ? id.toString().padStart(4, "0") : id;
}
console.log(tampil(a.id), tampil(b.id), b.dibuat);`,
   out:`0001 PLG-008 2024-09-03`,
   pts:['type untuk nama tipe apa pun.','| = salah satu, & = gabungan.','interface untuk objek yang diperluas, type untuk union/turunan.'],
   q:[['Tipe { a: 1 } & { b: 2 } berisi?',['Properti a dan b','Hanya a','Salah satu'],0,'Intersection menggabungkan.']]}
 ]},
{t:'Narrowing & assertion',lvl:'Menengah',d:'Mempersempit tipe dengan pemeriksaan, type predicate, dan discriminated union.',nodes:['Type Guards / Narrowing','typeof Type Guards','instanceof Operator','Equality in Type Guards and Narrowing','Truthiness','Type Predicates','Type Assertions with as','as const','as any','Non-null Assertion','Satisfies Keyword'],
 lessons:[
  {k:'c',t:'Type guard & discriminated union',nodes:['Type Guards / Narrowing','typeof Type Guards','instanceof Operator','Equality in Type Guards and Narrowing','Truthiness','Type Predicates'],lang:'ts',
   b:['<b>Narrowing</b>: setelah pemeriksaan <code>typeof</code>, <code>instanceof</code>, <code>in</code>, atau perbandingan, TypeScript tahu tipe yang lebih sempit di dalam cabang itu.',
      '<b>Discriminated union</b> adalah pola paling berguna: setiap varian punya properti penanda yang sama (misalnya <code>jenis</code>), dan <code>switch</code> pada penanda itu membuat setiap cabang aman. Tambahkan pemeriksaan <code>never</code> agar TypeScript protes jika ada varian baru yang lupa ditangani.',
      '<b>Type predicate</b> <code>x is T</code> membuat fungsi pemeriksa milikmu sendiri.'],
   code:`type Bayar =
  | { jenis: "qris"; merchant: string }
  | { jenis: "va"; bank: string; nomor: string }
  | { jenis: "cod" };

function keterangan(b: Bayar): string {
  switch (b.jenis) {
    case "qris": return "QRIS " + b.merchant;
    case "va": return \`VA \${b.bank} \${b.nomor}\`;
    case "cod": return "Bayar di tempat";
    default: { const cek: never = b; return cek; }
  }
}

const adalahVA = (b: Bayar): b is Extract<Bayar, { jenis: "va" }> => b.jenis === "va";

const daftar: Bayar[] = [{ jenis: "qris", merchant: "Toko Nusantara" }, { jenis: "va", bank: "BCA", nomor: "8808" }, { jenis: "cod" }];
daftar.forEach(b => console.log(keterangan(b)));
console.log(daftar.filter(adalahVA).map(b => b.bank));`,
   out:`QRIS Toko Nusantara
VA BCA 8808
Bayar di tempat
[ 'BCA' ]`,
   pts:['typeof, instanceof, in, dan === mempersempit tipe.','Discriminated union: properti penanda + switch.','Cek never memastikan semua varian ditangani.','Type predicate: fungsi pemeriksa sendiri.'],
   q:[['Gunanya const cek: never = b di default?',['TypeScript error jika ada varian yang belum ditangani','Mempercepat kode','Menghapus varian'],0,'Pemeriksaan kelengkapan (exhaustiveness).']]},
  {k:'c',t:'as, as const, ! & satisfies',nodes:['Type Assertions with as','as const','as any','Non-null Assertion','Satisfies Keyword'],lang:'ts',
   b:['<code>as</code> memberi tahu kompiler "percayalah, tipenya ini". Ia tidak memeriksa apa pun saat berjalan, jadi pakai seperlunya. <code>!</code> (non-null assertion) menyatakan nilai pasti tidak null; salah pakai berarti error saat program jalan.',
      '<code>as const</code> membuat nilai literal dan readonly, berguna untuk daftar konstanta. <code>satisfies</code> memeriksa bahwa nilai cocok dengan tipe tertentu <b>tanpa</b> kehilangan tipe yang lebih spesifik.'],
   code:`const KATEGORI = ["Minuman", "Camilan", "Bumbu"] as const;
type Kategori = typeof KATEGORI[number];          // "Minuman" | "Camilan" | "Bumbu"

const warna = {
  Minuman: "#2E5E8C",
  Camilan: "#B4532A",
  Bumbu: "#2F7A52",
} satisfies Record<Kategori, string>;

const k: Kategori = "Camilan";
console.log(k, warna[k], KATEGORI.length);
const data = JSON.parse('{"nama":"Kopi"}') as { nama: string };
console.log(data.nama.toUpperCase());`,
   out:`Camilan #B4532A 3
KOPI`,
   pts:['as tidak memeriksa saat berjalan.','! pada nilai yang ternyata null menyebabkan crash.','as const: literal + readonly.','satisfies: cek tipe tanpa melebarkan.'],
   q:[['Bedanya satisfies dengan anotasi tipe biasa?',['Tipe nilai yang spesifik tetap dipertahankan','Tidak ada beda','satisfies mematikan pemeriksaan'],0,'Nilai diperiksa, tapi tipenya tidak dilebarkan.']]}
 ]},
{t:'Kelas',lvl:'Menengah',d:'Kelas dengan modifier akses, parameter konstruktor, kelas abstrak, dan polimorfisme.',nodes:['Classes','Class','Access Modifiers','Constructor Parameters','Constructor Overloading','Abstract Classes','Inheritance vs. Polymorphism','Method Overriding'],
 lessons:[
  {k:'c',t:'Kelas & modifier akses',nodes:['Classes','Class','Access Modifiers','Constructor Parameters','Constructor Overloading'],lang:'ts',
   b:['Kelas TypeScript menambahkan <b>modifier akses</b>: <code>public</code> (bawaan), <code>private</code> (hanya di kelas itu), <code>protected</code> (kelas itu dan turunannya), serta <code>readonly</code>.',
      '<b>Parameter properties</b> menyingkat konstruktor: menulis <code>constructor(private saldo: number)</code> otomatis membuat dan mengisi properti saldo. Untuk privasi sungguhan saat berjalan, JavaScript punya <code>#field</code>.'],
   code:`class Rekening {
  #riwayat: string[] = [];
  constructor(public readonly pemilik: string, private saldo: number) {}

  setor(n: number): void {
    this.saldo += n;
    this.#riwayat.push("setor " + n);
  }
  tarik(n: number): boolean {
    if (n > this.saldo) return false;
    this.saldo -= n;
    this.#riwayat.push("tarik " + n);
    return true;
  }
  get info(): string { return \`\${this.pemilik}: \${this.saldo} (\${this.#riwayat.length} transaksi)\`; }
}

const r = new Rekening("Andi", 500000);
r.setor(100000);
console.log(r.tarik(900000), r.tarik(200000));
console.log(r.info);
// r.saldo = 0;   // error: Property 'saldo' is private and only accessible within class 'Rekening'.`,
   out:`false true
Andi: 400000 (2 transaksi)`,
   pts:['public, private, protected, readonly.','Parameter properties meringkas konstruktor.','private hanya saat kompilasi; #field privat saat berjalan.'],
   q:[['constructor(private saldo: number) melakukan apa?',['Membuat dan mengisi properti privat saldo','Hanya parameter biasa','Error sintaks'],0,'Itu parameter property.']]},
  {k:'c',t:'Kelas abstrak & polimorfisme',nodes:['Abstract Classes','Inheritance vs. Polymorphism','Method Overriding'],lang:'ts',
   b:['<b>Kelas abstrak</b> tidak bisa dibuat objeknya langsung; ia menjadi kerangka bersama dengan method <code>abstract</code> yang wajib diisi kelas turunan.',
      '<b>Polimorfisme</b>: kode yang bekerja dengan tipe induk otomatis memanggil versi method milik objek sebenarnya. Kata kunci <code>override</code> menegaskan bahwa method menimpa milik induk; aktifkan opsi <code>noImplicitOverride</code> agar wajib ditulis.'],
   code:`abstract class Pengiriman {
  constructor(protected beratKg: number) {}
  abstract tarifPerKg(): number;
  biaya(): number { return Math.max(1, Math.ceil(this.beratKg)) * this.tarifPerKg(); }
}

class Reguler extends Pengiriman { tarifPerKg() { return 10000; } }
class Kilat extends Pengiriman {
  tarifPerKg() { return 18000; }
  override biaya(): number { return super.biaya() + 5000; }   // tambah biaya asuransi
}

const kiriman: Pengiriman[] = [new Reguler(1.2), new Kilat(1.2), new Reguler(0.3)];
kiriman.forEach(k => console.log(k.constructor.name, k.biaya()));`,
   out:`Reguler 20000
Kilat 41000
Reguler 10000`,
   pts:['abstract class: kerangka, tidak bisa di-new.','abstract method wajib diimplementasikan.','override menimpa method induk.','Polimorfisme lewat tipe induk.'],
   q:[['new Pengiriman(1) menghasilkan?',['Error: tidak bisa membuat instance kelas abstrak','Objek Pengiriman','null'],0,'Kelas abstrak hanya untuk diwarisi.']]}
 ]},
{t:'Generics',lvl:'Lanjutan',d:'Fungsi dan tipe yang bekerja untuk banyak tipe sekaligus, dengan batasan.',nodes:['Generics','Generic Types','Generic Constraints'],
 lessons:[
  {k:'c',t:'Fungsi & tipe generik',nodes:['Generics','Generic Types','Generic Constraints'],lang:'ts',
   b:['<b>Generics</b> adalah parameter tipe. <code>function pertama&lt;T&gt;(arr: T[]): T | undefined</code> bekerja untuk array apa pun dan tetap tahu tipe elemennya. Tanpa generics kamu terpaksa memakai any dan kehilangan informasi tipe.',
      '<b>Constraint</b> <code>&lt;T extends { id: number }&gt;</code> membatasi T agar setidaknya punya properti tertentu. Tipe juga bisa generik, misalnya <code>type Hasil&lt;T&gt; = { ok: true; data: T } | { ok: false; error: string }</code>.'],
   code:`function pertama<T>(arr: T[]): T | undefined {
  return arr[0];
}

function cariById<T extends { id: number }>(daftar: T[], id: number): T | undefined {
  return daftar.find(x => x.id === id);
}

type Hasil<T> = { ok: true; data: T } | { ok: false; error: string };

function bagi(a: number, b: number): Hasil<number> {
  return b === 0 ? { ok: false, error: "pembagi nol" } : { ok: true, data: a / b };
}

const produk = [{ id: 1, nama: "Kopi" }, { id: 2, nama: "Teh" }];
console.log(pertama(["a", "b"]), pertama([10, 20]));
console.log(cariById(produk, 2)?.nama);
const h = bagi(10, 0);
console.log(h.ok ? h.data : h.error);`,
   out:`a 10
Teh
pembagi nol`,
   pts:['Generics = parameter tipe.','Tipe elemen tetap diketahui, tanpa any.','extends membatasi T.','Tipe generik seperti Hasil<T>.'],
   q:[['Apa arti <T extends { id: number }>?',['T harus punya properti id bertipe number','T adalah number','T mewarisi kelas id'],0,'Itu generic constraint.']]}
 ]},
{t:'Utility types',lvl:'Lanjutan',d:'Tipe bawaan untuk mengubah tipe lain: Partial, Pick, Omit, Record, dan kawan-kawan.',nodes:['Utility Types','Partial Type','Pick','Omit','Readonly','Record Utility Type','Exclude','Extract','NonNullable Utility Type','ReturnType','Parameters Utility Type','InstanceType','Awaited'],
 lessons:[
  {k:'c',t:'Partial, Pick, Omit, Readonly & Record',nodes:['Utility Types','Partial Type','Pick','Omit','Readonly','Record Utility Type'],lang:'ts',
   b:['Utility types membuat tipe baru dari tipe lama. <code>Partial&lt;T&gt;</code> membuat semua properti opsional (cocok untuk data update), <code>Pick&lt;T, K&gt;</code> mengambil sebagian properti, <code>Omit&lt;T, K&gt;</code> membuang sebagian, <code>Readonly&lt;T&gt;</code> membuat tidak bisa diubah, dan <code>Record&lt;K, V&gt;</code> membuat objek berkunci K bernilai V.'],
   code:`interface Produk { id: number; nama: string; harga: number; stok: number }

type UbahProduk = Partial<Omit<Produk, "id">>;
type Ringkas = Pick<Produk, "nama" | "harga">;
type StokPerKota = Record<"Jakarta" | "Bandung", number>;

function ubah(p: Produk, perubahan: UbahProduk): Produk {
  return { ...p, ...perubahan };
}

const kopi: Readonly<Produk> = { id: 1, nama: "Kopi Gayo", harga: 85000, stok: 40 };
const baru = ubah(kopi, { harga: 80000 });
const r: Ringkas = { nama: baru.nama, harga: baru.harga };
const stok: StokPerKota = { Jakarta: 25, Bandung: 15 };
console.log(r, stok.Bandung);
// kopi.harga = 1;   // error: Cannot assign to 'harga' because it is a read-only property.`,
   out:`{ nama: 'Kopi Gayo', harga: 80000 } 15`,
   pts:['Partial: semua opsional.','Pick/Omit: ambil/buang properti.','Readonly: tidak bisa diubah.','Record: peta kunci ke nilai.'],
   q:[['Tipe untuk data update yang semua kolomnya opsional?',['Partial<T>','Required<T>','Pick<T>'],0,'Partial membuat semua properti opsional.']]},
  {k:'c',t:'Exclude, Extract, ReturnType & lainnya',nodes:['Exclude','Extract','NonNullable Utility Type','ReturnType','Parameters Utility Type','InstanceType','Awaited'],lang:'ts',
   b:['Untuk union: <code>Exclude&lt;U, X&gt;</code> membuang anggota, <code>Extract&lt;U, X&gt;</code> mengambil anggota yang cocok, <code>NonNullable&lt;T&gt;</code> membuang null dan undefined.',
      'Untuk fungsi dan kelas: <code>ReturnType</code>, <code>Parameters</code>, <code>InstanceType</code>, dan <code>Awaited</code> (isi dari Promise). Ini berguna saat memakai fungsi pustaka yang tipenya tidak diekspor.'],
   code:`type Status = "baru" | "dikirim" | "selesai" | "batal";
type Aktif = Exclude<Status, "selesai" | "batal">;          // "baru" | "dikirim"
type Final = Extract<Status, "selesai" | "batal" | "x">;   // "selesai" | "batal"

async function ambilPesanan(id: number) {
  return { id, status: "dikirim" as Status, total: 135000 };
}
type Pesanan = Awaited<ReturnType<typeof ambilPesanan>>;
type Arg = Parameters<typeof ambilPesanan>;                 // [id: number]

const a: Aktif = "dikirim";
const f: Final = "batal";
const args: Arg = [101];
ambilPesanan(...args).then((p: Pesanan) => console.log(a, f, p.total));`,
   out:`dikirim batal 135000`,
   pts:['Exclude/Extract untuk anggota union.','NonNullable membuang null/undefined.','ReturnType, Parameters, InstanceType, Awaited untuk fungsi dan kelas.'],
   q:[['Tipe isi dari Promise<string>?',['Awaited<Promise<string>> = string','ReturnType','Extract'],0,'Awaited membuka Promise.']]}
 ]},
{t:'Tipe lanjutan',lvl:'Profesional',d:'keyof, typeof, mapped, conditional, template literal, dan tipe rekursif.',nodes:['Advanced Types','keyof Operator','Mapped Types','Conditional Types','Template Literal Types','Recursive Types'],
 lessons:[
  {k:'c',t:'keyof, mapped & conditional types',nodes:['Advanced Types','keyof Operator','Mapped Types','Conditional Types'],lang:'ts',
   b:['<code>keyof T</code> menghasilkan union nama properti T. Gabungkan dengan <code>T[K]</code> untuk fungsi seperti <code>ambil(obj, "nama")</code> yang tahu tipe hasilnya.',
      '<b>Mapped type</b> mengubah setiap properti: <code>{ [K in keyof T]: ... }</code>. Begitulah Partial dan Readonly dibuat. <b>Conditional type</b> <code>T extends U ? X : Y</code> memilih tipe berdasarkan syarat, dan <code>infer</code> menangkap bagian tipe.'],
   code:`function ambil<T, K extends keyof T>(obj: T, kunci: K): T[K] {
  return obj[kunci];
}

type Opsional<T> = { [K in keyof T]?: T[K] };
type JadiString<T> = { [K in keyof T]: string };
type IsiArray<T> = T extends (infer E)[] ? E : never;

const p = { nama: "Kopi Gayo", harga: 85000 };
const h = ambil(p, "harga");                 // number
const form: JadiString<typeof p> = { nama: "Kopi Gayo", harga: "85000" };
const draf: Opsional<typeof p> = { nama: "Draf" };
type X = IsiArray<string[]>;                 // string
const x: X = "ok";
console.log(h + 1, form.harga + "!", draf.harga ?? "-", x);`,
   out:`85001 85000! - ok`,
   pts:['keyof T = union nama properti.','T[K] = tipe properti K.','Mapped type: [K in keyof T].','Conditional + infer untuk memilih dan menangkap tipe.'],
   q:[['keyof { a: 1; b: 2 } adalah?',['"a" | "b"','1 | 2','string'],0,'Union nama properti.']]},
  {k:'c',t:'Template literal & tipe rekursif',nodes:['Template Literal Types','Recursive Types'],lang:'ts',
   b:['<b>Template literal type</b> menyusun string pada level tipe: <code>`on${Capitalize&lt;E&gt;}`</code> mengubah "klik" menjadi "onKlik". Berguna untuk nama event, rute, atau kunci CSS.',
      '<b>Tipe rekursif</b> merujuk dirinya sendiri, misalnya struktur pohon kategori atau JSON.'],
   code:`type Peristiwa = "klik" | "ubah";
type Handler = \`on\${Capitalize<Peristiwa>}\`;      // "onKlik" | "onUbah"

type Kategori = { nama: string; anak?: Kategori[] };
const pohon: Kategori = { nama: "Minuman", anak: [{ nama: "Kopi", anak: [{ nama: "Arabika" }] }, { nama: "Teh" }] };

function hitung(k: Kategori): number {
  return 1 + (k.anak ?? []).reduce((n, a) => n + hitung(a), 0);
}

const h: Handler = "onKlik";
console.log(h, hitung(pohon));`,
   out:`onKlik 4`,
   pts:['Template literal type menyusun string tipe.','Capitalize, Uppercase, Lowercase adalah helper bawaan.','Tipe rekursif untuk pohon dan JSON.'],
   q:[['Hasil `get${Capitalize<"nama">}`?',['"getNama"','"getnama"','string'],0,'Capitalize membuat huruf pertama kapital.']]}
 ]},
{t:'Modul & ekosistem',lvl:'Profesional',d:'Modul, namespace, deklarasi ambient, decorator, dan alat di sekitar TypeScript.',nodes:['TypeScript Modules','External Modules in TypeScript','Namespaces','Ambient Modules','Global Augmentation','Namespace Augmentation','Decorators','TypeScript Ecosystem','Formatting','Linting','Build Tools','Useful Packages'],
 lessons:[
  {k:'c',t:'Modul, deklarasi & augmentasi',nodes:['TypeScript Modules','External Modules in TypeScript','Namespaces','Ambient Modules','Global Augmentation','Namespace Augmentation'],lang:'ts',run:false,
   b:['TypeScript modern memakai modul ES (<code>import</code>/<code>export</code>). <code>import type</code> mengimpor tipe saja sehingga hilang sepenuhnya dari hasil JavaScript. Namespace adalah cara lama, kini jarang dipakai.',
      'Pustaka JavaScript tanpa tipe dijelaskan dengan file deklarasi <code>.d.ts</code>, yang banyak tersedia di paket <code>@types/...</code>. Kamu juga bisa menulis <b>ambient module</b> sendiri atau menambah properti ke tipe global (<b>augmentation</b>), misalnya menambah <code>window.dataLayer</code>.'],
   code:`// tipe.ts
export type Produk = { id: number; nama: string };

// layanan.ts
import type { Produk } from "./tipe";          // hilang saat dikompilasi

// global.d.ts — menambah properti ke window
declare global {
  interface Window { dataLayer: unknown[] }
}
export {};

// modul-tanpa-tipe.d.ts
declare module "kalkulator-ongkir" {
  export function hitung(beratKg: number, kota: string): number;
}`,
   pts:['Pakai modul ES; namespace sudah jarang.','import type untuk tipe saja.','.d.ts dan @types untuk pustaka JavaScript.','declare global untuk augmentasi.'],
   q:[['Paket tipe untuk pustaka lodash biasanya bernama?',['@types/lodash','lodash-ts','ts-lodash'],0,'Proyek DefinitelyTyped.']]},
  {k:'c',t:'Decorator & alat ekosistem',nodes:['Decorators','TypeScript Ecosystem','Formatting','Linting','Build Tools','Useful Packages'],lang:'ts',
   b:['<b>Decorator</b> adalah fungsi yang membungkus kelas atau method untuk menambah perilaku, misalnya mencatat log atau mengukur waktu. Framework seperti Angular dan NestJS memakainya secara luas.',
      'Ekosistem sehari-hari: <b>typescript-eslint</b> untuk linting, <b>Prettier</b> atau Biome untuk format, <b>tsx</b> untuk menjalankan, <b>tsup</b>/<b>Vite</b> untuk build, dan <b>Zod</b> untuk validasi data saat berjalan yang sekaligus menghasilkan tipe.'],
   code:`function catat(asli: any, konteks: ClassMethodDecoratorContext) {
  return function (this: unknown, ...args: unknown[]) {
    console.log(\`panggil \${String(konteks.name)}(\${args.join(", ")})\`);
    return asli.apply(this, args);
  };
}

class Kasir {
  @catat
  bayar(total: number, uang: number) { return uang - total; }
}

console.log("kembalian", new Kasir().bayar(85000, 100000));`,
   out:`panggil bayar(85000, 100000)
kembalian 15000`,
   pts:['Decorator membungkus kelas/method.','typescript-eslint, Prettier, tsx, tsup, Zod.','Zod memvalidasi saat berjalan dan menghasilkan tipe.'],
   q:[['Decorator ditulis dengan simbol?',['@','#','$'],0,'Contoh: @catat.']]}
 ]},
{t:'Proyek akhir TypeScript',lvl:'Profesional',d:'Bangun pustaka kecil yang sepenuhnya bertipe dan teruji.',nodes:[],
 lessons:[
  {k:'proj',t:'Pustaka keranjang belanja bertipe',stack:'TypeScript + Node',
   brief:'Tulis modul keranjang belanja yang aman tipe: produk, item, diskon, dan ringkasan pembayaran. Jalankan dengan Node dan uji dengan Vitest.',
   feats:['tsconfig dengan "strict": true dan tanpa any','Tipe Produk, Item, dan Diskon berbentuk discriminated union (persen, potongan tetap, gratis ongkir)','Kelas Keranjang dengan field privat dan method tambah, kurangi, hapus','Fungsi ringkasan mengembalikan Hasil<T> (ok/error) alih-alih melempar error','Validasi input dari JSON dengan unknown + type guard (atau Zod)','Pemeriksaan exhaustiveness dengan never','Minimal 5 tes Vitest'],
   steps:['Definisikan semua tipe dulu.','Tulis kelas dan fungsi; biarkan kompiler menuntunmu.','Tambahkan validasi untuk data dari luar.','Tulis tes dan jalankan npx tsc --noEmit.'],
   files:[['keranjang.ts','ts',`type Produk = { id: number; nama: string; harga: number };
type Diskon = { jenis: "persen"; nilai: number } | { jenis: "potong"; nilai: number } | { jenis: "ongkir" };
type Hasil<T> = { ok: true; data: T } | { ok: false; error: string };

export class Keranjang {
  #isi = new Map<number, { produk: Produk; jumlah: number }>();
  tambah(p: Produk, n = 1): void {
    const lama = this.#isi.get(p.id);
    this.#isi.set(p.id, { produk: p, jumlah: (lama?.jumlah ?? 0) + n });
  }
  ringkasan(d?: Diskon, ongkir = 15000): Hasil<{ subtotal: number; potongan: number; total: number }> {
    if (this.#isi.size === 0) return { ok: false, error: "Keranjang kosong" };
    const subtotal = [...this.#isi.values()].reduce((t, i) => t + i.produk.harga * i.jumlah, 0);
    let potongan = 0;
    if (d) {
      switch (d.jenis) {
        case "persen": potongan = Math.round(subtotal * d.nilai / 100); break;
        case "potong": potongan = Math.min(d.nilai, subtotal); break;
        case "ongkir": potongan = ongkir; break;
        default: { const cek: never = d; return cek; }
      }
    }
    return { ok: true, data: { subtotal, potongan, total: subtotal + ongkir - potongan } };
  }
}

const k = new Keranjang();
k.tambah({ id: 1, nama: "Kopi Gayo", harga: 85000 }, 2);
console.log(k.ringkasan({ jenis: "persen", nilai: 10 }));`]],
   out:`{ ok: true, data: { subtotal: 170000, potongan: 17000, total: 168000 } }`}
 ]}
];
