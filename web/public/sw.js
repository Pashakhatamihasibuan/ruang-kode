/* Ruang Kode versi Next.js tidak memakai service worker.
   Berkas ini menggantikan service worker versi lama: menghapus cache lama, melepas dirinya,
   lalu memuat ulang tab yang terbuka agar pengunjung lama langsung melihat versi baru. */
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (e) => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) await caches.delete(k);
    await self.registration.unregister();
    const tabs = await self.clients.matchAll({ type: "window" });
    for (const c of tabs) c.navigate(c.url).catch(() => {});
  })());
});
