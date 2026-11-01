/* ===================== VISUALISASI ===================== */
/* Bahasa pelajaran yang sedang dibuka. Di jalur Java, lab hanya menampilkan Java (tanpa kolom Python). */
let VLANG=null;
const JO=()=>VLANG==='java',PO=()=>VLANG==='python';
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
  const notesP=['Semua dimulai dari <b>kode sumber</b>, yaitu teks yang kamu tulis di file <code>halo.py</code>.',
    'Perintah <code>python halo.py</code> menyalakan <b>interpreter</b>. Tidak ada langkah kompilasi terpisah yang harus kamu jalankan.',
    'Interpreter membuat bytecode secara otomatis dan tersembunyi.',
    'Perintah dijalankan satu per satu dari atas ke bawah. Error di baris 10 baru ketahuan saat baris 10 dijalankan.',
    'Teks tampil di layar.'];
  const frames=(JO()?notesJ:PO()?notesP:notes).map((n,s)=>({s,note:n}));
  const lane=(name,cls,arr,s)=>`<div class="lane"><span class="lane-name ${cls}">${name}</span>${arr.map((x,i)=>`${i?'<span class="arrow">→</span>':''}<span class="node ${i<=s?'on':''} ${i===s?'cur':''}">${x}</span>`).join('')}</div>`;
  player(el,frames,(st,f)=>{st.innerHTML=(PO()?'':lane('JAVA','j',J,f.s))+(JO()?'':lane('PYTHON','p',P,f.s))});
},
forloop(el){
  el.innerHTML=`<div class="row"><label for="fl-n">Nilai n:</label><select class="inp" id="fl-n">${[2,3,4,5].map(v=>`<option ${v===3?'selected':''}>${v}</option>`).join('')}</select></div><div class="pl"></div>`;
  const build=n=>{
    const fr=[];let out='';
    if(PO()){
      fr.push({ph:'init',i:'(belum ada)',out,note:`<b>range(1, ${n} + 1)</b> menyiapkan deret 1 sampai ${n}. Batas akhir ${n+1} tidak ikut.`});
      for(let i=1;i<=n;i++){
        fr.push({ph:'check',i,out,note:`<b>Ambil nilai berikutnya</b> dari deret: i = ${i}. Masih ada nilai, jadi masuk ke badan loop.`});
        out+='*'.repeat(i)+'\n';
        fr.push({ph:'body',i,out,note:`<b>Badan loop</b> mencetak ${i} bintang.`});
      }
      fr.push({ph:'check',i:n,out,end:true,note:`<b>Deret habis.</b> Loop selesai setelah ${n} putaran.`});
      return fr;
    }
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
      ${PO()?'':`<div><div class="eyebrow" style="color:var(--java)">Java</div><div class="mini">for (<span class="${on('init')}">int i = 1</span>; <span class="${on('check')}">i &lt;= ${n}</span>; <span class="${on('upd')}">i++</span>) {
    <span class="${on('body')}">System.out.println("*".repeat(i));</span>
}</div></div>`}
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
      if(done){cls='skip';r='dilewati'}else if(s>=t){cls='t';r=PO()?'True':'true';done=true;res=g}else{cls='f';r=PO()?'False':'false'}
      const cj=`<code>${i?'else if':'if'} (${esc(j)})</code>`,cp=`<code>${i?'elif':'if'} ${esc(p)}:</code>`;
      html+=`<div class="dec ${cls}">${JO()?cj:PO()?cp:cj+'<span style="color:var(--muted)">·</span>'+cp}<span>→ ${g}</span><span class="res">${r}</span></div>`;
    });
    html+=`<div class="dec ${done?'skip':'t'}"><code>else</code><span>→ D</span><span class="res">${done?'dilewati':'dijalankan'}</span></div>`;
    $('#ie-f',el).innerHTML=html;$('#ie-r',el).textContent=res;
  };
  $('#ie-s',el).addEventListener('input',upd);upd();
},
boolean(el){
  let p=true,q=false;
  el.innerHTML=`<div class="grid2"><div><div class="row"><button class="toggle" id="bp"></button><button class="toggle" id="bq"></button><span style="color:var(--muted);font-size:.85rem">klik untuk mengubah</span></div>
  <table class="tt" style="margin-top:10px"><thead><tr>${PO()?'':'<th>Java</th>'}${JO()?'':'<th>Python</th>'}<th>Hasil</th></tr></thead><tbody id="btb"></tbody></table></div>
  <div><div class="eyebrow">Loop while: lempar sampai dapat 6</div><div class="mini" style="margin:8px 0">${PO()?'while dadu != 6: ...':'while (dadu != 6) { ... }'}</div><div class="row"><button class="btn primary" id="roll">Lempar dadu</button><span id="rcount" class="log"></span></div><div class="row" id="dice" style="margin-top:10px"></div></div></div>`;
  const B=v=>`<span class="${v?'val-t':'val-f'}">${PO()?(v?'True':'False'):v}</span>`;
  const upd=()=>{
    $('#bp',el).innerHTML=`p = ${B(p)}`;$('#bq',el).innerHTML=`q = ${B(q)}`;
    const rows=[['p &amp;&amp; q','p and q',p&&q],['p || q','p or q',p||q],['!p','not p',!p],['!(p &amp;&amp; q)','not (p and q)',!(p&&q)],['!p || !q','not p or not q',!p||!q]];
    $('#btb',el).innerHTML=rows.map(r=>`<tr>${PO()?'':`<td><code>${r[0]}</code></td>`}${JO()?'':`<td><code>${r[1]}</code></td>`}<td>${B(r[2])}</td></tr>`).join('');
  };
  $('#bp',el).onclick=()=>{p=!p;upd()};$('#bq',el).onclick=()=>{q=!q;upd()};upd();
  $('#roll',el).onclick=()=>{
    clearTimers();const box=$('#dice',el);box.innerHTML='';let n=0;$('#rcount',el).textContent='';
    const t=setInterval(()=>{
      const d=rnd(1,6);n++;box.insertAdjacentHTML('beforeend',`<span class="die ${d===6?'six':''}">${d}</span>`);
      if(d===6||n>=40){clearInterval(t);$('#rcount',el).innerHTML=`Kondisi <code>dadu != 6</code> menjadi ${PO()?'False':'false'} setelah <b>${n}</b> lemparan.`}
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
  el.innerHTML=`<div class="grid2"><div class="blueprint">${PO()?'class Titik<br>  atribut: x, y<br>  geser(dx, dy)<br>  jarak_ke_asal()<br>  __str__()':'class Titik<br>  field: x, y<br>  geser(dx, dy)<br>  jarakKeAsal()<br>  toString()'}</div>
   <div class="row" style="align-content:flex-start"><button class="btn primary" id="ob-new">${PO()?'Titik(x, y)':'new Titik(x, y)'}</button><button class="btn" id="ob-clr">Hapus semua</button><p class="log" id="ob-log" style="flex-basis:100%">Kelas hanyalah cetak biru. Klik tombol untuk membuat objek.</p></div></div>
   <div class="objs" id="ob-list"></div>`;
  const draw=(hi)=>{
    $('#ob-list',el).innerHTML=objs.map((o,i)=>`<div class="obj" ${i===hi?'style="border-color:var(--ok)"':''}><span class="nm">p${o.id} → Titik</span><span>x = <b>${o.x}</b>, y = <b>${o.y}</b></span><span style="color:var(--muted);font-size:.82rem">jarak = ${Math.sqrt(o.x*o.x+o.y*o.y).toFixed(2)}</span><button class="btn" data-i="${i}">p${o.id}.geser(1, 1)</button></div>`).join('');
  };
  $('#ob-new',el).onclick=()=>{
    if(objs.length>=6){$('#ob-log',el).textContent='Cukup enam objek dulu. Hapus untuk mulai lagi.';return}
    const o={id:++k,x:rnd(0,9),y:rnd(0,9)};objs.push(o);
    $('#ob-log',el).innerHTML=`Konstruktor berjalan: <code>${PO()?`p${o.id} = Titik(${o.x}, ${o.y})`:`Titik p${o.id} = new Titik(${o.x}, ${o.y});`}</code> Objek ini punya ${PO()?'atribut':'field'} sendiri.`;draw(objs.length-1);
  };
  $('#ob-clr',el).onclick=()=>{objs=[];k=0;draw();$('#ob-log',el).textContent='Semua objek dihapus.'};
  $('#ob-list',el).addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const i=+b.dataset.i;objs[i].x++;objs[i].y++;
    $('#ob-log',el).innerHTML=`<code>p${objs[i].id}.geser(1, 1)</code> hanya mengubah objek p${objs[i].id}. Objek lain tidak tersentuh.`;draw(i)});
  $('#ob-new',el).click();$('#ob-new',el).click();
},
inherit(el){
  const kids={Kucing:'Meong',Anjing:'Guk',Burung:'Cuit'};
  el.innerHTML=`<div class="tree-cls"><div class="cls abs">«abstrak» Hewan<br><small>kenalkan(), suara()</small></div><div style="color:var(--muted)">${PO()?'▲ mewarisi ▲':'▲ extends ▲'}</div>
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
    $('#ll-c',el).innerHTML=`<span class="ptr front">front →</span>`+L.map((v,i)=>`<div class="lnode ${f(i)}"><span>${v}</span><span>next</span></div><span class="ptr">→</span>`).join('')+`<span class="ptr">${PO()?'None':'null'}</span>`;
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
  <div class="pipe" id="fn-p"></div><div class="grid2">${PO()?'':'<div class="mini" id="fn-j"></div>'}${JO()?'':'<div class="mini" id="fn-py"></div>'}</div>`;
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
    if(!PO())$('#fn-j',el).innerHTML=`<span class="c">// Java</span>\n`+hl(j,'java');
    if(!JO())$('#fn-py',el).innerHTML=`<span class="c"># Python</span>\n`+hl(py,'python');
  };
  el.querySelectorAll('select').forEach(s=>s.addEventListener('change',upd));upd();
}
};

