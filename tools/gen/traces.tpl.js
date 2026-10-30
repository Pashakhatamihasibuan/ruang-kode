/* ===================== JALANKAN LANGKAH DEMI LANGKAH =====================
   Dibuat oleh tools/gen/traces.py dari eksekusi sungguhan. l.trc = {s, o, cut}:
   s = langkah [baris, fungsi, variabel (lengkap jika penanda 1, selain itu hanya yang berubah), panjang keluaran, penanda],
   o = keluaran lengkap. */
(()=>{
const TRC=%TRACES%;
const M={java:JAVA_MODULES,python:PY_MODULES,ts:TS_MODULES,fe0:FE0_MODULES,fe:FE_MODULES};
for(const [key,v] of Object.entries(TRC)){const i=key.indexOf(':'),mods=M[key.slice(0,i)],ti=key.slice(i+1);
  const l=mods&&mods.flatMap(m=>m.lessons).find(x=>x.t===ti&&x.k==='c');if(!l)throw new Error('traces: pelajaran tidak ditemukan: '+key);l.trc=v}
})();
