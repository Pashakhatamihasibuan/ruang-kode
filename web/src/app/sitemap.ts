import type { MetadataRoute } from "next";
import { catalog, bodies, SITE_URL } from "@/lib/data";

export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const u = (p: string, priority: number) => ({ url: SITE_URL + p, priority, changeFrequency: "weekly" as const });
  const out = [u("/", 1), u("/belajar", 0.9), u("/glosarium", 0.6)];
  for (const t of catalog().tracks) {
    out.push(u(`/belajar/${t.k}`, 0.8));
    for (const slug of Object.keys(bodies(t.k))) out.push(u(`/belajar/${t.k}/${slug}`, 0.6));
  }
  return out;
}
