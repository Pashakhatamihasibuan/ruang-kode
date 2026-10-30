/* Service worker Ruang Kode (dibuat oleh build.py). Inti aplikasi dan semua materi
   disimpan saat dipasang, jadi situs tetap bisa dibuka tanpa internet. */
const V='rk-%VERSION%',EXT='rk-ext',PRE=%PRECACHE%;
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
