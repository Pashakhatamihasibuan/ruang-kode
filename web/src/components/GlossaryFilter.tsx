"use client";
import { useEffect, useState } from "react";

export function GlossaryFilter({ cats }: { cats: string[] }) {
  const [q, setQ] = useState("");
  const [c, setC] = useState("");
  const [n, setN] = useState<number | null>(null);
  useEffect(() => {
    const w = q.toLowerCase().trim();
    let shown = 0;
    document.querySelectorAll<HTMLElement>("[data-gcat]").forEach((sec) => {
      let k = 0;
      const catOk = !c || sec.dataset.gcat === c;
      sec.querySelectorAll<HTMLElement>("[data-gname]").forEach((a) => {
        const ok = catOk && (!w || a.dataset.gname!.includes(w));
        a.hidden = !ok;
        if (ok) k++;
      });
      sec.hidden = k === 0;
      shown += k;
    });
    setN(q || c ? shown : null);
  }, [q, c]);
  return (
    <div className="filters" role="search">
      <label htmlFor="gq" className="sr-only">Cari istilah</label>
      <input id="gq" type="search" placeholder="Cari istilah, mis. primary key, closure, KPI…" value={q} onChange={(e) => setQ(e.target.value)} />
      <label htmlFor="gc" className="sr-only">Kategori</label>
      <select id="gc" value={c} onChange={(e) => setC(e.target.value)} style={{ maxWidth: 260 }}>
        <option value="">Semua kategori</option>
        {cats.map((x) => <option key={x} value={x}>{x}</option>)}
      </select>
      <span className="small muted" aria-live="polite">{n === null ? "" : `${n} istilah cocok`}</span>
    </div>
  );
}
