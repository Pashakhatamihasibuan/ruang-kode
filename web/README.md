# Ruang Kode · versi Next.js

Situs Ruang Kode yang dibangun ulang dengan **Next.js 16 (App Router) + React 19 + TypeScript**, gaya **Bauhaus**, dan diekspor sebagai situs statis (`output: "export"`).

## Menjalankan

```bash
# 1. buat data kurikulum (dari akar repositori)
python3 build.py          # menulis web/src/data/*.json, web/public/lab/legacy-*, web/src/lib/sqle.js

# 2. jalankan aplikasi
cd web
npm install
npm run dev               # http://localhost:3000
npm run build             # hasil statis di web/out
```

## Struktur

| Bagian | Isi |
|---|---|
| `src/app` | Halaman: beranda, `/belajar` (katalog), `/belajar/[jalur]`, `/belajar/[jalur]/[pelajaran]`, `/glosarium`, `/saya`, `sitemap.xml`, `robots.txt`, manifest |
| `src/components` | Komponen UI. Komponen interaktif (`"use client"`): kuis, Runner Python, WebLab, konsol SQL, Tracer, pencarian |
| `src/lib` | Pembaca data saat build, pewarna kode (Shiki, saat build), progres (localStorage `rk-lms`, sama dengan versi lama) |
| `public/lab` | Halaman sandbox untuk menjalankan kode siswa: Python (Pyodide), pratinjau HTML/CSS/JS, dan visual interaktif |
| `scripts/postbuild.mjs` | Memasang Content-Security-Policy per halaman (hash SHA-256 skrip inline) dan menyalin aset unduhan |

## Keamanan

- **CSP ketat per halaman:** `script-src 'self'` + hash setiap skrip inline, tanpa `unsafe-inline`/`unsafe-eval` di halaman utama.
- **Kode siswa terisolasi:** Python, HTML/CSS/JS, dan visual berjalan di iframe `sandbox="allow-scripts"` (asal buram), jadi tidak bisa membaca localStorage, cookie, atau DOM situs. Pesan antar-frame diperiksa sumbernya.
- **Header** (lihat `vercel.json`): HSTS, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, `COOP`, `X-Frame-Options`, `frame-ancestors`.
- **Tanpa server, akun, atau pelacak.** Progres hanya di browser pengguna dan bisa diunduh sebagai cadangan.

## Deploy ke Vercel

Buat proyek Vercel dengan **Root Directory = `web`**. Konfigurasi build sudah ada di `vercel.json`.
