// Pasca-build: pasang Content-Security-Policy per halaman dengan hash SHA-256 setiap skrip inline,
// sehingga hanya skrip milik situs yang boleh berjalan (tanpa 'unsafe-inline').
// Juga menyalin aset statis besar (unduhan desain, proyek mini) dari akar repositori.
import { createHash } from "node:crypto";
import { readdir, readFile, writeFile, cp, stat } from "node:fs/promises";
import path from "node:path";

const OUT = path.resolve("out");
const ROOT = path.resolve("..");

async function* walk(dir) {
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (e.name !== "lab" && e.name !== "_next") yield* walk(p); }
    else if (e.name.endsWith(".html")) yield p;
  }
}

const BASE = [
  "default-src 'self'",
  "img-src 'self' data:",
  "style-src 'self' 'unsafe-inline'",
  "font-src 'self'",
  "connect-src 'self'",
  "frame-src 'self'",
  "worker-src 'self'",
  "manifest-src 'self'",
  "object-src 'none'",
  "base-uri 'self'",
  "form-action 'self'",
  "upgrade-insecure-requests",
];

const sha = (s) => "'sha256-" + createHash("sha256").update(s, "utf8").digest("base64") + "'";
let n = 0;
for await (const f of walk(OUT)) {
  let html = await readFile(f, "utf8");
  if (html.includes('http-equiv="Content-Security-Policy"')) continue;
  const hashes = new Set();
  for (const m of html.matchAll(/<script(?![^>]*\bsrc=)([^>]*)>([\s\S]*?)<\/script>/g)) {
    if (/type="application\/(ld\+)?json"/.test(m[1])) continue;
    hashes.add(sha(m[2]));
  }
  const csp = [`script-src 'self' ${[...hashes].join(" ")}`.trim(), ...BASE].join("; ");
  html = html.replace(/<meta charSet="utf-8"\/>/i, (m) => `${m}<meta http-equiv="Content-Security-Policy" content="${csp}">`);
  await writeFile(f, html);
  n++;
}
console.log(`CSP dipasang di ${n} halaman`);

for (const d of ["desain", "mini-project"]) {
  try { await stat(path.join(ROOT, d)); await cp(path.join(ROOT, d), path.join(OUT, d), { recursive: true }); console.log(`disalin: ${d}/`); }
  catch { console.warn(`lewati: ${d}/ tidak ditemukan`); }
}
for (const f of await readdir(ROOT)) if (/^google[\w]+\.html$/.test(f)) await cp(path.join(ROOT, f), path.join(OUT, f));
