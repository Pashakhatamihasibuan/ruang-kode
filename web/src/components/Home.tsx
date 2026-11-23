"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { load } from "@/lib/progress";

/** Tombol "Lanjutkan" ke pelajaran terakhir yang dibuka. */
export function Resume() {
  const [href, setHref] = useState<{ u: string; t: string } | null>(null);
  useEffect(() => {
    const s = load();
    const last = Object.entries(s.lastAt || {}).sort((a, b) => b[1] - a[1])[0];
    if (!last) return;
    const id = s.last[last[0]];
    fetch("/ids.json").then((r) => r.json()).then((m: Record<string, [string, string]>) => {
      if (m[id]) setHref({ u: m[id][0], t: m[id][1] });
    }).catch(() => {});
  }, []);
  if (!href) return <Link className="btn" href="/saya">Lihat progres saya</Link>;
  return <Link className="btn" href={href.u} title={href.t}>Lanjutkan: {href.t.length > 34 ? href.t.slice(0, 33) + "…" : href.t}</Link>;
}

/** Tautan lama berbentuk /#dsci-5-5 atau /#sql diarahkan ke URL halaman baru. */
export function LegacyHash() {
  const router = useRouter();
  useEffect(() => {
    const h = decodeURIComponent(location.hash.slice(1));
    if (!h || !/^[\w-]+$/.test(h)) return;
    const pages: Record<string, string> = { saya: "/saya", glosarium: "/glosarium", katalog: "/belajar", beranda: "/" };
    if (pages[h]) { router.replace(pages[h]); return; }
    fetch("/ids.json").then((r) => r.json()).then((m: Record<string, [string, string]>) => {
      if (m[h]) router.replace(m[h][0]);
    }).catch(() => {});
  }, [router]);
  return null;
}
