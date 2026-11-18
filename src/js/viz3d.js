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
S.loop={t:'Perulangan sebagai tangga: semua jenis loop',
 p:[{k:'jenis',l:'Jenis perulangan',t:'o',o:[['for','for'],['while','while'],['do','do-while'],['each','for-each'],['nested','bersarang (nested)'],['break','break'],['continue','continue'],['banding','Bandingkan for, while, do-while']],v:'for'},
   {k:'a',l:'Mulai (i = …)',t:'n',min:-3,max:10,v:0},{k:'z',l:'Batas (i < …)',t:'n',min:-3,max:20,v:4},{k:'s',l:'Langkah (i += …)',t:'n',min:1,max:5,v:1},
   {k:'b',l:'break saat i = … (jenis break)',t:'n',min:-3,max:20,v:2}],
 steps:P=>{const vals=[];for(let i=P.a;i<P.z&&vals.length<9;i+=P.s)vals.push(i);const N=vals.length,more=P.a+N*P.s<P.z,end=P.a+N*P.s;
  const X=(k,n=N)=>(k-(Math.max(n,1)-1)/2)*1.3;
  const tangga=(list,st,z=0,pre='s')=>list.map((v,k)=>B(pre+k,X(k,list.length),k*.4-.3,z,{w:1.2,h:.4,d:1.4,c:st(k,v),t:'i='+v}));
  const bola=(id,k,y,z=0,c='warn',n=N)=>B(id,n?X(k,n):0,y,z,{w:.5,h:.5,d:.5,c,ball:1});
  const lt=(n=N,d=3)=>lantai(Math.max(6,n*1.4+2),d);
  const J=P.jenis;
  /* ---- bandingkan tiga jenis berdampingan ---- */
  if(J==='banding'){const nDo=Math.max(1,N),dv=N?vals:[P.a];const lanes=[['for',N,vals,-2.2],['while',N,vals,0],['do-while',nDo,dv,2.2]];
    const pang=(fin)=>[lantai(Math.max(7,Math.max(nDo,1)*1.4+3),7.4),...lanes.flatMap(([nm,n,list,z])=>[G('ln'+nm,X(0,Math.max(nDo,1))-1.9,0,z,nm,'idx'),
      ...list.map((v,k)=>B('s'+nm+k,X(k,Math.max(nDo,1)),k*.4-.3,z,{w:1.2,h:.4,d:1.4,c:fin&&k<n?'ok':'mute',t:'i='+v})),
      B('b'+nm,fin?(n?X(n-1,Math.max(nDo,1)):X(0,Math.max(nDo,1))-1.2):X(0,Math.max(nDo,1))-1.2,fin&&n?(n-1)*.4+.35:0,z,{w:.5,h:.5,d:.5,c:n?'warn':'bad',ball:1}),
      ...(fin?[G('n'+nm,X(Math.max(n,1)-1,Math.max(nDo,1))+.9,Math.max(n,1)*.4+.9,z,n+'×',n?'ok':'bad')]:[])])];
    return [
     {cap:`Tiga loop dengan aturan yang sama: mulai i = ${P.a}, ulang selama i &lt; ${P.z}, langkah ${P.s}. Bedanya hanya <b>kapan kondisi dicek</b>.`,it:pang(false)},
     {cap:N?`Hasil: for dan while sama-sama jalan <b>${N} kali</b>${more?'+':''}, do-while juga ${nDo} kali. Selama kondisi awal benar, ketiganya setara. Sekarang coba ubah <b>Mulai</b> menjadi ≥ ${P.z}.`
        :`Kondisi awal ${P.a} &lt; ${P.z} sudah <b>salah</b>. for dan while mengecek di awal, jadi <b>0 kali</b>. do-while menjalankan badan dulu baru mengecek, jadi tetap <b>1 kali</b>. Inilah beda utamanya.`,it:pang(true)},
     {cap:'Ringkasnya: <b>for</b> untuk jumlah putaran yang pasti, <b>while</b> untuk berhenti karena keadaan, <b>do-while</b> jika badan harus jalan minimal sekali (misalnya menampilkan menu lalu bertanya "ulangi?").',it:pang(true)}]}
  /* ---- for-each ---- */
  if(J==='each'){const data=N?vals.map(v=>v*10):[];const kot=(hi)=>[lt(),...data.map((v,k)=>B('e'+k,X(k),0,0,{w:1,h:1,d:1,c:k<hi?'ok':k===hi?'warn':'mute',t:String(v)})),G('arr',X(0)-1.6,1.2,0,'data','idx')];
    if(!N)return [{cap:'Koleksinya <b>kosong</b>, jadi for-each tidak menjalankan badannya sama sekali. Ubah Mulai dan Batas agar ada isinya.',it:[lt(),G('k',0,.5,0,'[ ] kosong','bad')]}];
    return [{cap:`<code>for (x : data)</code> / <code>for x in data</code>: for-each mengambil <b>isi</b> koleksi satu per satu, tanpa indeks dan tanpa kondisi yang kita tulis. Data berisi ${N} elemen.`,it:kot(-1)},
      ...data.map((v,k)=>({cap:`Putaran ${k+1}: x = <b>${v}</b>. Tidak ada <code>i++</code> yang bisa lupa ditulis, dan tidak mungkin salah indeks.`,it:[...kot(k),B('bola',X(k),.9,0,{w:.5,h:.5,d:.5,c:'warn',ball:1})]})),
      {cap:`Elemen habis, loop berhenti otomatis setelah <b>${N} putaran</b>. Pakai for-each jika hanya perlu membaca setiap isi; pakai for biasa jika butuh nomor indeksnya.`,it:kot(N)}]}
  /* ---- bersarang ---- */
  if(J==='nested'){const R=Math.max(1,Math.min(4,N)),C=3,rows=(N?vals:[P.a]).slice(0,R);
    const grid=(r)=>[lantai(C*1.3+3,R*1.3+2),...rows.flatMap((v,ri)=>[...Array(C)].map((_,c)=>B('g'+ri+'_'+c,(c-1)*1.3,ri<r?0:-.2,(ri-(R-1)/2)*1.3,{w:1,h:ri<r?.8:.3,d:1,c:ri<r?'ok':ri===r?'warn':'mute',t:ri<=r?String(v*(c+1)):''}))),
      ...rows.map((v,ri)=>G('rl'+ri,-3.2,0,(ri-(R-1)/2)*1.3,'luar i='+v,'idx')),...[0,1,2].map(c=>G('cl'+c,(c-1)*1.3,-.4,(R/2)*1.3+.8,'dalam j='+(c+1),'idx'))];
    if(!N)return [{cap:'Loop luar tidak pernah jalan (kondisi awal salah), jadi loop dalam juga tidak pernah jalan.',it:[lantai(6,3),G('k',0,.5,0,'0 × 3 = 0','bad')]}];
    return [{cap:`Loop <b>bersarang</b>: loop luar (i) berjalan ${R} kali, dan di <b>setiap</b> putaran luar, loop dalam (j = 1..3) berjalan sampai habis.`,it:grid(-1)},
      ...rows.map((v,ri)=>({cap:`Putaran luar i = ${v}: loop dalam jalan 3 kali → ${[1,2,3].map(j=>v*j).join(', ')} (i × j). Baru setelah itu i naik.`,it:grid(ri)})),
      {cap:`Total badan loop dalam dijalankan ${R} × 3 = <b>${R*3} kali</b>. Hati-hati: loop bersarang cepat membengkak, 1000 × 1000 = sejuta putaran.`,it:grid(R)}]}
  /* ---- for, while, do-while, break, continue (satu tangga) ---- */
  const dv=J==='do'&&!N?[P.a]:vals,M=dv.length;
  const kode={for:`<code>for (i = ${P.a}; i &lt; ${P.z}; i += ${P.s})</code>`,while:`<code>i = ${P.a}; while (i &lt; ${P.z}) { …; i += ${P.s} }</code>`,do:`<code>i = ${P.a}; do { …; i += ${P.s} } while (i &lt; ${P.z})</code>`,
    break:`<code>for (i = ${P.a}; i &lt; ${P.z}; i += ${P.s}) { if (i == ${P.b}) break; … }</code>`,continue:`<code>for (i = ${P.a}; i &lt; ${P.z}; i += ${P.s}) { if (i % 2 == 0) continue; … }</code>`}[J]||'';
  if(!M)return [{cap:`${kode}: kondisi awal <code>${P.a} &lt; ${P.z}</code> sudah <b>salah</b>, jadi badan <b>tidak pernah dijalankan</b> (0 putaran).${J==='while'||J==='for'?' Coba jenis do-while dengan angka yang sama: badannya tetap jalan sekali.':''}`,it:[lt(),bola('bola',0,0),G('cek',0,1.3,0,`${P.a} < ${P.z} salah`,'bad')]}];
  const stopAt=J==='break'?dv.indexOf(P.b):-1;
  const warna=(n,cur)=>(k,v)=>J==='continue'&&k<n&&v%2===0?'mute':J==='break'&&stopAt>=0&&k>=stopAt?(k<n?'bad':'mute'):k<n?'ok':'mute';
  const st=[{cap:J==='do'?`${kode}: do-while langsung menjalankan badan <b>tanpa mengecek</b> dulu. Kondisi baru diperiksa di akhir setiap putaran.`
     :`${kode}: ${J==='while'?'while mengecek kondisi <b>sebelum</b> setiap putaran.':J==='break'?`loop ini akan <b>berhenti paksa</b> saat i = ${P.b}.`:J==='continue'?'angka genap akan <b>dilewati</b>, tetapi loop tetap lanjut.':'for menulis nilai awal, kondisi, dan perubahan dalam satu baris.'} Nilai i: ${dv.join(', ')}${more?', …':''}.`,
     it:[lt(M),...tangga(dv,warna(0)),bola('bola',-1.2,0,0,'warn',M),G('cek',X(0,M)-1.2,1.4,0,'i = '+P.a,'warn')]}];
  for(let k=0;k<M;k++){const v=dv[k];
    if(J==='break'&&v===P.b){st.push({cap:`i = ${v}: kondisi <code>i == ${P.b}</code> benar, jadi <b>break</b>. Loop langsung berhenti walaupun <code>i &lt; ${P.z}</code> masih benar. Sisa tangga tidak pernah dinaiki.`,it:[lt(M),...tangga(dv,warna(k+1)),bola('bola',k,k*.4+.35,0,'bad',M),G('cek',X(k,M),k*.4+1.5,0,'break! keluar','bad')]});return st}
    const skip=J==='continue'&&v%2===0;
    const ket=J==='do'&&k===0?`Putaran 1: badan dijalankan <b>dulu</b> (i = ${v}), baru dicek: <code>${v+P.s} &lt; ${P.z}</code> → <b>${v+P.s<P.z}</b>.${N?'':' Kondisinya salah, tetapi badan sudah terlanjur jalan sekali.'}`
      :skip?`Putaran ${k+1}: i = ${v} genap, jadi <b>continue</b>: sisa badan dilewati, langsung ke putaran berikutnya.`
      :`Putaran ${k+1}: cek <code>i &lt; ${P.z}</code> → ${v} &lt; ${P.z} <b>benar</b>, badan dijalankan, lalu <code>i += ${P.s}</code> menjadi ${v+P.s}.`;
    st.push({cap:ket,it:[lt(M),...tangga(dv,warna(k+1)),bola('bola',k,k*.4+.35,0,skip?'mute':'warn',M),G('cek',X(k,M),k*.4+1.5,0,skip?`i = ${v} dilewati`:`i = ${v} → ${v+P.s}`,skip?'idx':'warn')]})}
  const jalan=J==='continue'?dv.filter(v=>v%2!==0).length:M;
  st.push(more?{cap:`(Tangga dipotong di 9 putaran agar muat di layar; perulangan sebenarnya masih berlanjut sampai i ≥ ${P.z}.)`,it:[lt(M),...tangga(dv,warna(M)),bola('bola',M-1,(M-1)*.4+.35,0,'warn',M)]}
   :{cap:`Cek lagi: <code>i &lt; ${P.z}</code> → ${J==='do'&&!N?P.a+P.s:end} &lt; ${P.z} <b>salah</b>. Perulangan berhenti. ${J==='continue'?`Ada ${M} putaran, tetapi badan hanya benar-benar bekerja <b>${jalan} kali</b> (angka ganjil).`:`Total <b>${M} putaran</b>.`}${J==='break'?` Angka ${P.b} tidak pernah muncul, jadi break tidak terpicu.`:''}`,
     it:[lt(M),...tangga(dv,warna(M)),bola('bola',M,M*.4+.2,0,'warn',M),G('cek',X(M-1,M)+.6,M*.4+1.6,0,'salah → keluar','bad')]});
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

/* ---------- logika boolean ---------- */
S.bool={t:'Logika boolean: dua saklar masuk ke gerbang logika',
 p:[{k:'p',l:'p',t:'o',o:[['1','true'],['0','false']],v:'1'},{k:'q',l:'q',t:'o',o:[['1','true'],['0','false']],v:'0'},
   {k:'op',l:'Operator',t:'o',o:[['and','AND (&&)'],['or','OR (||)'],['not','NOT (!p)'],['xor','XOR (^)']],v:'and'}],
 steps:P=>{const p=String(P.p)==='1',q=String(P.q)==='1',op=P.op;
  const f=(a,b)=>op==='and'?a&&b:op==='or'?a||b:op==='not'?!a:a!==b;
  const r=f(p,q),sym={and:'&&',or:'||',not:'!',xor:'^'}[op],nm={and:'AND',or:'OR',not:'NOT',xor:'XOR'}[op];
  const pakaiQ=op!=='not',sc=(op==='and'&&!p)||(op==='or'&&p);
  const ekspr=op==='not'?`!${p}`:`${p} ${sym} ${q}`;
  const kol=v=>v?'ok':'bad';
  const pang=(st)=>{const qOn=pakaiQ&&!(st>=1&&sc);return [lantai(9,4),
    B('pin',-3.2,1.1,0,{w:1.5,h:.7,d:.9,c:st>=1?kol(p):'acc',t:'p = '+p}),
    B('qin',-3.2,-.1,0,{w:1.5,h:.7,d:.9,c:!pakaiQ?'mute':st>=1&&sc?'mute':st>=1?kol(q):'acc',t:pakaiQ?(st>=1&&sc?'q dilewati':'q = '+q):'q (tak dipakai)'}),
    R('rp',[-2.45,1.1,0],[-.75,.6,0],st>=1?kol(p):'mute'),R('rq',[-2.45,-.1,0],[-.75,.4,0],qOn&&st>=1?kol(q):'mute'),
    B('gate',0,.5,0,{w:1.5,h:1.5,d:1.2,c:'glass',t:nm}),R('ro',[.75,.5,0],[2.35,.5,0],st>=2?kol(r):'mute'),
    B('out',3.1,.5,0,{w:1.5,h:.8,d:.9,c:st>=2?kol(r):'mute',t:st>=2?String(r):'?'})]};
  const rows=op==='not'?[[true],[false]]:[[true,true],[true,false],[false,true],[false,false]];
  const tabel=()=>{const cols=op==='not'?['p','!p']:['p','q',nm],x0=-(cols.length-1)*.8;
    return [lantai(7,3),...cols.map((c,j)=>G("h"+j,x0+j*1.6,2.65,0,c,"idx")),
     ...rows.flatMap((row,i)=>{const hasil=f(row[0],row[1]),cur=row[0]===p&&(op==='not'||row[1]===q),vals=[...row,hasil];
      return vals.map((v,j)=>B('t'+i+'_'+j,x0+j*1.6,1.9-i*.75,0,{w:1.4,h:.48,d:.3,c:cur?kol(v):'mute',t:String(v)}))})]};
  const nTrue=rows.filter(rw=>f(rw[0],rw[1])).length;
  return [
   {cap:op==='not'?`<b>NOT</b> hanya butuh satu masukan: ia membalik nilai p.`:`Dua masukan boolean, <b>p</b> dan <b>q</b>, masuk ke gerbang <b>${nm}</b> (<code>${sym}</code>). Hasilnya juga boolean: true atau false.`,it:pang(0)},
   {cap:op==='not'?`p = ${p}. q tidak dipakai sama sekali.`:sc?`p = ${p} sudah menentukan hasil ${nm}, jadi q <b>tidak dicek</b>. Inilah <b>short-circuit</b>: ${op==='and'?'AND langsung false jika sisi kiri false':'OR langsung true jika sisi kiri true'}.`
      :`p = ${p} belum cukup untuk menentukan hasil, jadi q = ${q} ikut dicek.${op==='xor'?' XOR selalu butuh kedua sisi.':''}`,it:pang(1)},
   {cap:`<code>${ekspr}</code> menghasilkan <b>${r}</b>. ${op==='and'?'AND hanya true jika kedua sisi true.':op==='or'?'OR true jika minimal satu sisi true.':op==='xor'?'XOR true jika kedua sisi berbeda.':'NOT membalik nilai.'}`,it:pang(2)},
   {cap:`Tabel kebenaran ${nm}: hasil true di <b>${nTrue} dari ${rows.length}</b> baris. Baris berwarna adalah nilai p${op==='not'?'':' dan q'} yang sedang kamu pilih. Ubah nilainya di panel Eksperimen.`,it:tabel()}]}};

/* ---------- bilangan acak ---------- */
/* generator acak semu kecil (mulberry32): seed sama selalu memberi urutan yang sama */
const prng=seed=>{let a=(seed>>>0)||1;return ()=>{a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return ((t^t>>>14)>>>0)/4294967296}};
S.acak={t:'Bilangan acak: dari desimal 0..1 menjadi angka dadu',
 p:[{k:'a',l:'Batas bawah',t:'n',min:-5,max:20,v:1},{k:'b',l:'Batas atas (ikut)',t:'n',min:-5,max:30,v:6},
   {k:'n',l:'Jumlah lemparan',t:'n',min:1,max:30,v:12},{k:'seed',l:'Seed',t:'n',min:0,max:9999,v:42}],
 steps:P=>{let lo=Math.min(P.a,P.b),hi=Math.max(P.a,P.b),pot=false;if(hi-lo+1>10){hi=lo+9;pot=true}
  const K=hi-lo+1,rnd=prng(P.seed),rs=Array.from({length:P.n},()=>rnd()),hs=rs.map(r=>Math.floor(r*K)+lo);
  const X=k=>(k-(K-1)/2)*1.1,r0=rs[0],h0=hs[0],idx=h0-lo;
  const garis=()=>[B('gr',0,1.9,0,{w:6,h:.12,d:.3,c:'mute'}),G('g0',-3,2.4,0,'0','idx'),G('g1',3,2.4,0,'1 (tak pernah)','idx')];
  const kotak=(hl)=>Array.from({length:K},(_,k)=>B('k'+k,X(k),-.2,0,{w:1,h:.5,d:1,c:k===hl?'ok':'acc',t:String(lo+k)}));
  const cnt=Array(K).fill(0);hs.forEach(h=>cnt[h-lo]++);const mx=Math.max(...cnt,1);
  const tiang=()=>cnt.map((c,k)=>c?B("c"+k,X(k),.05+c/mx*1,0,{w:.8,h:c/mx*2,d:.8,c:'warn',t:String(c)}):null).filter(Boolean);
  const daftar=hs.slice(0,15).join(', ')+(hs.length>15?', …':'');
  const lt=()=>lantai(Math.max(7,K*1.1+2),3);
  return [
   {cap:`Fungsi acak dasar memberi desimal <b>0 ≤ r &lt; 1</b>. Kali ini r = <code>${r0.toFixed(4)}</code>. Angka 0 bisa keluar, tetapi 1 tidak pernah.`,it:[lt(),...garis(),B('bola',-3+r0*6,2.3,0,{w:.45,h:.45,d:.45,c:'warn',ball:1}),...kotak(-1)]},
   {cap:`Rentang ${lo}..${hi} berisi ${K} angka. <code>floor(${r0.toFixed(4)} × ${K})</code> = ${idx}, lalu + ${lo} = <b>${h0}</b>.${pot?' (Visual dibatasi 10 kotak.)':''} Tanpa "+1" pada lebar rentang, angka ${hi} tidak akan pernah keluar.`,it:[lt(),...garis(),B('bola',X(idx),.45,0,{w:.45,h:.45,d:.45,c:'ok',ball:1}),...kotak(idx)]},
   {cap:`${P.n} lemparan: ${daftar}. Tinggi tiang = berapa kali angka itu keluar. Makin banyak lemparan, tingginya makin rata.`,it:[lt(),...kotak(-1),...tiang()]},
   {cap:`Seed ${P.seed} <b>selalu</b> memberi urutan yang sama ini. Ganti seed di panel Eksperimen dan urutannya berubah; kembalikan ke ${P.seed} dan urutannya sama lagi. Inilah cara program diuji ulang dengan hasil acak yang bisa diulang.`,it:[lt(),...kotak(-1),...tiang()]}]}};


/* ===================== SQL & POSTGRESQL ===================== */
const PROD=[[1,'Kopi',25,'Minuman'],[2,'Teh',15,'Minuman'],[3,'Roti',30,'Makanan'],[4,'Keju',60,'Makanan'],[5,'Susu',40,'Minuman'],[6,'Madu',85,'Lainnya']];
S.query={t:'Urutan kerja query SQL: FROM, WHERE, SELECT, ORDER BY, LIMIT',
 p:[{k:'min',l:'WHERE harga ≥ (ribu)',t:'n',min:0,max:100,v:30},{k:'ord',l:'ORDER BY harga',t:'o',o:[['desc','DESC (besar dulu)'],['asc','ASC (kecil dulu)']],v:'desc'},{k:'lim',l:'LIMIT',t:'n',min:1,max:6,v:3}],
 steps:P=>{const CX=[-3.3,-1.3,.9,3.3],W=[.9,2,1.6,2.2],Z=k=>(k-2.5)*.82,cols=['id','nama','harga','kategori'];
  const cell=(r,j,k,c,y=0)=>B('q'+r[0]+'_'+j,CX[j],y,Z(k),{w:W[j],h:.32,d:.68,c,t:String(r[j])});
  const head=js=>js.map(j=>G('h'+j,CX[j],.75,Z(-1.1),cols[j],'idx'));
  const lt=lantai(10.5,6.6);
  const lolos=PROD.filter(r=>r[2]>=P.min),gagal=PROD.filter(r=>r[2]<P.min);
  const urut=[...lolos].sort((a,b)=>P.ord==='asc'?a[2]-b[2]:b[2]-a[2]),hasil=urut.slice(0,P.lim);
  const S2=[1,2];
  return [
   {cap:`<code>FROM produk</code> dikerjakan <b>pertama</b>: database mengambil seluruh tabel, ${PROD.length} baris dengan 4 kolom. Setiap baris satu produk, setiap kolom satu jenis data.`,
    it:[lt,...head([0,1,2,3]),...PROD.flatMap((r,k)=>[0,1,2,3].map(j=>cell(r,j,k,'acc')))]},
   {cap:`<code>WHERE harga &gt;= ${P.min}</code> memeriksa setiap baris. ${lolos.length} baris lolos (hijau), ${gagal.length} baris dibuang (merah). WHERE bekerja per baris, sebelum kolom dipilih.`,
    it:[lt,...head([0,1,2,3]),...PROD.flatMap((r,k)=>{const ok=r[2]>=P.min;return [0,1,2,3].map(j=>cell(r,j,k,ok?'ok':'bad',ok?0:.7))})]},
   {cap:`<code>SELECT nama, harga</code> baru dikerjakan sekarang: hanya kolom yang diminta yang dibawa. Kolom id dan kategori tidak ikut ke hasil.`,
    it:[lt,...head(S2),...PROD.flatMap((r,k)=>r[2]>=P.min?S2.map(j=>cell(r,j,k,'acc')):[])]},
   {cap:`<code>ORDER BY harga ${P.ord.toUpperCase()}</code> menyusun ulang baris yang tersisa: ${P.ord==='desc'?'harga terbesar di atas':'harga terkecil di atas'}. Perhatikan baris-barisnya berpindah tempat.`,
    it:[lt,...head(S2),...urut.flatMap((r,k)=>S2.map(j=>cell(r,j,k,'warn')))]},
   {cap:lolos.length?`<code>LIMIT ${P.lim}</code> hanya mengambil ${P.lim} baris teratas. Hasil akhir: ${hasil.map(r=>r[1]).join(', ')}.`:'Tidak ada baris yang lolos WHERE, jadi hasilnya kosong. Coba turunkan batas harga di panel Eksperimen.',
    it:[lt,...head(S2),...hasil.flatMap((r,k)=>S2.map(j=>cell(r,j,k,'ok')))]},
   {cap:'Urutan <b>menulis</b> query: SELECT, FROM, WHERE, ORDER BY, LIMIT. Urutan <b>dikerjakan</b>: FROM → WHERE → SELECT → ORDER BY → LIMIT. Karena itu alias di SELECT belum dikenal di WHERE.',
    it:[lt,...head(S2),...hasil.flatMap((r,k)=>S2.map(j=>cell(r,j,k,'ok'))),G('urut',0,2.3,0,'FROM → WHERE → SELECT → ORDER BY → LIMIT','warn')]}]}};

const JUAL=[['Minuman',12],['Makanan',30],['Minuman',8],['Lainnya',5],['Makanan',22],['Minuman',15],['Lainnya',9],['Makanan',18]];
S.group={t:'GROUP BY: mengelompokkan baris lalu meringkas setiap kelompok',
 p:[{k:'fn',l:'Fungsi agregat',t:'o',o:[['sum','SUM(jumlah)'],['count','COUNT(*)'],['avg','AVG(jumlah)'],['max','MAX(jumlah)']],v:'sum'},{k:'hv',l:'HAVING hasil ≥',t:'n',min:0,max:100,v:40}],
 steps:P=>{const K=['Minuman','Makanan','Lainnya'],KC=['acc','warn','ok'],GX=k=>(k-1)*3.1,nm={sum:'SUM',count:'COUNT',avg:'AVG',max:'MAX'}[P.fn]||'SUM';
  const agg=k=>{const v=JUAL.filter(r=>r[0]===K[k]).map(r=>r[1]);return P.fn==='count'?v.length:P.fn==='avg'?Math.round(v.reduce((a,b)=>a+b,0)/v.length*10)/10:P.fn==='max'?Math.max(...v):v.reduce((a,b)=>a+b,0)};
  const A=K.map((_,k)=>agg(k)),mx=Math.max(...A,1),lt=lantai(10,6);
  const lepas=()=>JUAL.map((r,i)=>B('r'+i,(i-3.5)*1.15,0,1.7,{w:.95,h:.5,d:.8,c:KC[K.indexOf(r[0])],t:String(r[1])}));
  const tumpuk=()=>{const c=[0,0,0];return JUAL.map((r,i)=>{const k=K.indexOf(r[0]),h=c[k]++;return B('r'+i,GX(k),h*.56-.05,-.6,{w:.95,h:.5,d:.8,c:KC[k],t:String(r[1])})})};
  const nama=()=>K.map((n,k)=>G('g'+k,GX(k),-.55,.4,n,'idx'));
  const tiang=f=>K.map((n,k)=>{const h=Math.max(.3,A[k]/mx*2.6);return B('a'+k,GX(k),h/2-.3,-.6,{w:1.3,h,d:1.1,c:f(k),t:String(A[k])})});
  const lolos=K.filter((_,k)=>A[k]>=P.hv);
  return [
   {cap:`Tabel penjualan berisi ${JUAL.length} baris. Warna menunjukkan kategori. Kita ingin tahu <b>${nm}</b> per kategori.`,it:[lt,...lepas()]},
   {cap:'<code>GROUP BY kategori</code> mengumpulkan baris dengan kategori yang sama ke satu tumpukan. Perhatikan setiap kotak berpindah ke kelompoknya.',it:[lt,...tumpuk(),...nama()]},
   {cap:`<code>${nm}(${P.fn==='count'?'*':'jumlah'})</code> meringkas setiap tumpukan menjadi <b>satu baris</b>: ${K.map((n,k)=>`${n} = ${A[k]}`).join(', ')}.`,it:[lt,...tiang(k=>KC[k]),...nama()]},
   {cap:`<code>HAVING ${nm}(...) &gt;= ${P.hv}</code> menyaring <b>kelompok</b>, bukan baris. Yang lolos: ${lolos.length?lolos.join(', '):'tidak ada'}. WHERE menyaring sebelum dikelompokkan, HAVING sesudahnya.`,
    it:[lt,...tiang(k=>A[k]>=P.hv?'ok':'bad'),...nama(),...K.map((n,k)=>A[k]<P.hv?G('x'+k,GX(k),2.9,-.6,'dibuang','bad'):null).filter(Boolean)]},
   {cap:'Urutannya: FROM → WHERE → <b>GROUP BY</b> → <b>HAVING</b> → SELECT → ORDER BY. Setiap kolom di SELECT harus ikut di GROUP BY atau dibungkus fungsi agregat.',it:[lt,...tiang(k=>A[k]>=P.hv?'ok':'mute'),...nama()]}]}};

S.index={t:'Index: lompat lewat pohon B-tree, bukan memeriksa baris satu per satu',
 p:[{k:'n',l:'Jumlah baris di tabel',t:'n',min:16,max:100000000,v:1000000},{k:'cari',l:'Cari id ke- (1–16)',t:'n',min:1,max:16,v:11}],
 steps:P=>{const V=16,c=Math.min(V,Math.max(1,P.cari)),n=Math.max(V,P.n),X=k=>(k-(V-1)/2)*.62,lv=Math.ceil(Math.log2(n)),fmt=v=>v.toLocaleString('id-ID');
  const tabel=f=>Array.from({length:V},(_,k)=>B('t'+k,X(k),-.05,0,{w:.5,h:.5,d:1.1,c:f(k),t:String(k+1)}));
  const L1=c<=8?0:1,L2=Math.floor((c-1)/4),nx1=i=>(i-.5)*5,nx2=i=>(i-1.5)*2.5,LX=X(c-1);
  const nd=(id,x,y,col,t)=>B(id,x,y,0,{w:1.4,h:.48,d:.7,c:col,t});
  const pohon=on=>[nd('n0',0,3.4,on>=1?'ok':'acc','1–16'),...[0,1].map(i=>nd('n1'+i,nx1(i),2.4,on>=1&&i===L1?'ok':'acc',i?'9–16':'1–8')),
    ...[0,1,2,3].map(i=>nd('n2'+i,nx2(i),1.4,on>=1&&i===L2?'ok':'acc',`${i*4+1}–${i*4+4}`)),
    ...[0,1].map(i=>R('e1'+i,[0,3.15,0],[nx1(i),2.65,0],on>=1&&i===L1?'ok':'mute')),...[0,1,2,3].map(i=>R('e2'+i,[nx1(i<2?0:1),2.15,0],[nx2(i),1.65,0],on>=1&&i===L2?'ok':'mute')),
    ...(on>=2?[R('e3',[nx2(L2),1.15,0],[LX,.25,0],'ok')]:[])];
  const lt=lantai(11.5,3.4);
  return [
   {cap:`Tabel ini berisi <b>${fmt(n)} baris</b> (digambar 16 saja). Kita mencari baris dengan id = ${c}.`,it:[lt,...tabel(()=>'acc')]},
   {cap:`<b>Tanpa index</b>, database membaca baris satu per satu dari awal (<i>sequential scan</i>). Di sini ${c} baris diperiksa sebelum ketemu. Untuk ${fmt(n)} baris, terburuknya ${fmt(n)} kali periksa.`,
    it:[lt,...tabel(k=>k<c-1?'mute':k===c-1?'ok':'acc'),B('bola',LX,.6,0,{w:.4,h:.4,d:.4,c:'warn',ball:1})]},
   {cap:'<code>CREATE INDEX</code> membangun <b>pohon B-tree</b>: setiap simpul mencatat rentang id di bawahnya, seperti daftar isi buku.',it:[lt,...tabel(()=>'acc'),...pohon(0)]},
   {cap:`Mencari id ${c}: mulai dari akar, pilih cabang yang rentangnya memuat ${c}, terus turun. Hanya satu jalur yang dilewati.`,it:[lt,...tabel(()=>'acc'),...pohon(1)]},
   {cap:`Daun menunjuk langsung ke barisnya. Untuk ${fmt(n)} baris, cukup sekitar <b>${lv} langkah</b> (log₂ n), bukan ${fmt(n)}. Inilah <i>index scan</i> yang terlihat di EXPLAIN.`,it:[lt,...tabel(k=>k===c-1?'ok':'acc'),...pohon(2)]},
   {cap:'Index tidak gratis: setiap INSERT dan UPDATE juga harus memperbarui pohonnya, dan index memakan ruang disk. Buat index untuk kolom yang sering dipakai di WHERE, JOIN, dan ORDER BY.',it:[lt,...tabel(k=>k===c-1?'ok':'acc'),...pohon(2),G('biaya',0,4.3,0,'baca cepat · tulis sedikit lebih lambat','warn')]}]}};

S.fk={t:'Primary key dan foreign key: tabel yang saling menunjuk',
 p:[{k:'id',l:'pelanggan_id pesanan baru',t:'n',min:1,max:9,v:4}],
 steps:P=>{const PL=[[1,'Ani'],[2,'Budi'],[3,'Citra']],PS=[[101,1],[102,3],[103,1]],Y=k=>2.2-k*.75,LX=-3,RX=2.8;
  const pel=f=>PL.map((r,k)=>B('p'+r[0],LX,Y(k),0,{w:2.4,h:.5,d:.8,c:f(r[0]),t:`${r[0]} · ${r[1]}`}));
  const pes=f=>PS.map((r,k)=>B('o'+r[0],RX,Y(k),0,{w:2.4,h:.5,d:.8,c:f(r[0]),t:`${r[0]} → ${r[1]}`}));
  const ruas=(on)=>PS.map((r,k)=>R('f'+r[0],[RX-1.2,Y(k),0],[LX+1.2,Y(PL.findIndex(p=>p[0]===r[1])),0],on?'ok':'mute'));
  const kep=()=>[G('hp',LX,3,0,'pelanggan (PK: id)','idx'),G('ho',RX,3,0,'pesanan (FK: pelanggan_id)','idx')];
  const ada=PL.some(r=>r[0]===P.id),lt=lantai(10,3);
  const baru=(c,y)=>B('o104',RX,y,0,{w:2.4,h:.5,d:.8,c,t:`104 → ${P.id}`});
  return [
   {cap:'Dua tabel: <b>pelanggan</b> dan <b>pesanan</b>. Setiap pesanan menyimpan <code>pelanggan_id</code> untuk menunjuk pemiliknya.',it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'acc')]},
   {cap:'<b>Primary key</b> (id) adalah identitas unik setiap baris: tidak boleh kembar dan tidak boleh NULL. Tidak ada dua pelanggan dengan id yang sama.',it:[lt,...kep(),...pel(()=>'warn'),...pes(()=>'mute')]},
   {cap:'<b>Foreign key</b> <code>pelanggan_id REFERENCES pelanggan(id)</code> menghubungkan setiap pesanan ke satu pelanggan. Ani punya dua pesanan, Budi belum punya.',it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'ok'),...ruas(1)]},
   ada?{cap:`<code>INSERT INTO pesanan VALUES (104, ${P.id})</code>: pelanggan ${P.id} ada, jadi baris baru <b>diterima</b> dan langsung terhubung.`,it:[lt,...kep(),...pel(id=>id===P.id?'ok':'acc'),...pes(()=>'ok'),...ruas(1),baru('ok',Y(3)),R('f104',[RX-1.2,Y(3),0],[LX+1.2,Y(P.id-1),0],'ok')]}
      :{cap:`<code>INSERT INTO pesanan VALUES (104, ${P.id})</code> <b>ditolak</b>: pelanggan ${P.id} tidak ada. Pesan error: <i>violates foreign key constraint</i>. Database menjaga agar tidak ada pesanan "yatim".`,it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'ok'),...ruas(1),baru('bad',Y(3)+.4),G('err',RX,Y(3)-.5,0,'ditolak: pelanggan tidak ada','bad')]},
   {cap:'Constraint lain menjaga data tetap benar: <code>NOT NULL</code> (wajib diisi), <code>UNIQUE</code> (tidak boleh kembar), <code>CHECK (harga &gt; 0)</code>. Ubah pelanggan_id di panel Eksperimen untuk mencoba.',it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'ok'),...ruas(1),...(ada?[baru('ok',Y(3)),R('f104',[RX-1.2,Y(3),0],[LX+1.2,Y(P.id-1),0],'ok')]:[])]}]}};

S.tx={t:'Transaksi: semua langkah berhasil, atau tidak sama sekali',
 p:[{k:'n',l:'Transfer dari A ke B (ribu)',t:'n',min:1,max:900,v:150},{k:'gagal',l:'Server mati di tengah?',t:'o',o:[['0','Tidak'],['1','Ya']],v:'0'}],
 steps:P=>{const A0=500,B0=200,n=P.n,mati=String(P.gagal)==='1',kurang=n>A0;
  const akun=(id,x,v,c)=>{const h=Math.max(.3,v/400*1.6);return B(id,x,h/2-.3,0,{w:1.8,h,d:1.4,c,t:`${id==='akA'?'A':'B'}: ${v}`})};
  const uang=(x,y,c='warn')=>B('uang',x,y,0,{w:.55,h:.55,d:.55,c,ball:1,t:String(n)});
  const lt=lantai(9,3.4),tot=v=>G('tot',0,3.3,0,'total = '+v,'idx');
  const s=[{lb:'BEGIN',cap:`<code>BEGIN</code> membuka transaksi. Saldo A = ${A0}, B = ${B0}, total ${A0+B0}. Kita akan memindahkan ${n} dari A ke B.`,it:[lt,akun('akA',-2.6,A0,'acc'),akun('akB',2.6,B0,'acc'),tot(A0+B0)]}];
  if(kurang){s.push({lb:'Kurangi A',cap:`<code>UPDATE akun SET saldo = saldo - ${n}</code> pada A melanggar <code>CHECK (saldo &gt;= 0)</code> karena saldo A hanya ${A0}. Database menolak perubahan ini.`,it:[lt,akun('akA',-2.6,A0,'bad'),akun('akB',2.6,B0,'acc'),tot(A0+B0),G('err',-2.6,2.6,0,'CHECK gagal','bad')]},
    {lb:'ROLLBACK',cap:'<code>ROLLBACK</code>: transaksi dibatalkan. Tidak ada saldo yang berubah.',it:[lt,akun('akA',-2.6,A0,'acc'),akun('akB',2.6,B0,'acc'),tot(A0+B0)]})}
  else{s.push({lb:'Kurangi A',cap:`<code>UPDATE ... saldo - ${n} WHERE id = 'A'</code>. Saldo A menjadi ${A0-n}, tetapi belum permanen: transaksi lain belum melihat perubahan ini.`,it:[lt,akun('akA',-2.6,A0-n,'warn'),akun('akB',2.6,B0,'acc'),uang(0,1.8),tot(`${A0+B0-n} (sementara)`)]});
    if(mati)s.push({lb:'Gagal',cap:'Server tiba-tiba mati sebelum B ditambah. Kalau tidak ada transaksi, uang ini akan <b>hilang</b>.',it:[lt,akun('akA',-2.6,A0-n,'warn'),akun('akB',2.6,B0,'mute'),uang(0,1.8,'bad'),G('err',0,3.3,0,'⚡ server mati','bad')]},
      {lb:'ROLLBACK',cap:`Saat hidup lagi, PostgreSQL membaca WAL dan membatalkan transaksi yang belum COMMIT. Saldo A kembali ${A0}. Total tetap ${A0+B0}: <b>atomicity</b>.`,it:[lt,akun('akA',-2.6,A0,'ok'),akun('akB',2.6,B0,'ok'),tot(A0+B0)]});
    else s.push({lb:'Tambah B',cap:`<code>UPDATE ... saldo + ${n} WHERE id = 'B'</code>. Uang berpindah ke B.`,it:[lt,akun('akA',-2.6,A0-n,'warn'),akun('akB',2.6,B0+n,'warn'),uang(2.6,(B0+n)/400*1.6+.2),tot(A0+B0)]},
      {lb:'COMMIT',cap:`<code>COMMIT</code>: kedua perubahan disimpan permanen <b>bersamaan</b>. A = ${A0-n}, B = ${B0+n}, total tetap ${A0+B0}.`,it:[lt,akun('akA',-2.6,A0-n,'ok'),akun('akB',2.6,B0+n,'ok'),tot(A0+B0)]})}
  s.push({lb:'ACID',cap:'<b>ACID</b>: <b>A</b>tomicity (semua atau tidak sama sekali), <b>C</b>onsistency (aturan seperti CHECK selalu dijaga), <b>I</b>solation (transaksi lain tidak melihat keadaan setengah jadi), <b>D</b>urability (yang sudah COMMIT tidak hilang). Coba pilih "Server mati" di Eksperimen.',
    it:[...s[s.length-1].it.filter(o=>o.id!=='uang'&&o.id!=='err')]});
  return s}};

const NIL=[['A','Ani',90],['B','Eka',95],['A','Budi',85],['B','Fajar',80],['A','Citra',85],['A','Dodi',70],['B','Gita',80]];
S.window={t:'Window function: menghitung per kelompok tanpa meringkas baris',
 p:[{k:'fn',l:'Fungsi',t:'o',o:[['rn','ROW_NUMBER()'],['rank','RANK()'],['dense','DENSE_RANK()'],['run','SUM(nilai) berjalan']],v:'rank'}],
 steps:P=>{const CX=[-3.4,-1.6,.4,2.8],Wd=[1,2,1.4,2.2],nm={rn:'ROW_NUMBER()',rank:'RANK()',dense:'DENSE_RANK()',run:'SUM(nilai)'}[P.fn]||'RANK()';
  const cell=(r,j,z,c,t)=>B('w'+r[1]+j,CX[j],0,z,{w:Wd[j],h:.32,d:.62,c,t:t??String(r[j])});
  const PC=k=>k==='A'?'acc':'warn';
  const part=[...NIL].sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:0),urut=[...NIL].sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:b[2]-a[2]);
  const zz=(list)=>{let g=0,prev=null;return list.map((r,k)=>{if(prev&&prev!==r[0])g++;prev=r[0];return (k-3)*.72+g*.6-.3})};
  const hit=r=>{const p=urut.filter(x=>x[0]===r[0]),i=p.indexOf(r);if(P.fn==='rn')return i+1;if(P.fn==='rank')return p.filter(x=>x[2]>r[2]).length+1;
    if(P.fn==='dense')return new Set(p.filter(x=>x[2]>r[2]).map(x=>x[2])).size+1;return p.slice(0,i+1).reduce((a,x)=>a+x[2],0)};
  const head=on=>['kelas','nama','nilai',on?nm:''].map((h,j)=>h?G('h'+j,CX[j],.75,-3.4,h,'idx'):null).filter(Boolean);
  const lt=lantai(10,7.4);
  const baris=(list,col,on)=>{const Z=zz(list);return list.flatMap((r,k)=>[...[0,1,2].map(j=>cell(r,j,Z[k],col(r))),...(on?[cell(r,3,Z[k],'ok',String(hit(r)))]:[])])};
  const seri=urut.filter((r,k)=>urut.some(x=>x!==r&&x[0]===r[0]&&x[2]===r[2]));
  return [
   {cap:`Tabel nilai ${NIL.length} siswa dari kelas A dan B, urutannya acak.`,it:[lt,...head(0),...baris(NIL,()=>'mute',0)]},
   {cap:'<code>PARTITION BY kelas</code> membagi baris menjadi jendela per kelas. Perhitungan nanti hanya melihat baris di jendelanya sendiri.',it:[lt,...head(0),...baris(part,r=>PC(r[0]),0)]},
   {cap:'<code>ORDER BY nilai DESC</code> mengurutkan baris <b>di dalam</b> setiap jendela, dari nilai tertinggi.',it:[lt,...head(0),...baris(urut,r=>PC(r[0]),0)]},
   {cap:`<code>${nm} OVER (PARTITION BY kelas ORDER BY nilai DESC)</code> menambah satu kolom baru. ${P.fn==='rn'?'ROW_NUMBER selalu 1, 2, 3, … meski nilainya sama.':P.fn==='rank'?'RANK memberi angka sama untuk nilai kembar, lalu melompat (1, 2, 2, 4).':P.fn==='dense'?'DENSE_RANK memberi angka sama untuk nilai kembar tanpa lompatan (1, 2, 2, 3).':'SUM berjalan menjumlahkan nilai dari atas sampai baris ini, dan mulai lagi di kelas berikutnya.'}${seri.length&&P.fn!=='run'?` Perhatikan ${seri.map(r=>r[1]).join(' dan ')}.`:''}`,
    it:[lt,...head(1),...baris(urut,r=>PC(r[0]),1)]},
   {cap:'Bedanya dengan GROUP BY: GROUP BY meringkas banyak baris menjadi satu, sedangkan window function <b>mempertahankan setiap baris</b> dan menambah kolom hasil. Ganti fungsinya di panel Eksperimen.',it:[lt,...head(1),...baris(urut,r=>PC(r[0]),1)]}]}};

S.mvcc={t:'MVCC: setiap UPDATE membuat versi baris baru',
 p:[{k:'u',l:'Jumlah UPDATE',t:'n',min:1,max:5,v:3},{k:'vac',l:'Jalankan VACUUM?',t:'o',o:[['1','Ya'],['0','Belum']],v:'1'}],
 steps:P=>{const u=Math.max(1,Math.min(5,P.u)),X=k=>(k-u/2)*1.55,ver=(k,c,t)=>B('v'+k,X(k),0,0,{w:1.3,h:.7,d:1.1,c,t:t||`stok=${50-k*5}`});
  const lt=lantai(Math.max(8,u*1.6+3),4),all=f=>Array.from({length:u+1},(_,k)=>ver(k,f(k)));
  const xid=k=>G('x'+k,X(k),1,0,`xmin ${100+k}${k<u?` · xmax ${101+k}`:''}`,'idx');
  const baca=on=>on?[B('rd',X(0),2.2,1.6,{w:.5,h:.5,d:.5,c:'warn',ball:1,t:'T1'}),R('rr',[X(0),1.95,0],[X(0),.4,0],'warn')]:[];
  return [
   {cap:'<code>INSERT</code> membuat versi pertama baris produk (stok = 50). Setiap versi mencatat <b>xmin</b>: nomor transaksi yang membuatnya.',it:[lt,ver(0,'ok'),xid(0)]},
   {cap:'Transaksi <b>T1</b> mulai membaca dan melihat versi ini. Selama T1 berjalan, ia harus terus melihat data yang sama.',it:[lt,ver(0,'ok'),xid(0),...baca(1)]},
   {cap:`${u}× <code>UPDATE</code>: PostgreSQL <b>tidak menimpa</b> baris lama. Ia membuat versi baru dan menandai versi lama dengan <b>xmax</b>. T1 tetap membaca versi lamanya tanpa dikunci: pembaca tidak menghalangi penulis.`,
    it:[lt,...all(k=>k===u?'ok':'mute'),...Array.from({length:u+1},(_,k)=>xid(k)),...baca(1)]},
   {cap:`T1 selesai. Sekarang ${u} versi lama tidak dipakai siapa pun: ini <b>dead tuple</b>. Mereka masih memakan ruang disk dan memperlambat scan. Inilah <b>bloat</b>.`,
    it:[lt,...all(k=>k===u?'ok':'bad'),...Array.from({length:u},(_,k)=>G('d'+k,X(k),1,0,'mati','bad')),G('x'+u,X(u),1,0,`xmin ${100+u}`,'idx')]},
   String(P.vac)==='1'?{cap:'<code>VACUUM</code> menyapu dead tuple sehingga ruangnya bisa dipakai ulang. Autovacuum menjalankannya otomatis di latar; pantau dengan <code>pg_stat_user_tables</code>.',it:[lt,ver(u,'ok'),G('x'+u,X(u),1,0,`xmin ${100+u}`,'idx'),...Array.from({length:u},(_,k)=>B('ks'+k,X(k),-.38,0,{w:1.3,h:.06,d:1.1,c:'glass',flat:1}))]}
     :{cap:'Tanpa VACUUM, dead tuple terus menumpuk setiap kali ada UPDATE dan DELETE. Pilih "Ya" di Eksperimen untuk melihat VACUUM bekerja.',it:[lt,...all(k=>k===u?'ok':'bad'),...Array.from({length:u},(_,k)=>G('d'+k,X(k),1,0,'mati','bad'))]}]}};

S.repl={t:'Replikasi: salinan database yang selalu mengikuti primary',
 p:[{k:'r',l:'Jumlah replika',t:'n',min:1,max:3,v:2},{k:'mode',l:'Mode',t:'o',o:[['async','Asinkron'],['sync','Sinkron']],v:'async'},{k:'mati',l:'Primary mati?',t:'o',o:[['0','Tidak'],['1','Ya']],v:'1'}],
 steps:P=>{const r=Math.max(1,Math.min(3,P.r)),RY=i=>(i-(r-1)/2)*1.5+.6,PX=-1,RX=3.2,CX=-4.6,sync=P.mode==='sync';
  const prim=(c,t='primary')=>B('pri',PX,.6,0,{w:1.8,h:1.1,d:1.4,c,t});
  const rep=(f,lab=i=>'replika '+(i+1))=>Array.from({length:r},(_,i)=>B('rep'+i,RX,RY(i),0,{w:1.8,h:.8,d:1.2,c:f(i),t:lab(i)}));
  const wal=on=>Array.from({length:r},(_,i)=>R('w'+i,[PX+.9,.6,0],[RX-.9,RY(i),0],on?'ok':'mute'));
  const cli=B('cli',CX,.6,0,{w:.9,h:.9,d:.9,c:'warn',t:'app'}),lt=lantai(11,4);
  const s=[
   {lb:'Tulis',cap:'Aplikasi menulis data (INSERT, UPDATE) hanya ke <b>primary</b>. Setiap perubahan dicatat dulu di <b>WAL</b> (write-ahead log).',it:[lt,cli,R('cw',[CX+.45,.6,0],[PX-.9,.6,0],'warn'),prim('acc'),...rep(()=>'mute'),...wal(0)]},
   {lb:'Kirim WAL',cap:sync?'Mode <b>sinkron</b>: primary menunggu replika mengonfirmasi sudah menerima WAL sebelum COMMIT selesai. Data aman, tetapi setiap tulisan sedikit lebih lambat.':'Mode <b>asinkron</b>: primary langsung menjawab COMMIT, lalu WAL mengalir ke replika. Cepat, tetapi replika bisa tertinggal beberapa milidetik (<i>replication lag</i>).',
    it:[lt,cli,prim('acc'),...rep(()=>'ok'),...wal(1),...(sync?[G('ack',(PX+RX)/2,RY(0)+1.1,0,'tunggu konfirmasi','warn')]:[])]},
   {lb:'Baca',cap:'Replika bisa melayani query baca (SELECT), sehingga beban primary berkurang. Ini disebut <i>read scaling</i>.',it:[lt,cli,prim('acc'),...rep(()=>'ok',()=>'SELECT ✓'),...wal(1)]}];
  if(String(P.mati)==='1')s.push(
   {lb:'Primary mati',cap:'Primary tiba-tiba mati. Penulisan berhenti, tetapi replika masih punya salinan data.',it:[lt,cli,prim('bad','mati'),...rep(()=>'acc'),...wal(0)]},
   {lb:'Failover',cap:`<b>Failover</b>: replika 1 dipromosikan menjadi primary baru (misalnya oleh Patroni). Aplikasi diarahkan ke sana.${sync?' Dengan mode sinkron, tidak ada transaksi yang hilang.':' Dengan mode asinkron, transaksi terakhir yang belum terkirim bisa hilang.'}`,
    it:[lt,cli,prim('mute','mati'),...rep(i=>i===0?'ok':'acc',i=>i===0?'primary baru':'replika '+(i+1)),R('cw',[CX+.45,.6,0],[RX-.9,RY(0),0],'warn')]});
  s.push({lb:'Intinya',cap:'Replikasi untuk ketersediaan tinggi dan membagi beban baca. Replikasi <b>bukan backup</b>: DELETE yang salah ikut tersalin ke replika. Tetap buat backup terjadwal.',it:s[s.length-1].it});
  return s}};

/* ===================== WEB, FRONTEND, DSA, DATA ===================== */
/* graf umum di bidang xy: N = {k:[x,y,teks]}, warna simpul dan ruas ditentukan fungsi */
function graf(N,Ed,col,ecol,w=1){const ys=Object.values(N).map(n=>n[1]),it=[lantai(10,3,Math.min(...ys)-1.4)];
  Ed.forEach(([a,b])=>{const A=N[a],Bn=N[b];it.push(R('e'+a+'_'+b,[A[0],A[1],0],[Bn[0],Bn[1],0],ecol?ecol(a,b):'mute'))});
  Object.entries(N).forEach(([k,[x,y,t]])=>it.push(B('n'+k,x,y,0,{w:t.length>4?Math.max(1.4,t.length*.17)*w:.9,h:.75,d:.75,c:col(k),t:E(t)})));return it}

/* ---------- HTTP: perjalanan request ---------- */
S.http={t:'Cara web bekerja: perjalanan satu request dari browser ke server dan kembali',
 p:[{k:'cache',l:'Alamat IP sudah di-cache?',t:'o',o:[['0','Belum'],['1','Sudah']],v:'0'},{k:'st',l:'Jawaban server',t:'o',o:[['200','200 OK'],['404','404 Not Found'],['500','500 Server Error']],v:'200'}],
 steps:P=>{const BX=-4.2,SX=1.4,DX=4.4,DNS=[-.9,2.7],st=String(P.st),c=String(P.cache)==='1';
  const sc=st==='200'?'ok':st==='404'?'warn':'bad',lt=lantai(11,3.6);
  const base=(b='acc',s='acc',d='acc',n='mute')=>[lt,B('br',BX,.3,0,{w:1.8,h:1.3,d:1.2,c:b,t:'browser'}),B('dns',DNS[0],DNS[1],0,{w:1.3,h:.6,d:.9,c:n,t:'DNS'}),
    B('srv',SX,.3,0,{w:1.5,h:1.6,d:1.2,c:s,t:'server'}),B('db',DX,.1,0,{w:1.2,h:1.1,d:1.2,c:d,t:'DB'})];
  const pk=(x,y,col,t)=>B('pk',x,y,0,{w:.5,h:.5,d:.5,c:col,ball:1,t});
  const ln=(id,a,b,col)=>R(id,a,b,col);
  return [
   {cap:'Kamu mengetik <code>tokonusantara.id/produk</code> lalu menekan Enter. Browser hanya tahu <b>nama</b> situsnya, belum tahu alamat komputernya.',it:[...base('warn'),G('url',BX,1.6,0,'tokonusantara.id/produk','idx')]},
   c?{cap:'Alamat IP situs ini sudah tersimpan di <b>cache</b> browser dari kunjungan sebelumnya, jadi tanya DNS dilewati. Hemat puluhan milidetik.',it:[...base('ok'),G('ip',BX,1.6,0,'IP dari cache: 103.10.2.7','ok')]}
    :{cap:'Browser bertanya ke <b>DNS</b>, buku telepon internet: "berapa alamat IP tokonusantara.id?" DNS menjawab <code>103.10.2.7</code>.',it:[...base('acc','acc','acc','ok'),ln('ld',[BX+.9,.9,0],[DNS[0]-.6,DNS[1],0],'ok'),pk(DNS[0]-1.6,DNS[1]-.4,'warn','?'),G('ip',DNS[0],DNS[1]+.8,0,'103.10.2.7','ok')]},
   {cap:'Browser mengirim <b>HTTP request</b> ke server: <code>GET /produk</code> beserta header seperti <code>Accept</code> dan cookie. Dengan HTTPS, isinya dienkripsi di perjalanan.',it:[...base('acc','warn'),ln('lr',[BX+.9,.3,0],[SX-.75,.3,0],'warn'),pk((BX+SX)/2,.75,'warn','GET'),G('req',(BX+SX)/2,1.6,0,'GET /produk','idx')]},
   st==='404'?{cap:'Server mencari rute <code>/produk</code> tetapi tidak menemukannya. Tidak perlu bertanya ke database.',it:[...base('acc','warn'),G('err',SX,2,0,'rute tidak ada','warn')]}
    :{cap:st==='500'?'Server menjalankan kode untuk rute itu dan bertanya ke database, tetapi query-nya gagal (misalnya tabel tidak ada). Ini kesalahan di sisi server.':'Server menjalankan kode untuk rute itu: bertanya ke database <code>SELECT * FROM produk</code>, lalu menyusun hasilnya menjadi HTML atau JSON.',
      it:[...base('acc','warn',st==='500'?'bad':'ok'),ln('lq',[SX+.75,.3,0],[DX-.6,.3,0],st==='500'?'bad':'ok'),pk((SX+DX)/2,.75,st==='500'?'bad':'ok','SQL')]},
   {cap:`Server mengirim <b>HTTP response</b> dengan kode status <code>${st}</code>${st==='200'?': berhasil, isinya data produk.':st==='404'?': halaman tidak ditemukan (kesalahan di alamat yang diminta).':': server error (kesalahan di sisi server).'} Kode 2xx berarti berhasil, 3xx dialihkan, 4xx salah di klien, 5xx salah di server.`,
    it:[...base('acc',sc),ln('lr',[BX+.9,.3,0],[SX-.75,.3,0],sc),pk((BX+SX)/2,.75,sc,st)]},
   {cap:st==='200'?'Browser membaca HTML, lalu meminta file lain yang dibutuhkan (CSS, JS, gambar) dengan cara yang sama, dan menggambar halamannya. Semua ini biasanya selesai dalam ratusan milidetik.':'Browser menampilkan halaman kesalahan. Buka DevTools → tab <b>Network</b> untuk melihat setiap request, kode status, dan waktunya.',
    it:[...base(sc,'acc'),G('hasil',BX,1.6,0,st==='200'?'halaman tampil ✓':'halaman error '+st,sc)]}]}};

/* ---------- Flexbox dan Grid ---------- */
S.flex={t:'Flexbox dan Grid: menata kotak di sepanjang sumbu',
 p:[{k:'dir',l:'flex-direction',t:'o',o:[['row','row (mendatar)'],['column','column (menurun)']],v:'row'},
  {k:'jc',l:'justify-content',t:'o',o:[['flex-start','flex-start'],['center','center'],['space-between','space-between'],['space-around','space-around']],v:'space-between'},
  {k:'n',l:'Jumlah item',t:'n',min:2,max:6,v:4}],
 steps:P=>{const n=Math.max(2,Math.min(6,P.n)),row=P.dir!=='column',CW=8,CH=4,pad=.2,IW=CW-2*pad,IH=CH-2*pad;
  const L=row?IW:IH,s=row?1.15:.55,KC=['acc','warn','ok','idx','acc','warn'];
  const box=[lantai(10,3,-2.6),B('cont',0,0,-.35,{w:CW,h:CH,d:.15,c:'glass'})];
  const it=(i,cx,cy,w,h,c)=>B('i'+i,cx,cy,0,{w,h,d:.5,c:c||KC[i],t:String(i+1)});
  const tempat=(jc,sizes)=>{const tot=sizes.reduce((a,b)=>a+b,0),free=Math.max(0,L-tot);let start=0,gap=0;
    if(jc==='center')start=free/2;else if(jc==='space-between')gap=n>1?free/(n-1):0;else if(jc==='space-around'){gap=free/n;start=gap/2}
    const out=[];let p=start;sizes.forEach(z=>{out.push(p+z/2-L/2);p+=z+gap});return out};
  const tata=(jc,align,grow)=>{const sizes=Array.from({length:n},(_,i)=>grow&&i===1?L-s*(n-1):s),pos=tempat(grow?'flex-start':jc,sizes);
    return sizes.map((z,i)=>{const cross=align==='center'?(row?.9:1.6):(row?IH:IW);
      return row?it(i,pos[i],0,z-.06,cross-.06):it(i,0,-pos[i],cross-.06,z-.06)})};
  const sumbu=row?G('ax',0,CH/2+.45,0,'sumbu utama →','idx'):G('ax',-CW/2-.9,0,0,'sumbu utama ↓','idx');
  const blok=Array.from({length:n},(_,i)=>it(i,0,IH/2-.3-i*.62,IW-.06,.56));
  const cols=3,rows=Math.ceil(n/cols),gw=IW/cols,gh=IH/rows;
  const grid=Array.from({length:n},(_,i)=>it(i,(i%cols+.5)*gw-IW/2,IH/2-(Math.floor(i/cols)+.5)*gh,gw-.2,gh-.2));
  return [
   {cap:'Tanpa aturan apa pun, setiap <code>div</code> adalah elemen <b>block</b>: mengambil lebar penuh dan turun ke baris berikutnya. Inilah alur normal.',it:[...box,...blok]},
   {cap:`<code>display: flex</code> mengubah wadah menjadi flex container. Anak-anaknya berjajar di <b>sumbu utama</b> (${row?'mendatar, karena flex-direction: row':'menurun, karena flex-direction: column'}) dan secara bawaan meregang penuh di sumbu silang.`,it:[...box,...tata('flex-start','stretch'),sumbu]},
   {cap:`<code>justify-content: ${P.jc}</code> mengatur sisa ruang di <b>sumbu utama</b>. ${P.jc==='space-between'?'Item pertama dan terakhir menempel ke tepi, sisanya dibagi rata.':P.jc==='center'?'Semua item berkumpul di tengah.':P.jc==='space-around'?'Setiap item mendapat ruang yang sama di kedua sisinya.':'Semua item menempel di awal sumbu.'}`,it:[...box,...tata(P.jc,'stretch'),sumbu]},
   {cap:'<code>align-items: center</code> mengatur posisi di <b>sumbu silang</b>: item tidak lagi meregang, melainkan berada di tengah. Ingat: justify untuk sumbu utama, align untuk sumbu silang.',it:[...box,...tata(P.jc,'center'),sumbu]},
   {cap:'<code>flex-grow: 1</code> pada item 2 membuatnya <b>menyerap semua sisa ruang</b>. Pola ini dipakai untuk kolom pencarian yang mengisi navbar.',it:[...box,...tata(P.jc,'center',1),sumbu]},
   {cap:`<code>display: grid; grid-template-columns: repeat(3, 1fr)</code> menata dalam <b>dua dimensi</b> sekaligus: ${n} item mengisi ${rows} baris × 3 kolom. Pakai flexbox untuk satu baris atau kolom, grid untuk tata letak baris dan kolom.`,it:[...box,...grid]}]}};

/* ---------- React: komponen, props, state ---------- */
S.react={t:'React: pohon komponen, props turun, state memicu render ulang',
 p:[{k:'klik',l:'Klik tombol "+ Keranjang"',t:'n',min:1,max:9,v:1},{k:'memo',l:'Kartu dibungkus React.memo?',t:'o',o:[['0','Tidak'],['1','Ya']],v:'0'}],
 steps:P=>{const N={app:[0,2.4,'App'],hd:[-2.6,.9,'Header'],ls:[2,.9,'DaftarProduk'],k1:[.4,-.7,'Kartu'],k2:[2,-.7,'Kartu'],k3:[3.6,-.7,'Kartu']};
  const Ed=[['app','hd'],['app','ls'],['ls','k1'],['ls','k2'],['ls','k3']],memo=String(P.memo)==='1',k=P.klik;
  const g=(col,ecol,extra=[])=>[...graf(N,Ed,col,ecol,.85),...extra];
  const isi=G('cnt',-2.6,1.6,0,'🛒 '+k,'ok');
  return [
   {cap:'Antarmuka React disusun dari <b>komponen</b>: fungsi yang mengembalikan JSX. <code>App</code> berisi <code>Header</code> dan <code>DaftarProduk</code>, yang berisi tiga <code>Kartu</code>.',it:g(()=>'acc')},
   {cap:'<b>Props</b> mengalir <b>turun</b> dari induk ke anak, seperti argumen fungsi. <code>&lt;Kartu produk={p} /&gt;</code>: Kartu hanya membaca props, tidak boleh mengubahnya.',it:g(x=>x==='hd'?'mute':'acc',(a,b)=>a==='app'&&b==='hd'?'mute':'warn',[G('pp',3.4,.1,0,'props ↓','warn')])},
   {cap:'<b>State</b> adalah data milik komponen yang bisa berubah: <code>const [jumlah, setJumlah] = useState(0)</code> di App. Kartu menerima fungsi <code>onTambah</code> lewat props dan memanggilnya saat tombol diklik.',it:g(x=>x==='app'?'warn':x==='k2'?'ok':'mute',(a,b)=>b==='k2'||(a==='app'&&b==='ls')?'ok':'mute',[G('ev',.7,1.9,0,'↑ onTambah()','ok')])},
   {cap:`<code>setJumlah</code> dipanggil ${k}×. Setiap kali state App berubah, App dan <b>semua turunannya</b> dirender ulang.${memo?' Kecuali Kartu: dengan <code>React.memo</code>, React melewatinya karena props-nya tidak berubah.':' Kartu ikut dirender ulang walaupun datanya sama.'}`,
    it:g(x=>x[0]==='k'&&memo?'mute':'warn',(a,b)=>b[0]==='k'&&memo?'mute':'warn',[isi])},
   {cap:'React membandingkan hasil render baru dengan yang lama (<b>reconciliation</b>) dan hanya mengubah bagian DOM yang berbeda: angka di Header. Bagian lain di layar tidak disentuh.',it:g(x=>x==='hd'?'ok':'mute',()=>'mute',[isi])}]}};

/* ---------- hash table ---------- */
S.hash={t:'Hash table: fungsi hash menunjuk laci yang tepat',
 p:[{k:'isi',l:'Kunci (pisahkan koma)',t:'s',v:'apel, jeruk, mangga, kiwi, salak, duku'},{k:'m',l:'Jumlah laci (bucket)',t:'n',min:3,max:7,v:5},{k:'cari',l:'Kunci yang dicari',t:'s',v:'kiwi'}],
 steps:P=>{let K=[...new Set(nama(P.isi,7).map(s=>s.toLowerCase()))];if(!K.length)K=['apel'];const m=Math.max(3,Math.min(7,P.m));
  const kode=s=>[...s].reduce((a,c)=>a+c.charCodeAt(0),0),h=s=>kode(s)%m,X=i=>(i-(m-1)/2)*1.45;
  const cari=(String(P.cari).split(',')[0]||'').trim().toLowerCase().slice(0,8)||K[0],hc=h(cari);
  const pos={},isi=Array.from({length:m},()=>[]);K.forEach(k=>{const b=h(k);pos[k]=[b,isi[b].length];isi[b].push(k)});
  const laci=f=>Array.from({length:m},(_,i)=>B('b'+i,X(i),-.35,0,{w:1.25,h:.2,d:1.3,c:f?f(i):'glass',t:String(i)}));
  const kunci=(k,c,on=true)=>{const [b,d]=pos[k];return B('k'+k,on?X(b):X(b),on?d*.55+.05:3,0,{w:1.2,h:.48,d:.9,c,t:E(k)})};
  const lt=lantai(Math.max(8,m*1.5+1),3.4,-.6),tab=K.filter(k=>isi[pos[k][0]].length>1),k0=K[0];
  const rantai=isi[hc],ada=rantai.includes(cari);
  return [
   {cap:`Hash table menyiapkan ${m} <b>laci</b> bernomor 0 sampai ${m-1}. Tujuannya: menyimpan dan menemukan data <b>tanpa memeriksa satu per satu</b>.`,it:[lt,...laci()]},
   {cap:`<b>Fungsi hash</b> mengubah kunci menjadi nomor laci. Di sini: jumlahkan kode huruf "${E(k0)}" = ${kode(k0)}, lalu ${kode(k0)} mod ${m} = <b>${h(k0)}</b>. Kunci yang sama selalu menghasilkan nomor yang sama.`,
    it:[lt,...laci(i=>i===h(k0)?'ok':'glass'),kunci(k0,'warn'),G('rumus',X(h(k0)),2.1,0,`${kode(k0)} mod ${m} = ${h(k0)}`,'warn')]},
   {cap:`Semua kunci dimasukkan dengan cara yang sama: ${K.map(k=>`${E(k)}→${h(k)}`).join(', ')}.`,it:[lt,...laci(),...K.map(k=>kunci(k,'acc'))]},
   tab.length?{cap:`<b>Tabrakan</b> (collision): ${tab.map(E).join(', ')} mendapat laci yang sama. Solusinya <i>chaining</i>: laci menyimpan daftar kecil, jadi kunci ditumpuk di laci itu.`,it:[lt,...laci(i=>isi[i].length>1?'bad':'glass'),...K.map(k=>kunci(k,tab.includes(k)?'warn':'mute'))]}
    :{cap:'Kali ini tidak ada tabrakan: setiap kunci mendapat laci sendiri. Kalau dua kunci mendapat laci yang sama, laci itu menyimpan daftar kecil (<i>chaining</i>). Coba kurangi jumlah laci di Eksperimen.',it:[lt,...laci(),...K.map(k=>kunci(k,'acc'))]},
   {cap:`Mencari "${E(cari)}": hitung hash-nya = <b>${hc}</b>, langsung buka laci ${hc}${rantai.length>1?`, lalu bandingkan ${rantai.length} kunci di dalamnya`:''}. ${ada?'<b>Ketemu.</b>':'Tidak ada di laci itu, jadi kunci ini <b>tidak tersimpan</b>.'} Laci lain tidak disentuh sama sekali.`,
    it:[lt,...laci(i=>i===hc?(ada?'ok':'bad'):'glass'),...K.map(k=>kunci(k,k===cari?'ok':pos[k][0]===hc?'warn':'mute')),G('cari',X(hc),Math.max(1,rantai.length*.55+.6),0,'hash("'+E(cari)+'") = '+hc,ada?'ok':'bad')]},
   {cap:`Rata-rata pencarian <b>O(1)</b>: berapa pun banyak datanya, langkahnya tetap. Load factor = ${K.length}/${m} = ${(K.length/m).toFixed(2)}. Kalau terlalu penuh, tabel diperbesar (rehash) agar tabrakan tetap jarang. <code>dict</code> Python dan <code>HashMap</code> Java bekerja seperti ini.`,it:[lt,...laci(),...K.map(k=>kunci(k,'acc'))]}]}};

/* ---------- binary search ---------- */
S.bsearch={t:'Binary search: buang separuh data setiap langkah',
 p:[{k:'n',l:'Jumlah data (terurut)',t:'n',min:5,max:15,v:11},{k:'cari',l:'Angka yang dicari',t:'n',min:-99,max:999,v:56}],
 steps:P=>{const n=Math.max(5,Math.min(15,P.n)),A=[2,5,8,12,16,23,38,45,56,72,81,88,91,95,99].slice(0,n),X=i=>(i-(n-1)/2)*.78,c=P.cari;
  const lt=lantai(Math.max(8,n*.8+1.5),3);
  const sel=(lo,hi,mid,found)=>A.map((v,i)=>{const inR=i>=lo&&i<=hi;return B('a'+i,X(i),inR?0:-.25,0,{w:.68,h:inR?.62:.3,d:.8,c:i===mid?(found?'ok':'warn'):inR?'acc':'mute',t:String(v)})});
  const pin=(lo,hi,mid)=>[G('lo',X(lo),1.2,0,'lo','idx'),G('hi',X(hi),1.2,0,'hi','idx'),...(mid!=null?[G('mid',X(mid),1.8,0,'mid','warn')]:[])].filter((g,j,arr)=>!(g.id==='hi'&&lo===hi));
  const st=[{lb:'Data terurut',cap:`Ada ${n} angka yang sudah <b>terurut</b>. Binary search hanya bekerja pada data terurut. Kita mencari <b>${c}</b>.`,it:[lt,...sel(0,n-1),...pin(0,n-1)]}];
  let lo=0,hi=n-1,k=0,found=false;
  while(lo<=hi){const mid=(lo+hi)>>1;k++;const v=A[mid];
    if(v===c){found=true;st.push({lb:'Ketemu',cap:`mid = (${lo} + ${hi}) / 2 = ${mid}. A[${mid}] = ${v}: <b>ketemu</b> dalam ${k} langkah.`,it:[lt,...sel(lo,hi,mid,1),...pin(lo,hi,mid)]});break}
    st.push({lb:'Langkah '+k,cap:`mid = (${lo} + ${hi}) / 2 = ${mid}. A[${mid}] = ${v} ${v<c?`lebih kecil dari ${c}, jadi buang separuh <b>kiri</b>: lo = ${mid+1}.`:`lebih besar dari ${c}, jadi buang separuh <b>kanan</b>: hi = ${mid-1}.`}`,it:[lt,...sel(lo,hi,mid),...pin(lo,hi,mid)]});
    if(v<c)lo=mid+1;else hi=mid-1}
  if(!found)st.push({lb:'Tidak ada',cap:`lo melewati hi, artinya rentang pencarian habis: <b>${c} tidak ada</b>. Hanya ${k} angka yang diperiksa.`,it:[lt,...sel(1,0),G('x',0,1.4,0,'rentang kosong','bad')]});
  st.push({lb:'O(log n)',cap:`Binary search memeriksa ${k} angka; pencarian linear bisa memeriksa sampai ${n}. Untuk sejuta data cukup sekitar <b>20 langkah</b>, karena setiap langkah membuang separuh: O(log n).`,it:st[st.length-1].it});
  return st}};

/* ---------- graph: BFS dan DFS ---------- */
S.graph={t:'Graph: menjelajah simpul dengan BFS atau DFS',
 p:[{k:'mode',l:'Cara menjelajah',t:'o',o:[['bfs','BFS (melebar, pakai queue)'],['dfs','DFS (mendalam, pakai stack)']],v:'bfs'},{k:'s',l:'Mulai dari',t:'o',o:[['A','A'],['C','C'],['G','G']],v:'A'}],
 steps:P=>{const N={A:[-3.6,1.2,'A'],B:[-1.6,2.4,'B'],C:[-1.6,0,'C'],D:[.6,2.4,'D'],E:[.6,0,'E'],F:[3,1.2,'F'],G:[2.8,-1.2,'G']};
  const Ed=[['A','B'],['A','C'],['B','D'],['C','E'],['D','F'],['E','F'],['E','G'],['F','G']],adj={};
  Object.keys(N).forEach(k=>adj[k]=[]);Ed.forEach(([a,b])=>{adj[a].push(b);adj[b].push(a)});Object.values(adj).forEach(v=>v.sort());
  const bfs=P.mode!=='dfs',s=N[P.s]?P.s:'A',seen=new Set([s]),done=[],via={};let F=[[s,null]];const st=[];
  const tagF=()=>G('fr',0,-2.5,0,(bfs?'antrean: ':'stack: ')+(F.length?F.map(f=>f[0]).join(' '):'kosong'),'idx');
  const draw=(cur)=>graf(N,Ed,k=>k===cur?'warn':done.includes(k)?'ok':F.some(f=>f[0]===k)?'acc':'mute',(a,b)=>via[b]===a||via[a]===b?'ok':'mute');
  st.push({lb:'Mulai',cap:`Graph berisi ${Object.keys(N).length} simpul dan ${Ed.length} ruas. Kita menjelajah dengan <b>${bfs?'BFS':'DFS'}</b> mulai dari ${s}. ${bfs?'BFS memakai antrean (queue): yang masuk duluan diproses duluan.':'DFS memakai stack: yang terakhir masuk diproses duluan, jadi terus masuk ke dalam.'}`,it:[...draw(null),tagF()]});
  while(F.length){const [cur,par]=bfs?F.shift():F.pop();if(done.includes(cur))continue;done.push(cur);if(par)via[cur]=par;
    const baru=adj[cur].filter(x=>bfs?!seen.has(x):!done.includes(x));
    if(bfs)baru.forEach(x=>{seen.add(x);F.push([x,cur])});else [...baru].reverse().forEach(x=>F.push([x,cur]));
    st.push({lb:'Kunjungi '+cur,cap:`Ambil <b>${cur}</b> dari ${bfs?'depan antrean':'atas stack'}. Tetangga yang belum dikunjungi: ${baru.length?baru.join(', '):'tidak ada'}${baru.length?`, ${bfs?'masuk ke belakang antrean':'ditumpuk ke stack'}`:''}. Urutan sejauh ini: ${done.join(' → ')}.`,it:[...draw(cur),tagF()]})}
  st.push({lb:'Intinya',cap:`Urutan ${bfs?'BFS':'DFS'}: <b>${done.join(' → ')}</b>. ${bfs?'BFS menjelajah lapis demi lapis, sehingga menemukan jalur dengan ruas paling sedikit.':'DFS menelusuri satu cabang sampai mentok baru mundur; cocok untuk mendeteksi siklus dan topological sort.'} Ganti caranya di panel Eksperimen untuk membandingkan.`,it:[...draw(null)]});
  return st}};

/* ---------- pipeline data (ETL) ---------- */
S.etl={t:'Pipeline data: Extract, Transform, Load',
 p:[{k:'kotor',l:'Baris kotor (kosong/duplikat)',t:'n',min:0,max:3,v:2},{k:'mode',l:'Cara jalan',t:'o',o:[['batch','Batch (terjadwal)'],['stream','Streaming (terus-menerus)']],v:'batch'}],
 steps:P=>{const kt=Math.max(0,Math.min(3,P.kotor)),R8=8,SC=['acc','warn','mute'],src=i=>i%3,dirty=i=>i<kt*3&&i%3===1;
  const ST=[-3.9,-1.8,.2,2.2,4],lt=lantai(10.5,4);
  const sumber=[B('s0',ST[0],1.8,0,{w:1.4,h:.5,d:1,c:'acc',t:'DB app'}),B('s1',ST[0],.6,0,{w:1.4,h:.5,d:1,c:'warn',t:'CSV'}),B('s2',ST[0],-.6,0,{w:1.4,h:.5,d:1,c:'mute',t:'API'})];
  const tahap=on=>[G('tE',ST[1],2.9,0,'Extract',on==='E'?'warn':'idx'),G('tT',ST[2],2.9,0,'Transform',on==='T'?'warn':'idx'),G('tL',ST[3],2.9,0,'Load',on==='L'?'warn':'idx')];
  const wh=B('wh',ST[4],.2,0,{w:1.5,h:1.8,d:1.4,c:'mute',t:'warehouse'});
  const bersih=Array.from({length:R8},(_,i)=>i).filter(i=>!dirty(i));
  const row=(i,x,y,c,z=0)=>B('r'+i,x,y,z,{w:.42,h:.42,d:.42,c,t:dirty(i)?'!':''});
  const awal=i=>row(i,ST[0]+1.25,1.8-src(i)*1.2,SC[src(i)],(Math.floor(i/3)-1)*.45);
  const pipa=[R('p1',[ST[0]+.8,.6,0],[ST[3]+.5,.6,0],'mute')];
  return [
   {cap:`Data tersebar di tiga <b>sumber</b> dengan format berbeda: database aplikasi, file CSV, dan API. ${kt?`Ada ${kt} baris kotor (tanda !).`:'Semua baris bersih.'}`,it:[lt,...sumber,...tahap(),wh,...Array.from({length:R8},(_,i)=>awal(i))]},
   {cap:'<b>Extract</b>: pipeline menyalin data dari setiap sumber ke area sementara (staging) tanpa mengubah isinya.',it:[lt,...sumber,...tahap('E'),wh,...pipa,...Array.from({length:R8},(_,i)=>row(i,ST[1]+(i%2)*.5-.25,Math.floor(i/2)*.48-.2,SC[src(i)]))]},
   {cap:`<b>Transform</b>: data dibersihkan dan diseragamkan: format tanggal dan mata uang disamakan${kt?`, ${kt} baris kotor dibuang`:''}. Semua baris kini berwarna sama karena formatnya seragam.`,
    it:[lt,...sumber,...tahap('T'),wh,...pipa,...Array.from({length:R8},(_,i)=>dirty(i)?row(i,ST[2]+Math.floor(i/3)*.7-.7,-.35,'bad',1.4):row(i,ST[2]+(bersih.indexOf(i)%2)*.5-.25,Math.floor(bersih.indexOf(i)/2)*.48-.2,'ok'))]},
   {cap:`<b>Load</b>: ${bersih.length} baris bersih dimuat ke <b>data warehouse</b>, gudang data yang dirancang untuk analisis. Kalau pipeline dijalankan ulang, hasilnya harus tetap sama (<i>idempoten</i>).`,
    it:[lt,...sumber,...tahap('L'),B('wh',ST[4],.2,0,{w:1.5,h:1.8,d:1.4,c:'ok',t:'warehouse'}),...pipa,...bersih.map((i,j)=>row(i,ST[4]+(j%2)*.5-.25,Math.floor(j/2)*.48-.35,'ok',.95))]},
   {cap:'Analis dan dashboard membaca dari warehouse, bukan dari database aplikasi, sehingga query berat tidak mengganggu pengguna aplikasi.',
    it:[lt,...sumber,...tahap(),B('wh',ST[4],.2,0,{w:1.5,h:1.8,d:1.4,c:'ok',t:'warehouse'}),...[.8,1.4,1.1].map((h,j)=>B('bar'+j,ST[4]-.5+j*.5,1.6+h/2,0,{w:.38,h,d:.38,c:['acc','warn','ok'][j]})),G('dash',ST[4],3.4,0,'dashboard','idx')]},
   P.mode==='stream'?{cap:'<b>Streaming</b>: setiap kejadian (pesanan, klik) mengalir saat itu juga lewat antrean pesan seperti <b>Kafka</b>. Data di dashboard hampir real-time, tetapi sistemnya lebih rumit.',
      it:[lt,...sumber,...tahap(),B('wh',ST[4],.2,0,{w:1.5,h:1.8,d:1.4,c:'ok',t:'warehouse'}),R('p1',[ST[0]+.8,.6,0],[ST[3]+.5,.6,0],'ok'),...bersih.slice(0,5).map((i,j)=>row(i,ST[1]+j*1.1-.3,.6,'ok'))]}
    :{cap:'<b>Batch</b>: pipeline berjalan terjadwal, misalnya setiap malam pukul 01.00, memproses semua data sehari sekaligus. Penjadwalnya biasanya <b>Airflow</b> dalam bentuk DAG. Sederhana dan murah, tetapi datanya tertinggal sampai jadwal berikutnya.',
      it:[lt,...sumber,...tahap(),B('wh',ST[4],.2,0,{w:1.5,h:1.8,d:1.4,c:'ok',t:'warehouse'}),...pipa,G('jam',0,-1.6,0,'⏰ setiap hari 01.00','warn'),...Array.from({length:R8},(_,i)=>awal(i))]}]}};

/* ---------- sorting dasar ---------- */
S.sort={t:'Sorting dasar: bubble sort dan insertion sort langkah demi langkah',
 p:[{k:'isi',l:'Angka (pisahkan koma)',t:'s',v:'5, 2, 8, 1, 9, 3'},{k:'algo',l:'Algoritma',t:'o',o:[['bubble','Bubble sort'],['insert','Insertion sort']],v:'bubble'}],
 steps:P=>{let v=angka(P.isi,7).map(x=>Math.max(-99,Math.min(99,x)));if(v.length<2)v=[5,2,8,1];const n=v.length;
  const mx=Math.max(...v.map(Math.abs),1),X=i=>(i-(n-1)/2)*1.05,lt=lantai(Math.max(8,n*1.1+1.5),3);
  let a=v.map((x,i)=>({x,id:i}));const st=[];
  const bar=(o,i,c,up=0)=>{const h=.25+Math.abs(o.x)/mx*2.4;return B('s'+o.id,X(i),h/2-.5+up,0,{w:.82,h,d:.82,c,t:String(o.x)})};
  const snap=f=>a.map((o,i)=>bar(o,i,...f(i,o)));
  st.push({lb:'Mulai',cap:`Data awal: ${v.join(', ')}. Tinggi balok sesuai nilainya. Kita urutkan dari kecil ke besar dengan <b>${P.algo==='insert'?'insertion sort':'bubble sort'}</b>.`,it:[lt,...snap(()=>['acc'])]});
  let cmp=0,swp=0;
  if(P.algo==='insert'){
    for(let i=1;i<n;i++){const key=a[i];
      st.push({lb:'Ambil '+key.x,cap:`Ambil ${key.x}. Bagian kiri (hijau) sudah terurut; ${key.x} akan disisipkan ke posisi yang tepat di sana.`,it:[lt,...snap((j,o)=>o===key?['warn',.9]:j<i?['ok']:['acc'])]});
      let j=i-1;while(j>=0&&a[j].x>key.x){cmp++;a[j+1]=a[j];j--}if(j>=0)cmp++;a[j+1]=key;swp+=i-1-j;
      st.push({lb:'Sisipkan '+key.x,cap:`${i-1-j?`${i-1-j} angka yang lebih besar digeser ke kanan, lalu ${key.x} masuk di posisi ${j+1}.`:`${key.x} sudah lebih besar dari tetangga kirinya, jadi tetap di tempat.`}`,it:[lt,...snap((q,o)=>o===key?['warn']:q<=i?['ok']:['acc'])]})}}
  else{
    for(let p=0;p<n-1;p++){let tukar=false;
      for(let j=0;j<n-1-p;j++){cmp++;const t=a[j].x>a[j+1].x;if(t){[a[j],a[j+1]]=[a[j+1],a[j]];swp++;tukar=true}
        st.push({lb:`Putaran ${p+1}`,cap:`Bandingkan dua tetangga: ${t?`${a[j+1].x} &gt; ${a[j].x}, jadi <b>ditukar</b>.`:`${a[j].x} ≤ ${a[j+1].x}, sudah urut, tidak ditukar.`}${j===n-2-p?` Akhir putaran ${p+1}: angka terbesar yang tersisa sudah "menggelembung" ke kanan.`:''}`,
          it:[lt,...snap((q)=>q===j||q===j+1?[t?'bad':'warn']:q>=n-p?['ok']:['acc'])]})}
      if(!tukar){st.push({lb:'Berhenti dini',cap:`Satu putaran penuh tanpa pertukaran: data sudah urut, jadi berhenti lebih awal.`,it:[lt,...snap(()=>['ok'])]});break}}}
  st.push({lb:'Selesai',cap:`Terurut: ${a.map(o=>o.x).join(', ')}. Butuh ${cmp} perbandingan dan ${swp} ${P.algo==='insert'?'pergeseran':'pertukaran'}. Kedua algoritma ini O(n²): cukup untuk data kecil, tetapi untuk data besar pakai merge sort atau sort bawaan bahasa.`,it:[lt,...snap(()=>['ok'])]});
  return st}};

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
 p:[{k:'q',l:'Antrean (pisah koma)',t:'s',v:'Ani, Budi, Citra'},{k:'k',l:'Jumlah dilayani',t:'n',min:0,max:5,v:1}],
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
 p:[{k:'f',l:'Commit di branch fitur',t:'n',min:1,max:4,v:2},{k:'m',l:'Commit baru di main',t:'n',min:0,max:3,v:0}],
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
const RULES=[
 /* materi data, web, dan algoritma: judulnya spesifik, jadi berlaku di jalur mana pun (atau hanya jalur yang disebut) */
 [/^(select & from|where: menyaring baris|order by, limit & distinct|urutan eksekusi query|basis data relasional: tabel, baris, kolom|sintaks & kata kunci sql)$|memilih & menyaring: loc|katalog toko nusantara/i,'query',1],[/^operator$/i,'query',1,['sql']],
 [/fungsi agregat|^group ?by$|groupby|^having$|pivot_table|ringkasan stok/i,'group',1],[/^index:|jenis indeks|explain analyze|optimasi query|pg_stat_statements/i,'index',1],
 [/primary key|unique, not null|^create table$|tipe data dan constraint|database, schema, dan tabel|^alter, drop|merancang tabel dan relasi|tabel fakta & dimensi|laporan pesanan pelanggan/i,'fk',1],
 [/^acid|transaksi dan tingkat isolasi/i,'tx',1],[/mvcc|vacuum/i,'mvcc',1],[/replikasi|backup logis|dasar sistem terdistribusi|nosql, cap/i,'repl',1],
 [/window function|lead, lag|running total|peringkat & tren/i,'window',1],
 [/cara web bekerja|\bhttp|cors & csp|pengujian api rest|mengambil data: fetch|fetch di komponen|api dengan django rest|membuat rest api|^view dan url$|mengambil data api|route handlers|api & web scraping/i,'http',1],
 [/^flexbox$|^grid$|flexbox dan grid|sistem grid 12|display & alur normal|^row, column|^column, row|auto layout|section fitur dengan grid/i,'flex',1],
 [/komponen & jsx|^props$|state dengan usestate|useeffect|useref|usereducer|custom hook|input terkendali|memecah komponen|statelesswidget dan statefulwidget|state dengan remember|^props, emit|^ref, reactive|server component vs client/i,'react',1],
 [/hash table|hashing & collision|pola dict dan set|dictionary lanjutan & operasi set|^map: menghitung kemunculan|^set: himpunan tanpa duplikat/i,'hash',1],
 [/binary search(?! tree)|big-o|kompleksitas waktu/i,'bsearch',1],[/(?<!open )\bgraph\b|\bbfs\b|\bdfs\b|dijkstra|topological/i,'graph',1],
 [/\betl\b|pipeline|airflow|batch, streaming|kafka|siklus hidup data|lineage|warehouse, lake/i,'etl',1],[/sorting dasar|bubble sort|insertion sort/i,'sort',1],
 [/box model/i,'box',1],[/z-index|stacking context/i,'zindex',1],[/\bjoin\b/i,'join',1],[/\bbranch|\bmerge\b|\bcommit\b/i,'git',1],
 [/rekursi|recursion|call stack/i,'rekursi'],[/\bqueue|antrean|antrian|\bdeque/i,'queue'],[/(?<!tech |full ?)\bstack\b|tumpukan/i,'stack'],[/\bdom\b/i,'dom',1],
 [/\btree\b|pohon|\bbst\b|\bheap\b/i,'tree'],[/\b2d\b|dua dimensi|matriks|matrix|multidimensi/i,'matrix'],[/\barray|larik|\blist\b|arraylist|koleksi|collection/i,'array'],
 [/random number|bilangan acak|angka acak/i,'acak'],[/boolean logic|logika boolean|ekspresi boolean|operator logika/i,'bool'],[/perulangan|\bloop|\bfor\b|while|iterasi/i,'loop'],[/percabangan|\bif\b|kondisi|\bwhen\b|switch|keputusan/i,'if'],
 [/\bclass|kelas|\bobjek|\bobject|\boop\b|pewarisan|inheritance/i,'oop'],[/fungsi|function|\bmethod|metode|prosedur/i,'func'],[/variabel|variable|tipe data|val dan var/i,'var']];
const KODE=new Set(['java','python','js','jsx','ts','tsx','dart','kotlin','tx']),LOGIKA=/^(pseudo|flowg|logika|dsa|algo)$/;
window.v3dOf=function(t,title){if(!t||!title)return null;
  const kode=KODE.has(t.lang)||LOGIKA.test(t.k);
  for(const [rx,s,any,langs] of RULES)if(rx.test(title)&&(langs?langs.includes(t.lang)||langs.includes(t.k):any||kode))return s;return null};
window.V3DT=k=>S[k]&&S[k].t;
/* jenis loop awal ditebak dari judul pelajaran, agar adegan langsung menampilkan jenis yang dibahas */
window.v3dInit=function(k,title){const t=String(title||'');
  if(k==='sort')return /insertion/i.test(t)&&!/bubble/i.test(t)?{algo:'insert'}:null;
  if(k==='graph')return /\bdfs\b|topological/i.test(t)&&!/\bbfs\b/i.test(t)?{mode:'dfs'}:null;
  if(k==='flex')return /^grid$|grid 12/i.test(t)?{n:6}:null;
  if(k==='window')return /lead, lag|running total|tren/i.test(t)?{fn:'run'}:null;
  if(k==='group')return /having/i.test(t)?{hv:40}:null;
  if(k!=='loop')return null;
  if(/do-while|kapan for|repeat-until|simbol do\b|semua jenis/i.test(t))return {jenis:'banding'};
  if(/bersarang|nested|loop di dalam loop/i.test(t))return {jenis:'nested'};
  if(/\bbreak\b|penghentian/i.test(t))return {jenis:'break'};
  if(/continue/i.test(t))return {jenis:'continue'};
  if(/for\.\.\.of|for-each|foreach|enhanced/i.test(t))return {jenis:'each'};
  if(/while|tak pasti/i.test(t))return {jenis:'while'};
  return null};

/* ---------- mesin panggung ---------- */
const FACES=[['f',0,0],['b',0,180],['r',0,90],['l',0,-90],['t',90,0],['u',-90,0]];
function blockHTML(o,U){const w=o.w*U,h=o.h*U,d=o.d*U,ln=o.t?`<b>${o.t}</b>`:'',tt=o.tt?`<i>${o.tt}</i>`:'';
  return FACES.map(([k,rx,ry])=>{const fw=k==='r'||k==='l'?d:w,fh=k==='t'||k==='u'?d:h,tz=k==='r'||k==='l'?w/2:k==='t'||k==='u'?h/2:d/2;
    if(o.flat&&k!=='f'&&k!=='b')return '';
    return `<div class="f3 f-${k}" style="width:${fw}px;height:${fh}px;transform:translate(-50%,-50%) rotateX(${rx}deg) rotateY(${ry}deg) translateZ(${tz}px)">${k==='f'?ln+(o.flat?'':''):k==='t'?tt:''}</div>`}).join('')}
function place(o,U){return `translate3d(${o.x*U}px,${-o.y*U}px,${o.z*U}px) rotateY(${o.ry||0}deg) rotateZ(${-(o.rz||0)}deg)`}

/* label pendek tiap langkah untuk garis waktu (dipakai bila jumlah langkah cocok) */
const LB={var:['Rak memori','Isi umur','Isi nama','Ambil nilai','Ganti isi'],array:['Deretan kotak','Indeks 0','Akses langsung','Tambah','Panjang'],
 matrix:['Ukuran','Satu baris','Satu kolom','Satu sel'],if:['Persimpangan','Cek kondisi','Pilih cabang','Uji batas'],bool:['Masukan','Cek p dulu','Hasil','Tabel kebenaran'],
 acak:['Desimal 0..1','Ke rentang','Banyak lemparan','Seed'],stack:['Tumpukan','Push','Peek','Pop','Sisa'],queue:['Antrean','Enqueue','Dequeue','Maju'],
 rekursi:['Panggil','Tumpuk','Kasus dasar','Kembali','Kembali lagi','Hasil'],dom:['Akar','Anak','Telusuri'],oop:['Cetak biru','Objek pertama','Banyak objek','Pewarisan'],
 func:['Mesin','Masukan','Kembalikan','Pakai ulang'],box:['Kotak','Pisah lapisan','Padding','Border','Margin','Lebar total'],zindex:['Urutan HTML','Pakai z-index','Konteks tumpukan'],
 join:['Dua tabel','Cocokkan','Hasil'],git:['Commit','Branch','Merge'],
 query:['FROM','WHERE','SELECT','ORDER BY','LIMIT','Urutan eksekusi'],group:['Data','GROUP BY','Agregat','HAVING','Intinya'],index:['Tabel','Full scan','B-tree','Telusuri','Langsung ke baris','Biaya'],
 fk:['Dua tabel','Primary key','Foreign key','INSERT','Constraint'],window:['Data','PARTITION BY','ORDER BY','Fungsi','Beda GROUP BY'],mvcc:['INSERT','Transaksi baca','UPDATE','Dead tuple','VACUUM'],
 http:['URL','DNS','Request','Server','Response','Tampil'],flex:['Alur normal','display:flex','justify-content','align-items','flex-grow','Grid 2D'],react:['Komponen','Props','State','Render ulang','Ubah DOM'],
 hash:['Laci','Fungsi hash','Isi semua','Tabrakan','Cari','Rata-rata O(1)'],etl:['Sumber','Extract','Transform','Load','Analisis','Batch/stream']};
window.V3D=function(host,key,init,opt){const sc=S[key];if(!sc)return;const mini=!!(opt&&opt.mini);
  const rm=RMq(),RX0=-30,RY0=-38;let i=0,rx=RX0,ry=RY0,auto=null,U=40;const els=new Map();
  /* parameter eksperimen: nilai awal dari definisi adegan, langkah dihitung ulang setiap kali diubah */
  const PD=(sc.p||[]).map(d=>init&&init[d.k]!=null?{...d,v:init[d.k]}:d),P={};PD.forEach(d=>P[d.k]=d.v);
  const hitung=()=>{try{return typeof sc.steps==='function'?sc.steps(P):sc.steps}catch(e){return [{cap:'Nilai ini belum bisa digambar. Coba angka lain.',it:[lantai()]}]}};
  let steps=hitung();
  const label=(k)=>{const s=steps[k],L=LB[key];if(s&&s.lb)return s.lb;if(L&&L.length===steps.length)return L[k];
    if(k===0)return 'Mulai';if(k===steps.length-1)return 'Intinya';const c=String(s.cap).replace(/<[^>]+>/g,''),m=c.match(/^(Putaran \d+|Bandingkan)/);return m?m[0]:/ketemu/i.test(c)?'Ketemu':'Langkah '+(k+1)};
  const tagOf=k=>k===0?['Mulai','t-a']:k===steps.length-1?['Intinya','t-c']:['Konsep','t-b'];
  const fld=d=>{const id=`v3-${key}-${d.k}-${Math.random().toString(36).slice(2,7)}`;
    const inp=d.t==='o'?`<select id="${id}" data-k="${d.k}">${d.o.map(([v,l])=>`<option value="${v}"${v===d.v?' selected':''}>${l}</option>`).join('')}</select>`
      :d.t==='n'?`<input id="${id}" data-k="${d.k}" type="number" inputmode="numeric" step="1" min="${d.min}" max="${d.max}" value="${d.v}">`
      :`<input id="${id}" data-k="${d.k}" type="text" value="${d.v}" maxlength="40" autocomplete="off" spellcheck="false">`;
    return `<label class="s3fld" for="${id}"><span>${d.l}${d.t==='n'?` <small>${d.min}…${d.max}</small>`:''}</span>${inp}</label>`};
  const panel=PD.length?`<details class="s3exp" open><summary><span aria-hidden="true">🧪</span> Eksperimen: ubah angkanya</summary>
    <div class="s3form">${PD.map(fld).join('')}<button class="tlink" type="button" data-a="reset">Kembalikan nilai awal</button></div>
    <p class="s3tip">Perubahan langsung diterapkan pada langkah yang sedang dibuka.</p></details>`:'';
  host.innerHTML=`<div class="stg${mini?' is-mini':''}">
   <div class="stg-main">
    ${PD.length?'<div class="stg-hud" aria-label="Nilai yang sedang dipakai"></div>':''}
    <div class="s3" tabindex="0" role="img" aria-label="Adegan 3D: ${sc.t}. Seret atau tekan tombol panah untuk memutar."><div class="s3cam"><div class="w3"></div></div><div class="s3tags"></div>
     <span class="s3hint" aria-hidden="true">⟲ seret untuk memutar</span><button class="s3view" type="button" data-a="view" title="Kembali ke sudut awal">Sudut awal</button></div>
    <div class="stg-prog" aria-hidden="true"><i></i></div>
    <ol class="stg-tl" aria-label="Langkah"></ol>
   </div>
   <aside class="stg-rail">
    <div class="rail-top"><span class="rail-n"></span><span class="rail-tag"></span></div>
    <h4 class="rail-h"></h4>
    <p class="s3cap" aria-live="polite"></p>
    <div class="rail-nav"><button class="btn" type="button" data-a="prev">← Kembali</button><button class="btn primary" type="button" data-a="next"></button></div>
    <div class="rail-play"><button class="rp" type="button" data-a="replay">⟲ Ulangi <kbd>R</kbd></button><button class="rp" type="button" data-a="play" aria-pressed="false"></button><span class="rail-kb"><kbd>←</kbd><kbd>→</kbd> langkah</span></div>
    ${panel}
   </aside></div>`;
  const st=host.querySelector('.s3'),w=host.querySelector('.w3'),cap=host.querySelector('.s3cap'),tg=host.querySelector('.s3tags'),tl=host.querySelector('.stg-tl'),
    hud=host.querySelector('.stg-hud'),bar=host.querySelector('.stg-prog i'),bPlay=host.querySelector('[data-a=play]');
  /* label diproyeksikan ke 2D agar selalu terbaca dan tidak tertutup benda */
  const proj=(x,y,z)=>{const a=ry*Math.PI/180,b=rx*Math.PI/180,X=x*U,Y=-y*U,Z=z*U;
    const x1=X*Math.cos(a)+Z*Math.sin(a),z1=-X*Math.sin(a)+Z*Math.cos(a),y2=Y*Math.cos(b)-z1*Math.sin(b),z2=Y*Math.sin(b)+z1*Math.cos(b);
    const W=st.clientWidth,H=st.clientHeight,ox=W/2,oy=H*.4,cx=W/2,cy=H*.56,k=1100/(1100-z2);return [ox+(cx+x1-ox)*k,oy+(cy+y2-oy)*k]};
  const view=()=>{w.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg)`;
    const W=st.clientWidth;els.forEach(e=>{if(e._tag){const [l,t]=proj(...e._p),h=e.offsetWidth/2+4;e.style.left=Math.max(h,Math.min(W-h,l))+'px';e.style.top=t+'px'}})};
  const optLabel=d=>{const o=(d.o||[]).find(x=>String(x[0])===String(P[d.k]));return o?o[1]:P[d.k]};
  function hudDraw(){if(!hud)return;hud.innerHTML=PD.map(d=>`<span class="hud-c"><small>${d.l}</small><b>${E(String(d.t==='o'?optLabel(d):P[d.k]).slice(0,28))}</b></span>`).join('')}
  function tlDraw(){tl.innerHTML=steps.map((s,k)=>`<li><button type="button" data-go="${k}"${k===i?' aria-current="step"':''} class="${k<i?'done':k===i?'now':''}"><span class="tn">${k<i?'✓':k+1}</span><span class="tl-l">${label(k)}</span></button></li>`).join('')}
  function draw(again){if(i>steps.length-1)i=steps.length-1;const s=steps[i];U=Math.max(26,Math.min(60,st.clientWidth/11));const seen=new Set();
    if(again){els.forEach(e=>e.remove());els.clear()}
    let nf=0;
    s.it.forEach(o=>{seen.add(o.id);let e=els.get(o.id);const fresh=!e,prevC=e&&e._c,prevT=e&&e._t;
      if(fresh){e=document.createElement('div');els.set(o.id,e);(o.tag?tg:w).appendChild(e)}
      if(o.tag){e.className=`t3 ${o.c?'c-'+o.c:''}`;e.innerHTML=o.t;e._tag=1;e._p=[o.x,o.y,o.z];
        if(!rm&&(fresh||prevT!==o.t)){e.classList.add('pop')}e._t=o.t}
      else{e.className=`b3 c-${o.c}${o.ball?' ball':''}${o.rod?' rod':''}${o.flat?' flat':''}`;e.innerHTML=blockHTML(o,U);e.style.transform=place(o,U);
        /* berubah warna atau isi: kilau sebentar agar mata tertuju ke sana */
        if(!fresh&&!rm&&(prevC!==o.c||prevT!==o.t)&&o.c!=='floor'){e.classList.add('pulse');setTimeout(()=>e.classList.remove('pulse'),950)}
        e._c=o.c;e._t=o.t}
      /* benda baru muncul bergiliran, bukan sekaligus */
      if(fresh&&!rm){const d=Math.min(nf++,12)*70;e.style.transitionDelay=d+'ms';e.classList.add('in');
        requestAnimationFrame(()=>requestAnimationFrame(()=>e.classList.remove('in')));setTimeout(()=>{e.style.transitionDelay=''},d+800)}});
    els.forEach((e,id)=>{if(seen.has(id))return;els.delete(id);if(rm)e.remove();else{e.classList.add('out');setTimeout(()=>e.remove(),450)}});
    /* teks di sisi benda dikecilkan bila tidak muat (layar sempit) */
    w.querySelectorAll('.f3>b,.f3>i').forEach(t=>{const f=t.parentNode,cw=f.clientWidth-4,ch=f.clientHeight-2,sw=t.scrollWidth,sh=t.offsetHeight;
      const k=Math.min(1,cw/sw,ch/sh);t.style.transform=k<1?`scale(${Math.max(.35,k)})`:''});
    view();const N=steps.length,[tt,tc]=tagOf(i);
    cap.innerHTML=s.cap;host.querySelector('.rail-h').textContent=label(i);host.querySelector('.rail-n').textContent=`Langkah ${i+1} / ${N}`;
    const tgEl=host.querySelector('.rail-tag');tgEl.textContent=tt;tgEl.className='rail-tag '+tc;
    bar.style.width=((i+1)/N*100)+'%';tlDraw();hudDraw();
    host.querySelector('[data-a=prev]').disabled=i===0;
    host.querySelector('[data-a=next]').innerHTML=i<N-1?`Lanjut: ${label(i+1)} →`:'↺ Mulai lagi dari awal'}
  const setPlay=on=>{bPlay.setAttribute('aria-pressed',on?'true':'false');bPlay.innerHTML=on?'❚❚ Jeda <kbd>Spasi</kbd>':'▶ Putar <kbd>Spasi</kbd>'};
  const stop=()=>{clearInterval(auto);auto=null;setPlay(false)};
  const go=d=>{stop();const j=i+d;if(j<0)return;if(j>steps.length-1){if(d>0&&i===steps.length-1){i=0;draw()}return}i=j;draw()};
  const toggle=()=>{if(auto)return stop();if(i===steps.length-1){i=0;draw()}setPlay(true);
    auto=setInterval(()=>{if(!host.isConnected)return stop();if(i>=steps.length-1){stop();if(mini&&opt.onEnd)opt.onEnd();return}i++;draw()},mini?3000:3400)};
  const replay=()=>{draw(true)};
  if(!mini&&typeof stepReg==='function')stepReg({host,go,toggle,replay});
  host.addEventListener('click',e=>{const g=e.target.closest('[data-go]');if(g){stop();i=+g.dataset.go;draw();return}
    const a=e.target.closest('[data-a]');if(!a)return;const k=a.dataset.a;
    if(k==='next')go(1);else if(k==='prev')go(-1);else if(k==='replay')replay();else if(k==='play')toggle();
    else if(k==='view'){rx=RX0;ry=RY0;view()}});
  let drag=null;
  st.addEventListener('pointerdown',e=>{if(e.target.closest('button'))return;drag={x:e.clientX,y:e.clientY,rx,ry};st.setPointerCapture(e.pointerId);st.classList.add('grab')});
  st.addEventListener('pointermove',e=>{if(!drag)return;ry=drag.ry+(e.clientX-drag.x)*.45;rx=Math.max(-80,Math.min(25,drag.rx-(e.clientY-drag.y)*.35));view()});
  const up=()=>{drag=null;st.classList.remove('grab')};st.addEventListener('pointerup',up);st.addEventListener('pointercancel',up);
  st.addEventListener('keydown',e=>{const m={ArrowLeft:[0,-10],ArrowRight:[0,10],ArrowUp:[-8,0],ArrowDown:[8,0]}[e.key];if(!m)return;e.preventDefault();
    rx=Math.max(-80,Math.min(25,rx+m[0]));ry+=m[1];view()});
  let rw;window.addEventListener('resize',()=>{clearTimeout(rw);rw=setTimeout(()=>{if(host.isConnected)draw(true)},200)});
  if(PD.length){let tm;const form=host.querySelector('.s3form');
    const baca=el=>{const d=PD.find(x=>x.k===el.dataset.k);if(!d)return;
      if(d.t==='n'){let v=Math.round(Number(el.value));if(!Number.isFinite(v)||el.value==='')return;v=Math.max(d.min,Math.min(d.max,v));P[d.k]=v}
      else P[d.k]=el.value};
    const terap=()=>{stop();steps=hitung();draw()};
    form.addEventListener('input',e=>{if(!e.target.dataset.k)return;baca(e.target);clearTimeout(tm);tm=setTimeout(terap,220)});
    form.addEventListener('change',e=>{const el=e.target,d=PD.find(x=>x.k===el.dataset.k);if(d&&d.t==='n'){el.value=P[d.k]}});
    form.querySelector('[data-a=reset]').addEventListener('click',()=>{PD.forEach(d=>{P[d.k]=d.v;const el=form.querySelector(`[data-k="${d.k}"]`);el.value=d.v});terap()});}
  setPlay(false);draw();if(mini)toggle();
};
})();
