"use client";
/* Progres belajar disimpan di browser (localStorage 'rk-lms'), formatnya sama dengan versi lama
   sehingga progres siswa tetap terbawa. Tidak ada data yang dikirim ke server. */

export interface Lms {
  done: Record<string, 1>;
  last: Record<string, string>;
  lastAt: Record<string, number>;
  days: Record<string, number>;
  act: Record<string, 1>;
  task: Record<string, 1>;
  qok: Record<string, 1>;
  xp: number;
  [k: string]: unknown;
}

const KEY = "rk-lms";
const today = () => {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
};

export function load(): Lms {
  let s: Partial<Lms> = {};
  try {
    const raw = localStorage.getItem(KEY);
    const v = raw ? JSON.parse(raw) : null;
    if (v && typeof v === "object" && !Array.isArray(v)) s = v;
  } catch {}
  const base = { done: {}, last: {}, lastAt: {}, days: {}, act: {}, task: {}, qok: {}, xp: 0 };
  for (const [k, v] of Object.entries(base)) {
    const cur = (s as Record<string, unknown>)[k];
    if (cur == null || typeof cur !== typeof v) (s as Record<string, unknown>)[k] = v;
  }
  return s as Lms;
}

export function save(s: Lms) {
  try {
    localStorage.setItem(KEY, JSON.stringify(s));
  } catch {}
  window.dispatchEvent(new Event("rk-lms"));
}

export function touch(s: Lms) {
  s.act[today()] = 1;
}

export function markDone(id: string, track: string): boolean {
  const s = load();
  if (s.done[id]) return false;
  s.done[id] = 1;
  s.days[today()] = (s.days[today()] || 0) + 1;
  s.xp += 10;
  s.last[track] = id;
  s.lastAt[track] = Date.now();
  touch(s);
  save(s);
  return true;
}

export function unmark(id: string) {
  const s = load();
  delete s.done[id];
  save(s);
}

export function visit(id: string, track: string) {
  const s = load();
  s.last[track] = id;
  s.lastAt[track] = Date.now();
  touch(s);
  save(s);
}

export function award(key: string, xp: number, bucket: "qok" | "task" = "qok") {
  const s = load();
  if (s[bucket][key]) return;
  s[bucket][key] = 1;
  s.xp += xp;
  touch(s);
  save(s);
}

export function streak(s: Lms): number {
  let n = 0;
  const d = new Date();
  const key = (x: Date) => `${x.getFullYear()}-${String(x.getMonth() + 1).padStart(2, "0")}-${String(x.getDate()).padStart(2, "0")}`;
  if (!s.act[key(d)]) d.setDate(d.getDate() - 1);
  while (s.act[key(d)]) {
    n++;
    d.setDate(d.getDate() - 1);
  }
  return n;
}

export function toast(msg: string) {
  window.dispatchEvent(new CustomEvent("rk-toast", { detail: msg }));
}

/** Menghapus progres satu jalur. Mengembalikan salinan data sebelum dihapus agar bisa diurungkan. */
export function resetTrack(k: string, ids: string[]): Lms {
  const s = load();
  const before = JSON.parse(JSON.stringify(s)) as Lms;
  const own = new Set(ids);
  let xp = 0;
  for (const id of ids) if (s.done[id]) { delete s.done[id]; xp += 10; }
  for (const [bucket, pts] of [["qok", 2], ["task", 5]] as const)
    for (const key of Object.keys(s[bucket])) if (own.has(key.split("#")[0])) { delete s[bucket][key]; xp += pts; }
  delete s.last[k];
  delete s.lastAt[k];
  s.xp = Math.max(0, s.xp - xp);
  save(s);
  return before;
}

/** Menghapus seluruh progres di browser ini. Mengembalikan salinan data sebelum dihapus. */
export function resetAll(): Lms {
  const before = load();
  save({ done: {}, last: {}, lastAt: {}, days: {}, act: {}, task: {}, qok: {}, xp: 0 });
  return before;
}

/** Memulihkan data yang tadi dihapus. */
export function restore(s: Lms) {
  save(s);
}
