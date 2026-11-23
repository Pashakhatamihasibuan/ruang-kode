import Link from "next/link";

export default function NotFound() {
  return (
    <div className="wrap">
      <div className="card" style={{ marginTop: 40, textAlign: "center" }}>
        <span className="eyebrow">404</span>
        <h1>Halaman tidak ditemukan</h1>
        <p className="muted">Mungkin alamatnya berubah. Cari materinya lewat katalog atau tombol cari (Ctrl+K).</p>
        <Link className="btn primary" href="/belajar">Buka katalog materi</Link>
      </div>
    </div>
  );
}
