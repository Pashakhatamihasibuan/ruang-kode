/* ===================== VISUALISASI v3 =====================
   Visual untuk jalur Web, Git, Data, dan Desain. Setiap fungsi didaftarkan ke VIZ2
   sehingga dipakai lewat field viz pada pelajaran. Kontrol interaktif memakai elemen
   form biasa agar bisa dioperasikan dengan keyboard. */
const seg=(name,opts,cur)=>`<div class="seg" role="group" aria-label="${name}">${opts.map(([v,l])=>`<button data-v="${v}" aria-pressed="${v===cur}">${l}</button>`).join('')}</div>`;
const segWire=(host,sel,fn)=>host.querySelector(sel).addEventListener('click',e=>{const b=e.target.closest('[data-v]');if(!b)return;b.parentNode.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));fn(b.dataset.v)});
const rng=(id,label,min,max,val,step=1,unit='')=>`<label class="v3-r"><span>${label} <output id="${id}o">${val}${unit}</output></span><input type="range" id="${id}" min="${min}" max="${max}" step="${step}" value="${val}"></label>`;

/* --- pola umum: aktor dan pesan berurutan --- */
function seqViz(host,actors,steps,o={}){
  const draw=(st,f,i)=>{st.innerHTML=`<div class="v3-seq" style="--n:${actors.length}">
    <div class="v3-act">${actors.map((a,k)=>`<div class="${steps[i].on&&steps[i].on.includes(k)?'on':''}"><b>${a[0]}</b><small>${a[1]||''}</small></div>`).join('')}</div>
    <div class="v3-msgs">${steps.slice(0,i+1).filter(s=>s.from!=null).map((s,k,arr)=>{const a=Math.min(s.from,s.to),b=Math.max(s.from,s.to);
      return `<div class="v3-msg ${k===arr.length-1?'cur':''} ${s.to<s.from?'back':''}" style="--a:${a};--b:${b}"><span>${s.label}</span></div>`}).join('')}</div></div>`};
  return player(host,steps.map(s=>({...s,note:s.note})),draw,{speed:o.speed||1500});
}
/* --- pola umum: tahapan berderet --- */
function stageViz(host,stages,steps,o={}){
  const draw=(st,f)=>{st.innerHTML=`<div class="v3-stages">${stages.map((s,k)=>`<div class="v3-st ${f.on.includes(k)?'on':''} ${f.skip&&f.skip.includes(k)?'skip':''}"><b>${s[0]}</b><small>${s[1]||''}</small></div>`).join('<span class="v3-arr" aria-hidden="true">→</span>')}</div>${f.extra?`<div class="v3-extra">${f.extra}</div>`:''}`};
  return player(host,steps,draw,{speed:o.speed||1400});
}

/* ---------- WEB ---------- */
function httpViz(host){
  seqViz(host,[['Browser','kamu'],['DNS','buku alamat'],['Server','tokonusantara.id']],[
    {on:[0],note:'Kamu mengetik <code>tokonusantara.id</code> dan menekan Enter. Browser belum tahu alamat IP server.'},
    {from:0,to:1,on:[0,1],label:'Alamat IP tokonusantara.id?',note:'Browser bertanya ke <b>DNS</b>, seperti mencari nomor telepon di buku alamat.'},
    {from:1,to:0,on:[0,1],label:'103.21.45.7',note:'DNS menjawab dengan alamat IP. Jawaban ini disimpan (cache) agar kunjungan berikutnya lebih cepat.'},
    {from:0,to:2,on:[0,2],label:'Jabat tangan TCP + TLS',note:'Browser membuka koneksi ke server dan menyepakati kunci enkripsi (HTTPS).'},
    {from:0,to:2,on:[0,2],label:'GET / HTTP/2',note:'Browser mengirim <b>permintaan HTTP</b>: metode GET, alamat halaman, dan header.'},
    {from:2,to:0,on:[0,2],label:'200 OK + HTML',note:'Server membalas kode status <b>200</b> dan dokumen HTML.'},
    {from:0,to:2,on:[0,2],label:'GET gaya.css, app.js, logo.svg',note:'Saat membaca HTML, browser menemukan CSS, JS, dan gambar, lalu memintanya juga.'},
    {on:[0],note:'Semua berkas diterima. Browser menyusun DOM, menerapkan CSS, menjalankan JS, lalu menggambar halaman.'}]);
}
const SPEC_PRESET=['#menu .aktif','nav a.tombol:hover','.kartu p','p','ul li:first-child','#beli'];
function specOf(sel){
  let s=sel.replace(/:not\(([^)]*)\)/g,' $1 ');let a=0,b=0,c=0;
  a=(s.match(/#[\w-]+/g)||[]).length;s=s.replace(/#[\w-]+/g,' ');
  b=(s.match(/\.[\w-]+|\[[^\]]*\]|:(?!:)[\w-]+(\([^)]*\))?/g)||[]).length;s=s.replace(/\.[\w-]+|\[[^\]]*\]|:(?!:)[\w-]+(\([^)]*\))?/g,' ');
  c=(s.match(/::[\w-]+|(^|[\s>+~])[a-zA-Z][\w-]*/g)||[]).length;return [a,b,c];
}
function specificityViz(host){
  host.innerHTML=`<div class="v3-spec"><label>Selector A <input class="inp v3-in" id="spA" value="#menu .aktif"></label><label>Selector B <input class="inp v3-in" id="spB" value="nav a.tombol:hover"></label></div><div class="v3-presets">${SPEC_PRESET.map(p=>`<button class="chip" data-p="${esc(p)}">${esc(p)}</button>`).join('')}</div><div class="v3-specout" aria-live="polite"></div>`;
  const A=$('#spA',host),B=$('#spB',host),out=$('.v3-specout',host);let last=B;
  const show=()=>{const a=specOf(A.value),b=specOf(B.value);const cmp=a[0]-b[0]||a[1]-b[1]||a[2]-b[2];
    const col=(s,lab,win)=>`<div class="v3-sc ${win?'win':''}"><b>${lab}</b><div class="v3-abc">${['ID','Kelas/atribut/pseudo-class','Elemen'].map((n,i)=>`<span><i>${s[i]}</i><small>${n}</small></span>`).join('')}</div><code>(${s.join(', ')})</code></div>`;
    out.innerHTML=col(a,'A',cmp>0)+col(b,'B',cmp<0)+`<p class="v3-verdict">${cmp>0?'A menang':cmp<0?'B menang':'Seri: aturan yang ditulis terakhir menang'}. Bandingkan dari kiri: ID dulu, lalu kelas, lalu elemen.</p>`};
  host.addEventListener('input',show);host.addEventListener('focusin',e=>{if(e.target===A||e.target===B)last=e.target});
  host.addEventListener('click',e=>{const p=e.target.closest('[data-p]');if(p){last.value=p.dataset.p;show()}});show();
}
function boxmodelViz(host){
  host.innerHTML=`<div class="v3-ctl">${rng('bmW','width',100,260,200,10,'px')}${rng('bmP','padding',0,40,16,2,'px')}${rng('bmB','border',0,16,4,1,'px')}${rng('bmM','margin',0,40,20,2,'px')}</div>${seg('box-sizing',[['content-box','content-box'],['border-box','border-box']],'content-box')}<div class="v3-bm"></div><p class="v3-sum" aria-live="polite"></p>`;
  let bs='content-box';const v=id=>+$('#'+id,host).value;
  const draw=()=>{const w=v('bmW'),p=v('bmP'),b=v('bmB'),m=v('bmM');['bmW','bmP','bmB','bmM'].forEach(id=>$('#'+id+'o',host).textContent=v(id)+'px');
    const content=bs==='content-box'?w:Math.max(0,w-2*p-2*b),total=bs==='content-box'?w+2*p+2*b:w;
    $('.v3-bm',host).innerHTML=`<div class="bm-m" style="padding:${m/2}px"><span>margin ${m}</span><div class="bm-b" style="border-width:${Math.max(1,b/2)}px"><span>border ${b}</span><div class="bm-p" style="padding:${p/2}px"><span>padding ${p}</span><div class="bm-c" style="width:${content/2+40}px">konten ${content}px</div></div></div></div>`;
    $('.v3-sum',host).innerHTML=bs==='content-box'?`Lebar tampil = ${w} + 2×${p} + 2×${b} = <b>${total}px</b> (margin ${m}px di luar). Dengan content-box, padding dan border <b>menambah</b> lebar.`:`Lebar tampil tetap <b>${total}px</b>; konten menyusut menjadi ${content}px. Dengan border-box, padding dan border <b>termasuk</b> dalam width.`};
  host.addEventListener('input',draw);segWire(host,'.seg',x=>{bs=x;draw()});draw();
}
function flexboxViz(host){
  const S={'flex-direction':['row','column','row-reverse'],'justify-content':['flex-start','center','space-between','space-around','flex-end'],'align-items':['stretch','flex-start','center','flex-end'],'flex-wrap':['nowrap','wrap']};
  const cur={'flex-direction':'row','justify-content':'flex-start','align-items':'stretch','flex-wrap':'nowrap',gap:8};
  host.innerHTML=`<div class="v3-props">${Object.entries(S).map(([k,vs])=>`<label>${k}<select class="inp" data-k="${k}">${vs.map(v=>`<option>${v}</option>`).join('')}</select></label>`).join('')}${rng('fxG','gap',0,32,8,2,'px')}</div><div class="v3-flex"></div><pre class="code v3-css"></pre>`;
  const draw=()=>{const box=$('.v3-flex',host);box.style.cssText=Object.entries(cur).map(([k,v])=>`${k}:${k==='gap'?v+'px':v}`).join(';');
    box.innerHTML=['Kopi','Teh Melati','Madu','Keripik','Sambal'].map((t,i)=>`<div class="fx-i" style="min-height:${[36,52,30,44,38][i]}px">${t}</div>`).join('');$('#fxGo',host).textContent=cur.gap+'px';
    $('.v3-css',host).innerHTML=hl(`.wadah {\n  display: flex;\n${Object.entries(cur).map(([k,v])=>`  ${k}: ${k==='gap'?v+'px':v};`).join('\n')}\n}`,'css')};
  host.addEventListener('input',e=>{const k=e.target.dataset.k;if(k)cur[k]=e.target.value;if(e.target.id==='fxG')cur.gap=+e.target.value;draw()});draw();
}
function gridViz(host){
  const T=[['repeat(3, 1fr)','3 kolom sama'],['200px 1fr','sidebar + isi'],['repeat(auto-fill, minmax(110px, 1fr))','auto-fill responsif'],['1fr 2fr 1fr','rasio 1:2:1']];
  let t=0,span=1;
  host.innerHTML=`${seg('Kolom',T.map((x,i)=>[String(i),x[1]]),'0')}<div class="v3-ctl">${rng('grS','kartu pertama span',1,3,1,1)}${rng('grG','gap',0,24,10,2,'px')}</div><div class="v3-grid"></div><pre class="code v3-css"></pre>`;
  const draw=()=>{const g=+$('#grG',host).value;span=+$('#grS',host).value;$('#grSo',host).textContent=span;$('#grGo',host).textContent=g+'px';const box=$('.v3-grid',host);
    box.style.gridTemplateColumns=T[t][0];box.style.gap=g+'px';box.innerHTML=Array.from({length:7},(_,i)=>`<div class="gr-i" ${i===0&&span>1?`style="grid-column:span ${span}"`:''}>${i+1}</div>`).join('');
    $('.v3-css',host).innerHTML=hl(`.galeri {\n  display: grid;\n  grid-template-columns: ${T[t][0]};\n  gap: ${g}px;\n}${span>1?`\n.galeri > :first-child { grid-column: span ${span}; }`:''}`,'css')};
  host.addEventListener('input',draw);segWire(host,'.seg',x=>{t=+x;draw()});draw();
}
function renderViz(host){
  const S=[['HTML → DOM','pohon elemen'],['CSS → CSSOM','aturan gaya'],['Render tree','yang terlihat'],['Layout','posisi & ukuran'],['Paint','piksel warna'],['Composite','susun lapisan']];
  let mode='load',P;host.innerHTML=seg('Skenario',[['load','Muat halaman'],['width','Ubah width'],['color','Ubah warna'],['transform','Ubah transform']],'load')+'<div class="pl"></div>';
  const F={load:[{on:[0],note:'Browser membaca HTML dan membangun <b>DOM</b>.'},{on:[0,1],note:'Sambil itu, CSS diubah menjadi <b>CSSOM</b>. CSS menghambat tampilan sampai selesai dimuat.'},{on:[2],note:'DOM + CSSOM digabung menjadi <b>render tree</b>; elemen <code>display:none</code> tidak ikut.'},{on:[3],note:'<b>Layout</b> menghitung posisi dan ukuran setiap kotak.'},{on:[4],note:'<b>Paint</b> mengisi piksel: teks, warna, bayangan.'},{on:[5],note:'<b>Composite</b> menyusun lapisan menjadi gambar akhir di layar.'}],
    width:[{on:[3,4,5],skip:[0,1,2],note:'Mengubah <code>width</code> memaksa <b>layout, paint, dan composite</b> diulang. Mahal bila terjadi setiap frame animasi.'}],
    color:[{on:[4,5],skip:[0,1,2,3],note:'Mengubah <code>color</code> atau <code>background</code> melewati layout, tetapi tetap <b>paint</b> ulang.'}],
    transform:[{on:[5],skip:[0,1,2,3,4],note:'<code>transform</code> dan <code>opacity</code> cukup di-<b>composite</b> ulang, sering dikerjakan GPU. Inilah alasan animasi yang mulus memakai keduanya.'}]};
  const build=()=>{if(P)P.set(F[mode]);else P=stageViz($('.pl',host),S,F[mode])};segWire(host,'.seg',x=>{mode=x;build()});build();
}
function jsloopViz(host){
  const code=['console.log("A");','setTimeout(() => console.log("B"), 0);','Promise.resolve().then(() => console.log("C"));','console.log("D");'];
  const fr=[{line:0,stack:['console.log("A")'],api:[],micro:[],task:[],out:'A',note:'Kode sinkron berjalan di <b>call stack</b>. "A" langsung dicetak.'},
    {line:1,stack:['setTimeout(...)'],api:['timer 0 md → B'],micro:[],task:[],out:'A',note:'<code>setTimeout</code> diserahkan ke <b>Web API</b> browser. Call stack tidak menunggu.'},
    {line:1,stack:[],api:[],micro:[],task:['() => log("B")'],out:'A',note:'Timer selesai (0 md), callback masuk <b>antrean task</b>, tetapi belum boleh jalan karena kode sinkron belum habis.'},
    {line:2,stack:['Promise.then(...)'],api:[],micro:['() => log("C")'],task:['() => log("B")'],out:'A',note:'Callback <code>.then</code> masuk <b>antrean microtask</b>, yang selalu didahulukan.'},
    {line:3,stack:['console.log("D")'],api:[],micro:['() => log("C")'],task:['() => log("B")'],out:'A\nD',note:'Baris terakhir sinkron: "D" dicetak.'},
    {line:-1,stack:['() => log("C")'],api:[],micro:[],task:['() => log("B")'],out:'A\nD\nC',note:'Call stack kosong. <b>Event loop</b> menghabiskan semua microtask dulu: "C".'},
    {line:-1,stack:['() => log("B")'],api:[],micro:[],task:[],out:'A\nD\nC\nB',note:'Baru kemudian satu task diambil: "B". Urutan akhir: A, D, C, B.'}];
  const box=(t,xs)=>`<div class="v3-q"><b>${t}</b>${xs.length?xs.map(x=>`<code>${esc(x)}</code>`).join(''):'<i>kosong</i>'}</div>`;
  player(host,fr,(st,f)=>{st.innerHTML=`<div class="v3-loop"><ol class="v3-code">${code.map((c,i)=>`<li class="${f.line===i?'cur':''}">${hl(c,'js')}</li>`).join('')}</ol><div class="v3-qs">${box('Call stack',f.stack)}${box('Web API',f.api)}${box('Microtask',f.micro)}${box('Task',f.task)}</div><div class="console">${esc(f.out)}</div></div>`},{speed:1700});
}
function vitalsViz(host){
  const M=[['lcp','LCP','Largest Contentful Paint: elemen terbesar tampil',0.5,6,2.1,0.1,'s',2.5,4],['inp','INP','Interaction to Next Paint: respons setelah ketukan',50,800,180,10,'ms',200,500],['cls','CLS','Cumulative Layout Shift: tata letak bergeser',0,0.5,0.05,0.01,'',0.1,0.25]];
  host.innerHTML=`<div class="v3-ctl">${M.map(m=>rng('cv'+m[0],m[1],m[3],m[4],m[5],m[6],m[7])).join('')}</div><div class="v3-vit"></div>`;
  const draw=()=>{$('.v3-vit',host).innerHTML=M.map(m=>{const v=+$('#cv'+m[0],host).value;$('#cv'+m[0]+'o',host).textContent=v+m[7];const s=v<=m[8]?['baik','ok']:v<=m[9]?['perlu perbaikan','mid']:['buruk','bad'];
    return `<div class="vt ${s[1]}"><b>${m[1]}</b><span class="vt-v">${v}${m[7]}</span><span class="vt-s">${s[0]}</span><small>${m[2]}. Baik ≤ ${m[8]}${m[7]}, buruk > ${m[9]}${m[7]}</small></div>`}).join('')};
  host.addEventListener('input',draw);draw();
}
function ssrViz(host){
  const D={csr:[['HTML kosong + JS',0,1.2,'net'],['Unduh & jalankan JS',1.2,2.6,'js'],['Ambil data API',2.6,3.6,'net'],['Konten tampil & interaktif',3.6,4.2,'ok']],
    ssr:[['Server merender HTML + data',0,1.4,'srv'],['Konten tampil (belum interaktif)',1.4,2.4,'ok2'],['Unduh JS & hydrate',2.4,3.2,'js'],['Interaktif',3.2,3.6,'ok']],
    ssg:[['HTML jadi dari CDN',0,0.5,'net'],['Konten tampil',0.5,1.2,'ok2'],['Hydrate',1.2,1.9,'js'],['Interaktif',1.9,2.2,'ok']]};
  const N={csr:'<b>CSR</b>: browser menerima halaman kosong lalu membangun semuanya dengan JavaScript. Layar putih lebih lama, buruk untuk SEO.',ssr:'<b>SSR</b>: server mengirim HTML yang sudah berisi data. Konten cepat tampil; JavaScript lalu "menghidupkan" tombol (hydration).',ssg:'<b>SSG</b>: HTML dibuat saat build dan disajikan dari CDN. Paling cepat, cocok untuk konten yang jarang berubah.'};
  host.innerHTML=seg('Strategi',[['csr','CSR'],['ssr','SSR'],['ssg','SSG']],'csr')+'<div class="v3-tl"></div><p class="note"></p>';
  const draw=m=>{$('.v3-tl',host).innerHTML=D[m].map(([l,a,b,c])=>`<div class="v-gr"><span>${l}</span><div class="v-gt"><i class="${c}" style="left:${a/4.4*100}%;width:${(b-a)/4.4*100}%"></i></div></div>`).join('')+`<div class="v-gr"><span></span><div class="v-axis">${[0,1,2,3,4].map(x=>`<b>${x} dtk</b>`).join('')}</div></div>`;$('.note',host).innerHTML=N[m]};
  segWire(host,'.seg',draw);draw('csr');
}
function reactstateViz(host){
  let count=0,n=1,log=[{n:1,c:0,why:'Render pertama'}];
  host.innerHTML=`<div class="v3-rs"><div class="rs-app"><div class="eyebrow">Tampilan</div><p class="rs-v">Keranjang: <b id="rsC">0</b> barang</p><div class="v3-act-row"><button class="btn primary" id="rsAdd">+ Tambah</button><button class="btn" id="rsSame">Set ke nilai sama</button><button class="btn" id="rsVar">Ubah variabel biasa</button></div></div><div><div class="eyebrow">Riwayat render</div><ol class="rs-log" aria-live="polite"></ol></div></div><p class="note"></p>`;
  let plain=0;
  const draw=(note)=>{$('#rsC',host).textContent=count;const ol=$('.rs-log',host);ol.innerHTML=log.slice(-6).map(x=>`<li><b>Render #${x.n}</b> count = ${x.c}<small>${x.why}</small></li>`).join('');if(note)$('.note',host).innerHTML=note;const li=ol.lastElementChild;if(li&&li.animate&&!RM())li.animate([{background:'var(--hl)'},{background:'transparent'}],{duration:900})};
  $('#rsAdd',host).onclick=()=>{count++;n++;log.push({n,c:count,why:'setCount(count + 1)'});draw('<code>setCount</code> menyimpan nilai baru lalu React <b>merender ulang</b> komponen. Hanya teks angka yang berubah di DOM.')};
  $('#rsSame',host).onclick=()=>draw(`<code>setCount(${count})</code> dengan nilai yang sama: React melihat tidak ada perubahan dan <b>melewati</b> render.`);
  $('#rsVar',host).onclick=()=>{plain++;draw(`Variabel biasa berubah menjadi ${plain}, tetapi React <b>tidak tahu</b>, jadi tidak ada render. Itulah kenapa data yang memengaruhi tampilan disimpan di state.`)};
  draw('Tekan tombol untuk melihat kapan komponen dirender ulang.');
}

/* ---------- GIT ---------- */
function gitsimViz(host){
  let C,head,br,n,remote;
  const reset=()=>{C=[{id:'a1',p:[],b:'main',m:'halaman awal'}];br={main:'a1'};head='main';n=1;remote=null};reset();
  const msgs=['tambah produk','gaya tombol','perbaiki harga','tambah keranjang','README','validasi form'];
  host.innerHTML=`<div class="v3-act-row"><button class="btn primary" data-g="commit">git commit</button><button class="btn" data-g="branch">git switch -c fitur</button><button class="btn" data-g="main">git switch main</button><button class="btn" data-g="merge">git merge fitur</button><button class="btn" data-g="push">git push</button><button class="btn" data-g="reset">Ulang</button></div><div class="v3-git"></div><pre class="console v3-term" aria-live="polite"></pre>`;
  let term='$ git log --oneline\na1 halaman awal';
  const draw=()=>{const lanes={main:0,fitur:1},W=Math.max(320,C.length*64+40);
    const pos=Object.fromEntries(C.map((c,i)=>[c.id,{x:30+i*64,y:34+lanes[c.b]*56}]));
    const edges=C.flatMap(c=>c.p.map(p=>`<path d="M${pos[p].x},${pos[p].y} C${pos[p].x+32},${pos[p].y} ${pos[c.id].x-32},${pos[c.id].y} ${pos[c.id].x},${pos[c.id].y}" class="ge"/>`)).join('');
    const nodes=C.map(c=>`<g class="gn ${c.p.length>1?'mg':''} b-${c.b}"><circle cx="${pos[c.id].x}" cy="${pos[c.id].y}" r="11"/><text x="${pos[c.id].x}" y="${pos[c.id].y+28}">${c.id}</text></g>`).join('');
    const tags=Object.entries(br).map(([b,id],k)=>`<g class="gt b-${b}"><rect x="${pos[id].x-30}" y="${pos[id].y-36-(Object.values(br).filter(v=>v===id).indexOf(id)>-1&&b==='fitur'&&br.main===id?16:0)}" width="60" height="16" rx="8"/><text x="${pos[id].x}" y="${pos[id].y-24-(b==='fitur'&&br.main===id?16:0)}">${b}${b===head?' ◀ HEAD':''}</text></g>`).join('');
    const rem=remote?`<g class="gt rm"><rect x="${pos[remote].x-34}" y="${pos[remote].y+36}" width="68" height="16" rx="8"/><text x="${pos[remote].x}" y="${pos[remote].y+48}">origin/main</text></g>`:'';
    $('.v3-git',host).innerHTML=`<svg viewBox="0 0 ${W} 150" width="${W}" height="150" role="img" aria-label="Grafik commit">${edges}${nodes}${tags}${rem}</svg>`;$('.v3-term',host).textContent=term};
  host.addEventListener('click',e=>{const b=e.target.closest('[data-g]');if(!b)return;const g=b.dataset.g;
    if(g==='reset'){reset();term='$ git log --oneline\na1 halaman awal'}
    else if(g==='commit'){n++;const id=(head==='main'?'m':'f')+n,m=msgs[(n-2)%msgs.length];C.push({id,p:[br[head]],b:head,m});br[head]=id;term=`$ git commit -m "${m}"\n[${head} ${id}] ${m}\n 1 file changed`}
    else if(g==='branch'){if(br.fitur){term='fatal: a branch named \'fitur\' already exists';}else{br.fitur=br[head];head='fitur';term="$ git switch -c fitur\nSwitched to a new branch 'fitur'"}}
    else if(g==='main'){head='main';term="$ git switch main\nSwitched to branch 'main'"}
    else if(g==='merge'){if(!br.fitur){term='merge: fitur - not something we can merge'}else if(head!=='main'){term='Pindah dulu ke main: git switch main'}
      else{const anc=id=>{const s=new Set();const go=x=>{if(s.has(x))return;s.add(x);C.find(c=>c.id===x).p.forEach(go)};go(id);return s};
        if(anc(br.main).has(br.fitur))term='Already up to date.';
        else if(anc(br.fitur).has(br.main)){br.main=br.fitur;C.filter(c=>c.b==='fitur').forEach(c=>c.b='fitur');term=`$ git merge fitur\nUpdating... Fast-forward`}
        else{n++;const id='m'+n;C.push({id,p:[br.main,br.fitur],b:'main',m:'merge fitur'});br.main=id;term=`$ git merge fitur\nMerge made by the 'ort' strategy.`}}}
    else if(g==='push'){if(head!=='main'){term=`$ git push -u origin ${head}\n * [new branch] ${head} -> ${head}`}else{remote=br.main;term='$ git push\nTo github.com:sariw/toko.git\n   main -> main'}}
    draw()});draw();
}

/* ---------- DATA ---------- */
function statsViz(host){
  const base=[5.2,5.5,5.8,6.0,6.1,6.3,6.5];
  host.innerHTML=`<div class="v3-ctl">${rng('stX','gaji direktur (juta)',6,60,48,1)}</div><svg class="v3-dots" viewBox="0 0 640 110" role="img" aria-label="Sebaran gaji"></svg><div class="v3-kpis"></div>`;
  const draw=()=>{const x=+$('#stX',host).value;$('#stXo',host).textContent=x;const d=[...base,x].sort((a,b)=>a-b),mean=d.reduce((a,b)=>a+b)/d.length,med=(d[3]+d[4])/2;
    const sx=v=>20+(v-4)/(60-4)*600;
    $('.v3-dots',host).innerHTML=`<line x1="20" x2="620" y1="60" y2="60" class="ax"/>${[10,20,30,40,50,60].map(t=>`<text x="${sx(t)}" y="98" class="tk">${t}</text>`).join('')}${d.map((v,i)=>`<circle cx="${sx(v)}" cy="${60-(i%2)*10}" r="7" class="${v===x?'out':''}"/>`).join('')}<line x1="${sx(mean)}" x2="${sx(mean)}" y1="18" y2="74" class="mean"/><text x="${sx(mean)}" y="14" class="ml">mean</text><line x1="${sx(med)}" x2="${sx(med)}" y1="30" y2="74" class="med"/><text x="${sx(med)}" y="26" class="ml2">median</text>`;
    $('.v3-kpis',host).innerHTML=`<span><b>${mean.toFixed(2)}</b> mean</span><span><b>${med.toFixed(2)}</b> median</span><span><b>${(Math.sqrt(d.reduce((a,v)=>a+(v-mean)**2,0)/(d.length-1))).toFixed(2)}</b> std</span>`};
  host.addEventListener('input',draw);draw();
}
function chartpickViz(host){
  const Q=[['bar','Membandingkan kategori','Omzet per kota: batang mudah dibandingkan panjangnya.'],['line','Tren waktu','Omzet harian: garis menunjukkan naik turun berurutan.'],['hist','Distribusi','Jumlah barang per transaksi: histogram memperlihatkan bentuk sebaran.'],['scatter','Hubungan dua angka','Biaya iklan lawan pengunjung: tiap titik satu hari.'],['stack','Komposisi','Omzet per kota dipecah per kategori.']];
  host.innerHTML=seg('Pertanyaan',Q.map(q=>[q[0],q[1]]),'bar')+'<svg class="v3-chart" viewBox="0 0 360 180" role="img"></svg><p class="note"></p>';
  const V=[78,62,45,30,18],L=['Jkt','Sby','Bdg','Mdn','Yog'];
  const SV={bar:()=>V.map((v,i)=>`<rect x="20" y="${12+i*32}" width="${v*4}" height="22" rx="3" class="c1"/><text x="${28+v*4}" y="${28+i*32}" class="lb">${L[i]} ${v}</text>`).join(''),
    line:()=>{const p=[30,34,31,40,46,43,52,58,55,63,70,68].map((v,i)=>`${20+i*30},${170-v*2}`);return `<polyline points="${p.join(' ')}" class="ln"/>${p.map(x=>`<circle cx="${x.split(',')[0]}" cy="${x.split(',')[1]}" r="3" class="c1"/>`).join('')}`},
    hist:()=>[3,9,16,22,18,11,6,2].map((v,i)=>`<rect x="${20+i*41}" y="${170-v*7}" width="39" height="${v*7}" class="c1"/>`).join(''),
    scatter:()=>[[1,120],[2,190],[3,260],[4,300],[5,390],[6,450],[2.5,210],[4.5,350],[3.5,280],[5.5,410]].map(([a,b])=>`<circle cx="${20+a*52}" cy="${175-b*0.33}" r="5" class="c1"/>`).join(''),
    stack:()=>V.map((v,i)=>[v*.5,v*.3,v*.2].map((w,k,a)=>`<rect x="${20+a.slice(0,k).reduce((s,x)=>s+x,0)*4}" y="${12+i*32}" width="${w*4}" height="22" class="c${k+1}"/>`).join('')+`<text x="${28+v*4}" y="${28+i*32}" class="lb">${L[i]}</text>`).join('')};
  const draw=k=>{$('.v3-chart',host).innerHTML=SV[k]();$('.note',host).innerHTML=Q.find(q=>q[0]===k)[2]};segWire(host,'.seg',draw);draw('bar');
}
function sheetViz(host){
  const R=[['Jakarta','Kopi Gayo',3,255000],['Bandung','Teh Melati',10,250000],['Jakarta','Keripik',25,375000],['Surabaya','Kopi Gayo',2,170000],['Bandung','Madu Hutan',1,120000],['Jakarta','Teh Melati',6,150000],['Medan','Kopi Gayo',4,340000],['Surabaya','Keripik',30,450000]];
  const F=[['=SUM(D2:D9)',r=>true,3,rs=>rs.reduce((a,r)=>a+r[3],0)],['=AVERAGE(C2:C9)',r=>true,2,rs=>rs.reduce((a,r)=>a+r[2],0)/rs.length],['=COUNTIF(A2:A9;"Jakarta")',r=>r[0]==='Jakarta',0,rs=>rs.length],['=SUMIFS(D2:D9;A2:A9;"Jakarta")',r=>r[0]==='Jakarta',3,rs=>rs.reduce((a,r)=>a+r[3],0)],['=MAX(D2:D9)',r=>true,3,rs=>Math.max(...rs.map(r=>r[3]))]];
  host.innerHTML=`<div class="v3-presets">${F.map((f,i)=>`<button class="chip" data-f="${i}" aria-pressed="${i===0}">${esc(f[0])}</button>`).join('')}</div><div class="rt v3-sheet"></div><p class="v3-fx" aria-live="polite"></p>`;
  const draw=i=>{const f=F[i],hit=R.filter(f[1]);host.querySelectorAll('[data-f]').forEach(b=>b.setAttribute('aria-pressed',+b.dataset.f===i));
    $('.v3-sheet',host).innerHTML=`<table><thead><tr><th></th>${['A','B','C','D'].map(c=>`<th>${c}</th>`).join('')}</tr><tr><th>1</th><td>kota</td><td>produk</td><td>jumlah</td><td>omzet</td></tr></thead><tbody>${R.map((r,k)=>`<tr><th>${k+2}</th>${r.map((v,c)=>`<td class="${f[1](r)&&(c===f[2]||(i>=2&&c===0))?'on':''}">${typeof v==='number'&&c===3?v.toLocaleString('id-ID'):esc(v)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
    const v=f[3](hit);$('.v3-fx',host).innerHTML=`<code>${esc(f[0])}</code> → <b>${Number.isInteger(v)?v.toLocaleString('id-ID'):v.toFixed(2).replace('.',',')}</b> (${hit.length} baris ikut dihitung)`};
  host.addEventListener('click',e=>{const b=e.target.closest('[data-f]');if(b)draw(+b.dataset.f)});draw(0);
}
function mapreduceViz(host){
  const chunks=['kopi enak kirim cepat','kopi wangi harga pas','kirim lambat kopi enak'];
  const pairs=chunks.map(c=>c.split(' ').map(w=>[w,1]));const groups={};pairs.flat().forEach(([w])=>(groups[w]=groups[w]||[]).push(1));
  const col=(t,body,on)=>`<div class="mr-col ${on?'on':''}"><b>${t}</b>${body}</div>`;
  const fr=[0,1,2,3].map(s=>({s,note:['Data besar dipecah menjadi potongan yang disebar ke beberapa mesin.','<b>Map</b>: setiap mesin memproses potongannya sendiri secara paralel dan mengeluarkan pasangan (kata, 1).','<b>Shuffle</b>: pasangan dengan kunci yang sama dikirim ke mesin yang sama.','<b>Reduce</b>: setiap kelompok dijumlahkan. Hasil akhir: jumlah setiap kata.'][s]}));
  player(host,fr,(st,f)=>{st.innerHTML=`<div class="v3-mr">${col('Input',chunks.map((c,i)=>`<div class="mr-c">mesin ${i+1}: ${esc(c)}</div>`).join(''),f.s===0)}${f.s>=1?col('Map',pairs.map(p=>`<div class="mr-c">${p.map(([w])=>`(${w},1)`).join(' ')}</div>`).join(''),f.s===1):''}${f.s>=2?col('Shuffle',Object.entries(groups).map(([w,v])=>`<div class="mr-c">${w}: [${v.join(',')}]</div>`).join(''),f.s===2):''}${f.s>=3?col('Reduce',Object.entries(groups).sort((a,b)=>b[1].length-a[1].length).map(([w,v])=>`<div class="mr-c"><b>${w}</b> = ${v.length}</div>`).join(''),true):''}</div>`},{speed:1800});
}
function starschemaViz(host){
  const T={fakta_penjualan:['id','tanggal_id 🔗','produk_id 🔗','toko_id 🔗','jumlah','harga','diskon_persen'],dim_tanggal:['tanggal_id 🔑','tanggal','bulan','kuartal','hari'],dim_produk:['produk_id 🔑','nama','kategori','hpp','harga'],dim_toko:['toko_id 🔑','nama','kota','wilayah']};
  const P={fakta_penjualan:[210,90],dim_tanggal:[20,10],dim_produk:[400,10],dim_toko:[210,220]};
  host.innerHTML=`<p class="muted">Klik tabel dimensi untuk melihat kolom kunci yang menghubungkannya ke tabel fakta.</p><div class="v3-star"></div><pre class="code v3-css"></pre>`;
  let on='dim_produk';
  const draw=()=>{const key=on.replace('dim_','')+'_id';
    $('.v3-star',host).innerHTML=`<svg viewBox="0 0 590 330" role="img" aria-label="Skema bintang">${Object.keys(T).filter(t=>t!=='fakta_penjualan').map(t=>`<line x1="${P[t][0]+85}" y1="${P[t][1]+50}" x2="${P.fakta_penjualan[0]+85}" y2="${P.fakta_penjualan[1]+60}" class="${t===on?'on':''}"/>`).join('')}
    ${Object.entries(T).map(([t,cols])=>`<g class="tb ${t==='fakta_penjualan'?'fact':''} ${t===on?'on':''}" data-t="${t}" tabindex="0" role="button" aria-label="${t}"><rect x="${P[t][0]}" y="${P[t][1]}" width="170" height="${22+cols.length*15}" rx="8"/><text x="${P[t][0]+10}" y="${P[t][1]+16}" class="tn">${t}</text>${cols.map((c,i)=>`<text x="${P[t][0]+10}" y="${P[t][1]+34+i*15}" class="${c.startsWith(key)?'k':''}">${c}</text>`).join('')}</g>`).join('')}</svg>`;
    $('.v3-css',host).innerHTML=hl(`SELECT d.${on==='dim_tanggal'?'bulan':on==='dim_produk'?'kategori':'wilayah'}, SUM(f.jumlah * f.harga) AS omzet\nFROM fakta_penjualan f\nJOIN ${on} d ON d.${key} = f.${key}\nGROUP BY 1;`,'sql')};
  const pick=e=>{const g=e.target.closest('[data-t]');if(g&&g.dataset.t!=='fakta_penjualan'){on=g.dataset.t;draw()}};
  host.addEventListener('click',pick);host.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(e)}});draw();
}
function normCdf(z){const t=1/(1+0.2316419*Math.abs(z)),d=0.3989423*Math.exp(-z*z/2),p=d*t*(0.3193815+t*(-0.3565638+t*(1.781478+t*(-1.821256+t*1.330274))));return z>0?1-p:p}
function abtestViz(host){
  host.innerHTML=`<div class="v3-ab">${['A','B'].map((g,i)=>`<fieldset><legend>Versi ${g}${i?' (perubahan)':' (kontrol)'}</legend><label>Pengunjung <input class="inp" type="number" min="10" id="ab${g}n" value="4000"></label><label>Konversi <input class="inp" type="number" min="0" id="ab${g}k" value="${i?516:448}"></label></fieldset>`).join('')}</div><div class="v3-abo" aria-live="polite"></div>`;
  const draw=()=>{const g=id=>Math.max(0,+$('#'+id,host).value||0);const nA=Math.max(1,g('abAn')),nB=Math.max(1,g('abBn')),kA=Math.min(nA,g('abAk')),kB=Math.min(nB,g('abBk'));
    const pA=kA/nA,pB=kB/nB,pp=(kA+kB)/(nA+nB),se=Math.sqrt(pp*(1-pp)*(1/nA+1/nB))||1e-9,z=(pB-pA)/se,p=2*(1-normCdf(Math.abs(z)));
    const ci=(q,n)=>{const e=1.96*Math.sqrt(q*(1-q)/n);return [Math.max(0,q-e),Math.min(1,q+e)]},cA=ci(pA,nA),cB=ci(pB,nB),pc=x=>(x*100).toFixed(1).replace('.',',')+'%',mx=Math.max(cA[1],cB[1],0.01)*1.15;
    $('.v3-abo',host).innerHTML=`${[['A',pA,cA],['B',pB,cB]].map(([n,q,c])=>`<div class="v-gr"><span>${n}: ${pc(q)}</span><div class="v-gt ci"><i class="${n==='B'?'b':''}" style="left:${c[0]/mx*100}%;width:${(c[1]-c[0])/mx*100}%"></i><em style="left:${q/mx*100}%"></em></div></div>`).join('')}
      <p class="v3-verdict ${p<0.05?'ok':''}">Selisih ${((pB-pA)*100).toFixed(2).replace('.',',')} poin · z = ${z.toFixed(2)} · p = ${p<0.001?'< 0,001':p.toFixed(3).replace('.',',')} → ${p<0.05?'<b>signifikan</b> pada α = 0,05':'<b>belum signifikan</b>; perbedaan masih wajar terjadi karena kebetulan'}.</p><small class="muted">Garis menunjukkan selang kepercayaan 95%, titik menunjukkan tingkat konversi.</small>`};
  host.addEventListener('input',draw);draw();
}
function etlViz(host){
  const S=[['Sumber','kasir, aplikasi'],['Extract','ambil'],['Transform','bersihkan'],['Load','muat'],['Warehouse','siap analisis'],['Dashboard','dipakai']];
  const rec=[`{"id":"101","kota":"  jakarta","total":"Rp 255.000","tgl":"01/10/2024"}`,`{"id":"101","kota":"  jakarta","total":"Rp 255.000","tgl":"01/10/2024"}`,`{"id":101,"kota":"Jakarta","total":255000,"tanggal":"2024-10-01"}`,`INSERT ... ON CONFLICT (id) DO UPDATE`,`fakta_penjualan: 1 baris, tanggal_id 20241001`,`Omzet Jakarta 1 Okt: Rp 255.000`];
  stageViz(host,S,S.map((s,i)=>({on:[i],extra:`<code>${esc(rec[i])}</code>`,note:['Data lahir di sistem operasional: database kasir, event aplikasi, berkas pemasok.','<b>Extract</b>: data diambil, sebaiknya inkremental (hanya yang baru sejak kemarin).','<b>Transform</b>: rapikan teks, ubah tipe, buang duplikat, samakan format tanggal.','<b>Load</b>: muat secara idempoten agar aman dijalankan ulang.','Data tersimpan di warehouse dalam model bintang.','Dashboard dan analis membaca data yang sudah bersih.'][i]})));
}
function batchstreamViz(host){
  const ev=[1,2,2.5,4,5.5,6,7.5,9,10,11.5];
  const fr=[0,2,4,6,8,10,12].map(t=>({t,note:t===0?'Peristiwa (titik) datang sepanjang waktu. Bandingkan kapan hasilnya tersedia.':`Menit ${t}: streaming sudah memproses ${ev.filter(e=>e<=t).length} peristiwa; batch (tiap 6 menit) baru memproses ${ev.filter(e=>e<=Math.floor(t/6)*6).length}.`}));
  player(host,fr,(st,f)=>{const x=v=>v/12*100;st.innerHTML=`<div class="v3-bs">${[['Peristiwa',ev.map(e=>`<i class="ev ${e<=f.t?'on':''}" style="left:${x(e)}%"></i>`).join('')],['Streaming',ev.filter(e=>e<=f.t).map(e=>`<i class="ok" style="left:${x(e+0.2)}%"></i>`).join('')],['Batch',[6,12].filter(b=>b<=f.t).map(b=>`<i class="blk" style="left:${x(b)-1}%"><span>${ev.filter(e=>e<=b&&e>b-6).length}</span></i>`).join('')]].map(([n,b])=>`<div class="bs-r"><span>${n}</span><div class="bs-t">${b}<em style="left:${x(f.t)}%"></em></div></div>`).join('')}<div class="bs-r"><span></span><div class="v-axis">${[0,2,4,6,8,10,12].map(v=>`<b class="${v===f.t?'cur':''}">${v}</b>`).join('')}</div></div></div>`},{speed:1300});
}
function kafkaViz(host){
  const E=[['p-101','dibayar'],['p-102','dibayar'],['p-101','dikemas'],['p-103','dibayar'],['p-102','dikirim'],['p-101','dikirim']];
  const part=k=>[...k].reduce((a,c)=>a+c.charCodeAt(0),0)%3;
  const fr=[];const P=[[],[],[]],off=[0,0,0];
  fr.push({P:P.map(x=>[...x]),off:[...off],note:'Topik <code>pesanan</code> punya 3 partisi. Consumer group "gudang" punya 2 consumer: C1 membaca partisi 0 dan 1, C2 membaca partisi 2.'});
  E.forEach(([k,v])=>{const p=part(k);P[p].push(k+' '+v);fr.push({P:P.map(x=>[...x]),off:[...off],hl:[p,P[p].length-1],note:`Producer mengirim <b>${k}: ${v}</b>. Key yang sama selalu masuk partisi yang sama (partisi ${p}), sehingga urutan per pesanan terjaga.`})});
  [0,1,2].forEach(p=>{off[p]=P[p].length;fr.push({P:P.map(x=>[...x]),off:[...off],note:`${p<2?'C1':'C2'} membaca partisi ${p} sampai offset ${off[p]} lalu meng-commit offset. Pesan tetap tersimpan dan bisa dibaca ulang grup lain.`})});
  player(host,fr,(st,f)=>{st.innerHTML=`<div class="v3-kf"><div class="kf-p"><b>Producer</b><small>aplikasi toko</small></div><div class="kf-parts">${f.P.map((xs,p)=>`<div class="kf-row"><span>P${p}</span><div class="kf-log">${xs.map((x,i)=>`<i class="${f.hl&&f.hl[0]===p&&f.hl[1]===i?'new':''} ${i<f.off[p]?'read':''}">${i}<small>${esc(x)}</small></i>`).join('')}</div><span class="kf-c">${p<2?'C1':'C2'} · offset ${f.off[p]}</span></div>`).join('')}</div></div>`},{speed:1500});
}

/* ---------- DESAIN ---------- */
function foggViz(host){
  host.innerHTML=`<div class="v3-ctl">${rng('fgM','Motivasi',1,10,3)}${rng('fgA','Kemudahan',1,10,3)}</div><svg class="v3-fogg" viewBox="0 0 320 220" role="img" aria-label="Model perilaku Fogg"></svg><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const m=+$('#fgM',host).value,a=+$('#fgA',host).value;$('#fgMo',host).textContent=m;$('#fgAo',host).textContent=a;
    const X=v=>30+v*27,Y=v=>200-v*18,curve=Array.from({length:46},(_,i)=>{const x=1+i*0.2;return `${X(x)},${Y(Math.min(10.5,14/x))}`}).join(' '),ok=m*a>=14;
    $('.v3-fogg',host).innerHTML=`<line x1="30" y1="200" x2="310" y2="200" class="ax"/><line x1="30" y1="200" x2="30" y2="8" class="ax"/><text x="300" y="215" class="tk" text-anchor="end">mudah →</text><text x="36" y="16" class="tk">motivasi tinggi</text><polyline points="${curve}" class="al"/><text x="250" y="${Y(14/8.6)-8}" class="tk">garis aksi</text><circle cx="${X(a)}" cy="${Y(m)}" r="9" class="${ok?'ok':'bad'}"/>`;
    $('.v3-verdict',host).innerHTML=ok?'Di atas garis aksi: saat <b>pemicu</b> datang, pengguna kemungkinan bertindak.':'Di bawah garis aksi: pemicu hanya mengganggu. Naikkan <b>kemudahan</b> (lebih sedikit langkah) atau motivasi.';$('.v3-verdict',host).classList.toggle('ok',ok)};
  host.addEventListener('input',draw);draw();
}
function hookViz(host){
  const S=[['Trigger','Notifikasi 19.00 "Waktunya belajar 10 menit"','Lama-lama pemicunya internal: rasa ingin menjaga kebiasaan.'],['Action','Satu ketukan "Lanjut pelajaran"','Tindakan dibuat sesederhana mungkin.'],['Variable reward','Kuis acak, kadang lencana kejutan','Hadiah yang tidak selalu sama membuat penasaran.'],['Investment','Streak hari ke-n, catatan pribadi','Pengguna menaruh sesuatu yang membuat pemicu berikutnya lebih kuat.']];
  const fr=[];for(let lap=1;lap<=2;lap++)S.forEach((s,i)=>fr.push({i,lap,note:`<b>${s[0]}</b>: ${s[1]}. ${s[2]}${lap===2&&i===3?' Putaran kedua: streak bertambah, kebiasaan menguat.':''}`}));
  player(host,fr,(st,f)=>{const pos=[[160,30],[290,120],[160,210],[30,120]];st.innerHTML=`<svg class="v3-hook" viewBox="0 0 320 240" role="img" aria-label="Siklus Hook"><circle cx="160" cy="120" r="88" class="ring"/>${S.map((s,i)=>`<g class="${i===f.i?'on':''}"><circle cx="${pos[i][0]}" cy="${pos[i][1]}" r="${i===f.i?30:24}"/><text x="${pos[i][0]}" y="${pos[i][1]+4}">${s[0].split(' ').pop()}</text></g>`).join('')}<text x="160" y="116" class="mid">putaran ${f.lap}</text><text x="160" y="134" class="mid sm">streak ${f.lap===1?(f.i===3?1:0):(f.i===3?2:1)} hari</text></svg>`},{speed:1600});
}
function tokensViz(host){
  const TH={terang:{'teal.700':'#0F766E','gray.50':'#F6F7F5','gray.900':'#1C1B19',white:'#FFFFFF'},gelap:{'teal.300':'#5EEAD4','gray.950':'#121413','gray.100':'#ECEDEA','gray.900':'#06201D'},merek:{'orange.700':'#C2410C','cream.50':'#FFF7ED','brown.900':'#3B1D0F',white:'#FFFFFF'}};
  const MAP={terang:[['color.bg','gray.50'],['color.text','gray.900'],['color.action.primary','teal.700'],['color.on-action','white']],gelap:[['color.bg','gray.950'],['color.text','gray.100'],['color.action.primary','teal.300'],['color.on-action','gray.900']],merek:[['color.bg','cream.50'],['color.text','brown.900'],['color.action.primary','orange.700'],['color.on-action','white']]};
  host.innerHTML=seg('Tema',[['terang','Terang'],['gelap','Gelap'],['merek','Merek lain']],'terang')+'<div class="v3-tok"></div>';
  const draw=t=>{const v=Object.fromEntries(MAP[t].map(([s,p])=>[s,TH[t][p]]));
    $('.v3-tok',host).innerHTML=`<table class="tk-t"><thead><tr><th>Komponen</th><th>Semantik</th><th>Primitif</th></tr></thead><tbody>${MAP[t].map(([s,p])=>`<tr><td>${s==='color.action.primary'?'button.primary.bg':s==='color.on-action'?'button.primary.text':'halaman'}</td><td><code>${s}</code></td><td><i class="sw" style="background:${TH[t][p]}"></i><code>${p}</code> ${TH[t][p]}</td></tr>`).join('')}</tbody></table>
     <div class="tk-prev" style="background:${v['color.bg']};color:${v['color.text']}"><b>Saldo tabungan</b><span>Rp 2.400.000</span><button style="background:${v['color.action.primary']};color:${v['color.on-action']}">Tambah setoran</button></div>`};
  segWire(host,'.seg',draw);draw('terang');
}
function lum(hex){const c=hex.replace('#','').match(/../g).map(x=>parseInt(x,16)/255).map(v=>v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4);return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]}
function contrastViz(host){
  host.innerHTML=`<div class="v3-ctl"><label class="v3-col">Teks <input type="color" id="ctF" value="#0f766e"></label><label class="v3-col">Latar <input type="color" id="ctB" value="#ffffff"></label></div><div class="v3-presets">${[['#1c1b19','#ffffff'],['#0f766e','#ffffff'],['#5eead4','#ffffff'],['#b91c1c','#fef2f2'],['#9ca3af','#ffffff'],['#ecedea','#121413']].map(([f,b])=>`<button class="chip" data-f="${f}" data-b="${b}"><i class="sw" style="background:${f}"></i>/<i class="sw" style="background:${b}"></i></button>`).join('')}</div><div class="v3-ct" aria-live="polite"></div>`;
  const draw=()=>{const f=$('#ctF',host).value,b=$('#ctB',host).value,L1=lum(f),L2=lum(b),r=(Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
    const row=(n,need)=>`<span class="${r>=need?'ok':'bad'}">${r>=need?'✓':'✗'} ${n} (≥ ${need}:1)</span>`;
    $('.v3-ct',host).innerHTML=`<div class="ct-prev" style="color:${f};background:${b}"><b style="font-size:1.4rem">Rp 2.400.000</b><span>Teks isi 16px untuk dibaca pengguna.</span></div><div class="ct-r"><b>${r.toFixed(2).replace('.',',')}:1</b><div>${row('AA teks normal',4.5)}${row('AA teks besar & komponen UI',3)}${row('AAA teks normal',7)}</div></div>`};
  host.addEventListener('input',draw);host.addEventListener('click',e=>{const c=e.target.closest('[data-f]');if(c){$('#ctF',host).value=c.dataset.f;$('#ctB',host).value=c.dataset.b;draw()}});draw();
}
function typescaleViz(host){
  const R=[['1.125','Major second'],['1.2','Minor third'],['1.25','Major third'],['1.333','Perfect fourth'],['1.5','Perfect fifth']];
  host.innerHTML=`<div class="v3-ctl">${rng('tsB','ukuran dasar',14,20,16,1,'px')}<label class="v3-r"><span>rasio</span><select class="inp" id="tsR">${R.map(([v,n])=>`<option value="${v}" ${v==='1.25'?'selected':''}>${v} · ${n}</option>`).join('')}</select></label></div><div class="v3-ts"></div>`;
  const draw=()=>{const b=+$('#tsB',host).value,r=+$('#tsR',host).value;$('#tsBo',host).textContent=b+'px';
    $('.v3-ts',host).innerHTML=[4,3,2,1,0,-1].map(k=>{const px=b*r**k;return `<div class="ts-r"><code>${k>=0?'font-size-'+(k+2)+'00':'font-size-100'}</code><small>${px.toFixed(1)}px · ${(px/16).toFixed(3)}rem</small><span style="font-size:${Math.min(px,56)}px">Celengan</span></div>`}).join('')};
  host.addEventListener('input',draw);draw();
}

Object.assign(VIZ2,{http:httpViz,specificity:specificityViz,boxmodel:boxmodelViz,flexbox:flexboxViz,grid:gridViz,render:renderViz,jsloop:jsloopViz,vitals:vitalsViz,ssr:ssrViz,reactstate:reactstateViz,
  gitsim:gitsimViz,stats:statsViz,chartpick:chartpickViz,sheet:sheetViz,mapreduce:mapreduceViz,starschema:starschemaViz,abtest:abtestViz,etl:etlViz,batchstream:batchstreamViz,kafka:kafkaViz,
  fogg:foggViz,hook:hookViz,tokens:tokensViz,contrast:contrastViz,typescale:typescaleViz});
Object.assign(VIZ2T,{http:'Perjalanan sebuah permintaan web',specificity:'Kalkulator specificity',boxmodel:'Box model interaktif',flexbox:'Taman bermain flexbox',grid:'Taman bermain grid',render:'Pipeline render browser',jsloop:'Event loop JavaScript',vitals:'Core Web Vitals',ssr:'CSR, SSR, dan SSG',reactstate:'State dan render ulang',
  gitsim:'Simulator Git',stats:'Mean lawan median',chartpick:'Memilih grafik',sheet:'Lembar kerja & rumus',mapreduce:'MapReduce langkah demi langkah',starschema:'Skema bintang',abtest:'Kalkulator A/B test',etl:'Data mengalir lewat ETL',batchstream:'Batch lawan streaming',kafka:'Kafka: partisi & consumer',
  fogg:'Model perilaku Fogg',hook:'Siklus Hook',tokens:'Token tiga lapis',contrast:'Pemeriksa kontras',typescale:'Skala tipografi'});
