// Merekam eksekusi program JavaScript/TypeScript baris per baris lewat Chrome DevTools Protocol
// (dipakai tools/gen/traces.py). Pemakaian: node trace_js.js <berkas.js|berkas.ts>
// Keluaran (stdout): JSON {steps, out, cut, err}. Setiap langkah: [baris, nama fungsi, variabel {nama: nilai}, panjang keluaran].
// TypeScript dijalankan dengan --experimental-strip-types: tipe diganti spasi, jadi nomor baris tetap sama.
const {spawn}=require('child_process'),path=require('path');
const MAX=200,file=path.resolve(process.argv[2]);
const args=['--inspect-brk=127.0.0.1:0'];if(file.endsWith('.ts'))args.push('--experimental-strip-types','--no-warnings');
const child=spawn(process.execPath,[...args,file],{stdio:['ignore','pipe','pipe']});
let out='',errText='',ws=null,id=0;const wait=new Map(),steps=[],SCRIPTS={};let cut=false,done=false;
child.stdout.on('data',d=>out+=d);
child.stderr.on('data',d=>{const s=String(d);errText+=s;const m=/ws:\/\/[^\s]+/.exec(s);if(m&&!ws)connect(m[0])});
const send=(method,params={})=>new Promise(res=>{const i=++id;wait.set(i,res);ws.send(JSON.stringify({id:i,method,params}))});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
function fmt(o){
  if(!o)return '?';
  if(o.type==='string')return JSON.stringify(o.value).slice(0,48);
  if(o.type==='number'||o.type==='boolean'||o.type==='bigint')return String(o.value??o.description);
  if(o.type==='undefined')return 'undefined';
  if(o.subtype==='null')return 'null';
  const p=o.preview;
  if(p){const v=x=>x.type==='string'?JSON.stringify(x.value):x.value;
    if(p.subtype==='array')return ('['+p.properties.map(v).join(', ')+(p.overflow?', …':'')+']').slice(0,48);
    if(p.subtype==='map'||p.subtype==='set')return o.description;
    if(o.className==='Object')return ('{'+p.properties.map(x=>x.name+': '+v(x)).join(', ')+(p.overflow?', …':'')+'}').slice(0,48);
    return (o.className+' {'+p.properties.map(x=>x.name+': '+v(x)).join(', ')+'}').slice(0,48)}
  return o.description||o.type;
}
const SKIP=new Set(['exports','require','module','__filename','__dirname','this']);
async function vars(frame){
  const got={};
  for(const sc of frame.scopeChain){
    if(sc.type==='global')continue;
    const r=await send('Runtime.getProperties',{objectId:sc.object.objectId,ownProperties:true,generatePreview:true});
    for(const p of r.result||[]){if(SKIP.has(p.name)||p.name in got||!p.value)continue;
      if(p.value.type==='function'||p.value.className==='Function')continue;
      if(p.value.type==='undefined'&&sc.type!=='local')continue; // let/const yang belum sampai deklarasinya
      got[p.name]=fmt(p.value)}}
  return got;
}
async function onPaused(m){
  const f=m.params.callFrames[0];
  const ours=(SCRIPTS[f.location.scriptId]||f.url||'').replace(/^file:\/\//,'')===file;
  if(!ours){await send(m.params.reason==='Break on start'?'Debugger.stepInto':'Debugger.stepOut');return}
  if(steps.length>=MAX){cut=true;finish();return}
  await sleep(4);
  steps.push([f.location.lineNumber+1,f.functionName||'<module>',await vars(f),out.length]);
  await send('Debugger.stepInto');
}
function connect(u){
  ws=new WebSocket(u);
  ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&wait.has(m.id)){wait.get(m.id)(m.result||{});wait.delete(m.id);return}
    if(m.method==='Debugger.scriptParsed')SCRIPTS[m.params.scriptId]=m.params.url;
    if(m.method==='Debugger.paused')onPaused(m).catch(()=>finish());
    if(m.method==='Runtime.executionContextDestroyed')setTimeout(finish,30)};
  ws.onopen=async()=>{await send('Runtime.enable');await send('Debugger.enable');
    await send('Debugger.setBlackboxPatterns',{patterns:['^node:','internal/']});
    await send('Runtime.runIfWaitingForDebugger')};
  ws.onerror=()=>{};
}
function finish(){if(done)return;done=true;try{child.kill()}catch(e){}
  const err=/Uncaught|Error:/.test(errText.replace(/Debugger (listening|attached)[^\n]*\n|For help, see[^\n]*\n|Waiting for the debugger[^\n]*\n/g,''))&&!cut?'error':null;
  steps.push([0,'<module>',steps.length?steps[steps.length-1][2]:{},out.length]);
  process.stdout.write(JSON.stringify({steps,out,cut,err}));process.exit(0)}
child.on('exit',()=>setTimeout(finish,30));
setTimeout(()=>{cut=true;finish()},20000);
