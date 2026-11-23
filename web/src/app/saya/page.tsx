import type { Metadata } from "next";
import { catalog } from "@/lib/data";
import { MyProgress } from "@/components/MyProgress";

export const metadata: Metadata = {
  title: "Progres saya",
  description: "Lihat jalur yang sedang kamu pelajari, pelajaran yang sudah selesai, XP, dan hari beruntun belajar. Progres tersimpan hanya di browser ini.",
  alternates: { canonical: "/saya" },
  robots: { index: false, follow: true },
};

export default function Saya() {
  const tracks = catalog().tracks.map((t) => ({
    k: t.k, name: t.name, mark: t.mark, c: t.c,
    ids: t.mods.flatMap((m) => m.lessons.map((l) => (l.k === "see" ? l.srcId! : l.id))),
  }));
  return (
    <div className="wrap">
      <ol className="crumbs" aria-label="Lokasi"><li><a href="/">Beranda</a></li><li aria-current="page">Progres saya</li></ol>
      <h1>Progres saya</h1>
      <MyProgress tracks={tracks} />
    </div>
  );
}
