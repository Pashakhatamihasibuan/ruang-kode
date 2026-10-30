/* ===================== PERBAIKI KODE YANG ERROR =====================
   Dibuat oleh tools/gen/bugs.py: satu kesalahan khas pemula ditanam di contoh kode, lalu kode
   rusak itu dijalankan dan pesan error aslinya disimpan. l.bug = {code, err, line, kind, why}. */
(()=>{
const BUGS=%BUGS%;
const M={java:JAVA_MODULES,python:PY_MODULES,ts:TS_MODULES,fe0:FE0_MODULES,fe:FE_MODULES,pda:PDA_MODULES,da:DA_MODULES,de:DE_MODULES,bi:BI_MODULES,sql:SQL_MODULES};
for(const [key,b] of Object.entries(BUGS)){const i=key.indexOf(':'),mods=M[key.slice(0,i)],ti=key.slice(i+1);
  const l=mods&&mods.flatMap(m=>m.lessons).find(x=>x.t===ti&&x.k==='c');if(!l)throw new Error('bugs: pelajaran tidak ditemukan: '+key);l.bug=b}
})();
