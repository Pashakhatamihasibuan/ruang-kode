/* ===================== RENDER ===================== */
let done=new Set(store.get('rk-done',[]));
let codeMode=store.get('rk-code','both');
let glState={q:'',cat:'Semua',focus:null};
let storyAns=store.get('rk-story',{});
let storyHide=store.get('rk-story-hide',true); // sembunyikan kode di kuis cerita
let pendingFocus=null; // {ti,k}: buka topik ti lalu tunjuk penanda k setelah bab tampil

/* urutan opsi diacak tetap (jawaban di data selalu di depan) */
function perm(n,seed){const a=[...Array(n).keys()];let s=(seed*7919+13)%233280;for(let i=n-1;i>0;i--){s=(s*9301+49297)%233280;const j=Math.floor(s/233280*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const lvlOf=b=>CH[b-1].lvl;
const slug=s=>s.toLowerCase();

/* indeks: id glosarium -> tempat istilah itu ditunjuk di kode topik */
const GLUSE={};
for(const n in TOPICS)TOPICS[n].forEach((tp,ti)=>{for(const k in tp.legend){const id=tp.legend[k][0];(GLUSE[id]=GLUSE[id]||[]);if(!GLUSE[id].some(u=>u.n==n&&u.ti===ti))GLUSE[id].push({n:+n,ti,k,t:tp.t})}});

function storyStats(lvl){const ix=STORIES.map((s,i)=>i).filter(i=>!lvl||lvlOf(STORIES[i].b)===lvl);
  const ans=ix.filter(i=>storyAns[i]!=null);return {total:ix.length,ans:ans.length,ok:ans.filter(i=>storyAns[i]===STORIES[i].a).length}}

function renderNav(cur){
  const st=L=>{const s=storyStats(L);return `<span class="cnt-s">${s.ok}/${s.total}</span>`};
  let h=`<div class="nav-group"><a href="#beranda" ${cur==='beranda'?'aria-current="page"':''}><span class="num">◎</span>Peta belajar</a>
   <a href="#kuis" ${cur==='kuis'?'aria-current="page"':''}><span class="num">?!</span>Kuis cerita${st()}</a>
   ${LEVELS.map(L=>`<a class="sub" href="#kuis-${slug(L.k)}" ${cur==='kuis-'+slug(L.k)?'aria-current="page"':''}>${L.k}${st(L.k)}</a>`).join('')}
   <a href="#glosarium" ${cur==='glosarium'?'aria-current="page"':''}><span class="num">Aa</span>Glosarium istilah</a></div>`;
  LEVELS.forEach(L=>{
    h+=`<div class="nav-group"><div class="eyebrow">${L.k}</div>${CH.filter(c=>c.lvl===L.k).map(c=>`<a href="#bab-${c.n}" ${cur==='bab-'+c.n?'aria-current="page"':''}><span class="num">${c.n}</span><span>${c.t}</span>${done.has(c.n)?'<span class="done-mark" aria-label="selesai">✓</span>':''}</a>`).join('')}</div>`;
  });
  $('#nav').innerHTML=h;
  $('#progTxt').textContent=`${done.size} dari ${CH.length} bab selesai`;
  $('#progBar').style.width=`${done.size/CH.length*100}%`;
}

function renderHome(){
  const peek=`public static void main(String[] args) {
    System.out.println("Halo!");
}`;
  const peekPy=`def main():
    print("Halo!")`;
  const next=CH.find(c=>!done.has(c.n))||CH[0];
  const nTopik=Object.values(TOPICS).flat().length;
  return `<section class="hero"><div>
    <div class="eyebrow">Mengikuti urutan Building Java Programs (edisi 6) &amp; Building Python Programs</div>
    <h1 style="margin-top:10px">Belajar dua bahasa, satu konsep pada satu waktu</h1>
    <p class="lead">19 bab dipecah menjadi ${nTopik} topik kecil. Di setiap topik kamu menerjemahkan kalimat sehari-hari menjadi kode, membedah setiap bagiannya, lalu menonton komputer menjalankannya baris demi baris.</p>
    <div class="row cta"><a class="btn primary" href="#bab-${next.n}" style="text-decoration:none">${done.size?'Lanjutkan':'Mulai'}: Bab ${next.n} ${next.t}</a><a class="tlink" href="#kuis">Kuis cerita · ${STORIES.length} soal</a><a class="tlink" href="#glosarium">Glosarium · ${GL.length} istilah</a></div>
  </div>
  <div class="split-card"><div class="lbl"><span class="lj">JAVA</span><span class="lp">PYTHON</span></div>
   <pre class="code" style="background:var(--code-bg)">${hl(peek,'java')}</pre><pre class="code" style="background:var(--code-bg);border-top:1px dashed #33435A">${hl(peekPy,'python')}</pre></div>
  </section>
  <section class="section"><h2>Lima langkah di setiap topik</h2><div class="how">
   <div><b>1. Dari kalimat ke kode</b>Setiap kalimat manusia diterjemahkan menjadi satu baris Java dan Python, lalu kamu mencoba sendiri.</div>
   <div><b>2. Anatomi</b>Klik bagian kode berwarna untuk melihat istilahnya: mana tipe data, mana variabel, mana kondisi.</div>
   <div><b>3. Eksekusi</b>Jalankan baris demi baris. Lihat kotak memori terisi dan keluaran muncul.</div>
   <div><b>4. Rumus praktis</b>Pola sintaks asli Java dan Python untuk menulis kode sejenis.</div>
   <div><b>5. Mini project</b>Program kecil untuk dibuat sendiri, lengkap dengan solusi yang bisa dibuka dan ditutup.</div></div></section>
  <section class="section"><h2>Peta belajar</h2><div class="path">${LEVELS.map(L=>`<div class="lvl"><h3>${L.k} <small>${CH.filter(c=>c.lvl===L.k).length} bab</small></h3><p style="color:var(--muted);font-size:.9rem">${L.d}</p><ol>${CH.filter(c=>c.lvl===L.k).map(c=>`<li><a href="#bab-${c.n}" class="${done.has(c.n)?'done':''}"><span class="num">${c.n}</span><span>${c.t}</span></a></li>`).join('')}</ol><a class="btn" href="#kuis-${slug(L.k)}" style="text-decoration:none;align-self:flex-start;margin-top:auto">Kuis cerita ${L.k}</a></div>`).join('')}</div></section>`;
}

function codePane(lang,code,out,copy=true){
  const o=out==null?'':(typeof out==='string'?out:out[lang]);
  return `<div class="pane ${lang}"><div class="pane-h"><span>${lang==='java'?'JAVA':'PYTHON'}</span>${copy?`<button class="copy" data-copy="${lang}">Salin</button>`:''}</div><pre class="code">${hl(code,lang)}</pre>${o?`<pre class="out">${esc(o)}</pre>`:''}</div>`;
}

/* ---------- topik: penanda, anatomi, pelacak ---------- */
const MK_RE=/«(\w+)\|([^»]*)»/g;
const strip=code=>code.replace(/«\w+\|([^»]*)»/g,'$1');
function markHL(code,lang,keys){
  let out='',last=0,m;MK_RE.lastIndex=0;
  while((m=MK_RE.exec(code))){
    const i=keys.indexOf(m[1]);
    out+=hl(code.slice(last,m.index),lang)+`<span class="mk" data-k="${m[1]}" style="--mc:var(--m${i%6})" tabindex="0" role="button" aria-label="Bagian ${i+1}">${hl(m[2],lang)}<sup>${i+1}</sup></span>`;
    last=MK_RE.lastIndex;
  }
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
function prim(v,L){
  if(v===null||v===undefined)return L==='j'?'null':'None';
  if(typeof v==='boolean')return L==='j'?String(v):(v?'True':'False');
  const s=String(v);
  if(L==='p'&&s==='null')return 'None';
  return s;
}
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
  const lang=L==='j'?'java':'python';
  const lines=strip(tp[lang]).split('\n');
  const mem=Object.entries(f.mem);
  stage.innerHTML=`<div class="tracer">
   <div class="pane ${lang}"><div class="pane-h"><span>${lang.toUpperCase()}</span><span class="tl-hint">${f.line?`baris ${f.line} sedang dijalankan`:''}</span></div>
    <ol class="tlines">${lines.map((ln,i)=>`<li class="${f.line===i+1?'cur':''}"><span class="ln">${i+1}</span><span>${hl(ln,lang)||' '}</span></li>`).join('')}</ol></div>
   <div class="tside"><div><div class="eyebrow">Memori</div><div class="mem">${mem.length?mem.map(([k,[t,v]])=>{const ts=t.split('|');const wide=v!==null&&typeof v==='object';
      return `<div class="mbox ${f.chg.has(k)?'chg':''} ${wide?'wide':''}"><div class="mh"><span class="mn">${esc(k)}</span><span class="mt">${esc(L==='j'?ts[0]:(ts[1]??ts[0]))}</span></div><div class="mv">${rv(v,L)}</div></div>`}).join(''):'<span class="mempty">Belum ada variabel di memori.</span>'}</div></div>
    <div><div class="eyebrow">Keluaran</div><div class="console ${f.fresh?'fresh':''}">${esc(f.out)}</div></div></div></div>`;
}

function topicHTML(c,ti){
  const tp=TOPICS[c.n][ti],keys=Object.keys(tp.legend),tps=TOPICS[c.n];
  const ord=perm(tp.ex.o.length,c.n*10+ti);
  const L=codeMode==='python'?'p':'j';
  return `<div class="steps" role="list">${['Kalimat → kode','Anatomi','Eksekusi','Rumus','Mini project'].map((l,i)=>`<button role="listitem" data-ph="${i}"><span>${i+1}</span>${l}</button>`).join('')}</div>
  <article class="phase"><header class="ph-h"><span class="ph-n">1</span><div><h3>Dari kalimat ke kode</h3><p>Tulis dulu maksudmu dalam bahasa sehari-hari. Setiap kalimat menjadi satu baris kode.</p></div></header>
   <div class="trt"><div class="trr th"><div>Kalimat manusia</div><div class="j">Java</div><div class="p">Python</div></div>
    ${tp.tr.map(r=>`<div class="trr"><div class="trs">${esc(r[0])}</div><pre class="trc" data-l="Java">${hl(r[1],'java')}</pre><pre class="trc" data-l="Python">${r[2].startsWith('(')?`<span class="c">${esc(r[2])}</span>`:hl(r[2],'python')}</pre></div>`).join('')}</div>
   <div class="ex"><div><span class="eyebrow">Giliranmu menerjemahkan</span><p class="exq">“${esc(tp.ex.q)}”</p></div>
    <div class="exo">${ord.map(oi=>{const o=tp.ex.o[oi];return `<button class="opt code-opt" data-o="${oi}"><pre data-l="Java">${hl(o[0],'java')}</pre><pre data-l="Python">${hl(o[1],'python')}</pre></button>`}).join('')}</div>
    <p class="why" hidden></p></div></article>

  <article class="phase" id="anat"><header class="ph-h"><span class="ph-n">2</span><div><h3>Anatomi kode</h3><p>Klik bagian kode yang bernomor, atau klik istilah di daftar, untuk melihat istilah mana yang dimaksud.</p></div></header>
   <div class="codes anat-codes"><div class="pane java"><div class="pane-h"><span>JAVA</span></div><pre class="code">${markHL(tp.java,'java',keys)}</pre></div><div class="pane python"><div class="pane-h"><span>PYTHON</span></div><pre class="code">${markHL(tp.python,'python',keys)}</pre></div></div>
   <ol class="legend">${keys.map((k,i)=>{const [id,d]=tp.legend[k],g=GLMAP[id];return `<li style="--mc:var(--m${i%6})" data-k="${k}"><button class="lg" data-k="${k}"><span class="badge">${i+1}</span><span><b>${g?g.t:id}</b>${g?` <small>${g.en}</small>`:''}<span class="ld">${esc(d)}</span></span></button><button class="glink" data-term="${id}" title="Buka di glosarium">Glosarium</button></li>`}).join('')}</ol></article>

  <article class="phase"><header class="ph-h"><span class="ph-n">3</span><div><h3>Eksekusi baris demi baris</h3><p>Garis kuning adalah baris yang sedang dijalankan. Kotak hijau di memori berarti nilainya baru saja berubah.</p></div></header>
   <div class="seg" role="group" aria-label="Bahasa eksekusi" id="trLang"><button data-l="j" aria-pressed="${L==='j'}">Java</button><button data-l="p" aria-pressed="${L==='p'}">Python</button></div>
   <div id="trHost" class="trhost"></div></article>

  <article class="phase"><header class="ph-h"><span class="ph-n">4</span><div><h3>Rumus praktis</h3><p>Pola sintaks yang dipakai programmer. Ganti kata seperti <code>type</code>, <code>name</code>, dan <code>value</code> dengan milikmu sendiri.</p></div></header>
   <div class="codes">${codePane('java',RUMUS[c.n+'.'+ti][0],null,false)}${codePane('python',RUMUS[c.n+'.'+ti][1],null,false)}</div><ul class="rl">${tp.rumus.i.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></article>
  ${projHTML(c,ti)}
  <div class="tnav">${ti>0?`<button class="btn" data-go="${ti-1}">◀ ${c.n}.${ti} ${tps[ti-1].t}</button>`:'<span></span>'}${ti<tps.length-1?`<button class="btn primary" data-go="${ti+1}">${c.n}.${ti+2} ${tps[ti+1].t} ▶</button>`:'<button class="btn" data-to="#lab">Lanjut ke lab interaktif ▼</button>'}</div>`;
}

function projHTML(c,ti){
  const p=PROJ[c.n+'.'+ti];if(!p)return '';
  const con=(lbl,o)=>`<div><div class="eyebrow">${lbl}</div><div class="console">${esc(o)}</div></div>`;
  return `<article class="phase" id="proj"><header class="ph-h"><span class="ph-n">5</span><div><h3>Mini project: ${esc(p.t)}</h3><p>Kerjakan sendiri dulu di editor atau IDE kamu. Buka solusi hanya untuk mencocokkan.</p></div></header>
   <p class="pj-s">${esc(p.s)}</p>
   ${p.file?`<div><div class="eyebrow">Isi file ${esc(p.file[0])}</div><div class="console">${esc(p.file[1])}</div></div>`:''}
   ${p.inp?`<div><div class="eyebrow">Contoh input dari pengguna</div><div class="console">${esc(p.inp)}</div></div>`:''}
   <div><div class="eyebrow">Langkah dari kalimat ke kode</div><ol class="rl" style="margin-top:6px">${p.l.map(x=>`<li>${esc(x)}</li>`).join('')}</ol></div>
   <div class="${p.oj===p.op?'':'grid2'}">${p.oj===p.op?con('Keluaran yang diharapkan',p.oj):con('Keluaran yang diharapkan · Java',p.oj)+con('Keluaran yang diharapkan · Python',p.op)}</div>
   <button class="btn primary pj-tg" aria-expanded="false" aria-controls="pjSol">Tampilkan solusi</button>
   <div class="codes" id="pjSol" hidden>${codePane('java',p.java)}${codePane('python',p.python)}</div></article>`;
}

function activateMark(root,k,scroll){
  const box=$('#anat',root);if(!box)return;
  const on=k&&!box.querySelector(`.legend li[data-k="${k}"].on`);
  box.querySelectorAll('.mk,.legend li').forEach(e=>e.classList.toggle('on',on&&e.dataset.k===k));
  box.classList.toggle('has-active',!!on);
  if(on&&scroll){const m=box.querySelector(`.mk[data-k="${k}"]`)||box.querySelector(`.legend li[data-k="${k}"]`);m.scrollIntoView({block:'center',behavior:'smooth'})}
}

function drawTopic(c,ti,focusK){
  const host=$('#tbody');
  document.querySelectorAll('.ttab').forEach(b=>b.setAttribute('aria-selected',+b.dataset.ti===ti));
  host.innerHTML=topicHTML(c,ti);
  const tp=TOPICS[c.n][ti];
  let L=codeMode==='python'?'p':'j';
  const pl=player($('#trHost'),tracerFrames(tp,L),(st,f)=>drawTrace(st,f,tp,L),{speed:1500});
  $('#trLang').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;L=b.dataset.l;
    $('#trLang').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));pl.set(tracerFrames(tp,L))});
  const ex=$('.ex',host);
  ex.addEventListener('click',e=>{const b=e.target.closest('.opt');if(!b||b.disabled)return;const pick=+b.dataset.o;
    ex.querySelectorAll('.opt').forEach(x=>{x.disabled=true;const o=+x.dataset.o;if(o===tp.ex.a)x.classList.add('right');else if(o===pick)x.classList.add('wrong')});
    const w=$('.why',ex);w.hidden=false;w.innerHTML=(pick===tp.ex.a?'<b style="color:var(--ok)">Tepat.</b> ':'<b style="color:var(--bad)">Belum tepat.</b> ')+esc(tp.ex.w)});
  const an=$('#anat',host);
  an.addEventListener('click',e=>{
    const g=e.target.closest('.glink');if(g){glState={q:'',cat:'Semua',focus:g.dataset.term};location.hash='glosarium';return}
    const m=e.target.closest('.mk,.lg');if(m)activateMark(host,m.dataset.k,false)});
  an.addEventListener('keydown',e=>{const m=e.target.closest('.mk');if(m&&(e.key==='Enter'||e.key===' ')){e.preventDefault();activateMark(host,m.dataset.k,false)}});
  const pj=$('#proj',host);
  if(pj){const p=PROJ[c.n+'.'+ti];pj.addEventListener('click',e=>{
    const t=e.target.closest('.pj-tg');
    if(t){const sol=$('#pjSol',pj),show=sol.hidden;sol.hidden=!show;t.setAttribute('aria-expanded',show);t.textContent=show?'Sembunyikan solusi':'Tampilkan solusi';t.classList.toggle('primary',!show);return}
    const b=e.target.closest('[data-copy]');if(!b)return;const txt=p[b.dataset.copy];
    try{navigator.clipboard.writeText(txt).then(()=>{b.textContent='Tersalin';setTimeout(()=>b.textContent='Salin',1400)},()=>{selectPre(b);b.textContent='Tekan Ctrl+C'})}catch(err){selectPre(b);b.textContent='Tekan Ctrl+C'}})}
  $('.steps',host).addEventListener('click',e=>{const b=e.target.closest('[data-ph]');if(b)host.querySelectorAll('.phase')[+b.dataset.ph].scrollIntoView({behavior:'smooth',block:'start'})});
  $('.tnav',host).addEventListener('click',e=>{const b=e.target.closest('[data-go]');if(!b)return;drawTopic(c,+b.dataset.go);$('#topics').scrollIntoView({block:'start'})});
  if(focusK){activateMark(host,focusK,true);$('#anat',host).classList.add('flash');setTimeout(()=>$('#anat')&&$('#anat').classList.remove('flash'),2200)}
}

function renderChapter(c){
  const prev=CH[c.n-2],next=CH[c.n],tps=TOPICS[c.n]||[];
  return `<header class="ch-head"><div class="eyebrow">Bab ${c.n} · ${c.lvl}</div><h1>${c.t}</h1>
   <div class="tags"><span class="tag j">Java: ${c.en}</span><span class="tag p">Python: ${c.py}</span></div></header>
  <nav class="toc" aria-label="Di halaman ini">${[['Konsep','#konsep'],tps.length&&['Topik','#topics'],['Lab','#lab'],['Program','#prog'],['Istilah','#istilah'],['Kuis','#quiz']].filter(Boolean).map(([l,t])=>`<button data-to="${t}">${l}</button>`).join('')}</nav>
  <section class="prose" id="konsep">${c.body.map(p=>`<p>${p}</p>`).join('')}</section>
  <ul class="points">${c.points.map(p=>`<li>${p}</li>`).join('')}</ul>
  ${tps.length?`<section class="topics" id="topics"><div><div class="eyebrow">Pelajari per topik</div><h2 style="margin-top:4px">${tps.length} topik di bab ini</h2></div>
   <div class="ttabs" role="tablist">${tps.map((tp,i)=>`<button class="ttab" role="tab" data-ti="${i}" aria-selected="false"><span>${c.n}.${i+1}</span>${tp.t}</button>`).join('')}</div>
   <div id="tbody" class="tbody"></div></section>`:''}
  <section class="viz" id="lab" aria-label="Visualisasi"><div class="viz-head"><h3>Lab interaktif: ${c.vizT}</h3><p>${c.vizD}</p></div><div id="vizHost" style="display:flex;flex-direction:column;gap:14px;min-width:0"></div></section>
  <section class="section" id="prog"><div class="code-tools"><h2>Program lengkap</h2><div class="seg" role="group" aria-label="Tampilan kode" id="codeSeg">
    <button data-m="both" aria-pressed="${codeMode==='both'}">Berdampingan</button><button data-m="java" aria-pressed="${codeMode==='java'}">Java</button><button data-m="python" aria-pressed="${codeMode==='python'}">Python</button></div></div>
   <div class="codes ${codeMode==='both'?'':'only-'+codeMode}" id="codes">${codePane('java',c.java,c.out)}${codePane('python',c.python,c.out)}</div></section>
  <section class="section"><h2>Java lawan Python</h2><div class="tbl"><table class="cmp"><thead><tr><th>Aspek</th><th class="j">Java</th><th class="p">Python</th></tr></thead><tbody>${c.cmp.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join('')}</tbody></table></div></section>
  <div class="tip"><b>Tip mentor.</b> ${c.tip}</div>
  <section class="section" id="istilah"><h2>Istilah di bab ini</h2><p style="color:var(--muted);font-size:.9rem">Istilah bertanda ◉ bisa ditunjukkan langsung di kode topik. Yang lain membuka glosarium.</p><div class="terms">${c.terms.map(id=>{const u=(GLUSE[id]||[]).find(x=>x.n===c.n);return `<button class="term-chip ${u?'in-code':''}" data-term="${id}">${u?'◉ ':''}${GLMAP[id].t}</button>`}).join('')}</div></section>
  <section class="section" id="quiz"><h2>Kuis cepat</h2><div class="quiz">${c.quiz.map((q,qi)=>`<div class="q" data-q="${qi}"><b>${qi+1}. ${q.q}</b><div class="opts">${q.o.map((o,oi)=>`<button class="opt" data-o="${oi}">${o}</button>`).join('')}</div><p class="why" hidden></p></div>`).join('')}</div>
   ${STORIES.some(s=>s.b===c.n)?`<a class="btn" href="#kuis-${slug(c.lvl)}" style="text-decoration:none;align-self:flex-start">Coba kuis cerita tingkat ${c.lvl} ▶</a>`:''}</section>
  <footer class="ch-foot"><label class="donebox"><input type="checkbox" id="doneBox" ${done.has(c.n)?'checked':''}> Tandai bab ini selesai</label>
   <div class="row">${prev?`<a class="btn" href="#bab-${prev.n}" style="text-decoration:none">◀ Bab ${prev.n}</a>`:''}${next?`<a class="btn primary" href="#bab-${next.n}" style="text-decoration:none">Bab ${next.n}: ${next.t} ▶</a>`:`<a class="btn primary" href="#kuis" style="text-decoration:none">Ke kuis cerita ▶</a>`}</div></footer>`;
}

function wireChapter(c){
  VIZ[c.viz]($('#vizHost'));
  if(TOPICS[c.n]){
    $('.ttabs').addEventListener('click',e=>{const b=e.target.closest('.ttab');if(b)drawTopic(c,+b.dataset.ti)});
    const pf=pendingFocus;pendingFocus=null;
    drawTopic(c,pf?pf.ti:0,pf&&pf.k);
  }
  $('#codeSeg').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;codeMode=b.dataset.m;store.set('rk-code',codeMode);
    $('#codeSeg').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));$('#codes').className='codes '+(codeMode==='both'?'':'only-'+codeMode)});
  $('#codes').addEventListener('click',e=>{const b=e.target.closest('[data-copy]');if(!b)return;const txt=c[b.dataset.copy];
    const ok=()=>{b.textContent='Tersalin';setTimeout(()=>b.textContent='Salin',1400)};
    try{navigator.clipboard.writeText(txt).then(ok,()=>{selectPre(b);b.textContent='Tekan Ctrl+C'})}catch(err){selectPre(b);b.textContent='Tekan Ctrl+C'}});
  document.querySelectorAll('.term-chip').forEach(b=>b.onclick=()=>{
    const u=(GLUSE[b.dataset.term]||[]).find(x=>x.n===c.n);
    if(u){drawTopic(c,u.ti,u.k)}else{glState={q:'',cat:'Semua',focus:b.dataset.term};location.hash='glosarium'}});
  document.querySelectorAll('.quiz .q').forEach(qe=>qe.addEventListener('click',e=>{
    const b=e.target.closest('.opt');if(!b)return;const q=c.quiz[+qe.dataset.q];const pick=+b.dataset.o;
    qe.querySelectorAll('.opt').forEach((x,i)=>{x.disabled=true;if(i===q.a)x.classList.add('right');else if(i===pick)x.classList.add('wrong')});
    const w=$('.why',qe);w.hidden=false;w.innerHTML=(pick===q.a?'<b style="color:var(--ok)">Benar.</b> ':'<b style="color:var(--bad)">Belum tepat.</b> ')+q.w;
  }));
  $('#doneBox').onchange=e=>{e.target.checked?done.add(c.n):done.delete(c.n);store.set('rk-done',[...done]);renderNav('bab-'+c.n)};
}
function selectPre(b){const pre=b.closest('.pane').querySelector('pre.code');const r=document.createRange();r.selectNodeContents(pre);const s=getSelection();s.removeAllRanges();s.addRange(r)}

/* ---------- kuis cerita ---------- */
function storyCard(s,i){
  const a=storyAns[i],ans=a!=null,ord=perm(s.o.length,i+3);
  const panes=[s.java&&codePane('java',s.java,null,false),s.python&&codePane('python',s.python,null,false)].filter(Boolean);
  return `<article class="story ${ans?(a===s.a?'is-ok':'is-bad'):''}" data-si="${i}">
   <div class="tags"><span class="tag">Bab ${s.b} · ${CH[s.b-1].t}</span><span class="tag">${lvlOf(s.b)}</span>${ans?`<span class="tag ${a===s.a?'okt':'badt'}">${a===s.a?'Benar':'Belum tepat'}</span>`:''}</div>
   <h3>${esc(s.t)}</h3><p class="st">${esc(s.s)}</p>
   ${panes.length?(()=>{const hid=storyHide&&!ans,lb=panes.length===2?'Java & Python':(s.java?'Java':'Python');
     return `<button class="btn peek" aria-expanded="${!hid}" data-lb="${lb}">${hid?'Tampilkan':'Sembunyikan'} kode (${lb})</button><div class="codes ${panes.length===1?'only-one':''}" ${hid?'hidden':''}>${panes.join('')}</div>`})():''}
   <b>${esc(s.q)}</b>
   <div class="opts">${ord.map(oi=>`<button class="opt ${ans?(oi===s.a?'right':(oi===a?'wrong':'')):''}" data-o="${oi}" ${ans?'disabled':''}>${esc(s.o[oi])}</button>`).join('')}</div>
   <p class="why" ${ans?'':'hidden'}>${ans?esc(s.w):''}</p>
   <a class="more" href="#bab-${s.b}">Pelajari lagi Bab ${s.b}: ${CH[s.b-1].t} →</a></article>`;
}
function renderStories(lvl){
  const S=storyStats(lvl);
  const list=STORIES.map((s,i)=>[s,i]).filter(([s])=>!lvl||lvlOf(s.b)===lvl);
  return `<header class="ch-head"><div class="eyebrow">Kuis cerita${lvl?' · '+lvl:''}</div><h1>Kode di kehidupan sehari-hari</h1>
   <p class="lead" style="color:var(--muted);max-width:62ch">Setiap soal adalah cerita kecil. Baca situasinya, ubah ceritanya menjadi langkah di kepalamu, lalu tebak apa yang dilakukan kodenya.</p></header>
  <div class="score"><div><span class="big">${S.ok}</span><span class="of"> / ${S.total} benar</span></div>
   <div class="sc-bar"><div class="bar"><i style="width:${S.total?S.ans/S.total*100:0}%"></i></div><small>${S.ans} dari ${S.total} sudah dijawab</small></div>
   <label class="donebox hidebox"><input type="checkbox" id="stHide" ${storyHide?'checked':''}> Sembunyikan kode</label>
   <button class="btn" id="stReset" ${S.ans?'':'disabled'}>Ulangi ${lvl?'tingkat ini':'semua'}</button></div>
  <p class="st-mode">${storyHide?'Mode baca soal: kode disembunyikan. Pahami ceritanya, lalu bayangkan sendiri programnya. Kode muncul setelah kamu menjawab.':'Kode ditampilkan di setiap soal.'}</p>
  <nav class="chips" aria-label="Tingkat"><a class="chip" href="#kuis" ${!lvl?'aria-current="page"':''}>Semua (${STORIES.length})</a>${LEVELS.map(L=>`<a class="chip" href="#kuis-${slug(L.k)}" ${lvl===L.k?'aria-current="page"':''}>${L.k} (${storyStats(L.k).total})</a>`).join('')}</nav>
  <div class="stories" id="stories">${list.map(([s,i])=>storyCard(s,i)).join('')}</div>`;
}
function wireStories(lvl,cur){
  $('#stHide').onchange=e=>{storyHide=e.target.checked;store.set('rk-story-hide',storyHide);const y=scrollY;route();scrollTo(0,y)};
  $('#stories').addEventListener('click',e=>{const pk=e.target.closest('.peek');if(pk){const cd=pk.nextElementSibling,show=cd.hidden;cd.hidden=!show;
      pk.setAttribute('aria-expanded',show);pk.textContent=`${show?'Sembunyikan':'Tampilkan'} kode (${pk.dataset.lb})`;return}
    const b=e.target.closest('.opt');if(!b||b.disabled)return;const card=b.closest('.story'),i=+card.dataset.si;
    storyAns[i]=+b.dataset.o;store.set('rk-story',storyAns);
    const tmp=document.createElement('div');tmp.innerHTML=storyCard(STORIES[i],i);card.replaceWith(tmp.firstElementChild);
    refreshScore(lvl,cur)});
  $('#stReset').onclick=()=>{STORIES.forEach((s,i)=>{if(!lvl||lvlOf(s.b)===lvl)delete storyAns[i]});store.set('rk-story',storyAns);route()};
}
function refreshScore(lvl,cur){const S=storyStats(lvl);$('.score .big').textContent=S.ok;$('.score .bar i').style.width=`${S.ans/S.total*100}%`;
  $('.score small').textContent=`${S.ans} dari ${S.total} sudah dijawab`;$('#stReset').disabled=!S.ans;renderNav(cur)}

/* ---------- glosarium ---------- */
function seenIn(id){return CH.filter(c=>c.terms.includes(id))}
function renderGlossary(){
  return `<header class="ch-head"><div class="eyebrow">Kamus</div><h1>Glosarium istilah pemrograman</h1>
  <p class="lead" style="color:var(--muted);max-width:60ch">${GL.length} istilah yang sering muncul di Java dan Python, dengan padanan bahasa Inggrisnya. Tombol "Tunjukkan di kode" membawamu ke bagian kode yang dimaksud.</p></header>
  <div class="gl-tools"><input class="gl-search" id="glq" type="search" placeholder="Cari istilah, misalnya rekursi atau polymorphism" aria-label="Cari istilah"></div>
  <div class="chips" id="glc">${['Semua',...CATS].map(k=>`<button class="chip" data-c="${k}" aria-pressed="false">${k}</button>`).join('')}</div>
  <div class="gl-list" id="gll"></div>`;
}
function drawGlossary(){
  const q=glState.q.trim().toLowerCase();
  document.querySelectorAll('#glc .chip').forEach(b=>b.setAttribute('aria-pressed',b.dataset.c===glState.cat));
  const list=GL.filter(g=>(glState.cat==='Semua'||g.c===glState.cat)&&(!q||(g.t+' '+g.en+' '+g.d).toLowerCase().includes(q))).sort((a,b)=>a.t.localeCompare(b.t,'id'));
  $('#gll').innerHTML=list.length?list.map(g=>{const s=seenIn(g.id),u=(GLUSE[g.id]||[]).slice(0,4);return `<article class="gl" id="t-${g.id}"><span class="cat">${g.c}</span><h3>${g.t}<small>${g.en}</small></h3><p>${esc(g.d)}</p>${g.ex?`<pre>${esc(g.ex)}</pre>`:''}${u.length?`<div class="show-in"><span>Tunjukkan di kode:</span>${u.map(x=>`<button class="show" data-n="${x.n}" data-ti="${x.ti}" data-k="${x.k}">${x.n}.${x.ti+1} ${x.t}</button>`).join('')}</div>`:''}${s.length?`<div class="seen">Dibahas di: ${s.map(c=>`<a href="#bab-${c.n}">Bab ${c.n}</a>`).join('')}</div>`:''}</article>`}).join(''):`<p class="empty">Tidak ada istilah yang cocok dengan "${esc(glState.q)}". Coba kata lain atau pilih kategori Semua.</p>`;
}
function wireGlossary(){
  const inp=$('#glq');inp.value=glState.q;
  inp.addEventListener('input',()=>{glState.q=inp.value;glState.focus=null;drawGlossary()});
  $('#glc').addEventListener('click',e=>{const b=e.target.closest('.chip');if(!b)return;glState.cat=b.dataset.c;drawGlossary()});
  $('#gll').addEventListener('click',e=>{const b=e.target.closest('.show');if(!b)return;pendingFocus={ti:+b.dataset.ti,k:b.dataset.k};
    const h='bab-'+b.dataset.n;if(location.hash==='#'+h)route();else location.hash=h});
  drawGlossary();
  if(glState.focus){const el=document.getElementById('t-'+glState.focus);if(el){el.classList.add('flash');el.scrollIntoView({block:'center'});setTimeout(()=>el.classList.remove('flash'),2200)}glState.focus=null}
}

function route(){
  clearTimers();closeMenu();
  const h=(location.hash||'#beranda').slice(1);
  const v=$('#view');
  const m=/^bab-(\d+)$/.exec(h),k=/^kuis(?:-(\w+))?$/.exec(h);
  const focusing=!!pendingFocus;
  if(m&&CH[+m[1]-1]){const c=CH[+m[1]-1];v.innerHTML=renderChapter(c);renderNav(h);if(!focusing)window.scrollTo(0,0);wireChapter(c);document.title=`Bab ${c.n}: ${c.t} · Ruang Kode`;return}
  if(k&&(!k[1]||LEVELS.some(L=>slug(L.k)===k[1]))){const lvl=k[1]?LEVELS.find(L=>slug(L.k)===k[1]).k:null;v.innerHTML=renderStories(lvl);renderNav(h);wireStories(lvl,h);document.title=`Kuis cerita${lvl?' '+lvl:''} · Ruang Kode`}
  else if(h==='glosarium'){v.innerHTML=renderGlossary();renderNav(h);wireGlossary();document.title='Glosarium · Ruang Kode'}
  else{v.innerHTML=renderHome();renderNav('beranda');document.title='Ruang Kode Java & Python'}
  if(!(h==='glosarium'&&document.querySelector('.gl.flash')))window.scrollTo(0,0);
}
function closeMenu(){$('#side').classList.remove('open');$('#scrim').classList.remove('open');$('#menuBtn').setAttribute('aria-expanded','false')}
$('#menuBtn').onclick=()=>{const o=!$('#side').classList.contains('open');$('#side').classList.toggle('open',o);$('#scrim').classList.toggle('open',o);$('#menuBtn').setAttribute('aria-expanded',o)};
$('#scrim').onclick=closeMenu;
document.addEventListener('click',e=>{const b=e.target.closest('[data-to]');if(!b)return;const t=document.querySelector(b.dataset.to);if(t)t.scrollIntoView({behavior:'smooth',block:'start'})});
window.addEventListener('hashchange',route);
route();
