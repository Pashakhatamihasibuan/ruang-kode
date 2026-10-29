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
  java:new Set('public private protected static void class int double boolean char long float byte short new return if else for while do break continue import extends implements interface abstract final this super null true false try catch finally throw throws switch case default var package'.split(' ')),
  python:new Set('def class return if elif else for while in not and or import from as None True False try except finally raise with lambda pass break continue is yield global nonlocal del'.split(' '))
};
const BUILT = {
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
function hl(code,lang){
  if(lang==='sql')return hlSql(code);
  if(lang==='text'||!KW[lang])return esc(code);
  const re = lang==='java'
    ? /(\/\/[^\n]*)|("(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|([\s\S])/g
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

/* player langkah demi langkah */
function player(host,frames,draw,opts={}){
  host.innerHTML=`<div class="stage"></div><p class="note" aria-live="polite"></p>
  <div class="ctrl"><button class="btn" data-a="reset">Ulang</button><button class="btn" data-a="prev">◀ Sebelumnya</button><button class="btn primary" data-a="next">Berikutnya ▶</button><button class="btn" data-a="play">Putar otomatis</button><span class="cnt"></span></div>`;
  const stage=$('.stage',host),note=$('.note',host),cnt=$('.cnt',host);
  const pb=$('[data-a=play]',host),nb=$('[data-a=next]',host),bb=$('[data-a=prev]',host);
  let i=0,t=null;
  const stop=()=>{if(t){clearInterval(t);t=null}pb.textContent='Putar otomatis'};
  function show(){draw(stage,frames[i],i);note.innerHTML=frames[i].note||'';cnt.textContent=`Langkah ${i+1} / ${frames.length}`;bb.disabled=i===0;nb.disabled=i===frames.length-1}
  $('.ctrl',host).addEventListener('click',e=>{
    const b=e.target.closest('button');if(!b)return;const a=b.dataset.a;
    if(a==='next'&&i<frames.length-1)i++;
    if(a==='prev'&&i>0)i--;
    if(a==='reset'){stop();i=0}
    if(a==='play'){
      if(t){stop();return}
      if(i===frames.length-1)i=0;
      pb.textContent='Jeda';
      t=setInterval(()=>{if(i<frames.length-1){i++;show()}else stop()},opts.speed||1100);TIMERS.push(t);
    }
    show();
  });
  show();
  return {set(f){stop();frames=f;i=0;show()}};
}
function cellsHTML(arr,cls=()=>'',ix=true){
  return `<div class="cells">${arr.map((v,i)=>`<div class="cell ${cls(i,v)}">${ix?`<span class="ix">${i}</span>`:''}${v===undefined||v===null?'':esc(v)}</div>`).join('')}</div>`;
}

