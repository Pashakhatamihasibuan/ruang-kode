/* ===================== JALUR REACT =====================
   Mengikuti roadmap.sh/react. Pelajaran w dengan react:true menjalankan JSX di pratinjau
   (React 18 + Babel dari jsDelivr). Kode cukup mendefinisikan function App(). */
const REACT_MODULES=[
{t:'Dasar React',lvl:'Pemula',d:'Komponen, JSX, props, state, event, percabangan, dan daftar.',
 nodes:['Components','Functional Components','JSX','Props vs State','Events','Conditional Rendering','Lists and Keys','Rendering','CLI Tools','Vite'],
 lessons:[
  {k:'w',t:'Komponen & JSX',react:true,nodes:['Components','Functional Components','JSX','CLI Tools','Vite'],
   b:['React membangun antarmuka dari <b>komponen</b>: fungsi yang mengembalikan tampilan. Nama komponen diawali huruf kapital, misalnya <code>KartuProduk</code>, dan dipakai seperti tag HTML: <code>&lt;KartuProduk /&gt;</code>.',
      'Tampilan ditulis dengan <b>JSX</b>, sintaks mirip HTML di dalam JavaScript. Perbedaannya: <code>className</code> pengganti class, <code>htmlFor</code> pengganti for, setiap tag harus ditutup, dan ekspresi JavaScript ditulis di dalam <code>{ }</code>. Satu komponen harus mengembalikan satu elemen induk, atau fragment <code>&lt;&gt;...&lt;/&gt;</code>.',
      'Proyek nyata biasanya dibuat dengan <code>npm create vite@latest</code>. Di sini, pratinjau langsung menjalankan komponen <code>App</code>.'],
   js:`function KartuProduk() {
  const nama = "Kopi Gayo";
  const harga = 85000;
  return (
    <div className="kartu">
      <h3>{nama}</h3>
      <p>Rp{harga.toLocaleString("id-ID")}</p>
    </div>
  );
}

function App() {
  return (
    <>
      <h2>Produk pilihan</h2>
      <KartuProduk />
      <KartuProduk />
    </>
  );
}`,
   css:`body{font:14px system-ui,sans-serif}.kartu{border:1px solid #ddd;border-radius:10px;padding:8px 12px;margin:6px 0}`,
   task:{q:'Tampilkan <b>tiga</b> kartu produk.',test:`document.querySelectorAll('.kartu').length>=3`,hint:'Tambahkan satu <KartuProduk /> lagi di App.'},
   pts:['Komponen = fungsi yang mengembalikan JSX.','Nama komponen diawali huruf kapital.','className, htmlFor, dan tag tertutup di JSX.','{ } untuk ekspresi JavaScript.'],
   q:[['Atribut class di JSX ditulis?',['className','class','cssClass'],0,'class adalah kata kunci di JavaScript.'],
      ['Kenapa nama komponen harus kapital?',['Agar dibedakan dari tag HTML biasa','Aturan gaya saja','Agar lebih cepat'],0,'<kartu> dianggap tag HTML, <Kartu> dianggap komponen.']]},
  {k:'w',t:'Props',react:true,nodes:['Props vs State','Components'],
   b:['<b>Props</b> adalah data yang dikirim dari komponen induk ke anak, seperti argumen fungsi: <code>&lt;KartuProduk nama="Teh" harga={25000} /&gt;</code>. Anak menerimanya sebagai objek; biasanya langsung di-destructure: <code>function KartuProduk({ nama, harga })</code>.',
      'Props bersifat <b>hanya-baca</b>: anak tidak boleh mengubahnya. Prop khusus <code>children</code> berisi apa pun yang ditulis di antara tag pembuka dan penutup, sehingga komponen bisa membungkus komponen lain.'],
   js:`function KartuProduk({ nama, harga, promo = false }) {
  return (
    <div className={"kartu" + (promo ? " promo" : "")}>
      <h3>{nama}</h3>
      <p>Rp{harga.toLocaleString("id-ID")}</p>
    </div>
  );
}

function Bingkai({ judul, children }) {
  return <section><h2>{judul}</h2>{children}</section>;
}

function App() {
  return (
    <Bingkai judul="Katalog">
      <KartuProduk nama="Kopi Gayo" harga={85000} promo />
      <KartuProduk nama="Teh Melati" harga={25000} />
    </Bingkai>
  );
}`,
   css:`body{font:14px system-ui,sans-serif}.kartu{border:1px solid #ddd;border-radius:10px;padding:8px 12px;margin:6px 0}.promo{border-color:#B4532A;background:#F6ECE5}`,
   task:{q:'Tambahkan kartu "Madu Hutan" seharga 120000 dengan prop promo.',test:`[...document.querySelectorAll('.kartu.promo')].some(k=>/Madu/.test(k.textContent))`,hint:'<KartuProduk nama="Madu Hutan" harga={120000} promo />'},
   pts:['Props dikirim dari induk ke anak.','Props hanya-baca.','Angka dan ekspresi ditulis di { }, teks boleh pakai tanda kutip.','children untuk membungkus isi.'],
   q:[['Bolehkah anak mengubah props?',['Tidak, props hanya-baca','Boleh kapan saja','Hanya angka'],0,'Data mengalir satu arah dari atas ke bawah.']]},
  {k:'w',t:'State dengan useState',react:true,nodes:['useState Hook','Props vs State','Rendering'],viz:'reactstate',
   b:['<b>State</b> adalah data milik komponen yang bisa berubah, misalnya jumlah barang di keranjang. <code>const [jumlah, setJumlah] = useState(0)</code> memberi nilai sekarang dan fungsi untuk menggantinya.',
      'Saat setter dipanggil, React <b>me-render ulang</b> komponen dengan nilai baru. Jangan mengubah state langsung (<code>jumlah++</code>), selalu lewat setter. Jika nilai baru bergantung pada nilai lama, pakai bentuk fungsi: <code>setJumlah(j =&gt; j + 1)</code>.',
      'Untuk array dan objek, buat salinan baru: <code>setDaftar([...daftar, item])</code>, bukan <code>daftar.push(item)</code>.'],
   js:`function Penghitung() {
  const [jumlah, setJumlah] = useState(0);
  return (
    <div className="kartu">
      <p>Kopi Gayo di keranjang: <b>{jumlah}</b></p>
      <button onClick={() => setJumlah(j => Math.max(0, j - 1))}>−</button>
      <button onClick={() => setJumlah(j => j + 1)}>+</button>
      <p>Subtotal: Rp{(jumlah * 85000).toLocaleString("id-ID")}</p>
    </div>
  );
}

function App() {
  return <Penghitung />;
}`,
   css:`body{font:14px system-ui,sans-serif}.kartu{border:1px solid #ddd;border-radius:10px;padding:8px 12px}button{width:32px;height:32px;margin-right:6px}`,
   task:{q:'Klik tombol + sampai jumlahnya 3.',test:`/di keranjang: 3/.test(document.body.textContent)`,hint:'Tekan + tiga kali di pratinjau.'},
   pts:['useState mengembalikan [nilai, setter].','Memanggil setter memicu render ulang.','Pakai setter berbentuk fungsi bila bergantung nilai lama.','Jangan mutasi array/objek state; buat salinan.'],
   q:[['Kenapa jumlah++ tidak memperbarui tampilan?',['React tidak tahu ada perubahan tanpa setter','jumlah const sehingga error saja','Karena butuh useEffect'],0,'Hanya setter yang menjadwalkan render ulang.']]},
  {k:'w',t:'Event, percabangan & daftar',react:true,nodes:['Events','Conditional Rendering','Lists and Keys'],
   b:['Event di React ditulis camelCase: <code>onClick</code>, <code>onChange</code>, <code>onSubmit</code>, dan diberi fungsi, bukan pemanggilan fungsi: <code>onClick={hapus}</code>, bukan <code>onClick={hapus()}</code>.',
      'Percabangan memakai JavaScript biasa: <code>{stok &gt; 0 ? &lt;Beli /&gt; : &lt;Habis /&gt;}</code> atau <code>{promo &amp;&amp; &lt;Badge /&gt;}</code>. Hati-hati: <code>{0 &amp;&amp; ...}</code> menampilkan angka 0.',
      'Daftar dibuat dengan <code>map</code>. Setiap elemen wajib punya <code>key</code> unik dan stabil, biasanya id dari data. Jangan pakai indeks array jika urutan bisa berubah.'],
   js:`const PRODUK = [
  { id: 1, nama: "Kopi Gayo", stok: 40 },
  { id: 7, nama: "Rendang Kaleng", stok: 0 },
  { id: 2, nama: "Teh Melati", stok: 120 },
];

function App() {
  const [hanyaAda, setHanyaAda] = useState(false);
  const daftar = hanyaAda ? PRODUK.filter(p => p.stok > 0) : PRODUK;
  return (
    <div>
      <label>
        <input type="checkbox" checked={hanyaAda} onChange={e => setHanyaAda(e.target.checked)} />
        {" "}Hanya yang tersedia
      </label>
      <ul>
        {daftar.map(p => (
          <li key={p.id}>
            {p.nama} {p.stok > 0 ? <span className="ok">tersedia</span> : <span className="habis">habis</span>}
          </li>
        ))}
      </ul>
    </div>
  );
}`,
   css:`body{font:14px system-ui,sans-serif}.ok{color:#2F7A52}.habis{color:#B23A2E}`,
   task:{q:'Centang "Hanya yang tersedia" sehingga produk habis tidak tampil.',test:`!/Rendang/.test(document.querySelector('ul').textContent)`,hint:'Klik kotak centang di pratinjau.'},
   pts:['Event camelCase, berisi fungsi.','Percabangan dengan ternary atau &&.','Daftar dengan map dan key unik yang stabil.'],
   q:[['Prop key sebaiknya berisi?',['id unik dari data','Indeks array selalu','Math.random()'],0,'key membantu React mengenali elemen antar-render.']]}
 ]},
{t:'Hooks',lvl:'Menengah',d:'Efek samping, referensi, memo, reducer, context, dan hook buatan sendiri.',
 nodes:['Hooks','useEffect Hook','useRef','useMemo','useCallback','useReducer','useContext','Context','Writing Custom Hooks','Hooks Best Practices','Component Life Cycle'],
 lessons:[
  {k:'w',t:'useEffect & siklus hidup',react:true,nodes:['useEffect Hook','Component Life Cycle'],
   b:['<code>useEffect</code> menjalankan <b>efek samping</b> setelah render: mengambil data, memasang timer, atau berlangganan event. Array dependensi menentukan kapan efek dijalankan ulang: <code>[]</code> hanya sekali saat komponen muncul, <code>[id]</code> setiap kali id berubah.',
      'Kembalikan fungsi <b>cleanup</b> untuk membersihkan, misalnya mematikan timer saat komponen hilang. Ini pengganti siklus hidup componentDidMount/Unmount di komponen kelas.',
      'Jangan pakai useEffect untuk menghitung nilai turunan dari state; hitung saja langsung saat render.'],
   js:`function Jam() {
  const [detik, setDetik] = useState(0);
  useEffect(() => {
    const t = setInterval(() => setDetik(d => d + 1), 1000);
    return () => clearInterval(t);        // cleanup
  }, []);                                  // sekali saat muncul
  return <p>Sudah belajar {detik} detik</p>;
}

function App() {
  const [tampil, setTampil] = useState(true);
  useEffect(() => { document.title = tampil ? "Fokus" : "Istirahat"; }, [tampil]);
  return (
    <div>
      <button onClick={() => setTampil(t => !t)}>{tampil ? "Istirahat" : "Mulai lagi"}</button>
      {tampil && <Jam />}
    </div>
  );
}`,
   pts:['useEffect untuk efek samping setelah render.','[] sekali, [x] setiap x berubah, tanpa array setiap render.','Kembalikan cleanup untuk timer dan langganan.','Nilai turunan dihitung saat render, bukan lewat efek.'],
   q:[['useEffect(fn, []) dijalankan?',['Sekali setelah render pertama','Setiap render','Tidak pernah'],0,'Dependensi kosong berarti tidak ada yang ditunggu berubah.']]},
  {k:'w',t:'useRef, useMemo & useCallback',react:true,nodes:['useRef','useMemo','useCallback','Refs','Hooks Best Practices'],
   b:['<code>useRef</code> menyimpan nilai yang bertahan antar-render <b>tanpa</b> memicu render ulang, dan sering dipakai untuk menunjuk elemen DOM, misalnya memfokuskan input.',
      '<code>useMemo</code> mengingat hasil perhitungan berat dan menghitung ulang hanya saat dependensinya berubah. <code>useCallback</code> mengingat fungsi agar identitasnya tetap sama. Keduanya alat optimasi: pakai saat ada masalah performa yang terukur, bukan di semua tempat.',
      'Aturan hooks: panggil hanya di tingkat atas komponen (tidak di dalam if atau loop), dan hanya dari komponen atau hook lain.'],
   js:`function App() {
  const inputRef = useRef(null);
  const [cari, setCari] = useState("");
  const [klik, setKlik] = useState(0);

  const angka = useMemo(() => {
    // anggap ini perhitungan berat
    return Array.from({ length: 2000 }, (_, i) => i).filter(n => String(n).includes(cari || "x"));
  }, [cari]);

  return (
    <div>
      <input ref={inputRef} value={cari} onChange={e => setCari(e.target.value)} placeholder="Cari angka" />
      <button onClick={() => inputRef.current.focus()}>Fokus ke input</button>
      <p>{angka.length} angka cocok</p>
      <button onClick={() => setKlik(k => k + 1)}>Klik {klik}</button>
      <p><small>Klik tombol tidak menghitung ulang daftar angka karena useMemo.</small></p>
    </div>
  );
}`,
   pts:['useRef: nilai bertahan tanpa render ulang; akses DOM.','useMemo mengingat hasil, useCallback mengingat fungsi.','Optimasi hanya bila perlu.','Hooks dipanggil di tingkat atas komponen.'],
   q:[['Mengubah ref.current memicu render ulang?',['Tidak','Ya','Hanya untuk angka'],0,'Itu bedanya ref dengan state.']]},
  {k:'w',t:'useReducer & Context',react:true,nodes:['useReducer','useContext','Context'],
   b:['Saat state rumit dengan banyak jenis perubahan, <code>useReducer</code> mengumpulkan semua logika di satu fungsi <b>reducer</b>: <code>(state, aksi) =&gt; stateBaru</code>. Komponen cukup mengirim aksi: <code>dispatch({ type: "tambah", id })</code>.',
      '<b>Context</b> mengirim data ke banyak komponen jauh di bawah tanpa meneruskan props berlapis-lapis (prop drilling). Buat dengan <code>createContext</code>, sediakan dengan <code>&lt;Ctx.Provider value={...}&gt;</code>, baca dengan <code>useContext(Ctx)</code>. Cocok untuk tema, bahasa, atau pengguna yang login.'],
   js:`const KeranjangCtx = React.createContext(null);

function reducer(state, aksi) {
  switch (aksi.type) {
    case "tambah": return { ...state, [aksi.nama]: (state[aksi.nama] || 0) + 1 };
    case "kosongkan": return {};
    default: return state;
  }
}

function TombolBeli({ nama }) {
  const { dispatch } = useContext(KeranjangCtx);
  return <button onClick={() => dispatch({ type: "tambah", nama })}>Beli {nama}</button>;
}

function Ringkasan() {
  const { isi, dispatch } = useContext(KeranjangCtx);
  const total = Object.values(isi).reduce((a, b) => a + b, 0);
  return <p>{total} barang <button onClick={() => dispatch({ type: "kosongkan" })}>Kosongkan</button></p>;
}

function App() {
  const [isi, dispatch] = useReducer(reducer, {});
  return (
    <KeranjangCtx.Provider value={{ isi, dispatch }}>
      <TombolBeli nama="Kopi" /> <TombolBeli nama="Teh" />
      <Ringkasan />
    </KeranjangCtx.Provider>
  );
}`,
   task:{q:'Klik tombol beli sampai keranjang berisi 4 barang.',test:`/4 barang/.test(document.body.textContent)`,hint:'Tekan tombol Beli empat kali.'},
   pts:['useReducer: logika perubahan state di satu fungsi.','Context menghindari prop drilling.','Provider menyediakan, useContext membaca.'],
   q:[['Masalah yang diselesaikan Context?',['Meneruskan props lewat banyak lapisan','Mempercepat render','Mengambil data dari server'],0,'Itu disebut prop drilling.']]},
  {k:'w',t:'Custom hook',react:true,nodes:['Writing Custom Hooks','Hooks Best Practices'],
   b:['Logika berisi hook yang dipakai di beberapa komponen bisa diekstrak menjadi <b>custom hook</b>: fungsi biasa yang namanya diawali <code>use</code> dan memanggil hook lain.',
      'Contoh: <code>useLocalStorage</code> menyimpan state ke localStorage agar tidak hilang saat halaman dimuat ulang. Setiap komponen yang memakainya mendapat state sendiri.'],
   js:`function useLocalStorage(kunci, awal) {
  const [nilai, setNilai] = useState(() => {
    try { return JSON.parse(localStorage.getItem(kunci)) ?? awal; } catch { return awal; }
  });
  useEffect(() => {
    try { localStorage.setItem(kunci, JSON.stringify(nilai)); } catch {}
  }, [kunci, nilai]);
  return [nilai, setNilai];
}

function App() {
  const [nama, setNama] = useLocalStorage("nama-pembeli", "");
  return (
    <div>
      <label>Nama pembeli <input value={nama} onChange={e => setNama(e.target.value)} /></label>
      <p>Halo, {nama || "tamu"}! Muat ulang pratinjau: namamu tetap ada.</p>
    </div>
  );
}`,
   pts:['Custom hook = fungsi berawalan use yang memanggil hook.','Berbagi logika, bukan berbagi state.','Contoh umum: useFetch, useLocalStorage, useDebounce.'],
   q:[['Syarat nama custom hook?',['Diawali use','Diawali hook','Huruf kapital'],0,'Agar aturan hooks bisa diperiksa linter.']]}
 ]},
{t:'Pola komponen',lvl:'Menengah',d:'Komposisi, render props, HOC, portal, error boundary, dan suspense.',
 nodes:['Composition vs Inheritance','Render Props','High Order Components','Portals','Error Boundaries','Suspense'],
 lessons:[
  {k:'c',t:'Komposisi, render props & HOC',nodes:['Composition vs Inheritance','Render Props','High Order Components'],lang:'jsx',run:false,
   b:['React menyarankan <b>komposisi</b>, bukan pewarisan kelas: komponen kecil digabung lewat props dan children. Komponen <code>Modal</code> tidak perlu tahu isinya; ia cukup menampilkan <code>children</code>.',
      '<b>Render props</b> adalah prop berisi fungsi yang mengembalikan JSX, sehingga komponen bisa berbagi perilaku sambil membiarkan pemakainya menentukan tampilan. <b>Higher-order component</b> (HOC) adalah fungsi yang menerima komponen dan mengembalikan komponen baru yang ditambahi kemampuan.',
      'Kedua pola ini kini sebagian besar digantikan custom hook, tapi masih banyak ditemui di kode dan pustaka lama.'],
   code:`// Komposisi
function Kartu({ judul, children }) {
  return <section className="kartu"><h3>{judul}</h3>{children}</section>;
}
<Kartu judul="Promo"><p>Diskon 20%</p></Kartu>

// Render props
function Mouse({ render }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return <div onMouseMove={e => setPos({ x: e.clientX, y: e.clientY })}>{render(pos)}</div>;
}
<Mouse render={({ x, y }) => <p>Kursor di {x}, {y}</p>} />

// Higher-order component
function denganLogin(Komponen) {
  return function Terlindungi(props) {
    const user = useContext(UserCtx);
    return user ? <Komponen {...props} /> : <p>Silakan masuk dulu.</p>;
  };
}
const HalamanAkun = denganLogin(Akun);`,
   pts:['Utamakan komposisi lewat props dan children.','Render props: prop berupa fungsi yang mengembalikan JSX.','HOC: fungsi komponen → komponen.','Custom hook adalah cara modern berbagi perilaku.'],
   q:[['HOC adalah?',['Fungsi yang menerima komponen dan mengembalikan komponen','Komponen kelas induk','Hook bawaan'],0,'Higher-order seperti fungsi tingkat tinggi.']]},
  {k:'w',t:'Portal, error boundary & suspense',react:true,nodes:['Portals','Error Boundaries','Suspense'],
   b:['<b>Portal</b> merender anak ke node DOM lain, misalnya modal yang harus berada di luar elemen dengan overflow tersembunyi: <code>ReactDOM.createPortal(isi, document.body)</code>.',
      '<b>Error boundary</b> menangkap error saat render di komponen anak dan menampilkan cadangan, sehingga satu komponen rusak tidak membuat seluruh aplikasi putih. Saat ini error boundary masih ditulis sebagai komponen kelas.',
      '<b>Suspense</b> menampilkan cadangan (misalnya loader) selama anak menunggu kode atau data, dipakai bersama <code>React.lazy</code> atau framework seperti Next.js.'],
   js:`class Pengaman extends React.Component {
  constructor(p) { super(p); this.state = { error: null }; }
  static getDerivedStateFromError(error) { return { error }; }
  render() {
    return this.state.error
      ? <p className="err">Ups, bagian ini gagal dimuat: {this.state.error.message}</p>
      : this.props.children;
  }
}

function Rusak() { throw new Error("data harga kosong"); }

function Modal({ onTutup }) {
  return ReactDOM.createPortal(
    <div className="modal"><p>Saya dirender di document.body lewat portal.</p><button onClick={onTutup}>Tutup</button></div>,
    document.body
  );
}

function App() {
  const [buka, setBuka] = useState(false);
  return (
    <div>
      <button onClick={() => setBuka(true)}>Buka modal</button>
      {buka && <Modal onTutup={() => setBuka(false)} />}
      <Pengaman><Rusak /></Pengaman>
      <p>Bagian lain tetap jalan.</p>
    </div>
  );
}`,
   css:`body{font:14px system-ui,sans-serif}.modal{position:fixed;inset:20% 10% auto;background:#fff;border:1px solid #ccc;border-radius:12px;padding:12px;box-shadow:0 20px 40px #0003}.err{color:#B23A2E}`,
   pts:['Portal merender ke luar pohon DOM induk.','Error boundary mencegah satu error merusak seluruh aplikasi.','Suspense menampilkan cadangan saat menunggu.'],
   q:[['Tanpa error boundary, error render di satu komponen menyebabkan?',['Seluruh pohon React dilepas (layar kosong)','Hanya komponen itu hilang','Tidak ada efek'],0,'Karena itu pasang error boundary di titik penting.']]}
 ]},
{t:'Form & validasi',lvl:'Menengah',d:'Input terkendali, pustaka form, dan validasi skema.',nodes:['Forms','React hook form','Formik','Types & Validation','Zod'],
 lessons:[
  {k:'w',t:'Input terkendali',react:true,nodes:['Forms'],
   b:['Pada <b>controlled input</b>, nilai input berasal dari state dan setiap ketikan memperbarui state lewat <code>onChange</code>. React menjadi satu-satunya sumber kebenaran, sehingga mudah memvalidasi dan menampilkan pesan error saat itu juga.',
      'Kirim form dengan <code>onSubmit</code> dan panggil <code>e.preventDefault()</code>. Tampilkan error di dekat input dan hubungkan dengan <code>aria-describedby</code> agar dibacakan.'],
   js:`function App() {
  const [form, setForm] = useState({ nama: "", email: "" });
  const [kirim, setKirim] = useState(false);
  const ubah = e => setForm({ ...form, [e.target.name]: e.target.value });
  const err = {
    nama: form.nama.trim().length < 3 ? "Nama minimal 3 huruf" : "",
    email: !/^\\S+@\\S+\\.\\S+$/.test(form.email) ? "Format email belum benar" : "",
  };
  const valid = !err.nama && !err.email;
  return (
    <form onSubmit={e => { e.preventDefault(); setKirim(true); }}>
      <label htmlFor="nama">Nama</label>
      <input id="nama" name="nama" value={form.nama} onChange={ubah} aria-describedby="e-nama" />
      <small id="e-nama">{form.nama && err.nama}</small>
      <label htmlFor="email">Email</label>
      <input id="email" name="email" value={form.email} onChange={ubah} aria-describedby="e-email" />
      <small id="e-email">{form.email && err.email}</small>
      <button disabled={!valid}>Daftar</button>
      {kirim && <p>Terima kasih, {form.nama}!</p>}
    </form>
  );
}`,
   css:`body{font:14px system-ui,sans-serif}form{display:grid;gap:4px;max-width:260px}small{color:#B23A2E;min-height:1em}`,
   task:{q:'Isi nama dan email yang valid, lalu tekan Daftar.',test:`/Terima kasih/.test(document.body.textContent)`,hint:'Nama minimal 3 huruf, email seperti a@b.co.'},
   pts:['Controlled input: value dari state, onChange memperbarui state.','Validasi saat mengetik dan saat kirim.','Hubungkan pesan error dengan aria-describedby.'],
   q:[['Sumber kebenaran nilai pada controlled input?',['State React','DOM','localStorage'],0,'Itu arti "terkendali".']]},
  {k:'c',t:'React Hook Form & Zod',nodes:['React hook form','Formik','Types & Validation','Zod'],lang:'tsx',run:false,
   b:['Untuk form besar, pustaka seperti <b>React Hook Form</b> (atau Formik) mengurangi kode berulang dan render ulang. Ia mendaftarkan input dengan <code>register</code> dan menyediakan error secara terstruktur.',
      '<b>Zod</b> mendefinisikan skema validasi sekali, lalu dipakai di frontend dan backend, sekaligus menghasilkan tipe TypeScript otomatis. Pustaka sejenis: Valibot dan Yup.'],
   code:`import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

const Skema = z.object({
  nama: z.string().min(3, "Nama minimal 3 huruf"),
  email: z.string().email("Format email belum benar"),
  umur: z.coerce.number().int().min(17, "Minimal 17 tahun"),
});
type Daftar = z.infer<typeof Skema>;

export function FormDaftar() {
  const { register, handleSubmit, formState: { errors } } =
    useForm<Daftar>({ resolver: zodResolver(Skema) });
  return (
    <form onSubmit={handleSubmit(data => console.log(data))}>
      <input {...register("nama")} />  <small>{errors.nama?.message}</small>
      <input {...register("email")} /> <small>{errors.email?.message}</small>
      <input {...register("umur")} />  <small>{errors.umur?.message}</small>
      <button>Daftar</button>
    </form>
  );
}`,
   pts:['React Hook Form: register, handleSubmit, errors.','Zod: satu skema untuk validasi dan tipe.','z.infer menghasilkan tipe TypeScript dari skema.'],
   q:[['Keuntungan Zod?',['Satu skema untuk validasi dan tipe','Membuat CSS','Routing'],0,'Skema dipakai ulang di banyak tempat.']]}
 ]},
{t:'Routing & state global',lvl:'Lanjutan',d:'Berpindah halaman di aplikasi satu halaman dan berbagi state antar-halaman.',nodes:['Routing','React Router','react-router','TanStack Router','State Management','Zustand','Jotai','MobX'],
 lessons:[
  {k:'c',t:'React Router',nodes:['Routing','React Router','react-router','TanStack Router'],lang:'jsx',run:false,
   b:['Aplikasi React biasanya satu halaman HTML (SPA). <b>Router</b> memetakan alamat URL ke komponen tanpa memuat ulang halaman, sehingga tombol back browser tetap bekerja.',
      'Dengan React Router: definisikan rute, pakai <code>&lt;Link&gt;</code> alih-alih <code>&lt;a&gt;</code>, baca parameter dengan <code>useParams</code>, dan pindah halaman lewat kode dengan <code>useNavigate</code>. TanStack Router adalah alternatif dengan dukungan TypeScript yang lebih ketat.'],
   code:`import { createBrowserRouter, RouterProvider, Link, useParams, Outlet } from "react-router-dom";

function Layout() {
  return (<><nav><Link to="/">Beranda</Link> · <Link to="/produk/1">Kopi Gayo</Link></nav><Outlet /></>);
}
function DetailProduk() {
  const { id } = useParams();          // "/produk/1" → id = "1"
  return <h1>Produk #{id}</h1>;
}

const router = createBrowserRouter([
  { path: "/", element: <Layout />, children: [
    { index: true, element: <h1>Beranda</h1> },
    { path: "produk/:id", element: <DetailProduk /> },
    { path: "*", element: <h1>Halaman tidak ditemukan</h1> },
  ]},
]);

export default function App() { return <RouterProvider router={router} />; }`,
   pts:['Router memetakan URL ke komponen.','Link mencegah muat ulang halaman.','useParams membaca bagian dinamis URL.','Rute * untuk halaman 404.'],
   q:[['Kenapa pakai Link, bukan a?',['Agar pindah halaman tanpa memuat ulang','Agar SEO lebih baik','Wajib secara sintaks'],0,'Link ditangani router di sisi klien.']]},
  {k:'c',t:'Zustand, Jotai & kawan-kawan',nodes:['State Management','Zustand','Jotai','MobX'],lang:'js',run:false,
   b:['Context cukup untuk data yang jarang berubah. Untuk state global yang sering berubah (keranjang, filter, data pengguna), pustaka state management lebih praktis dan efisien.',
      '<b>Zustand</b> membuat store kecil dengan satu fungsi, tanpa provider. <b>Jotai</b> memecah state menjadi atom-atom kecil. <b>Redux Toolkit</b> masih banyak dipakai di perusahaan besar. <b>MobX</b> memakai pendekatan observable. Untuk data dari server, gunakan TanStack Query (modul berikutnya), bukan store global.'],
   code:`import { create } from "zustand";

export const useKeranjang = create(set => ({
  isi: [],
  tambah: produk => set(s => ({ isi: [...s.isi, produk] })),
  kosongkan: () => set({ isi: [] }),
}));

// di komponen mana pun, tanpa Provider:
function Ikon() {
  const jumlah = useKeranjang(s => s.isi.length);   // hanya render ulang jika jumlah berubah
  return <span>🛒 {jumlah}</span>;
}`,
   pts:['Context untuk data yang jarang berubah.','Zustand: store sederhana tanpa provider.','Pilih selector agar render ulang seminimal mungkin.','Data server ditangani pustaka data fetching.'],
   q:[['Data produk dari API sebaiknya dikelola dengan?',['TanStack Query / SWR','Zustand saja','useRef'],0,'Pustaka data fetching menangani cache dan muat ulang.']]}
 ]},
{t:'Data dari server',lvl:'Lanjutan',d:'Memanggil API, menangani loading dan error, serta cache data.',nodes:['API Calls','Axios','TanStack Query','SWR','rtk-query','Apollo','Relay','urql'],
 lessons:[
  {k:'w',t:'Fetch di komponen',react:true,nodes:['API Calls','Axios'],
   b:['Pola dasar mengambil data: simpan <b>data</b>, <b>loading</b>, dan <b>error</b> di state, panggil API di <code>useEffect</code>, dan tampilkan ketiga keadaan itu. Abaikan respons yang datang setelah komponen hilang atau parameter berubah.',
      'Axios adalah alternatif fetch dengan fitur interceptor dan JSON otomatis. Contoh di bawah memakai API tiruan agar berjalan di mana saja.'],
   js:`const DB = { kopi: ["Kopi Gayo", "Kopi Toraja"], teh: ["Teh Melati", "Teh Hijau"] };
const api = kat => new Promise((ok, gagal) => setTimeout(() =>
  kat === "error" ? gagal(new Error("Server sedang sibuk")) : ok(DB[kat] || []), 700));

function App() {
  const [kat, setKat] = useState("kopi");
  const [st, setSt] = useState({ loading: true, data: [], error: null });
  useEffect(() => {
    let aktif = true;
    setSt(s => ({ ...s, loading: true, error: null }));
    api(kat).then(data => aktif && setSt({ loading: false, data, error: null }))
            .catch(error => aktif && setSt({ loading: false, data: [], error }));
    return () => { aktif = false; };
  }, [kat]);
  return (
    <div>
      {["kopi", "teh", "error"].map(k => <button key={k} onClick={() => setKat(k)}>{k}</button>)}
      {st.loading ? <p>Memuat…</p> : st.error ? <p className="err">{st.error.message}</p>
        : <ul>{st.data.map(n => <li key={n}>{n}</li>)}</ul>}
    </div>
  );
}`,
   css:`body{font:14px system-ui,sans-serif}.err{color:#B23A2E}button{margin-right:4px}`,
   pts:['Tangani tiga keadaan: loading, error, data.','Abaikan respons usang dengan flag atau AbortController.','Axios: alternatif fetch dengan fitur tambahan.'],
   q:[['Kenapa perlu flag aktif di contoh?',['Mencegah respons lama menimpa data baru','Mempercepat fetch','Wajib untuk JSX'],0,'Ini mencegah race condition.']]},
  {k:'c',t:'TanStack Query, SWR & GraphQL',nodes:['TanStack Query','SWR','rtk-query','Apollo','Relay','urql'],lang:'jsx',run:false,
   b:['<b>TanStack Query</b> dan <b>SWR</b> mengurus hal yang merepotkan: cache, muat ulang di latar belakang, retry, pagination, dan berbagi data yang sama antar-komponen. Kode komponen menjadi pendek.',
      'Untuk API GraphQL, klien seperti <b>Apollo</b>, <b>urql</b>, dan <b>Relay</b> melakukan hal serupa dengan query GraphQL. RTK Query adalah pilihan bagi proyek yang memakai Redux Toolkit.'],
   code:`import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";

function DaftarProduk() {
  const { data, isPending, error } = useQuery({
    queryKey: ["produk"],
    queryFn: () => fetch("/api/produk").then(r => r.json()),
    staleTime: 60_000,            // dianggap segar 1 menit
  });
  const qc = useQueryClient();
  const tambah = useMutation({
    mutationFn: p => fetch("/api/produk", { method: "POST", body: JSON.stringify(p) }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["produk"] }),   // muat ulang daftar
  });
  if (isPending) return <p>Memuat…</p>;
  if (error) return <p>Gagal: {error.message}</p>;
  return <ul>{data.map(p => <li key={p.id}>{p.nama}</li>)}</ul>;
}`,
   pts:['queryKey menjadi kunci cache.','invalidateQueries memuat ulang data setelah perubahan.','Apollo/urql/Relay untuk GraphQL.'],
   q:[['Fungsi queryKey?',['Kunci cache untuk data itu','Kunci API rahasia','Nama komponen'],0,'Komponen dengan key sama berbagi data.']]}
 ]},
{t:'Styling & pustaka komponen',lvl:'Lanjutan',d:'CSS Modules, Tailwind, pustaka komponen, headless UI, dan animasi.',nodes:['Styling','CSS Modules','Tailwind CSS','Panda CSS','Component / Libraries','Material UI','Chakra UI','Shadcn UI','Radix UI','Headless Component Libraries','React Aria','Ark UI','Animation','Framer Motion','react spring'],
 lessons:[
  {k:'c',t:'Menata komponen',nodes:['Styling','CSS Modules','Tailwind CSS','Panda CSS'],lang:'jsx',run:false,
   b:['<b>CSS Modules</b> membuat nama class unik per file secara otomatis, jadi <code>.tombol</code> di dua komponen tidak bentrok. <b>Tailwind</b> menata langsung lewat utility class. <b>Panda CSS</b> dan pustaka CSS-in-JS menulis gaya di JavaScript dengan dukungan tipe.',
      'Pilih satu pendekatan per proyek agar konsisten. Tailwind paling banyak dipakai di proyek React baru.'],
   code:`// Tombol.module.css
// .tombol { padding: 8px 16px; border-radius: 999px; }
// .utama  { background: #1C1B19; color: white; }

import gaya from "./Tombol.module.css";
export function Tombol({ utama, children }) {
  return <button className={\`\${gaya.tombol} \${utama ? gaya.utama : ""}\`}>{children}</button>;
}

// Versi Tailwind
export function TombolTw({ children }) {
  return <button className="px-4 py-2 rounded-full bg-stone-900 text-white hover:opacity-90">{children}</button>;
}`,
   pts:['CSS Modules: class unik per komponen.','Tailwind: utility class di JSX.','Konsisten satu pendekatan per proyek.'],
   q:[['Masalah yang diselesaikan CSS Modules?',['Nama class bentrok antar-komponen','Ukuran gambar','Routing'],0,'Nama class dibuat unik otomatis.']]},
  {k:'c',t:'Pustaka komponen & animasi',nodes:['Component / Libraries','Material UI','Chakra UI','Shadcn UI','Radix UI','Headless Component Libraries','React Aria','Ark UI','Animation','Framer Motion','react spring'],lang:'jsx',run:false,
   b:['Pustaka komponen siap pakai seperti <b>Material UI</b> dan <b>Chakra UI</b> mempercepat pembuatan antarmuka. Pustaka <b>headless</b> seperti <b>Radix UI</b>, <b>React Aria</b>, dan <b>Ark UI</b> menyediakan perilaku dan aksesibilitas (keyboard, fokus, ARIA) tanpa gaya, sehingga tampilannya bebas kamu atur. <b>shadcn/ui</b> menyalin komponen berbasis Radix + Tailwind langsung ke proyekmu.',
      'Untuk animasi, <b>Framer Motion</b> (kini bernama Motion) dan <b>react-spring</b> menyediakan animasi deklaratif dan berbasis fisika.'],
   code:`import * as Dialog from "@radix-ui/react-dialog";
import { motion } from "framer-motion";

export function KonfirmasiHapus({ onHapus }) {
  return (
    <Dialog.Root>
      <Dialog.Trigger>Hapus</Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/40" />
        <Dialog.Content asChild>
          <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }}
                      className="fixed top-1/3 left-1/2 -translate-x-1/2 bg-white p-6 rounded-xl">
            <Dialog.Title>Hapus produk?</Dialog.Title>
            <button onClick={onHapus}>Ya, hapus</button>
            <Dialog.Close>Batal</Dialog.Close>
          </motion.div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}`,
   pts:['Pustaka bergaya (MUI, Chakra) vs headless (Radix, React Aria).','Headless: perilaku dan aksesibilitas, tanpa gaya.','Framer Motion untuk animasi deklaratif.'],
   q:[['Keunggulan pustaka headless?',['Aksesibilitas siap, tampilan bebas','Sudah ada tema lengkap','Tidak butuh React'],0,'Kamu yang menentukan gayanya.']]}
 ]},
{t:'Pengujian & ekosistem',lvl:'Profesional',d:'Menguji komponen, framework SSR, aplikasi mobile, dan TypeScript.',nodes:['Testing','Jest','Vitest','React Testing Library','Playwright','Cypress','SSR Frameworks','Next.js','Astro','Mobile Applications','React Native','TypeScript','Server APIs'],
 lessons:[
  {k:'c',t:'Menguji komponen',nodes:['Testing','Jest','Vitest','React Testing Library','Playwright','Cypress'],lang:'jsx',run:false,
   b:['<b>React Testing Library</b> menguji komponen seperti pengguna memakainya: cari elemen berdasarkan teks atau peran (role), klik, lalu periksa hasilnya. Jalankan dengan Vitest atau Jest.',
      'Tes end-to-end dengan <b>Playwright</b> atau <b>Cypress</b> menjalankan browser sungguhan dan menguji alur lengkap, misalnya dari memilih produk sampai checkout.'],
   code:`import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { test, expect } from "vitest";
import Penghitung from "./Penghitung";

test("tombol + menambah jumlah", async () => {
  render(<Penghitung />);
  await userEvent.click(screen.getByRole("button", { name: "+" }));
  await userEvent.click(screen.getByRole("button", { name: "+" }));
  expect(screen.getByText(/di keranjang: 2/)).toBeInTheDocument();
});`,
   pts:['Uji perilaku yang dilihat pengguna, bukan detail internal.','Cari elemen lewat role dan teks.','Playwright/Cypress untuk alur end-to-end.'],
   q:[['Cara terbaik mencari tombol di RTL?',['getByRole("button", { name })','querySelector(".btn")','Lewat state'],0,'Role sekaligus menguji aksesibilitas.']]},
  {k:'c',t:'Next.js, React Native & TypeScript',nodes:['SSR Frameworks','Next.js','Astro','Mobile Applications','React Native','TypeScript','Server APIs'],lang:'tsx',run:false,
   b:['<b>Next.js</b> adalah framework React yang menambahkan routing berbasis folder, server-side rendering, React Server Components, dan API route. Halaman dirender di server sehingga cepat tampil dan ramah SEO. <b>Astro</b> cocok untuk situs konten yang sebagian besar statis.',
      '<b>React Native</b> memakai konsep React yang sama untuk membuat aplikasi Android dan iOS sungguhan. <b>TypeScript</b> kini menjadi standar di proyek React profesional: props dan state punya tipe yang diperiksa sebelum aplikasi berjalan.'],
   code:`// app/produk/[id]/page.tsx  (Next.js App Router, Server Component)
type Produk = { id: number; nama: string; harga: number };

export default async function Halaman({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const res = await fetch(\`https://api.tokonusantara.id/produk/\${id}\`, { next: { revalidate: 60 } });
  const p: Produk = await res.json();
  return (
    <main>
      <h1>{p.nama}</h1>
      <p>Rp{p.harga.toLocaleString("id-ID")}</p>
    </main>
  );
}`,
   pts:['Next.js: routing folder, SSR, Server Components.','Astro untuk situs konten.','React Native untuk aplikasi mobile.','TypeScript memeriksa props sebelum berjalan.'],
   q:[['Keuntungan SSR?',['Halaman cepat tampil dan ramah SEO','Tidak butuh server','Ukuran JS jadi nol'],0,'HTML sudah jadi saat dikirim.']]}
 ]},
{t:'Proyek akhir React',lvl:'Profesional',d:'Bangun toko online mini dengan komponen, state, dan data API.',nodes:[],
 lessons:[
  {k:'proj',t:'Toko online mini',stack:'React',
   brief:'Bangun aplikasi katalog dan keranjang Toko Nusantara dengan React. Data produk diambil dari API (boleh tiruan), keranjang tersimpan di localStorage.',
   feats:['Komponen terpisah: App, DaftarProduk, KartuProduk, Keranjang','Filter kategori dan pencarian nama (controlled input)','Keadaan loading dan error saat mengambil data','Keranjang dengan useReducer: tambah, kurangi, hapus, total harga','Keranjang tersimpan dengan custom hook useLocalStorage','Daftar memakai key yang stabil','Minimal dua tes dengan Vitest + React Testing Library','Terbit di Vercel atau Netlify'],
   steps:['Buat proyek: npm create vite@latest toko -- --template react.','Bangun komponen dengan data statis dulu.','Tambahkan state, reducer, dan data API.','Tulis tes, lalu terbitkan.'],
   files:[['src/App.jsx','jsx',`import { useEffect, useReducer, useState } from "react";

const PRODUK = [
  { id: 1, nama: "Kopi Gayo", kategori: "Minuman", harga: 85000 },
  { id: 2, nama: "Teh Melati", kategori: "Minuman", harga: 25000 },
  { id: 3, nama: "Keripik Singkong", kategori: "Camilan", harga: 15000 },
];
const ambil = () => new Promise(r => setTimeout(() => r(PRODUK), 500));

function keranjang(state, a) {
  switch (a.type) {
    case "tambah": return { ...state, [a.id]: (state[a.id] || 0) + 1 };
    case "kurang": {
      const n = (state[a.id] || 0) - 1, s = { ...state };
      if (n <= 0) delete s[a.id]; else s[a.id] = n;
      return s;
    }
    default: return state;
  }
}

export default function App() {
  const [produk, setProduk] = useState(null);
  const [cari, setCari] = useState("");
  const [isi, dispatch] = useReducer(keranjang, {}, () => JSON.parse(localStorage.getItem("krj") || "{}"));
  useEffect(() => { ambil().then(setProduk); }, []);
  useEffect(() => { localStorage.setItem("krj", JSON.stringify(isi)); }, [isi]);
  if (!produk) return <p>Memuat…</p>;
  const tampil = produk.filter(p => p.nama.toLowerCase().includes(cari.toLowerCase()));
  const total = Object.entries(isi).reduce((t, [id, n]) => t + n * produk.find(p => p.id === +id).harga, 0);
  return (
    <main>
      <input value={cari} onChange={e => setCari(e.target.value)} placeholder="Cari produk" aria-label="Cari produk" />
      <ul>{tampil.map(p => (
        <li key={p.id}>{p.nama} · Rp{p.harga.toLocaleString("id-ID")}
          <button onClick={() => dispatch({ type: "kurang", id: p.id })}>−</button>
          {isi[p.id] || 0}
          <button onClick={() => dispatch({ type: "tambah", id: p.id })}>+</button>
        </li>))}
      </ul>
      <p>Total: Rp{total.toLocaleString("id-ID")}</p>
    </main>
  );
}`]]}
 ]}
];
