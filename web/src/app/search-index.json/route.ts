import { catalog, glossary, lessonHref } from "@/lib/data";

export const dynamic = "force-static";

export function GET() {
  const rows: [string, string, string, string][] = [];
  for (const t of catalog().tracks) {
    rows.push([t.name, `/belajar/${t.k}`, t.h, "Jalur"]);
    t.mods.forEach((m) => m.lessons.forEach((l) => {
      if (l.k !== "see") rows.push([l.title, lessonHref(t, l), `${t.name} · ${m.t}`, l.kind]);
    }));
  }
  for (const g of glossary().items) rows.push([g.t, `/glosarium#${g.id}`, g.en || g.c, "Istilah"]);
  return Response.json(rows);
}
