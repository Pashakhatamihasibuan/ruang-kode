/* ===================== VISUALISASI ===================== */
/* Bahasa pelajaran yang sedang dibuka. Di jalur Java, lab hanya menampilkan Java (tanpa kolom Python). */
let VLANG=null;
const JO=()=>VLANG==='java';
const VIZ = {
compile(el){
  const J=['Halo.java','javac (compiler)','Halo.class (bytecode)','JVM menjalankan','Keluaran'];
  const P=['halo.py','python (interpreter)','bytecode internal','eksekusi baris demi baris','Keluaran'];
  const notes=['Semua dimulai dari <b>kode sumber</b>, yaitu teks yang kamu tulis.',
    'Java: <code>javac</code> memeriksa seluruh file. Error sintaks ketahuan di sini, sebelum program jalan. Python: interpreter langsung mengambil alih.',
    'Java menyimpan bytecode ke file <code>Halo.class</code>. Python juga membuat bytecode, tapi otomatis dan tersembunyi.',
    'JVM menjalankan bytecode. Interpreter Python mengeksekusi perintah satu per satu.',
    'Teks tampil di layar. Pada Python, error di baris 10 baru ketahuan saat baris 10 dijalankan.'];
  const notesJ=['Semua dimulai dari <b>kode sumber</b>, yaitu teks yang kamu tulis di file <code>Halo.java</code>.',
    '<code>javac</code> memeriksa seluruh file. Error sintaks ketahuan di sini, sebelum program jalan.',
    'Hasil kompilasi disimpan sebagai <b>bytecode</b> di file <code>Halo.class</code>.',
    'JVM (Java Virtual Machine) menjalankan bytecode. Karena itu file .class yang sama bisa jalan di Windows, macOS, dan Linux.',
    'Teks tampil di layar.'];
  const frames=(JO()?notesJ:notes).map((n,s)=>({s,note:n}));
  const lane=(name,cls,arr,s)=>`<div class="lane"><span class="lane-name ${cls}">${name}</span>${arr.map((x,i)=>`${i?'<span class="arrow">→</span>':''}<span class="node ${i<=s?'on':''} ${i===s?'cur':''}">${x}</span>`).join('')}</div>`;
  player(el,frames,(st,f)=>{st.innerHTML=lane('JAVA','j',J,f.s)+(JO()?'':lane('PYTHON','p',P,f.s))});
},
forloop(el){
  el.innerHTML=`<div class="row"><label for="fl-n">Nilai n:</label><select class="inp" id="fl-n">${[2,3,4,5].map(v=>`<option ${v===3?'selected':''}>${v}</option>`).join('')}</select></div><div class="pl"></div>`;
  const build=n=>{
    const fr=[];let out='';
    fr.push({ph:'init',i:1,out,note:'<b>Inisialisasi</b> <code>int i = 1</code>. Bagian ini hanya dijalankan sekali.'});
    for(let i=1;i<=n;i++){
      fr.push({ph:'check',i,out,note:`<b>Cek kondisi</b> <code>${i} &lt;= ${n}</code> bernilai <span class="val-t">true</span>, jadi masuk ke badan loop.`});
      out+='*'.repeat(i)+'\n';
      fr.push({ph:'body',i,out,note:`<b>Badan loop</b> mencetak ${i} bintang.`});
      fr.push({ph:'upd',i:i+1,out,note:`<b>Update</b> <code>i++</code>, sekarang i = ${i+1}.`});
    }
    fr.push({ph:'check',i:n+1,out,end:true,note:`<b>Cek kondisi</b> <code>${n+1} &lt;= ${n}</code> bernilai <span class="val-f">false</span>. Loop selesai setelah ${n} putaran.`});
    return fr;
  };
  const draw=(st,f)=>{
    const n=+$('#fl-n',el).value;
    const on=p=>f.ph===p?'on':'';
    st.innerHTML=`<div class="grid2">
      <div><div class="eyebrow" style="color:var(--java)">Java</div><div class="mini">for (<span class="${on('init')}">int i = 1</span>; <span class="${on('check')}">i &lt;= ${n}</span>; <span class="${on('upd')}">i++</span>) {
    <span class="${on('body')}">System.out.println("*".repeat(i));</span>
}</div></div>
      ${JO()?'':`<div><div class="eyebrow" style="color:var(--py)">Python</div><div class="mini"><span class="${f.ph!=='body'?'on':''}">for i in range(1, ${n} + 1):</span>
    <span class="${on('body')}">print("*" * i)</span></div></div>`}
    </div>
    <div class="row" style="margin-top:12px"><span class="var">i = <b>${f.i}</b></span><span class="var">n = <b>${n}</b></span></div>
    <div class="console" style="margin-top:10px">${esc(f.out)}</div>`;
  };
  const p=player($('.pl',el),build(3),draw);
  $('#fl-n',el).addEventListener('change',e=>p.set(build(+e.target.value)));
},
callstack(el){
  const F=(f,v,cls='')=>({f,v,cls});
  const frames=[
    {st:[F('main',{})],out:'',note:'Program dimulai. Bingkai <b>main</b> dibuat di call stack.'},
    {st:[F('main',{}),F('kuadrat',{x:3},'top')],out:'',note:'main memanggil <code>kuadrat(3)</code>. Argumen 3 disalin ke parameter <code>x</code> di bingkai baru.'},
    {st:[F('main',{}),F('kuadrat',{x:3,'return':9},'ret')],out:'',note:'kuadrat menghitung <code>x * x</code> = 9 lalu <code>return</code>.'},
    {st:[F('main',{a:9})],out:'',note:'Bingkai kuadrat dibuang. Nilai 9 disimpan ke <code>a</code>. Variabel x sudah tidak ada lagi (scope).'},
    {st:[F('main',{a:9}),F('kuadrat',{x:4},'top')],out:'',note:'Panggilan kedua <code>kuadrat(4)</code> mendapat bingkai baru dengan x = 4.'},
    {st:[F('main',{a:9}),F('kuadrat',{x:4,'return':16},'ret')],out:'',note:'Mengembalikan 16.'},
    {st:[F('main',{a:9,b:16})],out:'',note:'Nilai 16 disimpan ke <code>b</code>.'},
    {st:[F('main',{a:9,b:16})],out:'25',note:'main mencetak <code>a + b</code> = 25. Program selesai.'}
  ];
  const code=`<div class="grid2"><div class="mini"><span class="k">static int</span> kuadrat(<span class="k">int</span> x) {
    <span class="k">return</span> x * x;
}
<span class="c">// di main:</span>
<span class="k">int</span> a = kuadrat(3);
<span class="k">int</span> b = kuadrat(4);
System.out.println(a + b);</div><div class="mini"><span class="k">def</span> kuadrat(x):
    <span class="k">return</span> x * x

<span class="c"># di main:</span>
a = kuadrat(3)
b = kuadrat(4)
print(a + b)</div></div>`;
  el.innerHTML=code+'<div class="pl"></div>';
  player($('.pl',el),frames,(st,f)=>{
    st.innerHTML=`<div class="eyebrow" style="margin:6px 0 8px">Call stack (atas = sedang berjalan)</div><div class="frames">${f.st.map(fr=>`<div class="frame ${fr.cls}"><b>${fr.f}()</b>${Object.entries(fr.v).map(([k,v])=>`<span>${k} = ${v}</span>`).join('')||'<span style="color:var(--muted)">belum ada variabel</span>'}</div>`).join('')}</div><div class="console" style="margin-top:10px">${f.out}</div>`;
  });
},
ifelse(el){
  el.innerHTML=`<div class="row"><label for="ie-s">Skor:</label><input type="range" id="ie-s" min="0" max="100" value="85" style="flex:1;min-width:160px"><span class="big" id="ie-v">85</span></div><div class="flow" id="ie-f"></div><div class="row"><span>Hasil:</span><span class="big" id="ie-r"></span></div>`;
  const conds=[['skor >= 90','skor >= 90','A',90],['skor >= 80','skor >= 80','B',80],['skor >= 70','skor >= 70','C',70]];
  const upd=()=>{
    const s=+$('#ie-s',el).value;$('#ie-v',el).textContent=s;
    let done=false,res='D',html='';
    conds.forEach(([j,p,g,t],i)=>{
      let cls,r;
      if(done){cls='skip';r='dilewati'}else if(s>=t){cls='t';r='true';done=true;res=g}else{cls='f';r='false'}
      html+=`<div class="dec ${cls}"><code>${i?'else if':'if'} (${esc(j)})</code><span style="color:var(--muted)">·</span><code>${i?'elif':'if'} ${esc(p)}:</code><span>→ ${g}</span><span class="res">${r}</span></div>`;
    });
    html+=`<div class="dec ${done?'skip':'t'}"><code>else</code><span>→ D</span><span class="res">${done?'dilewati':'dijalankan'}</span></div>`;
    $('#ie-f',el).innerHTML=html;$('#ie-r',el).textContent=res;
  };
  $('#ie-s',el).addEventListener('input',upd);upd();
},
boolean(el){
  let p=true,q=false;
  el.innerHTML=`<div class="grid2"><div><div class="row"><button class="toggle" id="bp"></button><button class="toggle" id="bq"></button><span style="color:var(--muted);font-size:.85rem">klik untuk mengubah</span></div>
  <table class="tt" style="margin-top:10px"><thead><tr><th>Java</th>${JO()?'':'<th>Python</th>'}<th>Hasil</th></tr></thead><tbody id="btb"></tbody></table></div>
  <div><div class="eyebrow">Loop while: lempar sampai dapat 6</div><div class="mini" style="margin:8px 0">while (dadu != 6) { ... }</div><div class="row"><button class="btn primary" id="roll">Lempar dadu</button><span id="rcount" class="log"></span></div><div class="row" id="dice" style="margin-top:10px"></div></div></div>`;
  const B=v=>`<span class="${v?'val-t':'val-f'}">${v}</span>`;
  const upd=()=>{
    $('#bp',el).innerHTML=`p = ${B(p)}`;$('#bq',el).innerHTML=`q = ${B(q)}`;
    const rows=[['p &amp;&amp; q','p and q',p&&q],['p || q','p or q',p||q],['!p','not p',!p],['!(p &amp;&amp; q)','not (p and q)',!(p&&q)],['!p || !q','not p or not q',!p||!q]];
    $('#btb',el).innerHTML=rows.map(r=>`<tr><td><code>${r[0]}</code></td>${JO()?'':`<td><code>${r[1]}</code></td>`}<td>${B(r[2])}</td></tr>`).join('');
  };
  $('#bp',el).onclick=()=>{p=!p;upd()};$('#bq',el).onclick=()=>{q=!q;upd()};upd();
  $('#roll',el).onclick=()=>{
    clearTimers();const box=$('#dice',el);box.innerHTML='';let n=0;$('#rcount',el).textContent='';
    const t=setInterval(()=>{
      const d=rnd(1,6);n++;box.insertAdjacentHTML('beforeend',`<span class="die ${d===6?'six':''}">${d}</span>`);
      if(d===6||n>=40){clearInterval(t);$('#rcount',el).innerHTML=`Kondisi <code>dadu != 6</code> menjadi false setelah <b>${n}</b> lemparan.`}
    },260);TIMERS.push(t);
  };
},
file(el){
  const lines=[['Budi','85','90'],['Sari','78','92']];
  const fr=[];let out='';
  lines.forEach((ln,li)=>{
    fr.push({li,ti:-1,nama:'-',total:0,n:0,out,note:`<code>nextLine()</code> membaca satu baris utuh: "${ln.join(' ')}".`});
    fr.push({li,ti:0,nama:ln[0],total:0,n:0,out,note:`<code>next()</code> mengambil token pertama: nama = "${ln[0]}".`});
    let total=0,n=0;
    for(let k=1;k<ln.length;k++){total+=+ln[k];n++;fr.push({li,ti:k,nama:ln[0],total,n,out,note:`<code>hasNextInt()</code> true, <code>nextInt()</code> = ${ln[k]}. total = ${total}.`})}
    out+=`${ln[0]}: ${(total/n).toFixed(1)}\n`;
    fr.push({li,ti:ln.length,nama:ln[0],total,n,out,note:`<code>hasNextInt()</code> false karena baris habis. Cetak rata-rata ${total} / ${n} = ${(total/n).toFixed(1)}.`});
  });
  fr.push({li:2,ti:-1,nama:'-',total:0,n:0,out,note:'<code>hasNextLine()</code> false. File selesai dibaca.'});
  player(el,fr,(st,f)=>{
    st.innerHTML=`<div class="eyebrow" style="margin-bottom:6px">nilai.txt</div><div class="mini" style="white-space:normal">${lines.map((ln,li)=>`<div>${ln.map((t,ti)=>{let c='';if(li<f.li||(li===f.li&&ti<f.ti))c='used';if(li===f.li&&ti===f.ti)c='cur';return `<span class="tok ${c}">${t}</span>`}).join('')}</div>`).join('')}</div>
    <div class="vars" style="margin-top:10px"><span class="var">nama = <b>${esc(f.nama)}</b></span><span class="var">total = <b>${f.total}</b></span><span class="var">n = <b>${f.n}</b></span></div>
    <div class="console" style="margin-top:10px">${esc(f.out)}</div>`;
  });
},
array(el){
  const base=[3,8,1,9,4];
  el.innerHTML=`<div class="row"><label for="ar-i">Indeks:</label><input class="inp" type="number" id="ar-i" value="2"><button class="btn primary" id="ar-go">Akses a[i]</button></div>
  <div id="ar-cells"></div><div id="ar-res" class="vars"></div>
  <div style="border-top:1px solid var(--line);padding-top:14px;display:flex;flex-direction:column;gap:10px">
   <div class="eyebrow">Referensi: apa yang terjadi pada a?</div>
   <div class="row"><button class="btn" id="ar-alias">b = a</button><button class="btn" id="ar-copy">b = salinan a</button><button class="btn primary" id="ar-set" disabled>b[0] = 99</button></div>
   <div id="ar-ref" class="log">Pilih cara membuat b terlebih dahulu.</div><div id="ar-refv"></div></div>`;
  const cells=(hi)=>$('#ar-cells',el).innerHTML=cellsHTML(base,i=>i===hi?'hl':'');
  cells(-1);
  $('#ar-go',el).onclick=()=>{
    const i=parseInt($('#ar-i',el).value,10);const n=base.length;
    if(isNaN(i))return;
    const jOk=i>=0&&i<n, pOk=i>=-n&&i<n, pi=i<0?n+i:i;
    cells(jOk?i:(pOk?pi:-1));
    $('#ar-res',el).innerHTML=`<span class="var" style="border-color:var(--java)">Java <code>a[${i}]</code> → ${jOk?`<b>${base[i]}</b>`:'<span class="err">ArrayIndexOutOfBoundsException</span>'}</span>
      <span class="var" style="border-color:var(--py)">Python <code>a[${i}]</code> → ${pOk?`<b>${base[pi]}</b>${i<0?' (indeks negatif dihitung dari belakang)':''}`:'<span class="err">IndexError</span>'}</span>`;
  };
  let mode=null,a=[...base],b=null;
  const drawRef=()=>{
    if(!mode){$('#ar-refv',el).innerHTML='';return}
    const row=(lbl,arr)=>`<div class="row" style="flex-wrap:nowrap"><span class="var" style="flex:none">${lbl} →</span>${cellsHTML(arr,(i)=>i===0&&arr[0]===99?'new':'',false)}</div>`;
    $('#ar-refv',el).innerHTML=`<div style="overflow-x:auto">${mode==='alias'?row('a, b',a):row('a',a)+row('b',b)}</div>`;
  };
  $('#ar-alias',el).onclick=()=>{mode='alias';a=[...base];b=a;$('#ar-set',el).disabled=false;$('#ar-ref',el).innerHTML='<code>b = a</code> hanya menyalin <b>referensi</b>. a dan b menunjuk array yang sama.';drawRef()};
  $('#ar-copy',el).onclick=()=>{mode='copy';a=[...base];b=[...base];$('#ar-set',el).disabled=false;$('#ar-ref',el).innerHTML='<code>Arrays.copyOf(a, 5)</code> / <code>a.copy()</code> membuat array <b>baru</b> dengan isi yang sama.';drawRef()};
  $('#ar-set',el).onclick=()=>{b[0]=99;$('#ar-ref',el).innerHTML=mode==='alias'?'a[0] ikut menjadi <b>99</b> karena a dan b adalah array yang sama.':'Hanya b yang berubah. a tetap <b>3</b> karena keduanya array terpisah.';drawRef()};
},
objects(el){
  let objs=[],k=0;
  el.innerHTML=`<div class="grid2"><div class="blueprint">class Titik<br>  field: x, y<br>  geser(dx, dy)<br>  jarakKeAsal()<br>  toString()</div>
   <div class="row" style="align-content:flex-start"><button class="btn primary" id="ob-new">new Titik(x, y)</button><button class="btn" id="ob-clr">Hapus semua</button><p class="log" id="ob-log" style="flex-basis:100%">Kelas hanyalah cetak biru. Klik tombol untuk membuat objek.</p></div></div>
   <div class="objs" id="ob-list"></div>`;
  const draw=(hi)=>{
    $('#ob-list',el).innerHTML=objs.map((o,i)=>`<div class="obj" ${i===hi?'style="border-color:var(--ok)"':''}><span class="nm">p${o.id} → Titik</span><span>x = <b>${o.x}</b>, y = <b>${o.y}</b></span><span style="color:var(--muted);font-size:.82rem">jarak = ${Math.sqrt(o.x*o.x+o.y*o.y).toFixed(2)}</span><button class="btn" data-i="${i}">p${o.id}.geser(1, 1)</button></div>`).join('');
  };
  $('#ob-new',el).onclick=()=>{
    if(objs.length>=6){$('#ob-log',el).textContent='Cukup enam objek dulu. Hapus untuk mulai lagi.';return}
    const o={id:++k,x:rnd(0,9),y:rnd(0,9)};objs.push(o);
    $('#ob-log',el).innerHTML=`Konstruktor berjalan: <code>Titik p${o.id} = new Titik(${o.x}, ${o.y});</code> Objek ini punya field sendiri.`;draw(objs.length-1);
  };
  $('#ob-clr',el).onclick=()=>{objs=[];k=0;draw();$('#ob-log',el).textContent='Semua objek dihapus.'};
  $('#ob-list',el).addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const i=+b.dataset.i;objs[i].x++;objs[i].y++;
    $('#ob-log',el).innerHTML=`<code>p${objs[i].id}.geser(1, 1)</code> hanya mengubah objek p${objs[i].id}. Objek lain tidak tersentuh.`;draw(i)});
  $('#ob-new',el).click();$('#ob-new',el).click();
},
inherit(el){
  const kids={Kucing:'Meong',Anjing:'Guk',Burung:'Cuit'};
  el.innerHTML=`<div class="tree-cls"><div class="cls abs">«abstrak» Hewan<br><small>kenalkan(), suara()</small></div><div style="color:var(--muted)">▲ extends ▲</div>
  <div class="kids">${Object.keys(kids).map(k=>`<button class="cls" data-k="${k}" aria-pressed="false">${k}</button>`).join('')}</div></div>
  <div id="in-info" class="log">Pilih salah satu kelas anak.</div>
  <div class="row"><button class="btn primary" id="in-run">Jalankan loop polimorfis</button></div><div class="console" id="in-out"></div>`;
  el.querySelectorAll('.kids .cls').forEach(b=>b.onclick=()=>{
    el.querySelectorAll('.kids .cls').forEach(x=>x.setAttribute('aria-pressed',x===b));
    const k=b.dataset.k;
    $('#in-info',el).innerHTML=`<b>${k}</b> mewarisi <code>nama</code> dan <code>kenalkan()</code> dari Hewan apa adanya, lalu <b>override</b> <code>suara()</code> sehingga mengembalikan "${kids[k]}".`;
  });
  $('#in-run',el).onclick=()=>{
    clearTimers();const names={Kucing:'Tom',Anjing:'Spike',Burung:'Tweety'};const out=$('#in-out',el);out.textContent='';let i=0;const ks=Object.keys(kids);
    const t=setInterval(()=>{const k=ks[i];out.textContent+=`${names[k]} berkata ${kids[k]}   ← h adalah ${k}\n`;i++;if(i>=ks.length)clearInterval(t)},450);TIMERS.push(t);
  };
},
arraylist(el){
  let L=['apel','mangga','jeruk'];
  el.innerHTML=`<div class="row"><label for="al-v">Nilai</label><input class="inp" id="al-v" value="pisang"><label for="al-i">Indeks</label><input class="inp" type="number" id="al-i" value="1" style="width:4.5em"></div>
  <div class="row"><button class="btn" data-o="add">add(nilai)</button><button class="btn" data-o="ins">add(indeks, nilai)</button><button class="btn" data-o="rem">remove(indeks)</button><button class="btn" data-o="reset">Ulang</button></div>
  <div style="overflow-x:auto" id="al-c"></div><div class="vars"><span class="var" id="al-s"></span></div><p class="log" id="al-log">Coba sisipkan "pisang" di indeks 1.</p>`;
  const draw=(f=()=>'')=>{$('#al-c',el).innerHTML=cellsHTML(L,f);$('#al-s',el).innerHTML=`size() / len() = <b>${L.length}</b>`};
  draw();
  el.querySelector('.row:nth-child(2)').addEventListener('click',e=>{
    const b=e.target.closest('button');if(!b)return;const o=b.dataset.o;
    const v=($('#al-v',el).value||'x').slice(0,10);const i=parseInt($('#al-i',el).value,10);const log=$('#al-log',el);
    if(o==='reset'){L=['apel','mangga','jeruk'];draw();log.textContent='Kembali ke isi awal.';return}
    if(o==='add'){if(L.length>=9){log.innerHTML='<span class="err">Visual ini dibatasi 9 elemen.</span>';return}L.push(v);draw(k=>k===L.length-1?'new':'');log.innerHTML=`Java <code>list.add("${esc(v)}")</code> · Python <code>lst.append("${esc(v)}")</code>. Tidak ada yang bergeser.`;return}
    if(isNaN(i)){log.innerHTML='<span class="err">Isi indeks dulu.</span>';return}
    if(o==='ins'){
      if(i<0||i>L.length){log.innerHTML=`<span class="err">IndexOutOfBoundsException</span>: indeks harus 0 sampai ${L.length}.`;return}
      if(L.length>=9){log.innerHTML='<span class="err">Visual ini dibatasi 9 elemen.</span>';return}
      L.splice(i,0,v);draw(k=>k===i?'new':(k>i?'moved':''));
      log.innerHTML=`Java <code>list.add(${i}, "${esc(v)}")</code> · Python <code>lst.insert(${i}, "${esc(v)}")</code>. <b>${L.length-1-i}</b> elemen bergeser ke kanan (garis putus-putus).`;
    }
    if(o==='rem'){
      if(i<0||i>=L.length){log.innerHTML=`<span class="err">IndexOutOfBoundsException</span>: indeks harus 0 sampai ${L.length-1}.`;return}
      const r=L.splice(i,1)[0];draw(k=>k>=i?'moved':'');
      log.innerHTML=`Java <code>list.remove(${i})</code> · Python <code>lst.pop(${i})</code> mengembalikan "${esc(r)}". <b>${L.length-i}</b> elemen bergeser ke kiri.`;
    }
  });
},
collections(el){
  el.innerHTML=`<label for="co-t" class="eyebrow">Kalimat</label><input class="gl-search" id="co-t" value="satu dua tiga dua satu satu">
  <div class="grid2"><div><div class="eyebrow">List (urutan asli, duplikat boleh)</div><div id="co-l" style="margin-top:6px"></div>
  <div class="eyebrow" style="margin-top:14px">Set (unik, TreeSet terurut)</div><div id="co-s" style="margin-top:6px"></div></div>
  <div><div class="eyebrow">Map (kata → jumlah)</div><div id="co-m" style="margin-top:6px;display:flex;flex-direction:column;gap:5px"></div></div></div>`;
  const upd=()=>{
    const w=$('#co-t',el).value.toLowerCase().split(/\s+/).filter(Boolean).slice(0,40);
    $('#co-l',el).innerHTML=w.map(x=>`<span class="tok">${esc(x)}</span>`).join('')||'<span class="log">kosong</span>';
    const s=[...new Set(w)].sort();
    $('#co-s',el).innerHTML=s.map(x=>`<span class="tok cur">${esc(x)}</span>`).join('')+`<div class="log">${w.length} kata di list, ${s.length} di set</div>`;
    const m={};w.forEach(x=>m[x]=(m[x]||0)+1);const mx=Math.max(1,...Object.values(m));
    $('#co-m',el).innerHTML=Object.keys(m).sort().map(k=>`<div style="display:grid;grid-template-columns:90px 1fr 24px;gap:8px;align-items:center;font:.85rem var(--f-mono)"><span style="overflow:hidden;text-overflow:ellipsis">${esc(k)}</span><span style="height:14px;border-radius:4px;background:var(--py);width:${m[k]/mx*100}%"></span><b>${m[k]}</b></div>`).join('');
  };
  $('#co-t',el).addEventListener('input',upd);upd();
},
recursion(el){
  el.innerHTML=`<div class="row"><label for="rc-n">faktorial(n), n =</label><select class="inp" id="rc-n">${[2,3,4,5].map(v=>`<option ${v===4?'selected':''}>${v}</option>`).join('')}</select></div><div class="pl"></div>`;
  const build=n=>{
    const fr=[];const st=[];
    for(let k=n;k>=1;k--){
      st.push({n:k,s:k>1?'wait':'base'});
      fr.push({st:st.map(x=>({...x})),note:k>1?`Panggil <code>faktorial(${k})</code>. Karena ${k} &gt; 1, ia harus menunggu <code>${k} * faktorial(${k-1})</code>.`:`<code>faktorial(1)</code> adalah <b>base case</b>: langsung mengembalikan 1 tanpa memanggil lagi.`});
    }
    let val=1;
    st[st.length-1].s='ret';st[st.length-1].v=1;
    fr.push({st:st.map(x=>({...x})),note:'Mulai kembali: faktorial(1) mengembalikan 1.'});
    for(let k=2;k<=n;k++){
      st.pop();val*=k;const top=st[st.length-1];top.s='ret';top.v=val;
      fr.push({st:st.map(x=>({...x})),note:`Bingkai di atasnya dibuang. <code>faktorial(${k})</code> = ${k} * ${val/k} = <b>${val}</b>.`});
    }
    fr.push({st:[],res:val,note:`Semua bingkai selesai. Hasil akhir faktorial(${n}) = <b>${val}</b>.`});
    return fr;
  };
  const p=player($('.pl',el),build(4),(s,f)=>{
    s.innerHTML=`<div class="eyebrow" style="margin:6px 0 8px">Call stack (atas = paling baru)</div><div class="frames">${f.st.map((x,i)=>`<div class="frame ${x.s==='ret'?'ret':(i===f.st.length-1?'top':'')}"><b>faktorial(${x.n})</b><span>${x.s==='ret'?`return ${x.v}`:x.s==='base'?'base case':`menunggu ${x.n} * faktorial(${x.n-1})`}</span></div>`).join('')}</div>${f.res?`<div class="console" style="margin-top:10px">${f.res}</div>`:''}`;
  },{speed:1200});
  $('#rc-n',el).addEventListener('change',e=>p.set(build(+e.target.value)));
},
sorting(el){
  el.innerHTML=`<div class="eyebrow">Selection sort</div><div class="pl1"></div>
  <div style="border-top:1px solid var(--line);padding-top:14px" class="eyebrow">Binary search</div>
  <div class="row"><label for="bs-t">Cari angka</label><select class="inp" id="bs-t"></select></div><div class="pl2"></div>`;
  const A=[29,10,14,37,13,5,22];
  const fr=[];const a=[...A];let cmp=0;
  fr.push({a:[...a],i:-1,note:'Data awal. Tugas: urutkan dari kecil ke besar.'});
  for(let i=0;i<a.length-1;i++){
    let m=i;
    for(let j=i+1;j<a.length;j++){cmp++;
      const lebih=a[j]<a[m];if(lebih)m=j;
      fr.push({a:[...a],i,j,m,note:`Posisi ${i}: bandingkan ${a[j]} dengan minimum sementara. ${lebih?`${a[j]} lebih kecil, jadi minimum baru.`:'Minimum tetap.'} (perbandingan ke-${cmp})`});
    }
    [a[i],a[m]]=[a[m],a[i]];
    fr.push({a:[...a],i,m:i,sw:true,note:`Tukar minimum (${a[i]}) ke posisi ${i}. Bagian hijau sudah terurut.`});
  }
  fr.push({a:[...a],i:a.length,note:`Selesai dengan ${cmp} perbandingan. Untuk n = 7 itu n(n-1)/2 = 21, pertumbuhan O(n²).`});
  const mx=Math.max(...A);
  player($('.pl1',el),fr,(s,f)=>{
    s.innerHTML=`<div class="bars">${f.a.map((v,k)=>{let c='';if(k<f.i||(f.sw&&k===f.i)||f.i>=f.a.length)c='sorted';if(k===f.j)c='cmp';if(k===f.m&&!f.sw&&f.i<f.a.length)c='min';return `<div class="barv ${c}" style="height:${18+v/mx*82}%">${v}</div>`}).join('')}</div>
    <div class="row log"><span>■ <span style="color:var(--java)">minimum sementara</span></span><span>■ <span style="color:var(--hl-ink);background:var(--hl);padding:0 4px;border-radius:3px">dibandingkan</span></span><span style="color:var(--ok)">■ terurut</span></div>`;
  },{speed:700});
  const S=[2,5,8,12,16,23,38,45,56,72,91];
  $('#bs-t',el).innerHTML=[...S,50].map(v=>`<option ${v===23?'selected':''}>${v}</option>`).join('');
  const build=t=>{
    const fr=[];let L=0,R=S.length-1,step=0;
    fr.push({L,R,M:-1,note:`Cari ${t}. Rentang awal indeks 0 sampai ${R}.`});
    while(L<=R){
      const M=Math.floor((L+R)/2);step++;
      if(S[M]===t){fr.push({L,R,M,found:true,note:`Langkah ${step}: tengah = ${M}, a[${M}] = ${S[M]}. <b>Ketemu!</b> Hanya ${step} perbandingan dari ${S.length} data.`});return fr}
      if(S[M]<t){fr.push({L,R,M,note:`Langkah ${step}: tengah = ${M}, a[${M}] = ${S[M]} &lt; ${t}. Buang separuh kiri: kiri = ${M+1}.`});L=M+1}
      else{fr.push({L,R,M,note:`Langkah ${step}: tengah = ${M}, a[${M}] = ${S[M]} &gt; ${t}. Buang separuh kanan: kanan = ${M-1}.`});R=M-1}
    }
    fr.push({L,R,M:-1,note:`kiri (${L}) &gt; kanan (${R}). ${t} tidak ada, kembalikan <b>-1</b> setelah ${step} langkah.`});
    return fr;
  };
  const p2=player($('.pl2',el),build(23),(s,f)=>{
    s.innerHTML=cellsHTML(S,k=>k===f.M?(f.found?'new':'hl'):(k<f.L||k>f.R?'dim':''))+`<div class="vars"><span class="var">kiri = <b>${f.L}</b></span><span class="var">kanan = <b>${f.R}</b></span><span class="var">tengah = <b>${f.M<0?'-':f.M}</b></span></div>`;
  });
  $('#bs-t',el).addEventListener('change',e=>p2.set(build(+e.target.value)));
},
stackqueue(el){
  let S=[],Q=[],n=1;
  el.innerHTML=`<div class="row"><label for="sq-v">Nilai berikutnya</label><input class="inp" id="sq-v" value="1"></div>
  <div class="stackq"><div><div class="eyebrow" style="margin-bottom:6px">Stack (LIFO)</div><div class="row" style="margin-bottom:8px"><button class="btn j" id="s-push">push</button><button class="btn j" id="s-pop">pop</button></div><div class="stk" id="s-v"></div></div>
  <div style="min-width:0"><div class="eyebrow" style="margin-bottom:6px">Queue (FIFO)</div><div class="row" style="margin-bottom:8px"><button class="btn p" id="q-add">add / append</button><button class="btn p" id="q-rem">remove / popleft</button></div>
  <div class="log" style="display:flex;justify-content:space-between"><span>← depan (keluar)</span><span>belakang (masuk) ←</span></div><div class="que" id="q-v"></div></div></div><p class="log" id="sq-log">Masukkan 1, 2, 3 ke keduanya, lalu keluarkan satu dari masing-masing.</p>`;
  const draw=(sh,qh)=>{
    $('#s-v',el).innerHTML=S.map((v,i)=>`<div class="cell ${i===sh?'new':''}">${esc(v)}</div>`).reverse().join('')||'<div class="log" style="text-align:center">kosong</div>';
    $('#q-v',el).innerHTML=Q.map((v,i)=>`<div class="cell ${i===qh?'new':''}">${esc(v)}</div>`).join('')||'<span class="log">kosong</span>';
  };
  const val=()=>{const v=($('#sq-v',el).value||String(n)).slice(0,4);n++;$('#sq-v',el).value=n;return v};
  const log=h=>$('#sq-log',el).innerHTML=h;
  $('#s-push',el).onclick=()=>{if(S.length>=7)return log('Stack visual ini dibatasi 7.');const v=val();S.push(v);draw(S.length-1);log(`push(${esc(v)}) menaruh di <b>atas</b>.`)};
  $('#s-pop',el).onclick=()=>{if(!S.length)return log('<span class="err">EmptyStackException</span>: stack kosong.');const v=S.pop();draw();log(`pop() mengambil <b>${esc(v)}</b>, yang terakhir masuk.`)};
  $('#q-add',el).onclick=()=>{if(Q.length>=8)return log('Queue visual ini dibatasi 8.');const v=val();Q.push(v);draw(-1,Q.length-1);log(`add(${esc(v)}) masuk di <b>belakang</b> antrean.`)};
  $('#q-rem',el).onclick=()=>{if(!Q.length)return log('<span class="err">NoSuchElementException</span>: antrean kosong.');const v=Q.shift();draw();log(`remove() mengambil <b>${esc(v)}</b>, yang pertama masuk.`)};
  draw();
},
arrayintlist(el){
  let data=[0,0,0,0],size=0;
  el.innerHTML=`<div class="row"><label for="ai-v">Nilai</label><input class="inp" type="number" id="ai-v" value="7"><button class="btn primary" id="ai-add">add(nilai)</button><label for="ai-i">get(</label><input class="inp" type="number" id="ai-i" value="0" style="width:4.5em"><span>)</span><button class="btn" id="ai-get">get</button><button class="btn" id="ai-r">Ulang</button></div>
  <div style="overflow-x:auto" id="ai-c"></div><div class="vars"><span class="var" id="ai-sz"></span><span class="var" id="ai-cp"></span></div><p class="log" id="ai-log">Slot bertitik masih kosong. Tambahkan elemen sampai penuh.</p>`;
  const draw=(f=()=>'')=>{$('#ai-c',el).innerHTML=cellsHTML(data.map((v,i)=>i<size?v:'·'),(i)=>(i>=size?'empty ':'')+f(i));$('#ai-sz',el).innerHTML=`size = <b>${size}</b>`;$('#ai-cp',el).innerHTML=`kapasitas = <b>${data.length}</b>`};
  const log=h=>$('#ai-log',el).innerHTML=h;
  $('#ai-add',el).onclick=()=>{
    const v=parseInt($('#ai-v',el).value,10);if(isNaN(v))return;
    if(data.length>=16&&size===data.length)return log('Visual ini berhenti di kapasitas 16. Klik Ulang.');
    let msg='';
    if(size===data.length){const old=data.length;data=data.concat(new Array(old).fill(0));msg=`<b>Penuh!</b> Buat array baru berkapasitas ${data.length}, salin ${old} elemen lama. `}
    data[size]=v;size++;draw(i=>i===size-1?'new':'');
    log(msg+`elementData[${size-1}] = ${v}, lalu size++.`);
    $('#ai-v',el).value=rnd(1,99);
  };
  $('#ai-get',el).onclick=()=>{
    const i=parseInt($('#ai-i',el).value,10);if(isNaN(i))return;
    if(i<0||i>=size){draw(k=>k===i?'bad':'');return log(`<span class="err">IndexOutOfBoundsException: indeks ${i}</span>. Precondition 0 ≤ i &lt; size (${size}) dilanggar, walaupun slotnya mungkin ada di array.`)}
    draw(k=>k===i?'hl':'');log(`get(${i}) = <b>${data[i]}</b>`);
  };
  $('#ai-r',el).onclick=()=>{data=[0,0,0,0];size=0;draw();log('Kembali kosong dengan kapasitas 4.')};
  draw();
},
linkedlist(el){
  let L=[12,7,30];
  el.innerHTML=`<div class="row"><label for="ll-v">Nilai</label><input class="inp" type="number" id="ll-v" value="5"><button class="btn" data-o="first">addFirst</button><button class="btn" data-o="last">addLast</button><button class="btn" data-o="rem">removeFirst</button><button class="btn" data-o="reset">Ulang</button></div>
  <div style="overflow-x:auto"><div class="ll" id="ll-c"></div></div><p class="log" id="ll-log">front menunjuk node pertama. Setiap node menunjuk node berikutnya.</p>`;
  const draw=(f=()=>'')=>{
    $('#ll-c',el).innerHTML=`<span class="ptr front">front →</span>`+L.map((v,i)=>`<div class="lnode ${f(i)}"><span>${v}</span><span>next</span></div><span class="ptr">→</span>`).join('')+`<span class="ptr">null</span>`;
  };
  const log=h=>$('#ll-log',el).innerHTML=h;
  el.querySelector('.row').addEventListener('click',e=>{
    const b=e.target.closest('button');if(!b)return;const o=b.dataset.o;const v=parseInt($('#ll-v',el).value,10)||0;
    if(o==='reset'){L=[12,7,30];draw();return log('Kembali ke isi awal.')}
    if(o!=='rem'&&L.length>=8)return log('Visual ini dibatasi 8 node.');
    if(o==='first'){L.unshift(v);draw(i=>i===0?'new':'');log(`<code>front = new ListNode(${v}, front)</code>. Node baru menunjuk node lama, lalu front dipindah. <b>1 langkah</b>, tidak ada yang bergeser.`)}
    if(o==='last'){L.push(v);draw(i=>i===L.length-1?'new':(i<L.length-1?'hl':''));log(L.length===1?'List kosong, jadi node baru langsung menjadi front.':`<code>cur</code> berjalan dari front melewati <b>${L.length-1}</b> node (kuning) sampai <code>cur.next == null</code>, lalu <code>cur.next = new ListNode(${v})</code>.`)}
    if(o==='rem'){if(!L.length)return log('<span class="err">List kosong</span>: front == null, tidak ada yang bisa dihapus.');const r=L.shift();draw();log(`<code>front = front.next</code>. Node ${r} tidak lagi direferensikan dan nanti dibersihkan garbage collector.`)}
    $('#ll-v',el).value=rnd(1,99);
  });
  draw();
},
bst(el){
  let root=null;
  const ins=(v)=>{const path=[];if(!root){root={v,l:null,r:null};return path}let n=root;while(true){path.push(n.v);if(v===n.v)return null;if(v<n.v){if(!n.l){n.l={v,l:null,r:null};return path}n=n.l}else{if(!n.r){n.r={v,l:null,r:null};return path}n=n.r}}};
  const init=()=>{root=null;[50,30,70,20,40,60,80].forEach(ins)};init();
  el.innerHTML=`<div class="row"><label for="bt-v">Nilai</label><input class="inp" type="number" id="bt-v" value="45"><button class="btn primary" id="bt-add">Sisipkan</button><button class="btn" id="bt-r">Ulang</button></div>
  <div class="row"><span class="log">Traversal:</span><button class="btn" data-t="pre">Pre-order</button><button class="btn" data-t="in">In-order</button><button class="btn" data-t="post">Post-order</button></div>
  <div style="overflow-x:auto" id="bt-svg"></div><div class="console" id="bt-out"></div><p class="log" id="bt-log">Angka lebih kecil ke kiri, lebih besar ke kanan.</p>`;
  const draw=(hl=new Set(),nw=null)=>{
    const pos=[];let x=0;
    const walk=(n,d)=>{if(!n)return;walk(n.l,d+1);n.x=x++;n.d=d;pos.push(n);walk(n.r,d+1)};walk(root,0);
    const W=Math.max(320,x*46+20),H=(Math.max(0,...pos.map(p=>p.d))+1)*60+10;
    const cx=n=>n.x*46+33,cy=n=>n.d*60+30;
    let e='',c='';
    pos.forEach(n=>{[n.l,n.r].forEach(k=>{if(k)e+=`<line class="edge" x1="${cx(n)}" y1="${cy(n)}" x2="${cx(k)}" y2="${cy(k)}"/>`});
      c+=`<circle class="nd ${hl.has(n.v)?'hl':''} ${n.v===nw?'new':''}" cx="${cx(n)}" cy="${cy(n)}" r="18"/><text x="${cx(n)}" y="${cy(n)+4.5}" text-anchor="middle">${n.v}</text>`});
    $('#bt-svg',el).innerHTML=`<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="Binary search tree">${e}${c}</svg>`;
  };
  draw();
  const log=h=>$('#bt-log',el).innerHTML=h;
  $('#bt-add',el).onclick=()=>{
    clearTimers();const v=parseInt($('#bt-v',el).value,10);if(isNaN(v))return;
    let cnt=0;(function c(n){if(n){cnt++;c(n.l);c(n.r)}})(root);
    if(cnt>=15)return log('Visual ini dibatasi 15 node. Klik Ulang.');
    const p=ins(v);
    if(p===null)return log(`${v} sudah ada di pohon. BST ini tidak menyimpan duplikat.`);
    draw(new Set(p),v);$('#bt-out',el).textContent='';
    log(p.length?`Jalur pembanding: ${p.join(' → ')}. ${v} ditempatkan sebagai anak ${v<p[p.length-1]?'kiri':'kanan'} dari ${p[p.length-1]} (${p.length} perbandingan).`:`${v} menjadi akar.`);
    $('#bt-v',el).value=rnd(1,99);
  };
  $('#bt-r',el).onclick=()=>{clearTimers();init();draw();$('#bt-out',el).textContent='';log('Kembali ke pohon awal.')};
  el.querySelectorAll('[data-t]').forEach(b=>b.onclick=()=>{
    clearTimers();const seq=[],t=b.dataset.t;
    (function go(n){if(!n)return;if(t==='pre')seq.push(n.v);go(n.l);if(t==='in')seq.push(n.v);go(n.r);if(t==='post')seq.push(n.v)})(root);
    const names={pre:'akar, kiri, kanan',in:'kiri, akar, kanan',post:'kiri, kanan, akar'};
    log(`${b.textContent}: ${names[t]}.${t==='in'?' Perhatikan hasilnya terurut.':''}`);
    let i=0;const done=new Set();$('#bt-out',el).textContent='';
    const tm=setInterval(()=>{done.add(seq[i]);draw(done);$('#bt-out',el).textContent=seq.slice(0,i+1).join(' ');i++;if(i>=seq.length)clearInterval(tm)},500);TIMERS.push(tm);
  });
},
hashheap(el){
  const B=7;let T,H;
  const reset=()=>{T=Array.from({length:B},()=>[]);[15,8,23].forEach(v=>T[v%B].push(v));H=[];[42,7,19,3].forEach(push)};
  function push(v){H.push(v);let i=H.length-1;while(i>0){const p=Math.floor((i-1)/2);if(H[p]<=H[i])break;[H[p],H[i]]=[H[i],H[p]];i=p}return i}
  function pop(){const top=H[0];const last=H.pop();if(H.length){H[0]=last;let i=0;while(true){const l=2*i+1,r=l+1;let m=i;if(l<H.length&&H[l]<H[m])m=l;if(r<H.length&&H[r]<H[m])m=r;if(m===i)break;[H[m],H[i]]=[H[i],H[m]];i=m}}return top}
  reset();
  el.innerHTML=`<div class="grid2"><div style="min-width:0"><div class="eyebrow">Hash table (7 ember, chaining)</div>
  <div class="row" style="margin:8px 0"><input class="inp" type="number" id="hh-h" value="22" aria-label="Nilai untuk hash table"><button class="btn primary" id="hh-ins">put</button></div>
  <div class="buckets" id="hh-b"></div><p class="log" id="hh-hl">indeks = nilai % 7</p></div>
  <div style="min-width:0"><div class="eyebrow">Min-heap (priority queue)</div>
  <div class="row" style="margin:8px 0"><input class="inp" type="number" id="hh-p" value="5" aria-label="Nilai untuk heap"><button class="btn primary" id="hh-add">add</button><button class="btn" id="hh-rm">remove min</button><button class="btn" id="hh-r">Ulang</button></div>
  <div style="overflow-x:auto" id="hh-tree"></div><div style="overflow-x:auto" id="hh-arr"></div><p class="log" id="hh-pl">Induk selalu ≤ anaknya, jadi minimum ada di akar.</p></div></div>`;
  const drawT=(hit=-1,nv=null)=>{$('#hh-b',el).innerHTML=T.map((ch,i)=>`<div class="bucket ${i===hit?'hit':''}"><span class="bi">[${i}]</span><div class="chain">${ch.map(v=>`<span class="tok ${v===nv?(ch.length>1?'col':'cur'):''}">${v}</span>`).join('<span class="arrow">→</span>')}</div></div>`).join('')};
  const drawH=(hi=-1)=>{
    const W=300,lv=Math.max(1,Math.ceil(Math.log2(H.length+1))),Hh=lv*52+10;
    const P=i=>{const d=Math.floor(Math.log2(i+1)),k=i-(2**d-1);return [((k+.5)/2**d)*W,d*52+26]};
    let e='',c='';
    H.forEach((v,i)=>{if(i){const[a,b]=P(Math.floor((i-1)/2)),[x,y]=P(i);e+=`<line class="edge" x1="${a}" y1="${b}" x2="${x}" y2="${y}"/>`}
      const[x,y]=P(i);c+=`<circle class="nd ${i===hi?'hl':''} ${i===0?'new':''}" cx="${x}" cy="${y}" r="16"/><text x="${x}" y="${y+4.5}" text-anchor="middle">${v}</text>`});
    $('#hh-tree',el).innerHTML=H.length?`<svg width="${W}" height="${Hh}" viewBox="0 0 ${W} ${Hh}" role="img" aria-label="Min-heap">${e}${c}</svg>`:'<p class="log">Heap kosong.</p>';
    $('#hh-arr',el).innerHTML=`<div class="log" style="margin-top:4px">Disimpan sebagai array:</div>`+cellsHTML(H,i=>i===hi?'hl':'');
  };
  drawT();drawH();
  $('#hh-ins',el).onclick=()=>{
    const v=parseInt($('#hh-h',el).value,10);if(isNaN(v)||v<0)return;
    const i=v%B;
    if(T[i].includes(v)){drawT(i,v);$('#hh-hl',el).innerHTML=`${v} sudah ada di ember [${i}]. Kunci tidak disimpan dua kali.`;return}
    if(T.flat().length>=18)return;
    T[i].push(v);drawT(i,v);
    $('#hh-hl',el).innerHTML=`${v} % 7 = <b>${i}</b>. ${T[i].length>1?`<span class="err">Collision</span> dengan ${T[i].slice(0,-1).join(', ')}, jadi ditambahkan ke rantai.`:'Ember kosong, langsung masuk.'}`;
    $('#hh-h',el).value=rnd(0,60);
  };
  $('#hh-add',el).onclick=()=>{const v=parseInt($('#hh-p',el).value,10);if(isNaN(v))return;if(H.length>=15)return;const at=push(v);drawH(at);$('#hh-pl',el).innerHTML=`${v} ditaruh di ujung array, lalu <b>naik</b> (bubble up) selama lebih kecil dari induknya. Berhenti di indeks ${at}.`;$('#hh-p',el).value=rnd(1,60)};
  $('#hh-rm',el).onclick=()=>{if(!H.length){$('#hh-pl',el).innerHTML='<span class="err">Heap kosong.</span>';return}const v=pop();drawH();$('#hh-pl',el).innerHTML=`Keluar: <b>${v}</b> (minimum). Elemen terakhir dipindah ke akar lalu <b>turun</b> sampai aturan heap terpenuhi.`};
  $('#hh-r',el).onclick=()=>{reset();drawT();drawH();$('#hh-hl',el).textContent='indeks = nilai % 7';$('#hh-pl',el).textContent='Kembali ke isi awal.'};
},
functional(el){
  const D=[1,2,3,4,5,6,7,8,9,10];
  const FL={semua:[null,null,null],genap:[x=>x%2===0,'n -> n % 2 == 0','n % 2 == 0'],ganjil:[x=>x%2===1,'n -> n % 2 == 1','n % 2 == 1'],lebih5:[x=>x>5,'n -> n > 5','n > 5']};
  const MP={tetap:[x=>x,null,null],kali2:[x=>x*2,'n -> n * 2','n * 2'],kuadrat:[x=>x*x,'n -> n * n','n * n'],plus10:[x=>x+10,'n -> n + 10','n + 10']};
  const RD={list:[null],jumlah:[a=>a.reduce((s,x)=>s+x,0),'.reduce(0, Integer::sum)','sum'],maks:[a=>a.length?Math.max(...a):'(kosong)','.max(Integer::compare).get()','max'],banyak:[a=>a.length,'.count()','len']};
  el.innerHTML=`<div class="row"><label for="fn-f">filter</label><select class="inp" id="fn-f"><option value="semua">semua</option><option value="genap" selected>genap</option><option value="ganjil">ganjil</option><option value="lebih5">&gt; 5</option></select>
  <label for="fn-m">map</label><select class="inp" id="fn-m"><option value="tetap">tetap</option><option value="kali2">× 2</option><option value="kuadrat" selected>kuadrat</option><option value="plus10">+ 10</option></select>
  <label for="fn-r">reduce</label><select class="inp" id="fn-r"><option value="list">(kumpulkan list)</option><option value="jumlah" selected>jumlah</option><option value="maks">maksimum</option><option value="banyak">banyaknya</option></select></div>
  <div class="pipe" id="fn-p"></div><div class="grid2"><div class="mini" id="fn-j"></div>${JO()?'':'<div class="mini" id="fn-py"></div>'}</div>`;
  const upd=()=>{
    const f=FL[$('#fn-f',el).value],m=MP[$('#fn-m',el).value],r=RD[$('#fn-r',el).value];
    const a1=f[0]?D.filter(f[0]):D,a2=a1.map(m[0]),res=r[0]?r[0](a2):null;
    const chips=a=>a.length?a.map(x=>`<span class="tok">${x}</span>`).join(''):'<span class="log">kosong</span>';
    $('#fn-p',el).innerHTML=`<div class="pstage"><span class="lab">data</span><div>${chips(D)}</div></div>
     <div class="pstage"><span class="lab">filter</span><div>${chips(a1)}</div></div>
     <div class="pstage"><span class="lab">map</span><div>${chips(a2)}</div></div>
     <div class="pstage"><span class="lab">${r[0]?'reduce':'collect'}</span><div>${r[0]?`<span class="big">${res}</span>`:`[${a2.join(', ')}]`}</div></div>`;
    let j='angka.stream()';if(f[1])j+=`\n    .filter(${f[1]})`;if(m[1])j+=`\n    .map(${m[1]})`;j+=r[1]?`\n    ${r[1]}`:`\n    .collect(Collectors.toList())`;j+=';';
    const expr=m[2]?m[2]:'n',cond=f[2]?` if ${f[2]}`:'';
    const py=r[2]?(r[2]==='len'?`len([n for n in angka${cond}])`:`${r[2]}(${expr} for n in angka${cond})`):`[${expr} for n in angka${cond}]`;
    $('#fn-j',el).innerHTML=`<span class="c">// Java</span>\n`+hl(j,'java');
    if(!JO())$('#fn-py',el).innerHTML=`<span class="c"># Python</span>\n`+hl(py,'python');
  };
  el.querySelectorAll('select').forEach(s=>s.addEventListener('change',upd));upd();
}
};


/* ===================== MESIN SQL =====================
   Simulator SQL kecil untuk belajar: dialek mirip SQLite/PostgreSQL, data di memori.
   Selain hasil, mesin ini merekam jejak tiap tahap (FROM, WHERE, GROUP BY, ...) untuk visualisasi. */
const SQLE=(()=>{
class SqlError extends Error{constructor(msg,hint){super(msg);this.hint=hint||''}}
const lc=s=>String(s).toLowerCase();

/* ---------- tokenizer ---------- */
function tokenize(src){
  const T=[];let i=0;const n=src.length;
  while(i<n){
    const c=src[i];
    if(/\s/.test(c)){i++;continue}
    if(c==='-'&&src[i+1]==='-'){while(i<n&&src[i]!=='\n')i++;continue}
    if(c==='/'&&src[i+1]==='*'){const j=src.indexOf('*/',i+2);i=j<0?n:j+2;continue}
    const p=i;
    if(/[0-9]/.test(c)||(c==='.'&&/[0-9]/.test(src[i+1]||''))){
      let j=i;while(j<n&&/[0-9]/.test(src[j]))j++;
      if(src[j]==='.'){j++;while(j<n&&/[0-9]/.test(src[j]))j++}
      if(/[eE]/.test(src[j]||'')&&/[-+0-9]/.test(src[j+1]||'')){j+=2;while(j<n&&/[0-9]/.test(src[j]))j++}
      T.push({t:'num',v:Number(src.slice(i,j)),p});i=j;continue}
    if(c==="'"){let j=i+1,s='';
      for(;;){if(j>=n)throw new SqlError("Teks belum ditutup: tanda kutip ' tidak berpasangan.","Setiap teks diapit dua kutip tunggal, misalnya 'Jakarta'.");
        if(src[j]==="'"){if(src[j+1]==="'"){s+="'";j+=2;continue}break}s+=src[j++]}
      T.push({t:'str',v:s,p});i=j+1;continue}
    if(c==='"'||c==='`'||c==='['){const cl=c==='['?']':c,j=src.indexOf(cl,i+1);
      if(j<0)throw new SqlError(`Nama berkutip ${c} belum ditutup.`);T.push({t:'id',v:src.slice(i+1,j),q:1,p});i=j+1;continue}
    if(/[A-Za-z_]/.test(c)){let j=i;while(j<n&&/[A-Za-z0-9_]/.test(src[j]))j++;const w=src.slice(i,j);T.push({t:'id',v:w,u:w.toUpperCase(),p});i=j;continue}
    const two=src.substr(i,2);
    if(['<=','>=','<>','!=','==','||'].includes(two)){T.push({t:'op',v:two,p});i+=2;continue}
    if('(),.;=<>+-*/%'.includes(c)){T.push({t:'op',v:c,p});i++;continue}
    throw new SqlError(`Karakter tidak dikenal: ${c}`,'Periksa tanda baca. Teks memakai kutip tunggal, bukan kutip miring.');
  }
  T.push({t:'eof',v:'',p:n});return T;
}

/* kata yang tidak boleh dianggap alias */
const RES=new Set('SELECT FROM WHERE GROUP BY HAVING ORDER LIMIT OFFSET JOIN INNER LEFT RIGHT FULL OUTER CROSS NATURAL ON USING AS AND OR NOT UNION ALL INTERSECT EXCEPT INTO VALUES SET WINDOW CASE WHEN THEN ELSE END ASC DESC IS NULL IN LIKE BETWEEN DISTINCT EXISTS'.split(' '));
const KWLIST='SELECT FROM WHERE GROUP BY HAVING ORDER LIMIT OFFSET JOIN INNER LEFT RIGHT FULL OUTER CROSS ON AS AND OR NOT UNION INSERT INTO VALUES UPDATE SET DELETE CREATE TABLE ALTER DROP TRUNCATE VIEW INDEX DISTINCT BETWEEN LIKE NULL PRIMARY KEY FOREIGN REFERENCES UNIQUE CHECK DEFAULT BEGIN COMMIT ROLLBACK SAVEPOINT CASE WHEN THEN ELSE END WITH RECURSIVE OVER PARTITION'.split(' ');
function lev(a,b){const d=[...Array(b.length+1).keys()];for(let i=1;i<=a.length;i++){let p=d[0];d[0]=i;for(let j=1;j<=b.length;j++){const t=d[j];d[j]=Math.min(d[j]+1,d[j-1]+1,p+(a[i-1]===b[j-1]?0:1));p=t}}return d[b.length]}
function guessKw(w){if(!w)return null;const u=w.toUpperCase();if(KWLIST.includes(u))return null;let best=null,bd=3;
  for(const k of KWLIST){const d=lev(u,k);if(d<bd&&k.length>2){bd=d;best=k}}return bd<=(u.length>=4?2:1)?best:null}

/* ---------- parser ---------- */
class Parser{
  constructor(src){this.src=src;this.T=tokenize(src);this.i=0}
  get pk(){return this.T[this.i]}
  la(k=1){return this.T[this.i+k]}
  next(){return this.T[this.i++]}
  isKw(...w){const t=this.pk;return t.t==='id'&&!t.q&&w.includes(t.u)}
  kw(...w){if(this.isKw(...w))return this.next().u;return null}
  needKw(w,ctx){if(!this.kw(w))this.fail(`Diharapkan ${w}${ctx?' '+ctx:''}`);}
  isOp(o){const t=this.pk;return t.t==='op'&&t.v===o}
  op(o){if(this.isOp(o)){this.i++;return true}return false}
  needOp(o,ctx){if(!this.op(o))this.fail(`Diharapkan tanda ${o}${ctx?' '+ctx:''}`)}
  fail(msg){const t=this.pk;const near=t.t==='eof'?'akhir perintah':`"${t.t==='str'?"'"+t.v+"'":t.v}"`;
    const g=t.t==='id'?guessKw(t.v):null;
    throw new SqlError(`${msg}, tetapi yang ditemukan ${near}.`,g?`Mungkin maksudmu ${g}?`:'')}
  ident(what='nama'){const t=this.pk;if(t.t!=='id')this.fail(`Diharapkan ${what}`);this.i++;return t.v}
  identList(){const a=[this.ident()];while(this.op(','))a.push(this.ident());return a}
  all(){const out=[];
    while(this.pk.t!=='eof'){if(this.op(';'))continue;const st=this.statement();out.push(st);
      if(!this.op(';')&&this.pk.t!=='eof')this.fail('Perintah seharusnya selesai di sini (pisahkan dengan titik koma ;)')}
    return out}
  statement(){
    const start=this.pk.p,st=this.stmt0();st.sql=this.src.slice(start,this.pk.p).trim();return st}
  stmt0(){
    if(this.kw('EXPLAIN')){if(this.kw('QUERY'))this.needKw('PLAN');return {type:'explain',q:this.select()}}
    if(this.isKw('SELECT','WITH')||this.isOp('('))return this.select();
    const t=this.pk;
    switch(t.t==='id'?t.u:''){
      case 'INSERT':return this.insert();
      case 'UPDATE':return this.update();
      case 'DELETE':return this.del();
      case 'CREATE':return this.create();
      case 'ALTER':return this.alter();
      case 'DROP':return this.drop();
      case 'TRUNCATE':this.next();this.kw('TABLE');return {type:'truncate',name:this.ident('nama tabel')};
      case 'BEGIN':case 'START':this.next();this.kw('TRANSACTION','WORK');return {type:'begin'};
      case 'COMMIT':case 'END':this.next();this.kw('TRANSACTION','WORK');return {type:'commit'};
      case 'ROLLBACK':{this.next();this.kw('TRANSACTION','WORK');if(this.kw('TO')){this.kw('SAVEPOINT');return {type:'rollback',to:this.ident()}}return {type:'rollback'}}
      case 'SAVEPOINT':this.next();return {type:'savepoint',name:this.ident()};
      case 'RELEASE':this.next();this.kw('SAVEPOINT');return {type:'release',name:this.ident()};
      case 'GRANT':case 'REVOKE':return this.grant();
    }
    const g=t.t==='id'?guessKw(t.v):null;
    throw new SqlError(`Perintah tidak dikenali: "${t.v}".`,g?`Mungkin maksudmu ${g}?`:'Perintah SQL biasanya dimulai dengan SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, atau DROP.');
  }
  /* SELECT */
  select(){
    let ctes=null;
    if(this.kw('WITH')){const rec=!!this.kw('RECURSIVE');ctes=[];
      do{const name=this.ident('nama CTE');let cols=null;if(this.op('(')){cols=this.identList();this.needOp(')')}
        this.needKw('AS','setelah nama CTE');this.needOp('(');const q=this.select();this.needOp(')');ctes.push({name,cols,q,rec})}while(this.op(','))}
    let body=this.core();
    while(this.isKw('UNION','INTERSECT','EXCEPT')){let o=this.next().u;if(o==='UNION'&&this.kw('ALL'))o='UNION ALL';else this.kw('DISTINCT');
      body={type:'compound',op:o,l:body,r:this.core()}}
    let order=null,limit=null,offset=null;
    if(this.kw('ORDER')){this.needKw('BY','setelah ORDER');order=this.orderList()}
    if(this.kw('LIMIT')){limit=this.expr();if(this.kw('OFFSET'))offset=this.expr();else if(this.op(',')){offset=limit;limit=this.expr()}}
    else if(this.kw('OFFSET')){offset=this.expr();this.kw('ROWS','ROW');if(this.kw('FETCH')){this.kw('FIRST','NEXT');limit=this.expr();this.kw('ROWS','ROW');this.needKw('ONLY')}}
    else if(this.kw('FETCH')){this.kw('FIRST','NEXT');limit=this.expr();this.kw('ROWS','ROW');this.needKw('ONLY')}
    return {type:'select',ctes,body,order,limit,offset};
  }
  orderList(){const a=[];do{const e=this.expr();let desc=false;if(this.kw('DESC'))desc=true;else this.kw('ASC');
      let nulls=null;if(this.kw('NULLS')){nulls=this.kw('FIRST','LAST')}a.push({e,desc,nulls})}while(this.op(','));return a}
  core(){
    if(this.op('(')){const q=this.select();this.needOp(')');return {type:'paren',q}}
    if(this.kw('VALUES')){const rows=[];do{this.needOp('(');rows.push(this.exprList());this.needOp(')')}while(this.op(','));return {type:'values',rows}}
    if(!this.kw('SELECT'))this.fail('Diharapkan SELECT');
    const distinct=!!this.kw('DISTINCT');this.kw('ALL');
    if(this.kw('TOP')){this._top=this.primary()}
    const cols=[];
    do{
      if(this.op('*')){cols.push({star:true});continue}
      if(this.pk.t==='id'&&this.la().t==='op'&&this.la().v==='.'&&this.la(2).t==='op'&&this.la(2).v==='*'){const tb=this.next().v;this.i+=2;cols.push({star:true,table:tb});continue}
      const s=this.pk.p,e=this.expr(),txt=this.src.slice(s,this.pk.p).trim();let alias=null;
      if(this.kw('AS'))alias=this.pk.t==='str'?this.next().v:this.ident('alias');
      else if(this.pk.t==='id'&&(this.pk.q||!RES.has(this.pk.u))&&!this.isKw('FROM'))alias=this.next().v;
      cols.push({e,alias,txt});
    }while(this.op(','));
    if(this.isKw('FORM','FRM','FRON','FOM'))this.fail('Diharapkan FROM atau koma');
    let from=null,where=null,group=null,having=null;
    if(this.kw('FROM'))from=this.from();
    if(this.kw('WHERE'))where=this.expr();
    if(this.kw('GROUP')){this.needKw('BY','setelah GROUP');group=this.exprList()}
    if(this.kw('HAVING'))having=this.expr();
    const top=this._top;this._top=null;
    return {type:'core',distinct,cols,from,where,group,having,top};
  }
  fromItem(){
    if(this.op('(')){
      if(this.isKw('SELECT','WITH','VALUES')){const q=this.select();this.needOp(')');return {kind:'sub',q,alias:this.alias()}}
      const f=this.from();this.needOp(')');return f}
    const name=this.ident('nama tabel');return {kind:'table',name,alias:this.alias()}
  }
  alias(){if(this.kw('AS'))return this.ident('alias');
    if(this.pk.t==='id'&&(this.pk.q||!RES.has(this.pk.u))&&!this.isKw('WHERE','GROUP','ORDER','LIMIT','HAVING','ON','USING','JOIN','INNER','LEFT','RIGHT','FULL','CROSS','UNION','EXCEPT','INTERSECT','SET','OFFSET','FETCH','NATURAL'))return this.next().v;
    return null}
  from(){
    let L=this.fromItem();
    for(;;){
      if(this.op(',')){L={kind:'join',jt:'CROSS',comma:true,l:L,r:this.fromItem()};continue}
      let jt=null;
      if(this.kw('JOIN'))jt='INNER';
      else if(this.kw('INNER')){this.needKw('JOIN','setelah INNER');jt='INNER'}
      else if(this.isKw('LEFT','RIGHT','FULL')){jt=this.next().u;this.kw('OUTER');this.needKw('JOIN',`setelah ${jt}`)}
      else if(this.kw('CROSS')){this.needKw('JOIN','setelah CROSS');jt='CROSS'}
      else break;
      const R=this.fromItem();let on=null,using=null;
      if(this.kw('ON'))on=this.expr();else if(this.kw('USING')){this.needOp('(');using=this.identList();this.needOp(')')}
      else if(jt!=='CROSS')this.fail(`${jt} JOIN perlu kondisi ON, misalnya ON a.id = b.a_id`);
      L={kind:'join',jt,l:L,r:R,on,using};
    }
    return L;
  }
  /* ekspresi */
  exprList(){const a=[this.expr()];while(this.op(','))a.push(this.expr());return a}
  expr(){return this.or()}
  or(){let l=this.and();while(this.kw('OR'))l={op:'OR',l,r:this.and()};return l}
  and(){let l=this.not();while(this.kw('AND'))l={op:'AND',l,r:this.not()};return l}
  not(){if(this.kw('NOT'))return {op:'NOT',e:this.not()};return this.cmp()}
  cmp(){
    let l=this.cat();
    for(;;){
      const t=this.pk;
      if(t.t==='op'&&['=','==','!=','<>','<','<=','>','>='].includes(t.v)){this.i++;
        const o=t.v==='=='?'=':t.v==='<>'?'!=':t.v;
        if(this.isKw('ANY','ALL','SOME')){const q=this.next().u;this.needOp('(');const s=this.select();this.needOp(')');l={op:'quant',o,q:q==='SOME'?'ANY':q,e:l,s};continue}
        l={op:'cmp',o,l,r:this.cat()};continue}
      if(this.kw('IS')){const not=!!this.kw('NOT');if(this.kw('NULL')){l={op:'isnull',e:l,not};continue}
        if(this.kw('DISTINCT')){this.needKw('FROM');l={op:'is',l,r:this.cat(),not:!not};continue}
        l={op:'is',l,r:this.cat(),not};continue}
      if(this.kw('ISNULL')){l={op:'isnull',e:l,not:false};continue}
      if(this.kw('NOTNULL')){l={op:'isnull',e:l,not:true};continue}
      const save=this.i,not=!!this.kw('NOT');
      if(this.kw('IN')){this.needOp('(','setelah IN');
        if(this.isKw('SELECT','WITH')){const q=this.select();this.needOp(')');l={op:'in',e:l,q,not}}
        else{const list=this.isOp(')')?[]:this.exprList();this.needOp(')');l={op:'in',e:l,list,not}}continue}
      if(this.kw('LIKE','ILIKE')){const p=this.cat();let esc=null;if(this.kw('ESCAPE'))esc=this.cat();l={op:'like',e:l,p,not,esc};continue}
      if(this.kw('BETWEEN')){const a=this.cat();this.needKw('AND','di BETWEEN ... AND ...');l={op:'between',e:l,a,b:this.cat(),not};continue}
      if(not)this.i=save;
      break;
    }
    return l;
  }
  cat(){let l=this.add();while(this.op('||'))l={op:'bin',o:'||',l,r:this.add()};return l}
  add(){let l=this.mul();for(;;){if(this.op('+'))l={op:'bin',o:'+',l,r:this.mul()};else if(this.op('-'))l={op:'bin',o:'-',l,r:this.mul()};else return l}}
  mul(){let l=this.un();for(;;){const t=this.pk;if(t.t==='op'&&'*/%'.includes(t.v)&&t.v.length===1){this.i++;l={op:'bin',o:t.v,l,r:this.un()}}else return l}}
  un(){if(this.op('-'))return {op:'neg',e:this.un()};if(this.op('+'))return this.un();return this.primary()}
  primary(){
    const t=this.pk;
    if(t.t==='num'){this.i++;return {op:'lit',v:t.v}}
    if(t.t==='str'){this.i++;return {op:'lit',v:t.v}}
    if(this.op('(')){
      if(this.isKw('SELECT','WITH')){const q=this.select();this.needOp(')');return {op:'sub',q}}
      const e=this.expr();
      if(this.op(',')){const list=[e,...this.exprList()];this.needOp(')');return {op:'row',list}}
      this.needOp(')');return e}
    if(t.t!=='id'){if(t.t==='eof')this.fail('Perintah berhenti di tengah jalan: masih kurang ekspresi');this.fail('Diharapkan nilai, nama kolom, atau fungsi')}
    if(!t.q){
      switch(t.u){
        case 'NULL':this.i++;return {op:'lit',v:null};
        case 'TRUE':this.i++;return {op:'lit',v:1};
        case 'FALSE':this.i++;return {op:'lit',v:0};
        case 'CURRENT_DATE':case 'CURRENT_TIMESTAMP':case 'CURRENT_TIME':this.i++;return {op:'fn',name:t.u,args:[]};
        case 'CASE':return this.caseExpr();
        case 'CAST':{this.i++;this.needOp('(');const e=this.expr();this.needKw('AS');const ty=this.typeName();this.needOp(')');return {op:'cast',e,ty}}
        case 'EXISTS':{this.i++;this.needOp('(');const q=this.select();this.needOp(')');return {op:'exists',q}}
        case 'EXTRACT':if(this.la().v==='('){this.i+=2;const part=this.ident();this.needKw('FROM');const e=this.expr();this.needOp(')');return {op:'fn',name:'DATEPART',args:[{op:'lit',v:lc(part)},e]}}break;
        case 'INTERVAL':break;
      }
    }
    this.i++;
    if(this.isOp('(')&&!t.q){
      this.i++;const name=t.u;let args=[],star=false,distinct=false;
      if(this.op('*')){star=true}
      else if(!this.isOp(')')){
        distinct=!!this.kw('DISTINCT');
        if(['DATEADD','DATEPART','DATEDIFF','DATE_PART','DATETRUNC','DATE_TRUNC'].includes(name)&&this.pk.t==='id'&&!this.pk.q&&this.la().v===','){args.push({op:'lit',v:lc(this.next().v)});this.needOp(',')}
        args.push(...this.exprList());
        if(name==='STRING_AGG'||name==='GROUP_CONCAT'){if(this.kw('ORDER')){this.needKw('BY');this.orderList()}}
      }
      this.needOp(')',`untuk menutup ${name}(`);
      const f={op:'fn',name,args,star,distinct};
      if(this.kw('FILTER')){this.needOp('(');this.needKw('WHERE');f.filter=this.expr();this.needOp(')')}
      if(this.kw('OVER'))f.over=this.overSpec();
      return f;
    }
    if(this.op('.')){
      if(this.pk.t!=='id')this.fail('Diharapkan nama kolom setelah titik');
      return {op:'col',table:t.v,name:this.next().v}}
    return {op:'col',name:t.v,q:t.q}
  }
  overSpec(){
    this.needOp('(','setelah OVER');const w={part:null,order:null,frame:null};
    if(this.kw('PARTITION')){this.needKw('BY');w.part=this.exprList()}
    if(this.kw('ORDER')){this.needKw('BY');w.order=this.orderList()}
    if(this.isKw('ROWS','RANGE')){const k=this.next().u;let depth=0;const s=this.i;while(!(depth===0&&this.isOp(')'))){if(this.pk.t==='eof')this.fail('Diharapkan )');if(this.isOp('('))depth++;if(this.isOp(')'))depth--;this.i++}
      const txt=this.T.slice(s,this.i).map(x=>String(x.v).toUpperCase()).join(' ');
      w.frame=k+' '+txt}
    this.needOp(')');return w}
  caseExpr(){this.i++;let base=null;if(!this.isKw('WHEN'))base=this.expr();const whens=[];
    while(this.kw('WHEN')){const c=this.expr();this.needKw('THEN','setelah WHEN');whens.push([c,this.expr()])}
    if(!whens.length)this.fail('CASE butuh minimal satu WHEN ... THEN ...');
    let els=null;if(this.kw('ELSE'))els=this.expr();this.needKw('END','untuk menutup CASE');return {op:'case',base,whens,els}}
  typeName(){let ty=this.ident('tipe data');while(this.pk.t==='id'&&['VARYING','PRECISION'].includes(this.pk.u))ty+=' '+this.next().v;
    if(this.op('(')){ty+='('+this.next().v;while(this.op(','))ty+=','+this.next().v;this.needOp(')');ty+=')'}return ty}
  /* DML */
  insert(){this.next();this.kw('OR')&&this.next();this.needKw('INTO','setelah INSERT');const name=this.ident('nama tabel');let cols=null;
    if(this.isOp('(')&&!(this.la().t==='id'&&['SELECT','WITH'].includes(this.la().u))){this.i++;cols=this.identList();this.needOp(')')}
    if(this.kw('DEFAULT')){this.needKw('VALUES');return {type:'insert',name,cols,rows:[[]]}}
    if(this.kw('VALUES')){const rows=[];do{this.needOp('(','sebelum daftar nilai');rows.push(this.exprList());this.needOp(')','setelah daftar nilai')}while(this.op(','));
      return {type:'insert',name,cols,rows}}
    if(this.isKw('SELECT','WITH')||this.isOp('('))return {type:'insert',name,cols,q:this.select()};
    this.fail('Diharapkan VALUES atau SELECT');}
  update(){this.next();const name=this.ident('nama tabel');const alias=this.alias();this.needKw('SET','setelah nama tabel');const sets=[];
    do{const c=this.ident('nama kolom');this.needOp('=','setelah nama kolom di SET');sets.push([c,this.expr()])}while(this.op(','));
    let where=null;if(this.kw('WHERE'))where=this.expr();return {type:'update',name,alias,sets,where}}
  del(){this.next();this.needKw('FROM','setelah DELETE');const name=this.ident('nama tabel');const alias=this.alias();let where=null;if(this.kw('WHERE'))where=this.expr();return {type:'delete',name,alias,where}}
  /* DDL */
  create(){this.next();
    let replace=false,unique=false,temp=false;
    if(this.kw('OR')){this.needKw('REPLACE');replace=true}
    if(this.kw('TEMP','TEMPORARY'))temp=true;
    if(this.kw('UNIQUE'))unique=true;
    if(this.kw('TABLE')){let ine=false;if(this.kw('IF')){this.needKw('NOT');this.needKw('EXISTS');ine=true}
      const name=this.ident('nama tabel');
      if(this.kw('AS'))return {type:'createas',name,q:this.select(),ine};
      this.needOp('(','setelah nama tabel');const cols=[],cons=[];
      do{
        if(this.isKw('PRIMARY','FOREIGN','UNIQUE','CHECK','CONSTRAINT')){cons.push(this.tableCons());continue}
        cols.push(this.colDef());
      }while(this.op(','));
      this.needOp(')','untuk menutup daftar kolom');return {type:'create',name,cols,cons,ine}}
    if(this.kw('VIEW')){let ine=false;if(this.kw('IF')){this.needKw('NOT');this.needKw('EXISTS');ine=true}
      const name=this.ident('nama view');let cols=null;if(this.op('(')){cols=this.identList();this.needOp(')')}this.needKw('AS');const s=this.pk.p;const q=this.select();
      return {type:'view',name,q,replace,cols,ine,body:this.src.slice(s,this.pk.p).trim()}}
    if(this.kw('INDEX')){let ine=false;if(this.kw('IF')){this.needKw('NOT');this.needKw('EXISTS');ine=true}
      const name=this.ident('nama index');this.needKw('ON');const table=this.ident('nama tabel');this.needOp('(');const cols=[];
      do{cols.push(this.ident('nama kolom'));this.kw('ASC','DESC')}while(this.op(','));this.needOp(')');return {type:'index',name,table,cols,unique,ine}}
    if(this.isKw('PROCEDURE','FUNCTION','TRIGGER'))throw new SqlError(`CREATE ${this.pk.u} tidak didukung di simulator ini.`,'Simulator memakai dialek mirip SQLite yang tidak punya stored procedure. Baca contoh sintaks MySQL/PostgreSQL di materi, lalu coba di database sungguhan.');
    this.fail('Diharapkan TABLE, VIEW, atau INDEX setelah CREATE')}
  colDef(){const c={name:this.ident('nama kolom'),type:''};
    if(this.pk.t==='id'&&!['PRIMARY','NOT','NULL','UNIQUE','DEFAULT','CHECK','REFERENCES','CONSTRAINT','AUTOINCREMENT','AUTO_INCREMENT','GENERATED'].includes(this.pk.u))c.type=this.typeName();
    for(;;){
      if(this.kw('CONSTRAINT')){this.ident();continue}
      if(this.kw('PRIMARY')){this.needKw('KEY');this.kw('ASC','DESC');c.pk=true;if(this.kw('AUTOINCREMENT','AUTO_INCREMENT'))c.auto=true;continue}
      if(this.kw('AUTOINCREMENT','AUTO_INCREMENT')){c.auto=true;continue}
      if(this.kw('NOT')){this.needKw('NULL');c.nn=true;continue}
      if(this.kw('NULL'))continue;
      if(this.kw('UNIQUE')){c.unique=true;continue}
      if(this.kw('DEFAULT')){c.def=this.isOp('(')?(this.i++,(e=>(this.needOp(')'),e))(this.expr())):this.un();continue}
      if(this.kw('CHECK')){this.needOp('(');const s=this.pk.p;c.check=this.expr();c.checkTxt=this.src.slice(s,this.pk.p).trim();this.needOp(')');continue}
      if(this.kw('REFERENCES')){c.ref=this.refClause();continue}
      break;
    }
    return c}
  refClause(){const table=this.ident('nama tabel rujukan');let cols=null;if(this.op('(')){cols=this.identList();this.needOp(')')}
    let onDelete=null,onUpdate=null;
    while(this.kw('ON')){const w=this.kw('DELETE','UPDATE');let a;if(this.kw('CASCADE'))a='CASCADE';else if(this.kw('SET')){a=this.kw('NULL','DEFAULT')==='NULL'?'SET NULL':'SET DEFAULT'}else if(this.kw('RESTRICT'))a='RESTRICT';else{this.needKw('NO');this.needKw('ACTION');a='NO ACTION'}
      if(w==='DELETE')onDelete=a;else onUpdate=a}
    return {table,cols,onDelete,onUpdate}}
  tableCons(){let cname=null;if(this.kw('CONSTRAINT'))cname=this.ident();
    if(this.kw('PRIMARY')){this.needKw('KEY');this.needOp('(');const cols=this.identList();this.needOp(')');return {k:'pk',cols,cname}}
    if(this.kw('UNIQUE')){this.needOp('(');const cols=this.identList();this.needOp(')');return {k:'unique',cols,cname}}
    if(this.kw('CHECK')){this.needOp('(');const e=this.expr();this.needOp(')');return {k:'check',e,cname}}
    if(this.kw('FOREIGN')){this.needKw('KEY');this.needOp('(');const cols=this.identList();this.needOp(')');this.needKw('REFERENCES');return {k:'fk',cols,ref:this.refClause(),cname}}
    this.fail('Diharapkan PRIMARY KEY, FOREIGN KEY, UNIQUE, atau CHECK')}
  alter(){this.next();if(this.kw('VIEW'))throw new SqlError('ALTER VIEW tidak didukung.','Untuk mengubah view, pakai CREATE OR REPLACE VIEW nama AS SELECT ...');
    this.needKw('TABLE','setelah ALTER');const name=this.ident('nama tabel');
    if(this.kw('ADD')){if(this.isKw('CONSTRAINT','PRIMARY','FOREIGN','UNIQUE','CHECK'))return {type:'alter',name,act:'addcons',cons:this.tableCons()};this.kw('COLUMN');return {type:'alter',name,act:'add',col:this.colDef()}}
    if(this.kw('DROP')){this.kw('COLUMN');return {type:'alter',name,act:'drop',col:this.ident('nama kolom')}}
    if(this.kw('RENAME')){if(this.kw('TO'))return {type:'alter',name,act:'rename',to:this.ident()};this.kw('COLUMN');const a=this.ident();this.needKw('TO');return {type:'alter',name,act:'renamecol',from:a,to:this.ident()}}
    if(this.kw('ALTER','MODIFY')){this.kw('COLUMN');const c=this.ident();this.kw('TYPE');this.kw('SET','DATA')&&this.kw('TYPE');const ty=this.typeName();return {type:'alter',name,act:'type',col:c,ty}}
    this.fail('Diharapkan ADD, DROP, RENAME, atau ALTER COLUMN')}
  drop(){this.next();const k=this.kw('TABLE','VIEW','INDEX');if(!k)this.fail('Diharapkan TABLE, VIEW, atau INDEX setelah DROP');
    let ie=false;if(this.kw('IF')){this.needKw('EXISTS');ie=true}const name=this.ident();this.kw('CASCADE','RESTRICT');return {type:'drop',k,name,ie}}
  grant(){const g=this.next().u;const privs=[];
    do{let p=this.ident('hak akses').toUpperCase();if(p==='ALL')this.kw('PRIVILEGES');privs.push(p)}while(this.op(','));
    this.needKw('ON');this.kw('TABLE');const obj=this.ident('nama tabel');
    if(g==='GRANT')this.needKw('TO');else this.needKw('FROM');const who=this.ident('nama pengguna');
    return {type:'grant',g,privs,obj,who}}
}

/* ---------- nilai & perbandingan ---------- */
const isNum=v=>typeof v==='number';
const numish=s=>typeof s==='string'&&/^\s*[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?\s*$/.test(s);
function toNum(v){if(v==null)return null;if(isNum(v))return v;if(numish(v))return Number(v);const m=/^\s*[-+]?\d+(\.\d+)?/.exec(v);return m?Number(m[0]):0}
function cmpv(a,b){
  if(isNum(a)&&isNum(b))return a-b;
  if(isNum(a))return numish(b)?a-Number(b):-1;
  if(isNum(b))return numish(a)?Number(a)-b:1;
  return a<b?-1:a>b?1:0;
}
function truth(v){if(v==null)return null;if(isNum(v))return v!==0;return toNum(v)!==0}
const B=x=>x==null?null:(x?1:0);
function sortKey(a,b){if(a==null&&b==null)return 0;if(a==null)return -1;if(b==null)return 1;return cmpv(a,b)}
const keyOf=arr=>JSON.stringify(arr.map(v=>v==null?null:isNum(v)?v:'s'+v));
function affinity(type,v){
  if(v==null)return null;const t=(type||'').toUpperCase();
  if(/INT/.test(t)){if(numish(v)){const n=Number(v);return n}return v}
  if(/REAL|FLOA|DOUB|NUM|DEC/.test(t)){return numish(v)?Number(v):v}
  if(/CHAR|CLOB|TEXT|DATE|TIME/.test(t)){return isNum(v)?String(v):v}
  if(/BOOL/.test(t)){if(typeof v==='string'&&/^(true|false)$/i.test(v))return /^t/i.test(v)?1:0;return v}
  return v;
}
function likeRe(p,esc){let s='^';for(let i=0;i<p.length;i++){const c=p[i];if(esc&&c===esc){s+=p[++i].replace(/[.*+?^${}()|[\]\\]/g,'\\$&');continue}
  if(c==='%')s+='[\\s\\S]*';else if(c==='_')s+='[\\s\\S]';else s+=c.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}return new RegExp(s+'$','i')}

/* ---------- tanggal ---------- */
const pad=(n,w=2)=>String(n).padStart(w,'0');
function pdate(v){if(v==null)return null;if(v==='now'){return new Date()}
  const m=/^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{2}):(\d{2})(?::(\d{2}))?)?/.exec(String(v));if(!m)return null;
  return new Date(Date.UTC(+m[1],+m[2]-1,+m[3],+(m[4]||0),+(m[5]||0),+(m[6]||0)))}
const fdate=d=>`${d.getUTCFullYear()}-${pad(d.getUTCMonth()+1)}-${pad(d.getUTCDate())}`;
const ftime=d=>`${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}:${pad(d.getUTCSeconds())}`;
function nowUTC(){const n=new Date();return new Date(Date.UTC(n.getFullYear(),n.getMonth(),n.getDate(),n.getHours(),n.getMinutes(),n.getSeconds()))}
function addPart(d,part,n){d=new Date(d.getTime());part=lc(part).replace(/s$/,'');
  const map={year:'FullYear',yy:'FullYear',yyyy:'FullYear',month:'Month',mm:'Month',m:'Month',day:'Date',dd:'Date',d:'Date',hour:'Hours',hh:'Hours',minute:'Minutes',mi:'Minutes',second:'Seconds',ss:'Seconds'};
  if(part==='week'||part==='wk'){d.setUTCDate(d.getUTCDate()+7*n);return d}
  const k=map[part];if(!k)throw new SqlError(`Bagian tanggal tidak dikenal: ${part}`,'Gunakan year, month, day, hour, minute, atau second.');
  d['setUTC'+k](d['getUTC'+k]()+n);return d}
function getPart(d,part){part=lc(part).replace(/s$/,'');
  switch(part){case 'year':case 'yy':case 'yyyy':return d.getUTCFullYear();case 'month':case 'mm':case 'm':return d.getUTCMonth()+1;case 'day':case 'dd':case 'd':return d.getUTCDate();
    case 'hour':case 'hh':return d.getUTCHours();case 'minute':case 'mi':return d.getUTCMinutes();case 'second':case 'ss':return d.getUTCSeconds();
    case 'dow':case 'weekday':case 'dw':return d.getUTCDay();case 'quarter':case 'qq':return Math.floor(d.getUTCMonth()/3)+1;case 'doy':case 'dayofyear':return Math.floor((d-Date.UTC(d.getUTCFullYear(),0,1))/864e5)+1}
  throw new SqlError(`Bagian tanggal tidak dikenal: ${part}`)}
function dateMods(d,mods){for(const m of mods){const s=String(m).trim().toLowerCase();let r;
  if((r=/^([-+]?\d+(?:\.\d+)?)\s+(year|month|day|hour|minute|second)s?$/.exec(s)))d=addPart(d,r[2],+r[1]);
  else if(s==='start of month')d=new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),1));
  else if(s==='start of year')d=new Date(Date.UTC(d.getUTCFullYear(),0,1));
  else if(s==='start of day')d=new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),d.getUTCDate()));
  else throw new SqlError(`Pengubah tanggal tidak dikenal: '${m}'`,"Contoh yang benar: '+7 days', '-1 month', 'start of month'.")}return d}
function strftime(f,d){return f.replace(/%([dmYHMSjwf%])/g,(_,c)=>({d:pad(d.getUTCDate()),m:pad(d.getUTCMonth()+1),Y:d.getUTCFullYear(),H:pad(d.getUTCHours()),M:pad(d.getUTCMinutes()),S:pad(d.getUTCSeconds()),j:pad(getPart(d,'doy'),3),w:d.getUTCDay(),f:pad(d.getUTCSeconds())+'.000','%':'%'}[c]))}

/* ---------- fungsi ---------- */
const AGG=new Set(['COUNT','SUM','AVG','MIN','MAX','TOTAL','GROUP_CONCAT','STRING_AGG']);
const WIN=new Set(['ROW_NUMBER','RANK','DENSE_RANK','NTILE','LAG','LEAD','FIRST_VALUE','LAST_VALUE','PERCENT_RANK','CUME_DIST']);
const round=(x,n=0)=>{const f=Math.pow(10,n);return Math.round((x+Math.sign(x)*1e-12)*f)/f};
const SCALAR={
  ABS:a=>a[0]==null?null:Math.abs(toNum(a[0])),
  ROUND:a=>a[0]==null?null:round(toNum(a[0]),a[1]==null?0:toNum(a[1])),
  CEIL:a=>a[0]==null?null:Math.ceil(toNum(a[0])),CEILING:a=>a[0]==null?null:Math.ceil(toNum(a[0])),
  FLOOR:a=>a[0]==null?null:Math.floor(toNum(a[0])),
  MOD:a=>a[0]==null||a[1]==null||toNum(a[1])===0?null:toNum(a[0])%toNum(a[1]),
  POWER:a=>a[0]==null||a[1]==null?null:Math.pow(toNum(a[0]),toNum(a[1])),POW:a=>SCALAR.POWER(a),
  SQRT:a=>a[0]==null?null:Math.sqrt(toNum(a[0])),SIGN:a=>a[0]==null?null:Math.sign(toNum(a[0])),
  UPPER:a=>a[0]==null?null:String(a[0]).toUpperCase(),LOWER:a=>a[0]==null?null:String(a[0]).toLowerCase(),
  LENGTH:a=>a[0]==null?null:String(a[0]).length,LEN:a=>SCALAR.LENGTH(a),CHAR_LENGTH:a=>SCALAR.LENGTH(a),
  SUBSTR:a=>{if(a[0]==null)return null;const s=String(a[0]);let st=toNum(a[1]);const n=a[2]==null?undefined:toNum(a[2]);const i=st>0?st-1:(st<0?s.length+st:0);return n===undefined?s.slice(i):s.substr(i,st===0?Math.max(0,n-1):n)},
  SUBSTRING:a=>SCALAR.SUBSTR(a),
  REPLACE:a=>a[0]==null?null:String(a[0]).split(String(a[1]??'')).join(String(a[2]??'')),
  CONCAT:a=>a.map(x=>x==null?'':String(x)).join(''),
  CONCAT_WS:a=>a.slice(1).filter(x=>x!=null).map(String).join(a[0]==null?'':String(a[0])),
  TRIM:a=>a[0]==null?null:String(a[0]).trim(),LTRIM:a=>a[0]==null?null:String(a[0]).replace(/^\s+/,''),RTRIM:a=>a[0]==null?null:String(a[0]).replace(/\s+$/,''),
  INSTR:a=>a[0]==null||a[1]==null?null:String(a[0]).indexOf(String(a[1]))+1,
  LEFT:a=>a[0]==null?null:String(a[0]).slice(0,toNum(a[1])),RIGHT:a=>a[0]==null?null:(toNum(a[1])?String(a[0]).slice(-toNum(a[1])):''),
  REVERSE:a=>a[0]==null?null:[...String(a[0])].reverse().join(''),
  LPAD:a=>a[0]==null?null:String(a[0]).padStart(toNum(a[1]),a[2]==null?' ':String(a[2])),RPAD:a=>a[0]==null?null:String(a[0]).padEnd(toNum(a[1]),a[2]==null?' ':String(a[2])),
  COALESCE:a=>{for(const x of a)if(x!=null)return x;return null},IFNULL:a=>a[0]!=null?a[0]:a[1],ISNULL:a=>a[0]!=null?a[0]:a[1],NVL:a=>a[0]!=null?a[0]:a[1],
  NULLIF:a=>a[0]!=null&&a[1]!=null&&cmpv(a[0],a[1])===0?null:a[0],
  IIF:a=>truth(a[0])?a[1]:a[2],
  TYPEOF:a=>a[0]==null?'null':isNum(a[0])?(Number.isInteger(a[0])?'integer':'real'):'text',
  GREATEST:a=>a.some(x=>x==null)?null:a.reduce((m,x)=>cmpv(x,m)>0?x:m),LEAST:a=>a.some(x=>x==null)?null:a.reduce((m,x)=>cmpv(x,m)<0?x:m),
  RANDOM:()=>Math.floor(Math.random()*2**31),
  CURRENT_DATE:()=>fdate(nowUTC()),CURRENT_TIMESTAMP:()=>{const d=nowUTC();return fdate(d)+' '+ftime(d)},CURRENT_TIME:()=>ftime(nowUTC()),
  NOW:()=>SCALAR.CURRENT_TIMESTAMP(),GETDATE:()=>SCALAR.CURRENT_TIMESTAMP(),
  DATE:a=>{let d=a[0]==='now'||a[0]===undefined?nowUTC():pdate(a[0]);if(!d)return null;return fdate(dateMods(d,a.slice(1)))},
  TIME:a=>{let d=a[0]==='now'?nowUTC():pdate(a[0]);if(!d)return null;return ftime(dateMods(d,a.slice(1)))},
  DATETIME:a=>{let d=a[0]==='now'?nowUTC():pdate(a[0]);if(!d)return null;d=dateMods(d,a.slice(1));return fdate(d)+' '+ftime(d)},
  TIMESTAMP:a=>SCALAR.DATETIME(a),
  STRFTIME:a=>{const d=a[1]==='now'?nowUTC():pdate(a[1]);return d?strftime(String(a[0]),dateMods(d,a.slice(2))):null},
  DATEADD:a=>{const d=pdate(a[2]);if(!d)return null;const r=addPart(d,a[0],toNum(a[1]));return /\d\d:\d\d/.test(String(a[2]))?fdate(r)+' '+ftime(r):fdate(r)},
  DATE_ADD:a=>{const d=pdate(a[0]);if(!d)return null;const m=/^\s*([-+]?\d+)\s+(\w+)/.exec(String(a[1]));if(!m)throw new SqlError("DATE_ADD butuh teks seperti '7 day'");return fdate(addPart(d,m[2],+m[1]))},
  DATEPART:a=>{const d=pdate(a[1]);return d?getPart(d,a[0]):null},DATE_PART:a=>SCALAR.DATEPART(a),
  DATEDIFF:a=>{if(a.length===3){const x=pdate(a[1]),y=pdate(a[2]);if(!x||!y)return null;const p=lc(a[0]);if(/^(year|yy)/.test(p))return y.getUTCFullYear()-x.getUTCFullYear();if(/^(month|mm)/.test(p))return (y.getUTCFullYear()-x.getUTCFullYear())*12+y.getUTCMonth()-x.getUTCMonth();return Math.round((y-x)/864e5)}
    const x=pdate(a[0]),y=pdate(a[1]);return x&&y?Math.round((x-y)/864e5):null},
  JULIANDAY:a=>{const d=a[0]==='now'?nowUTC():pdate(a[0]);return d?d.getTime()/864e5+2440587.5:null},
  YEAR:a=>{const d=pdate(a[0]);return d?d.getUTCFullYear():null},MONTH:a=>{const d=pdate(a[0]);return d?d.getUTCMonth()+1:null},DAY:a=>{const d=pdate(a[0]);return d?d.getUTCDate():null},
};

/* ---------- basis data ---------- */
function newDb(){return {tables:{},views:{},indexes:{},grants:[],tx:null}}
const snap=db=>JSON.parse(JSON.stringify({tables:db.tables,views:db.views,indexes:db.indexes,grants:db.grants}));
function restore(db,s){const c=JSON.parse(JSON.stringify(s));db.tables=c.tables;db.views=c.views;db.indexes=c.indexes;db.grants=c.grants}
function getTable(db,name,ctx){const t=db.tables[lc(name)];if(!t){
  const all=Object.values(db.tables).map(x=>x.name);let g=null,bd=3;for(const n of all){const d=lev(lc(name),lc(n));if(d<bd){bd=d;g=n}}
  throw new SqlError(`Tabel "${name}" tidak ada${ctx?' '+ctx:''}.`,g?`Mungkin maksudmu ${g}?`:(all.length?`Tabel yang tersedia: ${all.join(', ')}.`:'Belum ada tabel. Buat dulu dengan CREATE TABLE.'))}return t}
const colIx=(t,c)=>t.cols.findIndex(x=>lc(x.name)===lc(c));

/* ---------- evaluasi ekspresi ---------- */
/* scope: {src:[{alias,label,cols:[nama]}], row:[[...] per sumber], parent, grp:[row...]|null, win:Map, aliases:{}, ctx} */
function findCol(sc,node){
  for(let s=sc;s;s=s.parent){
    if(!s.src)continue;
    let hit=null;
    for(let i=0;i<s.src.length;i++){const S=s.src[i];
      if(node.table&&lc(S.alias)!==lc(node.table))continue;
      const j=S.cols.findIndex(c=>lc(c)===lc(node.name));
      if(j>=0){if(hit&&!node.table)throw new SqlError(`Nama kolom "${node.name}" ambigu: ada di ${hit.S.label} dan ${S.label}.`,`Tulis lengkap dengan nama tabelnya, misalnya ${S.label}.${node.name}`);hit={s,i,j,S}}}
    if(hit)return hit;
    if(s.aliases&&!node.table){const a=s.aliases[lc(node.name)];if(a)return {alias:a,s}}
  }
  return null;
}
function colErr(sc,node){
  const names=[];for(let s=sc;s;s=s.parent)if(s.src)s.src.forEach(S=>S.cols.forEach(c=>names.push(c)));
  if(node.table){let ok=false;for(let s=sc;s;s=s.parent)if(s.src&&s.src.some(S=>lc(S.alias)===lc(node.table)))ok=true;
    if(!ok)return new SqlError(`Tabel atau alias "${node.table}" tidak dikenal di query ini.`,'Pastikan tabel itu ada di FROM/JOIN, dan kalau memakai alias, tulis aliasnya.')}
  let g=null,bd=3;for(const n of names){const d=lev(lc(node.name),lc(n));if(d<bd){bd=d;g=n}}
  const looksText=node.q;
  return new SqlError(`Kolom "${node.table?node.table+'.':''}${node.name}" tidak ditemukan.`,looksText?`Teks diapit kutip tunggal ('...'), bukan kutip ganda.`:(g?`Mungkin maksudmu ${g}?`:(names.length?`Kolom yang tersedia: ${[...new Set(names)].join(', ')}.`:'')))}
function rowsOfGroup(sc){return sc.grp}
function ev(n,sc){
  switch(n.op){
    case 'lit':return n.v;
    case 'col':{const h=findCol(sc,n);if(!h){throw colErr(sc,n)}
      if(h.alias){return ev(h.alias,{...h.s,aliases:null})}
      const s=h.s;
      if(s.grp&&s.row==null){const r=s.grp[0];return r?(r[h.i]?r[h.i][h.j]:null):null}
      const r=s.row[h.i];return r?r[h.j]:null}
    case 'neg':{const v=ev(n.e,sc);return v==null?null:-toNum(v)}
    case 'bin':{const a=ev(n.l,sc),b=ev(n.r,sc);
      if(n.o==='||')return a==null||b==null?null:String(a)+String(b);
      if(a==null||b==null)return null;const x=toNum(a),y=toNum(b);
      switch(n.o){case '+':return x+y;case '-':return x-y;case '*':return x*y;
        case '/':return y===0?null:x/y;case '%':return y===0?null:x%y}}
    case 'cmp':{const a=ev(n.l,sc),b=ev(n.r,sc);if(a==null||b==null)return null;const c=cmpv(a,b);
      return B({'=':c===0,'!=':c!==0,'<':c<0,'<=':c<=0,'>':c>0,'>=':c>=0}[n.o])}
    case 'is':{const a=ev(n.l,sc),b=ev(n.r,sc);const eq=(a==null&&b==null)||(a!=null&&b!=null&&cmpv(a,b)===0);return B(n.not?!eq:eq)}
    case 'isnull':{const v=ev(n.e,sc);return B(n.not?v!=null:v==null)}
    case 'AND':{const a=truth(ev(n.l,sc));if(a===false)return 0;const b=truth(ev(n.r,sc));if(b===false)return 0;return a===null||b===null?null:1}
    case 'OR':{const a=truth(ev(n.l,sc));if(a===true)return 1;const b=truth(ev(n.r,sc));if(b===true)return 1;return a===null||b===null?null:0}
    case 'NOT':{const a=truth(ev(n.e,sc));return a===null?null:B(!a)}
    case 'between':{const v=ev(n.e,sc),a=ev(n.a,sc),b=ev(n.b,sc);if(v==null||a==null||b==null)return null;const r=cmpv(v,a)>=0&&cmpv(v,b)<=0;return B(n.not?!r:r)}
    case 'like':{const v=ev(n.e,sc),p=ev(n.p,sc);if(v==null||p==null)return null;const r=likeRe(String(p),n.esc?ev(n.esc,sc):null).test(String(v));return B(n.not?!r:r)}
    case 'in':{const v=ev(n.e,sc);let vals;
      if(n.q){const r=runQuery(n.q,sc.ctx,sc);if(r.cols.length!==1)throw new SqlError('Subquery di IN harus mengembalikan tepat satu kolom.');vals=r.rows.map(x=>x[0])}
      else vals=n.list.map(e=>ev(e,sc));
      if(v==null)return vals.length?null:B(n.not);
      let found=false,hasNull=false;for(const x of vals){if(x==null){hasNull=true;continue}if(cmpv(v,x)===0){found=true;break}}
      if(found)return B(!n.not);return hasNull?null:B(n.not)}
    case 'quant':{const v=ev(n.e,sc);const r=runQuery(n.s,sc.ctx,sc);const vals=r.rows.map(x=>x[0]);
      const t=x=>{if(v==null||x==null)return null;const c=cmpv(v,x);return {'=':c===0,'!=':c!==0,'<':c<0,'<=':c<=0,'>':c>0,'>=':c>=0}[n.o]};
      if(n.q==='ALL'){let nul=false;for(const x of vals){const z=t(x);if(z===false)return 0;if(z===null)nul=true}return nul?null:1}
      let nul=false;for(const x of vals){const z=t(x);if(z===true)return 1;if(z===null)nul=true}return nul?null:0}
    case 'exists':{const r=runQuery(n.q,sc.ctx,sc,{limit1:true});return B(r.rows.length>0)}
    case 'sub':{const r=runQuery(n.q,sc.ctx,sc);if(r.cols.length!==1)throw new SqlError('Subquery skalar harus mengembalikan tepat satu kolom.','Pilih satu kolom saja di SELECT dalam kurung.');
      return r.rows.length?r.rows[0][0]:null}
    case 'row':throw new SqlError('Daftar nilai dalam kurung tidak bisa dipakai di sini.');
    case 'case':{
      if(n.base){const b=ev(n.base,sc);for(const [w,t] of n.whens){const x=ev(w,sc);if(b!=null&&x!=null&&cmpv(b,x)===0)return ev(t,sc)}}
      else for(const [w,t] of n.whens)if(truth(ev(w,sc))===true)return ev(t,sc);
      return n.els?ev(n.els,sc):null}
    case 'cast':{const v=ev(n.e,sc);if(v==null)return null;const t=n.ty.toUpperCase();
      if(/INT/.test(t))return Math.trunc(toNum(v));if(/REAL|FLOA|DOUB|NUM|DEC/.test(t))return toNum(v);if(/CHAR|TEXT|STR/.test(t))return isNum(v)?String(v):String(v);
      if(/DATE/.test(t)){const d=pdate(v);return d?fdate(d):null}return v}
    case 'fn':{
      if(n.over){if(!sc.win||!sc.win.has(n))throw new SqlError(`Fungsi window ${n.name}() hanya boleh dipakai di SELECT atau ORDER BY.`);return sc.win.get(n)}
      if(AGG.has(n.name)&&!(['MIN','MAX'].includes(n.name)&&n.args.length>1)){
        const G=sc.grp;if(!G)throw new SqlError(`Fungsi agregat ${n.name}() tidak boleh dipakai di sini.`,n.name+'() menghitung banyak baris sekaligus. Pakai di SELECT atau HAVING, bukan di WHERE. Untuk menyaring hasil agregat, gunakan HAVING.');
        return aggregate(n,G,sc)}
      if(WIN.has(n.name))throw new SqlError(`${n.name}() adalah fungsi window dan butuh OVER (...).`,`Contoh: ${n.name}() OVER (ORDER BY harga DESC)`);
      if(n.name==='MIN'||n.name==='MAX'){const a=n.args.map(e=>ev(e,sc));return SCALAR[n.name==='MIN'?'LEAST':'GREATEST'](a)}
      const f=SCALAR[n.name];if(!f)throw new SqlError(`Fungsi ${n.name}() tidak dikenal.`,'Fungsi yang didukung antara lain: COUNT, SUM, AVG, MIN, MAX, ROUND, UPPER, LOWER, LENGTH, SUBSTR, REPLACE, COALESCE, NULLIF, DATE.');
      return f(n.args.map(e=>ev(e,sc)))}
  }
  throw new SqlError('Ekspresi tidak didukung.');
}
function aggregate(n,G,sc){
  let vals=[];
  for(const r of G){const s2={...sc,row:r,grp:null};if(n.filter&&truth(ev(n.filter,s2))!==true)continue;vals.push(n.star?1:ev(n.args[0],s2))}
  if(!n.star)vals=vals.filter(v=>v!=null);
  if(n.distinct){const seen=new Set;vals=vals.filter(v=>{const k=keyOf([v]);if(seen.has(k))return false;seen.add(k);return true})}
  switch(n.name){
    case 'COUNT':return vals.length;
    case 'SUM':return vals.length?vals.reduce((a,b)=>a+toNum(b),0):null;
    case 'TOTAL':return vals.reduce((a,b)=>a+toNum(b),0);
    case 'AVG':return vals.length?vals.reduce((a,b)=>a+toNum(b),0)/vals.length:null;
    case 'MIN':return vals.length?vals.reduce((m,x)=>cmpv(x,m)<0?x:m):null;
    case 'MAX':return vals.length?vals.reduce((m,x)=>cmpv(x,m)>0?x:m):null;
    case 'GROUP_CONCAT':case 'STRING_AGG':{const sep=n.args[1]?ev(n.args[1],{...sc,row:G[0]||null,grp:null}):',';return vals.length?vals.map(String).join(sep):null}
  }
}
function hasAgg(n){if(!n||typeof n!=='object')return false;
  if(n.op==='fn'&&!n.over&&AGG.has(n.name)&&!(['MIN','MAX'].includes(n.name)&&n.args.length>1))return true;
  if(n.op==='sub'||n.op==='exists'||n.op==='in'&&n.q||n.op==='quant'){if(n.op==='in')return hasAgg(n.e);return n.op==='quant'?hasAgg(n.e):false}
  for(const k in n){if(k==='over')continue;const v=n[k];if(Array.isArray(v)){for(const x of v)if(Array.isArray(x)?x.some(hasAgg):hasAgg(x))return true}else if(v&&typeof v==='object'&&hasAgg(v))return true}
  return false}
function collectWin(n,out){if(!n||typeof n!=='object')return out;if(n.op==='fn'&&n.over)out.push(n);
  if(n.op==='sub'||n.op==='exists')return out;
  for(const k in n){const v=n[k];if(Array.isArray(v))v.forEach(x=>Array.isArray(x)?x.forEach(y=>collectWin(y,out)):collectWin(x,out));else if(v&&typeof v==='object'&&k!=='q')collectWin(v,out)}return out}

/* ---------- FROM ---------- */
function nullRow(S){return S.cols.map(()=>null)}
function evalFrom(it,ctx,outer,tr){
  if(it.kind==='table'){
    const key=lc(it.name),alias=it.alias||it.name;
    if(ctx.ctes&&ctx.ctes[key]){const c=ctx.ctes[key];return {src:[{alias,label:alias,cols:c.cols,tbl:it.name}],rows:c.rows.map(r=>[r])}}
    if(ctx.db.views[key]){const v=ctx.db.views[key];const r=runQuery(v.q,{...ctx,ctes:null},null);const cols=v.cols||r.cols;return {src:[{alias,label:alias,cols,tbl:v.name,view:1}],rows:r.rows.map(x=>[x])}}
    const t=getTable(ctx.db,it.name);
    ctx.stats.scanned+=t.rows.length;
    return {src:[{alias,label:alias,cols:t.cols.map(c=>c.name),tbl:t.name}],rows:t.rows.map(r=>[r])};
  }
  if(it.kind==='sub'){const r=runQuery(it.q,{...ctx},outer);const alias=it.alias||'subquery';return {src:[{alias,label:alias,cols:r.cols}],rows:r.rows.map(x=>[x])}}
  const L=evalFrom(it.l,ctx,outer),R=evalFrom(it.r,ctx,outer);
  const src=[...L.src,...R.src],rows=[],pairs=[];
  let cond=it.on;
  if(it.using){cond=it.using.map(c=>({op:'cmp',o:'=',l:{op:'col',table:L.src[L.src.length-1].alias,name:c},r:{op:'col',table:R.src[0].alias,name:c}})).reduce((a,b)=>a?{op:'AND',l:a,r:b}:b,null)}
  const rm=new Array(R.rows.length).fill(false);
  L.rows.forEach((l,li)=>{let hit=false;
    R.rows.forEach((r,ri)=>{const row=[...l,...r];
      if(it.jt==='CROSS'||truth(ev(cond,{src,row,parent:outer,ctx}))===true){rows.push(row);pairs.push([li,ri]);hit=true;rm[ri]=true}});
    if(!hit&&(it.jt==='LEFT'||it.jt==='FULL')){rows.push([...l,...R.src.map(nullRow)]);pairs.push([li,null])}});
  if(it.jt==='RIGHT'||it.jt==='FULL')R.rows.forEach((r,ri)=>{if(!rm[ri]){rows.push([...L.src.map(nullRow),...r]);pairs.push([null,ri])}});
  if(tr&&!tr.join&&L.src.length===1&&R.src.length===1)tr.join={type:it.jt,comma:!!it.comma,on:it.on||it.using?true:false,
    left:{label:L.src[0].label,cols:L.src[0].cols,rows:L.rows.map(x=>x[0])},right:{label:R.src[0].label,cols:R.src[0].cols,rows:R.rows.map(x=>x[0])},pairs};
  return {src,rows};
}

/* ---------- SELECT ---------- */
function runQuery(q,ctx,outer,opt={}){
  if(q.type!=='select')throw new SqlError('Diharapkan SELECT');
  let c={...ctx,ctes:{...(ctx.ctes||{})}};
  if(q.ctes)for(const ct of q.ctes){
    const key=lc(ct.name);
    if(ct.rec&&q.ctes&&refersTo(ct.q,key)){
      const b=ct.q.body;if(b.type!=='compound'||!/UNION/.test(b.op))throw new SqlError('CTE rekursif harus berbentuk: query awal UNION [ALL] query rekursif.');
      const all=b.op==='UNION ALL';
      const anchor=runBody(b.l,c,outer);const cols=ct.cols||anchor.cols;
      let total=anchor.rows.slice(),work=anchor.rows.slice();const seen=new Set(total.map(keyOf));let it=0;
      while(work.length){if(++it>1000)throw new SqlError('CTE rekursif berhenti setelah 1000 putaran.','Pastikan bagian rekursif punya kondisi berhenti, misalnya WHERE n < 10.');
        const step=runBody(b.r,{...c,ctes:{...c.ctes,[key]:{cols,rows:work}}},outer);
        let nw=step.rows;if(!all)nw=nw.filter(r=>{const k=keyOf(r);if(seen.has(k))return false;seen.add(k);return true});
        total.push(...nw);work=nw;if(total.length>5000)throw new SqlError('Hasil CTE rekursif terlalu besar (lebih dari 5000 baris).')}
      c.ctes[key]={cols,rows:total};
    }else{const r=runQuery(ct.q,c,outer);c.ctes[key]={cols:ct.cols||r.cols,rows:r.rows}}
  }
  const tr=opt.trace?{}:null;
  if(q.body.type==='core'){
    return runCore(q.body,c,outer,{order:q.order,limit:q.limit,offset:q.offset,tr,limit1:opt.limit1});
  }
  const r=runBody(q.body,c,outer);
  let rows=r.rows;
  if(q.order){
    const pos=q.order.map(o=>{if(o.e.op==='lit'&&isNum(o.e.v))return o.e.v-1;if(o.e.op==='col'&&!o.e.table){const i=r.cols.findIndex(x=>lc(x)===lc(o.e.name));if(i>=0)return i}
      throw new SqlError('ORDER BY pada UNION harus memakai nama kolom hasil atau nomor kolom.')});
    rows=rows.slice().sort((a,b)=>{for(let k=0;k<pos.length;k++){const d=sortKey(a[pos[k]],b[pos[k]]);if(d)return q.order[k].desc?-d:d}return 0})}
  rows=applyLimit(rows,q.limit,q.offset,c);
  return {cols:r.cols,rows};
}
function refersTo(q,key){let f=false;(function w(n){if(!n||typeof n!=='object'||f)return;if(n.kind==='table'&&lc(n.name)===key){f=true;return}for(const k in n){const v=n[k];if(Array.isArray(v))v.forEach(w);else if(v&&typeof v==='object')w(v)}})(q);return f}
function applyLimit(rows,limit,offset,ctx){
  const off=offset?toNum(ev(offset,{ctx})):0;let lim=limit?toNum(ev(limit,{ctx})):null;if(lim!=null&&lim<0)lim=null;
  return rows.slice(off,lim==null?undefined:off+lim)}
function runBody(b,ctx,outer){
  if(b.type==='core')return runCore(b,ctx,outer,{});
  if(b.type==='paren')return runQuery(b.q,ctx,outer);
  if(b.type==='values'){const rows=b.rows.map(r=>r.map(e=>ev(e,{ctx,parent:outer})));return {cols:rows[0].map((_,i)=>'column'+(i+1)),rows}}
  const L=runBody(b.l,ctx,outer),R=runBody(b.r,ctx,outer);
  if(L.cols.length!==R.cols.length)throw new SqlError(`Kedua sisi ${b.op} harus punya jumlah kolom yang sama (${L.cols.length} lawan ${R.cols.length}).`);
  let rows;const K=new Set(R.rows.map(keyOf));
  if(b.op==='UNION ALL')rows=[...L.rows,...R.rows];
  else if(b.op==='UNION'){const s=new Set;rows=[...L.rows,...R.rows].filter(r=>{const k=keyOf(r);if(s.has(k))return false;s.add(k);return true})}
  else if(b.op==='INTERSECT'){const s=new Set;rows=L.rows.filter(r=>{const k=keyOf(r);if(!K.has(k)||s.has(k))return false;s.add(k);return true})}
  else{const s=new Set;rows=L.rows.filter(r=>{const k=keyOf(r);if(K.has(k)||s.has(k))return false;s.add(k);return true})}
  return {cols:L.cols,rows};
}
function colLabel(c){if(c.alias)return c.alias;if(c.e.op==='col')return c.e.name;return c.txt}
function runCore(core,ctx,outer,o){
  const tr=o.tr;
  const F=core.from?evalFrom(core.from,ctx,outer,tr):{src:[],rows:[[]]};
  const src=F.src;
  if(tr){tr.from={cols:src.flatMap(S=>S.cols.map(c=>src.length>1?S.label+'.'+c:c)),rows:F.rows.map(r=>r.flat()),tables:src.map(S=>S.label)}}
  // alias SELECT boleh dipakai di GROUP BY/HAVING/ORDER BY
  const aliases={};core.cols.forEach(c=>{if(!c.star&&c.alias)aliases[lc(c.alias)]=c.e});
  const base={src,parent:outer,ctx};
  let rows=F.rows;
  if(core.where){if(hasAgg(core.where))throw new SqlError('Fungsi agregat tidak boleh dipakai di WHERE.','WHERE menyaring baris satu per satu, sebelum dikelompokkan. Untuk menyaring hasil COUNT/SUM/AVG, gunakan HAVING setelah GROUP BY.');
    const keep=rows.map(r=>truth(ev(core.where,{...base,row:r}))===true);
    if(tr)tr.where={keep};rows=rows.filter((r,i)=>keep[i])}
  // ekspansi bintang
  const outCols=[],exprs=[];
  for(const c of core.cols){
    if(c.star){let any=false;src.forEach((S,i)=>{if(c.table&&lc(S.alias)!==lc(c.table))return;any=true;S.cols.forEach((cn,j)=>{outCols.push(cn);exprs.push({op:'col',table:S.alias,name:cn,_ix:[i,j]})})});
      if(!any)throw new SqlError(c.table?`Tabel "${c.table}" tidak ada di FROM.`:'SELECT * butuh FROM.');continue}
    outCols.push(colLabel(c));exprs.push(c.e)}
  const agg=!!core.group||exprs.some(hasAgg)||(core.having&&hasAgg(core.having))||(o.order||[]).some(x=>hasAgg(x.e));
  let items;
  if(agg){
    const gsc=r=>({...base,row:r,aliases});
    const groupExprs=(core.group||[]).map(g=>g.op==='lit'&&isNum(g.v)?(exprs[g.v-1]||(()=>{throw new SqlError('Nomor kolom di GROUP BY di luar jangkauan.')})()):g);
    if(groupExprs.some(hasAgg))throw new SqlError('Fungsi agregat tidak boleh dipakai di GROUP BY.');
    const map=new Map;const order=[];
    rows.forEach((r,ri)=>{const k=keyOf(groupExprs.map(g=>ev(g,gsc(r))));if(!map.has(k)){map.set(k,[]);order.push(k)}map.get(k).push(ri)});
    let groups=order.map(k=>map.get(k));
    if(!core.group&&!groups.length)groups=[[]];
    if(tr&&core.group)tr.group={groups:groups.map(ix=>({idx:ix.map(i=>tr.where?tr.where.keep.reduce((a,kp,j)=>{if(kp)a.push(j);return a},[])[i]:i),label:ix.length?groupExprs.map(g=>fmt(ev(g,gsc(rows[ix[0]])))).join(', '):''}))};
    items=groups.map(ix=>({...base,row:null,grp:ix.map(i=>rows[i]),aliases}));
    if(core.having){const keep=items.map(s=>truth(ev(core.having,s))===true);if(tr)tr.having={keep};items=items.filter((s,i)=>keep[i])}
  }else{
    if(core.having)throw new SqlError('HAVING hanya dipakai bersama GROUP BY atau fungsi agregat.','Untuk menyaring baris biasa, gunakan WHERE.');
    items=rows.map(r=>({...base,row:r,aliases}));
  }
  // fungsi window
  const wins=[];exprs.forEach(e=>collectWin(e,wins));(o.order||[]).forEach(x=>collectWin(x.e,wins));
  if(wins.length){items.forEach(s=>s.win=new Map);for(const w of wins)computeWin(w,items)}
  // proyeksi
  let out=items.map(s=>exprs.map(e=>e._ix?(s.row?(s.row[e._ix[0]]||[])[e._ix[1]]??null:(s.grp[0]?s.grp[0][e._ix[0]][e._ix[1]]:null)):ev(e,s)));
  if(tr)tr.select={cols:outCols,rows:out.map(r=>r.slice())};
  let idx=out.map((_,i)=>i);
  if(core.distinct){const s=new Set;idx=idx.filter(i=>{const k=keyOf(out[i]);if(s.has(k))return false;s.add(k);return true});if(tr)tr.distinct={keep:out.map((_,i)=>idx.includes(i))}}
  if(o.order){
    const keys=idx.map(i=>o.order.map(x=>{
      if(x.e.op==='lit'&&isNum(x.e.v)){if(x.e.v<1||x.e.v>outCols.length)throw new SqlError('Nomor kolom di ORDER BY di luar jangkauan.');return out[i][x.e.v-1]}
      if(x.e.op==='col'&&!x.e.table){const ai=core.cols.findIndex(c=>!c.star&&c.alias&&lc(c.alias)===lc(x.e.name));if(ai>=0){const pos=exprs.indexOf(core.cols[ai].e);return out[i][pos]}}
      return ev(x.e,items[i])}));
    const pos=idx.map((_,k)=>k);
    pos.sort((a,b)=>{for(let k=0;k<o.order.length;k++){const X=o.order[k];let d;const va=keys[a][k],vb=keys[b][k];
      if(X.nulls&&(va==null)!==(vb==null))return (va==null)===(X.nulls==='FIRST')?-1:1;
      d=sortKey(va,vb);if(d)return X.desc?-d:d}return a-b});
    idx=pos.map(k=>idx[k]);
    if(tr)tr.order={idx:idx.slice()};
  }
  let fin=idx.map(i=>out[i]);
  const top=core.top?toNum(ev(core.top,{ctx})):null;
  if(o.limit||o.offset){const before=fin.length;fin=applyLimit(fin,o.limit,o.offset,ctx);if(tr)tr.limit={n:fin.length,from:before,offset:o.offset?toNum(ev(o.offset,{ctx})):0}}
  else if(top!=null){fin=fin.slice(0,top);if(tr)tr.limit={n:fin.length,from:idx.length,offset:0}}
  const res={cols:outCols,rows:fin};if(tr)res.trace=tr;return res;
}
function computeWin(w,items){
  const spec=w.over;
  const parts=new Map;const ord=[];
  items.forEach((s,i)=>{const k=keyOf((spec.part||[]).map(e=>ev(e,s)));if(!parts.has(k)){parts.set(k,[]);ord.push(k)}parts.get(k).push(i)});
  for(const k of ord){
    let P=parts.get(k);
    const okeys=P.map(i=>(spec.order||[]).map(x=>ev(x.e,items[i])));
    const pos=P.map((_,j)=>j);
    if(spec.order)pos.sort((a,b)=>{for(let q=0;q<spec.order.length;q++){const d=sortKey(okeys[a][q],okeys[b][q]);if(d)return spec.order[q].desc?-d:d}return a-b});
    const S=pos.map(j=>P[j]),K=pos.map(j=>keyOf(okeys[j]));
    const n=S.length;
    const argv=(i,ai,def)=>w.args[ai]?ev(w.args[ai],items[i]):def;
    let rank=0,dense=0;
    S.forEach((ii,j)=>{
      const peerStart=j===0||K[j]!==K[j-1];if(peerStart){rank=j+1;dense++}
      let v;
      switch(w.name){
        case 'ROW_NUMBER':v=j+1;break;
        case 'RANK':v=rank;break;
        case 'DENSE_RANK':v=dense;break;
        case 'PERCENT_RANK':v=n>1?(rank-1)/(n-1):0;break;
        case 'CUME_DIST':{let e=j;while(e+1<n&&K[e+1]===K[j])e++;v=(e+1)/n;break}
        case 'NTILE':{const b=toNum(argv(ii,0,1));const per=Math.floor(n/b),extra=n%b;let acc=0,t=1;for(;t<=b;t++){const sz=per+(t<=extra?1:0);if(j<acc+sz)break;acc+=sz}v=t;break}
        case 'LAG':case 'LEAD':{const off=toNum(argv(ii,1,1));const t=w.name==='LAG'?j-off:j+off;v=t>=0&&t<n?ev(w.args[0],items[S[t]]):argv(ii,2,null);break}
        case 'FIRST_VALUE':v=ev(w.args[0],items[S[0]]);break;
        case 'LAST_VALUE':{let e=spec.order?j:n-1;if(spec.order&&!/UNBOUNDED FOLLOWING/.test(spec.frame||''))while(e+1<n&&K[e+1]===K[j])e++;else e=n-1;v=ev(w.args[0],items[S[e]]);break}
        default:{
          if(!AGG.has(w.name))throw new SqlError(`Fungsi ${w.name}() tidak bisa dipakai dengan OVER.`);
          let end=n-1;
          if(spec.order){end=j;if(!/ROWS/.test(spec.frame||''))while(end+1<n&&K[end+1]===K[j])end++}
          let start=0;const fm=/ROWS BETWEEN (\d+) PRECEDING AND CURRENT ROW/.exec(spec.frame||'');if(fm)start=Math.max(0,j-+fm[1]);
          const G=[];for(let q=start;q<=end;q++){const it=items[S[q]];if(it.grp)G.push(...it.grp);else G.push(it.row)}
          const it0=items[ii];
          if(it0.grp){ // agregat di atas grup: nilai agregat per grup lalu dijumlah
            const vals=[];for(let q=start;q<=end;q++)vals.push(ev(w.args[0],items[S[q]]));
            const nn=vals.filter(x=>x!=null);
            v=w.name==='COUNT'?(w.star?end-start+1:nn.length):w.name==='SUM'?(nn.length?nn.reduce((a,b)=>a+toNum(b),0):null):w.name==='AVG'?(nn.length?nn.reduce((a,b)=>a+toNum(b),0)/nn.length:null):w.name==='MIN'?(nn.length?nn.reduce((m,x)=>cmpv(x,m)<0?x:m):null):(nn.length?nn.reduce((m,x)=>cmpv(x,m)>0?x:m):null);
          }else v=aggregate({...w,over:null},G,it0);
        }
      }
      items[ii].win.set(w,v);
    });
  }
}

/* ---------- penulisan data & batasan ---------- */
function checkRow(db,t,row,skipIdx){
  t.cols.forEach((c,i)=>{if((c.nn||c.pk)&&row[i]==null&&!(c.pk&&isIntPk(t,c)))throw new SqlError(`Kolom ${t.name}.${c.name} tidak boleh kosong (NOT NULL).`,`Isi nilai untuk ${c.name} di INSERT/UPDATE.`)});
  const sc={src:[{alias:t.name,label:t.name,cols:t.cols.map(c=>c.name)}],row:[row]};
  t.cols.forEach(c=>{if(c.check&&truth(ev(c.check,sc))===false)throw new SqlError(`Nilai melanggar aturan CHECK pada kolom ${t.name}.${c.name}.`,'Aturan: '+(c.checkTxt||'lihat definisi tabel'))});
  (t.checks||[]).forEach(ch=>{if(truth(ev(ch.e,sc))===false)throw new SqlError(`Baris melanggar aturan CHECK${ch.cname?' '+ch.cname:''} pada tabel ${t.name}.`)});
  for(const u of uniqueSets(db,t)){
    const vals=u.cols.map(i=>row[i]);if(vals.some(v=>v==null))continue;
    t.rows.forEach((r,ri)=>{if(ri===skipIdx)return;if(u.cols.every((i,k)=>r[i]!=null&&cmpv(r[i],vals[k])===0))
      throw new SqlError(`Nilai ${vals.map(fmt).join(', ')} sudah ada di ${t.name}.${u.cols.map(i=>t.cols[i].name).join(', ')} (${u.why}).`,u.why==='PRIMARY KEY'?'Primary key harus unik untuk setiap baris.':'Kolom ini tidak boleh punya nilai kembar.')})}
  for(const fk of t.fks||[]){
    const vals=fk.cols.map(c=>row[colIx(t,c)]);if(vals.some(v=>v==null))continue;
    const p=db.tables[lc(fk.table)];if(!p)throw new SqlError(`Tabel rujukan ${fk.table} tidak ada.`);
    const pc=(fk.refCols||pkCols(p)).map(c=>colIx(p,c));
    if(!p.rows.some(r=>pc.every((i,k)=>r[i]!=null&&cmpv(r[i],vals[k])===0)))
      throw new SqlError(`FOREIGN KEY gagal: ${t.name}.${fk.cols.join(',')} = ${vals.map(fmt).join(', ')} tidak ada di ${p.name}.${pc.map(i=>p.cols[i].name).join(',')}.`,`Tambahkan dulu barisnya di tabel ${p.name}, atau pakai nilai yang sudah ada.`)}
}
const pkCols=t=>t.cols.filter(c=>c.pk).map(c=>c.name);
const isIntPk=(t,c)=>c.pk&&/INT/i.test(c.type)&&t.cols.filter(x=>x.pk).length===1;
function uniqueSets(db,t){const u=[];const pk=t.cols.map((c,i)=>c.pk?i:-1).filter(i=>i>=0);if(pk.length)u.push({cols:pk,why:'PRIMARY KEY'});
  t.cols.forEach((c,i)=>{if(c.unique)u.push({cols:[i],why:'UNIQUE'})});(t.uniques||[]).forEach(cs=>u.push({cols:cs.map(c=>colIx(t,c)),why:'UNIQUE'}));
  Object.values(db.indexes).forEach(ix=>{if(ix.unique&&lc(ix.table)===lc(t.name))u.push({cols:ix.cols.map(c=>colIx(t,c)),why:'UNIQUE INDEX '+ix.name})});return u}
function children(db,t){const out=[];for(const c of Object.values(db.tables))for(const fk of c.fks||[])if(lc(fk.table)===lc(t.name))out.push({c,fk});return out}
function deleteRows(db,t,idxSet,depth=0){
  // aturan ON DELETE di tabel anak
  const doomed=t.rows.filter((r,i)=>idxSet.has(i));
  for(const {c,fk} of children(db,t)){
    const pc=(fk.refCols||pkCols(t)).map(x=>colIx(t,x)),cc=fk.cols.map(x=>colIx(c,x));
    const hit=new Set;c.rows.forEach((r,ri)=>{if(doomed.some(d=>pc.every((pi,k)=>r[cc[k]]!=null&&cmpv(r[cc[k]],d[pi])===0)))hit.add(ri)});
    if(!hit.size)continue;
    if(fk.onDelete==='CASCADE'){if(c===t){hit.forEach(i=>idxSet.add(i))}else deleteRows(db,c,hit,depth+1)}
    else if(fk.onDelete==='SET NULL'){hit.forEach(ri=>cc.forEach(ci=>c.rows[ri][ci]=null))}
    else if(!(c===t&&[...hit].every(i=>idxSet.has(i))))throw new SqlError(`Tidak bisa menghapus dari ${t.name}: baris itu masih dirujuk oleh ${c.name}.${fk.cols.join(',')} (FOREIGN KEY).`,`Hapus dulu baris terkait di ${c.name}, atau buat FOREIGN KEY dengan ON DELETE CASCADE.`)
  }
  const n=t.rows.length;t.rows=t.rows.filter((r,i)=>!idxSet.has(i));return n-t.rows.length;
}

/* ---------- eksekusi perintah ---------- */
function fmt(v){if(v==null)return 'NULL';if(isNum(v))return Number.isInteger(v)?String(v):String(round(v,4));return String(v)}
function tableFromDef(db,st){
  const cols=st.cols.map(c=>({name:c.name,type:c.type||'',pk:!!c.pk,nn:!!c.nn,unique:!!c.unique,def:c.def||null,check:c.check||null,checkTxt:c.checkTxt||'',auto:!!c.auto}));
  const names=new Set;cols.forEach(c=>{if(names.has(lc(c.name)))throw new SqlError(`Kolom ${c.name} ditulis dua kali.`);names.add(lc(c.name))});
  const t={name:st.name,cols,rows:[],fks:[],uniques:[],checks:[]};
  st.cols.forEach(c=>{if(c.ref)t.fks.push({cols:[c.name],table:c.ref.table,refCols:c.ref.cols,onDelete:c.ref.onDelete})});
  for(const k of st.cons){
    if(k.k==='pk'){k.cols.forEach(n=>{const i=colIx(t,n);if(i<0)throw new SqlError(`PRIMARY KEY menyebut kolom ${n} yang tidak ada.`);t.cols[i].pk=true})}
    else if(k.k==='unique')t.uniques.push(k.cols);
    else if(k.k==='check')t.checks.push({e:k.e,cname:k.cname});
    else if(k.k==='fk')t.fks.push({cols:k.cols,table:k.ref.table,refCols:k.ref.cols,onDelete:k.ref.onDelete,cname:k.cname});
  }
  for(const fk of t.fks){fk.cols.forEach(n=>{if(colIx(t,n)<0)throw new SqlError(`FOREIGN KEY menyebut kolom ${n} yang tidak ada.`)});
    if(lc(fk.table)!==lc(t.name)&&!db.tables[lc(fk.table)])throw new SqlError(`FOREIGN KEY merujuk tabel ${fk.table} yang belum ada.`,'Buat tabel induknya lebih dulu.')}
  return t;
}
function insertRow(db,t,vals,cols){
  const row=t.cols.map(c=>c.def?ev(c.def,{}):null);
  const set=cols?cols.map(n=>{const i=colIx(t,n);if(i<0)throw new SqlError(`Kolom "${n}" tidak ada di tabel ${t.name}.`,`Kolom ${t.name}: ${t.cols.map(c=>c.name).join(', ')}.`);return i}):t.cols.map((_,i)=>i);
  if(vals.length!==set.length)throw new SqlError(`Jumlah nilai (${vals.length}) tidak sama dengan jumlah kolom (${set.length}).`,cols?'Setiap kolom yang disebut butuh tepat satu nilai.':`Tabel ${t.name} punya ${t.cols.length} kolom: ${t.cols.map(c=>c.name).join(', ')}. Sebutkan kolomnya, misalnya INSERT INTO ${t.name} (kolom1, kolom2) VALUES (...).`);
  set.forEach((ci,k)=>row[ci]=affinity(t.cols[ci].type,vals[k]));
  t.cols.forEach((c,i)=>{if(row[i]==null&&isIntPk(t,c)){t.seq=Math.max(t.seq||0,...t.rows.map(r=>toNum(r[i])||0))+1;row[i]=t.seq}});
  checkRow(db,t,row,-1);t.rows.push(row);
}
function execOne(db,st,opt){
  const ctx={db,ctes:null,stats:{scanned:0}};
  switch(st.type){
    case 'select':{const r=runQuery(st,ctx,null,{trace:opt.trace});return {kind:'rows',cols:r.cols,rows:r.rows,trace:r.trace,stats:ctx.stats}}
    case 'explain':return {kind:'rows',cols:['detail'],rows:plan(db,st.q).map(x=>[x])};
    case 'create':{const k=lc(st.name);if(db.tables[k]||db.views[k]){if(st.ine)return {kind:'msg',msg:`Tabel ${st.name} sudah ada, dilewati.`};throw new SqlError(`Tabel ${st.name} sudah ada.`,'Pakai CREATE TABLE IF NOT EXISTS, atau hapus dulu dengan DROP TABLE.')}
      db.tables[k]=tableFromDef(db,st);return {kind:'msg',msg:`Tabel ${st.name} dibuat dengan ${st.cols.length} kolom.`,ddl:true}}
    case 'createas':{const r=runQuery(st.q,ctx,null);const k=lc(st.name);if(db.tables[k])throw new SqlError(`Tabel ${st.name} sudah ada.`);
      db.tables[k]={name:st.name,cols:r.cols.map(n=>({name:n,type:''})),rows:r.rows.map(x=>x.slice()),fks:[],uniques:[],checks:[]};return {kind:'msg',msg:`Tabel ${st.name} dibuat dari hasil query (${r.rows.length} baris).`,ddl:true}}
    case 'insert':{const t=getTable(db,st.name,'untuk INSERT');let rows;
      if(st.q){rows=runQuery(st.q,ctx,null).rows}else rows=st.rows.map(r=>r.map(e=>ev(e,{ctx})));
      if(st.rows&&st.rows.length===1&&st.rows[0].length===0){rows=[[]];t.rows.push(t.cols.map(c=>c.def?ev(c.def,{}):null));return {kind:'msg',msg:'1 baris ditambahkan.'}}
      rows.forEach(r=>insertRow(db,t,r,st.cols));return {kind:'msg',msg:`${rows.length} baris ditambahkan ke ${t.name}.`,changed:t.name}}
    case 'update':{const t=getTable(db,st.name,'untuk UPDATE');const al=st.alias||t.name;const S=[{alias:al,label:t.name,cols:t.cols.map(c=>c.name)}];
      const sets=st.sets.map(([c,e])=>{const i=colIx(t,c);if(i<0)throw new SqlError(`Kolom "${c}" tidak ada di tabel ${t.name}.`);return [i,e]});
      let n=0;const old=t.rows.map(r=>r.slice());
      t.rows.forEach((r,ri)=>{const sc={src:S,row:[old[ri]],ctx};if(st.where&&truth(ev(st.where,sc))!==true)return;
        const nr=old[ri].slice();sets.forEach(([i,e])=>nr[i]=affinity(t.cols[i].type,ev(e,sc)));
        // jangan putus rujukan anak
        for(const {c,fk} of children(db,t)){const pc=(fk.refCols||pkCols(t)).map(x=>colIx(t,x)),cc=fk.cols.map(x=>colIx(c,x));
          if(pc.some(i=>cmpv(old[ri][i]??'',nr[i]??'')!==0)&&c.rows.some(x=>pc.every((pi,k)=>x[cc[k]]!=null&&cmpv(x[cc[k]],old[ri][pi])===0)))
            throw new SqlError(`Tidak bisa mengubah ${t.name}.${pc.map(i=>t.cols[i].name)}: nilainya masih dirujuk oleh ${c.name}.`)}
        checkRow(db,t,nr,ri);t.rows[ri]=nr;n++});
      return {kind:'msg',msg:`${n} baris diubah di ${t.name}.`+(st.where?'':' (Tanpa WHERE: semua baris ikut berubah!)'),changed:t.name,warn:!st.where}}
    case 'delete':{const t=getTable(db,st.name,'untuk DELETE');const al=st.alias||t.name;const S=[{alias:al,label:t.name,cols:t.cols.map(c=>c.name)}];
      const set=new Set;t.rows.forEach((r,ri)=>{if(!st.where||truth(ev(st.where,{src:S,row:[r],ctx}))===true)set.add(ri)});
      const n=deleteRows(db,t,set);return {kind:'msg',msg:`${n} baris dihapus dari ${t.name}.`+(st.where?'':' (Tanpa WHERE: semua baris terhapus!)'),changed:t.name,warn:!st.where}}
    case 'truncate':{const t=getTable(db,st.name);if(children(db,t).some(({c,fk})=>c!==t&&c.rows.length))throw new SqlError(`TRUNCATE ${t.name} ditolak: tabel lain masih merujuk ke tabel ini.`,'Kosongkan dulu tabel anaknya.');
      const n=t.rows.length;t.rows=[];t.seq=0;return {kind:'msg',msg:`Tabel ${t.name} dikosongkan (${n} baris hilang). Strukturnya tetap ada.`,changed:t.name}}
    case 'drop':{const k=lc(st.name);
      if(st.k==='TABLE'){const t=db.tables[k];if(!t){if(st.ie)return {kind:'msg',msg:'Tabel tidak ada, dilewati.'};getTable(db,st.name)}
        const ch=children(db,t).filter(x=>x.c!==t);if(ch.length)throw new SqlError(`Tabel ${t.name} tidak bisa dihapus: masih dirujuk FOREIGN KEY dari ${ch.map(x=>x.c.name).join(', ')}.`,'Hapus dulu tabel anaknya, atau hapus constraint-nya.');
        delete db.tables[k];Object.keys(db.indexes).forEach(i=>{if(lc(db.indexes[i].table)===k)delete db.indexes[i]});return {kind:'msg',msg:`Tabel ${t.name} dihapus beserta seluruh datanya.`,ddl:true}}
      if(st.k==='VIEW'){if(!db.views[k]){if(st.ie)return {kind:'msg',msg:'View tidak ada, dilewati.'};throw new SqlError(`View ${st.name} tidak ada.`)}delete db.views[k];return {kind:'msg',msg:`View ${st.name} dihapus. Tabel aslinya tidak terpengaruh.`,ddl:true}}
      if(!db.indexes[k]){if(st.ie)return {kind:'msg',msg:'Index tidak ada, dilewati.'};throw new SqlError(`Index ${st.name} tidak ada.`)}delete db.indexes[k];return {kind:'msg',msg:`Index ${st.name} dihapus.`,ddl:true}}
    case 'alter':{const t=getTable(db,st.name);
      if(st.act==='add'){if(colIx(t,st.col.name)>=0)throw new SqlError(`Kolom ${st.col.name} sudah ada.`);const c={name:st.col.name,type:st.col.type||'',nn:!!st.col.nn,unique:!!st.col.unique,def:st.col.def||null,check:st.col.check||null};
        const dv=c.def?ev(c.def,{}):null;if(c.nn&&dv==null&&t.rows.length)throw new SqlError(`Kolom NOT NULL baru butuh DEFAULT karena tabel ${t.name} sudah berisi data.`);
        t.cols.push(c);t.rows.forEach(r=>r.push(dv));if(st.col.ref)t.fks.push({cols:[c.name],table:st.col.ref.table,refCols:st.col.ref.cols,onDelete:st.col.ref.onDelete});
        return {kind:'msg',msg:`Kolom ${c.name} ditambahkan ke ${t.name}.`,ddl:true}}
      if(st.act==='drop'){const i=colIx(t,st.col);if(i<0)throw new SqlError(`Kolom ${st.col} tidak ada di ${t.name}.`);if(t.cols[i].pk)throw new SqlError('Kolom PRIMARY KEY tidak bisa dihapus.');
        if(children(db,t).some(({fk})=>(fk.refCols||[]).some(c=>lc(c)===lc(st.col))))throw new SqlError('Kolom ini masih dirujuk FOREIGN KEY tabel lain.');
        t.cols.splice(i,1);t.rows.forEach(r=>r.splice(i,1));t.fks=(t.fks||[]).filter(f=>!f.cols.some(c=>lc(c)===lc(st.col)));return {kind:'msg',msg:`Kolom ${st.col} dihapus dari ${t.name}.`,ddl:true}}
      if(st.act==='rename'){const k2=lc(st.to);if(db.tables[k2])throw new SqlError(`Tabel ${st.to} sudah ada.`);const old=t.name;delete db.tables[lc(old)];t.name=st.to;db.tables[k2]=t;
        Object.values(db.tables).forEach(x=>(x.fks||[]).forEach(f=>{if(lc(f.table)===lc(old))f.table=st.to}));return {kind:'msg',msg:`Tabel ${old} diganti nama menjadi ${st.to}.`,ddl:true}}
      if(st.act==='renamecol'){const i=colIx(t,st.from);if(i<0)throw new SqlError(`Kolom ${st.from} tidak ada.`);t.cols[i].name=st.to;return {kind:'msg',msg:`Kolom ${st.from} diganti nama menjadi ${st.to}.`,ddl:true}}
      if(st.act==='type'){const i=colIx(t,st.col);if(i<0)throw new SqlError(`Kolom ${st.col} tidak ada.`);t.cols[i].type=st.ty;t.rows.forEach(r=>r[i]=affinity(st.ty,r[i]));return {kind:'msg',msg:`Tipe kolom ${st.col} diubah menjadi ${st.ty}.`,ddl:true}}
      if(st.act==='addcons'){const k=st.cons;if(k.k==='check'){t.checks.push({e:k.e,cname:k.cname});try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){t.checks.pop();throw e}}
        else if(k.k==='unique'){t.uniques.push(k.cols);try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){t.uniques.pop();throw e}}
        else if(k.k==='fk'){t.fks.push({cols:k.cols,table:k.ref.table,refCols:k.ref.cols,onDelete:k.ref.onDelete});try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){t.fks.pop();throw e}}
        else throw new SqlError('Menambah PRIMARY KEY lewat ALTER tidak didukung.');
        return {kind:'msg',msg:`Constraint ditambahkan ke ${t.name}.`,ddl:true}}}
    case 'view':{const k=lc(st.name);if(db.tables[k])throw new SqlError(`Sudah ada tabel bernama ${st.name}.`);
      if(db.views[k]&&!st.replace){if(st.ine)return {kind:'msg',msg:'View sudah ada, dilewati.'};throw new SqlError(`View ${st.name} sudah ada.`,'Pakai CREATE OR REPLACE VIEW untuk mengubahnya.')}
      runQuery(st.q,ctx,null);const existed=!!db.views[k];db.views[k]={name:st.name,q:st.q,cols:st.cols,body:st.body};
      return {kind:'msg',msg:existed?`View ${st.name} diperbarui.`:`View ${st.name} dibuat. Pakai seperti tabel: SELECT * FROM ${st.name};`,ddl:true}}
    case 'index':{const k=lc(st.name);const t=getTable(db,st.table);if(db.indexes[k]){if(st.ine)return {kind:'msg',msg:'Index sudah ada, dilewati.'};throw new SqlError(`Index ${st.name} sudah ada.`)}
      st.cols.forEach(c=>{if(colIx(t,c)<0)throw new SqlError(`Kolom ${c} tidak ada di ${t.name}.`)});
      db.indexes[k]={name:st.name,table:t.name,cols:st.cols,unique:st.unique};
      if(st.unique){try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){delete db.indexes[k];throw new SqlError(`UNIQUE INDEX gagal dibuat: sudah ada nilai kembar di ${st.cols.join(', ')}.`)}}
      return {kind:'msg',msg:`Index ${st.name} dibuat pada ${t.name}(${st.cols.join(', ')}).`,ddl:true}}
    case 'begin':if(db.tx)throw new SqlError('Transaksi sudah berjalan.','Akhiri dulu dengan COMMIT atau ROLLBACK.');db.tx={snap:snap(db),sp:[]};return {kind:'msg',msg:'Transaksi dimulai. Perubahan berikutnya belum permanen sampai COMMIT.',tx:true};
    case 'commit':if(!db.tx)throw new SqlError('Tidak ada transaksi yang sedang berjalan.','Mulai dengan BEGIN.');db.tx=null;return {kind:'msg',msg:'COMMIT: semua perubahan dalam transaksi disimpan permanen.',tx:true};
    case 'rollback':{if(!db.tx)throw new SqlError('Tidak ada transaksi yang sedang berjalan.','Mulai dengan BEGIN.');
      if(st.to){const i=db.tx.sp.map(s=>lc(s.name)).lastIndexOf(lc(st.to));if(i<0)throw new SqlError(`Savepoint ${st.to} tidak ada.`);restore(db,db.tx.sp[i].snap);db.tx.sp=db.tx.sp.slice(0,i+1);return {kind:'msg',msg:`Kembali ke savepoint ${st.to}. Perubahan setelahnya dibatalkan, transaksi masih berjalan.`,tx:true}}
      restore(db,db.tx.snap);db.tx=null;return {kind:'msg',msg:'ROLLBACK: semua perubahan sejak BEGIN dibatalkan.',tx:true}}
    case 'savepoint':if(!db.tx){db.tx={snap:snap(db),sp:[]}}db.tx.sp.push({name:st.name,snap:snap(db)});return {kind:'msg',msg:`Savepoint ${st.name} dibuat.`,tx:true};
    case 'release':if(!db.tx)throw new SqlError('Tidak ada transaksi.');db.tx.sp=db.tx.sp.filter(s=>lc(s.name)!==lc(st.name));return {kind:'msg',msg:`Savepoint ${st.name} dilepas.`,tx:true};
    case 'grant':{getTable(db,st.obj);
      if(st.g==='GRANT'){st.privs.forEach(p=>{if(!db.grants.some(g=>g.who===st.who&&g.obj===st.obj&&g.p===p))db.grants.push({who:st.who,obj:st.obj,p})});return {kind:'msg',msg:`(Simulasi) Hak ${st.privs.join(', ')} pada ${st.obj} diberikan ke ${st.who}.`,grant:true}}
      db.grants=db.grants.filter(g=>!(g.who===st.who&&g.obj===st.obj&&(st.privs.includes(g.p)||st.privs.includes('ALL'))));return {kind:'msg',msg:`(Simulasi) Hak ${st.privs.join(', ')} pada ${st.obj} dicabut dari ${st.who}.`,grant:true}}
  }
  throw new SqlError('Perintah belum didukung.');
}
/* rencana eksekusi sederhana untuk EXPLAIN */
function plan(db,q){
  const out=[];const b=q.body;if(b.type!=='core'){out.push('COMPOUND QUERY');return out}
  const eqs=[];(function w(e){if(!e)return;if(e.op==='AND'){w(e.l);w(e.r);return}if(e.op==='cmp'&&e.o==='='){if(e.l.op==='col'&&e.r.op!=='col')eqs.push([e.l,'=']);else if(e.r.op==='col'&&e.l.op!=='col')eqs.push([e.r,'='])}
    if(e.op==='cmp'&&['<','>','<=','>='].includes(e.o)&&e.l.op==='col'&&e.r.op==='lit')eqs.push([e.l,'>']);if(e.op==='between'&&e.e.op==='col')eqs.push([e.e,'>'])})(b.where);
  const tables=[];(function w(f,on){if(!f)return;if(f.kind==='join'){w(f.l);w(f.r,f.on);return}tables.push({f,on})})(b.from);
  tables.forEach(({f,on},ti)=>{
    if(f.kind!=='table'){out.push('SCAN subquery');return}
    const t=db.tables[lc(f.name)];if(!t){out.push(`SCAN ${f.name}`);return}
    const al=lc(f.alias||f.name);const preds=[...eqs];
    if(on)(function w(e){if(!e)return;if(e.op==='AND'){w(e.l);w(e.r);return}if(e.op==='cmp'&&e.o==='='&&e.l.op==='col'&&e.r.op==='col'){[e.l,e.r].forEach(c=>{if(c.table&&lc(c.table)===al)preds.push([c,'='])})}})(on);
    const mine=preds.filter(([c])=>(!c.table||lc(c.table)===al)&&colIx(t,c.name)>=0);
    const pk=t.cols.find(c=>c.pk);
    let used=null;
    for(const [c,k] of mine){
      if(pk&&lc(pk.name)===lc(c.name)&&isIntPk(t,pk)&&k==='='){used=`SEARCH ${t.name} USING INTEGER PRIMARY KEY (${c.name}=?)`;break}
      const ix=Object.values(db.indexes).find(x=>lc(x.table)===lc(t.name)&&lc(x.cols[0])===lc(c.name));
      if(ix){used=`SEARCH ${t.name} USING INDEX ${ix.name} (${c.name}${k==='='?'=?':'>?'})`;if(k==='=')break}
    }
    out.push(used||`SCAN ${t.name}`+(ti>0?' (cek setiap baris untuk setiap baris tabel sebelumnya)':''));
  });
  if(b.group)out.push('USE TEMP B-TREE FOR GROUP BY');
  if(q.order){const oc=q.order[0].e;const ix=oc.op==='col'&&tables.length===1&&Object.values(db.indexes).find(x=>tables[0].f.kind==='table'&&lc(x.table)===lc(tables[0].f.name)&&lc(x.cols[0])===lc(oc.name));if(!ix)out.push('USE TEMP B-TREE FOR ORDER BY')}
  return out;
}

/* ---------- API publik ---------- */
function parse(sql){return new Parser(sql).all()}
function exec(db,sql,opt={}){
  const stmts=parse(sql);if(!stmts.length)throw new SqlError('Belum ada perintah untuk dijalankan.','Tulis query, misalnya SELECT * FROM produk;');
  const res=[];
  for(let i=0;i<stmts.length;i++){
    const st=stmts[i];const before=db.tx?null:snap(db);
    try{const r=execOne(db,st,{trace:opt.trace&&i===stmts.length-1});r.sql=st.sql;r.type=st.type;res.push(r)}
    catch(e){if(before)restore(db,before);if(e instanceof SqlError){e.stmt=i;e.sql=st.sql;e.done=res}throw e}
  }
  return res;
}
function create(seed){const db=newDb();if(seed)exec(db,seed);return db}
function schema(db){return Object.values(db.tables).map(t=>({name:t.name,rows:t.rows.length,cols:t.cols.map(c=>({name:c.name,type:c.type,pk:c.pk,fk:(t.fks||[]).find(f=>f.cols.some(x=>lc(x)===lc(c.name)))}))}))
  .concat(Object.values(db.views).map(v=>({name:v.name,view:true,cols:[]})))}
function clone(db){const c=newDb();restore(c,snap(db));return c}
return {exec,parse,create,schema,clone,fmt,SqlError,tokenize,snap,restore};
})();
if(typeof module!=='undefined')module.exports=SQLE;

/* ===================== DATABASE CONTOH =====================
   "Toko Nusantara": pelanggan, produk, pesanan, detail_pesanan, karyawan, rekening. */
const SEED={toko:`CREATE TABLE pelanggan (
  id INTEGER PRIMARY KEY,
  nama TEXT NOT NULL,
  kota TEXT,
  bergabung DATE
);
INSERT INTO pelanggan VALUES
 (1,'Andi','Jakarta','2023-01-15'),
 (2,'Budi','Bandung','2023-03-02'),
 (3,'Citra','Surabaya','2023-06-20'),
 (4,'Dewi','Jakarta','2024-01-08'),
 (5,'Eko','Medan','2024-02-14'),
 (6,'Fitri','Bandung','2024-05-30'),
 (7,'Gita',NULL,'2024-07-11'),
 (8,'Hadi','Yogyakarta','2024-09-03');
CREATE TABLE produk (
  id INTEGER PRIMARY KEY,
  nama TEXT NOT NULL,
  kategori TEXT NOT NULL,
  harga INTEGER CHECK (harga > 0),
  stok INTEGER DEFAULT 0
);
INSERT INTO produk VALUES
 (1,'Kopi Gayo','Minuman',85000,40),
 (2,'Teh Melati','Minuman',25000,120),
 (3,'Keripik Singkong','Camilan',15000,200),
 (4,'Kacang Mete','Camilan',60000,35),
 (5,'Sambal Bawang','Bumbu',30000,80),
 (6,'Madu Hutan','Minuman',120000,15),
 (7,'Rendang Kaleng','Makanan',75000,0),
 (8,'Kerupuk Udang','Camilan',20000,150);
CREATE TABLE pesanan (
  id INTEGER PRIMARY KEY,
  pelanggan_id INTEGER REFERENCES pelanggan(id),
  tanggal DATE NOT NULL,
  status TEXT DEFAULT 'baru'
);
INSERT INTO pesanan VALUES
 (101,1,'2024-10-01','selesai'),
 (102,2,'2024-10-03','selesai'),
 (103,1,'2024-10-07','dikirim'),
 (104,3,'2024-10-12','selesai'),
 (105,4,'2024-10-15','batal'),
 (106,2,'2024-10-20','selesai'),
 (107,6,'2024-11-02','dikirim'),
 (108,1,'2024-11-05','baru'),
 (109,5,'2024-11-09','selesai'),
 (110,8,'2024-11-15','baru');
CREATE TABLE detail_pesanan (
  pesanan_id INTEGER REFERENCES pesanan(id),
  produk_id INTEGER REFERENCES produk(id),
  jumlah INTEGER NOT NULL CHECK (jumlah > 0),
  PRIMARY KEY (pesanan_id, produk_id)
);
INSERT INTO detail_pesanan VALUES
 (101,1,2),(101,3,5),(102,2,3),(102,8,4),(103,6,1),(104,4,2),(104,3,3),(104,5,1),
 (105,1,1),(106,7,2),(106,2,2),(107,8,10),(108,1,1),(108,6,1),(109,5,6),(110,3,2);
CREATE TABLE karyawan (
  id INTEGER PRIMARY KEY,
  nama TEXT NOT NULL,
  jabatan TEXT,
  atasan_id INTEGER REFERENCES karyawan(id),
  divisi TEXT,
  gaji INTEGER
);
INSERT INTO karyawan VALUES
 (1,'Sari','Direktur',NULL,'Pusat',30000000),
 (2,'Tono','Manajer Gudang',1,'Gudang',15000000),
 (3,'Umi','Manajer Penjualan',1,'Penjualan',16000000),
 (4,'Vino','Staf Gudang',2,'Gudang',7000000),
 (5,'Wati','Staf Gudang',2,'Gudang',7500000),
 (6,'Yudi','Sales',3,'Penjualan',8000000),
 (7,'Zahra','Sales',3,'Penjualan',8500000),
 (8,'Rio','Sales',3,'Penjualan',8000000);
CREATE TABLE rekening (
  id INTEGER PRIMARY KEY,
  pemilik TEXT NOT NULL,
  saldo INTEGER NOT NULL CHECK (saldo >= 0)
);
INSERT INTO rekening VALUES (1,'Andi',500000),(2,'Budi',300000);`};

/* ===================== DATABASE CONTOH BI =====================
   Skema bintang (star schema) penjualan Toko Nusantara Januari-Juni 2024:
   satu tabel fakta dan tiga dimensi. Dibuat dengan skrip ber-seed tetap. */
SEED.bi=`CREATE TABLE dim_produk (
  produk_id INTEGER PRIMARY KEY,
  nama TEXT,
  kategori TEXT,
  hpp INTEGER,
  harga INTEGER
);
INSERT INTO dim_produk VALUES
 (1,'Kopi Gayo','Minuman',52000,85000),
 (2,'Teh Melati','Minuman',14000,25000),
 (3,'Keripik Singkong','Camilan',8000,15000),
 (4,'Kacang Mete','Camilan',38000,60000),
 (5,'Sambal Bawang','Bumbu',17000,30000),
 (6,'Madu Hutan','Minuman',78000,120000);
CREATE TABLE dim_toko (
  toko_id INTEGER PRIMARY KEY,
  nama TEXT,
  kota TEXT,
  wilayah TEXT
);
INSERT INTO dim_toko VALUES
 (1,'Toko Sudirman','Jakarta','Jawa'),
 (2,'Toko Dago','Bandung','Jawa'),
 (3,'Toko Tunjungan','Surabaya','Jawa'),
 (4,'Toko Kesawan','Medan','Sumatra'),
 (5,'Online','Nasional','Online');
CREATE TABLE dim_tanggal (
  tanggal_id INTEGER PRIMARY KEY,
  tanggal DATE,
  tahun INTEGER,
  bulan INTEGER,
  nama_bulan TEXT,
  kuartal INTEGER,
  hari TEXT
);
INSERT INTO dim_tanggal VALUES
 (20240105,'2024-01-05',2024,1,'Jan',1,'Jumat'),
 (20240115,'2024-01-15',2024,1,'Jan',1,'Senin'),
 (20240125,'2024-01-25',2024,1,'Jan',1,'Kamis'),
 (20240205,'2024-02-05',2024,2,'Feb',1,'Senin'),
 (20240215,'2024-02-15',2024,2,'Feb',1,'Kamis'),
 (20240225,'2024-02-25',2024,2,'Feb',1,'Minggu'),
 (20240305,'2024-03-05',2024,3,'Mar',1,'Selasa'),
 (20240315,'2024-03-15',2024,3,'Mar',1,'Jumat'),
 (20240325,'2024-03-25',2024,3,'Mar',1,'Senin'),
 (20240405,'2024-04-05',2024,4,'Apr',2,'Jumat'),
 (20240415,'2024-04-15',2024,4,'Apr',2,'Senin'),
 (20240425,'2024-04-25',2024,4,'Apr',2,'Kamis'),
 (20240505,'2024-05-05',2024,5,'May',2,'Minggu'),
 (20240515,'2024-05-15',2024,5,'May',2,'Rabu'),
 (20240525,'2024-05-25',2024,5,'May',2,'Sabtu'),
 (20240605,'2024-06-05',2024,6,'Jun',2,'Rabu'),
 (20240615,'2024-06-15',2024,6,'Jun',2,'Sabtu'),
 (20240625,'2024-06-25',2024,6,'Jun',2,'Selasa');
CREATE TABLE fakta_penjualan (
  id INTEGER PRIMARY KEY,
  tanggal_id INTEGER REFERENCES dim_tanggal(tanggal_id),
  produk_id INTEGER REFERENCES dim_produk(produk_id),
  toko_id INTEGER REFERENCES dim_toko(toko_id),
  jumlah INTEGER,
  harga INTEGER,
  diskon_persen INTEGER
);
INSERT INTO fakta_penjualan VALUES
 (1,20240105,3,1,11,15000,0),
 (2,20240105,2,1,2,25000,10),
 (3,20240105,4,1,2,60000,0),
 (4,20240105,5,2,1,30000,0),
 (5,20240105,1,2,8,85000,5),
 (6,20240105,2,2,2,25000,0),
 (7,20240105,1,3,2,85000,10),
 (8,20240105,5,3,2,30000,0),
 (9,20240105,4,3,11,60000,10),
 (10,20240105,1,4,2,85000,0),
 (11,20240105,5,4,1,30000,10),
 (12,20240105,4,4,3,60000,0),
 (13,20240105,4,5,20,60000,0),
 (14,20240105,2,5,18,25000,0),
 (15,20240105,1,5,5,85000,10),
 (16,20240115,5,1,2,30000,10),
 (17,20240115,2,1,12,25000,0),
 (18,20240115,3,1,10,15000,0),
 (19,20240115,5,2,11,30000,10),
 (20,20240115,2,2,7,25000,0),
 (21,20240115,4,2,8,60000,10),
 (22,20240115,4,3,4,60000,0),
 (23,20240115,3,3,12,15000,0),
 (24,20240115,5,3,2,30000,10),
 (25,20240115,3,4,6,15000,5),
 (26,20240115,5,4,5,30000,10),
 (27,20240115,4,4,2,60000,0),
 (28,20240115,5,5,12,30000,0),
 (29,20240115,4,5,16,60000,5),
 (30,20240115,2,5,2,25000,0),
 (31,20240125,5,1,6,30000,0),
 (32,20240125,6,1,10,120000,5),
 (33,20240125,3,1,10,15000,5),
 (34,20240125,1,2,9,85000,0),
 (35,20240125,6,2,1,120000,0),
 (36,20240125,3,2,11,15000,10),
 (37,20240125,6,3,12,120000,5),
 (38,20240125,4,3,11,60000,0),
 (39,20240125,3,3,1,15000,5),
 (40,20240125,3,4,8,15000,0),
 (41,20240125,2,4,4,25000,0),
 (42,20240125,1,4,4,85000,0),
 (43,20240125,4,5,4,60000,0),
 (44,20240125,6,5,16,120000,5),
 (45,20240125,5,5,18,30000,0),
 (46,20240205,2,1,12,25000,5),
 (47,20240205,4,1,6,60000,5),
 (48,20240205,3,1,4,15000,0),
 (49,20240205,1,2,6,85000,0),
 (50,20240205,2,2,1,25000,5),
 (51,20240205,5,2,10,30000,0),
 (52,20240205,3,3,3,15000,5),
 (53,20240205,6,3,9,120000,0),
 (54,20240205,1,3,12,85000,10),
 (55,20240205,3,4,8,15000,10),
 (56,20240205,2,4,7,25000,5),
 (57,20240205,1,4,9,85000,5),
 (58,20240205,1,5,4,85000,0),
 (59,20240205,4,5,4,60000,0),
 (60,20240205,5,5,16,30000,0),
 (61,20240215,1,1,4,85000,0),
 (62,20240215,3,1,10,15000,0),
 (63,20240215,6,1,9,120000,0),
 (64,20240215,3,2,2,15000,0),
 (65,20240215,5,2,10,30000,5),
 (66,20240215,1,2,5,85000,0),
 (67,20240215,3,3,8,15000,0),
 (68,20240215,5,3,2,30000,5),
 (69,20240215,6,3,8,120000,5),
 (70,20240215,4,4,3,60000,0),
 (71,20240215,3,4,12,15000,0),
 (72,20240215,1,4,14,85000,0),
 (73,20240215,4,5,8,60000,10),
 (74,20240215,2,5,12,25000,0),
 (75,20240215,1,5,26,85000,10),
 (76,20240225,1,1,13,85000,0),
 (77,20240225,5,1,12,30000,0),
 (78,20240225,3,1,9,15000,0),
 (79,20240225,2,2,9,25000,10),
 (80,20240225,3,2,9,15000,0),
 (81,20240225,6,2,11,120000,0),
 (82,20240225,5,3,7,30000,0),
 (83,20240225,2,3,4,25000,10),
 (84,20240225,6,3,8,120000,0),
 (85,20240225,6,4,5,120000,5),
 (86,20240225,1,4,7,85000,0),
 (87,20240225,5,4,12,30000,10),
 (88,20240225,3,5,12,15000,0),
 (89,20240225,4,5,8,60000,0),
 (90,20240225,6,5,8,120000,5),
 (91,20240305,2,1,8,25000,10),
 (92,20240305,3,1,10,15000,0),
 (93,20240305,6,1,8,120000,0),
 (94,20240305,6,2,7,120000,0),
 (95,20240305,1,2,11,85000,0),
 (96,20240305,5,2,7,30000,0),
 (97,20240305,1,3,10,85000,0),
 (98,20240305,4,3,12,60000,0),
 (99,20240305,5,3,3,30000,0),
 (100,20240305,1,4,14,85000,0),
 (101,20240305,2,4,10,25000,10),
 (102,20240305,4,4,8,60000,0),
 (103,20240305,2,5,2,25000,0),
 (104,20240305,5,5,24,30000,0),
 (105,20240305,6,5,18,120000,0),
 (106,20240315,4,1,1,60000,0),
 (107,20240315,2,1,4,25000,0),
 (108,20240315,5,1,9,30000,0),
 (109,20240315,5,2,9,30000,5),
 (110,20240315,3,2,3,15000,0),
 (111,20240315,6,2,12,120000,0),
 (112,20240315,4,3,9,60000,0),
 (113,20240315,5,3,9,30000,0),
 (114,20240315,6,3,9,120000,10),
 (115,20240315,1,4,13,85000,0),
 (116,20240315,4,4,3,60000,0),
 (117,20240315,2,4,3,25000,5),
 (118,20240315,5,5,12,30000,10),
 (119,20240315,1,5,21,85000,10),
 (120,20240315,6,5,16,120000,0),
 (121,20240325,5,1,4,30000,0),
 (122,20240325,1,1,4,85000,0),
 (123,20240325,2,1,9,25000,5),
 (124,20240325,5,2,8,30000,0),
 (125,20240325,1,2,13,85000,10),
 (126,20240325,6,2,10,120000,10),
 (127,20240325,2,3,9,25000,10),
 (128,20240325,3,3,8,15000,10),
 (129,20240325,4,3,4,60000,10),
 (130,20240325,3,4,8,15000,0),
 (131,20240325,5,4,7,30000,0),
 (132,20240325,2,4,7,25000,5),
 (133,20240325,3,5,14,15000,0),
 (134,20240325,1,5,11,85000,0),
 (135,20240325,2,5,4,25000,0),
 (136,20240405,6,1,5,120000,0),
 (137,20240405,3,1,8,15000,0),
 (138,20240405,2,1,12,25000,0),
 (139,20240405,4,2,11,60000,0),
 (140,20240405,6,2,3,120000,5),
 (141,20240405,2,2,9,25000,5),
 (142,20240405,3,3,6,15000,0),
 (143,20240405,4,3,2,60000,0),
 (144,20240405,2,3,1,25000,0),
 (145,20240405,5,4,12,30000,0),
 (146,20240405,4,4,7,60000,0),
 (147,20240405,6,4,9,120000,10),
 (148,20240405,3,5,4,15000,0),
 (149,20240405,5,5,4,30000,0),
 (150,20240405,1,5,14,85000,0),
 (151,20240415,1,1,7,85000,5),
 (152,20240415,2,1,11,25000,0),
 (153,20240415,3,1,7,15000,0),
 (154,20240415,5,2,12,30000,0),
 (155,20240415,6,2,2,120000,0),
 (156,20240415,4,2,1,60000,0),
 (157,20240415,4,3,1,60000,0),
 (158,20240415,1,3,9,85000,0),
 (159,20240415,3,3,10,15000,0),
 (160,20240415,1,4,12,85000,0),
 (161,20240415,3,4,6,15000,10),
 (162,20240415,6,4,7,120000,0),
 (163,20240415,5,5,18,30000,0),
 (164,20240415,2,5,4,25000,0),
 (165,20240415,1,5,14,85000,0),
 (166,20240425,2,1,11,25000,0),
 (167,20240425,6,1,9,120000,0),
 (168,20240425,3,1,5,15000,5),
 (169,20240425,5,2,6,30000,0),
 (170,20240425,2,2,5,25000,0),
 (171,20240425,3,2,1,15000,0),
 (172,20240425,6,3,9,120000,5),
 (173,20240425,5,3,4,30000,5),
 (174,20240425,2,3,2,25000,5),
 (175,20240425,6,4,9,120000,0),
 (176,20240425,4,4,12,60000,0),
 (177,20240425,5,4,4,30000,0),
 (178,20240425,2,5,12,25000,0),
 (179,20240425,6,5,6,120000,0),
 (180,20240425,4,5,4,60000,0),
 (181,20240505,4,1,2,60000,5),
 (182,20240505,2,1,9,25000,0),
 (183,20240505,1,1,15,85000,0),
 (184,20240505,6,2,8,120000,0),
 (185,20240505,3,2,3,15000,0),
 (186,20240505,1,2,13,85000,0),
 (187,20240505,3,3,9,15000,0),
 (188,20240505,6,3,4,120000,0),
 (189,20240505,5,3,5,30000,0),
 (190,20240505,3,4,6,15000,5),
 (191,20240505,2,4,2,25000,5),
 (192,20240505,1,4,10,85000,10),
 (193,20240505,6,5,18,120000,0),
 (194,20240505,2,5,4,25000,0),
 (195,20240505,5,5,4,30000,0),
 (196,20240515,4,1,7,60000,0),
 (197,20240515,5,1,5,30000,0),
 (198,20240515,1,1,16,85000,0),
 (199,20240515,1,2,16,85000,10),
 (200,20240515,5,2,7,30000,0),
 (201,20240515,2,2,12,25000,5),
 (202,20240515,2,3,1,25000,10),
 (203,20240515,3,3,11,15000,5),
 (204,20240515,6,3,12,120000,10),
 (205,20240515,2,4,11,25000,10),
 (206,20240515,5,4,12,30000,0),
 (207,20240515,1,4,7,85000,0),
 (208,20240515,1,5,9,85000,5),
 (209,20240515,2,5,16,25000,10),
 (210,20240515,3,5,2,15000,0),
 (211,20240525,6,1,8,120000,0),
 (212,20240525,5,1,1,30000,5),
 (213,20240525,2,1,2,25000,10),
 (214,20240525,5,2,12,30000,5),
 (215,20240525,1,2,10,85000,0),
 (216,20240525,6,2,5,120000,0),
 (217,20240525,6,3,12,120000,5),
 (218,20240525,2,3,8,25000,5),
 (219,20240525,5,3,2,30000,5),
 (220,20240525,6,4,10,120000,0),
 (221,20240525,3,4,2,15000,10),
 (222,20240525,1,4,8,85000,0),
 (223,20240525,3,5,2,15000,5),
 (224,20240525,6,5,2,120000,5),
 (225,20240525,2,5,10,25000,0),
 (226,20240605,6,1,5,120000,10),
 (227,20240605,2,1,5,25000,5),
 (228,20240605,4,1,8,60000,5),
 (229,20240605,1,2,11,85000,0),
 (230,20240605,5,2,8,30000,0),
 (231,20240605,2,2,5,25000,5),
 (232,20240605,1,3,11,85000,5),
 (233,20240605,5,3,4,30000,0),
 (234,20240605,4,3,2,60000,10),
 (235,20240605,1,4,12,85000,0),
 (236,20240605,2,4,10,25000,10),
 (237,20240605,3,4,5,15000,0),
 (238,20240605,6,5,16,120000,5),
 (239,20240605,3,5,14,15000,0),
 (240,20240605,2,5,6,25000,0),
 (241,20240615,4,1,5,60000,0),
 (242,20240615,6,1,7,120000,0),
 (243,20240615,5,1,7,30000,0),
 (244,20240615,1,2,12,85000,0),
 (245,20240615,3,2,7,15000,0),
 (246,20240615,6,2,4,120000,0),
 (247,20240615,6,3,6,120000,0),
 (248,20240615,3,3,7,15000,5),
 (249,20240615,5,3,10,30000,0),
 (250,20240615,3,4,1,15000,0),
 (251,20240615,4,4,2,60000,0),
 (252,20240615,6,4,11,120000,0),
 (253,20240615,6,5,10,120000,5),
 (254,20240615,2,5,18,25000,0),
 (255,20240615,5,5,8,30000,0),
 (256,20240625,4,1,9,60000,10),
 (257,20240625,1,1,10,85000,0),
 (258,20240625,6,1,1,120000,5),
 (259,20240625,4,2,11,60000,0),
 (260,20240625,5,2,8,30000,0),
 (261,20240625,2,2,9,25000,0),
 (262,20240625,2,3,6,25000,0),
 (263,20240625,4,3,5,60000,0),
 (264,20240625,5,3,12,30000,0),
 (265,20240625,4,4,8,60000,10),
 (266,20240625,2,4,11,25000,5),
 (267,20240625,3,4,2,15000,0),
 (268,20240625,6,5,8,120000,10),
 (269,20240625,2,5,16,25000,10),
 (270,20240625,1,5,14,85000,5),
 (271,20240105,1,2,8,85000,5),
 (272,20240615,1,4,3,80000,0);
`;
SEED.kosong='';

/* ===================== VISUALISASI v2 =====================
   Dipakai pelajaran jalur (c dan s). Setiap fungsi: VIZ2[nama](host, {lang, lesson}).
   Animasi memakai FLIP (posisi lama -> baru) dan menghormati prefers-reduced-motion. */
const RM=()=>{try{return matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){return false}};
let VUID=0;
function flip(root,render){
  const pos=new Map();
  root.querySelectorAll('[data-key]').forEach(e=>pos.set(e.dataset.key,e.getBoundingClientRect()));
  render();
  if(RM()||!pos.size)return;
  root.querySelectorAll('[data-key]').forEach(e=>{
    const p=pos.get(e.dataset.key),r=e.getBoundingClientRect();
    if(!e.animate)return;
    if(p){const dx=p.left-r.left,dy=p.top-r.top;if(Math.abs(dx)>1||Math.abs(dy)>1)e.animate([{transform:`translate(${dx}px,${dy}px)`},{transform:'none'}],{duration:520,easing:'cubic-bezier(.2,.75,.2,1)'})}
    else e.animate([{opacity:0,transform:'translateY(8px)'},{opacity:1,transform:'none'}],{duration:360,easing:'ease-out'});
  });
}
const fv=v=>v==null?'<i class="nul">NULL</i>':esc(SQLE.fmt(v));
const rupiah=n=>'Rp'+Number(n).toLocaleString('id-ID');
function rtable(cols,rows,o={}){
  const max=o.max||40,shown=rows.slice(0,max);
  return `<div class="rt"><table><thead><tr>${o.lead?`<th class="lead">${o.lead===true?'':esc(o.lead)}</th>`:''}${cols.map((c,i)=>`<th class="${o.colCls?o.colCls(i):''}">${esc(c)}</th>`).join('')}</tr></thead><tbody>${shown.map(r=>`<tr ${r.k!=null?`data-key="${r.k}"`:''} class="${r.cls||''}">${o.lead?`<td class="lead">${r.tag||''}</td>`:''}${r.v.map((x,i)=>`<td class="${r.cc?r.cc(i):''}">${r.raw?x:fv(x)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>${rows.length>max?`<p class="v-more">… dan ${rows.length-max} baris lagi</p>`:''}`;
}
const LBL={java:{t:'Java'},python:{t:'Python'}};

/* ---------- pipeline query: urutan logis eksekusi SELECT ---------- */
const CLAUSES=['FROM','WHERE','GROUP BY','HAVING','SELECT','DISTINCT','ORDER BY','LIMIT'];
function pipeFrames(db,sql){
  let res;
  try{res=SQLE.exec(SQLE.clone(db),sql,{trace:true})}catch(e){return {err:e.message}}
  const last=res[res.length-1],t=last&&last.trace;
  if(!t||!t.from||!t.select)return {err:'Penjelasan langkah tersedia untuk satu query SELECT (tanpa UNION). Jalankan query SELECT lalu coba lagi.'};
  const F=[],fr=t.from,cols=fr.cols,all=fr.rows.map((v,i)=>({k:'f'+i,v}));
  const tb=fr.tables.join(', ');
  F.push({c:'FROM',cols,rows:all,note:t.join
    ?`<b>FROM + ${t.join.comma?'CROSS':t.join.type} JOIN</b> memasangkan baris ${esc(t.join.left.label)} dengan ${esc(t.join.right.label)}. Hasilnya ${fr.rows.length} baris gabungan. Sel <i class="nul">NULL</i> berarti tidak ada pasangan.`
    :`<b>FROM ${esc(tb)}</b> dijalankan paling awal: database mengambil semua ${fr.rows.length} baris dari tabel.`});
  let kept=fr.rows.map((_,i)=>i);
  if(t.where){const K=t.where.keep,n=K.filter(Boolean).length;
    F.push({c:'WHERE',cols,rows:all.map((r,i)=>({...r,cls:K[i]?'keep':'drop'})),note:`<b>WHERE</b> memeriksa kondisi pada setiap baris. ${n} baris lolos (hijau), ${K.length-n} baris dibuang (dicoret).`});
    kept=kept.filter(i=>K[i]);
    F.push({c:'WHERE',cols,rows:kept.map(i=>all[i]),note:`Tersisa ${kept.length} baris. Semua langkah berikutnya hanya melihat baris ini.`});
  }
  const S=t.select;let sk=null;
  if(t.group){const G=t.group.groups;
    const rows=G.flatMap((g,gi)=>g.idx.map((i,j)=>({k:'f'+i,v:fr.rows[i],cls:'g'+(gi%6),tag:j===0?esc(g.label||'(semua)'):''})));
    F.push({c:'GROUP BY',cols,rows,lead:'kelompok',note:`<b>GROUP BY</b> menyusun baris dengan nilai yang sama ke dalam ${G.length} kelompok. Satu kelompok nanti menjadi satu baris hasil.`});
    let gk=G.map((_,i)=>i);
    if(t.having){const K=t.having.keep;
      F.push({c:'HAVING',cols,lead:'kelompok',rows:rows.map(r=>{const gi=G.findIndex(g=>g.idx.includes(+r.k.slice(1)));return {...r,cls:r.cls+' '+(K[gi]?'keep':'drop')}}),
        note:`<b>HAVING</b> menyaring kelompok, bukan baris. ${K.filter(Boolean).length} kelompok lolos. Di sinilah syarat dengan COUNT, SUM, atau AVG ditulis.`});
      gk=gk.filter(i=>K[i]);}
    sk=gk.map(i=>G[i].idx.length?'f'+G[i].idx[0]:'s'+i);
  }else sk=kept.map(i=>'f'+i);
  if(sk.length!==S.rows.length)sk=S.rows.map((_,i)=>'s'+i);
  F.push({c:'SELECT',cols:S.cols,rows:S.rows.map((v,i)=>({k:sk[i],v})),note:t.group
    ?`<b>SELECT</b> menghitung kolom untuk setiap kelompok, misalnya COUNT atau SUM. Alias dengan AS baru lahir di sini.`
    :`<b>SELECT</b> memilih dan menghitung kolom yang diminta: ${S.cols.map(esc).join(', ')}.`});
  let idx=S.rows.map((_,i)=>i);
  if(t.distinct){const K=t.distinct.keep;
    F.push({c:'DISTINCT',cols:S.cols,rows:idx.map(i=>({k:sk[i],v:S.rows[i],cls:K[i]?'keep':'drop'})),note:`<b>DISTINCT</b> membuang baris kembar. ${K.filter(x=>!x).length} baris duplikat dicoret.`});
    idx=idx.filter(i=>K[i]);}
  if(t.order){idx=t.order.idx;
    F.push({c:'ORDER BY',cols:S.cols,rows:idx.map(i=>({k:sk[i],v:S.rows[i]})),note:`<b>ORDER BY</b> mengurutkan hasil. Karena dijalankan setelah SELECT, ORDER BY boleh memakai alias kolom.`});}
  if(t.limit){const L=t.limit;
    F.push({c:'LIMIT',cols:S.cols,rows:idx.map((i,j)=>({k:sk[i],v:S.rows[i],cls:j>=L.offset&&j<L.offset+L.n?'keep':'drop'})),note:`<b>LIMIT${L.offset?' / OFFSET':''}</b> mengambil ${L.n} baris${L.offset?` setelah melewati ${L.offset} baris`:' teratas'} dari ${L.from} baris.`});
    idx=idx.slice(L.offset,L.offset+L.n);
    F.push({c:'LIMIT',cols:S.cols,rows:idx.map(i=>({k:sk[i],v:S.rows[i]})),note:`Hasil akhir: ${idx.length} baris.`});}
  else F[F.length-1].note+=` Hasil akhir: ${idx.length} baris.`;
  return {F};
}
function sqlPipeline(host,db,sql){
  const p=pipeFrames(db,sql);
  if(p.err){host.innerHTML=`<p class="v-err">${esc(p.err)}</p>`;return}
  const order=CLAUSES.filter(c=>p.F.some(f=>f.c===c));
  player(host,p.F,(st,f)=>flip(st,()=>{const ci=order.indexOf(f.c);
    st.innerHTML=`<div class="v-pipe" aria-label="Urutan eksekusi">${order.map((c,i)=>`<span class="${i===ci?'cur':i<ci?'done':''}">${c}</span>`).join('<i aria-hidden="true">›</i>')}</div>${rtable(f.cols,f.rows,{lead:f.lead})}`}),{speed:1700});
}

/* ---------- JOIN ---------- */
function venn(type,ln,rn){
  const id='vc'+(++VUID),L=type==='LEFT'||type==='FULL',R=type==='RIGHT'||type==='FULL';
  return `<svg class="venn" viewBox="0 0 160 84" role="img" aria-label="Diagram ${type} JOIN"><defs><clipPath id="${id}"><circle cx="62" cy="42" r="30"/></clipPath></defs>
   <circle cx="62" cy="42" r="30" class="${L?'on':''}"/><circle cx="98" cy="42" r="30" class="${R?'on':''}"/>
   <circle cx="98" cy="42" r="30" clip-path="url(#${id})" class="on"/>
   <circle cx="62" cy="42" r="30" class="ln"/><circle cx="98" cy="42" r="30" class="ln"/>
   <text x="20" y="80">${ln}</text><text x="140" y="80" text-anchor="end">${rn}</text></svg>`;
}
function joinViz(host,mode){
  const self=mode==='SELF';
  const C=self?{L:'karyawan',la:'k',R:'karyawan',ra:'a',on:'k.atasan_id = a.id',lc:[0,1,3],rc:[0,1],sel:'k.nama AS karyawan, a.nama AS atasan',ln:'k (karyawan)',rn:'a (atasan)',res:['karyawan','atasan'],li:1,ri:1}
               :{L:'pelanggan',la:'p',R:'pesanan',ra:'s',on:'s.pelanggan_id = p.id',lc:[0,1],rc:[0,1],sel:'p.nama, s.id AS pesanan',ln:'pelanggan',rn:'pesanan',res:['nama','pesanan'],li:1,ri:0};
  const types=self?['INNER','LEFT']:['INNER','LEFT','RIGHT','FULL'];
  let type=mode==='LEFT'?'LEFT':'INNER';
  const db=SQLE.create(SEED.toko);
  host.innerHTML=`<div class="v-jhead"><div class="seg" role="group" aria-label="Jenis JOIN">${types.map(t=>`<button data-t="${t}" aria-pressed="${t===type}">${t}</button>`).join('')}</div><div class="v-jven"></div></div><pre class="code v-q"></pre><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function build(){
    host.querySelectorAll('[data-t]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.t===type));
    $('.v-jven',host).innerHTML=venn(type,C.ln,C.rn);
    const q=`SELECT ${C.sel}\nFROM ${C.L} ${C.la}\n${type} JOIN ${C.R} ${C.ra} ON ${C.on};`;
    $('.v-q',host).innerHTML=hl(q,'sql');
    const r=SQLE.exec(db,q,{trace:true})[0],j=r.trace.join,pairs=j.pairs;
    const frames=[{li:-1,upto:0,note:`Kiri: tabel <b>${esc(C.ln)}</b>. Kanan: <b>${esc(C.rn)}</b>. JOIN akan mencocokkan setiap baris kiri dengan baris kanan yang memenuhi <code>${esc(C.on)}</code>.`}];
    let n=0;
    j.left.rows.forEach((_,i)=>{const mine=pairs.map((p,k)=>[p,k]).filter(([p])=>p[0]===i);if(!mine.length)return;n+=mine.length;
      const miss=mine[0][0][1]==null;
      frames.push({li:i,ri:mine.map(([p])=>p[1]).filter(x=>x!=null),upto:n,note:miss
        ?`<b>${esc(j.left.rows[i][C.li])}</b> tidak punya pasangan. ${type==='LEFT'||type==='FULL'?`Karena ${type} JOIN, baris ini tetap masuk dengan kolom kanan berisi NULL.`:''}`
        :`<b>${esc(j.left.rows[i][C.li])}</b> cocok dengan ${mine.length} baris kanan, jadi menghasilkan ${mine.length} baris.`})});
    const skipped=j.left.rows.map((_,i)=>i).filter(i=>!pairs.some(p=>p[0]===i));
    if(skipped.length&&type!=='LEFT'&&type!=='FULL')frames.push({li:-1,miss:skipped,upto:n,note:`${skipped.map(i=>esc(j.left.rows[i][C.li])).join(', ')} tidak punya pasangan, jadi <b>dibuang</b> oleh ${type} JOIN.`});
    const ro=pairs.map((p,k)=>[p,k]).filter(([p])=>p[0]==null);
    if(ro.length){n+=ro.length;frames.push({li:-1,ri:ro.map(([p])=>p[1]),upto:n,note:`Baris kanan tanpa pasangan ikut masuk karena ${type} JOIN; kolom kiri berisi NULL.`})}
    frames[frames.length-1].note+=` Total ${r.rows.length} baris.`;
    const draw=(st,f)=>{
      const lrow=(v,i)=>`<li data-i="${i}" class="${f.li===i?'cur':''} ${f.miss&&f.miss.includes(i)?'miss':''} ${pairs.slice(0,f.upto).some(p=>p[0]===i)?'used':''}">${C.lc.map(c=>`<span>${fv(v[c])}</span>`).join('')}</li>`;
      const rrow=(v,i)=>`<li data-i="${i}" class="${f.ri&&f.ri.includes(i)?'cur':''} ${pairs.slice(0,f.upto).some(p=>p[1]===i)?'used':''}">${C.rc.map(c=>`<span>${fv(v[c])}</span>`).join('')}</li>`;
      st.innerHTML=`<div class="v-jn"><div><div class="v-cap">${esc(C.ln)} <small>${C.lc.map(c=>j.left.cols[c]).join(' · ')}</small></div><ol class="v-jl">${j.left.rows.map(lrow).join('')}</ol></div><svg class="v-jsvg" aria-hidden="true"></svg>
        <div><div class="v-cap">${esc(C.rn)} <small>${C.rc.map(c=>j.right.cols[c]).join(' · ')}</small></div><ol class="v-jl r">${j.right.rows.map(rrow).join('')}</ol></div></div>
        <div class="v-cap">Hasil (${f.upto} baris)</div>${rtable(C.res,r.rows.slice(0,f.upto).map((v,i)=>({k:'r'+i,v,cls:i>=f.upto-(f.ri?f.ri.length:0)-(f.li>=0?0:0)?'':''})),{max:30})}`;
      requestAnimationFrame(()=>lines(st,f));
    };
    function lines(st,f){
      const box=$('.v-jn',st);if(!box)return;const svg=$('.v-jsvg',st),B=box.getBoundingClientRect(),S=svg.getBoundingClientRect();
      const L=[...st.querySelectorAll('.v-jl:not(.r) li')],Rr=[...st.querySelectorAll('.v-jl.r li')];
      let h='';
      pairs.slice(0,f.upto).forEach(([a,b],k)=>{if(a==null||b==null)return;const A=L[a].getBoundingClientRect(),Z=Rr[b].getBoundingClientRect();
        const y1=A.top+A.height/2-S.top,y2=Z.top+Z.height/2-S.top,w=S.width;const cur=f.li===a;
        h+=`<path d="M0 ${y1} C ${w*.5} ${y1}, ${w*.5} ${y2}, ${w} ${y2}" class="${cur?'cur':''}" pathLength="1"/>`});
      svg.setAttribute('viewBox',`0 0 ${S.width} ${S.height}`);svg.innerHTML=h;
    }
    if(!P)P=player(pl,frames,draw,{speed:1300});else P.set(frames);
    P._d=draw;
  }
  host.addEventListener('click',e=>{const b=e.target.closest('[data-t]');if(!b)return;type=b.dataset.t;P=null;pl.innerHTML='';build()});
  build();
}

/* ---------- diagram ER Toko Nusantara ---------- */
function erViz(host){
  const db=SQLE.create(SEED.toko),sc=SQLE.schema(db);const T=Object.fromEntries(sc.map(t=>[t.name,t]));
  const POS={pelanggan:[10,16],pesanan:[262,16],detail_pesanan:[514,16],produk:[514,196],karyawan:[10,196],rekening:[262,216]};
  const W=196,RH=19,HH=28;
  const rowY=(t,c)=>POS[t][1]+HH+RH*T[t].cols.findIndex(x=>x.name===c)+RH/2;
  const REL=[
    {id:'r1',a:'pelanggan',b:'pesanan',d:`M ${10+W} ${rowY('pelanggan','id')} C 240 ${rowY('pelanggan','id')}, 236 ${rowY('pesanan','pelanggan_id')}, 262 ${rowY('pesanan','pelanggan_id')}`,
      note:'<b>pelanggan 1 — N pesanan.</b> Satu pelanggan bisa punya banyak pesanan. Kolom <code>pesanan.pelanggan_id</code> adalah foreign key yang menunjuk <code>pelanggan.id</code>.'},
    {id:'r2',a:'pesanan',b:'detail_pesanan',d:`M ${262+W} ${rowY('pesanan','id')} C 490 ${rowY('pesanan','id')}, 488 ${rowY('detail_pesanan','pesanan_id')}, 514 ${rowY('detail_pesanan','pesanan_id')}`,
      note:'<b>pesanan 1 — N detail_pesanan.</b> Satu pesanan berisi beberapa baris barang.'},
    {id:'r3',a:'produk',b:'detail_pesanan',d:`M 514 ${rowY('detail_pesanan','produk_id')} L 496 ${rowY('detail_pesanan','produk_id')} L 496 ${rowY('produk','id')} L 514 ${rowY('produk','id')}`,
      note:'<b>produk 1 — N detail_pesanan.</b> Tabel detail_pesanan adalah <i>tabel penghubung</i>: ia memecah hubungan banyak-ke-banyak antara pesanan dan produk. Primary key-nya gabungan (pesanan_id, produk_id).'},
    {id:'r4',a:'karyawan',b:'karyawan',d:`M ${10+W} ${rowY('karyawan','atasan_id')} C 236 ${rowY('karyawan','atasan_id')}, 236 ${rowY('karyawan','id')}, ${10+W} ${rowY('karyawan','id')}`,
      note:'<b>karyawan → karyawan.</b> Relasi ke diri sendiri: <code>atasan_id</code> menunjuk karyawan lain. Inilah bahan SELF JOIN dan CTE rekursif.'}];
  const frames=[{note:'Diagram ER (Entity Relationship) Toko Nusantara. Setiap kotak adalah tabel; 🔑 primary key, 🔗 foreign key. Tekan Berikutnya untuk menelusuri relasinya.'},...REL.map(r=>({r:r.id,note:r.note})),
    {r:'x',note:'<b>rekening</b> berdiri sendiri, tanpa relasi. Tabel ini dipakai untuk latihan transaksi.'}];
  player(host,frames,(st,f)=>{
    const act=REL.find(r=>r.id===f.r),on=t=>f.r==='x'?t==='rekening':act?(act.a===t||act.b===t):true;
    st.innerHTML=`<div class="v-er"><svg viewBox="0 0 720 340" role="img" aria-label="Diagram ER">
     ${REL.map(r=>`<path d="${r.d}" class="rel ${f.r===r.id?'cur':''} ${f.r&&f.r!==r.id?'dim':''}"/>`).join('')}
     ${Object.entries(POS).map(([t,[x,y]])=>{const tb=T[t],h=HH+RH*tb.cols.length;return `<g class="ent ${on(t)?'':'dim'} ${act&&on(t)||f.r==='x'&&on(t)?'cur':''}">
       <rect x="${x}" y="${y}" width="${W}" height="${h}" rx="9"/><text x="${x+12}" y="${y+19}" class="tn">${t}</text><line x1="${x}" x2="${x+W}" y1="${y+HH}" y2="${y+HH}"/>
       ${tb.cols.map((c,i)=>`<text x="${x+12}" y="${y+HH+RH*i+14}" class="cn">${c.pk?'🔑 ':c.fk?'🔗 ':''}${c.name}</text><text x="${x+W-10}" y="${y+HH+RH*i+14}" class="ct" text-anchor="end">${(c.type||'').toLowerCase()}</text>`).join('')}</g>`}).join('')}
    </svg></div>`;
  },{speed:2200});
}

/* ---------- index: SCAN lawan pencarian biner ---------- */
function indexViz(host){
  const N=32,vals=[];let s=7;for(let i=0;i<N;i++){s=(s*37+11)%97;vals.push(1000+s*500+i)}
  const sorted=[...vals].sort((a,b)=>a-b);
  host.innerHTML=`<div class="row"><label>Cari harga = <select class="inp v-tg">${[sorted[3],sorted[17],sorted[29],vals[30]].map((v,i)=>`<option value="${v}" ${i===2?'selected':''}>${v}</option>`).join('')}</select></label></div><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function build(){
    const tg=+$('.v-tg',host).value;const sc=vals.indexOf(tg);
    const bs=[];let lo=0,hi=N-1;while(lo<=hi){const m=(lo+hi)>>1;bs.push({lo,hi,m});if(sorted[m]===tg)break;if(sorted[m]<tg)lo=m+1;else hi=m-1}
    const steps=Math.max(sc+1,bs.length),fr=[];
    for(let k=0;k<steps;k++){const b=bs[Math.min(k,bs.length-1)];fr.push({k,s:Math.min(k,sc),b,sd:k>=sc,bd:k>=bs.length-1,
      note:k>=sc&&k>=bs.length-1?`Selesai. Tanpa index: <b>${sc+1}</b> baris dibaca. Dengan index: hanya <b>${bs.length}</b> langkah. Pada sejuta baris, bedanya sekitar 1.000.000 lawan 20.`
        :`Langkah ${k+1}. SCAN membaca baris satu per satu. Index yang terurut memotong wilayah pencarian jadi setengah setiap langkah.`})}
    const draw=(st,f)=>{st.innerHTML=`<div class="v-ix"><div class="v-cap">Tanpa index: <b>SCAN</b> tabel <span class="v-ct">${Math.min(f.k,f.s)+1} dibaca</span></div>
      ${cellsHTML(vals,i=>i===f.s?(f.sd?'found':'hl'):i<f.s?'seen':'',false)}
      <div class="v-cap">Dengan index: <b>SEARCH</b> lewat B-tree (urut) <span class="v-ct">${Math.min(f.k,bs.length-1)+1} langkah</span></div>
      ${cellsHTML(sorted,i=>i===f.b.m?(f.bd?'found':'hl'):(i<f.b.lo||i>f.b.hi)?'dim':'',false)}</div>`};
    if(!P)P=player(pl,fr,draw,{speed:700});else P.set(fr);
  }
  $('.v-tg',host).onchange=build;build();
}

/* ---------- transaksi ---------- */
function txnViz(host){
  let mode='ok';
  host.innerHTML=`<div class="seg" role="group" aria-label="Skenario"><button data-m="ok" aria-pressed="true">Transfer berhasil</button><button data-m="fail" aria-pressed="false">Gagal di tengah</button></div><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  const F={ok:[
    {sql:'',a:500000,b:300000,st:'',note:'Andi akan mentransfer Rp200.000 ke Budi. Total uang di sistem: Rp800.000.'},
    {sql:'BEGIN;',a:500000,b:300000,st:'tx',snap:1,note:'<b>BEGIN</b> membuka transaksi. Database mencatat keadaan awal agar bisa kembali kapan saja.'},
    {sql:"UPDATE rekening SET saldo = saldo - 200000 WHERE pemilik = 'Andi';",a:300000,b:300000,st:'tx',snap:1,pa:1,note:'Saldo Andi berkurang, tapi perubahan ini <b>belum permanen</b>. Total sementara hanya Rp600.000.'},
    {sql:"UPDATE rekening SET saldo = saldo + 200000 WHERE pemilik = 'Budi';",a:300000,b:500000,st:'tx',snap:1,pa:1,pb:1,note:'Saldo Budi bertambah. Total kembali Rp800.000.'},
    {sql:'COMMIT;',a:300000,b:500000,st:'done',note:'<b>COMMIT</b>: kedua perubahan disimpan permanen bersamaan. Inilah <i>atomicity</i>: semua atau tidak sama sekali.'}],
   fail:[
    {sql:'',a:500000,b:300000,st:'',note:'Skenario yang sama, tapi server mati sebelum perintah kedua.'},
    {sql:'BEGIN;',a:500000,b:300000,st:'tx',snap:1,note:'<b>BEGIN</b> membuka transaksi dan menyimpan titik kembali.'},
    {sql:"UPDATE rekening SET saldo = saldo - 200000 WHERE pemilik = 'Andi';",a:300000,b:300000,st:'tx',snap:1,pa:1,note:'Saldo Andi sudah berkurang (belum permanen).'},
    {sql:'-- server mati / error!',a:300000,b:300000,st:'err',snap:1,pa:1,note:'Terjadi kegagalan. Tanpa transaksi, Rp200.000 milik Andi akan <b>hilang</b> dari sistem.'},
    {sql:'ROLLBACK;',a:500000,b:300000,st:'rb',note:'<b>ROLLBACK</b> (otomatis saat gagal) mengembalikan semua ke titik BEGIN. Uang Andi utuh, total tetap Rp800.000.'}]};
  const draw=(st,f)=>{st.innerHTML=`<pre class="code v-q">${f.sql?hl(f.sql,'sql'):'<span class="c">-- belum ada perintah</span>'}</pre>
    <div class="v-acc"><div class="v-acct ${f.pa?'pend':''} ${f.st==='done'?'ok':''}"><span>Andi</span><b>${rupiah(f.a)}</b>${f.pa?'<small>belum permanen</small>':''}</div>
    <div class="v-acct ${f.pb?'pend':''} ${f.st==='done'?'ok':''}"><span>Budi</span><b>${rupiah(f.b)}</b>${f.pb?'<small>belum permanen</small>':''}</div>
    <div class="v-acct tot ${f.a+f.b!==800000?'bad':''}"><span>Total</span><b>${rupiah(f.a+f.b)}</b></div></div>
    <div class="v-txs ${f.st}">${f.st==='tx'?'Transaksi berjalan · titik kembali tersimpan':f.st==='err'?'Gagal! Transaksi belum selesai':f.st==='rb'?'Dibatalkan: kembali ke keadaan awal':f.st==='done'?'Tersimpan permanen':'Tidak ada transaksi'}</div>`};
  function build(){host.querySelectorAll('[data-m]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.m===mode));if(!P)P=player(pl,F[mode],draw,{speed:1700});else P.set(F[mode])}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-m]');if(b){mode=b.dataset.m;build()}});build();
}

/* ---------- tingkat isolasi ---------- */
function isolationViz(host){
  const LV=['READ UNCOMMITTED','READ COMMITTED','REPEATABLE READ','SERIALIZABLE'];let lv=1;
  host.innerHTML=`<div class="seg v-wrap" role="group" aria-label="Tingkat isolasi">${LV.map((l,i)=>`<button data-l="${i}" aria-pressed="${i===lv}">${l}</button>`).join('')}</div><div class="pl"></div><div class="v-iso-t"></div>`;
  const pl=$('.pl',host);let P;
  const steps=l=>[
    {s:'A',sql:'BEGIN;\nUPDATE rekening SET saldo = 0 WHERE id = 1;',note:'Sesi A mengubah saldo Andi menjadi 0, tapi <b>belum COMMIT</b>.'},
    {s:'B',sql:'SELECT saldo FROM rekening WHERE id = 1;',r:l===0?'0':'500000',bad:l===0&&'Dirty read',note:l===0?'Sesi B membaca data yang belum di-commit. Kalau A membatalkan, B memakai angka palsu.':'Sesi B tetap melihat 500000, karena perubahan A belum di-commit.'},
    {s:'A',sql:'COMMIT;',note:'Sesi A menyimpan perubahannya.'},
    {s:'B',sql:'SELECT saldo FROM rekening WHERE id = 1;',r:l<=1?'0':'500000',bad:l<=1&&'Non-repeatable read',note:l<=1?'Query yang sama di transaksi B memberi angka berbeda.':'B tetap melihat snapshot awal transaksinya: hasil konsisten.'},
    {s:'A',sql:"INSERT INTO rekening VALUES (3, 'Citra', 100000);\nCOMMIT;",note:'Sesi A menambah rekening baru.'},
    {s:'B',sql:'SELECT COUNT(*) FROM rekening;',r:l<=2?'3':'2',bad:l<=2&&'Phantom read',note:l<=2?'Muncul baris "hantu" yang tadinya tidak ada. (PostgreSQL sudah mencegah ini di REPEATABLE READ, standar SQL belum.)':'SERIALIZABLE: B seolah berjalan sendirian, tidak melihat baris baru.'}];
  const draw=(st,f,i)=>{const S=steps(lv).slice(0,i+1);
    st.innerHTML=`<div class="v-iso"><div class="v-cap">Sesi A</div><div class="v-cap">Sesi B</div>${S.map((x,k)=>`<div class="v-ist ${x.s==='A'?'a':'b'} ${k===i?'cur':''}" data-key="s${k}"><pre class="code">${hl(x.sql,'sql')}</pre>${x.r!=null?`<div class="v-res ${x.bad?'bad':'ok'}">→ ${x.r}${x.bad?` <b>${x.bad}</b>`:''}</div>`:''}</div>`).join('')}</div>`};
  function table(){$('.v-iso-t',host).innerHTML=`<div class="tbl"><table class="cmp"><thead><tr><th>Tingkat</th><th>Dirty read</th><th>Non-repeatable</th><th>Phantom</th></tr></thead><tbody>${LV.map((l,i)=>`<tr class="${i===lv?'cur':''}"><td>${l}</td>${[0,1,2].map(k=>`<td>${i>k?'<span class="ok">dicegah</span>':'<span class="bad">mungkin</span>'}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`}
  function build(){host.querySelectorAll('[data-l]').forEach(b=>b.setAttribute('aria-pressed',+b.dataset.l===lv));const fr=steps(lv).map(x=>({note:x.note}));
    if(!P)P=player(pl,fr,draw,{speed:1800});else P.set(fr);table()}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-l]');if(b){lv=+b.dataset.l;build()}});build();
}

/* ---------- SQL injection ---------- */
function injectionViz(host){
  const db=SQLE.create("CREATE TABLE akun (id INTEGER PRIMARY KEY, username TEXT, password TEXT); INSERT INTO akun VALUES (1,'andi','rahasia1'),(2,'budi','kopi123'),(3,'admin','Adm!n2024');");
  const PRE=[['Login normal','andi','rahasia1'],['Password salah','andi','tebak'],["admin' --","admin' --",'apa saja'],["' OR '1'='1","x","' OR '1'='1"]];
  host.innerHTML=`<div class="chips">${PRE.map((p,i)=>`<button class="chip" data-p="${i}">${esc(p[0])}</button>`).join('')}</div>
   <div class="v-inj-f"><label>Username<input class="inp" id="ij-u" autocomplete="off" spellcheck="false"></label><label>Password<input class="inp" id="ij-p" autocomplete="off" spellcheck="false"></label></div>
   <div class="v-inj"><div><div class="v-cap bad">Tidak aman: string dirangkai</div><pre class="code v-q" id="ij-q1"></pre><div class="v-res" id="ij-r1"></div></div>
   <div><div class="v-cap ok">Aman: parameter (prepared statement)</div><pre class="code v-q" id="ij-q2"></pre><div class="v-res" id="ij-r2"></div></div></div>`;
  const U=$('#ij-u',host),Pw=$('#ij-p',host);
  const run=q=>{try{const r=SQLE.exec(db,q);const x=r[r.length-1];return x.rows.length?{ok:true,t:`Login berhasil sebagai <b>${esc(x.rows[0][1])}</b>${x.rows.length>1?` (query mengembalikan ${x.rows.length} akun!)`:''}`}:{ok:false,t:'Login ditolak: username atau password salah.'}}catch(e){return {ok:false,t:'Error: '+esc(e.message)}}};
  function upd(){const u=U.value,p=Pw.value;
    const q1=`SELECT id, username FROM akun WHERE username = '${u}' AND password = '${p}';`;
    $('#ij-q1',host).innerHTML=hl(q1,'sql');
    const q2=`SELECT id, username FROM akun WHERE username = ? AND password = ?;\n-- nilai terikat: [${JSON.stringify(u)}, ${JSON.stringify(p)}]`;
    $('#ij-q2',host).innerHTML=hl(q2,'sql');
    const r1=run(q1),r2=run(`SELECT id, username FROM akun WHERE username = '${u.replace(/'/g,"''")}' AND password = '${p.replace(/'/g,"''")}';`);
    const atk=/['-]/.test(u+p);
    $('#ij-r1',host).className='v-res '+(r1.ok&&atk?'bad':r1.ok?'ok':'');$('#ij-r1',host).innerHTML=r1.t+(r1.ok&&atk?' ⚠️ Penyerang masuk tanpa password yang benar.':'');
    $('#ij-r2',host).className='v-res '+(r2.ok?'ok':'');$('#ij-r2',host).innerHTML=r2.t+(atk&&!r2.ok?' Input dianggap teks biasa, bukan bagian dari perintah SQL.':'');}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-p]');if(!b)return;const p=PRE[+b.dataset.p];U.value=p[1];Pw.value=p[2];upd()});
  U.oninput=Pw.oninput=upd;U.value=PRE[2][1];Pw.value=PRE[2][2];upd();
}

/* ---------- CTE rekursif: bagan organisasi ---------- */
function recursiveViz(host){
  const db=SQLE.create(SEED.toko);
  const q=`WITH RECURSIVE bawahan AS (\n  SELECT id, nama, jabatan, atasan_id, 1 AS level\n  FROM karyawan WHERE atasan_id IS NULL\n  UNION ALL\n  SELECT k.id, k.nama, k.jabatan, k.atasan_id, b.level + 1\n  FROM karyawan k JOIN bawahan b ON k.atasan_id = b.id\n)\nSELECT * FROM bawahan;`;
  const rows=SQLE.exec(db,q)[0].rows;const maxL=Math.max(...rows.map(r=>r[4]));
  const fr=[{L:0,note:'CTE rekursif punya dua bagian: <b>anchor</b> (titik awal) dan <b>bagian rekursif</b> yang memanggil CTE itu sendiri.'}];
  for(let L=1;L<=maxL;L++)fr.push({L,note:L===1?'<b>Anchor</b>: karyawan tanpa atasan (atasan_id IS NULL) menjadi baris pertama, level 1.':`<b>Iterasi ${L-1}</b>: JOIN karyawan dengan baris level ${L-1} yang baru ditemukan. Hasilnya ${rows.filter(r=>r[4]===L).length} baris level ${L}.`});
  fr.push({L:maxL+1,note:`<b>Iterasi ${maxL}</b>: tidak ada lagi karyawan yang atasannya di level ${maxL}. Hasil kosong, rekursi <b>berhenti</b>. Total ${rows.length} baris.`});
  host.innerHTML=`<pre class="code v-q">${hl(q,'sql')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-org">${Array.from({length:maxL},(_,i)=>i+1).map(L=>`<div class="v-lv ${L<=f.L?'':'off'}"><span class="v-lvn">level ${L}</span>${rows.filter(r=>r[4]===L&&L<=f.L).map(r=>`<div class="v-pn ${r[4]===f.L?'new':''}" data-key="k${r[0]}"><b>${esc(r[1])}</b><small>${esc(r[2])}</small></div>`).join('')}</div>`).join('')}</div>`}),{speed:1800});
}

/* ---------- window function ---------- */
function windowViz(host){
  const FN={'ROW_NUMBER()':'ROW_NUMBER()','RANK()':'RANK()','SUM(gaji)':'SUM(gaji)'};let fn='RANK()';
  const db=SQLE.create(SEED.toko);
  host.innerHTML=`<div class="seg" role="group" aria-label="Fungsi window">${Object.keys(FN).map(k=>`<button data-f="${k}" aria-pressed="${k===fn}">${k}</button>`).join('')}</div><pre class="code v-q"></pre><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function build(){
    host.querySelectorAll('[data-f]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.f===fn));
    const q=`SELECT nama, divisi, gaji,\n  ${FN[fn]} OVER (PARTITION BY divisi ORDER BY gaji DESC) AS hasil\nFROM karyawan\nORDER BY divisi, gaji DESC;`;
    $('.v-q',host).innerHTML=hl(q,'sql');
    const rows=SQLE.exec(db,q)[0].rows,divs=[...new Set(rows.map(r=>r[1]))];
    const fr=[{n:-1,note:'<b>PARTITION BY divisi</b> membagi baris per divisi (warna). <b>ORDER BY gaji DESC</b> mengurutkan di dalam setiap partisi. Berbeda dengan GROUP BY, semua baris tetap ada.'}];
    rows.forEach((r,i)=>{const first=i===0||rows[i-1][1]!==r[1];
      fr.push({n:i,note:fn==='ROW_NUMBER()'?`${esc(r[0])}: nomor urut ${r[3]} di divisi ${esc(r[1])}.${first?' Partisi baru, hitungan mulai dari 1.':''}`
        :fn==='RANK()'?`${esc(r[0])}: peringkat ${r[3]}.${!first&&rows[i-1][2]===r[2]?' Gajinya sama dengan baris sebelumnya, jadi peringkatnya sama, dan peringkat berikutnya akan melompat.':first?' Partisi baru, peringkat mulai dari 1.':''}`
        :`${esc(r[0])}: total berjalan ${rupiah(r[3])} (jumlah gaji dari baris pertama partisi sampai baris ini).`})});
    const draw=(st,f)=>{st.innerHTML=rtable(['nama','divisi','gaji','hasil'],rows.map((r,i)=>({v:[esc(r[0]),esc(r[1]),rupiah(r[2]),i<=f.n?`<b>${fn==='SUM(gaji)'?rupiah(r[3]):r[3]}</b>`:'<span class="v-wait">?</span>'],raw:true,cls:'g'+divs.indexOf(r[1])+(i===f.n?' cur':'')+(i>0&&rows[i-1][1]!==r[1]?' brk':'')})))};
    if(!P)P=player(pl,fr,draw,{speed:1100});else P.set(fr);
  }
  host.addEventListener('click',e=>{const b=e.target.closest('[data-f]');if(b){fn=b.dataset.f;build()}});build();
}

/* ---------- anatomi tabel ---------- */
function sqlTableViz(host){
  const db=SQLE.create(SEED.toko),r=SQLE.exec(db,'SELECT * FROM pelanggan;')[0];
  const fr=[{s:'t',note:'Ini <b>tabel</b> <code>pelanggan</code>: kumpulan data sejenis dengan struktur yang sama.'},
    {s:'c',note:'Satu <b>kolom</b> (field) menyimpan satu jenis atribut, misalnya <code>nama</code>. Semua nilai di kolom bertipe sama.'},
    {s:'r',note:'Satu <b>baris</b> (record) adalah satu pelanggan lengkap: Citra dari Surabaya.'},
    {s:'x',note:'Satu <b>sel</b> adalah pertemuan baris dan kolom: kota milik Citra.'},
    {s:'pk',note:'Kolom <code>id</code> adalah <b>primary key</b>: unik dan tidak boleh kosong, jadi setiap baris bisa ditunjuk dengan pasti.'},
    {s:'n',note:'<b>NULL</b> berarti nilainya tidak diketahui atau kosong, bukan teks "NULL" dan bukan angka 0. Kota Gita belum diisi.'}];
  player(host,fr,(st,f)=>{st.innerHTML=`<div class="v-anat s-${f.s}">${rtable(r.cols,r.rows.map((v,i)=>({v,cls:(i===2?'r3':'')+(i===6?' r7':''),cc:c=>(c===1?'cn':'')+(c===0?' pk':'')+(c===2&&i===2?' cx':'')+(c===2&&i===6?' cnul':'')})),{colCls:c=>(c===1?'cn':'')+(c===0?' pk':'')})}</div>`},{speed:1800});
}

/* ---------- SQL lawan NoSQL ---------- */
function sqlNoSqlViz(host){
  const fr=[{s:0,note:'Kiri: data relasional, pelanggan disimpan sekali dan pesanan menunjuknya lewat id. Kanan: basis data dokumen (NoSQL) menyalin data pelanggan ke setiap pesanan agar sekali baca langsung lengkap.'},
    {s:1,note:'Andi pindah ke Bogor. Di SQL cukup <b>1 sel</b> yang diubah. Di dokumen, <b>3 salinan</b> harus diubah; kalau satu terlewat, data jadi tidak konsisten.'},
    {s:2,note:'Sebaliknya, membaca satu pesanan lengkap di dokumen tidak butuh JOIN. NoSQL unggul untuk data yang bentuknya berubah-ubah dan skala besar; SQL unggul untuk konsistensi dan query yang fleksibel.'}];
  player(host,fr,(st,f)=>{const k=f.s>=1?'Bogor':'Jakarta',H=f.s===1?'hl':'';
    st.innerHTML=`<div class="v-2col"><div><div class="v-cap">SQL: tabel terpisah</div>${rtable(['id','nama','kota'],[{v:[1,'Andi',`<span class="${H}">${k}</span>`],raw:true},{v:[2,'Budi','Bandung']}].map(x=>x.raw?x:{v:x.v}),{})}
      ${rtable(['id','pelanggan_id','tanggal'],[[101,1,'2024-10-01'],[103,1,'2024-10-07'],[108,1,'2024-11-05']].map(v=>({v})))}</div>
     <div><div class="v-cap">NoSQL: dokumen</div>${[101,103,108].map((id,i)=>`<pre class="code v-doc ${f.s===2&&i===0?'cur':''}">{ <span class="t">"_id"</span>: ${id},
  <span class="t">"pelanggan"</span>: { <span class="t">"nama"</span>: <span class="s">"Andi"</span>, <span class="t">"kota"</span>: <span class="s ${H}">"${k}"</span> },
  <span class="t">"items"</span>: [ … ] }</pre>`).join('')}</div></div>`},{speed:2600});
}

/* ---------- Java/Python: konversi tipe ---------- */
function castingViz(host,{lang}){
  const J=lang!=='python';
  const box=(v,t,cls='')=>`<div class="v-val ${cls}"><b>${esc(v)}</b><span>${esc(t)}</span></div>`;
  const bits=(n,w)=>{const s=(BigInt.asUintN(64,BigInt(n))).toString(2).padStart(64,'0');return s.slice(64-w)};
  const fr=J?[
    {h:`<div class="v-ladder">${['byte 8','short 16','int 32','long 64','float 32','double 64'].map((x,i)=>`<span class="${i===2||i===5?'on':''}">${x.split(' ')[0]}<small>${x.split(' ')[1]} bit</small></span>`).join('<i>→</i>')}</div><div class="v-cv">${box('7','int')}<span class="v-fn">otomatis</span>${box('7.0','double','ok')}</div>`,note:'<b>Widening</b>: dari tipe kecil ke tipe besar (ke kanan) aman dan otomatis. <code>double rata = jumlah;</code>'},
    {h:`<div class="v-cv">${box('9.99','double')}<span class="v-fn">(int)</span>${box('9','int','warn')}</div><p class="v-sub">Bagian <s>.99</s> dibuang, bukan dibulatkan.</p>`,note:'<b>Narrowing</b> butuh cast eksplisit <code>(int)</code>. Java memaksamu menulisnya sebagai tanda kamu sadar ada data yang hilang.'},
    {h:`<div class="v-cv">${box('3.000.000.000','long')}<span class="v-fn">(int)</span>${box('-1.294.967.296','int','bad')}</div><div class="v-bits"><div><small>long (64 bit)</small><code><span class="cut">${bits(3000000000,64).slice(0,32)}</span>${bits(3000000000,64).slice(32)}</code></div><div><small>int (32 bit)</small><code><span class="sign">1</span>${bits(3000000000,32).slice(1)}</code></div></div>`,note:'<b>Overflow</b>: 32 bit atas dipotong. Bit paling kiri yang tersisa bernilai 1, dan pada int itu tanda <b>negatif</b>. Hasilnya angka yang sama sekali berbeda.'},
    {h:`<div class="v-cv">${box("'A'",'char')}<span class="v-fn">int kode = huruf</span>${box('65','int','ok')}</div>`,note:'char sebenarnya angka: kode Unicode huruf A adalah 65.'},
    {h:`<div class="v-cv">${box('7 / 2','int / int')}<span class="v-fn">=</span>${box('3','int','warn')}</div><div class="v-cv">${box('(double) 7 / 2','double / int')}<span class="v-fn">=</span>${box('3.5','double','ok')}</div>`,note:'Pembagian dua int menghasilkan int. Ubah salah satu operand ke double untuk mendapat pecahan.'}]
  :[
    {h:`<div class="v-cv">${box('"42"','str')}<span class="v-fn">int()</span>${box('42','int','ok')}</div>`,note:'Python tidak mengubah tipe diam-diam antara teks dan angka. Pakai <code>int()</code>, <code>float()</code>, atau <code>str()</code>. Hasil <code>input()</code> selalu str.'},
    {h:`<div class="v-cv">${box('9.99','float')}<span class="v-fn">int()</span>${box('9','int','warn')}</div><p class="v-sub">Pecahan <s>.99</s> dipotong ke arah nol. Untuk membulatkan pakai <code>round()</code>.</p>`,note:'<code>int(9.99)</code> memotong, bukan membulatkan.'},
    {h:`<div class="v-cv">${box('"4.5"','str')}<span class="v-fn">int()</span>${box('ValueError','error','bad')}</div><div class="v-cv">${box('"4.5"','str')}<span class="v-fn">float()</span>${box('4.5','float','ok')}</div>`,note:'Teks berisi pecahan tidak bisa langsung jadi int. Ubah dulu ke float.'},
    {h:`<div class="v-cv">${box('2 ** 100','int')}<span class="v-fn">=</span>${box('1267650600228229401496703205376','int','ok')}</div>`,note:'int di Python tidak punya batas ukuran, jadi tidak ada overflow seperti di Java.'},
    {h:`<div class="v-cv">${box('7 / 2','int / int')}<span class="v-fn">=</span>${box('3.5','float','ok')}</div><div class="v-cv">${box('7 // 2','int // int')}<span class="v-fn">=</span>${box('3','int','warn')}</div>`,note:'<code>/</code> selalu menghasilkan float, <code>//</code> pembagian bulat.'},
    {h:`<div class="v-cv">${box('0, "", []','int, str, list')}<span class="v-fn">bool()</span>${box('False','bool','warn')}</div>`,note:'Nilai "kosong" dianggap False saat dipakai di if. Ini disebut truthy dan falsy.'}];
  player(host,fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-cast">${f.h}</div>`}),{speed:2200});
}

/* ---------- garbage collection ---------- */
function gcViz(host,{lang}){
  const P=lang==='python';
  const fr=[
    {code:P?'a = Toko("A")':'Toko a = new Toko("A");',v:{a:1},o:[1],note:'Objek #1 dibuat di <b>heap</b>. Variabel a di stack menyimpan referensinya.'},
    {code:P?'b = Toko("B")':'Toko b = new Toko("B");',v:{a:1,b:2},o:[1,2],note:'Objek #2 dibuat, dirujuk oleh b.'},
    {code:'a = b'+(P?'':';'),v:{a:2,b:2},o:[1,2],note:'a sekarang menunjuk objek #2. Objek #1 tidak dirujuk siapa pun: <b>tidak terjangkau</b>.'},
    {code:P?'b = None':'b = null;',v:{a:2,b:null},o:[1,2],note:'b dikosongkan, tapi objek #2 masih dirujuk a, jadi masih hidup.'},
    {code:P?'# hitungan referensi #1 = 0':'// GC: fase mark',v:{a:2,b:null},o:[1,2],mark:1,note:P?'Python memakai <b>reference counting</b>: begitu jumlah perujuk objek #1 menjadi 0, ia langsung bisa dibuang.':'Garbage collector menelusuri dari stack (root). Objek yang terjangkau <b>ditandai</b> (mark).'},
    {code:P?'# memori #1 dibebaskan':'// GC: fase sweep',v:{a:2,b:null},o:[2],note:'Objek yang tidak terjangkau <b>disapu</b> (sweep) dan memorinya dipakai ulang. Kamu tidak perlu memanggil free() seperti di C.'}];
  player(host,fr,(st,f)=>flip(st,()=>{const refs=id=>Object.entries(f.v).filter(([,x])=>x===id).map(([k])=>k);
    st.innerHTML=`<pre class="code v-q">${hl(f.code,P?'python':'java')}</pre><div class="v-mem2"><div><div class="v-cap">Stack</div>${Object.entries(f.v).map(([k,x])=>`<div class="v-var" data-key="v${k}"><span>${k}</span><b>${x==null?(P?'None':'null'):'→ #'+x}</b></div>`).join('')}</div>
     <div><div class="v-cap">Heap</div><div class="v-heap">${f.o.map(id=>{const r=refs(id);return `<div class="v-obj ${r.length?'':'dead'} ${f.mark&&r.length?'mark':''}" data-key="o${id}"><b>#${id} Toko("${id===1?'A':'B'}")</b><small>${r.length?'dirujuk: '+r.join(', '):'tidak terjangkau'}${P?` · refcount ${r.length}`:''}</small></div>`}).join('')}</div></div></div>`}),{speed:1900});
}

/* ---------- pass by value ---------- */
function passvalViz(host,{lang}){
  const P=lang==='python',nl=P?'None':'null';
  const code=P?'def ubah(n, a):\n    n = 99\n    a[0] = 99\n\nx = 5\narr = [1, 2, 3]\nubah(x, arr)\nprint(x, arr)':'static void ubah(int n, int[] a) {\n    n = 99;\n    a[0] = 99;\n}\n// di main:\nint x = 5;\nint[] arr = {1, 2, 3};\nubah(x, arr);\nSystem.out.println(x + " " + arr[0]);';
  const fr=[
    {m:{x:5,arr:'#1'},h:[1,2,3],note:'main punya x = 5 dan arr yang menunjuk objek array #1 di heap.'},
    {m:{x:5,arr:'#1'},u:{n:5,a:'#1'},h:[1,2,3],note:P?'Saat ubah dipanggil, n dan a menerima <b>referensi yang sama</b> dengan x dan arr (pass by object reference).':'Java selalu <b>pass by value</b>: n menerima salinan nilai 5, a menerima salinan <i>alamat</i> array, jadi menunjuk objek yang sama.'},
    {m:{x:5,arr:'#1'},u:{n:99,a:'#1'},h:[1,2,3],cn:1,note:P?'<code>n = 99</code> hanya mengikat ulang nama lokal n. x di luar tidak berubah.':'<code>n = 99</code> hanya mengubah salinan. x di main tetap 5.'},
    {m:{x:5,arr:'#1'},u:{n:99,a:'#1'},h:[99,2,3],ch:1,note:'<code>a[0] = 99</code> mengubah isi objek yang dipakai bersama. arr di main ikut melihat perubahan.'},
    {m:{x:5,arr:'#1'},h:[99,2,3],note:`ubah selesai, frame-nya hilang. Keluaran: <b>${P?'5 [99, 2, 3]':'5 99'}</b>.`}];
  host.innerHTML=`<pre class="code v-q">${hl(code,P?'python':'java')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{const fb=(nm,o,cls)=>`<div class="v-frame ${cls||''}" data-key="fr${nm}"><div class="v-cap">${nm}()</div>${Object.entries(o).map(([k,x])=>`<div class="v-var ${(k==='n'&&f.cn)?'chg':''}"><span>${k}</span><b>${String(x).startsWith('#')?'→ '+x:x}</b></div>`).join('')}</div>`;
    st.innerHTML=`<div class="v-mem2"><div><div class="v-cap">Stack</div><div class="v-stack">${f.u?fb('ubah',f.u,'top'):''}${fb('main',f.m)}</div></div><div><div class="v-cap">Heap</div><div class="v-obj ${f.ch?'chg':''}"><b>#1 array</b>${cellsHTML(f.h,i=>f.ch&&i===0?'hl':'')}</div></div></div>`}),{speed:1900});
  void nl;
}

/* ---------- exception: stack unwinding ---------- */
function unwindViz(host,{lang}){
  const P=lang==='python',E=P?'ZeroDivisionError':'ArithmeticException';
  const code=P?'def bagi(a, b):\n    return a / b        # b = 0!\n\ndef proses():\n    return bagi(10, 0)\n\ntry:\n    proses()\nexcept ZeroDivisionError as e:\n    print("Gagal:", e)':'static int bagi(int a, int b) {\n    return a / b;      // b = 0!\n}\nstatic int proses() {\n    return bagi(10, 0);\n}\n// main:\ntry {\n    proses();\n} catch (ArithmeticException e) {\n    System.out.println("Gagal: " + e.getMessage());\n}';
  const S=['main','proses','bagi'];
  const fr=[{n:1,note:'main memanggil proses() di dalam blok try.'},{n:2,note:'proses memanggil bagi(10, 0). Call stack bertambah.'},{n:3,note:'bagi memanggil dirinya di puncak stack, lalu membagi dengan 0.'},
    {n:3,ex:2,note:`<b>${E}</b> dilempar di bagi. Tidak ada ${P?'except':'catch'} di sini, jadi frame bagi dibuang.`},
    {n:2,ex:1,note:`Exception naik ke proses. Di sini juga tidak ada penangkap: frame proses dibuang. Proses ini disebut <b>stack unwinding</b>.`},
    {n:1,ex:0,cat:1,note:`main punya ${P?'except ZeroDivisionError':'catch (ArithmeticException e)'}. Exception tertangkap, program tidak crash.`},
    {n:1,cat:1,out:P?'Gagal: division by zero':'Gagal: / by zero',note:'Blok penangkap dijalankan dan program lanjut normal.'}];
  host.innerHTML=`<pre class="code v-q">${hl(code,P?'python':'java')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-mem2"><div><div class="v-cap">Call stack</div><div class="v-stack">${S.slice(0,f.n).map((s,i)=>`<div class="v-frame ${f.ex===i?'throw':''} ${f.cat&&i===0?'catch':''}" data-key="s${s}"><b>${s}()</b>${f.ex===i?`<small>${E} ↑</small>`:''}</div>`).reverse().join('')}</div></div>
    <div><div class="v-cap">Keluaran</div><div class="console">${f.out?esc(f.out):''}</div></div></div>`}),{speed:1700});
}

/* ---------- stream / comprehension ---------- */
function streamViz(host,{lang}){
  const P=lang==='python',D=[5,12,8,3,20,15];
  const code=P?'data = [5, 12, 8, 3, 20, 15]\nhasil = [x * 2 for x in data if x > 7]\nprint(hasil)':'List<Integer> data = List.of(5, 12, 8, 3, 20, 15);\nList<Integer> hasil = data.stream()\n    .filter(x -> x > 7)\n    .map(x -> x * 2)\n    .collect(Collectors.toList());';
  const ST=P?['data','if x > 7','x * 2','hasil [ ]']:['data','filter(x > 7)','map(x * 2)','collect'];
  const fr=[{pos:D.map(()=>0),note:P?'Comprehension membaca data satu per satu: saring dengan if, ubah dengan ekspresi di depan, kumpulkan ke list.':'Stream memproses elemen <b>satu per satu</b> melewati seluruh pipeline, bukan tahap demi tahap untuk semua data.'}];
  const pos=D.map(()=>0);
  D.forEach((x,i)=>{pos[i]=1;fr.push({pos:[...pos],note:`${x} masuk ke ${ST[1]}.`});
    if(x>7){pos[i]=2;fr.push({pos:[...pos],note:`${x} lolos, lalu diubah menjadi ${x*2}.`});pos[i]=3;fr.push({pos:[...pos],note:`${x*2} masuk ke hasil.`})}
    else{pos[i]=-1;fr.push({pos:[...pos],note:`${x} tidak lolos (${x} ≤ 7), dibuang.`})}});
  fr[fr.length-1].note+=` Hasil akhir: [${D.filter(x=>x>7).map(x=>x*2).join(', ')}].`;
  host.innerHTML=`<pre class="code v-q">${hl(code,P?'python':'java')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-lanes">${ST.map((s,c)=>`<div class="v-lane"><div class="v-cap">${esc(s)}</div><div class="v-toks">${D.map((x,i)=>f.pos[i]===c?`<span class="tok ${c===2||c===3?'ok':''}" data-key="t${i}">${c>=2?x*2:x}</span>`:'').join('')}</div></div>`).join('')}</div>
    <div class="v-drop">${D.map((x,i)=>f.pos[i]===-1?`<span class="tok bad" data-key="t${i}">${x}</span>`:'').join('')}</div>`}),{speed:900});
}

/* ---------- race condition ---------- */
function raceViz(host,{lang}){
  const P=lang==='python';let lock=false;
  host.innerHTML=`<div class="seg" role="group" aria-label="Mode"><button data-k="0" aria-pressed="true">Tanpa kunci</button><button data-k="1" aria-pressed="false">${P?'Dengan Lock':'Dengan synchronized'}</button></div><div class="pl"></div>`;
  const pl=$('.pl',host);let Pl;
  const F={0:[[0,'-','-','','','Dua thread sama-sama ingin menjalankan <code>counter += 1</code>. Itu sebenarnya tiga langkah: baca, tambah, tulis.'],
      [0,'baca 0','-','1','','Thread 1 membaca counter = 0.'],[0,'baca 0','baca 0','2','','Sebelum Thread 1 menulis, Thread 2 juga membaca 0.'],
      [1,'tulis 1','baca 0','1','','Thread 1 menulis 0 + 1 = 1.'],[1,'tulis 1','tulis 1','2','bad','Thread 2 juga menulis 0 + 1 = 1. Satu penambahan <b>hilang</b>! Seharusnya 2. Inilah <b>race condition</b>.']],
    1:[[0,'-','-','','','Sekarang bagian kritis dikunci: hanya satu thread boleh masuk.'],[0,'🔒 baca 0','menunggu','1','','Thread 1 memegang kunci dan membaca 0. Thread 2 harus menunggu.'],
      [1,'tulis 1 🔓','menunggu','1','','Thread 1 menulis 1 lalu melepas kunci.'],[1,'selesai','🔒 baca 1','2','','Thread 2 mendapat kunci dan membaca nilai terbaru, 1.'],[2,'selesai','tulis 2 🔓','2','ok','Hasil benar: 2. Harganya: thread bergantian, jadi sedikit lebih lambat.']]};
  const draw=(st,f)=>{st.innerHTML=`<div class="v-race"><div class="v-th ${f.a==='1'?'cur':''}"><div class="v-cap">Thread 1</div><b>${f.t1}</b></div><div class="v-shared ${f.r}"><div class="v-cap">counter (bersama)</div><b>${f.c}</b>${f.r==='bad'?'<small>harapan: 2</small>':''}</div><div class="v-th ${f.a==='2'?'cur':''}"><div class="v-cap">Thread 2</div><b>${f.t2}</b></div></div>`};
  const fr=k=>F[k].map(([c,t1,t2,a,r,note])=>({c,t1,t2,a,r,note}));
  function build(){host.querySelectorAll('[data-k]').forEach(b=>b.setAttribute('aria-pressed',(b.dataset.k==='1')===lock));if(!Pl)Pl=player(pl,fr(+lock),draw,{speed:1700});else Pl.set(fr(+lock))}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-k]');if(b){lock=b.dataset.k==='1';build()}});build();
}

/* ---------- siklus build Maven ---------- */
function buildViz(host){
  const PH=[['validate','Cek pom.xml dan struktur proyek.',[]],['compile','javac mengubah src/main/java menjadi .class.',['target/classes/App.class']],
    ['test','JUnit menjalankan tes. Jika satu gagal, build berhenti di sini.',['target/surefire-reports/ (12 tes lulus)']],
    ['package','Kelas dibungkus menjadi file JAR.',['target/app-1.0.jar']],['install','JAR disalin ke repositori lokal ~/.m2 agar proyek lain bisa memakainya.',['~/.m2/.../app-1.0.jar']],
    ['deploy','JAR dikirim ke repositori jarak jauh (misalnya Nexus atau Maven Central).',['repo.perusahaan.com/app-1.0.jar']]];
  const fr=PH.map((p,i)=>({i,note:`<b>mvn ${p[0]}</b>: ${p[1]} Menjalankan satu fase berarti menjalankan semua fase sebelumnya juga.`}));
  fr.unshift({i:-1,note:'Maven menjalankan <b>fase</b> berurutan. Ketik <code>mvn package</code> dan fase validate, compile, test, package berjalan otomatis. Gradle punya urutan serupa: <code>gradle build</code>.'});
  player(host,fr,(st,f)=>flip(st,()=>{st.innerHTML=`<div class="v-pipe big">${PH.map((p,i)=>`<span class="${i===f.i?'cur':i<f.i?'done':''}">${p[0]}</span>`).join('<i aria-hidden="true">›</i>')}</div>
    <div class="v-tree"><div>📁 proyek/</div><div class="in">📄 pom.xml</div><div class="in">📁 src/main/java/App.java</div><div class="in">📁 src/test/java/AppTest.java</div>${PH.slice(0,f.i+1).flatMap((p,i)=>p[2].map((a,k)=>`<div class="in new" data-key="a${i}${k}">✓ ${esc(a)}</div>`)).join('')}</div>`}),{speed:1600});
}

/* ---------- decorator ---------- */
function decoratorViz(host){
  const code='def catat(fungsi):\n    def pembungkus(*args):\n        print("mulai", fungsi.__name__)\n        hasil = fungsi(*args)\n        print("selesai")\n        return hasil\n    return pembungkus\n\n@catat\ndef tambah(a, b):\n    return a + b\n\nprint(tambah(2, 3))';
  const fr=[{a:'',out:'',note:'<code>@catat</code> di atas <code>def tambah</code> sama artinya dengan <code>tambah = catat(tambah)</code>.'},
    {a:'wrap',out:'',note:'Nama <b>tambah</b> kini menunjuk ke <b>pembungkus</b>. Fungsi asli tersimpan di dalamnya sebagai <code>fungsi</code> (closure).'},
    {a:'before',out:'mulai tambah\n',note:'Memanggil tambah(2, 3) sebenarnya memanggil pembungkus. Kode "sebelum" jalan dulu.'},
    {a:'inner',out:'mulai tambah\n',note:'pembungkus memanggil fungsi asli: 2 + 3 = 5.'},
    {a:'after',out:'mulai tambah\nselesai\n',note:'Kode "sesudah" jalan, lalu hasil 5 dikembalikan.'},
    {a:'done',out:'mulai tambah\nselesai\n5\n',note:'Decorator menambah perilaku (log, cek izin, cache, ukur waktu) tanpa mengubah isi fungsi aslinya.'}];
  host.innerHTML=`<pre class="code v-q">${hl(code,'python')}</pre><div class="pl"></div>`;
  player($('.pl',host),fr,(st,f)=>{st.innerHTML=`<div class="v-mem2"><div><div class="v-name">tambah →</div><div class="v-wrap1 ${f.a?'on':''} ${['before','after'].includes(f.a)?'cur':''}"><div class="v-cap">${f.a?'pembungkus':'tambah (asli)'}</div>${f.a?`<div class="v-step ${f.a==='before'?'cur':''}">print("mulai")</div><div class="v-wrap2 ${f.a==='inner'?'cur':''}"><div class="v-cap">fungsi = tambah asli</div>return a + b</div><div class="v-step ${f.a==='after'?'cur':''}">print("selesai")</div>`:'<div class="v-wrap2">return a + b</div>'}</div></div>
    <div><div class="v-cap">Keluaran</div><div class="console">${esc(f.out)}</div></div></div>`},{speed:1800});
}

/* ---------- event loop asyncio ---------- */
function eventloopViz(host){
  let mode='async';const T=[['A',2],['B',1],['C',3]];
  host.innerHTML=`<div class="seg" role="group" aria-label="Mode"><button data-m="sync" aria-pressed="false">Berurutan (sync)</button><button data-m="async" aria-pressed="true">asyncio.gather</button></div><div class="pl"></div>`;
  const pl=$('.pl',host);let P;
  function frames(){const fr=[];const end=mode==='sync'?6:3;
    for(let t=0;t<=end;t++){const bars=T.map(([n,d],i)=>{const st=mode==='sync'?T.slice(0,i).reduce((a,x)=>a+x[1],0):0;return {n,st,d,p:Math.max(0,Math.min(d,t-st))}});
      fr.push({t,bars,note:mode==='sync'?(t===0?'Tanpa async, unduhan A, B, C dijalankan satu per satu. Program diam menunggu setiap unduhan.':t===end?`Selesai di detik ${end}. Waktu habis untuk menunggu.`:`Detik ${t}: hanya satu tugas berjalan, yang lain antre.`)
        :(t===0?'Event loop memulai A. Saat A <code>await</code> jaringan, loop langsung beralih ke B, lalu C. Ketiganya menunggu bersamaan.':t===end?`Selesai di detik ${end}, setara tugas terlama. Satu thread saja, tanpa lock.`:`Detik ${t}: ${bars.filter(b=>b.p===b.d&&t>=b.d).map(b=>b.n).join(', ')||'belum ada'} selesai; sisanya masih menunggu I/O.`)})}
    return fr}
  const draw=(st,f)=>{st.innerHTML=`<div class="v-gantt">${f.bars.map(b=>`<div class="v-gr"><span>unduh ${b.n} (${b.d} dtk)</span><div class="v-gt"><i style="left:${b.st/6*100}%;width:${b.p/6*100}%" class="${b.p===b.d?'ok':''}"></i></div></div>`).join('')}<div class="v-gr"><span></span><div class="v-axis">${[0,1,2,3,4,5,6].map(x=>`<b class="${x===f.t?'cur':''}">${x}</b>`).join('')}</div></div></div>`};
  function build(){host.querySelectorAll('[data-m]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.m===mode));if(!P)P=player(pl,frames(),draw,{speed:1000});else P.set(frames())}
  host.addEventListener('click',e=>{const b=e.target.closest('[data-m]');if(b){mode=b.dataset.m;build()}});build();
}

const VIZ2={
  casting:castingViz,gc:gcViz,passval:passvalViz,unwind:unwindViz,stream:streamViz,race:raceViz,build:buildViz,decorator:decoratorViz,eventloop:eventloopViz,
  sqltable:sqlTableViz,sqlvsnosql:sqlNoSqlViz,er:erViz,index:indexViz,txn:txnViz,isolation:isolationViz,injection:injectionViz,recursive:recursiveViz,window:windowViz,
  pipeline:(h,{lesson})=>{h.innerHTML=`<pre class="code v-q">${hl(lesson.vq,'sql')}</pre><div class="pl"></div>`;sqlPipeline($('.pl',h),SQLE.create(SEED.toko),lesson.vq)},
  join:(h,{lesson})=>joinViz(h,lesson.vj||'INNER')
};
const VIZ2T={casting:'Konversi tipe',gc:'Garbage collection',passval:'Cara argumen dikirim',unwind:'Exception merambat di call stack',stream:'Data mengalir lewat pipeline',race:'Race condition',build:'Siklus build',decorator:'Decorator membungkus fungsi',eventloop:'Event loop',
  sqltable:'Anatomi tabel',sqlvsnosql:'SQL lawan NoSQL',er:'Diagram relasi',index:'Index lawan full scan',txn:'Transaksi transfer',isolation:'Tingkat isolasi',injection:'Simulasi SQL injection',recursive:'CTE rekursif',window:'Window function',pipeline:'Urutan eksekusi query',join:'JOIN baris demi baris'};

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
