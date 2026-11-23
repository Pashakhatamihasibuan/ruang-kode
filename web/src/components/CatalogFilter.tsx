"use client";
import { useEffect, useState } from "react";

export function CatalogFilter({ groups }: { groups: { k: string; t: string }[] }) {
  const [g, setG] = useState("");
  const [q, setQ] = useState("");
  const [n, setN] = useState<number | null>(null);
  useEffect(() => {
    const w = q.toLowerCase().trim();
    let shown = 0;
    document.querySelectorAll<HTMLElement>("[data-group]").forEach((sec) => {
      let c = 0;
      sec.querySelectorAll<HTMLElement>("[data-name]").forEach((a) => {
        const ok = (!g || a.dataset.g === g) && (!w || a.dataset.name!.includes(w));
        a.hidden = !ok;
        if (ok) c++;
      });
      sec.hidden = c === 0;
      shown += c;
    });
    setN(g || w ? shown : null);
  }, [g, q]);
  return (
    <div className="filters" role="search">
      <label htmlFor="kq" className="sr-only">Saring jalur</label>
      <input id="kq" type="search" placeholder="Saring jalur, mis. python, data, desain…" value={q} onChange={(e) => setQ(e.target.value)} />
      <div className="tabs" role="group" aria-label="Kelompok">
        <button type="button" className="btn sm" aria-pressed={g === ""} onClick={() => setG("")}>Semua</button>
        {groups.map((x) => (
          <button type="button" key={x.k} className="btn sm" aria-pressed={g === x.k} onClick={() => setG(g === x.k ? "" : x.k)}>{x.t}</button>
        ))}
      </div>
      <span className="small muted" aria-live="polite">{n === null ? "" : `${n} jalur cocok`}</span>
    </div>
  );
}
