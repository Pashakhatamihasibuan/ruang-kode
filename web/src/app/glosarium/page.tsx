import type { Metadata } from "next";
import { glossary } from "@/lib/data";
import { GlossaryFilter } from "@/components/GlossaryFilter";

export const metadata: Metadata = {
  title: "Glosarium istilah pemrograman, data, dan desain",
  description: "Kamus istilah pemrograman, basis data, web, data dan BI, desain, serta sistem informasi dalam bahasa Indonesia, lengkap dengan padanan bahasa Inggris dan contoh.",
  alternates: { canonical: "/glosarium" },
};

export default function Glosarium() {
  const { cats, items } = glossary();
  return (
    <div className="wrap">
      <ol className="crumbs" aria-label="Lokasi"><li><a href="/">Beranda</a></li><li aria-current="page">Glosarium</li></ol>
      <div className="card" style={{ marginBottom: 24 }}>
        <span className="eyebrow">{items.length} istilah</span>
        <h1>Glosarium</h1>
        <p className="muted" style={{ margin: 0 }}>Istilah yang sering muncul di materi, dijelaskan dengan bahasa sehari-hari.</p>
      </div>
      <GlossaryFilter cats={cats} />
      {cats.map((c) => {
        const xs = items.filter((g) => g.c === c);
        if (!xs.length) return null;
        return (
          <section key={c} data-gcat={c} className="sec" style={{ marginTop: 32 }} aria-labelledby={`c-${c.replace(/\W+/g, "-")}`}>
            <h2 id={`c-${c.replace(/\W+/g, "-")}`}>{c}</h2>
            <div className="gl-list">
              {xs.map((g) => (
                <article className="card gl-item" id={g.id} key={g.id} data-gname={`${g.t} ${g.en ?? ""} ${g.d}`.toLowerCase()}>
                  <h3>{g.t}</h3>
                  {g.en && <span className="en" lang="en">{g.en}</span>}
                  <p>{g.d}</p>
                  {g.ex && <code>{g.ex}</code>}
                </article>
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}
