/* ===================== KODE PEMULA VS KODE RAPI =====================
   Perbandingan cara pemula dan cara yang lebih rapi (best practice), termasuk trik yang
   jarang diketahui. Ditempel ke pelajaran berdasarkan judulnya: l.pro = [{t,why,a,b,out,lang}].
   Setiap pasangan kode sudah dijalankan dan menghasilkan keluaran yang sama. */
(()=>{
const PRO=%PRO%;
const M={java:JAVA_MODULES,python:PY_MODULES,sql:SQL_MODULES,html:HTML_MODULES,css:CSS_MODULES,fe0:FE0_MODULES,fe:FE_MODULES,react:REACT_MODULES,ts:TS_MODULES,git:GIT_MODULES,pda:PDA_MODULES,da:DA_MODULES,bi:BI_MODULES,de:DE_MODULES,ux:UX_MODULES,ds:DS_MODULES};
for(const [key,list] of Object.entries(PRO)){const i=key.indexOf(':'),mods=M[key.slice(0,i)],ti=key.slice(i+1);
  const l=mods&&mods.flatMap(m=>m.lessons).find(x=>x.t===ti);if(!l)throw new Error('tips: pelajaran tidak ditemukan: '+key);l.pro=(l.pro||[]).concat(list)}
})();
