import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = { title: "Sedang offline", robots: { index: false, follow: false } };

export default function OfflinePage() {
  return (
    <div className="wrap" style={{ minHeight: "70vh" }}>
      <section className="card" style={{ marginTop: 28 }} aria-labelledby="off-h">
        <span className="eyebrow">Tanpa internet</span>
        <h1 id="off-h">Halaman ini belum tersimpan di perangkatmu</h1>
        <p>Kamu sedang offline. Halaman yang pernah kamu buka, atau jalur yang kamu simpan dengan tombol “Simpan jalur untuk offline”, tetap bisa dibuka. Progres belajarmu aman di perangkat ini.</p>
        <p className="muted small">Menjalankan kode Python butuh internet karena mesinnya diunduh saat pertama dipakai.</p>
        <div className="row-btn">
          <Link className="btn primary" href="/saya">Buka progres saya</Link>
          <Link className="btn" href="/belajar">Lihat semua materi</Link>
        </div>
      </section>
    </div>
  );
}
