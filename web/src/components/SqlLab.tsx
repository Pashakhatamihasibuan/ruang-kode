"use client";
import { useMemo, useRef, useState } from "react";
import { SQLE, SEED, type SqlResult } from "@/lib/sqle";
import type { Task } from "@/lib/data";
import { award, markDone, toast } from "@/lib/progress";

/* Konsol SQL memakai mesin SQL Ruang Kode yang berjalan di browser (tanpa server, tanpa eval). */

function Result({ r }: { r: SqlResult[] }) {
  return (
    <div className="stack" style={{ display: "grid", gap: 10 }}>
      {r.map((x, i) => x.kind === "rows" ? (
        <div className="res" key={i}>
          <table>
            <thead><tr>{x.cols.map((c, j) => <th key={j} scope="col">{c}</th>)}</tr></thead>
            <tbody>{x.rows.slice(0, 200).map((row, j) => <tr key={j}>{row.map((v, k) => <td key={k}>{v == null ? "NULL" : SQLE.fmt(v)}</td>)}</tr>)}</tbody>
          </table>
          <p className="small muted" style={{ margin: "6px 12px" }}>{x.rows.length} baris{x.rows.length > 200 ? " (200 pertama ditampilkan)" : ""}</p>
        </div>
      ) : <p key={i} className="msg ok">✓ {x.msg}</p>)}
    </div>
  );
}

const errMsg = (e: unknown) => {
  const x = e as { message?: string; hint?: string };
  return `${x.message ?? String(e)}${x.hint ? ` ${x.hint}` : ""}`;
};

function grade(task: Task, sql: string, seed: string): { ok: boolean; msg: string; r?: SqlResult[] } {
  if (!sql.trim()) return { ok: false, msg: "Tulis dulu query-mu." };
  const fin = (s: string) => { const db = SQLE.create(seed); const r = SQLE.exec(db, s); return task.check ? SQLE.exec(db, task.check).pop()! : r[r.length - 1]; };
  let exp: SqlResult, got: SqlResult;
  try { exp = fin(task.a!); } catch { return { ok: false, msg: "Kunci jawaban gagal dijalankan." }; }
  try { got = fin(sql); } catch (e) { return { ok: false, msg: `Query-mu menghasilkan error: ${errMsg(e)}` }; }
  if (got.kind !== "rows" || exp.kind !== "rows") return { ok: false, msg: "Perintah terakhirmu tidak menghasilkan tabel. Tantangan ini meminta hasil berupa baris data." };
  const K = (r: unknown[]) => r.map((v) => (v == null ? "∅" : SQLE.fmt(v))).join("\u0001");
  if (got.cols.length !== exp.cols.length) return { ok: false, msg: `Hasilmu punya ${got.cols.length} kolom, yang diminta ${exp.cols.length} kolom.`, r: [got] };
  if (got.rows.length !== exp.rows.length) return { ok: false, msg: `Hasilmu ${got.rows.length} baris, seharusnya ${exp.rows.length} baris. Periksa lagi WHERE, JOIN, atau GROUP BY.`, r: [got] };
  const A = got.rows.map(K), B = exp.rows.map(K);
  const same = [...A].sort().every((v, i) => v === [...B].sort()[i]);
  if (task.order) {
    if (A.every((v, i) => v === B[i])) return { ok: true, msg: "Isi dan urutannya tepat.", r: [got] };
    if (same) return { ok: false, msg: "Isinya sudah benar, tapi urutannya belum. Perhatikan ORDER BY.", r: [got] };
    return { ok: false, msg: "Isi hasilmu belum sama dengan yang diminta.", r: [got] };
  }
  return same ? { ok: true, msg: "Hasilnya tepat.", r: [got] } : { ok: false, msg: "Isi hasilmu belum sama dengan yang diminta.", r: [got] };
}

function Editor({ value, onChange, onRun, label, rows = 6 }: { value: string; onChange: (s: string) => void; onRun: () => void; label: string; rows?: number }) {
  return (
    <textarea className="editor" spellCheck={false} aria-label={label} rows={rows} value={value} style={{ minHeight: 120 }}
      onChange={(e) => onChange(e.target.value)}
      onKeyDown={(e) => { if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); onRun(); } }} />
  );
}

export function SqlConsole({ db = "toko", examples = [], initial }: { db?: string; examples?: [string, string][]; initial?: string }) {
  const seed = SEED[db] ?? SEED.toko;
  const dbRef = useRef<unknown>(null);
  const [sql, setSql] = useState(initial ?? examples[0]?.[1] ?? "SELECT * FROM produk;");
  const [res, setRes] = useState<{ r?: SqlResult[]; err?: string; ms?: number } | null>(null);
  const [ver, setVer] = useState(0);
  const schema = useMemo(() => { dbRef.current ??= SQLE.create(seed); return SQLE.schema(dbRef.current); }, [seed, ver]); // eslint-disable-line react-hooks/exhaustive-deps
  const run = (s = sql) => {
    dbRef.current ??= SQLE.create(seed);
    const t0 = performance.now();
    try { const r = SQLE.exec(dbRef.current, s); setRes({ r, ms: performance.now() - t0 }); if (r.some((x) => x.kind === "msg")) setVer((v) => v + 1); }
    catch (e) { setRes({ err: errMsg(e) }); }
  };
  return (
    <div className="sql-grid">
      <aside className="clay-in schema" aria-label="Skema database">
        <span className="eyebrow">Skema database</span>
        {schema.map((t) => (
          <details key={t.name}>
            <summary>{t.view ? "👁 " : ""}{t.name} <span className="small muted">{t.view ? "view" : `${t.rows} baris`}</span></summary>
            <ul>{t.cols.map((c) => <li key={c.name}><code>{c.name}</code> <span className="small muted">{c.type}</span></li>)}</ul>
            <button type="button" className="btn sm" onClick={() => { const s = `SELECT * FROM ${t.name} LIMIT 10;`; setSql(s); run(s); }}>Lihat isi</button>
          </details>
        ))}
      </aside>
      <div className="runner">
        {examples.length > 0 && (
          <div className="tabs" role="group" aria-label="Contoh query">
            {examples.map(([t, s], i) => <button type="button" key={i} className="btn sm" onClick={() => { setSql(s); run(s); }}>{t}</button>)}
          </div>
        )}
        <Editor value={sql} onChange={setSql} onRun={() => run()} label="Editor SQL" rows={Math.min(14, sql.split("\n").length + 2)} />
        <div className="acts">
          <button type="button" className="btn primary" onClick={() => run()}>▶ Jalankan</button>
          <button type="button" className="btn" onClick={() => { dbRef.current = SQLE.create(seed); setVer((v) => v + 1); setRes({ r: [{ kind: "msg", msg: "Database dikembalikan ke data awal." }] }); }}>Reset database</button>
          <p className="hint">Ctrl+Enter untuk menjalankan. Database berjalan di browser dan bisa direset kapan saja.</p>
        </div>
        <div aria-live="polite">
          {res?.err && <p className="msg bad">✖ {res.err}</p>}
          {res?.r && <Result r={res.r} />}
        </div>
      </div>
    </div>
  );
}

export function SqlTasks({ tasks, db = "toko", lid, track }: { tasks: Task[]; db?: string; lid: string; track: string }) {
  const seed = SEED[db] ?? SEED.toko;
  const [src, setSrc] = useState<string[]>(() => tasks.map(() => ""));
  const [fb, setFb] = useState<(ReturnType<typeof grade> | null)[]>(() => tasks.map(() => null));
  const [key, setKey] = useState<boolean[]>(() => tasks.map(() => false));
  const solved = fb.filter((f) => f?.ok).length;
  const check = (i: number) => {
    const r = grade(tasks[i], src[i], seed);
    const next = fb.map((x, j) => (j === i ? r : x));
    setFb(next);
    if (r.ok) {
      award(`${lid}#${i}`, 5, "task");
      if (next.every((x) => x?.ok) && markDone(lid, track)) toast("+10 XP · Semua tantangan selesai");
    }
  };
  return (
    <div className="stack">
      <p className="chip mint" aria-live="polite">{solved}/{tasks.length} tantangan selesai</p>
      {tasks.map((t, i) => (
        <div className="qi" key={i}>
          <p style={{ fontWeight: 800 }}>{i + 1}. <span dangerouslySetInnerHTML={{ __html: t.q }} /></p>
          <Editor value={src[i]} onChange={(s) => setSrc(src.map((x, j) => (j === i ? s : x)))} onRun={() => check(i)} label={`Jawaban tantangan ${i + 1}`} rows={4} />
          <div className="acts" style={{ display: "flex", gap: 10, flexWrap: "wrap", marginTop: 10 }}>
            <button type="button" className="btn primary" onClick={() => check(i)}>Periksa</button>
            {t.a && <button type="button" className="btn" aria-expanded={key[i]} onClick={() => setKey(key.map((x, j) => (j === i ? !x : x)))}>{key[i] ? "Sembunyikan kunci" : "Lihat kunci jawaban"}</button>}
          </div>
          {key[i] && t.a && <pre className="out" style={{ marginTop: 10 }}>{t.a}</pre>}
          <div aria-live="polite">
            {fb[i] && <p className={`fb ${fb[i]!.ok ? "ok" : "bad"}`}><b>{fb[i]!.ok ? "✓ Benar! " : "Belum tepat. "}</b>{fb[i]!.msg}</p>}
            {fb[i]?.r && <Result r={fb[i]!.r!} />}
          </div>
        </div>
      ))}
    </div>
  );
}
