import Link from "next/link";
import type { Track } from "@/lib/data";
import { lessonCount } from "@/lib/data";
import { TrackProgress } from "./ProgressMarks";

export function TrackCard({ t, groupName }: { t: Track; groupName?: string }) {
  const ids = t.mods.flatMap((m) => m.lessons.map((l) => (l.k === "see" ? l.srcId! : l.id)));
  return (
    <Link href={`/belajar/${t.k}`} className="card tcard" prefetch={false} data-g={t.g} data-name={`${t.name} ${t.h}`.toLowerCase()}
      style={{ ["--tc" as string]: t.c }}>
      <div className="hd">
        <span className="blob" aria-hidden="true">{t.mark}</span>
        <div>
          <h3>{t.name}</h3>
          {groupName && <span className="small muted">{groupName}</span>}
        </div>
      </div>
      <p>{t.h}</p>
      <div className="meta"><span>{t.mods.length} modul</span><span aria-hidden="true">·</span><span>{lessonCount(t)} pelajaran</span></div>
      <TrackProgress ids={ids} variant="bar" />
    </Link>
  );
}
