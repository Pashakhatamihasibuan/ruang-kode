/* ===================== VISUAL 3D DI PELAJARAN =====================
   Adegan 3D ringan (CSS 3D, tanpa pustaka) yang menjelaskan konsep dengan benda:
   kotak variabel, deretan array, tumpukan stack, pohon, cetak biru class, lapisan box model, dll.
   Setiap adegan = daftar langkah; tiap langkah berisi keterangan dan benda-benda di panggung.
   Benda dengan id yang sama berpindah dengan animasi, sehingga perubahan mudah diikuti.
   Panggung bisa diputar dengan diseret atau tombol panah; tombol Berikutnya menjalankan langkah. */
(function(){
const RMq=()=>{try{return matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){return false}};
/* pembuat benda: B = balok, G = label melayang (selalu menghadap kamera), R = batang penghubung */
const B=(id,x,y,z,o={})=>({id,x,y,z,w:1,h:1,d:1,c:'acc',...o});
const G=(id,x,y,z,t,c='')=>({id,tag:1,x,y,z,t,c});
function R(id,a,b,c='mute'){const dx=b[0]-a[0],dy=b[1]-a[1],L=Math.hypot(dx,dy);
  return {id,x:(a[0]+b[0])/2,y:(a[1]+b[1])/2,z:a[2]||0,w:L,h:.08,d:.08,c,rz:Math.atan2(dy,dx)*180/Math.PI,rod:1}}
const lantai=(w=8,d=4,y=-.6)=>B('lantai',0,y,0,{w,h:.12,d,c:'floor'});

const S={};
/* ---------- variabel ---------- */
S.var={t:'Variabel sebagai kotak berlabel di memori',steps:(()=>{
  const rak=[lantai(7,3)],kotak=(id,x,nama)=>[B('k-'+id,x,0,0,{w:1.6,h:1.2,d:1.4,c:'glass'}),G('n-'+id,x,1.25,0,nama)];
  return [
   {cap:'Bayangkan memori komputer sebagai rak. Setiap variabel adalah <b>kotak berlabel</b>: labelnya nama variabel, isinya nilai.',it:[...rak]},
   {cap:'<code>umur = 17</code> membuat kotak bernama <b>umur</b>, lalu memasukkan nilai 17 ke dalamnya.',it:[...rak,...kotak('umur',-1.9,'umur'),B('v17',-1.9,-.05,0,{w:.8,h:.8,d:.8,t:'17',tt:'int'})]},
   {cap:'<code>nama = "Sari"</code> membuat kotak kedua. Setiap kotak hanya menyimpan <b>satu nilai</b> pada satu waktu.',it:[...rak,...kotak('umur',-1.9,'umur'),B('v17',-1.9,-.05,0,{w:.8,h:.8,d:.8,t:'17',tt:'int'}),...kotak('nama',1.9,'nama'),B('vS',1.9,-.05,0,{w:1.1,h:.8,d:.8,c:'ok',t:'"Sari"',tt:'teks'})]},
   {cap:'<code>umur = umur + 1</code>: nilai lama <b>diambil</b> dulu untuk dihitung (17 + 1)…',it:[...rak,...kotak('umur',-1.9,'umur'),B('v17',-1.9,2.1,0,{w:.8,h:.8,d:.8,t:'17',c:'warn'}),G('hit',-1.9,3.1,0,'17 + 1 = 18','warn'),...kotak('nama',1.9,'nama'),B('vS',1.9,-.05,0,{w:1.1,h:.8,d:.8,c:'ok',t:'"Sari"'})]},
   {cap:'…lalu hasilnya <b>menggantikan</b> isi lama. Nilai 17 hilang; kotak umur sekarang berisi 18. Nama kotaknya tetap sama.',it:[...rak,...kotak('umur',-1.9,'umur'),B('v18',-1.9,-.05,0,{w:.8,h:.8,d:.8,t:'18',tt:'int'}),...kotak('nama',1.9,'nama'),B('vS',1.9,-.05,0,{w:1.1,h:.8,d:.8,c:'ok',t:'"Sari"'})]}]})()};
/* ---------- array / list ---------- */
S.array={t:'Array: deretan kotak bernomor (indeks)',steps:(()=>{
  const v=[7,3,9,1,5],row=(hi=-1,extra)=>[lantai(9,3),...v.map((n,i)=>B('a'+i,(i-2.5)*1.25,0,0,{t:String(n),c:hi<0?'acc':i===hi?'warn':'mute',y:i===hi?.5:0})),...v.map((n,i)=>G('i'+i,(i-2.5)*1.25,-1,0.9,'['+i+']','idx')),...(extra||[])];
  return [
   {cap:'Array menyimpan banyak nilai <b>berurutan</b> dalam satu nama. Setiap kotak punya nomor urut yang disebut <b>indeks</b>.',it:row()},
   {cap:'Indeks dimulai dari <b>0</b>, bukan 1. Jadi <code>nilai[0]</code> adalah kotak pertama, yaitu 7.',it:row(0)},
   {cap:'<code>nilai[3]</code> adalah kotak <b>keempat</b>, isinya 1. Komputer langsung melompat ke kotak itu tanpa memeriksa kotak lain.',it:row(3)},
   {cap:'Menambah elemen di akhir (<code>append</code>/<code>push</code>/<code>add</code>) menaruh kotak baru di indeks berikutnya, yaitu 5.',it:row(-1,[B('a5',(5-2.5)*1.25,0,0,{t:'8',c:'ok'}),G('i5',(5-2.5)*1.25,-1,0.9,'[5]','idx')])},
   {cap:'Panjang array sekarang <b>6</b>, sedangkan indeks terakhirnya <b>5</b>. Indeks terakhir selalu panjang − 1.',it:row(-1,[B('a5',(5-2.5)*1.25,0,0,{t:'8',c:'ok'}),G('i5',(5-2.5)*1.25,-1,0.9,'[5]','idx'),G('len',.6,1.6,0,'panjang = 6','warn')])}]})()};
/* ---------- array 2D ---------- */
S.matrix={t:'Array dua dimensi: baris dan kolom',steps:(()=>{
  const R3=3,C4=4,val=(r,c)=>r*4+c+1;
  const grid=f=>{const any=[0,1,2].some(r=>[0,1,2,3].some(c=>f(r,c)));return [lantai(6.4,4.6),...[...Array(R3*C4)].map((_,k)=>{const r=Math.floor(k/C4),c=k%C4,s=f(r,c);return B('m'+k,(c-1.5)*1.3,s?.45:0,(r-1)*1.3,{t:String(val(r,c)),c:s||(any?'mute':'acc'),h:s?1.3:.6})}),
    ...[0,1,2].map(r=>G('r'+r,-3.5,0,(r-1)*1.3,'baris '+r,'idx')),...[0,1,2,3].map(c=>G('c'+c,(c-1.5)*1.3,-.4,2.4,'kolom '+c,'idx'))]};
  return [
   {cap:'Array 2D adalah <b>array berisi array</b>: seperti papan dengan baris dan kolom, misalnya kursi bioskop atau nilai siswa per mata pelajaran.',it:grid(()=>0)},
   {cap:'Satu baris (<code>m[1]</code>) adalah array biasa berisi 4 nilai.',it:grid(r=>r===1?'ok':0)},
   {cap:'Satu kolom (indeks kolom 2 di setiap baris) diambil dengan perulangan baris: <code>m[0][2]</code>, <code>m[1][2]</code>, <code>m[2][2]</code>.',it:grid((r,c)=>c===2?'warn':0)},
   {cap:'Satu sel ditunjuk dengan <b>dua indeks</b>: baris dulu, lalu kolom. <code>m[1][2]</code> = 7.',it:grid((r,c)=>r===1&&c===2?'warn':0)}]})()};
/* ---------- perulangan ---------- */
S.loop={t:'Perulangan sebagai tangga yang dinaiki satu per satu',steps:(()=>{
  const N=4,tangga=n=>[lantai(8,3),...[...Array(N)].map((_,i)=>B('s'+i,(i-1.5)*1.4,(i*.5)-.3,0,{w:1.3,h:.4+i*.0,d:1.6,c:i<n?'ok':'mute',t:'i='+i}))],
    bola=(i,y)=>B('bola',(i-1.5)*1.4,y,0,{w:.5,h:.5,d:.5,c:'warn',ball:1});
  const st=[{cap:'<code>for (i = 0; i &lt; 4; i++)</code>: perulangan mengulang badan kode selama kondisi masih benar. Bayangkan tangga 4 anak tangga.',it:[...tangga(0),bola(-1.1,0),G('cek',-2.8,1.6,0,'i = 0','warn')]}];
  for(let i=0;i<N;i++)st.push({cap:`Putaran ${i+1}: cek <code>i &lt; 4</code> → ${i} &lt; 4 <b>benar</b>, badan dijalankan (naik satu anak tangga), lalu <code>i++</code> menjadi ${i+1}.`,it:[...tangga(i+1),bola(i,i*.5+.35),G('cek',(i-1.5)*1.4,i*.5+1.5,0,`i = ${i} → ${i+1}`,'warn')]});
  st.push({cap:'Cek lagi: <code>i &lt; 4</code> → 4 &lt; 4 <b>salah</b>. Perulangan berhenti dan program lanjut ke baris setelahnya. Total 4 putaran.',it:[...tangga(N),bola(4,1.5),G('cek',3.6,2.6,0,'4 < 4 salah → keluar','bad')]});
  return st})()};
/* ---------- percabangan ---------- */
S.if={t:'Percabangan: jalan bercabang yang dipilih oleh kondisi',steps:(()=>{
  const jalan=(on)=>[lantai(9,5),B('j0',-2.6,-.45,0,{w:3,h:.1,d:1,c:'mute'}),B('jy',1.9,-.45,-1.3,{w:3.2,h:.1,d:.9,c:on==='y'?'ok':'mute',ry:-20}),B('jn',1.9,-.45,1.3,{w:3.2,h:.1,d:.9,c:on==='n'?'bad':'mute',ry:20}),
    B('gerbang',-.6,.3,0,{w:.9,h:1.5,d:1.4,c:'glass',t:'≥ 75?'}),G('ya',2.6,.5,-2,'ya: "Lulus"','ok'),G('tidak',2.6,.5,2,'tidak: "Remedial"','bad')];
  return [
   {cap:'<code>if (nilai &gt;= 75)</code> seperti persimpangan. Program tiba di gerbang kondisi lalu memilih <b>satu</b> jalan saja.',it:[...jalan(),B('bola',-3.8,0,0,{w:.5,h:.5,d:.5,c:'warn',ball:1,t:'80'})]},
   {cap:'nilai = 80. Kondisi <code>80 &gt;= 75</code> bernilai <b>true</b>…',it:[...jalan(),B('bola',-.6,1.4,0,{w:.5,h:.5,d:.5,c:'warn',ball:1,t:'80'})]},
   {cap:'…maka program masuk ke cabang <b>if</b> dan mencetak "Lulus". Cabang else dilewati sama sekali.',it:[...jalan('y'),B('bola',3,0,-1.7,{w:.5,h:.5,d:.5,c:'ok',ball:1,t:'80'})]},
   {cap:'Jika nilai = 60, kondisinya <b>false</b>, sehingga program masuk ke cabang <b>else</b> dan mencetak "Remedial".',it:[...jalan('n'),B('bola',3,0,1.7,{w:.5,h:.5,d:.5,c:'bad',ball:1,t:'60'})]}]})()};
/* ---------- stack ---------- */
S.stack={t:'Stack: tumpukan piring, yang terakhir masuk keluar pertama (LIFO)',steps:(()=>{
  const p=(id,k,c='acc')=>B(id,0,k*.55-.2,0,{w:2.4,h:.45,d:2.4,c,t:id});
  const base=[lantai(6,4),G('top',-2.9,2.2,0,'↓ push · ↑ pop di atas','idx')];
  return [
   {cap:'Stack bekerja seperti tumpukan piring: piring baru selalu ditaruh <b>di atas</b>.',it:[...base,p('A',0)]},
   {cap:'<code>push(B)</code> lalu <code>push(C)</code>: tumpukan bertambah tinggi.',it:[...base,p('A',0),p('B',1),p('C',2,'ok')]},
   {cap:'<code>peek()</code> hanya melihat piring paling atas (C) tanpa mengambilnya.',it:[...base,p('A',0),p('B',1),p('C',2,'warn')]},
   {cap:'<code>pop()</code> mengambil piring <b>teratas</b>, yaitu C, yang terakhir masuk. Inilah LIFO: Last In, First Out.',it:[...base,p('A',0),p('B',1),B('C',2.8,2.4,0,{w:2.4,h:.45,d:2.4,c:'bad',t:'C'})]},
   {cap:'Dipakai untuk tombol Undo, riwayat Back di browser, dan <b>call stack</b> saat fungsi memanggil fungsi lain.',it:[...base,p('A',0),p('B',1)]}]})()};
/* ---------- queue ---------- */
S.queue={t:'Queue: antrean kasir, yang pertama datang dilayani pertama (FIFO)',steps:(()=>{
  const o=(id,i,c='acc')=>B(id,i*1.2-1,0,0,{w:.9,h:1.3,d:.9,c,t:id});
  const kasir=[lantai(9,3),B('kasir',-3.4,0,0,{w:1,h:1.6,d:1.6,c:'glass',t:'kasir'}),G('dep',-2.2,1.7,0,'depan: keluar','idx'),G('bel',2.4,1.7,0,'belakang: masuk','idx')];
  return [
   {cap:'Queue seperti antrean kasir: orang baru masuk dari <b>belakang</b>, yang dilayani selalu yang paling <b>depan</b>.',it:[...kasir,o('Ani',0),o('Budi',1)]},
   {cap:'<code>enqueue(Citra)</code> menaruh Citra di belakang antrean.',it:[...kasir,o('Ani',0),o('Budi',1),o('Citra',2,'ok')]},
   {cap:'<code>dequeue()</code> melayani Ani, yang datang <b>pertama</b>. Inilah FIFO: First In, First Out.',it:[...kasir,B('Ani',-3.4,1.8,0,{w:.9,h:1.3,d:.9,c:'warn',t:'Ani'}),o('Budi',1),o('Citra',2)]},
   {cap:'Antrean maju: Budi sekarang di depan. Queue dipakai untuk antrean cetak, pesan masuk, dan BFS pada graf.',it:[...kasir,o('Budi',0),o('Citra',1)]}]})()};
/* ---------- rekursi / call stack ---------- */
S.rekursi={t:'Rekursi dan call stack: fungsi yang memanggil dirinya sendiri',steps:(()=>{
  const f=(n,k,c='acc',t)=>B('f'+n,0,k*.6-.2,0,{w:3.4,h:.5,d:2,c,t:t||`faktorial(${n})`});
  const base=[lantai(7,4)];const st=[];
  st.push({cap:'Setiap pemanggilan fungsi membuat <b>bingkai</b> baru di call stack. <code>faktorial(3)</code> dipanggil pertama.',it:[...base,f(3,0)]});
  st.push({cap:'faktorial(3) butuh faktorial(2), jadi bingkai baru ditumpuk di atasnya. faktorial(3) <b>menunggu</b>.',it:[...base,f(3,0,'mute'),f(2,1)]});
  st.push({cap:'faktorial(2) memanggil faktorial(1). Inilah <b>kasus dasar</b>: langsung mengembalikan 1 tanpa memanggil lagi.',it:[...base,f(3,0,'mute'),f(2,1,'mute'),f(1,2,'ok')]});
  st.push({cap:'Bingkai teratas selesai dan dibuang. Hasil 1 dikirim ke bawah: faktorial(2) = 2 × 1 = 2.',it:[...base,f(3,0,'mute'),f(2,1,'warn','faktorial(2) = 2'),G('r',2.4,2,0,'↩ 1','ok')]});
  st.push({cap:'faktorial(3) = 3 × 2 = <b>6</b>. Tumpukan kosong lagi. Tanpa kasus dasar, tumpukan terus tumbuh sampai <b>stack overflow</b>.',it:[...base,f(3,0,'ok','faktorial(3) = 6'),G('r',2.4,1.2,0,'↩ 2','ok')]});
  return st})()};
/* ---------- pohon (BST) dan DOM ---------- */
function pohon(nodes,edges,hi){const it=[lantai(9,3,-3.4)];
  edges.forEach(([a,b])=>{const A=nodes[a],Bn=nodes[b];it.push(R('e'+a+b,[A[0],A[1],0],[Bn[0],Bn[1],0],hi&&hi.includes(a)&&hi.includes(b)?'warn':'mute'))});
  Object.entries(nodes).forEach(([k,[x,y,t]])=>it.push(B('n'+k,x,y,0,{w:t.length>3?1.5:.9,h:.8,d:.8,c:!hi?'acc':hi.includes(k)?'warn':'mute',t})));return it}
S.tree={t:'Tree: data bercabang dari satu akar',steps:(()=>{
  const N={a:[0,1.6,'8'],b:[-2.2,0,'3'],c:[2.2,0,'10'],d:[-3.2,-1.6,'1'],e:[-1.2,-1.6,'6'],f:[3.2,-1.6,'14']},E=[['a','b'],['a','c'],['b','d'],['b','e'],['c','f']];
  return [
   {cap:'Tree menyusun data seperti silsilah terbalik: satu <b>akar</b> (8) di atas, bercabang ke <b>anak</b>, sampai <b>daun</b> di bawah.',it:pohon(N,E)},
   {cap:'Pada Binary Search Tree, anak kiri selalu lebih kecil dan anak kanan lebih besar. Mencari 6: mulai dari akar 8.',it:pohon(N,E,['a'])},
   {cap:'6 &lt; 8, jadi ke kiri ke 3. 6 &gt; 3, jadi ke kanan ke 6. <b>Ketemu</b> dalam 3 langkah, separuh data terlewati di setiap langkah.',it:pohon(N,E,['a','b','e'])}]})()};
S.dom={t:'DOM: halaman HTML sebagai pohon elemen',steps:(()=>{
  const N={a:[0,1.6,'html'],b:[-2.2,0,'head'],c:[2.2,0,'body'],d:[-2.2,-1.6,'title'],e:[1,-1.6,'h1'],f:[3.4,-1.6,'p']},E=[['a','b'],['a','c'],['b','d'],['c','e'],['c','f']];
  return [
   {cap:'Browser membaca HTML lalu membangun <b>DOM</b>: pohon objek. <code>&lt;html&gt;</code> adalah akarnya.',it:pohon(N,E)},
   {cap:'Elemen yang bersarang di dalam elemen lain menjadi <b>anak</b>. <code>h1</code> dan <code>p</code> adalah anak <code>body</code> dan saling bersaudara.',it:pohon(N,E,['c','e','f'])},
   {cap:'JavaScript menelusuri pohon ini: <code>document.querySelector("h1")</code> berjalan dari akar sampai menemukan simpulnya, lalu bisa mengubah isinya.',it:pohon(N,E,['a','c','e'])}]})()};
/* ---------- class dan objek ---------- */
S.oop={t:'Class sebagai cetak biru, objek sebagai benda jadinya',steps:(()=>{
  const cb=[B('cb',0,-.3,0,{w:5,h:.15,d:3,c:'glass'}),G('cbt',-3.4,-.3,0,'class Kucing { nama, warna, meong() }')];
  const obj=(id,x,t,c='acc')=>B(id,x,1.2,0,{w:1.3,h:1.3,d:1.3,c,t,tt:'objek'});
  return [
   {cap:'<b>Class</b> adalah cetak biru: daftar data (atribut) dan perilaku (method). Cetak biru sendiri belum menjadi kucing.',it:[lantai(8,5,-.8),...cb]},
   {cap:'<code>new Kucing("Oyen", "oranye")</code> membuat <b>objek</b> pertama dari cetak biru itu.',it:[lantai(8,5,-.8),...cb,obj('o1',-1.4,'Oyen','warn')]},
   {cap:'Objek kedua memakai cetak biru yang sama tetapi menyimpan <b>datanya sendiri</b>. Mengubah Belang tidak mengubah Oyen.',it:[lantai(8,5,-.8),...cb,obj('o1',-1.4,'Oyen','warn'),obj('o2',1.4,'Belang','ok')]},
   {cap:'<b>Pewarisan</b>: class Kucing dibangun di atas class Hewan, sehingga ikut memiliki atribut dan method Hewan seperti <code>makan()</code>.',it:[lantai(8,5,-1.8),B('hw',0,-1.3,0,{w:5,h:.15,d:3,c:'mute'}),G('hwt',-3.4,-1.3,0,'class Hewan { makan() }'),...cb,obj('o1',-1.4,'Oyen','warn'),obj('o2',1.4,'Belang','ok')]}]})()};
/* ---------- fungsi ---------- */
S.func={t:'Fungsi sebagai mesin: masukan diproses menjadi keluaran',steps:(()=>{
  const mesin=[lantai(9,3),B('mesin',0,.2,0,{w:2.2,h:1.6,d:1.6,c:'glass',t:'luas(p, l)',tt:'return p * l'})];
  return [
   {cap:'Fungsi adalah mesin bernama. Ia menerima <b>parameter</b>, menjalankan badannya, lalu <b>mengembalikan</b> hasil.',it:[...mesin,B('p',-3.6,0,0,{w:.7,h:.7,d:.7,t:'4',c:'warn'}),B('l',-2.7,0,0,{w:.7,h:.7,d:.7,t:'3',c:'warn'})]},
   {cap:'Pemanggilan <code>luas(4, 3)</code> memasukkan 4 dan 3 ke parameter p dan l.',it:[...mesin,B('p',-.5,.2,0,{w:.5,h:.5,d:.5,t:'4',c:'warn'}),B('l',.5,.2,0,{w:.5,h:.5,d:.5,t:'3',c:'warn'})]},
   {cap:'Mesin menghitung <code>4 * 3</code> dan mengeluarkan <b>12</b>. Nilai ini bisa disimpan: <code>hasil = luas(4, 3)</code>.',it:[...mesin,B('h',3.2,0,0,{w:.9,h:.9,d:.9,t:'12',c:'ok'})]},
   {cap:'Mesin yang sama dipakai ulang dengan masukan berbeda: <code>luas(5, 2)</code> menghasilkan 10. Tulis sekali, pakai berkali-kali.',it:[...mesin,B('h',3.2,0,0,{w:.9,h:.9,d:.9,t:'10',c:'ok'}),B('p',-3.6,0,0,{w:.7,h:.7,d:.7,t:'5',c:'mute'}),B('l',-2.7,0,0,{w:.7,h:.7,d:.7,t:'2',c:'mute'})]}]})()};
/* ---------- box model CSS ---------- */
S.box={t:'Box model: empat lapisan setiap elemen',steps:(()=>{
  const L=(gap,hi)=>[['margin',5.2,3.6,'mg'],['border',4.2,2.8,'bd'],['padding',3.8,2.4,'pd'],['konten',2.6,1.4,'ct']].map(([n,w,h,c],i)=>
    B('L'+i,0,0,i*gap,{w,h,d:.06,c:hi===undefined||hi===i?c:'mute',t:n,flat:1}));
  return [
   {cap:'Setiap elemen HTML adalah kotak. Dari depan terlihat datar, padahal tersusun dari <b>empat lapisan</b>.',it:L(.02)},
   {cap:'Kita pisahkan lapisannya. Paling dalam <b>konten</b> (teks/gambar), dibungkus <b>padding</b>, lalu <b>border</b>, lalu <b>margin</b>.',it:L(1)},
   {cap:'<b>padding</b> adalah ruang di dalam kotak, antara konten dan border. Warna latar ikut mengisi padding.',it:L(1,2)},
   {cap:'<b>border</b> adalah garis tepi kotak. Ketebalannya ikut menambah ukuran kotak.',it:L(1,1)},
   {cap:'<b>margin</b> adalah jarak di luar kotak ke elemen lain, selalu transparan.',it:L(1,0)},
   {cap:'Dengan <code>box-sizing: border-box</code>, <code>width</code> sudah termasuk padding dan border, sehingga ukuran kotak mudah ditebak.',it:[...L(.02),G('w',0,2.4,0,'width = konten + padding + border','warn')]}]})()};
/* ---------- z-index ---------- */
S.zindex={t:'z-index: urutan lapisan ke arah layar',steps:(()=>{
  const k=(id,x,y,z,c,t)=>B(id,x,y,z,{w:2.6,h:1.8,d:.06,c,t,flat:1});
  return [
   {cap:'Elemen yang bertumpuk punya urutan ke arah mata pengguna (sumbu z). Dari depan kita hanya melihat yang paling atas.',it:[k('A',-.8,.5,0,'acc','A z-index 1'),k('B',0,0,.8,'ok','B z-index 2'),k('C',.8,-.5,1.6,'warn','C z-index 3')]},
   {cap:'Diberi <code>z-index: 10</code>, kartu A <b>pindah ke lapisan paling depan</b>. Nilai lebih besar = lebih dekat ke pengguna.',it:[k('A',-.8,.5,2.4,'acc','A z-index 10'),k('B',0,0,.8,'ok','B z-index 2'),k('C',.8,-.5,1.6,'warn','C z-index 3')]},
   {cap:'z-index hanya bekerja pada elemen dengan <code>position</code> selain static (atau anak flex/grid), dan dibandingkan di dalam <b>stacking context</b> yang sama.',it:[k('A',-.8,.5,2.4,'acc','A z-index 10'),k('B',0,0,.8,'ok','B z-index 2'),k('C',.8,-.5,1.6,'warn','C z-index 3'),G('n',0,2,0,'position: relative','idx')]}]})()};
/* ---------- SQL JOIN ---------- */
S.join={t:'JOIN: menggabungkan dua tabel lewat kolom yang sama',steps:(()=>{
  const P=[['1','Ani'],['2','Budi'],['3','Citra']],O=[['1','Kopi'],['1','Teh'],['3','Roti']];
  const tab=(hi)=>[lantai(10,5,-2),G('tp',-3,2,0,'pelanggan','idx'),G('to',3,2,0,'pesanan','idx'),
    ...P.map(([id,n],i)=>B('p'+i,-3,1-i,0,{w:2.6,h:.7,d:.8,t:id+' · '+n,c:hi&&hi.p.includes(i)?'warn':'acc'})),
    ...O.map(([id,n],i)=>B('o'+i,3,1-i,0,{w:2.6,h:.7,d:.8,t:'pel '+id+' · '+n,c:hi&&hi.o.includes(i)?'warn':'ok'}))];
  const rod=(a,b)=>R('r'+a+b,[-1.7,1-a,0],[1.7,1-b,0],'warn');
  return [
   {cap:'Dua tabel terpisah: <b>pelanggan</b> dan <b>pesanan</b>. Kolom <code>pelanggan_id</code> di pesanan menunjuk ke id pelanggan.',it:tab()},
   {cap:'<code>JOIN ... ON pesanan.pelanggan_id = pelanggan.id</code> mencari pasangan baris yang nilainya sama.',it:[...tab({p:[0,2],o:[0,1,2]}),rod(0,0),rod(0,1),rod(2,2)]},
   {cap:'Setiap pasangan menjadi satu baris hasil. Ani muncul dua kali karena punya dua pesanan. Budi tidak muncul: tanpa pesanan, <b>INNER JOIN</b> membuangnya (LEFT JOIN akan mempertahankannya).',it:[lantai(10,5,-2),G('th',0,2,0,'hasil JOIN','idx'),
     ...[['Ani','Kopi'],['Ani','Teh'],['Citra','Roti']].map(([a,b],i)=>B('h'+i,0,1-i,0,{w:4,h:.7,d:.8,t:a+' · '+b,c:'warn'}))]}]})()};
/* ---------- git ---------- */
S.git={t:'Git: commit sebagai titik, branch sebagai jalur',steps:(()=>{
  const c=(id,x,y,col='acc')=>B(id,x,y,0,{w:.8,h:.8,d:.8,c:col,t:id,ball:1});
  const main=n=>[...[...Array(n)]].map((_,i)=>c('m'+(i+1),-3+i*1.5,0)),line=(a,b,col)=>R('l'+a+b,a,b,col);
  return [
   {cap:'Setiap <b>commit</b> adalah titik simpan seluruh proyek. Commit tersusun berurutan di branch <b>main</b>.',it:[lantai(10,4,-1.2),...main(3),line([-3,0],[0,0],'mute'),G('bm',-4.6,0,0,'main','idx')]},
   {cap:'<code>git switch -c fitur</code> membuat jalur baru yang bercabang dari commit terakhir. Commit di fitur tidak mengganggu main.',it:[lantai(10,4,-1.2),...main(3),line([-3,0],[0,0],'mute'),line([0,0],[1.5,1.6],'ok'),c('f1',1.5,1.6,'ok'),c('f2',3,1.6,'ok'),line([1.5,1.6],[3,1.6],'ok'),G('bm',-4.6,0,0,'main','idx'),G('bf',4.4,1.6,0,'fitur','ok')]},
   {cap:'<code>git merge fitur</code> menyatukan kembali: commit gabungan <b>M</b> di main berisi perubahan kedua jalur.',it:[lantai(10,4,-1.2),...main(3),line([-3,0],[0,0],'mute'),line([0,0],[1.5,1.6],'ok'),c('f1',1.5,1.6,'ok'),c('f2',3,1.6,'ok'),line([1.5,1.6],[3,1.6],'ok'),line([0,0],[4.5,0],'mute'),line([3,1.6],[4.5,0],'ok'),c('M',4.5,0,'warn'),G('bm',-4.6,0,0,'main','idx')]}]})()};

/* ---------- pencocokan pelajaran -> adegan ---------- */
const RULES=[[/box model/i,'box',1],[/z-index|stacking context/i,'zindex',1],[/\bjoin\b/i,'join',1],[/\bbranch|\bmerge\b|\bcommit\b/i,'git',1],
 [/rekursi|recursion|call stack/i,'rekursi'],[/\bqueue|antrean|antrian|\bdeque/i,'queue'],[/(?<!tech |full ?)\bstack\b|tumpukan/i,'stack'],[/\bdom\b/i,'dom',1],
 [/\btree\b|pohon|\bbst\b|\bheap\b/i,'tree'],[/\b2d\b|dua dimensi|matriks|matrix|multidimensi/i,'matrix'],[/\barray|larik|\blist\b|arraylist|koleksi|collection/i,'array'],
 [/perulangan|\bloop|\bfor\b|while|iterasi/i,'loop'],[/percabangan|\bif\b|kondisi|\bwhen\b|switch|keputusan/i,'if'],
 [/\bclass|kelas|\bobjek|\bobject|\boop\b|pewarisan|inheritance/i,'oop'],[/fungsi|function|\bmethod|metode|prosedur/i,'func'],[/variabel|variable|tipe data|val dan var/i,'var']];
const KODE=new Set(['java','python','js','jsx','ts','tsx','dart','kotlin','tx']),LOGIKA=/^(pseudo|flowg|logika|dsa|algo)$/;
window.v3dOf=function(t,title){if(!t||!title)return null;
  const kode=KODE.has(t.lang)||LOGIKA.test(t.k);
  for(const [rx,s,any] of RULES)if(rx.test(title)&&(any||kode))return s;return null};
window.V3DT=k=>S[k]&&S[k].t;

/* ---------- mesin panggung ---------- */
const FACES=[['f',0,0],['b',0,180],['r',0,90],['l',0,-90],['t',90,0],['u',-90,0]];
function blockHTML(o,U){const w=o.w*U,h=o.h*U,d=o.d*U,ln=o.t?`<b>${o.t}</b>`:'',tt=o.tt?`<i>${o.tt}</i>`:'';
  return FACES.map(([k,rx,ry])=>{const fw=k==='r'||k==='l'?d:w,fh=k==='t'||k==='u'?d:h,tz=k==='r'||k==='l'?w/2:k==='t'||k==='u'?h/2:d/2;
    if(o.flat&&k!=='f'&&k!=='b')return '';
    return `<div class="f3 f-${k}" style="width:${fw}px;height:${fh}px;transform:translate(-50%,-50%) rotateX(${rx}deg) rotateY(${ry}deg) translateZ(${tz}px)">${k==='f'?ln+(o.flat?'':''):k==='t'?tt:''}</div>`}).join('')}
function place(o,U){return `translate3d(${o.x*U}px,${-o.y*U}px,${o.z*U}px) rotateY(${o.ry||0}deg) rotateZ(${-(o.rz||0)}deg)`}

window.V3D=function(host,key){const sc=S[key];if(!sc)return;
  const rm=RMq();let i=0,rx=-20,ry=-28,auto=null,U=40;const els=new Map();
  host.innerHTML=`<div class="s3wrap"><div class="s3" tabindex="0" role="img" aria-label="Adegan 3D: ${sc.t}. Seret atau tekan tombol panah untuk memutar."><div class="s3cam"><div class="w3"></div></div><div class="s3tags"></div>
   <span class="s3hint" aria-hidden="true">⟲ seret untuk memutar</span></div>
   <p class="s3cap" aria-live="polite"></p>
   <div class="s3ctl"><button class="btn" data-a="prev">◀ Sebelumnya</button><span class="s3n"></span><button class="btn primary" data-a="next">Berikutnya ▶</button>
    <button class="btn" data-a="play" aria-pressed="false">▶ Putar otomatis</button><button class="tlink" data-a="view">Sudut awal</button></div></div>`;
  const st=host.querySelector('.s3'),w=host.querySelector('.w3'),cap=host.querySelector('.s3cap'),tg=host.querySelector('.s3tags'),n=host.querySelector('.s3n');
  /* label diproyeksikan ke 2D agar selalu terbaca dan tidak tertutup benda */
  const proj=(x,y,z)=>{const a=ry*Math.PI/180,b=rx*Math.PI/180,X=x*U,Y=-y*U,Z=z*U;
    const x1=X*Math.cos(a)+Z*Math.sin(a),z1=-X*Math.sin(a)+Z*Math.cos(a),y2=Y*Math.cos(b)-z1*Math.sin(b),z2=Y*Math.sin(b)+z1*Math.cos(b);
    const W=st.clientWidth,H=st.clientHeight,ox=W/2,oy=H*.4,cx=W/2,cy=H*.54,k=900/(900-z2);return [ox+(cx+x1-ox)*k,oy+(cy+y2-oy)*k]};
  const view=()=>{w.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg)`;
    const W=st.clientWidth;els.forEach(e=>{if(e._tag){const [l,t]=proj(...e._p),h=e.offsetWidth/2+4;e.style.left=Math.max(h,Math.min(W-h,l))+'px';e.style.top=t+'px'}})};
  function draw(){const s=sc.steps[i];U=Math.max(26,Math.min(58,st.clientWidth/10.5));const seen=new Set();
    s.it.forEach(o=>{seen.add(o.id);let e=els.get(o.id);const fresh=!e;
      if(fresh){e=document.createElement('div');els.set(o.id,e);(o.tag?tg:w).appendChild(e)}
      if(o.tag){e.className=`t3 ${o.c?'c-'+o.c:''}`;e.innerHTML=o.t;e._tag=1;e._p=[o.x,o.y,o.z]}
      else{e.className=`b3 c-${o.c}${o.ball?' ball':''}${o.rod?' rod':''}${o.flat?' flat':''}`;e.innerHTML=blockHTML(o,U);e.style.transform=place(o,U)}
      if(fresh&&!rm){e.classList.add('in');requestAnimationFrame(()=>requestAnimationFrame(()=>e.classList.remove('in')))}});
    els.forEach((e,id)=>{if(seen.has(id))return;els.delete(id);if(rm)e.remove();else{e.classList.add('out');setTimeout(()=>e.remove(),450)}});
    /* teks di sisi benda dikecilkan bila tidak muat (layar sempit) */
    w.querySelectorAll('.f3>b,.f3>i').forEach(t=>{const f=t.parentNode,cw=f.clientWidth-4,ch=f.clientHeight-2,sw=t.scrollWidth,sh=t.offsetHeight;
      const k=Math.min(1,cw/sw,ch/sh);t.style.transform=k<1?`scale(${Math.max(.35,k)})`:''});
    view();cap.innerHTML=s.cap;n.textContent=`${i+1} / ${sc.steps.length}`;
    host.querySelector('[data-a=prev]').disabled=i===0;host.querySelector('[data-a=next]').disabled=i===sc.steps.length-1}
  const stop=()=>{clearInterval(auto);auto=null;const b=host.querySelector('[data-a=play]');b.setAttribute('aria-pressed','false');b.textContent='▶ Putar otomatis'};
  host.querySelector('.s3ctl').addEventListener('click',e=>{const a=e.target.closest('[data-a]');if(!a)return;const k=a.dataset.a;
    if(k==='next'&&i<sc.steps.length-1){i++;draw()}
    else if(k==='prev'&&i>0){i--;draw()}
    else if(k==='view'){rx=-20;ry=-28;view()}
    else if(k==='play'){if(auto)return stop();if(i===sc.steps.length-1){i=0;draw()}a.setAttribute('aria-pressed','true');a.textContent='❚❚ Jeda';
      auto=setInterval(()=>{if(!host.isConnected)return stop();if(i>=sc.steps.length-1)return stop();i++;draw()},3200)}});
  let drag=null;
  st.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,rx,ry};st.setPointerCapture(e.pointerId);st.classList.add('grab')});
  st.addEventListener('pointermove',e=>{if(!drag)return;ry=drag.ry+(e.clientX-drag.x)*.45;rx=Math.max(-80,Math.min(25,drag.rx-(e.clientY-drag.y)*.35));view()});
  const up=()=>{drag=null;st.classList.remove('grab')};st.addEventListener('pointerup',up);st.addEventListener('pointercancel',up);
  st.addEventListener('keydown',e=>{const m={ArrowLeft:[0,-10],ArrowRight:[0,10],ArrowUp:[-8,0],ArrowDown:[8,0]}[e.key];if(!m)return;e.preventDefault();
    rx=Math.max(-80,Math.min(25,rx+m[0]));ry+=m[1];view()});
  let rw;window.addEventListener('resize',()=>{clearTimeout(rw);rw=setTimeout(()=>{if(host.isConnected){els.forEach(e=>e.remove());els.clear();draw()}},200)});
  draw();
};
})();
