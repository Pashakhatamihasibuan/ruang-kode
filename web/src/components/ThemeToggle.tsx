"use client";
import { useEffect, useState } from "react";

type T = "auto" | "light" | "dark";
const NEXT: Record<T, T> = { auto: "light", light: "dark", dark: "auto" };
const LBL: Record<T, string> = { auto: "Tema: ikuti perangkat", light: "Tema: terang", dark: "Tema: gelap" };
const IC: Record<T, React.ReactNode> = {
  auto: <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" strokeWidth="2" /><path d="M12 4a8 8 0 0 1 0 16z" fill="currentColor" /></svg>,
  light: <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="12" cy="12" r="4.5" fill="currentColor" /><g stroke="currentColor" strokeWidth="2" strokeLinecap="round"><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8" /></g></svg>,
  dark: <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z" fill="currentColor" /></svg>,
};

export function ThemeToggle() {
  const [t, setT] = useState<T>("auto");
  useEffect(() => {
    try {
      const v = JSON.parse(localStorage.getItem("rk-theme") || '"auto"');
      if (v === "light" || v === "dark") setT(v);
    } catch {}
  }, []);
  const change = () => {
    const n = NEXT[t];
    setT(n);
    try { localStorage.setItem("rk-theme", JSON.stringify(n)); } catch {}
    const r = document.documentElement;
    if (n === "auto") delete r.dataset.theme; else r.dataset.theme = n;
  };
  return (
    <button type="button" className="btn icon-btn" onClick={change} aria-label={`${LBL[t]}. Ganti tema`} title={LBL[t]}>
      {IC[t]}
    </button>
  );
}
