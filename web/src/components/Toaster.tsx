"use client";
import { useEffect, useState } from "react";

export function Toaster() {
  const [msg, setMsg] = useState("");
  const [on, setOn] = useState(false);
  useEffect(() => {
    let h: ReturnType<typeof setTimeout>;
    const f = (e: Event) => {
      setMsg((e as CustomEvent<string>).detail);
      setOn(true);
      clearTimeout(h);
      h = setTimeout(() => setOn(false), 2600);
    };
    window.addEventListener("rk-toast", f);
    return () => window.removeEventListener("rk-toast", f);
  }, []);
  return <div className={`toast${on ? " on" : ""}`} role="status" aria-live="polite">{msg}</div>;
}
