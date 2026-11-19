"""PostgreSQL 16 sungguhan untuk contoh & proyek DBA. Hasil disimpan di tools/deep/pg.cache.json (ikut di-commit),
sehingga build di mesin tanpa PostgreSQL tetap menghasilkan keluaran yang sama."""
import hashlib, json, pathlib, re, subprocess, tempfile
ROOT = pathlib.Path(__file__).resolve().parents[2]

PG_CACHE_F = ROOT / 'tools/deep/pg.cache.json'          # dilacak git: build tanpa PostgreSQL tetap bisa
PG_CACHE = json.loads(PG_CACHE_F.read_text()) if PG_CACHE_F.exists() else {}
PG = {'siap': False, 'dir': '/tmp/pgdeep', 'port': '54329', 'n': 0}


def _pg(*args, **kw):
    return subprocess.run(['runuser', '-u', 'postgres', '--', *args], capture_output=True, text=True, **kw)


def pg_mulai():
    if PG['siap']:
        return
    bin_ = '/usr/lib/postgresql/16/bin'
    if not pathlib.Path(PG['dir'], 'PG_VERSION').exists():
        _pg('mkdir', '-p', PG['dir'])
        r = _pg(f'{bin_}/initdb', '-D', PG['dir'], '-U', 'postgres', '--locale=C.UTF-8', '-E', 'UTF8')
        if r.returncode:
            raise RuntimeError(r.stderr)
        with open(f"{PG['dir']}/postgresql.conf", 'a') as f:
            f.write("\nshared_preload_libraries = 'pg_stat_statements'\ntimezone = 'Asia/Jakarta'\nlc_messages = 'C'\n")
    if _pg(f'{bin_}/pg_ctl', '-D', PG['dir'], 'status').returncode:
        r = _pg(f'{bin_}/pg_ctl', '-D', PG['dir'], '-o', f"-p {PG['port']} -k /tmp", '-l', f"{PG['dir']}/log", '-w', 'start')
        if r.returncode:
            raise RuntimeError(r.stderr + r.stdout)
    PG['siap'] = True


def jalan_pg(code, setup=''):
    """Menjalankan SQL di PostgreSQL 16 sungguhan (psql), database baru per contoh; keluaran psql apa adanya."""
    pg_mulai()
    PG['n'] += 1
    db = f"contoh_{PG['n']}"
    _pg('psql', '-h', '/tmp', '-p', PG['port'], '-X', '-q', '-c', f'DROP DATABASE IF EXISTS {db}', '-c', f'CREATE DATABASE {db}')
    with tempfile.NamedTemporaryFile('w', suffix='.sql', delete=False, dir='/tmp') as f:
        f.write((setup + '\n' if setup else '') + '\\set ECHO none\n' + code + '\n')
    pathlib.Path(f.name).chmod(0o644)
    r = subprocess.run(['runuser', '-u', 'postgres', '--', 'psql', '-h', '/tmp', '-p', PG['port'], '-X', '-q', '-P', 'pager=off',
                        '-d', db, '-f', f.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=120)
    out = '\n'.join(l.rstrip() for l in r.stdout.splitlines())
    out = re.sub(r'^psql:[^:]+:\d+: ', '', out, flags=re.M)
    _pg('psql', '-h', '/tmp', '-p', PG['port'], '-X', '-q', '-c', f'DROP DATABASE IF EXISTS {db} WITH (FORCE)')
    pathlib.Path(f.name).unlink()
    return out.rstrip('\n')



def pg(code, setup=''):
    """Jalankan dengan cache: kunci = hash(setup + kode)."""
    key = hashlib.sha1(('pg\0' + setup + '\0' + code).encode()).hexdigest()
    if key not in PG_CACHE:
        PG_CACHE[key] = jalan_pg(code, setup)
        simpan()
    return PG_CACHE[key]


def simpan():
    PG_CACHE_F.write_text(json.dumps(PG_CACHE, ensure_ascii=False, indent=0, sort_keys=True))
