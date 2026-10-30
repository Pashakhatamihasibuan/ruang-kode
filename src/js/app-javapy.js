/* ===================== PELAJARAN JAVA & PYTHON (lab & topic) =====================
   Dipindahkan dari app.js lama tanpa perubahan perilaku. */
function labHTML(n,lang){
  const c=CH[n-1];
  return `<nav class="toc" aria-label="Di halaman ini">${[['Konsep','#konsep'],['Lab','#lab'],['Program','#prog'],['Istilah','#istilah'],['Kuis','#quiz']].map(([a,b])=>`<button data-to="${b}">${a}</button>`).join('')}</nav>
  <section class="prose" id="konsep">${c.body.map(p=>`<p>${p}</p>`).join('')}</section>
  <ul class="points">${c.points.map(p=>`<li>${p}</li>`).join('')}</ul>
  <section class="viz" id="lab" aria-label="Visualisasi"><div class="viz-head"><span class="eyebrow">Lab interaktif</span><h3>${c.vizT}</h3><p>${c.vizD}</p></div><div id="vizHost" class="vizhost"></div></section>
  <section class="section" id="prog"><h2>Program lengkap</h2>${pane(lang,c[lang],{out:c.out==null?null:typeof c.out==='string'?c.out:c.out[lang]})}</section>
  <div class="tip"><b>Tip mentor.</b> ${c.tip}</div>
  <section class="section" id="istilah"><h2>Istilah di pelajaran ini</h2><div class="terms">${c.terms.map(id=>`<button class="term-chip" data-term="${id}">${GLMAP[id].t}</button>`).join('')}</div></section>
  <section class="section" id="quiz"><h2>Kuis cepat</h2>${quizHTML(c.quiz,n)}</section>`;
}
function wireLab(n){const c=CH[n-1];VIZ[c.viz]($('#vizHost'));wireQuiz($('#quiz'),c.quiz)}

/* ---------- jenis topic: lima langkah, satu bahasa ---------- */
const MK_RE=/«(\w+)\|([^»]*)»/g;
const strip=code=>code.replace(/«\w+\|([^»]*)»/g,'$1');
function markHL(code,lang,keys){
  let out='',last=0,m;MK_RE.lastIndex=0;
  while((m=MK_RE.exec(code))){const i=keys.indexOf(m[1]);
    out+=hl(code.slice(last,m.index),lang)+`<span class="mk" data-k="${m[1]}" style="--mc:var(--m${i%6})" tabindex="0" role="button" aria-label="Bagian ${i+1}">${hl(m[2],lang)}<sup>${i+1}</sup></span>`;last=MK_RE.lastIndex}
  return out+hl(code.slice(last),lang);
}
const traceSteps=tp=>typeof tp.trace==='function'?tp.trace():tp.trace;
function tracerFrames(tp,L){
  let mem={},out='';
  return traceSteps(tp).filter(s=>!s.only||s.only===L).map(s=>{
    mem={...mem};const chg=new Set();
    [...(s.d||[]),...(s['d'+L]||[])].forEach(k=>delete mem[k]);
    for(const src of [s.s,s['s'+L]])if(src)for(const k in src){mem[k]=src[k];chg.add(k)}
    const o=(s.o||'')+(s['o'+L]||'');out+=o;
    return {line:s[L],mem,chg,out,fresh:!!o,note:esc(s['n'+L]||s.n||'')};
  });
}
function prim(v,L){if(v===null||v===undefined)return L==='j'?'null':'None';if(typeof v==='boolean')return L==='j'?String(v):(v?'True':'False');const s=String(v);if(L==='p'&&s==='null')return 'None';return s}
function rv(v,L){
  const P=x=>esc(prim(x,L));
  if(v===null||typeof v!=='object')return P(v);
  const hs=h=>new Set(h==null?[]:[].concat(h));
  const cells=(arr,cls=()=>'',lab=i=>i)=>arr.length?`<div class="cells sm">${arr.map((x,i)=>`<div class="cell ${cls(i)}"><span class="ix">${lab(i)}</span>${P(x)}</div>`).join('')}</div>`:'<span class="mempty">(kosong)</span>';
  if(Array.isArray(v))return cells(v);
  if(v.arr){const H=hs(v.hl),lo=v.lo??0,hi=v.hi??v.arr.length-1;
    return (v.ref?`<span class="ref">→ menunjuk objek ${esc(v.ref)}</span>`:'')
      +cells(v.arr,i=>[H.has(i)?'hl':'',(i<lo||i>hi)?'dim':'',v.used!=null&&i>=v.used?'empty':'',v.done!=null&&i<v.done?'sorted':''].join(' '))
      +(v.lo!=null?`<span class="ref">${lo<=hi?`wilayah pencarian: indeks ${lo} sampai ${hi}`:'wilayah pencarian kosong'}</span>`:'')
      +(v.used!=null?`<span class="ref">terpakai: ${v.used} dari ${v.arr.length}</span>`:'');}
  if(v.str!=null){const H=hs(v.hl);return cells([...v.str].map(ch=>ch===' '?'␣':ch),i=>H.has(i)?'hl':'')}
  if(v.obj){const e=Object.entries(v.obj);return e.length?`<div class="ofields">${e.map(([k,x])=>`<span><i>${esc(k)}</i> = ${P(x)}</span>`).join('')}</div>`:'<span class="mempty">(objek baru, belum ada field)</span>'}
  if(v.map){const e=Object.entries(v.map);return e.length?`<div class="ofields">${e.map(([k,x])=>`<span class="${k===v.hl?'hl':''}"><i>"${esc(k)}"</i> → ${P(x)}</span>`).join('')}</div>`:'<span class="mempty">{ } kosong</span>'}
  if(v.set)return v.set.length?`<div class="ofields">${v.set.map(x=>`<span>${P(x)}</span>`).join('')}</div>`:'<span class="mempty">(himpunan kosong)</span>';
  if(v.chain)return `<div class="ll sm">${v.chain.map((x,i)=>`<div class="lnode ${i===v.at?'hl':''}"><span>${P(x)}</span><span>next</span></div><span class="ptr">→</span>`).join('')}<span class="ptr">${L==='j'?'null':'None'}</span></div>`;
  if(v.buckets)return `<div class="buckets">${v.buckets.map((b,i)=>`<div class="bucket ${i===v.hit?'hit':''}"><span class="bi">[${i}]</span><div class="chain">${b.map((x,k)=>`<span class="tok ${k>0?'col':''}">${P(x)}</span>`).join('')}</div></div>`).join('')}</div>`;
  if(v.stack)return cells(v.stack,()=>'',i=>i===v.stack.length-1?'atas':'');
  if(v.queue)return cells(v.queue,()=>'',i=>i===0?'depan':(i===v.queue.length-1?'belakang':''));
  return esc(JSON.stringify(v));
}
function drawTrace(stage,f,tp,L){
  const lang=L==='j'?'java':'python',lines=strip(tp[lang]).split('\n'),mem=Object.entries(f.mem);
  stage.innerHTML=`<div class="tracer">
   <div class="pane ${lang}"><div class="pane-h"><span>${lang.toUpperCase()}</span><span class="tl-hint">${f.line?`baris ${f.line} sedang dijalankan`:''}</span></div>
    <ol class="tlines">${lines.map((ln,i)=>`<li class="${f.line===i+1?'cur':''}"><span class="ln">${i+1}</span><span>${hl(ln,lang)||' '}</span></li>`).join('')}</ol></div>
   <div class="tside"><div><div class="eyebrow">Memori</div><div class="mem">${mem.length?mem.map(([k,[t,v]])=>{const ts=t.split('|');const wide=v!==null&&typeof v==='object';
      return `<div class="mbox ${f.chg.has(k)?'chg':''} ${wide?'wide':''}"><div class="mh"><span class="mn">${esc(k)}</span><span class="mt">${esc(L==='j'?ts[0]:(ts[1]??ts[0]))}</span></div><div class="mv">${rv(v,L)}</div></div>`}).join(''):'<span class="mempty">Belum ada variabel di memori.</span>'}</div></div>
    <div><div class="eyebrow">Keluaran</div><div class="console ${f.fresh?'fresh':''}">${esc(f.out)}</div></div></div></div>`;
}
const topicOf=ref=>{const [n,i]=ref.split('.').map(Number);return {n,i,tp:TOPICS[n][i]}};
function topicHTML1(ref,lang){
  const {n,i,tp}=topicOf(ref),keys=Object.keys(tp.legend),J=lang==='java',ord=perm(tp.ex.o.length,n*10+i),p=PROJ[ref],R2=RUMUS[ref];
  const pyCell=s=>s.startsWith('(')?`<span class="c">${esc(s)}</span>`:hl(s,'python');
  const o=p&&(J?p.oj:p.op);
  return `<div class="steps" role="list">${['Kalimat → kode','Anatomi','Eksekusi','Rumus','Mini project'].map((x,k)=>`<button role="listitem" data-ph="${k}"><span>${k+1}</span>${x}</button>`).join('')}</div>
  <article class="phase"><header class="ph-h"><span class="ph-n">1</span><div><h3>Dari kalimat ke kode</h3><p>Tulis dulu maksudmu dalam bahasa sehari-hari. Setiap kalimat menjadi satu baris kode.</p></div></header>
   <div class="trt one"><div class="trr th"><div>Kalimat manusia</div><div class="${J?'j':'p'}">${J?'Java':'Python'}</div></div>
    ${tp.tr.map(r=>`<div class="trr"><div class="trs">${esc(r[0])}</div><pre class="trc" data-l="${J?'Java':'Python'}">${J?hl(r[1],'java'):pyCell(r[2])}</pre></div>`).join('')}</div>
   <div class="ex"><div><span class="eyebrow">Giliranmu menerjemahkan</span><p class="exq">“${esc(tp.ex.q)}”</p></div>
    <div class="exo">${ord.map(oi=>`<button class="opt code-opt" data-o="${oi}"><pre>${hl(tp.ex.o[oi][J?0:1],lang)}</pre></button>`).join('')}</div><p class="why" hidden></p></div></article>
  <article class="phase" id="anat"><header class="ph-h"><span class="ph-n">2</span><div><h3>Anatomi kode</h3><p>Klik bagian kode yang bernomor, atau klik istilah di daftar, untuk melihat bagian mana yang dimaksud.</p></div></header>
   <div class="pane ${lang}"><div class="pane-h"><span>${J?'JAVA':'PYTHON'}</span></div><pre class="code">${markHL(tp[lang],lang,keys)}</pre></div>
   <ol class="legend">${keys.map((k,q)=>{const [id,d]=tp.legend[k],g=GLMAP[id];return `<li style="--mc:var(--m${q%6})" data-k="${k}"><button class="lg" data-k="${k}"><span class="badge">${q+1}</span><span><b>${g?g.t:id}</b>${g?` <small>${g.en}</small>`:''}<span class="ld">${esc(d)}</span></span></button><button class="glink" data-term="${id}" title="Buka di glosarium">Glosarium</button></li>`}).join('')}</ol></article>
  <article class="phase"><header class="ph-h"><span class="ph-n">3</span><div><h3>Eksekusi baris demi baris</h3><p>Garis kuning adalah baris yang sedang dijalankan. Kotak hijau di memori berarti nilainya baru saja berubah.</p></div></header><div id="trHost" class="trhost"></div></article>
  <article class="phase"><header class="ph-h"><span class="ph-n">4</span><div><h3>Rumus praktis</h3><p>Pola sintaks yang dipakai programmer. Ganti kata seperti <code>type</code>, <code>name</code>, dan <code>value</code> dengan milikmu sendiri.</p></div></header>
   ${pane(lang,R2[J?0:1],{copy:false})}<ul class="rl">${tp.rumus.i.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></article>
  ${p?`<article class="phase" id="proj"><header class="ph-h"><span class="ph-n">5</span><div><h3>Mini project: ${esc(p.t)}</h3><p>Kerjakan sendiri dulu di editor atau IDE kamu. Buka solusi hanya untuk mencocokkan.</p></div></header>
   <p class="pj-s">${esc(p.s)}</p>
   ${p.file?`<div><div class="eyebrow">Isi file ${esc(p.file[0])}</div><div class="console">${esc(p.file[1])}</div></div>`:''}
   ${p.inp?`<div><div class="eyebrow">Contoh input dari pengguna</div><div class="console">${esc(p.inp)}</div></div>`:''}
   <div><div class="eyebrow">Langkah dari kalimat ke kode</div><ol class="rl">${p.l.map(s=>`<li>${esc(s)}</li>`).join('')}</ol></div>
   <div><div class="eyebrow">Keluaran yang diharapkan</div><div class="console">${esc(o)}</div></div>
   <button class="btn primary pj-tg" aria-expanded="false" aria-controls="pjSol">Tampilkan solusi</button>
   <div id="pjSol" hidden>${pane(lang,p[lang])}</div></article>`:''}`;
}
function activateMark(root,k,scroll){
  const box=$('#anat',root);if(!box)return;
  const on=k&&!box.querySelector(`.legend li[data-k="${k}"].on`);
  box.querySelectorAll('.mk,.legend li').forEach(e=>e.classList.toggle('on',on&&e.dataset.k===k));
  box.classList.toggle('has-active',!!on);
  if(on&&scroll){const m=box.querySelector(`.mk[data-k="${k}"]`)||box.querySelector(`.legend li[data-k="${k}"]`);m.scrollIntoView({block:'center',behavior:'smooth'})}
}
function wireTopic1(ref,lang){
  const {tp}=topicOf(ref),host=$('.l-body'),L=lang==='java'?'j':'p';
  player($('#trHost'),tracerFrames(tp,L),(st,f)=>drawTrace(st,f,tp,L),{speed:1500});
  const ex=$('.ex',host);
  ex.addEventListener('click',e=>{const b=e.target.closest('.opt');if(!b||b.disabled)return;const pick=+b.dataset.o;
    ex.querySelectorAll('.opt').forEach(x=>{x.disabled=true;const o=+x.dataset.o;if(o===tp.ex.a)x.classList.add('right');else if(o===pick)x.classList.add('wrong')});
    const w=$('.why',ex);w.hidden=false;w.innerHTML=(pick===tp.ex.a?'<b class="okc">Tepat.</b> ':'<b class="badc">Belum tepat.</b> ')+esc(tp.ex.w)});
  const an=$('#anat',host);
  an.addEventListener('click',e=>{const m=e.target.closest('.mk,.lg');if(m)activateMark(host,m.dataset.k,false)});
  an.addEventListener('keydown',e=>{const m=e.target.closest('.mk');if(m&&(e.key==='Enter'||e.key===' ')){e.preventDefault();activateMark(host,m.dataset.k,false)}});
  const pj=$('#proj',host);
  if(pj)pj.addEventListener('click',e=>{const tg=e.target.closest('.pj-tg');if(!tg)return;const sol=$('#pjSol',pj),show=sol.hidden;sol.hidden=!show;tg.setAttribute('aria-expanded',show);tg.textContent=show?'Sembunyikan solusi':'Tampilkan solusi';tg.classList.toggle('primary',!show)});
  $('.steps',host).addEventListener('click',e=>{const b=e.target.closest('[data-ph]');if(b)host.querySelectorAll('.phase')[+b.dataset.ph].scrollIntoView({behavior:'smooth',block:'start'})});
  if(pendingFocus){const k=pendingFocus.k;pendingFocus=null;setTimeout(()=>{activateMark(host,k,true);an.classList.add('flash');setTimeout(()=>an.classList.remove('flash'),2200)},60)}
}
