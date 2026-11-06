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
/* Setiap adegan: t = judul, p = parameter yang bisa diubah pengguna (panel Eksperimen),
   steps(P) = daftar langkah yang dihitung ulang dari nilai parameter.
   Jenis parameter: n (angka, min..max), s (teks, daftar dipisah koma), o (pilihan). */
const angka=(s,max=7)=>String(s).split(/[,\s]+/).map(Number).filter(v=>Number.isFinite(v)).map(v=>Math.round(v)).slice(0,max);
const nama=(s,max=5)=>String(s).split(',').map(v=>v.trim().slice(0,8)).filter(Boolean).slice(0,max);
const E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* ---------- variabel ---------- */
S.var={t:'Variabel sebagai kotak berlabel di memori',
 p:[{k:'a',l:'Nilai awal umur',t:'n',min:-99,max:999,v:17},{k:'b',l:'Ditambah',t:'n',min:-99,max:99,v:1},{k:'nm',l:'Isi nama',t:'s',v:'Sari',ph:'teks'}],
 steps:P=>{const a=P.a,b=P.b,c=a+b,nm=E(String(P.nm).slice(0,10)||'""');
  const rak=[lantai(7,3)],kotak=(id,x,n)=>[B('k-'+id,x,0,0,{w:1.6,h:1.2,d:1.4,c:'glass'}),G('n-'+id,x,1.25,0,n)];
  const vU=(id,v,y=-.05,c='acc')=>B(id,-1.9,y,0,{w:.8,h:.8,d:.8,t:String(v),tt:'int',c}),vN=B('vS',1.9,-.05,0,{w:1.3,h:.8,d:.8,c:'ok',t:`"${nm}"`,tt:'teks'});
  return [
   {cap:'Bayangkan memori komputer sebagai rak. Setiap variabel adalah <b>kotak berlabel</b>: labelnya nama variabel, isinya nilai.',it:[...rak]},
   {cap:`<code>umur = ${a}</code> membuat kotak bernama <b>umur</b>, lalu memasukkan nilai ${a} ke dalamnya.`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v0',a)]},
   {cap:`<code>nama = "${nm}"</code> membuat kotak kedua. Setiap kotak hanya menyimpan <b>satu nilai</b> pada satu waktu.`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v0',a),...kotak('nama',1.9,'nama'),vN]},
   {cap:`<code>umur = umur + ${b}</code>: nilai lama <b>diambil</b> dulu untuk dihitung (${a} + ${b})…`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v0',a,2.1,'warn'),G('hit',-1.9,3.1,0,`${a} + ${b} = ${c}`,'warn'),...kotak('nama',1.9,'nama'),vN]},
   {cap:`…lalu hasilnya <b>menggantikan</b> isi lama. Nilai ${a} hilang; kotak umur sekarang berisi <b>${c}</b>. Nama kotaknya tetap sama.`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v1',c),...kotak('nama',1.9,'nama'),vN]}]}};

/* ---------- array / list ---------- */
S.array={t:'Array: deretan kotak bernomor (indeks)',
 p:[{k:'isi',l:'Isi array (pisahkan koma)',t:'s',v:'7, 3, 9, 1, 5'},{k:'ix',l:'Indeks yang diambil',t:'n',min:-3,max:9,v:3},{k:'add',l:'Nilai yang ditambahkan',t:'n',min:-99,max:999,v:8}],
 steps:P=>{let v=angka(P.isi,6);if(!v.length)v=[0];const L=v.length,ix=P.ix,X=i=>(i-(L)/2)*1.25;
  const row=(hi=-1,extra=[],n=L,vv=v)=>[lantai(Math.max(6,(n+1)*1.3+1),3),...vv.slice(0,n).map((x,i)=>B('a'+i,X(i),i===hi?.5:0,0,{t:String(x),c:hi<0?'acc':i===hi?'warn':'mute'})),...vv.slice(0,n).map((x,i)=>G('i'+i,X(i),-1,0.9,'['+i+']','idx')),...extra];
  const ok=ix>=0&&ix<L,v2=[...v,P.add];
  return [
   {cap:`Array ini menyimpan <b>${L} nilai</b> berurutan dalam satu nama. Setiap kotak punya nomor urut yang disebut <b>indeks</b>.`,it:row()},
   {cap:`Indeks dimulai dari <b>0</b>, bukan 1. Jadi <code>nilai[0]</code> adalah kotak pertama, yaitu ${v[0]}.`,it:row(0)},
   ok?{cap:`<code>nilai[${ix}]</code> adalah kotak ke-${ix+1}, isinya <b>${v[ix]}</b>. Komputer langsung melompat ke kotak itu tanpa memeriksa kotak lain.`,it:row(ix)}
     :{cap:`<code>nilai[${ix}]</code> <b>tidak ada</b>! Indeks yang sah hanya 0 sampai ${L-1}. Java melempar <code>ArrayIndexOutOfBoundsException</code>, Python <code>IndexError</code>${ix<0?' (kecuali Python: indeks negatif dihitung dari belakang, <code>nilai['+ix+']</code> = '+(v[L+ix]??'tetap error')+')':''}.`,
       it:row(-1,[B('ghost',X(ix),.5,0,{t:'?',c:'bad'}),G('err',X(Math.max(0,Math.min(L-1,ix))),2,0,'di luar batas!','bad')])},
   {cap:`Menambah ${P.add} di akhir (<code>append</code>/<code>push</code>/<code>add</code>) menaruh kotak baru di indeks berikutnya, yaitu ${L}.`,it:row(-1,[B('a'+L,X(L),0,0,{t:String(P.add),c:'ok'}),G('i'+L,X(L),-1,0.9,'['+L+']','idx')],L,v2)},
   {cap:`Panjang array sekarang <b>${L+1}</b>, sedangkan indeks terakhirnya <b>${L}</b>. Indeks terakhir selalu panjang − 1.`,it:row(-1,[B('a'+L,X(L),0,0,{t:String(P.add),c:'ok'}),G('i'+L,X(L),-1,0.9,'['+L+']','idx'),G('len',0,1.6,0,`panjang = ${L+1}`,'warn')],L,v2)}]}};

/* ---------- array 2D ---------- */
S.matrix={t:'Array dua dimensi: baris dan kolom',
 p:[{k:'r',l:'Jumlah baris',t:'n',min:1,max:4,v:3},{k:'c',l:'Jumlah kolom',t:'n',min:1,max:5,v:4},{k:'tr',l:'Ambil baris ke-',t:'n',min:0,max:5,v:1},{k:'tc',l:'Ambil kolom ke-',t:'n',min:0,max:6,v:2}],
 steps:P=>{const R3=P.r,C4=P.c,val=(r,c)=>r*C4+c+1,ok=P.tr<R3&&P.tc<C4;
  const grid=f=>{const any=[...Array(R3)].some((_,r)=>[...Array(C4)].some((_,c)=>f(r,c)));return [lantai(C4*1.3+1.4,R3*1.3+1.4),...[...Array(R3*C4)].map((_,k)=>{const r=Math.floor(k/C4),c=k%C4,s=f(r,c);return B('m'+r+'_'+c,(c-(C4-1)/2)*1.3,s?.45:0,(r-(R3-1)/2)*1.3,{t:String(val(r,c)),c:s||(any?'mute':'acc'),h:s?1.3:.6})}),
    ...[...Array(R3)].map((_,r)=>G('r'+r,-(C4/2)*1.3-1.2,0,(r-(R3-1)/2)*1.3,'baris '+r,'idx')),...[...Array(C4)].map((_,c)=>G('c'+c,(c-(C4-1)/2)*1.3,-.4,(R3/2)*1.3+.9,'kolom '+c,'idx'))]};
  const tr=Math.min(P.tr,R3-1),tc=Math.min(P.tc,C4-1);
  return [
   {cap:`Array 2D ini berukuran <b>${R3} × ${C4}</b>: ${R3} baris, masing-masing berisi ${C4} nilai. Total ${R3*C4} sel, seperti denah kursi bioskop.`,it:grid(()=>0)},
   {cap:`Satu baris (<code>m[${tr}]</code>) adalah array biasa berisi ${C4} nilai.`,it:grid(r=>r===tr?'ok':0)},
   {cap:`Satu kolom (kolom ${tc} di setiap baris) diambil dengan perulangan baris: ${[...Array(R3)].map((_,r)=>`<code>m[${r}][${tc}]</code>`).join(', ')}.`,it:grid((r,c)=>c===tc?'warn':0)},
   ok?{cap:`Satu sel ditunjuk dengan <b>dua indeks</b>: baris dulu, lalu kolom. <code>m[${P.tr}][${P.tc}]</code> = <b>${val(P.tr,P.tc)}</b>.`,it:grid((r,c)=>r===P.tr&&c===P.tc?'warn':0)}
     :{cap:`<code>m[${P.tr}][${P.tc}]</code> <b>di luar batas</b>. Baris yang sah 0–${R3-1} dan kolom 0–${C4-1}, jadi program akan error.`,it:[...grid(()=>0),G('err',0,2,0,'di luar batas!','bad')]}]}};

/* ---------- perulangan ---------- */
S.loop={t:'Perulangan sebagai tangga yang dinaiki satu per satu',
 p:[{k:'a',l:'Mulai (i = …)',t:'n',min:-3,max:10,v:0},{k:'z',l:'Batas (i < …)',t:'n',min:-3,max:20,v:4},{k:'s',l:'Langkah (i += …)',t:'n',min:1,max:5,v:1}],
 steps:P=>{const vals=[];for(let i=P.a;i<P.z&&vals.length<9;i+=P.s)vals.push(i);const N=vals.length,more=P.a+N*P.s<P.z;
  const X=k=>(k-(N-1)/2)*1.3,tangga=n=>[lantai(Math.max(6,N*1.4+2),3),...vals.map((v,k)=>B('s'+k,X(k),k*.4-.3,0,{w:1.2,h:.4,d:1.6,c:k<n?'ok':'mute',t:'i='+v}))],
    bola=(k,y)=>B('bola',N?X(k):0,y,0,{w:.5,h:.5,d:.5,c:'warn',ball:1});
  const kode=`<code>for (i = ${P.a}; i &lt; ${P.z}; i += ${P.s})</code>`;
  if(!N)return [{cap:`${kode}: kondisi awal <code>${P.a} &lt; ${P.z}</code> sudah <b>salah</b>, jadi badan perulangan <b>tidak pernah dijalankan</b> sama sekali (0 putaran).`,it:[lantai(6,3),bola(0,0),G('cek',0,1.3,0,`${P.a} < ${P.z} salah`,'bad')]}];
  const st=[{cap:`${kode}: perulangan mengulang badan kode selama kondisi masih benar. Nilai i: ${vals.join(', ')}${more?', …':''}. Ada <b>${N}${more?'+':''} anak tangga</b>.`,it:[...tangga(0),bola(-1.2,0),G('cek',X(0)-1.2,1.4,0,'i = '+P.a,'warn')]}];
  vals.forEach((v,k)=>st.push({cap:`Putaran ${k+1}: cek <code>i &lt; ${P.z}</code> → ${v} &lt; ${P.z} <b>benar</b>, badan dijalankan, lalu <code>i += ${P.s}</code> menjadi ${v+P.s}.`,it:[...tangga(k+1),bola(k,k*.4+.35),G('cek',X(k),k*.4+1.5,0,`i = ${v} → ${v+P.s}`,'warn')]}));
  const end=P.a+N*P.s;
  st.push(more?{cap:`(Tangga dipotong di 9 putaran agar muat di layar; perulangan sebenarnya masih berlanjut sampai i ≥ ${P.z}.)`,it:[...tangga(N),bola(N-1,(N-1)*.4+.35)]}
   :{cap:`Cek lagi: <code>i &lt; ${P.z}</code> → ${end} &lt; ${P.z} <b>salah</b>. Perulangan berhenti. Total <b>${N} putaran</b>.`,it:[...tangga(N),bola(N,N*.4+.2),G('cek',X(N-1)+.6,N*.4+1.6,0,`${end} < ${P.z} salah → keluar`,'bad')]});
  return st}};

/* ---------- percabangan ---------- */
S.if={t:'Percabangan: jalan bercabang yang dipilih oleh kondisi',
 p:[{k:'n',l:'Nilai siswa',t:'n',min:0,max:100,v:80},{k:'b',l:'Batas lulus (≥)',t:'n',min:0,max:100,v:75}],
 steps:P=>{const lulus=P.n>=P.b;
  const jalan=(on)=>[lantai(9,5),B('j0',-2.6,-.45,0,{w:3,h:.1,d:1,c:'mute'}),B('jy',1.9,-.45,-1.3,{w:3.2,h:.1,d:.9,c:on==='y'?'ok':'mute',ry:-20}),B('jn',1.9,-.45,1.3,{w:3.2,h:.1,d:.9,c:on==='n'?'bad':'mute',ry:20}),
    B('gerbang',-.6,.3,0,{w:.9,h:1.5,d:1.4,c:'glass',t:'≥ '+P.b+'?'}),G('ya',2.6,.5,-2,'ya: "Lulus"','ok'),G('tidak',2.6,.5,2,'tidak: "Remedial"','bad')];
  const bola=(x,y,z,c)=>B('bola',x,y,z,{w:.55,h:.55,d:.55,c,ball:1,t:String(P.n)});
  return [
   {cap:`<code>if (nilai &gt;= ${P.b})</code> seperti persimpangan. Program tiba di gerbang kondisi lalu memilih <b>satu</b> jalan saja.`,it:[...jalan(),bola(-3.8,0,0,'warn')]},
   {cap:`nilai = ${P.n}. Kondisi <code>${P.n} &gt;= ${P.b}</code> bernilai <b>${lulus}</b>…`,it:[...jalan(),bola(-.6,1.4,0,'warn')]},
   lulus?{cap:'…maka program masuk ke cabang <b>if</b> dan mencetak "Lulus". Cabang else dilewati sama sekali.',it:[...jalan('y'),bola(3,0,-1.7,'ok')]}
        :{cap:'…maka program masuk ke cabang <b>else</b> dan mencetak "Remedial". Cabang if dilewati sama sekali.',it:[...jalan('n'),bola(3,0,1.7,'bad')]},
   {cap:`Coba ubah angkanya di panel Eksperimen. ${P.n===P.b?'Perhatikan: nilai <b>sama dengan</b> batas tetap lulus karena operatornya <code>&gt;=</code>. Dengan <code>&gt;</code> hasilnya akan berbeda.':'Uji juga nilai yang <b>persis sama</b> dengan batas, karena di situlah bug sering bersembunyi.'}`,it:[...jalan(lulus?'y':'n'),bola(3,0,lulus?-1.7:1.7,lulus?'ok':'bad')]}]}};

/* ---------- stack ---------- */
S.stack={t:'Stack: tumpukan piring, yang terakhir masuk keluar pertama (LIFO)',
 p:[{k:'n',l:'Jumlah push',t:'n',min:1,max:6,v:3},{k:'k',l:'Jumlah pop',t:'n',min:0,max:6,v:1}],
 steps:P=>{const L='ABCDEF'.slice(0,P.n).split(''),k=Math.min(P.k,P.n);
  const p=(id,i,c='acc',x=0,y)=>B(id,x,y??i*.55-.2,0,{w:2.4,h:.45,d:2.4,c,t:id});
  const base=[lantai(7,4),G('top',-3,2.4,0,'↓ push · ↑ pop di atas','idx')];
  const keluar=L.slice(L.length-k).reverse();
  return [
   {cap:`Stack bekerja seperti tumpukan piring: piring baru selalu ditaruh <b>di atas</b>. Kita akan push ${P.n} piring.`,it:[...base,p(L[0],0)]},
   {cap:`${L.map(x=>`<code>push(${x})</code>`).join(' ')}: tumpukan setinggi ${P.n}. Piring ${L[L.length-1]} ada di paling atas.`,it:[...base,...L.map((x,i)=>p(x,i,i===L.length-1?'ok':'acc'))]},
   {cap:`<code>peek()</code> hanya melihat piring paling atas (${L[L.length-1]}) tanpa mengambilnya.`,it:[...base,...L.map((x,i)=>p(x,i,i===L.length-1?'warn':'acc'))]},
   k?{cap:`${k}× <code>pop()</code> mengambil dari atas: ${keluar.join(', ')}. Yang terakhir masuk keluar pertama (LIFO).${P.k>P.n?` Pop ke-${P.n+1} akan error karena stack sudah kosong.`:''}`,
      it:[...base,...L.map((x,i)=>i>=L.length-k?p(x,i,'bad',3,(L.length-1-i)*.55+.6):p(x,i))]}
    :{cap:'Tanpa <code>pop()</code>, semua piring tetap di tumpukan.',it:[...base,...L.map((x,i)=>p(x,i))]},
   {cap:`Sisa di stack: ${L.length-k?L.slice(0,L.length-k).join(', '):'kosong'}. Stack dipakai untuk Undo, tombol Back di browser, dan <b>call stack</b>.`,it:[...base,...L.slice(0,L.length-k).map((x,i)=>p(x,i))]}]}};

/* ---------- queue ---------- */
S.queue={t:'Queue: antrean kasir, yang pertama datang dilayani pertama (FIFO)',
 p:[{k:'q',l:'Yang datang (urut, pisahkan koma)',t:'s',v:'Ani, Budi, Citra'},{k:'k',l:'Jumlah dilayani',t:'n',min:0,max:5,v:1}],
 steps:P=>{let Q=nama(P.q,5);if(!Q.length)Q=['Ani'];const k=Math.min(P.k,Q.length);
  const o=(id,i,c='acc')=>B('q-'+id,i*1.15-1.6,0,0,{w:.95,h:1.3,d:.9,c,t:E(id)});
  const kasir=[lantai(10,3),B('kasir',-3.6,0,0,{w:1,h:1.6,d:1.6,c:'glass',t:'kasir'}),G('dep',-2.4,1.8,0,'depan: keluar','idx'),G('bel',2.6,1.8,0,'belakang: masuk','idx')];
  return [
   {cap:`Queue seperti antrean kasir: orang baru masuk dari <b>belakang</b>, yang dilayani selalu yang paling <b>depan</b>. ${E(Q[0])} datang pertama.`,it:[...kasir,o(Q[0],0)]},
   {cap:`${Q.slice(1).map(x=>`<code>enqueue(${E(x)})</code>`).join(' ')||'Tidak ada yang datang lagi.'} Setiap orang baru berdiri di belakang.`,it:[...kasir,...Q.map((x,i)=>o(x,i,i?'ok':'acc'))]},
   k?{cap:`${k}× <code>dequeue()</code> melayani ${Q.slice(0,k).map(E).join(', ')}: yang datang <b>pertama</b> dilayani pertama (FIFO).${P.k>Q.length?' Dequeue berikutnya error karena antrean kosong.':''}`,it:[...kasir,...Q.map((x,i)=>i<k?B('q-'+x,-3.6,1.9+i*.2,0,{w:.95,h:1.3,d:.9,c:'warn',t:E(x)}):o(x,i))]}
    :{cap:'Belum ada yang dilayani; antrean tetap utuh.',it:[...kasir,...Q.map((x,i)=>o(x,i))]},
   {cap:`Antrean maju: ${Q.length-k?E(Q[k])+' sekarang di depan':'antrean kosong'}. Queue dipakai untuk antrean cetak, pesan masuk, dan BFS pada graf.`,it:[...kasir,...Q.slice(k).map((x,i)=>o(x,i))]}]}};

/* ---------- rekursi / call stack ---------- */
S.rekursi={t:'Rekursi dan call stack: fungsi yang memanggil dirinya sendiri',
 p:[{k:'n',l:'Hitung faktorial(n), n =',t:'n',min:1,max:6,v:3}],
 steps:P=>{const N=P.n,fak=n=>n<=1?1:n*fak(n-1);
  const f=(n,k,c='acc',t)=>B('f'+n,0,k*.6-.2,0,{w:3.6,h:.5,d:2,c,t:t||`faktorial(${n})`});
  const base=[lantai(7,4)],st=[];
  for(let d=0;d<N;d++){const n=N-d,frames=[...Array(d+1)].map((_,j)=>f(N-j,j,j===d?(n===1?'ok':'acc'):'mute'));
    st.push({cap:d===0?`Setiap pemanggilan fungsi membuat <b>bingkai</b> baru di call stack. <code>faktorial(${N})</code> dipanggil pertama.`
      :n===1?`faktorial(2) memanggil faktorial(1). Inilah <b>kasus dasar</b>: langsung mengembalikan 1 tanpa memanggil lagi. Tumpukan setinggi ${N} bingkai.`
      :`faktorial(${n+1}) butuh faktorial(${n}), jadi bingkai baru ditumpuk. Bingkai di bawahnya <b>menunggu</b>.`,it:[...base,...frames]})}
  for(let n=2;n<=N;n++){const k=N-n,frames=[...Array(k+1)].map((_,j)=>j===k?f(N-j,j,'warn',`faktorial(${n}) = ${fak(n)}`):f(N-j,j,'mute'));
    st.push({cap:`Bingkai teratas selesai dan dibuang. Hasil ${fak(n-1)} dikirim ke bawah: faktorial(${n}) = ${n} × ${fak(n-1)} = <b>${fak(n)}</b>.`,it:[...base,...frames,G('r',2.6,k*.6+.8,0,'↩ '+fak(n-1),'ok')]})}
  st.push({cap:`Hasil akhir faktorial(${N}) = <b>${fak(N)}</b>. Ada ${N} bingkai yang pernah ditumpuk. Tanpa kasus dasar, tumpukan terus tumbuh sampai <b>stack overflow</b>.`,it:[...base,f(N,0,'ok',`faktorial(${N}) = ${fak(N)}`)]});
  return st}};

/* ---------- pohon (BST) dan DOM ---------- */
function pohon(nodes,edges,hi,bad){const ys=Object.values(nodes).map(n=>n[1]),it=[lantai(9,3,Math.min(...ys)-1.8)];
  edges.forEach(([a,b])=>{const A=nodes[a],Bn=nodes[b];it.push(R('e'+a+'_'+b,[A[0],A[1],0],[Bn[0],Bn[1],0],hi&&hi.includes(String(a))&&hi.includes(String(b))?'warn':'mute'))});
  Object.entries(nodes).forEach(([k,[x,y,t]])=>it.push(B('n'+k,x,y,0,{w:t.length>3?1.5:.9,h:.8,d:.8,c:!hi?'acc':hi.includes(k)?(bad&&k===hi[hi.length-1]?'bad':'warn'):'mute',t})));return it}
S.tree={t:'Tree: data bercabang dari satu akar',
 p:[{k:'isi',l:'Angka yang disisipkan (urut)',t:'s',v:'8, 3, 10, 1, 6, 14'},{k:'cari',l:'Angka yang dicari',t:'n',min:-99,max:999,v:6}],
 steps:P=>{let v=[...new Set(angka(P.isi,9))];if(!v.length)v=[8];
  const T={};const ins=(x)=>{let c=v[0],d=0;if(!T[c])T[c]={d:0};if(x===c)return;for(;;){d++;const s=x<c?'l':'r';if(T[c][s]==null){T[c][s]=x;T[x]={d,p:c};return}c=T[c][s]}};
  v.forEach(ins);const order=[];(function io(n){if(n==null)return;io(T[n].l);order.push(n);io(T[n].r)})(v[0]);
  const W=order.length,N={},Ed=[];order.forEach((n,i)=>{N[n]=[(i-(W-1)/2)*Math.min(1.3,8/W),1.6-T[n].d*1.4,String(n)];if(T[n].p!=null)Ed.push([T[n].p,n])});
  const path=[];let c=v[0],found=false;while(c!=null){path.push(String(c));if(c===P.cari){found=true;break}c=P.cari<c?T[c].l:T[c].r}
  const maxd=Math.max(...order.map(n=>T[n].d))+1;
  const st=[{cap:`Angka ${v.join(', ')} disisipkan berurutan ke Binary Search Tree: yang lebih kecil ke kiri, yang lebih besar ke kanan. Akarnya ${v[0]}, tingginya ${maxd} tingkat.`,it:pohon(N,Ed)}];
  path.forEach((x,i)=>{const n=+x,last=i===path.length-1;
    st.push({cap:last&&found?`<b>${P.cari} ketemu</b> dalam ${i+1} langkah, tanpa memeriksa ${W-i-1} simpul lainnya.`
      :`Bandingkan ${P.cari} dengan ${n}: ${P.cari<n?`lebih kecil, ke <b>kiri</b>`:`lebih besar, ke <b>kanan</b>`}${(P.cari<n?T[n].l:T[n].r)==null?', tetapi cabang itu kosong.':'.'}`,it:pohon(N,Ed,path.slice(0,i+1))})});
  if(!found)st.push({cap:`Cabangnya kosong, jadi <b>${P.cari} tidak ada</b> di pohon. Pencarian berhenti setelah ${path.length} langkah saja.`,it:pohon(N,Ed,path,true)});
  return st}};
S.dom={t:'DOM: halaman HTML sebagai pohon elemen',steps:(()=>{
  const N={a:[0,1.6,'html'],b:[-2.2,0,'head'],c:[2.2,0,'body'],d:[-2.2,-1.6,'title'],e:[1,-1.6,'h1'],f:[3.4,-1.6,'p']},Ed=[['a','b'],['a','c'],['b','d'],['c','e'],['c','f']];
  return [
   {cap:'Browser membaca HTML lalu membangun <b>DOM</b>: pohon objek. <code>&lt;html&gt;</code> adalah akarnya.',it:pohon(N,Ed)},
   {cap:'Elemen yang bersarang di dalam elemen lain menjadi <b>anak</b>. <code>h1</code> dan <code>p</code> adalah anak <code>body</code> dan saling bersaudara.',it:pohon(N,Ed,['c','e','f'])},
   {cap:'JavaScript menelusuri pohon ini: <code>document.querySelector("h1")</code> berjalan dari akar sampai menemukan simpulnya, lalu bisa mengubah isinya.',it:pohon(N,Ed,['a','c','e'])}]})()};

/* ---------- class dan objek ---------- */
S.oop={t:'Class sebagai cetak biru, objek sebagai benda jadinya',
 p:[{k:'o',l:'Nama objek (pisahkan koma)',t:'s',v:'Oyen, Belang'}],
 steps:P=>{let O=nama(P.o,4);if(!O.length)O=['Oyen'];const X=i=>(i-(O.length-1)/2)*1.7,C=['warn','ok','acc','bad'];
  const cb=[B('cb',0,-.3,0,{w:Math.max(5,O.length*1.8),h:.15,d:3,c:'glass'}),G('cbt',-3.4,-.3,0,'class Kucing { nama, warna, meong() }')];
  const obj=(i,c)=>B('o'+i,X(i),1.2,0,{w:1.3,h:1.3,d:1.3,c,t:E(O[i]),tt:'objek'});
  return [
   {cap:'<b>Class</b> adalah cetak biru: daftar data (atribut) dan perilaku (method). Cetak biru sendiri belum menjadi kucing.',it:[lantai(8,5,-.8),...cb]},
   {cap:`<code>new Kucing("${E(O[0])}")</code> membuat <b>objek</b> pertama dari cetak biru itu.`,it:[lantai(8,5,-.8),...cb,obj(0,C[0])]},
   {cap:O.length>1?`${O.length} objek dibuat dari cetak biru yang sama, masing-masing menyimpan <b>datanya sendiri</b>. Mengubah ${E(O[1])} tidak mengubah ${E(O[0])}.`:'Tambahkan nama lain di panel Eksperimen untuk membuat objek kedua dari cetak biru yang sama.',it:[lantai(8,5,-.8),...cb,...O.map((_,i)=>obj(i,C[i]))]},
   {cap:'<b>Pewarisan</b>: class Kucing dibangun di atas class Hewan, sehingga semua objek ikut memiliki method Hewan seperti <code>makan()</code>.',it:[lantai(8,5,-1.8),B('hw',0,-1.3,0,{w:Math.max(5,O.length*1.8),h:.15,d:3,c:'mute'}),G('hwt',-3.4,-1.3,0,'class Hewan { makan() }'),...cb,...O.map((_,i)=>obj(i,C[i]))]}]}};

/* ---------- fungsi ---------- */
S.func={t:'Fungsi sebagai mesin: masukan diproses menjadi keluaran',
 p:[{k:'p',l:'Panjang (p)',t:'n',min:-99,max:999,v:4},{k:'l',l:'Lebar (l)',t:'n',min:-99,max:999,v:3},{k:'op',l:'Isi fungsi',t:'o',o:[['*','return p * l (luas)'],['+','return 2 * (p + l) (keliling)']],v:'*'}],
 steps:P=>{const kel=P.op==='+',nm=kel?'keliling':'luas',h=kel?2*(P.p+P.l):P.p*P.l,rumus=kel?`2 * (${P.p} + ${P.l})`:`${P.p} * ${P.l}`;
  const mesin=[lantai(9,3),B('mesin',0,.2,0,{w:2.4,h:1.6,d:1.6,c:'glass',t:`${nm}(p, l)`,tt:kel?'return 2*(p+l)':'return p * l'})];
  const q=(id,x,y,v,s=.7,c='warn')=>B(id,x,y,0,{w:s,h:s,d:s,t:String(v),c});
  return [
   {cap:'Fungsi adalah mesin bernama. Ia menerima <b>parameter</b>, menjalankan badannya, lalu <b>mengembalikan</b> hasil.',it:[...mesin,q('p',-3.8,0,P.p),q('l',-2.8,0,P.l)]},
   {cap:`Pemanggilan <code>${nm}(${P.p}, ${P.l})</code> memasukkan ${P.p} ke p dan ${P.l} ke l.`,it:[...mesin,q('p',-.55,.2,P.p,.5),q('l',.55,.2,P.l,.5)]},
   {cap:`Mesin menghitung <code>${rumus}</code> dan mengembalikan <b>${h}</b>. Nilai ini bisa disimpan: <code>hasil = ${nm}(${P.p}, ${P.l})</code>.`,it:[...mesin,q('h',3.3,0,h,.95,'ok')]},
   {cap:`Mesin yang sama bisa dipakai ulang dengan masukan lain, atau isinya diganti (lihat pilihan "Isi fungsi"). Tulis sekali, pakai berkali-kali.`,it:[...mesin,q('h',3.3,0,h,.95,'ok'),q('p',-3.8,0,P.p,.7,'mute'),q('l',-2.8,0,P.l,.7,'mute')]}]}};

/* ---------- box model CSS ---------- */
S.box={t:'Box model: empat lapisan setiap elemen',
 p:[{k:'w',l:'width (px)',t:'n',min:20,max:400,v:200},{k:'pd',l:'padding (px)',t:'n',min:0,max:80,v:20},{k:'bd',l:'border (px)',t:'n',min:0,max:30,v:5},{k:'mg',l:'margin (px)',t:'n',min:0,max:80,v:16},
   {k:'bs',l:'box-sizing',t:'o',o:[['content-box','content-box'],['border-box','border-box']],v:'content-box'}],
 steps:P=>{const bb=P.bs==='border-box',konten=bb?Math.max(0,P.w-2*P.pd-2*P.bd):P.w,lebar=konten+2*P.pd+2*P.bd,total=lebar+2*P.mg;
  const sc=5.4/Math.max(total,1),hc=.55;/* tinggi konten tetap 60px agar fokus pada lebar */
  const ch=60,dims=[['margin',total,ch+2*(P.pd+P.bd+P.mg),'mg'],['border',lebar,ch+2*(P.pd+P.bd),'bd'],['padding',konten+2*P.pd,ch+2*P.pd,'pd'],['konten',konten,ch,'ct']];
  const L=(gap,hi)=>dims.map(([n,w,h,c],i)=>B('L'+i,0,0,i*gap,{w:Math.max(.05,w*sc),h:Math.max(.05,h*sc*hc*1.6),d:.06,c:hi===undefined||hi===i?c:'mute',t:n,flat:1}));
  return [
   {cap:'Setiap elemen HTML adalah kotak. Dari depan terlihat datar, padahal tersusun dari <b>empat lapisan</b>.',it:L(.02)},
   {cap:'Kita pisahkan lapisannya. Paling dalam <b>konten</b>, dibungkus <b>padding</b>, lalu <b>border</b>, lalu <b>margin</b>.',it:L(1)},
   {cap:`<b>padding ${P.pd}px</b> adalah ruang di dalam kotak, di kiri dan kanan konten. Warna latar ikut mengisi padding.`,it:L(1,2)},
   {cap:`<b>border ${P.bd}px</b> adalah garis tepi kotak. ${bb?'Dengan border-box, border mengambil ruang dari dalam width.':'Ketebalannya menambah lebar kotak.'}`,it:L(1,1)},
   {cap:`<b>margin ${P.mg}px</b> adalah jarak di luar kotak ke elemen lain, selalu transparan dan tidak ikut dihitung dalam lebar kotak.`,it:L(1,0)},
   {cap:bb?`<code>box-sizing: border-box</code>: lebar kotak tetap <b>${lebar}px</b> sesuai width, kontennya menyusut menjadi ${P.w} − 2×${P.pd} − 2×${P.bd} = <b>${konten}px</b>.${P.w<2*P.pd+2*P.bd?' Padding dan border lebih besar dari width, jadi konten tidak punya ruang!':''}`
     :`<code>box-sizing: content-box</code>: width ${P.w}px hanya untuk konten. Lebar kotak sebenarnya ${P.w} + 2×${P.pd} + 2×${P.bd} = <b>${lebar}px</b>, plus margin menjadi ${total}px ruang. Coba ganti ke border-box.`,
    it:[...L(.02),G('wd',0,(ch+2*(P.pd+P.bd+P.mg))*sc*hc*.8+.6,0,`lebar kotak = ${lebar}px · konten = ${konten}px`,'warn')]}]}};

/* ---------- z-index ---------- */
S.zindex={t:'z-index: urutan lapisan ke arah layar',
 p:[{k:'a',l:'z-index kartu A',t:'n',min:-10,max:99,v:1},{k:'b',l:'z-index kartu B',t:'n',min:-10,max:99,v:2},{k:'c',l:'z-index kartu C',t:'n',min:-10,max:99,v:3}],
 steps:P=>{const cards=[['A',P.a,'acc',-.8,.5],['B',P.b,'ok',0,0],['C',P.c,'warn',.8,-.5]];
  const urut=cards.map((c,i)=>({c,i})).sort((x,y)=>x.c[1]-y.c[1]||x.i-y.i);const rank={};urut.forEach((o,r)=>rank[o.c[0]]=r);
  const k=(z)=>cards.map(([id,zi,c,x,y],i)=>B(id,x,y,z?rank[id]*.9:i*.9,{w:2.6,h:1.8,d:.06,c,t:`${id} z-index ${zi}`,flat:1}));
  const atas=urut[2].c[0],seri=new Set([P.a,P.b,P.c]).size<3;
  return [
   {cap:'Tiga kartu bertumpuk mengikuti urutan di HTML: A, lalu B, lalu C. Tanpa z-index, yang ditulis belakangan tampil di atas.',it:k(false)},
   {cap:`Sekarang z-index dipakai: urutan dari belakang ke depan menjadi <b>${urut.map(o=>o.c[0]).join(' → ')}</b>. Kartu <b>${atas}</b> paling dekat ke pengguna.${seri?' Ada nilai yang sama: untuk yang seri, urutan di HTML yang menentukan.':''}`,it:k(true)},
   {cap:'z-index hanya bekerja pada elemen dengan <code>position</code> selain static (atau anak flex/grid), dan dibandingkan di dalam <b>stacking context</b> yang sama. Nilai negatif menaruh elemen di belakang.',it:[...k(true),G('n',0,2,0,'position: relative','idx')]}]}};

/* ---------- SQL JOIN ---------- */
S.join={t:'JOIN: menggabungkan dua tabel lewat kolom yang sama',
 p:[{k:'j',l:'Jenis JOIN',t:'o',o:[['INNER','INNER JOIN'],['LEFT','LEFT JOIN']],v:'INNER'},{k:'ids',l:'pelanggan_id tiap pesanan',t:'s',v:'1, 1, 3'}],
 steps:P=>{const PL=[[1,'Ani'],[2,'Budi'],[3,'Citra']],MENU=['Kopi','Teh','Roti','Kue','Susu'];let ids=angka(P.ids,5);if(!ids.length)ids=[1];
  const O=ids.map((id,i)=>[id,MENU[i]]),left=P.j==='LEFT';
  const tab=(hi)=>[lantai(10,6,-.6-Math.max(3,O.length)),G('tp',-3,2,0,'pelanggan','idx'),G('to',3,2,0,'pesanan','idx'),
    ...PL.map(([id,n],i)=>B('p'+i,-3,1-i,0,{w:2.6,h:.7,d:.8,t:id+' · '+n,c:hi&&hi.p.includes(i)?'warn':'acc'})),
    ...O.map(([id,n],i)=>B('o'+i,3,1-i,0,{w:2.6,h:.7,d:.8,t:'pel '+id+' · '+n,c:hi&&hi.o.includes(i)?'warn':'ok'}))];
  const pairs=[];PL.forEach(([id],a)=>O.forEach(([oid],b)=>{if(oid===id)pairs.push([a,b])}));
  const hasil=[];PL.forEach(([id,n],a)=>{const m=O.filter(o=>o[0]===id);if(m.length)m.forEach(o=>hasil.push([n,o[1],0]));else if(left)hasil.push([n,'NULL',1])});
  const yatim=O.filter(o=>!PL.some(p=>p[0]===o[0]));
  return [
   {cap:'Dua tabel terpisah: <b>pelanggan</b> dan <b>pesanan</b>. Kolom <code>pelanggan_id</code> di pesanan menunjuk ke id pelanggan.',it:tab()},
   {cap:`<code>${P.j} JOIN ... ON pesanan.pelanggan_id = pelanggan.id</code> mencari pasangan baris yang nilainya sama. Ditemukan <b>${pairs.length} pasangan</b>.${yatim.length?` Pesanan dengan id ${yatim.map(o=>o[0]).join(', ')} tidak punya pelanggan, jadi tidak ikut.`:''}`,
    it:[...tab({p:[...new Set(pairs.map(x=>x[0]))],o:pairs.map(x=>x[1])}),...pairs.map(([a,b])=>R('r'+a+'_'+b,[-1.7,1-a,0],[1.7,1-b,0],'warn'))]},
   {cap:`Hasil ${P.j} JOIN: <b>${hasil.length} baris</b>. ${left?'LEFT JOIN mempertahankan <b>semua pelanggan</b>; yang tidak punya pesanan diisi NULL.':'INNER JOIN hanya menyimpan baris yang punya pasangan; pelanggan tanpa pesanan hilang.'} Coba ganti jenis JOIN atau isi pelanggan_id.`,
    it:[lantai(10,6,-.6-Math.max(3,hasil.length)),G('th',0,2,0,'hasil '+P.j+' JOIN','idx'),...(hasil.length?hasil.map(([a,b,nul],i)=>B('h'+i,0,1-i,0,{w:4,h:.7,d:.8,t:a+' · '+b,c:nul?'mute':'warn'})):[G('kos',0,0,0,'(kosong)','bad')])]}]}};

/* ---------- git ---------- */
S.git={t:'Git: commit sebagai titik, branch sebagai jalur',
 p:[{k:'f',l:'Commit di branch fitur',t:'n',min:1,max:4,v:2},{k:'m',l:'Commit baru di main setelah bercabang',t:'n',min:0,max:3,v:0}],
 steps:P=>{const c=(id,x,y,col='acc')=>B(id,x,y,0,{w:.75,h:.75,d:.75,c:col,t:id,ball:1}),line=(a,b,col)=>R('l'+a.join('_')+'-'+b.join('_'),a,b,col);
  const sp=1.25,x0=-4,base=[c('m1',x0,0),c('m2',x0+sp,0),c('m3',x0+2*sp,0),line([x0,0],[x0+2*sp,0],'mute')],bx=x0+2*sp;
  const fit=[...Array(P.f)].map((_,i)=>c('f'+(i+1),bx+(i+1)*sp,1.6,'ok')),fl=[line([bx,0],[bx+sp,1.6],'ok'),...(P.f>1?[line([bx+sp,1.6],[bx+P.f*sp,1.6],'ok')]:[])];
  const mm=[...Array(P.m)].map((_,i)=>c('m'+(4+i),bx+(i+1)*sp,0)),ml=P.m?[line([bx,0],[bx+P.m*sp,0],'mute')]:[];
  const lantaiG=lantai(Math.max(10,(3+P.f+1)*sp+2),4,-1.2),lab=[G('bm',x0-1.4,0,0,'main','idx'),G('bf',bx+P.f*sp+.9,1.6,0,'fitur','ok')];
  const ff=P.m===0,mx=bx+(Math.max(P.f,P.m)+1)*sp;
  return [
   {cap:'Setiap <b>commit</b> adalah titik simpan seluruh proyek. Commit tersusun berurutan di branch <b>main</b>.',it:[lantaiG,...base,G('bm',x0-1.4,0,0,'main','idx')]},
   {cap:`<code>git switch -c fitur</code> membuat jalur baru dari commit terakhir, lalu ${P.f} commit dibuat di sana.${P.m?` Sementara itu main juga maju ${P.m} commit.`:' Main tidak berubah.'}`,it:[lantaiG,...base,...fit,...fl,...mm,...ml,...lab]},
   ff?{cap:'<code>git merge fitur</code>: karena main tidak punya commit baru, Git cukup <b>menggeser label main</b> ke ujung fitur. Ini disebut <b>fast-forward</b>, tanpa commit gabungan.',it:[lantaiG,...base,...fit,...fl,G('bm',bx+P.f*sp,2.6,0,'main = fitur','warn')]}
     :{cap:`<code>git merge fitur</code>: kedua jalur sama-sama maju, jadi Git membuat commit gabungan <b>M</b> yang berisi perubahan keduanya. Jika file yang sama diubah di kedua jalur, bisa terjadi <b>konflik</b>.`,it:[lantaiG,...base,...fit,...fl,...mm,...ml,line([bx+P.m*sp,0],[mx,0],'mute'),line([bx+P.f*sp,1.6],[mx,0],'ok'),c('M',mx,0,'warn'),...lab]}]}};

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
  /* parameter eksperimen: nilai awal dari definisi adegan, langkah dihitung ulang setiap kali diubah */
  const PD=sc.p||[],P={};PD.forEach(d=>P[d.k]=d.v);
  const hitung=()=>{try{return typeof sc.steps==='function'?sc.steps(P):sc.steps}catch(e){return [{cap:'Nilai ini belum bisa digambar. Coba angka lain.',it:[lantai()]}]}};
  let steps=hitung();
  const fld=d=>{const id=`v3-${key}-${d.k}-${Math.random().toString(36).slice(2,7)}`;
    const inp=d.t==='o'?`<select id="${id}" data-k="${d.k}">${d.o.map(([v,l])=>`<option value="${v}"${v===d.v?' selected':''}>${l}</option>`).join('')}</select>`
      :d.t==='n'?`<input id="${id}" data-k="${d.k}" type="number" inputmode="numeric" step="1" min="${d.min}" max="${d.max}" value="${d.v}">`
      :`<input id="${id}" data-k="${d.k}" type="text" value="${d.v}" maxlength="40" autocomplete="off" spellcheck="false">`;
    return `<label class="s3fld" for="${id}"><span>${d.l}${d.t==='n'?` <small>${d.min}…${d.max}</small>`:''}</span>${inp}</label>`};
  const panel=PD.length?`<details class="s3exp" open><summary><span aria-hidden="true">🧪</span> Eksperimen: ubah angkanya, lihat apa yang terjadi</summary>
    <div class="s3form">${PD.map(fld).join('')}<button class="tlink" type="button" data-a="reset">Kembalikan nilai awal</button></div>
    <p class="s3tip">Perubahan langsung diterapkan pada langkah yang sedang dibuka. Tekan Sebelumnya atau Berikutnya untuk melihat langkah lain dengan nilai barumu.</p></details>`:'';
  host.innerHTML=`<div class="s3wrap"><div class="s3" tabindex="0" role="img" aria-label="Adegan 3D: ${sc.t}. Seret atau tekan tombol panah untuk memutar."><div class="s3cam"><div class="w3"></div></div><div class="s3tags"></div>
   <span class="s3hint" aria-hidden="true">⟲ seret untuk memutar</span></div>
   <p class="s3cap" aria-live="polite"></p>
   ${panel}<div class="s3ctl"><button class="btn" data-a="prev">◀ Sebelumnya</button><span class="s3n"></span><button class="btn primary" data-a="next">Berikutnya ▶</button>
    <button class="btn" data-a="play" aria-pressed="false">▶ Putar otomatis</button><button class="tlink" data-a="view">Sudut awal</button></div></div>`;
  const st=host.querySelector('.s3'),w=host.querySelector('.w3'),cap=host.querySelector('.s3cap'),tg=host.querySelector('.s3tags'),n=host.querySelector('.s3n');
  /* label diproyeksikan ke 2D agar selalu terbaca dan tidak tertutup benda */
  const proj=(x,y,z)=>{const a=ry*Math.PI/180,b=rx*Math.PI/180,X=x*U,Y=-y*U,Z=z*U;
    const x1=X*Math.cos(a)+Z*Math.sin(a),z1=-X*Math.sin(a)+Z*Math.cos(a),y2=Y*Math.cos(b)-z1*Math.sin(b),z2=Y*Math.sin(b)+z1*Math.cos(b);
    const W=st.clientWidth,H=st.clientHeight,ox=W/2,oy=H*.4,cx=W/2,cy=H*.54,k=900/(900-z2);return [ox+(cx+x1-ox)*k,oy+(cy+y2-oy)*k]};
  const view=()=>{w.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg)`;
    const W=st.clientWidth;els.forEach(e=>{if(e._tag){const [l,t]=proj(...e._p),h=e.offsetWidth/2+4;e.style.left=Math.max(h,Math.min(W-h,l))+'px';e.style.top=t+'px'}})};
  function draw(){if(i>steps.length-1)i=steps.length-1;const s=steps[i];U=Math.max(26,Math.min(58,st.clientWidth/10.5));const seen=new Set();
    s.it.forEach(o=>{seen.add(o.id);let e=els.get(o.id);const fresh=!e;
      if(fresh){e=document.createElement('div');els.set(o.id,e);(o.tag?tg:w).appendChild(e)}
      if(o.tag){e.className=`t3 ${o.c?'c-'+o.c:''}`;e.innerHTML=o.t;e._tag=1;e._p=[o.x,o.y,o.z]}
      else{e.className=`b3 c-${o.c}${o.ball?' ball':''}${o.rod?' rod':''}${o.flat?' flat':''}`;e.innerHTML=blockHTML(o,U);e.style.transform=place(o,U)}
      if(fresh&&!rm){e.classList.add('in');requestAnimationFrame(()=>requestAnimationFrame(()=>e.classList.remove('in')))}});
    els.forEach((e,id)=>{if(seen.has(id))return;els.delete(id);if(rm)e.remove();else{e.classList.add('out');setTimeout(()=>e.remove(),450)}});
    /* teks di sisi benda dikecilkan bila tidak muat (layar sempit) */
    w.querySelectorAll('.f3>b,.f3>i').forEach(t=>{const f=t.parentNode,cw=f.clientWidth-4,ch=f.clientHeight-2,sw=t.scrollWidth,sh=t.offsetHeight;
      const k=Math.min(1,cw/sw,ch/sh);t.style.transform=k<1?`scale(${Math.max(.35,k)})`:''});
    view();cap.innerHTML=s.cap;n.textContent=`${i+1} / ${steps.length}`;
    host.querySelector('[data-a=prev]').disabled=i===0;host.querySelector('[data-a=next]').disabled=i===steps.length-1}
  const stop=()=>{clearInterval(auto);auto=null;const b=host.querySelector('[data-a=play]');b.setAttribute('aria-pressed','false');b.textContent='▶ Putar otomatis'};
  host.querySelector('.s3ctl').addEventListener('click',e=>{const a=e.target.closest('[data-a]');if(!a)return;const k=a.dataset.a;
    if(k==='next'&&i<steps.length-1){i++;draw()}
    else if(k==='prev'&&i>0){i--;draw()}
    else if(k==='view'){rx=-20;ry=-28;view()}
    else if(k==='play'){if(auto)return stop();if(i===steps.length-1){i=0;draw()}a.setAttribute('aria-pressed','true');a.textContent='❚❚ Jeda';
      auto=setInterval(()=>{if(!host.isConnected)return stop();if(i>=steps.length-1)return stop();i++;draw()},3200)}});
  let drag=null;
  st.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,rx,ry};st.setPointerCapture(e.pointerId);st.classList.add('grab')});
  st.addEventListener('pointermove',e=>{if(!drag)return;ry=drag.ry+(e.clientX-drag.x)*.45;rx=Math.max(-80,Math.min(25,drag.rx-(e.clientY-drag.y)*.35));view()});
  const up=()=>{drag=null;st.classList.remove('grab')};st.addEventListener('pointerup',up);st.addEventListener('pointercancel',up);
  st.addEventListener('keydown',e=>{const m={ArrowLeft:[0,-10],ArrowRight:[0,10],ArrowUp:[-8,0],ArrowDown:[8,0]}[e.key];if(!m)return;e.preventDefault();
    rx=Math.max(-80,Math.min(25,rx+m[0]));ry+=m[1];view()});
  let rw;window.addEventListener('resize',()=>{clearTimeout(rw);rw=setTimeout(()=>{if(host.isConnected){els.forEach(e=>e.remove());els.clear();draw()}},200)});
  if(PD.length){let tm;const form=host.querySelector('.s3form');
    const baca=el=>{const d=PD.find(x=>x.k===el.dataset.k);if(!d)return;
      if(d.t==='n'){let v=Math.round(Number(el.value));if(!Number.isFinite(v)||el.value==='')return;v=Math.max(d.min,Math.min(d.max,v));P[d.k]=v}
      else P[d.k]=el.value};
    const terap=()=>{stop();steps=hitung();draw()};
    form.addEventListener('input',e=>{if(!e.target.dataset.k)return;baca(e.target);clearTimeout(tm);tm=setTimeout(terap,220)});
    form.addEventListener('change',e=>{const el=e.target,d=PD.find(x=>x.k===el.dataset.k);if(d&&d.t==='n'){el.value=P[d.k]}});
    form.querySelector('[data-a=reset]').addEventListener('click',()=>{PD.forEach(d=>{P[d.k]=d.v;const el=form.querySelector(`[data-k="${d.k}"]`);el.value=d.v});terap()});}
  draw();
};
})();
