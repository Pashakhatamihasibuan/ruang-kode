import type { MetadataRoute } from "next";

export const dynamic = "force-static";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Ruang Kode · Akademi coding, data & desain",
    short_name: "Ruang Kode",
    description: "Belajar coding, data, dan desain berbahasa Indonesia sampai siap kerja.",
    lang: "id",
    start_url: "/",
    scope: "/",
    display: "standalone",
    background_color: "#eceffa",
    theme_color: "#5140c8",
    icons: [
      { src: "/icons/icon-192.png", sizes: "192x192", type: "image/png" },
      { src: "/icons/icon-512.png", sizes: "512x512", type: "image/png" },
      { src: "/icons/maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
    shortcuts: [{ name: "Progres saya", url: "/saya" }, { name: "Semua materi", url: "/belajar" }],
  };
}
