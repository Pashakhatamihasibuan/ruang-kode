import type { Metadata } from "next";
import { catalog, groupName, lessonCount } from "@/lib/data";
import { TrackCard } from "@/components/TrackCard";
import { CatalogFilter } from "@/components/CatalogFilter";
import { DoneMarks } from "@/components/ProgressMarks";

export const metadata: Metadata = {
  title: "Semua materi",
  description: "Katalog lengkap jalur belajar Ruang Kode: pemrograman, web dan frontend, data, desain, sistem informasi, dan alat kerja. Semua materi gratis dan berbahasa Indonesia.",
  alternates: { canonical: "/belajar" },
};

export default function Katalog() {
  const { tracks, groups } = catalog();
  const total = tracks.reduce((a, t) => a + lessonCount(t), 0);
  return (
    <div className="wrap">
      <ol className="crumbs" aria-label="Lokasi"><li><a href="/">Beranda</a></li><li aria-current="page">Materi</li></ol>
      <div className="card" style={{ marginBottom: 28 }}>
        <span className="eyebrow">Katalog</span>
        <h1>Semua materi</h1>
        <p className="muted" style={{ margin: 0 }}>{tracks.length} jalur · {total.toLocaleString("id-ID")} pelajaran. Pilih satu jalur, atau ikuti rute karier di beranda.</p>
      </div>
      <CatalogFilter groups={groups.map((g) => ({ k: g.k, t: groupName(g.k) }))} />
      {groups.map((g) => {
        const ts = tracks.filter((t) => t.g === g.k);
        if (!ts.length) return null;
        return (
          <section className="sec" key={g.k} data-group={g.k} aria-labelledby={`k-${g.k}`} style={{ marginTop: 32 }}>
            <h2 id={`k-${g.k}`}>{groupName(g.k)}</h2>
            <div className="grid g4">{ts.map((t) => <TrackCard key={t.k} t={t} />)}</div>
          </section>
        );
      })}
      <DoneMarks />
    </div>
  );
}
