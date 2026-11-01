/* ===================== NAVIGASI, PENCARIAN, TEMA & RUTE ===================== */
function megaHTML(){
  return `<div class="mega-in">${GROUPS.map(([g,n])=>`<div class="mg-col"><div class="eyebrow">${n}</div>${TRACKS.filter(t=>t.g===g).map(t=>{const p=prog(t.k);return `<a class="mg-t ${tcls(t)}" href="#${t.k}"><span class="tmark sm">${t.mark}</span><span>${t.name}</span>${p.d?`<small>${pct(p.p)}</small>`:''}</a>`}).join('')}</div>`).join('')}
   <div class="mg-foot"><a href="#katalog">Lihat katalog lengkap →</a><a href="#persiapan">Persiapan laptop →</a><span class="muted">${TRACKS.length} jalur · ${nLessons} pelajaran</span></div></div>`;
}
function drawerHTML(){
  return `<div class="dr-in"><div class="dr-h"><b>Menu</b><button class="icon-btn" id="drClose" aria-label="Tutup menu">✕</button></div>
   <nav class="dr-nav"><a href="#beranda">Beranda</a><a href="#katalog">Katalog</a><a href="#saya">Belajar saya</a><a href="#ulang">Ulang <span class="badge wrongN" hidden></span></a><a href="#kuis">Kuis cerita</a><a href="#glosarium">Glosarium</a><a href="#persiapan">Persiapan laptop</a></nav>
   ${GROUPS.map(([g,n])=>`<div class="dr-g"><div class="eyebrow">${n}</div>${TRACKS.filter(t=>t.g===g).map(t=>`<a class="mg-t ${tcls(t)}" href="#${t.k}"><span class="tmark sm">${t.mark}</span><span>${t.name}</span>${prog(t.k).d?`<small>${pct(prog(t.k).p)}</small>`:''}</a>`).join('')}</div>`).join('')}</div>`;
}
function setMega(o){const m=$('#mega'),b=$('#catBtn');o=o??m.hidden;m.hidden=!o;if(o)m.innerHTML=megaHTML();b.setAttribute('aria-expanded',o)}
function setDrawer(o){const d=$('#drawer'),b=$('#menuBtn');o=o??d.hidden;d.hidden=!o;b.setAttribute('aria-expanded',o);$('#scrim').classList.toggle('open',o);
  if(o){d.innerHTML=drawerHTML();updateBadges();$('#drClose').onclick=()=>setDrawer(false);$('#drClose').focus()}}

/* ---------- tema ---------- */
const THEMES=['auto','light','dark'],THL={auto:'Tema: ikuti sistem',light:'Tema: terang',dark:'Tema: gelap'},THI={auto:'◐',light:'☀',dark:'☾'};
function applyTheme(t){const r=document.documentElement;if(t==='auto')delete r.dataset.theme;else r.dataset.theme=t;const b=$('#themeBtn');if(b){b.textContent=THI[t];b.title=THL[t];b.setAttribute('aria-label',THL[t])}}
let THEME=store.get('rk-theme','auto');applyTheme(THEME);

/* keadaan glosarium dipakai rute dan tautan istilah, jadi dideklarasikan di sini */
let glState={q:'',cat:'Semua',focus:null},pendingFocus=null;
/* event pasang aplikasi (beforeinstallprompt) disimpan agar tombol Pasang bisa memakainya */
let INSTALL=null;

/* ---------- pencarian (Ctrl+K) ---------- */
let SIDX=null,sSel=0,sRes=[];
function searchIndex(){
  if(SIDX)return SIDX;SIDX=[];
  TRACKS.forEach(t=>{SIDX.push({k:'Jalur',t:t.name,s:t.h,h:'#'+t.k,tr:t});
    t.mods.forEach((m,mi)=>SIDX.push({k:'Modul',t:m.t,s:`${t.name} · Modul ${mi+1}`,h:'#'+FLAT[t.k].find(x=>x.mi===mi).id,tr:t}));
    FLAT[t.k].forEach(x=>{if(!x.src)SIDX.push({k:KIND[kindOf(x)],t:x.title,s:`${t.name} · Modul ${x.mi+1}`,h:'#'+x.id,tr:t,n:(x.l.nodes||[]).join(' ')})})});
  if(typeof GL!=='undefined')GL.forEach(g=>SIDX.push({k:'Istilah',t:g.t,s:g.en,h:'#glosarium',g:g.id}));
  [['Belajar saya','#saya'],['Daftar ulang soal','#ulang'],['Kuis cerita','#kuis'],['Katalog','#katalog']].forEach(([t,h])=>SIDX.push({k:'Halaman',t,s:'',h}));
  return SIDX;
}
const fold=s=>s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');
function doSearch(q){
  const w=fold(q).split(/\s+/).filter(Boolean);if(!w.length)return [];
  return searchIndex().map(e=>{const T=fold(e.t),all=T+' '+fold(e.s)+' '+fold(e.n||'');if(!w.every(x=>all.includes(x)))return null;
    let sc=(T.startsWith(w[0])?30:0)+(w.every(x=>T.includes(x))?20:0)+({Jalur:15,Modul:8,Halaman:6}[e.k]||0)-T.length/20;return {e,sc}}).filter(Boolean).sort((a,b)=>b.sc-a.sc).slice(0,30).map(r=>r.e);
}
function openSearch(){const p=$('#palette');p.hidden=false;if(!ready(['book']))need(['book']).then(()=>{SIDX=null;if(!p.hidden)drawSearch($('#sQ').value)},()=>{});$('#scrim').classList.add('open');const i=$('#sQ');i.value='';drawSearch('');setTimeout(()=>i.focus(),10)}
function closeSearch(){$('#palette').hidden=true;$('#scrim').classList.remove('open')}
function drawSearch(q){sRes=q.trim()?doSearch(q):TRACKS.filter(t=>LMS.last[t.k]).map(t=>({k:'Lanjutkan',t:resumeOf(t.k).title,s:t.name,h:'#'+resumeOf(t.k).id,tr:t}));sSel=0;
  $('#sList').innerHTML=sRes.length?sRes.map((r,i)=>`<li role="option" id="so${i}" aria-selected="${i===0}"><a href="${r.h}" data-g="${r.g||''}" class="${r.tr?tcls(r.tr):''}"><span class="s-k">${esc(r.k)}</span><span class="s-t"><b>${esc(r.t)}</b><small>${esc(r.s)}</small></span></a></li>`).join('')
   :`<li class="s-empty">${q.trim()?`Tidak ada hasil untuk "${esc(q)}".`:'Ketik untuk mencari jalur, modul, pelajaran, atau istilah.'}</li>`;
  $('#sQ').setAttribute('aria-activedescendant',sRes.length?'so0':'')}
function moveSel(d){if(!sRes.length)return;sSel=(sSel+d+sRes.length)%sRes.length;document.querySelectorAll('#sList [role=option]').forEach((li,i)=>li.setAttribute('aria-selected',i===sSel));const li=$('#so'+sSel);li.scrollIntoView({block:'nearest'});$('#sQ').setAttribute('aria-activedescendant','so'+sSel)}
function goSearch(a){if(a.dataset.g){glState={q:'',cat:'Semua',focus:a.dataset.g}}closeSearch();if(location.hash===a.getAttribute('href'))route();else location.hash=a.getAttribute('href')}

/* ---------- rute ---------- */
function setNav(tk,cur){
  document.querySelectorAll('#gmain [data-r]').forEach(a=>{if(a.dataset.r===cur)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
  document.documentElement.className=tk?'t-'+tk:'';document.documentElement.dataset.track=tk||'';
}
function route(){
  GL_LANG=null;clearTimers();toggleOutline(false);setMega(false);if(!$('#drawer').hidden)setDrawer(false);if(!$('#palette').hidden)closeSearch();
  let h=(location.hash||'#beranda').slice(1);
  const v=$('#view'),ol=$('#outline'),shell=$('#shell');
  const old=/^bab-(\d+)$/.exec(h);
  if(/^kuis-(dasar|menengah|lanjutan)$/.test(h)){location.replace('#kuis-java');return}
  const focusing=!!pendingFocus,x=BYID[h];
  let m;
  const want=old?['book']:x?needsOf(x.t.k):TK[h]?needsOf(h):(m=/^(\w+)-(tes|ujian-\d+|ringkasan-\d+)$/.exec(h))&&TK[m[1]]?needsOf(m[1])
    :/^kuis/.test(h)?['book','rt']:h==='glosarium'?['book']:[];
  if(!ready(want)){v.dataset.page='loading';v.innerHTML='<div class="loading" role="status"><span class="spin"></span>Memuat materi…</div>';
    need(want).then(()=>{if((location.hash||'#beranda').slice(1)===h)route()},()=>{v.innerHTML='<div class="loading err" role="alert"><p>Materi gagal dimuat. Periksa koneksi internet.</p><button class="btn primary" onclick="route()">Coba lagi</button></div>'});return}
  if(old){const y=labLesson(+old[1]);location.replace('#'+(y?y.id:'java'));return}
  shell.classList.toggle('has-ol',!!x);ol.hidden=!x;
  const page=(name,html,wire,title,tk='',cur='')=>{v.dataset.page=name;v.innerHTML=html;setNav(tk,cur);document.title=title+' · Ruang Kode';if(wire)wire()};
  if(x&&!isOpen(x)){shell.classList.remove('has-ol');ol.hidden=true;page('locked',renderLocked(x),null,`Terkunci · ${x.title}`,x.t.k);scrollTo(0,0);return}
  if(x){v.dataset.page='lesson';ol.innerHTML=renderOutline(x);v.innerHTML=renderLesson(x);setNav(x.t.k,'');document.title=`${x.title} · ${x.t.name} · Ruang Kode`;
    if(!focusing)scrollTo(0,0);wireLesson(x);const c=$('#outline [aria-current="page"]');if(c)c.scrollIntoView({block:'center'});
    v.classList.remove('enter');void v.offsetWidth;v.classList.add('enter');return}
  if(TK[h])page('course',renderCourse(TK[h]),()=>wireCourse(TK[h]),`Jalur ${TK[h].name}`,h);
  else if((m=/^(\w+)-tes$/.exec(h))&&TK[m[1]])page('quiz',renderPlacement(TK[m[1]]),wireExam,`Tes penempatan ${TK[m[1]].name}`,m[1]);
  else if((m=/^(\w+)-ujian-(\d+)$/.exec(h))&&TK[m[1]]&&TK[m[1]].mods[m[2]-1]&&!modDone(m[1],m[2]-1))page('locked',renderLockedExam(TK[m[1]],m[2]-1),null,'Ujian modul terkunci',m[1]);
  else if((m=/^(\w+)-ujian-(\d+)$/.exec(h))&&TK[m[1]]&&TK[m[1]].mods[m[2]-1])page('quiz',renderExam(TK[m[1]],m[2]-1),wireExam,`Ujian modul ${m[2]} ${TK[m[1]].name}`,m[1]);
  else if((m=/^(\w+)-ringkasan-(\d+)$/.exec(h))&&TK[m[1]]&&TK[m[1]].mods[m[2]-1])page('summary',renderSummary(TK[m[1]],m[2]-1),null,`Ringkasan modul ${m[2]} ${TK[m[1]].name}`,m[1]);
  else if((m=/^(\w+)-sertifikat$/.exec(h))&&TK[m[1]]){location.replace('#'+m[1]);return}
  else if((m=/^persiapan(?:-(\w+))?$/.exec(h))&&(!m[1]||TK[m[1]])){const tk=m[1]||'';page('setup',renderSetup(tk),()=>wireSetup(tk),'Persiapan laptop','','persiapan')}
  else if(h==='katalog')page('course',renderCatalog(),wireCatalog,'Katalog','','katalog');
  else if(h==='saya')page('quiz',renderMine(),wireMine,'Belajar saya','','saya');
  else if(h==='ulang')page('quiz',renderReview(),wireReview,'Ulang','','ulang');
  else if(/^kuis(-(java|python|sql))?$/.test(h)){const tk=h.split('-')[1]||'java';page('quiz',renderStories(tk),()=>wireStories(tk),'Kuis cerita','','kuis')}
  else if(h==='glosarium')page('glossary',renderGlossary(),wireGlossary,'Glosarium','','glosarium');
  else{page('home',renderHome(),wireHome,'Belajar coding, data & desain');document.title='Ruang Kode · Akademi coding, data & desain'}
  v.classList.remove('enter');void v.offsetWidth;v.classList.add('enter');
  if(!(h==='glosarium'&&document.querySelector('.gl.flash')))scrollTo(0,0);
}

/* ---------- peristiwa global ---------- */
document.addEventListener('click',e=>{
  const c=e.target.closest('.copy[data-copy]');if(c){copyFrom(c);return}
  const pa=e.target.closest('[data-proall]');if(pa){const o=pa.getAttribute('aria-expanded')!=='true';pa.closest('.pro-sec').querySelectorAll('details.pro').forEach(d=>d.open=o);pa.setAttribute('aria-expanded',o);pa.textContent=o?'Tutup semua':'Buka semua';return}
  const sa=e.target.closest('#sList a');if(sa){e.preventDefault();goSearch(sa);return}
  const tg=e.target.closest('[data-term]');if(tg&&!tg.closest('.gl')){glState={q:'',cat:'Semua',focus:tg.dataset.term};location.hash='glosarium';return}
  const b=e.target.closest('[data-to]');if(b){const t=document.querySelector(b.dataset.to);if(t)t.scrollIntoView({behavior:RM()?'auto':'smooth',block:'start'})}
  if(!$('#mega').hidden&&!e.target.closest('#mega,#catBtn'))setMega(false);
});
$('#catBtn').onclick=()=>setMega();
$('#menuBtn').onclick=()=>setDrawer();
$('#srchBtn').onclick=openSearch;
$('#themeBtn').onclick=()=>{THEME=THEMES[(THEMES.indexOf(THEME)+1)%3];store.set('rk-theme',THEME);applyTheme(THEME);toast(THL[THEME])};
$('#scrim').onclick=()=>{toggleOutline(false);setDrawer(false);closeSearch()};
$('#sQ').addEventListener('input',e=>drawSearch(e.target.value));
$('#sQ').addEventListener('keydown',e=>{if(e.key==='ArrowDown'){e.preventDefault();moveSel(1)}else if(e.key==='ArrowUp'){e.preventDefault();moveSel(-1)}else if(e.key==='Enter'){const a=$(`#so${sSel} a`);if(a){e.preventDefault();goSearch(a)}}});
document.addEventListener('keydown',e=>{
  if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();$('#palette').hidden?openSearch():closeSearch();return}
  if(e.key==='/'&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)&&$('#palette').hidden){e.preventDefault();openSearch();return}
  if(e.key==='Escape'){if(!$('#palette').hidden)closeSearch();else if(!$('#mega').hidden){setMega(false);$('#catBtn').focus()}else if(!$('#drawer').hidden)setDrawer(false);else if($('#outline').classList.contains('open'))toggleOutline(false)}
});
addEventListener('scroll',()=>{const p=$('#rprog');if(!p)return;const d=document.documentElement,mx=d.scrollHeight-innerHeight;p.style.transform=`scaleX(${mx>0&&BYID[location.hash.slice(1)]?Math.min(1,scrollY/mx):0})`},{passive:true});
addEventListener('hashchange',route);
updateBadges();route();

/* ---------- versi web: siapkan materi lebih awal dan pasang service worker (offline) ---------- */
addEventListener('beforeinstallprompt',e=>{e.preventDefault();INSTALL=e;document.querySelectorAll('#instBtn,#suInst').forEach(b=>b.hidden=false)});
if(CHUNK){
  (window.requestIdleCallback||(f=>setTimeout(f,1500)))(()=>need(['rt',...recent().slice(0,2).flatMap(t=>needsOf(t.k))]).catch(()=>{}));
  if('serviceWorker' in navigator&&(location.protocol==='https:'||location.hostname==='localhost'))navigator.serviceWorker.register('/sw.js').then(r=>{
    if(!navigator.serviceWorker.controller)r.addEventListener('updatefound',()=>{const w=r.installing;if(w)w.addEventListener('statechange',()=>{if(w.state==='activated')toast('Ruang Kode siap dipakai offline')})})}).catch(()=>{});
}
