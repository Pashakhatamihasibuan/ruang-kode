import Link from "next/link";
import { catalog, groupName, lessonCount } from "@/lib/data";
import { TrackCard } from "@/components/TrackCard";
import { Resume, LegacyHash } from "@/components/Home";

const FEATS = [
  { ic: "▶", c: "var(--mint)", t: "Kode langsung jalan", d: "Python berjalan di browser, konsol SQL dengan database contoh, dan editor HTML/CSS/JS dengan pratinjau langsung." },
  { ic: "◎", c: "var(--peach)", t: "Studi kasus industri", d: "Setiap materi ditutup dengan kasus nyata: masalah bisnis, data, langkah kerja, dan keputusan yang bisa dipertanggungjawabkan." },
  { ic: "▣", c: "var(--sky)", t: "Proyek portofolio di tiap jalur", d: "6 proyek mini dan 4 proyek besar langsung di dalam jalur, lengkap dengan kode final standar industri yang bisa dibuka setelah mencoba." },
  { ic: "✓", c: "var(--lilac)", t: "Kuis dan latihan bertahap", d: "Soal latihan dengan petunjuk, kunci jawaban tersembunyi, kuis di akhir pelajaran, dan progres yang tersimpan otomatis." },
  { ic: "◔", c: "var(--butter)", t: "Belajar dengan ritme sendiri", d: "Semua materi terbuka, tanpa akun. Progres disimpan hanya di perangkatmu dan bisa dilanjutkan kapan saja." },
  { ic: "⚿", c: "var(--rose)", t: "Aman sejak rancangan", d: "Kode yang kamu jalankan diisolasi di sandbox terpisah, halaman dilindungi Content Security Policy, dan tidak ada pelacak." },
];

export default function Home() {
  const { tracks, paths, groups } = catalog();
  const total = tracks.reduce((a, t) => a + lessonCount(t), 0);
  const byK = Object.fromEntries(tracks.map((t) => [t.k, t]));
  return (
    <div className="wrap">
      <LegacyHash />
      <section className="hero" aria-labelledby="hero-h">
        <div className="card">
          <span className="eyebrow">Akademi berbahasa Indonesia</span>
          <h1 id="hero-h">Belajar coding, data, dan desain sampai <em>siap kerja</em>.</h1>
          <p className="lead">{tracks.length} jalur belajar yang disusun bertahap dari nol, dengan studi kasus industri, proyek portofolio, dan latihan yang langsung bisa dicoba di browser.</p>
          <div className="acts">
            <Link className="btn primary" href="/belajar">Pilih jalur belajar</Link>
            <Resume />
          </div>
        </div>
        <div className="hero-art" aria-label="Ringkasan isi">
          <div className="tile" style={{ background: "var(--lilac)" }}><b>{tracks.length}</b><span>jalur belajar</span></div>
          <div className="tile" style={{ background: "var(--mint)" }}><b>{total.toLocaleString("id-ID")}</b><span>pelajaran</span></div>
          <div className="tile" style={{ background: "var(--peach)" }}><b>{paths.length}</b><span>rute karier</span></div>
          <div className="tile" style={{ background: "var(--sky)" }}><b>0</b><span>biaya dan iklan</span></div>
        </div>
      </section>

      <section className="sec" aria-labelledby="rute-h">
        <div className="sec-h">
          <div><span className="eyebrow">Rute karier</span><h2 id="rute-h">Mau jadi apa?</h2></div>
          <p>Ikuti urutan jalur yang biasa diminta perekrut untuk peran ini.</p>
        </div>
        <div className="grid g3">
          {paths.map((p) => (
            <div className="card path" key={p.k}>
              <h3>{p.t}</h3>
              <p className="muted" style={{ margin: 0 }}>{p.d}</p>
              <ol aria-label={`Urutan jalur ${p.t}`}>
                {p.tr.filter((k) => byK[k]).map((k, i) => (
                  <li key={k}><Link href={`/belajar/${k}`} prefetch={false}>{i + 1}. {byK[k].name}</Link></li>
                ))}
              </ol>
            </div>
          ))}
        </div>
      </section>

      <section className="sec" aria-labelledby="fitur-h">
        <div className="sec-h"><div><span className="eyebrow">Cara belajar</span><h2 id="fitur-h">Dibuat supaya kamu benar-benar bisa</h2></div></div>
        <div className="grid g3">
          {FEATS.map((f) => (
            <div className="card feat" key={f.t}>
              <div className="ic" style={{ background: f.c }} aria-hidden="true">{f.ic}</div>
              <h3>{f.t}</h3>
              <p>{f.d}</p>
            </div>
          ))}
        </div>
      </section>

      {groups.map((g) => {
        const ts = tracks.filter((t) => t.g === g.k);
        if (!ts.length) return null;
        return (
          <section className="sec" key={g.k} aria-labelledby={`g-${g.k}`}>
            <div className="sec-h"><div><span className="eyebrow">{ts.length} jalur</span><h2 id={`g-${g.k}`}>{groupName(g.k)}</h2></div></div>
            <div className="grid g4">{ts.map((t) => <TrackCard key={t.k} t={t} />)}</div>
          </section>
        );
      })}
    </div>
  );
}
