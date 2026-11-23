"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { load } from "@/lib/progress";

export function ResumeTrack({ track, ids, fallback }: { track: string; ids: string[]; fallback: string }) {
  const [st, setSt] = useState<{ u: string; label: string }>({ u: fallback, label: "Mulai dari pelajaran pertama" });
  useEffect(() => {
    const s = load();
    const d = ids.filter((i) => s.done[i]).length;
    if (!d && !s.last[track]) return;
    const next = ids.find((i) => !s.done[i]);
    const target = s.last[track] && !s.done[s.last[track]] ? s.last[track] : next;
    if (!target) { setSt({ u: fallback, label: "Jalur selesai · ulangi dari awal" }); return; }
    fetch("/ids.json").then((r) => r.json()).then((m: Record<string, [string, string]>) => {
      if (m[target]) setSt({ u: m[target][0], label: `Lanjutkan: ${m[target][1]}` });
    }).catch(() => {});
  }, [track, ids, fallback]);
  return <Link className="btn primary" href={st.u}>{st.label}</Link>;
}
