"use client";
import { useEffect, useState } from "react";
import { load, markDone, unmark, visit, toast } from "@/lib/progress";

export function DoneBar({ lid, track, last }: { lid: string; track: string; last: boolean }) {
  const [done, setDone] = useState(false);
  useEffect(() => {
    visit(lid, track);
    const f = () => setDone(!!load().done[lid]);
    f();
    window.addEventListener("rk-lms", f);
    return () => window.removeEventListener("rk-lms", f);
  }, [lid, track]);
  return (
    <div className="card donebar">
      <div>
        <b>{done ? "Pelajaran ini sudah selesai." : "Sudah paham materi ini?"}</b>
        <p className="small muted" style={{ margin: 0 }}>{done ? "Progresmu tersimpan di browser ini." : last ? "Tandai selesai untuk menuntaskan modul ini." : "Tandai selesai, lalu lanjut ke pelajaran berikutnya."}</p>
      </div>
      {done
        ? <button type="button" className="btn" onClick={() => unmark(lid)}>Batalkan tanda selesai</button>
        : <button type="button" className="btn ok" onClick={() => { if (markDone(lid, track)) toast("+10 XP · Pelajaran selesai"); }}>✓ Tandai selesai</button>}
    </div>
  );
}

export function SideToggle() {
  const [open, setOpen] = useState(false);
  useEffect(() => { document.getElementById("side")?.classList.toggle("open", open); }, [open]);
  useEffect(() => {
    // gulir daftar materi (bukan halaman) agar sub materi yang sedang dibuka terlihat
    const side = document.getElementById("side"), cur = side?.querySelector<HTMLElement>('[aria-current="page"]');
    if (side && cur && side.scrollHeight > side.clientHeight) side.scrollTop = cur.offsetTop - side.clientHeight / 3;
  }, []);
  return (
    <button type="button" className="btn sm side-toggle" aria-expanded={open} aria-controls="side" onClick={() => setOpen(!open)}>
      ☰ {open ? "Tutup daftar pelajaran" : "Daftar pelajaran"}
    </button>
  );
}
