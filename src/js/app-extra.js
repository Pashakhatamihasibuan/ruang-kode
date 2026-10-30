/* ===================== KUIS CERITA & GLOSARIUM ===================== */
/* ===================== KUIS CERITA ===================== */
const SQL_STORIES=[
  {lvl:'Dasar',m:3,t:'Promo khusus Jakarta',s:'Tim pemasaran ingin mengirim voucher hanya ke pelanggan yang tinggal di Jakarta. Rina menulis query untuk mengambil nama mereka.',sql:"SELECT nama FROM pelanggan\nWHERE kota = 'Jakarta';",q:'Apa hasil query ini?',o:['2 baris: Andi dan Dewi','1 baris: Andi','8 baris, semua pelanggan','0 baris, karena huruf J kapital'],a:0,w:'Hanya Andi dan Dewi yang kotanya Jakarta. WHERE menyaring baris sebelum hasil ditampilkan.'},
  {lvl:'Dasar',m:5,t:'Menghitung pelanggan',s:'Manajer bertanya berapa pelanggan yang sudah mengisi kota. Salah satu pelanggan, Gita, belum mengisinya.',sql:'SELECT COUNT(*) AS a, COUNT(kota) AS b\nFROM pelanggan;',q:'Berapa nilai a dan b?',o:['a = 8, b = 7','a = 8, b = 8','a = 7, b = 7','a = 7, b = 8'],a:0,w:'COUNT(*) menghitung semua baris (8), COUNT(kota) melewati nilai NULL, jadi 7.'},
  {lvl:'Dasar',m:3,t:'Mencari yang belum isi kota',s:'Admin ingin menemukan pelanggan yang kotanya kosong, lalu menulis kondisi dengan tanda sama dengan.',sql:'SELECT nama FROM pelanggan\nWHERE kota = NULL;',q:'Apa yang terjadi?',o:['0 baris; seharusnya pakai IS NULL','1 baris: Gita','Error sintaks','8 baris'],a:0,w:'NULL berarti "tidak diketahui". Membandingkan apa pun dengan = NULL hasilnya bukan TRUE, jadi tidak ada baris yang lolos. Pakai WHERE kota IS NULL.'},
  {lvl:'Dasar',m:4,t:'Lupa WHERE',s:'Budi ingin mengubah harga Teh Melati menjadi Rp10.000, tapi terburu-buru dan lupa menulis WHERE.',sql:'UPDATE produk SET harga = 10000;',q:'Berapa produk yang harganya berubah?',o:['Semua 8 produk','Hanya 1 produk','Tidak ada, karena error','Hanya produk di atas Rp10.000'],a:0,w:'Tanpa WHERE, UPDATE berlaku untuk semua baris. Biasakan menulis SELECT dengan WHERE yang sama dulu untuk mengecek baris yang akan terkena.'},
  {lvl:'Dasar',m:3,t:'Produk termahal',s:'Pemilik toko ingin tahu satu produk paling mahal untuk dipajang di halaman depan.',sql:'SELECT nama FROM produk\nORDER BY harga DESC\nLIMIT 1;',q:'Produk apa yang muncul?',o:['Madu Hutan','Kopi Gayo','Rendang Kaleng','Keripik Singkong'],a:0,w:'ORDER BY harga DESC menaruh harga tertinggi (Madu Hutan, Rp120.000) di atas, lalu LIMIT 1 mengambil baris pertama.'},
  {lvl:'Menengah',m:5,t:'Rekap per kategori',s:'Untuk laporan bulanan, Sari menghitung jumlah produk di setiap kategori.',sql:'SELECT kategori, COUNT(*)\nFROM produk\nGROUP BY kategori;',q:'Berapa baris hasilnya?',o:['4 baris','8 baris','1 baris','3 baris'],a:0,w:'GROUP BY membuat satu baris per kategori: Minuman, Camilan, Bumbu, dan Makanan.'},
  {lvl:'Menengah',m:7,t:'Pelanggan yang belum belanja',s:'Tim CRM mencari pelanggan yang belum pernah memesan untuk diberi ucapan selamat datang.',sql:'SELECT p.nama\nFROM pelanggan p\nLEFT JOIN pesanan s ON s.pelanggan_id = p.id\nGROUP BY p.nama\nHAVING COUNT(s.id) = 0;',q:'Siapa yang muncul?',o:['Gita','Tidak ada','Gita dan Hadi','Error: COUNT tidak boleh di HAVING'],a:0,w:'LEFT JOIN mempertahankan pelanggan tanpa pesanan dengan s.id NULL. COUNT(s.id) untuk Gita bernilai 0.'},
  {lvl:'Menengah',m:7,t:'Berapa baris gabungan?',s:'Ada 8 pelanggan dan 10 pesanan. Setiap pesanan pasti punya pelanggan yang terdaftar.',sql:'SELECT COUNT(*)\nFROM pelanggan p\nJOIN pesanan s ON s.pelanggan_id = p.id;',q:'Berapa hasil COUNT(*)?',o:['10','8','18','80'],a:0,w:'INNER JOIN menghasilkan satu baris untuk setiap pasangan yang cocok. Setiap dari 10 pesanan punya tepat satu pelanggan, jadi 10 baris.'},
  {lvl:'Menengah',m:8,t:'Di atas rata-rata',s:'Bagian keuangan ingin daftar produk yang harganya di atas rata-rata semua produk.',sql:'SELECT nama FROM produk\nWHERE harga > (SELECT AVG(harga) FROM produk);',q:'Berapa produk yang muncul?',o:['4 produk','3 produk','5 produk','Error: subquery tidak boleh di WHERE'],a:0,w:'Rata-rata harga Rp53.750. Yang di atasnya: Kopi Gayo, Kacang Mete, Madu Hutan, Rendang Kaleng.'},
  {lvl:'Lanjutan',m:11,t:'Transfer yang dibatalkan',s:'Saldo Andi Rp500.000. Kasir memulai transfer, lalu sadar salah nominal dan membatalkannya.',sql:'BEGIN;\nUPDATE rekening SET saldo = saldo - 100000 WHERE id = 1;\nROLLBACK;\nSELECT saldo FROM rekening WHERE id = 1;',q:'Berapa saldo yang tampil?',o:['500000','400000','0','Error karena ROLLBACK'],a:0,w:'ROLLBACK membatalkan semua perubahan sejak BEGIN, jadi saldo kembali Rp500.000.'},
  {lvl:'Lanjutan',m:14,t:'Peringkat gaji tim penjualan',s:'HR membuat peringkat gaji di divisi Penjualan. Yudi dan Rio sama-sama bergaji Rp8.000.000.',sql:"SELECT nama, RANK() OVER (ORDER BY gaji DESC) AS r\nFROM karyawan\nWHERE divisi = 'Penjualan';",q:'Berapa peringkat Rio?',o:['3, sama dengan Yudi','4','2','1'],a:0,w:'Umi 1, Zahra 2, lalu Yudi dan Rio seri di 3. RANK memberi angka sama untuk nilai seri.'},
  {lvl:'Lanjutan',m:12,t:'Form login yang bocor',s:"Aplikasi menyusun query dengan menyambung teks dari form: \"... WHERE username = '\" + input + \"'\". Seseorang mengetik ' OR '1'='1 di kolom username.",sql:"SELECT * FROM akun\nWHERE username = '' OR '1'='1';",q:'Apa yang terjadi?',o:['Semua akun terbaca karena kondisinya selalu benar','Error sintaks, login gagal','Hanya akun bernama OR yang terbaca','Tabel akun terhapus'],a:0,w:"Input penyerang menjadi bagian dari perintah SQL. '1'='1' selalu benar. Solusinya: parameter (prepared statement), bukan menyambung string."}];
let storyAns=store.get('rk-story2',{}),storyHide=store.get('rk-story-hide',true),storyLv='Semua';
function storiesOf(tk){
  if(tk==='sql')return SQL_STORIES.map((s,i)=>({key:'s'+i,lvl:s.lvl,s,code:s.sql,lang:'sql',link:{h:'#sql-'+s.m+'-1',t:`Modul ${s.m}: ${SQL_MODULES[s.m-1].t}`}}));
  return STORIES.map((s,i)=>[s,i]).filter(([s])=>s[tk]).map(([s,i])=>{const x=FLAT[tk].find(y=>y.l.k==='lab'&&y.l.n===s.b);return {key:tk[0]+i,lvl:CH[s.b-1].lvl,s,code:s[tk],lang:tk,link:x?{h:'#'+x.id,t:`${x.title}`}:null}});
}
function storyCard(it,ix){
  const s=it.s,a=storyAns[it.key],ans=a!=null,ord=perm(s.o.length,ix+3),hid=storyHide&&!ans;
  return `<article class="story ${ans?(a===s.a?'is-ok':'is-bad'):''}" data-key="${it.key}">
   <div class="tags"><span class="tag">${it.lvl}</span>${ans?`<span class="tag ${a===s.a?'okt':'badt'}">${a===s.a?'Benar':'Belum tepat'}</span>`:''}</div>
   <h3>${esc(s.t)}</h3><p class="st">${esc(s.s)}</p>
   <button class="btn peek" aria-expanded="${!hid}">${hid?'Tampilkan':'Sembunyikan'} kode</button><div ${hid?'hidden':''}>${pane(it.lang,it.code,{copy:false})}</div>
   <b>${esc(s.q)}</b>
   <div class="opts">${ord.map(oi=>`<button class="opt ${ans?(oi===s.a?'right':(oi===a?'wrong':'')):''}" data-o="${oi}" ${ans?'disabled':''}>${esc(s.o[oi])}</button>`).join('')}</div>
   <p class="why" ${ans?'':'hidden'}>${ans?esc(s.w):''}</p>
   ${it.link?`<a class="more" href="${it.link.h}">Pelajari lagi: ${esc(it.link.t)} →</a>`:''}</article>`;
}
function renderStories(tk){
  const all=storiesOf(tk),list=all.filter(x=>storyLv==='Semua'||x.lvl===storyLv);
  const ans=all.filter(x=>storyAns[x.key]!=null),ok=ans.filter(x=>storyAns[x.key]===x.s.a);
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>Kuis cerita</span></nav>
   <div class="eyebrow">Kuis cerita</div><h1>Kode di kehidupan sehari-hari</h1>
   <p class="lead muted">Setiap soal adalah cerita kecil. Baca situasinya, bayangkan langkahnya, lalu tebak apa yang dilakukan kodenya.</p></header>
  <div class="tabs3" role="tablist" aria-label="Jalur">${TRACKS.filter(t=>['java','python','sql'].includes(t.k)).map(t=>`<a role="tab" class="t-${t.k}" href="#kuis-${t.k}" aria-selected="${t.k===tk}"><span class="tmark">${t.mark}</span>${t.name} <small>${storiesOf(t.k).length} soal</small></a>`).join('')}</div>
  <div class="score"><div><span class="big">${ok.length}</span><span class="of"> / ${all.length} benar</span></div>
   <div class="sc-bar"><div class="bar"><i style="width:${all.length?ans.length/all.length*100:0}%"></i></div><small>${ans.length} dari ${all.length} sudah dijawab</small></div>
   <label class="donebox hidebox"><input type="checkbox" id="stHide" ${storyHide?'checked':''}> Sembunyikan kode</label>
   <button class="btn" id="stReset" ${ans.length?'':'disabled'}>Ulangi</button></div>
  <div class="chips" role="group" aria-label="Tingkat" id="stLv">${['Semua',...LEVELS.map(L=>L.k)].map(L=>`<button class="chip" data-l="${L}" aria-pressed="${L===storyLv}">${L}</button>`).join('')}</div>
  <div class="stories" id="stories">${list.length?list.map((x,i)=>storyCard(x,all.indexOf(x))).join(''):'<p class="empty">Belum ada soal di tingkat ini.</p>'}</div>`;
}
function wireStories(tk){
  const all=storiesOf(tk);
  $('#stHide').onchange=e=>{storyHide=e.target.checked;store.set('rk-story-hide',storyHide);const y=scrollY;route();scrollTo(0,y)};
  $('#stLv').addEventListener('click',e=>{const b=e.target.closest('[data-l]');if(!b)return;storyLv=b.dataset.l;const y=scrollY;route();scrollTo(0,y)});
  $('#stories').addEventListener('click',e=>{
    const pk=e.target.closest('.peek');if(pk){const cd=pk.nextElementSibling,show=cd.hidden;cd.hidden=!show;pk.setAttribute('aria-expanded',show);pk.textContent=`${show?'Sembunyikan':'Tampilkan'} kode`;return}
    const b=e.target.closest('.opt');if(!b||b.disabled)return;const card=b.closest('.story'),it=all.find(x=>x.key===card.dataset.key);
    storyAns[it.key]=+b.dataset.o;store.set('rk-story2',storyAns);
    const tmp=document.createElement('div');tmp.innerHTML=storyCard(it,all.indexOf(it));card.replaceWith(tmp.firstElementChild);
    const ans=all.filter(x=>storyAns[x.key]!=null),ok=ans.filter(x=>storyAns[x.key]===x.s.a);
    $('.score .big').textContent=ok.length;$('.score .bar i').style.width=`${ans.length/all.length*100}%`;$('.score small').textContent=`${ans.length} dari ${all.length} sudah dijawab`;$('#stReset').disabled=false});
  $('#stReset').onclick=()=>{all.forEach(x=>delete storyAns[x.key]);store.set('rk-story2',storyAns);route()};
}

/* ===================== GLOSARIUM ===================== */
CATS.push('Basis Data');
[['sql-rdbms','Basis data relasional','relational database (RDBMS)','Basis data yang menyimpan data dalam tabel-tabel yang saling terhubung lewat kunci. Contoh: PostgreSQL, MySQL, SQLite, SQL Server, Oracle.'],
 ['sql-query','Query','query','Perintah untuk meminta atau mengubah data di basis data, ditulis dalam SQL.','SELECT nama FROM pelanggan;'],
 ['sql-tabel','Tabel, baris, kolom','table, row, column','Tabel menyimpan data sejenis. Setiap baris adalah satu catatan, setiap kolom satu atribut dengan tipe data tertentu.'],
 ['sql-pk','Primary key','primary key','Kolom (atau gabungan kolom) yang nilainya unik dan tidak boleh NULL, dipakai untuk menunjuk satu baris dengan pasti.','id INTEGER PRIMARY KEY'],
 ['sql-fk','Foreign key','foreign key','Kolom yang menunjuk primary key di tabel lain. Database menolak nilai yang tidak punya pasangan.','pelanggan_id INTEGER REFERENCES pelanggan(id)'],
 ['sql-constraint','Constraint','constraint','Aturan yang dijaga database: NOT NULL, UNIQUE, CHECK, PRIMARY KEY, FOREIGN KEY, DEFAULT.','harga INTEGER CHECK (harga > 0)'],
 ['sql-null','NULL (SQL)','NULL','Penanda nilai yang tidak diketahui atau tidak ada. Bukan 0 dan bukan teks kosong. Diperiksa dengan IS NULL, bukan = NULL.','WHERE kota IS NULL'],
 ['sql-ddl','DDL dan DML','data definition / manipulation language','DDL mengatur struktur (CREATE, ALTER, DROP). DML mengubah isi data (INSERT, UPDATE, DELETE). DQL membaca data (SELECT).'],
 ['sql-where','WHERE','WHERE clause','Klausa untuk menyaring baris berdasarkan kondisi sebelum dikelompokkan atau ditampilkan.','WHERE harga > 50000'],
 ['sql-agregat','Fungsi agregat','aggregate function','Fungsi yang meringkas banyak baris menjadi satu nilai: COUNT, SUM, AVG, MIN, MAX.','SELECT AVG(harga) FROM produk;'],
 ['sql-groupby','GROUP BY dan HAVING','GROUP BY / HAVING','GROUP BY mengelompokkan baris yang nilainya sama. HAVING menyaring kelompok setelah agregat dihitung.','GROUP BY kategori HAVING COUNT(*) > 1'],
 ['sql-join','JOIN','join','Menggabungkan baris dari dua tabel berdasarkan kondisi. INNER JOIN hanya yang cocok; LEFT JOIN mempertahankan semua baris tabel kiri.','FROM pesanan s JOIN pelanggan p ON s.pelanggan_id = p.id'],
 ['sql-subquery','Subquery','subquery','Query di dalam query lain, misalnya di WHERE atau FROM. Correlated subquery merujuk baris query luarnya.','WHERE harga > (SELECT AVG(harga) FROM produk)'],
 ['sql-view','View','view','Query yang disimpan dengan nama dan bisa dipakai seperti tabel. Tidak menyimpan data sendiri.','CREATE VIEW laris AS SELECT ...;'],
 ['sql-index','Index','index','Struktur data tambahan (biasanya B-tree) agar pencarian tidak perlu membaca seluruh tabel. Mempercepat baca, sedikit memperlambat tulis.','CREATE INDEX idx_kota ON pelanggan(kota);'],
 ['sql-transaksi','Transaksi','transaction','Sekelompok perintah yang diperlakukan sebagai satu kesatuan: COMMIT menyimpan semuanya, ROLLBACK membatalkan semuanya.','BEGIN; ... COMMIT;'],
 ['sql-acid','ACID','atomicity, consistency, isolation, durability','Empat jaminan transaksi: utuh (semua atau tidak sama sekali), konsisten dengan aturan, terisolasi dari transaksi lain, dan tahan lama setelah COMMIT.'],
 ['sql-normalisasi','Normalisasi','normalization','Merancang tabel agar data tidak berulang (1NF, 2NF, 3NF), dengan memecah data ke tabel terpisah yang dihubungkan foreign key.'],
 ['sql-injection','SQL injection','SQL injection','Serangan dengan menyisipkan potongan SQL lewat input pengguna. Dicegah dengan parameter (prepared statement), bukan menyambung string.'],
 ['sql-prepared','Prepared statement','prepared statement','Query dengan placeholder (?) yang nilainya dikirim terpisah, sehingga input selalu dianggap data, bukan perintah.','SELECT * FROM akun WHERE username = ?'],
 ['sql-cte','CTE','common table expression','Query bernama sementara yang ditulis dengan WITH di awal query. CTE rekursif bisa menelusuri hierarki seperti bagan organisasi.','WITH laris AS (SELECT ...) SELECT * FROM laris;'],
 ['sql-window','Window function','window function','Fungsi yang menghitung nilai dari sekelompok baris terkait tanpa menggabungkannya: ROW_NUMBER, RANK, LAG, LEAD, SUM OVER.','RANK() OVER (PARTITION BY divisi ORDER BY gaji DESC)'],
 ['sql-explain','EXPLAIN','query plan','Perintah untuk melihat rencana eksekusi query: tabel dibaca penuh (SCAN) atau lewat index (SEARCH).','EXPLAIN QUERY PLAN SELECT ...;'],
 ['sql-procedure','Stored procedure','stored procedure','Kumpulan perintah SQL yang disimpan di server database dan dipanggil dengan nama, misalnya CALL proses_gaji().']
].forEach(([id,t,en,d,ex])=>{const g={id,t,en,c:'Basis Data',d};if(ex)g.ex=ex;GL.push(g);GLMAP[id]=g});
const GLUSE={};
for(const n in TOPICS)TOPICS[n].forEach((tp,ti)=>{for(const k in tp.legend){const id=tp.legend[k][0];(GLUSE[id]=GLUSE[id]||[]);if(!GLUSE[id].some(u=>u.n==n&&u.ti===ti))GLUSE[id].push({n:+n,ti,k,t:tp.t})}});
const topicLesson=(n,ti)=>FLAT.java.find(x=>x.l.k==='topic'&&x.l.ref===n+'.'+ti)||FLAT.python.find(x=>x.l.k==='topic'&&x.l.ref===n+'.'+ti);
const labLesson=n=>FLAT.java.find(x=>x.l.k==='lab'&&x.l.n===n);
function renderGlossary(){
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>Glosarium</span></nav><div class="eyebrow">Kamus</div><h1>Glosarium istilah</h1>
  <p class="lead muted">${GL.length} istilah pemrograman dan basis data, lengkap dengan padanan bahasa Inggrisnya. Tombol "Tunjukkan di kode" membawamu ke bagian kode yang dimaksud.</p></header>
  <div class="gl-tools"><input class="gl-search" id="glq" type="search" placeholder="Cari istilah, misalnya rekursi, JOIN, atau polymorphism" aria-label="Cari istilah"></div>
  <div class="chips" id="glc">${['Semua',...CATS].map(k=>`<button class="chip" data-c="${k}" aria-pressed="false">${k}</button>`).join('')}</div>
  <div class="gl-list" id="gll"></div>`;
}
function drawGlossary(){
  const q=glState.q.trim().toLowerCase();
  document.querySelectorAll('#glc .chip').forEach(b=>b.setAttribute('aria-pressed',b.dataset.c===glState.cat));
  const list=GL.filter(g=>(glState.cat==='Semua'||g.c===glState.cat)&&(!q||(g.t+' '+g.en+' '+g.d).toLowerCase().includes(q))).sort((a,b)=>a.t.localeCompare(b.t,'id'));
  $('#gll').innerHTML=list.length?list.map(g=>{const s=CH.filter(c=>c.terms.includes(g.id)),u=(GLUSE[g.id]||[]).slice(0,4).filter(x=>topicLesson(x.n,x.ti));
    return `<article class="gl" id="t-${g.id}"><span class="cat">${g.c}</span><h3>${g.t}<small>${g.en}</small></h3><p>${esc(g.d)}</p>${g.ex?`<pre>${esc(g.ex)}</pre>`:''}${u.length?`<div class="show-in"><span>Tunjukkan di kode:</span>${u.map(x=>`<button class="show" data-n="${x.n}" data-ti="${x.ti}" data-k="${x.k}">${esc(x.t)}</button>`).join('')}</div>`:''}${s.length?`<div class="seen">Dibahas di: ${s.map(c=>{const x=labLesson(c.n);return x?`<a href="#${x.id}">${esc(c.t)}</a>`:''}).join('')}</div>`:''}</article>`}).join('')
    :`<p class="empty">Tidak ada istilah yang cocok dengan "${esc(glState.q)}". Coba kata lain atau pilih kategori Semua.</p>`;
}
function wireGlossary(){
  const inp=$('#glq');inp.value=glState.q;
  inp.addEventListener('input',()=>{glState.q=inp.value;glState.focus=null;drawGlossary()});
  $('#glc').addEventListener('click',e=>{const b=e.target.closest('.chip');if(!b)return;glState.cat=b.dataset.c;drawGlossary()});
  $('#gll').addEventListener('click',e=>{const b=e.target.closest('.show');if(!b)return;const x=topicLesson(+b.dataset.n,+b.dataset.ti);if(!x)return;pendingFocus={k:b.dataset.k};
    if(location.hash==='#'+x.id)route();else location.hash=x.id});
  drawGlossary();
  if(glState.focus){const el=document.getElementById('t-'+glState.focus);if(el){el.classList.add('flash');el.scrollIntoView({block:'center'});setTimeout(()=>el.classList.remove('flash'),2200)}glState.focus=null}
}
