"""Proyek portofolio di dalam setiap jalur: modul terakhir tiap jalur berisi pelajaran "see"
yang meminjam proyek dari jalur Proyek Portofolio. Progresnya dipakai bersama, jadi proyek
yang sudah dikerjakan di satu jalur langsung tercatat selesai di jalur lain dan di menu Proyek."""

# jalur -> (konstanta modul di JS, judul modul proyek di jalur Proyek Portofolio)
PETA = {
    'pseudo': ('PSEUDO_MODULES', 'Proyek Logika, Python & Algoritma: 6 mini + 4 besar'),
    'flowg': ('FLOWG_MODULES', 'Proyek Logika, Python & Algoritma: 6 mini + 4 besar'),
    'python': ('PY_MODULES', 'Proyek Logika, Python & Algoritma: 6 mini + 4 besar'),
    'dsa': ('DSA_MODULES', 'Proyek Logika, Python & Algoritma: 6 mini + 4 besar'),
    'java': ('JAVA_MODULES', 'Proyek Backend Java: 6 mini + 4 besar'),
    'django': ('DJANGO_MODULES', 'Proyek Backend Python (Django): 6 mini + 4 besar'),
    'js': ('JS_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'ts': ('TS_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'fe0': ('FE0_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'html': ('HTML_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'css': ('CSS_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'tw': ('TW_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'bs': ('BS_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'fe': ('FE_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'react': ('REACT_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'nextjs': ('NEXTJS_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'vue': ('VUE_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'slw': ('SLW_MODULES', 'Proyek Frontend: 6 mini + 4 besar'),
    'dart': ('DART_MODULES', 'Proyek Mobile Developer: 6 mini + 4 besar'),
    'kotlin': ('KOTLIN_MODULES', 'Proyek Mobile Developer: 6 mini + 4 besar'),
    'flutter': ('FLUTTER_MODULES', 'Proyek Mobile Developer: 6 mini + 4 besar'),
    'compose': ('COMPOSE_MODULES', 'Proyek Mobile Developer: 6 mini + 4 besar'),
    'kmp': ('KMP_MODULES', 'Proyek Mobile Developer: 6 mini + 4 besar'),
    'slm': ('SLM_MODULES', 'Proyek Mobile Developer: 6 mini + 4 besar'),
    'sql': ('SQL_MODULES', 'Proyek DBA PostgreSQL: 6 mini + 4 besar'),
    'pgdba': ('PGDBA_MODULES', 'Proyek DBA PostgreSQL: 6 mini + 4 besar'),
    'pda': ('PDA_MODULES', 'Proyek Data Analyst & BI: 6 mini + 4 besar'),
    'da': ('DA_MODULES', 'Proyek Data Analyst & BI: 6 mini + 4 besar'),
    'bi': ('BI_MODULES', 'Proyek Data Analyst & BI: 6 mini + 4 besar'),
    'dsci': ('DSCI_MODULES', 'Proyek Data Scientist: 6 mini + 4 besar'),
    'de': ('DE_MODULES', 'Proyek Data Engineer: 6 mini + 4 besar'),
    'ux': ('UX_MODULES', 'Proyek UI/UX Designer: 6 mini + 4 besar'),
    'ui': ('UI_MODULES', 'Proyek UI/UX Designer: 6 mini + 4 besar'),
    'ds': ('DS_MODULES', 'Proyek UI/UX Designer: 6 mini + 4 besar'),
    'qa': ('QA_MODULES', 'Proyek QA Engineer: 6 mini + 4 besar'),
    'sim': ('SIM_MODULES', 'Proyek Analis Sistem Informasi & BI: 6 mini + 4 besar'),
    'msi': ('MSI_MODULES', 'Proyek Analis Sistem Informasi & BI: 6 mini + 4 besar'),
    'git': ('GIT_MODULES', 'Standar proyek yang dicari perekrut'),
}
LAMAR = 'Menyajikan portofolio dan melamar kerja'


def modul_portofolio(proj):
    """Kembalikan {konstanta: modul} untuk setiap jalur."""
    by = {m['t']: m for m in proj}
    lamar = [{'k': 'see', 'ref': 'proj:' + l['t']} for l in by[LAMAR]['lessons']]
    hasil = {}
    for tk, (konst, judul) in PETA.items():
        src = by[judul]
        nama = judul.split(':')[0].replace('Proyek ', '') if judul.startswith('Proyek ') else 'portofolio'
        hasil[konst] = {
            't': 'Proyek portofolio: 6 mini + 4 besar' if judul.startswith('Proyek ') else 'Proyek portofolio dan standar industri',
            'lvl': 'Profesional',
            'd': (f'Proyek berstandar industri untuk jalur {nama}: kerjakan proyek mini lalu proyek besar, '
                  'bandingkan dengan kode final yang bisa dibuka setelah mencoba sendiri, lalu sajikan di CV dan wawancara. '
                  'Progresnya tercatat juga di menu Proyek Portofolio.'),
            'nodes': ['Portfolio Projects'],
            'lessons': [{'k': 'see', 'ref': 'proj:' + l['t']} for l in src['lessons']] + lamar,
        }
    return hasil
