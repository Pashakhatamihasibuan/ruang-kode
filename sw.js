/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-c84832d442',EXT='rk-ext',PRE=["/", "/c/rt.0b8e477805.js", "/c/book.fcc2fe4bf9.js", "/c/t-java.7a6f493f72.js", "/c/t-python.9c57b527ff.js", "/c/t-sql.aa39e8a6f6.js", "/c/t-html.aec5f27da8.js", "/c/t-css.b5cb5d84c8.js", "/c/t-fe0.ce24da4260.js", "/c/t-fe.657f7e7cf1.js", "/c/t-react.5441f6eb3e.js", "/c/t-ts.ec5aaa1802.js", "/c/t-git.c4b757e845.js", "/c/t-pda.d457c6d19c.js", "/c/t-da.50283623dc.js", "/c/t-bi.52494b1085.js", "/c/t-de.95c8df4dd6.js", "/c/t-ux.f487e550c9.js", "/c/t-ds.df0b5f3e28.js", "/manifest.webmanifest", "/icons/icon-192.png"];
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
