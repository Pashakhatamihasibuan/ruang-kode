"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { Icon } from "./Icon";

type Row = [string, string, string, string]; // judul, url, keterangan, jenis
const norm = (s: string) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");

export function Search() {
  const dlg = useRef<HTMLDialogElement>(null);
  const inp = useRef<HTMLInputElement>(null);
  const [rows, setRows] = useState<Row[] | null>(null);
  const [q, setQ] = useState("");
  const [sel, setSel] = useState(0);
  const router = useRouter();

  const open = useCallback(() => {
    dlg.current?.showModal();
    inp.current?.focus();
    if (!rows) fetch("/search-index.json").then((r) => r.json()).then(setRows).catch(() => setRows([]));
  }, [rows]);

  useEffect(() => {
    const k = (e: KeyboardEvent) => {
      const t = e.target as HTMLElement;
      const typing = t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.isContentEditable);
      if ((e.key === "k" && (e.ctrlKey || e.metaKey)) || (e.key === "/" && !typing)) {
        e.preventDefault();
        open();
      }
    };
    window.addEventListener("keydown", k);
    return () => window.removeEventListener("keydown", k);
  }, [open]);

  const hits = useMemo(() => {
    if (!rows) return [];
    const words = norm(q).split(/\s+/).filter(Boolean);
    if (!words.length) return rows.filter((r) => r[3] === "Jalur").slice(0, 12);
    const out: [number, Row][] = [];
    for (const r of rows) {
      const t = norm(r[0]), all = t + " " + norm(r[2]);
      if (!words.every((w) => all.includes(w))) continue;
      const s = (t.startsWith(words[0]) ? 0 : 2) + (r[3] === "Jalur" ? -1 : 0) + t.length / 200;
      out.push([s, r]);
      if (out.length > 400) break;
    }
    return out.sort((a, b) => a[0] - b[0]).slice(0, 30).map((x) => x[1]);
  }, [rows, q]);

  useEffect(() => setSel(0), [q]);
  const go = (u: string) => {
    dlg.current?.close();
    router.push(u);
  };
  const onKey = (e: React.KeyboardEvent) => {
    if (e.key === "ArrowDown") { e.preventDefault(); setSel((s) => Math.min(s + 1, hits.length - 1)); }
    else if (e.key === "ArrowUp") { e.preventDefault(); setSel((s) => Math.max(s - 1, 0)); }
    else if (e.key === "Enter" && hits[sel]) { e.preventDefault(); go(hits[sel][1]); }
  };
  useEffect(() => {
    document.getElementById(`sr-${sel}`)?.scrollIntoView({ block: "nearest" });
  }, [sel]);

  return (
    <>
      <button type="button" className="btn search-btn" onClick={open} aria-label="Cari materi (Ctrl+K)">
        <Icon name="search" size={18} /><span className="t">Cari materi…</span><kbd>Ctrl K</kbd>
      </button>
      <dialog ref={dlg} className="dlg" aria-label="Pencarian" onClick={(e) => e.target === dlg.current && dlg.current?.close()}>
        <div className="box">
          <label htmlFor="sq" className="sr-only">Cari jalur, pelajaran, atau istilah</label>
          <input ref={inp} id="sq" type="search" placeholder="Cari jalur, pelajaran, atau istilah…" autoComplete="off"
            value={q} onChange={(e) => setQ(e.target.value)} onKeyDown={onKey}
            role="combobox" aria-expanded="true" aria-controls="sr-list" aria-activedescendant={hits[sel] ? `sr-${sel}` : undefined} />
          <ul id="sr-list" role="listbox" aria-label="Hasil pencarian">
            {rows === null && <li className="muted">Memuat indeks…</li>}
            {rows && !hits.length && <li className="muted">Tidak ada hasil untuk “{q}”.</li>}
            {hits.map((r, i) => (
              <li key={r[1] + i} role="option" id={`sr-${i}`} aria-selected={i === sel}>
                <a href={r[1]} aria-selected={i === sel} onClick={(e) => { e.preventDefault(); go(r[1]); }} tabIndex={-1}>
                  <b>{r[0]}</b><small>{r[3]} · {r[2]}</small>
                </a>
              </li>
            ))}
          </ul>
          <p className="small muted" style={{ margin: 0 }}><kbd>↑</kbd> <kbd>↓</kbd> pilih · <kbd>Enter</kbd> buka · <kbd>Esc</kbd> tutup</p>
        </div>
      </dialog>
    </>
  );
}
