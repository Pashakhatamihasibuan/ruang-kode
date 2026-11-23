import { catalog, lessonHref } from "@/lib/data";

export const dynamic = "force-static";

/** id pelajaran -> [url, judul]; dipakai tombol Lanjutkan, halaman progres, dan tautan lama. */
export function GET() {
  const m: Record<string, [string, string]> = {};
  for (const t of catalog().tracks) {
    m[t.k] = [`/belajar/${t.k}`, t.name];
    t.mods.forEach((mod) => mod.lessons.forEach((l) => { if (l.k !== "see") m[l.id] = [lessonHref(t, l), l.title]; }));
  }
  return Response.json(m);
}
