/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-cdd4e227d8',EXT='rk-ext',PRE=["/", "/c/rt.976478227c.js", "/c/book.34e885cb84.js", "/c/t-java.34595b9265.js", "/c/t-python.28b443b88b.js", "/c/t-sql.073e67a901.js", "/c/t-html.4312a78231.js", "/c/t-css.a98cabf7b9.js", "/c/t-fe0.fdd739c5fb.js", "/c/t-fe.ff0a7e993e.js", "/c/t-react.21233b6003.js", "/c/t-ts.dc9df83671.js", "/c/t-git.dfe511eb76.js", "/c/t-pda.881ab9fc4d.js", "/c/t-da.fc5a10470b.js", "/c/t-bi.4b34be9efa.js", "/c/t-de.c070e01a79.js", "/c/t-ux.82c5ad169d.js", "/c/t-ds.0be464db15.js", "/c/t-msi.9d2a04e1b5.js", "/c/t-sim.e30cfd7b8f.js", "/c/t-pseudo.da5c1d7ecd.js", "/c/t-flowg.9e550a037f.js", "/c/t-dart.13d4a5d562.js", "/c/t-flutter.0baad888b5.js", "/c/t-kotlin.c14b067fcc.js", "/c/t-compose.dbfd1a7adf.js", "/c/t-kmp.f501c1456d.js", "/c/t-tw.85f45ac949.js", "/c/t-bs.75f081a80d.js", "/c/t-ui.6346f69b06.js", "/c/t-slw.c9b0ba923e.js", "/c/t-slm.78d8e12d07.js", "/c/t-dsa.a735191ba3.js", "/c/t-pgdba.339589875e.js", "/c/t-qa.00b7d4fb61.js", "/c/t-django.b7a6fe670e.js", "/c/t-nextjs.9ec846c958.js", "/c/t-vue.af043a068e.js", "/c/t-dsci.e1e7ecbf59.js", "/c/t-proj.977913cb12.js", "/manifest.webmanifest", "/icons/icon-192.png"];
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
