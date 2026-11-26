"use client";
import { useEffect, useState } from "react";
import { load } from "@/lib/progress";

/** Menandai tautan pelajaran yang sudah selesai (atribut data-lid) setelah halaman statis dimuat. */
export function DoneMarks() {
  useEffect(() => {
    const paint = () => {
      const s = load();
      document.querySelectorAll<HTMLElement>("[data-lid]").forEach((a) => {
        if (s.done[a.dataset.lid!]) a.setAttribute("data-done", ""); else a.removeAttribute("data-done");
      });
      // hitungan selesai per materi di sidebar, misalnya "3/7"; penuh diberi tanda centang
      document.querySelectorAll<HTMLElement>("[data-ids]").forEach((c) => {
        const ids = (c.dataset.ids || "").split(",").filter(Boolean);
        const d = ids.filter((i) => s.done[i]).length;
        c.textContent = d === ids.length && d > 0 ? "✓" : d ? `${d}/${ids.length}` : String(ids.length);
        c.setAttribute("aria-label", d ? `${d} dari ${ids.length} sub materi selesai` : `${ids.length} sub materi`);
        if (d === ids.length && d > 0) c.setAttribute("data-full", ""); else c.removeAttribute("data-full");
      });
    };
    paint();
    window.addEventListener("rk-lms", paint);
    window.addEventListener("storage", paint);
    return () => { window.removeEventListener("rk-lms", paint); window.removeEventListener("storage", paint); };
  }, []);
  return null;
}

/** Cincin/bar progres untuk sekumpulan id pelajaran. */
export function TrackProgress({ ids, variant = "ring" }: { ids: string[]; variant?: "ring" | "bar" }) {
  const [d, setD] = useState(0);
  useEffect(() => {
    const f = () => { const s = load(); setD(ids.filter((i) => s.done[i]).length); };
    f();
    window.addEventListener("rk-lms", f);
    return () => window.removeEventListener("rk-lms", f);
  }, [ids]);
  const p = ids.length ? Math.round((d / ids.length) * 100) : 0;
  if (variant === "bar")
    return (
      <div className="bar" role="progressbar" aria-label="Progres jalur" aria-valuenow={p} aria-valuemin={0} aria-valuemax={100} style={{ ["--p" as string]: p }}>
        <i />
      </div>
    );
  return (
    <div className="ring" style={{ ["--p" as string]: p }} role="img" aria-label={`${d} dari ${ids.length} pelajaran selesai`}>
      <span>{p}%</span>
    </div>
  );
}
