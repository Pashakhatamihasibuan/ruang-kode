"""Pendalaman jalur React: istilah dunia kerja, komponen TSX siap pakai, dan logika yang dijalankan dengan Node."""
K = 'react'


def R(t, code, b=None, lang='tsx'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def T(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='ts')


D = {
'Komponen & JSX': dict(
  ist=[('Component', 'Fungsi yang menerima props dan mengembalikan JSX; nama diawali huruf kapital.'),
       ('JSX', 'Sintaks mirip HTML di JavaScript; dikompilasi menjadi pemanggilan fungsi jsx().'),
       ('Fragment (<>...</>)', 'Membungkus beberapa elemen tanpa menambah div ke DOM.'),
       ('Declarative UI', 'Kita menulis tampilan untuk suatu state; React yang memperbarui DOM.'),
       ('Virtual DOM & reconciliation', 'React membandingkan pohon elemen lama dan baru, lalu hanya mengubah bagian yang berbeda.')],
  cx=[R('Komponen kartu produk', r'''
type Produk = { nama: string; harga: number; gambar: string; stok: number };

export function KartuProduk({ nama, harga, gambar, stok }: Produk) {
  const habis = stok === 0;
  return (
    <article className="kartu">
      <img src={gambar} alt={nama} width={240} height={240} loading="lazy" />
      <h3>{nama}</h3>
      <p className="harga">Rp{harga.toLocaleString("id-ID")}</p>
      {habis ? <span className="badge">Stok habis</span> : <small>Sisa {stok}</small>}
    </article>
  );
}'''),
      T('Apa yang sebenarnya dihasilkan JSX', r'''
// <h3 className="judul">Halo {nama}</h3> dikompilasi menjadi jsx("h3", {...})
type El = { type: string; props: { children?: (El | string)[]; [k: string]: unknown } };
const jsx = (type: string, props: Record<string, unknown>, ...children: (El | string)[]): El =>
  ({ type, props: { ...props, children } });

function render(el: El | string): string {
  if (typeof el === "string") return el;
  const attr = Object.entries(el.props).filter(([k]) => k !== "children")
    .map(([k, v]) => ` ${k === "className" ? "class" : k}="${v}"`).join("");
  return `<${el.type}${attr}>${(el.props.children ?? []).map(render).join("")}</${el.type}>`;
}
const nama = "Rina";
const pohon = jsx("article", { className: "kartu" }, jsx("h3", {}, "Halo ", nama), jsx("p", { className: "harga" }, "Rp45.000"));
console.log(JSON.stringify(pohon).slice(0, 80) + "...");
console.log(render(pohon));
''', 'Elemen React hanyalah objek biasa. Inilah alasan JSX bisa disimpan di variabel, dikembalikan dari fungsi, dan dipetakan dari array.')]),

'Props': dict(
  ist=[('Props', 'Data dari induk ke anak; bersifat read-only.'),
       ('children', 'Prop khusus berisi elemen di antara tag pembuka dan penutup.'),
       ('Default value', 'Nilai bawaan lewat destructuring: { ukuran = "md" }.'),
       ('Prop drilling', 'Meneruskan props melewati banyak lapis komponen; solusinya Context atau komposisi.'),
       ('Unidirectional data flow', 'Data mengalir satu arah dari atas ke bawah.')],
  cx=[R('Tombol yang dapat dipakai ulang dengan varian', r'''
import type { ComponentProps, ReactNode } from "react";

type TombolProps = ComponentProps<"button"> & {
  varian?: "utama" | "sekunder" | "bahaya";
  ukuran?: "sm" | "md" | "lg";
  ikon?: ReactNode;
};

export function Tombol({ varian = "utama", ukuran = "md", ikon, children, ...sisa }: TombolProps) {
  return (
    <button className={`btn btn-${varian} btn-${ukuran}`} {...sisa}>
      {ikon && <span aria-hidden="true">{ikon}</span>}
      {children}
    </button>
  );
}

// Pemakaian
<Tombol onClick={simpan}>Simpan</Tombol>
<Tombol varian="bahaya" ukuran="sm" ikon="🗑" disabled={!dipilih}>Hapus</Tombol>''')]),

'State dengan useState': dict(
  ist=[('State', 'Data milik komponen yang, bila berubah, memicu render ulang.'),
       ('Immutable update', 'Buat salinan baru ({...obj}, [...arr]); jangan mengubah state langsung.'),
       ('Functional update', 'setN(n => n + 1) memakai nilai terbaru; aman saat beberapa update beruntun.'),
       ('Batching', 'React 18+ menggabungkan beberapa setState menjadi satu render.'),
       ('Lifting state up', 'Memindahkan state ke induk bersama agar dua komponen bisa berbagi.')],
  cx=[R('Penghitung jumlah barang', r'''
import { useState } from "react";

export function PilihJumlah({ stok }: { stok: number }) {
  const [qty, setQty] = useState(1);
  return (
    <div className="qty">
      <button onClick={() => setQty((q) => Math.max(1, q - 1))} aria-label="Kurangi">−</button>
      <output aria-live="polite">{qty}</output>
      <button onClick={() => setQty((q) => Math.min(stok, q + 1))} aria-label="Tambah" disabled={qty >= stok}>+</button>
    </div>
  );
}'''),
      T('Kenapa functional update penting', r'''
// simulasi: setState mengantre update, lalu React memprosesnya sekali (batching)
function buatState<T>(awal: T) {
  let nilai = awal; const antre: ((v: T) => T)[] = [];
  const set = (x: T | ((v: T) => T)) => antre.push(typeof x === "function" ? (x as (v: T) => T) : () => x);
  const flush = () => { for (const f of antre.splice(0)) nilai = f(nilai); return nilai; };
  return { get: () => nilai, set, flush };
}
const a = buatState(0);
a.set(a.get() + 1); a.set(a.get() + 1); a.set(a.get() + 1);   // ketiganya membaca 0
console.log("setN(n + 1) x3      ->", a.flush());
const b = buatState(0);
b.set((n) => n + 1); b.set((n) => n + 1); b.set((n) => n + 1);
console.log("setN(n => n + 1) x3 ->", b.flush());

const keranjang = [{ sku: "KP", qty: 1 }];
const salah = keranjang; salah[0].qty = 2;                   // mutasi: referensi sama, React tidak melihat perubahan
const benar = keranjang.map((i) => (i.sku === "KP" ? { ...i, qty: 3 } : i));
console.log("mutasi: referensi sama?", salah === keranjang, "| salinan baru?", benar !== keranjang);
''')]),

'Event, percabangan & daftar': dict(
  ist=[('Synthetic event', 'Pembungkus event browser yang konsisten di semua browser.'),
       ('Conditional rendering', '&&, operator ternary, atau return lebih awal.'),
       ('key', 'Identitas stabil setiap item daftar; pakai id, bukan indeks array.'),
       ('preventDefault', 'Mencegah aksi bawaan seperti reload saat submit form.')],
  cx=[R('Daftar tugas dengan filter', r'''
import { useState } from "react";
type Tugas = { id: string; judul: string; selesai: boolean };

export function DaftarTugas({ awal }: { awal: Tugas[] }) {
  const [tugas, setTugas] = useState(awal);
  const [filter, setFilter] = useState<"semua" | "aktif" | "selesai">("semua");
  const tampil = tugas.filter((t) => filter === "semua" || (filter === "selesai") === t.selesai);

  const toggle = (id: string) =>
    setTugas((ts) => ts.map((t) => (t.id === id ? { ...t, selesai: !t.selesai } : t)));

  return (
    <section>
      <div role="group" aria-label="Filter">
        {(["semua", "aktif", "selesai"] as const).map((f) => (
          <button key={f} aria-pressed={filter === f} onClick={() => setFilter(f)}>{f}</button>
        ))}
      </div>
      {tampil.length === 0 ? (
        <p>Tidak ada tugas {filter}.</p>
      ) : (
        <ul>
          {tampil.map((t) => (
            <li key={t.id}>
              <label><input type="checkbox" checked={t.selesai} onChange={() => toggle(t.id)} /> {t.judul}</label>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}'''),
      T('Kenapa key = indeks bermasalah', r'''
// React mencocokkan item lama dan baru berdasarkan key
const lama = ["Ani", "Budi", "Citra"];
const baru = ["Zara", ...lama];   // item baru disisipkan di depan

function cocokkan(keyFn: (n: string, i: number) => string) {
  const petaLama = new Map(lama.map((n, i) => [keyFn(n, i), n]));
  return baru.map((n, i) => {
    const k = keyFn(n, i), dulu = petaLama.get(k);
    return dulu === undefined ? `${n}: dibuat baru` : dulu === n ? `${n}: dipakai ulang` : `${n}: memakai state milik ${dulu}!`;
  });
}
console.log("key = indeks :", cocokkan((_, i) => String(i)).join(" | "));
console.log("key = id     :", cocokkan((n) => n).join(" | "));
''', 'Dengan indeks sebagai key, isi input atau checkbox milik "Ani" bisa berpindah ke "Zara". Dengan id, setiap item tetap membawa state-nya sendiri.')]),

'useEffect & siklus hidup': dict(
  ist=[('Side effect', 'Kerja di luar render: fetch, timer, langganan, akses DOM.'),
       ('Dependency array', '[] sekali saat mount, [x] saat x berubah, tanpa array setiap render.'),
       ('Cleanup function', 'Fungsi yang dikembalikan effect untuk membersihkan timer/langganan.'),
       ('Strict Mode double invoke', 'Di development effect dijalankan dua kali untuk mendeteksi cleanup yang hilang.'),
       ('You might not need an effect', 'Nilai turunan dihitung saat render, bukan disimpan lewat effect.')],
  cx=[R('Jam digital dan judul tab dengan cleanup', r'''
import { useEffect, useState } from "react";

export function Jam() {
  const [sekarang, setSekarang] = useState(() => new Date());
  useEffect(() => {
    const id = setInterval(() => setSekarang(new Date()), 1000);
    return () => clearInterval(id);            // cleanup saat unmount
  }, []);
  return <time>{sekarang.toLocaleTimeString("id-ID")}</time>;
}

export function JudulKeranjang({ jumlah }: { jumlah: number }) {
  useEffect(() => {
    document.title = jumlah ? `(${jumlah}) Keranjang` : "Toko";
  }, [jumlah]);                               // hanya saat jumlah berubah
  return null;
}

// Anti-pattern: effect untuk nilai turunan
// const [total, setTotal] = useState(0);
// useEffect(() => setTotal(item.reduce(...)), [item]);
// Benar: const total = item.reduce((a, i) => a + i.harga * i.qty, 0);'''),
      T('Simulasi mount, update, dan cleanup', r'''
function komponen(nama: string) {
  let cleanup: (() => void) | undefined; let depsLama: unknown[] | undefined;
  return (deps: unknown[]) => {
    const berubah = !depsLama || deps.some((d, i) => !Object.is(d, depsLama![i]));
    if (!berubah) return console.log(`render ${nama}: deps sama, effect dilewati`);
    cleanup?.();
    console.log(`render ${nama}: jalankan effect untuk userId=${deps[0]}`);
    cleanup = () => console.log(`  cleanup: batalkan langganan userId=${deps[0]}`);
    depsLama = deps;
  };
}
const profil = komponen("Profil");
profil([1]); profil([1]); profil([2]);
''')]),

'useRef, useMemo & useCallback': dict(
  ist=[('useRef', 'Wadah nilai yang bertahan antar-render tanpa memicu render; juga untuk akses elemen DOM.'),
       ('useMemo', 'Menyimpan hasil perhitungan mahal sampai dependensinya berubah.'),
       ('useCallback', 'Menyimpan referensi fungsi agar anak yang di-memo tidak render ulang.'),
       ('Referential equality', 'Objek/fungsi baru setiap render dianggap berbeda walau isinya sama.'),
       ('React Compiler', 'Kompiler (stabil 2025) yang otomatis melakukan memoization; mengurangi kebutuhan useMemo manual.')],
  cx=[R('Fokus otomatis dan filter mahal', r'''
import { memo, useCallback, useEffect, useMemo, useRef, useState } from "react";

export function CariProduk({ produk }: { produk: { id: number; nama: string }[] }) {
  const inputRef = useRef<HTMLInputElement>(null);
  const [q, setQ] = useState("");
  useEffect(() => inputRef.current?.focus(), []);

  const hasil = useMemo(
    () => produk.filter((p) => p.nama.toLowerCase().includes(q.toLowerCase())),
    [produk, q],
  );
  const pilih = useCallback((id: number) => console.log("dipilih", id), []);

  return (
    <>
      <input ref={inputRef} value={q} onChange={(e) => setQ(e.target.value)} placeholder="Cari..." />
      <Daftar item={hasil} onPilih={pilih} />
    </>
  );
}
const Daftar = memo(function Daftar({ item, onPilih }: { item: { id: number; nama: string }[]; onPilih: (id: number) => void }) {
  return <ul>{item.map((p) => <li key={p.id} onClick={() => onPilih(p.id)}>{p.nama}</li>)}</ul>;
});'''),
      T('Kenapa fungsi baru membuat memo tidak berguna', r'''
const renderAnak = { tanpaCallback: 0, denganCallback: 0 };
let fnTersimpan: (() => void) | undefined;
let propsLamaA: (() => void) | undefined, propsLamaB: (() => void) | undefined;

for (let render = 1; render <= 5; render++) {
  const fnBaru = () => {};                          // dibuat ulang setiap render
  fnTersimpan ??= () => {};                         // seperti useCallback(fn, [])
  if (!Object.is(fnBaru, propsLamaA)) renderAnak.tanpaCallback++;
  if (!Object.is(fnTersimpan, propsLamaB)) renderAnak.denganCallback++;
  propsLamaA = fnBaru; propsLamaB = fnTersimpan;
}
console.log("5 render induk -> anak memo render ulang:", renderAnak);
console.log("{} === {} ?", ({} as object) === ({} as object));
''')]),

'useReducer & Context': dict(
  ist=[('useReducer', 'State dikelola fungsi reducer(state, action); cocok untuk logika kompleks.'),
       ('Action', 'Objek { type, payload } yang menjelaskan apa yang terjadi.'),
       ('Context', 'Membagikan nilai ke seluruh pohon tanpa prop drilling.'),
       ('Provider', 'Komponen yang menyediakan nilai Context.'),
       ('Pure function', 'Reducer harus murni: tanpa efek samping, hasil hanya bergantung input.')],
  cx=[T('Reducer keranjang yang bisa diuji tanpa browser', r'''
type Item = { sku: string; nama: string; harga: number; qty: number };
type State = { item: Item[]; kupon: string | null };
type Action =
  | { type: "tambah"; item: Omit<Item, "qty"> }
  | { type: "ubahQty"; sku: string; qty: number }
  | { type: "hapus"; sku: string }
  | { type: "kupon"; kode: string | null };

function reducer(s: State, a: Action): State {
  switch (a.type) {
    case "tambah": {
      const ada = s.item.some((i) => i.sku === a.item.sku);
      return { ...s, item: ada ? s.item.map((i) => (i.sku === a.item.sku ? { ...i, qty: i.qty + 1 } : i)) : [...s.item, { ...a.item, qty: 1 }] };
    }
    case "ubahQty": return { ...s, item: s.item.map((i) => (i.sku === a.sku ? { ...i, qty: a.qty } : i)).filter((i) => i.qty > 0) };
    case "hapus": return { ...s, item: s.item.filter((i) => i.sku !== a.sku) };
    case "kupon": return { ...s, kupon: a.kode };
  }
}
const aksi: Action[] = [
  { type: "tambah", item: { sku: "KP", nama: "Kopi", harga: 45000 } },
  { type: "tambah", item: { sku: "TH", nama: "Teh", harga: 28000 } },
  { type: "tambah", item: { sku: "KP", nama: "Kopi", harga: 45000 } },
  { type: "ubahQty", sku: "TH", qty: 0 },
  { type: "kupon", kode: "HEMAT10" },
];
const akhir = aksi.reduce(reducer, { item: [], kupon: null });
console.log(akhir.item.map((i) => `${i.nama} x${i.qty}`).join(", "), "| kupon:", akhir.kupon);
console.log("total:", akhir.item.reduce((t, i) => t + i.harga * i.qty, 0).toLocaleString("id-ID"));
''', 'Karena reducer murni, ia bisa diuji dengan Vitest tanpa me-render komponen apa pun.'),
      R('Menyambungkan reducer ke Context', r'''
import { createContext, useContext, useReducer, type Dispatch, type ReactNode } from "react";

const KeranjangCtx = createContext<{ state: State; dispatch: Dispatch<Action> } | null>(null);

export function KeranjangProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(reducer, { item: [], kupon: null });
  return <KeranjangCtx.Provider value={{ state, dispatch }}>{children}</KeranjangCtx.Provider>;
}
export function useKeranjang() {
  const ctx = useContext(KeranjangCtx);
  if (!ctx) throw new Error("useKeranjang harus dipakai di dalam <KeranjangProvider>");
  return ctx;
}''')]),

'Custom hook': dict(
  ist=[('Custom hook', 'Fungsi berawalan use yang membungkus logika ber-state agar dapat dipakai ulang.'),
       ('Rules of Hooks', 'Panggil hook hanya di level atas komponen/hook, tidak di dalam if atau loop.'),
       ('eslint-plugin-react-hooks', 'Linter yang menegakkan aturan hook dan dependency array.')],
  cx=[R('useLocalStorage, useDebounce, dan useMediaQuery', r'''
import { useEffect, useState, useSyncExternalStore } from "react";

export function useLocalStorage<T>(kunci: string, awal: T) {
  const [nilai, setNilai] = useState<T>(() => {
    try { const s = localStorage.getItem(kunci); return s ? (JSON.parse(s) as T) : awal; }
    catch { return awal; }
  });
  useEffect(() => { try { localStorage.setItem(kunci, JSON.stringify(nilai)); } catch {} }, [kunci, nilai]);
  return [nilai, setNilai] as const;
}

export function useDebounce<T>(nilai: T, ms = 300) {
  const [d, setD] = useState(nilai);
  useEffect(() => { const t = setTimeout(() => setD(nilai), ms); return () => clearTimeout(t); }, [nilai, ms]);
  return d;
}

export function useMediaQuery(q: string) {
  return useSyncExternalStore(
    (cb) => { const m = matchMedia(q); m.addEventListener("change", cb); return () => m.removeEventListener("change", cb); },
    () => matchMedia(q).matches,
    () => false,                             // nilai saat SSR
  );
}

// Pemakaian
const [tema, setTema] = useLocalStorage<"terang" | "gelap">("tema", "terang");
const qDebounced = useDebounce(q, 400);
const mobile = useMediaQuery("(max-width: 640px)");'''),
      T('Logika useDebounce diuji dengan waktu palsu', r'''
function debounceSim(ms: number) {
  let jadwal: { at: number; v: string } | null = null; const terkirim: string[] = [];
  return {
    ketik: (t: number, v: string) => { jadwal = { at: t + ms, v }; },
    maju: (t: number) => { if (jadwal && t >= jadwal.at) { terkirim.push(`${jadwal.v}@${jadwal.at}ms`); jadwal = null; } },
    terkirim,
  };
}
const s = debounceSim(400);
const ketikan: [number, string][] = [[0, "s"], [120, "se"], [250, "sep"], [900, "sepa"], [1000, "sepat"], [1100, "sepatu"]];
for (let t = 0; t <= 2000; t += 50) {
  const k = ketikan.find(([w]) => w === t); if (k) s.ketik(...k);
  s.maju(t);
}
console.log("6 ketukan ->", s.terkirim.length, "request:", s.terkirim.join(", "));
''')]),

'useTransition & useDeferredValue: tetap responsif': dict(
  ist=[('Concurrent rendering', 'React dapat menyela render yang kurang penting demi input pengguna.'),
       ('useTransition', 'Menandai update sebagai tidak mendesak; isPending untuk indikator.'),
       ('useDeferredValue', 'Versi nilai yang "tertinggal" agar daftar berat tidak menghambat input.'),
       ('INP', 'Interaction to Next Paint: metrik Core Web Vitals untuk responsivitas (target < 200 ms).')],
  cx=[R('Pencarian 10.000 baris yang tetap lancar diketik', r'''
import { memo, useDeferredValue, useState, useTransition } from "react";

export function Pencarian({ data }: { data: string[] }) {
  const [q, setQ] = useState("");
  const qTunda = useDeferredValue(q);
  const usang = q !== qTunda;
  return (
    <>
      <input value={q} onChange={(e) => setQ(e.target.value)} />
      <div style={{ opacity: usang ? 0.5 : 1 }}><Hasil q={qTunda} data={data} /></div>
    </>
  );
}
const Hasil = memo(({ q, data }: { q: string; data: string[] }) => (
  <ul>{data.filter((d) => d.includes(q)).slice(0, 200).map((d) => <li key={d}>{d}</li>)}</ul>
));

export function Tab() {
  const [tab, setTab] = useState("ringkasan");
  const [isPending, startTransition] = useTransition();
  return (
    <nav aria-busy={isPending}>
      {["ringkasan", "laporan", "grafik"].map((t) => (
        <button key={t} onClick={() => startTransition(() => setTab(t))}>{t}</button>
      ))}
    </nav>
  );
}''')]),

'Komposisi, render props & HOC': dict(
  ist=[('Composition', 'Menyusun komponen kecil lewat children dan slot; lebih disukai daripada pewarisan.'),
       ('Compound component', 'Komponen yang bekerja bersama: <Tabs><Tabs.List/><Tabs.Panel/></Tabs>.'),
       ('Render props', 'Prop berupa fungsi yang mengembalikan JSX.'),
       ('HOC', 'Higher-Order Component: fungsi yang menerima komponen dan mengembalikan komponen baru; kini jarang, diganti hook.')],
  cx=[R('Kartu dengan slot dan compound component', r'''
import { createContext, useContext, useState, type ReactNode } from "react";

export function Kartu({ judul, aksi, children }: { judul: ReactNode; aksi?: ReactNode; children: ReactNode }) {
  return (
    <section className="kartu">
      <header>{judul}{aksi && <div className="aksi">{aksi}</div>}</header>
      <div>{children}</div>
    </section>
  );
}

const TabCtx = createContext<{ aktif: string; set: (v: string) => void }>(null!);
export function Tabs({ awal, children }: { awal: string; children: ReactNode }) {
  const [aktif, set] = useState(awal);
  return <TabCtx.Provider value={{ aktif, set }}>{children}</TabCtx.Provider>;
}
Tabs.Tombol = ({ id, children }: { id: string; children: ReactNode }) => {
  const { aktif, set } = useContext(TabCtx);
  return <button role="tab" aria-selected={aktif === id} onClick={() => set(id)}>{children}</button>;
};
Tabs.Panel = ({ id, children }: { id: string; children: ReactNode }) =>
  useContext(TabCtx).aktif === id ? <div role="tabpanel">{children}</div> : null;

// Render props
export function Mouse({ render }: { render: (p: { x: number; y: number }) => ReactNode }) {
  const [p, setP] = useState({ x: 0, y: 0 });
  return <div onPointerMove={(e) => setP({ x: e.clientX, y: e.clientY })}>{render(p)}</div>;
}''')]),

'Portal, error boundary & suspense': dict(
  ist=[('Portal', 'createPortal merender anak ke node DOM lain (modal, toast) namun tetap di pohon React.'),
       ('Error boundary', 'Komponen kelas yang menangkap error render anak dan menampilkan fallback.'),
       ('Suspense', 'Menampilkan fallback saat anak menunggu kode (lazy) atau data.'),
       ('Code splitting', 'React.lazy(() => import(...)) memecah bundle agar halaman awal lebih ringan.')],
  cx=[R('Modal, error boundary, dan lazy loading', r'''
import { Component, lazy, Suspense, type ReactNode } from "react";
import { createPortal } from "react-dom";

export function Modal({ buka, tutup, children }: { buka: boolean; tutup: () => void; children: ReactNode }) {
  if (!buka) return null;
  return createPortal(
    <div className="latar" onClick={tutup}>
      <div role="dialog" aria-modal="true" onClick={(e) => e.stopPropagation()}>{children}</div>
    </div>,
    document.body,
  );
}

export class BatasError extends Component<{ fallback: ReactNode; children: ReactNode }, { error: Error | null }> {
  state = { error: null as Error | null };
  static getDerivedStateFromError(error: Error) { return { error }; }
  componentDidCatch(error: Error) { kirimKeSentry(error); }
  render() { return this.state.error ? this.props.fallback : this.props.children; }
}

const Grafik = lazy(() => import("./Grafik"));      // bundle terpisah

export function Dasbor() {
  return (
    <BatasError fallback={<p>Grafik gagal dimuat. <a href="">Muat ulang</a></p>}>
      <Suspense fallback={<div className="skeleton" style={{ height: 320 }} />}>
        <Grafik />
      </Suspense>
    </BatasError>
  );
}''')]),

'Memecah komponen: kapan & bagaimana': dict(
  ist=[('Single responsibility', 'Satu komponen satu tugas; mudah diuji dan dipakai ulang.'),
       ('Container vs presentational', 'Komponen pengambil data dipisah dari komponen tampilan murni.'),
       ('Colocation', 'Simpan state, gaya, dan tes sedekat mungkin dengan komponen yang memakainya.'),
       ('Feature folder', 'Struktur folder per fitur (features/checkout/...) alih-alih per jenis file.')],
  cx=[R('Dari satu komponen 300 baris menjadi bagian kecil', r'''
src/features/checkout/
├── CheckoutPage.tsx        // container: ambil data, susun bagian
├── components/
│   ├── RingkasanPesanan.tsx   // presentational: hanya props -> UI
│   ├── FormAlamat.tsx
│   └── PilihPembayaran.tsx
├── hooks/useCheckout.ts       // logika & state
├── api.ts                     // panggilan server
└── checkout.test.tsx

// CheckoutPage.tsx
export function CheckoutPage() {
  const { keranjang, alamat, setAlamat, bayar, status } = useCheckout();
  return (
    <main className="checkout">
      <FormAlamat nilai={alamat} onUbah={setAlamat} />
      <PilihPembayaran onPilih={bayar} memuat={status === "memproses"} />
      <RingkasanPesanan item={keranjang.item} />
    </main>
  );
}

// Tanda komponen perlu dipecah:
// - lebih dari ~150 baris atau beberapa useState yang tidak berhubungan
// - bagian JSX yang diberi komentar "// bagian X"
// - bagian yang render ulang terlalu sering padahal datanya jarang berubah''', lang='text')]),

'Input terkendali': dict(
  ist=[('Controlled component', 'Nilai input disimpan di state dan diubah lewat onChange.'),
       ('Uncontrolled component', 'Nilai dibaca dari DOM saat dibutuhkan (ref atau FormData).'),
       ('Form actions', 'React 19: <form action={fn}> dengan useActionState untuk status kirim.'),
       ('Inline validation', 'Pesan error muncul di dekat field saat blur atau submit.')],
  cx=[R('Form pendaftaran dengan validasi inline', r'''
import { useState, type FormEvent } from "react";

type Data = { nama: string; email: string; hp: string };
const aturan: Record<keyof Data, (v: string) => string | null> = {
  nama: (v) => (v.trim().length < 3 ? "Nama minimal 3 huruf" : null),
  email: (v) => (/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(v) ? null : "Format email belum benar"),
  hp: (v) => (/^(\+62|0)8\d{8,11}$/.test(v) ? null : "Nomor HP diawali 08 atau +628"),
};

export function FormDaftar() {
  const [data, setData] = useState<Data>({ nama: "", email: "", hp: "" });
  const [disentuh, setDisentuh] = useState<Partial<Record<keyof Data, boolean>>>({});
  const error = (k: keyof Data) => (disentuh[k] ? aturan[k](data[k]) : null);

  function kirim(e: FormEvent) {
    e.preventDefault();
    setDisentuh({ nama: true, email: true, hp: true });
    if (Object.keys(aturan).every((k) => !aturan[k as keyof Data](data[k as keyof Data]))) simpan(data);
  }
  return (
    <form onSubmit={kirim} noValidate>
      {(Object.keys(aturan) as (keyof Data)[]).map((k) => (
        <label key={k}>
          {k}
          <input value={data[k]} aria-invalid={!!error(k)} aria-describedby={`${k}-err`}
            onChange={(e) => setData({ ...data, [k]: e.target.value })}
            onBlur={() => setDisentuh({ ...disentuh, [k]: true })} />
          <small id={`${k}-err`} role="alert">{error(k)}</small>
        </label>
      ))}
      <button>Daftar</button>
    </form>
  );
}'''),
      T('Aturan validasi yang sama dijalankan', r'''
const aturan = {
  nama: (v: string) => (v.trim().length < 3 ? "Nama minimal 3 huruf" : null),
  email: (v: string) => (/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(v) ? null : "Format email belum benar"),
  hp: (v: string) => (/^(\+62|0)8\d{8,11}$/.test(v) ? null : "Nomor HP diawali 08 atau +628"),
};
const percobaan = [
  { nama: "Al", email: "al@contoh", hp: "021555" },
  { nama: "Alya", email: "alya@contoh.id", hp: "081234567890" },
];
for (const d of percobaan) {
  const err = Object.entries(aturan).map(([k, f]) => f(d[k as keyof typeof d])).filter(Boolean);
  console.log(d.nama.padEnd(5), err.length ? err.join("; ") : "valid, siap dikirim");
}
''')]),

'React Hook Form & Zod': dict(
  ist=[('React Hook Form', 'Pustaka form berbasis uncontrolled input; render ulang minimal.'),
       ('Zod', 'Pustaka skema validasi yang juga menghasilkan tipe TypeScript.'),
       ('zodResolver', 'Jembatan agar React Hook Form memakai skema Zod.'),
       ('Schema sharing', 'Skema yang sama dipakai di frontend dan backend agar aturan tidak berbeda.')],
  cx=[R('Form checkout dengan RHF + Zod', r'''
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

const skema = z.object({
  nama: z.string().min(3, "Nama minimal 3 huruf"),
  hp: z.string().regex(/^(\+62|0)8\d{8,11}$/, "Nomor HP tidak valid"),
  kodePos: z.string().regex(/^\d{5}$/, "Kode pos 5 digit"),
  kirim: z.enum(["reguler", "kilat"]),
  setujuData: z.literal(true, { errorMap: () => ({ message: "Wajib disetujui" }) }),
});
type Checkout = z.infer<typeof skema>;

export function FormCheckout() {
  const { register, handleSubmit, formState: { errors, isSubmitting } } =
    useForm<Checkout>({ resolver: zodResolver(skema), defaultValues: { kirim: "reguler" } });

  return (
    <form onSubmit={handleSubmit(async (d) => { await fetch("/api/checkout", { method: "POST", body: JSON.stringify(d) }); })}>
      <input {...register("nama")} placeholder="Nama penerima" />
      {errors.nama && <p role="alert">{errors.nama.message}</p>}
      <input {...register("hp")} inputMode="tel" placeholder="08..." />
      {errors.hp && <p role="alert">{errors.hp.message}</p>}
      <input {...register("kodePos")} inputMode="numeric" />
      <select {...register("kirim")}><option value="reguler">Reguler</option><option value="kilat">Kilat</option></select>
      <label><input type="checkbox" {...register("setujuData")} /> Saya setuju data dipakai untuk pengiriman</label>
      <button disabled={isSubmitting}>{isSubmitting ? "Memproses..." : "Bayar"}</button>
    </form>
  );
}''')]),

'React Router': dict(
  ist=[('Client-side routing', 'Berpindah halaman tanpa reload penuh; URL dikelola JavaScript.'),
       ('Nested route & Outlet', 'Layout induk merender anak di <Outlet />.'),
       ('Dynamic segment', '/produk/:id dibaca dengan useParams.'),
       ('Loader / action', 'React Router 7 (mode framework/data) memuat data sebelum halaman dirender.'),
       ('Protected route', 'Rute yang mengalihkan ke login bila belum masuk.')],
  cx=[R('Konfigurasi rute dengan layout dan rute terlindungi', r'''
import { createBrowserRouter, Navigate, Outlet, RouterProvider, useParams, Link } from "react-router";

function Layout() {
  return (
    <>
      <nav><Link to="/">Beranda</Link> <Link to="/produk/12">Produk</Link> <Link to="/akun">Akun</Link></nav>
      <main><Outlet /></main>
    </>
  );
}
function WajibLogin() {
  const user = useAuth();
  return user ? <Outlet /> : <Navigate to="/masuk" replace />;
}
function DetailProduk() {
  const { id } = useParams();
  return <h1>Produk #{id}</h1>;
}

const router = createBrowserRouter([
  { path: "/", element: <Layout />, errorElement: <Halaman404 />, children: [
    { index: true, element: <Beranda /> },
    { path: "produk/:id", element: <DetailProduk />, loader: ({ params }) => fetch(`/api/produk/${params.id}`) },
    { element: <WajibLogin />, children: [{ path: "akun", element: <Akun /> }] },
    { path: "masuk", element: <Masuk /> },
  ] },
]);
export default function App() { return <RouterProvider router={router} />; }'''),
      T('Cara router mencocokkan URL', r'''
function cocok(pola: string, url: string): Record<string, string> | null {
  const p = pola.split("/").filter(Boolean), u = url.split("?")[0].split("/").filter(Boolean);
  if (p.length !== u.length) return null;
  const param: Record<string, string> = {};
  for (let i = 0; i < p.length; i++) {
    if (p[i].startsWith(":")) param[p[i].slice(1)] = decodeURIComponent(u[i]);
    else if (p[i] !== u[i]) return null;
  }
  return param;
}
const rute = ["/", "/produk/:id", "/toko/:slug/produk/:id", "/akun"];
for (const url of ["/produk/12", "/toko/kopi-nusantara/produk/7?ref=ig", "/akun", "/blog/1"]) {
  const r = rute.map((p) => [p, cocok(p, url)] as const).find(([, m]) => m);
  console.log(url.padEnd(38), r ? `${r[0]} ${JSON.stringify(r[1])}` : "404 Tidak ditemukan");
}
''')]),

'Zustand, Jotai & kawan-kawan': dict(
  ist=[('Global state', 'State yang dibutuhkan banyak komponen jauh: user, keranjang, tema.'),
       ('Zustand', 'Store kecil berbasis hook; populer karena tanpa boilerplate.'),
       ('Jotai', 'State atomik: potongan kecil (atom) yang bisa digabung.'),
       ('Redux Toolkit', 'Standar lama perusahaan besar; cocok untuk tim besar dengan devtools ketat.'),
       ('Selector', 'Memilih sebagian store agar komponen hanya render saat bagian itu berubah.')],
  cx=[R('Store keranjang dengan Zustand dan persist', r'''
import { create } from "zustand";
import { persist } from "zustand/middleware";

type Item = { sku: string; nama: string; harga: number; qty: number };
type KeranjangStore = {
  item: Item[];
  tambah: (i: Omit<Item, "qty">) => void;
  hapus: (sku: string) => void;
  total: () => number;
};

export const useKeranjang = create<KeranjangStore>()(
  persist(
    (set, get) => ({
      item: [],
      tambah: (i) => set((s) => {
        const ada = s.item.find((x) => x.sku === i.sku);
        return { item: ada ? s.item.map((x) => (x.sku === i.sku ? { ...x, qty: x.qty + 1 } : x)) : [...s.item, { ...i, qty: 1 }] };
      }),
      hapus: (sku) => set((s) => ({ item: s.item.filter((x) => x.sku !== sku) })),
      total: () => get().item.reduce((t, x) => t + x.harga * x.qty, 0),
    }),
    { name: "keranjang" },        // disimpan di localStorage
  ),
);

// Komponen hanya render ulang saat jumlah item berubah (selector)
const jumlah = useKeranjang((s) => s.item.length);'''),
      T('Store mini dengan langganan dan selector', r'''
function createStore<S>(awal: S) {
  let state = awal; const pendengar = new Set<() => void>();
  return {
    get: () => state,
    set: (f: (s: S) => Partial<S>) => { state = { ...state, ...f(state) }; pendengar.forEach((l) => l()); },
    subscribe<T>(pilih: (s: S) => T, cb: (v: T) => void) {
      let lama = pilih(state);
      const l = () => { const baru = pilih(state); if (!Object.is(baru, lama)) { lama = baru; cb(baru); } };
      pendengar.add(l); return () => pendengar.delete(l);
    },
  };
}
const store = createStore({ user: "tamu", item: [] as string[], tema: "terang" });
store.subscribe((s) => s.item.length, (n) => console.log("[Badge] render, jumlah =", n));
store.subscribe((s) => s.tema, (t) => console.log("[Header] render, tema =", t));
store.set((s) => ({ item: [...s.item, "Kopi"] }));
store.set(() => ({ user: "rina" }));                  // tidak ada yang render ulang
store.set(() => ({ tema: "gelap" }));
store.set((s) => ({ item: [...s.item, "Teh"] }));
''')]),

'Fetch di komponen': dict(
  ist=[('Race condition', 'Respons lama datang setelah respons baru dan menimpanya.'),
       ('AbortController', 'Membatalkan fetch saat komponen unmount atau parameter berubah.'),
       ('Waterfall', 'Request berurutan yang seharusnya paralel; memperlambat halaman.'),
       ('use()', 'API React 19 untuk membaca Promise di dalam Suspense.')],
  cx=[R('Fetch dengan pembatalan dan status', r'''
import { useEffect, useState } from "react";

export function Profil({ id }: { id: number }) {
  const [state, setState] = useState<{ data?: User; error?: string; memuat: boolean }>({ memuat: true });

  useEffect(() => {
    const ctrl = new AbortController();
    setState({ memuat: true });
    fetch(`/api/user/${id}`, { signal: ctrl.signal })
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`))))
      .then((data) => setState({ data, memuat: false }))
      .catch((e) => { if (e.name !== "AbortError") setState({ error: e.message, memuat: false }); });
    return () => ctrl.abort();                  // id berubah -> request lama dibatalkan
  }, [id]);

  if (state.memuat) return <p>Memuat...</p>;
  if (state.error) return <p role="alert">Gagal: {state.error}</p>;
  return <h2>{state.data!.nama}</h2>;
}'''),
      T('Race condition dan cara AbortController mencegahnya', r'''
const tunda = (ms: number, signal?: AbortSignal) => new Promise<void>((ok, gagal) => {
  const t = setTimeout(ok, ms);
  signal?.addEventListener("abort", () => { clearTimeout(t); gagal(new Error("AbortError")); });
});
async function fetchUser(id: number, signal?: AbortSignal) {
  await tunda(id === 1 ? 120 : 30, signal);       // user 1 lambat, user 2 cepat
  return `User ${id}`;
}
async function tanpaAbort() {
  let tampil = "";
  const p1 = fetchUser(1).then((u) => (tampil = u));
  const p2 = fetchUser(2).then((u) => (tampil = u));   // pengguna sudah pindah ke user 2
  await Promise.all([p1, p2]);
  console.log("tanpa abort  -> tampil:", tampil, "(salah)");
}
async function denganAbort() {
  let tampil = ""; const c1 = new AbortController();
  const p1 = fetchUser(1, c1.signal).then((u) => (tampil = u)).catch(() => {});
  c1.abort();                                           // cleanup effect saat id berubah
  await Promise.all([p1, fetchUser(2).then((u) => (tampil = u))]);
  console.log("dengan abort -> tampil:", tampil);
}
await tanpaAbort(); await denganAbort();
''')]),

'TanStack Query, SWR & GraphQL': dict(
  ist=[('Server state', 'Data milik server yang di-cache di klien; berbeda dari UI state.'),
       ('Stale-while-revalidate', 'Tampilkan cache dulu, ambil ulang di belakang layar.'),
       ('Query key', 'Identitas cache, misalnya ["produk", id].'),
       ('Mutation & invalidation', 'Setelah data diubah, query terkait ditandai basi dan diambil ulang.'),
       ('Optimistic update', 'UI diubah sebelum server menjawab, dibatalkan jika gagal.')],
  cx=[R('Daftar produk dan mutasi dengan TanStack Query v5', r'''
import { QueryClient, QueryClientProvider, useMutation, useQuery, useQueryClient } from "@tanstack/react-query";

const qc = new QueryClient({ defaultOptions: { queries: { staleTime: 60_000, retry: 2 } } });

function useProduk(kategori: string) {
  return useQuery({
    queryKey: ["produk", kategori],
    queryFn: ({ signal }) => fetch(`/api/produk?kat=${kategori}`, { signal }).then((r) => r.json()),
  });
}
function useTambahFavorit() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => fetch(`/api/favorit/${id}`, { method: "POST" }),
    onMutate: async (id) => {                       // optimistic update
      await qc.cancelQueries({ queryKey: ["favorit"] });
      const lama = qc.getQueryData<number[]>(["favorit"]);
      qc.setQueryData<number[]>(["favorit"], (f = []) => [...f, id]);
      return { lama };
    },
    onError: (_e, _id, ctx) => qc.setQueryData(["favorit"], ctx?.lama),
    onSettled: () => qc.invalidateQueries({ queryKey: ["favorit"] }),
  });
}
function Katalog() {
  const { data, isPending, isError, refetch } = useProduk("kopi");
  const fav = useTambahFavorit();
  if (isPending) return <Skeleton />;
  if (isError) return <button onClick={() => refetch()}>Coba lagi</button>;
  return data.map((p: { id: number; nama: string }) => <button key={p.id} onClick={() => fav.mutate(p.id)}>♡ {p.nama}</button>);
}''')]),

'Empat keadaan data: memuat, error, kosong, ada': dict(
  ist=[('Loading state', 'Skeleton atau spinner; skeleton mengurangi layout shift (CLS).'),
       ('Error state', 'Pesan yang menjelaskan masalah dan tombol coba lagi.'),
       ('Empty state', 'Tampilan saat data kosong, dengan ajakan bertindak.'),
       ('Success state', 'Data tampil; perhatikan juga data parsial dan sangat panjang.')],
  cx=[R('Komponen yang menangani keempat keadaan', r'''
type Q<T> = { isPending: boolean; isError: boolean; error?: Error; data?: T[]; refetch: () => void };

export function DaftarPesanan({ q }: { q: Q<Pesanan> }) {
  if (q.isPending) return <ul aria-busy="true">{Array.from({ length: 4 }, (_, i) => <li key={i} className="skeleton h-16" />)}</ul>;
  if (q.isError) return (
    <div role="alert" className="error">
      <p>Pesanan gagal dimuat. Periksa koneksi lalu coba lagi.</p>
      <button onClick={q.refetch}>Coba lagi</button>
    </div>
  );
  if (!q.data?.length) return (
    <div className="kosong">
      <img src="/ilustrasi/kosong.svg" alt="" />
      <p>Belum ada pesanan.</p>
      <a href="/produk" className="btn">Mulai belanja</a>
    </div>
  );
  return <ul>{q.data.map((p) => <BarisPesanan key={p.id} p={p} />)}</ul>;
}'''),
      T('Tabel keputusan tampilan', r'''
type Q = { isPending: boolean; isError: boolean; data?: unknown[] };
const pilihTampilan = (q: Q) =>
  q.isPending ? "skeleton" : q.isError ? "pesan error + Coba lagi" : !q.data?.length ? "empty state + CTA" : `daftar ${q.data.length} item`;
const kasus: [string, Q][] = [
  ["pertama dibuka", { isPending: true, isError: false }],
  ["server 500", { isPending: false, isError: true }],
  ["pengguna baru", { isPending: false, isError: false, data: [] }],
  ["pengguna lama", { isPending: false, isError: false, data: [1, 2, 3] }],
];
for (const [n, q] of kasus) console.log(n.padEnd(15), "->", pilihTampilan(q));
''')]),

'Menata komponen': dict(
  ist=[('CSS Modules', 'File .module.css dengan nama kelas yang otomatis unik per komponen.'),
       ('Tailwind CSS', 'Kelas utilitas langsung di JSX; standar banyak tim 2026.'),
       ('CSS-in-JS', 'styled-components/Emotion; berkurang popularitasnya karena biaya runtime di RSC.'),
       ('cva / clsx', 'Utilitas untuk menyusun kelas berdasarkan varian dan kondisi.')],
  cx=[R('Varian tombol dengan cva + Tailwind', r'''
import { cva, type VariantProps } from "class-variance-authority";
import clsx from "clsx";

const tombol = cva("inline-flex items-center gap-2 rounded-lg font-medium focus-visible:outline-2", {
  variants: {
    varian: { utama: "bg-emerald-600 text-white hover:bg-emerald-700", garis: "border border-slate-300 hover:bg-slate-50" },
    ukuran: { sm: "h-8 px-3 text-sm", md: "h-10 px-4", lg: "h-12 px-6 text-lg" },
  },
  defaultVariants: { varian: "utama", ukuran: "md" },
});

type Props = React.ComponentProps<"button"> & VariantProps<typeof tombol>;
export const Tombol = ({ varian, ukuran, className, ...p }: Props) =>
  <button className={clsx(tombol({ varian, ukuran }), className)} {...p} />;

/* CSS Modules: Kartu.module.css -> .kartu { ... } menjadi Kartu_kartu__x7a2 */
import s from "./Kartu.module.css";
export const Kartu = ({ aktif }: { aktif: boolean }) => <div className={clsx(s.kartu, aktif && s.aktif)} />;'''),
      T('Cara clsx menyusun nama kelas', r'''
type Nilai = string | false | null | undefined | Record<string, boolean>;
const clsx = (...a: Nilai[]) => a.flatMap((x) => (!x ? [] : typeof x === "string" ? [x] : Object.keys(x).filter((k) => x[k]))).join(" ");
const aktif = true, nonaktif = false, ukuran = "lg";
console.log(clsx("btn", aktif && "btn-aktif", nonaktif && "opacity-50", { [`btn-${ukuran}`]: true, "w-full": false }));
''')]),

'Pustaka komponen & animasi': dict(
  ist=[('Headless UI', 'Komponen tanpa gaya yang menangani perilaku dan aksesibilitas (Radix, React Aria).'),
       ('shadcn/ui', 'Komponen yang disalin ke proyek sendiri, berbasis Radix + Tailwind.'),
       ('MUI / Mantine / Ant Design', 'Pustaka komponen lengkap dengan gaya bawaan, cocok untuk dasbor.'),
       ('Motion (Framer Motion)', 'Pustaka animasi deklaratif; hormati prefers-reduced-motion.')],
  cx=[R('Dialog shadcn/ui dan animasi daftar dengan Motion', r'''
// npx shadcn@latest add dialog button
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { AnimatePresence, motion, useReducedMotion } from "motion/react";

export function HapusAlamat({ onHapus }: { onHapus: () => void }) {
  return (
    <Dialog>
      <DialogTrigger asChild><Button variant="destructive">Hapus alamat</Button></DialogTrigger>
      <DialogContent>
        <DialogHeader><DialogTitle>Hapus alamat ini?</DialogTitle></DialogHeader>
        <p>Alamat tidak bisa dikembalikan setelah dihapus.</p>
        <Button variant="destructive" onClick={onHapus}>Ya, hapus</Button>
      </DialogContent>
    </Dialog>
  );
}

export function Notifikasi({ daftar }: { daftar: { id: string; teks: string }[] }) {
  const kurangi = useReducedMotion();
  return (
    <AnimatePresence>
      {daftar.map((n) => (
        <motion.li key={n.id} layout
          initial={{ opacity: 0, y: kurangi ? 0 : -12 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}>{n.teks}</motion.li>
      ))}
    </AnimatePresence>
  );
}''')]),

'Menguji komponen': dict(
  ist=[('Vitest', 'Test runner cepat yang kompatibel dengan Vite; pengganti Jest di banyak proyek.'),
       ('React Testing Library', 'Menguji seperti pengguna: cari elemen berdasarkan role dan teks.'),
       ('user-event', 'Simulasi interaksi realistis (ketik, klik, tab).'),
       ('MSW', 'Mock Service Worker: memalsukan API di level jaringan.'),
       ('Playwright', 'Tes end-to-end di browser sungguhan.')],
  cx=[R('Tes komponen PilihJumlah dan form', r'''
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

describe("PilihJumlah", () => {
  it("tidak melebihi stok", async () => {
    const user = userEvent.setup();
    render(<PilihJumlah stok={2} />);
    await user.click(screen.getByRole("button", { name: "Tambah" }));
    expect(screen.getByRole("status")).toHaveTextContent("2");
    expect(screen.getByRole("button", { name: "Tambah" })).toBeDisabled();
  });
});

describe("FormDaftar", () => {
  it("menampilkan error lalu mengirim data valid", async () => {
    const user = userEvent.setup(); const simpan = vi.fn();
    render(<FormDaftar onSimpan={simpan} />);
    await user.click(screen.getByRole("button", { name: "Daftar" }));
    expect(await screen.findByText("Nama minimal 3 huruf")).toBeVisible();
    await user.type(screen.getByLabelText("nama"), "Alya");
    await user.type(screen.getByLabelText("email"), "alya@contoh.id");
    await user.type(screen.getByLabelText("hp"), "081234567890");
    await user.click(screen.getByRole("button", { name: "Daftar" }));
    expect(simpan).toHaveBeenCalledWith({ nama: "Alya", email: "alya@contoh.id", hp: "081234567890" });
  });
});'''),
      T('Tes unit untuk logika murni (tanpa DOM)', r'''
import assert from "node:assert/strict";
// pola describe/it/test yang sama dipakai Vitest; di sini runner mini agar keluaran ringkas
const test = (nama: string, fn: () => void) => {
  try { fn(); console.log("✓", nama); } catch (e) { console.log("✗", nama, "-", (e as Error).message.replace(/\s+/g, " ")); }
};

const subtotal = (item: { harga: number; qty: number }[]) => item.reduce((t, i) => t + i.harga * i.qty, 0);
const ongkir = (berat: number, kilat: boolean) => Math.ceil(berat) * (kilat ? 18000 : 9000);

test("subtotal keranjang", () => assert.equal(subtotal([{ harga: 45000, qty: 2 }, { harga: 28000, qty: 1 }]), 118000));
test("keranjang kosong = 0", () => assert.equal(subtotal([]), 0));
test("ongkir dibulatkan ke atas per kg", () => assert.equal(ongkir(1.2, false), 18000));
test("ongkir kilat dua kali lipat", () => assert.equal(ongkir(1, true), 18000));
test("contoh tes yang gagal", () => assert.equal(ongkir(2.01, false), 18000));
''')]),

'Next.js, React Native & TypeScript': dict(
  ist=[('Next.js', 'Framework React untuk web: routing berbasis file, SSR/SSG, Server Components.'),
       ('React Native / Expo', 'Membuat aplikasi Android dan iOS dengan React.'),
       ('React Server Components', 'Komponen yang berjalan hanya di server; tidak menambah JavaScript ke klien.'),
       ('Vite', 'Alat build untuk SPA React; titik awal paling umum di luar Next.js.')],
  cx=[R('Komponen yang sama di tiga lingkungan', r'''
// 1) Vite SPA (web, render di browser)
export function Sapa({ nama }: { nama: string }) {
  return <h1 className="text-2xl">Halo, {nama}</h1>;
}

// 2) Next.js App Router: Server Component (async, akses DB langsung)
export default async function Halaman({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const user = await db.user.findUnique({ where: { id } });
  return <Sapa nama={user?.nama ?? "tamu"} />;
}

// 3) React Native / Expo: elemen native, bukan HTML
import { Text, View, Pressable } from "react-native";
export function SapaMobile({ nama }: { nama: string }) {
  return (
    <View style={{ padding: 16 }}>
      <Text style={{ fontSize: 24 }}>Halo, {nama}</Text>
      <Pressable onPress={() => alert("Hai!")}><Text>Sapa balik</Text></Pressable>
    </View>
  );
}''')]),

'Toko online mini': dict(
  ist=[('MVP', 'Minimum Viable Product: fitur inti yang cukup untuk diuji pengguna.'),
       ('Feature-based structure', 'Folder per fitur: katalog, keranjang, checkout.'),
       ('Persisted cart', 'Keranjang tersimpan walau halaman dimuat ulang.'),
       ('Lighthouse', 'Audit performa, aksesibilitas, dan SEO; target skor 90+.')],
  cx=[R('Kerangka aplikasi toko', r'''
src/
├── main.tsx                 // QueryClientProvider + RouterProvider
├── routes.tsx               // /, /produk/:id, /keranjang, /checkout
├── features/
│   ├── katalog/  (DaftarProduk, KartuProduk, useProduk)
│   ├── keranjang/ (store.ts Zustand+persist, IkonKeranjang, HalamanKeranjang)
│   └── checkout/ (FormCheckout RHF+Zod, RingkasanPesanan)
└── shared/ (Tombol, Modal, format.ts)

// features/katalog/DaftarProduk.tsx
export function DaftarProduk() {
  const [q, setQ] = useState("");
  const qTunda = useDeferredValue(q);
  const { data = [], isPending, isError, refetch } = useProduk();
  const tampil = useMemo(() => data.filter((p) => p.nama.toLowerCase().includes(qTunda.toLowerCase())), [data, qTunda]);
  const tambah = useKeranjang((s) => s.tambah);

  if (isPending) return <GridSkeleton />;
  if (isError) return <Gagal onCoba={refetch} />;
  return (
    <>
      <input type="search" value={q} onChange={(e) => setQ(e.target.value)} aria-label="Cari produk" />
      {tampil.length === 0 ? <p>Produk "{q}" tidak ditemukan.</p> : (
        <ul className="grid">{tampil.map((p) => <KartuProduk key={p.id} {...p} onTambah={() => tambah(p)} />)}</ul>
      )}
    </>
  );
}''', lang='tsx'),
      T('Logika inti toko diuji di Node', r'''
type Produk = { id: number; nama: string; harga: number; kategori: string };
const katalog: Produk[] = [
  { id: 1, nama: "Kopi Gayo 250g", harga: 65000, kategori: "kopi" },
  { id: 2, nama: "Kopi Toraja 250g", harga: 72000, kategori: "kopi" },
  { id: 3, nama: "Teh Melati", harga: 18000, kategori: "teh" },
  { id: 4, nama: "French Press", harga: 185000, kategori: "alat" },
];
const cari = (q: string, kat?: string) =>
  katalog.filter((p) => p.nama.toLowerCase().includes(q.toLowerCase()) && (!kat || p.kategori === kat));
const urut = (d: Produk[], by: "termurah" | "termahal") => [...d].sort((a, b) => (by === "termurah" ? a.harga - b.harga : b.harga - a.harga));

type Item = Produk & { qty: number };
let keranjang: Item[] = [];
const tambah = (p: Produk) => {
  keranjang = keranjang.some((i) => i.id === p.id) ? keranjang.map((i) => (i.id === p.id ? { ...i, qty: i.qty + 1 } : i)) : [...keranjang, { ...p, qty: 1 }];
};
const rp = (n: number) => "Rp" + n.toLocaleString("id-ID");

console.log("cari 'kopi' termahal:", urut(cari("kopi"), "termahal").map((p) => p.nama).join(", "));
tambah(katalog[0]); tambah(katalog[0]); tambah(katalog[3]);
const sub = keranjang.reduce((t, i) => t + i.harga * i.qty, 0);
const ongkir = sub >= 200000 ? 0 : 15000;
keranjang.forEach((i) => console.log(`${i.nama.padEnd(16)} x${i.qty} ${rp(i.harga * i.qty).padStart(11)}`));
console.log(`Subtotal ${rp(sub)} | Ongkir ${ongkir ? rp(ongkir) : "GRATIS"} | Total ${rp(sub + ongkir)}`);
''')]),
}
