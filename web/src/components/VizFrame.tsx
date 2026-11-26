"use client";
import { useEffect, useRef, useState } from "react";

/** Visual interaktif lama dijalankan di iframe sandbox (gaya dan skripnya tidak bercampur dengan halaman). */
export function VizFrame({ viz, v3, v3p, lang, lesson, title }: { viz?: string; v3?: string; v3p?: Record<string, unknown> | null; lang: string; lesson: Record<string, unknown>; title: string }) {
  const ref = useRef<HTMLIFrameElement>(null);
  const [h, setH] = useState(v3 ? 540 : 360);
  const [show, setShow] = useState(false);
  const box = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // dimuat saat mendekati layar agar halaman awal tetap ringan (3D memakai paket kecil /lab/v3d)
    const el = box.current;
    if (!el) return;
    const io = new IntersectionObserver((es) => { if (es.some((x) => x.isIntersecting)) { setShow(true); io.disconnect(); } }, { rootMargin: "1200px" });
    io.observe(el);
    return () => io.disconnect();
  }, []);

  useEffect(() => {
    const theme = () => document.documentElement.dataset.theme || "auto";
    const f = (e: MessageEvent) => {
      if (!ref.current || e.source !== ref.current.contentWindow || !e.data?.rkViz) return;
      if (e.data.ready) ref.current.contentWindow!.postMessage({ viz, v3, v3p, lang, lesson, theme: theme() }, "*");
      if (typeof e.data.h === "number") setH(Math.max(200, Math.min(e.data.h + 4, 2400)));
    };
    window.addEventListener("message", f);
    return () => window.removeEventListener("message", f);
  }, [viz, v3, v3p, lang, lesson]);

  return (
    <div ref={box} className="clay-in" style={{ padding: 6, minHeight: v3 ? 560 : 220 }}>
      {show
        ? <iframe ref={ref} className="viz-frame" src={v3 && !viz ? "/lab/v3d" : "/lab/viz"} sandbox="allow-scripts" title={`Visual interaktif${v3 ? " 3D" : ""}: ${title}`} style={{ height: h }} loading="lazy" />
        : <p className="muted" style={{ padding: 16 }}>Memuat visual…</p>}
    </div>
  );
}
