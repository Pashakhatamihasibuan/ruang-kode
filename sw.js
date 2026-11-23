/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-53690c9af3',EXT='rk-ext',PRE=["/", "/c/rt.976478227c.js", "/c/book.34e885cb84.js", "/c/t-java.907f2d3bea.js", "/c/t-python.4ef47aac0c.js", "/c/t-sql.85042201a8.js", "/c/t-html.e4aeec0477.js", "/c/t-css.4c5ca2ada5.js", "/c/t-fe0.0a93a6f359.js", "/c/t-fe.ed222f022b.js", "/c/t-react.996de3c418.js", "/c/t-ts.ff4a053bab.js", "/c/t-git.cb8e3b97c0.js", "/c/t-pda.6e7e56ba6c.js", "/c/t-da.60defdacdc.js", "/c/t-bi.762770e68a.js", "/c/t-de.d6920e39ec.js", "/c/t-ux.6c82e38ac8.js", "/c/t-ds.fc9d0a17b0.js", "/c/t-msi.1b9896dcf2.js", "/c/t-sim.53fcf5fac6.js", "/c/t-pseudo.0e6d851f4b.js", "/c/t-flowg.b07a95f9ef.js", "/c/t-dart.eb50c3d226.js", "/c/t-flutter.b82adb53ad.js", "/c/t-kotlin.5290cff317.js", "/c/t-compose.d66e14095f.js", "/c/t-kmp.d9594e0377.js", "/c/t-tw.ee04c0d2ab.js", "/c/t-bs.6951262998.js", "/c/t-ui.0bd0cb30e3.js", "/c/t-slw.c16a37712e.js", "/c/t-slm.eeb7d807c6.js", "/c/t-dsa.474bc2ea80.js", "/c/t-pgdba.38a431ce16.js", "/c/t-qa.af1b924362.js", "/c/t-django.a801a1977a.js", "/c/t-nextjs.ee07e705d6.js", "/c/t-vue.2709c699b7.js", "/c/t-dsci.5e461e791f.js", "/c/t-proj.e4679d36b1.js", "/c/t-js.b1ed567ab9.js", "/manifest.webmanifest", "/icons/icon-192.png"];
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
