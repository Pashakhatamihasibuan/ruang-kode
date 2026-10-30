/* ===================== LATIHAN BERTAHAP =====================
   Dibuat otomatis dari contoh kode pelajaran, sebelum siswa menulis kode sendiri:
   1. Susun baris: baris kode diacak, siswa menyusunnya kembali (tanpa seret, cukup klik).
   2. Isi bagian kosong: beberapa kata kunci dihilangkan dari kode.
   3. Perbaiki error: kode dengan satu kesalahan khas pemula dan pesan error aslinya (l.bug, dari tools/gen/bugs.py).
   Ketiganya punya petunjuk bertingkat: arah umum, lalu bantuan satu langkah, lalu jawaban. */
const PR_LANGS=['python','java','js','ts','sql'];
const PR_KW={
  python:['def','return','for','in','if','elif','else','while','import','from','print','range','len','append','class','self','True','False','None','and','or','not','lambda','with','try','except','yield','break','continue'],
  java:['public','static','void','int','double','boolean','String','for','if','else','while','return','new','class','System.out.println','private','final','this','extends','implements','try','catch'],
  js:['const','let','function','return','for','of','in','if','else','while','console.log','new','class','async','await','map','filter','reduce','push','try','catch','throw'],
  ts:['const','let','function','return','for','of','if','else','console.log','interface','type','extends','keyof','number','string','boolean','class','new','readonly'],
  sql:['SELECT','FROM','WHERE','GROUP BY','ORDER BY','JOIN','ON','HAVING','COUNT','SUM','AVG','AS','LIMIT','DESC','AND','OR','IN','LEFT JOIN','DISTINCT','OVER','PARTITION BY','WITH','CASE','WHEN','THEN','END']};
const PR_COM={python:'#',sql:'--'};
/* ganti isi teks dan komentar dengan spasi agar kata kunci di dalamnya tidak ikut dipilih */
function prMask(line,lang){
  let out='',q=null;const com=PR_COM[lang]||'//';
  for(let i=0;i<line.length;i++){const c=line[i];
    if(q){out+=' ';if(c==='\\'){out+=' ';i++}else if(c===q)q=null;continue}
    if(line.startsWith(com,i)){out+=' '.repeat(line.length-i);break}
    if(c==='"'||c==="'"||c==='`'){q=c;out+=' ';continue}
    out+=c}
  return out;
}
const prIsCom=(s,lang)=>{const t=s.trim();return !t||t.startsWith(PR_COM[lang]||'//')||t.startsWith('/*')||t.startsWith('*')};
function prLines(code,lang){return code.split('\n').map(s=>s.replace(/\s+$/,'').replace(/\s+(#|\/\/|--) .*$/,m=>prMask(m,lang).trim()?m:'')).filter(s=>!prIsCom(s,lang))}
function prBlanks(code,lang){
  const kws=PR_KW[lang]||[],lines=code.split('\n'),c=[];
  lines.forEach((ln,li)=>{if(prIsCom(ln,lang))return;const mk=prMask(ln,lang);
    for(const k of kws){const rx=new RegExp(`(^|[^\\w.])(${k.replace(/[.]/g,'\\.').replace(/ /g,'\\s+')})(?![\\w])`,lang==='sql'?'gi':'g');let m;
      while((m=rx.exec(mk))){c.push({li,at:m.index+m[1].length,len:m[2].length,tok:ln.substr(m.index+m[1].length,m[2].length)})}}});
  /* satu lubang per baris, kata kunci yang berbeda-beda, tersebar dari atas ke bawah */
  const byLine=[...new Set(c.map(x=>x.li))].map(li=>c.filter(x=>x.li===li).sort((a,b)=>b.len-a.len||a.at-b.at)[0]);
  const n=Math.min(3,byLine.length),pickd=[],used=new Set();
  for(let i=0;i<byLine.length&&pickd.length<n;i++){const x=byLine[Math.floor((i+.5)*byLine.length/n)%byLine.length]||byLine[i];if(!used.has(x.tok)&&!pickd.includes(x)){pickd.push(x);used.add(x.tok)}}
  for(const x of byLine){if(pickd.length>=n)break;if(!pickd.includes(x)&&!used.has(x.tok)){pickd.push(x);used.add(x.tok)}}
  return pickd.sort((a,b)=>a.li-b.li||a.at-b.at);
}
function prOk(l,lang){if(!l.code||!PR_LANGS.includes(lang))return false;const n=prLines(l.code,lang).length;return n>=3&&n<=16}
function practiceHTML(l,lang){
  const ok=prOk(l,lang);if(!ok&&!l.bug)return '';
  const bl=ok?prBlanks(l.code,lang):[];
  const src=l.code.split('\n');let fill='';
  src.forEach((ln,li)=>{const bs=bl.filter(b=>b.li===li);let pos=0,row='';
    bs.forEach(b=>{const i=bl.indexOf(b);row+=hl(ln.slice(pos,b.at),lang)+`<input class="pr-in" data-b="${i}" aria-label="Bagian kosong ${i+1}" autocomplete="off" autocapitalize="off" spellcheck="false" style="width:${Math.max(3,b.len)+1.5}ch">`;pos=b.at+b.len});
    fill+=row+hl(ln.slice(pos),lang)+'\n'});
  return `<section class="section pr-sec" id="latihan"><h2>Latihan bertahap</h2>
  <p class="muted">Sebelum menulis sendiri, latih dulu dengan langkah-langkah kecil ini. Petunjuk dibuka bertahap: coba dulu tanpa bantuan.</p>
  <div class="pr-tabs" role="tablist" aria-label="Langkah latihan">${[ok&&'Susun baris',bl.length&&'Isi bagian kosong',l.bug&&'Perbaiki error'].map((n,i)=>n?`<button role="tab" data-pt="${i+1}">${n}</button>`:'').join('')}</div>
  ${ok?`<div class="pr-pane" data-pp="1"><p>Baris-baris kode di atas diacak. Coba tanpa menggulir ke atas: klik baris di <b>Pilihan</b> sesuai urutan yang benar. Klik baris di <b>Susunanmu</b> untuk mengembalikannya.</p>
   <div class="pr-grid"><div><div class="eyebrow">Pilihan</div><ol class="pr-pool" id="prPool"></ol></div><div><div class="eyebrow">Susunanmu</div><ol class="pr-ans" id="prAns"></ol></div></div>
   <div class="sl-act"><button class="btn primary" id="prChk">Periksa</button><button class="btn" id="prHint">Petunjuk (1/3)</button><button class="tlink" id="prReset">Ulangi</button></div><div id="prFb" aria-live="polite"></div></div>`:''}
  ${bl.length?`<div class="pr-pane" data-pp="2" hidden><p>Isi ${bl.length} bagian kosong agar kodenya sama dengan contoh. Coba dari ingatan dulu, jangan menggulir ke atas.</p>
   <div class="pane tx pr-fill"><div class="pane-h"><span>${LANGLBL[lang]||'KODE'} · isi yang kosong</span></div><pre class="code">${fill.replace(/\n$/,'')}</pre></div>
   <div class="pr-bank" id="prBank" hidden></div>
   <div class="sl-act"><button class="btn primary" id="fbChk">Periksa</button><button class="btn" id="fbHint">Petunjuk (1/3)</button></div><div id="fbFb" aria-live="polite"></div></div>`:''}
  ${l.bug?`<div class="pr-pane" data-pp="3" hidden><p>Kode ini mirip contoh di atas, tetapi ada <b>satu kesalahan</b> yang sering dibuat pemula. Baca pesan error-nya, temukan barisnya, lalu perbaiki langsung di editor.</p>
   <div class="eyebrow">Pesan error saat dijalankan</div><div class="console err pr-err">${esc(l.bug.err)}</div>
   <div class="pane tx"><div class="pane-h"><span>${LANGLBL[lang]||'KODE'} · perbaiki di sini</span></div>${editorHTML('bgEd',l.bug.code,'Editor perbaikan kode',lang)}</div>
   <div class="sl-act"><button class="btn primary" id="bgChk">Periksa</button><button class="btn" id="bgHint">Petunjuk (1/3)</button><button class="tlink" id="bgReset">Kembalikan kode rusak</button></div><div id="bgFb" aria-live="polite"></div></div>`:''}
  </section>`;
}
function wirePractice(l,lang){
  const sec=$('#latihan');if(!sec)return;
  const tabs=[...sec.querySelectorAll('[data-pt]')],show=pt=>{tabs.forEach(x=>x.setAttribute('aria-selected',x.dataset.pt===pt));sec.querySelectorAll('[data-pp]').forEach(p=>p.hidden=p.dataset.pp!==pt)};
  show(tabs[0].dataset.pt);sec.querySelector('.pr-tabs').onclick=e=>{const b=e.target.closest('[data-pt]');if(b)show(b.dataset.pt)};
  wireBug(l,lang);if(!prOk(l,lang))return;
  const lines=prLines(l.code,lang),N=lines.length,key=qkey(l.code);
  let ord=perm(N,l.code.length);if(ord.every((v,i)=>v===i))ord=ord.reverse();
  let pool=[...ord],ans=[],hint=0;
  const lineHTML=i=>`<code>${hl(lines[i].replace(/^\s+/,m=>'\u00a0'.repeat(m.length)),lang)}</code>`;
  const draw=()=>{$('#prPool').innerHTML=pool.map(i=>`<li><button data-i="${i}">${lineHTML(i)}</button></li>`).join('')||'<li class="muted small">Semua baris sudah dipakai.</li>';
    $('#prAns').innerHTML=ans.map((i,k)=>`<li><button data-i="${i}" class="${hint>=2&&k<fixedN()?'fixed':''}">${lineHTML(i)}</button></li>`).join('')||'<li class="muted small">Belum ada baris.</li>'};
  /* baris dianggap benar jika teksnya sama, karena baris yang identik boleh bertukar tempat */
  const same=(a,b)=>lines[a]===lines[b];
  const fixedN=()=>{let k=0;while(k<ans.length&&same(ans[k],k))k++;return k};
  $('#prPool').onclick=e=>{const b=e.target.closest('[data-i]');if(!b)return;const i=+b.dataset.i;pool=pool.filter(x=>x!==i);ans.push(i);draw();$('#prFb').innerHTML=''};
  $('#prAns').onclick=e=>{const b=e.target.closest('[data-i]');if(!b)return;const i=+b.dataset.i;ans=ans.filter(x=>x!==i);pool.push(i);draw();$('#prFb').innerHTML=''};
  $('#prReset').onclick=()=>{pool=[...ord];ans=[];draw();$('#prFb').innerHTML=''};
  $('#prChk').onclick=()=>{const fb=$('#prFb'),k=fixedN();
    if(ans.length<N&&k===ans.length){fb.innerHTML=`<div class="tk-fb">Sejauh ini benar (${k} dari ${N} baris). Lanjutkan.</div>`;return}
    if(k===N){fb.innerHTML='<div class="tk-fb ok"><b>✓ Urutannya benar!</b> Lanjut ke langkah berikutnya.</div>';const t='p'+key;if(!LMS.task[t]){LMS.task[t]=1;award(3,'· Susun baris')}return}
    fb.innerHTML=`<div class="tk-fb bad"><b>Belum.</b> ${k?`${k} baris pertama sudah benar; baris ke-${k+1} belum tepat.`:'Baris pertama belum tepat.'} Klik baris yang salah untuk mengembalikannya.</div>`};
  const H=[()=>`Mulailah dari yang harus ada lebih dulu: ${lang==='sql'?'urutan klausa SQL adalah SELECT → FROM → JOIN → WHERE → GROUP BY → HAVING → ORDER BY.':'import di paling atas, variabel dibuat sebelum dipakai, fungsi atau kelas ditulis sebelum dipanggil, dan isi blok berada setelah baris yang diakhiri '+(lang==='python'?'titik dua (:)':'kurung kurawal {')+'.'}`,
    ()=>{const k=fixedN();ans=ans.slice(0,k);pool=ord.filter(i=>!ans.includes(i));const nx=pool.find(i=>same(i,k));if(nx!=null){pool=pool.filter(x=>x!==nx);ans.push(nx)}draw();return `Baris ke-${k+1} sudah dipasangkan untukmu. Baris yang benar ditandai.`},
    ()=>{ans=[...Array(N).keys()];pool=[];draw();return 'Ini susunan lengkapnya. Bandingkan dengan susunanmu tadi, lalu coba langkah 2.'}];
  $('#prHint').onclick=e=>{const m=H[Math.min(hint,2)]();hint=Math.min(hint+1,3);e.target.textContent=hint<3?`Petunjuk (${hint+1}/3)`:'Petunjuk habis';e.target.disabled=hint>=3;$('#prFb').innerHTML=`<div class="tk-fb">💡 ${m}</div>`};
  draw();
  /* isi bagian kosong */
  const bl=prBlanks(l.code,lang);if(!bl.length)return;let fh=0;
  const norm=s=>lang==='sql'?s.trim().replace(/\s+/g,' ').toUpperCase():s.trim().replace(/\s+/g,' ');
  const ins=[...sec.querySelectorAll('.pr-in')];
  ins.forEach(i=>i.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();$('#fbChk').click()}}));
  $('#fbChk').onclick=()=>{let ok=0;ins.forEach(i=>{const b=bl[+i.dataset.b],good=norm(i.value)===norm(b.tok);i.classList.toggle('ok',good);i.classList.toggle('bad',!good&&!!i.value.trim());if(good)ok++});
    const fb=$('#fbFb');if(ok===bl.length){fb.innerHTML='<div class="tk-fb ok"><b>✓ Semua benar!</b> Kamu siap menulis kode serupa sendiri.</div>';const t='f'+key;if(!LMS.task[t]){LMS.task[t]=1;award(3,'· Isi bagian kosong')}}
    else fb.innerHTML=`<div class="tk-fb bad">${ok} dari ${bl.length} benar. Kotak merah masih salah${ins.some(i=>!i.value.trim())?', kotak kosong belum diisi':''}.</div>`};
  $('#fbHint').onclick=e=>{const fb=$('#fbFb');
    if(fh===0){ins.forEach(i=>{const b=bl[+i.dataset.b];i.placeholder=b.tok[0]+'·'.repeat(b.tok.length-1)});fb.innerHTML='<div class="tk-fb">💡 Huruf pertama dan panjang setiap kata sudah ditampilkan di kotaknya.</div>'}
    else if(fh===1){const extra=(PR_KW[lang]||[]).filter(k=>!bl.some(b=>b.tok===k)).slice(0,3);const bank=shuffle([...new Set(bl.map(b=>b.tok)),...extra]);const bx=$('#prBank');bx.hidden=false;bx.innerHTML=`<span class="eyebrow">Pilihan kata</span>${bank.map(w=>`<code>${esc(w)}</code>`).join('')}`;fb.innerHTML='<div class="tk-fb">💡 Jawabannya ada di antara pilihan kata di atas.</div>'}
    else{ins.forEach(i=>{i.value=bl[+i.dataset.b].tok});$('#fbChk').click();fb.insertAdjacentHTML('beforeend','<div class="tk-fb">Jawaban sudah diisi. Hapus lalu coba ketik ulang dari ingatan.</div>')}
    fh=Math.min(fh+1,3);e.target.textContent=fh<3?`Petunjuk (${fh+1}/3)`:'Petunjuk habis';e.target.disabled=fh>=3};
}
function wireBug(l,lang){
  const B=l.bug;if(!B||!$('#bgEd'))return;let h=0;
  const ed=wireEditor($('#bgEd'),()=>$('#bgChk').click()),N=s=>s.split('\n').map(x=>x.replace(/\s+$/,'')).join('\n').replace(/\n+$/,'');
  const good=l.code.split('\n'),fb=$('#bgFb');
  $('#bgChk').onclick=()=>{const cur=N(ed.get()),want=N(l.code);
    if(cur===want){fb.innerHTML='<div class="tk-fb ok"><b>✓ Error berhasil diperbaiki!</b> Kode sekarang sama dengan versi yang benar dan bisa dijalankan.</div>';const t='b'+qkey(l.code);if(!LMS.task[t]){LMS.task[t]=1;award(5,'· Perbaiki error')}return}
    const cl=cur.split('\n'),fixed=N(cl[B.line-1]||'')===N(good[B.line-1]);
    fb.innerHTML=`<div class="tk-fb bad"><b>Belum.</b> ${fixed?'Baris yang rusak sudah benar, tetapi ada bagian lain yang ikut berubah. Tekan "Kembalikan kode rusak" lalu ubah hanya bagian yang salah.':'Error-nya masih ada. Baca lagi pesan error-nya: nomor baris dan tanda ^ menunjuk ke dekat kesalahannya.'}</div>`};
  const why=()=>(lang==='python'?pyFriendly(B.err):lang==='js'?jsFriendly(B.err):'')||B.why;
  const H=[()=>`Arti pesan error-nya: ${why()}`,()=>`Kesalahannya ada di baris ${B.line}: <code>${esc(B.code.split('\n')[B.line-1].trim())}</code>`,()=>`Baris yang benar: <code>${esc(good[B.line-1].trim())}</code>`];
  $('#bgHint').onclick=e=>{fb.innerHTML=`<div class="tk-fb">💡 ${H[Math.min(h,2)]()}</div>`;h=Math.min(h+1,3);e.target.textContent=h<3?`Petunjuk (${h+1}/3)`:'Petunjuk habis';e.target.disabled=h>=3};
  $('#bgReset').onclick=()=>{ed.set(B.code);fb.innerHTML=''};
}
