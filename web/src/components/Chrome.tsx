import Link from "next/link";
import { NavLinks } from "./NavLinks";
import { ThemeToggle } from "./ThemeToggle";
import { Search } from "./Search";

export function Header() {
  return (
    <header className="top">
      <div className="wrap">
        <div className="top-in">
          <Link className="brand" href="/" aria-label="Ruang Kode, ke beranda">
            <span className="blob" aria-hidden="true">RK</span>
            <span>Ruang Kode<small>coding · data · desain</small></span>
          </Link>
          <nav className="nav" aria-label="Utama"><NavLinks variant="top" /></nav>
          <Search />
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}

export function MobileNav() {
  return (
    <nav className="mnav" aria-label="Navigasi bawah">
      <NavLinks variant="bottom" />
    </nav>
  );
}

export function Footer() {
  return (
    <footer className="foot">
      <div className="wrap">
        <div className="card">
          <div>
            <b>Ruang Kode</b> · dikembangkan oleh Pasha Khatami Hasibuan
            <br />Kurikulum mengikuti <a href="https://roadmap.sh" rel="noopener noreferrer" target="_blank">roadmap.sh</a> dan kebutuhan industri 2026–2030.
          </div>
          <div>
            Progres tersimpan hanya di browser ini. Tidak ada akun, iklan, atau pelacak.
            <br /><Link href="/belajar">Semua materi</Link> · <Link href="/glosarium">Glosarium</Link> · <Link href="/saya">Progres saya</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
