/* ===================== SIMULATOR FLOWCHART & PSEUDOCODE =====================
   Satu program (lesson.fc) digambar sebagai flowchart bergaya Flowgorithm,
   ditulis ulang sebagai pseudocode, lalu dijalankan langkah demi langkah.
   fc = {name, in:[input...], p:[node...]}
   node: {t:'dec',v,ty,arr} {t:'in',v} {t:'asg',v,e} {t:'out',e}
         {t:'if',c,y:[],n:[]} {t:'while',c,b:[]} {t:'for',v,a,z,s,b:[]} {t:'do',c,u,b:[]}
   Ekspresi memakai sintaks Flowgorithm: = (sama dengan), <>, mod, and, or, not, & (gabung teks). */
const FCF={Int:Math.trunc,Sqrt:Math.sqrt,Abs:Math.abs,Len:s=>String(s).length,ToString:String,ToInteger:x=>parseInt(x,10),Char:(s,i)=>String(s)[i],FCS:v=>fcOut(v)};
const fcJs=e=>String(e).replace(/"[^"]*"|\b(mod|and|or|not)\b|<>|!=|==|<=|>=|=|&|\^/g,m=>m[0]==='"'?m:({mod:'%',and:'&&',or:'||',not:'!','<>':'!=','!=':'!=','==':'==','<=':'<=','>=':'>=','=':'==','&':'+','^':'**'})[m]);
/* & (gabung teks) dipecah di tingkat teratas agar angka dan array diformat rapi */
function fcCat(e){const p=[];let d=0,q=false,b=0;e=String(e);for(let i=0;i<e.length;i++){const c=e[i];if(c==='"')q=!q;else if(!q){if(c==='('||c==='[')d++;else if(c===')'||c===']')d--;else if(c==='&'&&!d){p.push(e.slice(b,i));b=i+1}}}p.push(e.slice(b));return p}
const fcEv=(S,e)=>{const p=fcCat(e),js=p.length>1?p.map(x=>'FCS('+fcJs(x)+')').join('+'):fcJs(e);return Function('S','F','with(F)with(S){return ('+js+')}')(S,FCF)};
const fcSet=(S,lhs,v)=>Function('S','F','v','with(F)with(S){'+lhs+'=v}')(S,FCF,v);
const fcFmt=v=>v===undefined?'—':Array.isArray(v)?'['+v.map(fcFmt).join(', ')+']':typeof v==='string'?'"'+v+'"':typeof v==='number'&&!Number.isInteger(v)?String(Math.round(v*1000)/1000):String(v);
const fcOut=v=>Array.isArray(v)?'['+v.map(fcOut).join(', ')+']':typeof v==='number'&&!Number.isInteger(v)?String(Math.round(v*1000)/1000):String(v);
function fcIds(list,c){list.forEach(n=>{n.id='n'+(c.k++);['y','n','b'].forEach(k=>Array.isArray(n[k])&&fcIds(n[k],c))})}
const fcLabel=n=>({dec:()=>`${n.ty} ${n.v}${n.arr?'['+n.arr+']':''}`,in:()=>`Input ${n.v}`,asg:()=>`${n.v} = ${n.e}`,out:()=>`Output ${n.e}`,
  if:()=>n.c,while:()=>n.c,do:()=>n.c,for:()=>`${n.v} = ${n.a} to ${n.z}${n.s&&n.s!=='1'?' step '+n.s:''}`})[n.t]();

/* ---------- pseudocode ---------- */
function fcPseudo(fc){
  const L=[],at={};const em=(d,s,id)=>{if(id)at[id]=L.length;L.push({d,s,id})};
  const ex=e=>String(e).replace(/"[^"]*"|\s&\s/g,m=>m[0]==='"'?m:', ');
  em(0,'START','s');
  const walk=(list,d)=>list.forEach(n=>{
    if(n.t==='dec')em(d,`DECLARE ${n.v} : ${n.arr?`ARRAY[${n.arr}] OF `:''}${n.ty.toUpperCase()}`,n.id);
    else if(n.t==='in')em(d,`INPUT ${n.v}`,n.id);
    else if(n.t==='asg')em(d,`${n.v} ← ${n.e}`,n.id);
    else if(n.t==='out')em(d,`OUTPUT ${ex(n.e)}`,n.id);
    else if(n.t==='if'){em(d,`IF ${n.c} THEN`,n.id);walk(n.y,d+1);if(n.n.length){em(d,'ELSE');walk(n.n,d+1)}em(d,'ENDIF')}
    else if(n.t==='while'){em(d,`WHILE ${n.c} DO`,n.id);walk(n.b,d+1);em(d,'ENDWHILE')}
    else if(n.t==='for'){em(d,`FOR ${n.v} ← ${n.a} TO ${n.z}${n.s&&n.s!=='1'?' STEP '+n.s:''} DO`,n.id);walk(n.b,d+1);em(d,'ENDFOR')}
    else if(n.t==='do'){em(d,'REPEAT');walk(n.b,d+1);em(d,`UNTIL ${n.u||'NOT ('+n.c+')'}`,n.id)}
  });
  walk(fc.p,1);em(0,'END','e');
  return {L,at};
}

/* ---------- menjalankan program ---------- */
function fcRun(fc,inputs){
  const S={},T={},out=[],inp=[...inputs],F=[];let g=0;
  const snap=(id,note)=>F.push({id,note,vars:Object.keys(T).map(k=>[k,T[k],fcFmt(S[k])]),out:out.slice()});
  const base=v=>T[String(v).split('[')[0].trim()]||'';
  const coerce=(ty,v)=>/^Integer/.test(ty)&&typeof v==='number'?Math.trunc(v):v;
  const run=list=>{for(const n of list){if(++g>1500)throw new Error('Program berputar terlalu lama (lebih dari 1500 langkah). Periksa kondisi berhentinya.');step(n)}};
  const step=n=>{
    if(n.t==='dec'){n.v.split(',').map(s=>s.trim()).forEach(v=>{T[v]=n.ty+(n.arr?'[]':'');S[v]=n.arr?Array(fcEv(S,n.arr)).fill(undefined):undefined});snap(n.id,`Menyiapkan variabel <b>${esc(n.v)}</b> bertipe ${n.ty}${n.arr?' (array)':''}. Isinya belum ada.`)}
    else if(n.t==='in'){const raw=inp.length?inp.shift():'0',ty=base(n.v);let v=raw;if(/^Integer/.test(ty))v=parseInt(raw,10)||0;else if(/^Real/.test(ty))v=parseFloat(raw)||0;else if(/^Boolean/.test(ty))v=/^(true|benar|1)$/i.test(raw);
      fcSet(S,n.v,v);snap(n.id,`Pengguna mengetik <b>${esc(raw)}</b>, disimpan ke <b>${esc(n.v)}</b>.`)}
    else if(n.t==='asg'){const v=coerce(base(n.v),fcEv(S,n.e));fcSet(S,n.v,v);snap(n.id,`Hitung <code>${esc(n.e)}</code> = <b>${esc(fcFmt(v))}</b>, simpan ke <b>${esc(n.v)}</b>.`)}
    else if(n.t==='out'){const v=fcOut(fcEv(S,n.e));out.push(v);snap(n.id,`Tampilkan ke layar: <b>${esc(v)}</b>`)}
    else if(n.t==='if'){const c=!!fcEv(S,n.c);snap(n.id,`Periksa <code>${esc(n.c)}</code> → <b>${c?'benar':'salah'}</b>, jalur ${c?'Benar (kanan)':'Salah (kiri)'} dipilih.`);run(c?n.y:n.n)}
    else if(n.t==='while'){for(;;){const c=!!fcEv(S,n.c);snap(n.id,`Periksa <code>${esc(n.c)}</code> → <b>${c?'benar':'salah'}</b>. ${c?'Masuk ke badan loop.':'Loop selesai, lanjut ke bawah.'}`);if(!c)break;run(n.b)}}
    else if(n.t==='for'){const st=n.s?fcEv(S,n.s):1;fcSet(S,n.v,fcEv(S,n.a));for(;;){const z=fcEv(S,n.z),c=st>0?S[n.v]<=z:S[n.v]>=z;
      snap(n.id,`${esc(n.v)} = ${esc(fcFmt(S[n.v]))}. ${c?`Masih ${st>0?'≤':'≥'} ${esc(fcFmt(z))}, jalankan badan loop.`:`Sudah melewati ${esc(fcFmt(z))}, loop selesai.`}`);if(!c)break;run(n.b);S[n.v]+=st}}
    else if(n.t==='do'){for(;;){run(n.b);const c=!!fcEv(S,n.c);snap(n.id,`Badan loop sudah jalan, baru periksa <code>${esc(n.c)}</code> → <b>${c?'benar':'salah'}</b>. ${c?'Ulangi.':'Selesai.'}`);if(!c)break}}
  };
  snap('s','Program dimulai.');
  try{run(fc.p);snap('e','Program selesai.')}catch(e){F.push({id:'e',note:`<span class="err">${esc(e.message)}</span>`,vars:F[F.length-1].vars,out:out.slice(),err:1})}
  return F;
}

/* ---------- tata letak flowchart ---------- */
const FC_CW=7.2,FC_H=36,FC_G=26;
function fcLay(list){
  const it=list.map(fcNode);let l=0,r=0,h=0;it.forEach((x,k)=>{l=Math.max(l,x.l);r=Math.max(r,x.r);h+=x.h+(k?FC_G:0)});
  return {l,r,h,draw(cx,y,o){let yy=y;it.forEach((x,k)=>{if(k){o.push(`<path class="fc-ln" d="M${cx} ${yy} V${yy+FC_G-2}" marker-end="url(#fcA)"/>`);yy+=FC_G}x.draw(cx,yy,o);yy+=x.h})}};
}
function fcShape(kind,id,cx,y,w,h,txt){
  const x=cx-w/2;let s;
  if(kind==='pill')s=`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${h/2}"/>`;
  else if(kind==='para')s=`<polygon points="${x+10},${y} ${x+w},${y} ${x+w-10},${y+h} ${x},${y+h}"/>`;
  else if(kind==='dia')s=`<polygon points="${cx},${y} ${x+w},${y+h/2} ${cx},${y+h} ${x},${y+h/2}"/>`;
  else if(kind==='hex')s=`<polygon points="${x+12},${y} ${x+w-12},${y} ${x+w},${y+h/2} ${x+w-12},${y+h} ${x+12},${y+h} ${x},${y+h/2}"/>`;
  else if(kind==='dec')s=`<rect x="${x}" y="${y}" width="${w}" height="${h}"/><path class="fc-in" d="M${x+6} ${y} V${y+h} M${x} ${y+6} H${x+w}"/>`;
  else s=`<rect x="${x}" y="${y}" width="${w}" height="${h}"/>`;
  return `<g class="fc-s fc-${kind}" data-id="${id}">${s}<text x="${cx+(kind==='dec'?3:0)}" y="${y+h/2+4}">${esc(txt)}</text></g>`;
}
function fcNode(n){
  const txt=n.t==='s'?'Mulai':n.t==='e'?'Selesai':fcLabel(n),tw=txt.length*FC_CW;
  if(['s','e','dec','in','out','asg'].includes(n.t)){
    const kind={s:'pill',e:'pill',dec:'dec',in:'para',out:'para',asg:'rect'}[n.t],w=Math.max(n.t==='s'||n.t==='e'?90:96,tw+(kind==='para'?40:28));
    return {l:w/2,r:w/2,h:FC_H,draw:(cx,y,o)=>o.push(fcShape(kind,n.id,cx,y,w,FC_H,txt))};
  }
  const dw=Math.max(112,tw*1.3+44),dh=n.t==='for'?FC_H+4:50,kind=n.t==='for'?'hex':'dia',dwf=n.t==='for'?Math.max(110,tw+40):dw;
  if(n.t==='if'){
    const Y=fcLay(n.y),N=fcLay(n.n),oR=Math.max(dwf/2+16,Y.l+16),oL=Math.max(dwf/2+16,N.r+16);
    const l=Math.max(dwf/2,oL+N.l),r=Math.max(dwf/2,oR+Y.r),bh=Math.max(Y.h,N.h),h=dh+14+bh+(bh?18:4)+4;
    return {l,r,h,draw(cx,y,o){
      const my=y+dh/2,yb=y+dh+14,ym=yb+bh+(bh?18:4),xr=cx+oR,xl=cx-oL;
      o.push(fcShape(kind,n.id,cx,y,dwf,dh,txt));
      [[Y,xr,cx+dwf/2,'Benar','start'],[N,xl,cx-dwf/2,'Salah','end']].forEach(([B,xx,cor,lab,an])=>{
        o.push(`<text class="fc-lb" x="${cor+(an==='start'?6:-6)}" y="${my-6}" text-anchor="${an}">${lab}</text>`);
        if(B.h){o.push(`<path class="fc-ln" d="M${cor} ${my} H${xx} V${yb-2}" marker-end="url(#fcA)"/>`);B.draw(xx,yb,o);o.push(`<path class="fc-ln" d="M${xx} ${yb+B.h} V${ym} H${cx}"/>`)}
        else o.push(`<path class="fc-ln" d="M${cor} ${my} H${xx} V${ym} H${cx}"/>`)});
      o.push(`<circle class="fc-dot" cx="${cx}" cy="${ym}" r="4"/>`)}};
  }
  const B=fcLay(n.b),l=Math.max(dwf/2,B.l)+22,r=Math.max(dwf/2,B.r)+22;
  if(n.t==='do'){
    const h=20+B.h+(B.h?20:0)+dh+16;
    return {l,r,h,draw(cx,y,o){
      const yb=y+20,yd=yb+B.h+(B.h?20:0),xl=cx-l+4;
      o.push(`<circle class="fc-dot" cx="${cx}" cy="${y+6}" r="4"/>`);
      if(B.h){o.push(`<path class="fc-ln" d="M${cx} ${y+10} V${yb-2}" marker-end="url(#fcA)"/>`);B.draw(cx,yb,o);o.push(`<path class="fc-ln" d="M${cx} ${yb+B.h} V${yd-2}" marker-end="url(#fcA)"/>`)}
      o.push(fcShape(kind,n.id,cx,yd,dwf,dh,txt));
      o.push(`<path class="fc-ln" d="M${cx-dwf/2} ${yd+dh/2} H${xl} V${y+6} H${cx-6}" marker-end="url(#fcA)"/><text class="fc-lb" x="${cx-dwf/2-6}" y="${yd+dh/2-6}" text-anchor="end">Benar</text>`);
      o.push(`<path class="fc-ln" d="M${cx} ${yd+dh} V${yd+dh+16}"/><text class="fc-lb" x="${cx+6}" y="${yd+dh+13}">Salah</text>`)}};
  }
  const h=dh+20+B.h+(B.h?14:0)+20;
  return {l,r,h,draw(cx,y,o){
    const my=y+dh/2,yb=y+dh+20,y1=yb+B.h+(B.h?14:0),xl=cx-l+4,xr=cx+r-4,ye=y1+18;
    o.push(fcShape(kind,n.id,cx,y,dwf,dh,txt));
    if(B.h){o.push(`<path class="fc-ln" d="M${cx} ${y+dh} V${yb-2}" marker-end="url(#fcA)"/>`);B.draw(cx,yb,o);o.push(`<path class="fc-ln" d="M${cx} ${yb+B.h} V${y1}"/>`)}
    else o.push(`<path class="fc-ln" d="M${cx} ${y+dh} V${y1}"/>`);
    o.push(`<path class="fc-ln" d="M${cx} ${y1} H${xl} V${my} H${cx-dwf/2-2}" marker-end="url(#fcA)"/>`);
    o.push(`<path class="fc-ln" d="M${cx+dwf/2} ${my} H${xr} V${ye} H${cx}"/>`);
    const lt=n.t==='for'?['Ulangi','Selesai']:['Benar','Salah'];
    o.push(`<text class="fc-lb" x="${cx+6}" y="${y+dh+14}">${lt[0]}</text><text class="fc-lb" x="${cx+dwf/2+6}" y="${my-6}">${lt[1]}</text>`)}};
}
function fcSVG(fc){
  const all=fcLay([{t:'s',id:'s'},...fc.p,{t:'e',id:'e'}]),P=14,W=Math.ceil(all.l+all.r+P*2),H=Math.ceil(all.h+P*2),o=[];
  all.draw(P+all.l,P,o);
  return `<svg class="fc-svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Flowchart program ${esc(fc.name||'')}"><defs><marker id="fcA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" class="fc-ah"/></marker></defs>${o.join('')}</svg>`;
}

function fcViz(host,{lesson}){
  const fc=lesson.fc;if(!fc)return;
  const c={k:1};fcIds(fc.p,c);
  const ps=fcPseudo(fc),hasIn=fc.in&&fc.in.length;
  host.innerHTML=`${hasIn?`<div class="fc-inp"><label for="fcIn">Input untuk program (pisahkan dengan koma)</label><div class="fc-inr"><input class="inp" id="fcIn" value="${esc(fc.in.join(', '))}" autocomplete="off"><button class="btn" id="fcGo">Jalankan dengan input ini</button></div></div>`:''}
  <div class="fc-grid"><div class="fc-cw"><div class="fc-tools"><span class="fc-hint">Geser untuk melihat seluruh flowchart.</span><button class="tlink" data-fit aria-pressed="false">Muat ke lebar layar</button></div><div class="fc-chart" tabindex="0" role="region" aria-label="Flowchart, bisa digeser">${fcSVG(fc)}</div></div>
  <div class="fc-side"><div class="fc-box"><div class="eyebrow">Pseudocode</div><ol class="fc-ps">${ps.L.map((x,i)=>`<li data-i="${i}"><span style="padding-left:${x.d*1.4}em">${esc(x.s)}</span></li>`).join('')}</ol></div>
  <div class="fc-box"><div class="eyebrow">Variabel</div><div class="fc-vars"></div></div>
  <div class="fc-box"><div class="eyebrow">Layar keluaran</div><pre class="fc-con"></pre></div></div></div><div class="fc-play"></div>`;
  const chart=$('.fc-chart',host),lines=[...host.querySelectorAll('.fc-ps li')],vars=$('.fc-vars',host),con=$('.fc-con',host);
  let prev=null;
  const fit=$('[data-fit]',host),tools=$('.fc-tools',host),svg=$('.fc-svg',host);
  const chk=()=>{const over=svg.getBoundingClientRect().width>chart.clientWidth+2||chart.classList.contains('fit');tools.hidden=!over};
  fit.onclick=()=>{const on=chart.classList.toggle('fit');fit.setAttribute('aria-pressed',on);fit.textContent=on?'Ukuran asli':'Muat ke lebar layar'};
  requestAnimationFrame(chk);if(window.ResizeObserver)new ResizeObserver(chk).observe(chart);
  const draw=(st,f)=>{
    host.querySelectorAll('.fc-s.on').forEach(g=>g.classList.remove('on'));
    const g=host.querySelector(`.fc-s[data-id="${f.id}"]`);if(g){g.classList.add('on');
      const r=g.getBoundingClientRect(),cr=chart.getBoundingClientRect();if(r.top<cr.top||r.bottom>cr.bottom||r.left<cr.left||r.right>cr.right)chart.scrollTo({top:chart.scrollTop+r.top-cr.top-cr.height/2+r.height/2,left:chart.scrollLeft+r.left-cr.left-cr.width/2+r.width/2,behavior:RM()?'auto':'smooth'})}
    lines.forEach(li=>li.classList.toggle('on',ps.at[f.id]===+li.dataset.i));
    const pv=prev&&prev.vars?Object.fromEntries(prev.vars.map(v=>[v[0],v[2]])):{};
    vars.innerHTML=f.vars.length?`<table class="fc-vt"><thead><tr><th scope="col">Nama</th><th scope="col">Tipe</th><th scope="col">Nilai</th></tr></thead><tbody>${f.vars.map(v=>`<tr class="${pv[v[0]]!==undefined&&pv[v[0]]!==v[2]?'chg':''}"><th scope="row">${esc(v[0])}</th><td>${esc(v[1])}</td><td>${esc(v[2])}</td></tr>`).join('')}</tbody></table>`:'<p class="muted">Belum ada variabel.</p>';
    con.textContent=f.out.length?f.out.join('\n'):' ';con.classList.toggle('empty',!f.out.length);
    st.innerHTML='';prev=f;
  };
  const frames=inp=>{prev=null;return fcRun(fc,inp)};
  const pl=player($('.fc-play',host),frames(fc.in||[]),draw,{speed:900});
  const go=$('#fcGo',host);if(go){const ip=$('#fcIn',host);go.onclick=()=>pl.set(frames(ip.value.split(',').map(s=>s.trim()).filter(s=>s!=='')));ip.onkeydown=e=>{if(e.key==='Enter'){e.preventDefault();go.click()}}}
}

/* ---------- memilih jenis loop ---------- */
function loopPickViz(host){
  const Q=[['Mencetak nomor kursi 1 sampai 40','for','Jumlah putaran sudah pasti: 40.'],
    ['Meminta PIN sampai benar','do','Pertanyaan harus muncul minimal sekali, lalu diulang selama PIN salah.'],
    ['Menabung sampai saldo mencapai Rp1.000.000','while','Kita tidak tahu berapa minggu; yang diketahui hanya kondisi berhentinya.'],
    ['Menjumlahkan semua harga di keranjang','each','Kita hanya perlu membaca setiap isi koleksi, tidak butuh nomor indeksnya.'],
    ['Menukar dua angka bersebelahan selama masih ada yang tertukar (bubble sort)','while','Berhenti saat satu putaran tidak ada pertukaran, jadi jumlah putaran tidak pasti.'],
    ['Menampilkan menu kasir sampai pengguna memilih Keluar','do','Menu tampil dulu, baru dicek pilihannya.'],
    ['Mencetak tabel perkalian 1 sampai 10','for','Batas awal dan akhir jelas: for bersarang 10 × 10.'],
    ['Membaca baris file sampai habis','while','Jumlah baris tidak diketahui sebelumnya; berhenti saat tidak ada baris lagi.']];
  const N={for:'for',while:'while',do:'do-while',each:'for-each'};let i=0,sc=0;
  const show=()=>{const q=Q[i];host.innerHTML=`<div class="lp"><p class="lp-c">Kasus ${i+1} dari ${Q.length}</p><p class="lp-q">${esc(q[0])}</p><div class="lp-o" role="group" aria-label="Pilih jenis loop">${Object.keys(N).map(k=>`<button class="btn" data-k="${k}">${N[k]}</button>`).join('')}</div><div class="lp-fb" aria-live="polite"></div></div>`;
    host.querySelector('.lp-o').onclick=e=>{const b=e.target.closest('button');if(!b)return;const ok=b.dataset.k===q[1];if(ok)sc++;
      host.querySelectorAll('.lp-o button').forEach(x=>{x.disabled=true;if(x.dataset.k===q[1])x.classList.add('ok');else if(x===b)x.classList.add('bad')});
      $('.lp-fb',host).innerHTML=`<div class="tk-fb ${ok?'ok':'bad'}"><b>${ok?'✓ Tepat.':'Kurang tepat.'}</b> Pilihan terbaik: <b>${N[q[1]]}</b>. ${esc(q[2])}</div><div class="sl-act"><button class="btn primary" id="lpN">${i<Q.length-1?'Kasus berikutnya':'Lihat skor'}</button></div>`;
      $('#lpN',host).onclick=()=>{i++;if(i<Q.length)show();else{host.innerHTML=`<div class="lp"><p class="lp-q">Skor: ${sc} dari ${Q.length}</p><p class="muted">${sc>=7?'Bagus! Kamu sudah bisa memilih loop sesuai kebutuhan.':'Baca lagi tabel ringkas di atas, lalu coba sekali lagi.'}</p><button class="btn" id="lpR">Ulangi</button></div>`;$('#lpR',host).onclick=()=>{i=0;sc=0;show()}}}}};
  show();
}
Object.assign(VIZ2,{fc:fcViz,looppick:loopPickViz});
Object.assign(VIZ2T,{fc:'Simulator flowchart dan pseudocode',looppick:'Pilih loop yang tepat'});
