/* ===================== APLIKASI LMS: DATA & KEADAAN =====================
   16 jalur dalam 5 kategori, mengikuti roadmap.sh. Rute:
   #beranda, #katalog, #saya, #ulang, #kuis[-tk], #glosarium,
   #<tk> (halaman jalur), #<tk>-M-L (pelajaran), #<tk>-tes (tes penempatan),
   #<tk>-ujian-M (ujian modul), #<tk>-sertifikat. */
const GROUPS=[
  ['prog','Pemrograman','Bahasa untuk membangun aplikasi, backend, dan otomasi.'],
  ['web','Web & Frontend','Membangun situs dan aplikasi web yang cepat dan mudah dipakai.'],
  ['data','Data','Mengolah, menganalisis, dan mengalirkan data menjadi keputusan.'],
  ['des','Desain','Merancang pengalaman dan sistem visual yang konsisten.'],
  ['tool','Alat kerja','Alat yang dipakai setiap tim pengembang.']];
const TRACKS=[
  {k:'java',g:'prog',name:'Java',lang:'java',mods:JAVA_MODULES,road:'java',mark:'J',h:'Java dari nol sampai siap kerja',d:'Bahasa bertipe statis untuk Android, perbankan, dan backend skala besar. Dari variabel dan OOP sampai konkurensi, JDBC, dan Spring Boot.'},
  {k:'python',g:'prog',name:'Python',lang:'python',mods:PY_MODULES,road:'python',mark:'Py',h:'Python yang rapi dan idiomatik',d:'Bahasa ringkas untuk otomasi, data, AI, dan web. Dari sintaks dasar sampai type hints, testing, asyncio, dan framework web.'},
  {k:'ts',g:'prog',name:'TypeScript',lang:'ts',mods:TS_MODULES,road:'typescript',mark:'TS',h:'JavaScript yang lebih aman dengan tipe',d:'Tipe dasar, interface, generics, narrowing, utility types, sampai konfigurasi proyek nyata.'},
  {k:'fe0',g:'web',name:'Frontend Pemula',lang:'js',mods:FE0_MODULES,road:'frontend-beginner',mark:'FE',h:'Langkah pertama menjadi frontend developer',d:'HTML, CSS, JavaScript, Git, npm, Tailwind, React dasar, pengujian, dan menerbitkan situs pertamamu.'},
  {k:'html',g:'web',name:'HTML',lang:'html',mods:HTML_MODULES,road:'html',mark:'&lt;/&gt;',h:'Struktur halaman web yang benar',d:'Elemen, teks, link, media, tabel, form, HTML semantik, aksesibilitas, dan SEO dasar.'},
  {k:'css',g:'web',name:'CSS',lang:'css',mods:CSS_MODULES,road:'css',mark:'{}',h:'Tampilan rapi di semua layar',d:'Selector, box model, flexbox, grid, responsif, variabel, animasi, dan arsitektur CSS.'},
  {k:'fe',g:'web',name:'Frontend',lang:'js',mods:FE_MODULES,road:'frontend',mark:'FD',h:'Frontend developer profesional',d:'Internet, JavaScript lanjutan, build tools, testing, keamanan, performa, PWA, SSR, sampai AI di frontend.'},
  {k:'react',g:'web',name:'React',lang:'jsx',mods:REACT_MODULES,road:'react',mark:'⚛',h:'Antarmuka modern dengan React',d:'Komponen, props, state, hooks, form, routing, data dari server, styling, dan pengujian.'},
  {k:'sql',g:'data',name:'SQL',lang:'sql',mods:SQL_MODULES,road:'sql',mark:'SQL',h:'SQL untuk aplikasi dan analisis data',d:'Jalankan query sungguhan di konsol bawaan, dari SELECT pertama sampai JOIN, transaksi, index, dan window function.'},
  {k:'pda',g:'data',name:'Python Analisis Data',lang:'python',mods:PDA_MODULES,road:'python-data-analysis',mark:'pd',h:'Analisis data dengan NumPy dan pandas',d:'Membaca, membersihkan, mengolah, dan memvisualisasikan data, lalu statistik dan data skala besar.'},
  {k:'da',g:'data',name:'Data Analyst',lang:'python',mods:DA_MODULES,road:'data-analyst',mark:'DA',h:'Menjadi data analyst',d:'Spreadsheet, SQL, Python, statistik, visualisasi, big data, dan dasar machine learning.'},
  {k:'bi',g:'data',name:'BI Analyst',lang:'sql',mods:BI_MODULES,road:'bi-analyst',mark:'BI',h:'Metrik, model data, dan dashboard',d:'KPI, skema bintang, statistik untuk bisnis, desain dashboard, Power BI/Tableau, dan etika data.'},
  {k:'de',g:'data',name:'Data Engineer',lang:'python',mods:DE_MODULES,road:'data-engineer',mark:'DE',h:'Membangun pipeline data yang andal',d:'Database, pemodelan, ETL/ELT, Airflow, Kafka, Spark, cloud, kualitas data, dan keamanan.'},
  {k:'ux',g:'des',name:'UX Design',lang:'text',mods:UX_MODULES,road:'ux-design',mark:'UX',h:'Merancang perilaku pengguna',d:'Psikologi keputusan, model Fogg dan Hook, strategi perubahan perilaku, riset, prototyping, dan A/B test.'},
  {k:'ds',g:'des',name:'Design System',lang:'css',mods:DS_MODULES,road:'design-system',mark:'DS',h:'Satu sumber kebenaran desain',d:'Bahasa desain, token, komponen dengan semua state, dokumentasi, versi, dan tata kelola.'},
  {k:'git',g:'tool',name:'Git & GitHub',lang:'bash',mods:GIT_MODULES,road:'git-github-beginner',mark:'git',h:'Version control dan kolaborasi',d:'Commit, branch, merge, remote, pull request, GitHub Pages, Actions, dan keamanan repositori.'}];
const TK=Object.fromEntries(TRACKS.map(t=>[t.k,t]));
const PATHS=[
  {k:'fe',t:'Frontend Developer',d:'Membangun antarmuka web yang cepat dan mudah dipakai.',tr:['fe0','html','css','git','ts','react','fe']},
  {k:'da',t:'Data Analyst',d:'Menjawab pertanyaan bisnis dengan data.',tr:['sql','pda','da','bi']},
  {k:'de',t:'Data Engineer',d:'Membangun jalur data dari sumber ke dashboard.',tr:['python','sql','git','pda','de']},
  {k:'ux',t:'UI/UX Designer',d:'Merancang pengalaman dan sistem desain.',tr:['ux','ds','html','css']},
  {k:'be',t:'Backend Java',d:'Membangun layanan dan API yang andal.',tr:['java','sql','git']}];
const LVL4=['Pemula','Menengah','Lanjutan','Profesional'];
const KIND={lab:'Konsep & lab',topic:'Topik 5 langkah',c:'Konsep & kode',s:'Praktik SQL',w:'Praktik langsung',proj:'Proyek akhir',mini:'Proyek mini'};
const MIN={lab:15,topic:12,c:8,s:10,w:12,proj:60};
const lid=(tk,mi,li)=>`${tk}-${mi+1}-${li+1}`;
function lessonTitle(l){if(l.k==='lab')return CH[l.n-1].t;if(l.k==='topic'){const [n,i]=l.ref.split('.').map(Number);return TOPICS[n][i].t}return l.t}
const FLAT=Object.fromEntries(TRACKS.map(t=>[t.k,t.mods.flatMap((m,mi)=>m.lessons.map((l,li)=>({t,m,mi,l,li,id:lid(t.k,mi,li),title:l.k==='see'?'':lessonTitle(l)})))]));
const BYID=Object.fromEntries(Object.values(FLAT).flat().map(x=>[x.id,x]));
/* pelajaran "see" meminjam pelajaran jalur lain; progresnya ikut pelajaran asal */
Object.values(FLAT).flat().filter(x=>x.l.k==='see').forEach(x=>{const i=x.l.ref.indexOf(':'),tk=x.l.ref.slice(0,i),ti=x.l.ref.slice(i+1);
  x.src=FLAT[tk].find(y=>y.title===ti&&y.l.k!=='see');x.title=x.src?x.src.title:ti});
const base=x=>x.src||x;
const kindOf=x=>{const y=base(x);return y.l.mini?'mini':y.l.k};
const minOf=x=>MIN[base(x).l.k]||10;
const hours=t=>Math.max(1,Math.round(FLAT[t.k].reduce((a,x)=>a+minOf(x),0)/60));
const nLessons=Object.values(FLAT).flat().length;

/* ---------- progres ---------- */
const today=()=>{const d=new Date();return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`};
const LMS=store.get('rk-lms',null)||(()=>{const s={done:{},last:{}};
  const old=store.get('rk-done',[]);old.forEach(n=>['java','python'].forEach(tk=>{const x=FLAT[tk].find(y=>y.l.k==='lab'&&y.l.n===n);if(x)s.done[x.id]=1}));return s})();
for(const [k,v] of Object.entries({done:{},last:{},lastAt:{},wrong:{},exam:{},days:{},act:{},proj:{},task:{},qok:{},xp:0,name:'',goal:3}))if(LMS[k]==null)LMS[k]=v;
const saveLms=()=>{store.set('rk-lms',LMS);updateBadges()};
const isDone=x=>!!LMS.done[base(x).id];
function prog(tk){const F=FLAT[tk];const d=F.filter(isDone).length;return {d,n:F.length,p:F.length?d/F.length:0}}
function nextOf(tk){const F=FLAT[tk];return F.find(x=>!isDone(x))||F[0]}
function resumeOf(tk){const l=BYID[LMS.last[tk]];return l&&!isDone(l)?l:nextOf(tk)}
function modProg(tk,mi){const F=FLAT[tk].filter(x=>x.mi===mi);return {d:F.filter(isDone).length,n:F.length}}
function touch(){LMS.act[today()]=1}
function streak(){let n=0;const d=new Date();const key=x=>`${x.getFullYear()}-${String(x.getMonth()+1).padStart(2,'0')}-${String(x.getDate()).padStart(2,'0')}`;
  if(!LMS.act[key(d)])d.setDate(d.getDate()-1);while(LMS.act[key(d)]){n++;d.setDate(d.getDate()-1)}return n}
function award(xp,msg){LMS.xp+=xp;touch();saveLms();toast(`<b>+${xp} XP</b> ${msg||''}`)}
function markDone(x,silent){const y=base(x);if(LMS.done[y.id])return false;LMS.done[y.id]=1;LMS.days[today()]=(LMS.days[today()]||0)+1;
  const p=prog(x.t.k);if(!silent)award(10,p.d===p.n?`· Jalur ${x.t.name} selesai! Ambil sertifikatmu.`:'· Pelajaran selesai');else saveLms();return true}
function toast(html){const t=$('#toast');if(!t)return;t.innerHTML=html;t.classList.add('on');clearTimeout(toast.h);toast.h=setTimeout(()=>t.classList.remove('on'),2600)}
function updateBadges(){const n=Object.keys(LMS.wrong).length;document.querySelectorAll('.wrongN').forEach(b=>{b.textContent=n||'';b.hidden=!n})}

/* ---------- komponen kecil ---------- */
const ring=(p,size=56)=>{const r=size/2-4,c=2*Math.PI*r;return `<svg class="ring" viewBox="0 0 ${size} ${size}" width="${size}" height="${size}" aria-hidden="true"><circle cx="${size/2}" cy="${size/2}" r="${r}" class="rb"/><circle cx="${size/2}" cy="${size/2}" r="${r}" class="rf" style="stroke-dasharray:${c};stroke-dashoffset:${c*(1-p)}"/></svg>`};
const LANGLBL={java:'JAVA',python:'PYTHON',sql:'SQL',ts:'TYPESCRIPT',js:'JAVASCRIPT',jsx:'JSX',html:'HTML',css:'CSS',bash:'TERMINAL',yaml:'YAML',json:'JSON',text:'CONTOH'};
function pane(lang,code,o={}){
  const lab=o.label||LANGLBL[lang]||'KODE';
  return `<div class="pane ${lang==='java'||lang==='python'?lang:'tx'}"><div class="pane-h"><span>${lab}</span>${o.copy!==false?'<button class="copy" data-copy>Salin</button>':''}</div><pre class="code">${hl(code,lang)}</pre>${o.out?`<pre class="out">${esc(o.out)}</pre>`:''}</div>`;
}
function copyText(txt,b,label='Salin'){
  const fail=()=>{b.textContent='Pilih teks lalu Ctrl+C'};
  try{navigator.clipboard.writeText(txt).then(()=>{b.textContent='Tersalin';setTimeout(()=>b.textContent=label,1400)},fail)}catch(e){fail()}}
function copyFrom(b){const pre=b.closest('.pane').querySelector('pre.code');
  try{navigator.clipboard.writeText(pre.textContent).then(()=>{b.textContent='Tersalin';setTimeout(()=>b.textContent='Salin',1400)},()=>{const r=document.createRange();r.selectNodeContents(pre);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Tekan Ctrl+C'})}catch(e){}}
const nodesHTML=n=>n&&n.length?`<div class="l-nodes"><span>Topik roadmap</span>${n.map(x=>`<span class="rn">${esc(x)}</span>`).join('')}</div>`:'';
const qkey=s=>{let h=5381;for(const c of String(s))h=(h*33+c.charCodeAt(0))|0;return 'q'+(h>>>0).toString(36)};

/* kuis pilihan ganda: items = [{q,o,a,w}]; jawaban salah masuk daftar ulang */
function quizHTML(items,seed){
  return `<div class="quiz">${items.map((q,qi)=>{const ord=perm(q.o.length,seed*13+qi);return `<div class="q" data-q="${qi}"><b>${qi+1}. ${q.q}</b><div class="opts">${ord.map(oi=>`<button class="opt" data-o="${oi}">${q.o[oi]}</button>`).join('')}</div><p class="why" hidden></p></div>`}).join('')}</div>`;
}
function wireQuiz(root,items,o={}){
  root.querySelectorAll('.quiz .q').forEach(qe=>qe.addEventListener('click',e=>{
    const b=e.target.closest('.opt');if(!b||b.disabled)return;const q=items[+qe.dataset.q],pick=+b.dataset.o,ok=pick===q.a,k=qkey(q.q);
    qe.querySelectorAll('.opt').forEach(x=>{x.disabled=true;const v=+x.dataset.o;if(v===q.a)x.classList.add('right');else if(v===pick)x.classList.add('wrong')});
    const w=$('.why',qe);w.hidden=false;w.innerHTML=(ok?'<b class="okc">Benar.</b> ':'<b class="badc">Belum tepat.</b> ')+q.w;
    qe.classList.add(ok?'is-ok':'is-bad');touch();
    if(ok){delete LMS.wrong[k];if(!LMS.qok[k]){LMS.qok[k]=1;LMS.xp+=2}}else LMS.wrong[k]={q:q.q,o:q.o,a:q.a,w:q.w,ref:q.ref||(q.x&&q.x.id)||o.ref||location.hash.slice(1),t:Date.now()};
    saveLms();if(o.onAnswer)o.onAnswer(ok,+qe.dataset.q);
  }));
}
function perm(n,seed){const a=[...Array(n).keys()];let s=(seed*7919+13)%233280;for(let i=n-1;i>0;i--){s=(s*9301+49297)%233280;const j=Math.floor(s/233280*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const normQ=([q,o,a,w])=>({q:esc(q),o:o.map(esc),a,w:esc(w)});
/* bank soal satu modul, dipakai ujian dan tes penempatan */
function bankOf(tk,mi){
  return FLAT[tk].filter(x=>x.mi===mi).flatMap(x=>{const y=base(x),l=y.l;
    if(l.k==='lab')return CH[l.n-1].quiz.map(q=>({...q,x}));
    return (l.q||[]).map(q=>({...normQ(q),x}))});
}
function shuffle(a){a=[...a];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
