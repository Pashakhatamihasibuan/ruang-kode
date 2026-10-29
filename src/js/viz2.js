/* ===================== VISUALISASI v2 =====================
   Dipakai pelajaran jalur (c dan s). Setiap fungsi: VIZ2[nama](host, {lang, lesson}).
   Animasi memakai FLIP (posisi lama -> baru) dan menghormati prefers-reduced-motion. */
const RM=()=>{try{return matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){return false}};
let VUID=0;
function flip(root,render){
  const pos=new Map();
  root.querySelectorAll('[data-key]').forEach(e=>pos.set(e.dataset.key,e.getBoundingClientRect()));
  render();
  if(RM()||!pos.size)return;
  root.querySelectorAll('[data-key]').forEach(e=>{
    const p=pos.get(e.dataset.key),r=e.getBoundingClientRect();
    if(!e.animate)return;
    if(p){const dx=p.left-r.left,dy=p.top-r.top;if(Math.abs(dx)>1||Math.abs(dy)>1)e.animate([{transform:`translate(${dx}px,${dy}px)`},{transform:'none'}],{duration:520,easing:'cubic-bezier(.2,.75,.2,1)'})}
    else e.animate([{opacity:0,transform:'translateY(8px)'},{opacity:1,transform:'none'}],{duration:360,easing:'ease-out'});
  });
}
const fv=v=>v==null?'<i class="nul">NULL</i>':esc(SQLE.fmt(v));
const rupiah=n=>'Rp'+Number(n).toLocaleString('id-ID');
function rtable(cols,rows,o={}){
  const max=o.max||40,shown=rows.slice(0,max);
  return `<div class="rt"><table><thead><tr>${o.lead?`<th class="lead">${o.lead===true?'':esc(o.lead)}</th>`:''}${cols.map((c,i)=>`<th class="${o.colCls?o.colCls(i):''}">${esc(c)}</th>`).join('')}</tr></thead><tbody>${shown.map(r=>`<tr ${r.k!=null?`data-key="${r.k}"`:''} class="${r.cls||''}">${o.lead?`<td class="lead">${r.tag||''}</td>`:''}${r.v.map((x,i)=>`<td class="${r.cc?r.cc(i):''}">${r.raw?x:fv(x)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>${rows.length>max?`<p class="v-more">… dan ${rows.length-max} baris lagi</p>`:''}`;
}
const LBL={java:{t:'Java'},python:{t:'Python'}};

/* ---------- pipeline query: urutan logis eksekusi SELECT ---------- */
const CLAUSES=['FROM','WHERE','GROUP BY','HAVING','SELECT','DISTINCT','ORDER BY','LIMIT'];
function pipeFrames(db,sql){
  let res;
  try{res=SQLE.exec(SQLE.clone(db),sql,{trace:true})}catch(e){return {err:e.message}}
  const last=res[res.length-1],t=last&&last.trace;
  if(!t||!t.from||!t.select)return {err:'Penjelasan langkah tersedia untuk satu query SELECT (tanpa UNION). Jalankan query SELECT lalu coba lagi.'};
  const F=[],fr=t.from,cols=fr.cols,all=fr.rows.map((v,i)=>({k:'f'+i,v}));
  const tb=fr.tables.join(', ');
  F.push({c:'FROM',cols,rows:all,note:t.join
    ?`<b>FROM + ${t.join.comma?'CROSS':t.join.type} JOIN</b> memasangkan baris ${esc(t.join.left.label)} dengan ${esc(t.join.right.label)}. Hasilnya ${fr.rows.length} baris gabungan. Sel <i class="nul">NULL</i> berarti tidak ada pasangan.`
    :`<b>FROM ${esc(tb)}</b> dijalankan paling awal: database mengambil semua ${fr.rows.length} baris dari tabel.`});
  let kept=fr.rows.map((_,i)=>i);
  if(t.where){const K=t.where.keep,n=K.filter(Boolean).length;
    F.push({c:'WHERE',cols,rows:all.map((r,i)=>({...r,cls:K[i]?'keep':'drop'})),note:`<b>WHERE</b> memeriksa kondisi pada setiap baris. ${n} baris lolos (hijau), ${K.length-n} baris dibuang (dicoret).`});
    kept=kept.filter(i=>K[i]);
    F.push({c:'WHERE',cols,rows:kept.map(i=>all[i]),note:`Tersisa ${kept.length} baris. Semua langkah berikutnya hanya melihat baris ini.`});
  }
  const S=t.select;let sk=null;
  if(t.group){const G=t.group.groups;
    const rows=G.flatMap((g,gi)=>g.idx.map((i,j)=>({k:'f'+i,v:fr.rows[i],cls:'g'+(gi%6),tag:j===0?esc(g.label||'(semua)'):''})));
    F.push({c:'GROUP BY',cols,rows,lead:'kelompok',note:`<b>GROUP BY</b> menyusun baris dengan nilai yang sama ke dalam ${G.length} kelompok. Satu kelompok nanti menjadi satu baris hasil.`});
    let gk=G.map((_,i)=>i);
    if(t.having){const K=t.having.keep;
      F.push({c:'HAVING',cols,lead:'kelompok',rows:rows.map(r=>{const gi=G.findIndex(g=>g.idx.includes(+r.k.slice(1)));return {...r,cls:r.cls+' '+(K[gi]?'keep':'drop')}}),
        note:`<b>HAVING</b> menyaring kelompok, bukan baris. ${K.filter(Boolean).length} kelompok lolos. Di sinilah syarat dengan COUNT, SUM, atau AVG ditulis.`});
      gk=gk.filter(i=>K[i]);}
    sk=gk.map(i=>G[i].idx.length?'f'+G[i].idx[0]:'s'+i);
  }else sk=kept.map(i=>'f'+i);
  if(sk.length!==S.rows.length)sk=S.rows.map((_,i)=>'s'+i);
  F.push({c:'SELECT',cols:S.cols,rows:S.rows.map((v,i)=>({k:sk[i],v})),note:t.group
    ?`<b>SELECT</b> menghitung kolom untuk setiap kelompok, misalnya COUNT atau SUM. Alias dengan AS baru lahir di sini.`
    :`<b>SELECT</b> memilih dan menghitung kolom yang diminta: ${S.cols.map(esc).join(', ')}.`});
  let idx=S.rows.map((_,i)=>i);
  if(t.distinct){const K=t.distinct.keep;
    F.push({c:'DISTINCT',cols:S.cols,rows:idx.map(i=>({k:sk[i],v:S.rows[i],cls:K[i]?'keep':'drop'})),note:`<b>DISTINCT</b> membuang baris kembar. ${K.filter(x=>!x).length} baris duplikat dicoret.`});
    idx=idx.filter(i=>K[i]);}
  if(t.order){idx=t.order.idx;
    F.push({c:'ORDER BY',cols:S.cols,rows:idx.map(i=>({k:sk[i],v:S.rows[i]})),note:`<b>ORDER BY</b> mengurutkan hasil. Karena dijalankan setelah SELECT, ORDER BY boleh memakai alias kolom.`});}
  if(t.limit){const L=t.limit;
    F.push({c:'LIMIT',cols:S.cols,rows:idx.map((i,j)=>({k:sk[i],v:S.rows[i],cls:j>=L.offset&&j<L.offset+L.n?'keep':'drop'})),note:`<b>LIMIT${L.offset?' / OFFSET':''}</b> mengambil ${L.n} baris${L.offset?` setelah melewati ${L.offset} baris`:' teratas'} dari ${L.from} baris.`});
    idx=idx.slice(L.offset,L.offset+L.n);
    F.push({c:'LIMIT',cols:S.cols,rows:idx.map(i=>({k:sk[i],v:S.rows[i]})),note:`Hasil akhir: ${idx.length} baris.`});}
  else F[F.length-1].note+=` Hasil akhir: ${idx.length} baris.`;
  return {F};
}
function sqlPipeline(host,db,sql){
  const p=pipeFrames(db,sql);
  if(p.err){host.innerHTML=`<p class="v-err">${esc(p.err)}</p>`;return}
  const order=CLAUSES.filter(c=>p.F.some(f=>f.c===c));
  player(host,p.F,(st,f)=>flip(st,()=>{const ci=order.indexOf(f.c);
    st.innerHTML=`<div class="v-pipe" aria-label="Urutan eksekusi">${order.map((c,i)=>`<span class="${i===ci?'cur':i<ci?'done':''}">${c}</span>`).join('<i aria-hidden="true">›</i>')}</div>${rtable(f.cols,f.rows,{lead:f.lead})}`}),{speed:1700});
}

/* ---------- JOIN ---------- */
function venn(type,ln,rn){
  const id='vc'+(++VUID),L=type==='LEFT'||type==='FULL',R=type==='RIGHT'||type==='FULL';
  return `<svg class="venn" viewBox="0 0 160 84" role="img" aria-label="Diagram ${type} JOIN"><defs><clipPath id="${id}"><circle cx="62" cy="42" r="30"/></clipPath></defs>
   <circle cx="62" cy="42" r="30" class="${L?'on':''}"/><circle cx="98" cy="42" r="30" class="${R?'on':''}"/>
   <circle cx="98" cy="42" r="30" clip-path="url(#${id})" class="on"/>
   <circle cx="62" cy="42" r="30" class="ln"/><circle cx="98" cy="42" r="30" class="ln"/>
   <text x="20" y="80">${ln}</text><text x="140" y="80" text-anchor="end">${rn}</text></svg>`;
}
function joinViz(host,mode){
  const self=mode==='SELF';
  const C=self?{L:'karyawan',la:'k',R:'karyawan',ra:'a',on:'k.atasan_id = a.id',lc:[0,1,3],rc:[0,1],sel:'k.nama AS karyawan, a.nama AS atasan',ln:'k (karyawan)',rn:'a (atasan)',res:['karyawan','atasan'],li:1,ri:1}
               :{L:'pelanggan',la:'p',R:'pesanan',ra:'s',on:'s.pelanggan_id = p.id',lc:[0,1],rc:[0,1],sel:'p.nama, s.id AS pesanan',ln:'pelanggan',rn:'pesanan',res:['nama','pesanan'],li:1,ri:0};
  const types=self?['INNER','LEFT']:['INNER','LEFT','RIGHT','FULL'];
  let type=mode==='LEFT'?'LEFT':'INNER';
  const db=SQLE.create(SEED.toko);
  host.innerHTML=`<div class="v-jhead"><div class="seg" role="group" aria-label="Jenis JOIN">${types.map(t=>`<button data-t="${t}" aria-pressed="${t===type}">${t}</button>`).join('')}</div><div class="v-jven"></div></div><pre class="code v-q"></pre><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function build(){
    host.querySelectorAll('[data-t]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.t===type));
    $('.v-jven',host).innerHTML=venn(type,C.ln,C.rn);
    const q=`SELECT ${C.sel}\nFROM ${C.L} ${C.la}\n${type} JOIN ${C.R} ${C.ra} ON ${C.on};`;
    $('.v-q',host).innerHTML=hl(q,'sql');
    const r=SQLE.exec(db,q,{trace:true})[0],j=r.trace.join,pairs=j.pairs;
    const frames=[{li:-1,upto:0,note:`Kiri: tabel <b>${esc(C.ln)}</b>. Kanan: <b>${esc(C.rn)}</b>. JOIN akan mencocokkan setiap baris kiri dengan baris kanan yang memenuhi <code>${esc(C.on)}</code>.`}];
    let n=0;
    j.left.rows.forEach((_,i)=>{const mine=pairs.map((p,k)=>[p,k]).filter(([p])=>p[0]===i);if(!mine.length)return;n+=mine.length;
      const miss=mine[0][0][1]==null;
      frames.push({li:i,ri:mine.map(([p])=>p[1]).filter(x=>x!=null),upto:n,note:miss
        ?`<b>${esc(j.left.rows[i][C.li])}</b> tidak punya pasangan. ${type==='LEFT'||type==='FULL'?`Karena ${type} JOIN, baris ini tetap masuk dengan kolom kanan berisi NULL.`:''}`
        :`<b>${esc(j.left.rows[i][C.li])}</b> cocok dengan ${mine.length} baris kanan, jadi menghasilkan ${mine.length} baris.`})});
    const skipped=j.left.rows.map((_,i)=>i).filter(i=>!pairs.some(p=>p[0]===i));
    if(skipped.length&&type!=='LEFT'&&type!=='FULL')frames.push({li:-1,miss:skipped,upto:n,note:`${skipped.map(i=>esc(j.left.rows[i][C.li])).join(', ')} tidak punya pasangan, jadi <b>dibuang</b> oleh ${type} JOIN.`});
    const ro=pairs.map((p,k)=>[p,k]).filter(([p])=>p[0]==null);
    if(ro.length){n+=ro.length;frames.push({li:-1,ri:ro.map(([p])=>p[1]),upto:n,note:`Baris kanan tanpa pasangan ikut masuk karena ${type} JOIN; kolom kiri berisi NULL.`})}
    frames[frames.length-1].note+=` Total ${r.rows.length} baris.`;
    const draw=(st,f)=>{
      const lrow=(v,i)=>`<li data-i="${i}" class="${f.li===i?'cur':''} ${f.miss&&f.miss.includes(i)?'miss':''} ${pairs.slice(0,f.upto).some(p=>p[0]===i)?'used':''}">${C.lc.map(c=>`<span>${fv(v[c])}</span>`).join('')}</li>`;
      const rrow=(v,i)=>`<li data-i="${i}" class="${f.ri&&f.ri.includes(i)?'cur':''} ${pairs.slice(0,f.upto).some(p=>p[1]===i)?'used':''}">${C.rc.map(c=>`<span>${fv(v[c])}</span>`).join('')}</li>`;
      st.innerHTML=`<div class="v-jn"><div><div class="v-cap">${esc(C.ln)} <small>${C.lc.map(c=>j.left.cols[c]).join(' · ')}</small></div><ol class="v-jl">${j.left.rows.map(lrow).join('')}</ol></div><svg class="v-jsvg" aria-hidden="true"></svg>
        <div><div class="v-cap">${esc(C.rn)} <small>${C.rc.map(c=>j.right.cols[c]).join(' · ')}</small></div><ol class="v-jl r">${j.right.rows.map(rrow).join('')}</ol></div></div>
        <div class="v-cap">Hasil (${f.upto} baris)</div>${rtable(C.res,r.rows.slice(0,f.upto).map((v,i)=>({k:'r'+i,v,cls:i>=f.upto-(f.ri?f.ri.length:0)-(f.li>=0?0:0)?'':''})),{max:30})}`;
      requestAnimationFrame(()=>lines(st,f));
    };
    function lines(st,f){
      const box=$('.v-jn',st);if(!box)return;const svg=$('.v-jsvg',st),B=box.getBoundingClientRect(),S=svg.getBoundingClientRect();
      const L=[...st.querySelectorAll('.v-jl:not(.r) li')],Rr=[...st.querySelectorAll('.v-jl.r li')];
      let h='';
      pairs.slice(0,f.upto).forEach(([a,b],k)=>{if(a==null||b==null)return;const A=L[a].getBoundingClientRect(),Z=Rr[b].getBoundingClientRect();
        const y1=A.top+A.height/2-S.top,y2=Z.top+Z.height/2-S.top,w=S.width;const cur=f.li===a;
        h+=`<path d="M0 ${y1} C ${w*.5} ${y1}, ${w*.5} ${y2}, ${w} ${y2}" class="${cur?'cur':''}" pathLength="1"/>`});
      svg.setAttribute('viewBox',`0 0 ${S.width} ${S.height}`);svg.innerHTML=h;
    }
    if(!P)P=player(pl,frames,draw,{speed:1300});else P.set(frames);
    P._d=draw;
  }
  host.addEventListener('click',e=>{const b=e.target.closest('[data-t]');if(!b)return;type=b.dataset.t;P=null;pl.innerHTML='';build()});
  build();
}

/* ---------- diagram ER Toko Nusantara ---------- */
function erViz(host){
  const db=SQLE.create(SEED.toko),sc=SQLE.schema(db);const T=Object.fromEntries(sc.map(t=>[t.name,t]));
  const POS={pelanggan:[10,16],pesanan:[262,16],detail_pesanan:[514,16],produk:[514,196],karyawan:[10,196],rekening:[262,216]};
  const W=196,RH=19,HH=28;
  const rowY=(t,c)=>POS[t][1]+HH+RH*T[t].cols.findIndex(x=>x.name===c)+RH/2;
  const REL=[
    {id:'r1',a:'pelanggan',b:'pesanan',d:`M ${10+W} ${rowY('pelanggan','id')} C 240 ${rowY('pelanggan','id')}, 236 ${rowY('pesanan','pelanggan_id')}, 262 ${rowY('pesanan','pelanggan_id')}`,
      note:'<b>pelanggan 1 — N pesanan.</b> Satu pelanggan bisa punya banyak pesanan. Kolom <code>pesanan.pelanggan_id</code> adalah foreign key yang menunjuk <code>pelanggan.id</code>.'},
    {id:'r2',a:'pesanan',b:'detail_pesanan',d:`M ${262+W} ${rowY('pesanan','id')} C 490 ${rowY('pesanan','id')}, 488 ${rowY('detail_pesanan','pesanan_id')}, 514 ${rowY('detail_pesanan','pesanan_id')}`,
      note:'<b>pesanan 1 — N detail_pesanan.</b> Satu pesanan berisi beberapa baris barang.'},
    {id:'r3',a:'produk',b:'detail_pesanan',d:`M 514 ${rowY('detail_pesanan','produk_id')} L 496 ${rowY('detail_pesanan','produk_id')} L 496 ${rowY('produk','id')} L 514 ${rowY('produk','id')}`,
      note:'<b>produk 1 — N detail_pesanan.</b> Tabel detail_pesanan adalah <i>tabel penghubung</i>: ia memecah hubungan banyak-ke-banyak antara pesanan dan produk. Primary key-nya gabungan (pesanan_id, produk_id).'},
    {id:'r4',a:'karyawan',b:'karyawan',d:`M ${10+W} ${rowY('karyawan','atasan_id')} C 236 ${rowY('karyawan','atasan_id')}, 236 ${rowY('karyawan','id')}, ${10+W} ${rowY('karyawan','id')}`,
      note:'<b>karyawan → karyawan.</b> Relasi ke diri sendiri: <code>atasan_id</code> menunjuk karyawan lain. Inilah bahan SELF JOIN dan CTE rekursif.'}];
  const frames=[{note:'Diagram ER (Entity Relationship) Toko Nusantara. Setiap kotak adalah tabel; 🔑 primary key, 🔗 foreign key. Tekan Berikutnya untuk menelusuri relasinya.'},...REL.map(r=>({r:r.id,note:r.note})),
    {r:'x',note:'<b>rekening</b> berdiri sendiri, tanpa relasi. Tabel ini dipakai untuk latihan transaksi.'}];
  player(host,frames,(st,f)=>{
    const act=REL.find(r=>r.id===f.r),on=t=>f.r==='x'?t==='rekening':act?(act.a===t||act.b===t):true;
    st.innerHTML=`<div class="v-er"><svg viewBox="0 0 720 340" role="img" aria-label="Diagram ER">
     ${REL.map(r=>`<path d="${r.d}" class="rel ${f.r===r.id?'cur':''} ${f.r&&f.r!==r.id?'dim':''}"/>`).join('')}
     ${Object.entries(POS).map(([t,[x,y]])=>{const tb=T[t],h=HH+RH*tb.cols.length;return `<g class="ent ${on(t)?'':'dim'} ${act&&on(t)||f.r==='x'&&on(t)?'cur':''}">
       <rect x="${x}" y="${y}" width="${W}" height="${h}" rx="9"/><text x="${x+12}" y="${y+19}" class="tn">${t}</text><line x1="${x}" x2="${x+W}" y1="${y+HH}" y2="${y+HH}"/>
       ${tb.cols.map((c,i)=>`<text x="${x+12}" y="${y+HH+RH*i+14}" class="cn">${c.pk?'🔑 ':c.fk?'🔗 ':''}${c.name}</text><text x="${x+W-10}" y="${y+HH+RH*i+14}" class="ct" text-anchor="end">${(c.type||'').toLowerCase()}</text>`).join('')}</g>`}).join('')}
    </svg></div>`;
  },{speed:2200});
}

/* ---------- index: SCAN lawan pencarian biner ---------- */
function indexViz(host){
  const N=32,vals=[];let s=7;for(let i=0;i<N;i++){s=(s*37+11)%97;vals.push(1000+s*500+i)}
  const sorted=[...vals].sort((a,b)=>a-b);
  host.innerHTML=`<div class="row"><label>Cari harga = <select class="inp v-tg">${[sorted[3],sorted[17],sorted[29],vals[30]].map((v,i)=>`<option value="${v}" ${i===2?'selected':''}>${v}</option>`).join('')}</select></label></div><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function build(){
    const tg=+$('.v-tg',host).value;const sc=vals.indexOf(tg);
    const bs=[];let lo=0,hi=N-1;while(lo<=hi){const m=(lo+hi)>>1;bs.push({lo,hi,m});if(sorted[m]===tg)break;if(sorted[m]<tg)lo=m+1;else hi=m-1}
    const steps=Math.max(sc+1,bs.length),fr=[];
    for(let k=0;k<steps;k++){const b=bs[Math.min(k,bs.length-1)];fr.push({k,s:Math.min(k,sc),b,sd:k>=sc,bd:k>=bs.length-1,
      note:k>=sc&&k>=bs.length-1?`Selesai. Tanpa index: <b>${sc+1}</b> baris dibaca. Dengan index: hanya <b>${bs.length}</b> langkah. Pada sejuta baris, bedanya sekitar 1.000.000 lawan 20.`
        :`Langkah ${k+1}. SCAN membaca baris satu per satu. Index yang terurut memotong wilayah pencarian jadi setengah setiap langkah.`})}
    const draw=(st,f)=>{st.innerHTML=`<div class="v-ix"><div class="v-cap">Tanpa index: <b>SCAN</b> tabel <span class="v-ct">${Math.min(f.k,f.s)+1} dibaca</span></div>
      ${cellsHTML(vals,i=>i===f.s?(f.sd?'found':'hl'):i<f.s?'seen':'',false)}
      <div class="v-cap">Dengan index: <b>SEARCH</b> lewat B-tree (urut) <span class="v-ct">${Math.min(f.k,bs.length-1)+1} langkah</span></div>
      ${cellsHTML(sorted,i=>i===f.b.m?(f.bd?'found':'hl'):(i<f.b.lo||i>f.b.hi)?'dim':'',false)}</div>`};
    if(!P)P=player(pl,fr,draw,{speed:700});else P.set(fr);
  }
  $('.v-tg',host).onchange=build;build();
}

/* ---------- transaksi ---------- */
function txnViz(host){
  let mode='ok';
  host.innerHTML=`<div class="seg" role="group" aria-label="Skenario"><button data-m="ok" aria-pressed="true">Transfer berhasil</button><button data-m="fail" aria-pressed="false">Gagal di tengah</button></div><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  const F={ok:[
    {sql:'',a:500000,b:300000,st:'',note:'Andi akan mentransfer Rp200.000 ke Budi. Total uang di sistem: Rp800.000.'},
    {sql:'BEGIN;',a:500000,b:300000,st:'tx',snap:1,note:'<b>BEGIN</b> membuka transaksi. Database mencatat keadaan awal agar bisa kembali kapan saja.'},
    {sql:"UPDATE rekening SET saldo = saldo - 200000 WHERE pemilik = 'Andi';",a:300000,b:300000,st:'tx',snap:1,pa:1,note:'Saldo Andi berkurang, tapi perubahan ini <b>belum permanen</b>. Total sementara hanya Rp600.000.'},
    {sql:"UPDATE rekening SET saldo = saldo + 200000 WHERE pemilik = 'Budi';",a:300000,b:500000,st:'tx',snap:1,pa:1,pb:1,note:'Saldo Budi bertambah. Total kembali Rp800.000.'},
    {sql:'COMMIT;',a:300000,b:500000,st:'done',note:'<b>COMMIT</b>: kedua perubahan disimpan permanen bersamaan. Inilah <i>atomicity</i>: semua atau tidak sama sekali.'}],
   fail:[
    {sql:'',a:500000,b:300000,st:'',note:'Skenario yang sama, tapi server mati sebelum perintah kedua.'},
    {sql:'BEGIN;',a:500000,b:300000,st:'tx',snap:1,note:'<b>BEGIN</b> membuka transaksi dan menyimpan titik kembali.'},
    {sql:"UPDATE rekening SET saldo = saldo - 200000 WHERE pemilik = 'Andi';",a:300000,b:300000,st:'tx',snap:1,pa:1,note:'Saldo Andi sudah berkurang (belum permanen).'},
    {sql:'-- server mati / error!',a:300000,b:300000,st:'err',snap:1,pa:1,note:'Terjadi kegagalan. Tanpa transaksi, Rp200.000 milik Andi akan <b>hilang</b> dari sistem.'},
    {sql:'ROLLBACK;',a:500000,b:300000,st:'rb',note:'<b>ROLLBACK</b> (otomatis saat gagal) mengembalikan semua ke titik BEGIN. Uang Andi utuh, total tetap Rp800.000.'}]};
  const draw=(st,f)=>{st.innerHTML=`<pre class="code v-q">${f.sql?hl(f.sql,'sql'):'<span class="c">-- belum ada perintah</span>'}</pre>
    <div class="v-acc"><div class="v-acct ${f.pa?'pend':''} ${f.st==='done'?'ok':''}"><span>Andi</span><b>${rupiah(f.a)}</b>${f.pa?'<small>belum permanen</small>':''}</div>
    <div class="v-acct ${f.pb?'pend':''} ${f.st==='done'?'ok':''}"><span>Budi</span><b>${rupiah(f.b)}</b>${f.pb?'<small>belum permanen</small>':''}</div>
    <div class="v-acct tot ${f.a+f.b!==800000?'bad':''}"><span>Total</span><b>${rupiah(f.a+f.b)}</b></div></div>
    <div class="v-txs ${f.st}">${f.st==='tx'?'Transaksi berjalan · titik kembali tersimpan':f.st==='err'?'Gagal! Transaksi belum selesai':f.st==='rb'?'Dibatalkan: kembali ke keadaan awal':f.st==='done'?'Tersimpan permanen':'Tidak ada transaksi'}</div>`};
  function build(){host.querySelectorAll('[data-m]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.m===mode));if(!P)P=player(pl,F[mode],draw,{speed:1700});else P.set(F[mode])}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-m]');if(b){mode=b.dataset.m;build()}});build();
}

/* ---------- tingkat isolasi ---------- */
function isolationViz(host){
  const LV=['READ UNCOMMITTED','READ COMMITTED','REPEATABLE READ','SERIALIZABLE'];let lv=1;
  host.innerHTML=`<div class="seg v-wrap" role="group" aria-label="Tingkat isolasi">${LV.map((l,i)=>`<button data-l="${i}" aria-pressed="${i===lv}">${l}</button>`).join('')}</div><div class="pl"></div><div class="v-iso-t"></div>`;
  const pl=$('.pl',host);let P;
  const steps=l=>[
    {s:'A',sql:'BEGIN;\nUPDATE rekening SET saldo = 0 WHERE id = 1;',note:'Sesi A mengubah saldo Andi menjadi 0, tapi <b>belum COMMIT</b>.'},
    {s:'B',sql:'SELECT saldo FROM rekening WHERE id = 1;',r:l===0?'0':'500000',bad:l===0&&'Dirty read',note:l===0?'Sesi B membaca data yang belum di-commit. Kalau A membatalkan, B memakai angka palsu.':'Sesi B tetap melihat 500000, karena perubahan A belum di-commit.'},
    {s:'A',sql:'COMMIT;',note:'Sesi A menyimpan perubahannya.'},
    {s:'B',sql:'SELECT saldo FROM rekening WHERE id = 1;',r:l<=1?'0':'500000',bad:l<=1&&'Non-repeatable read',note:l<=1?'Query yang sama di transaksi B memberi angka berbeda.':'B tetap melihat snapshot awal transaksinya: hasil konsisten.'},
    {s:'A',sql:"INSERT INTO rekening VALUES (3, 'Citra', 100000);\nCOMMIT;",note:'Sesi A menambah rekening baru.'},
    {s:'B',sql:'SELECT COUNT(*) FROM rekening;',r:l<=2?'3':'2',bad:l<=2&&'Phantom read',note:l<=2?'Muncul baris "hantu" yang tadinya tidak ada. (PostgreSQL sudah mencegah ini di REPEATABLE READ, standar SQL belum.)':'SERIALIZABLE: B seolah berjalan sendirian, tidak melihat baris baru.'}];
  const draw=(st,f,i)=>{const S=steps(lv).slice(0,i+1);
    st.innerHTML=`<div class="v-iso"><div class="v-cap">Sesi A</div><div class="v-cap">Sesi B</div>${S.map((x,k)=>`<div class="v-ist ${x.s==='A'?'a':'b'} ${k===i?'cur':''}" data-key="s${k}"><pre class="code">${hl(x.sql,'sql')}</pre>${x.r!=null?`<div class="v-res ${x.bad?'bad':'ok'}">→ ${x.r}${x.bad?` <b>${x.bad}</b>`:''}</div>`:''}</div>`).join('')}</div>`};
  function table(){$('.v-iso-t',host).innerHTML=`<div class="tbl"><table class="cmp"><thead><tr><th>Tingkat</th><th>Dirty read</th><th>Non-repeatable</th><th>Phantom</th></tr></thead><tbody>${LV.map((l,i)=>`<tr class="${i===lv?'cur':''}"><td>${l}</td>${[0,1,2].map(k=>`<td>${i>k?'<span class="ok">dicegah</span>':'<span class="bad">mungkin</span>'}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`}
  function build(){host.querySelectorAll('[data-l]').forEach(b=>b.setAttribute('aria-pressed',+b.dataset.l===lv));const fr=steps(lv).map(x=>({note:x.note}));
    if(!P)P=player(pl,fr,draw,{speed:1800});else P.set(fr);table()}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-l]');if(b){lv=+b.dataset.l;build()}});build();
}

/* ---------- SQL injection ---------- */
function injectionViz(host){
  const db=SQLE.create("CREATE TABLE akun (id INTEGER PRIMARY KEY, username TEXT, password TEXT); INSERT INTO akun VALUES (1,'andi','rahasia1'),(2,'budi','kopi123'),(3,'admin','Adm!n2024');");
  const PRE=[['Login normal','andi','rahasia1'],['Password salah','andi','tebak'],["admin' --","admin' --",'apa saja'],["' OR '1'='1","x","' OR '1'='1"]];
  host.innerHTML=`<div class="chips">${PRE.map((p,i)=>`<button class="chip" data-p="${i}">${esc(p[0])}</button>`).join('')}</div>
   <div class="v-inj-f"><label>Username<input class="inp" id="ij-u" autocomplete="off" spellcheck="false"></label><label>Password<input class="inp" id="ij-p" autocomplete="off" spellcheck="false"></label></div>
   <div class="v-inj"><div><div class="v-cap bad">Tidak aman: string dirangkai</div><pre class="code v-q" id="ij-q1"></pre><div class="v-res" id="ij-r1"></div></div>
   <div><div class="v-cap ok">Aman: parameter (prepared statement)</div><pre class="code v-q" id="ij-q2"></pre><div class="v-res" id="ij-r2"></div></div></div>`;
  const U=$('#ij-u',host),Pw=$('#ij-p',host);
  const run=q=>{try{const r=SQLE.exec(db,q);const x=r[r.length-1];return x.rows.length?{ok:true,t:`Login berhasil sebagai <b>${esc(x.rows[0][1])}</b>${x.rows.length>1?` (query mengembalikan ${x.rows.length} akun!)`:''}`}:{ok:false,t:'Login ditolak: username atau password salah.'}}catch(e){return {ok:false,t:'Error: '+esc(e.message)}}};
  function upd(){const u=U.value,p=Pw.value;
    const q1=`SELECT id, username FROM akun WHERE username = '${u}' AND password = '${p}';`;
    $('#ij-q1',host).innerHTML=hl(q1,'sql');
    const q2=`SELECT id, username FROM akun WHERE username = ? AND password = ?;\n-- nilai terikat: [${JSON.stringify(u)}, ${JSON.stringify(p)}]`;
    $('#ij-q2',host).innerHTML=hl(q2,'sql');
    const r1=run(q1),r2=run(`SELECT id, username FROM akun WHERE username = '${u.replace(/'/g,"''")}' AND password = '${p.replace(/'/g,"''")}';`);
    const atk=/['-]/.test(u+p);
    $('#ij-r1',host).className='v-res '+(r1.ok&&atk?'bad':r1.ok?'ok':'');$('#ij-r1',host).innerHTML=r1.t+(r1.ok&&atk?' ⚠️ Penyerang masuk tanpa password yang benar.':'');
    $('#ij-r2',host).className='v-res '+(r2.ok?'ok':'');$('#ij-r2',host).innerHTML=r2.t+(atk&&!r2.ok?' Input dianggap teks biasa, bukan bagian dari perintah SQL.':'');}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-p]');if(!b)return;const p=PRE[+b.dataset.p];U.value=p[1];Pw.value=p[2];upd()});
  U.oninput=Pw.oninput=upd;U.value=PRE[2][1];Pw.value=PRE[2][2];upd();
}

/* ---------- CTE rekursif: bagan organisasi ---------- */
function recursiveViz(host){
  const db=SQLE.create(SEED.toko);
  const q=`WITH RECURSIVE bawahan AS (\n  SELECT id, nama, jabatan, atasan_id, 1 AS level\n  FROM karyawan WHERE atasan_id IS NULL\n  UNION ALL\n  SELECT k.id, k.nama, k.jabatan, k.atasan_id, b.level + 1\n  FROM karyawan k JOIN bawahan b ON k.atasan_id = b.id\n)\nSELECT * FROM bawahan;`;
  const rows=SQLE.exec(db,q)[0].rows;const maxL=Math.max(...rows.map(r=>r[4]));
  const fr=[{L:0,note:'CTE rekursif punya dua bagian: <b>anchor</b> (titik awal) dan <b>bagian rekursif</b> yang memanggil CTE itu sendiri.'}];
  for(let L=1;L<=maxL;L++)fr.push({L,note:L===1?'<b>Anchor</b>: karyawan tanpa atasan (atasan_id IS NULL) menjadi baris pertama, level 1.':`<b>Iterasi ${L-1}</b>: JOIN karyawan dengan baris level ${L-1} yang baru ditemukan. Hasilnya ${rows.filter(r=>r[4]===L).length} baris level ${L}.`});
  fr.push({L:maxL+1,note:`<b>Iterasi ${maxL}</b>: tidak ada lagi karyawan yang atasannya di level ${maxL}. Hasil kosong, rekursi <b>berhenti</b>. Total ${rows.length} baris.`});
  host.innerHTML=`<pre class="code v-q">${hl(q,'sql')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-org">${Array.from({length:maxL},(_,i)=>i+1).map(L=>`<div class="v-lv ${L<=f.L?'':'off'}"><span class="v-lvn">level ${L}</span>${rows.filter(r=>r[4]===L&&L<=f.L).map(r=>`<div class="v-pn ${r[4]===f.L?'new':''}" data-key="k${r[0]}"><b>${esc(r[1])}</b><small>${esc(r[2])}</small></div>`).join('')}</div>`).join('')}</div>`}),{speed:1800});
}

/* ---------- window function ---------- */
function windowViz(host){
  const FN={'ROW_NUMBER()':'ROW_NUMBER()','RANK()':'RANK()','SUM(gaji)':'SUM(gaji)'};let fn='RANK()';
  const db=SQLE.create(SEED.toko);
  host.innerHTML=`<div class="seg" role="group" aria-label="Fungsi window">${Object.keys(FN).map(k=>`<button data-f="${k}" aria-pressed="${k===fn}">${k}</button>`).join('')}</div><pre class="code v-q"></pre><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function build(){
    host.querySelectorAll('[data-f]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.f===fn));
    const q=`SELECT nama, divisi, gaji,\n  ${FN[fn]} OVER (PARTITION BY divisi ORDER BY gaji DESC) AS hasil\nFROM karyawan\nORDER BY divisi, gaji DESC;`;
    $('.v-q',host).innerHTML=hl(q,'sql');
    const rows=SQLE.exec(db,q)[0].rows,divs=[...new Set(rows.map(r=>r[1]))];
    const fr=[{n:-1,note:'<b>PARTITION BY divisi</b> membagi baris per divisi (warna). <b>ORDER BY gaji DESC</b> mengurutkan di dalam setiap partisi. Berbeda dengan GROUP BY, semua baris tetap ada.'}];
    rows.forEach((r,i)=>{const first=i===0||rows[i-1][1]!==r[1];
      fr.push({n:i,note:fn==='ROW_NUMBER()'?`${esc(r[0])}: nomor urut ${r[3]} di divisi ${esc(r[1])}.${first?' Partisi baru, hitungan mulai dari 1.':''}`
        :fn==='RANK()'?`${esc(r[0])}: peringkat ${r[3]}.${!first&&rows[i-1][2]===r[2]?' Gajinya sama dengan baris sebelumnya, jadi peringkatnya sama, dan peringkat berikutnya akan melompat.':first?' Partisi baru, peringkat mulai dari 1.':''}`
        :`${esc(r[0])}: total berjalan ${rupiah(r[3])} (jumlah gaji dari baris pertama partisi sampai baris ini).`})});
    const draw=(st,f)=>{st.innerHTML=rtable(['nama','divisi','gaji','hasil'],rows.map((r,i)=>({v:[esc(r[0]),esc(r[1]),rupiah(r[2]),i<=f.n?`<b>${fn==='SUM(gaji)'?rupiah(r[3]):r[3]}</b>`:'<span class="v-wait">?</span>'],raw:true,cls:'g'+divs.indexOf(r[1])+(i===f.n?' cur':'')+(i>0&&rows[i-1][1]!==r[1]?' brk':'')})))};
    if(!P)P=player(pl,fr,draw,{speed:1100});else P.set(fr);
  }
  host.addEventListener('click',e=>{const b=e.target.closest('[data-f]');if(b){fn=b.dataset.f;build()}});build();
}

/* ---------- anatomi tabel ---------- */
function sqlTableViz(host){
  const db=SQLE.create(SEED.toko),r=SQLE.exec(db,'SELECT * FROM pelanggan;')[0];
  const fr=[{s:'t',note:'Ini <b>tabel</b> <code>pelanggan</code>: kumpulan data sejenis dengan struktur yang sama.'},
    {s:'c',note:'Satu <b>kolom</b> (field) menyimpan satu jenis atribut, misalnya <code>nama</code>. Semua nilai di kolom bertipe sama.'},
    {s:'r',note:'Satu <b>baris</b> (record) adalah satu pelanggan lengkap: Citra dari Surabaya.'},
    {s:'x',note:'Satu <b>sel</b> adalah pertemuan baris dan kolom: kota milik Citra.'},
    {s:'pk',note:'Kolom <code>id</code> adalah <b>primary key</b>: unik dan tidak boleh kosong, jadi setiap baris bisa ditunjuk dengan pasti.'},
    {s:'n',note:'<b>NULL</b> berarti nilainya tidak diketahui atau kosong, bukan teks "NULL" dan bukan angka 0. Kota Gita belum diisi.'}];
  player(host,fr,(st,f)=>{st.innerHTML=`<div class="v-anat s-${f.s}">${rtable(r.cols,r.rows.map((v,i)=>({v,cls:(i===2?'r3':'')+(i===6?' r7':''),cc:c=>(c===1?'cn':'')+(c===0?' pk':'')+(c===2&&i===2?' cx':'')+(c===2&&i===6?' cnul':'')})),{colCls:c=>(c===1?'cn':'')+(c===0?' pk':'')})}</div>`},{speed:1800});
}

/* ---------- SQL lawan NoSQL ---------- */
function sqlNoSqlViz(host){
  const fr=[{s:0,note:'Kiri: data relasional, pelanggan disimpan sekali dan pesanan menunjuknya lewat id. Kanan: basis data dokumen (NoSQL) menyalin data pelanggan ke setiap pesanan agar sekali baca langsung lengkap.'},
    {s:1,note:'Andi pindah ke Bogor. Di SQL cukup <b>1 sel</b> yang diubah. Di dokumen, <b>3 salinan</b> harus diubah; kalau satu terlewat, data jadi tidak konsisten.'},
    {s:2,note:'Sebaliknya, membaca satu pesanan lengkap di dokumen tidak butuh JOIN. NoSQL unggul untuk data yang bentuknya berubah-ubah dan skala besar; SQL unggul untuk konsistensi dan query yang fleksibel.'}];
  player(host,fr,(st,f)=>{const k=f.s>=1?'Bogor':'Jakarta',H=f.s===1?'hl':'';
    st.innerHTML=`<div class="v-2col"><div><div class="v-cap">SQL: tabel terpisah</div>${rtable(['id','nama','kota'],[{v:[1,'Andi',`<span class="${H}">${k}</span>`],raw:true},{v:[2,'Budi','Bandung']}].map(x=>x.raw?x:{v:x.v}),{})}
      ${rtable(['id','pelanggan_id','tanggal'],[[101,1,'2024-10-01'],[103,1,'2024-10-07'],[108,1,'2024-11-05']].map(v=>({v})))}</div>
     <div><div class="v-cap">NoSQL: dokumen</div>${[101,103,108].map((id,i)=>`<pre class="code v-doc ${f.s===2&&i===0?'cur':''}">{ <span class="t">"_id"</span>: ${id},
  <span class="t">"pelanggan"</span>: { <span class="t">"nama"</span>: <span class="s">"Andi"</span>, <span class="t">"kota"</span>: <span class="s ${H}">"${k}"</span> },
  <span class="t">"items"</span>: [ … ] }</pre>`).join('')}</div></div>`},{speed:2600});
}

/* ---------- Java/Python: konversi tipe ---------- */
function castingViz(host,{lang}){
  const J=lang!=='python';
  const box=(v,t,cls='')=>`<div class="v-val ${cls}"><b>${esc(v)}</b><span>${esc(t)}</span></div>`;
  const bits=(n,w)=>{const s=(BigInt.asUintN(64,BigInt(n))).toString(2).padStart(64,'0');return s.slice(64-w)};
  const fr=J?[
    {h:`<div class="v-ladder">${['byte 8','short 16','int 32','long 64','float 32','double 64'].map((x,i)=>`<span class="${i===2||i===5?'on':''}">${x.split(' ')[0]}<small>${x.split(' ')[1]} bit</small></span>`).join('<i>→</i>')}</div><div class="v-cv">${box('7','int')}<span class="v-fn">otomatis</span>${box('7.0','double','ok')}</div>`,note:'<b>Widening</b>: dari tipe kecil ke tipe besar (ke kanan) aman dan otomatis. <code>double rata = jumlah;</code>'},
    {h:`<div class="v-cv">${box('9.99','double')}<span class="v-fn">(int)</span>${box('9','int','warn')}</div><p class="v-sub">Bagian <s>.99</s> dibuang, bukan dibulatkan.</p>`,note:'<b>Narrowing</b> butuh cast eksplisit <code>(int)</code>. Java memaksamu menulisnya sebagai tanda kamu sadar ada data yang hilang.'},
    {h:`<div class="v-cv">${box('3.000.000.000','long')}<span class="v-fn">(int)</span>${box('-1.294.967.296','int','bad')}</div><div class="v-bits"><div><small>long (64 bit)</small><code><span class="cut">${bits(3000000000,64).slice(0,32)}</span>${bits(3000000000,64).slice(32)}</code></div><div><small>int (32 bit)</small><code><span class="sign">1</span>${bits(3000000000,32).slice(1)}</code></div></div>`,note:'<b>Overflow</b>: 32 bit atas dipotong. Bit paling kiri yang tersisa bernilai 1, dan pada int itu tanda <b>negatif</b>. Hasilnya angka yang sama sekali berbeda.'},
    {h:`<div class="v-cv">${box("'A'",'char')}<span class="v-fn">int kode = huruf</span>${box('65','int','ok')}</div>`,note:'char sebenarnya angka: kode Unicode huruf A adalah 65.'},
    {h:`<div class="v-cv">${box('7 / 2','int / int')}<span class="v-fn">=</span>${box('3','int','warn')}</div><div class="v-cv">${box('(double) 7 / 2','double / int')}<span class="v-fn">=</span>${box('3.5','double','ok')}</div>`,note:'Pembagian dua int menghasilkan int. Ubah salah satu operand ke double untuk mendapat pecahan.'}]
  :[
    {h:`<div class="v-cv">${box('"42"','str')}<span class="v-fn">int()</span>${box('42','int','ok')}</div>`,note:'Python tidak mengubah tipe diam-diam antara teks dan angka. Pakai <code>int()</code>, <code>float()</code>, atau <code>str()</code>. Hasil <code>input()</code> selalu str.'},
    {h:`<div class="v-cv">${box('9.99','float')}<span class="v-fn">int()</span>${box('9','int','warn')}</div><p class="v-sub">Pecahan <s>.99</s> dipotong ke arah nol. Untuk membulatkan pakai <code>round()</code>.</p>`,note:'<code>int(9.99)</code> memotong, bukan membulatkan.'},
    {h:`<div class="v-cv">${box('"4.5"','str')}<span class="v-fn">int()</span>${box('ValueError','error','bad')}</div><div class="v-cv">${box('"4.5"','str')}<span class="v-fn">float()</span>${box('4.5','float','ok')}</div>`,note:'Teks berisi pecahan tidak bisa langsung jadi int. Ubah dulu ke float.'},
    {h:`<div class="v-cv">${box('2 ** 100','int')}<span class="v-fn">=</span>${box('1267650600228229401496703205376','int','ok')}</div>`,note:'int di Python tidak punya batas ukuran, jadi tidak ada overflow seperti di Java.'},
    {h:`<div class="v-cv">${box('7 / 2','int / int')}<span class="v-fn">=</span>${box('3.5','float','ok')}</div><div class="v-cv">${box('7 // 2','int // int')}<span class="v-fn">=</span>${box('3','int','warn')}</div>`,note:'<code>/</code> selalu menghasilkan float, <code>//</code> pembagian bulat.'},
    {h:`<div class="v-cv">${box('0, "", []','int, str, list')}<span class="v-fn">bool()</span>${box('False','bool','warn')}</div>`,note:'Nilai "kosong" dianggap False saat dipakai di if. Ini disebut truthy dan falsy.'}];
  player(host,fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-cast">${f.h}</div>`}),{speed:2200});
}

/* ---------- garbage collection ---------- */
function gcViz(host,{lang}){
  const P=lang==='python';
  const fr=[
    {code:P?'a = Toko("A")':'Toko a = new Toko("A");',v:{a:1},o:[1],note:'Objek #1 dibuat di <b>heap</b>. Variabel a di stack menyimpan referensinya.'},
    {code:P?'b = Toko("B")':'Toko b = new Toko("B");',v:{a:1,b:2},o:[1,2],note:'Objek #2 dibuat, dirujuk oleh b.'},
    {code:'a = b'+(P?'':';'),v:{a:2,b:2},o:[1,2],note:'a sekarang menunjuk objek #2. Objek #1 tidak dirujuk siapa pun: <b>tidak terjangkau</b>.'},
    {code:P?'b = None':'b = null;',v:{a:2,b:null},o:[1,2],note:'b dikosongkan, tapi objek #2 masih dirujuk a, jadi masih hidup.'},
    {code:P?'# hitungan referensi #1 = 0':'// GC: fase mark',v:{a:2,b:null},o:[1,2],mark:1,note:P?'Python memakai <b>reference counting</b>: begitu jumlah perujuk objek #1 menjadi 0, ia langsung bisa dibuang.':'Garbage collector menelusuri dari stack (root). Objek yang terjangkau <b>ditandai</b> (mark).'},
    {code:P?'# memori #1 dibebaskan':'// GC: fase sweep',v:{a:2,b:null},o:[2],note:'Objek yang tidak terjangkau <b>disapu</b> (sweep) dan memorinya dipakai ulang. Kamu tidak perlu memanggil free() seperti di C.'}];
  player(host,fr,(st,f)=>flip(st,()=>{const refs=id=>Object.entries(f.v).filter(([,x])=>x===id).map(([k])=>k);
    st.innerHTML=`<pre class="code v-q">${hl(f.code,P?'python':'java')}</pre><div class="v-mem2"><div><div class="v-cap">Stack</div>${Object.entries(f.v).map(([k,x])=>`<div class="v-var" data-key="v${k}"><span>${k}</span><b>${x==null?(P?'None':'null'):'→ #'+x}</b></div>`).join('')}</div>
     <div><div class="v-cap">Heap</div><div class="v-heap">${f.o.map(id=>{const r=refs(id);return `<div class="v-obj ${r.length?'':'dead'} ${f.mark&&r.length?'mark':''}" data-key="o${id}"><b>#${id} Toko("${id===1?'A':'B'}")</b><small>${r.length?'dirujuk: '+r.join(', '):'tidak terjangkau'}${P?` · refcount ${r.length}`:''}</small></div>`}).join('')}</div></div></div>`}),{speed:1900});
}

/* ---------- pass by value ---------- */
function passvalViz(host,{lang}){
  const P=lang==='python',nl=P?'None':'null';
  const code=P?'def ubah(n, a):\n    n = 99\n    a[0] = 99\n\nx = 5\narr = [1, 2, 3]\nubah(x, arr)\nprint(x, arr)':'static void ubah(int n, int[] a) {\n    n = 99;\n    a[0] = 99;\n}\n// di main:\nint x = 5;\nint[] arr = {1, 2, 3};\nubah(x, arr);\nSystem.out.println(x + " " + arr[0]);';
  const fr=[
    {m:{x:5,arr:'#1'},h:[1,2,3],note:'main punya x = 5 dan arr yang menunjuk objek array #1 di heap.'},
    {m:{x:5,arr:'#1'},u:{n:5,a:'#1'},h:[1,2,3],note:P?'Saat ubah dipanggil, n dan a menerima <b>referensi yang sama</b> dengan x dan arr (pass by object reference).':'Java selalu <b>pass by value</b>: n menerima salinan nilai 5, a menerima salinan <i>alamat</i> array, jadi menunjuk objek yang sama.'},
    {m:{x:5,arr:'#1'},u:{n:99,a:'#1'},h:[1,2,3],cn:1,note:P?'<code>n = 99</code> hanya mengikat ulang nama lokal n. x di luar tidak berubah.':'<code>n = 99</code> hanya mengubah salinan. x di main tetap 5.'},
    {m:{x:5,arr:'#1'},u:{n:99,a:'#1'},h:[99,2,3],ch:1,note:'<code>a[0] = 99</code> mengubah isi objek yang dipakai bersama. arr di main ikut melihat perubahan.'},
    {m:{x:5,arr:'#1'},h:[99,2,3],note:`ubah selesai, frame-nya hilang. Keluaran: <b>${P?'5 [99, 2, 3]':'5 99'}</b>.`}];
  host.innerHTML=`<pre class="code v-q">${hl(code,P?'python':'java')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{const fb=(nm,o,cls)=>`<div class="v-frame ${cls||''}" data-key="fr${nm}"><div class="v-cap">${nm}()</div>${Object.entries(o).map(([k,x])=>`<div class="v-var ${(k==='n'&&f.cn)?'chg':''}"><span>${k}</span><b>${String(x).startsWith('#')?'→ '+x:x}</b></div>`).join('')}</div>`;
    st.innerHTML=`<div class="v-mem2"><div><div class="v-cap">Stack</div><div class="v-stack">${f.u?fb('ubah',f.u,'top'):''}${fb('main',f.m)}</div></div><div><div class="v-cap">Heap</div><div class="v-obj ${f.ch?'chg':''}"><b>#1 array</b>${cellsHTML(f.h,i=>f.ch&&i===0?'hl':'')}</div></div></div>`}),{speed:1900});
  void nl;
}

/* ---------- exception: stack unwinding ---------- */
function unwindViz(host,{lang}){
  const P=lang==='python',E=P?'ZeroDivisionError':'ArithmeticException';
  const code=P?'def bagi(a, b):\n    return a / b        # b = 0!\n\ndef proses():\n    return bagi(10, 0)\n\ntry:\n    proses()\nexcept ZeroDivisionError as e:\n    print("Gagal:", e)':'static int bagi(int a, int b) {\n    return a / b;      // b = 0!\n}\nstatic int proses() {\n    return bagi(10, 0);\n}\n// main:\ntry {\n    proses();\n} catch (ArithmeticException e) {\n    System.out.println("Gagal: " + e.getMessage());\n}';
  const S=['main','proses','bagi'];
  const fr=[{n:1,note:'main memanggil proses() di dalam blok try.'},{n:2,note:'proses memanggil bagi(10, 0). Call stack bertambah.'},{n:3,note:'bagi memanggil dirinya di puncak stack, lalu membagi dengan 0.'},
    {n:3,ex:2,note:`<b>${E}</b> dilempar di bagi. Tidak ada ${P?'except':'catch'} di sini, jadi frame bagi dibuang.`},
    {n:2,ex:1,note:`Exception naik ke proses. Di sini juga tidak ada penangkap: frame proses dibuang. Proses ini disebut <b>stack unwinding</b>.`},
    {n:1,ex:0,cat:1,note:`main punya ${P?'except ZeroDivisionError':'catch (ArithmeticException e)'}. Exception tertangkap, program tidak crash.`},
    {n:1,cat:1,out:P?'Gagal: division by zero':'Gagal: / by zero',note:'Blok penangkap dijalankan dan program lanjut normal.'}];
  host.innerHTML=`<pre class="code v-q">${hl(code,P?'python':'java')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-mem2"><div><div class="v-cap">Call stack</div><div class="v-stack">${S.slice(0,f.n).map((s,i)=>`<div class="v-frame ${f.ex===i?'throw':''} ${f.cat&&i===0?'catch':''}" data-key="s${s}"><b>${s}()</b>${f.ex===i?`<small>${E} ↑</small>`:''}</div>`).reverse().join('')}</div></div>
    <div><div class="v-cap">Keluaran</div><div class="console">${f.out?esc(f.out):''}</div></div></div>`}),{speed:1700});
}

/* ---------- stream / comprehension ---------- */
function streamViz(host,{lang}){
  const P=lang==='python',D=[5,12,8,3,20,15];
  const code=P?'data = [5, 12, 8, 3, 20, 15]\nhasil = [x * 2 for x in data if x > 7]\nprint(hasil)':'List<Integer> data = List.of(5, 12, 8, 3, 20, 15);\nList<Integer> hasil = data.stream()\n    .filter(x -> x > 7)\n    .map(x -> x * 2)\n    .collect(Collectors.toList());';
  const ST=P?['data','if x > 7','x * 2','hasil [ ]']:['data','filter(x > 7)','map(x * 2)','collect'];
  const fr=[{pos:D.map(()=>0),note:P?'Comprehension membaca data satu per satu: saring dengan if, ubah dengan ekspresi di depan, kumpulkan ke list.':'Stream memproses elemen <b>satu per satu</b> melewati seluruh pipeline, bukan tahap demi tahap untuk semua data.'}];
  const pos=D.map(()=>0);
  D.forEach((x,i)=>{pos[i]=1;fr.push({pos:[...pos],note:`${x} masuk ke ${ST[1]}.`});
    if(x>7){pos[i]=2;fr.push({pos:[...pos],note:`${x} lolos, lalu diubah menjadi ${x*2}.`});pos[i]=3;fr.push({pos:[...pos],note:`${x*2} masuk ke hasil.`})}
    else{pos[i]=-1;fr.push({pos:[...pos],note:`${x} tidak lolos (${x} ≤ 7), dibuang.`})}});
  fr[fr.length-1].note+=` Hasil akhir: [${D.filter(x=>x>7).map(x=>x*2).join(', ')}].`;
  host.innerHTML=`<pre class="code v-q">${hl(code,P?'python':'java')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-lanes">${ST.map((s,c)=>`<div class="v-lane"><div class="v-cap">${esc(s)}</div><div class="v-toks">${D.map((x,i)=>f.pos[i]===c?`<span class="tok ${c===2||c===3?'ok':''}" data-key="t${i}">${c>=2?x*2:x}</span>`:'').join('')}</div></div>`).join('')}</div>
    <div class="v-drop">${D.map((x,i)=>f.pos[i]===-1?`<span class="tok bad" data-key="t${i}">${x}</span>`:'').join('')}</div>`}),{speed:900});
}

/* ---------- race condition ---------- */
function raceViz(host,{lang}){
  const P=lang==='python';let lock=false;
  host.innerHTML=`<div class="seg" role="group" aria-label="Mode"><button data-k="0" aria-pressed="true">Tanpa kunci</button><button data-k="1" aria-pressed="false">${P?'Dengan Lock':'Dengan synchronized'}</button></div><div class="pl"></div>`;
  const pl=$('.pl',host);let Pl;
  const F={0:[[0,'-','-','','','Dua thread sama-sama ingin menjalankan <code>counter += 1</code>. Itu sebenarnya tiga langkah: baca, tambah, tulis.'],
      [0,'baca 0','-','1','','Thread 1 membaca counter = 0.'],[0,'baca 0','baca 0','2','','Sebelum Thread 1 menulis, Thread 2 juga membaca 0.'],
      [1,'tulis 1','baca 0','1','','Thread 1 menulis 0 + 1 = 1.'],[1,'tulis 1','tulis 1','2','bad','Thread 2 juga menulis 0 + 1 = 1. Satu penambahan <b>hilang</b>! Seharusnya 2. Inilah <b>race condition</b>.']],
    1:[[0,'-','-','','','Sekarang bagian kritis dikunci: hanya satu thread boleh masuk.'],[0,'🔒 baca 0','menunggu','1','','Thread 1 memegang kunci dan membaca 0. Thread 2 harus menunggu.'],
      [1,'tulis 1 🔓','menunggu','1','','Thread 1 menulis 1 lalu melepas kunci.'],[1,'selesai','🔒 baca 1','2','','Thread 2 mendapat kunci dan membaca nilai terbaru, 1.'],[2,'selesai','tulis 2 🔓','2','ok','Hasil benar: 2. Harganya: thread bergantian, jadi sedikit lebih lambat.']]};
  const draw=(st,f)=>{st.innerHTML=`<div class="v-race"><div class="v-th ${f.a==='1'?'cur':''}"><div class="v-cap">Thread 1</div><b>${f.t1}</b></div><div class="v-shared ${f.r}"><div class="v-cap">counter (bersama)</div><b>${f.c}</b>${f.r==='bad'?'<small>harapan: 2</small>':''}</div><div class="v-th ${f.a==='2'?'cur':''}"><div class="v-cap">Thread 2</div><b>${f.t2}</b></div></div>`};
  const fr=k=>F[k].map(([c,t1,t2,a,r,note])=>({c,t1,t2,a,r,note}));
  function build(){host.querySelectorAll('[data-k]').forEach(b=>b.setAttribute('aria-pressed',(b.dataset.k==='1')===lock));if(!Pl)Pl=player(pl,fr(+lock),draw,{speed:1700});else Pl.set(fr(+lock))}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-k]');if(b){lock=b.dataset.k==='1';build()}});build();
}

/* ---------- siklus build Maven ---------- */
function buildViz(host){
  const PH=[['validate','Cek pom.xml dan struktur proyek.',[]],['compile','javac mengubah src/main/java menjadi .class.',['target/classes/App.class']],
    ['test','JUnit menjalankan tes. Jika satu gagal, build berhenti di sini.',['target/surefire-reports/ (12 tes lulus)']],
    ['package','Kelas dibungkus menjadi file JAR.',['target/app-1.0.jar']],['install','JAR disalin ke repositori lokal ~/.m2 agar proyek lain bisa memakainya.',['~/.m2/.../app-1.0.jar']],
    ['deploy','JAR dikirim ke repositori jarak jauh (misalnya Nexus atau Maven Central).',['repo.perusahaan.com/app-1.0.jar']]];
  const fr=PH.map((p,i)=>({i,note:`<b>mvn ${p[0]}</b>: ${p[1]} Menjalankan satu fase berarti menjalankan semua fase sebelumnya juga.`}));
  fr.unshift({i:-1,note:'Maven menjalankan <b>fase</b> berurutan. Ketik <code>mvn package</code> dan fase validate, compile, test, package berjalan otomatis. Gradle punya urutan serupa: <code>gradle build</code>.'});
  player(host,fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-pipe big">${PH.map((p,i)=>`<span class="${i===f.i?'cur':i<f.i?'done':''}">${p[0]}</span>`).join('<i aria-hidden="true">›</i>')}</div>
    <div class="v-tree"><div>📁 proyek/</div><div class="in">📄 pom.xml</div><div class="in">📁 src/main/java/App.java</div><div class="in">📁 src/test/java/AppTest.java</div>${PH.slice(0,f.i+1).flatMap((p,i)=>p[2].map((a,k)=>`<div class="in new" data-key="a${i}${k}">✓ ${esc(a)}</div>`)).join('')}</div>`}),{speed:1600});
}

/* ---------- decorator ---------- */
function decoratorViz(host){
  const code='def catat(fungsi):\n    def pembungkus(*args):\n        print("mulai", fungsi.__name__)\n        hasil = fungsi(*args)\n        print("selesai")\n        return hasil\n    return pembungkus\n\n@catat\ndef tambah(a, b):\n    return a + b\n\nprint(tambah(2, 3))';
  const fr=[{a:'',out:'',note:'<code>@catat</code> di atas <code>def tambah</code> sama artinya dengan <code>tambah = catat(tambah)</code>.'},
    {a:'wrap',out:'',note:'Nama <b>tambah</b> kini menunjuk ke <b>pembungkus</b>. Fungsi asli tersimpan di dalamnya sebagai <code>fungsi</code> (closure).'},
    {a:'before',out:'mulai tambah\n',note:'Memanggil tambah(2, 3) sebenarnya memanggil pembungkus. Kode "sebelum" jalan dulu.'},
    {a:'inner',out:'mulai tambah\n',note:'pembungkus memanggil fungsi asli: 2 + 3 = 5.'},
    {a:'after',out:'mulai tambah\nselesai\n',note:'Kode "sesudah" jalan, lalu hasil 5 dikembalikan.'},
    {a:'done',out:'mulai tambah\nselesai\n5\n',note:'Decorator menambah perilaku (log, cek izin, cache, ukur waktu) tanpa mengubah isi fungsi aslinya.'}];
  host.innerHTML=`<pre class="code v-q">${hl(code,'python')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>{st.innerHTML=`<div class="v-mem2"><div><div class="v-name">tambah →</div><div class="v-wrap1 ${f.a?'on':''} ${['before','after'].includes(f.a)?'cur':''}"><div class="v-cap">${f.a?'pembungkus':'tambah (asli)'}</div>${f.a?`<div class="v-step ${f.a==='before'?'cur':''}">print("mulai")</div><div class="v-wrap2 ${f.a==='inner'?'cur':''}"><div class="v-cap">fungsi = tambah asli</div>return a + b</div><div class="v-step ${f.a==='after'?'cur':''}">print("selesai")</div>`:'<div class="v-wrap2">return a + b</div>'}</div></div>
    <div><div class="v-cap">Keluaran</div><div class="console">${esc(f.out)}</div></div></div>`},{speed:1800});
}

/* ---------- event loop asyncio ---------- */
function eventloopViz(host){
  let mode='async';const T=[['A',2],['B',1],['C',3]];
  host.innerHTML=`<div class="seg" role="group" aria-label="Mode"><button data-m="sync" aria-pressed="false">Berurutan (sync)</button><button data-m="async" aria-pressed="true">asyncio.gather</button></div><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function frames(){const fr=[];const end=mode==='sync'?6:3;
    for(let t=0;t<=end;t++){const bars=T.map(([n,d],i)=>{const st=mode==='sync'?T.slice(0,i).reduce((a,x)=>a+x[1],0):0;return {n,st,d,p:Math.max(0,Math.min(d,t-st))}});
      fr.push({t,bars,note:mode==='sync'?(t===0?'Tanpa async, unduhan A, B, C dijalankan satu per satu. Program diam menunggu setiap unduhan.':t===end?`Selesai di detik ${end}. Waktu habis untuk menunggu.`:`Detik ${t}: hanya satu tugas berjalan, yang lain antre.`)
        :(t===0?'Event loop memulai A. Saat A <code>await</code> jaringan, loop langsung beralih ke B, lalu C. Ketiganya menunggu bersamaan.':t===end?`Selesai di detik ${end}, setara tugas terlama. Satu thread saja, tanpa lock.`:`Detik ${t}: ${bars.filter(b=>b.p===b.d&&t>=b.d).map(b=>b.n).join(', ')||'belum ada'} selesai; sisanya masih menunggu I/O.`)})}
    return fr}
  const draw=(st,f)=>{st.innerHTML=`<div class="v-gantt">${f.bars.map(b=>`<div class="v-gr"><span>unduh ${b.n} (${b.d} dtk)</span><div class="v-gt"><i style="left:${b.st/6*100}%;width:${b.p/6*100}%" class="${b.p===b.d?'ok':''}"></i></div></div>`).join('')}<div class="v-gr"><span></span><div class="v-axis">${[0,1,2,3,4,5,6].map(x=>`<b class="${x===f.t?'cur':''}">${x}</b>`).join('')}</div></div></div>`};
  function build(){host.querySelectorAll('[data-m]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.m===mode));if(!P)P=player(pl,frames(),draw,{speed:1000});else P.set(frames())}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-m]');if(b){mode=b.dataset.m;build()}});build();
}

const VIZ2={
  casting:castingViz,gc:gcViz,passval:passvalViz,unwind:unwindViz,stream:streamViz,race:raceViz,build:buildViz,decorator:decoratorViz,eventloop:eventloopViz,
  sqltable:sqlTableViz,sqlvsnosql:sqlNoSqlViz,er:erViz,index:indexViz,txn:txnViz,isolation:isolationViz,injection:injectionViz,recursive:recursiveViz,window:windowViz,
  pipeline:(h,{lesson})=>{h.innerHTML=`<pre class="code v-q">${hl(lesson.vq,'sql')}</pre><div class="pl"></div>`;sqlPipeline($('.pl',h),SQLE.create(SEED.toko),lesson.vq)},
  join:(h,{lesson})=>joinViz(h,lesson.vj||'INNER')
};
const VIZ2T={casting:'Konversi tipe',gc:'Garbage collection',passval:'Cara argumen dikirim',unwind:'Exception merambat di call stack',stream:'Data mengalir lewat pipeline',race:'Race condition',build:'Siklus build',decorator:'Decorator membungkus fungsi',eventloop:'Event loop',
  sqltable:'Anatomi tabel',sqlvsnosql:'SQL lawan NoSQL',er:'Diagram relasi',index:'Index lawan full scan',txn:'Transaksi transfer',isolation:'Tingkat isolasi',injection:'Simulasi SQL injection',recursive:'CTE rekursif',window:'Window function',pipeline:'Urutan eksekusi query',join:'JOIN baris demi baris'};
