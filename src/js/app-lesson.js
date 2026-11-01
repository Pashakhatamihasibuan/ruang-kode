/* ===================== RUANG PELAJARAN =====================
   Jenis: lab/topic (Java & Python lama), c (konsep + kode), s (SQL), w (editor + pratinjau),
   proj (proyek akhir), see (pinjam pelajaran jalur lain). */
function renderOutline(x){
  const t=x.t,p=prog(t.k);
  return `<div class="ol-head"><a class="ol-t ${tcls(t)}" href="#${t.k}"><span class="tmark">${t.mark}</span><span><b>${t.name}</b><small>${p.d} dari ${p.n} selesai</small></span></a><div class="bar"><i style="width:${p.p*100}%"></i></div></div>
  <nav class="ol-nav" aria-label="Daftar materi ${t.name}">${t.mods.map((m,mi)=>{const mp=modProg(t.k,mi);return `<details ${mi===x.mi?'open':''}><summary><span class="ol-n">${mp.d===mp.n?'✓':mi+1}</span><span>${m.t}</span><small>${mp.d}/${mp.n}</small></summary>
    <ol>${FLAT[t.k].filter(y=>y.mi===mi).map(y=>`<li><a href="#${y.id}" class="${isDone(y)?'done':isOpen(y)?'':'locked'}" ${y.id===x.id?'aria-current="page"':''}><span class="chk" aria-hidden="true"></span>${esc(y.title)}${isOpen(y)?'':'<span class="sr">(terkunci)</span>'}</a></li>`).join('')}</ol></details>`}).join('')}</nav>`;
}
/* halaman pengganti untuk pelajaran yang belum terbuka */
function renderLocked(x){
  const t=x.t,need=nextOf(t.k),pv=lockOf(x);
  return `<div class="lock-pg ${tcls(t)}"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><a href="#${t.k}">${t.name}</a><span>/</span><span>Modul ${x.mi+1}</span></nav>
   <div class="lock-ic" aria-hidden="true">🔒</div><div class="eyebrow">Modul ${x.mi+1} · Pelajaran ${x.li+1}</div><h1>${esc(x.title)}</h1>
   <p class="lead">Pelajaran ini belum terbuka. Materi di Ruang Kode disusun bertahap: setiap pelajaran memakai bekal dari pelajaran sebelumnya, jadi kerjakan berurutan.</p>
   ${pv?`<p>Selesaikan dulu <b>${esc(pv.title)}</b>.</p>`:''}
   <div class="lock-act"><a class="btn primary" href="#${need.id}">Lanjut ke ${esc(need.title)} ▶</a><a class="btn" href="#${t.k}">Lihat kurikulum</a></div>
   <p class="muted small">Sudah menguasai materinya? Ikuti <a href="#${t.k}-tes">tes penempatan</a> untuk melewati modul yang sudah kamu kuasai.</p></div>`;
}
function renderLockedExam(t,mi){const mp=modProg(t.k,mi);
  return `<div class="lock-pg ${tcls(t)}"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><a href="#${t.k}">${t.name}</a></nav>
   <div class="lock-ic" aria-hidden="true">🔒</div><div class="eyebrow">Ujian modul ${mi+1}</div><h1>${esc(t.mods[mi].t)}</h1>
   <p class="lead">Ujian modul terbuka setelah semua pelajaran di modul ini selesai. Saat ini ${mp.d} dari ${mp.n} pelajaran selesai.</p>
   <div class="lock-act"><a class="btn primary" href="#${nextOf(t.k).id}">Lanjutkan belajar ▶</a><a class="btn" href="#${t.k}">Lihat kurikulum</a></div></div>`}
function renderLesson(x){
  const {t,m,mi,li}=x,y=base(x),l=y.l,F=FLAT[t.k],i=F.indexOf(x),prev=F[i-1],next=F[i+1],dn=isDone(x);
  if(!x.src&&l.k==='see')return `<p class="empty">Pelajaran rujukan tidak ditemukan.</p>`;
  let body='';
  if(l.k==='lab')body=labHTML(l.n,y.t.lang);
  else if(l.k==='topic')body=topicHTML1(l.ref,y.t.lang);
  else if(l.k==='c')body=conceptHTML(l,y.t);
  else if(l.k==='w')body=webHTML(l);
  else if(l.k==='proj')body=projHTML(l,y);
  else body=sqlLessonHTML(l);
  return `<div class="l-top"><button class="btn ol-btn" id="olBtn" aria-controls="outline" aria-expanded="false">☰ Daftar materi</button>
   <nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><a href="#${t.k}">${t.name}</a><span>/</span><span>Modul ${mi+1}</span></nav></div>
  <header class="l-head ${tcls(t)}"><div class="eyebrow">Modul ${mi+1}: ${m.t} · Pelajaran ${li+1} dari ${m.lessons.length}</div>
   <h1>${esc(x.title)}</h1>
   <div class="l-meta"><span class="kchip k-${l.k}">${KIND[kindOf(x)]}</span><span>±${minOf(x)} menit</span><span>${m.lvl}</span>${dn?'<span class="okc">✓ Selesai</span>':''}</div>
   ${x.src?`<p class="borrow ${tcls(y.t)}"><span class="tmark sm">${y.t.mark}</span>Pelajaran ini juga ada di jalur <a href="#${y.id}">${y.t.name}</a>. Progresnya tersimpan bersama, jadi cukup dikerjakan sekali.</p>`:''}
   ${nodesHTML(l.nodes)}</header>
  <div class="l-body">${body}</div>
  <footer class="l-foot"><div class="lf-done">${dn?'<span class="okc">✓ Pelajaran ini sudah selesai.</span> <button class="tlink" id="undo">Tandai belum selesai</button>':'<span>Sudah paham? Jawab kuisnya lalu tandai selesai untuk membuka pelajaran berikutnya (+10 XP).</span>'}</div>
   <p class="need-q" id="needQ" role="alert" hidden></p>
   <div class="lf-nav">${prev?`<a class="btn" href="#${prev.id}" title="${esc(prev.title)}">◀ Sebelumnya</a>`:`<a class="btn" href="#${t.k}">◀ Kurikulum</a>`}
   <button class="btn primary" id="doneNext">${next?(dn?'Lanjut':'Selesai, lanjut')+' ▶':(dn?'Kembali ke kurikulum':'Selesaikan jalur 🎉')}</button></div>
   ${next?`<a class="lf-next" href="#${next.id}"><small>Berikutnya${next.mi!==mi?` · Modul ${next.mi+1}`:''}</small><b>${esc(next.title)}</b></a>`:''}
   ${!next||next.mi!==mi?`<a class="lf-exam" href="#${t.k}-ringkasan-${mi+1}">📄 Baca ringkasan modul ${mi+1} sebelum lanjut →</a>`:''}
   ${next&&next.mi!==mi&&bankOf(t.k,mi).length>=3?`<a class="lf-exam" href="#${t.k}-ujian-${mi+1}">📝 Modul ${mi+1} selesai? Coba ujian modulnya dulu →</a>`:''}</footer>`;
}
function wireLesson(x){
  const {t}=x,y=base(x),l=y.l,F=FLAT[t.k],next=F[F.indexOf(x)+1];
  LMS.last[t.k]=x.id;LMS.lastAt[t.k]=Date.now();touch();saveLms();
  $('#olBtn').onclick=()=>toggleOutline();
  /* pelajaran baru dianggap selesai setelah semua soal Cek pemahaman dijawab */
  $('#doneNext').onclick=()=>{
    const left=isDone(x)?[]:[...document.querySelectorAll('#view .quiz .q')].filter(q=>!q.matches('.is-ok,.is-bad'));
    if(left.length){const m=$('#needQ');m.hidden=false;m.textContent=`Jawab dulu ${left.length} soal di bagian kuis sebelum lanjut. Jawaban salah tidak menghalangi, soalnya akan masuk daftar Ulang.`;
      left[0].scrollIntoView({behavior:RM()?'auto':'smooth',block:'center'});left[0].classList.add('flash');setTimeout(()=>left[0].classList.remove('flash'),1600);return}
    markDone(x);location.hash=next?next.id:t.k};
  const u=$('#undo');if(u)u.onclick=()=>{delete LMS.done[y.id];saveLms();route()};
  linkTerms($('#view .l-body'));
  if(l.k==='lab')wireLab(l.n,y.t.lang);
  else if(l.k==='topic')wireTopic1(l.ref,y.t.lang);
  else if(l.k==='c')wireConcept(l,y.t,x);
  else if(l.k==='w')wireWeb(l,x);
  else if(l.k==='proj')wireProj(l,x);
  else wireSql(l,x);
}
function toggleOutline(o){const ol=$('#outline');o=o??!ol.classList.contains('open');ol.classList.toggle('open',o);$('#scrim').classList.toggle('open',o);const b=$('#olBtn');if(b)b.setAttribute('aria-expanded',o)}
const vizHTML=(l,hint)=>l.viz&&VIZ2[l.viz]?`<section class="viz" id="lab"><div class="viz-head"><span class="eyebrow">Visual interaktif</span><h3>${VIZ2T[l.viz]}</h3>${hint?`<p>${hint}</p>`:''}</div><div id="vizHost" class="vizhost"></div></section>`:'';
/* kode pemula vs kode rapi: tersembunyi sampai dibuka, agar siswa sempat menebak dulu */
const proHTML=l=>l.pro&&l.pro.length?`<section class="section pro-sec" id="pro"><div class="sec-h row"><h2>Kode pemula vs kode rapi</h2><button class="tlink" data-proall aria-expanded="false">Buka semua</button></div>
  <p class="muted">Dua cara menulis hal yang sama. Coba tebak dulu apa kelebihan versi rapi, lalu buka untuk membandingkan.</p>
  ${l.pro.map(p=>{const lang=p.lang,o=p.out!=null?`<div class="pro-out"><div class="eyebrow">Keluaran keduanya sama</div><pre class="out">${esc(p.out)}</pre></div>`
    :p.outA!=null?`<div class="pro-out two"><div><div class="eyebrow">Keluaran kode pemula</div><pre class="out">${esc(p.outA)}</pre></div><div><div class="eyebrow">Keluaran kode rapi</div><pre class="out">${esc(p.outB)}</pre></div></div>`:'';
   return `<details class="pro"><summary><span class="pro-tag">${esc(p.tag)}</span><b>${esc(p.t)}</b></summary><div class="pro-in">
    <div class="pro-grid"><div class="pro-a">${pane(lang,p.a,{label:'✗ KODE PEMULA'})}</div><div class="pro-b">${pane(lang,p.b,{label:'✓ KODE RAPI'})}</div></div>${o}<p class="pro-why">${p.why}</p></div></details>`}).join('')}</section>`:'';
const ptsHTML=l=>proHTML(l)+(l.pts&&l.pts.length?`<section class="section"><h2>Poin penting</h2><ul class="points">${l.pts.map(p=>`<li>${p}</li>`).join('')}</ul></section>`:'');
const qHTML=l=>(l.q||[]).length?`<section class="section" id="quiz"><h2>Cek pemahaman</h2>${quizHTML(l.q.map(normQ),l.t.length)}</section>`:'';
const wireQ=l=>{const q=$('#quiz');if(q)wireQuiz(q,l.q.map(normQ))};

/* ---------- editor kode dengan sorotan sintaks ---------- */
function editorHTML(id,val,label,lang='sql',ph='Tulis kode di sini…'){return `<div class="ed" id="${id}" data-lang="${lang}"><pre class="ed-hl code" aria-hidden="true">${hl(val,lang)}\n</pre><textarea spellcheck="false" autocapitalize="off" autocomplete="off" aria-label="${label}" placeholder="${ph}">${esc(val)}</textarea></div>`}
function wireEditor(box,onRun,onInput){
  const ta=$('textarea',box),pre=$('.ed-hl',box),lang=box.dataset.lang||'sql';
  const sync=()=>{pre.innerHTML=hl(ta.value,lang)+'\n';ta.style.height='auto';ta.style.height=Math.max(96,ta.scrollHeight+2)+'px';pre.style.height=ta.style.height;pre.scrollLeft=ta.scrollLeft};
  ta.addEventListener('input',()=>{sync();if(onInput)onInput()});ta.addEventListener('scroll',()=>{pre.scrollTop=ta.scrollTop;pre.scrollLeft=ta.scrollLeft});
  ta.addEventListener('keydown',e=>{
    if((e.ctrlKey||e.metaKey)&&e.key==='Enter'){e.preventDefault();onRun&&onRun()}
    else if(e.key==='Tab'&&!e.shiftKey&&!e.ctrlKey&&!e.altKey){const s=ta.selectionStart,en=ta.selectionEnd;if(s===en){e.preventDefault();ta.setRangeText('  ',s,en,'end');sync()}}});
  requestAnimationFrame(sync);
  return {get:()=>ta.value,set:v=>{ta.value=v;sync()},ta};
}

/* ---------- jenis c: konsep + kode ---------- */
const PYOK=['python'];
function conceptHTML(l,t){
  const lang=l.lang||t.lang,live=l.code&&l.out!=null&&l.run!==false,py=live&&lang==='python';
  return `<section class="prose">${l.b.map(p=>`<p>${p}</p>`).join('')}</section>
  ${vizHTML(l,'Coba kontrolnya atau tekan Berikutnya, lalu perhatikan apa yang berubah.')}
  ${l.code?`<section class="section" id="prog"><h2>${lang==='text'?'Contoh':'Contoh kode'}</h2>
   ${py?`<div class="pane python"><div class="pane-h"><span>PYTHON · bisa diedit</span><button class="copy" data-copyed>Salin</button></div>${editorHTML('pyEd',l.code,'Editor Python','python')}</div>`:pane(lang,l.code)}
   ${l.out!=null?(l.run===false?`<div><div class="eyebrow">Contoh keluaran</div><div class="console">${esc(l.out)}</div></div>`
     :`<details class="guess" id="guess"><summary>🤔 Tebak keluarannya dulu sebelum menjalankan</summary><textarea class="bk" id="gIn" placeholder="Tulis keluaran yang kamu perkirakan, satu baris per baris"></textarea><div class="sl-act"><button class="btn" id="gChk">Periksa tebakan</button></div><div id="gFb" aria-live="polite"></div></details>
      <div class="runbox"><button class="btn primary" id="runBtn">▶ Jalankan</button>${trBtn(l)}${py?'<button class="btn" id="pyReset">Kembalikan kode</button>':''}<span class="rb-hint">${py?'Ubah kodenya lalu jalankan. Kode asli menampilkan keluaran yang sudah diuji; kode yang diubah dijalankan dengan Python di browser (Pyodide).':`Keluaran kode ini sudah diuji dengan ${({java:'Java 21',ts:'Node 22 (TypeScript)',js:'Node 22',sql:'mesin SQL Ruang Kode',bash:'Bash'})[lang]||'Python 3.13'}.`}</span></div><div class="console run" id="runOut" hidden></div>${tracerHTML(l,lang)}`):''}</section>`:''}
  ${practiceHTML(l,lang)}${ptsHTML(l)}${qHTML(l)}`;
}
let PY=null,PYFAIL=false;
function loadPy(){
  if(PY)return PY;
  PY=new Promise((res,rej)=>{const s=document.createElement('script');s.src='https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js';
    const to=setTimeout(()=>rej(new Error('waktu habis')),45000);
    s.onload=()=>{try{loadPyodide({indexURL:'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/'}).then(p=>{clearTimeout(to);res(p)},rej)}catch(e){rej(e)}};s.onerror=()=>rej(new Error('tidak bisa diunduh'));document.head.appendChild(s)});
  PY.catch(()=>{PYFAIL=true;PY=null});return PY;
}
async function runPy(code,onOut){
  const py=await loadPy();let out='';const push=s=>{out+=s+'\n';onOut(out)};
  py.setStdout({batched:push});py.setStderr({batched:push});
  const bad=[];await py.loadPackagesFromImports(code,{messageCallback:m=>{if(/^Loading /.test(m)&&!out)onOut('Memuat paket '+m.slice(8)+'…')},errorCallback:m=>bad.push(m)});
  if(bad.length){const n=[...new Set(bad.join(' ').match(/[a-z_]+(?=-\d)/g)||[])].join(', ');push(`Paket ${n||"yang dibutuhkan kode ini"} gagal diunduh. Periksa koneksi internet lalu jalankan lagi.`);return out}
  out='';onOut('');
  const g=py.globals.get('dict')();
  try{await py.runPythonAsync(code,{globals:g})}catch(e){const m=String(e.message||e).trim().split('\n'),i=m.findIndex(s=>/^\s*File "<exec>"/.test(s));
    push(i>=0?['Traceback (most recent call last):',...m.slice(i)].join('\n'):m.slice(-2).join('\n'));const fh=pyFriendly(m.join('\n'));if(fh)push('\n💡 '+fh)}
  finally{g.destroy&&g.destroy()}
  return out;
}
const normOut=s=>s.replace(/\r/g,'').split('\n').map(x=>x.replace(/\s+$/,'')).join('\n').trim();
function wireConcept(l,t,x){
  if(l.viz&&VIZ2[l.viz])VIZ2[l.viz]($('#vizHost'),{lang:t.lang,lesson:l});
  const rb=$('#runBtn'),box=$('#runOut'),ed=$('#pyEd')?wireEditor($('#pyEd'),()=>rb&&rb.click()):null;
  const typeOut=(txt,done)=>{box.hidden=false;box.classList.remove('err');box.textContent='';const lines=txt.split('\n');let k=0;
    const step=()=>{box.textContent+=(k?'\n':'')+lines[k];k++;if(k<lines.length)TIMERS.push(setTimeout(step,RM()?0:90));else done&&done()};TIMERS.push(setTimeout(step,RM()?0:200))};
  if(rb)rb.onclick=async()=>{const code=ed?ed.get():l.code;rb.disabled=true;rb.textContent='Berjalan…';const fin=()=>{rb.disabled=false;rb.textContent='↻ Jalankan lagi'};
    if(!ed||code.trim()===l.code.trim()){typeOut(l.out,fin);return}
    if(PYFAIL){box.hidden=false;box.classList.add('err');box.textContent='Python di browser (Pyodide) tidak bisa dimuat di halaman ini, misalnya karena koneksi atau pembatasan keamanan. Buka versi web Ruang Kode untuk menjalankan kode yang diubah, atau tekan "Kembalikan kode" untuk melihat keluaran aslinya.';fin();return}
    box.hidden=false;box.classList.remove('err');box.textContent='Memuat Python di browser (sekali saja, ±10 MB)…';
    try{const o=await runPy(code,s=>{box.textContent=s});if(!o)box.textContent='(program selesai tanpa keluaran)'}
    catch(e){box.classList.add('err');box.textContent=`Python di browser gagal dimuat (${e.message}). Coba lagi nanti, atau tekan "Kembalikan kode" untuk melihat keluaran asli.`}
    fin()};
  const pr=$('#pyReset');if(pr)pr.onclick=()=>{ed.set(l.code);box.hidden=true};
  const ce=$('[data-copyed]');if(ce)ce.onclick=e=>{e.stopPropagation();copyText(ed.get(),ce)};
  const gc=$('#gChk');if(gc)gc.onclick=()=>{const g=normOut($('#gIn').value),a=normOut(l.out),fb=$('#gFb');
    if(!g){fb.innerHTML='<p class="muted">Tulis dulu tebakanmu.</p>';return}
    if(g===a){fb.innerHTML='<div class="tk-fb ok"><b>✓ Tepat sekali!</b> Kamu membaca kodenya seperti komputer.</div>';const k='g'+qkey(l.code);if(!LMS.qok[k]){LMS.qok[k]=1;award(3,'· Tebakan tepat')}}
    else{const G=g.split('\n'),A=a.split('\n'),same=A.filter((v,i)=>G[i]===v).length;fb.innerHTML=`<div class="tk-fb bad"><b>Belum tepat.</b> ${same} dari ${A.length} baris sudah cocok. Jalankan kodenya untuk membandingkan.</div>`}};
  wirePractice(l,l.lang||t.lang);wireTracer(l);
  wireQ(l);
}

/* pesan error JavaScript yang umum, dijelaskan dalam bahasa sehari-hari */
const JSERR=[
  [/(\S+) is not defined/,m=>`Nama "${m[1]}" belum dibuat. Periksa ejaannya (huruf besar-kecil berpengaruh), atau buat dulu dengan let, const, atau function.`],
  [/Cannot read propert(?:y|ies) of (undefined|null)(?: \(reading '([^']+)'\))?/,m=>`Kamu mengambil ${m[2]?`.${m[2]}`:'properti'} dari nilai yang ${m[1]==='null'?'null (kosong)':'undefined (belum ada)'}. Sering terjadi saat querySelector tidak menemukan elemen, atau data belum dimuat. Periksa nama selector atau isi variabelnya.`],
  [/Cannot set propert(?:y|ies) of (undefined|null)/,()=>`Kamu mengisi properti pada nilai yang kosong. Biasanya elemen yang dicari dengan querySelector tidak ditemukan; cek kembali id atau class-nya.`],
  [/(\S+) is not a function/,m=>`"${m[1]}" bukan fungsi, jadi tidak bisa dipanggil dengan (). Periksa ejaan nama method-nya, atau pastikan nilainya memang fungsi.`],
  [/Assignment to constant variable/,()=>`Variabel const tidak boleh diisi ulang. Pakai let jika nilainya memang perlu berubah.`],
  [/Identifier '([^']+)' has already been declared/,m=>`Nama "${m[1]}" dibuat dua kali. Hapus let/const yang kedua, atau pakai nama lain.`],
  [/Unexpected end of input/,()=>`Kode berhenti sebelum selesai. Biasanya ada kurung kurawal }, kurung ), atau kutip yang belum ditutup.`],
  [/Unexpected token '?([^' ]+)'?/,m=>`Ada tanda "${m[1]}" di tempat yang tidak diharapkan. Periksa tanda baca di sekitarnya: koma, titik koma, kurung, atau kutip.`],
  [/Invalid or unexpected token/,()=>`Ada karakter yang tidak dikenali. Sering karena kutip miring (“ ”) hasil salin dari dokumen; ganti dengan kutip biasa " atau '.`],
  [/missing \) after argument list/,()=>`Kurung tutup ) kurang saat memanggil fungsi, atau ada koma/kutip yang terlewat di antara argumen.`],
  [/(\S+) is not iterable/,m=>`"${m[1]}" tidak bisa diulang dengan for...of atau spread (...). Pastikan nilainya array atau string.`],
  [/Failed to fetch|NetworkError/,()=>`Permintaan ke server gagal. Periksa alamat URL dan koneksi internet.`],
  [/Unexpected token .* in JSON|is not valid JSON|JSON\.parse/,()=>`Teks yang dibaca bukan JSON yang valid. Kunci dan teks di JSON wajib memakai kutip ganda.`]];
const PYERR=[
  [/NameError: name '([^']+)' is not defined/,m=>`Nama "${m[1]}" belum dibuat. Periksa ejaannya (huruf besar-kecil berpengaruh) atau buat dulu variabelnya sebelum dipakai.`],
  [/IndentationError/,()=>`Indentasi (spasi di awal baris) tidak rapi. Isi blok setelah tanda titik dua (:) harus menjorok sama dalam, biasanya 4 spasi.`],
  [/SyntaxError: (?:invalid syntax|expected ':')/,()=>`Penulisan kode tidak sesuai aturan Python. Periksa titik dua (:) setelah if/for/def, kurung, dan kutip di baris yang ditunjuk.`],
  [/SyntaxError: unterminated string/,()=>`Teks belum ditutup. Pastikan kutip pembuka dan penutupnya sama.`],
  [/SyntaxError: '\(' was never closed|SyntaxError: unexpected EOF/,()=>`Ada kurung yang belum ditutup.`],
  [/TypeError: can only concatenate str \(not "(\w+)"\) to str/,m=>`Teks tidak bisa langsung digabung dengan ${m[1]}. Ubah dulu dengan str(...), atau pakai f-string seperti f"Total: {angka}".`],
  [/TypeError: unsupported operand type/,()=>`Operasi ini tidak bisa dilakukan pada dua tipe data tersebut, misalnya teks ditambah angka. Samakan dulu tipenya dengan int(), float(), atau str().`],
  [/ZeroDivisionError/,()=>`Pembagian dengan nol. Periksa dulu pembaginya dengan if sebelum membagi.`],
  [/IndexError: list index out of range/,()=>`Indeks melewati panjang list. Ingat indeks dimulai dari 0, jadi indeks terakhir adalah len(data) - 1.`],
  [/KeyError: (.+)/,m=>`Kunci ${m[1]} tidak ada di dictionary. Periksa ejaannya, atau pakai .get(kunci) yang mengembalikan None jika tidak ada.`],
  [/ValueError: invalid literal for int\(\)/,()=>`Teks itu tidak bisa diubah menjadi angka bulat. Pastikan isinya hanya digit, atau pakai float() untuk angka desimal.`],
  [/AttributeError: '(\w+)' object has no attribute '(\w+)'/,m=>`Tipe ${m[1]} tidak punya method atau atribut "${m[2]}". Periksa ejaannya atau tipe datanya.`],
  [/ModuleNotFoundError: No module named '([^']+)'/,m=>`Modul "${m[1]}" tidak tersedia di sini. Di laptop, pasang dulu dengan pip install ${m[1]}.`]];
const pyFriendly=msg=>{for(const [rx,f] of PYERR){const m=rx.exec(msg);if(m)return f(m)}return ''};
function jsFriendly(msg){for(const [rx,f] of JSERR){const m=rx.exec(msg);if(m)return f(m)}return ''}

/* ---------- jenis w: editor HTML/CSS/JS/React + pratinjau ---------- */
const REACT_CDN=['https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js','https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js','https://cdn.jsdelivr.net/npm/@babel/standalone@7.26.4/babel.min.js'];
let WID=0;
function webTabs(l){return [l.html!=null&&['html','HTML','html'],l.css!=null&&['css','CSS','css'],l.js!=null&&['js',l.react?'JSX':'JavaScript',l.react?'jsx':'js']].filter(Boolean)}
function webHTML(l){
  const tabs=webTabs(l);
  return `<section class="prose">${l.b.map(p=>`<p>${p}</p>`).join('')}</section>
  ${vizHTML(l,'Coba kontrolnya, lalu perhatikan apa yang berubah.')}
  <section class="wlab" id="wlab"><div class="w-head"><div class="w-tabs" role="tablist">${tabs.map(([k,n],i)=>`<button role="tab" data-t="${k}" aria-selected="${i===0}">${n}</button>`).join('')}</div>
    <div class="w-act"><button class="btn primary" id="wRun">▶ Jalankan <kbd>Ctrl</kbd><kbd>Enter</kbd></button><button class="btn" id="wReset">Reset</button></div></div>
   <div class="w-grid"><div class="w-eds">${tabs.map(([k,n,lang],i)=>`<div class="w-ed" data-t="${k}" ${i?'hidden':''}>${editorHTML('wEd-'+k,l[k],'Editor '+n,lang)}</div>`).join('')}</div>
    <div class="w-out"><div class="w-prevh"><span>Pratinjau</span>${l.react?'<small>React 18</small>':''}</div><iframe class="w-frame" id="wFrame" sandbox="allow-scripts allow-modals" title="Pratinjau hasil kode"></iframe>
     <div class="w-con" id="wCon" ${l.console||l.react?'':'hidden'}><div class="w-conh">Konsol</div><pre id="wLog"></pre></div></div></div></section>
  ${l.task?`<section class="task" id="task"><div class="eyebrow">Tantangan · diperiksa otomatis</div><h3>${l.task.q}</h3>
    <div class="sl-act"><button class="btn primary" id="wChk">Periksa</button>${l.task.hint?'<button class="btn" id="wHint" aria-expanded="false">Petunjuk</button>':''}</div>
    ${l.task.hint?`<p class="hint" id="wHintT" hidden>💡 ${esc(l.task.hint)}</p>`:''}<div id="wFb" aria-live="polite"></div></section>`:''}
  ${ptsHTML(l)}${qHTML(l)}`;
}
function previewDoc(l,c,id){
  const scr=s=>String(s||'').replace(/<\/script/gi,'<\\/script');
  const boot=`<script>(function(){var ID=${JSON.stringify(id)};window.__logs=[];function f(v){if(typeof v==='string')return v;try{return JSON.stringify(v)}catch(e){return String(v)}}
function send(t,a){var s=Array.prototype.map.call(a,f).join(' ');if(t!=='error')window.__logs.push(s);parent.postMessage({rk:ID,t:t,s:s},'*')}
['log','info','warn','error'].forEach(function(k){var o=console[k];console[k]=function(){send(k,arguments);if(o)o.apply(console,arguments)}});
addEventListener('error',function(e){send('error',[e.message])});addEventListener('unhandledrejection',function(e){send('error',[String(e.reason)])});
window.__rkTest=function(){try{return !!(${l.task&&l.task.test||'false'})}catch(e){return false}};
addEventListener('message',function(e){if(e.data&&e.data.rkTest===ID)parent.postMessage({rk:ID,t:'test',r:window.__rkTest()},'*')})})()<\/script>`;
  const css=`<style>${String(c.css||'').replace(/<\/style/gi,'<\\/style')}</style>`;
  if(l.react)return `<!doctype html><html><head><meta charset="utf-8">${css}</head><body>${c.html||''}<div id="root"></div>${boot}${REACT_CDN.map(u=>`<script src="${u}"><\/script>`).join('')}
<script>if(!window.React||!window.Babel)console.error('React belum termuat. Periksa koneksi internet lalu tekan Jalankan lagi.')<\/script>
<script type="text/babel" data-presets="react">const {useState,useEffect,useRef,useMemo,useCallback,useReducer,useContext,useId}=React;
${scr(c.js)}
ReactDOM.createRoot(document.getElementById('root')).render(<App/>);<\/script></body></html>`;
  return `<!doctype html><html><head><meta charset="utf-8">${css}</head><body>${c.html||''}${boot}${c.js!=null?`<script>${scr(c.js)}<\/script>`:''}</body></html>`;
}
let MSGH=null;
function wireWeb(l,x){
  if(l.viz&&VIZ2[l.viz])VIZ2[l.viz]($('#vizHost'),{lesson:l});
  const tabs=webTabs(l),eds={},fr=$('#wFrame'),log=$('#wLog'),con=$('#wCon');let id='',deb=null,pending=null;
  const run=()=>{id='w'+(++WID);log.textContent='';log.classList.remove('err');const c={};tabs.forEach(([k])=>c[k]=eds[k].get());fr.srcdoc=previewDoc(l,c,id)};
  tabs.forEach(([k])=>eds[k]=wireEditor($('#wEd-'+k),run,()=>{clearTimeout(deb);deb=setTimeout(run,700)}));
  $('.w-tabs').addEventListener('click',e=>{const b=e.target.closest('[data-t]');if(!b)return;document.querySelectorAll('.w-tabs [data-t]').forEach(z=>z.setAttribute('aria-selected',z===b));document.querySelectorAll('.w-ed').forEach(z=>z.hidden=z.dataset.t!==b.dataset.t)});
  $('#wRun').onclick=run;$('#wReset').onclick=()=>{tabs.forEach(([k])=>eds[k].set(l[k]));run()};
  if(MSGH)removeEventListener('message',MSGH);
  MSGH=e=>{const d=e.data;if(!d||d.rk!==id)return;
    if(d.t==='test'){if(pending){pending(d.r);pending=null}return}
    con.hidden=false;const line=document.createElement('div');line.className='lg-'+d.t;line.textContent=(d.t==='error'?'⚠ ':'')+d.s;log.appendChild(line);
    const fr2=d.t==='error'&&jsFriendly(d.s);if(fr2){const h=document.createElement('div');h.className='lg-hint';h.textContent='💡 '+fr2;log.appendChild(h)}log.scrollTop=log.scrollHeight};
  addEventListener('message',MSGH);
  const ck=$('#wChk');if(ck)ck.onclick=()=>{const fb=$('#wFb');fb.innerHTML='<p class="muted">Memeriksa…</p>';
    const tm=setTimeout(()=>{if(pending){pending=null;fb.innerHTML='<div class="tk-fb bad"><b>Pratinjau tidak merespons.</b> Pastikan kodenya tidak error, lalu tekan Jalankan dan periksa lagi.</div>'}},2500);
    pending=r=>{clearTimeout(tm);if(r){fb.innerHTML='<div class="tk-fb ok"><b>✓ Berhasil!</b> Tantangan selesai.</div>';const k=x.id+'#w';if(!LMS.task[k]){LMS.task[k]=1;LMS.xp+=5}markDone(x)}
      else fb.innerHTML='<div class="tk-fb bad"><b>Belum.</b> Hasil di pratinjau belum sesuai tantangan. Baca lagi soalnya atau buka petunjuk.</div>'};
    fr.contentWindow.postMessage({rkTest:id},'*')};
  const hb=$('#wHint');if(hb)hb.onclick=()=>{const h=$('#wHintT');h.hidden=!h.hidden;hb.setAttribute('aria-expanded',!h.hidden)};
  run();wireQ(l);
}

/* ---------- jenis proj: proyek akhir ---------- */
function projHTML(l,y){
  const got=LMS.proj[y.id]||[],html=l.files.find(f=>f[1]==='html');
  return `<section class="pj-brief"><div class="eyebrow">Brief proyek · ${esc(l.stack)}</div><p class="lead">${esc(l.brief)}</p></section>
  <section class="section"><div class="sec-h row"><h2>Fitur yang harus ada</h2><span class="muted" id="pjN">${got.length}/${l.feats.length}</span></div>
   <div class="mod-bar"><i id="pjBar" style="width:${got.length/l.feats.length*100}%"></i></div>
   <ul class="pj-feats" id="pjF">${l.feats.map((f,i)=>`<li><label><input type="checkbox" data-i="${i}" ${got.includes(i)?'checked':''}><span>${esc(f)}</span></label></li>`).join('')}</ul>
   <p class="muted">Centang setiap fitur setelah berhasil kamu buat. Proyek otomatis selesai saat semua fitur tercentang (+50 XP).</p></section>
  <section class="section"><h2>Langkah kerja</h2><ol class="rl">${l.steps.map(s=>`<li>${esc(s)}</li>`).join('')}</ol></section>
  <section class="section"><h2>Berkas awal & contoh solusi</h2><p class="muted">Kerjakan sendiri dulu di editor atau IDE-mu, lalu bandingkan.</p>
   <div class="w-tabs pj-tabs" role="tablist">${l.files.map((f,i)=>`<button role="tab" data-f="${i}" aria-selected="${i===0}">${esc(f[0])}</button>`).join('')}</div>
   ${l.files.map((f,i)=>`<div class="pj-file" data-f="${i}" ${i?'hidden':''}>${pane(f[1],f[2],{label:esc(f[0])})}</div>`).join('')}
   <div class="sl-act">${html?'<button class="btn" id="pjPrev">Lihat pratinjau</button>':''}${l.sql?'<button class="btn" id="pjSql">Jalankan di konsol SQL</button>':''}</div>
   <div id="pjOut"></div></section>`;
}
function wireProj(l,x){
  const y=base(x),F=$('#pjF');
  F.addEventListener('change',()=>{const got=[...F.querySelectorAll('input:checked')].map(c=>+c.dataset.i);LMS.proj[y.id]=got;$('#pjN').textContent=`${got.length}/${l.feats.length}`;$('#pjBar').style.width=`${got.length/l.feats.length*100}%`;
    if(got.length===l.feats.length&&markDone(x,true)){award(50,'· Proyek akhir selesai! 🎉')}else{touch();saveLms()}});
  document.querySelector('.pj-tabs').addEventListener('click',e=>{const b=e.target.closest('[data-f]');if(!b)return;document.querySelectorAll('.pj-tabs [data-f]').forEach(z=>z.setAttribute('aria-selected',z===b));document.querySelectorAll('.pj-file').forEach(z=>z.hidden=z.dataset.f!==b.dataset.f)});
  const pv=$('#pjPrev');if(pv)pv.onclick=()=>{const g=k=>l.files.filter(f=>f[1]===k).map(f=>f[2]).join('\n');$('#pjOut').innerHTML='<iframe class="w-frame pj-frame" sandbox="allow-scripts" title="Pratinjau proyek"></iframe>';$('#pjOut iframe').srcdoc=`<!doctype html><html><head><meta charset="utf-8"><style>${g('css')}</style></head><body>${g('html').replace(/<link[^>]*>/g,'').replace(/<script src[^>]*><\/script>/g,'')}<script>${g('js').replace(/<\/script/gi,'<\\/script')}<\/script></body></html>`};
  const sq=$('#pjSql');if(sq)sq.onclick=()=>{const seed=SEED[l.sql.db]||'';let db=SQLE.create(seed);$('#pjOut').innerHTML=`${editorHTML('pjEd',l.files[l.sql.file][2],'Editor SQL proyek')}<div class="sl-act"><button class="btn primary" id="pjRun">▶ Jalankan</button></div><div class="sl-out" id="pjRes"></div>`;
    const ed=wireEditor($('#pjEd'),go);function go(){db=SQLE.create(seed);try{$('#pjRes').innerHTML=resultHTML(SQLE.exec(db,ed.get()))}catch(e){$('#pjRes').innerHTML=errHTML(e)}}$('#pjRun').onclick=go;go()};
}

/* ---------- jenis s: pelajaran SQL dengan konsol ---------- */
const DBNAME={toko:'Toko Nusantara',bi:'Gudang data BI (skema bintang)',kosong:'Database kosong'};
const tasksOf=l=>l.tasks||(l.task?[l.task]:[]);
function sqlLessonHTML(l){
  const T=tasksOf(l),db=l.db||'toko';
  return `<nav class="toc" aria-label="Di halaman ini">${[['Konsep','.prose'],l.viz&&['Visual','#lab'],['Konsol','#sqlab'],T.length&&['Tantangan','#task0'],l.q&&l.q.length&&['Kuis','#quiz']].filter(Boolean).map(([a,b])=>`<button data-to="${b}">${a}</button>`).join('')}</nav>
  <section class="prose">${l.b.map(p=>`<p>${p}</p>`).join('')}</section>
  ${l.viz&&VIZ2[l.viz]?`<section class="viz" id="lab"><div class="viz-head"><span class="eyebrow">Visual</span><h3>${VIZ2T[l.viz]}</h3></div><div id="vizHost" class="vizhost"></div></section>`:''}
  <section class="sqlab" id="sqlab"><div class="sl-head"><div><span class="eyebrow">Konsol SQL · ${DBNAME[db]}</span><h2>Coba sendiri</h2></div><p>Pilih contoh atau tulis query sendiri. Database berjalan di browser; tekan Reset untuk kembali ke data awal.</p></div>
   <div class="sl-ex" role="group" aria-label="Contoh query">${(l.ex||[]).map(([lab],i)=>`<button class="chip" data-ex="${i}" aria-pressed="${i===0}">${esc(lab)}</button>`).join('')}</div>
   <div class="sl-grid"><div class="sl-main">
     ${editorHTML('slEd',(l.ex&&l.ex[0]?l.ex[0][1]:''),'Editor SQL','sql','Tulis query SQL di sini…')}
     <div class="sl-act"><button class="btn primary" id="slRun">▶ Jalankan <kbd>Ctrl</kbd><kbd>Enter</kbd></button><button class="btn" id="slWhy">Jelaskan langkah</button><button class="btn" id="slReset">Reset database</button></div>
     <div class="sl-out" id="slOut" aria-live="polite"></div>
     <div class="sl-steps" id="slSteps" hidden></div></div>
    <aside class="sl-schema" id="slSchema" aria-label="Skema database"></aside></div></section>
  ${l.syn?`<section class="section"><h2>Di sistem lain</h2><p class="muted">Sintaks berikut hanya untuk dibaca, karena konsol di atas tidak menjalankannya.</p>${pane(/mongo/i.test(l.syn[0])?'text':/kode aplikasi/i.test(l.syn[0])?'java':'sql',l.syn[1],{label:esc(l.syn[0]).toUpperCase()})}</section>`:''}
  ${T.length>1?`<div class="sec-h row"><h2>Tantangan</h2><span class="muted" id="tkN"></span></div>`:''}
  ${T.map((t,i)=>`<section class="task" id="task${i}"><div class="eyebrow">Tantangan ${T.length>1?`${i+1} dari ${T.length}`:''} · dinilai otomatis</div><h3>${t.q}</h3>
    ${editorHTML('tkEd'+i,'','Jawaban tantangan '+(i+1),'sql','Tulis query jawabanmu…')}
    <div class="sl-act"><button class="btn primary" data-tk="${i}">Periksa jawaban</button><button class="btn" data-key="${i}" aria-expanded="false">Lihat kunci jawaban</button></div>
    <div class="tkFb" aria-live="polite"></div><div class="tkKey" hidden>${pane('sql',t.a,{label:'KUNCI JAWABAN'})}</div></section>`).join('')}
  ${ptsHTML(l)}${qHTML(l)}`;
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
  return `<div class="eyebrow">Skema database</div>${SQLE.schema(db).map(t=>`<details><summary><button class="sc-t" data-tb="${esc(t.name)}" title="Masukkan SELECT * FROM ${esc(t.name)}">${t.view?'👁 ':''}${esc(t.name)}</button>${t.view?'<small>view</small>':`<small>${t.rows} baris</small>`}</summary>
    <ul>${t.cols.map(c=>`<li><span>${c.pk?'🔑 ':c.fk?'🔗 ':''}${esc(c.name)}</span><small>${esc((c.type||'').toLowerCase())}${c.fk?` → ${esc(c.fk.table)}`:''}</small></li>`).join('')}</ul></details>`).join('')||'<p class="muted">Belum ada tabel. Buat dengan CREATE TABLE.</p>'}`;
}
const now=()=>performance&&performance.now?performance.now():Date.now();
function wireSql(l,x){
  const seed=SEED[l.db||'toko'];
  if(l.viz&&VIZ2[l.viz])VIZ2[l.viz]($('#vizHost'),{lesson:l});
  let db=SQLE.create(seed);
  const out=$('#slOut'),steps=$('#slSteps'),sch=$('#slSchema');
  const drawSchema=()=>sch.innerHTML=schemaHTML(db);
  const ed=wireEditor($('#slEd'),run);
  function run(){steps.hidden=true;const sql=ed.get();const t0=now();
    try{const r=SQLE.exec(db,sql);out.innerHTML=resultHTML(r,now()-t0);if(r.some(z=>z.kind==='msg'))drawSchema();
      if(!RM()&&out.animate)out.animate([{opacity:.3,transform:'translateY(4px)'},{opacity:1,transform:'none'}],{duration:260,easing:'ease-out'})}
    catch(e){out.innerHTML=errHTML(e);drawSchema()}}
  $('#slRun').onclick=run;
  $('#slWhy').onclick=()=>{steps.hidden=false;sqlPipeline(steps,db,ed.get());steps.scrollIntoView({block:'nearest',behavior:RM()?'auto':'smooth'})};
  $('#slReset').onclick=()=>{db=SQLE.create(seed);drawSchema();out.innerHTML=`<div class="sl-msg ok">✓ Database dikembalikan ke data awal.</div>`};
  $('.sl-ex').addEventListener('click',e=>{const b=e.target.closest('[data-ex]');if(!b)return;$('.sl-ex').querySelectorAll('button').forEach(z=>z.setAttribute('aria-pressed',z===b));ed.set(l.ex[+b.dataset.ex][1]);run()});
  sch.addEventListener('click',e=>{const b=e.target.closest('[data-tb]');if(!b)return;e.preventDefault();ed.set(`SELECT * FROM ${b.dataset.tb};`);run()});
  drawSchema();if(l.ex&&l.ex.length)run();
  const T=tasksOf(l),key=i=>`${base(x).id}#${i}`;
  const cnt=()=>{const n=T.filter((t,i)=>LMS.task[key(i)]).length;const el=$('#tkN');if(el)el.textContent=`${n}/${T.length} selesai`;return n};cnt();
  T.forEach((t,i)=>{const sec=$('#task'+i),tk=wireEditor($('#tkEd'+i),check),fb=$('.tkFb',sec);
    if(LMS.task[key(i)])sec.classList.add('solved');
    $(`[data-tk="${i}"]`,sec).onclick=check;
    $(`[data-key="${i}"]`,sec).onclick=e=>{const k=$('.tkKey',sec),s=k.hidden;k.hidden=!s;e.target.setAttribute('aria-expanded',s);e.target.textContent=s?'Sembunyikan kunci':'Lihat kunci jawaban'};
    function check(){const r=gradeSql(t,tk.get(),seed);
      fb.innerHTML=`<div class="tk-fb ${r.ok?'ok':'bad'}" role="status"><b>${r.ok?'✓ Benar!':'Belum tepat.'}</b> ${r.msg}</div>${r.html||''}`;
      if(r.ok){sec.classList.add('solved');if(!LMS.task[key(i)]){LMS.task[key(i)]=1;award(5,'· Tantangan SQL')}if(cnt()===T.length&&markDone(x)){$('#outline').innerHTML=renderOutline(x)}}}});
  wireQ(l);
}
function gradeSql(task,sql,seed=SEED.toko){
  if(!sql.trim())return {ok:false,msg:'Tulis dulu query-mu di editor tantangan.'};
  const fin=s=>{const db=SQLE.create(seed);const r=SQLE.exec(db,s);return task.check?SQLE.exec(db,task.check).pop():r[r.length-1]};
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
  const same=(p,q)=>{const a=[...p].sort(),b=[...q].sort();return a.every((v,i)=>v===b[i])};
  if(task.order){if(A.every((v,i)=>v===B[i]))return {ok:true,msg:'Isi dan urutannya tepat.',html:show};
    if(same(A,B))return {ok:false,msg:'Isinya sudah benar, tapi urutannya belum. Perhatikan ORDER BY.',html:show}}
  else if(same(A,B))return {ok:true,msg:task.check?'Perubahan datamu sesuai yang diminta.':'Hasil query-mu sama persis dengan yang diminta.',html:view+show};
  const A2=got.rows.map(r=>K(r).sort().join('\u0001')),B2=exp.rows.map(r=>K(r).sort().join('\u0001'));
  if(same(A2,B2)&&!task.order)return {ok:true,msg:'Isinya benar, hanya urutan kolomnya berbeda.',html:show};
  return {ok:false,msg:'Jumlah baris dan kolom sudah sesuai, tapi ada nilai yang berbeda. Bandingkan hasilmu dengan soal sekali lagi.',html:view+show};
}
