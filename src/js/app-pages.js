/* ===================== HALAMAN: BERANDA, KATALOG, JALUR, UJIAN, SAYA, ULANG ===================== */
const tcls=t=>`t-${t.k}`;
const pct=p=>Math.round(p*100)+'%';
function trackCard(t,o={}){const p=prog(t.k);
  return `<a class="tcard2 ${tcls(t)}" href="#${t.k}"><span class="tmark">${t.mark}</span><span class="tc2-b"><b>${t.name}</b><small>${t.mods.length} modul · ${FLAT[t.k].length} pelajaran · ±${hours(t)} jam</small>${o.desc!==false?`<span class="tc2-d">${t.h}</span>`:''}</span>
   <span class="tc2-p">${p.d?`<span class="mbar"><i style="width:${p.p*100}%"></i></span><small>${pct(p.p)}</small>`:'<small class="muted">Belum mulai</small>'}</span></a>`}
const recent=()=>TRACKS.filter(t=>LMS.last[t.k]||prog(t.k).d).sort((a,b)=>(LMS.lastAt[b.k]||0)-(LMS.lastAt[a.k]||0));

/* ---------- beranda ---------- */
const HERO=[
  ['python','Python',`nama = "Sinta"\nhobi = ["kopi", "buku"]\nprint(f"Halo, {nama}! Suka {hobi[0]}?")`,'Halo, Sinta! Suka kopi?'],
  ['sql','SQL',`SELECT nama, kota\nFROM pelanggan\nWHERE kota = 'Jakarta';`,null],
  ['ts','TypeScript',`type Produk = { nama: string; harga: number };\nconst kopi: Produk = { nama: "Kopi Gayo", harga: 85000 };\nconsole.log(\`\${kopi.nama}: Rp\${kopi.harga}\`);`,'Kopi Gayo: Rp85000'],
  ['java','Java',`String nama = "Sinta";\nint umur = 21;\nSystem.out.println("Halo, " + nama + "!");`,'Halo, Sinta!']];
function renderHome(){
  const rs=recent(),st=streak(),td=LMS.days[today()]||0,goal=LMS.goal||3,wn=dueN();
  const greet=(()=>{const h=new Date().getHours();return h<11?'Selamat pagi':h<15?'Selamat siang':h<19?'Selamat sore':'Selamat malam'})();
  const hero=rs.length?`<section class="dash">
    <div class="dash-main"><div class="eyebrow">${greet}${LMS.name?', '+esc(LMS.name):''}</div><h1>Lanjutkan dari terakhir kali.</h1>
      <a class="resume-big ${tcls(rs[0])}" href="#${resumeOf(rs[0].k).id}"><span class="tmark lg">${rs[0].mark}</span><span class="rb-t"><small>${rs[0].name} · Modul ${resumeOf(rs[0].k).mi+1}</small><b>${esc(resumeOf(rs[0].k).title)}</b><span class="mbar"><i style="width:${prog(rs[0].k).p*100}%"></i></span></span><span class="btn primary">Lanjut ▶</span></a></div>
    <div class="dash-stats"><div class="ds-goal">${ring(Math.min(1,td/goal),92)}<span><b>${td}/${goal}</b><small>target hari ini</small></span></div>
      <ul class="ds-list"><li><b>${st}</b><span>hari beruntun</span></li><li><b>${LMS.xp}</b><span>XP</span></li><li><b>${Object.keys(LMS.done).length}</b><span>pelajaran selesai</span></li></ul>
      ${wn?`<a class="ds-rev" href="#ulang">${wn} soal perlu diulang →</a>`:''}</div></section>
    ${rs.length>1?`<section class="section"><div class="sec-h row"><h2>Jalur yang sedang kamu ikuti</h2><a class="tlink" href="#saya">Lihat semua progres</a></div><div class="resume">${rs.slice(1,5).map(t=>{const x=resumeOf(t.k),p=prog(t.k);return `<a class="rcard ${tcls(t)}" href="#${x.id}"><span class="tmark">${t.mark}</span><span class="rc-t"><small>${t.name} · Modul ${x.mi+1}</small><b>${esc(x.title)}</b></span><span class="rc-p">${pct(p.p)}</span></a>`}).join('')}</div></section>`:''}`
   :`<section class="h-hero"><div class="h-copy">
      <div class="eyebrow">Akademi teknologi berbahasa Indonesia · kurikulum mengikuti roadmap.sh</div>
      <h1>Belajar <em>coding</em>, <em>data</em>, dan <em>desain</em> sambil melihat semuanya bekerja.</h1>
      <p class="lead">${TRACKS.length} jalur belajar dan ${nLessons} pelajaran, dari HTML pertamamu sampai pipeline data. Visual yang bergerak, editor yang langsung jalan, konsol SQL di browser, dan proyek akhir di setiap jalur.</p>
      <div class="cta"><button class="btn primary lg" data-to="#karier">Pilih tujuan karier ▼</button><a class="btn lg" href="#katalog">Lihat semua jalur</a></div></div>
    <div class="h-demo" id="hDemo" aria-label="Contoh kode"><div class="h-tabs">${HERO.map((h,i)=>`<button data-h="${i}" class="${h[0]}" aria-pressed="${i===0}">${h[1]}</button>`).join('')}</div><div class="h-body"></div></div></section>`;
  return `${hero}
  <section class="section" id="karier"><div class="sec-h"><div class="eyebrow">Jalur karier</div><h2>Mau jadi apa?</h2><p>Setiap jalur karier menyusun beberapa jalur belajar dalam urutan yang disarankan. Progresmu dihitung otomatis.</p></div>
   <div class="paths">${PATHS.map(pa=>{const ts=pa.tr.map(k=>TK[k]),dn=ts.reduce((a,t)=>a+prog(t.k).d,0),nn=ts.reduce((a,t)=>a+prog(t.k).n,0),nx=ts.find(t=>prog(t.k).p<1)||ts[0];
     return `<article class="cpath"><div class="cpath-h"><h3>${pa.t}</h3><span class="muted">${pct(dn/nn)}</span></div><p>${pa.d}</p>
      <ol class="cpath-steps">${ts.map(t=>{const p=prog(t.k);return `<li class="${tcls(t)} ${p.p>=1?'full':p.d?'part':''}"><a href="#${t.k}"><span class="tmark sm">${t.mark}</span>${t.name}</a></li>`}).join('')}</ol>
      <a class="btn ${dn?'primary':''}" href="#${dn?resumeOf(nx.k).id:nx.k}">${dn?'Lanjutkan '+nx.name:'Mulai dari '+nx.name}</a></article>`}).join('')}</div></section>
  <section class="section"><div class="sec-h row"><div><div class="eyebrow">Katalog</div><h2>Semua jalur belajar</h2></div><a class="tlink" href="#katalog">Buka katalog lengkap →</a></div>
   ${GROUPS.map(([g,n])=>`<div class="cat-row"><h3 class="cat-h">${n}</h3><div class="tgrid">${TRACKS.filter(t=>t.g===g).map(t=>trackCard(t,{desc:false})).join('')}</div></div>`).join('')}</section>
  ${rs.length?'':`<section class="section"><div class="sec-h"><div class="eyebrow">Metode</div><h2>Cara belajar di sini</h2></div>
   <ol class="method">${[['Baca konsep singkat','Bahasa sehari-hari, langsung ke inti, dengan contoh dari toko dan aplikasi lokal.'],['Lihat kodenya bekerja','Visual bergerak menunjukkan isi memori, alur data, atau perhitungan langkah demi langkah.'],['Coba sendiri','Editor HTML/CSS/JS/React dengan pratinjau langsung, konsol SQL, dan tebak keluaran.'],['Uji dan ulangi','Kuis di setiap pelajaran, ujian modul, daftar ulang soal yang salah, dan proyek akhir.']].map((m,i)=>`<li><span>${i+1}</span><b>${m[0]}</b><p>${m[1]}</p></li>`).join('')}</ol></section>`}
  <section class="section"><div class="more2"><a class="mcard" href="#kuis"><span class="eyebrow">Latihan</span><b>Kuis cerita</b><p>Soal berbentuk cerita sehari-hari untuk Java, Python, dan SQL.</p></a>
   <a class="mcard" href="#glosarium"><span class="eyebrow">Kamus</span><b>Glosarium</b><p>Istilah pemrograman dan basis data dengan padanan bahasa Inggrisnya.</p></a>
   <a class="mcard" href="#saya"><span class="eyebrow">Progres</span><b>Belajar saya</b><p>Target harian, hari beruntun, XP, nilai ujian, dan cadangan progres.</p></a></div></section>`;
}
function wireHome(){
  const box=$('#hDemo');if(!box)return;let i=0;
  const show=k=>{i=k;const [lang,,code,out]=HERO[k];box.querySelectorAll('[data-h]').forEach(b=>b.setAttribute('aria-pressed',+b.dataset.h===k));
    let res=out?`<pre class="out">${esc(out)}</pre>`:'';
    if(!out&&typeof SQLE==='undefined'){need(['rt']).then(()=>{if(i===k&&box.isConnected)show(k)},()=>{});res='<p class="muted">Memuat…</p>'}
    else if(!out){try{const r=SQLE.exec(SQLE.create(SEED.toko),code)[0];res=`<div class="h-res">${rtable(r.cols,r.rows.map(v=>({v})))}</div>`}catch(e){}}
    $('.h-body',box).innerHTML=`<pre class="code">${code.split('\n').map((ln,j)=>`<span class="ln" style="--d:${j}">${hl(ln,lang)||' '}</span>`).join('\n')}</pre><div class="h-out" style="--d:${code.split('\n').length}">${res}</div>`};
  box.addEventListener('click',e=>{const b=e.target.closest('[data-h]');if(b){show(+b.dataset.h);clearInterval(t)}});
  show(0);const t=setInterval(()=>show((i+1)%HERO.length),5200);TIMERS.push(t);
}

/* ---------- katalog ---------- */
let catState={q:'',g:'semua'};
function renderCatalog(){
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>Katalog</span></nav>
   <div class="eyebrow">Katalog</div><h1>${TRACKS.length} jalur belajar</h1><p class="lead muted">${nLessons} pelajaran dalam ${GROUPS.length} kategori. Semua jalur mengikuti roadmap.sh dan bisa diikuti bersamaan.</p></header>
   <div class="gl-tools"><input class="gl-search" id="catQ" type="search" placeholder="Saring jalur, misalnya data, react, atau desain" aria-label="Saring jalur" value="${esc(catState.q)}"></div>
   <div class="chips" id="catG">${[['semua','Semua'],...GROUPS.map(g=>[g[0],g[1]])].map(([k,n])=>`<button class="chip" data-g="${k}" aria-pressed="${k===catState.g}">${n}</button>`).join('')}</div>
   <div id="catList"></div>`;
}
function drawCatalog(){
  const q=catState.q.trim().toLowerCase();
  $('#catList').innerHTML=GROUPS.filter(g=>catState.g==='semua'||g[0]===catState.g).map(([g,n,d])=>{
    const ts=TRACKS.filter(t=>t.g===g&&(!q||(t.name+' '+t.h+' '+t.d+' '+n).toLowerCase().includes(q)));
    return ts.length?`<section class="cat-row"><div class="cat-hd"><h2>${n}</h2><p class="muted">${d}</p></div><div class="tgrid wide">${ts.map(t=>trackCard(t)).join('')}</div></section>`:''}).join('')||`<p class="empty">Tidak ada jalur yang cocok dengan "${esc(catState.q)}".</p>`;
}
function wireCatalog(){
  $('#catQ').addEventListener('input',e=>{catState.q=e.target.value;drawCatalog()});
  $('#catG').addEventListener('click',e=>{const b=e.target.closest('[data-g]');if(!b)return;catState.g=b.dataset.g;$('#catG').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));drawCatalog()});
  drawCatalog();
}

/* ---------- halaman jalur ---------- */
let lvFilter='Semua';
const examKey=(tk,mi)=>`${tk}-${mi}`;
function renderCourse(t){
  const p=prog(t.k),nx=resumeOf(t.k),projs=FLAT[t.k].filter(x=>base(x).l.k==='proj'),ex=t.mods.map((m,mi)=>LMS.exam[examKey(t.k,mi)]).filter(v=>v>=70).length;
  return `<header class="c-hero ${tcls(t)}">
    <nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><a href="#katalog">Katalog</a><span>/</span><span>${t.name}</span></nav>
    <div class="c-grid"><div>
      <div class="eyebrow">${GROUPS.find(g=>g[0]===t.g)[1]} · <a href="https://roadmap.sh/${t.road}" target="_blank" rel="noopener">mengikuti roadmap.sh/${t.road}</a></div>
      <h1>${t.h}</h1><p class="lead">${t.d}</p>
      <ul class="tc-stats"><li><b>${t.mods.length}</b> modul</li><li><b>${p.n}</b> pelajaran</li><li><b>±${hours(t)}</b> jam belajar</li></ul>
    </div>
    <div class="c-prog"><div class="tc-ring big">${ring(p.p,112)}<span>${pct(p.p)}</span></div><p>${p.d} dari ${p.n} pelajaran selesai</p>
      <a class="btn primary" href="#${nx.id}">${p.d?'Lanjutkan':'Mulai belajar'} ▶</a><small>${p.d?'Berikutnya: ':'Pelajaran pertama: '}${esc(nx.title)}</small></div></div>
  </header>
  <div class="c-acts">
   <a class="c-act" href="#${t.k}-tes"><b>Tes penempatan</b><span>Sudah pernah belajar? Ukur dulu, lalu lompati modul yang sudah dikuasai.</span></a>
   <a class="c-act" href="#persiapan-${t.k}"><b>Siapkan laptop</b><span>${esc(setupItems(t.k).map(x=>x.name).join(', '))}</span></a>
   ${projs.length?`<a class="c-act" href="#${projs[projs.length-1].id}"><b>Proyek akhir</b><span>${esc(projs[projs.length-1].title)}${isDone(projs[projs.length-1])?' · ✓ selesai':''}</span></a>`:''}</div>
  <div class="c-tools"><div class="chips" role="group" aria-label="Saring tingkat" id="lvF">${['Semua',...LVL4.filter(L=>t.mods.some(m=>m.lvl===L))].map(L=>`<button class="chip" data-l="${L}" aria-pressed="${L===lvFilter}">${L}</button>`).join('')}</div>
   <button class="tlink" id="expAll">Buka semua modul</button></div>
  <ol class="road ${tcls(t)}" id="road">${t.mods.map((m,mi)=>{const mp=modProg(t.k,mi),cur=nx.mi===mi,bank=bankN(t.k,mi),sc=LMS.exam[examKey(t.k,mi)];
    return `<li class="mod ${mp.d===mp.n?'full':''} ${cur?'cur':''}" data-lvl="${m.lvl}" ${lvFilter!=='Semua'&&m.lvl!==lvFilter?'hidden':''}>
     <div class="mod-rail"><span class="mod-dot">${mp.d===mp.n?'✓':mi+1}</span></div>
     <div class="mod-card"><div class="mod-top"><span class="eyebrow">Modul ${mi+1} · ${m.lvl}</span><span class="mod-p">${mp.d}/${mp.n}</span></div>
      <h3>${m.t}</h3><p>${m.d}</p>
      <div class="mod-bar"><i style="width:${mp.d/mp.n*100}%"></i></div>
      <details ${cur?'open':''}><summary>${mp.n} pelajaran · ±${FLAT[t.k].filter(x=>x.mi===mi).reduce((a,x)=>a+minOf(x),0)} menit</summary>
       <ol class="les-list">${FLAT[t.k].filter(x=>x.mi===mi).map(x=>`<li><a href="#${x.id}" class="${isDone(x)?'done':isOpen(x)?'':'locked'} ${x.id===nx.id?'next':''}"><span class="chk" aria-hidden="true"></span><span class="lt">${esc(x.title)}${isOpen(x)?'':'<span class="sr">(terkunci)</span>'}</span><small>${x.src?'↗ '+x.src.t.name:KIND[kindOf(x)]}</small></a></li>`).join('')}</ol>
       ${mp.d?`<a class="mod-sum" href="#${t.k}-ringkasan-${mi+1}">📄 Ringkasan modul${mp.d<mp.n?` · ${mp.d}/${mp.n}`:''}</a>`:''}
       ${bank>=3?`<a class="mod-exam ${mp.d===mp.n?'':'locked'}" href="#${t.k}-ujian-${mi+1}"><span>${mp.d===mp.n?'📝':'🔒'} Ujian modul · ${Math.min(10,bank)} soal</span><b>${mp.d<mp.n?'Terbuka setelah modul selesai':sc!=null?`Nilai terbaik ${sc}${sc>=70?' ✓':''}`:'Belum dicoba'}</b></a>`:''}
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

/* ---------- ujian modul & tes penempatan ---------- */
let EXAM=null;
function scoreBar(){return `<div class="score" id="exScore"><div><span class="big">0</span><span class="of"> / ${EXAM.items.length} benar</span></div><div class="sc-bar"><div class="bar"><i style="width:0%"></i></div><small>0 dari ${EXAM.items.length} dijawab</small></div></div>`}
function renderExam(t,mi){
  const m=t.mods[mi],items=shuffle(bankOf(t.k,mi)).slice(0,10);EXAM={kind:'ujian',t,mi,items,ans:{}};const best=LMS.exam[examKey(t.k,mi)];
  return `<header class="ch-head ${tcls(t)}"><nav class="crumb" aria-label="Lokasi"><a href="#${t.k}">${t.name}</a><span>/</span><span>Ujian modul ${mi+1}</span></nav>
   <div class="eyebrow">Ujian modul ${mi+1} · ${m.lvl}</div><h1>${m.t}</h1><p class="lead muted">${items.length} soal acak dari pelajaran modul ini. Lulus dengan nilai 70 atau lebih. ${best!=null?`Nilai terbaikmu: <b>${best}</b>.`:''}</p></header>
   ${scoreBar()}<section class="section" id="exQ">${quizHTML(items,mi+7)}</section><div id="exRes" aria-live="polite"></div>`;
}
function renderPlacement(t){
  const items=t.mods.flatMap((m,mi)=>shuffle(bankOf(t.k,mi)).slice(0,2).map(q=>({...q,mi}))).slice(0,24);EXAM={kind:'tes',t,items,ans:{}};
  return `<header class="ch-head ${tcls(t)}"><nav class="crumb" aria-label="Lokasi"><a href="#${t.k}">${t.name}</a><span>/</span><span>Tes penempatan</span></nav>
   <div class="eyebrow">Tes penempatan</div><h1>Mulai dari mana di jalur ${t.name}?</h1><p class="lead muted">${items.length} soal, dua dari setiap modul, berurutan dari yang paling dasar. Jawab yang kamu tahu; boleh berhenti kapan saja dan lihat rekomendasinya.</p></header>
   ${scoreBar()}<section class="section" id="exQ">${quizHTML(items,3)}</section><div class="sl-act"><button class="btn primary" id="exStop">Lihat rekomendasi</button></div><div id="exRes" aria-live="polite"></div>`;
}
function wireExam(){
  const E=EXAM,res=$('#exRes');
  const upd=()=>{const n=Object.keys(E.ans).length,ok=Object.values(E.ans).filter(Boolean).length;$('#exScore .big').textContent=ok;$('#exScore .bar i').style.width=`${n/E.items.length*100}%`;$('#exScore small').textContent=`${n} dari ${E.items.length} dijawab`;
    if(n===E.items.length)finish()};
  function finish(){const ok=Object.values(E.ans).filter(Boolean).length;
    if(E.kind==='ujian'){const sc=Math.round(ok/E.items.length*100),k=examKey(E.t.k,E.mi),prev=LMS.exam[k];LMS.exam[k]=Math.max(prev||0,sc);
      if(sc>=70&&!(prev>=70))award(30,'· Ujian modul lulus');else saveLms();
      const nx=E.t.mods[E.mi+1];
      res.innerHTML=`<div class="exam-res ${sc>=70?'ok':'bad'}"><b class="big">${sc}</b><div><h3>${sc>=70?'Lulus! 🎉':'Belum lulus'}</h3><p>${ok} dari ${E.items.length} benar. ${sc>=70?'Kamu menguasai modul ini.':'Soal yang salah sudah masuk daftar <a href="#ulang">Ulang</a>. Pelajari lagi lalu coba ujian baru.'}</p>
        <div class="sl-act"><button class="btn" onclick="route()">Ujian lagi (soal diacak)</button>${nx?`<a class="btn primary" href="#${FLAT[E.t.k].find(x=>x.mi===E.mi+1).id}">Lanjut modul ${E.mi+2} ▶</a>`:`<a class="btn primary" href="#${E.t.k}">Kembali ke jalur</a>`}</div></div></div>`;
    }else placementResult();
    res.scrollIntoView({behavior:RM()?'auto':'smooth',block:'center'})}
  function placementResult(){
    const per=E.t.mods.map((m,mi)=>{const its=E.items.map((q,i)=>[q,i]).filter(([q])=>q.mi===mi);return {mi,n:its.length,ok:its.filter(([,i])=>E.ans[i]===true).length}});
    let k=0;while(k<per.length&&(per[k].n===0||per[k].ok===per[k].n))k++;
    E.k=k;
    res.innerHTML=`<div class="exam-res"><b class="big">${k}</b><div><h3>${k===0?'Mulai dari Modul 1':`Kamu tampaknya sudah menguasai Modul 1–${k}`}</h3>
      <p>${per.map(p=>`M${p.mi+1}: ${p.ok}/${p.n}`).join(' · ')}</p>
      <div class="sl-act">${k>0?`<button class="btn" id="exSkip">Tandai Modul 1–${k} sudah dikuasai</button>`:''}<a class="btn primary" href="#${(FLAT[E.t.k].find(x=>x.mi===Math.min(k,E.t.mods.length-1))||FLAT[E.t.k][0]).id}">Mulai Modul ${Math.min(k,E.t.mods.length-1)+1} ▶</a></div></div></div>`;
    const sk=$('#exSkip');if(sk)sk.onclick=()=>{FLAT[E.t.k].filter(x=>x.mi<k).forEach(x=>markDone(x,true));toast(`Modul 1–${k} ditandai selesai`);location.hash=E.t.k}}
  wireQuiz($('#exQ'),E.items,{onAnswer:(ok,i)=>{E.ans[i]=ok;upd()}});
  const st=$('#exStop');if(st)st.onclick=()=>finish();
}

/* ---------- belajar saya ---------- */
function heat(){const out=[];const d=new Date();d.setDate(d.getDate()-7*12+1);
  for(let i=0;i<84;i++){const k=`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;const v=LMS.days[k]||0;out.push(`<i class="h${Math.min(3,v>=LMS.goal?3:v?Math.ceil(v/LMS.goal*2):LMS.act[k]?1:0)}" title="${k}: ${v} pelajaran"></i>`);d.setDate(d.getDate()+1)}
  return `<div class="heat" aria-label="Aktivitas 12 minggu terakhir">${out.join('')}</div>`}
function renderMine(){
  const act=TRACKS.filter(t=>prog(t.k).d||LMS.last[t.k]),ex=Object.entries(LMS.exam);
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>Belajar saya</span></nav><div class="eyebrow">Belajar saya</div><h1>${LMS.name?esc(LMS.name):'Progres belajarmu'}</h1></header>
   <div class="kpis"><div><b>${streak()}</b><span>hari beruntun</span></div><div><b>${LMS.xp}</b><span>XP</span></div><div><b>${Object.keys(LMS.done).length}</b><span>pelajaran selesai</span></div><div><b>${Object.keys(LMS.act).length}</b><span>hari aktif</span></div><div><b>${ex.filter(([,v])=>v>=70).length}</b><span>ujian lulus</span></div></div>
   <section class="section"><div class="sec-h row"><h2>Aktivitas</h2><label class="goal">Target harian <select class="inp" id="goal">${[1,2,3,5,8].map(n=>`<option value="${n}" ${n===LMS.goal?'selected':''}>${n} pelajaran</option>`).join('')}</select></label></div>${heat()}<p class="muted">Kotak lebih gelap berarti lebih banyak pelajaran selesai hari itu.</p></section>
   <section class="section"><h2>Jalur yang diikuti</h2>${act.length?`<div class="tgrid wide">${act.map(t=>trackCard(t)).join('')}</div>`:'<p class="empty">Belum ada. <a href="#katalog">Pilih jalur di katalog</a>.</p>'}</section>
   ${ex.length?`<section class="section"><h2>Nilai ujian modul</h2><div class="exl">${ex.map(([k,v])=>{const i=k.lastIndexOf('-'),t=TK[k.slice(0,i)],mi=+k.slice(i+1);return t?`<a class="${tcls(t)}" href="#${t.k}-ujian-${mi+1}"><span class="tmark sm">${t.mark}</span><span>${esc(t.mods[mi].t)}</span><b class="${v>=70?'okc':'badc'}">${v}</b></a>`:''}).join('')}</div></section>`:''}
   <section class="section"><h2>Profil & data</h2><div class="prof">
    <label>Nama (untuk sapaan) <input class="gl-search" id="pName" value="${esc(LMS.name||'')}" maxlength="60"></label>
    <div class="sl-act"><button class="btn" id="bkCopy">Salin cadangan progres</button><button class="btn" id="bkShow" aria-expanded="false">Pulihkan dari cadangan</button><button class="btn danger" id="rsAll">Hapus semua progres</button></div>
    <div id="bkBox" hidden><textarea class="bk" id="bkTxt" placeholder="Tempel teks cadangan di sini"></textarea><button class="btn primary" id="bkLoad">Pulihkan</button></div>
    <div id="rsBox" hidden class="confirm"><p>Semua progres, XP, dan nilai ujian di browser ini akan dihapus. Lanjutkan?</p><div class="sl-act"><button class="btn danger" id="rsYes">Ya, hapus</button><button class="btn" id="rsNo">Batal</button></div></div>
    <p class="muted" id="bkMsg" aria-live="polite">Progres tersimpan di browser ini saja. Salin cadangan untuk memindahkannya ke perangkat lain.</p></div></section>
   ${CHUNK?`<section class="section"><h2>Aplikasi & offline</h2><div class="prof"><p>${matchMedia('(display-mode: standalone)').matches?'Ruang Kode sudah terpasang sebagai aplikasi.':'Pasang Ruang Kode di HP atau laptop agar bisa dibuka seperti aplikasi.'} Setelah dibuka sekali dengan internet, semua materi tersimpan dan bisa dipelajari tanpa koneksi. Menjalankan kode Python dan React tetap butuh internet saat pertama kali.</p>
    <div class="sl-act"><button class="btn primary" id="instBtn" ${INSTALL?'':'hidden'}>Pasang aplikasi</button></div></div></section>`:''}`;
}
function wireMine(){
  const ib=$('#instBtn');if(ib)ib.onclick=async()=>{if(!INSTALL)return;INSTALL.prompt();const r=await INSTALL.userChoice;INSTALL=null;ib.hidden=true;if(r.outcome==='accepted')toast('Ruang Kode dipasang')};
  $('#goal').onchange=e=>{LMS.goal=+e.target.value;saveLms();route()};
  $('#pName').oninput=e=>{LMS.name=e.target.value.trim();saveLms()};
  $('#bkCopy').onclick=e=>copyText(btoa(unescape(encodeURIComponent(JSON.stringify(LMS)))),e.target,'Salin cadangan progres');
  $('#bkShow').onclick=e=>{const b=$('#bkBox');b.hidden=!b.hidden;e.target.setAttribute('aria-expanded',!b.hidden)};
  $('#bkLoad').onclick=()=>{try{const d=JSON.parse(decodeURIComponent(escape(atob($('#bkTxt').value.trim()))));if(!d.done)throw 0;Object.keys(LMS).forEach(k=>delete LMS[k]);Object.assign(LMS,d);saveLms();toast('Progres dipulihkan');route()}catch(e){$('#bkMsg').textContent='Teks cadangan tidak dikenali. Pastikan disalin utuh.'}};
  $('#rsAll').onclick=()=>{$('#rsBox').hidden=false};$('#rsNo').onclick=()=>{$('#rsBox').hidden=true};
  $('#rsYes').onclick=()=>{const keep={name:LMS.name};Object.keys(LMS).forEach(k=>delete LMS[k]);Object.assign(LMS,{done:{},last:{},lastAt:{},wrong:{},exam:{},days:{},act:{},proj:{},task:{},qok:{},xp:0,goal:3},keep);saveLms();toast('Progres dihapus');route()};
}

/* ---------- daftar ulang ---------- */
/* ringkasan modul: poin penting dari setiap pelajaran yang sudah diselesaikan */
function pointsOf(x){const y=base(x),l=y.l;
  if(l.k==='lab')return chFor(l.n,y.t.lang).points||[];
  if(l.k==='topic'){const [n,i]=l.ref.split('.').map(Number),tp=tpFor(l.ref,TOPICS[n][i],y.t.lang);return tp.rumus?[`<code>${esc(tp.rumus.f)}</code>`,...tp.rumus.i.map(esc)]:[]}
  return l.pts||[]}
function renderSummary(t,mi){
  const m=t.mods[mi],F=FLAT[t.k].filter(x=>x.mi===mi),mp=modProg(t.k,mi);
  return `<header class="ch-head ${tcls(t)}"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><a href="#${t.k}">${t.name}</a><span>/</span><span>Modul ${mi+1}</span></nav>
   <div class="eyebrow">Ringkasan modul ${mi+1} · ${mp.d} dari ${mp.n} pelajaran selesai</div><h1>${esc(m.t)}</h1><p class="lead muted">${m.d}</p></header>
   <ol class="sum-list">${F.map(x=>{const p=pointsOf(x);return `<li class="${isDone(x)?'':'todo'}"><h2><a href="#${x.id}">${esc(x.title)}</a></h2>
     ${isDone(x)?(p.length?`<ul class="points">${p.map(v=>`<li>${v}</li>`).join('')}</ul>`:'<p class="muted small">Pelajaran praktik, tidak ada poin ringkasan.</p>')
      :`<p class="muted small">${isOpen(x)?'Selesaikan pelajaran ini untuk melihat ringkasannya.':'🔒 Terbuka setelah pelajaran sebelumnya selesai.'}</p>`}</li>`}).join('')}</ol>
   <div class="lock-act">${mp.d===mp.n&&bankN(t.k,mi)>=3?`<a class="btn primary" href="#${t.k}-ujian-${mi+1}">📝 Uji pemahaman: ujian modul</a>`:`<a class="btn primary" href="#${nextOf(t.k).id}">Lanjutkan belajar ▶</a>`}<a class="btn" href="#${t.k}">Kurikulum</a></div>`;
}
function renderReview(){
  const all=Object.entries(LMS.wrong),W=all.filter(([,v])=>isDue(v)).sort((a,b)=>b[1].t-a[1].t),later=all.filter(([,v])=>!isDue(v)).sort((a,b)=>a[1].due-b[1].due);
  EXAM={items:W.map(([k,v])=>({...v,k}))};
  const when=ts=>{const d=Math.round((new Date(ts).setHours(0,0,0,0)-new Date().setHours(0,0,0,0))/DAY);return d<=1?'besok':`${d} hari lagi`};
  const nextGroups=later.reduce((m,[,v])=>{const w=when(v.due);m[w]=(m[w]||0)+1;return m},{});
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>Ulang</span></nav><div class="eyebrow">Pengulangan berjarak</div><h1>Soal yang perlu diulang</h1>
   <p class="lead muted">Jawaban yang salah di kuis dan ujian masuk ke sini. Jawab benar, lalu soal yang sama muncul lagi besok, 3 hari, dan 7 hari kemudian. Mengulang dengan jeda seperti ini membuat materi lebih lama diingat.</p></header>
   ${later.length?`<div class="rv-sched"><b>Terjadwal:</b> ${Object.entries(nextGroups).map(([w,n])=>`${n} soal ${w}`).join(' · ')}</div>`:''}
   ${W.length?`<div class="sl-act"><span class="muted">${W.length} soal untuk hari ini</span><button class="btn" id="rvClear">Kosongkan daftar</button></div><section class="section" id="rvQ">${quizHTML(EXAM.items,11)}</section>`
    :`<div class="empty big">🎉 Tidak ada soal untuk diulang hari ini. <a href="#katalog">Lanjut belajar</a>.</div>`}`;
}
function wireReview(){
  const q=$('#rvQ');if(!q)return;
  q.querySelectorAll('.q').forEach((qe,i)=>{const it=EXAM.items[i],x=BYID[it.ref];if(x)qe.insertAdjacentHTML('beforeend',`<a class="more" href="#${x.id}">Dari: ${esc(x.t.name)} · ${esc(x.title)} →</a>`)});
  wireQuiz(q,EXAM.items,{onAnswer:(ok,i,lv)=>{if(ok)toast(lv==='done'?'Dikuasai! Soal keluar dari daftar ulang':`Benar. Muncul lagi ${lv===1?'besok':lv+' hari lagi'}`);else toast('Belum tepat. Soal ini diulang lagi hari ini')}});
  $('#rvClear').onclick=()=>{LMS.wrong={};saveLms();route()};
}
