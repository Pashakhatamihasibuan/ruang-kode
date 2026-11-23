"use client";
import { useMemo, useState } from "react";

type Raw = [number, string, Record<string, unknown>, string, number?];
interface Step { ln: number; fn: string; v: Record<string, unknown>; o: string; ch: string[] }

function steps(s: Raw[]): Step[] {
  let pv: Record<string, unknown> = {}, pf: string | null = null;
  return s.map(([ln, fn, d, o, full]) => {
    let v: Record<string, unknown>;
    if (full || fn !== pf) v = { ...d };
    else {
      v = { ...pv, ...d };
      ((d["-"] as string[]) || []).forEach((k) => delete v[k]);
      delete v["-"];
    }
    const ch = Object.keys(v).filter((k) => pv[k] !== v[k] && fn === pf);
    pv = v; pf = fn;
    return { ln, fn, v, o, ch };
  });
}

/** Memutar ulang rekaman eksekusi: baris yang akan dijalankan, isi variabel, dan keluaran. */
export function Tracer({ code, trace, cut }: { code: string; trace: Raw[]; cut?: boolean }) {
  const S = useMemo(() => steps(trace), [trace]);
  const [i, setI] = useState(0);
  const [open, setOpen] = useState(false);
  const s = S[i];
  const lines = code.split("\n");
  const fnName = (f: string) => (f === "<module>" || f === "main" ? "program utama" : f + "()");
  if (!open) return <button type="button" className="btn" onClick={() => setOpen(true)}>👣 Jalankan langkah demi langkah</button>;
  return (
    <div className="card" style={{ background: "var(--surface-2)" }} onKeyDown={(e) => {
      if (e.key === "ArrowRight") setI((x) => Math.min(x + 1, S.length - 1));
      if (e.key === "ArrowLeft") setI((x) => Math.max(x - 1, 0));
    }}>
      <div className="acts" style={{ display: "flex", gap: 8, flexWrap: "wrap", alignItems: "center", marginBottom: 12 }}>
        <button type="button" className="btn sm" onClick={() => setI(0)} aria-label="Ke awal">⏮</button>
        <button type="button" className="btn sm" onClick={() => setI(Math.max(i - 1, 0))}>◀ Mundur</button>
        <button type="button" className="btn sm primary" onClick={() => setI(Math.min(i + 1, S.length - 1))}>Maju ▶</button>
        <input type="range" min={0} max={S.length - 1} value={i} onChange={(e) => setI(+e.target.value)} aria-label="Pilih langkah" style={{ flex: "1 1 160px" }} />
        <span className="small muted" aria-live="polite">Langkah {i + 1} dari {S.length}{s.ln ? ` · di ${fnName(s.fn)}` : ""}</span>
      </div>
      <div className="trc-grid">
        <div className="clay-in trc-code" aria-label="Kode">
          {lines.map((l, k) => <div key={k} className={s.ln === k + 1 ? "on" : undefined}><i>{k + 1}</i>{l || " "}</div>)}
        </div>
        <div>
          <span className="eyebrow">Variabel</span>
          <table className="trc-vars"><tbody>
            {Object.keys(s.v).length ? Object.entries(s.v).map(([k, v]) => (
              <tr key={k} className={s.ch.includes(k) ? "chg" : undefined}><th scope="row">{k}</th><td>{String(v)}</td></tr>
            )) : <tr><td className="muted">Belum ada variabel.</td></tr>}
          </tbody></table>
          <div className="out-l">Keluaran sejauh ini</div>
          <pre className="out">{s.o || " "}</pre>
        </div>
      </div>
      <p className="small muted" style={{ marginTop: 10 }}>Baris yang disorot adalah baris yang <b>akan</b> dijalankan berikutnya. Variabel yang baru berubah diberi warna hijau. Panah kiri/kanan juga bisa dipakai.{cut ? " Program ini panjang, jadi hanya 200 langkah pertama yang ditampilkan." : ""}</p>
    </div>
  );
}
