"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { load, resetAll, resetTrack, restore, streak, toast, type Lms } from "@/lib/progress";

type T = { k: string; name: string; mark: string; c: string; ids: string[] };

export function MyProgress({ tracks }: { tracks: T[] }) {
  const [s, setS] = useState<Lms | null>(null);
  const [ask, setAsk] = useState<string | null>(null); // kunci jalur, "*" untuk semua, null bila tidak ada konfirmasi
  const [undo, setUndo] = useState<{ data: Lms; label: string } | null>(null);
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
  const doReset = (key: string) => {
    if (key === "*") {
      setUndo({ data: resetAll(), label: "Semua progres dihapus." });
    } else {
      const t = tracks.find((x) => x.k === key)!;
      setUndo({ data: resetTrack(t.k, t.ids), label: `Progres ${t.name} dihapus.` });
    }
    setAsk(null);
  };
  const doUndo = () => {
    if (!undo) return;
    restore(undo.data);
    setUndo(null);
    toast("Progres dipulihkan.");
  };
  const Confirm = ({ k, what }: { k: string; what: string }) => (
    <div className="msg bad stack-sm" role="alertdialog" aria-label={`Konfirmasi hapus ${what}`}>
      <span>Hapus {what}? Tanda selesai, XP kuis, dan latihan ikut terhapus.</span>
      <div className="row-btn">
        <button type="button" className="btn sm danger" onClick={() => doReset(k)} autoFocus>Ya, hapus</button>
        <button type="button" className="btn sm" onClick={() => setAsk(null)}>Batal</button>
      </div>
    </div>
  );
  return (
    <div className="stack">
      <div aria-live="polite">
        {undo && (
          <div className="msg info row-btn" style={{ justifyContent: "space-between" }}>
            <span>{undo.label}</span>
            <button type="button" className="btn sm" onClick={doUndo}>↶ Urungkan</button>
          </div>
        )}
      </div>
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
              <div key={t.k} className="card tcard" style={{ ["--tc" as string]: t.c }}>
                <div className="hd"><span className="blob" aria-hidden="true">{t.mark}</span>
                  <h2 style={{ fontSize: "1.1rem", margin: 0 }}><Link href={`/belajar/${t.k}`}>{t.name}</Link></h2></div>
                <p>{t.d} dari {t.ids.length} pelajaran selesai ({p}%)</p>
                <div className="bar" role="progressbar" aria-label={`Progres ${t.name}`} aria-valuenow={p} aria-valuemin={0} aria-valuemax={100} style={{ ["--p" as string]: p }}><i /></div>
                {ask === t.k ? <Confirm k={t.k} what={`progres ${t.name}`} /> : (
                  <div className="row-btn">
                    <Link className="btn sm primary" href={`/belajar/${t.k}`}>Lanjutkan</Link>
                    <button type="button" className="btn sm" onClick={() => setAsk(t.k)} aria-label={`Hapus progres ${t.name}`}>Hapus progres</button>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
      <div className="card">
        <h2>Data progres</h2>
        <p className="muted">Progres hanya disimpan di browser ini dan tidak pernah dikirim ke server. Simpan cadangan sebelum mengganti perangkat atau menghapus data browser.</p>
        <div className="row-btn">
          <button type="button" className="btn" onClick={exportData}>⬇ Unduh cadangan progres (JSON)</button>
          {total > 0 || rows.length > 0 ? (ask === "*" ? null : <button type="button" className="btn danger" onClick={() => setAsk("*")}>Hapus semua progres</button>) : null}
        </div>
        {ask === "*" && <Confirm k="*" what="semua progres di browser ini" />}
      </div>
    </div>
  );
}
