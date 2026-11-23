/* ===================== UTIL ===================== */
const $ = (s,r=document)=>r.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const store = {
  get(k,d){try{const v=localStorage.getItem(k);return v==null?d:JSON.parse(v)}catch(e){return d}},
  set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
};
let TIMERS=[];
function clearTimers(){TIMERS.forEach(t=>{clearInterval(t);clearTimeout(t)});TIMERS=[]}
const rnd=(a,b)=>a+Math.floor(Math.random()*(b-a+1));

const KW = {
  dart:new Set('void var final const late class extends implements with mixin abstract return if else for while do break continue import export part new this super null true false try catch finally throw rethrow switch case default async await yield required static enum typedef get set is as in on assert dynamic int double num bool String List Map Set Future Stream override'.split(' ')),
  kotlin:new Set('fun val var class object interface data sealed enum open abstract override private public internal protected companion return if else when for while do break continue import package this super null true false try catch finally throw is as in by suspend lateinit const typealias init constructor out vararg inline'.split(' ')),
  java:new Set('public private protected static void class int double boolean char long float byte short new return if else for while do break continue import extends implements interface abstract final this super null true false try catch finally throw throws switch case default var package'.split(' ')),
  python:new Set('def class return if elif else for while in not and or import from as None True False try except finally raise with lambda pass break continue is yield global nonlocal del'.split(' '))
};
const BUILT = {
  dart:new Set('print Widget BuildContext MaterialApp Scaffold Text Column Row Container setState StatelessWidget StatefulWidget State'.split(' ')),
  kotlin:new Set('println listOf mutableListOf mapOf setOf Int Long Double Boolean String List Map Unit Any Modifier Text Column Row Button remember mutableStateOf'.split(' ')),
  java:new Set('System Math String Scanner Random Arrays ArrayList List Map Set HashMap TreeMap HashSet TreeSet Integer Double Stack Queue LinkedList PriorityQueue Collectors File Exception FileNotFoundException IndexOutOfBoundsException Iterator'.split(' ')),
  python:new Set('print len range input int float str list dict set sorted sum max min open self math random deque heapq reduce filter map abs ABC abstractmethod'.split(' '))
};
const SQLKW=new Set('select from where and or not in is null as distinct group by having order asc desc limit offset fetch first next rows only top join inner left right full outer cross on using union all intersect except with recursive insert into values update set delete create table view index unique primary key foreign references check default constraint alter add drop column rename to truncate begin commit rollback savepoint release transaction grant revoke case when then else end exists between like ilike any some over partition explain query plan cascade if replace returning procedure function language returns declare int integer text varchar char date real numeric decimal boolean serial pivot for nulls'.split(' '));
const SQLFN=new Set('count sum avg min max coalesce nullif upper lower length substr substring trim round abs cast concat now date strftime extract dateadd datediff datepart row_number rank dense_rank ntile lag lead first_value last_value replace instr ifnull iif julianday'.split(' '));
function hlSql(code){
  const re=/(--[^\n]*)|('(?:[^']|'')*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|([\s\S])/g;
  let out='',m;
  while((m=re.exec(code))){
    const [tok,com,str,num,word]=m;
    if(com) out+=`<span class="c">${esc(com)}</span>`;
    else if(str) out+=`<span class="s">${esc(str)}</span>`;
    else if(num) out+=`<span class="n">${num}</span>`;
    else if(word){const w=word.toLowerCase();
      if(SQLKW.has(w)) out+=`<span class="k">${word}</span>`;
      else if(SQLFN.has(w)&&code[re.lastIndex]==='(') out+=`<span class="f">${word}</span>`;
      else out+=word;
    } else out+=esc(tok);
  }
  return out;
}
const JSKW=new Set('const let var function return if else for while do break continue new class extends import export from default async await try catch finally throw switch case typeof instanceof in of this super null undefined true false void yield static get set delete interface type enum implements readonly public private protected abstract as keyof never unknown any declare namespace satisfies infer is'.split(' '));
const JSTY=new Set('string number boolean bigint symbol object Array Promise Record Partial Pick Omit Readonly Map Set Date Math JSON console document window React Error Number String Object'.split(' '));
function hlJs(code){
  const re=/(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|(`(?:[^`\\]|\\.)*`|"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_$][\w$]*)|([\s\S])/g;
  let out='',m;
  while((m=re.exec(code))){const [tok,com,str,num,word]=m;
    if(com)out+=`<span class="c">${esc(com)}</span>`;else if(str)out+=`<span class="s">${esc(str)}</span>`;else if(num)out+=`<span class="n">${num}</span>`;
    else if(word){if(JSKW.has(word))out+=`<span class="k">${word}</span>`;else if(JSTY.has(word)||/^[A-Z][a-z]/.test(word))out+=`<span class="t">${word}</span>`;else if(code[re.lastIndex]==='(')out+=`<span class="f">${word}</span>`;else out+=word}
    else out+=esc(tok)}
  return out;
}
function hlHtml(code){
  const re=/(<!--[\s\S]*?-->)|(<\/?)([A-Za-z][\w-]*)|("[^"\n]*"|'[^'\n]*')|(\s)([A-Za-z_:@][\w:.-]*)(?==)|([\s\S])/g;
  let out='',m,inTag=false;
  while((m=re.exec(code))){const [tok,com,open,tag,str,sp,attr]=m;
    if(com)out+=`<span class="c">${esc(com)}</span>`;
    else if(open){inTag=true;out+=esc(open)+`<span class="k">${tag}</span>`}
    else if(str&&inTag)out+=`<span class="s">${esc(str)}</span>`;
    else if(attr&&inTag)out+=sp+`<span class="t">${attr}</span>`;
    else{if(tok==='>')inTag=false;out+=esc(tok)}}
  return out;
}
function hlCss(code){
  const re=/(\/\*[\s\S]*?\*\/)|("[^"\n]*"|'[^'\n]*')|(#[0-9a-fA-F]{3,8}\b|-?\b\d+(?:\.\d+)?(?:px|rem|em|%|vh|vw|fr|s|ms|deg|ch)?)|(--[\w-]+|[a-z-]+)(?=\s*:)|(@[\w-]+)|([\s\S])/g;
  let out='',m;
  while((m=re.exec(code))){const [tok,com,str,num,prop,at]=m;
    if(com)out+=`<span class="c">${esc(com)}</span>`;else if(str)out+=`<span class="s">${esc(str)}</span>`;else if(num)out+=`<span class="n">${num}</span>`;
    else if(prop)out+=`<span class="t">${prop}</span>`;else if(at)out+=`<span class="k">${at}</span>`;else out+=esc(tok)}
  return out;
}
function hlBash(code){
  return code.split('\n').map(l=>{const m=/^(\s*)(\$ )?(.*)$/.exec(l);
    if(/^\s*#/.test(l))return `<span class="c">${esc(l)}</span>`;
    const [,ind,pr,rest]=m;const w=rest.split(/(\s+)/);
    return esc(ind)+(pr?'<span class="c">$ </span>':'')+w.map((x,i)=>i===0&&x?`<span class="k">${esc(x)}</span>`:/^-/.test(x)?`<span class="t">${esc(x)}</span>`:/^["']/.test(x)?`<span class="s">${esc(x)}</span>`:esc(x)).join('')}).join('\n');
}
function hl(code,lang){
  if(lang==='sql')return hlSql(code);
  if(lang==='js'||lang==='ts'||lang==='jsx'||lang==='tsx'||lang==='json')return hlJs(code);
  if(lang==='html'||lang==='xml')return hlHtml(code);
  if(lang==='css'||lang==='scss')return hlCss(code);
  if(lang==='bash'||lang==='shell')return hlBash(code);
  if(lang==='text'||!KW[lang])return esc(code);
  const re = lang==='java'||lang==='dart'||lang==='kotlin'
    ? /(\/\/[^\n]*)|("(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|([\s\S])/g
    : /(#[^\n]*)|([fF]?"(?:[^"\\\n]|\\.)*"|[fF]?'(?:[^'\\\n]|\\.)*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|([\s\S])/g;
  let out='',m;
  while((m=re.exec(code))){
    const [tok,com,str,num,word]=m;
    if(com) out+=`<span class="c">${esc(com)}</span>`;
    else if(str) out+=`<span class="s">${esc(str)}</span>`;
    else if(num) out+=`<span class="n">${num}</span>`;
    else if(word){
      if(KW[lang].has(word)) out+=`<span class="k">${word}</span>`;
      else if(BUILT[lang].has(word)||/^[A-Z][a-z]/.test(word)) out+=`<span class="t">${word}</span>`;
      else if(code[re.lastIndex]==='(') out+=`<span class="f">${word}</span>`;
      else out+=word;
    } else out+=esc(tok);
  }
  return out;
}

/* ---------- pintasan keyboard untuk semua pemutar langkah (lab 2D dan panggung 3D) ----------
   ← → pindah langkah, R ulangi, Spasi putar/jeda. Yang dikendalikan: pemutar terakhir yang disentuh,
   atau pemutar yang paling banyak terlihat di layar. */
const STEPS=[];let STEP_LAST=null;
function stepReg(ctl){STEPS.push(ctl);const h=ctl.host;h.addEventListener('pointerdown',()=>{STEP_LAST=ctl});h.addEventListener('focusin',()=>{STEP_LAST=ctl});return ctl}
function stepPick(){for(let k=STEPS.length-1;k>=0;k--)if(!STEPS[k].host.isConnected)STEPS.splice(k,1);
  const vis=c=>{const r=c.host.getBoundingClientRect();return Math.max(0,Math.min(r.bottom,innerHeight)-Math.max(r.top,0))};
  if(STEP_LAST&&STEP_LAST.host.isConnected&&vis(STEP_LAST)>120)return STEP_LAST;
  let best=null,bv=120;STEPS.forEach(c=>{const v=vis(c);if(v>bv){bv=v;best=c}});return best}
document.addEventListener('keydown',e=>{if(e.altKey||e.ctrlKey||e.metaKey||e.defaultPrevented)return;const t=e.target;
  if(t&&(/^(INPUT|SELECT|TEXTAREA)$/.test(t.tagName)||t.isContentEditable||(t.classList&&t.classList.contains('s3'))))return;
  if(e.key===' '&&t&&/^(BUTTON|A|SUMMARY)$/.test(t.tagName))return;
  if(!/^(ArrowRight|ArrowLeft|r|R| )$/.test(e.key))return;const c=stepPick();if(!c)return;
  const k=e.key;if(k==='ArrowRight')c.go(1);else if(k==='ArrowLeft')c.go(-1);else if(k===' ')c.toggle();else c.replay();e.preventDefault()});

/* player langkah demi langkah: dipakai semua lab 2D. Tampilannya sama dengan panggung 3D:
   bilah progres, titik langkah, kotak penjelasan berlabel, Kembali/Lanjut, Ulangi, Putar/Jeda. */
function player(host,frames,draw,opts={}){
  host.innerHTML=`<div class="stage"></div>
  <div class="pl-steps"><div class="stg-prog" aria-hidden="true"><i></i></div><ol class="pl-dots" aria-label="Langkah"></ol></div>
  <div class="pl-box"><div class="rail-top"><span class="rail-n cnt"></span><span class="rail-tag"></span></div><p class="note" aria-live="polite"></p></div>
  <div class="ctrl"><button class="btn" data-a="prev">← Kembali</button><button class="btn primary" data-a="next">Lanjut →</button>
   <button class="rp" data-a="reset">⟲ Ulangi <kbd>R</kbd></button><button class="rp" data-a="play" aria-pressed="false">▶ Putar <kbd>Spasi</kbd></button></div>`;
  const stage=$('.stage',host),note=$('.note',host),cnt=$('.cnt',host),bar=$('.stg-prog i',host),dots=$('.pl-dots',host),tag=$('.rail-tag',host);
  const pb=$('[data-a=play]',host),nb=$('[data-a=next]',host),bb=$('[data-a=prev]',host);
  let i=0,t=null;
  const stop=()=>{if(t){clearInterval(t);t=null}pb.setAttribute('aria-pressed','false');pb.innerHTML='▶ Putar <kbd>Spasi</kbd>'};
  function show(){const N=frames.length;draw(stage,frames[i],i);note.innerHTML=frames[i].note||'';cnt.textContent=`Langkah ${i+1} / ${N}`;
    const [tt,tc]=i===0?['Mulai','t-a']:i===N-1?['Selesai','t-c']:['Proses','t-b'];tag.textContent=tt;tag.className='rail-tag '+tc;
    bar.style.width=((i+1)/N*100)+'%';
    dots.innerHTML=N<=24?frames.map((f,k)=>`<li><button type="button" data-go="${k}" class="${k<i?'done':k===i?'now':''}" aria-label="Langkah ${k+1}"${k===i?' aria-current="step"':''}></button></li>`).join(''):'';
    bb.disabled=i===0;nb.disabled=false;nb.textContent=i<N-1?'Lanjut →':'↺ Dari awal';
    stage.classList.remove('pl-flash');void stage.offsetWidth;stage.classList.add('pl-flash')}
  const go=d=>{stop();if(d>0&&i===frames.length-1)i=0;else i=Math.max(0,Math.min(frames.length-1,i+d));show()};
  const toggle=()=>{if(t){stop();return}if(i===frames.length-1)i=0;pb.setAttribute('aria-pressed','true');pb.innerHTML='❚❚ Jeda <kbd>Spasi</kbd>';show();
    t=setInterval(()=>{if(!host.isConnected)return stop();if(i<frames.length-1){i++;show()}else stop()},opts.speed||1100);TIMERS.push(t)};
  const replay=()=>{stop();i=0;show()};
  stepReg({host,go,toggle,replay});
  host.addEventListener('click',e=>{const g=e.target.closest('[data-go]');if(g&&host.contains(g)&&dots.contains(g)){stop();i=+g.dataset.go;show();return}
    const b=e.target.closest('.ctrl button');if(!b||!host.contains(b))return;const a=b.dataset.a;
    if(a==='next')go(1);else if(a==='prev')go(-1);else if(a==='reset')replay();else if(a==='play')toggle()});
  show();
  return {set(f){stop();frames=f;i=0;show()}};
}
function cellsHTML(arr,cls=()=>'',ix=true){
  return `<div class="cells">${arr.map((v,i)=>`<div class="cell ${cls(i,v)}">${ix?`<span class="ix">${i}</span>`:''}${v===undefined||v===null?'':esc(v)}</div>`).join('')}</div>`;
}


;/* ===================== VISUALISASI ===================== */
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


;/* ===================== MESIN SQL =====================
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

;/* ===================== DATABASE CONTOH =====================
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

;/* ===================== DATABASE CONTOH BI =====================
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

;/* ===================== VISUALISASI v2 =====================
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

;/* ===================== VISUALISASI v3 =====================
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
  const draw=()=>{const lanes={main:0,fitur:1},W=Math.max(320,C.length*64+60);
    const pos=Object.fromEntries(C.map((c,i)=>[c.id,{x:44+i*64,y:34+lanes[c.b]*56}]));
    const edges=C.flatMap(c=>c.p.map(p=>`<path d="M${pos[p].x},${pos[p].y} C${pos[p].x+32},${pos[p].y} ${pos[c.id].x-32},${pos[c.id].y} ${pos[c.id].x},${pos[c.id].y}" class="ge"/>`)).join('');
    const nodes=C.map(c=>`<g class="gn ${c.p.length>1?'mg':''} b-${c.b}"><circle cx="${pos[c.id].x}" cy="${pos[c.id].y}" r="11"/><text x="${pos[c.id].x}" y="${pos[c.id].y+28}">${c.id}</text></g>`).join('');
    const tags=Object.entries(br).map(([b,id],k)=>`<g class="gt b-${b}"><rect x="${pos[id].x-(b===head?40:30)}" y="${pos[id].y-36-(Object.values(br).filter(v=>v===id).indexOf(id)>-1&&b==='fitur'&&br.main===id?16:0)}" width="${b===head?80:60}" height="16" rx="8"/><text x="${pos[id].x}" y="${pos[id].y-24-(b==='fitur'&&br.main===id?16:0)}">${b}${b===head?' ◀ HEAD':''}</text></g>`).join('');
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
  const SV={bar:()=>V.map((v,i)=>`<rect x="20" y="${12+i*32}" width="${v*3.6}" height="22" rx="3" class="c1"/><text x="${28+v*3.6}" y="${28+i*32}" class="lb">${L[i]} ${v}</text>`).join(''),
    line:()=>{const p=[30,34,31,40,46,43,52,58,55,63,70,68].map((v,i)=>`${20+i*30},${170-v*2}`);return `<polyline points="${p.join(' ')}" class="ln"/>${p.map(x=>`<circle cx="${x.split(',')[0]}" cy="${x.split(',')[1]}" r="3" class="c1"/>`).join('')}`},
    hist:()=>[3,9,16,22,18,11,6,2].map((v,i)=>`<rect x="${20+i*41}" y="${170-v*7}" width="39" height="${v*7}" class="c1"/>`).join(''),
    scatter:()=>[[1,120],[2,190],[3,260],[4,300],[5,390],[6,450],[2.5,210],[4.5,350],[3.5,280],[5.5,410]].map(([a,b])=>`<circle cx="${20+a*52}" cy="${175-b*0.33}" r="5" class="c1"/>`).join(''),
    stack:()=>V.map((v,i)=>[v*.5,v*.3,v*.2].map((w,k,a)=>`<rect x="${20+a.slice(0,k).reduce((s,x)=>s+x,0)*3.6}" y="${12+i*32}" width="${w*3.6}" height="22" class="c${k+1}"/>`).join('')+`<text x="${28+v*3.6}" y="${28+i*32}" class="lb">${L[i]}</text>`).join('')};
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

;/* teks SVG panjang dibungkus menjadi beberapa baris, tidak dipotong */
function svgWrap(t,max,x,y,lh,cls){const L=[];let c='';String(t).split(' ').forEach(w=>{if(c&&(c+' '+w).length>max){L.push(c);c=w}else c=c?c+' '+w:w});if(c)L.push(c);return `<text x="${x}" y="${y}" class="${cls}">${L.map((l,i)=>`<tspan x="${x}" dy="${i?lh:0}">${esc(l)}</tspan>`).join('')}</text>`}
/* ===================== VISUAL JALUR MANAJEMEN SISTEM INFORMASI =====================
   Visual dan animasi untuk pelajaran MSI. Memakai pola umum dari viz3.js (player,
   stageViz, seqViz, seg) dan didaftarkan ke VIZ2 sehingga dipakai lewat field viz. */
const ORG4=[['perusahaan','Perusahaan'],['startup','Startup'],['sekolah','Sekolah'],['organisasi','Organisasi']];
const orgSeg=cur=>seg('Konteks',ORG4,cur||'perusahaan');
/* pasang pemilih konteks + area isi; fn(v, el) menggambar ulang */
function orgWrap(host,fn,first='perusahaan'){
  host.innerHTML=`<div class="v3-ctl">${orgSeg(first)}</div><div class="mv-body"></div>`;
  const body=$('.mv-body',host);segWire(host,'.seg',v=>fn(v,body));fn(first,body);
}

/* 1. SIM vs MSI */
function simmsiViz(host){
  const D={perusahaan:{sys:['ERP','CRM','Kasir (TPS)','Absensi'],sim:'Laporan stok & penjualan harian',mgr:'manajer cabang',msi:['Strategi: ERP mendukung ekspansi 10 cabang','Anggaran: Rp 1,2 M selama 3 tahun','Proyek: migrasi data 6 bulan','Keamanan: hak akses per gudang','SDM: pelatihan 80 staf']},
    startup:{sys:['Aplikasi pemesanan','Dasbor metrik','SaaS akuntansi','CRM ringan'],sim:'Dasbor pesanan & retensi mingguan',mgr:'founder',msi:['Strategi: bangun inti, langganan sisanya','Anggaran: biaya cloud < 8% omzet','Proyek: rilis tiap 2 minggu','Keamanan: MFA semua akun admin','SDM: satu orang pemilik data']},
    sekolah:{sys:['SIAKAD','Dapodik','Presensi','Situs sekolah'],sim:'Rekap nilai & presensi per kelas',mgr:'kepala sekolah',msi:['Strategi: rapor digital untuk orang tua','Anggaran: dana BOS untuk lisensi','Proyek: input nilai online semester ini','Keamanan: data siswa hanya untuk wali kelas','SDM: pelatihan guru 2 sesi']},
    organisasi:{sys:['Simpan pinjam','Pendataan anggota','Formulir donasi','Grup pesan'],sim:'Laporan simpanan & pinjaman bulanan',mgr:'pengurus',msi:['Strategi: transparansi untuk anggota','Anggaran: hosting Rp 150 rb/bulan','Proyek: pindah dari buku besar ke aplikasi','Keamanan: dua admin, kata sandi kuat','SDM: serah terima saat pengurus ganti']}};
  orgWrap(host,(v,el)=>{const d=D[v];
    el.innerHTML=`<div class="mv-nest"><div class="mv-outer"><span class="mv-lab">MSI · cara mengelola</span>
      <ul class="mv-acts">${d.msi.map((m,i)=>`<li style="--d:${i}">${esc(m)}</li>`).join('')}</ul>
      <div class="mv-inner"><span class="mv-lab">Sistem informasi organisasi</span>
        <div class="mv-sys">${d.sys.map(s=>`<span>${esc(s)}</span>`).join('')}<span class="sim">SIM</span></div>
        <div class="mv-flow"><b>SIM</b><i>→</i><span>${esc(d.sim)}</span><i>→</i><span>keputusan ${esc(d.mgr)}</span></div></div></div></div>
      <p class="v3-verdict">SIM adalah salah satu <b>sistem</b> di kotak dalam. MSI adalah kotak luar: semua keputusan untuk <b>mengelola</b> sistem-sistem itu.</p>`},'sekolah');
}

/* 2. Data → informasi → pengetahuan → keputusan */
function dikViz(host){
  const D={perusahaan:['4.210 struk kasir','dijumlah per produk & cabang','Produk A habis di 3 cabang sebelum 14.00','Pola sama tiap gajian','Naikkan stok minimum produk A'],
    startup:['Log klik 50.000 pengguna','dihitung per langkah daftar','40% berhenti di verifikasi KTP','Verifikasi rumit memang menurunkan konversi','Sederhanakan verifikasi'],
    sekolah:['Presensi 960 siswa','direkap per kelas','XI-4 terlambat 2x seminggu','Angkot jalur itu sering telat','Wali kelas cek jadwal angkutan'],
    organisasi:['300 formulir relawan','dikelompokkan per hari','Relawan terbanyak Sabtu pagi','Kegiatan Sabtu biasanya ramai','Pindahkan baksos ke Sabtu']};
  const S=[['Data','fakta mentah'],['Pengolahan','urut, hitung, banding'],['Informasi','bermakna'],['Pengetahuan','+ pengalaman'],['Keputusan','tindakan']];
  orgWrap(host,(v,el)=>{const d=D[v];stageViz(el,S,S.map((s,i)=>({on:[i],extra:`<code>${esc(d[i])}</code>`,note:[`<b>Data</b> mentah belum membantu siapa pun mengambil keputusan.`,`Data <b>diolah</b>: diurutkan, dijumlah, dibandingkan.`,`Hasilnya <b>informasi</b>: akurat, tepat waktu, relevan.`,`Informasi + pengalaman = <b>pengetahuan</b> tentang mengapa itu terjadi.`,`Pengetahuan menjadi <b>keputusan</b> yang bisa diukur hasilnya.`][i]})),{speed:1700})});
}

/* 3. Input-proses-output dan 6 komponen */
function ipoViz(host){
  const C=['Perangkat keras','Perangkat lunak','Data','Prosedur','Manusia','Jaringan'];
  const F=[{on:[0],c:[0,4],note:'<b>Input</b>: kasir memindai barcode dengan pemindai (perangkat keras) dan dioperasikan manusia.'},
    {on:[1],c:[1,2],note:'<b>Proses</b>: aplikasi kasir (perangkat lunak) mencari harga di data barang dan menghitung total.'},
    {on:[2],c:[0,1],note:'<b>Output</b>: struk tercetak dan stok berkurang.'},
    {on:[3],c:[2,5],note:'<b>Penyimpanan</b>: transaksi dikirim lewat jaringan ke server pusat agar bisa dipakai lagi.'},
    {on:[4],c:[3,4],note:'<b>Umpan balik</b>: manajer melihat selisih stok; prosedur stok opname diperbaiki. Tanpa prosedur dan manusia yang terlatih, teknologi saja tidak cukup.'}];
  const S=[['Input','scan barang'],['Proses','hitung total'],['Output','struk, stok'],['Simpan','server pusat'],['Umpan balik','perbaiki']];
  player(host,F,(st,f)=>{st.innerHTML=`<div class="v3-stages">${S.map((s,k)=>`<div class="v3-st ${f.on.includes(k)?'on':''}"><b>${s[0]}</b><small>${s[1]}</small></div>`).join('<span class="v3-arr" aria-hidden="true">→</span>')}</div>
    <div class="mv-comp">${C.map((c,k)=>`<span class="${f.c.includes(k)?'on':''}">${c}</span>`).join('')}</div>`},{speed:1800});
}

/* 4-5. Piramida tingkat manajemen */
function pyramidViz(host){
  const L=[['Strategis','pimpinan puncak','EIS','tidak terstruktur','5 tahun ke depan'],['Taktis','manajer menengah','MIS / DSS','semi-terstruktur','bulanan, kuartalan'],['Operasional','supervisor & staf','TPS','terstruktur','harian']];
  const D={perusahaan:['Buka 10 cabang di Sumatra?','Berapa stok tiap gudang bulan depan?','Catat 4.000 transaksi kasir hari ini'],
    startup:['Masuk kota baru atau perdalam kota lama?','Kanal promosi mana yang paling efisien?','Proses 1.200 pesanan hari ini'],
    sekolah:['Buka jurusan baru tahun depan?','Kelas mana butuh remedial semester ini?','Catat presensi 960 siswa pagi ini'],
    organisasi:['Ubah koperasi menjadi digital penuh?','Berapa batas pinjaman anggota bulan ini?','Catat setoran simpanan hari ini']};
  orgWrap(host,(v,el)=>{const fr=[2,1,0].map(i=>({i,note:`<b>${L[i][0]}</b> (${L[i][1]}): keputusan ${L[i][3]}, rentang ${L[i][4]}. Contoh: <i>${esc(D[v][i])}</i> Sistem pendukung: <b>${L[i][2]}</b>.`}));
    fr.push({i:-1,all:1,note:'Data mengalir ke atas: transaksi TPS diringkas MIS, dianalisis DSS, lalu tampil di dasbor EIS pimpinan.'});
    player(el,fr,(st,f)=>{st.innerHTML=`<svg class="mv-pyr" viewBox="0 0 320 210" role="img" aria-label="Piramida tingkat manajemen">${L.map((l,k)=>{const y=10+k*66,w1=60+k*90,w2=150+k*90;return `<g class="${f.i===k||f.all?'on':''}"><polygon points="${160-w1/2},${y} ${160+w1/2},${y} ${160+w2/2},${y+62} ${160-w2/2},${y+62}"/><text x="160" y="${y+30}">${l[0]}</text><text x="160" y="${y+48}" class="s">${l[2]}</text></g>`}).join('')}${f.all?'<path d="M300 195 L300 20" class="up"/><text x="296" y="16" class="s" text-anchor="end">data naik</text>':''}</svg>`},{speed:2000})},'sekolah');
}

/* 7. ERP, CRM, SCM: satu pesanan melewati modul */
function erpViz(host){
  seqViz(host,[['Pelanggan','toko'],['CRM','data pelanggan'],['ERP Penjualan','pesanan'],['SCM Gudang','stok & kirim'],['ERP Keuangan','faktur']],[
    {on:[0],note:'Toko Maju memesan 50 karton minyak lewat sales.'},
    {from:0,to:1,on:[0,1],label:'riwayat & limit kredit',note:'<b>CRM</b> menampilkan riwayat belanja dan limit kredit pelanggan. Sales tahu toko ini pelanggan setia.'},
    {from:1,to:2,on:[1,2],label:'buat sales order',note:'Pesanan dibuat di modul penjualan <b>ERP</b>, memakai data pelanggan yang sama (tanpa ketik ulang).'},
    {from:2,to:3,on:[2,3],label:'cek & pesan stok',note:'<b>SCM</b> memeriksa stok di gudang terdekat dan menjadwalkan truk.'},
    {from:3,to:4,on:[3,4],label:'barang terkirim',note:'Saat barang dikirim, <b>keuangan</b> otomatis membuat faktur dan piutang.'},
    {from:4,to:1,on:[1,4],label:'status bayar',note:'Status pembayaran kembali ke CRM. Satu basis data, semua bagian melihat angka yang sama.'}],{speed:1700});
}

/* 11. SDLC: waterfall vs agile */
function sdlcViz(host){
  const S=[['Rencana',''],['Analisis',''],['Desain',''],['Bangun',''],['Uji',''],['Rilis & rawat','']];
  host.innerHTML=`<div class="v3-ctl">${seg('Model',[['wf','Waterfall'],['ag','Agile']],'wf')}</div><div class="mv-body"></div>`;
  const body=$('.mv-body',host);
  const run=v=>{if(v==='wf'){stageViz(body,S,S.map((s,i)=>({on:[i],note:`Waterfall: <b>${s[0]}</b> selesai dulu sebelum tahap berikutnya. Cocok saat kebutuhan stabil, misalnya integrasi Dapodik dengan aturan yang sudah baku.${i===5?' Pengguna baru melihat hasil di akhir: perubahan kebutuhan jadi mahal.':''}`})),{speed:1300})}
    else{const fr=[];for(let sp=1;sp<=3;sp++)['Rencana','Desain','Bangun','Uji','Rilis'].forEach((x,i)=>fr.push({sp,i,note:`Sprint ${sp} (2 minggu): <b>${x}</b>.${i===4?` Rilis kecil ke pengguna: ${['pesan & bayar','status kirim','langganan'][sp-1]}. Masukan dipakai di sprint berikutnya.`:''}`}));
      player(body,fr,(st,f)=>{st.innerHTML=`<div class="mv-sprints">${[1,2,3].map(sp=>`<div class="mv-spr ${sp===f.sp?'on':''} ${sp<f.sp?'done':''}"><b>Sprint ${sp}</b><div>${['Rencana','Desain','Bangun','Uji','Rilis'].map((x,i)=>`<span class="${sp<f.sp||(sp===f.sp&&i<=f.i)?'on':''}">${x}</span>`).join('')}</div></div>`).join('')}</div>`},{speed:900})}};
  segWire(host,'.seg',run);run('wf');
}

/* 12. DFD pendaftaran siswa */
function dfdViz(host){
  seqViz(host,[['Calon siswa','entitas luar'],['1.0 Pendaftaran','proses'],['D1 Data siswa','penyimpanan'],['2.0 Verifikasi','proses'],['Bendahara','entitas luar']],[
    {on:[0],note:'DFD memakai empat simbol: <b>entitas luar</b>, <b>proses</b>, <b>penyimpanan data</b>, dan <b>aliran data</b>.'},
    {from:0,to:1,on:[0,1],label:'formulir + berkas',note:'Calon siswa mengirim formulir dan berkas.'},
    {from:1,to:2,on:[1,2],label:'data pendaftar',note:'Proses pendaftaran menyimpan data ke D1.'},
    {from:2,to:3,on:[2,3],label:'data untuk dicek',note:'Panitia memverifikasi berkas dari D1.'},
    {from:3,to:4,on:[3,4],label:'daftar lolos',note:'Daftar siswa lolos dikirim ke bendahara untuk tagihan daftar ulang.'},
    {from:3,to:0,on:[0,3],label:'pengumuman',note:'Hasil verifikasi kembali ke calon siswa. Setiap aliran data diberi nama, dan tidak ada data yang muncul tanpa sumber.'}],{speed:1700});
}

/* 13. Studi kelayakan: biaya-manfaat */
function roiViz(host){
  host.innerHTML=`<div class="v3-ctl">${rng('rB','Biaya awal (juta)',10,300,120,10)}${rng('rO','Biaya per tahun (juta)',0,100,20,5)}${rng('rM','Manfaat per tahun (juta)',0,200,70,5)}</div><div class="mv-roi"></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const B=+$('#rB',host).value,O=+$('#rO',host).value,M=+$('#rM',host).value;['rB','rO','rM'].forEach(id=>$('#'+id+'o',host).textContent=$('#'+id,host).value);
    const cum=[];let c=-B;for(let y=1;y<=5;y++){c+=M-O;cum.push(c)}const mx=Math.max(B,...cum.map(Math.abs),1),pb=cum.findIndex(x=>x>=0);
    const roi=Math.round((cum[4])/(B+O*5)*100);
    $('.mv-roi',host).innerHTML=`<div class="mv-bars"><div><i class="neg" style="height:${B/mx*50}%;top:50%"></i><small>Th 0</small></div>${cum.map((x,i)=>`<div><i class="${x>=0?'pos':'neg'}" style="height:${Math.abs(x)/mx*50}%;${x>=0?`bottom:50%`:'top:50%'}"></i><small>Th ${i+1}</small><em>${x}</em></div>`).join('')}<span class="zero"></span></div>`;
    const v=$('.v3-verdict',host);v.innerHTML=pb>=0?`Balik modal di <b>tahun ke-${pb+1}</b>. ROI 5 tahun <b>${roi}%</b>. Ingat aspek TELOS lain: teknis, hukum, operasional, dan jadwal.`:`Belum balik modal dalam 5 tahun (ROI ${roi}%). Kecilkan biaya awal, pilih SaaS, atau cari manfaat yang lebih besar.`;v.classList.toggle('ok',pb>=0)};
  host.addEventListener('input',draw);draw();
}

/* 14. Cloud: siapa mengelola apa */
function cloudViz(host){
  const L=['Aplikasi','Data','Runtime','Sistem operasi','Server & penyimpanan','Gedung & listrik'];
  const M={onprem:[0,0,0,0,0,0],iaas:[0,0,0,0,1,1],paas:[0,0,1,1,1,1],saas:[1,0,1,1,1,1]};
  const N={onprem:'<b>On-premise</b>: semua milik dan urusan organisasi. Contoh: server SIAKAD di ruang TU sekolah.',iaas:'<b>IaaS</b>: sewa server virtual. Contoh: startup menyewa VM untuk aplikasi pesanan.',paas:'<b>PaaS</b>: cukup unggah kode. Contoh: tim kecil memakai platform hosting aplikasi.',saas:'<b>SaaS</b>: langsung pakai aplikasinya. Contoh: koperasi memakai aplikasi akuntansi langganan. Data tetap tanggung jawabmu.'};
  host.innerHTML=`<div class="v3-ctl">${seg('Model',[['onprem','On-premise'],['iaas','IaaS'],['paas','PaaS'],['saas','SaaS']],'onprem')}</div><div class="mv-stack"></div><p class="v3-verdict"></p>`;
  const draw=v=>{$('.mv-stack',host).innerHTML=L.map((l,i)=>`<div class="${M[v][i]?'vendor':'own'}"><span>${l}</span><small>${M[v][i]?'penyedia':'organisasi'}</small></div>`).join('');$('.v3-verdict',host).innerHTML=N[v]};
  segWire(host,'.seg',draw);draw('onprem');
}

/* 15. Keamanan: kendali vs ancaman */
function ciaViz(host){
  const K=[['mfa','MFA'],['enk','Enkripsi'],['bak','Backup 3-2-1'],['akses','Hak akses minimum'],['log','Log audit']];
  const T=[['Kata sandi admin bocor','C',['mfa']],['Laptop bendahara hilang','C',['enk']],['Ransomware mengunci server','A',['bak']],['Staf magang mengubah nilai','I',['akses','log']],['Server mati saat rapor dibagikan','A',['bak']],['Data pelanggan disadap di Wi-Fi publik','C',['enk']]];
  host.innerHTML=`<div class="mv-chk">${K.map(([k,n])=>`<label><input type="checkbox" value="${k}"> ${n}</label>`).join('')}</div><ul class="mv-threats"></ul><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const on=[...host.querySelectorAll('input:checked')].map(x=>x.value);let n=0;
    $('.mv-threats',host).innerHTML=T.map(([t,c,need])=>{const ok=need.every(x=>on.includes(x));n+=ok;return `<li class="${ok?'ok':'bad'}"><span class="cia">${c}</span>${t}<b>${ok?'✓ tertangani':'✗ berisiko'}</b></li>`}).join('');
    const v=$('.v3-verdict',host);v.innerHTML=`${n} dari ${T.length} ancaman tertangani. C = kerahasiaan, I = integritas, A = ketersediaan.${n===T.length?' Lengkap: keamanan butuh beberapa lapis kendali sekaligus.':''}`;v.classList.toggle('ok',n===T.length)};
  host.addEventListener('change',draw);draw();
}

/* 16. Backup 3-2-1 vs bencana */
function backupViz(host){
  const C=[['asli','Server kantor','lokal'],['nas','NAS di kantor','lokal'],['usb','Hard disk di lemari','lokal'],['cloud','Cloud (offsite)','luar']];
  const E=[['ransom','Ransomware',['asli','nas']],['api','Kebakaran kantor',['asli','nas','usb']],['rusak','Server rusak',['asli']]];
  host.innerHTML=`<p class="small muted">Pilih salinan yang dimiliki, lalu uji dengan bencana.</p><div class="mv-chk">${C.map(([k,n],i)=>`<label><input type="checkbox" value="${k}" ${i===0?'checked disabled':''}> ${n}</label>`).join('')}</div><div class="v3-ctl">${seg('Bencana',E.map(e=>[e[0],e[1]]),'')}</div><div class="mv-copies"></div><p class="v3-verdict" aria-live="polite"></p>`;
  let ev='';const draw=()=>{const on=[...host.querySelectorAll('input:checked')].map(x=>x.value),hit=ev?E.find(e=>e[0]===ev)[2]:[];
    $('.mv-copies',host).innerHTML=C.filter(c=>on.includes(c[0])).map(c=>`<span class="${hit.includes(c[0])?'lost':'safe'}">${c[1]}<small>${hit.includes(c[0])?'hilang':'aman'}</small></span>`).join('');
    const survive=on.filter(c=>!hit.includes(c)).length,r321=on.length>=3&&on.includes('cloud');
    const v=$('.v3-verdict',host);v.innerHTML=(ev?(survive?`Data selamat (${survive} salinan tersisa). `:'<b>Semua salinan hilang.</b> ')
      :'')+(r321?'Aturan 3-2-1 terpenuhi: 3 salinan, 2 media, 1 di luar lokasi.':'Belum 3-2-1: butuh 3 salinan dan 1 di luar lokasi.');v.classList.toggle('ok',!!(ev?survive:r321))};
  host.addEventListener('change',draw);segWire(host,'.seg',v=>{ev=v;draw()});draw();
}

/* 18. Balanced scorecard */
function bscViz(host){
  const P=['Keuangan','Pelanggan','Proses internal','Belajar & tumbuh'];
  const D={perusahaan:['Margin naik 2%','Keluhan kirim < 1%','Pesanan diproses < 4 jam','80% staf lulus pelatihan ERP'],
    startup:['Biaya akuisisi < Rp 40 rb','Retensi bulan-1 > 35%','Rilis tiap 2 minggu','Setiap fitur diuji 5 pengguna'],
    sekolah:['Dana BOS terserap 100%','Kepuasan orang tua > 4/5','Rapor terbit H+3 ujian','Semua guru mahir SIAKAD'],
    organisasi:['Kas tercatat 100%','Anggota aktif naik 20%','Laporan RAT tepat waktu','Pengurus baru terlatih 1 bulan']};
  orgWrap(host,(v,el)=>{el.innerHTML=`<div class="mv-bsc">${P.map((p,i)=>`<div style="--d:${i}"><small>${p}</small><b>${esc(D[v][i])}</b></div>`).join('')}<span class="mid">Visi &amp; strategi</span></div><p class="v3-verdict">Empat sudut pandang saling terhubung: orang yang terlatih memperbaiki proses, proses yang baik memuaskan pelanggan, pelanggan puas memperbaiki keuangan.</p>`});
}

/* 19. Segitiga proyek */
function triangleViz(host){
  host.innerHTML=`<div class="v3-ctl">${rng('tS','Lingkup (jumlah fitur)',2,20,8)}${rng('tW','Waktu (minggu)',2,24,8)}${rng('tT','Anggota tim',1,8,3)}</div><div class="mv-tri"></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const s=+$('#tS',host).value,w=+$('#tW',host).value,t=+$('#tT',host).value;['tS','tW','tT'].forEach(id=>$('#'+id+'o',host).textContent=$('#'+id,host).value);
    const cap=w*t/3,ratio=s/cap,biaya=w*t*12;
    $('.mv-tri',host).innerHTML=`<div class="mv-meter"><span>Beban kerja vs kapasitas</span><div><i class="${ratio>1.15?'bad':ratio>0.95?'warn':'ok'}" style="width:${Math.min(100,ratio*60)}%"></i></div><small>${Math.round(ratio*100)}% · biaya ±Rp ${biaya} juta</small></div>`;
    const v=$('.v3-verdict',host);v.innerHTML=ratio>1.15?'Terlalu ambisius: <b>kualitas</b> akan dikorbankan. Kurangi lingkup (MVP), tambah waktu, atau tambah tim (dengan biaya).':ratio>0.95?'Ketat. Siapkan cadangan waktu dan prioritas fitur (MoSCoW).':'Realistis. Lingkup, waktu, dan biaya seimbang.';v.classList.toggle('ok',ratio<=0.95)};
  host.addEventListener('input',draw);draw();
}

/* 20-23. Studi kasus: sebelum dan sesudah */
function caseViz(host,o={}){
  const t=(o.lesson&&o.lesson.t)||'';
  const C=/perusahaan/i.test(t)?{s:[['Sales','order'],['ERP','satu data'],['Gudang','ambil barang'],['Kirim','truk'],['Faktur','otomatis'],['Dasbor','direksi']],b:'Pesanan lewat telepon, ditulis ulang 3 kali, stok di Excel tiap gudang.',a:'Satu pesanan masuk sekali, semua bagian melihat stok yang sama.',k:['Salah kirim 6% → 1%','Tutup buku 10 → 3 hari']}
    :/startup/i.test(t)?{s:[['Pelanggan','pesan'],['Aplikasi','pesanan'],['QRIS','bayar'],['Dapur','siapkan'],['Kurir','antar'],['Dasbor','metrik']],b:'Pesanan via chat dan spreadsheet; sering salah porsi dan alamat.',a:'Pesanan terstruktur, pembayaran tercatat otomatis.',k:['Salah kirim 5% → 1,4%','Waktu admin 4 → 1 jam/hari']}
    :/sekolah/i.test(t)?{s:[['Guru','input nilai'],['SIAKAD','olah'],['Wali kelas','cek'],['Rapor','digital'],['Orang tua','lihat'],['Dapodik','sinkron']],b:'Nilai di kertas dan file terpisah; rapor terlambat 2 minggu.',a:'Nilai masuk sekali, rapor dan laporan ke Dapodik dari data yang sama.',k:['Rapor H+14 → H+3','Rekap presensi otomatis']}
    :{s:[['Anggota','setor'],['Bendahara','catat'],['Aplikasi','simpan pinjam'],['Anggota','cek saldo'],['Pengurus','laporan'],['RAT','transparan']],b:'Buku besar tulisan tangan; anggota tidak bisa cek saldo.',a:'Setiap anggota melihat simpanan dan pinjamannya sendiri.',k:['Laporan RAT siap H-7','Selisih kas mendekati 0']};
  const fr=[{on:[],before:1,note:'<b>Sebelum</b>: '+C.b}].concat(C.s.map((s,i)=>({on:[i],note:`<b>${s[0]}</b>: ${s[1]}.`})),[{on:C.s.map((_,i)=>i),after:1,note:'<b>Sesudah</b>: '+C.a}]);
  player(host,fr,(st,f)=>{st.innerHTML=`<div class="v3-stages">${C.s.map((s,k)=>`<div class="v3-st ${f.on.includes(k)?'on':''} ${f.before?'skip':''}"><b>${s[0]}</b><small>${s[1]}</small></div>`).join('<span class="v3-arr" aria-hidden="true">→</span>')}</div>${f.after?`<div class="mv-kpi">${C.k.map(k=>`<span>${k}</span>`).join('')}</div>`:''}`},{speed:1400});
}

/* 27. MSI dan UX: diagram Venn bertahap */
function rolesViz(host){
  const I=[['m','Anggaran & ROI'],['m','Keamanan data'],['m','Integrasi sistem'],['u','Riset pengguna'],['u','Alur & wireframe'],['u','Uji kegunaan'],['b','Kebutuhan'],['b','Prioritas'],['b','KPI sukses']];
  const fr=I.map((x,i)=>({n:i+1,note:`<b>${x[1]}</b>: ${x[0]==='m'?'tanggung jawab pengelola SI (MSI)':x[0]==='u'?'tanggung jawab UX Designer':'dikerjakan <b>bersama</b>, di sinilah keduanya bertemu'}.`}));
  player(host,fr,(st,f)=>{const pos={m:[82,0],u:[278,0],b:[180,0]},cnt={m:0,u:0,b:0};
    st.innerHTML=`<svg class="mv-venn" viewBox="0 0 360 210" role="img" aria-label="Peran MSI dan UX"><circle cx="125" cy="105" r="100" class="m"/><circle cx="235" cy="105" r="100" class="u"/><text x="70" y="20" class="h">MSI</text><text x="290" y="20" class="h">UX</text>${I.slice(0,f.n).map((x,i)=>{const y=72+cnt[x[0]]++*28;return `<text x="${pos[x[0]][0]}" y="${y}" class="${i===f.n-1?'cur':''}">${x[1]}</text>`}).join('')}</svg>`},{speed:1500});
}

/* 28. Alur aplikasi baru */
function newappViz(host){
  const S=[['Masalah','MSI+UX'],['Riset','UX'],['Kelayakan','MSI'],['Kebutuhan','MSI+UX'],['Rancang','UX+MSI'],['Prototipe & uji','UX'],['Bangun MVP','dev'],['Uji','QA'],['Rilis','MSI'],['Ukur','MSI+UX']];
  const N=['Tetapkan masalah dan target terukur: salah kirim di bawah 2%.','Wawancara 8 pelanggan dan 3 kurir.','TELOS dan biaya-manfaat: bangun sendiri atau langganan SaaS?','User story, aturan data, dan persetujuan UU PDP.','User flow, wireframe, ERD, arsitektur.','Prototipe diuji 5 pengguna. <b>Gerbang</b>: lanjut atau perbaiki desain dulu.','Bangun fitur inti saja dulu.','Uji fungsi, keamanan, WCAG 2.2 AA, HP murah. <b>Gerbang</b>: siap rilis?','Pelatihan, migrasi data, rilis bertahap.','Bandingkan dengan target di langkah 1, lalu putuskan fitur berikutnya.'];
  player(host,S.map((s,i)=>({i,note:`<b>${i+1}. ${s[0]}</b> (${s[1]}): ${N[i]}`})),(st,f)=>{st.innerHTML=`<ol class="mv-steps">${S.map((s,k)=>`<li class="${k===f.i?'on':''} ${k<f.i?'done':''} ${k===5||k===7?'gate':''}"><b>${s[0]}</b><small>${s[1]}</small></li>`).join('')}</ol>`},{speed:1500});
}

/* 29. Audit dan prioritas perbaikan aplikasi lama */
function auditViz(host){
  const F=[['pw','Password disimpan polos','OWASP A02',5,2],['bak','Tidak ada backup','BCP 3-2-1',5,2],['cap','Login hanya captcha gambar','WCAG 3.3.8',4,2],['lambat','Halaman nilai 9 detik di 3G','Performa',4,3],['kontras','Kontras teks 2.8:1','WCAG 1.4.3',3,1],['tombol','Tombol 16px di ponsel','WCAG 2.5.8',3,1],['ikon','Ikon terlihat kuno','Estetika',1,3]];
  const done=new Set();
  host.innerHTML=`<div class="mv-audit"><svg class="mv-mx" viewBox="0 0 220 220" role="img" aria-label="Matriks dampak dan usaha"></svg><ul class="mv-find"></ul></div><div class="mv-meter"><span>Skor kepatuhan standar</span><div><i class="ok"></i></div><small></small></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const X=e=>20+(e-0.5)*62,Y=d=>185-(d-1)*36;
    $('.mv-mx',host).innerHTML=`<rect x="20" y="10" width="200" height="200" class="bg"/><line x1="120" y1="10" x2="120" y2="210"/><line x1="20" y1="110" x2="220" y2="110"/><text x="70" y="24" class="q">kerjakan dulu</text><text x="170" y="24" class="q">rencanakan</text><text x="70" y="206" class="q">sambil lalu</text><text x="170" y="206" class="q">tunda</text><text x="6" y="110" class="ax" transform="rotate(-90 6 110)">dampak →</text><text x="120" y="219" class="ax">usaha →</text>${F.map(([k,,,d,e],i)=>`<circle cx="${X(e)+(i%3)*16-8}" cy="${Y(d)}" r="7" class="${done.has(k)?'fixed':d>=5?'crit':'open'}"/>`).join('')}`;
    const sorted=[...F].sort((a,b)=>(b[3]-a[3])||(a[4]-b[4]));
    $('.mv-find',host).innerHTML=sorted.map(([k,n,s,d])=>`<li class="${done.has(k)?'fixed':''}"><span><b>${n}</b><small>${s} · dampak ${d}</small></span><button class="btn sm" data-k="${k}" ${done.has(k)?'disabled':''}>${done.has(k)?'Selesai':'Perbaiki'}</button></li>`).join('');
    const tot=F.reduce((a,f)=>a+f[3],0),got=F.filter(f=>done.has(f[0])).reduce((a,f)=>a+f[3],0),p=Math.round(30+got/tot*70);
    $('.mv-meter i',host).style.width=p+'%';$('.mv-meter small',host).textContent=p+'%';
    const next=sorted.find(f=>!done.has(f[0]));const v=$('.v3-verdict',host);
    v.innerHTML=next?`Daftar sudah diurutkan: keamanan dan hukum dulu, lalu dampak terbesar per usaha. Berikutnya: <b>${next[1]}</b>.`:'Semua temuan selesai. Langkah terakhir: <b>ukur ulang</b> dengan metrik yang sama seperti saat audit.';v.classList.toggle('ok',!next)};
  host.addEventListener('click',e=>{const b=e.target.closest('[data-k]');if(b){done.add(b.dataset.k);draw()}});draw();
}

Object.assign(VIZ2,{simmsi:simmsiViz,dik:dikViz,ipo:ipoViz,pyramid:pyramidViz,erp:erpViz,sdlc:sdlcViz,dfd:dfdViz,roi:roiViz,cloud:cloudViz,cia:ciaViz,backup:backupViz,bsc:bscViz,triangle:triangleViz,mcase:caseViz,roles:rolesViz,newapp:newappViz,audit:auditViz});
Object.assign(VIZ2T,{simmsi:'SIM di dalam MSI',dik:'Dari data menjadi keputusan',ipo:'Input, proses, output, dan komponennya',pyramid:'Piramida tingkat manajemen',erp:'Satu pesanan melewati ERP, CRM, dan SCM',sdlc:'Waterfall lawan Agile',dfd:'Diagram aliran data (DFD)',roi:'Kalkulator biaya-manfaat',cloud:'Siapa mengelola apa di cloud',cia:'Kendali keamanan lawan ancaman',backup:'Uji cadangan 3-2-1',bsc:'Balanced scorecard',triangle:'Segitiga proyek',mcase:'Sebelum dan sesudah sistem',roles:'Peran MSI dan UX Designer',newapp:'Alur membuat aplikasi baru',audit:'Audit dan prioritas perbaikan'});

/* SIM: empat jenis laporan dari data yang sama */
function reportsViz(host){
  const D=[['Jakarta','Budi',42,5],['Jakarta','Sari',38,22],['Bandung','Dewi',27,3],['Bandung','Eko',31,18],['Medan','Fitri',19,2],['Medan','Gita',24,15]];
  const rp=n=>'Rp '+n+' jt';
  host.innerHTML=`<div class="v3-ctl">${seg('Jenis laporan',[['jad','Terjadwal'],['adh','Sesuai permintaan'],['exc','Pengecualian'],['dd','Drill-down']],'jad')}</div><div class="mv-rep"></div><p class="v3-verdict" aria-live="polite"></p>`;
  let open='';
  const draw=v=>{const el=$('.mv-rep',host),vd=$('.v3-verdict',host);let h='';
    const cab=[...new Set(D.map(r=>r[0]))].map(c=>[c,D.filter(r=>r[0]===c).reduce((a,r)=>a+r[2],0),D.filter(r=>r[0]===c).reduce((a,r)=>a+r[3],0)]);
    if(v==='jad'){h=`<table class="lt"><caption>Penjualan mingguan per cabang · terbit tiap Senin 07.00</caption><thead><tr><th>Cabang</th><th>Omzet</th><th>Stok tersisa</th></tr></thead><tbody>${cab.map(c=>`<tr><th>${c[0]}</th><td>${rp(c[1])}</td><td>${c[2]} karton</td></tr>`).join('')}</tbody></table>`;vd.innerHTML='<b>Terjadwal</b>: format sama, waktu sama, untuk pemantauan rutin.'}
    if(v==='adh'){h=`<p class="mv-q">❓ "Kasir mana yang omzetnya di atas Rp 30 jt minggu ini?"</p><table class="lt"><thead><tr><th>Kasir</th><th>Cabang</th><th>Omzet</th></tr></thead><tbody>${D.filter(r=>r[2]>30).map(r=>`<tr><th>${r[1]}</th><td>${r[0]}</td><td>${rp(r[2])}</td></tr>`).join('')}</tbody></table>`;vd.innerHTML='<b>Sesuai permintaan</b>: dibuat saat manajer punya pertanyaan khusus.'}
    if(v==='exc'){h=`<table class="lt"><caption>Hanya stok di bawah minimum (10 karton)</caption><thead><tr><th>Cabang</th><th>Pos kasir</th><th>Stok</th></tr></thead><tbody>${D.filter(r=>r[3]<10).map(r=>`<tr class="mv-bad"><th>${r[0]}</th><td>${r[1]}</td><td>${r[3]} karton ⚠</td></tr>`).join('')}</tbody></table>`;vd.innerHTML=`<b>Pengecualian</b>: dari ${D.length} baris, hanya ${D.filter(r=>r[3]<10).length} yang butuh tindakan.`}
    if(v==='dd'){const tot=D.reduce((a,r)=>a+r[2],0);h=`<div class="mv-dd"><button class="mv-ddb" data-c="">Total nasional: ${rp(tot)}</button>${cab.map(c=>`<div><button class="mv-ddb" data-c="${c[0]}" aria-expanded="${open===c[0]}">${open===c[0]?'▾':'▸'} ${c[0]}: ${rp(c[1])}</button>${open===c[0]?`<ul>${D.filter(r=>r[0]===c[0]).map(r=>`<li>${r[1]}: ${rp(r[2])}</li>`).join('')}</ul>`:''}</div>`).join('')}</div>`;vd.innerHTML='<b>Drill-down</b>: klik cabang untuk merinci sampai ke kasir.'}
    el.innerHTML=h};
  let cur='jad';segWire(host,'.seg',v=>{cur=v;draw(v)});
  host.addEventListener('click',e=>{const b=e.target.closest('.mv-ddb');if(b&&b.dataset.c){open=open===b.dataset.c?'':b.dataset.c;draw('dd')}});draw('jad');
}
/* SIM: model keberhasilan DeLone & McLean */
function deloneViz(host){
  const K=[['sys','Kualitas sistem'],['inf','Kualitas informasi'],['svc','Kualitas layanan']];
  host.innerHTML=`<div class="v3-ctl">${rng('dlS','Kualitas sistem',1,5,2)}${rng('dlI','Kualitas informasi',1,5,3)}${rng('dlV','Kualitas layanan',1,5,3)}</div><div class="mv-dl"></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const a=+$('#dlS',host).value,b=+$('#dlI',host).value,c=+$('#dlV',host).value;['dlS','dlI','dlV'].forEach(id=>$('#'+id+'o',host).textContent=$('#'+id,host).value);
    const use=Math.min(5,(a*0.45+b*0.35+c*0.2)),sat=Math.min(5,(a*0.3+b*0.4+c*0.3)),net=Math.min(5,(use*0.5+sat*0.5));
    const bar=(n,v)=>`<div class="mv-dlb"><span>${n}</span><div><i class="${v>=3.5?'ok':v>=2.5?'warn':'bad'}" style="width:${v/5*100}%"></i></div><b>${v.toFixed(1)}</b></div>`;
    $('.mv-dl',host).innerHTML=`<div class="mv-dlc"><small>Penyebab</small>${bar('Sistem',a)}${bar('Informasi',b)}${bar('Layanan',c)}</div><span class="v3-arr" aria-hidden="true">→</span><div class="mv-dlc"><small>Akibat</small>${bar('Penggunaan',use)}${bar('Kepuasan',sat)}</div><span class="v3-arr" aria-hidden="true">→</span><div class="mv-dlc"><small>Hasil</small>${bar('Manfaat bersih',net)}</div>`;
    const v=$('.v3-verdict',host),low=K[[a,b,c].indexOf(Math.min(a,b,c))][1];v.innerHTML=net>=3.5?'SIM berhasil: dipakai, disukai, dan memberi manfaat nyata.':`Manfaat belum terasa. Perbaiki dulu dimensi terlemah: <b>${low}</b>. Contoh: SIAKAD yang lambat membuat guru kembali ke spreadsheet.`;v.classList.toggle('ok',net>=3.5)};
  host.addEventListener('input',draw);draw();
}
Object.assign(VIZ2,{reports:reportsViz,delone:deloneViz});
Object.assign(VIZ2T,{reports:'Empat jenis laporan SIM',delone:'Model keberhasilan DeLone & McLean'});

/* ===== berpikir sistem dan problem solving ===== */
function icebergViz(host){
  const D={perusahaan:['Pesanan salah kirim minggu ini','Naik setiap akhir bulan','Stok di Excel tiap gudang, tidak sinkron','"Yang penting barang keluar dulu"'],
    startup:['Banyak pengguna berhenti','Selalu di langkah verifikasi','Verifikasi 6 langkah, server lambat','"Fitur baru lebih penting dari kemudahan"'],
    sekolah:['Rapor terlambat','Setiap akhir semester','Nilai dikirim via file berbeda, diketik ulang','"Sistem itu urusan operator"'],
    organisasi:['Laporan RAT terlambat','Setiap tahun','Catatan di buku, bendahara sendirian','"Pengurus lama pasti ingat"']};
  const L=[['Kejadian','apa yang terlihat','Reaksi: memadamkan api'],['Pola','apa yang berulang','Antisipasi'],['Struktur','apa yang menyebabkan','Rancang ulang proses & sistem'],['Pola pikir','keyakinan di baliknya','Ubah cara pandang']];
  orgWrap(host,(v,el)=>{const fr=L.map((l,i)=>({i,note:`<b>${l[0]}</b> (${l[1]}): <i>${esc(D[v][i])}</i>. Tindakan di lapisan ini: ${l[2]}.${i===3?' Semakin dalam lapisannya, semakin besar dan tahan lama dampak solusinya.':''}`}));
    player(el,fr,(st,f)=>{st.innerHTML=`<svg class="mv-ice" viewBox="0 0 340 250" role="img" aria-label="Model gunung es"><rect x="0" y="62" width="340" height="188" class="sea"/><line x1="0" y1="62" x2="340" y2="62" class="wl"/><text x="6" y="76" class="s" style="text-anchor:start">permukaan air</text>
      ${L.map((l,k)=>{const y=[14,70,128,186][k],h=[48,54,54,58][k],w=[90,170,240,300][k];return `<g class="${k<=f.i?'on':''} ${k===f.i?'cur':''}"><path d="M${170-w/2+ (k?0:20)},${y+h} L${170-w/2+(k?0:30)},${y} L${170+w/2-(k?0:30)},${y} L${170+w/2-(k?0:20)},${y+h} Z"/><text x="170" y="${y+22}">${l[0]}</text>${k<=f.i?svgWrap(D[v][k],34,170,y+(D[v][k].length>34?35:38),11,'s'):`<text x="170" y="${y+38}" class="s">?</text>`}</g>`}).join('')}</svg>`},{speed:2200})},'sekolah');
}
function lensViz(host){
  const P=[['Guru','Pengguna','Harus < 1 menit per kelas'],['Orang tua','Pengguna','Kabar saat anak tidak hadir'],['Kepala sekolah','Manajemen','Alpa tanpa keterangan turun'],['Tata usaha','Proses','Rekap bulanan tidak perlu lagi'],['Guru BK','Data','Lihat siswa berisiko saja'],['Tim TI','Teknologi','Ringan di Android murah'],['Bendahara','Keuangan','Rp 3 jt/th, hemat 40 jam/bln'],['Siswa tanpa HP','Hukum & etika','Tetap tercatat, data dilindungi']];
  host.innerHTML=`<p class="small muted">Masalah: <b>membuat aplikasi presensi sekolah</b>. Klik setiap pemangku kepentingan untuk menyalakan lensanya.</p><div class="mv-lens"><div class="mv-lc">Aplikasi presensi<small>0 / ${P.length} lensa</small></div>${P.map((p,i)=>`<button class="mv-lp" data-i="${i}" style="--a:${i/P.length}" aria-pressed="false"><b>${p[0]}</b><small>${p[1]}</small></button>`).join('')}</div><ul class="mv-lfind"></ul><p class="v3-verdict" aria-live="polite"></p>`;
  const on=new Set();const draw=()=>{host.querySelectorAll('.mv-lp').forEach(b=>b.setAttribute('aria-pressed',on.has(+b.dataset.i)));$('.mv-lc small',host).textContent=`${on.size} / ${P.length} lensa`;
    $('.mv-lfind',host).innerHTML=[...on].map(i=>`<li><b>${P[i][0]}</b> · ${P[i][1]}: ${P[i][2]}</li>`).join('');
    const v=$('.v3-verdict',host);v.innerHTML=on.size===P.length?'Gambaran utuh: keputusan sekarang bisa dijelaskan dari semua sudut pandang.':on.size?`Masih ${P.length-on.size} sudut pandang yang belum dilihat. Solusi dari sebagian lensa berisiko gagal di lensa lain.`:'Belum ada sudut pandang. Mulai dari siapa saja.';v.classList.toggle('ok',on.size===P.length)};
  host.addEventListener('click',e=>{const b=e.target.closest('.mv-lp');if(b){const i=+b.dataset.i;on.has(i)?on.delete(i):on.add(i);draw()}});draw();
}
function whysViz(host){
  const W=[['Pesanan salah kirim','gejala'],['Kotak tertukar saat diambil kurir',''],['Label ditulis tangan dan mirip',''],['Admin menyalin pesanan dari chat',''],['Tidak ada formulir pesanan terstruktur',''],['Proses tidak pernah ditinjau saat bisnis tumbuh','akar']];
  const F=[['Orang','Guru belum terlatih input online'],['Proses','Nilai lewat 3 tahap kirim file'],['Data','Format nilai beda tiap guru'],['Teknologi','Server lambat di jam sibuk'],['Kebijakan','Batas input tidak jelas'],['Lingkungan','Sinyal lemah di ruang guru']];
  host.innerHTML=`<div class="v3-ctl">${seg('Alat',[['why','5 Why'],['fish','Tulang ikan']],'why')}</div><div class="mv-body"></div>`;const body=$('.mv-body',host);
  const run=v=>{if(v==='why'){player(body,W.map((w,i)=>({i,note:i===0?'Mulai dari <b>gejala</b> yang terlihat. Tanyakan: <b>mengapa?</b>':i===W.length-1?'<b>Akar masalah</b> ditemukan: sesuatu yang bisa diperbaiki. Solusi: formulir pesanan + label cetak otomatis, bukan sekadar menegur kurir.':`Mengapa? → ${esc(w[0])}.`})),(st,f)=>{st.innerHTML=`<ol class="mv-why">${W.slice(0,f.i+1).map((w,k)=>`<li class="${w[1]} ${k===f.i?'cur':''}">${k?'<span class="q">Mengapa?</span>':''}<b>${esc(w[0])}</b>${w[1]?`<small>${w[1]}</small>`:''}</li>`).join('')}</ol>`},{speed:1600})}
    else{player(body,F.map((x,i)=>({i,note:`Kategori <b>${x[0]}</b>: ${x[1]}.${i===F.length-1?' Semua tulang terisi: penyebab ternyata ada di banyak kategori, bukan hanya teknologi.':''}`})),(st,f)=>{st.innerHTML=`<svg class="mv-fish" viewBox="0 0 430 200" role="img" aria-label="Diagram tulang ikan rapor terlambat"><line x1="20" y1="100" x2="340" y2="100" class="sp"/><polygon points="340,80 404,80 424,100 404,120 340,120" class="hd"/><text x="378" y="97" class="hdt">Rapor</text><text x="378" y="110" class="hdt">telat</text>
      ${F.map((x,k)=>{const top=k%2===0,col=Math.floor(k/2),xx=40+col*110,y2=top?28:172;return `<g class="${k<=f.i?'on':''} ${k===f.i?'cur':''}"><line x1="${xx}" y1="${y2}" x2="${xx+30}" y2="100"/><text x="${xx}" y="${top?20:190}" class="cat">${x[0]}</text>${k<=f.i?svgWrap(x[1],16,xx+(top?20:22),top?52:132,11,'c'):''}</g>`}).join('')}</svg>`},{speed:1500})}};
  segWire(host,'.seg',run);run('why');
}
function loopViz(host){
  const N=[['Data lengkap',170,30],['Laporan berguna',272,110],['Guru rajin input',170,190],['Aplikasi cepat',68,110]];
  host.innerHTML=`<div class="v3-ctl">${seg('Arah',[['up','Lingkaran baik'],['down','Lingkaran buruk']],'up')}</div><div class="mv-body"></div>`;const body=$('.mv-body',host);
  const run=v=>{const good=v==='up',lab=good?['Data lengkap ↑','Laporan berguna ↑','Guru rajin input ↑','Aplikasi cepat ↑']:['Data bolong ↓','Laporan tak dipercaya ↓','Guru pakai kertas ↓','Aplikasi lambat ↓'];
    const fr=[];for(let lap=1;lap<=2;lap++)[3,0,1,2].forEach((k,j)=>fr.push({k,lap,note:`${lap===2&&j===0?'Putaran kedua, efeknya makin besar. ':''}<b>${lab[k]}</b>${j<3?' menyebabkan langkah berikutnya.':' kembali memengaruhi awal lingkaran.'}${lap===2&&j===3?(good?' <b>Titik ungkit</b>: buat aplikasinya cepat dan satu laporan yang benar-benar membantu guru.':' Untuk memutusnya, perbaiki titik paling awal: kecepatan aplikasi.'):''}`}));
    player(body,fr,(st,f)=>{st.innerHTML=`<svg class="mv-loop ${good?'g':'b'}" viewBox="0 0 340 220" role="img" aria-label="Lingkaran sebab-akibat"><circle cx="170" cy="110" r="72" class="ring"/><text x="170" y="106" class="mid">${good?'R+':'R−'}</text><text x="170" y="122" class="ms">putaran ${f.lap}</text>${N.map((n,k)=>`<g class="${k===f.k?'cur':''}"><rect x="${n[1]-60}" y="${n[2]-16}" width="120" height="32" rx="10"/><text x="${n[1]}" y="${n[2]+4}">${lab[k]}</text></g>`).join('')}</svg>`},{speed:1400})};
  segWire(host,'.seg',run);run('up');
}
function holisticViz(host){
  const S=[['Keluhan','"Kami butuh aplikasi baru"'],['Definisi','60% anggota ragu saldo; RAT 6 jam'],['Gunung es','Struktur: buku tunggal, satu bendahara'],['Lensa','Lansia tanpa HP pintar; dinas butuh laporan baku'],['5 Why','Akar: tidak ada transparansi rutin'],['Alternatif','Aplikasi lengkap · Spreadsheet + slip cetak · Papan pengumuman'],['Keputusan','Spreadsheet + slip cetak (dampak tinggi, biaya rendah)'],['Efek samping','Slip berisi data pribadi → amplop tertutup'],['Ukur ulang','Survei kepercayaan + durasi RAT berikutnya']];
  player(host,S.map((s,i)=>({i,note:`<b>${s[0]}</b>: ${s[1]}.${i===0?' Pemikir sepotong-sepotong langsung membeli aplikasi. Pemikir sistem bertanya dulu.':''}${i===S.length-1?' Solusinya ternyata gabungan proses dan teknologi sederhana.':''}`})),(st,f)=>{st.innerHTML=`<ol class="mv-steps mv-hol">${S.map((s,k)=>`<li class="${k===f.i?'on':''} ${k<f.i?'done':''}"><b>${s[0]}</b><small>${k<=f.i?esc(s[1]):'…'}</small></li>`).join('')}</ol>`},{speed:1800});
}
Object.assign(VIZ2,{iceberg:icebergViz,lens:lensViz,whys:whysViz,loop:loopViz,holistic:holisticViz});
Object.assign(VIZ2T,{iceberg:'Model gunung es',lens:'Lensa pemangku kepentingan',whys:'5 Why dan diagram tulang ikan',loop:'Lingkaran sebab-akibat',holistic:'Berpikir utuh, langkah demi langkah'});

;/* ===================== ANIMASI: MEMBUAT VARIABEL =====================
   Animasi langkah demi langkah tentang cara variabel dibuat, diisi, diubah, dan dipakai.
   Satu skenario per bahasa (Java, Python, JavaScript, TypeScript, CSS, React). Kiri: kode
   yang "diketik" baris demi baris. Kanan: memori, yaitu kotak variabel dan isinya. */
const VARANIM={
 java:{file:'Main.java',lang:'java',code:['int umur = 17;','double harga = 12500.0;','String nama = "Sari";','umur = umur + 1;','final double PAJAK = 0.11;','double total = harga + harga * PAJAK;','umur = "tujuh belas";'],
  steps:[
   {ln:0,mem:[['umur','int','17','new']],note:'<b>Deklarasi + inisialisasi.</b> Java menyiapkan kotak bernama <code>umur</code> yang <b>hanya</b> boleh berisi bilangan bulat (<code>int</code>), lalu mengisinya dengan 17.'},
   {ln:1,mem:[['umur','int','17'],['harga','double','12500.0','new']],note:'Kotak <code>harga</code> bertipe <code>double</code> untuk bilangan pecahan.'},
   {ln:2,mem:[['umur','int','17'],['harga','double','12500.0'],['nama','String','"Sari"','new']],note:'<code>String</code> menyimpan teks. Teks ditulis di antara tanda kutip ganda.'},
   {ln:3,mem:[['umur','int','18','chg','17']],keep:1,note:'<b>Mengubah isi.</b> Ruas kanan dihitung dulu: umur (17) + 1 = 18, lalu hasilnya dimasukkan kembali ke kotak <code>umur</code>. Isi lama 17 hilang.'},
   {ln:4,mem:[['PAJAK','final double','0.11','new lock']],keep:1,note:'<code>final</code> membuat <b>konstanta</b>: isinya dikunci dan tidak bisa diubah lagi. Nama konstanta biasanya huruf besar.'},
   {ln:5,mem:[['total','double','13875.0','new']],keep:1,note:'Variabel dipakai dalam perhitungan: 12500.0 + 12500.0 × 0.11 = 13875.0.'},
   {ln:6,err:'error: incompatible types: String cannot be converted to int',keep:1,note:'<b>Error saat kompilasi.</b> Kotak <code>umur</code> bertipe <code>int</code>, jadi tidak bisa diisi teks. Java memeriksa tipe sebelum program jalan.'}]},
 python:{file:'main.py',lang:'python',code:['umur = 17','harga = 12500.0','nama = "Sari"','umur = umur + 1','PAJAK = 0.11','total = harga + harga * PAJAK','umur = "tujuh belas"'],
  steps:[
   {ln:0,mem:[['umur','int','17','new']],note:'<b>Membuat variabel</b> cukup dengan <code>=</code>. Python melihat nilainya (17) dan otomatis tahu tipenya <code>int</code>. Tidak perlu menulis tipe.'},
   {ln:1,mem:[['umur','int','17'],['harga','float','12500.0','new']],note:'Bilangan berkoma bertipe <code>float</code>.'},
   {ln:2,mem:[['umur','int','17'],['harga','float','12500.0'],['nama','str','"Sari"','new']],note:'Teks bertipe <code>str</code>. Boleh pakai kutip tunggal atau ganda.'},
   {ln:3,mem:[['umur','int','18','chg','17']],keep:1,note:'<b>Mengubah isi.</b> Ruas kanan dihitung dulu: 17 + 1 = 18, lalu nama <code>umur</code> sekarang menunjuk nilai 18.'},
   {ln:4,mem:[['PAJAK','float','0.11','new']],keep:1,note:'Python tidak punya konstanta sungguhan. <b>Kesepakatannya</b>: nama huruf besar berarti "jangan diubah".'},
   {ln:5,mem:[['total','float','13875.0','new']],keep:1,note:'Variabel dipakai dalam perhitungan: 12500.0 + 12500.0 × 0.11 = 13875.0.'},
   {ln:6,mem:[['umur','str','"tujuh belas"','chg','18']],keep:1,note:'<b>Boleh di Python</b>: tipe mengikuti nilainya (dynamic typing). Tapi hati-hati, <code>umur + 1</code> setelah ini akan error karena teks tidak bisa ditambah angka.'}]},
 js:{file:'main.js',lang:'js',code:['let umur = 17;','const nama = "Sari";','let harga = 12500;','umur = umur + 1;','const total = harga * 1.11;','console.log(nama, umur, total);','nama = "Budi";'],
  steps:[
   {ln:0,mem:[['umur','let','17','new']],note:'<code>let</code> membuat variabel yang <b>boleh diubah</b> nanti.'},
   {ln:1,mem:[['umur','let','17'],['nama','const','"Sari"','new lock']],note:'<code>const</code> membuat variabel yang <b>tidak boleh diisi ulang</b>. Biasakan memakai <code>const</code> kecuali memang perlu diubah.'},
   {ln:2,mem:[['harga','let','12500','new']],keep:1,note:'Angka di JavaScript bertipe <code>number</code>, baik bulat maupun pecahan.'},
   {ln:3,mem:[['umur','let','18','chg','17']],keep:1,note:'<b>Mengubah isi.</b> 17 + 1 = 18 dimasukkan kembali ke <code>umur</code>.'},
   {ln:4,mem:[['total','const','13875','new lock']],keep:1,note:'Variabel dipakai dalam perhitungan: 12500 × 1.11 = 13875.'},
   {ln:5,out:'Sari 18 13875',keep:1,note:'<code>console.log</code> membaca isi variabel dan menampilkannya di konsol.'},
   {ln:6,err:'TypeError: Assignment to constant variable.',keep:1,note:'<b>Error.</b> <code>nama</code> dibuat dengan <code>const</code>, jadi tidak bisa diisi ulang.'}]},
 ts:{file:'main.ts',lang:'ts',code:['let umur: number = 17;','const nama: string = "Sari";','let aktif = true;','umur = umur + 1;','let kota: string | null = null;','kota = "Bandung";','umur = "tujuh belas";'],
  steps:[
   {ln:0,mem:[['umur','number','17','new']],note:'TypeScript menambahkan <b>anotasi tipe</b> setelah titik dua: kotak <code>umur</code> hanya untuk <code>number</code>.'},
   {ln:1,mem:[['umur','number','17'],['nama','string','"Sari"','new lock']],note:'<code>const</code> + <code>string</code>: teks yang tidak boleh diisi ulang.'},
   {ln:2,mem:[['aktif','boolean','true','new']],keep:1,note:'<b>Inferensi tipe</b>: tanpa anotasi pun TypeScript tahu <code>aktif</code> bertipe <code>boolean</code> dari nilainya.'},
   {ln:3,mem:[['umur','number','18','chg','17']],keep:1,note:'Mengubah isi: 17 + 1 = 18. Tipenya tetap <code>number</code>.'},
   {ln:4,mem:[['kota','string | null','null','new']],keep:1,note:'<b>Union type</b>: <code>kota</code> boleh berisi teks <b>atau</b> <code>null</code> (belum diisi).'},
   {ln:5,mem:[['kota','string | null','"Bandung"','chg','null']],keep:1,note:'Sekarang <code>kota</code> berisi teks.'},
   {ln:6,err:"Type 'string' is not assignable to type 'number'.",keep:1,note:'<b>Error sebelum program jalan.</b> Editor sudah memberi garis merah: <code>umur</code> bertipe <code>number</code>.'}]},
 css:{file:'gaya.css',lang:'css',code:[':root {','  --merek: #0F766E;','  --radius: 8px;','}','.tombol { background: var(--merek); border-radius: var(--radius); }','.tema-gelap { --merek: #5EC9B5; }'],
  steps:[
   {ln:0,mem:[],note:'Variabel CSS (custom property) biasanya ditaruh di <code>:root</code> agar berlaku di seluruh halaman.'},
   {ln:1,mem:[['--merek','warna','#0F766E','new']],pv:'#0F766E',note:'Nama variabel CSS <b>wajib</b> diawali dua tanda minus: <code>--merek</code>.'},
   {ln:2,mem:[['--merek','warna','#0F766E'],['--radius','panjang','8px','new']],pv:'#0F766E',note:'Satu variabel bisa dipakai di ratusan tempat. Ubah satu kali, semua ikut berubah.'},
   {ln:4,mem:[['--merek','warna','#0F766E'],['--radius','panjang','8px']],pv:'#0F766E',btn:1,note:'<code>var(--merek)</code> <b>membaca</b> isi variabel. Tombol kini berwarna sesuai merek.'},
   {ln:5,mem:[['--merek','warna','#5EC9B5','chg','#0F766E'],['--radius','panjang','8px']],pv:'#5EC9B5',btn:1,dark:1,note:'Di dalam <code>.tema-gelap</code>, <code>--merek</code> diisi ulang. Tombol di dalamnya otomatis berubah warna tanpa menulis ulang aturan <code>.tombol</code>.'}]},
 react:{file:'Penghitung.jsx',lang:'jsx',code:['function Penghitung() {','  const [jumlah, setJumlah] = useState(0);','  const label = "Klik";','  return <button onClick={() => setJumlah(jumlah + 1)}>','    {label}: {jumlah}','  </button>;','}'],
  steps:[
   {ln:1,mem:[['jumlah','state','0','new'],['setJumlah','fungsi','ƒ']],ui:'Klik: 0',note:'<code>useState(0)</code> membuat <b>variabel state</b> bernilai awal 0, plus fungsi <code>setJumlah</code> untuk mengubahnya.'},
   {ln:2,mem:[['jumlah','state','0'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"','new']],ui:'Klik: 0',note:'Variabel biasa (<code>const</code>) dibuat ulang setiap render.'},
   {ln:4,mem:[['jumlah','state','0'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"']],ui:'Klik: 0',note:'JSX membaca variabel di dalam <code>{ }</code> untuk ditampilkan.'},
   {ln:3,mem:[['jumlah','state','1','chg','0'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"']],ui:'Klik: 1',click:1,note:'Tombol diklik → <code>setJumlah(0 + 1)</code>. React menyimpan nilai baru dan <b>merender ulang</b> komponen.'},
   {ln:3,mem:[['jumlah','state','2','chg','1'],['setJumlah','fungsi','ƒ'],['label','const','"Klik"']],ui:'Klik: 2',click:1,note:'Klik lagi → 2. Mengubah <code>jumlah</code> langsung (<code>jumlah = 2</code>) tidak akan memperbarui layar; selalu lewat <code>setJumlah</code>.'}]}};
function varanimViz(host,o={}){
  const S=VARANIM[o.va]||VARANIM.js;let mem=[];
  /* bangun memori kumulatif: keep=1 berarti gabungkan dengan langkah sebelumnya */
  const frames=[];S.steps.forEach(st=>{let m=mem.map(x=>x.slice(0,3));
    if(st.mem){if(st.keep){st.mem.forEach(n=>{const i=m.findIndex(x=>x[0]===n[0]);if(i>=0)m[i]=n;else m.push(n)})}else m=st.mem.map(x=>x.slice())}
    mem=m;frames.push({...st,m:m.map((x,i)=>{const n=(st.mem||[]).find(y=>y[0]===x[0]);return n||x})})});
  player(host,frames,(stage,f)=>{
    stage.innerHTML=`<div class="va"><div class="va-code"><div class="va-file">${S.file}</div><pre>${S.code.map((ln,i)=>`<span class="va-ln ${i===f.ln?'cur':''} ${i<f.ln||(f.ln<i&&false)?'done':''} ${f.err&&i===f.ln?'bad':''}"><em>${i+1}</em><code>${hl(ln,S.lang)||' '}</code></span>`).join('')}</pre>
      ${f.err?`<div class="va-err">✗ ${esc(f.err)}</div>`:''}${f.out?`<div class="va-out"><small>Konsol</small>${esc(f.out)}</div>`:''}</div>
     <div class="va-mem"><div class="va-file">Memori</div>${f.m.length?f.m.map(([n,t,v,fl,old])=>`<div class="va-box ${fl||''}"><span class="va-n">${esc(n)}</span><span class="va-v">${old!=null?`<s>${esc(old)}</s> `:''}<b>${esc(v)}</b>${fl&&fl.includes('lock')?' 🔒':''}</span><span class="va-t">${esc(t)}</span></div>`).join(''):'<p class="muted small">Belum ada variabel.</p>'}
      ${f.pv?`<div class="va-pv ${f.dark?'dark':''}"><small>Pratinjau</small>${f.btn?`<button tabindex="-1" style="background:${f.pv};border-radius:8px">Pesan sekarang</button>`:`<i style="background:${f.pv}"></i>`}</div>`:''}
      ${f.ui?`<div class="va-pv"><small>Layar</small><button tabindex="-1" class="${f.click?'clk':''}">${esc(f.ui)}</button></div>`:''}</div></div>`},{speed:2200});
}
VIZ2.varanim=varanimViz;VIZ2T.varanim='Animasi: membuat dan mengubah variabel';
/* pelajaran variabel di setiap jalur pemrograman */
function varAnimOf(tk,l){
  if((tk==='java'||tk==='python')&&l.k==='topic'&&l.ref==='2.0')return tk;
  if(tk==='fe0'&&l.t==='Variabel & tipe data')return 'js';
  if(tk==='ts'&&l.t==='Primitif, array & tuple')return 'ts';
  if(tk==='css'&&l.t==='Variabel CSS & tema')return 'css';
  if(tk==='react'&&l.t==='State dengan useState')return 'react';
  return null;
}

;/* ===================== SIMULATOR FLOWCHART & PSEUDOCODE =====================
   Satu program (lesson.fc) digambar sebagai flowchart bergaya Flowgorithm,
   ditulis ulang sebagai pseudocode, lalu dijalankan langkah demi langkah.
   fc = {name, in:[input...], p:[node...]}
   node: {t:'dec',v,ty,arr} {t:'in',v} {t:'asg',v,e} {t:'out',e}
         {t:'if',c,y:[],n:[]} {t:'while',c,b:[]} {t:'for',v,a,z,s,b:[]} {t:'do',c,u,b:[]}
   Ekspresi memakai sintaks Flowgorithm: = (sama dengan), <>, mod, and, or, not, & (gabung teks). */
const FCF={Int:Math.trunc,Sqrt:Math.sqrt,Abs:Math.abs,Len:s=>String(s).length,ToString:String,ToInteger:x=>parseInt(x,10),Char:(s,i)=>String(s)[i],FCS:v=>fcOut(v)};
const fcJs=e=>String(e).replace(/"[^"]*"|\b(mod|and|or|not)\b|<>|!=|==|<=|>=|=|&|\^/g,m=>m[0]==='"'?m:({mod:'%',and:'&&',or:'||',not:'!','<>':'!=','!=':'!=','==':'==','<=':'<=','>=':'>=','=':'==','&':'+','^':'**'})[m]);
/* & (gabung teks) dipecah di tingkat teratas agar angka dan array diformat rapi */
function fcCat(e){const p=[];let d=0,q=false,b=0;e=String(e);for(let i=0;i<e.length;i++){const c=e[i];if(c==='"')q=!q;else if(!q){if(c==='('||c==='[')d++;else if(c===')'||c===']')d--;else if(c==='&'&&!d){p.push(e.slice(b,i));b=i+1}}}p.push(e.slice(b));return p}
const fcEv=(S,e)=>{const p=fcCat(e),js=p.length>1?p.map(x=>'FCS('+fcJs(x)+')').join('+'):fcJs(e);return Function('S','F','with(F)with(S){return ('+js+')}')(S,FCF)};
const fcSet=(S,lhs,v)=>Function('S','F','v','with(F)with(S){'+lhs+'=v}')(S,FCF,v);
const fcFmt=v=>v===undefined?'—':Array.isArray(v)?'['+v.map(fcFmt).join(', ')+']':typeof v==='string'?'"'+v+'"':typeof v==='number'&&!Number.isInteger(v)?String(Math.round(v*1000)/1000):String(v);
const fcOut=v=>Array.isArray(v)?'['+v.map(fcOut).join(', ')+']':typeof v==='number'&&!Number.isInteger(v)?String(Math.round(v*1000)/1000):String(v);
function fcIds(list,c){list.forEach(n=>{n.id='n'+(c.k++);['y','n','b'].forEach(k=>Array.isArray(n[k])&&fcIds(n[k],c))})}
const fcLabel=n=>({dec:()=>`${n.ty} ${n.v}${n.arr?'['+n.arr+']':''}`,in:()=>`Input ${n.v}`,asg:()=>`${n.v} = ${n.e}`,out:()=>`Output ${n.e}`,
  if:()=>n.c,while:()=>n.c,do:()=>n.c,for:()=>`${n.v} = ${n.a} to ${n.z}${n.s&&n.s!=='1'?' step '+n.s:''}`})[n.t]();

/* ---------- pseudocode ---------- */
function fcPseudo(fc){
  const L=[],at={};const em=(d,s,id)=>{if(id)at[id]=L.length;L.push({d,s,id})};
  const ex=e=>String(e).replace(/"[^"]*"|\s&\s/g,m=>m[0]==='"'?m:', ');
  em(0,'START','s');
  const walk=(list,d)=>list.forEach(n=>{
    if(n.t==='dec')em(d,`DECLARE ${n.v} : ${n.arr?`ARRAY[${n.arr}] OF `:''}${n.ty.toUpperCase()}`,n.id);
    else if(n.t==='in')em(d,`INPUT ${n.v}`,n.id);
    else if(n.t==='asg')em(d,`${n.v} ← ${n.e}`,n.id);
    else if(n.t==='out')em(d,`OUTPUT ${ex(n.e)}`,n.id);
    else if(n.t==='if'){em(d,`IF ${n.c} THEN`,n.id);walk(n.y,d+1);if(n.n.length){em(d,'ELSE');walk(n.n,d+1)}em(d,'ENDIF')}
    else if(n.t==='while'){em(d,`WHILE ${n.c} DO`,n.id);walk(n.b,d+1);em(d,'ENDWHILE')}
    else if(n.t==='for'){em(d,`FOR ${n.v} ← ${n.a} TO ${n.z}${n.s&&n.s!=='1'?' STEP '+n.s:''} DO`,n.id);walk(n.b,d+1);em(d,'ENDFOR')}
    else if(n.t==='do'){em(d,'REPEAT');walk(n.b,d+1);em(d,`UNTIL ${n.u||'NOT ('+n.c+')'}`,n.id)}
  });
  walk(fc.p,1);em(0,'END','e');
  return {L,at};
}

/* ---------- menjalankan program ---------- */
function fcRun(fc,inputs){
  const S={},T={},out=[],inp=[...inputs],F=[];let g=0;
  const snap=(id,note)=>F.push({id,note,vars:Object.keys(T).map(k=>[k,T[k],fcFmt(S[k])]),out:out.slice()});
  const base=v=>T[String(v).split('[')[0].trim()]||'';
  const coerce=(ty,v)=>/^Integer/.test(ty)&&typeof v==='number'?Math.trunc(v):v;
  const run=list=>{for(const n of list){if(++g>1500)throw new Error('Program berputar terlalu lama (lebih dari 1500 langkah). Periksa kondisi berhentinya.');step(n)}};
  const step=n=>{
    if(n.t==='dec'){n.v.split(',').map(s=>s.trim()).forEach(v=>{T[v]=n.ty+(n.arr?'[]':'');S[v]=n.arr?Array(fcEv(S,n.arr)).fill(undefined):undefined});snap(n.id,`Menyiapkan variabel <b>${esc(n.v)}</b> bertipe ${n.ty}${n.arr?' (array)':''}. Isinya belum ada.`)}
    else if(n.t==='in'){const raw=inp.length?inp.shift():'0',ty=base(n.v);let v=raw;if(/^Integer/.test(ty))v=parseInt(raw,10)||0;else if(/^Real/.test(ty))v=parseFloat(raw)||0;else if(/^Boolean/.test(ty))v=/^(true|benar|1)$/i.test(raw);
      fcSet(S,n.v,v);snap(n.id,`Pengguna mengetik <b>${esc(raw)}</b>, disimpan ke <b>${esc(n.v)}</b>.`)}
    else if(n.t==='asg'){const v=coerce(base(n.v),fcEv(S,n.e));fcSet(S,n.v,v);snap(n.id,`Hitung <code>${esc(n.e)}</code> = <b>${esc(fcFmt(v))}</b>, simpan ke <b>${esc(n.v)}</b>.`)}
    else if(n.t==='out'){const v=fcOut(fcEv(S,n.e));out.push(v);snap(n.id,`Tampilkan ke layar: <b>${esc(v)}</b>`)}
    else if(n.t==='if'){const c=!!fcEv(S,n.c);snap(n.id,`Periksa <code>${esc(n.c)}</code> → <b>${c?'benar':'salah'}</b>, jalur ${c?'Benar (kanan)':'Salah (kiri)'} dipilih.`);run(c?n.y:n.n)}
    else if(n.t==='while'){for(;;){const c=!!fcEv(S,n.c);snap(n.id,`Periksa <code>${esc(n.c)}</code> → <b>${c?'benar':'salah'}</b>. ${c?'Masuk ke badan loop.':'Loop selesai, lanjut ke bawah.'}`);if(!c)break;run(n.b)}}
    else if(n.t==='for'){const st=n.s?fcEv(S,n.s):1;fcSet(S,n.v,fcEv(S,n.a));for(;;){const z=fcEv(S,n.z),c=st>0?S[n.v]<=z:S[n.v]>=z;
      snap(n.id,`${esc(n.v)} = ${esc(fcFmt(S[n.v]))}. ${c?`Masih ${st>0?'≤':'≥'} ${esc(fcFmt(z))}, jalankan badan loop.`:`Sudah melewati ${esc(fcFmt(z))}, loop selesai.`}`);if(!c)break;run(n.b);S[n.v]+=st}}
    else if(n.t==='do'){for(;;){run(n.b);const c=!!fcEv(S,n.c);snap(n.id,`Badan loop sudah jalan, baru periksa <code>${esc(n.c)}</code> → <b>${c?'benar':'salah'}</b>. ${c?'Ulangi.':'Selesai.'}`);if(!c)break}}
  };
  snap('s','Program dimulai.');
  try{run(fc.p);snap('e','Program selesai.')}catch(e){F.push({id:'e',note:`<span class="err">${esc(e.message)}</span>`,vars:F[F.length-1].vars,out:out.slice(),err:1})}
  return F;
}

/* ---------- tata letak flowchart ---------- */
const FC_CW=7.2,FC_H=36,FC_G=26;
function fcLay(list){
  const it=list.map(fcNode);let l=0,r=0,h=0;it.forEach((x,k)=>{l=Math.max(l,x.l);r=Math.max(r,x.r);h+=x.h+(k?FC_G:0)});
  return {l,r,h,draw(cx,y,o){let yy=y;it.forEach((x,k)=>{if(k){o.push(`<path class="fc-ln" d="M${cx} ${yy} V${yy+FC_G-2}" marker-end="url(#fcA)"/>`);yy+=FC_G}x.draw(cx,yy,o);yy+=x.h})}};
}
function fcShape(kind,id,cx,y,w,h,txt){
  const x=cx-w/2;let s;
  if(kind==='pill')s=`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${h/2}"/>`;
  else if(kind==='para')s=`<polygon points="${x+10},${y} ${x+w},${y} ${x+w-10},${y+h} ${x},${y+h}"/>`;
  else if(kind==='dia')s=`<polygon points="${cx},${y} ${x+w},${y+h/2} ${cx},${y+h} ${x},${y+h/2}"/>`;
  else if(kind==='hex')s=`<polygon points="${x+12},${y} ${x+w-12},${y} ${x+w},${y+h/2} ${x+w-12},${y+h} ${x+12},${y+h} ${x},${y+h/2}"/>`;
  else if(kind==='dec')s=`<rect x="${x}" y="${y}" width="${w}" height="${h}"/><path class="fc-in" d="M${x+6} ${y} V${y+h} M${x} ${y+6} H${x+w}"/>`;
  else s=`<rect x="${x}" y="${y}" width="${w}" height="${h}"/>`;
  return `<g class="fc-s fc-${kind}" data-id="${id}">${s}<text x="${cx+(kind==='dec'?3:0)}" y="${y+h/2+4}">${esc(txt)}</text></g>`;
}
function fcNode(n){
  const txt=n.t==='s'?'Mulai':n.t==='e'?'Selesai':fcLabel(n),tw=txt.length*FC_CW;
  if(['s','e','dec','in','out','asg'].includes(n.t)){
    const kind={s:'pill',e:'pill',dec:'dec',in:'para',out:'para',asg:'rect'}[n.t],w=Math.max(n.t==='s'||n.t==='e'?90:96,tw+(kind==='para'?40:28));
    return {l:w/2,r:w/2,h:FC_H,draw:(cx,y,o)=>o.push(fcShape(kind,n.id,cx,y,w,FC_H,txt))};
  }
  const dw=Math.max(112,tw*1.3+44),dh=n.t==='for'?FC_H+4:50,kind=n.t==='for'?'hex':'dia',dwf=n.t==='for'?Math.max(110,tw+40):dw;
  if(n.t==='if'){
    const Y=fcLay(n.y),N=fcLay(n.n),oR=Math.max(dwf/2+16,Y.l+16),oL=Math.max(dwf/2+16,N.r+16);
    const l=Math.max(dwf/2,oL+N.l),r=Math.max(dwf/2,oR+Y.r),bh=Math.max(Y.h,N.h),h=dh+14+bh+(bh?18:4)+4;
    return {l,r,h,draw(cx,y,o){
      const my=y+dh/2,yb=y+dh+14,ym=yb+bh+(bh?18:4),xr=cx+oR,xl=cx-oL;
      o.push(fcShape(kind,n.id,cx,y,dwf,dh,txt));
      [[Y,xr,cx+dwf/2,'Benar','start'],[N,xl,cx-dwf/2,'Salah','end']].forEach(([B,xx,cor,lab,an])=>{
        o.push(`<text class="fc-lb" x="${cor+(an==='start'?6:-6)}" y="${my-6}" text-anchor="${an}">${lab}</text>`);
        if(B.h){o.push(`<path class="fc-ln" d="M${cor} ${my} H${xx} V${yb-2}" marker-end="url(#fcA)"/>`);B.draw(xx,yb,o);o.push(`<path class="fc-ln" d="M${xx} ${yb+B.h} V${ym} H${cx}"/>`)}
        else o.push(`<path class="fc-ln" d="M${cor} ${my} H${xx} V${ym} H${cx}"/>`)});
      o.push(`<circle class="fc-dot" cx="${cx}" cy="${ym}" r="4"/>`)}};
  }
  const B=fcLay(n.b),l=Math.max(dwf/2,B.l)+22,r=Math.max(dwf/2,B.r)+22;
  if(n.t==='do'){
    const h=20+B.h+(B.h?20:0)+dh+16;
    return {l,r,h,draw(cx,y,o){
      const yb=y+20,yd=yb+B.h+(B.h?20:0),xl=cx-l+4;
      o.push(`<circle class="fc-dot" cx="${cx}" cy="${y+6}" r="4"/>`);
      if(B.h){o.push(`<path class="fc-ln" d="M${cx} ${y+10} V${yb-2}" marker-end="url(#fcA)"/>`);B.draw(cx,yb,o);o.push(`<path class="fc-ln" d="M${cx} ${yb+B.h} V${yd-2}" marker-end="url(#fcA)"/>`)}
      o.push(fcShape(kind,n.id,cx,yd,dwf,dh,txt));
      o.push(`<path class="fc-ln" d="M${cx-dwf/2} ${yd+dh/2} H${xl} V${y+6} H${cx-6}" marker-end="url(#fcA)"/><text class="fc-lb" x="${cx-dwf/2-6}" y="${yd+dh/2-6}" text-anchor="end">Benar</text>`);
      o.push(`<path class="fc-ln" d="M${cx} ${yd+dh} V${yd+dh+16}"/><text class="fc-lb" x="${cx+6}" y="${yd+dh+13}">Salah</text>`)}};
  }
  const h=dh+20+B.h+(B.h?14:0)+20;
  return {l,r,h,draw(cx,y,o){
    const my=y+dh/2,yb=y+dh+20,y1=yb+B.h+(B.h?14:0),xl=cx-l+4,xr=cx+r-4,ye=y1+18;
    o.push(fcShape(kind,n.id,cx,y,dwf,dh,txt));
    if(B.h){o.push(`<path class="fc-ln" d="M${cx} ${y+dh} V${yb-2}" marker-end="url(#fcA)"/>`);B.draw(cx,yb,o);o.push(`<path class="fc-ln" d="M${cx} ${yb+B.h} V${y1}"/>`)}
    else o.push(`<path class="fc-ln" d="M${cx} ${y+dh} V${y1}"/>`);
    o.push(`<path class="fc-ln" d="M${cx} ${y1} H${xl} V${my} H${cx-dwf/2-2}" marker-end="url(#fcA)"/>`);
    o.push(`<path class="fc-ln" d="M${cx+dwf/2} ${my} H${xr} V${ye} H${cx}"/>`);
    const lt=n.t==='for'?['Ulangi','Selesai']:['Benar','Salah'];
    o.push(`<text class="fc-lb" x="${cx+6}" y="${y+dh+14}">${lt[0]}</text><text class="fc-lb" x="${cx+dwf/2+6}" y="${my-6}">${lt[1]}</text>`)}};
}
function fcSVG(fc){
  const all=fcLay([{t:'s',id:'s'},...fc.p,{t:'e',id:'e'}]),P=14,W=Math.ceil(all.l+all.r+P*2),H=Math.ceil(all.h+P*2),o=[];
  all.draw(P+all.l,P,o);
  return `<svg class="fc-svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Flowchart program ${esc(fc.name||'')}"><defs><marker id="fcA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" class="fc-ah"/></marker></defs>${o.join('')}</svg>`;
}

function fcViz(host,{lesson}){
  const fc=lesson.fc;if(!fc)return;
  const c={k:1};fcIds(fc.p,c);
  const ps=fcPseudo(fc),hasIn=fc.in&&fc.in.length;
  host.innerHTML=`${hasIn?`<div class="fc-inp"><label for="fcIn">Input untuk program (pisahkan dengan koma)</label><div class="fc-inr"><input class="inp" id="fcIn" value="${esc(fc.in.join(', '))}" autocomplete="off"><button class="btn" id="fcGo">Jalankan dengan input ini</button></div></div>`:''}
  <div class="fc-grid"><div class="fc-cw"><div class="fc-tools"><span class="fc-hint">Geser untuk melihat seluruh flowchart.</span><button class="tlink" data-fit aria-pressed="false">Muat ke lebar layar</button></div><div class="fc-chart" tabindex="0" role="region" aria-label="Flowchart, bisa digeser">${fcSVG(fc)}</div></div>
  <div class="fc-side"><div class="fc-box"><div class="eyebrow">Pseudocode</div><ol class="fc-ps">${ps.L.map((x,i)=>`<li data-i="${i}"><span style="padding-left:${x.d*1.4}em">${esc(x.s)}</span></li>`).join('')}</ol></div>
  <div class="fc-box"><div class="eyebrow">Variabel</div><div class="fc-vars"></div></div>
  <div class="fc-box"><div class="eyebrow">Layar keluaran</div><pre class="fc-con"></pre></div></div></div><div class="fc-play"></div>`;
  const chart=$('.fc-chart',host),lines=[...host.querySelectorAll('.fc-ps li')],vars=$('.fc-vars',host),con=$('.fc-con',host);
  let prev=null;
  const fit=$('[data-fit]',host),tools=$('.fc-tools',host),svg=$('.fc-svg',host);
  const chk=()=>{const over=svg.getBoundingClientRect().width>chart.clientWidth+2||chart.classList.contains('fit');tools.hidden=!over};
  fit.onclick=()=>{const on=chart.classList.toggle('fit');fit.setAttribute('aria-pressed',on);fit.textContent=on?'Ukuran asli':'Muat ke lebar layar'};
  requestAnimationFrame(chk);if(window.ResizeObserver)new ResizeObserver(chk).observe(chart);
  const draw=(st,f)=>{
    host.querySelectorAll('.fc-s.on').forEach(g=>g.classList.remove('on'));
    const g=host.querySelector(`.fc-s[data-id="${f.id}"]`);if(g){g.classList.add('on');
      const r=g.getBoundingClientRect(),cr=chart.getBoundingClientRect();if(r.top<cr.top||r.bottom>cr.bottom||r.left<cr.left||r.right>cr.right)chart.scrollTo({top:chart.scrollTop+r.top-cr.top-cr.height/2+r.height/2,left:chart.scrollLeft+r.left-cr.left-cr.width/2+r.width/2,behavior:RM()?'auto':'smooth'})}
    lines.forEach(li=>li.classList.toggle('on',ps.at[f.id]===+li.dataset.i));
    const pv=prev&&prev.vars?Object.fromEntries(prev.vars.map(v=>[v[0],v[2]])):{};
    vars.innerHTML=f.vars.length?`<table class="fc-vt"><thead><tr><th scope="col">Nama</th><th scope="col">Tipe</th><th scope="col">Nilai</th></tr></thead><tbody>${f.vars.map(v=>`<tr class="${pv[v[0]]!==undefined&&pv[v[0]]!==v[2]?'chg':''}"><th scope="row">${esc(v[0])}</th><td>${esc(v[1])}</td><td>${esc(v[2])}</td></tr>`).join('')}</tbody></table>`:'<p class="muted">Belum ada variabel.</p>';
    con.textContent=f.out.length?f.out.join('\n'):' ';con.classList.toggle('empty',!f.out.length);
    st.innerHTML='';prev=f;
  };
  const frames=inp=>{prev=null;return fcRun(fc,inp)};
  const pl=player($('.fc-play',host),frames(fc.in||[]),draw,{speed:900});
  const go=$('#fcGo',host);if(go){const ip=$('#fcIn',host);go.onclick=()=>pl.set(frames(ip.value.split(',').map(s=>s.trim()).filter(s=>s!=='')));ip.onkeydown=e=>{if(e.key==='Enter'){e.preventDefault();go.click()}}}
}

/* ---------- memilih jenis loop ---------- */
function loopPickViz(host){
  const Q=[['Mencetak nomor kursi 1 sampai 40','for','Jumlah putaran sudah pasti: 40.'],
    ['Meminta PIN sampai benar','do','Pertanyaan harus muncul minimal sekali, lalu diulang selama PIN salah.'],
    ['Menabung sampai saldo mencapai Rp1.000.000','while','Kita tidak tahu berapa minggu; yang diketahui hanya kondisi berhentinya.'],
    ['Menjumlahkan semua harga di keranjang','each','Kita hanya perlu membaca setiap isi koleksi, tidak butuh nomor indeksnya.'],
    ['Menukar dua angka bersebelahan selama masih ada yang tertukar (bubble sort)','while','Berhenti saat satu putaran tidak ada pertukaran, jadi jumlah putaran tidak pasti.'],
    ['Menampilkan menu kasir sampai pengguna memilih Keluar','do','Menu tampil dulu, baru dicek pilihannya.'],
    ['Mencetak tabel perkalian 1 sampai 10','for','Batas awal dan akhir jelas: for bersarang 10 × 10.'],
    ['Membaca baris file sampai habis','while','Jumlah baris tidak diketahui sebelumnya; berhenti saat tidak ada baris lagi.']];
  const N={for:'for',while:'while',do:'do-while',each:'for-each'};let i=0,sc=0;
  const show=()=>{const q=Q[i];host.innerHTML=`<div class="lp"><p class="lp-c">Kasus ${i+1} dari ${Q.length}</p><p class="lp-q">${esc(q[0])}</p><div class="lp-o" role="group" aria-label="Pilih jenis loop">${Object.keys(N).map(k=>`<button class="btn" data-k="${k}">${N[k]}</button>`).join('')}</div><div class="lp-fb" aria-live="polite"></div></div>`;
    host.querySelector('.lp-o').onclick=e=>{const b=e.target.closest('button');if(!b)return;const ok=b.dataset.k===q[1];if(ok)sc++;
      host.querySelectorAll('.lp-o button').forEach(x=>{x.disabled=true;if(x.dataset.k===q[1])x.classList.add('ok');else if(x===b)x.classList.add('bad')});
      $('.lp-fb',host).innerHTML=`<div class="tk-fb ${ok?'ok':'bad'}"><b>${ok?'✓ Tepat.':'Kurang tepat.'}</b> Pilihan terbaik: <b>${N[q[1]]}</b>. ${esc(q[2])}</div><div class="sl-act"><button class="btn primary" id="lpN">${i<Q.length-1?'Kasus berikutnya':'Lihat skor'}</button></div>`;
      $('#lpN',host).onclick=()=>{i++;if(i<Q.length)show();else{host.innerHTML=`<div class="lp"><p class="lp-q">Skor: ${sc} dari ${Q.length}</p><p class="muted">${sc>=7?'Bagus! Kamu sudah bisa memilih loop sesuai kebutuhan.':'Baca lagi tabel ringkas di atas, lalu coba sekali lagi.'}</p><button class="btn" id="lpR">Ulangi</button></div>`;$('#lpR',host).onclick=()=>{i=0;sc=0;show()}}}}};
  show();
}
Object.assign(VIZ2,{fc:fcViz,looppick:loopPickViz});
Object.assign(VIZ2T,{fc:'Simulator flowchart dan pseudocode',looppick:'Pilih loop yang tepat'});

;/* ===================== VISUAL 3D DI PELAJARAN =====================
   Adegan 3D ringan (CSS 3D, tanpa pustaka) yang menjelaskan konsep dengan benda:
   kotak variabel, deretan array, tumpukan stack, pohon, cetak biru class, lapisan box model, dll.
   Setiap adegan = daftar langkah; tiap langkah berisi keterangan dan benda-benda di panggung.
   Benda dengan id yang sama berpindah dengan animasi, sehingga perubahan mudah diikuti.
   Panggung bisa diputar dengan diseret atau tombol panah; tombol Berikutnya menjalankan langkah. */
(function(){
const RMq=()=>{try{return matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){return false}};
/* pembuat benda: B = balok, G = label melayang (selalu menghadap kamera), R = batang penghubung */
const B=(id,x,y,z,o={})=>({id,x,y,z,w:1,h:1,d:1,c:'acc',...o});
const G=(id,x,y,z,t,c='')=>({id,tag:1,x,y,z,t,c});
function R(id,a,b,c='mute'){const dx=b[0]-a[0],dy=b[1]-a[1],L=Math.hypot(dx,dy);
  return {id,x:(a[0]+b[0])/2,y:(a[1]+b[1])/2,z:a[2]||0,w:L,h:.08,d:.08,c,rz:Math.atan2(dy,dx)*180/Math.PI,rod:1}}
const lantai=(w=8,d=4,y=-.6)=>B('lantai',0,y,0,{w,h:.12,d,c:'floor'});

const S={};
/* Setiap adegan: t = judul, p = parameter yang bisa diubah pengguna (panel Eksperimen),
   steps(P) = daftar langkah yang dihitung ulang dari nilai parameter.
   Jenis parameter: n (angka, min..max), s (teks, daftar dipisah koma), o (pilihan). */
const angka=(s,max=7)=>String(s).split(/[,\s]+/).map(Number).filter(v=>Number.isFinite(v)).map(v=>Math.round(v)).slice(0,max);
const nama=(s,max=5)=>String(s).split(',').map(v=>v.trim().slice(0,8)).filter(Boolean).slice(0,max);
const E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* ---------- variabel ---------- */
S.var={t:'Variabel sebagai kotak berlabel di memori',
 p:[{k:'a',l:'Nilai awal umur',t:'n',min:-99,max:999,v:17},{k:'b',l:'Ditambah',t:'n',min:-99,max:99,v:1},{k:'nm',l:'Isi nama',t:'s',v:'Sari',ph:'teks'}],
 steps:P=>{const a=P.a,b=P.b,c=a+b,nm=E(String(P.nm).slice(0,10)||'""');
  const rak=[lantai(7,3)],kotak=(id,x,n)=>[B('k-'+id,x,0,0,{w:1.6,h:1.2,d:1.4,c:'glass'}),G('n-'+id,x,1.25,0,n)];
  const vU=(id,v,y=-.05,c='acc')=>B(id,-1.9,y,0,{w:.8,h:.8,d:.8,t:String(v),tt:'int',c}),vN=B('vS',1.9,-.05,0,{w:1.3,h:.8,d:.8,c:'ok',t:`"${nm}"`,tt:'teks'});
  return [
   {cap:'Bayangkan memori komputer sebagai rak. Setiap variabel adalah <b>kotak berlabel</b>: labelnya nama variabel, isinya nilai.',it:[...rak]},
   {cap:`<code>umur = ${a}</code> membuat kotak bernama <b>umur</b>, lalu memasukkan nilai ${a} ke dalamnya.`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v0',a)]},
   {cap:`<code>nama = "${nm}"</code> membuat kotak kedua. Setiap kotak hanya menyimpan <b>satu nilai</b> pada satu waktu.`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v0',a),...kotak('nama',1.9,'nama'),vN]},
   {cap:`<code>umur = umur + ${b}</code>: nilai lama <b>diambil</b> dulu untuk dihitung (${a} + ${b})…`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v0',a,2.1,'warn'),G('hit',-1.9,3.1,0,`${a} + ${b} = ${c}`,'warn'),...kotak('nama',1.9,'nama'),vN]},
   {cap:`…lalu hasilnya <b>menggantikan</b> isi lama. Nilai ${a} hilang; kotak umur sekarang berisi <b>${c}</b>. Nama kotaknya tetap sama.`,it:[...rak,...kotak('umur',-1.9,'umur'),vU('v1',c),...kotak('nama',1.9,'nama'),vN]}]}};

/* ---------- array / list ---------- */
S.array={t:'Array: deretan kotak bernomor (indeks)',
 p:[{k:'isi',l:'Isi array (pisahkan koma)',t:'s',v:'7, 3, 9, 1, 5'},{k:'ix',l:'Indeks yang diambil',t:'n',min:-3,max:9,v:3},{k:'add',l:'Nilai yang ditambahkan',t:'n',min:-99,max:999,v:8}],
 steps:P=>{let v=angka(P.isi,6);if(!v.length)v=[0];const L=v.length,ix=P.ix,X=i=>(i-(L)/2)*1.25;
  const row=(hi=-1,extra=[],n=L,vv=v)=>[lantai(Math.max(6,(n+1)*1.3+1),3),...vv.slice(0,n).map((x,i)=>B('a'+i,X(i),i===hi?.5:0,0,{t:String(x),c:hi<0?'acc':i===hi?'warn':'mute'})),...vv.slice(0,n).map((x,i)=>G('i'+i,X(i),-1,0.9,'['+i+']','idx')),...extra];
  const ok=ix>=0&&ix<L,v2=[...v,P.add];
  return [
   {cap:`Array ini menyimpan <b>${L} nilai</b> berurutan dalam satu nama. Setiap kotak punya nomor urut yang disebut <b>indeks</b>.`,it:row()},
   {cap:`Indeks dimulai dari <b>0</b>, bukan 1. Jadi <code>nilai[0]</code> adalah kotak pertama, yaitu ${v[0]}.`,it:row(0)},
   ok?{cap:`<code>nilai[${ix}]</code> adalah kotak ke-${ix+1}, isinya <b>${v[ix]}</b>. Komputer langsung melompat ke kotak itu tanpa memeriksa kotak lain.`,it:row(ix)}
     :{cap:`<code>nilai[${ix}]</code> <b>tidak ada</b>! Indeks yang sah hanya 0 sampai ${L-1}. Java melempar <code>ArrayIndexOutOfBoundsException</code>, Python <code>IndexError</code>${ix<0?' (kecuali Python: indeks negatif dihitung dari belakang, <code>nilai['+ix+']</code> = '+(v[L+ix]??'tetap error')+')':''}.`,
       it:row(-1,[B('ghost',X(ix),.5,0,{t:'?',c:'bad'}),G('err',X(Math.max(0,Math.min(L-1,ix))),2,0,'di luar batas!','bad')])},
   {cap:`Menambah ${P.add} di akhir (<code>append</code>/<code>push</code>/<code>add</code>) menaruh kotak baru di indeks berikutnya, yaitu ${L}.`,it:row(-1,[B('a'+L,X(L),0,0,{t:String(P.add),c:'ok'}),G('i'+L,X(L),-1,0.9,'['+L+']','idx')],L,v2)},
   {cap:`Panjang array sekarang <b>${L+1}</b>, sedangkan indeks terakhirnya <b>${L}</b>. Indeks terakhir selalu panjang − 1.`,it:row(-1,[B('a'+L,X(L),0,0,{t:String(P.add),c:'ok'}),G('i'+L,X(L),-1,0.9,'['+L+']','idx'),G('len',0,1.6,0,`panjang = ${L+1}`,'warn')],L,v2)}]}};

/* ---------- array 2D ---------- */
S.matrix={t:'Array dua dimensi: baris dan kolom',
 p:[{k:'r',l:'Jumlah baris',t:'n',min:1,max:4,v:3},{k:'c',l:'Jumlah kolom',t:'n',min:1,max:5,v:4},{k:'tr',l:'Ambil baris ke-',t:'n',min:0,max:5,v:1},{k:'tc',l:'Ambil kolom ke-',t:'n',min:0,max:6,v:2}],
 steps:P=>{const R3=P.r,C4=P.c,val=(r,c)=>r*C4+c+1,ok=P.tr<R3&&P.tc<C4;
  const grid=f=>{const any=[...Array(R3)].some((_,r)=>[...Array(C4)].some((_,c)=>f(r,c)));return [lantai(C4*1.3+1.4,R3*1.3+1.4),...[...Array(R3*C4)].map((_,k)=>{const r=Math.floor(k/C4),c=k%C4,s=f(r,c);return B('m'+r+'_'+c,(c-(C4-1)/2)*1.3,s?.45:0,(r-(R3-1)/2)*1.3,{t:String(val(r,c)),c:s||(any?'mute':'acc'),h:s?1.3:.6})}),
    ...[...Array(R3)].map((_,r)=>G('r'+r,-(C4/2)*1.3-1.2,0,(r-(R3-1)/2)*1.3,'baris '+r,'idx')),...[...Array(C4)].map((_,c)=>G('c'+c,(c-(C4-1)/2)*1.3,-.4,(R3/2)*1.3+.9,'kolom '+c,'idx'))]};
  const tr=Math.min(P.tr,R3-1),tc=Math.min(P.tc,C4-1);
  return [
   {cap:`Array 2D ini berukuran <b>${R3} × ${C4}</b>: ${R3} baris, masing-masing berisi ${C4} nilai. Total ${R3*C4} sel, seperti denah kursi bioskop.`,it:grid(()=>0)},
   {cap:`Satu baris (<code>m[${tr}]</code>) adalah array biasa berisi ${C4} nilai.`,it:grid(r=>r===tr?'ok':0)},
   {cap:`Satu kolom (kolom ${tc} di setiap baris) diambil dengan perulangan baris: ${[...Array(R3)].map((_,r)=>`<code>m[${r}][${tc}]</code>`).join(', ')}.`,it:grid((r,c)=>c===tc?'warn':0)},
   ok?{cap:`Satu sel ditunjuk dengan <b>dua indeks</b>: baris dulu, lalu kolom. <code>m[${P.tr}][${P.tc}]</code> = <b>${val(P.tr,P.tc)}</b>.`,it:grid((r,c)=>r===P.tr&&c===P.tc?'warn':0)}
     :{cap:`<code>m[${P.tr}][${P.tc}]</code> <b>di luar batas</b>. Baris yang sah 0–${R3-1} dan kolom 0–${C4-1}, jadi program akan error.`,it:[...grid(()=>0),G('err',0,2,0,'di luar batas!','bad')]}]}};

/* ---------- perulangan ---------- */
S.loop={t:'Perulangan sebagai tangga: semua jenis loop',
 p:[{k:'jenis',l:'Jenis perulangan',t:'o',o:[['for','for'],['while','while'],['do','do-while'],['each','for-each'],['nested','bersarang (nested)'],['break','break'],['continue','continue'],['banding','Bandingkan for, while, do-while']],v:'for'},
   {k:'a',l:'Mulai (i = …)',t:'n',min:-3,max:10,v:0},{k:'z',l:'Batas (i < …)',t:'n',min:-3,max:20,v:4},{k:'s',l:'Langkah (i += …)',t:'n',min:1,max:5,v:1},
   {k:'b',l:'break saat i = … (jenis break)',t:'n',min:-3,max:20,v:2}],
 steps:P=>{const vals=[];for(let i=P.a;i<P.z&&vals.length<9;i+=P.s)vals.push(i);const N=vals.length,more=P.a+N*P.s<P.z,end=P.a+N*P.s;
  const X=(k,n=N)=>(k-(Math.max(n,1)-1)/2)*1.3;
  const tangga=(list,st,z=0,pre='s')=>list.map((v,k)=>B(pre+k,X(k,list.length),k*.4-.3,z,{w:1.2,h:.4,d:1.4,c:st(k,v),t:'i='+v}));
  const bola=(id,k,y,z=0,c='warn',n=N)=>B(id,n?X(k,n):0,y,z,{w:.5,h:.5,d:.5,c,ball:1});
  const lt=(n=N,d=3)=>lantai(Math.max(6,n*1.4+2),d);
  const J=P.jenis;
  /* ---- bandingkan tiga jenis berdampingan ---- */
  if(J==='banding'){const nDo=Math.max(1,N),dv=N?vals:[P.a];const lanes=[['for',N,vals,-2.2],['while',N,vals,0],['do-while',nDo,dv,2.2]];
    const pang=(fin)=>[lantai(Math.max(7,Math.max(nDo,1)*1.4+3),7.4),...lanes.flatMap(([nm,n,list,z])=>[G('ln'+nm,X(0,Math.max(nDo,1))-1.9,0,z,nm,'idx'),
      ...list.map((v,k)=>B('s'+nm+k,X(k,Math.max(nDo,1)),k*.4-.3,z,{w:1.2,h:.4,d:1.4,c:fin&&k<n?'ok':'mute',t:'i='+v})),
      B('b'+nm,fin?(n?X(n-1,Math.max(nDo,1)):X(0,Math.max(nDo,1))-1.2):X(0,Math.max(nDo,1))-1.2,fin&&n?(n-1)*.4+.35:0,z,{w:.5,h:.5,d:.5,c:n?'warn':'bad',ball:1}),
      ...(fin?[G('n'+nm,X(Math.max(n,1)-1,Math.max(nDo,1))+.9,Math.max(n,1)*.4+.9,z,n+'×',n?'ok':'bad')]:[])])];
    return [
     {cap:`Tiga loop dengan aturan yang sama: mulai i = ${P.a}, ulang selama i &lt; ${P.z}, langkah ${P.s}. Bedanya hanya <b>kapan kondisi dicek</b>.`,it:pang(false)},
     {cap:N?`Hasil: for dan while sama-sama jalan <b>${N} kali</b>${more?'+':''}, do-while juga ${nDo} kali. Selama kondisi awal benar, ketiganya setara. Sekarang coba ubah <b>Mulai</b> menjadi ≥ ${P.z}.`
        :`Kondisi awal ${P.a} &lt; ${P.z} sudah <b>salah</b>. for dan while mengecek di awal, jadi <b>0 kali</b>. do-while menjalankan badan dulu baru mengecek, jadi tetap <b>1 kali</b>. Inilah beda utamanya.`,it:pang(true)},
     {cap:'Ringkasnya: <b>for</b> untuk jumlah putaran yang pasti, <b>while</b> untuk berhenti karena keadaan, <b>do-while</b> jika badan harus jalan minimal sekali (misalnya menampilkan menu lalu bertanya "ulangi?").',it:pang(true)}]}
  /* ---- for-each ---- */
  if(J==='each'){const data=N?vals.map(v=>v*10):[];const kot=(hi)=>[lt(),...data.map((v,k)=>B('e'+k,X(k),0,0,{w:1,h:1,d:1,c:k<hi?'ok':k===hi?'warn':'mute',t:String(v)})),G('arr',X(0)-1.6,1.2,0,'data','idx')];
    if(!N)return [{cap:'Koleksinya <b>kosong</b>, jadi for-each tidak menjalankan badannya sama sekali. Ubah Mulai dan Batas agar ada isinya.',it:[lt(),G('k',0,.5,0,'[ ] kosong','bad')]}];
    return [{cap:`<code>for (x : data)</code> / <code>for x in data</code>: for-each mengambil <b>isi</b> koleksi satu per satu, tanpa indeks dan tanpa kondisi yang kita tulis. Data berisi ${N} elemen.`,it:kot(-1)},
      ...data.map((v,k)=>({cap:`Putaran ${k+1}: x = <b>${v}</b>. Tidak ada <code>i++</code> yang bisa lupa ditulis, dan tidak mungkin salah indeks.`,it:[...kot(k),B('bola',X(k),.9,0,{w:.5,h:.5,d:.5,c:'warn',ball:1})]})),
      {cap:`Elemen habis, loop berhenti otomatis setelah <b>${N} putaran</b>. Pakai for-each jika hanya perlu membaca setiap isi; pakai for biasa jika butuh nomor indeksnya.`,it:kot(N)}]}
  /* ---- bersarang ---- */
  if(J==='nested'){const R=Math.max(1,Math.min(4,N)),C=3,rows=(N?vals:[P.a]).slice(0,R);
    const grid=(r)=>[lantai(C*1.3+3,R*1.3+2),...rows.flatMap((v,ri)=>[...Array(C)].map((_,c)=>B('g'+ri+'_'+c,(c-1)*1.3,ri<r?0:-.2,(ri-(R-1)/2)*1.3,{w:1,h:ri<r?.8:.3,d:1,c:ri<r?'ok':ri===r?'warn':'mute',t:ri<=r?String(v*(c+1)):''}))),
      ...rows.map((v,ri)=>G('rl'+ri,-3.2,0,(ri-(R-1)/2)*1.3,'luar i='+v,'idx')),...[0,1,2].map(c=>G('cl'+c,(c-1)*1.3,-.4,(R/2)*1.3+.8,'dalam j='+(c+1),'idx'))];
    if(!N)return [{cap:'Loop luar tidak pernah jalan (kondisi awal salah), jadi loop dalam juga tidak pernah jalan.',it:[lantai(6,3),G('k',0,.5,0,'0 × 3 = 0','bad')]}];
    return [{cap:`Loop <b>bersarang</b>: loop luar (i) berjalan ${R} kali, dan di <b>setiap</b> putaran luar, loop dalam (j = 1..3) berjalan sampai habis.`,it:grid(-1)},
      ...rows.map((v,ri)=>({cap:`Putaran luar i = ${v}: loop dalam jalan 3 kali → ${[1,2,3].map(j=>v*j).join(', ')} (i × j). Baru setelah itu i naik.`,it:grid(ri)})),
      {cap:`Total badan loop dalam dijalankan ${R} × 3 = <b>${R*3} kali</b>. Hati-hati: loop bersarang cepat membengkak, 1000 × 1000 = sejuta putaran.`,it:grid(R)}]}
  /* ---- for, while, do-while, break, continue (satu tangga) ---- */
  const dv=J==='do'&&!N?[P.a]:vals,M=dv.length;
  const kode={for:`<code>for (i = ${P.a}; i &lt; ${P.z}; i += ${P.s})</code>`,while:`<code>i = ${P.a}; while (i &lt; ${P.z}) { …; i += ${P.s} }</code>`,do:`<code>i = ${P.a}; do { …; i += ${P.s} } while (i &lt; ${P.z})</code>`,
    break:`<code>for (i = ${P.a}; i &lt; ${P.z}; i += ${P.s}) { if (i == ${P.b}) break; … }</code>`,continue:`<code>for (i = ${P.a}; i &lt; ${P.z}; i += ${P.s}) { if (i % 2 == 0) continue; … }</code>`}[J]||'';
  if(!M)return [{cap:`${kode}: kondisi awal <code>${P.a} &lt; ${P.z}</code> sudah <b>salah</b>, jadi badan <b>tidak pernah dijalankan</b> (0 putaran).${J==='while'||J==='for'?' Coba jenis do-while dengan angka yang sama: badannya tetap jalan sekali.':''}`,it:[lt(),bola('bola',0,0),G('cek',0,1.3,0,`${P.a} < ${P.z} salah`,'bad')]}];
  const stopAt=J==='break'?dv.indexOf(P.b):-1;
  const warna=(n,cur)=>(k,v)=>J==='continue'&&k<n&&v%2===0?'mute':J==='break'&&stopAt>=0&&k>=stopAt?(k<n?'bad':'mute'):k<n?'ok':'mute';
  const st=[{cap:J==='do'?`${kode}: do-while langsung menjalankan badan <b>tanpa mengecek</b> dulu. Kondisi baru diperiksa di akhir setiap putaran.`
     :`${kode}: ${J==='while'?'while mengecek kondisi <b>sebelum</b> setiap putaran.':J==='break'?`loop ini akan <b>berhenti paksa</b> saat i = ${P.b}.`:J==='continue'?'angka genap akan <b>dilewati</b>, tetapi loop tetap lanjut.':'for menulis nilai awal, kondisi, dan perubahan dalam satu baris.'} Nilai i: ${dv.join(', ')}${more?', …':''}.`,
     it:[lt(M),...tangga(dv,warna(0)),bola('bola',-1.2,0,0,'warn',M),G('cek',X(0,M)-1.2,1.4,0,'i = '+P.a,'warn')]}];
  for(let k=0;k<M;k++){const v=dv[k];
    if(J==='break'&&v===P.b){st.push({cap:`i = ${v}: kondisi <code>i == ${P.b}</code> benar, jadi <b>break</b>. Loop langsung berhenti walaupun <code>i &lt; ${P.z}</code> masih benar. Sisa tangga tidak pernah dinaiki.`,it:[lt(M),...tangga(dv,warna(k+1)),bola('bola',k,k*.4+.35,0,'bad',M),G('cek',X(k,M),k*.4+1.5,0,'break! keluar','bad')]});return st}
    const skip=J==='continue'&&v%2===0;
    const ket=J==='do'&&k===0?`Putaran 1: badan dijalankan <b>dulu</b> (i = ${v}), baru dicek: <code>${v+P.s} &lt; ${P.z}</code> → <b>${v+P.s<P.z}</b>.${N?'':' Kondisinya salah, tetapi badan sudah terlanjur jalan sekali.'}`
      :skip?`Putaran ${k+1}: i = ${v} genap, jadi <b>continue</b>: sisa badan dilewati, langsung ke putaran berikutnya.`
      :`Putaran ${k+1}: cek <code>i &lt; ${P.z}</code> → ${v} &lt; ${P.z} <b>benar</b>, badan dijalankan, lalu <code>i += ${P.s}</code> menjadi ${v+P.s}.`;
    st.push({cap:ket,it:[lt(M),...tangga(dv,warna(k+1)),bola('bola',k,k*.4+.35,0,skip?'mute':'warn',M),G('cek',X(k,M),k*.4+1.5,0,skip?`i = ${v} dilewati`:`i = ${v} → ${v+P.s}`,skip?'idx':'warn')]})}
  const jalan=J==='continue'?dv.filter(v=>v%2!==0).length:M;
  st.push(more?{cap:`(Tangga dipotong di 9 putaran agar muat di layar; perulangan sebenarnya masih berlanjut sampai i ≥ ${P.z}.)`,it:[lt(M),...tangga(dv,warna(M)),bola('bola',M-1,(M-1)*.4+.35,0,'warn',M)]}
   :{cap:`Cek lagi: <code>i &lt; ${P.z}</code> → ${J==='do'&&!N?P.a+P.s:end} &lt; ${P.z} <b>salah</b>. Perulangan berhenti. ${J==='continue'?`Ada ${M} putaran, tetapi badan hanya benar-benar bekerja <b>${jalan} kali</b> (angka ganjil).`:`Total <b>${M} putaran</b>.`}${J==='break'?` Angka ${P.b} tidak pernah muncul, jadi break tidak terpicu.`:''}`,
     it:[lt(M),...tangga(dv,warna(M)),bola('bola',M,M*.4+.2,0,'warn',M),G('cek',X(M-1,M)+.6,M*.4+1.6,0,'salah → keluar','bad')]});
  return st}};

/* ---------- percabangan ---------- */
S.if={t:'Percabangan: jalan bercabang yang dipilih oleh kondisi',
 p:[{k:'n',l:'Nilai siswa',t:'n',min:0,max:100,v:80},{k:'b',l:'Batas lulus (≥)',t:'n',min:0,max:100,v:75}],
 steps:P=>{const lulus=P.n>=P.b;
  const jalan=(on)=>[lantai(9,5),B('j0',-2.6,-.45,0,{w:3,h:.1,d:1,c:'mute'}),B('jy',1.9,-.45,-1.3,{w:3.2,h:.1,d:.9,c:on==='y'?'ok':'mute',ry:-20}),B('jn',1.9,-.45,1.3,{w:3.2,h:.1,d:.9,c:on==='n'?'bad':'mute',ry:20}),
    B('gerbang',-.6,.3,0,{w:.9,h:1.5,d:1.4,c:'glass',t:'≥ '+P.b+'?'}),G('ya',2.6,.5,-2,'ya: "Lulus"','ok'),G('tidak',2.6,.5,2,'tidak: "Remedial"','bad')];
  const bola=(x,y,z,c)=>B('bola',x,y-.05,z,{w:.7,h:1.3,d:.5,c,s:'orang',t:String(P.n)});
  return [
   {cap:`<code>if (nilai &gt;= ${P.b})</code> seperti persimpangan. Program tiba di gerbang kondisi lalu memilih <b>satu</b> jalan saja.`,it:[...jalan(),bola(-3.8,0,0,'warn')]},
   {cap:`nilai = ${P.n}. Kondisi <code>${P.n} &gt;= ${P.b}</code> bernilai <b>${lulus}</b>…`,it:[...jalan(),bola(-.6,1.4,0,'warn')]},
   lulus?{cap:'…maka program masuk ke cabang <b>if</b> dan mencetak "Lulus". Cabang else dilewati sama sekali.',it:[...jalan('y'),bola(3,0,-1.7,'ok')]}
        :{cap:'…maka program masuk ke cabang <b>else</b> dan mencetak "Remedial". Cabang if dilewati sama sekali.',it:[...jalan('n'),bola(3,0,1.7,'bad')]},
   {cap:`Coba ubah angkanya di panel Eksperimen. ${P.n===P.b?'Perhatikan: nilai <b>sama dengan</b> batas tetap lulus karena operatornya <code>&gt;=</code>. Dengan <code>&gt;</code> hasilnya akan berbeda.':'Uji juga nilai yang <b>persis sama</b> dengan batas, karena di situlah bug sering bersembunyi.'}`,it:[...jalan(lulus?'y':'n'),bola(3,0,lulus?-1.7:1.7,lulus?'ok':'bad')]}]}};

/* ---------- logika boolean ---------- */
S.bool={t:'Logika boolean: dua saklar masuk ke gerbang logika',
 p:[{k:'p',l:'p',t:'o',o:[['1','true'],['0','false']],v:'1'},{k:'q',l:'q',t:'o',o:[['1','true'],['0','false']],v:'0'},
   {k:'op',l:'Operator',t:'o',o:[['and','AND (&&)'],['or','OR (||)'],['not','NOT (!p)'],['xor','XOR (^)']],v:'and'}],
 steps:P=>{const p=String(P.p)==='1',q=String(P.q)==='1',op=P.op;
  const f=(a,b)=>op==='and'?a&&b:op==='or'?a||b:op==='not'?!a:a!==b;
  const r=f(p,q),sym={and:'&&',or:'||',not:'!',xor:'^'}[op],nm={and:'AND',or:'OR',not:'NOT',xor:'XOR'}[op];
  const pakaiQ=op!=='not',sc=(op==='and'&&!p)||(op==='or'&&p);
  const ekspr=op==='not'?`!${p}`:`${p} ${sym} ${q}`;
  const kol=v=>v?'ok':'bad';
  const pang=(st)=>{const qOn=pakaiQ&&!(st>=1&&sc);return [lantai(9,4),
    B('pin',-3.2,1.1,0,{w:1.5,h:.7,d:.9,c:st>=1?kol(p):'acc',t:'p = '+p}),
    B('qin',-3.2,-.1,0,{w:1.5,h:.7,d:.9,c:!pakaiQ?'mute':st>=1&&sc?'mute':st>=1?kol(q):'acc',t:pakaiQ?(st>=1&&sc?'q dilewati':'q = '+q):'q (tak dipakai)'}),
    R('rp',[-2.45,1.1,0],[-.75,.6,0],st>=1?kol(p):'mute'),R('rq',[-2.45,-.1,0],[-.75,.4,0],qOn&&st>=1?kol(q):'mute'),
    B('gate',0,.5,0,{w:1.5,h:1.5,d:1.2,c:'glass',t:nm}),R('ro',[.75,.5,0],[2.35,.5,0],st>=2?kol(r):'mute'),
    B('out',3.1,.5,0,{w:1.5,h:.8,d:.9,c:st>=2?kol(r):'mute',t:st>=2?String(r):'?'})]};
  const rows=op==='not'?[[true],[false]]:[[true,true],[true,false],[false,true],[false,false]];
  const tabel=()=>{const cols=op==='not'?['p','!p']:['p','q',nm],x0=-(cols.length-1)*.8;
    return [lantai(7,3),...cols.map((c,j)=>G("h"+j,x0+j*1.6,2.65,0,c,"idx")),
     ...rows.flatMap((row,i)=>{const hasil=f(row[0],row[1]),cur=row[0]===p&&(op==='not'||row[1]===q),vals=[...row,hasil];
      return vals.map((v,j)=>B('t'+i+'_'+j,x0+j*1.6,1.9-i*.75,0,{w:1.4,h:.48,d:.3,c:cur?kol(v):'mute',t:String(v)}))})]};
  const nTrue=rows.filter(rw=>f(rw[0],rw[1])).length;
  return [
   {cap:op==='not'?`<b>NOT</b> hanya butuh satu masukan: ia membalik nilai p.`:`Dua masukan boolean, <b>p</b> dan <b>q</b>, masuk ke gerbang <b>${nm}</b> (<code>${sym}</code>). Hasilnya juga boolean: true atau false.`,it:pang(0)},
   {cap:op==='not'?`p = ${p}. q tidak dipakai sama sekali.`:sc?`p = ${p} sudah menentukan hasil ${nm}, jadi q <b>tidak dicek</b>. Inilah <b>short-circuit</b>: ${op==='and'?'AND langsung false jika sisi kiri false':'OR langsung true jika sisi kiri true'}.`
      :`p = ${p} belum cukup untuk menentukan hasil, jadi q = ${q} ikut dicek.${op==='xor'?' XOR selalu butuh kedua sisi.':''}`,it:pang(1)},
   {cap:`<code>${ekspr}</code> menghasilkan <b>${r}</b>. ${op==='and'?'AND hanya true jika kedua sisi true.':op==='or'?'OR true jika minimal satu sisi true.':op==='xor'?'XOR true jika kedua sisi berbeda.':'NOT membalik nilai.'}`,it:pang(2)},
   {cap:`Tabel kebenaran ${nm}: hasil true di <b>${nTrue} dari ${rows.length}</b> baris. Baris berwarna adalah nilai p${op==='not'?'':' dan q'} yang sedang kamu pilih. Ubah nilainya di panel Eksperimen.`,it:tabel()}]}};

/* ---------- bilangan acak ---------- */
/* generator acak semu kecil (mulberry32): seed sama selalu memberi urutan yang sama */
const prng=seed=>{let a=(seed>>>0)||1;return ()=>{a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return ((t^t>>>14)>>>0)/4294967296}};
S.acak={t:'Bilangan acak: dari desimal 0..1 menjadi angka dadu',
 p:[{k:'a',l:'Batas bawah',t:'n',min:-5,max:20,v:1},{k:'b',l:'Batas atas (ikut)',t:'n',min:-5,max:30,v:6},
   {k:'n',l:'Jumlah lemparan',t:'n',min:1,max:30,v:12},{k:'seed',l:'Seed',t:'n',min:0,max:9999,v:42}],
 steps:P=>{let lo=Math.min(P.a,P.b),hi=Math.max(P.a,P.b),pot=false;if(hi-lo+1>10){hi=lo+9;pot=true}
  const K=hi-lo+1,rnd=prng(P.seed),rs=Array.from({length:P.n},()=>rnd()),hs=rs.map(r=>Math.floor(r*K)+lo);
  const X=k=>(k-(K-1)/2)*1.1,r0=rs[0],h0=hs[0],idx=h0-lo;
  const garis=()=>[B('gr',0,1.9,0,{w:6,h:.12,d:.3,c:'mute'}),G('g0',-3,2.4,0,'0','idx'),G('g1',3,2.4,0,'1 (tak pernah)','idx')];
  const kotak=(hl)=>Array.from({length:K},(_,k)=>B('k'+k,X(k),-.2,0,{w:1,h:.5,d:1,c:k===hl?'ok':'acc',t:String(lo+k)}));
  const cnt=Array(K).fill(0);hs.forEach(h=>cnt[h-lo]++);const mx=Math.max(...cnt,1);
  const tiang=()=>cnt.map((c,k)=>c?B("c"+k,X(k),.05+c/mx*1,0,{w:.8,h:c/mx*2,d:.8,c:'warn',t:String(c)}):null).filter(Boolean);
  const daftar=hs.slice(0,15).join(', ')+(hs.length>15?', …':'');
  const lt=()=>lantai(Math.max(7,K*1.1+2),3);
  return [
   {cap:`Fungsi acak dasar memberi desimal <b>0 ≤ r &lt; 1</b>. Kali ini r = <code>${r0.toFixed(4)}</code>. Angka 0 bisa keluar, tetapi 1 tidak pernah.`,it:[lt(),...garis(),B('bola',-3+r0*6,2.3,0,{w:.45,h:.45,d:.45,c:'warn',ball:1}),...kotak(-1)]},
   {cap:`Rentang ${lo}..${hi} berisi ${K} angka. <code>floor(${r0.toFixed(4)} × ${K})</code> = ${idx}, lalu + ${lo} = <b>${h0}</b>.${pot?' (Visual dibatasi 10 kotak.)':''} Tanpa "+1" pada lebar rentang, angka ${hi} tidak akan pernah keluar.`,it:[lt(),...garis(),B('bola',X(idx),.45,0,{w:.45,h:.45,d:.45,c:'ok',ball:1}),...kotak(idx)]},
   {cap:`${P.n} lemparan: ${daftar}. Tinggi tiang = berapa kali angka itu keluar. Makin banyak lemparan, tingginya makin rata.`,it:[lt(),...kotak(-1),...tiang()]},
   {cap:`Seed ${P.seed} <b>selalu</b> memberi urutan yang sama ini. Ganti seed di panel Eksperimen dan urutannya berubah; kembalikan ke ${P.seed} dan urutannya sama lagi. Inilah cara program diuji ulang dengan hasil acak yang bisa diulang.`,it:[lt(),...kotak(-1),...tiang()]}]}};


/* ===================== SQL & POSTGRESQL ===================== */
const PROD=[[1,'Kopi',25,'Minuman'],[2,'Teh',15,'Minuman'],[3,'Roti',30,'Makanan'],[4,'Keju',60,'Makanan'],[5,'Susu',40,'Minuman'],[6,'Madu',85,'Lainnya']];
S.query={t:'Urutan kerja query SQL: FROM, WHERE, SELECT, ORDER BY, LIMIT',
 p:[{k:'min',l:'WHERE harga ≥ (ribu)',t:'n',min:0,max:100,v:30},{k:'ord',l:'ORDER BY harga',t:'o',o:[['desc','DESC (besar dulu)'],['asc','ASC (kecil dulu)']],v:'desc'},{k:'lim',l:'LIMIT',t:'n',min:1,max:6,v:3}],
 steps:P=>{const CX=[-3.3,-1.3,.9,3.3],W=[.9,2,1.6,2.2],Z=k=>(k-2.5)*.82,cols=['id','nama','harga','kategori'];
  const cell=(r,j,k,c,y=0)=>B('q'+r[0]+'_'+j,CX[j],y,Z(k),{w:W[j],h:.32,d:.68,c,t:String(r[j])});
  const head=js=>js.map(j=>G('h'+j,CX[j],.75,Z(-1.1),cols[j],'idx'));
  const lt=lantai(10.5,6.6);
  const lolos=PROD.filter(r=>r[2]>=P.min),gagal=PROD.filter(r=>r[2]<P.min);
  const urut=[...lolos].sort((a,b)=>P.ord==='asc'?a[2]-b[2]:b[2]-a[2]),hasil=urut.slice(0,P.lim);
  const S2=[1,2];
  return [
   {cap:`<code>FROM produk</code> dikerjakan <b>pertama</b>: database mengambil seluruh tabel, ${PROD.length} baris dengan 4 kolom. Setiap baris satu produk, setiap kolom satu jenis data.`,
    it:[lt,...head([0,1,2,3]),...PROD.flatMap((r,k)=>[0,1,2,3].map(j=>cell(r,j,k,'acc')))]},
   {cap:`<code>WHERE harga &gt;= ${P.min}</code> memeriksa setiap baris. ${lolos.length} baris lolos (hijau), ${gagal.length} baris dibuang (merah). WHERE bekerja per baris, sebelum kolom dipilih.`,
    it:[lt,...head([0,1,2,3]),...PROD.flatMap((r,k)=>{const ok=r[2]>=P.min;return [0,1,2,3].map(j=>cell(r,j,k,ok?'ok':'bad',ok?0:.7))})]},
   {cap:`<code>SELECT nama, harga</code> baru dikerjakan sekarang: hanya kolom yang diminta yang dibawa. Kolom id dan kategori tidak ikut ke hasil.`,
    it:[lt,...head(S2),...PROD.flatMap((r,k)=>r[2]>=P.min?S2.map(j=>cell(r,j,k,'acc')):[])]},
   {cap:`<code>ORDER BY harga ${P.ord.toUpperCase()}</code> menyusun ulang baris yang tersisa: ${P.ord==='desc'?'harga terbesar di atas':'harga terkecil di atas'}. Perhatikan baris-barisnya berpindah tempat.`,
    it:[lt,...head(S2),...urut.flatMap((r,k)=>S2.map(j=>cell(r,j,k,'warn')))]},
   {cap:lolos.length?`<code>LIMIT ${P.lim}</code> hanya mengambil ${P.lim} baris teratas. Hasil akhir: ${hasil.map(r=>r[1]).join(', ')}.`:'Tidak ada baris yang lolos WHERE, jadi hasilnya kosong. Coba turunkan batas harga di panel Eksperimen.',
    it:[lt,...head(S2),...hasil.flatMap((r,k)=>S2.map(j=>cell(r,j,k,'ok')))]},
   {cap:'Urutan <b>menulis</b> query: SELECT, FROM, WHERE, ORDER BY, LIMIT. Urutan <b>dikerjakan</b>: FROM → WHERE → SELECT → ORDER BY → LIMIT. Karena itu alias di SELECT belum dikenal di WHERE.',
    it:[lt,...head(S2),...hasil.flatMap((r,k)=>S2.map(j=>cell(r,j,k,'ok'))),G('urut',0,2.3,0,'FROM → WHERE → SELECT → ORDER BY → LIMIT','warn')]}]}};

const JUAL=[['Minuman',12],['Makanan',30],['Minuman',8],['Lainnya',5],['Makanan',22],['Minuman',15],['Lainnya',9],['Makanan',18]];
S.group={t:'GROUP BY: mengelompokkan baris lalu meringkas setiap kelompok',
 p:[{k:'fn',l:'Fungsi agregat',t:'o',o:[['sum','SUM(jumlah)'],['count','COUNT(*)'],['avg','AVG(jumlah)'],['max','MAX(jumlah)']],v:'sum'},{k:'hv',l:'HAVING hasil ≥',t:'n',min:0,max:100,v:40}],
 steps:P=>{const K=['Minuman','Makanan','Lainnya'],KC=['acc','warn','ok'],GX=k=>(k-1)*3.1,nm={sum:'SUM',count:'COUNT',avg:'AVG',max:'MAX'}[P.fn]||'SUM';
  const agg=k=>{const v=JUAL.filter(r=>r[0]===K[k]).map(r=>r[1]);return P.fn==='count'?v.length:P.fn==='avg'?Math.round(v.reduce((a,b)=>a+b,0)/v.length*10)/10:P.fn==='max'?Math.max(...v):v.reduce((a,b)=>a+b,0)};
  const A=K.map((_,k)=>agg(k)),mx=Math.max(...A,1),lt=lantai(10,6);
  const lepas=()=>JUAL.map((r,i)=>B('r'+i,(i-3.5)*1.15,0,1.7,{w:.95,h:.5,d:.8,c:KC[K.indexOf(r[0])],t:String(r[1])}));
  const tumpuk=()=>{const c=[0,0,0];return JUAL.map((r,i)=>{const k=K.indexOf(r[0]),h=c[k]++;return B('r'+i,GX(k),h*.56-.05,-.6,{w:.95,h:.5,d:.8,c:KC[k],t:String(r[1])})})};
  const nama=()=>K.map((n,k)=>G('g'+k,GX(k),-.55,.4,n,'idx'));
  const tiang=f=>K.map((n,k)=>{const h=Math.max(.3,A[k]/mx*2.6);return B('a'+k,GX(k),h/2-.3,-.6,{w:1.3,h,d:1.1,c:f(k),t:String(A[k])})});
  const lolos=K.filter((_,k)=>A[k]>=P.hv);
  return [
   {cap:`Tabel penjualan berisi ${JUAL.length} baris. Warna menunjukkan kategori. Kita ingin tahu <b>${nm}</b> per kategori.`,it:[lt,...lepas()]},
   {cap:'<code>GROUP BY kategori</code> mengumpulkan baris dengan kategori yang sama ke satu tumpukan. Perhatikan setiap kotak berpindah ke kelompoknya.',it:[lt,...tumpuk(),...nama()]},
   {cap:`<code>${nm}(${P.fn==='count'?'*':'jumlah'})</code> meringkas setiap tumpukan menjadi <b>satu baris</b>: ${K.map((n,k)=>`${n} = ${A[k]}`).join(', ')}.`,it:[lt,...tiang(k=>KC[k]),...nama()]},
   {cap:`<code>HAVING ${nm}(...) &gt;= ${P.hv}</code> menyaring <b>kelompok</b>, bukan baris. Yang lolos: ${lolos.length?lolos.join(', '):'tidak ada'}. WHERE menyaring sebelum dikelompokkan, HAVING sesudahnya.`,
    it:[lt,...tiang(k=>A[k]>=P.hv?'ok':'bad'),...nama(),...K.map((n,k)=>A[k]<P.hv?G('x'+k,GX(k),2.9,-.6,'dibuang','bad'):null).filter(Boolean)]},
   {cap:'Urutannya: FROM → WHERE → <b>GROUP BY</b> → <b>HAVING</b> → SELECT → ORDER BY. Setiap kolom di SELECT harus ikut di GROUP BY atau dibungkus fungsi agregat.',it:[lt,...tiang(k=>A[k]>=P.hv?'ok':'mute'),...nama()]}]}};

S.index={t:'Index: lompat lewat pohon B-tree, bukan memeriksa baris satu per satu',
 p:[{k:'n',l:'Jumlah baris di tabel',t:'n',min:16,max:100000000,v:1000000},{k:'cari',l:'Cari id ke- (1–16)',t:'n',min:1,max:16,v:11}],
 steps:P=>{const V=16,c=Math.min(V,Math.max(1,P.cari)),n=Math.max(V,P.n),X=k=>(k-(V-1)/2)*.62,lv=Math.ceil(Math.log2(n)),fmt=v=>v.toLocaleString('id-ID');
  const tabel=f=>Array.from({length:V},(_,k)=>B('t'+k,X(k),-.05,0,{w:.5,h:.5,d:1.1,c:f(k),t:String(k+1)}));
  const L1=c<=8?0:1,L2=Math.floor((c-1)/4),nx1=i=>(i-.5)*5,nx2=i=>(i-1.5)*2.5,LX=X(c-1);
  const nd=(id,x,y,col,t)=>B(id,x,y,0,{w:1.4,h:.48,d:.7,c:col,t});
  const pohon=on=>[nd('n0',0,3.4,on>=1?'ok':'acc','1–16'),...[0,1].map(i=>nd('n1'+i,nx1(i),2.4,on>=1&&i===L1?'ok':'acc',i?'9–16':'1–8')),
    ...[0,1,2,3].map(i=>nd('n2'+i,nx2(i),1.4,on>=1&&i===L2?'ok':'acc',`${i*4+1}–${i*4+4}`)),
    ...[0,1].map(i=>R('e1'+i,[0,3.15,0],[nx1(i),2.65,0],on>=1&&i===L1?'ok':'mute')),...[0,1,2,3].map(i=>R('e2'+i,[nx1(i<2?0:1),2.15,0],[nx2(i),1.65,0],on>=1&&i===L2?'ok':'mute')),
    ...(on>=2?[R('e3',[nx2(L2),1.15,0],[LX,.25,0],'ok')]:[])];
  const lt=lantai(11.5,3.4);
  return [
   {cap:`Tabel ini berisi <b>${fmt(n)} baris</b> (digambar 16 saja). Kita mencari baris dengan id = ${c}.`,it:[lt,...tabel(()=>'acc')]},
   {cap:`<b>Tanpa index</b>, database membaca baris satu per satu dari awal (<i>sequential scan</i>). Di sini ${c} baris diperiksa sebelum ketemu. Untuk ${fmt(n)} baris, terburuknya ${fmt(n)} kali periksa.`,
    it:[lt,...tabel(k=>k<c-1?'mute':k===c-1?'ok':'acc'),B('bola',LX,.6,0,{w:.4,h:.4,d:.4,c:'warn',ball:1})]},
   {cap:'<code>CREATE INDEX</code> membangun <b>pohon B-tree</b>: setiap simpul mencatat rentang id di bawahnya, seperti daftar isi buku.',it:[lt,...tabel(()=>'acc'),...pohon(0)]},
   {cap:`Mencari id ${c}: mulai dari akar, pilih cabang yang rentangnya memuat ${c}, terus turun. Hanya satu jalur yang dilewati.`,it:[lt,...tabel(()=>'acc'),...pohon(1)]},
   {cap:`Daun menunjuk langsung ke barisnya. Untuk ${fmt(n)} baris, cukup sekitar <b>${lv} langkah</b> (log₂ n), bukan ${fmt(n)}. Inilah <i>index scan</i> yang terlihat di EXPLAIN.`,it:[lt,...tabel(k=>k===c-1?'ok':'acc'),...pohon(2)]},
   {cap:'Index tidak gratis: setiap INSERT dan UPDATE juga harus memperbarui pohonnya, dan index memakan ruang disk. Buat index untuk kolom yang sering dipakai di WHERE, JOIN, dan ORDER BY.',it:[lt,...tabel(k=>k===c-1?'ok':'acc'),...pohon(2),G('biaya',0,4.3,0,'baca cepat · tulis sedikit lebih lambat','warn')]}]}};

S.fk={t:'Primary key dan foreign key: tabel yang saling menunjuk',
 p:[{k:'id',l:'pelanggan_id pesanan baru',t:'n',min:1,max:9,v:4}],
 steps:P=>{const PL=[[1,'Ani'],[2,'Budi'],[3,'Citra']],PS=[[101,1],[102,3],[103,1]],Y=k=>2.2-k*.75,LX=-3,RX=2.8;
  const pel=f=>PL.map((r,k)=>B('p'+r[0],LX,Y(k),0,{w:2.4,h:.5,d:.8,c:f(r[0]),t:`${r[0]} · ${r[1]}`}));
  const pes=f=>PS.map((r,k)=>B('o'+r[0],RX,Y(k),0,{w:2.4,h:.5,d:.8,c:f(r[0]),t:`${r[0]} → ${r[1]}`}));
  const ruas=(on)=>PS.map((r,k)=>R('f'+r[0],[RX-1.2,Y(k),0],[LX+1.2,Y(PL.findIndex(p=>p[0]===r[1])),0],on?'ok':'mute'));
  const kep=()=>[G('hp',LX,3,0,'pelanggan (PK: id)','idx'),G('ho',RX,3,0,'pesanan (FK: pelanggan_id)','idx')];
  const ada=PL.some(r=>r[0]===P.id),lt=lantai(10,3);
  const baru=(c,y)=>B('o104',RX,y,0,{w:2.4,h:.5,d:.8,c,t:`104 → ${P.id}`});
  return [
   {cap:'Dua tabel: <b>pelanggan</b> dan <b>pesanan</b>. Setiap pesanan menyimpan <code>pelanggan_id</code> untuk menunjuk pemiliknya.',it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'acc')]},
   {cap:'<b>Primary key</b> (id) adalah identitas unik setiap baris: tidak boleh kembar dan tidak boleh NULL. Tidak ada dua pelanggan dengan id yang sama.',it:[lt,...kep(),...pel(()=>'warn'),...pes(()=>'mute')]},
   {cap:'<b>Foreign key</b> <code>pelanggan_id REFERENCES pelanggan(id)</code> menghubungkan setiap pesanan ke satu pelanggan. Ani punya dua pesanan, Budi belum punya.',it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'ok'),...ruas(1)]},
   ada?{cap:`<code>INSERT INTO pesanan VALUES (104, ${P.id})</code>: pelanggan ${P.id} ada, jadi baris baru <b>diterima</b> dan langsung terhubung.`,it:[lt,...kep(),...pel(id=>id===P.id?'ok':'acc'),...pes(()=>'ok'),...ruas(1),baru('ok',Y(3)),R('f104',[RX-1.2,Y(3),0],[LX+1.2,Y(P.id-1),0],'ok')]}
      :{cap:`<code>INSERT INTO pesanan VALUES (104, ${P.id})</code> <b>ditolak</b>: pelanggan ${P.id} tidak ada. Pesan error: <i>violates foreign key constraint</i>. Database menjaga agar tidak ada pesanan "yatim".`,it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'ok'),...ruas(1),baru('bad',Y(3)+.4),G('err',RX,Y(3)-.5,0,'ditolak: pelanggan tidak ada','bad')]},
   {cap:'Constraint lain menjaga data tetap benar: <code>NOT NULL</code> (wajib diisi), <code>UNIQUE</code> (tidak boleh kembar), <code>CHECK (harga &gt; 0)</code>. Ubah pelanggan_id di panel Eksperimen untuk mencoba.',it:[lt,...kep(),...pel(()=>'acc'),...pes(()=>'ok'),...ruas(1),...(ada?[baru('ok',Y(3)),R('f104',[RX-1.2,Y(3),0],[LX+1.2,Y(P.id-1),0],'ok')]:[])]}]}};

S.tx={t:'Transaksi: semua langkah berhasil, atau tidak sama sekali',
 p:[{k:'n',l:'Transfer dari A ke B (ribu)',t:'n',min:1,max:900,v:150},{k:'gagal',l:'Server mati di tengah?',t:'o',o:[['0','Tidak'],['1','Ya']],v:'0'}],
 steps:P=>{const A0=500,B0=200,n=P.n,mati=String(P.gagal)==='1',kurang=n>A0;
  const akun=(id,x,v,c)=>{const h=Math.max(.3,v/400*1.6);return B(id,x,h/2-.3,0,{w:1.8,h,d:1.4,c,t:`${id==='akA'?'A':'B'}: ${v}`})};
  const uang=(x,y,c='warn')=>B('uang',x,y,0,{w:.55,h:.55,d:.55,c,ball:1,t:String(n)});
  const lt=lantai(9,3.4),tot=v=>G('tot',0,3.3,0,'total = '+v,'idx');
  const s=[{lb:'BEGIN',cap:`<code>BEGIN</code> membuka transaksi. Saldo A = ${A0}, B = ${B0}, total ${A0+B0}. Kita akan memindahkan ${n} dari A ke B.`,it:[lt,akun('akA',-2.6,A0,'acc'),akun('akB',2.6,B0,'acc'),tot(A0+B0)]}];
  if(kurang){s.push({lb:'Kurangi A',cap:`<code>UPDATE akun SET saldo = saldo - ${n}</code> pada A melanggar <code>CHECK (saldo &gt;= 0)</code> karena saldo A hanya ${A0}. Database menolak perubahan ini.`,it:[lt,akun('akA',-2.6,A0,'bad'),akun('akB',2.6,B0,'acc'),tot(A0+B0),G('err',-2.6,2.6,0,'CHECK gagal','bad')]},
    {lb:'ROLLBACK',cap:'<code>ROLLBACK</code>: transaksi dibatalkan. Tidak ada saldo yang berubah.',it:[lt,akun('akA',-2.6,A0,'acc'),akun('akB',2.6,B0,'acc'),tot(A0+B0)]})}
  else{s.push({lb:'Kurangi A',cap:`<code>UPDATE ... saldo - ${n} WHERE id = 'A'</code>. Saldo A menjadi ${A0-n}, tetapi belum permanen: transaksi lain belum melihat perubahan ini.`,it:[lt,akun('akA',-2.6,A0-n,'warn'),akun('akB',2.6,B0,'acc'),uang(0,1.8),tot(`${A0+B0-n} (sementara)`)]});
    if(mati)s.push({lb:'Gagal',cap:'Server tiba-tiba mati sebelum B ditambah. Kalau tidak ada transaksi, uang ini akan <b>hilang</b>.',it:[lt,akun('akA',-2.6,A0-n,'warn'),akun('akB',2.6,B0,'mute'),uang(0,1.8,'bad'),G('err',0,3.3,0,'⚡ server mati','bad')]},
      {lb:'ROLLBACK',cap:`Saat hidup lagi, PostgreSQL membaca WAL dan membatalkan transaksi yang belum COMMIT. Saldo A kembali ${A0}. Total tetap ${A0+B0}: <b>atomicity</b>.`,it:[lt,akun('akA',-2.6,A0,'ok'),akun('akB',2.6,B0,'ok'),tot(A0+B0)]});
    else s.push({lb:'Tambah B',cap:`<code>UPDATE ... saldo + ${n} WHERE id = 'B'</code>. Uang berpindah ke B.`,it:[lt,akun('akA',-2.6,A0-n,'warn'),akun('akB',2.6,B0+n,'warn'),uang(2.6,(B0+n)/400*1.6+.2),tot(A0+B0)]},
      {lb:'COMMIT',cap:`<code>COMMIT</code>: kedua perubahan disimpan permanen <b>bersamaan</b>. A = ${A0-n}, B = ${B0+n}, total tetap ${A0+B0}.`,it:[lt,akun('akA',-2.6,A0-n,'ok'),akun('akB',2.6,B0+n,'ok'),tot(A0+B0)]})}
  s.push({lb:'ACID',cap:'<b>ACID</b>: <b>A</b>tomicity (semua atau tidak sama sekali), <b>C</b>onsistency (aturan seperti CHECK selalu dijaga), <b>I</b>solation (transaksi lain tidak melihat keadaan setengah jadi), <b>D</b>urability (yang sudah COMMIT tidak hilang). Coba pilih "Server mati" di Eksperimen.',
    it:[...s[s.length-1].it.filter(o=>o.id!=='uang'&&o.id!=='err')]});
  return s}};

const NIL=[['A','Ani',90],['B','Eka',95],['A','Budi',85],['B','Fajar',80],['A','Citra',85],['A','Dodi',70],['B','Gita',80]];
S.window={t:'Window function: menghitung per kelompok tanpa meringkas baris',
 p:[{k:'fn',l:'Fungsi',t:'o',o:[['rn','ROW_NUMBER()'],['rank','RANK()'],['dense','DENSE_RANK()'],['run','SUM(nilai) berjalan']],v:'rank'}],
 steps:P=>{const CX=[-3.4,-1.6,.4,2.8],Wd=[1,2,1.4,2.2],nm={rn:'ROW_NUMBER()',rank:'RANK()',dense:'DENSE_RANK()',run:'SUM(nilai)'}[P.fn]||'RANK()';
  const cell=(r,j,z,c,t)=>B('w'+r[1]+j,CX[j],0,z,{w:Wd[j],h:.32,d:.62,c,t:t??String(r[j])});
  const PC=k=>k==='A'?'acc':'warn';
  const part=[...NIL].sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:0),urut=[...NIL].sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:b[2]-a[2]);
  const zz=(list)=>{let g=0,prev=null;return list.map((r,k)=>{if(prev&&prev!==r[0])g++;prev=r[0];return (k-3)*.72+g*.6-.3})};
  const hit=r=>{const p=urut.filter(x=>x[0]===r[0]),i=p.indexOf(r);if(P.fn==='rn')return i+1;if(P.fn==='rank')return p.filter(x=>x[2]>r[2]).length+1;
    if(P.fn==='dense')return new Set(p.filter(x=>x[2]>r[2]).map(x=>x[2])).size+1;return p.slice(0,i+1).reduce((a,x)=>a+x[2],0)};
  const head=on=>['kelas','nama','nilai',on?nm:''].map((h,j)=>h?G('h'+j,CX[j],.75,-3.4,h,'idx'):null).filter(Boolean);
  const lt=lantai(10,7.4);
  const baris=(list,col,on)=>{const Z=zz(list);return list.flatMap((r,k)=>[...[0,1,2].map(j=>cell(r,j,Z[k],col(r))),...(on?[cell(r,3,Z[k],'ok',String(hit(r)))]:[])])};
  const seri=urut.filter((r,k)=>urut.some(x=>x!==r&&x[0]===r[0]&&x[2]===r[2]));
  return [
   {cap:`Tabel nilai ${NIL.length} siswa dari kelas A dan B, urutannya acak.`,it:[lt,...head(0),...baris(NIL,()=>'mute',0)]},
   {cap:'<code>PARTITION BY kelas</code> membagi baris menjadi jendela per kelas. Perhitungan nanti hanya melihat baris di jendelanya sendiri.',it:[lt,...head(0),...baris(part,r=>PC(r[0]),0)]},
   {cap:'<code>ORDER BY nilai DESC</code> mengurutkan baris <b>di dalam</b> setiap jendela, dari nilai tertinggi.',it:[lt,...head(0),...baris(urut,r=>PC(r[0]),0)]},
   {cap:`<code>${nm} OVER (PARTITION BY kelas ORDER BY nilai DESC)</code> menambah satu kolom baru. ${P.fn==='rn'?'ROW_NUMBER selalu 1, 2, 3, … meski nilainya sama.':P.fn==='rank'?'RANK memberi angka sama untuk nilai kembar, lalu melompat (1, 2, 2, 4).':P.fn==='dense'?'DENSE_RANK memberi angka sama untuk nilai kembar tanpa lompatan (1, 2, 2, 3).':'SUM berjalan menjumlahkan nilai dari atas sampai baris ini, dan mulai lagi di kelas berikutnya.'}${seri.length&&P.fn!=='run'?` Perhatikan ${seri.map(r=>r[1]).join(' dan ')}.`:''}`,
    it:[lt,...head(1),...baris(urut,r=>PC(r[0]),1)]},
   {cap:'Bedanya dengan GROUP BY: GROUP BY meringkas banyak baris menjadi satu, sedangkan window function <b>mempertahankan setiap baris</b> dan menambah kolom hasil. Ganti fungsinya di panel Eksperimen.',it:[lt,...head(1),...baris(urut,r=>PC(r[0]),1)]}]}};

S.mvcc={t:'MVCC: setiap UPDATE membuat versi baris baru',
 p:[{k:'u',l:'Jumlah UPDATE',t:'n',min:1,max:5,v:3},{k:'vac',l:'Jalankan VACUUM?',t:'o',o:[['1','Ya'],['0','Belum']],v:'1'}],
 steps:P=>{const u=Math.max(1,Math.min(5,P.u)),X=k=>(k-u/2)*1.55,ver=(k,c,t)=>B('v'+k,X(k),0,0,{w:1.3,h:.7,d:1.1,c,t:t||`stok=${50-k*5}`});
  const lt=lantai(Math.max(8,u*1.6+3),4),all=f=>Array.from({length:u+1},(_,k)=>ver(k,f(k)));
  const xid=k=>G('x'+k,X(k),1,0,`xmin ${100+k}${k<u?` · xmax ${101+k}`:''}`,'idx');
  const baca=on=>on?[B('rd',X(0),2.2,1.6,{w:.5,h:.5,d:.5,c:'warn',ball:1,t:'T1'}),R('rr',[X(0),1.95,0],[X(0),.4,0],'warn')]:[];
  return [
   {cap:'<code>INSERT</code> membuat versi pertama baris produk (stok = 50). Setiap versi mencatat <b>xmin</b>: nomor transaksi yang membuatnya.',it:[lt,ver(0,'ok'),xid(0)]},
   {cap:'Transaksi <b>T1</b> mulai membaca dan melihat versi ini. Selama T1 berjalan, ia harus terus melihat data yang sama.',it:[lt,ver(0,'ok'),xid(0),...baca(1)]},
   {cap:`${u}× <code>UPDATE</code>: PostgreSQL <b>tidak menimpa</b> baris lama. Ia membuat versi baru dan menandai versi lama dengan <b>xmax</b>. T1 tetap membaca versi lamanya tanpa dikunci: pembaca tidak menghalangi penulis.`,
    it:[lt,...all(k=>k===u?'ok':'mute'),...Array.from({length:u+1},(_,k)=>xid(k)),...baca(1)]},
   {cap:`T1 selesai. Sekarang ${u} versi lama tidak dipakai siapa pun: ini <b>dead tuple</b>. Mereka masih memakan ruang disk dan memperlambat scan. Inilah <b>bloat</b>.`,
    it:[lt,...all(k=>k===u?'ok':'bad'),...Array.from({length:u},(_,k)=>G('d'+k,X(k),1,0,'mati','bad')),G('x'+u,X(u),1,0,`xmin ${100+u}`,'idx')]},
   String(P.vac)==='1'?{cap:'<code>VACUUM</code> menyapu dead tuple sehingga ruangnya bisa dipakai ulang. Autovacuum menjalankannya otomatis di latar; pantau dengan <code>pg_stat_user_tables</code>.',it:[lt,ver(u,'ok'),G('x'+u,X(u),1,0,`xmin ${100+u}`,'idx'),...Array.from({length:u},(_,k)=>B('ks'+k,X(k),-.38,0,{w:1.3,h:.06,d:1.1,c:'glass',flat:1}))]}
     :{cap:'Tanpa VACUUM, dead tuple terus menumpuk setiap kali ada UPDATE dan DELETE. Pilih "Ya" di Eksperimen untuk melihat VACUUM bekerja.',it:[lt,...all(k=>k===u?'ok':'bad'),...Array.from({length:u},(_,k)=>G('d'+k,X(k),1,0,'mati','bad'))]}]}};

S.repl={t:'Replikasi: salinan database yang selalu mengikuti primary',
 p:[{k:'r',l:'Jumlah replika',t:'n',min:1,max:3,v:2},{k:'mode',l:'Mode',t:'o',o:[['async','Asinkron'],['sync','Sinkron']],v:'async'},{k:'mati',l:'Primary mati?',t:'o',o:[['0','Tidak'],['1','Ya']],v:'1'}],
 steps:P=>{const r=Math.max(1,Math.min(3,P.r)),RY=i=>(i-(r-1)/2)*1.5+.6,PX=-1,RX=3.2,CX=-4.6,sync=P.mode==='sync';
  const prim=(c,t='primary')=>B('pri',PX,.6,0,{w:1.3,h:1.4,d:1.3,c,t,s:'db'});
  const rep=(f,lab=i=>'replika '+(i+1))=>Array.from({length:r},(_,i)=>B('rep'+i,RX,RY(i),0,{w:1,h:1.05,d:1,c:f(i),t:lab(i),s:'db'}));
  const wal=on=>Array.from({length:r},(_,i)=>R('w'+i,[PX+.9,.6,0],[RX-.9,RY(i),0],on?'ok':'mute'));
  const cli=B('cli',CX,.6,0,{w:1.2,h:1.1,d:.8,c:'warn',t:'app',s:'layar'}),lt=lantai(11,4);
  const s=[
   {lb:'Tulis',cap:'Aplikasi menulis data (INSERT, UPDATE) hanya ke <b>primary</b>. Setiap perubahan dicatat dulu di <b>WAL</b> (write-ahead log).',it:[lt,cli,R('cw',[CX+.45,.6,0],[PX-.9,.6,0],'warn'),prim('acc'),...rep(()=>'mute'),...wal(0)]},
   {lb:'Kirim WAL',cap:sync?'Mode <b>sinkron</b>: primary menunggu replika mengonfirmasi sudah menerima WAL sebelum COMMIT selesai. Data aman, tetapi setiap tulisan sedikit lebih lambat.':'Mode <b>asinkron</b>: primary langsung menjawab COMMIT, lalu WAL mengalir ke replika. Cepat, tetapi replika bisa tertinggal beberapa milidetik (<i>replication lag</i>).',
    it:[lt,cli,prim('acc'),...rep(()=>'ok'),...wal(1),...(sync?[G('ack',(PX+RX)/2,RY(0)+1.1,0,'tunggu konfirmasi','warn')]:[])]},
   {lb:'Baca',cap:'Replika bisa melayani query baca (SELECT), sehingga beban primary berkurang. Ini disebut <i>read scaling</i>.',it:[lt,cli,prim('acc'),...rep(()=>'ok',()=>'SELECT ✓'),...wal(1)]}];
  if(String(P.mati)==='1')s.push(
   {lb:'Primary mati',cap:'Primary tiba-tiba mati. Penulisan berhenti, tetapi replika masih punya salinan data.',it:[lt,cli,prim('bad','mati'),...rep(()=>'acc'),...wal(0)]},
   {lb:'Failover',cap:`<b>Failover</b>: replika 1 dipromosikan menjadi primary baru (misalnya oleh Patroni). Aplikasi diarahkan ke sana.${sync?' Dengan mode sinkron, tidak ada transaksi yang hilang.':' Dengan mode asinkron, transaksi terakhir yang belum terkirim bisa hilang.'}`,
    it:[lt,cli,prim('mute','mati'),...rep(i=>i===0?'ok':'acc',i=>i===0?'primary baru':'replika '+(i+1)),R('cw',[CX+.45,.6,0],[RX-.9,RY(0),0],'warn')]});
  s.push({lb:'Intinya',cap:'Replikasi untuk ketersediaan tinggi dan membagi beban baca. Replikasi <b>bukan backup</b>: DELETE yang salah ikut tersalin ke replika. Tetap buat backup terjadwal.',it:s[s.length-1].it});
  return s}};

/* ===================== WEB, FRONTEND, DSA, DATA ===================== */
/* graf umum di bidang xy: N = {k:[x,y,teks]}, warna simpul dan ruas ditentukan fungsi */
function graf(N,Ed,col,ecol,w=1,sh){const ys=Object.values(N).map(n=>n[1]),it=[lantai(10,3,Math.min(...ys)-1.4)];
  Ed.forEach(([a,b])=>{const A=N[a],Bn=N[b];it.push(R('e'+a+'_'+b,[A[0],A[1],0],[Bn[0],Bn[1],0],ecol?ecol(a,b):'mute'))});
  Object.entries(N).forEach(([k,[x,y,t]])=>it.push(B('n'+k,x,y,0,sh?{w:.8,h:1.1,d:.8,c:col(k),t:E(t),s:sh}:{w:t.length>4?Math.max(1.4,t.length*.17)*w:.9,h:.75,d:.75,c:col(k),t:E(t)})));return it}

/* ---------- HTTP: perjalanan request ---------- */
S.http={t:'Cara web bekerja: perjalanan satu request dari browser ke server dan kembali',
 p:[{k:'cache',l:'Alamat IP sudah di-cache?',t:'o',o:[['0','Belum'],['1','Sudah']],v:'0'},{k:'st',l:'Jawaban server',t:'o',o:[['200','200 OK'],['404','404 Not Found'],['500','500 Server Error']],v:'200'}],
 steps:P=>{const BX=-4.2,SX=1.4,DX=4.4,DNS=[-.9,2.7],st=String(P.st),c=String(P.cache)==='1';
  const sc=st==='200'?'ok':st==='404'?'warn':'bad',lt=lantai(11,3.6);
  const base=(b='acc',s='acc',d='acc',n='mute')=>[lt,B('br',BX,.3,0,{w:1.9,h:1.5,d:1,c:b,t:'browser',s:'layar'}),B('dns',DNS[0],DNS[1],0,{w:1,h:1.2,d:.35,c:n,t:'DNS',s:'buku'}),
    B('srv',SX,.3,0,{w:1.4,h:1.7,d:1.2,c:s,t:'server',s:'server'}),B('db',DX,.1,0,{w:1.2,h:1.2,d:1.2,c:d,t:'DB',s:'db'})];
  const pk=(x,y,col,t)=>B('pk',x,y,0,{w:.5,h:.5,d:.5,c:col,ball:1,t});
  const ln=(id,a,b,col)=>R(id,a,b,col);
  return [
   {cap:'Kamu mengetik <code>tokonusantara.id/produk</code> lalu menekan Enter. Browser hanya tahu <b>nama</b> situsnya, belum tahu alamat komputernya.',it:[...base('warn'),G('url',BX,1.6,0,'tokonusantara.id/produk','idx')]},
   c?{cap:'Alamat IP situs ini sudah tersimpan di <b>cache</b> browser dari kunjungan sebelumnya, jadi tanya DNS dilewati. Hemat puluhan milidetik.',it:[...base('ok'),G('ip',BX,1.6,0,'IP dari cache: 103.10.2.7','ok')]}
    :{cap:'Browser bertanya ke <b>DNS</b>, buku telepon internet: "berapa alamat IP tokonusantara.id?" DNS menjawab <code>103.10.2.7</code>.',it:[...base('acc','acc','acc','ok'),ln('ld',[BX+.9,.9,0],[DNS[0]-.6,DNS[1],0],'ok'),pk(DNS[0]-1.6,DNS[1]-.4,'warn','?'),G('ip',DNS[0],DNS[1]+.8,0,'103.10.2.7','ok')]},
   {cap:'Browser mengirim <b>HTTP request</b> ke server: <code>GET /produk</code> beserta header seperti <code>Accept</code> dan cookie. Dengan HTTPS, isinya dienkripsi di perjalanan.',it:[...base('acc','warn'),ln('lr',[BX+.9,.3,0],[SX-.75,.3,0],'warn'),pk((BX+SX)/2,.75,'warn','GET'),G('req',(BX+SX)/2,1.6,0,'GET /produk','idx')]},
   st==='404'?{cap:'Server mencari rute <code>/produk</code> tetapi tidak menemukannya. Tidak perlu bertanya ke database.',it:[...base('acc','warn'),G('err',SX,2,0,'rute tidak ada','warn')]}
    :{cap:st==='500'?'Server menjalankan kode untuk rute itu dan bertanya ke database, tetapi query-nya gagal (misalnya tabel tidak ada). Ini kesalahan di sisi server.':'Server menjalankan kode untuk rute itu: bertanya ke database <code>SELECT * FROM produk</code>, lalu menyusun hasilnya menjadi HTML atau JSON.',
      it:[...base('acc','warn',st==='500'?'bad':'ok'),ln('lq',[SX+.75,.3,0],[DX-.6,.3,0],st==='500'?'bad':'ok'),pk((SX+DX)/2,.75,st==='500'?'bad':'ok','SQL')]},
   {cap:`Server mengirim <b>HTTP response</b> dengan kode status <code>${st}</code>${st==='200'?': berhasil, isinya data produk.':st==='404'?': halaman tidak ditemukan (kesalahan di alamat yang diminta).':': server error (kesalahan di sisi server).'} Kode 2xx berarti berhasil, 3xx dialihkan, 4xx salah di klien, 5xx salah di server.`,
    it:[...base('acc',sc),ln('lr',[BX+.9,.3,0],[SX-.75,.3,0],sc),pk((BX+SX)/2,.75,sc,st)]},
   {cap:st==='200'?'Browser membaca HTML, lalu meminta file lain yang dibutuhkan (CSS, JS, gambar) dengan cara yang sama, dan menggambar halamannya. Semua ini biasanya selesai dalam ratusan milidetik.':'Browser menampilkan halaman kesalahan. Buka DevTools → tab <b>Network</b> untuk melihat setiap request, kode status, dan waktunya.',
    it:[...base(sc,'acc'),G('hasil',BX,1.6,0,st==='200'?'halaman tampil ✓':'halaman error '+st,sc)]}]}};

/* ---------- Flexbox dan Grid ---------- */
S.flex={t:'Flexbox dan Grid: menata kotak di sepanjang sumbu',
 p:[{k:'dir',l:'flex-direction',t:'o',o:[['row','row (mendatar)'],['column','column (menurun)']],v:'row'},
  {k:'jc',l:'justify-content',t:'o',o:[['flex-start','flex-start'],['center','center'],['space-between','space-between'],['space-around','space-around']],v:'space-between'},
  {k:'n',l:'Jumlah item',t:'n',min:2,max:6,v:4}],
 steps:P=>{const n=Math.max(2,Math.min(6,P.n)),row=P.dir!=='column',CW=8,CH=4,pad=.2,IW=CW-2*pad,IH=CH-2*pad;
  const L=row?IW:IH,s=row?1.15:.55,KC=['acc','warn','ok','idx','acc','warn'];
  const box=[lantai(10,3,-2.6),B('cont',0,0,-.35,{w:CW,h:CH,d:.15,c:'glass'})];
  const it=(i,cx,cy,w,h,c)=>B('i'+i,cx,cy,0,{w,h,d:.5,c:c||KC[i],t:String(i+1)});
  const tempat=(jc,sizes)=>{const tot=sizes.reduce((a,b)=>a+b,0),free=Math.max(0,L-tot);let start=0,gap=0;
    if(jc==='center')start=free/2;else if(jc==='space-between')gap=n>1?free/(n-1):0;else if(jc==='space-around'){gap=free/n;start=gap/2}
    const out=[];let p=start;sizes.forEach(z=>{out.push(p+z/2-L/2);p+=z+gap});return out};
  const tata=(jc,align,grow)=>{const sizes=Array.from({length:n},(_,i)=>grow&&i===1?L-s*(n-1):s),pos=tempat(grow?'flex-start':jc,sizes);
    return sizes.map((z,i)=>{const cross=align==='center'?(row?.9:1.6):(row?IH:IW);
      return row?it(i,pos[i],0,z-.06,cross-.06):it(i,0,-pos[i],cross-.06,z-.06)})};
  const sumbu=row?G('ax',0,CH/2+.45,0,'sumbu utama →','idx'):G('ax',-CW/2-.9,0,0,'sumbu utama ↓','idx');
  const blok=Array.from({length:n},(_,i)=>it(i,0,IH/2-.3-i*.62,IW-.06,.56));
  const cols=3,rows=Math.ceil(n/cols),gw=IW/cols,gh=IH/rows;
  const grid=Array.from({length:n},(_,i)=>it(i,(i%cols+.5)*gw-IW/2,IH/2-(Math.floor(i/cols)+.5)*gh,gw-.2,gh-.2));
  return [
   {cap:'Tanpa aturan apa pun, setiap <code>div</code> adalah elemen <b>block</b>: mengambil lebar penuh dan turun ke baris berikutnya. Inilah alur normal.',it:[...box,...blok]},
   {cap:`<code>display: flex</code> mengubah wadah menjadi flex container. Anak-anaknya berjajar di <b>sumbu utama</b> (${row?'mendatar, karena flex-direction: row':'menurun, karena flex-direction: column'}) dan secara bawaan meregang penuh di sumbu silang.`,it:[...box,...tata('flex-start','stretch'),sumbu]},
   {cap:`<code>justify-content: ${P.jc}</code> mengatur sisa ruang di <b>sumbu utama</b>. ${P.jc==='space-between'?'Item pertama dan terakhir menempel ke tepi, sisanya dibagi rata.':P.jc==='center'?'Semua item berkumpul di tengah.':P.jc==='space-around'?'Setiap item mendapat ruang yang sama di kedua sisinya.':'Semua item menempel di awal sumbu.'}`,it:[...box,...tata(P.jc,'stretch'),sumbu]},
   {cap:'<code>align-items: center</code> mengatur posisi di <b>sumbu silang</b>: item tidak lagi meregang, melainkan berada di tengah. Ingat: justify untuk sumbu utama, align untuk sumbu silang.',it:[...box,...tata(P.jc,'center'),sumbu]},
   {cap:'<code>flex-grow: 1</code> pada item 2 membuatnya <b>menyerap semua sisa ruang</b>. Pola ini dipakai untuk kolom pencarian yang mengisi navbar.',it:[...box,...tata(P.jc,'center',1),sumbu]},
   {cap:`<code>display: grid; grid-template-columns: repeat(3, 1fr)</code> menata dalam <b>dua dimensi</b> sekaligus: ${n} item mengisi ${rows} baris × 3 kolom. Pakai flexbox untuk satu baris atau kolom, grid untuk tata letak baris dan kolom.`,it:[...box,...grid]}]}};

/* ---------- React: komponen, props, state ---------- */
S.react={t:'React: pohon komponen, props turun, state memicu render ulang',
 p:[{k:'klik',l:'Klik tombol "+ Keranjang"',t:'n',min:1,max:9,v:1},{k:'memo',l:'Kartu dibungkus React.memo?',t:'o',o:[['0','Tidak'],['1','Ya']],v:'0'}],
 steps:P=>{const N={app:[0,2.4,'App'],hd:[-2.6,.9,'Header'],ls:[2,.9,'DaftarProduk'],k1:[.4,-.7,'Kartu'],k2:[2,-.7,'Kartu'],k3:[3.6,-.7,'Kartu']};
  const Ed=[['app','hd'],['app','ls'],['ls','k1'],['ls','k2'],['ls','k3']],memo=String(P.memo)==='1',k=P.klik;
  const g=(col,ecol,extra=[])=>[...graf(N,Ed,col,ecol,.85),...extra];
  const isi=G('cnt',-2.6,1.6,0,'🛒 '+k,'ok');
  return [
   {cap:'Antarmuka React disusun dari <b>komponen</b>: fungsi yang mengembalikan JSX. <code>App</code> berisi <code>Header</code> dan <code>DaftarProduk</code>, yang berisi tiga <code>Kartu</code>.',it:g(()=>'acc')},
   {cap:'<b>Props</b> mengalir <b>turun</b> dari induk ke anak, seperti argumen fungsi. <code>&lt;Kartu produk={p} /&gt;</code>: Kartu hanya membaca props, tidak boleh mengubahnya.',it:g(x=>x==='hd'?'mute':'acc',(a,b)=>a==='app'&&b==='hd'?'mute':'warn',[G('pp',3.4,.1,0,'props ↓','warn')])},
   {cap:'<b>State</b> adalah data milik komponen yang bisa berubah: <code>const [jumlah, setJumlah] = useState(0)</code> di App. Kartu menerima fungsi <code>onTambah</code> lewat props dan memanggilnya saat tombol diklik.',it:g(x=>x==='app'?'warn':x==='k2'?'ok':'mute',(a,b)=>b==='k2'||(a==='app'&&b==='ls')?'ok':'mute',[G('ev',.7,1.9,0,'↑ onTambah()','ok')])},
   {cap:`<code>setJumlah</code> dipanggil ${k}×. Setiap kali state App berubah, App dan <b>semua turunannya</b> dirender ulang.${memo?' Kecuali Kartu: dengan <code>React.memo</code>, React melewatinya karena props-nya tidak berubah.':' Kartu ikut dirender ulang walaupun datanya sama.'}`,
    it:g(x=>x[0]==='k'&&memo?'mute':'warn',(a,b)=>b[0]==='k'&&memo?'mute':'warn',[isi])},
   {cap:'React membandingkan hasil render baru dengan yang lama (<b>reconciliation</b>) dan hanya mengubah bagian DOM yang berbeda: angka di Header. Bagian lain di layar tidak disentuh.',it:g(x=>x==='hd'?'ok':'mute',()=>'mute',[isi])}]}};

/* ---------- hash table ---------- */
S.hash={t:'Hash table: fungsi hash menunjuk laci yang tepat',
 p:[{k:'isi',l:'Kunci (pisahkan koma)',t:'s',v:'apel, jeruk, mangga, kiwi, salak, duku'},{k:'m',l:'Jumlah laci (bucket)',t:'n',min:3,max:7,v:5},{k:'cari',l:'Kunci yang dicari',t:'s',v:'kiwi'}],
 steps:P=>{let K=[...new Set(nama(P.isi,7).map(s=>s.toLowerCase()))];if(!K.length)K=['apel'];const m=Math.max(3,Math.min(7,P.m));
  const kode=s=>[...s].reduce((a,c)=>a+c.charCodeAt(0),0),h=s=>kode(s)%m,X=i=>(i-(m-1)/2)*1.45;
  const cari=(String(P.cari).split(',')[0]||'').trim().toLowerCase().slice(0,8)||K[0],hc=h(cari);
  const pos={},isi=Array.from({length:m},()=>[]);K.forEach(k=>{const b=h(k);pos[k]=[b,isi[b].length];isi[b].push(k)});
  const laci=f=>Array.from({length:m},(_,i)=>B('b'+i,X(i),-.35,0,{w:1.25,h:.2,d:1.3,c:f?f(i):'glass',t:String(i)}));
  const kunci=(k,c,on=true)=>{const [b,d]=pos[k];return B('k'+k,on?X(b):X(b),on?d*.55+.05:3,0,{w:1.2,h:.48,d:.9,c,t:E(k)})};
  const lt=lantai(Math.max(8,m*1.5+1),3.4,-.6),tab=K.filter(k=>isi[pos[k][0]].length>1),k0=K[0];
  const rantai=isi[hc],ada=rantai.includes(cari);
  return [
   {cap:`Hash table menyiapkan ${m} <b>laci</b> bernomor 0 sampai ${m-1}. Tujuannya: menyimpan dan menemukan data <b>tanpa memeriksa satu per satu</b>.`,it:[lt,...laci()]},
   {cap:`<b>Fungsi hash</b> mengubah kunci menjadi nomor laci. Di sini: jumlahkan kode huruf "${E(k0)}" = ${kode(k0)}, lalu ${kode(k0)} mod ${m} = <b>${h(k0)}</b>. Kunci yang sama selalu menghasilkan nomor yang sama.`,
    it:[lt,...laci(i=>i===h(k0)?'ok':'glass'),kunci(k0,'warn'),G('rumus',X(h(k0)),2.1,0,`${kode(k0)} mod ${m} = ${h(k0)}`,'warn')]},
   {cap:`Semua kunci dimasukkan dengan cara yang sama: ${K.map(k=>`${E(k)}→${h(k)}`).join(', ')}.`,it:[lt,...laci(),...K.map(k=>kunci(k,'acc'))]},
   tab.length?{cap:`<b>Tabrakan</b> (collision): ${tab.map(E).join(', ')} mendapat laci yang sama. Solusinya <i>chaining</i>: laci menyimpan daftar kecil, jadi kunci ditumpuk di laci itu.`,it:[lt,...laci(i=>isi[i].length>1?'bad':'glass'),...K.map(k=>kunci(k,tab.includes(k)?'warn':'mute'))]}
    :{cap:'Kali ini tidak ada tabrakan: setiap kunci mendapat laci sendiri. Kalau dua kunci mendapat laci yang sama, laci itu menyimpan daftar kecil (<i>chaining</i>). Coba kurangi jumlah laci di Eksperimen.',it:[lt,...laci(),...K.map(k=>kunci(k,'acc'))]},
   {cap:`Mencari "${E(cari)}": hitung hash-nya = <b>${hc}</b>, langsung buka laci ${hc}${rantai.length>1?`, lalu bandingkan ${rantai.length} kunci di dalamnya`:''}. ${ada?'<b>Ketemu.</b>':'Tidak ada di laci itu, jadi kunci ini <b>tidak tersimpan</b>.'} Laci lain tidak disentuh sama sekali.`,
    it:[lt,...laci(i=>i===hc?(ada?'ok':'bad'):'glass'),...K.map(k=>kunci(k,k===cari?'ok':pos[k][0]===hc?'warn':'mute')),G('cari',X(hc),Math.max(1,rantai.length*.55+.6),0,'hash("'+E(cari)+'") = '+hc,ada?'ok':'bad')]},
   {cap:`Rata-rata pencarian <b>O(1)</b>: berapa pun banyak datanya, langkahnya tetap. Load factor = ${K.length}/${m} = ${(K.length/m).toFixed(2)}. Kalau terlalu penuh, tabel diperbesar (rehash) agar tabrakan tetap jarang. <code>dict</code> Python dan <code>HashMap</code> Java bekerja seperti ini.`,it:[lt,...laci(),...K.map(k=>kunci(k,'acc'))]}]}};

/* ---------- binary search ---------- */
S.bsearch={t:'Binary search: buang separuh data setiap langkah',
 p:[{k:'n',l:'Jumlah data (terurut)',t:'n',min:5,max:15,v:11},{k:'cari',l:'Angka yang dicari',t:'n',min:-99,max:999,v:56}],
 steps:P=>{const n=Math.max(5,Math.min(15,P.n)),A=[2,5,8,12,16,23,38,45,56,72,81,88,91,95,99].slice(0,n),X=i=>(i-(n-1)/2)*.78,c=P.cari;
  const lt=lantai(Math.max(8,n*.8+1.5),3);
  const sel=(lo,hi,mid,found)=>A.map((v,i)=>{const inR=i>=lo&&i<=hi;return B('a'+i,X(i),inR?0:-.25,0,{w:.68,h:inR?.62:.3,d:.8,c:i===mid?(found?'ok':'warn'):inR?'acc':'mute',t:String(v)})});
  const pin=(lo,hi,mid)=>[G('lo',X(lo),1.2,0,'lo','idx'),G('hi',X(hi),1.2,0,'hi','idx'),...(mid!=null?[G('mid',X(mid),1.8,0,'mid','warn')]:[])].filter((g,j,arr)=>!(g.id==='hi'&&lo===hi));
  const st=[{lb:'Data terurut',cap:`Ada ${n} angka yang sudah <b>terurut</b>. Binary search hanya bekerja pada data terurut. Kita mencari <b>${c}</b>.`,it:[lt,...sel(0,n-1),...pin(0,n-1)]}];
  let lo=0,hi=n-1,k=0,found=false;
  while(lo<=hi){const mid=(lo+hi)>>1;k++;const v=A[mid];
    if(v===c){found=true;st.push({lb:'Ketemu',cap:`mid = (${lo} + ${hi}) / 2 = ${mid}. A[${mid}] = ${v}: <b>ketemu</b> dalam ${k} langkah.`,it:[lt,...sel(lo,hi,mid,1),...pin(lo,hi,mid)]});break}
    st.push({lb:'Langkah '+k,cap:`mid = (${lo} + ${hi}) / 2 = ${mid}. A[${mid}] = ${v} ${v<c?`lebih kecil dari ${c}, jadi buang separuh <b>kiri</b>: lo = ${mid+1}.`:`lebih besar dari ${c}, jadi buang separuh <b>kanan</b>: hi = ${mid-1}.`}`,it:[lt,...sel(lo,hi,mid),...pin(lo,hi,mid)]});
    if(v<c)lo=mid+1;else hi=mid-1}
  if(!found)st.push({lb:'Tidak ada',cap:`lo melewati hi, artinya rentang pencarian habis: <b>${c} tidak ada</b>. Hanya ${k} angka yang diperiksa.`,it:[lt,...sel(1,0),G('x',0,1.4,0,'rentang kosong','bad')]});
  st.push({lb:'O(log n)',cap:`Binary search memeriksa ${k} angka; pencarian linear bisa memeriksa sampai ${n}. Untuk sejuta data cukup sekitar <b>20 langkah</b>, karena setiap langkah membuang separuh: O(log n).`,it:st[st.length-1].it});
  return st}};

/* ---------- graph: BFS dan DFS ---------- */
S.graph={t:'Graph: menjelajah simpul dengan BFS atau DFS',
 p:[{k:'mode',l:'Cara menjelajah',t:'o',o:[['bfs','BFS (melebar, pakai queue)'],['dfs','DFS (mendalam, pakai stack)']],v:'bfs'},{k:'s',l:'Mulai dari',t:'o',o:[['A','A'],['C','C'],['G','G']],v:'A'}],
 steps:P=>{const N={A:[-3.6,1.2,'A'],B:[-1.6,2.4,'B'],C:[-1.6,0,'C'],D:[.6,2.4,'D'],E:[.6,0,'E'],F:[3,1.2,'F'],G:[2.8,-1.2,'G']};
  const Ed=[['A','B'],['A','C'],['B','D'],['C','E'],['D','F'],['E','F'],['E','G'],['F','G']],adj={};
  Object.keys(N).forEach(k=>adj[k]=[]);Ed.forEach(([a,b])=>{adj[a].push(b);adj[b].push(a)});Object.values(adj).forEach(v=>v.sort());
  const bfs=P.mode!=='dfs',s=N[P.s]?P.s:'A',seen=new Set([s]),done=[],via={};let F=[[s,null]];const st=[];
  const tagF=()=>G('fr',0,-2.5,0,(bfs?'antrean: ':'stack: ')+(F.length?F.map(f=>f[0]).join(' '):'kosong'),'idx');
  const draw=(cur)=>graf(N,Ed,k=>k===cur?'warn':done.includes(k)?'ok':F.some(f=>f[0]===k)?'acc':'mute',(a,b)=>via[b]===a||via[a]===b?'ok':'mute',1,'gedung');
  st.push({lb:'Mulai',cap:`Graph berisi ${Object.keys(N).length} simpul dan ${Ed.length} ruas. Kita menjelajah dengan <b>${bfs?'BFS':'DFS'}</b> mulai dari ${s}. ${bfs?'BFS memakai antrean (queue): yang masuk duluan diproses duluan.':'DFS memakai stack: yang terakhir masuk diproses duluan, jadi terus masuk ke dalam.'}`,it:[...draw(null),tagF()]});
  while(F.length){const [cur,par]=bfs?F.shift():F.pop();if(done.includes(cur))continue;done.push(cur);if(par)via[cur]=par;
    const baru=adj[cur].filter(x=>bfs?!seen.has(x):!done.includes(x));
    if(bfs)baru.forEach(x=>{seen.add(x);F.push([x,cur])});else [...baru].reverse().forEach(x=>F.push([x,cur]));
    st.push({lb:'Kunjungi '+cur,cap:`Ambil <b>${cur}</b> dari ${bfs?'depan antrean':'atas stack'}. Tetangga yang belum dikunjungi: ${baru.length?baru.join(', '):'tidak ada'}${baru.length?`, ${bfs?'masuk ke belakang antrean':'ditumpuk ke stack'}`:''}. Urutan sejauh ini: ${done.join(' → ')}.`,it:[...draw(cur),tagF()]})}
  st.push({lb:'Intinya',cap:`Urutan ${bfs?'BFS':'DFS'}: <b>${done.join(' → ')}</b>. ${bfs?'BFS menjelajah lapis demi lapis, sehingga menemukan jalur dengan ruas paling sedikit.':'DFS menelusuri satu cabang sampai mentok baru mundur; cocok untuk mendeteksi siklus dan topological sort.'} Ganti caranya di panel Eksperimen untuk membandingkan.`,it:[...draw(null)]});
  return st}};

/* ---------- pipeline data (ETL) ---------- */
S.etl={t:'Pipeline data: Extract, Transform, Load',
 p:[{k:'kotor',l:'Baris kotor (kosong/duplikat)',t:'n',min:0,max:3,v:2},{k:'mode',l:'Cara jalan',t:'o',o:[['batch','Batch (terjadwal)'],['stream','Streaming (terus-menerus)']],v:'batch'}],
 steps:P=>{const kt=Math.max(0,Math.min(3,P.kotor)),R8=8,SC=['acc','warn','mute'],src=i=>i%3,dirty=i=>i<kt*3&&i%3===1;
  const ST=[-3.9,-1.8,.2,2.2,4],lt=lantai(10.5,4);
  const sumber=[B('s0',ST[0],1.75,0,{w:.9,h:.8,d:.9,c:'acc',t:'DB app',s:'db'}),B('s1',ST[0],.6,0,{w:.8,h:1,d:.1,c:'warn',t:'CSV',s:'dok'}),B('s2',ST[0],-.45,0,{w:1,h:.8,d:.9,c:'mute',t:'API',s:'server'})];
  const tahap=on=>[G('tE',ST[1],2.9,0,'Extract',on==='E'?'warn':'idx'),G('tT',ST[2],2.9,0,'Transform',on==='T'?'warn':'idx'),G('tL',ST[3],2.9,0,'Load',on==='L'?'warn':'idx')];
  const wh=B('wh',ST[4],.2,0,{w:1.7,h:1.6,d:1.5,c:'mute',t:'warehouse',s:'gudang'});
  const bersih=Array.from({length:R8},(_,i)=>i).filter(i=>!dirty(i));
  const row=(i,x,y,c,z=0)=>B('r'+i,x,y,z,{w:.42,h:.42,d:.42,c,t:dirty(i)?'!':''});
  const awal=i=>row(i,ST[0]+1.25,1.8-src(i)*1.2,SC[src(i)],(Math.floor(i/3)-1)*.45);
  const pipa=[R('p1',[ST[0]+.8,.6,0],[ST[3]+.5,.6,0],'mute')];
  return [
   {cap:`Data tersebar di tiga <b>sumber</b> dengan format berbeda: database aplikasi, file CSV, dan API. ${kt?`Ada ${kt} baris kotor (tanda !).`:'Semua baris bersih.'}`,it:[lt,...sumber,...tahap(),wh,...Array.from({length:R8},(_,i)=>awal(i))]},
   {cap:'<b>Extract</b>: pipeline menyalin data dari setiap sumber ke area sementara (staging) tanpa mengubah isinya.',it:[lt,...sumber,...tahap('E'),wh,...pipa,...Array.from({length:R8},(_,i)=>row(i,ST[1]+(i%2)*.5-.25,Math.floor(i/2)*.48-.2,SC[src(i)]))]},
   {cap:`<b>Transform</b>: data dibersihkan dan diseragamkan: format tanggal dan mata uang disamakan${kt?`, ${kt} baris kotor dibuang`:''}. Semua baris kini berwarna sama karena formatnya seragam.`,
    it:[lt,...sumber,...tahap('T'),wh,...pipa,...Array.from({length:R8},(_,i)=>dirty(i)?row(i,ST[2]+Math.floor(i/3)*.7-.7,-.35,'bad',1.4):row(i,ST[2]+(bersih.indexOf(i)%2)*.5-.25,Math.floor(bersih.indexOf(i)/2)*.48-.2,'ok'))]},
   {cap:`<b>Load</b>: ${bersih.length} baris bersih dimuat ke <b>data warehouse</b>, gudang data yang dirancang untuk analisis. Kalau pipeline dijalankan ulang, hasilnya harus tetap sama (<i>idempoten</i>).`,
    it:[lt,...sumber,...tahap('L'),B('wh',ST[4],.2,0,{w:1.7,h:1.6,d:1.5,c:'ok',t:'warehouse',s:'gudang'}),...pipa,...bersih.map((i,j)=>row(i,ST[4]+(j%2)*.5-.25,Math.floor(j/2)*.48-.35,'ok',.95))]},
   {cap:'Analis dan dashboard membaca dari warehouse, bukan dari database aplikasi, sehingga query berat tidak mengganggu pengguna aplikasi.',
    it:[lt,...sumber,...tahap(),B('wh',ST[4],.2,0,{w:1.7,h:1.6,d:1.5,c:'ok',t:'warehouse',s:'gudang'}),...[.8,1.4,1.1].map((h,j)=>B('bar'+j,ST[4]-.5+j*.5,1.6+h/2,0,{w:.38,h,d:.38,c:['acc','warn','ok'][j]})),G('dash',ST[4],3.4,0,'dashboard','idx')]},
   P.mode==='stream'?{cap:'<b>Streaming</b>: setiap kejadian (pesanan, klik) mengalir saat itu juga lewat antrean pesan seperti <b>Kafka</b>. Data di dashboard hampir real-time, tetapi sistemnya lebih rumit.',
      it:[lt,...sumber,...tahap(),B('wh',ST[4],.2,0,{w:1.7,h:1.6,d:1.5,c:'ok',t:'warehouse',s:'gudang'}),R('p1',[ST[0]+.8,.6,0],[ST[3]+.5,.6,0],'ok'),...bersih.slice(0,5).map((i,j)=>row(i,ST[1]+j*1.1-.3,.6,'ok'))]}
    :{cap:'<b>Batch</b>: pipeline berjalan terjadwal, misalnya setiap malam pukul 01.00, memproses semua data sehari sekaligus. Penjadwalnya biasanya <b>Airflow</b> dalam bentuk DAG. Sederhana dan murah, tetapi datanya tertinggal sampai jadwal berikutnya.',
      it:[lt,...sumber,...tahap(),B('wh',ST[4],.2,0,{w:1.7,h:1.6,d:1.5,c:'ok',t:'warehouse',s:'gudang'}),...pipa,G('jam',0,-1.6,0,'⏰ setiap hari 01.00','warn'),...Array.from({length:R8},(_,i)=>awal(i))]}]}};

/* ---------- sorting dasar ---------- */
S.sort={t:'Sorting dasar: bubble sort dan insertion sort langkah demi langkah',
 p:[{k:'isi',l:'Angka (pisahkan koma)',t:'s',v:'5, 2, 8, 1, 9, 3'},{k:'algo',l:'Algoritma',t:'o',o:[['bubble','Bubble sort'],['insert','Insertion sort']],v:'bubble'}],
 steps:P=>{let v=angka(P.isi,7).map(x=>Math.max(-99,Math.min(99,x)));if(v.length<2)v=[5,2,8,1];const n=v.length;
  const mx=Math.max(...v.map(Math.abs),1),X=i=>(i-(n-1)/2)*1.05,lt=lantai(Math.max(8,n*1.1+1.5),3);
  let a=v.map((x,i)=>({x,id:i}));const st=[];
  const bar=(o,i,c,up=0)=>{const h=.25+Math.abs(o.x)/mx*2.4;return B('s'+o.id,X(i),h/2-.5+up,0,{w:.82,h,d:.82,c,t:String(o.x)})};
  const snap=f=>a.map((o,i)=>bar(o,i,...f(i,o)));
  st.push({lb:'Mulai',cap:`Data awal: ${v.join(', ')}. Tinggi balok sesuai nilainya. Kita urutkan dari kecil ke besar dengan <b>${P.algo==='insert'?'insertion sort':'bubble sort'}</b>.`,it:[lt,...snap(()=>['acc'])]});
  let cmp=0,swp=0;
  if(P.algo==='insert'){
    for(let i=1;i<n;i++){const key=a[i];
      st.push({lb:'Ambil '+key.x,cap:`Ambil ${key.x}. Bagian kiri (hijau) sudah terurut; ${key.x} akan disisipkan ke posisi yang tepat di sana.`,it:[lt,...snap((j,o)=>o===key?['warn',.9]:j<i?['ok']:['acc'])]});
      let j=i-1;while(j>=0&&a[j].x>key.x){cmp++;a[j+1]=a[j];j--}if(j>=0)cmp++;a[j+1]=key;swp+=i-1-j;
      st.push({lb:'Sisipkan '+key.x,cap:`${i-1-j?`${i-1-j} angka yang lebih besar digeser ke kanan, lalu ${key.x} masuk di posisi ${j+1}.`:`${key.x} sudah lebih besar dari tetangga kirinya, jadi tetap di tempat.`}`,it:[lt,...snap((q,o)=>o===key?['warn']:q<=i?['ok']:['acc'])]})}}
  else{
    for(let p=0;p<n-1;p++){let tukar=false;
      for(let j=0;j<n-1-p;j++){cmp++;const t=a[j].x>a[j+1].x;if(t){[a[j],a[j+1]]=[a[j+1],a[j]];swp++;tukar=true}
        st.push({lb:`Putaran ${p+1}`,cap:`Bandingkan dua tetangga: ${t?`${a[j+1].x} &gt; ${a[j].x}, jadi <b>ditukar</b>.`:`${a[j].x} ≤ ${a[j+1].x}, sudah urut, tidak ditukar.`}${j===n-2-p?` Akhir putaran ${p+1}: angka terbesar yang tersisa sudah "menggelembung" ke kanan.`:''}`,
          it:[lt,...snap((q)=>q===j||q===j+1?[t?'bad':'warn']:q>=n-p?['ok']:['acc'])]})}
      if(!tukar){st.push({lb:'Berhenti dini',cap:`Satu putaran penuh tanpa pertukaran: data sudah urut, jadi berhenti lebih awal.`,it:[lt,...snap(()=>['ok'])]});break}}}
  st.push({lb:'Selesai',cap:`Terurut: ${a.map(o=>o.x).join(', ')}. Butuh ${cmp} perbandingan dan ${swp} ${P.algo==='insert'?'pergeseran':'pertukaran'}. Kedua algoritma ini O(n²): cukup untuk data kecil, tetapi untuk data besar pakai merge sort atau sort bawaan bahasa.`,it:[lt,...snap(()=>['ok'])]});
  return st}};

/* ===================== DATA SCIENCE ===================== */
/* ---------- K-Means ---------- */
S.kmeans={t:'K-Means: titik berkumpul ke pusat kelompok terdekat',
 p:[{k:'k',l:'Jumlah kelompok (k)',t:'n',min:2,max:4,v:3}],
 steps:P=>{const k=Math.max(2,Math.min(4,P.k)),rnd=prng(11),KC=['acc','warn','ok','bad'];
  const pusat=[[-2.6,-1],[2.4,-1.2],[0,1.4],[2.6,1.5]],pts=[];
  for(let i=0;i<21;i++){const c=pusat[i%3];pts.push([c[0]+(rnd()-.5)*2.2,c[1]+(rnd()-.5)*1.6])}
  let C=pts.slice(0,k).map(p=>[p[0]+.3,p[1]-.2]);const lt=lantai(8.5,5.4,-.35);
  const dot=(i,c)=>B('p'+i,pts[i][0],-.05,pts[i][1],{w:.36,h:.36,d:.36,c,ball:1});
  const cen=(j,on=1)=>B('c'+j,C[j][0],.5,C[j][1],{w:.42,h:1.1,d:.42,c:KC[j],t:'',s:'orang'});
  const lab=()=>pts.map(p=>{let b=0,bd=1e9;C.forEach((c,j)=>{const d=(p[0]-c[0])**2+(p[1]-c[1])**2;if(d<bd){bd=d;b=j}});return b});
  const st=[{lb:'Data',cap:`Ada ${pts.length} pelanggan tanpa label. Kita ingin membaginya menjadi <b>${k} kelompok</b> yang mirip. Posisi titik = dua fitur, misalnya frekuensi beli dan nilai belanja.`,it:[lt,...pts.map((_,i)=>dot(i,'mute'))]},
   {lb:'Pusat awal',cap:`K-Means memilih ${k} <b>pusat</b> awal (di sini: titik-titik pertama). Pusatnya digambarkan sebagai "ketua kelompok".`,it:[lt,...pts.map((_,i)=>dot(i,'mute')),...C.map((_,j)=>cen(j))]}];
  for(let it=1;it<=3;it++){const L=lab();
   st.push({lb:'Putaran '+it+': pilih',cap:`Setiap titik bergabung ke pusat <b>terdekat</b> dan ikut warnanya.${it>1?' Beberapa titik pindah kelompok karena pusatnya sudah bergeser.':''}`,it:[lt,...pts.map((_,i)=>dot(i,KC[L[i]])),...C.map((_,j)=>cen(j))]});
   const N=C.map((c,j)=>{const m=pts.filter((_,i)=>L[i]===j);return m.length?[m.reduce((a,p)=>a+p[0],0)/m.length,m.reduce((a,p)=>a+p[1],0)/m.length]:c});
   const geser=Math.max(...N.map((n,j)=>Math.hypot(n[0]-C[j][0],n[1]-C[j][1])));C=N;
   st.push({lb:'Putaran '+it+': geser',cap:`Setiap pusat pindah ke <b>rata-rata</b> anggotanya (pergeseran terbesar ${geser.toFixed(2)}). ${geser<.05?'Pusat hampir tidak bergerak lagi: algoritma <b>konvergen</b>.':'Ulangi: pilih pusat terdekat, lalu geser lagi.'}`,it:[lt,...pts.map((_,i)=>dot(i,KC[L[i]])),...C.map((_,j)=>cen(j))]});
   if(geser<.05)break}
  st.push({lb:'Intinya',cap:'K-Means mengulang dua langkah: <b>tetapkan</b> ke pusat terdekat, lalu <b>geser</b> pusat ke rata-rata. Fitur harus distandardisasi dulu, dan k dipilih dengan metode siku serta akal sehat bisnis. Ganti k di panel Eksperimen.',it:st[st.length-1].it});
  return st}};

/* ---------- gradient descent ---------- */
S.gd={t:'Gradient descent: bola menuruni lembah loss',
 p:[{k:'lr',l:'Learning rate',t:'o',o:[['0.1','0.1 (pelan)'],['0.3','0.3 (pas)'],['0.9','0.9 (memantul)'],['1.05','1.05 (meledak)']],v:'0.3'}],
 steps:P=>{const lr=+P.lr||.3,L=w=>(w-3)**2,X=w=>(w-3)*.75,Y=w=>Math.min(L(w),16)*.16-.2;
  const kurva=[];for(let i=0;i<24;i++){const a=-1+i*(8/23),b=-1+(i+1)*(8/23);kurva.push(R('k'+i,[X(a),Y(a),0],[X(b),Y(b),0],'mute'))}
  const lt=lantai(8,2.4,-.5),base=[lt,...kurva,G('min',X(3),-.9,0,'minimum: w = 3','ok')];
  const bola=(w,c)=>B('bola',X(Math.max(-1,Math.min(7,w))),Y(Math.max(-1,Math.min(7,w)))+.28,0,{w:.5,h:.5,d:.5,c,ball:1,t:''});
  let w=-1;const st=[{lb:'Mulai',cap:`Loss <code>L(w) = (w − 3)²</code> berbentuk lembah, paling rendah di w = 3. Bola mulai di w = ${w}. Learning rate = <b>${lr}</b>.`,it:[...base,bola(w,'warn')]}];
  for(let i=1;i<=6;i++){const g=2*(w-3),w2=w-lr*g;
   st.push({lb:'Langkah '+i,cap:`Turunan di w = ${w.toFixed(2)} adalah ${g.toFixed(2)}. Langkah: w = ${w.toFixed(2)} − ${lr} × ${g.toFixed(2)} = <b>${w2.toFixed(2)}</b>. Loss ${L(w).toFixed(2)} → ${L(w2).toFixed(2)}.`,it:[...base,bola(w2,Math.abs(w2-3)<Math.abs(w-3)?'ok':'bad'),G('tr',X(Math.max(-1,Math.min(7,w2))),Y(Math.max(-1,Math.min(7,w2)))+1,0,'w = '+w2.toFixed(2),'idx')]});w=w2}
  st.push({lb:'Intinya',cap:Math.abs(w-3)<.1?`Bola sampai di dasar lembah (w ≈ ${w.toFixed(2)}). Inilah cara model belajar: ulangi <code>w = w − lr × turunan</code>.`:lr>1?'Learning rate terlalu besar: setiap langkah melompati dasar lembah dan makin menjauh. Model <b>gagal konvergen</b>.':lr>.5?'Bola memantul ke kiri-kanan dasar lembah sebelum tenang. Bisa sampai, tetapi boros langkah.':'Bola bergerak terlalu pelan; butuh lebih banyak langkah untuk sampai.',it:[...base,bola(w,Math.abs(w-3)<.1?'ok':'warn')]});
  return st}};

/* ---------- train/test split ---------- */
S.split={t:'Train/test split: model diuji dengan data yang belum pernah dilihat',
 p:[{k:'u',l:'Porsi data uji (%)',t:'o',o:[['20','20%'],['25','25%'],['30','30%']],v:'25'}],
 steps:P=>{const n=20,u=Math.round(n*(+P.u||25)/100),rnd=prng(5),ord=[...Array(n).keys()].sort(()=>rnd()-.5);
  const X=i=>(i-(n-1)/2)*.42,lt=lantai(10,4.4,-.45),uji=new Set(ord.slice(0,u)),benar=new Set(ord.slice(0,u).filter((_,j)=>j%4!==3));
  const row=(i,x,z,c)=>B('r'+i,x,0,z,{w:.38,h:.5,d:.7,c,t:String(i+1)});
  const model=B('model',-.6,1.6,-1.4,{w:1.2,h:1.1,d:1,c:'glass',t:'model',s:'server'});
  const trainPos=i=>{const k=ord.indexOf(i)-u;return [-4+(k%8)*.45,-1.2+Math.floor(k/8)*.9]},testPos=i=>{const k=ord.indexOf(i);return [2.6+(k%4)*.45,-1.2+Math.floor(k/4)*.9]};
  return [
   {lb:'Data',cap:`Ada ${n} baris data berlabel (misalnya pelanggan dan apakah ia churn).`,it:[lt,...[...Array(n).keys()].map(i=>row(i,X(i),0,'acc'))]},
   {lb:'Acak',cap:'Data <b>diacak</b> dulu (lihat nomor barisnya berpindah) agar data latih dan uji sama-sama mewakili. Dengan <code>stratify=y</code>, proporsi kelas juga dijaga sama.',it:[lt,...[...Array(n).keys()].map(i=>row(i,X(ord.indexOf(i)),0,'acc'))]},
   {lb:'Bagi',cap:`<code>train_test_split(test_size=${(u/n).toFixed(2)})</code>: ${n-u} baris untuk <b>latih</b>, ${u} baris <b>disembunyikan</b> untuk uji (kuning).`,it:[lt,...[...Array(n).keys()].map(i=>{const t=uji.has(i),[x,z]=t?testPos(i):trainPos(i);return row(i,x,z,t?'warn':'acc')}),G('gl',-2.4,1.2,-.75,'data latih','idx'),G('gu',3.3,1.2,-.75,'data uji','warn')]},
   {lb:'Latih',cap:'<code>model.fit(X_train, y_train)</code>: model hanya belajar dari data latih. Data uji tetap tersembunyi.',it:[lt,model,...[...Array(n).keys()].map(i=>{const t=uji.has(i),[x,z]=t?testPos(i):trainPos(i);return row(i,x,z,t?'mute':'acc')}),R('fl',[-2.4,.4,-1.4],[-1.2,1.4,-1.4],'acc')]},
   {lb:'Uji',cap:`<code>model.score(X_test, y_test)</code>: model menebak data yang belum pernah dilihat. Benar ${benar.size} dari ${u} (${Math.round(benar.size/u*100)}%). Inilah perkiraan jujur kinerjanya di dunia nyata.`,it:[lt,model,...[...Array(n).keys()].map(i=>{const t=uji.has(i),[x,z]=t?testPos(i):trainPos(i);return row(i,x,z,t?(benar.has(i)?'ok':'bad'):'mute')}),R('fu',[0,1.4,-1.4],[2.6,.4,-1.4],'warn')]},
   {lb:'Intinya',cap:'Menilai model di data latihnya sendiri seperti ujian dengan soal yang sudah dibocorkan: nilainya tinggi tetapi menipu. Untuk penilaian yang lebih stabil, pakai <b>cross-validation</b>.',it:[lt,model,...[...Array(n).keys()].map(i=>{const t=uji.has(i),[x,z]=t?testPos(i):trainPos(i);return row(i,x,z,t?(benar.has(i)?'ok':'bad'):'acc')})]}]}};

/* ---------- stack ---------- */
S.stack={t:'Stack: tumpukan piring, yang terakhir masuk keluar pertama (LIFO)',
 p:[{k:'n',l:'Jumlah push',t:'n',min:1,max:6,v:3},{k:'k',l:'Jumlah pop',t:'n',min:0,max:6,v:1}],
 steps:P=>{const L='ABCDEF'.slice(0,P.n).split(''),k=Math.min(P.k,P.n);
  const p=(id,i,c='acc',x=0,y)=>B(id,x,y??i*.55-.3,0,{w:2.4,h:.26,d:2.4,c,t:id,s:'piring'});
  const base=[lantai(7,4),G('top',-3,2.4,0,'↓ push · ↑ pop di atas','idx')];
  const keluar=L.slice(L.length-k).reverse();
  return [
   {cap:`Stack bekerja seperti tumpukan piring: piring baru selalu ditaruh <b>di atas</b>. Kita akan push ${P.n} piring.`,it:[...base,p(L[0],0)]},
   {cap:`${L.map(x=>`<code>push(${x})</code>`).join(' ')}: tumpukan setinggi ${P.n}. Piring ${L[L.length-1]} ada di paling atas.`,it:[...base,...L.map((x,i)=>p(x,i,i===L.length-1?'ok':'acc'))]},
   {cap:`<code>peek()</code> hanya melihat piring paling atas (${L[L.length-1]}) tanpa mengambilnya.`,it:[...base,...L.map((x,i)=>p(x,i,i===L.length-1?'warn':'acc'))]},
   k?{cap:`${k}× <code>pop()</code> mengambil dari atas: ${keluar.join(', ')}. Yang terakhir masuk keluar pertama (LIFO).${P.k>P.n?` Pop ke-${P.n+1} akan error karena stack sudah kosong.`:''}`,
      it:[...base,...L.map((x,i)=>i>=L.length-k?p(x,i,'bad',3,(L.length-1-i)*.55+.6):p(x,i))]}
    :{cap:'Tanpa <code>pop()</code>, semua piring tetap di tumpukan.',it:[...base,...L.map((x,i)=>p(x,i))]},
   {cap:`Sisa di stack: ${L.length-k?L.slice(0,L.length-k).join(', '):'kosong'}. Stack dipakai untuk Undo, tombol Back di browser, dan <b>call stack</b>.`,it:[...base,...L.slice(0,L.length-k).map((x,i)=>p(x,i))]}]}};

/* ---------- queue ---------- */
S.queue={t:'Queue: antrean kasir, yang pertama datang dilayani pertama (FIFO)',
 p:[{k:'q',l:'Antrean (pisah koma)',t:'s',v:'Ani, Budi, Citra'},{k:'k',l:'Jumlah dilayani',t:'n',min:0,max:5,v:1}],
 steps:P=>{let Q=nama(P.q,5);if(!Q.length)Q=['Ani'];const k=Math.min(P.k,Q.length);
  const o=(id,i,c='acc')=>B('q-'+id,i*1.15-1.6,.05,0,{w:.8,h:1.4,d:.55,c,t:E(id),s:'orang'});
  const kasir=[lantai(10,3),B('kasir',-3.6,0,0,{w:1,h:1.6,d:1.6,c:'glass',t:'kasir'}),G('dep',-2.4,1.8,0,'depan: keluar','idx'),G('bel',2.6,1.8,0,'belakang: masuk','idx')];
  return [
   {cap:`Queue seperti antrean kasir: orang baru masuk dari <b>belakang</b>, yang dilayani selalu yang paling <b>depan</b>. ${E(Q[0])} datang pertama.`,it:[...kasir,o(Q[0],0)]},
   {cap:`${Q.slice(1).map(x=>`<code>enqueue(${E(x)})</code>`).join(' ')||'Tidak ada yang datang lagi.'} Setiap orang baru berdiri di belakang.`,it:[...kasir,...Q.map((x,i)=>o(x,i,i?'ok':'acc'))]},
   k?{cap:`${k}× <code>dequeue()</code> melayani ${Q.slice(0,k).map(E).join(', ')}: yang datang <b>pertama</b> dilayani pertama (FIFO).${P.k>Q.length?' Dequeue berikutnya error karena antrean kosong.':''}`,it:[...kasir,...Q.map((x,i)=>i<k?B('q-'+x,-3.6+i*.25,1.9,i*.3,{w:.8,h:1.4,d:.55,c:'warn',t:E(x),s:'orang'}):o(x,i))]}
    :{cap:'Belum ada yang dilayani; antrean tetap utuh.',it:[...kasir,...Q.map((x,i)=>o(x,i))]},
   {cap:`Antrean maju: ${Q.length-k?E(Q[k])+' sekarang di depan':'antrean kosong'}. Queue dipakai untuk antrean cetak, pesan masuk, dan BFS pada graf.`,it:[...kasir,...Q.slice(k).map((x,i)=>o(x,i))]}]}};

/* ---------- rekursi / call stack ---------- */
S.rekursi={t:'Rekursi dan call stack: fungsi yang memanggil dirinya sendiri',
 p:[{k:'n',l:'Hitung faktorial(n), n =',t:'n',min:1,max:6,v:3}],
 steps:P=>{const N=P.n,fak=n=>n<=1?1:n*fak(n-1);
  const f=(n,k,c='acc',t)=>B('f'+n,0,k*.6-.2,0,{w:3.6,h:.5,d:2,c,t:t||`faktorial(${n})`});
  const base=[lantai(7,4)],st=[];
  for(let d=0;d<N;d++){const n=N-d,frames=[...Array(d+1)].map((_,j)=>f(N-j,j,j===d?(n===1?'ok':'acc'):'mute'));
    st.push({cap:d===0?`Setiap pemanggilan fungsi membuat <b>bingkai</b> baru di call stack. <code>faktorial(${N})</code> dipanggil pertama.`
      :n===1?`faktorial(2) memanggil faktorial(1). Inilah <b>kasus dasar</b>: langsung mengembalikan 1 tanpa memanggil lagi. Tumpukan setinggi ${N} bingkai.`
      :`faktorial(${n+1}) butuh faktorial(${n}), jadi bingkai baru ditumpuk. Bingkai di bawahnya <b>menunggu</b>.`,it:[...base,...frames]})}
  for(let n=2;n<=N;n++){const k=N-n,frames=[...Array(k+1)].map((_,j)=>j===k?f(N-j,j,'warn',`faktorial(${n}) = ${fak(n)}`):f(N-j,j,'mute'));
    st.push({cap:`Bingkai teratas selesai dan dibuang. Hasil ${fak(n-1)} dikirim ke bawah: faktorial(${n}) = ${n} × ${fak(n-1)} = <b>${fak(n)}</b>.`,it:[...base,...frames,G('r',2.6,k*.6+.8,0,'↩ '+fak(n-1),'ok')]})}
  st.push({cap:`Hasil akhir faktorial(${N}) = <b>${fak(N)}</b>. Ada ${N} bingkai yang pernah ditumpuk. Tanpa kasus dasar, tumpukan terus tumbuh sampai <b>stack overflow</b>.`,it:[...base,f(N,0,'ok',`faktorial(${N}) = ${fak(N)}`)]});
  return st}};

/* ---------- pohon (BST) dan DOM ---------- */
function pohon(nodes,edges,hi,bad){const ys=Object.values(nodes).map(n=>n[1]),it=[lantai(9,3,Math.min(...ys)-1.8)];
  edges.forEach(([a,b])=>{const A=nodes[a],Bn=nodes[b];it.push(R('e'+a+'_'+b,[A[0],A[1],0],[Bn[0],Bn[1],0],hi&&hi.includes(String(a))&&hi.includes(String(b))?'warn':'mute'))});
  Object.entries(nodes).forEach(([k,[x,y,t]])=>it.push(B('n'+k,x,y,0,{w:t.length>3?1.5:.9,h:.8,d:.8,c:!hi?'acc':hi.includes(k)?(bad&&k===hi[hi.length-1]?'bad':'warn'):'mute',t})));return it}
S.tree={t:'Tree: data bercabang dari satu akar',
 p:[{k:'isi',l:'Angka yang disisipkan (urut)',t:'s',v:'8, 3, 10, 1, 6, 14'},{k:'cari',l:'Angka yang dicari',t:'n',min:-99,max:999,v:6}],
 steps:P=>{let v=[...new Set(angka(P.isi,9))];if(!v.length)v=[8];
  const T={};const ins=(x)=>{let c=v[0],d=0;if(!T[c])T[c]={d:0};if(x===c)return;for(;;){d++;const s=x<c?'l':'r';if(T[c][s]==null){T[c][s]=x;T[x]={d,p:c};return}c=T[c][s]}};
  v.forEach(ins);const order=[];(function io(n){if(n==null)return;io(T[n].l);order.push(n);io(T[n].r)})(v[0]);
  const W=order.length,N={},Ed=[];order.forEach((n,i)=>{N[n]=[(i-(W-1)/2)*Math.min(1.3,8/W),1.6-T[n].d*1.4,String(n)];if(T[n].p!=null)Ed.push([T[n].p,n])});
  const path=[];let c=v[0],found=false;while(c!=null){path.push(String(c));if(c===P.cari){found=true;break}c=P.cari<c?T[c].l:T[c].r}
  const maxd=Math.max(...order.map(n=>T[n].d))+1;
  const st=[{cap:`Angka ${v.join(', ')} disisipkan berurutan ke Binary Search Tree: yang lebih kecil ke kiri, yang lebih besar ke kanan. Akarnya ${v[0]}, tingginya ${maxd} tingkat.`,it:pohon(N,Ed)}];
  path.forEach((x,i)=>{const n=+x,last=i===path.length-1;
    st.push({cap:last&&found?`<b>${P.cari} ketemu</b> dalam ${i+1} langkah, tanpa memeriksa ${W-i-1} simpul lainnya.`
      :`Bandingkan ${P.cari} dengan ${n}: ${P.cari<n?`lebih kecil, ke <b>kiri</b>`:`lebih besar, ke <b>kanan</b>`}${(P.cari<n?T[n].l:T[n].r)==null?', tetapi cabang itu kosong.':'.'}`,it:pohon(N,Ed,path.slice(0,i+1))})});
  if(!found)st.push({cap:`Cabangnya kosong, jadi <b>${P.cari} tidak ada</b> di pohon. Pencarian berhenti setelah ${path.length} langkah saja.`,it:pohon(N,Ed,path,true)});
  return st}};
S.dom={t:'DOM: halaman HTML sebagai pohon elemen',steps:(()=>{
  const N={a:[0,1.6,'html'],b:[-2.2,0,'head'],c:[2.2,0,'body'],d:[-2.2,-1.6,'title'],e:[1,-1.6,'h1'],f:[3.4,-1.6,'p']},Ed=[['a','b'],['a','c'],['b','d'],['c','e'],['c','f']];
  return [
   {cap:'Browser membaca HTML lalu membangun <b>DOM</b>: pohon objek. <code>&lt;html&gt;</code> adalah akarnya.',it:pohon(N,Ed)},
   {cap:'Elemen yang bersarang di dalam elemen lain menjadi <b>anak</b>. <code>h1</code> dan <code>p</code> adalah anak <code>body</code> dan saling bersaudara.',it:pohon(N,Ed,['c','e','f'])},
   {cap:'JavaScript menelusuri pohon ini: <code>document.querySelector("h1")</code> berjalan dari akar sampai menemukan simpulnya, lalu bisa mengubah isinya.',it:pohon(N,Ed,['a','c','e'])}]})()};

/* ---------- class dan objek ---------- */
S.oop={t:'Class sebagai cetak biru, objek sebagai benda jadinya',
 p:[{k:'o',l:'Nama objek (pisahkan koma)',t:'s',v:'Oyen, Belang'}],
 steps:P=>{let O=nama(P.o,4);if(!O.length)O=['Oyen'];const X=i=>(i-(O.length-1)/2)*1.7,C=['warn','ok','acc','bad'];
  const cb=[B('cb',0,-.3,0,{w:Math.max(5,O.length*1.8),h:.15,d:3,c:'glass'}),G('cbt',-3.4,-.3,0,'class Kucing { nama, warna, meong() }')];
  const obj=(i,c)=>B('o'+i,X(i),1.2,0,{w:1.3,h:1.3,d:1.3,c,t:E(O[i]),tt:'objek'});
  return [
   {cap:'<b>Class</b> adalah cetak biru: daftar data (atribut) dan perilaku (method). Cetak biru sendiri belum menjadi kucing.',it:[lantai(8,5,-.8),...cb]},
   {cap:`<code>new Kucing("${E(O[0])}")</code> membuat <b>objek</b> pertama dari cetak biru itu.`,it:[lantai(8,5,-.8),...cb,obj(0,C[0])]},
   {cap:O.length>1?`${O.length} objek dibuat dari cetak biru yang sama, masing-masing menyimpan <b>datanya sendiri</b>. Mengubah ${E(O[1])} tidak mengubah ${E(O[0])}.`:'Tambahkan nama lain di panel Eksperimen untuk membuat objek kedua dari cetak biru yang sama.',it:[lantai(8,5,-.8),...cb,...O.map((_,i)=>obj(i,C[i]))]},
   {cap:'<b>Pewarisan</b>: class Kucing dibangun di atas class Hewan, sehingga semua objek ikut memiliki method Hewan seperti <code>makan()</code>.',it:[lantai(8,5,-1.8),B('hw',0,-1.3,0,{w:Math.max(5,O.length*1.8),h:.15,d:3,c:'mute'}),G('hwt',-3.4,-1.3,0,'class Hewan { makan() }'),...cb,...O.map((_,i)=>obj(i,C[i]))]}]}};

/* ---------- fungsi ---------- */
S.func={t:'Fungsi sebagai mesin: masukan diproses menjadi keluaran',
 p:[{k:'p',l:'Panjang (p)',t:'n',min:-99,max:999,v:4},{k:'l',l:'Lebar (l)',t:'n',min:-99,max:999,v:3},{k:'op',l:'Isi fungsi',t:'o',o:[['*','return p * l (luas)'],['+','return 2 * (p + l) (keliling)']],v:'*'}],
 steps:P=>{const kel=P.op==='+',nm=kel?'keliling':'luas',h=kel?2*(P.p+P.l):P.p*P.l,rumus=kel?`2 * (${P.p} + ${P.l})`:`${P.p} * ${P.l}`;
  const mesin=[lantai(9,3),B('mesin',0,.2,0,{w:2.4,h:1.6,d:1.6,c:'glass',t:`${nm}(p, l)`,tt:kel?'return 2*(p+l)':'return p * l'})];
  const q=(id,x,y,v,s=.7,c='warn')=>B(id,x,y,0,{w:s,h:s,d:s,t:String(v),c});
  return [
   {cap:'Fungsi adalah mesin bernama. Ia menerima <b>parameter</b>, menjalankan badannya, lalu <b>mengembalikan</b> hasil.',it:[...mesin,q('p',-3.8,0,P.p),q('l',-2.8,0,P.l)]},
   {cap:`Pemanggilan <code>${nm}(${P.p}, ${P.l})</code> memasukkan ${P.p} ke p dan ${P.l} ke l.`,it:[...mesin,q('p',-.55,.2,P.p,.5),q('l',.55,.2,P.l,.5)]},
   {cap:`Mesin menghitung <code>${rumus}</code> dan mengembalikan <b>${h}</b>. Nilai ini bisa disimpan: <code>hasil = ${nm}(${P.p}, ${P.l})</code>.`,it:[...mesin,q('h',3.3,0,h,.95,'ok')]},
   {cap:`Mesin yang sama bisa dipakai ulang dengan masukan lain, atau isinya diganti (lihat pilihan "Isi fungsi"). Tulis sekali, pakai berkali-kali.`,it:[...mesin,q('h',3.3,0,h,.95,'ok'),q('p',-3.8,0,P.p,.7,'mute'),q('l',-2.8,0,P.l,.7,'mute')]}]}};

/* ---------- box model CSS ---------- */
S.box={t:'Box model: empat lapisan setiap elemen',
 p:[{k:'w',l:'width (px)',t:'n',min:20,max:400,v:200},{k:'pd',l:'padding (px)',t:'n',min:0,max:80,v:20},{k:'bd',l:'border (px)',t:'n',min:0,max:30,v:5},{k:'mg',l:'margin (px)',t:'n',min:0,max:80,v:16},
   {k:'bs',l:'box-sizing',t:'o',o:[['content-box','content-box'],['border-box','border-box']],v:'content-box'}],
 steps:P=>{const bb=P.bs==='border-box',konten=bb?Math.max(0,P.w-2*P.pd-2*P.bd):P.w,lebar=konten+2*P.pd+2*P.bd,total=lebar+2*P.mg;
  const sc=5.4/Math.max(total,1),hc=.55;/* tinggi konten tetap 60px agar fokus pada lebar */
  const ch=60,dims=[['margin',total,ch+2*(P.pd+P.bd+P.mg),'mg'],['border',lebar,ch+2*(P.pd+P.bd),'bd'],['padding',konten+2*P.pd,ch+2*P.pd,'pd'],['konten',konten,ch,'ct']];
  const L=(gap,hi)=>dims.map(([n,w,h,c],i)=>B('L'+i,0,0,i*gap,{w:Math.max(.05,w*sc),h:Math.max(.05,h*sc*hc*1.6),d:.06,c:hi===undefined||hi===i?c:'mute',t:n,flat:1}));
  return [
   {cap:'Setiap elemen HTML adalah kotak. Dari depan terlihat datar, padahal tersusun dari <b>empat lapisan</b>.',it:L(.02)},
   {cap:'Kita pisahkan lapisannya. Paling dalam <b>konten</b>, dibungkus <b>padding</b>, lalu <b>border</b>, lalu <b>margin</b>.',it:L(1)},
   {cap:`<b>padding ${P.pd}px</b> adalah ruang di dalam kotak, di kiri dan kanan konten. Warna latar ikut mengisi padding.`,it:L(1,2)},
   {cap:`<b>border ${P.bd}px</b> adalah garis tepi kotak. ${bb?'Dengan border-box, border mengambil ruang dari dalam width.':'Ketebalannya menambah lebar kotak.'}`,it:L(1,1)},
   {cap:`<b>margin ${P.mg}px</b> adalah jarak di luar kotak ke elemen lain, selalu transparan dan tidak ikut dihitung dalam lebar kotak.`,it:L(1,0)},
   {cap:bb?`<code>box-sizing: border-box</code>: lebar kotak tetap <b>${lebar}px</b> sesuai width, kontennya menyusut menjadi ${P.w} − 2×${P.pd} − 2×${P.bd} = <b>${konten}px</b>.${P.w<2*P.pd+2*P.bd?' Padding dan border lebih besar dari width, jadi konten tidak punya ruang!':''}`
     :`<code>box-sizing: content-box</code>: width ${P.w}px hanya untuk konten. Lebar kotak sebenarnya ${P.w} + 2×${P.pd} + 2×${P.bd} = <b>${lebar}px</b>, plus margin menjadi ${total}px ruang. Coba ganti ke border-box.`,
    it:[...L(.02),G('wd',0,(ch+2*(P.pd+P.bd+P.mg))*sc*hc*.8+.6,0,`lebar kotak = ${lebar}px · konten = ${konten}px`,'warn')]}]}};

/* ---------- z-index ---------- */
S.zindex={t:'z-index: urutan lapisan ke arah layar',
 p:[{k:'a',l:'z-index kartu A',t:'n',min:-10,max:99,v:1},{k:'b',l:'z-index kartu B',t:'n',min:-10,max:99,v:2},{k:'c',l:'z-index kartu C',t:'n',min:-10,max:99,v:3}],
 steps:P=>{const cards=[['A',P.a,'acc',-.8,.5],['B',P.b,'ok',0,0],['C',P.c,'warn',.8,-.5]];
  const urut=cards.map((c,i)=>({c,i})).sort((x,y)=>x.c[1]-y.c[1]||x.i-y.i);const rank={};urut.forEach((o,r)=>rank[o.c[0]]=r);
  const k=(z)=>cards.map(([id,zi,c,x,y],i)=>B(id,x,y,z?rank[id]*.9:i*.9,{w:2.6,h:1.8,d:.06,c,t:`${id} z-index ${zi}`,flat:1}));
  const atas=urut[2].c[0],seri=new Set([P.a,P.b,P.c]).size<3;
  return [
   {cap:'Tiga kartu bertumpuk mengikuti urutan di HTML: A, lalu B, lalu C. Tanpa z-index, yang ditulis belakangan tampil di atas.',it:k(false)},
   {cap:`Sekarang z-index dipakai: urutan dari belakang ke depan menjadi <b>${urut.map(o=>o.c[0]).join(' → ')}</b>. Kartu <b>${atas}</b> paling dekat ke pengguna.${seri?' Ada nilai yang sama: untuk yang seri, urutan di HTML yang menentukan.':''}`,it:k(true)},
   {cap:'z-index hanya bekerja pada elemen dengan <code>position</code> selain static (atau anak flex/grid), dan dibandingkan di dalam <b>stacking context</b> yang sama. Nilai negatif menaruh elemen di belakang.',it:[...k(true),G('n',0,2,0,'position: relative','idx')]}]}};

/* ---------- SQL JOIN ---------- */
S.join={t:'JOIN: menggabungkan dua tabel lewat kolom yang sama',
 p:[{k:'j',l:'Jenis JOIN',t:'o',o:[['INNER','INNER JOIN'],['LEFT','LEFT JOIN']],v:'INNER'},{k:'ids',l:'pelanggan_id tiap pesanan',t:'s',v:'1, 1, 3'}],
 steps:P=>{const PL=[[1,'Ani'],[2,'Budi'],[3,'Citra']],MENU=['Kopi','Teh','Roti','Kue','Susu'];let ids=angka(P.ids,5);if(!ids.length)ids=[1];
  const O=ids.map((id,i)=>[id,MENU[i]]),left=P.j==='LEFT';
  const tab=(hi)=>[lantai(10,6,-.6-Math.max(3,O.length)),G('tp',-3,2,0,'pelanggan','idx'),G('to',3,2,0,'pesanan','idx'),
    ...PL.map(([id,n],i)=>B('p'+i,-3,1-i,0,{w:2.6,h:.7,d:.8,t:id+' · '+n,c:hi&&hi.p.includes(i)?'warn':'acc'})),
    ...O.map(([id,n],i)=>B('o'+i,3,1-i,0,{w:2.6,h:.7,d:.8,t:'pel '+id+' · '+n,c:hi&&hi.o.includes(i)?'warn':'ok'}))];
  const pairs=[];PL.forEach(([id],a)=>O.forEach(([oid],b)=>{if(oid===id)pairs.push([a,b])}));
  const hasil=[];PL.forEach(([id,n],a)=>{const m=O.filter(o=>o[0]===id);if(m.length)m.forEach(o=>hasil.push([n,o[1],0]));else if(left)hasil.push([n,'NULL',1])});
  const yatim=O.filter(o=>!PL.some(p=>p[0]===o[0]));
  return [
   {cap:'Dua tabel terpisah: <b>pelanggan</b> dan <b>pesanan</b>. Kolom <code>pelanggan_id</code> di pesanan menunjuk ke id pelanggan.',it:tab()},
   {cap:`<code>${P.j} JOIN ... ON pesanan.pelanggan_id = pelanggan.id</code> mencari pasangan baris yang nilainya sama. Ditemukan <b>${pairs.length} pasangan</b>.${yatim.length?` Pesanan dengan id ${yatim.map(o=>o[0]).join(', ')} tidak punya pelanggan, jadi tidak ikut.`:''}`,
    it:[...tab({p:[...new Set(pairs.map(x=>x[0]))],o:pairs.map(x=>x[1])}),...pairs.map(([a,b])=>R('r'+a+'_'+b,[-1.7,1-a,0],[1.7,1-b,0],'warn'))]},
   {cap:`Hasil ${P.j} JOIN: <b>${hasil.length} baris</b>. ${left?'LEFT JOIN mempertahankan <b>semua pelanggan</b>; yang tidak punya pesanan diisi NULL.':'INNER JOIN hanya menyimpan baris yang punya pasangan; pelanggan tanpa pesanan hilang.'} Coba ganti jenis JOIN atau isi pelanggan_id.`,
    it:[lantai(10,6,-.6-Math.max(3,hasil.length)),G('th',0,2,0,'hasil '+P.j+' JOIN','idx'),...(hasil.length?hasil.map(([a,b,nul],i)=>B('h'+i,0,1-i,0,{w:4,h:.7,d:.8,t:a+' · '+b,c:nul?'mute':'warn'})):[G('kos',0,0,0,'(kosong)','bad')])]}]}};

/* ---------- git ---------- */
S.git={t:'Git: commit sebagai titik, branch sebagai jalur',
 p:[{k:'f',l:'Commit di branch fitur',t:'n',min:1,max:4,v:2},{k:'m',l:'Commit baru di main',t:'n',min:0,max:3,v:0}],
 steps:P=>{const c=(id,x,y,col='acc')=>B(id,x,y,0,{w:.75,h:.75,d:.75,c:col,t:id,ball:1}),line=(a,b,col)=>R('l'+a.join('_')+'-'+b.join('_'),a,b,col);
  const sp=1.25,x0=-4,base=[c('m1',x0,0),c('m2',x0+sp,0),c('m3',x0+2*sp,0),line([x0,0],[x0+2*sp,0],'mute')],bx=x0+2*sp;
  const fit=[...Array(P.f)].map((_,i)=>c('f'+(i+1),bx+(i+1)*sp,1.6,'ok')),fl=[line([bx,0],[bx+sp,1.6],'ok'),...(P.f>1?[line([bx+sp,1.6],[bx+P.f*sp,1.6],'ok')]:[])];
  const mm=[...Array(P.m)].map((_,i)=>c('m'+(4+i),bx+(i+1)*sp,0)),ml=P.m?[line([bx,0],[bx+P.m*sp,0],'mute')]:[];
  const lantaiG=lantai(Math.max(10,(3+P.f+1)*sp+2),4,-1.2),lab=[G('bm',x0-1.4,0,0,'main','idx'),G('bf',bx+P.f*sp+.9,1.6,0,'fitur','ok')];
  const ff=P.m===0,mx=bx+(Math.max(P.f,P.m)+1)*sp;
  return [
   {cap:'Setiap <b>commit</b> adalah titik simpan seluruh proyek. Commit tersusun berurutan di branch <b>main</b>.',it:[lantaiG,...base,G('bm',x0-1.4,0,0,'main','idx')]},
   {cap:`<code>git switch -c fitur</code> membuat jalur baru dari commit terakhir, lalu ${P.f} commit dibuat di sana.${P.m?` Sementara itu main juga maju ${P.m} commit.`:' Main tidak berubah.'}`,it:[lantaiG,...base,...fit,...fl,...mm,...ml,...lab]},
   ff?{cap:'<code>git merge fitur</code>: karena main tidak punya commit baru, Git cukup <b>menggeser label main</b> ke ujung fitur. Ini disebut <b>fast-forward</b>, tanpa commit gabungan.',it:[lantaiG,...base,...fit,...fl,G('bm',bx+P.f*sp,2.6,0,'main = fitur','warn')]}
     :{cap:`<code>git merge fitur</code>: kedua jalur sama-sama maju, jadi Git membuat commit gabungan <b>M</b> yang berisi perubahan keduanya. Jika file yang sama diubah di kedua jalur, bisa terjadi <b>konflik</b>.`,it:[lantaiG,...base,...fit,...fl,...mm,...ml,line([bx+P.m*sp,0],[mx,0],'mute'),line([bx+P.f*sp,1.6],[mx,0],'ok'),c('M',mx,0,'warn'),...lab]}]}};

/* ---------- pencocokan pelajaran -> adegan ---------- */
const RULES=[
 /* judul yang mirip tetapi maknanya lain: jangan dipasangi adegan */
 [/decision tree|confusion matrix|feature engineering|random forest|t-sne/i,null,1],
 [/^peta besar: perjalanan satu request/i,'http',1],[/^merancang database postgresql/i,'fk',1],[/^transaksi: pesanan yang mengurangi stok/i,'tx',1],
 [/k-means|clustering/i,'kmeans',1],[/gradient descent|turunan dan|linear regression dari nol/i,'gd',1],[/train\/test split|validasi silang|cross.validation/i,'split',1],
 /* materi data, web, dan algoritma: judulnya spesifik, jadi berlaku di jalur mana pun (atau hanya jalur yang disebut) */
 [/^(select & from|where: menyaring baris|order by, limit & distinct|urutan eksekusi query|basis data relasional: tabel, baris, kolom|sintaks & kata kunci sql)$|memilih & menyaring: loc|katalog toko nusantara/i,'query',1],[/^operator$/i,'query',1,['sql']],
 [/fungsi agregat|^group ?by$|groupby|^having$|pivot_table|ringkasan stok/i,'group',1],[/^index:|jenis indeks|explain analyze|optimasi query|pg_stat_statements/i,'index',1],
 [/primary key|unique, not null|^create table$|tipe data dan constraint|database, schema, dan tabel|^alter, drop|merancang tabel dan relasi|tabel fakta & dimensi|laporan pesanan pelanggan/i,'fk',1],
 [/^acid|transaksi dan tingkat isolasi/i,'tx',1],[/mvcc|vacuum/i,'mvcc',1],[/replikasi|backup logis|dasar sistem terdistribusi|nosql, cap/i,'repl',1],
 [/window function|lead, lag|running total|peringkat & tren/i,'window',1],
 [/cara web bekerja|\bhttp|cors & csp|pengujian api rest|mengambil data: fetch|fetch di komponen|api dengan django rest|membuat rest api|^view dan url$|mengambil data api|route handlers|api & web scraping/i,'http',1],
 [/^flexbox$|^grid$|flexbox dan grid|sistem grid 12|display & alur normal|^row, column|^column, row|auto layout|section fitur dengan grid/i,'flex',1],
 [/komponen & jsx|^props$|state dengan usestate|useeffect|useref|usereducer|custom hook|input terkendali|memecah komponen|statelesswidget dan statefulwidget|state dengan remember|^props, emit|^ref, reactive|server component vs client/i,'react',1],
 [/hash table|hashing & collision|pola dict dan set|dictionary lanjutan & operasi set|^map: menghitung kemunculan|^set: himpunan tanpa duplikat/i,'hash',1],
 [/binary search(?! tree)|big-o|kompleksitas waktu/i,'bsearch',1],[/(?<!open )\bgraph\b|\bbfs\b|\bdfs\b|dijkstra|topological/i,'graph',1],
 [/\betl\b|pipeline|airflow|batch, streaming|kafka|siklus hidup data|lineage|warehouse, lake/i,'etl',1],[/sorting dasar|bubble sort|insertion sort/i,'sort',1],
 [/box model/i,'box',1],[/z-index|stacking context/i,'zindex',1],[/\bjoin\b/i,'join',1],[/\bbranch|\bmerge\b|\bcommit\b/i,'git',1],
 [/rekursi|recursion|call stack/i,'rekursi'],[/\bqueue|antrean|antrian|\bdeque/i,'queue'],[/(?<!tech |full ?)\bstack\b|tumpukan/i,'stack'],[/\bdom\b/i,'dom',1],
 [/\btree\b|pohon|\bbst\b|\bheap\b/i,'tree'],[/\b2d\b|dua dimensi|matriks|matrix|multidimensi/i,'matrix'],[/\barray|larik|\blist\b|arraylist|koleksi|collection/i,'array'],
 [/random number|bilangan acak|angka acak/i,'acak'],[/boolean logic|logika boolean|ekspresi boolean|operator logika/i,'bool'],[/perulangan|\bloop|\bfor\b|while|iterasi/i,'loop'],[/percabangan|\bif\b|kondisi|\bwhen\b|switch|keputusan/i,'if'],
 [/\bclass|kelas|\bobjek|\bobject|\boop\b|pewarisan|inheritance/i,'oop'],[/fungsi|function|\bmethod|metode|prosedur/i,'func'],[/variabel|variable|tipe data|val dan var/i,'var']];
const KODE=new Set(['java','python','js','jsx','ts','tsx','dart','kotlin','tx']),LOGIKA=/^(pseudo|flowg|logika|dsa|algo)$/;
window.v3dOf=function(t,title){if(!t||!title)return null;
  const kode=KODE.has(t.lang)||LOGIKA.test(t.k);
  for(const [rx,s,any,langs] of RULES)if(rx.test(title)&&(langs?langs.includes(t.lang)||langs.includes(t.k):any||kode))return s;return null};
window.V3DT=k=>S[k]&&S[k].t;
/* jenis loop awal ditebak dari judul pelajaran, agar adegan langsung menampilkan jenis yang dibahas */
window.v3dInit=function(k,title){const t=String(title||'');
  if(k==='sort')return /insertion/i.test(t)&&!/bubble/i.test(t)?{algo:'insert'}:null;
  if(k==='graph')return /\bdfs\b|topological/i.test(t)&&!/\bbfs\b/i.test(t)?{mode:'dfs'}:null;
  if(k==='flex')return /^grid$|grid 12/i.test(t)?{n:6}:null;
  if(k==='window')return /lead, lag|running total|tren/i.test(t)?{fn:'run'}:null;
  if(k==='group')return /having/i.test(t)?{hv:40}:null;
  if(k!=='loop')return null;
  if(/do-while|kapan for|repeat-until|simbol do\b|semua jenis/i.test(t))return {jenis:'banding'};
  if(/bersarang|nested|loop di dalam loop/i.test(t))return {jenis:'nested'};
  if(/\bbreak\b|penghentian/i.test(t))return {jenis:'break'};
  if(/continue/i.test(t))return {jenis:'continue'};
  if(/for\.\.\.of|for-each|foreach|enhanced/i.test(t))return {jenis:'each'};
  if(/while|tak pasti/i.test(t))return {jenis:'while'};
  return null};

/* ---------- mesin panggung ---------- */
const FACES=[['f',0,0],['b',0,180],['r',0,90],['l',0,-90],['t',90,0],['u',-90,0]];
function blockHTML(o,U){if(o.s&&SHAPE[o.s])return SHAPE[o.s](o,U);const w=o.w*U,h=o.h*U,d=o.d*U,ln=o.t?`<b>${o.t}</b>`:'',tt=o.tt?`<i>${o.tt}</i>`:'';
  return FACES.map(([k,rx,ry])=>{const fw=k==='r'||k==='l'?d:w,fh=k==='t'||k==='u'?d:h,tz=k==='r'||k==='l'?w/2:k==='t'||k==='u'?h/2:d/2;
    if(o.flat&&k!=='f'&&k!=='b')return '';
    return `<div class="f3 f-${k}" style="width:${fw}px;height:${fh}px;transform:translate(-50%,-50%) rotateX(${rx}deg) rotateY(${ry}deg) translateZ(${tz}px)">${k==='f'?ln+(o.flat?'':''):k==='t'?tt:''}</div>`}).join('')}
/* ---------- bentuk khusus: benda dirakit dari beberapa balok kecil agar mirip aslinya ----------
   o.s = 'orang' | 'gedung' | 'gudang' | 'server' | 'db' | 'layar' | 'dok' | 'buku' | 'piring'.
   Ukuran w,h,d tetap menjadi kotak pembatasnya; teks ditaruh di papan nama atau layar. */
function cub(x,y,z,w,h,d,U,cls='',txt={},rx=0){const fc=typeof cls==='function'?cls:()=>cls;
  return `<div class="pt" style="transform:translate3d(${x*U}px,${-y*U}px,${z*U}px)${rx?` rotateX(${rx}deg)`:''}">`+FACES.map(([k,a,b])=>{
    const fw=(k==='r'||k==='l'?d:w)*U,fh=(k==='t'||k==='u'?d:h)*U,tz=(k==='r'||k==='l'?w/2:k==='t'||k==='u'?h/2:d/2)*U;
    return `<div class="f3 f-${k} ${fc(k)}" style="width:${fw}px;height:${fh}px;transform:translate(-50%,-50%) rotateX(${a}deg) rotateY(${b}deg) translateZ(${tz}px)">${txt[k]||''}</div>`}).join('')+'</div>'}
function cyl(x,y,z,r,h,U,cls='',n=14){const sw=2*r*Math.tan(Math.PI/n)*U+1;let o=`<div class="pt" style="transform:translate3d(${x*U}px,${-y*U}px,${z*U}px)">`;
  for(let i=0;i<n;i++)o+=`<div class="f3 cyl ${i%2?'f-r':'f-f'} ${cls}" style="width:${sw}px;height:${h*U}px;transform:translate(-50%,-50%) rotateY(${i*360/n}deg) translateZ(${r*U*Math.cos(Math.PI/n)}px)"></div>`;
  for(const [k,a] of [['t',90],['u',-90]])o+=`<div class="f3 cap f-${k} ${cls}" style="width:${2*r*U}px;height:${2*r*U}px;transform:translate(-50%,-50%) rotateX(${a}deg) translateZ(${h/2*U}px)"></div>`;
  return o+'</div>'}
const papan=(o,U,y,z,mw)=>o.t?cub(0,y,z,Math.min(mw,Math.max(.7,String(o.t).replace(/<[^>]*>/g,'').length*.14)),.3,.04,U,k=>k==='f'?'sign':'sign dark',{f:`<b>${o.t}</b>`}):'';
const TAGSHAPE={orang:1,gedung:1,gudang:1,server:1,db:1,piring:1};
const SHAPE={
 orang(o,U){const {w,h,d}=o,hs=Math.min(w*.46,h*.26),lg=h*.36,ts=h*.33,y0=-h/2;
  return cub(-w*.13,y0+lg/2,0,w*.2,lg,d*.45,U,'dark')+cub(w*.13,y0+lg/2,0,w*.2,lg,d*.45,U,'dark')
   +cub(0,y0+lg+ts/2,0,w*.6,ts,d*.55,U)+cub(-w*.4,y0+lg+ts*.55,0,w*.16,ts*.9,d*.4,U)+cub(w*.4,y0+lg+ts*.55,0,w*.16,ts*.9,d*.4,U)
   +cub(0,y0+lg+ts+hs/2+h*.02,0,hs,hs,hs,U,k=>k==='t'?'hair':k==='b'?'hair':'sk')},
 gedung(o,U){const {w,h,d}=o,rf=Math.min(.14,h*.06);
  return cub(0,-rf/2,0,w,h-rf,d,U,k=>k==='t'||k==='u'?'':'win')+cub(0,h/2-rf/2,0,w*1.08,rf,d*1.08,U,'dark')
   +cub(0,-h/2+Math.min(.5,h*.18)/2,d/2+.01,Math.min(.4,w*.3),Math.min(.5,h*.18),.02,U,'door')},
 gudang(o,U){const {w,h,d}=o,rf=Math.min(.16,h*.08);
  return cub(0,-rf/2,0,w,h-rf,d,U,k=>k==='f'?'roll':'')+cub(0,h/2-rf/2,0,w*1.06,rf,d*1.08,U,'dark')},
 server(o,U){const {w,h,d}=o,n=h>1.2?3:2,g=.06,uh=(h-g*(n-1))/n;let s='';
  for(let i=0;i<n;i++)s+=cub(0,-h/2+uh/2+i*(uh+g),0,w,uh,d,U,k=>k==='f'?'led':k==='t'||k==='u'?'':'dark');
  return s},
 db(o,U){const {w,h,d}=o,r=Math.min(w,d)/2,n=3,g=.05,uh=(h-g*(n-1))/n;let s='';
  for(let i=0;i<n;i++)s+=cyl(0,-h/2+uh/2+i*(uh+g),0,r,uh,U);
  return s},
 layar(o,U){const {w,h,d}=o,sh=h*.72,ft=h*.06,nk=h-sh-ft;
  return cub(0,h/2-sh/2,0,w,sh,d*.22,U,k=>k==='f'?'scr':'dark',{f:o.t?`<b>${o.t}</b>`:''})+cub(0,-h/2+ft+nk/2,0,w*.12,nk,d*.12,U,'dark')+cub(0,-h/2+ft/2,0,w*.5,ft,d*.6,U,'dark')},
 dok(o,U){const {w,h,d}=o;return cub(0,0,0,w,h,Math.min(d,.18),U,k=>k==='f'||k==='b'?'doc':'doc',{f:o.t?`<b>${o.t}</b>`:''})},
 buku(o,U){const {w,h,d}=o;return cub(0,0,0,w,h,d,U,k=>k==='r'||k==='t'||k==='u'?'doc':'',{f:o.t?`<b>${o.t}</b>`:''})},
 piring(o,U){const {w,h,d}=o,r=Math.min(w,d)/2;return cyl(0,0,0,r,h,U,'',18)}};
function place(o,U){return `translate3d(${o.x*U}px,${-o.y*U}px,${o.z*U}px) rotateY(${o.ry||0}deg) rotateZ(${-(o.rz||0)}deg)`}

/* label pendek tiap langkah untuk garis waktu (dipakai bila jumlah langkah cocok) */
const LB={var:['Rak memori','Isi umur','Isi nama','Ambil nilai','Ganti isi'],array:['Deretan kotak','Indeks 0','Akses langsung','Tambah','Panjang'],
 matrix:['Ukuran','Satu baris','Satu kolom','Satu sel'],if:['Persimpangan','Cek kondisi','Pilih cabang','Uji batas'],bool:['Masukan','Cek p dulu','Hasil','Tabel kebenaran'],
 acak:['Desimal 0..1','Ke rentang','Banyak lemparan','Seed'],stack:['Tumpukan','Push','Peek','Pop','Sisa'],queue:['Antrean','Enqueue','Dequeue','Maju'],
 rekursi:['Panggil','Tumpuk','Kasus dasar','Kembali','Kembali lagi','Hasil'],dom:['Akar','Anak','Telusuri'],oop:['Cetak biru','Objek pertama','Banyak objek','Pewarisan'],
 func:['Mesin','Masukan','Kembalikan','Pakai ulang'],box:['Kotak','Pisah lapisan','Padding','Border','Margin','Lebar total'],zindex:['Urutan HTML','Pakai z-index','Konteks tumpukan'],
 join:['Dua tabel','Cocokkan','Hasil'],git:['Commit','Branch','Merge'],
 query:['FROM','WHERE','SELECT','ORDER BY','LIMIT','Urutan eksekusi'],group:['Data','GROUP BY','Agregat','HAVING','Intinya'],index:['Tabel','Full scan','B-tree','Telusuri','Langsung ke baris','Biaya'],
 fk:['Dua tabel','Primary key','Foreign key','INSERT','Constraint'],window:['Data','PARTITION BY','ORDER BY','Fungsi','Beda GROUP BY'],mvcc:['INSERT','Transaksi baca','UPDATE','Dead tuple','VACUUM'],
 http:['URL','DNS','Request','Server','Response','Tampil'],flex:['Alur normal','display:flex','justify-content','align-items','flex-grow','Grid 2D'],react:['Komponen','Props','State','Render ulang','Ubah DOM'],
 hash:['Laci','Fungsi hash','Isi semua','Tabrakan','Cari','Rata-rata O(1)'],etl:['Sumber','Extract','Transform','Load','Analisis','Batch/stream']};
window.V3D=function(host,key,init,opt){const sc=S[key];if(!sc)return;const mini=!!(opt&&opt.mini);
  const rm=RMq(),RX0=-30,RY0=-38;let i=0,rx=RX0,ry=RY0,auto=null,U=40;const els=new Map();
  /* parameter eksperimen: nilai awal dari definisi adegan, langkah dihitung ulang setiap kali diubah */
  const PD=(sc.p||[]).map(d=>init&&init[d.k]!=null?{...d,v:init[d.k]}:d),P={};PD.forEach(d=>P[d.k]=d.v);
  const hitung=()=>{try{return typeof sc.steps==='function'?sc.steps(P):sc.steps}catch(e){return [{cap:'Nilai ini belum bisa digambar. Coba angka lain.',it:[lantai()]}]}};
  let steps=hitung();
  const label=(k)=>{const s=steps[k],L=LB[key];if(s&&s.lb)return s.lb;if(L&&L.length===steps.length)return L[k];
    if(k===0)return 'Mulai';if(k===steps.length-1)return 'Intinya';const c=String(s.cap).replace(/<[^>]+>/g,''),m=c.match(/^(Putaran \d+|Bandingkan)/);return m?m[0]:/ketemu/i.test(c)?'Ketemu':'Langkah '+(k+1)};
  const tagOf=k=>k===0?['Mulai','t-a']:k===steps.length-1?['Intinya','t-c']:['Konsep','t-b'];
  const fld=d=>{const id=`v3-${key}-${d.k}-${Math.random().toString(36).slice(2,7)}`;
    const inp=d.t==='o'?`<select id="${id}" data-k="${d.k}">${d.o.map(([v,l])=>`<option value="${v}"${v===d.v?' selected':''}>${l}</option>`).join('')}</select>`
      :d.t==='n'?`<input id="${id}" data-k="${d.k}" type="number" inputmode="numeric" step="1" min="${d.min}" max="${d.max}" value="${d.v}">`
      :`<input id="${id}" data-k="${d.k}" type="text" value="${d.v}" maxlength="40" autocomplete="off" spellcheck="false">`;
    return `<label class="s3fld" for="${id}"><span>${d.l}${d.t==='n'?` <small>${d.min}…${d.max}</small>`:''}</span>${inp}</label>`};
  const panel=PD.length?`<details class="s3exp" open><summary><span aria-hidden="true">🧪</span> Eksperimen: ubah angkanya</summary>
    <div class="s3form">${PD.map(fld).join('')}<button class="tlink" type="button" data-a="reset">Kembalikan nilai awal</button></div>
    <p class="s3tip">Perubahan langsung diterapkan pada langkah yang sedang dibuka.</p></details>`:'';
  host.innerHTML=`<div class="stg${mini?' is-mini':''}">
   <div class="stg-main">
    ${PD.length?'<div class="stg-hud" aria-label="Nilai yang sedang dipakai"></div>':''}
    <div class="s3" tabindex="0" role="img" aria-label="Adegan 3D: ${sc.t}. Seret atau tekan tombol panah untuk memutar."><div class="s3cam"><div class="w3"></div></div><div class="s3tags"></div>
     <span class="s3hint" aria-hidden="true">⟲ seret untuk memutar</span><button class="s3view" type="button" data-a="view" title="Kembali ke sudut awal">Sudut awal</button></div>
    <div class="stg-prog" aria-hidden="true"><i></i></div>
    <ol class="stg-tl" aria-label="Langkah"></ol>
   </div>
   <aside class="stg-rail">
    <div class="rail-top"><span class="rail-n"></span><span class="rail-tag"></span></div>
    <h4 class="rail-h"></h4>
    <p class="s3cap" aria-live="polite"></p>
    <div class="rail-nav"><button class="btn" type="button" data-a="prev">← Kembali</button><button class="btn primary" type="button" data-a="next"></button></div>
    <div class="rail-play"><button class="rp" type="button" data-a="replay">⟲ Ulangi <kbd>R</kbd></button><button class="rp" type="button" data-a="play" aria-pressed="false"></button><span class="rail-kb"><kbd>←</kbd><kbd>→</kbd> langkah</span></div>
    ${panel}
   </aside></div>`;
  const st=host.querySelector('.s3'),w=host.querySelector('.w3'),cap=host.querySelector('.s3cap'),tg=host.querySelector('.s3tags'),tl=host.querySelector('.stg-tl'),
    hud=host.querySelector('.stg-hud'),bar=host.querySelector('.stg-prog i'),bPlay=host.querySelector('[data-a=play]');
  /* label diproyeksikan ke 2D agar selalu terbaca dan tidak tertutup benda */
  const proj=(x,y,z)=>{const a=ry*Math.PI/180,b=rx*Math.PI/180,X=x*U,Y=-y*U,Z=z*U;
    const x1=X*Math.cos(a)+Z*Math.sin(a),z1=-X*Math.sin(a)+Z*Math.cos(a),y2=Y*Math.cos(b)-z1*Math.sin(b),z2=Y*Math.sin(b)+z1*Math.cos(b);
    const W=st.clientWidth,H=st.clientHeight,ox=W/2,oy=H*.4,cx=W/2,cy=H*.56,k=1100/(1100-z2);return [ox+(cx+x1-ox)*k,oy+(cy+y2-oy)*k]};
  const view=()=>{w.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg)`;
    const W=st.clientWidth;els.forEach(e=>{if(e._tag){const [l,t]=proj(...e._p),h=e.offsetWidth/2+4;e.style.left=Math.max(h,Math.min(W-h,l))+'px';e.style.top=t+'px'}})};
  const optLabel=d=>{const o=(d.o||[]).find(x=>String(x[0])===String(P[d.k]));return o?o[1]:P[d.k]};
  function hudDraw(){if(!hud)return;hud.innerHTML=PD.map(d=>`<span class="hud-c"><small>${d.l}</small><b>${E(String(d.t==='o'?optLabel(d):P[d.k]).slice(0,28))}</b></span>`).join('')}
  function tlDraw(){tl.innerHTML=steps.map((s,k)=>`<li><button type="button" data-go="${k}"${k===i?' aria-current="step"':''} class="${k<i?'done':k===i?'now':''}"><span class="tn">${k<i?'✓':k+1}</span><span class="tl-l">${label(k)}</span></button></li>`).join('')}
  function draw(again){if(i>steps.length-1)i=steps.length-1;const s=steps[i];U=Math.max(26,Math.min(60,st.clientWidth/11));const seen=new Set();
    if(again){els.forEach(e=>e.remove());els.clear()}
    let nf=0;
    /* label bentuk khusus jadi tag melayang di atasnya (piring: di sampingnya) agar tidak tertutup benda lain */
    const items=s.it.flatMap(o=>o&&o.s&&o.t&&TAGSHAPE[o.s]?[o,o.s==='piring'?G(o.id+'~t',o.x+o.w/2+.45,o.y,o.z,o.t,'lbl'):G(o.id+'~t',o.x,o.y+o.h/2+.38,o.z,o.t,'lbl')]:[o]);
    items.forEach(o=>{seen.add(o.id);let e=els.get(o.id);const fresh=!e,prevC=e&&e._c,prevT=e&&e._t;
      if(fresh){e=document.createElement('div');els.set(o.id,e);(o.tag?tg:w).appendChild(e)}
      if(o.tag){e.className=`t3 ${o.c?'c-'+o.c:''}`;e.innerHTML=o.t;e._tag=1;e._p=[o.x,o.y,o.z];
        if(!rm&&(fresh||prevT!==o.t)){e.classList.add('pop')}e._t=o.t}
      else{e.className=`b3 c-${o.c}${o.s?' s-'+o.s:''}${o.ball?' ball':''}${o.rod?' rod':''}${o.flat?' flat':''}`;e.innerHTML=blockHTML(o,U);e.style.transform=place(o,U);
        /* berubah warna atau isi: kilau sebentar agar mata tertuju ke sana */
        if(!fresh&&!rm&&(prevC!==o.c||prevT!==o.t)&&o.c!=='floor'){e.classList.add('pulse');setTimeout(()=>e.classList.remove('pulse'),950)}
        e._c=o.c;e._t=o.t}
      /* benda baru muncul bergiliran, bukan sekaligus */
      if(fresh&&!rm){const d=Math.min(nf++,12)*70;e.style.transitionDelay=d+'ms';e.classList.add('in');
        requestAnimationFrame(()=>requestAnimationFrame(()=>e.classList.remove('in')));setTimeout(()=>{e.style.transitionDelay=''},d+800)}});
    els.forEach((e,id)=>{if(seen.has(id))return;els.delete(id);if(rm)e.remove();else{e.classList.add('out');setTimeout(()=>e.remove(),450)}});
    /* teks di sisi benda dikecilkan bila tidak muat (layar sempit) */
    w.querySelectorAll('.f3>b,.f3>i').forEach(t=>{const f=t.parentNode,cw=f.clientWidth-4,ch=f.clientHeight-2,sw=t.scrollWidth,sh=t.offsetHeight;
      const k=Math.min(1,cw/sw,ch/sh);t.style.transform=k<1?`scale(${Math.max(.35,k)})`:''});
    view();const N=steps.length,[tt,tc]=tagOf(i);
    cap.innerHTML=s.cap;host.querySelector('.rail-h').textContent=label(i);host.querySelector('.rail-n').textContent=`Langkah ${i+1} / ${N}`;
    const tgEl=host.querySelector('.rail-tag');tgEl.textContent=tt;tgEl.className='rail-tag '+tc;
    bar.style.width=((i+1)/N*100)+'%';tlDraw();hudDraw();
    host.querySelector('[data-a=prev]').disabled=i===0;
    host.querySelector('[data-a=next]').innerHTML=i<N-1?`Lanjut: ${label(i+1)} →`:'↺ Mulai lagi dari awal'}
  const setPlay=on=>{bPlay.setAttribute('aria-pressed',on?'true':'false');bPlay.innerHTML=on?'❚❚ Jeda <kbd>Spasi</kbd>':'▶ Putar <kbd>Spasi</kbd>'};
  const stop=()=>{clearInterval(auto);auto=null;setPlay(false)};
  const go=d=>{stop();const j=i+d;if(j<0)return;if(j>steps.length-1){if(d>0&&i===steps.length-1){i=0;draw()}return}i=j;draw()};
  const toggle=()=>{if(auto)return stop();if(i===steps.length-1){i=0;draw()}setPlay(true);
    auto=setInterval(()=>{if(!host.isConnected)return stop();if(i>=steps.length-1){stop();if(mini&&opt.onEnd)opt.onEnd();return}i++;draw()},mini?3000:3400)};
  const replay=()=>{draw(true)};
  if(!mini&&typeof stepReg==='function')stepReg({host,go,toggle,replay});
  host.addEventListener('click',e=>{const g=e.target.closest('[data-go]');if(g){stop();i=+g.dataset.go;draw();return}
    const a=e.target.closest('[data-a]');if(!a)return;const k=a.dataset.a;
    if(k==='next')go(1);else if(k==='prev')go(-1);else if(k==='replay')replay();else if(k==='play')toggle();
    else if(k==='view'){rx=RX0;ry=RY0;view()}});
  let drag=null;
  st.addEventListener('pointerdown',e=>{if(e.target.closest('button'))return;drag={x:e.clientX,y:e.clientY,rx,ry};st.setPointerCapture(e.pointerId);st.classList.add('grab')});
  st.addEventListener('pointermove',e=>{if(!drag)return;ry=drag.ry+(e.clientX-drag.x)*.45;rx=Math.max(-80,Math.min(25,drag.rx-(e.clientY-drag.y)*.35));view()});
  const up=()=>{drag=null;st.classList.remove('grab')};st.addEventListener('pointerup',up);st.addEventListener('pointercancel',up);
  st.addEventListener('keydown',e=>{const m={ArrowLeft:[0,-10],ArrowRight:[0,10],ArrowUp:[-8,0],ArrowDown:[8,0]}[e.key];if(!m)return;e.preventDefault();
    rx=Math.max(-80,Math.min(25,rx+m[0]));ry+=m[1];view()});
  let rw;window.addEventListener('resize',()=>{clearTimeout(rw);rw=setTimeout(()=>{if(host.isConnected)draw(true)},200)});
  if(PD.length){let tm;const form=host.querySelector('.s3form');
    const baca=el=>{const d=PD.find(x=>x.k===el.dataset.k);if(!d)return;
      if(d.t==='n'){let v=Math.round(Number(el.value));if(!Number.isFinite(v)||el.value==='')return;v=Math.max(d.min,Math.min(d.max,v));P[d.k]=v}
      else P[d.k]=el.value};
    const terap=()=>{stop();steps=hitung();draw()};
    form.addEventListener('input',e=>{if(!e.target.dataset.k)return;baca(e.target);clearTimeout(tm);tm=setTimeout(terap,220)});
    form.addEventListener('change',e=>{const el=e.target,d=PD.find(x=>x.k===el.dataset.k);if(d&&d.t==='n'){el.value=P[d.k]}});
    form.querySelector('[data-a=reset]').addEventListener('click',()=>{PD.forEach(d=>{P[d.k]=d.v;const el=form.querySelector(`[data-k="${d.k}"]`);el.value=d.v});terap()});}
  setPlay(false);draw();if(mini)toggle();
};
})();

;window.VIZ2=VIZ2;window.VIZ2T=VIZ2T;
