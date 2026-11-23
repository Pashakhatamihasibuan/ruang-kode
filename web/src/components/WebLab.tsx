"use client";
import { useCallback, useEffect, useId, useRef, useState } from "react";
import type { Task } from "@/lib/data";
import { award, markDone, toast } from "@/lib/progress";

const REACT_CDN = [
  "https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js",
  "https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js",
  "https://cdn.jsdelivr.net/npm/@babel/standalone@7.26.4/babel.min.js",
];
const TW_CDN = "https://cdn.tailwindcss.com/3.4.17";
const BS = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css", "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"];

type Src = { html?: string; css?: string; js?: string };
interface Opts { react?: boolean; tw?: boolean; bs?: boolean; test?: string }

function previewDoc(o: Opts, c: Src, id: string) {
  const scr = (s?: string) => String(s || "").replace(/<\/script/gi, "<\\/script");
  const boot = `<script>(function(){var ID=${JSON.stringify(id)};function f(v){if(typeof v==='string')return v;try{return JSON.stringify(v)}catch(e){return String(v)}}
function send(t,a){parent.postMessage({rk:ID,t:t,s:Array.prototype.map.call(a,f).join(' ')},'*')}
['log','info','warn','error'].forEach(function(k){var o=console[k];console[k]=function(){send(k,arguments);if(o)o.apply(console,arguments)}});
addEventListener('error',function(e){send('error',[e.message])});addEventListener('unhandledrejection',function(e){send('error',[String(e.reason)])});
window.__rkTest=function(){try{return !!(${o.test || "false"})}catch(e){return false}};
addEventListener('message',function(e){if(e.data&&e.data.rkTest===ID)parent.postMessage({rk:ID,t:'test',r:window.__rkTest()},'*')})})()<\/script>`;
  const css = `<style>${String(c.css || "").replace(/<\/style/gi, "<\\/style")}</style>`;
  if (o.react)
    return `<!doctype html><html><head><meta charset="utf-8">${css}</head><body>${c.html || ""}<div id="root"></div>${boot}${REACT_CDN.map((u) => `<script src="${u}"><\/script>`).join("")}
<script type="text/babel" data-presets="react">const {useState,useEffect,useRef,useMemo,useCallback,useReducer,useContext,useId}=React;
${scr(c.js)}
ReactDOM.createRoot(document.getElementById('root')).render(<App/>);<\/script></body></html>`;
  const fw = o.tw ? `<script src="${TW_CDN}"><\/script>` : o.bs ? `<link rel="stylesheet" href="${BS[0]}">` : "";
  const fwEnd = o.bs ? `<script src="${BS[1]}"><\/script>` : "";
  return `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">${fw}${css}</head><body>${c.html || ""}${boot}${fwEnd}${c.js != null ? `<script>${scr(c.js)}<\/script>` : ""}</body></html>`;
}

export function WebLab({ init, react, tw, bs, showConsole, task, lid, track }: {
  init: Src; react?: boolean; tw?: boolean; bs?: boolean; showConsole?: boolean; task?: Task; lid: string; track: string;
}) {
  const tabs = (["html", "css", "js"] as const).filter((k) => init[k] != null);
  const [tab, setTab] = useState<(typeof tabs)[number]>(tabs[0]);
  const [src, setSrc] = useState<Src>(init);
  const [logs, setLogs] = useState<{ t: string; s: string }[]>([]);
  const [fb, setFb] = useState<{ ok: boolean; msg: string } | null>(null);
  const [hint, setHint] = useState(false);
  const frame = useRef<HTMLIFrameElement>(null);
  const runId = useRef("");
  const pending = useRef("");
  const uid = useId();

  const run = useCallback(() => {
    runId.current = uid + Date.now();
    setLogs([]);
    pending.current = previewDoc({ react, tw, bs, test: task?.test }, src, runId.current);
    if (frame.current) frame.current.src = "/lab/web?" + Date.now();
  }, [src, react, tw, bs, task, uid]);

  useEffect(() => {
    const f = (e: MessageEvent) => {
      if (!frame.current || e.source !== frame.current.contentWindow) return;
      const d = e.data || {};
      if (d.rkWeb && d.ready && pending.current) {
        frame.current.contentWindow!.postMessage({ doc: pending.current }, "*");
        return;
      }
      if (d.rk !== runId.current) return;
      if (d.t === "test") {
        if (d.r) {
          setFb({ ok: true, msg: "✓ Tantangan berhasil. Hasilmu sesuai yang diminta." });
          award(`${lid}#w`, 5, "task");
          if (markDone(lid, track)) toast("+10 XP · Pelajaran selesai");
        } else setFb({ ok: false, msg: "Belum sesuai. Baca lagi tantangannya, ubah kode, lalu jalankan dan periksa lagi." });
        return;
      }
      setLogs((l) => [...l.slice(-199), { t: d.t, s: d.s }]);
    };
    window.addEventListener("message", f);
    return () => window.removeEventListener("message", f);
  }, [lid, track]);

  useEffect(() => { run(); /* jalankan sekali saat dibuka */ // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const check = () => {
    run();
    setTimeout(() => frame.current?.contentWindow?.postMessage({ rkTest: runId.current }, "*"), 900);
  };
  const names: Record<string, string> = { html: "HTML", css: "CSS", js: react ? "JSX" : "JavaScript" };

  return (
    <div className="stack">
      <div className="wlab-grid">
        <div className="runner">
          <div className="tabs" role="tablist" aria-label="Berkas">
            {tabs.map((k) => (
              <button key={k} type="button" role="tab" id={`tab-${uid}-${k}`} aria-controls={`pan-${uid}`} aria-selected={tab === k} className="btn sm" aria-pressed={tab === k} onClick={() => setTab(k)}>{names[k]}</button>
            ))}
          </div>
          <div role="tabpanel" id={`pan-${uid}`} aria-labelledby={`tab-${uid}-${tab}`}>
            <textarea className="editor" spellCheck={false} aria-label={`Editor ${names[tab]}`} rows={16} value={src[tab] ?? ""}
              onChange={(e) => setSrc({ ...src, [tab]: e.target.value })}
              onKeyDown={(e) => { if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); run(); } }} />
          </div>
          <div className="acts">
            <button type="button" className="btn primary" onClick={run}>▶ Jalankan</button>
            <button type="button" className="btn" onClick={() => { setSrc(init); setTimeout(run, 0); }}>Reset</button>
            <p className="hint">Ctrl+Enter untuk menjalankan. Pratinjau berjalan di sandbox terpisah.{react ? " Memakai React 18." : tw ? " Memakai Tailwind CSS 3.4." : bs ? " Memakai Bootstrap 5.3." : ""}</p>
          </div>
        </div>
        <div className="runner">
          <span className="eyebrow">Pratinjau</span>
          <iframe ref={frame} className="preview" sandbox="allow-scripts allow-modals" title="Pratinjau hasil kode" />
          {(showConsole || react || logs.length > 0) && (
            <div>
              <div className="out-l">Konsol</div>
              <pre className="out" aria-live="polite">{logs.length ? logs.map((l) => (l.t === "error" ? "✖ " : "") + l.s).join("\n") : "(belum ada log)"}</pre>
            </div>
          )}
        </div>
      </div>
      {task && (
        <div className="card" style={{ background: "var(--butter)" }}>
          <span className="eyebrow">Tantangan · diperiksa otomatis</span>
          <h3 dangerouslySetInnerHTML={{ __html: task.q }} />
          <div className="acts" style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
            {task.test && <button type="button" className="btn primary" onClick={check}>Periksa</button>}
            {task.hint && <button type="button" className="btn" aria-expanded={hint} onClick={() => setHint(!hint)}>Petunjuk</button>}
          </div>
          {hint && task.hint && <p className="fb ok">💡 {task.hint}</p>}
          <div aria-live="polite">{fb && <p className={`fb ${fb.ok ? "ok" : "bad"}`}>{fb.msg}</p>}</div>
        </div>
      )}
    </div>
  );
}
