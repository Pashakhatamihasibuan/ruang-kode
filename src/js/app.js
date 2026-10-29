/* ===================== APLIKASI LMS =====================
   Tiga jalur (Java, Python, SQL) mengikuti roadmap.sh. Rute:
   #beranda, #java|#python|#sql (halaman jalur), #java-M-L (pelajaran),
   #kuis[-java|-python|-sql], #glosarium. Rute lama #bab-N dialihkan. */
const TRACKS=[
  {k:'java',name:'Java',lang:'java',mods:JAVA_MODULES,road:'https://roadmap.sh/java',mark:'J',
   h:'Java dari nol sampai siap kerja',d:'Bahasa bertipe statis yang menjalankan aplikasi Android, sistem perbankan, dan backend skala besar. Dari variabel dan OOP sampai koleksi, konkurensi, JDBC, dan Spring Boot.'},
  {k:'python',name:'Python',lang:'python',mods:PY_MODULES,road:'https://roadmap.sh/python',mark:'Py',
   h:'Python yang rapi dan idiomatik',d:'Bahasa yang ringkas untuk otomasi, data, AI, dan web. Dari sintaks dasar dan struktur data bawaan sampai type hints, testing, asyncio, dan framework web.'},
  {k:'sql',name:'SQL',lang:'sql',mods:SQL_MODULES,road:'https://roadmap.sh/sql',mark:'SQL',
   h:'SQL untuk aplikasi dan analisis data',d:'Bahasa untuk berbicara dengan basis data. Tulis dan jalankan query sungguhan di konsol bawaan, dari SELECT pertama sampai JOIN, transaksi, index, dan window function.'}];
const TK=Object.fromEntries(TRACKS.map(t=>[t.k,t]));
const LVL4=['Pemula','Menengah','Lanjutan','Profesional'];
const KIND={lab:'Konsep & lab',topic:'Topik 5 langkah',c:'Konsep & kode',s:'Praktik SQL'};
const MIN={lab:15,topic:12,c:8,s:10};
const lid=(tk,mi,li)=>`${tk}-${mi+1}-${li+1}`;
function lessonTitle(l){if(l.k==='lab')return CH[l.n-1].t;if(l.k==='topic'){const [n,i]=l.ref.split('.').map(Number);return TOPICS[n][i].t}return l.t}
const FLAT=Object.fromEntries(TRACKS.map(t=>[t.k,t.mods.flatMap((m,mi)=>m.lessons.map((l,li)=>({t,m,mi,l,li,id:lid(t.k,mi,li),title:lessonTitle(l)})))]));
const BYID=Object.fromEntries(Object.values(FLAT).flat().map((x,i)=>[x.id,x]));
const hours=t=>Math.round(FLAT[t.k].reduce((a,x)=>a+MIN[x.l.k],0)/60);

/* ---------- progres ---------- */
const LMS=store.get('rk-lms',null)||(()=>{const s={done:{},last:{}};
  const old=store.get('rk-done',[]);old.forEach(n=>['java','python'].forEach(tk=>{const x=FLAT[tk].find(y=>y.l.k==='lab'&&y.l.n===n);if(x)s.done[x.id]=1}));return s})();
LMS.done=LMS.done||{};LMS.last=LMS.last||{};
const saveLms=()=>store.set('rk-lms',LMS);
function prog(tk){const F=FLAT[tk];const d=F.filter(x=>LMS.done[x.id]).length;return {d,n:F.length,p:F.length?d/F.length:0}}
function nextOf(tk){const F=FLAT[tk];return F.find(x=>!LMS.done[x.id])||F[0]}
function resumeOf(tk){const l=BYID[LMS.last[tk]];return l&&!LMS.done[l.id]?l:nextOf(tk)}
function modProg(tk,mi){const F=FLAT[tk].filter(x=>x.mi===mi);return {d:F.filter(x=>LMS.done[x.id]).length,n:F.length}}

/* ---------- komponen kecil ---------- */
const ring=(p,size=56)=>{const r=size/2-4,c=2*Math.PI*r;return `<svg class="ring" viewBox="0 0 ${size} ${size}" width="${size}" height="${size}" aria-hidden="true"><circle cx="${size/2}" cy="${size/2}" r="${r}" class="rb"/><circle cx="${size/2}" cy="${size/2}" r="${r}" class="rf" style="stroke-dasharray:${c};stroke-dashoffset:${c*(1-p)}"/></svg>`};
function pane(lang,code,o={}){
  const lab=o.label||(lang==='java'?'JAVA':lang==='python'?'PYTHON':lang==='sql'?'SQL':'TERMINAL');
  return `<div class="pane ${lang==='java'||lang==='python'?lang:'tx'}"><div class="pane-h"><span>${lab}</span>${o.copy!==false?'<button class="copy" data-copy>Salin</button>':''}</div><pre class="code">${hl(code,lang)}</pre>${o.out?`<pre class="out">${esc(o.out)}</pre>`:''}</div>`;
}
function copyFrom(b){const pre=b.closest('.pane').querySelector('pre.code');const txt=pre.textContent;
  const sel=()=>{const r=document.createRange();r.selectNodeContents(pre);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Tekan Ctrl+C'};
  try{navigator.clipboard.writeText(txt).then(()=>{b.textContent='Tersalin';setTimeout(()=>b.textContent='Salin',1400)},sel)}catch(e){sel()}}
const nodesHTML=n=>n&&n.length?`<div class="l-nodes"><span>Topik roadmap</span>${n.map(x=>`<span class="rn">${esc(x)}</span>`).join('')}</div>`:'';

/* kuis pilihan ganda: items = [{q,o,a,w}] */
function quizHTML(items,seed){
  return `<div class="quiz">${items.map((q,qi)=>{const ord=perm(q.o.length,seed*13+qi);return `<div class="q" data-q="${qi}"><b>${qi+1}. ${q.q}</b><div class="opts">${ord.map(oi=>`<button class="opt" data-o="${oi}">${q.o[oi]}</button>`).join('')}</div><p class="why" hidden></p></div>`}).join('')}</div>`;
}
function wireQuiz(root,items){
  root.querySelectorAll('.quiz .q').forEach(qe=>qe.addEventListener('click',e=>{
    const b=e.target.closest('.opt');if(!b||b.disabled)return;const q=items[+qe.dataset.q],pick=+b.dataset.o;
    qe.querySelectorAll('.opt').forEach(x=>{x.disabled=true;const o=+x.dataset.o;if(o===q.a)x.classList.add('right');else if(o===pick)x.classList.add('wrong')});
    const w=$('.why',qe);w.hidden=false;w.innerHTML=(pick===q.a?'<b class="okc">Benar.</b> ':'<b class="badc">Belum tepat.</b> ')+q.w;
    qe.classList.add(pick===q.a?'is-ok':'is-bad');
  }));
}
function perm(n,seed){const a=[...Array(n).keys()];let s=(seed*7919+13)%233280;for(let i=n-1;i>0;i--){s=(s*9301+49297)%233280;const j=Math.floor(s/233280*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}

/* ===================== BERANDA ===================== */
const HERO=[
  ['java','Java',`String nama = "Sinta";\nint umur = 21;\nSystem.out.println("Halo, " + nama + "!");`,'Halo, Sinta!'],
  ['python','Python',`nama = "Sinta"\nhobi = ["kopi", "buku"]\nprint(f"Halo, {nama}! Suka {hobi[0]}?")`,'Halo, Sinta! Suka kopi?'],
  ['sql','SQL',`SELECT nama, kota\nFROM pelanggan\nWHERE kota = 'Jakarta';`,null]];
function renderHome(){
  const started=TRACKS.filter(t=>prog(t.k).d>0||LMS.last[t.k]);
  const nL=Object.values(FLAT).flat().length;
  return `<section class="h-hero">
    <div class="h-copy">
      <div class="eyebrow">Akademi pemrograman berbahasa Indonesia · kurikulum mengikuti roadmap.sh</div>
      <h1>Belajar <em class="j">Java</em>, <em class="p">Python</em>, dan <em class="s">SQL</em> sambil melihat kodenya bekerja.</h1>
      <p class="lead">Tiga jalur terstruktur dari nol sampai tingkat profesional. ${nL} pelajaran, visual yang bergerak langkah demi langkah, dan konsol SQL yang berjalan langsung di browser.</p>
      <div class="cta">${started.length?`<a class="btn primary lg" href="#${resumeOf(started[0].k).id}">Lanjutkan ${started[0].name} ▶</a>`:'<button class="btn primary lg" data-to="#jalur">Pilih jalur belajar ▼</button>'}<a class="tlink" href="#kuis">Kuis cerita</a><a class="tlink" href="#glosarium">Glosarium</a></div>
    </div>
    <div class="h-demo" id="hDemo" aria-label="Contoh kode">
      <div class="h-tabs">${HERO.map((h,i)=>`<button data-h="${i}" class="${h[0]}" aria-pressed="${i===0}">${h[1]}</button>`).join('')}</div>
      <div class="h-body"></div>
    </div>
  </section>
  ${started.length?`<section class="section"><div class="sec-h"><h2>Lanjutkan belajar</h2></div><div class="resume">${started.map(t=>{const x=resumeOf(t.k),p=prog(t.k);return `<a class="rcard t-${t.k}" href="#${x.id}"><span class="tmark">${t.mark}</span><span class="rc-t"><small>${t.name} · Modul ${x.mi+1}</small><b>${esc(x.title)}</b></span><span class="rc-p">${Math.round(p.p*100)}%</span></a>`}).join('')}</div></section>`:''}
  <section class="section" id="jalur"><div class="sec-h"><div class="eyebrow">Tiga jalur, satu tempat</div><h2>Pilih jalur belajarmu</h2><p>Setiap jalur tersusun dalam modul berurutan, dari Pemula sampai Profesional. Kerjakan berurutan, atau lompat ke modul yang kamu butuhkan.</p></div>
   <div class="tcards">${TRACKS.map(t=>{const p=prog(t.k);return `<article class="tcard t-${t.k}">
     <div class="tc-top"><span class="tmark lg">${t.mark}</span><div class="tc-ring">${ring(p.p)}<span>${Math.round(p.p*100)}%</span></div></div>
     <h3>${t.name}</h3><p class="tc-h">${t.h}</p><p class="tc-d">${t.d}</p>
     <ul class="tc-stats"><li><b>${t.mods.length}</b> modul</li><li><b>${FLAT[t.k].length}</b> pelajaran</li><li><b>±${hours(t)}</b> jam</li></ul>
     <div class="tc-lv">${LVL4.filter(L=>t.mods.some(m=>m.lvl===L)).map(L=>`<span>${L}</span>`).join('')}</div>
     <div class="tc-act"><a class="btn primary" href="#${t.k}">${p.d?'Lanjutkan jalur':'Lihat kurikulum'}</a>${p.d?'':`<a class="tlink" href="#${FLAT[t.k][0].id}">Mulai pelajaran 1</a>`}</div></article>`}).join('')}</div></section>
  <section class="section"><div class="sec-h"><div class="eyebrow">Metode</div><h2>Cara belajar di sini</h2></div>
   <ol class="method">${[['Baca konsep singkat','Penjelasan pendek dengan bahasa sehari-hari, langsung ke inti.'],['Tonton kodenya bekerja','Visual bergerak menunjukkan apa yang terjadi di memori, di call stack, atau di dalam database.'],['Coba sendiri','Ubah kode, jalankan query di konsol SQL, dan kerjakan mini project.'],['Uji pemahaman','Kuis di setiap pelajaran, tantangan SQL yang dinilai otomatis, dan kuis cerita.']].map((m,i)=>`<li><span>${i+1}</span><b>${m[0]}</b><p>${m[1]}</p></li>`).join('')}</ol></section>
  <section class="section"><div class="sec-h"><h2>Bingung mulai dari mana?</h2></div>
   <div class="advice"><div><b>Belum pernah memprogram</b><p>Mulai dari <a href="#python">Python</a>. Sintaksnya ringkas, jadi kamu fokus ke cara berpikir.</p></div>
   <div><b>Ingin kerja di backend atau Android</b><p>Ambil <a href="#java">Java</a>. Disiplin tipe datanya membentuk kebiasaan yang baik.</p></div>
   <div><b>Bekerja dengan data atau laporan</b><p>Ambil <a href="#sql">SQL</a>. Bisa dipelajari bersamaan dengan Java atau Python.</p></div></div></section>
  <section class="section"><div class="more2"><a class="mcard" href="#kuis"><span class="eyebrow">Latihan</span><b>Kuis cerita</b><p>${STORIES.length+SQL_STORIES.length} soal berbentuk cerita sehari-hari, kodenya bisa disembunyikan.</p></a>
   <a class="mcard" href="#glosarium"><span class="eyebrow">Kamus</span><b>Glosarium</b><p>${GL.length} istilah pemrograman dan basis data dengan padanan bahasa Inggrisnya.</p></a></div></section>`;
}
function wireHome(){
  const box=$('#hDemo');if(!box)return;let i=0;
  const show=k=>{i=k;const [lang,,code,out]=HERO[k];box.querySelectorAll('[data-h]').forEach(b=>b.setAttribute('aria-pressed',+b.dataset.h===k));
    let res=out?`<pre class="out">${esc(out)}</pre>`:'';
    if(!out){try{const r=SQLE.exec(SQLE.create(SEED.toko),code)[0];res=`<div class="h-res">${rtable(r.cols,r.rows.map(v=>({v})))}</div>`}catch(e){}}
    $('.h-body',box).innerHTML=`<pre class="code">${code.split('\n').map((ln,j)=>`<span class="ln" style="--d:${j}">${hl(ln,lang)||' '}</span>`).join('\n')}</pre><div class="h-out" style="--d:${code.split('\n').length}">${res}</div>`};
  box.addEventListener('click',e=>{const b=e.target.closest('[data-h]');if(b){show(+b.dataset.h);clearInterval(t)}});
  show(0);const t=setInterval(()=>show((i+1)%HERO.length),5200);TIMERS.push(t);
}

/* ===================== HALAMAN JALUR ===================== */
let lvFilter='Semua';
function renderCourse(t){
  const p=prog(t.k),nx=resumeOf(t.k);
  return `<header class="c-hero t-${t.k}">
    <nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>${t.name}</span></nav>
    <div class="c-grid"><div>
      <div class="eyebrow">Jalur ${t.name} · <a href="${t.road}" target="_blank" rel="noopener">mengikuti roadmap.sh/${t.k}</a></div>
      <h1>${t.h}</h1><p class="lead">${t.d}</p>
      <ul class="tc-stats"><li><b>${t.mods.length}</b> modul</li><li><b>${p.n}</b> pelajaran</li><li><b>±${hours(t)}</b> jam belajar</li></ul>
    </div>
    <div class="c-prog"><div class="tc-ring big">${ring(p.p,112)}<span>${Math.round(p.p*100)}%</span></div><p>${p.d} dari ${p.n} pelajaran selesai</p>
      <a class="btn primary" href="#${nx.id}">${p.d?'Lanjutkan':'Mulai belajar'} ▶</a><small>${p.d?'Berikutnya: ':'Pelajaran pertama: '}${esc(nx.title)}</small></div></div>
  </header>
  <div class="c-tools"><div class="chips" role="group" aria-label="Saring tingkat" id="lvF">${['Semua',...LVL4.filter(L=>t.mods.some(m=>m.lvl===L))].map(L=>`<button class="chip" data-l="${L}" aria-pressed="${L===lvFilter}">${L}</button>`).join('')}</div>
   <button class="tlink" id="expAll">Buka semua modul</button></div>
  <ol class="road t-${t.k}" id="road">${t.mods.map((m,mi)=>{const mp=modProg(t.k,mi),cur=nx.mi===mi;
    return `<li class="mod ${mp.d===mp.n?'full':''} ${cur?'cur':''}" data-lvl="${m.lvl}" ${lvFilter!=='Semua'&&m.lvl!==lvFilter?'hidden':''}>
     <div class="mod-rail"><span class="mod-dot">${mp.d===mp.n?'✓':mi+1}</span></div>
     <div class="mod-card"><div class="mod-top"><span class="eyebrow">Modul ${mi+1} · ${m.lvl}</span><span class="mod-p">${mp.d}/${mp.n}</span></div>
      <h3>${m.t}</h3><p>${m.d}</p>
      <div class="mod-bar"><i style="width:${mp.d/mp.n*100}%"></i></div>
      <details ${cur?'open':''}><summary>${mp.n} pelajaran · ±${m.lessons.reduce((a,l)=>a+MIN[l.k],0)} menit</summary>
       <ol class="les-list">${FLAT[t.k].filter(x=>x.mi===mi).map(x=>`<li><a href="#${x.id}" class="${LMS.done[x.id]?'done':''} ${x.id===nx.id?'next':''}"><span class="chk" aria-hidden="true"></span><span class="lt">${esc(x.title)}</span><small>${KIND[x.l.k]}</small></a></li>`).join('')}</ol>
       <div class="mod-nodes">${m.nodes.map(x=>`<span class="rn">${esc(x)}</span>`).join('')}</div></details></div></li>`}).join('')}</ol>`;
}
function wireCourse(t){
  $('#lvF').addEventListener('click',e=>{const b=e.target.closest('[data-l]');if(!b)return;lvFilter=b.dataset.l;
    $('#lvF').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));
    document.querySelectorAll('#road .mod').forEach(li=>li.hidden=lvFilter!=='Semua'&&li.dataset.lvl!==lvFilter)});
  $('#expAll').onclick=e=>{const ds=document.querySelectorAll('#road details'),open=![...ds].every(d=>d.open);ds.forEach(d=>d.open=open);e.target.textContent=open?'Tutup semua modul':'Buka semua modul'};
  reveal(document.querySelectorAll('#road .mod'));
}
function reveal(els){
  if(RM()||!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return}
  const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}}),{rootMargin:'0px 0px -6% 0px'});
  els.forEach((e,i)=>{e.style.setProperty('--i',i%6);e.classList.add('rv');io.observe(e)});
}

/* ===================== HALAMAN PELAJARAN ===================== */
function renderOutline(x){
  const t=x.t,p=prog(t.k);
  return `<div class="ol-head"><a class="ol-t t-${t.k}" href="#${t.k}"><span class="tmark">${t.mark}</span><span><b>Jalur ${t.name}</b><small>${p.d} dari ${p.n} selesai</small></span></a><div class="bar"><i style="width:${p.p*100}%"></i></div></div>
  <nav class="ol-nav" aria-label="Daftar materi ${t.name}">${t.mods.map((m,mi)=>{const mp=modProg(t.k,mi);return `<details ${mi===x.mi?'open':''}><summary><span class="ol-n">${mp.d===mp.n?'✓':mi+1}</span><span>${m.t}</span><small>${mp.d}/${mp.n}</small></summary>
    <ol>${FLAT[t.k].filter(y=>y.mi===mi).map(y=>`<li><a href="#${y.id}" class="${LMS.done[y.id]?'done':''}" ${y.id===x.id?'aria-current="page"':''}><span class="chk" aria-hidden="true"></span>${esc(y.title)}</a></li>`).join('')}</ol></details>`}).join('')}</nav>`;
}
function renderLesson(x){
  const {t,m,mi,l,li}=x,F=FLAT[t.k],i=F.indexOf(x),prev=F[i-1],next=F[i+1];
  let body='';
  if(l.k==='lab')body=labHTML(l.n,t.lang);
  else if(l.k==='topic')body=topicHTML1(l.ref,t.lang);
  else if(l.k==='c')body=conceptHTML(l,t);
  else body=sqlLessonHTML(l);
  return `<div class="l-top"><button class="btn ol-btn" id="olBtn" aria-controls="outline" aria-expanded="false">☰ Daftar materi</button>
   <nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><a href="#${t.k}">${t.name}</a><span>/</span><span>Modul ${mi+1}</span></nav></div>
  <header class="l-head t-${t.k}"><div class="eyebrow">Modul ${mi+1}: ${m.t} · Pelajaran ${li+1} dari ${m.lessons.length}</div>
   <h1>${esc(x.title)}</h1>
   <div class="l-meta"><span class="kchip k-${l.k}">${KIND[l.k]}</span><span>±${MIN[l.k]} menit</span><span>${m.lvl}</span>${LMS.done[x.id]?'<span class="okc">✓ Selesai</span>':''}</div>
   ${nodesHTML(l.nodes)}</header>
  <div class="l-body">${body}</div>
  <footer class="l-foot"><div class="lf-done">${LMS.done[x.id]?'<span class="okc">✓ Pelajaran ini sudah selesai.</span> <button class="tlink" id="undo">Tandai belum selesai</button>':'<span>Sudah paham? Tandai selesai untuk mencatat progresmu.</span>'}</div>
   <div class="lf-nav">${prev?`<a class="btn" href="#${prev.id}" title="${esc(prev.title)}">◀ Sebelumnya</a>`:`<a class="btn" href="#${t.k}">◀ Kurikulum</a>`}
   <button class="btn primary" id="doneNext">${next?(LMS.done[x.id]?'Lanjut':'Selesai, lanjut')+' ▶':(LMS.done[x.id]?'Kembali ke kurikulum':'Selesaikan jalur 🎉')}</button></div>
   ${next?`<a class="lf-next" href="#${next.id}"><small>Berikutnya${next.mi!==mi?` · Modul ${next.mi+1}`:''}</small><b>${esc(next.title)}</b></a>`:''}</footer>`;
}
function wireLesson(x){
  const {t,l}=x,F=FLAT[t.k],next=F[F.indexOf(x)+1];
  LMS.last[t.k]=x.id;saveLms();
  $('#olBtn').onclick=()=>toggleOutline();
  $('#doneNext').onclick=()=>{LMS.done[x.id]=1;saveLms();location.hash=next?next.id:t.k};
  const u=$('#undo');if(u)u.onclick=()=>{delete LMS.done[x.id];saveLms();route()};
  if(l.k==='lab')wireLab(l.n);
  else if(l.k==='topic')wireTopic1(l.ref,t.lang);
  else if(l.k==='c')wireConcept(l,t);
  else wireSql(l);
}
function toggleOutline(o){const ol=$('#outline');o=o??!ol.classList.contains('open');ol.classList.toggle('open',o);$('#scrim').classList.toggle('open',o);const b=$('#olBtn');if(b)b.setAttribute('aria-expanded',o)}

/* ---------- jenis lab: konsep bab + lab interaktif ---------- */
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

/* ---------- jenis c: konsep + kode + visual ---------- */
function conceptHTML(l,t){
  const lang=l.lang||t.lang,q=(l.q||[]).map(([q,o,a,w])=>({q:esc(q),o:o.map(esc),a,w:esc(w)}));
  return `<section class="prose">${l.b.map(p=>`<p>${p}</p>`).join('')}</section>
  ${l.viz&&VIZ2[l.viz]?`<section class="viz" id="lab"><div class="viz-head"><span class="eyebrow">Visual</span><h3>${VIZ2T[l.viz]}</h3><p>Tekan Berikutnya atau Putar otomatis, lalu perhatikan apa yang berubah.</p></div><div id="vizHost" class="vizhost"></div></section>`:''}
  ${l.code?`<section class="section" id="prog"><h2>${lang==='text'?'Contoh':'Contoh kode'}</h2>${pane(lang,l.code)}
   ${l.out!=null?(l.run===false?`<div><div class="eyebrow">Contoh keluaran</div><div class="console">${esc(l.out)}</div></div>`
     :`<div class="runbox"><button class="btn primary" id="runBtn">▶ Jalankan</button><span class="rb-hint">Keluaran yang dihasilkan kode ini (sudah diuji dengan ${lang==='java'?'Java 21':'Python 3.13'}).</span></div><div class="console run" id="runOut" hidden></div>`):''}</section>`:''}
  ${l.pts&&l.pts.length?`<section class="section"><h2>Poin penting</h2><ul class="points">${l.pts.map(p=>`<li>${p}</li>`).join('')}</ul></section>`:''}
  ${q.length?`<section class="section" id="quiz"><h2>Cek pemahaman</h2>${quizHTML(q,l.t.length)}</section>`:''}`;
}
function wireConcept(l,t){
  if(l.viz&&VIZ2[l.viz])VIZ2[l.viz]($('#vizHost'),{lang:t.lang,lesson:l});
  const rb=$('#runBtn');
  if(rb)rb.onclick=()=>{const box=$('#runOut');box.hidden=false;box.textContent='';rb.disabled=true;rb.textContent='Berjalan…';
    const lines=l.out.split('\n');let k=0;const step=()=>{box.textContent+=(k?'\n':'')+lines[k];k++;if(k<lines.length){TIMERS.push(setTimeout(step,RM()?0:110))}else{rb.disabled=false;rb.textContent='↻ Jalankan lagi'}};
    TIMERS.push(setTimeout(step,RM()?0:250))};
  const q=$('#quiz');if(q)wireQuiz(q,(l.q||[]).map(([qq,o,a,w])=>({q:qq,o,a,w:esc(w)})));
}

/* ---------- jenis s: pelajaran SQL dengan konsol ---------- */
function sqlLessonHTML(l){
  const q=(l.q||[]).map(([q,o,a,w])=>({q:esc(q),o:o.map(esc),a,w:esc(w)}));
  return `<nav class="toc" aria-label="Di halaman ini">${[['Konsep','.prose'],l.viz&&['Visual','#lab'],['Konsol','#sqlab'],l.task&&['Tantangan','#task'],['Kuis','#quiz']].filter(Boolean).map(([a,b])=>`<button data-to="${b}">${a}</button>`).join('')}</nav>
  <section class="prose">${l.b.map(p=>`<p>${p}</p>`).join('')}</section>
  ${l.viz&&VIZ2[l.viz]?`<section class="viz" id="lab"><div class="viz-head"><span class="eyebrow">Visual</span><h3>${VIZ2T[l.viz]}</h3><p>Tekan Berikutnya atau Putar otomatis untuk melihat database bekerja.</p></div><div id="vizHost" class="vizhost"></div></section>`:''}
  <section class="sqlab" id="sqlab"><div class="sl-head"><div><span class="eyebrow">Konsol SQL · Toko Nusantara</span><h2>Coba sendiri</h2></div><p>Pilih contoh atau tulis query sendiri. Database berjalan di browser; tekan Reset untuk kembali ke data awal.</p></div>
   <div class="sl-ex" role="group" aria-label="Contoh query">${(l.ex||[]).map(([lab],i)=>`<button class="chip" data-ex="${i}" aria-pressed="${i===0}">${esc(lab)}</button>`).join('')}</div>
   <div class="sl-grid"><div class="sl-main">
     ${editorHTML('slEd',(l.ex&&l.ex[0]?l.ex[0][1]:''),'Editor SQL')}
     <div class="sl-act"><button class="btn primary" id="slRun">▶ Jalankan <kbd>Ctrl</kbd><kbd>Enter</kbd></button><button class="btn" id="slWhy">Jelaskan langkah</button><button class="btn" id="slReset">Reset database</button></div>
     <div class="sl-out" id="slOut" aria-live="polite"></div>
     <div class="sl-steps" id="slSteps" hidden></div></div>
    <aside class="sl-schema" id="slSchema" aria-label="Skema database"></aside></div></section>
  ${l.syn?`<section class="section"><h2>Di sistem lain</h2><p class="muted">Sintaks berikut hanya untuk dibaca, karena konsol di atas tidak menjalankannya.</p>${pane(/mongo/i.test(l.syn[0])?'text':/kode aplikasi/i.test(l.syn[0])?'java':'sql',l.syn[1],{label:esc(l.syn[0]).toUpperCase()})}</section>`:''}
  ${l.task?`<section class="task" id="task"><div class="eyebrow">Tantangan · dinilai otomatis</div><h3>${l.task.q}</h3>
    ${editorHTML('tkEd','','Jawaban tantangan')}
    <div class="sl-act"><button class="btn primary" id="tkRun">Periksa jawaban</button><button class="btn" id="tkAns" aria-expanded="false">Lihat kunci jawaban</button></div>
    <div id="tkFb" aria-live="polite"></div><div id="tkKey" hidden>${pane('sql',l.task.a,{label:'KUNCI JAWABAN'})}</div></section>`:''}
  ${l.pts&&l.pts.length?`<section class="section"><h2>Poin penting</h2><ul class="points">${l.pts.map(p=>`<li>${p}</li>`).join('')}</ul></section>`:''}
  ${q.length?`<section class="section" id="quiz"><h2>Cek pemahaman</h2>${quizHTML(q,l.t.length)}</section>`:''}`;
}
function editorHTML(id,val,label){return `<div class="ed" id="${id}"><pre class="ed-hl code" aria-hidden="true">${hl(val,'sql')}\n</pre><textarea spellcheck="false" autocapitalize="off" autocomplete="off" aria-label="${label}" placeholder="Tulis query SQL di sini…">${esc(val)}</textarea></div>`}
function wireEditor(box,onRun){
  const ta=$('textarea',box),pre=$('.ed-hl',box);
  const sync=()=>{pre.innerHTML=hl(ta.value,'sql')+'\n';pre.scrollTop=ta.scrollTop;pre.scrollLeft=ta.scrollLeft;ta.style.height='auto';ta.style.height=Math.max(96,ta.scrollHeight+2)+'px';pre.style.height=ta.style.height};
  ta.addEventListener('input',sync);ta.addEventListener('scroll',()=>{pre.scrollTop=ta.scrollTop;pre.scrollLeft=ta.scrollLeft});
  ta.addEventListener('keydown',e=>{
    if((e.ctrlKey||e.metaKey)&&e.key==='Enter'){e.preventDefault();onRun()}
    else if(e.key==='Tab'&&!e.shiftKey&&!e.ctrlKey){const s=ta.selectionStart,en=ta.selectionEnd;if(s===en){e.preventDefault();ta.setRangeText('  ',s,en,'end');sync()}}});
  requestAnimationFrame(sync);
  return {get:()=>ta.value,set:v=>{ta.value=v;sync()}};
}
function resultHTML(res,ms){
  return res.map(r=>r.kind==='rows'
    ?`<div class="sl-res"><div class="sl-meta"><span>${r.rows.length} baris</span>${r.stats&&r.stats.scanned?`<span>${r.stats.scanned} baris dibaca</span>`:''}${ms!=null?`<span>${ms<1?'<1':ms.toFixed(0)} md</span>`:''}</div>${r.rows.length?rtable(r.cols,r.rows.map((v,i)=>({v,k:'q'+i})),{max:60}):'<p class="sl-empty">Query berhasil, tapi tidak ada baris yang cocok.</p>'}</div>`
    :`<div class="sl-msg ${r.warn?'warn':'ok'}">${r.warn?'⚠️':'✓'} ${esc(r.msg)}</div>`).join('');
}
function errHTML(e){
  return `${e.done&&e.done.length?resultHTML(e.done):''}<div class="sl-err" role="alert"><b>Error${e.stmt!=null&&e.done&&e.done.length?` di perintah ke-${e.stmt+1}`:''}:</b> ${esc(e.message)}${e.hint?`<p class="sl-hint">💡 ${esc(e.hint)}</p>`:''}</div>`;
}
function schemaHTML(db){
  return `<div class="eyebrow">Skema database</div>${SQLE.schema(db).map(t=>`<details ${['pelanggan','produk','pesanan'].includes(t.name)?'':''}><summary><button class="sc-t" data-tb="${esc(t.name)}" title="Masukkan SELECT * FROM ${esc(t.name)}">${t.view?'👁 ':''}${esc(t.name)}</button>${t.view?'<small>view</small>':`<small>${t.rows} baris</small>`}</summary>
    <ul>${t.cols.map(c=>`<li><span>${c.pk?'🔑 ':c.fk?'🔗 ':''}${esc(c.name)}</span><small>${esc((c.type||'').toLowerCase())}${c.fk?` → ${esc(c.fk.table)}`:''}</small></li>`).join('')}</ul></details>`).join('')}`;
}
const now=()=>performance&&performance.now?performance.now():Date.now();
function wireSql(l){
  if(l.viz&&VIZ2[l.viz])VIZ2[l.viz]($('#vizHost'),{lesson:l});
  let db=SQLE.create(SEED.toko);
  const out=$('#slOut'),steps=$('#slSteps'),sch=$('#slSchema');
  const drawSchema=()=>sch.innerHTML=schemaHTML(db);
  const ed=wireEditor($('#slEd'),run);
  function run(){steps.hidden=true;const sql=ed.get();const t0=now();
    try{const r=SQLE.exec(db,sql);out.innerHTML=resultHTML(r,now()-t0);if(r.some(x=>x.kind==='msg'))drawSchema();
      if(!RM()&&out.animate)out.animate([{opacity:.3,transform:'translateY(4px)'},{opacity:1,transform:'none'}],{duration:260,easing:'ease-out'})}
    catch(e){out.innerHTML=errHTML(e);drawSchema()}}
  $('#slRun').onclick=run;
  $('#slWhy').onclick=()=>{steps.hidden=false;sqlPipeline(steps,db,ed.get());steps.scrollIntoView({block:'nearest',behavior:RM()?'auto':'smooth'})};
  $('#slReset').onclick=()=>{db=SQLE.create(SEED.toko);drawSchema();out.innerHTML='<div class="sl-msg ok">✓ Database dikembalikan ke data awal Toko Nusantara.</div>'};
  $('.sl-ex').addEventListener('click',e=>{const b=e.target.closest('[data-ex]');if(!b)return;$('.sl-ex').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));ed.set(l.ex[+b.dataset.ex][1]);run()});
  sch.addEventListener('click',e=>{const b=e.target.closest('[data-tb]');if(!b)return;e.preventDefault();ed.set(`SELECT * FROM ${b.dataset.tb};`);run()});
  drawSchema();if(l.ex&&l.ex.length)run();
  if(l.task){
    const tk=wireEditor($('#tkEd'),check),fb=$('#tkFb');
    $('#tkRun').onclick=check;
    $('#tkAns').onclick=e=>{const k=$('#tkKey'),s=k.hidden;k.hidden=!s;e.target.setAttribute('aria-expanded',s);e.target.textContent=s?'Sembunyikan kunci':'Lihat kunci jawaban'};
    function check(){const r=gradeSql(l.task,tk.get());
      fb.innerHTML=`<div class="tk-fb ${r.ok?'ok':'bad'}" role="status"><b>${r.ok?'✓ Benar!':'Belum tepat.'}</b> ${r.msg}</div>${r.html||''}`;
      if(r.ok){const x=BYID[location.hash.slice(1)];if(x&&!LMS.done[x.id]){LMS.done[x.id]=1;saveLms();$('#outline').innerHTML=renderOutline(x)}}}
  }
  wireQuiz($('.l-body'),(l.q||[]).map(([q,o,a,w])=>({q,o,a,w:esc(w)})));
}
function gradeSql(task,sql){
  if(!sql.trim())return {ok:false,msg:'Tulis dulu query-mu di editor tantangan.'};
  const fin=s=>{const db=SQLE.create(SEED.toko);const r=SQLE.exec(db,s);return task.check?SQLE.exec(db,task.check).pop():r[r.length-1]};
  let exp,got;
  try{exp=fin(task.a)}catch(e){return {ok:false,msg:'Kunci jawaban gagal dijalankan.'}}
  try{got=fin(sql)}catch(e){return {ok:false,msg:'Query-mu menghasilkan error.',html:errHTML(e)}}
  if(got.kind!=='rows')return {ok:false,msg:'Perintah terakhirmu tidak menghasilkan tabel. Tantangan ini meminta hasil berupa baris data.'};
  const K=r=>r.map(v=>v==null?'∅':SQLE.fmt(v));
  const view=task.check?`<p class="muted">Pemeriksaan: <code>${esc(task.check)}</code></p>`:'';
  const show=resultHTML([got]);
  if(got.cols.length!==exp.cols.length)return {ok:false,msg:`Hasilmu punya ${got.cols.length} kolom, yang diminta ${exp.cols.length} kolom${task.check?'':` (${exp.cols.map(esc).join(', ')})`}.`,html:view+show};
  if(got.rows.length!==exp.rows.length)return {ok:false,msg:`Hasilmu ${got.rows.length} baris, seharusnya ${exp.rows.length} baris. Periksa lagi kondisi WHERE, JOIN, atau GROUP BY.`,html:view+show};
  const A=got.rows.map(r=>K(r).join('\u0001')),B=exp.rows.map(r=>K(r).join('\u0001'));
  const same=(x,y)=>{const a=[...x].sort(),b=[...y].sort();return a.every((v,i)=>v===b[i])};
  if(task.order){if(A.every((v,i)=>v===B[i]))return {ok:true,msg:'Isi dan urutannya tepat.',html:show};
    if(same(A,B))return {ok:false,msg:'Isinya sudah benar, tapi urutannya belum. Perhatikan ORDER BY.',html:show}}
  else if(same(A,B))return {ok:true,msg:task.check?'Perubahan datamu sesuai yang diminta.':'Hasil query-mu sama persis dengan yang diminta.',html:view+show};
  const A2=got.rows.map(r=>K(r).sort().join('\u0001')),B2=exp.rows.map(r=>K(r).sort().join('\u0001'));
  if(same(A2,B2)&&!task.order)return {ok:true,msg:'Isinya benar, hanya urutan kolomnya berbeda.',html:show};
  return {ok:false,msg:'Jumlah baris dan kolom sudah sesuai, tapi ada nilai yang berbeda. Bandingkan hasilmu dengan soal sekali lagi.',html:view+show};
}

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
  <div class="tabs3" role="tablist" aria-label="Jalur">${TRACKS.map(t=>`<a role="tab" class="t-${t.k}" href="#kuis-${t.k}" aria-selected="${t.k===tk}"><span class="tmark">${t.mark}</span>${t.name} <small>${storiesOf(t.k).length} soal</small></a>`).join('')}</div>
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
let glState={q:'',cat:'Semua',focus:null},pendingFocus=null;
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

/* ===================== NAVIGASI & RUTE ===================== */
function setNav(tk,cur){
  document.querySelectorAll('#tracks a').forEach(a=>{const on=a.dataset.tk===tk;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
  document.querySelectorAll('#gx a').forEach(a=>{if(a.dataset.r===cur)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
  document.documentElement.dataset.track=tk||'';
  moveInd(tk);
}
function moveInd(tk){const ind=$('#ind'),a=tk&&$(`#tracks a[data-tk="${tk}"]`);if(!ind)return;
  if(!a){ind.style.opacity=0;return}ind.style.opacity=1;ind.style.width=a.offsetWidth+'px';ind.style.transform=`translateX(${a.offsetLeft}px)`}
function route(){
  clearTimers();toggleOutline(false);
  let h=(location.hash||'#beranda').slice(1);
  const v=$('#view'),ol=$('#outline'),shell=$('#shell');
  const old=/^bab-(\d+)$/.exec(h);
  if(old){const x=labLesson(+old[1]);location.replace('#'+(x?x.id:'java'));return}
  if(/^kuis-(dasar|menengah|lanjutan)$/.test(h)){location.replace('#kuis-java');return}
  const focusing=!!pendingFocus;
  const x=BYID[h];
  shell.classList.toggle('has-ol',!!x);ol.hidden=!x;
  v.dataset.page=x?'lesson':TK[h]?'course':/^kuis/.test(h)?'quiz':h==='glosarium'?'glossary':'home';
  if(x){ol.innerHTML=renderOutline(x);v.innerHTML=renderLesson(x);setNav(x.t.k,'');document.title=`${x.title} · ${x.t.name} · Ruang Kode`;
    if(!focusing)scrollTo(0,0);wireLesson(x);const cur=$('#outline [aria-current="page"]');if(cur)cur.scrollIntoView({block:'center'});
    v.classList.remove('enter');void v.offsetWidth;v.classList.add('enter');return}
  if(TK[h]){v.innerHTML=renderCourse(TK[h]);setNav(h,'');wireCourse(TK[h]);document.title=`Jalur ${TK[h].name} · Ruang Kode`}
  else if(/^kuis(-(java|python|sql))?$/.test(h)){const tk=h.split('-')[1]||'java';v.innerHTML=renderStories(tk);setNav('', 'kuis');wireStories(tk);document.title='Kuis cerita · Ruang Kode'}
  else if(h==='glosarium'){v.innerHTML=renderGlossary();setNav('','glosarium');wireGlossary();document.title='Glosarium · Ruang Kode'}
  else{v.innerHTML=renderHome();setNav('','');wireHome();document.title='Ruang Kode · Akademi Java, Python & SQL'}
  v.classList.remove('enter');void v.offsetWidth;v.classList.add('enter');
  if(!(h==='glosarium'&&document.querySelector('.gl.flash')))scrollTo(0,0);
}
document.addEventListener('click',e=>{
  const c=e.target.closest('.copy[data-copy]');if(c){copyFrom(c);return}
  const tg=e.target.closest('[data-term]');if(tg&&!tg.closest('.gl')){glState={q:'',cat:'Semua',focus:tg.dataset.term};location.hash='glosarium';return}
  const b=e.target.closest('[data-to]');if(b){const t=document.querySelector(b.dataset.to);if(t)t.scrollIntoView({behavior:RM()?'auto':'smooth',block:'start'})}
});
$('#scrim').onclick=()=>toggleOutline(false);
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('#outline').classList.contains('open'))toggleOutline(false)});
addEventListener('scroll',()=>{const p=$('#rprog');if(!p)return;const d=document.documentElement,m=d.scrollHeight-innerHeight;p.style.transform=`scaleX(${m>0&&BYID[location.hash.slice(1)]?Math.min(1,scrollY/m):0})`},{passive:true});
addEventListener('resize',()=>moveInd(document.documentElement.dataset.track));
addEventListener('hashchange',route);
route();
