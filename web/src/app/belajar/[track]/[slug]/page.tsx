import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import fs from "node:fs";
import path from "node:path";
import { catalog, track, bodies, flat, lessonHref, fixLinks, strip, clip, groupName, SITE_URL, type Body, type Track } from "@/lib/data";
import { Code, Out } from "@/components/Code";
import { Quiz } from "@/components/Quiz";
import { Runner } from "@/components/Runner";
import { Tracer } from "@/components/Tracer";
import { VizFrame } from "@/components/VizFrame";
import { WebLab } from "@/components/WebLab";
import { SqlConsole, SqlTasks } from "@/components/SqlLab";
import { DoneBar, SideToggle } from "@/components/LessonClient";
import { DoneMarks } from "@/components/ProgressMarks";

export const dynamicParams = false;
export function generateStaticParams() {
  return catalog().tracks.flatMap((t) => Object.keys(bodies(t.k)).map((slug) => ({ track: t.k, slug })));
}

type P = { params: Promise<{ track: string; slug: string }> };

function get(tk: string, slug: string) {
  const t = track(tk);
  const l = t ? bodies(t.k)[slug] : undefined;
  return t && l ? { t, l } : null;
}

export async function generateMetadata({ params }: P): Promise<Metadata> {
  const { track: tk, slug } = await params;
  const x = get(tk, slug);
  if (!x) return {};
  const lead = strip((x.l.b ?? []).join(" ") || x.l.brief || x.l.an || x.t.h);
  return {
    title: `${x.l.title} · ${x.t.name}`,
    description: clip(lead),
    alternates: { canonical: `/belajar/${tk}/${slug}` },
    openGraph: { type: "article", title: x.l.title, url: `/belajar/${tk}/${slug}`, description: clip(lead) },
  };
}

const KIT = JSON.parse(fs.readFileSync(path.join(process.cwd(), "src", "data", "kit.json"), "utf8")) as Record<string, { j: string; b: string; g: string; u: string; kb: number; pf: string }>;
const H = ({ html, as: Tag = "p", className }: { html: string; as?: "p" | "div" | "span" | "li" | "h3"; className?: string }) => (
  <Tag className={className} dangerouslySetInnerHTML={{ __html: fixLinks(html) }} />
);

function Section({ id, ic, bg, title, children, className = "" }: { id: string; ic: string; bg: string; title: string; children: React.ReactNode; className?: string }) {
  return (
    <section className={`card section ${className}`} id={id} aria-labelledby={`${id}-h`}>
      <h2 id={`${id}-h`}><span className="ic" style={{ background: bg }} aria-hidden="true">{ic}</span>{title}</h2>
      {children}
    </section>
  );
}

function Tables({ tb }: { tb: NonNullable<Body["tb"]> }) {
  return (
    <>
      {tb.map((x, i) => (
        <div className="tw" key={i}>
          <table>
            <caption>{x.c}</caption>
            <thead><tr>{x.h.map((c, j) => <th key={j} scope="col">{c}</th>)}</tr></thead>
            <tbody>{x.r.map((r, j) => <tr key={j}>{r.map((c, k) => <td key={k} dangerouslySetInnerHTML={{ __html: String(c) }} />)}</tr>)}</tbody>
          </table>
        </div>
      ))}
    </>
  );
}

async function Files({ files }: { files: [string, string, string][] }) {
  return (
    <div>
      {files.map(([name, lang, code], i) => (
        <details className="fold" key={i} open={i === 0}>
          <summary>{name}</summary>
          <div className="in"><Code code={code} lang={lang} label={name} /></div>
        </details>
      ))}
    </div>
  );
}

function Sidebar({ t, l }: { t: Track; l: Body }) {
  const m = t.mods[l.mi];
  return (
    <nav className="clay side" id="side" aria-label={`Daftar pelajaran ${t.name}`}>
      <span className="eyebrow">Modul {l.mi + 1} dari {t.mods.length}</span>
      <h2>{m.t}</h2>
      <ol>
        {m.lessons.map((x, i) => (
          <li key={x.id}>
            <Link href={lessonHref(t, x)} prefetch={false} data-lid={x.k === "see" ? x.srcId : x.id} aria-current={x.id === l.id ? "page" : undefined}>
              <span className="dot" aria-hidden="true">{i + 1}</span><span>{x.title}</span>
            </Link>
          </li>
        ))}
      </ol>
      <div className="mods-mini">
        <span className="eyebrow">Modul lain</span>
        <ol>
          {t.mods.map((mm, mi) => mi !== l.mi && mm.lessons[0] && (
            <li key={mi}><Link href={lessonHref(t, mm.lessons[0])} prefetch={false}><span className="dot" aria-hidden="true">{mi + 1}</span><span>{mm.t}</span></Link></li>
          ))}
        </ol>
      </div>
    </nav>
  );
}

export default async function LessonPage({ params }: P) {
  const { track: tk, slug } = await params;
  const x = get(tk, slug);
  if (!x) notFound();
  const { t, l } = x;
  const lang = l.lang || t.lang;
  const F = flat(t);
  const pos = F.findIndex((f) => f.l.id === l.id);
  const prev = F[pos - 1], next = F[pos + 1];
  const mod = t.mods[l.mi];
  const tasks = l.tasks ?? (l.task ? [l.task] : []);
  const isLastInMod = l.li === mod.lessons.length - 1;
  const vizLesson = l.viz ? { fc: l.fc, vq: l.vq, vj: l.vj, t: l.title } : {};
  const ld = {
    "@context": "https://schema.org", "@type": "LearningResource", name: l.title, inLanguage: "id", isAccessibleForFree: true,
    learningResourceType: "Pelajaran", educationalLevel: mod.lvl || undefined, url: `${SITE_URL}/belajar/${tk}/${slug}`,
    isPartOf: { "@type": "Course", name: t.name, url: `${SITE_URL}/belajar/${t.k}` },
    provider: { "@type": "Organization", name: "Ruang Kode", url: SITE_URL },
  };
  const crumbs = {
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    itemListElement: [["Materi", "/belajar"], [t.name, `/belajar/${t.k}`], [l.title, `/belajar/${tk}/${slug}`]].map(([n, u], i) => ({ "@type": "ListItem", position: i + 1, name: n, item: SITE_URL + u })),
  };
  const kindChip = ({ c: "Konsep & kode", w: "Praktik web", s: "Praktik SQL", lab: "Konsep & lab", topic: "Topik 5 langkah", proj: "Proyek", see: "" } as Record<string, string>)[l.k];

  return (
    <div className="wrap" style={{ ["--tc" as string]: t.c }}>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify([ld, crumbs]).replace(/</g, "\\u003c") }} />
      <ol className="crumbs" aria-label="Lokasi">
        <li><Link href="/belajar">Materi</Link></li>
        <li><Link href={`/belajar/${t.k}`}>{t.name}</Link></li>
        <li aria-current="page">Modul {l.mi + 1}</li>
      </ol>
      <div className="lesson">
        <Sidebar t={t} l={l} />
        <article className="lmain" aria-labelledby="l-h">
          <header className="card lhead">
            <div className="meta">
              <span className="blob" aria-hidden="true" style={{ width: 40, height: 40, borderRadius: "50%", fontSize: "0.75rem" }}>{t.mark}</span>
              <span className="chip lilac">{t.name}</span>
              {mod.lvl && <span className="chip mint">{mod.lvl}</span>}
              <span className="chip peach">{kindChip}</span>
              <SideToggle />
            </div>
            <h1 id="l-h">{l.title}</h1>
            <p className="muted" style={{ margin: 0 }}>Modul {l.mi + 1} · {mod.t} · pelajaran {l.li + 1} dari {mod.lessons.length} · {groupName(t.g)}</p>
          </header>

          <div className="body">
            {(l.an || (l.nodes && l.nodes.length > 0)) && (
              <section className="card analogy" aria-labelledby="an-h">
                <span className="eyebrow" id="an-h">Sekilas</span>
                {l.an && <p>{l.an}</p>}
                {l.nodes && l.nodes.length > 0 && (
                  <div className="nodes" aria-label="Topik yang dibahas">{l.nodes.map((n, i) => <span className="chip" key={i} style={{ background: "var(--surface-2)" }}>{n}</span>)}</div>
                )}
              </section>
            )}

            {l.k === "proj" ? (
              <>
                <Section id="brief" ic="◎" bg="var(--peach)" title="Ringkasan proyek">
                  <div className="prose">
                    {l.brief && <H html={l.brief} />}
                    {l.stack && <p><b>Teknologi:</b> {l.stack}</p>}
                  </div>
                </Section>
                {l.feats && <Section id="fitur" ic="★" bg="var(--mint)" title="Fitur yang dibuat"><ul className="prose">{l.feats.map((f, i) => <H key={i} as="li" html={f} />)}</ul></Section>}
                {l.steps && <Section id="langkah" ic="➜" bg="var(--sky)" title="Langkah kerja"><ol className="prose">{l.steps.map((s, i) => <H key={i} as="li" html={s} />)}</ol></Section>}
                {l.files && (
                  <Section id="berkas" ic="▤" bg="var(--lilac)" title="Kode proyek">
                    <Files files={l.files} />
                    {l.sql && l.files[l.sql.file] && (
                      <div style={{ marginTop: 18 }}>
                        <span className="eyebrow">Coba jalankan query proyek</span>
                        <SqlConsole db={l.sql.db} initial={l.files[l.sql.file][2]} />
                      </div>
                    )}
                  </Section>
                )}
              </>
            ) : (
              l.b && l.b.length > 0 && (
                <Section id="materi" ic="✎" bg="var(--lilac)" title="Materi">
                  <div className="prose">{l.b.map((p, i) => <H key={i} html={p} />)}</div>
                </Section>
              )
            )}

            {l.trs && (
              <Section id="terjemah" ic="⇄" bg="var(--mint)" title="Dari kalimat ke kode">
                <div className="tw"><table><thead><tr><th scope="col">Maksud</th><th scope="col">Kode</th></tr></thead>
                  <tbody>{l.trs.map((r, i) => <tr key={i}><td>{r[0]}</td><td><code>{r[1]}</code></td></tr>)}</tbody></table></div>
              </Section>
            )}

            {l.viz && (
              <Section id="visual" ic="◐" bg="var(--sky)" title="Visual interaktif">
                <p className="muted small">Coba kontrolnya, lalu perhatikan apa yang berubah.</p>
                <VizFrame viz={l.viz} lang={lang} lesson={vizLesson} title={l.title} />
              </Section>
            )}

            {l.tb && l.tb.length > 0 && (
              <Section id="tabel" ic="▦" bg="var(--butter)" title={l.title.startsWith("Studi kasus") ? "Langkah studi kasus" : "Ringkasan dalam tabel"}>
                <div style={{ display: "grid", gap: 16 }}><Tables tb={l.tb} /></div>
              </Section>
            )}

            {l.code && l.k !== "w" && (
              <Section id="kode" ic="{ }" bg="var(--mint)" title="Contoh kode">
                {l.out != null || l.fig ? (
                  <Runner code={l.code} out={l.out ?? null} fig={l.fig} lang={lang}>
                    <Code code={l.code} lang={lang} />
                  </Runner>
                ) : <Code code={l.code} lang={lang} />}
                {l.trc && <div style={{ marginTop: 14 }}><Tracer code={l.code} trace={l.trc.s} cut={l.trc.cut} /></div>}
              </Section>
            )}

            {l.k !== "w" && (["html", "css", "js"] as const).some((k) => l[k]) && (
              <Section id="kode-web" ic="</>" bg="var(--peach)" title="Kode">
                <div style={{ display: "grid", gap: 14 }}>
                  {(["html", "css", "js"] as const).map((k) => l[k] && <Code key={k} code={l[k]!} lang={k === "js" && l.react ? "jsx" : k} />)}
                </div>
              </Section>
            )}

            {l.k === "w" && (
              <Section id="lab" ic="▶" bg="var(--peach)" title="Coba langsung">
                <WebLab init={{ html: l.html, css: l.css, js: l.js }} react={l.react} tw={l.tw} bs={l.bs} showConsole={l.console} task={l.task} lid={l.id} track={t.k} />
              </Section>
            )}

            {l.k === "s" && (
              <>
                <Section id="konsol" ic="⌗" bg="var(--butter)" title="Konsol SQL">
                  <SqlConsole db={l.db} examples={l.ex ?? []} />
                </Section>
                {tasks.length > 0 && (
                  <Section id="tantangan" ic="✓" bg="var(--mint)" title="Tantangan · diperiksa otomatis">
                    <SqlTasks tasks={tasks} db={l.db} lid={l.id} track={t.k} />
                  </Section>
                )}
              </>
            )}
            {l.k !== "s" && l.k !== "w" && l.ex && l.ex.length > 0 && (
              <Section id="contoh" ic="⌗" bg="var(--butter)" title="Contoh query">
                <div style={{ display: "grid", gap: 14 }}>{l.ex.map(([lbl, s], i) => <Code key={i} code={s} lang="sql" label={lbl} />)}</div>
              </Section>
            )}

            {l.syn && (
              <Section id="banding" ic="⇆" bg="var(--sky)" title="Sebagai perbandingan">
                <Code code={l.syn[1]} lang={/mongo|js/i.test(l.syn[0]) ? "js" : "text"} label={l.syn[0]} />
              </Section>
            )}

            {l.bug && (
              <Section id="bug" ic="🐞" bg="var(--rose)" title="Cari bugnya">
                <p className="muted">Kode di bawah gagal dijalankan. Temukan kesalahannya sebelum membuka jawaban.</p>
                <Code code={l.bug.code} lang={lang} label="Kode yang bermasalah" />
                <details className="fold" style={{ marginTop: 12 }}>
                  <summary>Lihat pesan error dan penjelasannya</summary>
                  <div className="in">
                    <pre className="out err">{l.bug.err}{l.bug.line ? `\n(baris ${l.bug.line})` : ""}</pre>
                    <H html={l.bug.why} />
                  </div>
                </details>
              </Section>
            )}

            {l.deep && (l.deep.cx.length > 0 || l.deep.ist.length > 0) && (
              <Section id="dalam" ic="⚲" bg="var(--lilac)" title="Pendalaman: istilah dan kasus nyata">
                {l.deep.ist.length > 0 && (
                  <div className="tw" style={{ marginBottom: 18 }}>
                    <table><caption>Istilah penting</caption><thead><tr><th scope="col">Istilah</th><th scope="col">Artinya</th></tr></thead>
                      <tbody>{l.deep.ist.map(([a, b], i) => <tr key={i}><td><b>{a}</b></td><td>{b}</td></tr>)}</tbody></table>
                  </div>
                )}
                {l.deep.cx.map((c, i) => (
                  <details className="fold" key={i} open={i === 0}>
                    <summary>Kasus {i + 1}: {c.t}</summary>
                    <div className="in">
                      {c.b && <H html={c.b} />}
                      <Code code={c.code} lang={c.lang ?? lang} />
                      {c.out && <Out text={c.out} />}
                    </div>
                  </details>
                ))}
              </Section>
            )}

            {l.so && l.so.length > 0 && (
              <Section id="soal" ic="✍" bg="var(--peach)" title="Soal latihan">
                <p className="muted">Kerjakan dulu di editor atau kertasmu sendiri. Buka petunjuk jika buntu, dan buka jawaban hanya untuk mencocokkan.</p>
                <ol className="so">
                  {l.so.map((s, i) => (
                    <li key={i}>
                      <H html={s.q} />
                      <details><summary>Petunjuk</summary><H html={s.h} /></details>
                      {s.a && (
                        <details>
                          <summary>Lihat jawaban</summary>
                          <div style={{ display: "grid", gap: 10, marginTop: 10 }}>
                            <Code code={s.a} lang={s.lang ?? lang} label="Jawaban" />
                            {s.out != null && <Out text={s.out} />}
                          </div>
                        </details>
                      )}
                    </li>
                  ))}
                </ol>
              </Section>
            )}

            {l.pro && l.pro.length > 0 && (
              <Section id="rapi" ic="✦" bg="var(--mint)" title="Kode pemula vs kode rapi">
                {l.pro.map((p, i) => (
                  <details className="fold" key={i}>
                    <summary>{p.t}{p.tag && <span className="chip mint" style={{ marginLeft: "auto" }}>{p.tag}</span>}</summary>
                    <div className="in">
                      <H html={p.why} />
                      <Code code={p.a} lang={p.lang ?? lang} label="Kode pemula" />
                      <Code code={p.b} lang={p.lang ?? lang} label="Kode rapi (best practice)" />
                      {p.out && <Out text={p.out} label="Keluaran keduanya" />}
                    </div>
                  </details>
                ))}
              </Section>
            )}

            {l.fin && (
              <section className="card section final" id="final" aria-labelledby="final-h">
                <h2 id="final-h"><span className="ic" style={{ background: "var(--surface-2)" }} aria-hidden="true">🔒</span>Kode final standar industri</h2>
                <p>Coba kerjakan sendiri dulu. Setelah itu, buka penyelesaian lengkap untuk membandingkan.</p>
                <details className="fold">
                  <summary>Tampilkan kode final</summary>
                  <div className="in">
                    <H html={l.fin.n} />
                    <Code code={l.fin.tree} lang="text" label="Struktur folder" />
                    <Files files={l.fin.files} />
                    <Code code={l.fin.run} lang="bash" label="Cara menjalankan" />
                    {l.fin.cek?.length > 0 && (
                      <div>
                        <span className="eyebrow">Checklist pembanding</span>
                        <ul className="prose">{l.fin.cek.map((c, i) => <H key={i} as="li" html={c} />)}</ul>
                      </div>
                    )}
                  </div>
                </details>
              </section>
            )}

            {l.dl ? (
              <Section id="unduh" ic="⬇" bg="var(--sky)" title="Unduh desain untuk Figma">
                <div className="grid g3">
                  {l.dl.map((d) => KIT[d.k] && (
                    <div className="card" key={d.k + d.p} style={{ background: "var(--surface-2)" }}>
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      <img src={`/desain/thumb/${d.p}.webp`} alt={`Pratinjau desain ${KIT[d.k].j}`} loading="lazy" style={{ borderRadius: 0, aspectRatio: "4/3", objectFit: "cover", width: "100%" }} />
                      <h3 style={{ marginTop: 12 }}>{KIT[d.k].j}</h3>
                      <p className="small muted">{KIT[d.k].b} · {KIT[d.k].g}</p>
                      <a className="btn primary sm" href={`/desain/${d.k}.zip`} download>⬇ Unduh ZIP · {Math.round(KIT[d.k].kb)} KB</a>
                    </div>
                  ))}
                </div>
              </Section>
            ) : null}

            {l.hp && (
              <Section id="layar" ic="▯" bg="var(--mint)" title={l.hp.c}>
                <H html={l.hp.n} />
                <div className="grid g3">
                  {l.hp.s.map((x, i) => (
                    <figure key={i} style={{ margin: 0 }}>
                      <iframe srcDoc={x.d} sandbox="" title={x.t} loading="lazy" style={{ width: "100%", height: 560, border: 0, borderRadius: 0, boxShadow: "var(--clay-sm)", background: "#fff" }} />
                      <figcaption className="small muted" style={{ textAlign: "center", marginTop: 8 }}>{x.t}</figcaption>
                    </figure>
                  ))}
                </div>
              </Section>
            )}

            {l.pts && l.pts.length > 0 && (
              <Section id="poin" ic="★" bg="var(--butter)" title="Poin penting">
                <ul className="prose">{l.pts.map((p, i) => <H key={i} as="li" html={p} />)}</ul>
              </Section>
            )}

            {l.q && l.q.length > 0 && (
              <Section id="kuis" ic="?" bg="var(--rose)" title="Cek pemahaman">
                <Quiz items={l.q} lid={l.id} />
              </Section>
            )}

            <DoneBar lid={l.id} track={t.k} last={isLastInMod} />

            <nav className="pn" aria-label="Pelajaran sebelum dan sesudah">
              {prev ? <Link className="card" href={prev.href}><small>← Sebelumnya</small><b>{prev.l.title}</b></Link> : <span />}
              {next ? <Link className="card nx" href={next.href}><small>Berikutnya →</small><b>{next.l.title}</b></Link>
                : <Link className="card nx" href={`/belajar/${t.k}`}><small>Selesai →</small><b>Kembali ke jalur {t.name}</b></Link>}
            </nav>
          </div>
        </article>
      </div>
      <DoneMarks />
    </div>
  );
}
