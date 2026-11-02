/* ===================== ANIMASI: MEMBUAT VARIABEL =====================
   Animasi langkah demi langkah tentang cara variabel dibuat, diisi, diubah, dan dipakai.
   Satu skenario per bahasa (Java, Python, JavaScript, TypeScript, CSS, React). Kiri: kode
   yang "diketik" baris demi baris. Kanan: memori, yaitu kotak variabel dan isinya. */
const VARANIM={
 java:{file:'Main.java',lang:'java',code:['int umur = 17;','double harga = 12500.0;','String nama = "Sari";','umur = umur + 1;','final double PAJAK = 0.11;','double total = harga + harga * PAJAK;','umur = "tujuh belas";'],
  steps:[
   {ln:0,mem:[['umur','int','17','new']],note:'<b>Deklarasi + inisialisasi.</b> Java menyiapkan kotak bernama <code>umur</code> yang <b>hanya</b> boleh berisi bilangan bulat (<code>int</code>), lalu mengisinya dengan 17.'},
   {ln:1,mem:[['umur','int','17'],['harga','double','12500.0','new']],note:'Kotak <code>harga</code> bertipe <code>double</code> untuk bilangan pecahan.'},
   {ln:2,mem:[['umur','int','17'],['harga','double','12500.0'],['nama','String','"Sari"','new']],note:'<code>String</code> menyimpan teks. Teks ditulis di antara tanda kutip ganda.'},
   {ln:3,mem:[['umur','int','18','chg','17']],keep:1,note:'<b>Mengubah isi.</b> Ruas kanan dihitung dulu: umur (17) + 1 = 18, lalu hasilnya dimasukkan kembali ke kotak <code>umur</code>. Isi lama 17 hilang.'},
   {ln:4,mem:[['PAJAK','final double','0.11','new lock']],keep:1,note:'<code>final</code> membuat <b>konstanta</b>: isinya dikunci dan tidak bisa diubah lagi. Nama konstanta biasanya huruf besar.'},
   {ln:5,mem:[['total','double','13875.0','new']],keep:1,note:'Variabel dipakai dalam perhitungan: 12500.0 + 12500.0 × 0.11 = 13875.0.'},
   {ln:6,err:'error: incompatible types: String cannot be converted to int',keep:1,note:'<b>Error saat kompilasi.</b> Kotak <code>umur</code> bertipe <code>int</code>, jadi tidak bisa diisi teks. Java memeriksa tipe sebelum program jalan.'}]},
 python:{file:'main.py',lang:'python',code:['umur = 17','harga = 12500.0','nama = "Sari"','umur = umur + 1','PAJAK = 0.11','total = harga + harga * PAJAK','umur = "tujuh belas"'],
  steps:[
   {ln:0,mem:[['umur','int','17','new']],note:'<b>Membuat variabel</b> cukup dengan <code>=</code>. Python melihat nilainya (17) dan otomatis tahu tipenya <code>int</code>. Tidak perlu menulis tipe.'},
   {ln:1,mem:[['umur','int','17'],['harga','float','12500.0','new']],note:'Bilangan berkoma bertipe <code>float</code>.'},
   {ln:2,mem:[['umur','int','17'],['harga','float','12500.0'],['nama','str','"Sari"','new']],note:'Teks bertipe <code>str</code>. Boleh pakai kutip tunggal atau ganda.'},
   {ln:3,mem:[['umur','int','18','chg','17']],keep:1,note:'<b>Mengubah isi.</b> Ruas kanan dihitung dulu: 17 + 1 = 18, lalu nama <code>umur</code> sekarang menunjuk nilai 18.'},
   {ln:4,mem:[['PAJAK','float','0.11','new']],keep:1,note:'Python tidak punya konstanta sungguhan. <b>Kesepakatannya</b>: nama huruf besar berarti "jangan diubah".'},
   {ln:5,mem:[['total','float','13875.0','new']],keep:1,note:'Variabel dipakai dalam perhitungan: 12500.0 + 12500.0 × 0.11 = 13875.0.'},
   {ln:6,mem:[['umur','str','"tujuh belas"','chg','18']],keep:1,note:'<b>Boleh di Python</b>: tipe mengikuti nilainya (dynamic typing). Tapi hati-hati, <code>umur + 1</code> setelah ini akan error karena teks tidak bisa ditambah angka.'}]},
 js:{file:'main.js',lang:'js',code:['let umur = 17;','const nama = "Sari";','let harga = 12500;','umur = umur + 1;','const total = harga * 1.11;','console.log(nama, umur, total);','nama = "Budi";'],
  steps:[
   {ln:0,mem:[['umur','let','17','new']],note:'<code>let</code> membuat variabel yang <b>boleh diubah</b> nanti.'},
   {ln:1,mem:[['umur','let','17'],['nama','const','"Sari"','new lock']],note:'<code>const</code> membuat variabel yang <b>tidak boleh diisi ulang</b>. Biasakan memakai <code>const</code> kecuali memang perlu diubah.'},
   {ln:2,mem:[['harga','let','12500','new']],keep:1,note:'Angka di JavaScript bertipe <code>number</code>, baik bulat maupun pecahan.'},
   {ln:3,mem:[['umur','let','18','chg','17']],keep:1,note:'<b>Mengubah isi.</b> 17 + 1 = 18 dimasukkan kembali ke <code>umur</code>.'},
   {ln:4,mem:[['total','const','13875','new lock']],keep:1,note:'Variabel dipakai dalam perhitungan: 12500 × 1.11 = 13875.'},
   {ln:5,out:'Sari 18 13875',keep:1,note:'<code>console.log</code> membaca isi variabel dan menampilkannya di konsol.'},
   {ln:6,err:'TypeError: Assignment to constant variable.',keep:1,note:'<b>Error.</b> <code>nama</code> dibuat dengan <code>const</code>, jadi tidak bisa diisi ulang.'}]},
 ts:{file:'main.ts',lang:'ts',code:['let umur: number = 17;','const nama: string = "Sari";','let aktif = true;','umur = umur + 1;','let kota: string | null = null;','kota = "Bandung";','umur = "tujuh belas";'],
  steps:[
   {ln:0,mem:[['umur','number','17','new']],note:'TypeScript menambahkan <b>anotasi tipe</b> setelah titik dua: kotak <code>umur</code> hanya untuk <code>number</code>.'},
   {ln:1,mem:[['umur','number','17'],['nama','string','"Sari"','new lock']],note:'<code>const</code> + <code>string</code>: teks yang tidak boleh diisi ulang.'},
   {ln:2,mem:[['aktif','boolean','true','new']],keep:1,note:'<b>Inferensi tipe</b>: tanpa anotasi pun TypeScript tahu <code>aktif</code> bertipe <code>boolean</code> dari nilainya.'},
   {ln:3,mem:[['umur','number','18','chg','17']],keep:1,note:'Mengubah isi: 17 + 1 = 18. Tipenya tetap <code>number</code>.'},
   {ln:4,mem:[['kota','string | null','null','new']],keep:1,note:'<b>Union type</b>: <code>kota</code> boleh berisi teks <b>atau</b> <code>null</code> (belum diisi).'},
   {ln:5,mem:[['kota','string | null','"Bandung"','chg','null']],keep:1,note:'Sekarang <code>kota</code> berisi teks.'},
   {ln:6,err:"Type 'string' is not assignable to type 'number'.",keep:1,note:'<b>Error sebelum program jalan.</b> Editor sudah memberi garis merah: <code>umur</code> bertipe <code>number</code>.'}]},
 css:{file:'gaya.css',lang:'css',code:[':root {','  --merek: #0F766E;','  --radius: 8px;','}','.tombol { background: var(--merek); border-radius: var(--radius); }','.tema-gelap { --merek: #5EC9B5; }'],
  steps:[
   {ln:0,mem:[],note:'Variabel CSS (custom property) biasanya ditaruh di <code>:root</code> agar berlaku di seluruh halaman.'},
   {ln:1,mem:[['--merek','warna','#0F766E','new']],pv:'#0F766E',note:'Nama variabel CSS <b>wajib</b> diawali dua tanda minus: <code>--merek</code>.'},
   {ln:2,mem:[['--merek','warna','#0F766E'],['--radius','panjang','8px','new']],pv:'#0F766E',note:'Satu variabel bisa dipakai di ratusan tempat. Ubah satu kali, semua ikut berubah.'},
   {ln:4,mem:[['--merek','warna','#0F766E'],['--radius','panjang','8px']],pv:'#0F766E',btn:1,note:'<code>var(--merek)</code> <b>membaca</b> isi variabel. Tombol kini berwarna sesuai merek.'},
   {ln:5,mem:[['--merek','warna','#5EC9B5','chg','#0F766E'],['--radius','panjang','8px']],pv:'#5EC9B5',btn:1,dark:1,note:'Di dalam <code>.tema-gelap</code>, <code>--merek</code> diisi ulang. Tombol di dalamnya otomatis berubah warna tanpa menulis ulang aturan <code>.tombol</code>.'}]},
 react:{file:'Penghitung.jsx',lang:'jsx',code:['function Penghitung() {','  const [jumlah, setJumlah] = useState(0);','  const label = "Klik";','  return <button onClick={() => setJumlah(jumlah + 1)}>','    {label}: {jumlah}','  </button>;','}'],
  steps:[
   {ln:1,mem:[['jumlah','state','0','new'],['setJumlah','fungsi','ƒ']],ui:'Klik: 0',note:'<code>useState(0)</code> membuat <b>variabel state</b> bernilai awal 0, plus fungsi <code>setJumlah</code> untuk mengubahnya.'},
   {ln:2,mem:[['jumlah','state','0'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"','new']],ui:'Klik: 0',note:'Variabel biasa (<code>const</code>) dibuat ulang setiap render.'},
   {ln:4,mem:[['jumlah','state','0'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"']],ui:'Klik: 0',note:'JSX membaca variabel di dalam <code>{ }</code> untuk ditampilkan.'},
   {ln:3,mem:[['jumlah','state','1','chg','0'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"']],ui:'Klik: 1',click:1,note:'Tombol diklik → <code>setJumlah(0 + 1)</code>. React menyimpan nilai baru dan <b>merender ulang</b> komponen.'},
   {ln:3,mem:[['jumlah','state','2','chg','1'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"']],ui:'Klik: 2',click:1,note:'Klik lagi → 2. Mengubah <code>jumlah</code> langsung (<code>jumlah = 2</code>) tidak akan memperbarui layar; selalu lewat <code>setJumlah</code>.'}]}};
function varanimViz(host,o={}){
  const S=VARANIM[o.va]||VARANIM.js;let mem=[];
  /* bangun memori kumulatif: keep=1 berarti gabungkan dengan langkah sebelumnya */
  const frames=[];S.steps.forEach(st=>{let m=mem.map(x=>x.slice(0,3));
    if(st.mem){if(st.keep){st.mem.forEach(n=>{const i=m.findIndex(x=>x[0]===n[0]);if(i>=0)m[i]=n;else m.push(n)})}else m=st.mem.map(x=>x.slice())}
    mem=m;frames.push({...st,m:m.map((x,i)=>{const n=(st.mem||[]).find(y=>y[0]===x[0]);return n||x})})});
  player(host,frames,(stage,f)=>{
    stage.innerHTML=`<div class="va"><div class="va-code"><div class="va-file">${S.file}</div><pre>${S.code.map((ln,i)=>`<span class="va-ln ${i===f.ln?'cur':''} ${i<f.ln||(f.ln<i&&false)?'done':''} ${f.err&&i===f.ln?'bad':''}"><em>${i+1}</em><code>${hl(ln,S.lang)||' '}</code></span>`).join('')}</pre>
      ${f.err?`<div class="va-err">✗ ${esc(f.err)}</div>`:''}${f.out?`<div class="va-out"><small>Konsol</small>${esc(f.out)}</div>`:''}</div>
     <div class="va-mem"><div class="va-file">Memori</div>${f.m.length?f.m.map(([n,t,v,fl,old])=>`<div class="va-box ${fl||''}"><span class="va-n">${esc(n)}</span><span class="va-v">${old!=null?`<s>${esc(old)}</s> `:''}<b>${esc(v)}</b>${fl&&fl.includes('lock')?' 🔒':''}</span><span class="va-t">${esc(t)}</span></div>`).join(''):'<p class="muted small">Belum ada variabel.</p>'}
      ${f.pv?`<div class="va-pv ${f.dark?'dark':''}"><small>Pratinjau</small>${f.btn?`<button tabindex="-1" style="background:${f.pv};border-radius:8px">Pesan sekarang</button>`:`<i style="background:${f.pv}"></i>`}</div>`:''}
      ${f.ui?`<div class="va-pv"><small>Layar</small><button tabindex="-1" class="${f.click?'clk':''}">${esc(f.ui)}</button></div>`:''}</div></div>`},{speed:2200});
}
VIZ2.varanim=varanimViz;VIZ2T.varanim='Animasi: membuat dan mengubah variabel';
/* pelajaran variabel di setiap jalur pemrograman */
function varAnimOf(tk,l){
  if((tk==='java'||tk==='python')&&l.k==='topic'&&l.ref==='2.0')return tk;
  if(tk==='fe0'&&l.t==='Variabel & tipe data')return 'js';
  if(tk==='ts'&&l.t==='Primitif, array & tuple')return 'ts';
  if(tk==='css'&&l.t==='Variabel CSS & tema')return 'css';
  if(tk==='react'&&l.t==='State dengan useState')return 'react';
  return null;
}
