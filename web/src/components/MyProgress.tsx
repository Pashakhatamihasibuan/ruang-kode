"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { load, streak, type Lms } from "@/lib/progress";

type T = { k: string; name: string; mark: string; c: string; ids: string[] };

export function MyProgress({ tracks }: { tracks: T[] }) {
  const [s, setS] = useState<Lms | null>(null);
  useEffect(() => {
    const f = () => setS(load());
    f();
    window.addEventListener("rk-lms", f);
    return () => window.removeEventListener("rk-lms", f);
  }, []);
  if (!s) return <p className="muted">Memuat progres…</p>;
  const rows = tracks.map((t) => ({ ...t, d: t.ids.filter((i) => s.done[i]).length, at: s.lastAt?.[t.k] ?? 0 }))
    .filter((t) => t.d > 0 || t.at > 0).sort((a, b) => b.at - a.at);
  const total = Object.keys(s.done).length;
  const exportData = () => {
    const blob = new Blob([JSON.stringify(s, null, 1)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "progres-ruang-kode.json";
    a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  };
  return (
    <div className="stack">
      <div className="grid g4">
        <div className="card" style={{ background: "var(--lilac)" }}><span className="eyebrow">Pelajaran selesai</span><b style={{ fontSize: "2rem" }}>{total}</b></div>
        <div className="card" style={{ background: "var(--mint)" }}><span className="eyebrow">XP</span><b style={{ fontSize: "2rem" }}>{s.xp}</b></div>
        <div className="card" style={{ background: "var(--peach)" }}><span className="eyebrow">Hari beruntun</span><b style={{ fontSize: "2rem" }}>{streak(s)}</b></div>
        <div className="card" style={{ background: "var(--sky)" }}><span className="eyebrow">Jalur aktif</span><b style={{ fontSize: "2rem" }}>{rows.length}</b></div>
      </div>
      {rows.length === 0 ? (
        <div className="card">
          <h2>Belum ada progres</h2>
          <p className="muted">Buka satu jalur, pelajari materinya, lalu tekan “Tandai selesai”. Progres akan muncul di sini.</p>
          <Link className="btn primary" href="/belajar">Pilih jalur belajar</Link>
        </div>
      ) : (
        <div className="grid g3">
          {rows.map((t) => {
            const p = Math.round((t.d / t.ids.length) * 100);
            return (
              <Link key={t.k} href={`/belajar/${t.k}`} className="card tcard" style={{ ["--tc" as string]: t.c }}>
                <div className="hd"><span className="blob" aria-hidden="true">{t.mark}</span><h2 style={{ fontSize: "1.1rem", margin: 0 }}>{t.name}</h2></div>
                <p>{t.d} dari {t.ids.length} pelajaran selesai ({p}%)</p>
                <div className="bar" role="progressbar" aria-label={`Progres ${t.name}`} aria-valuenow={p} aria-valuemin={0} aria-valuemax={100} style={{ ["--p" as string]: p }}><i /></div>
              </Link>
            );
          })}
        </div>
      )}
      <div className="card">
        <h2>Data progres</h2>
        <p className="muted">Progres hanya disimpan di browser ini dan tidak pernah dikirim ke server. Simpan cadangan sebelum mengganti perangkat atau menghapus data browser.</p>
        <button type="button" className="btn" onClick={exportData}>⬇ Unduh cadangan progres (JSON)</button>
      </div>
    </div>
  );
}
