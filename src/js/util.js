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

