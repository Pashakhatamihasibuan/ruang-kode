/* ===================== PELAJARAN TAMBAHAN JALUR BARU =====================
   Dibuat oleh tools/gen/more.py. Setiap pelajaran ditambahkan di akhir modul yang dituju,
   sehingga alamat pelajaran lama (jalur-modul-urutan) tidak bergeser. */
(()=>{
const MORE=%MORE%;
const M={html:HTML_MODULES,css:CSS_MODULES,fe0:FE0_MODULES,fe:FE_MODULES,react:REACT_MODULES,ts:TS_MODULES,git:GIT_MODULES,pda:PDA_MODULES,da:DA_MODULES,bi:BI_MODULES,de:DE_MODULES,ux:UX_MODULES,ds:DS_MODULES};
for(const {track,module,lesson} of MORE){const m=(M[track]||[]).find(x=>x.t===module);
  if(!m)throw new Error('more: modul tidak ditemukan: '+track+' / '+module);m.lessons.push(lesson)}
})();
