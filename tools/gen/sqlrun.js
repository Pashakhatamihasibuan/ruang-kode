// Menjalankan query dengan mesin SQL Ruang Kode dan mencetak hasilnya sebagai teks.
// Pemakaian: echo '{"db":"toko","sql":"SELECT 1"}' | node sqlrun.js
const fs=require('fs'),vm=require('vm'),path=require('path');
const J=f=>fs.readFileSync(path.join(__dirname,'../../src/js',f),'utf8');
const {SQLE,SEED}=vm.runInNewContext(J('sqlengine.js')+J('sqldata.js')+J('sqldata-bi.js')+';({SQLE,SEED})');
const {db,sql}=JSON.parse(fs.readFileSync(0,'utf8'));
const res=SQLE.exec(SQLE.create(SEED[db]),sql);const r=res[res.length-1];
const rows=[r.cols,...r.rows.map(x=>x.map(v=>v==null?'NULL':String(v)))];
const w=r.cols.map((_,i)=>Math.max(...rows.map(x=>x[i].length)));
process.stdout.write(rows.map((x,j)=>x.map((v,i)=>v.padEnd(w[i])).join(' | ').trimEnd()+(j===0?'\n'+w.map(n=>'-'.repeat(n)).join('-+-'):'')).join('\n')+'\n');
