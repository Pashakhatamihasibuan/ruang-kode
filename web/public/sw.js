/* Service worker Ruang Kode: halaman yang pernah dibuka (atau disimpan lewat tombol "Simpan untuk offline")
   tetap bisa dibuka tanpa internet. Progres belajar tetap di localStorage; tidak ada data yang dikirim ke server.
   - Halaman: jaringan dulu, salinan cache bila offline, lalu halaman /offline bila belum pernah disimpan.
   - Aset build (/_next/static, ber-hash): cache dulu.
   - Lainnya (lab, ikon, data JSON): tampilkan cache, perbarui di belakang. */
const VER = "__BUILD__";
const PAGES = "rk-pages";
const STATIC = "rk-static";
const MISC = "rk-misc-" + VER;
const KEEP = [PAGES, STATIC, MISC];
const CORE = ["/", "/belajar", "/saya", "/glosarium", "/offline", "/manifest.webmanifest", "/icons/icon-192.png"];

self.addEventListener("install", (e) => {
  e.waitUntil((async () => {
    const c = await caches.open(PAGES);
    await Promise.all(CORE.map((u) => fetch(u, { cache: "no-cache" }).then((r) => r.ok && c.put(u, r)).catch(() => {})));
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (e) => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (!KEEP.includes(k)) await caches.delete(k);
    await self.clients.claim();
  })());
});

const key = (url) => { const u = new URL(url); u.search = ""; u.hash = ""; return u.pathname.replace(/\.html$/, "").replace(/(.)\/$/, "$1"); };

self.addEventListener("fetch", (e) => {
  const r = e.request;
  if (r.method !== "GET") return;
  const url = new URL(r.url);
  if (url.origin !== location.origin) return;

  if (r.mode === "navigate") {
    e.respondWith((async () => {
      const c = await caches.open(PAGES);
      try {
        const res = await fetch(r);
        if (res.ok && !res.redirected) c.put(key(r.url), res.clone());
        return res;
      } catch {
        return (await c.match(key(r.url))) || (await c.match("/offline")) || Response.error();
      }
    })());
    return;
  }

  if (url.pathname.startsWith("/_next/static/")) {
    e.respondWith((async () => {
      const c = await caches.open(STATIC);
      const hit = await c.match(r);
      if (hit) return hit;
      const res = await fetch(r);
      if (res.ok) c.put(r, res.clone());
      return res;
    })());
    return;
  }

  // payload navigasi React (?_rsc=) tidak disimpan: saat offline Next.js beralih ke muat halaman penuh dari cache
  if (url.searchParams.has("_rsc") || r.headers.get("RSC")) return;

  e.respondWith((async () => {
    const c = await caches.open(MISC);
    const hit = await c.match(r, { ignoreSearch: true });
    const net = fetch(r).then((res) => { if (res.ok) c.put(r, res.clone()); return res; }).catch(() => hit || Response.error());
    return hit || net;
  })());
});

/* pesan dari halaman: simpan daftar URL (satu jalur) ke cache halaman */
self.addEventListener("message", (e) => {
  const d = e.data || {};
  if (d.type !== "rk-save" || !Array.isArray(d.urls)) return;
  const port = e.ports && e.ports[0];
  e.waitUntil((async () => {
    const pages = await caches.open(PAGES), st = await caches.open(STATIC);
    const assets = new Set();
    let done = 0, fail = 0;
    for (const u of d.urls) {
      try {
        const res = await fetch(u, { cache: "no-cache" });
        if (!res.ok) throw new Error(String(res.status));
        const html = await res.clone().text();
        for (const m of html.matchAll(/\/_next\/static\/[^"'\s)]+/g)) assets.add(m[0]);
        await pages.put(key(new URL(u, location.origin).href), res);
      } catch { fail++; }
      done++;
      if (port) port.postMessage({ done, total: d.urls.length, fail });
    }
    for (const a of assets) if (!(await st.match(a))) await fetch(a).then((r) => r.ok && st.put(a, r)).catch(() => {});
    if (port) port.postMessage({ done, total: d.urls.length, fail, end: true });
  })());
});
