"""Pendalaman jalur Next.js: istilah dunia kerja, kode App Router siap pakai, dan logika yang dijalankan dengan Node."""
K = 'nextjs'


def R(t, code, b=None, lang='tsx'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def T(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='ts')


D = {
'Kenapa Next.js': dict(
  ist=[('Meta-framework', 'Framework di atas React yang menyediakan routing, rendering server, dan build.'),
       ('SSR / SSG / ISR', 'Render per request, saat build, atau statis yang diperbarui berkala.'),
       ('SEO', 'HTML sudah berisi konten saat dikirim, sehingga mudah dibaca mesin pencari.'),
       ('Turbopack', 'Bundler berbasis Rust yang menjadi default dev dan build di Next.js 15/16.'),
       ('Full-stack React', 'UI dan endpoint server dalam satu proyek.')],
  cx=[T('Membandingkan strategi rendering', r'''
type Strategi = { nama: string; kapanHtmlDibuat: string; ttfbMs: number; dataSegar: string; contoh: string };
const s: Strategi[] = [
  { nama: "CSR (SPA)", kapanHtmlDibuat: "di browser", ttfbMs: 50, dataSegar: "ya", contoh: "dasbor admin internal" },
  { nama: "SSR", kapanHtmlDibuat: "tiap request", ttfbMs: 300, dataSegar: "ya", contoh: "halaman akun, hasil pencarian" },
  { nama: "SSG", kapanHtmlDibuat: "saat build", ttfbMs: 30, dataSegar: "sampai build ulang", contoh: "blog, dokumentasi" },
  { nama: "ISR", kapanHtmlDibuat: "build + berkala", ttfbMs: 30, dataSegar: "maks N detik", contoh: "katalog produk" },
];
console.log("Strategi".padEnd(10), "HTML dibuat".padEnd(16), "TTFB".padStart(6), " Data segar".padEnd(20), "Cocok untuk");
for (const x of s) console.log(x.nama.padEnd(10), x.kapanHtmlDibuat.padEnd(16), (x.ttfbMs + "ms").padStart(6), " " + x.dataSegar.padEnd(19), x.contoh);
''', 'Angka TTFB hanya ilustrasi. Di Next.js, satu aplikasi bisa mencampur semua strategi per halaman.'),
      R('Membuat proyek', r'''
npx create-next-app@latest toko --ts --tailwind --eslint --app --src-dir
cd toko && npm run dev          # http://localhost:3000

src/app/
├── layout.tsx      # kerangka HTML semua halaman
├── page.tsx        # halaman "/"
└── globals.css''', lang='bash')]),

'App Router: page, layout, dan link': dict(
  ist=[('File-based routing', 'Folder di app/ menjadi segmen URL; page.tsx membuatnya dapat diakses.'),
       ('layout.tsx', 'UI bersama yang tetap ada saat berpindah halaman (tidak render ulang).'),
       ('<Link>', 'Navigasi sisi klien dengan prefetch otomatis.'),
       ('Route group (folder)', 'Folder dalam tanda kurung untuk mengelompokkan tanpa memengaruhi URL.'),
       ('Special files', 'loading.tsx, error.tsx, not-found.tsx, template.tsx.')],
  cx=[R('Struktur folder dan layout bersarang', r'''
app/
├── layout.tsx                 -> <html> root, font, header
├── page.tsx                   -> /
├── (toko)/
│   ├── layout.tsx             -> layout dengan sidebar kategori
│   ├── produk/page.tsx        -> /produk
│   └── keranjang/page.tsx     -> /keranjang
├── (akun)/akun/page.tsx       -> /akun
└── not-found.tsx

// app/layout.tsx
import Link from "next/link";
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="id">
      <body>
        <header>
          <Link href="/">Beranda</Link>
          <Link href="/produk">Produk</Link>
          <Link href="/keranjang" prefetch={false}>Keranjang</Link>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}'''),
      T('Dari daftar file ke tabel rute', r'''
const file = [
  "app/page.tsx", "app/(toko)/produk/page.tsx", "app/(toko)/produk/[slug]/page.tsx",
  "app/(toko)/keranjang/page.tsx", "app/blog/[...slug]/page.tsx", "app/api/produk/route.ts",
  "app/(toko)/layout.tsx", "app/_komponen/Tombol.tsx",
];
for (const f of file) {
  const m = f.match(/^app\/(.*?)\/?(page\.tsx|route\.ts)$/);
  if (!m) { console.log(f.padEnd(36), "-> bukan rute (layout/privat)"); continue; }
  const url = "/" + m[1].split("/").filter((s) => s && !/^\(.*\)$/.test(s) && !s.startsWith("_"))
    .map((s) => s.replace(/^\[\.\.\.(\w+)\]$/, ":$1*").replace(/^\[(\w+)\]$/, ":$1")).join("/");
  console.log(f.padEnd(36), "->", url, m[2] === "route.ts" ? "(API)" : "");
}
''')]),

'Route dinamis dan metadata': dict(
  ist=[('Dynamic segment [slug]', 'Folder [slug] menerima nilai apa pun dari URL.'),
       ('generateStaticParams', 'Daftar parameter yang di-render statis saat build.'),
       ('generateMetadata', 'Membuat title, description, dan Open Graph per halaman.'),
       ('Open Graph', 'Metadata pratinjau tautan di WhatsApp, X, LinkedIn.'),
       ('Canonical URL', 'Alamat utama halaman agar tidak dianggap konten duplikat.')],
  cx=[R('Halaman produk dengan metadata dinamis', r'''
// app/produk/[slug]/page.tsx
import type { Metadata } from "next";
import { notFound } from "next/navigation";

type Props = { params: Promise<{ slug: string }> };

export async function generateStaticParams() {
  const produk = await db.produk.findMany({ select: { slug: true }, take: 100 });
  return produk.map((p) => ({ slug: p.slug }));           // 100 terlaris dibuat saat build
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const p = await ambilProduk((await params).slug);
  if (!p) return {};
  return {
    title: `${p.nama} | Toko Kopi`,
    description: p.ringkasan.slice(0, 155),
    alternates: { canonical: `/produk/${p.slug}` },
    openGraph: { images: [{ url: p.gambar, width: 1200, height: 630 }] },
  };
}

export default async function Halaman({ params }: Props) {
  const p = await ambilProduk((await params).slug);
  if (!p) notFound();
  return <h1>{p.nama}</h1>;
}'''),
      T('Membuat slug dan memotong deskripsi untuk SEO', r'''
const slugify = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase()
  .replace(/&/g, " dan ").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const potong = (s: string, n = 155) => (s.length <= n ? s : s.slice(0, s.lastIndexOf(" ", n - 1)) + "…");

const produk = ["Kopi Arabika Gayo 250g", "Teh & Gula Aren — Paket Hemat", "Café Crème Spécial"];
produk.forEach((p) => console.log(p.padEnd(32), "->", "/produk/" + slugify(p)));
const desk = "Kopi arabika dari dataran tinggi Gayo, Aceh, diproses full wash dan disangrai medium. Rasa cokelat, jeruk, dan karamel dengan keasaman sedang yang cocok untuk V60 maupun espresso harian.";
const d = potong(desk);
console.log(d.length, "karakter:", d);
''')]),

'Server Component vs Client Component': dict(
  ist=[('React Server Component (RSC)', 'Default di App Router: berjalan di server, boleh async, akses DB langsung, tanpa JS ke klien.'),
       ('"use client"', 'Direktif di awal file yang menjadikannya Client Component (boleh state, effect, event).'),
       ('Bundle size', 'Kode Server Component tidak ikut dikirim ke browser.'),
       ('server-only', 'Paket penanda agar modul rahasia gagal di-build bila terimpor ke klien.')],
  cx=[R('Halaman server dengan tombol interaktif kecil', r'''
// app/produk/page.tsx  (Server Component: default)
import "server-only";
import { TombolTambah } from "./TombolTambah";

export default async function Produk() {
  const daftar = await db.produk.findMany({ orderBy: { terjual: "desc" }, take: 12 });  // query langsung
  return (
    <ul className="grid">
      {daftar.map((p) => (
        <li key={p.id}>
          <h3>{p.nama}</h3>
          <p>Rp{p.harga.toLocaleString("id-ID")}</p>
          <TombolTambah id={p.id} />      {/* hanya bagian ini yang butuh JS */}
        </li>
      ))}
    </ul>
  );
}

// app/produk/TombolTambah.tsx
"use client";
import { useState } from "react";
export function TombolTambah({ id }: { id: number }) {
  const [ok, setOk] = useState(false);
  return <button onClick={() => { tambahKeKeranjang(id); setOk(true); }}>{ok ? "✓ Ditambahkan" : "Tambah"}</button>;
}''')]),

'Pola komposisi dan batas client': dict(
  ist=[('Client boundary', 'File "use client" dan semua yang diimpornya menjadi bagian bundle klien.'),
       ('Children pattern', 'Client Component menerima Server Component lewat children agar tetap di server.'),
       ('Serializable props', 'Props dari server ke klien harus bisa di-JSON-kan (tanpa fungsi, kelas, Date mentah).'),
       ('Push client down', 'Letakkan "use client" serendah mungkin di pohon komponen.')],
  cx=[R('Sidebar interaktif yang membungkus konten server', r'''
// app/dasbor/Sidebar.tsx
"use client";
import { useState, type ReactNode } from "react";
export function Sidebar({ children }: { children: ReactNode }) {
  const [buka, setBuka] = useState(true);
  return (
    <aside data-buka={buka}>
      <button onClick={() => setBuka(!buka)} aria-expanded={buka}>Menu</button>
      {buka && children}          {/* children tetap Server Component */}
    </aside>
  );
}

// app/dasbor/layout.tsx  (server)
export default async function Layout({ children }: { children: ReactNode }) {
  const menu = await ambilMenuSesuaiPeran();      // data di server
  return (
    <div className="dasbor">
      <Sidebar><NavServer menu={menu} /></Sidebar>
      {children}
    </div>
  );
}

// SALAH: mengimpor Server Component di dalam file "use client"
// "use client"; import NavServer from "./NavServer";  -> NavServer ikut menjadi klien'''),
      T('Memeriksa apakah props aman dikirim ke klien', r'''
function cekSerializable(nilai: unknown, jalur = "props"): string[] {
  if (nilai === null || ["string", "number", "boolean", "undefined"].includes(typeof nilai)) return [];
  if (typeof nilai === "function") return [`${jalur}: fungsi tidak bisa dikirim (pakai Server Action)`];
  if (nilai instanceof Date) return [`${jalur}: Date sebaiknya dikirim sebagai string ISO`];
  if (nilai instanceof Map || nilai instanceof Set) return [];
  if (Array.isArray(nilai)) return nilai.flatMap((v, i) => cekSerializable(v, `${jalur}[${i}]`));
  if (Object.getPrototypeOf(nilai) !== Object.prototype) return [`${jalur}: instance kelas tidak didukung`];
  return Object.entries(nilai as object).flatMap(([k, v]) => cekSerializable(v, `${jalur}.${k}`));
}
class Uang { constructor(public n: number) {} }
const props = { nama: "Kopi", harga: 45000, dibuat: new Date(), onBeli: () => {}, diskon: new Uang(5000), tag: ["baru"] };
const masalah = cekSerializable(props);
console.log(masalah.length ? masalah.join("\n") : "semua aman");
''')]),

'Hydration dan kesalahan umum': dict(
  ist=[('Hydration', 'React di browser "menghidupkan" HTML dari server dengan memasang event handler.'),
       ('Hydration mismatch', 'HTML server berbeda dengan render pertama klien; React memberi peringatan dan merender ulang.'),
       ('suppressHydrationWarning', 'Pengecualian untuk nilai yang memang berbeda (misalnya jam).'),
       ('Selective hydration', 'Bagian dalam Suspense dihidupkan bertahap sesuai prioritas.')],
  cx=[R('Penyebab mismatch dan perbaikannya', r'''
// SALAH: nilai berbeda di server dan browser
export function Salam() {
  const jam = new Date().getHours();                  // zona waktu server (UTC) ≠ browser (WIB)
  return <p>{jam < 12 ? "Selamat pagi" : "Selamat siang"}</p>;
}
// SALAH: akses window saat render
const lebar = typeof window !== "undefined" ? window.innerWidth : 0;

// BENAR: tunda nilai khusus browser sampai setelah mount
"use client";
import { useEffect, useState } from "react";
export function SalamAman() {
  const [teks, setTeks] = useState<string | null>(null);
  useEffect(() => setTeks(new Date().getHours() < 12 ? "Selamat pagi" : "Selamat siang"), []);
  return <p>{teks ?? "Halo"}</p>;
}

// BENAR: komponen yang hanya jalan di browser
import dynamic from "next/dynamic";
const Peta = dynamic(() => import("./Peta"), { ssr: false, loading: () => <div className="skeleton h-80" /> });

// Penyebab lain: <p> di dalam <p>, <div> di dalam <p>, ekstensi browser yang menyisipkan atribut'''),
      T('Kenapa jam server dan browser berbeda', r'''
const momen = new Date(Date.UTC(2026, 10, 19, 4, 30));  // 04:30 UTC
const jamDi = (tz: string) => Number(new Intl.DateTimeFormat("en-GB", { hour: "numeric", hourCycle: "h23", timeZone: tz }).format(momen));
const salam = (j: number) => (j < 11 ? "Selamat pagi" : j < 15 ? "Selamat siang" : "Selamat sore");
const server = jamDi("UTC"), browser = jamDi("Asia/Jakarta");
console.log(`server (UTC) jam ${server}  -> "${salam(server)}"`);
console.log(`browser (WIB) jam ${browser} -> "${salam(browser)}"`);
console.log(salam(server) === salam(browser) ? "cocok" : "MISMATCH: teks HTML server berbeda dengan render klien");
''')]),

'Mengambil data dan revalidasi': dict(
  ist=[('fetch di Server Component', 'Ambil data langsung dengan async/await di komponen.'),
       ('Data Cache', 'Hasil fetch dapat di-cache; Next.js 15 tidak lagi meng-cache fetch secara default.'),
       ('revalidate', 'Waktu (detik) sebelum cache dianggap basi (ISR).'),
       ('revalidateTag / revalidatePath', 'Membuang cache secara on-demand setelah data berubah.'),
       ('"use cache"', 'Direktif cache baru (Next.js 16, Cache Components) untuk fungsi atau komponen.')],
  cx=[R('Katalog dengan ISR dan revalidasi berbasis tag', r'''
// app/produk/page.tsx
export const revalidate = 300;                      // ISR: halaman dibuat ulang maksimal tiap 5 menit

async function ambilProduk() {
  const r = await fetch("https://api.toko.id/produk", { next: { revalidate: 300, tags: ["produk"] } });
  if (!r.ok) throw new Error("Gagal memuat produk");
  return r.json() as Promise<Produk[]>;
}

export default async function Halaman() {
  const [produk, kategori] = await Promise.all([ambilProduk(), ambilKategori()]);   // paralel, bukan waterfall
  return <Katalog produk={produk} kategori={kategori} />;
}

// app/admin/actions.ts
"use server";
import { revalidateTag } from "next/cache";
export async function ubahHarga(id: number, harga: number) {
  await db.produk.update({ where: { id }, data: { harga } });
  revalidateTag("produk");                          // katalog langsung segar
}'''),
      T('Simulasi stale-while-revalidate', r'''
function buatCache(revalidateDetik: number, sumber: () => number) {
  let isi: { nilai: number; waktu: number } | null = null; let generasi = 0;
  return (t: number) => {
    if (!isi) { isi = { nilai: sumber(), waktu: t }; return `t=${t}s MISS  -> render baru (harga ${isi.nilai})`; }
    if (t - isi.waktu < revalidateDetik) return `t=${t}s HIT   -> dari cache (harga ${isi.nilai})`;
    const basi = isi.nilai; isi = { nilai: sumber(), waktu: t }; generasi++;
    return `t=${t}s STALE -> kirim cache lama (${basi}), regenerasi di belakang -> ${isi.nilai}`;
  };
}
let harga = 45000;
const ambil = buatCache(60, () => harga);
console.log(ambil(0)); console.log(ambil(30));
harga = 47000;                         // admin mengubah harga
console.log(ambil(45)); console.log(ambil(70)); console.log(ambil(80));
''', 'Pengunjung pertama setelah kedaluwarsa masih melihat data lama sekali, lalu pengunjung berikutnya mendapat versi baru. Pakai revalidateTag bila perubahan harus langsung terlihat.')]),

'Streaming dengan loading dan Suspense': dict(
  ist=[('Streaming SSR', 'Server mengirim HTML bertahap; bagian cepat tampil lebih dulu.'),
       ('loading.tsx', 'Fallback otomatis untuk satu segmen rute (dibungkus Suspense).'),
       ('Suspense boundary', 'Batas per bagian halaman agar komponen lambat tidak menahan semuanya.'),
       ('TTFB & FCP', 'Time to First Byte dan First Contentful Paint membaik dengan streaming.')],
  cx=[R('Dasbor dengan bagian yang dimuat bertahap', r'''
// app/dasbor/loading.tsx
export default function Loading() { return <div className="skeleton h-screen" />; }

// app/dasbor/page.tsx
import { Suspense } from "react";
export default function Dasbor() {
  return (
    <>
      <h1>Ringkasan Toko</h1>                                {/* langsung tampil */}
      <Suspense fallback={<KartuSkeleton />}><Omzet /></Suspense>          {/* 200 ms */}
      <Suspense fallback={<TabelSkeleton />}><PesananTerbaru /></Suspense> {/* 800 ms */}
      <Suspense fallback={<GrafikSkeleton />}><GrafikTahunan /></Suspense> {/* 2 detik */}
    </>
  );
}
async function GrafikTahunan() {
  const data = await laporanTahunan();     // query berat
  return <Grafik data={data} />;
}'''),
      T('Tanpa streaming vs dengan streaming', r'''
const bagian = [["Header", 0], ["Omzet", 200], ["Pesanan terbaru", 800], ["Grafik tahunan", 2000]] as const;
const tanpa = Math.max(...bagian.map(([, ms]) => ms));
console.log(`Tanpa streaming: layar kosong sampai ${tanpa} ms, lalu semua muncul bersamaan`);
console.log("Dengan streaming:");
for (const [nama, ms] of bagian) console.log(`  ${String(ms).padStart(5)} ms  ${nama} tampil`);
console.log(`Konten pertama ${tanpa / Math.max(1, bagian[1][1])}x lebih cepat terlihat`);
''')]),

'Server Actions dan Route Handlers': dict(
  ist=[('Server Action', 'Fungsi "use server" yang dipanggil dari form/klien dan berjalan di server.'),
       ('Progressive enhancement', 'Form dengan Server Action tetap berfungsi walau JavaScript belum dimuat.'),
       ('useActionState', 'Hook React 19 untuk status dan hasil sebuah action.'),
       ('Route Handler', 'File route.ts berisi fungsi GET/POST untuk API publik atau webhook.'),
       ('Webhook', 'Endpoint yang dipanggil layanan lain (misalnya payment gateway) saat ada kejadian.')],
  cx=[R('Form ulasan dengan Server Action dan webhook pembayaran', r'''
// app/produk/[slug]/actions.ts
"use server";
import { z } from "zod";
import { revalidatePath } from "next/cache";

const Ulasan = z.object({ produkId: z.coerce.number(), bintang: z.coerce.number().min(1).max(5), isi: z.string().min(10) });

export async function kirimUlasan(_: unknown, form: FormData) {
  const user = await auth();
  if (!user) return { error: "Silakan masuk dulu" };
  const hasil = Ulasan.safeParse(Object.fromEntries(form));
  if (!hasil.success) return { error: hasil.error.issues[0].message };
  await db.ulasan.create({ data: { ...hasil.data, userId: user.id } });
  revalidatePath(`/produk/${hasil.data.produkId}`);
  return { ok: true };
}

// FormUlasan.tsx
"use client";
import { useActionState } from "react";
export function FormUlasan({ produkId }: { produkId: number }) {
  const [state, action, pending] = useActionState(kirimUlasan, null);
  return (
    <form action={action}>
      <input type="hidden" name="produkId" value={produkId} />
      <select name="bintang">{[5, 4, 3, 2, 1].map((b) => <option key={b}>{b}</option>)}</select>
      <textarea name="isi" required minLength={10} />
      <button disabled={pending}>{pending ? "Mengirim..." : "Kirim ulasan"}</button>
      {state?.error && <p role="alert">{state.error}</p>}
    </form>
  );
}

// app/api/webhook/pembayaran/route.ts
export async function POST(req: Request) {
  const body = await req.text();
  if (!verifikasiSignature(body, req.headers.get("x-signature"))) return new Response("invalid", { status: 401 });
  const ev = JSON.parse(body);
  if (ev.status === "settlement") await tandaiLunas(ev.order_id);
  return Response.json({ diterima: true });
}'''),
      T('Verifikasi signature webhook dengan HMAC', r'''
import { createHmac, timingSafeEqual } from "node:crypto";

const RAHASIA = "kunci-rahasia-dari-dashboard-payment";
const tandatangan = (body: string) => createHmac("sha256", RAHASIA).update(body).digest("hex");
function verifikasi(body: string, sig: string | null) {
  if (!sig) return false;
  const a = Buffer.from(tandatangan(body)), b = Buffer.from(sig);
  return a.length === b.length && timingSafeEqual(a, b);     // tahan timing attack
}
const body = JSON.stringify({ order_id: "INV-2026-0042", status: "settlement", gross_amount: "148000" });
const sigAsli = tandatangan(body);
console.log("signature asli    :", verifikasi(body, sigAsli) ? "200 diterima" : "401 ditolak");
console.log("body diubah       :", verifikasi(body.replace("148000", "1000"), sigAsli) ? "200 diterima" : "401 ditolak");
console.log("tanpa signature   :", verifikasi(body, null) ? "200 diterima" : "401 ditolak");
''')]),

'Optimasi gambar dan font': dict(
  ist=[('next/image', 'Mengubah ukuran, format (WebP/AVIF), dan lazy load gambar otomatis.'),
       ('sizes & srcset', 'Memberi tahu browser lebar gambar di tiap breakpoint agar unduhan pas.'),
       ('priority / fetchPriority', 'Muat lebih dulu gambar LCP (biasanya hero).'),
       ('next/font', 'Font di-self-host saat build; tanpa request ke Google, tanpa layout shift.'),
       ('CLS', 'Cumulative Layout Shift; width/height pada gambar mencegah konten melompat.')],
  cx=[R('Hero dan grid produk yang dioptimalkan', r'''
import Image from "next/image";
import { Inter, Plus_Jakarta_Sans } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter", display: "swap" });
const jakarta = Plus_Jakarta_Sans({ subsets: ["latin"], weight: ["600", "800"], variable: "--font-judul" });

export default function Beranda({ produk }: { produk: Produk[] }) {
  return (
    <main className={`${inter.variable} ${jakarta.variable}`}>
      <Image src="/hero-kopi.jpg" alt="Biji kopi Gayo disangrai" width={1600} height={900}
             priority sizes="100vw" className="w-full h-auto" />
      <ul className="grid grid-cols-2 md:grid-cols-4">
        {produk.map((p) => (
          <li key={p.id}>
            <Image src={p.gambar} alt={p.nama} width={400} height={400}
                   sizes="(min-width: 768px) 25vw, 50vw" placeholder="blur" blurDataURL={p.blur} />
          </li>
        ))}
      </ul>
    </main>
  );
}'''),
      T('Berapa byte yang dihemat oleh sizes yang tepat', r'''
const lebarTersedia = [640, 750, 828, 1080, 1200, 1920];
const kbPerPx = (w: number) => Math.round((w * w) * 0.00009);   // perkiraan JPEG->WebP persegi
function pilih(lebarTampil: number, dpr: number) {
  const target = lebarTampil * dpr;
  return lebarTersedia.find((w) => w >= target) ?? lebarTersedia.at(-1)!;
}
for (const [perangkat, viewport, dpr] of [["Ponsel", 390, 3], ["Tablet", 820, 2], ["Laptop", 1440, 1]] as const) {
  const lebarKartu = viewport >= 768 ? viewport / 4 : viewport / 2;
  const tanpaSizes = pilih(viewport, dpr), denganSizes = pilih(lebarKartu, dpr);
  console.log(`${perangkat.padEnd(7)} tanpa sizes ${String(tanpaSizes).padStart(4)}px ~${String(kbPerPx(tanpaSizes)).padStart(3)} KB | dengan sizes ${String(denganSizes).padStart(4)}px ~${String(kbPerPx(denganSizes)).padStart(3)} KB`);
}
''')]),

'Middleware dan autentikasi': dict(
  ist=[('Middleware / proxy.ts', 'Kode yang berjalan sebelum request mencapai halaman (Next.js 16 menamainya proxy).'),
       ('Matcher', 'Pola path yang diproses middleware.'),
       ('Auth.js / Clerk / Better Auth', 'Pustaka autentikasi populer untuk Next.js.'),
       ('Session cookie (httpOnly)', 'Cookie yang tidak dapat dibaca JavaScript; melindungi dari pencurian token lewat XSS.'),
       ('Defense in depth', 'Cek auth di middleware dan juga di Server Component/Action, jangan hanya satu lapis.')],
  cx=[R('Melindungi /akun dan /admin', r'''
// middleware.ts (Next.js 15) atau proxy.ts (Next.js 16)
import { NextResponse, type NextRequest } from "next/server";

export function middleware(req: NextRequest) {
  const sesi = req.cookies.get("sesi")?.value;
  const { pathname } = req.nextUrl;
  if (!sesi) {
    const url = new URL("/masuk", req.url);
    url.searchParams.set("lanjut", pathname);
    return NextResponse.redirect(url);
  }
  const res = NextResponse.next();
  res.headers.set("x-frame-options", "DENY");
  return res;
}
export const config = { matcher: ["/akun/:path*", "/admin/:path*"] };

// app/admin/page.tsx  -> tetap cek ulang di server
export default async function Admin() {
  const user = await auth();
  if (user?.peran !== "admin") redirect("/");
  return <PanelAdmin />;
}'''),
      T('Logika matcher dan redirect', r'''
const matcher = ["/akun/:path*", "/admin/:path*"];
const keRegex = (p: string) => new RegExp("^" + p.replace(/\/:path\*$/, "(/.*)?") + "$");
function proses(path: string, sesi?: { peran: string }) {
  if (!matcher.some((m) => keRegex(m).test(path))) return "lewat (publik)";
  if (!sesi) return `302 -> /masuk?lanjut=${encodeURIComponent(path)}`;
  if (path.startsWith("/admin") && sesi.peran !== "admin") return "403 bukan admin";
  return "200 lanjut ke halaman";
}
const uji: [string, { peran: string }?][] = [["/produk"], ["/akun/pesanan"], ["/akun", { peran: "user" }], ["/admin/laporan", { peran: "user" }], ["/admin", { peran: "admin" }]];
for (const [p, s] of uji) console.log(p.padEnd(16), (s?.peran ?? "tamu").padEnd(6), "->", proses(p, s));
''')]),

'Variabel lingkungan dan deployment': dict(
  ist=[('.env.local', 'File variabel lingkungan lokal; tidak boleh di-commit.'),
       ('NEXT_PUBLIC_', 'Prefiks untuk variabel yang boleh terlihat di browser; selain itu hanya di server.'),
       ('Preview deployment', 'Setiap pull request mendapat URL sendiri untuk direview (Vercel, Netlify).'),
       ('output: "standalone"', 'Build mandiri untuk Docker/VPS tanpa node_modules penuh.'),
       ('Edge vs Node runtime', 'Edge lebih cepat start dan dekat pengguna, tetapi API Node terbatas.')],
  cx=[R('Konfigurasi env dan Docker', r'''
# .env.local  (JANGAN di-commit; tambahkan ke .gitignore)
DATABASE_URL="postgresql://user:pass@localhost:5432/toko"
MIDTRANS_SERVER_KEY="SB-Mid-server-xxx"          # rahasia: hanya server
NEXT_PUBLIC_SITE_URL="https://toko.example.id"    # aman tampil di browser

# Validasi env saat start (src/env.ts)
import { z } from "zod";
export const env = z.object({
  DATABASE_URL: z.string().url(),
  MIDTRANS_SERVER_KEY: z.string().min(10),
  NEXT_PUBLIC_SITE_URL: z.string().url(),
}).parse(process.env);

# next.config.ts
export default { output: "standalone", images: { remotePatterns: [{ hostname: "cdn.toko.id" }] } };

# Dockerfile (ringkas)
FROM node:22-alpine AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build
FROM node:22-alpine
WORKDIR /app
COPY --from=build /app/.next/standalone ./
COPY --from=build /app/.next/static ./.next/static
COPY --from=build /app/public ./public
CMD ["node", "server.js"]''', lang='bash'),
      T('Memeriksa env sebelum deploy', r'''
const env: Record<string, string | undefined> = {
  DATABASE_URL: "postgresql://user:pass@db:5432/toko",
  NEXT_PUBLIC_SITE_URL: "https://toko.example.id",
  NEXT_PUBLIC_MIDTRANS_SERVER_KEY: "SB-Mid-server-abc123",
  SENTRY_DSN: undefined,
};
const wajib = ["DATABASE_URL", "NEXT_PUBLIC_SITE_URL", "SENTRY_DSN"];
const kataRahasia = /SECRET|SERVER_KEY|PASSWORD|TOKEN|PRIVATE/;
for (const k of wajib) if (!env[k]) console.log(`✗ ${k} belum diisi`);
for (const k of Object.keys(env))
  if (k.startsWith("NEXT_PUBLIC_") && kataRahasia.test(k)) console.log(`✗ ${k}: rahasia akan bocor ke browser, hapus prefiks NEXT_PUBLIC_`);
const url = env.NEXT_PUBLIC_SITE_URL ?? "";
console.log(url.startsWith("https://") ? "✓ SITE_URL memakai HTTPS" : "✗ SITE_URL harus HTTPS");
''')]),
}
