// Menjalankan data.js dan berkas kurikulum di Node, lalu memecah setiap pelajaran
// menjadi kerangka (judul, jenis, jumlah soal) dan isi. Dipakai build.py.
// Pemakaian: node evaltracks.js data.js track-a.js track-b.js ...  -> JSON di stdout
const fs=require('fs'),vm=require('vm');
const files=process.argv.slice(2);
const src=files.map(f=>fs.readFileSync(f,'utf8')).join('\n;\n');
const names=[...new Set([...src.matchAll(/^const ([A-Z][A-Z0-9_]*_MODULES)\s*=/gm)].map(m=>m[1]))];
const ctx=vm.runInNewContext(src+`\n;({CH,TOPICS,M:{${names.join(',')}}})`,{console});
const SKEL=['k','t','n','ref','mini','nodes'];
const out={};
for(const [name,mods] of Object.entries(ctx.M)){
  const bodies=[],skel=mods.map(m=>{const {lessons,...meta}=m;return {...meta,lessons:lessons.map(l=>{
    const s={},b={};for(const [k,v] of Object.entries(l))(SKEL.includes(k)?s:b)[k]=v;
    if(l.k==='lab'){s._t=ctx.CH[l.n-1].t;s.qn=ctx.CH[l.n-1].quiz.length}
    else if(l.k==='topic'){const [n,i]=l.ref.split('.').map(Number);s._t=ctx.TOPICS[n][i].t;s.qn=0}
    else s.qn=(l.q||[]).length;
    bodies.push(b);return s})}});
  const bad=[];(function walk(v,p){if(typeof v==='function'||v instanceof RegExp||v===undefined)bad.push(p);else if(v&&typeof v==='object')for(const k in v)walk(v[k],p+'.'+k)})(bodies,name);
  if(bad.length){console.error('nilai bukan JSON:',bad.slice(0,10));process.exit(1)}
  out[name]={skel,bodies};
}
// ringkasan bab dan topik Java/Python untuk halaman statis (SEO)
const strip=c=>String(c||'').replace(/«\w+\|([^»]*)»/g,'$1');
const book={CH:ctx.CH.map(c=>({t:c.t,body:c.body,points:c.points,java:strip(c.java),python:strip(c.python),out:c.out,quiz:c.quiz})),
  TOPICS:Object.fromEntries(Object.entries(ctx.TOPICS).map(([n,a])=>[n,a.map(tp=>({t:tp.t,tr:tp.tr,java:strip(tp.java),python:strip(tp.python)}))]))};
process.stdout.write(JSON.stringify({tracks:out,book}));
