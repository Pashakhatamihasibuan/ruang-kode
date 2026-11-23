"use client";
import { useState } from "react";
import type { QuizItem } from "@/lib/data";
import { award } from "@/lib/progress";

const Html = ({ html, text }: { html: boolean; text: string }) =>
  html ? <span dangerouslySetInnerHTML={{ __html: text }} /> : <>{text}</>;

export function Quiz({ items, lid }: { items: QuizItem[]; lid: string }) {
  const [pick, setPick] = useState<(number | null)[]>(() => items.map(() => null));
  const answered = pick.filter((p) => p !== null).length;
  const right = pick.filter((p, i) => p === items[i].a).length;
  return (
    <div className="quiz">
      {items.map((it, i) => {
        const p = pick[i];
        const done = p !== null;
        return (
          <div className="qi" key={i}>
            <fieldset>
              <legend>{i + 1}. <Html html={it.html} text={it.q} /></legend>
              <div className="opts">
                {it.o.map((o, j) => (
                  <label key={j} className={`opt${done && j === it.a ? " right" : ""}${done && j === p && p !== it.a ? " wrong" : ""}`}>
                    <input type="radio" name={`q-${lid}-${i}`} disabled={done} checked={p === j}
                      onChange={() => {
                        setPick((s) => s.map((x, k) => (k === i ? j : x)));
                        if (j === it.a) award(`${lid}#q${i}`, 2);
                      }} />
                    <Html html={it.html} text={o} />
                  </label>
                ))}
              </div>
            </fieldset>
            {done && (
              <div className={`fb ${p === it.a ? "ok" : "bad"}`} role="status">
                <b>{p === it.a ? "✓ Benar. " : "Belum tepat. "}</b><Html html={it.html} text={it.w} />
              </div>
            )}
          </div>
        );
      })}
      <div className="score" aria-live="polite">
        {answered === items.length ? (
          <>
            <span>Skor: {right} dari {items.length}</span>
            <button type="button" className="btn sm" onClick={() => setPick(items.map(() => null))}>Ulangi kuis</button>
          </>
        ) : (
          <span className="muted small">{answered} dari {items.length} soal dijawab</span>
        )}
      </div>
    </div>
  );
}
