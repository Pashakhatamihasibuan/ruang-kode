/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-4a9c6332ce',EXT='rk-ext',PRE=["/", "/c/rt.976478227c.js", "/c/book.34e885cb84.js", "/c/t-java.34595b9265.js", "/c/t-python.28b443b88b.js", "/c/t-sql.073e67a901.js", "/c/t-html.3808b2509c.js", "/c/t-css.1e3cd196b4.js", "/c/t-fe0.9a11299ff3.js", "/c/t-fe.d50c01f146.js", "/c/t-react.ca2cfc1284.js", "/c/t-ts.ab46055a35.js", "/c/t-git.dfe511eb76.js", "/c/t-pda.881ab9fc4d.js", "/c/t-da.67c0dd9c80.js", "/c/t-bi.4b34be9efa.js", "/c/t-de.c070e01a79.js", "/c/t-ux.8c7c8e2e86.js", "/c/t-ds.34dd21aa94.js", "/c/t-msi.9d2a04e1b5.js", "/c/t-sim.e30cfd7b8f.js", "/c/t-pseudo.da5c1d7ecd.js", "/c/t-flowg.9e550a037f.js", "/c/t-dart.13d4a5d562.js", "/c/t-flutter.0baad888b5.js", "/c/t-kotlin.c14b067fcc.js", "/c/t-compose.dbfd1a7adf.js", "/c/t-kmp.f501c1456d.js", "/c/t-tw.807fa44377.js", "/c/t-bs.f30bc57a4b.js", "/c/t-ui.75095cb110.js", "/c/t-slw.2e5f2359e1.js", "/c/t-slm.37d8760e5c.js", "/c/t-dsa.a735191ba3.js", "/c/t-pgdba.339589875e.js", "/c/t-qa.00b7d4fb61.js", "/c/t-django.0545396f46.js", "/c/t-nextjs.bbe7731dcd.js", "/c/t-vue.44350f3ab6.js", "/c/t-dsci.91b513c2fe.js", "/c/t-proj.b2623a5718.js", "/c/t-js.e0b69cac43.js", "/manifest.webmanifest", "/icons/icon-192.png"];
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
