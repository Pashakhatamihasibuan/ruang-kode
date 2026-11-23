"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Icon } from "./Icon";

const ITEMS = [
  { href: "/", t: "Beranda", ic: "home" },
  { href: "/belajar", t: "Materi", ic: "grid" },
  { href: "/saya", t: "Progres saya", short: "Progres", ic: "chart" },
  { href: "/glosarium", t: "Glosarium", ic: "book" },
];

export function NavLinks({ variant }: { variant: "top" | "bottom" }) {
  const p = usePathname() || "/";
  const cur = (h: string) => (h === "/" ? p === "/" : p === h || p.startsWith(h + "/"));
  return (
    <>
      {ITEMS.filter((x) => variant === "bottom" || x.href !== "/").map((x) => (
        <Link key={x.href} href={x.href} aria-current={cur(x.href) ? "page" : undefined}>
          {variant === "bottom" && <Icon name={x.ic} size={22} />}
          {variant === "bottom" ? x.short ?? x.t : x.t}
        </Link>
      ))}
    </>
  );
}
