/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-cc1bcffadc',EXT='rk-ext',PRE=["/", "/c/rt.976478227c.js", "/c/book.34e885cb84.js", "/c/t-java.f11d08f0e4.js", "/c/t-python.1156418653.js", "/c/t-sql.8882b5e382.js", "/c/t-html.4312a78231.js", "/c/t-css.a98cabf7b9.js", "/c/t-fe0.057bd305e1.js", "/c/t-fe.ff0a7e993e.js", "/c/t-react.21233b6003.js", "/c/t-ts.dc9df83671.js", "/c/t-git.3fdf478b2b.js", "/c/t-pda.93d2841173.js", "/c/t-da.fc5a10470b.js", "/c/t-bi.2f6d2a04a4.js", "/c/t-de.55a1f8d86a.js", "/c/t-ux.668a257938.js", "/c/t-ds.8251de1445.js", "/c/t-msi.0294973270.js", "/c/t-sim.2c04ff715e.js", "/c/t-pseudo.a73110e08c.js", "/c/t-flowg.d7b097d394.js", "/c/t-dart.58dc56c6d0.js", "/c/t-flutter.8b443e6ee6.js", "/c/t-kotlin.18ae317de3.js", "/c/t-compose.b13c4d35a6.js", "/c/t-kmp.36d8110201.js", "/c/t-tw.85f45ac949.js", "/c/t-bs.75f081a80d.js", "/c/t-ui.1a36a51312.js", "/c/t-slw.d05ba2d123.js", "/c/t-slm.710cfc626a.js", "/c/t-dsa.6d3e80439c.js", "/c/t-pgdba.a31e3951ff.js", "/c/t-qa.8d3d5eb092.js", "/c/t-django.b7a6fe670e.js", "/c/t-nextjs.9ec846c958.js", "/c/t-vue.af043a068e.js", "/manifest.webmanifest", "/icons/icon-192.png"];
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
