"use client";
import { useEffect, useId, useRef, useState } from "react";

const svgSrc = (s: string) => "data:image/svg+xml;charset=utf-8," + encodeURIComponent(s);

/** Menampilkan keluaran yang sudah diuji; untuk Python, kode bisa diubah dan dijalankan di sandbox Pyodide. */
export function Runner({ code, out, fig, lang, children }: { code: string; out: string | null; fig?: string[]; lang: string; children: React.ReactNode }) {
  const py = lang === "python";
  const [edit, setEdit] = useState(false);
  const [src, setSrc] = useState(code);
  const [res, setRes] = useState<{ out: string; figs: string[]; err?: boolean; status?: string } | null>(null);
  const [busy, setBusy] = useState(false);
  const frame = useRef<HTMLIFrameElement>(null);
  const ready = useRef<Promise<void> | null>(null);
  const uid = useId();

  useEffect(() => {
    const f = (e: MessageEvent) => {
      if (!frame.current || e.source !== frame.current.contentWindow || !e.data?.rkPy) return;
      const d = e.data;
      if (d.ready) return;
      if (d.id !== uid) return;
      if (d.status) setRes((r) => ({ out: r?.out ?? "", figs: [], status: d.status }));
      if (typeof d.out === "string") setRes({ out: d.out, figs: d.figs ?? [], err: !!d.err });
      if (d.done) setBusy(false);
    };
    window.addEventListener("message", f);
    return () => window.removeEventListener("message", f);
  }, [uid]);

  const runPy = (c: string) => {
    if (!frame.current) {
      const ifr = document.createElement("iframe");
      ifr.src = "/lab/py";
      ifr.setAttribute("sandbox", "allow-scripts");
      ifr.title = "Mesin Python";
      ifr.hidden = true;
      document.body.appendChild(ifr);
      frame.current = ifr;
      ready.current = new Promise((res) => {
        const h = (e: MessageEvent) => { if (e.source === ifr.contentWindow && e.data?.ready) { window.removeEventListener("message", h); res(); } };
        window.addEventListener("message", h);
      });
    }
    ready.current!.then(() => frame.current!.contentWindow!.postMessage({ run: c, id: uid }, "*"));
  };

  const run = () => {
    const c = edit ? src : code;
    if (!edit || c.trim() === code.trim()) {
      setRes({ out: out ?? "", figs: fig ?? [] });
      return;
    }
    setBusy(true);
    setRes({ out: "", figs: [], status: "Menyiapkan Python…" });
    runPy(c);
  };

  return (
    <div className="runner">
      {edit ? (
        <>
          <label className="sr-only" htmlFor={`ed-${uid}`}>Editor kode Python</label>
          <textarea id={`ed-${uid}`} className="editor" spellCheck={false} value={src} rows={Math.min(28, src.split("\n").length + 2)}
            onChange={(e) => setSrc(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); run(); }
              if (e.key === "Tab" && !e.shiftKey) {
                e.preventDefault();
                const t = e.currentTarget, s = t.selectionStart;
                setSrc(src.slice(0, s) + "    " + src.slice(t.selectionEnd));
                requestAnimationFrame(() => { t.selectionStart = t.selectionEnd = s + 4; });
              }
            }} />
        </>
      ) : children}
      <div className="acts">
        <button type="button" className="btn primary" onClick={run} disabled={busy}>{busy ? "Berjalan…" : res ? "↻ Jalankan lagi" : "▶ Jalankan"}</button>
        {py && (edit
          ? <button type="button" className="btn" onClick={() => { setSrc(code); setEdit(false); setRes(null); }}>Kembalikan kode asli</button>
          : <button type="button" className="btn" onClick={() => setEdit(true)}>✎ Ubah kodenya</button>)}
        <p className="hint">{py
          ? "Kode asli menampilkan keluaran yang sudah diuji. Kode yang kamu ubah dijalankan dengan Python di browser (terisolasi dari situs). Ctrl+Enter untuk menjalankan."
          : "Keluaran ini sudah diuji saat materi dibuat."}</p>
      </div>
      {res && (
        <div aria-live="polite">
          {res.status && !res.out ? <p className="msg info">{res.status}</p> : <pre className={`out${res.err ? " err" : ""}`}>{res.out || "(tidak ada keluaran)"}</pre>}
          {res.figs.length > 0 && (
            <div className="figs">{res.figs.map((s, i) => <img key={i} src={svgSrc(s)} alt={`Grafik ${i + 1} dari hasil kode`} />)}</div>
          )}
        </div>
      )}
    </div>
  );
}
