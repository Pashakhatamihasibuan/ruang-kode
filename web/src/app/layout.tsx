import type { Metadata, Viewport } from "next";
import { Nunito, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Header, MobileNav, Footer } from "@/components/Chrome";
import { Toaster } from "@/components/Toaster";
import { SITE_URL } from "@/lib/data";

const sans = Nunito({ subsets: ["latin"], variable: "--f-sans", display: "swap", weight: ["400", "600", "700", "800"] });
const mono = JetBrains_Mono({ subsets: ["latin"], variable: "--f-mono", display: "swap", weight: ["400", "600"], preload: false });

const DESC = "Akademi coding, data, dan desain berbahasa Indonesia: 39 jalur belajar dari dasar sampai siap kerja, studi kasus industri, proyek portofolio, Python dan SQL langsung di browser.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: { default: "Ruang Kode · Belajar coding, data, dan desain sampai siap kerja", template: "%s · Ruang Kode" },
  description: DESC,
  applicationName: "Ruang Kode",
  authors: [{ name: "Pasha Khatami Hasibuan" }],
  alternates: { canonical: "/" },
  openGraph: { type: "website", siteName: "Ruang Kode", locale: "id_ID", url: "/", title: "Ruang Kode", description: DESC, images: ["/icons/og.png"] },
  twitter: { card: "summary_large_image" },
  icons: { icon: "/icons/icon-192.png", apple: "/icons/apple-touch-icon.png" },
  manifest: "/manifest.webmanifest",
  formatDetection: { telephone: false },
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#eceffa" },
    { media: "(prefers-color-scheme: dark)", color: "#1a1c2b" },
  ],
  width: "device-width",
  initialScale: 1,
};

// Tema dipasang sebelum halaman tergambar agar tidak berkedip. Skrip ini di-hash di CSP.
const THEME = `try{var t=JSON.parse(localStorage.getItem('rk-theme')||'"auto"');if(t==='light'||t==='dark')document.documentElement.dataset.theme=t}catch(e){}`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="id" className={`${sans.variable} ${mono.variable}`} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: THEME }} />
      </head>
      <body>
        <a className="skip" href="#isi">Langsung ke isi</a>
        <Header />
        <main id="isi" tabIndex={-1}>{children}</main>
        <Footer />
        <MobileNav />
        <Toaster />
      </body>
    </html>
  );
}
