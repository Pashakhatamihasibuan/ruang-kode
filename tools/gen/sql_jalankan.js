// Menjalankan query di mesin SQL situs. Masukan JSON [{db,sql}] dari stdin, keluaran teks tabel.
const fs=require('fs'),vm=require('vm');const R=require('path').join(__dirname,'../../src/js/');
const ctx={console};vm.createContext(ctx);
vm.runInContext(['sqlengine.js','sqldata.js','sqldata-bi.js'].map(f=>fs.readFileSync(R+f,'utf8')).join('\n;\n')+';this.SQLE=SQLE;this.SEED=SEED;',ctx);
const {SQLE,SEED}=ctx;
function tabel(r){if(!r||!r.cols)return r&&(r.msg||r.message)?(r.msg||r.message):JSON.stringify(r);const rows=r.rows.map(x=>x.map(v=>v===null||v===undefined?'NULL':String(v)));const w=r.cols.map((c,i)=>Math.max(c.length,...rows.map(x=>x[i].length)));const f=x=>x.map((v,i)=>v.padEnd(w[i])).join(' | ').trimEnd();return [f(r.cols),w.map(n=>'-'.repeat(n)).join('-+-'),...rows.map(f)].join('\n')}
const items=JSON.parse(fs.readFileSync(0,'utf8'));
const out=items.map(({db,sql})=>{try{const d=SQLE.create(SEED[db||'toko']);const res=SQLE.exec(d,sql);const L=Array.isArray(res)?res:[res];const last=L.filter(x=>x&&x.cols).pop()||L[L.length-1];return {ok:true,out:tabel(last),raw:L.length}}catch(e){return {ok:false,err:String(e.message||e)}}});
process.stdout.write(JSON.stringify(out));
