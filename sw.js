/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-05a5b5d246',EXT='rk-ext',PRE=["/", "/c/rt.0b8e477805.js", "/c/book.fcc2fe4bf9.js", "/c/t-java.76ab13764d.js", "/c/t-python.aa28563ecd.js", "/c/t-sql.fb7d7daf87.js", "/c/t-html.5778a86f66.js", "/c/t-css.bb390c66f7.js", "/c/t-fe0.54a13828a2.js", "/c/t-fe.f1c7bd8174.js", "/c/t-react.3a07257ab1.js", "/c/t-ts.961f0d398c.js", "/c/t-git.e32f6e1d1d.js", "/c/t-pda.9312d047d4.js", "/c/t-da.db4ccf6800.js", "/c/t-bi.8b189466cb.js", "/c/t-de.f6ddbf9334.js", "/c/t-ux.be9d71d9b0.js", "/c/t-ds.949a9c619d.js", "/manifest.webmanifest", "/icons/icon-192.png"];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(PRE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k.startsWith('rk-')&&k!==V&&k!==EXT).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
const put=(name,req,res)=>{if(res&&(res.ok||res.type==='opaque')){const c=res.clone();caches.open(name).then(x=>x.put(req,c))}return res};
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);
  if(u.origin===location.origin){
    if(r.mode==='navigate'){ /* halaman: jaringan dulu, salinan tersimpan bila offline */
      e.respondWith(fetch(r).then(res=>put(V,u.pathname==='/'||u.pathname==='/index.html'?'/':r,res)).catch(()=>caches.match(r).then(m=>m||caches.match('/'))));return}
    e.respondWith(caches.match(r).then(m=>m||fetch(r).then(res=>put(V,r,res))));return}
  /* font dan pustaka CDN berversi tetap (React, Babel, Pyodide): ambil dari cache dulu */
  if(/^(fonts\.googleapis\.com|fonts\.gstatic\.com|cdn\.jsdelivr\.net)$/.test(u.hostname))
    e.respondWith(caches.open(EXT).then(c=>c.match(r).then(m=>m||fetch(r).then(res=>put(EXT,r,res)))));
});
