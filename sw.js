/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-8c12b2c213',EXT='rk-ext',PRE=["/", "/c/rt.976478227c.js", "/c/book.34e885cb84.js", "/c/t-java.9f886452fb.js", "/c/t-python.0c7cc32207.js", "/c/t-sql.aa39e8a6f6.js", "/c/t-html.4312a78231.js", "/c/t-css.a98cabf7b9.js", "/c/t-fe0.057bd305e1.js", "/c/t-fe.ff0a7e993e.js", "/c/t-react.21233b6003.js", "/c/t-ts.dc9df83671.js", "/c/t-git.3fdf478b2b.js", "/c/t-pda.260f5b9d54.js", "/c/t-da.6353164264.js", "/c/t-bi.8805bda050.js", "/c/t-de.01beaa8dc7.js", "/c/t-ux.f487e550c9.js", "/c/t-ds.df0b5f3e28.js", "/c/t-msi.925c097357.js", "/c/t-sim.7abe99beff.js", "/c/t-pseudo.d0fc7d5404.js", "/c/t-flowg.d7b097d394.js", "/c/t-dart.58dc56c6d0.js", "/c/t-flutter.34341b3b82.js", "/c/t-kotlin.2b5be3c481.js", "/c/t-compose.13a7ae1066.js", "/c/t-kmp.36d8110201.js", "/c/t-tw.85f45ac949.js", "/c/t-bs.75f081a80d.js", "/manifest.webmanifest", "/icons/icon-192.png"];
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
