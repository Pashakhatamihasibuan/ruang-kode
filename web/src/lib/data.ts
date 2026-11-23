import fs from "node:fs";
import path from "node:path";

/* Data kurikulum dibaca saat build (web/src/data, dibuat oleh `python3 build.py`). */

export type Kind = "c" | "w" | "s" | "lab" | "topic" | "proj" | "see";

export interface LessonMeta {
  id: string;
  k: Kind;
  title: string;
  slug: string;
  kind: string;
  qn?: number;
  src?: string;
  srcId?: string;
  srcName?: string;
}
export interface ModuleMeta { t: string; d: string; lvl: string; lessons: LessonMeta[] }
export interface Track {
  k: string; g: string; name: string; lang: string; h: string; d: string;
  mark: string; c: string; cd: string; mods: ModuleMeta[];
}
export interface CareerPath { k: string; t: string; d: string; tr: string[] }
export interface Catalog { groups: { k: string; t: string }[]; tracks: Track[]; paths: CareerPath[] }

export interface QuizItem { q: string; o: string[]; a: number; w: string; html: boolean }
export interface Table { c: string; h: string[]; r: string[][] }
export interface FileEntry { 0: string; 1: string; 2: string }
export interface Body {
  id: string; k: Kind; title: string; slug: string; lang: string; mi: number; li: number;
  b?: string[]; code?: string; out?: string | null; fig?: string[]; tb?: Table[]; pts?: string[];
  q?: QuizItem[]; so?: { q: string; h: string; a?: string; out?: string | null; lang?: string }[];
  pro?: { t: string; tag?: string; why: string; a: string; b: string; out?: string; lang?: string }[];
  bug?: { code: string; err: string; line?: number; why: string };
  trc?: { s: [number, string, Record<string, unknown>, string, number?][]; cut?: boolean };
  fin?: { n: string; tree: string; files: [string, string, string][]; run: string; cek: string[] };
  deep?: { ist: [string, string][]; cx: { t: string; b?: string; code: string; lang?: string; out?: string }[] };
  an?: string; viz?: string; nodes?: string[]; trs?: [string, string][];
  html?: string; css?: string; js?: string; react?: boolean; tw?: boolean; bs?: boolean; console?: boolean; vp?: number;
  task?: Task; tasks?: Task[]; ex?: [string, string][]; db?: string; syn?: [string, string];
  brief?: string; stack?: string; feats?: string[]; steps?: string[]; files?: [string, string, string][];
  sql?: { db: string; file: number }; fc?: unknown; run?: boolean; vq?: string; vj?: string;
  dl?: { k: string; p: string }[]; hp?: { c: string; n: string; s: { t: string; d: string }[] };
}
export interface Task { q: string; a?: string; order?: boolean; check?: string; hint?: string; test?: string }
export interface GlossaryItem { id: string; t: string; en?: string; c: string; d: string; ex?: string; [k: string]: unknown }

const DATA = path.join(process.cwd(), "src", "data");
let _cat: Catalog | null = null;
const _bodies = new Map<string, Record<string, Body>>();

export function catalog(): Catalog {
  if (!_cat) _cat = JSON.parse(fs.readFileSync(path.join(DATA, "catalog.json"), "utf8")) as Catalog;
  return _cat;
}
export function track(k: string): Track | undefined {
  return catalog().tracks.find((t) => t.k === k);
}
export function bodies(k: string): Record<string, Body> {
  let b = _bodies.get(k);
  if (!b) {
    b = JSON.parse(fs.readFileSync(path.join(DATA, "t", `${k}.json`), "utf8")) as Record<string, Body>;
    _bodies.set(k, b);
  }
  return b;
}
export function glossary(): { cats: string[]; items: GlossaryItem[] } {
  return JSON.parse(fs.readFileSync(path.join(DATA, "glossary.json"), "utf8"));
}

export function lessonHref(t: Track, l: LessonMeta): string {
  return l.k === "see" ? `/belajar/${l.src}/${l.slug}` : `/belajar/${t.k}/${l.slug}`;
}

/** Peta id pelajaran lama (mis. dsci-5-5) ke URL baru, untuk tautan lama berbentuk #id. */
export function idMap(): Record<string, string> {
  const m: Record<string, string> = {};
  for (const t of catalog().tracks) {
    m[t.k] = `/belajar/${t.k}`;
    for (const mod of t.mods) for (const l of mod.lessons) m[l.id] = lessonHref(t, l);
  }
  return m;
}
let _ids: Record<string, string> | null = null;
/** Tautan internal di isi pelajaran (href="#jalur-1-2") diarahkan ke URL halaman baru. */
export function fixLinks(html: string): string {
  if (!html.includes('href="#')) return html;
  _ids ??= idMap();
  return html.replace(/href="#([\w-]+)"/g, (all, id: string) => (_ids![id] ? `href="${_ids![id]}"` : all));
}

export interface Flat { t: Track; mi: number; li: number; l: LessonMeta; href: string }
export function flat(t: Track): Flat[] {
  const out: Flat[] = [];
  t.mods.forEach((m, mi) => m.lessons.forEach((l, li) => out.push({ t, mi, li, l, href: lessonHref(t, l) })));
  return out;
}
export const lessonCount = (t: Track) => t.mods.reduce((a, m) => a + m.lessons.length, 0);
export const groupName = (g: string) => catalog().groups.find((x) => x.k === g)?.t ?? g;

export const SITE_URL = "https://ruang-kode-nine.vercel.app";
export const strip = (s: string) => s.replace(/<[^>]+>/g, "").replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/\s+/g, " ").trim();
export const clip = (s: string, n = 155) => (s.length > n ? s.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : s);
