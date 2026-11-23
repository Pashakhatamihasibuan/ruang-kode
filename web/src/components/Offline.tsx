"use client";
import { useEffect, useState } from "react";
import { toast } from "@/lib/progress";

/** Mendaftarkan service worker (mode offline) dan memberi tahu saat koneksi putus atau kembali. */
export function SwRegister() {
  useEffect(() => {
    if (!("serviceWorker" in navigator)) return;
    navigator.serviceWorker.register("/sw.js").catch(() => {});
    const off = () => toast("Kamu sedang offline. Halaman yang sudah disimpan tetap bisa dibuka.");
    const on = () => toast("Kembali online.");
    window.addEventListener("offline", off);
    window.addEventListener("online", on);
    return () => { window.removeEventListener("offline", off); window.removeEventListener("online", on); };
  }, []);
  return null;
}

/** Tombol menyimpan semua pelajaran satu jalur ke perangkat agar bisa dibuka tanpa internet. */
export function OfflineSave({ urls, name }: { urls: string[]; name: string }) {
  const [st, setSt] = useState<"cek" | "belum" | "simpan" | "siap" | "tidak">("cek");
  const [p, setP] = useState({ done: 0, total: urls.length, fail: 0 });

  useEffect(() => {
    if (!("serviceWorker" in navigator) || !("caches" in window)) { setSt("tidak"); return; }
    (async () => {
      try {
        const c = await caches.open("rk-pages");
        const hits = await Promise.all(urls.map((u) => c.match(u)));
        setSt(hits.every(Boolean) ? "siap" : "belum");
      } catch { setSt("tidak"); }
    })();
  }, [urls]);

  const save = async () => {
    const reg = await navigator.serviceWorker.ready;
    if (!reg.active) return;
    setSt("simpan");
    setP({ done: 0, total: urls.length, fail: 0 });
    const ch = new MessageChannel();
    ch.port1.onmessage = (e) => {
      const d = e.data;
      setP({ done: d.done, total: d.total, fail: d.fail });
      if (d.end) {
        setSt(d.fail ? "belum" : "siap");
        toast(d.fail ? `${d.fail} halaman gagal disimpan. Coba lagi saat koneksi stabil.` : `${name} tersimpan. Bisa dibuka tanpa internet.`);
      }
    };
    reg.active.postMessage({ type: "rk-save", urls }, [ch.port2]);
  };

  if (st === "tidak") return null;
  const pct = Math.round((p.done / Math.max(1, p.total)) * 100);
  return (
    <div className="offline-save" aria-live="polite">
      {st === "siap" ? (
        <span className="chip mint">✓ Tersimpan untuk offline</span>
      ) : st === "simpan" ? (
        <div className="stack-sm" style={{ minWidth: 220 }}>
          <span className="small">Menyimpan {p.done} dari {p.total} halaman…</span>
          <div className="bar" role="progressbar" aria-label="Progres menyimpan untuk offline" aria-valuenow={pct} aria-valuemin={0} aria-valuemax={100} style={{ ["--p" as string]: pct }}><i /></div>
        </div>
      ) : (
        <button type="button" className="btn sm" onClick={save} disabled={st === "cek"}>⤓ Simpan jalur untuk offline</button>
      )}
    </div>
  );
}
