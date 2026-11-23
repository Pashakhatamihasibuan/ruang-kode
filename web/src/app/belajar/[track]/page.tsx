import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { catalog, track, lessonHref, lessonCount, groupName, strip, clip, SITE_URL } from "@/lib/data";
import { DoneMarks, TrackProgress } from "@/components/ProgressMarks";
import { ResumeTrack } from "@/components/ResumeTrack";

export const dynamicParams = false;
export function generateStaticParams() {
  return catalog().tracks.map((t) => ({ track: t.k }));
}

type P = { params: Promise<{ track: string }> };

export async function generateMetadata({ params }: P): Promise<Metadata> {
  const t = track((await params).track);
  if (!t) return {};
  return {
    title: `${t.name}: ${t.h}`,
    description: clip(strip(`${t.h}. ${t.d}`)),
    alternates: { canonical: `/belajar/${t.k}` },
    openGraph: { title: `${t.name} · Ruang Kode`, url: `/belajar/${t.k}` },
  };
}

const KC: Record<string, string> = { c: "lilac", lab: "sky", topic: "mint", s: "butter", w: "peach", proj: "rose", see: "sky" };

export default async function TrackPage({ params }: P) {
  const t = track((await params).track);
  if (!t) notFound();
  const ids = t.mods.flatMap((m) => m.lessons.map((l) => (l.k === "see" ? l.srcId! : l.id)));
  const first = t.mods[0]?.lessons[0];
  const ld = {
    "@context": "https://schema.org", "@type": "Course", name: t.name, description: strip(t.d),
    provider: { "@type": "Organization", name: "Ruang Kode", sameAs: SITE_URL }, inLanguage: "id",
    isAccessibleForFree: true, url: `${SITE_URL}/belajar/${t.k}`,
    hasCourseInstance: { "@type": "CourseInstance", courseMode: "online", courseWorkload: `PT${Math.max(1, Math.round(lessonCount(t) * 0.4))}H` },
    offers: { "@type": "Offer", price: 0, priceCurrency: "IDR", category: "Free" },
  };
  return (
    <div className="wrap">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld).replace(/</g, "\\u003c") }} />
      <ol className="crumbs" aria-label="Lokasi">
        <li><Link href="/">Beranda</Link></li><li><Link href="/belajar">Materi</Link></li><li aria-current="page">{t.name}</li>
      </ol>
      <section className="card" style={{ ["--tc" as string]: t.c }} aria-labelledby="t-h">
        <div className="thead">
          <span className="blob lg" aria-hidden="true">{t.mark}</span>
          <div>
            <span className="eyebrow">{groupName(t.g)}</span>
            <h1 id="t-h">{t.name}</h1>
            <p>{t.h}</p>
          </div>
          <div className="tact"><TrackProgress ids={ids} /></div>
        </div>
        <p className="muted" style={{ marginTop: 16 }} dangerouslySetInnerHTML={{ __html: t.d }} />
        <div className="stats">
          <span className="chip lilac">{t.mods.length} modul</span>
          <span className="chip mint">{lessonCount(t)} pelajaran</span>
          <span className="chip peach">Gratis · tanpa akun</span>
        </div>
        <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginTop: 20 }}>
          {first && <ResumeTrack track={t.k} ids={ids} fallback={lessonHref(t, first)} />}
        </div>
      </section>
      <div className="mods">
        {t.mods.map((m, mi) => (
          <details className="card mod" key={mi} open={mi < 2}>
            <summary>
              <span className="n" aria-hidden="true">{mi + 1}</span>
              <div><h2>{m.t}</h2><p>{[m.lvl, `${m.lessons.length} pelajaran`].filter(Boolean).join(" · ")}{m.d ? ` · ${strip(m.d)}` : ""}</p></div>
              <span className="chev" aria-hidden="true">⌄</span>
            </summary>
            <ol className="lessons">
              {m.lessons.map((l, li) => (
                <li key={l.id}>
                  <Link href={lessonHref(t, l)} prefetch={false} data-lid={l.k === "see" ? l.srcId : l.id}>
                    <span className="dot" aria-hidden="true">{li + 1}</span>
                    <span className="ti">{l.title}{l.k === "see" && <small>dari jalur {l.srcName}</small>}</span>
                    <span className={`chip ${KC[l.k] ?? "lilac"}`}>{l.kind}</span>
                  </Link>
                </li>
              ))}
            </ol>
          </details>
        ))}
      </div>
      <DoneMarks />
    </div>
  );
}
