/* ===================== NAVIGASI, PENCARIAN, TEMA & RUTE ===================== */
function megaHTML(){
  return `<div class="mega-in">${GROUPS.map(([g,n])=>`<div class="mg-col"><div class="eyebrow">${n}</div>${TRACKS.filter(t=>t.g===g).map(t=>{const p=prog(t.k);return `<a class="mg-t ${tcls(t)}" href="#${t.k}"><span class="tmark sm">${t.mark}</span><span>${t.name}</span>${p.d?`<small>${pct(p.p)}</small>`:''}</a>`}).join('')}</div>`).join('')}
   <div class="mg-foot"><a href="#katalog">Lihat katalog lengkap →</a><span class="muted">${TRACKS.length} jalur · ${nLessons} pelajaran</span></div></div>`;
}
function drawerHTML(){
  return `<div class="dr-in"><div class="dr-h"><b>Menu</b><button class="icon-btn" id="drClose" aria-label="Tutup menu">✕</button></div>
   <nav class="dr-nav"><a href="#beranda">Beranda</a><a href="#katalog">Katalog</a><a href="#saya">Belajar saya</a><a href="#ulang">Ulang <span class="badge wrongN" hidden></span></a><a href="#kuis">Kuis cerita</a><a href="#glosarium">Glosarium</a></nav>
   ${GROUPS.map(([g,n])=>`<div class="dr-g"><div class="eyebrow">${n}</div>${TRACKS.filter(t=>t.g===g).map(t=>`<a class="mg-t ${tcls(t)}" href="#${t.k}"><span class="tmark sm">${t.mark}</span><span>${t.name}</span>${prog(t.k).d?`<small>${pct(prog(t.k).p)}</small>`:''}</a>`).join('')}</div>`).join('')}</div>`;
}
function setMega(o){const m=$('#mega'),b=$('#catBtn');o=o??m.hidden;m.hidden=!o;if(o)m.innerHTML=megaHTML();b.setAttribute('aria-expanded',o)}
function setDrawer(o){const d=$('#drawer'),b=$('#menuBtn');o=o??d.hidden;d.hidden=!o;b.setAttribute('aria-expanded',o);$('#scrim').classList.toggle('open',o);
  if(o){d.innerHTML=drawerHTML();updateBadges();$('#drClose').onclick=()=>setDrawer(false);$('#drClose').focus()}}

/* ---------- tema ---------- */
const THEMES=['auto','light','dark'],THL={auto:'Tema: ikuti sistem',light:'Tema: terang',dark:'Tema: gelap'},THI={auto:'◐',light:'☀',dark:'☾'};
function applyTheme(t){const r=document.documentElement;if(t==='auto')delete r.dataset.theme;else r.dataset.theme=t;const b=$('#themeBtn');if(b){b.textContent=THI[t];b.title=THL[t];b.setAttribute('aria-label',THL[t])}}
let THEME=store.get('rk-theme','auto');applyTheme(THEME);

/* ---------- pencarian (Ctrl+K) ---------- */
let SIDX=null,sSel=0,sRes=[];
function searchIndex(){
  if(SIDX)return SIDX;SIDX=[];
  TRACKS.forEach(t=>{SIDX.push({k:'Jalur',t:t.name,s:t.h,h:'#'+t.k,tr:t});
    t.mods.forEach((m,mi)=>SIDX.push({k:'Modul',t:m.t,s:`${t.name} · Modul ${mi+1}`,h:'#'+FLAT[t.k].find(x=>x.mi===mi).id,tr:t}));
    FLAT[t.k].forEach(x=>{if(!x.src)SIDX.push({k:KIND[kindOf(x)],t:x.title,s:`${t.name} · Modul ${x.mi+1}`,h:'#'+x.id,tr:t,n:(x.l.nodes||[]).join(' ')})})});
  GL.forEach(g=>SIDX.push({k:'Istilah',t:g.t,s:g.en,h:'#glosarium',g:g.id}));
  [['Belajar saya','#saya'],['Daftar ulang soal','#ulang'],['Kuis cerita','#kuis'],['Katalog','#katalog']].forEach(([t,h])=>SIDX.push({k:'Halaman',t,s:'',h}));
  return SIDX;
}
const fold=s=>s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');
function doSearch(q){
  const w=fold(q).split(/\s+/).filter(Boolean);if(!w.length)return [];
  return searchIndex().map(e=>{const T=fold(e.t),all=T+' '+fold(e.s)+' '+fold(e.n||'');if(!w.every(x=>all.includes(x)))return null;
    let sc=(T.startsWith(w[0])?30:0)+(w.every(x=>T.includes(x))?20:0)+({Jalur:15,Modul:8,Halaman:6}[e.k]||0)-T.length/20;return {e,sc}}).filter(Boolean).sort((a,b)=>b.sc-a.sc).slice(0,30).map(r=>r.e);
}
function openSearch(){const p=$('#palette');p.hidden=false;$('#scrim').classList.add('open');const i=$('#sQ');i.value='';drawSearch('');setTimeout(()=>i.focus(),10)}
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
  clearTimers();toggleOutline(false);setMega(false);if(!$('#drawer').hidden)setDrawer(false);if(!$('#palette').hidden)closeSearch();
  let h=(location.hash||'#beranda').slice(1);
  const v=$('#view'),ol=$('#outline'),shell=$('#shell');
  const old=/^bab-(\d+)$/.exec(h);
  if(old){const x=labLesson(+old[1]);location.replace('#'+(x?x.id:'java'));return}
  if(/^kuis-(dasar|menengah|lanjutan)$/.test(h)){location.replace('#kuis-java');return}
  const focusing=!!pendingFocus,x=BYID[h];
  let m;
  shell.classList.toggle('has-ol',!!x);ol.hidden=!x;
  const page=(name,html,wire,title,tk='',cur='')=>{v.dataset.page=name;v.innerHTML=html;setNav(tk,cur);document.title=title+' · Ruang Kode';if(wire)wire()};
  if(x){v.dataset.page='lesson';ol.innerHTML=renderOutline(x);v.innerHTML=renderLesson(x);setNav(x.t.k,'');document.title=`${x.title} · ${x.t.name} · Ruang Kode`;
    if(!focusing)scrollTo(0,0);wireLesson(x);const c=$('#outline [aria-current="page"]');if(c)c.scrollIntoView({block:'center'});
    v.classList.remove('enter');void v.offsetWidth;v.classList.add('enter');return}
  if(TK[h])page('course',renderCourse(TK[h]),()=>wireCourse(TK[h]),`Jalur ${TK[h].name}`,h);
  else if((m=/^(\w+)-tes$/.exec(h))&&TK[m[1]])page('quiz',renderPlacement(TK[m[1]]),wireExam,`Tes penempatan ${TK[m[1]].name}`,m[1]);
  else if((m=/^(\w+)-ujian-(\d+)$/.exec(h))&&TK[m[1]]&&TK[m[1]].mods[m[2]-1])page('quiz',renderExam(TK[m[1]],m[2]-1),wireExam,`Ujian modul ${m[2]} ${TK[m[1]].name}`,m[1]);
  else if((m=/^(\w+)-sertifikat$/.exec(h))&&TK[m[1]])page('quiz',renderCert(TK[m[1]]),()=>wireCert(TK[m[1]]),`Sertifikat ${TK[m[1]].name}`,m[1]);
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
