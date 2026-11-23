"""Kode final standar industri untuk 120 proyek karier (6 mini + 4 besar per jalur).

Kode penyelesaian di setiap proyek dipecah menjadi berkas sesuai komentar judul berkasnya
(mis. `// app/checkout/actions.ts`), lalu dilengkapi kerangka proyek yang biasa ada di tim
industri: konfigurasi lint/format, uji otomatis, CI, README, .gitignore, dan .env.example.
Hasilnya dipakai komponen `fin` (tersembunyi sampai pelajar menekan tombol)."""
import html
import re

_H = re.compile(r'^\s*(?://|#|--|<!--|/\*)\s*([\w@()\[\]./-]+\.[A-Za-z]{1,5})\b(.*)$')
_EXT = {'py': 'python', 'ts': 'ts', 'tsx': 'tsx', 'js': 'js', 'mjs': 'js', 'java': 'java', 'kt': 'kotlin', 'kts': 'kotlin', 'dart': 'dart', 'sql': 'sql',
        'yml': 'yaml', 'yaml': 'yaml', 'json': 'json', 'md': 'text', 'toml': 'toml', 'html': 'html', 'css': 'css', 'tf': 'hcl', 'hcl': 'hcl', 'conf': 'conf',
        'ini': 'conf', 'xml': 'html', 'swift': 'swift', 'txt': 'text', 'cfg': 'conf'}
_UTAMA = {'python': 'main.py', 'sql': 'db/solusi.sql', 'html': 'index.html', 'js': 'src/main.js', 'ts': 'src/main.ts', 'tsx': 'src/App.tsx',
          'java': 'src/main/java/Main.java', 'kotlin': 'app/src/main/kotlin/Main.kt', 'dart': 'lib/main.dart', 'yaml': 'deploy/manifest.yaml',
          'conf': 'config/postgresql.conf', 'hcl': 'infra/main.tf', 'text': 'docs/solusi.md'}


def polos(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t or ''))


def lang_dari(path, bawaan):
    ext = path.rsplit('.', 1)[-1].lower() if '.' in path.split('/')[-1] else ''
    return _EXT.get(ext, bawaan)


def pecah(code, lang):
    """Pisahkan kode penyelesaian menjadi berkas-berkas berdasarkan komentar judul berkas."""
    baris = code.split('\n')
    bagian, nama, isi = [], None, []
    for ln in baris:
        m = _H.match(ln)
        if m and ('/' in m.group(1) or '.' in m.group(1)) and not m.group(1).startswith('http'):
            if nama is not None or any(x.strip() for x in isi):
                bagian.append([nama, isi])
            nama, isi = m.group(1), [ln]
            continue
        isi.append(ln)
    bagian.append([nama, isi])
    hasil, sisa = [], []
    for nm, ls in bagian:
        teks = '\n'.join(ls).strip('\n')
        if not teks.strip():
            continue
        if nm is None:
            sisa.append(teks)
            continue
        hasil.append([nm, teks])
    if sisa:  # pembuka tanpa judul berkas: ikut berkas pertama atau menjadi berkas utama
        if hasil and len('\n'.join(sisa)) < 400:
            hasil[0][1] = '\n'.join(sisa) + '\n\n' + hasil[0][1]
        else:
            hasil.insert(0, [_UTAMA.get(lang, 'src/solusi.txt'), '\n\n'.join(sisa)])
    gabung = {}
    for nm, t in hasil:  # judul yang sama (mis. potongan models.py dua kali) digabung
        gabung[nm] = gabung[nm] + '\n\n' + t if nm in gabung else t
    return [[nm, lang_dari(nm, lang), t.rstrip() + '\n'] for nm, t in gabung.items()]


def profil(lang, stack, files):
    s = (stack or '').lower()
    nama = ' '.join(f[0] for f in files)
    if 'django' in s and lang == 'python':
        return 'django'
    if lang == 'python' and ('fastapi' in s):
        return 'fastapi'
    if lang in ('tsx', 'ts', 'js', 'html') or 'next.js' in s or 'react' in s or 'playwright' in s and lang != 'python':
        if 'next.js' in s:
            return 'next'
        if lang == 'html':
            return 'web'
        if 'k6' in s and lang == 'js':
            return 'k6'
        return 'react' if lang in ('tsx', 'ts') or 'react' in s else 'web'
    if lang == 'java':
        return 'spring' if 'spring' in s else 'java'
    if lang == 'dart':
        return 'flutter'
    if lang == 'kotlin':
        return 'kmp' if 'multiplatform' in s or 'commonMain' in nama else 'android'
    if lang == 'hcl':
        return 'terraform'
    if lang in ('yaml', 'conf') and ('kubernetes' in s or 'cloudnativepg' in s or 'pgbouncer' in s):
        return 'infra'
    if lang == 'sql':
        return 'sql'
    if lang == 'text' or lang == 'yaml':
        return 'docs'
    return 'python'


def _env(code):
    nama = set(re.findall(r"process\.env\.([A-Z][A-Z0-9_]+)", code)) | set(re.findall(r"os\.environ(?:\.get)?\(?\[?['\"]([A-Z][A-Z0-9_]+)", code)) \
        | set(re.findall(r"getenv\(['\"]([A-Z][A-Z0-9_]+)", code)) | set(re.findall(r"\$\{([A-Z][A-Z0-9_]{2,})\}", code))
    return sorted(n for n in nama if n not in ('HOME', 'PATH', 'CI'))


def _slug(t):
    kata, hasil = re.sub(r'[^a-z0-9]+', '-', polos(t).lower()).strip('-').split('-'), ''
    for k in kata:
        if len(hasil) + len(k) + 1 > 36:
            break
        hasil = f'{hasil}-{k}' if hasil else k
    return hasil or 'proyek'


# ---------------------------------------------------------------- berkas konfigurasi per profil
GI = {'python': '__pycache__/\n*.pyc\n.venv/\n.env\n.pytest_cache/\n.mypy_cache/\n.ruff_cache/\ndist/\n*.egg-info/\n.coverage\n',
      'node': 'node_modules/\ndist/\n.next/\n.env\n.env.local\ncoverage/\nplaywright-report/\ntest-results/\n',
      'java': 'target/\n.idea/\n*.iml\n.env\n',
      'flutter': '.dart_tool/\nbuild/\n.flutter-plugins*\n.env\n*.g.dart\n',
      'gradle': '.gradle/\nbuild/\nlocal.properties\n.idea/\n.env\n',
      'terraform': '.terraform/\n*.tfstate\n*.tfstate.*\n*.tfvars\n.env\n',
      'umum': '.env\n.DS_Store\n'}


def _pyproject(nama, dep, django=False):
    deps = ''.join(f'  "{d}",\n' for d in dep)
    return f'''[project]
name = "{nama}"
version = "1.0.0"
requires-python = ">=3.12"
dependencies = [
{deps}]

[dependency-groups]
dev = ["pytest>=8", "pytest-cov>=5", "ruff>=0.7", "mypy>=1.13"{', "pytest-django>=4.9"' if django else ''}]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "UP", "SIM", "S", "N"]
ignore = ["S101"]  # assert boleh di dalam tests/

[tool.mypy]
python_version = "3.12"
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
addopts = "-q --cov --cov-report=term-missing"
testpaths = ["tests"{', "."' if django else ''}]
{'DJANGO_SETTINGS_MODULE = "config.settings"' + chr(10) if django else ''}'''


def _dep_python(code, stack):
    peta = [('pandas', 'pandas>=2.2'), ('numpy', 'numpy>=2.0'), ('sklearn', 'scikit-learn>=1.5'), ('lightgbm', 'lightgbm>=4.5'), ('matplotlib', 'matplotlib>=3.9'),
            ('statsmodels', 'statsmodels>=0.14'), ('fastapi', 'fastapi>=0.115'), ('pydantic', 'pydantic>=2.9'), ('httpx', 'httpx>=0.27'), ('typer', 'typer>=0.12'),
            ('rich', 'rich>=13'), ('django', 'django>=5.1'), ('rest_framework', 'djangorestframework>=3.15'), ('celery', 'celery>=5.4'), ('redis', 'redis>=5'),
            ('anthropic', 'anthropic>=0.40'), ('mlflow', 'mlflow>=2.17'), ('shap', 'shap>=0.46'), ('psycopg', 'psycopg[binary]>=3.2'), ('sqlalchemy', 'sqlalchemy>=2.0'),
            ('aiokafka', 'aiokafka>=0.11'), ('prefect', 'prefect>=3.0'), ('airflow', 'apache-airflow>=2.10'), ('dlt', 'dlt>=1.3'), ('duckdb', 'duckdb>=1.1'),
            ('polars', 'polars>=1.9'), ('scipy', 'scipy>=1.14'), ('evidently', 'evidently>=0.4'), ('pgvector', 'pgvector>=0.3'), ('cachetools', 'cachetools>=5.5'),
            ('uvicorn', 'uvicorn>=0.32'), ('pact', 'pact-python>=2.2'), ('PIL', 'pillow>=11'), ('streamlit', 'streamlit>=1.39'), ('yaml', 'pyyaml>=6')]
    return [d for k, d in peta if re.search(rf'\b(import|from)\s+{re.escape(k)}\b', code)]


def _ci(nama, langkah, layanan='', setup=''):
    isi = ''.join(f'      - name: {n}\n        run: {c}\n' for n, c in langkah)
    return f'''name: CI
on:
  push:
    branches: [main]
  pull_request:

concurrency:
  group: ci-${{{{ github.ref }}}}
  cancel-in-progress: true

jobs:
  {nama}:
    runs-on: ubuntu-latest
    timeout-minutes: 20
{layanan}    steps:
      - uses: actions/checkout@v4
{setup}{isi}'''


PG = '''    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: app
        ports: ["5432:5432"]
        options: >-
          --health-cmd pg_isready --health-interval 5s --health-timeout 5s --health-retries 10
    env:
      DATABASE_URL: postgresql://postgres:postgres@localhost:5432/app
'''

SETUP_PY = '''      - uses: astral-sh/setup-uv@v3
      - run: uv python install 3.12 && uv sync --all-groups
'''
SETUP_NODE = '''      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
'''
SETUP_JAVA = '''      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 21
          cache: maven
'''
SETUP_FLUTTER = '''      - uses: subosito/flutter-action@v2
        with:
          channel: stable
          cache: true
      - run: flutter pub get
'''
SETUP_GRADLE = '''      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 21
      - uses: gradle/actions/setup-gradle@v4
'''

CEK_UMUM = [
    ['Fungsi', 'Semua fitur wajib berjalan, termasuk kasus kosong, input salah, dan batas (0, negatif, sangat besar).'],
    ['Struktur', 'Kode dipisah per tanggung jawab (data, logika, tampilan/antarmuka); tidak ada fungsi raksasa lebih dari ±40 baris.'],
    ['Penamaan', 'Nama variabel, fungsi, dan berkas menjelaskan maksudnya; konsisten satu bahasa.'],
    ['Uji otomatis', 'Ada test untuk logika inti dan kasus tepi; test berjalan di CI dan hijau.'],
    ['Kualitas kode', 'Lint dan formatter lulus tanpa peringatan yang diabaikan.'],
    ['Keamanan', 'Tidak ada rahasia (API key, password) di kode; input dari luar divalidasi; query memakai parameter.'],
    ['Dokumentasi', 'README menjelaskan masalah, cara menjalankan, cara menguji, dan keputusan teknis penting.'],
    ['Git', 'Commit kecil dengan pesan jelas; .gitignore mencegah berkas build/rahasia ikut ter-commit.'],
]
CEK_PROFIL = {
    'python': [['Tipe & gaya', 'Type hints di fungsi publik; <code>ruff check</code>, <code>ruff format --check</code>, dan <code>mypy</code> lulus.']],
    'fastapi': [['API', 'Skema request/response memakai Pydantic; status HTTP tepat (201, 400, 404, 422, 429); dependency injection untuk DB.']],
    'django': [['Django', 'Logika bisnis di service/model, bukan di view; izin (permission) diuji; query bebas N+1 (select_related/prefetch_related).'],
               ['Migrasi', 'Migrasi ter-commit, bisa dijalankan dari nol, dan tidak mengubah data tanpa rencana rollback.']],
    'web': [['HTML & a11y', 'HTML semantik dan valid; label di setiap input; fokus terlihat; lulus axe tanpa pelanggaran serius.'],
            ['Responsif', 'Rapi di 360, 768, dan 1440 px tanpa scroll horizontal.']],
    'react': [['React', 'State minimal dan diturunkan; efek dibersihkan (cleanup); key stabil; tidak ada <code>any</code> tanpa alasan.'],
              ['TypeScript', '<code>tsc --noEmit</code> lulus dengan <code>strict: true</code>.']],
    'next': [['Next.js', 'Data dibaca di Server Component; perhitungan sensitif (harga, izin) di server; rahasia hanya di variabel lingkungan server.'],
             ['TypeScript', '<code>tsc --noEmit</code> lulus dengan <code>strict: true</code>.']],
    'k6': [['Uji performa', 'Ambang (thresholds) p95 dan tingkat error ditetapkan; skenario mencerminkan pola trafik nyata.']],
    'java': [['Java', 'Kelas kecil dengan tanggung jawab tunggal; immutable bila bisa (record); exception spesifik, bukan <code>catch (Exception)</code> kosong.'],
             ['Uji', 'JUnit 5 + AssertJ; <code>mvn verify</code> hijau.']],
    'spring': [['Spring Boot', 'Controller tipis, logika di service, transaksi di service; validasi Bean Validation; error lewat <code>@RestControllerAdvice</code>.'],
               ['Uji', 'Unit test service + integration test dengan Testcontainers; <code>mvn verify</code> hijau.']],
    'flutter': [['Flutter', 'Widget kecil dan <code>const</code>; state dikelola satu pola (Riverpod/Bloc); tidak ada logika bisnis di <code>build()</code>.'],
                ['Analyzer', '<code>flutter analyze</code> tanpa isu; <code>dart format</code> rapi; widget test untuk layar utama.']],
    'android': [['Compose', 'UI stateless menerima state + event; ViewModel memegang StateFlow; tidak ada operasi I/O di composable.'],
                ['Gradle', '<code>./gradlew lint detekt test</code> hijau; dependensi lewat version catalog.']],
    'kmp': [['KMP', 'Logika dan data di <code>commonMain</code>; kode platform hanya di <code>expect/actual</code>; test di <code>commonTest</code>.']],
    'sql': [['SQL', 'Skema memakai constraint (PK, FK, CHECK, NOT NULL); query diperiksa dengan <code>EXPLAIN (ANALYZE, BUFFERS)</code>; migrasi bisa diulang.'],
            ['Gaya SQL', '<code>sqlfluff lint</code> lulus; nama tabel/kolom snake_case konsisten.']],
    'infra': [['Infrastruktur', 'Manifest tervalidasi (kubeconform); resource requests/limits ada; rahasia lewat Secret/KMS, bukan teks biasa.']],
    'terraform': [['Terraform', '<code>terraform fmt</code>, <code>validate</code>, <code>tflint</code>, dan <code>checkov</code> lulus; state di remote backend terkunci.']],
    'docs': [['Dokumen', 'Definisi, asumsi, dan sumber data tertulis jelas; bisa diikuti orang lain tanpa bertanya.']],
}


def _kerangka(prof, nama, lang, files, code, out, stack):
    """Berkas tambahan standar industri sesuai profil proyek."""
    ada = {f[0] for f in files}
    tambah, run = [], ''
    utama = files[0][0] if files else ''
    if prof in ('python', 'fastapi', 'django'):
        tambah.append(['pyproject.toml', 'toml', _pyproject(nama, _dep_python(code, stack), prof == 'django')] if 'pyproject.toml' not in ada else None)
        if out is not None and prof == 'python' and utama.endswith('.py'):
            tambah.append(['tests/keluaran_contoh.txt', 'text', out.rstrip() + '\n'])
            tambah.append(['tests/test_keluaran.py', 'python', f'''"""Golden test: keluaran program harus sama persis dengan keluaran yang sudah diverifikasi."""
import subprocess
import sys
from pathlib import Path

AKAR = Path(__file__).resolve().parents[1]


def test_keluaran_sesuai_contoh() -> None:
    hasil = subprocess.run([sys.executable, str(AKAR / "{utama}")], capture_output=True, text=True, check=True, timeout=60)
    harapan = (AKAR / "tests" / "keluaran_contoh.txt").read_text(encoding="utf-8")
    assert hasil.stdout.strip() == harapan.strip()


def test_program_tidak_menulis_ke_stderr() -> None:
    hasil = subprocess.run([sys.executable, str(AKAR / "{utama}")], capture_output=True, text=True, check=True, timeout=60)
    assert hasil.stderr == ""
'''])
        tambah.append(['.pre-commit-config.yaml', 'yaml', '''repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.4
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
'''])
        tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('test', [('Lint', 'uv run ruff check .'), ('Format', 'uv run ruff format --check .'),
                                                                         ('Tipe', 'uv run mypy .'), ('Test', 'uv run pytest')], PG if prof != 'python' or 'postgres' in stack.lower() else '', SETUP_PY)])
        tambah.append(['.gitignore', 'text', GI['python']])
        run = 'uv sync --all-groups          # pasang dependensi (atau: pip install -e ".[dev]")\n' + (
            'uv run python manage.py migrate\nuv run python manage.py runserver\n' if prof == 'django' else
            f'uv run fastapi dev {utama}\n' if prof == 'fastapi' else f'uv run python {utama}\n') + \
            'uv run ruff check . && uv run ruff format --check .\nuv run mypy .\nuv run pytest'
    elif prof in ('web', 'react', 'next', 'k6'):
        ts = prof in ('react', 'next') or any(f[0].endswith(('.ts', '.tsx')) for f in files)
        skrip = {'next': '"dev": "next dev", "build": "next build", "start": "next start"', 'react': '"dev": "vite", "build": "tsc -b && vite build", "preview": "vite preview"',
                 'web': '"dev": "vite", "build": "vite build", "preview": "vite preview"', 'k6': '"perf": "k6 run perf/flash-sale.js"'}[prof]
        dep = {'next': '"next": "^15.0.3", "react": "^19.0.0", "react-dom": "^19.0.0"', 'react': '"react": "^19.0.0", "react-dom": "^19.0.0"', 'web': '', 'k6': ''}[prof]
        for k, v in [('@tanstack/react-query', '^5.59.0'), ('@prisma/client', '^5.22.0'), ('recharts', '^2.13.0'), ('react-router-dom', '^7.0.1'), ('dexie', '^4.0.9'),
                     ('ai', '^4.0.0'), ('@ai-sdk/anthropic', '^1.0.0'), ('@ai-sdk/react', '^1.0.0'), ('drizzle-orm', '^0.36.0'), ('zod', '^3.23.8')]:
            if k in code:
                dep += (', ' if dep else '') + f'"{k}": "{v}"'
        dev = '"eslint": "^9.14.0", "@eslint/js": "^9.14.0", "prettier": "^3.3.3", "vitest": "^2.1.4", "@playwright/test": "^1.48.2", "@axe-core/playwright": "^4.10.0"'
        if ts:
            dev += ', "typescript": "^5.6.3", "typescript-eslint": "^8.13.0"'
        if prof in ('react', 'web'):
            dev += ', "vite": "^5.4.10"' + (', "@vitejs/plugin-react": "^4.3.3"' if prof == 'react' else '')
        if prof == 'web':
            dev += ', "html-validate": "^8.24.2"'
        tipe = ', "typecheck": "tsc --noEmit"' if ts else ''
        tambah.append(['package.json', 'json', f'''{{
  "name": "{nama}",
  "private": true,
  "type": "module",
  "scripts": {{
    {skrip},
    "lint": "eslint . && prettier --check ."{tipe},
    "test": "vitest run",
    "test:e2e": "playwright test"
  }},
  "dependencies": {{ {dep} }},
  "devDependencies": {{ {dev} }}
}}
''' if 'package.json' not in ada else None])
        if ts and 'tsconfig.json' not in ada:
            tambah.append(['tsconfig.json', 'json', '''{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["DOM", "DOM.Iterable", "ES2022"],
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "skipLibCheck": true,
    "noEmit": true,
    "paths": { "@/*": ["./*"] }
  },
  "include": ["**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules", "dist", ".next"]
}
'''])
        tambah.append(['eslint.config.js', 'js', ("import js from '@eslint/js';\nimport tseslint from 'typescript-eslint';\n\nexport default tseslint.config(\n  { ignores: ['dist', '.next', 'node_modules'] },\n  js.configs.recommended,\n  ...tseslint.configs.strict,\n);\n"
                                                  if ts else "import js from '@eslint/js';\nimport globals from 'globals';\n\nexport default [\n  { ignores: ['dist', 'node_modules'] },\n  js.configs.recommended,\n  { languageOptions: { globals: { ...globals.browser } } },\n];\n")])
        tambah.append(['.prettierrc.json', 'json', '{ "singleQuote": true, "printWidth": 100, "trailingComma": "all" }\n'])
        if not any('/tests/' in '/' + f[0] or f[0].endswith('.spec.ts') for f in files) and prof != 'k6':
            tambah.append(['tests/a11y.spec.' + ('ts' if ts else 'js'), 'ts' if ts else 'js', f'''import {{ test, expect }} from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

for (const lebar of [360, 768, 1440]) {{
  test(`halaman utama rapi dan aksesibel di ${{lebar}}px`, async ({{ page }}) => {{
    await page.setViewportSize({{ width: lebar, height: 900 }});
    await page.goto('/');
    const lebarDokumen = await page.evaluate(() => document.documentElement.scrollWidth);
    expect(lebarDokumen).toBeLessThanOrEqual(lebar);          // tidak ada scroll horizontal
    const hasil = await new AxeBuilder({{ page }}).withTags(['wcag2a', 'wcag2aa', 'wcag22aa']).analyze();
    expect(hasil.violations).toEqual([]);
  }});
}}
'''])
            tambah.append(['playwright.config.' + ('ts' if ts else 'js'), 'ts' if ts else 'js', f'''import {{ defineConfig }} from '@playwright/test';

export default defineConfig({{
  testDir: 'tests',
  use: {{ baseURL: 'http://localhost:{3000 if prof == 'next' else 5173}', trace: 'retain-on-failure' }},
  webServer: {{ command: 'npm run {'build && npm run start' if prof == 'next' else 'dev'}', port: {3000 if prof == 'next' else 5173}, reuseExistingServer: !process.env.CI }},
}});
'''])
        langkah = [('Lint', 'npm run lint')] + ([('Tipe', 'npm run typecheck')] if ts else []) + [('Unit test', 'npm test -- --passWithNoTests')]
        if prof == 'k6':
            langkah = [('Lint', 'npm run lint'), ('Uji performa (smoke)', 'docker run --rm -i grafana/k6 run --vus 1 --duration 10s - < perf/flash-sale.js')]
        else:
            langkah += [('Build', 'npm run build'), ('E2E + aksesibilitas', 'npx playwright install --with-deps chromium && npm run test:e2e')]
        tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('web', langkah, PG if 'prisma' in code.lower() or 'drizzle' in code else '', SETUP_NODE)])
        tambah.append(['.gitignore', 'text', GI['node']])
        run = 'npm install\n' + ('npx prisma migrate dev && npx prisma db seed\n' if 'prisma' in code.lower() else '') + \
              ('npm run perf\n' if prof == 'k6' else 'npm run dev\n') + 'npm run lint' + (' && npm run typecheck' if ts else '') + '\nnpm test\nnpm run test:e2e'
    elif prof in ('java', 'spring'):
        sb = prof == 'spring'
        dep = ('''    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-web</artifactId></dependency>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-validation</artifactId></dependency>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-data-jpa</artifactId></dependency>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-actuator</artifactId></dependency>
    <dependency><groupId>org.flywaydb</groupId><artifactId>flyway-database-postgresql</artifactId></dependency>
    <dependency><groupId>org.postgresql</groupId><artifactId>postgresql</artifactId><scope>runtime</scope></dependency>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-test</artifactId><scope>test</scope></dependency>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-testcontainers</artifactId><scope>test</scope></dependency>
    <dependency><groupId>org.testcontainers</groupId><artifactId>postgresql</artifactId><scope>test</scope></dependency>
''' if sb else '''    <dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter</artifactId><version>5.11.3</version><scope>test</scope></dependency>
    <dependency><groupId>org.assertj</groupId><artifactId>assertj-core</artifactId><version>3.26.3</version><scope>test</scope></dependency>
''')
        induk = '''  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.3.5</version>
  </parent>
''' if sb else ''
        tambah.append(['pom.xml', 'html', f'''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
{induk}  <groupId>id.ruangkode</groupId>
  <artifactId>{nama}</artifactId>
  <version>1.0.0</version>
  <properties>
    <java.version>21</java.version>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>
  <dependencies>
{dep}  </dependencies>
  <build>
    <plugins>
{'      <plugin><groupId>org.springframework.boot</groupId><artifactId>spring-boot-maven-plugin</artifactId></plugin>' + chr(10) if sb else '      <plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-surefire-plugin</artifactId><version>3.5.2</version></plugin>' + chr(10)}      <plugin>
        <groupId>com.diffplug.spotless</groupId>
        <artifactId>spotless-maven-plugin</artifactId>
        <version>2.43.0</version>
        <configuration><java><googleJavaFormat/></java></configuration>
        <executions><execution><goals><goal>check</goal></goals></execution></executions>
      </plugin>
    </plugins>
  </build>
</project>
'''])
        if out is not None and not sb and utama.endswith('Main.java'):
            tambah.append(['src/test/resources/keluaran_contoh.txt', 'text', out.rstrip() + '\n'])
            tambah.append(['src/test/java/MainTest.java', 'java', '''import static org.assertj.core.api.Assertions.assertThat;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import org.junit.jupiter.api.Test;

/** Golden test: keluaran Main harus sama dengan keluaran yang sudah diverifikasi. */
class MainTest {

  @Test
  void keluaranSesuaiContoh() throws Exception {
    PrintStream asli = System.out;
    ByteArrayOutputStream tangkap = new ByteArrayOutputStream();
    System.setOut(new PrintStream(tangkap, true, StandardCharsets.UTF_8));
    try {
      Main.main(new String[0]);
    } finally {
      System.setOut(asli);
    }
    String harapan = Files.readString(Path.of("src/test/resources/keluaran_contoh.txt"));
    assertThat(tangkap.toString(StandardCharsets.UTF_8).strip()).isEqualTo(harapan.strip());
  }
}
'''])
        tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('build', [('Format', 'mvn -B spotless:check'), ('Build + test', 'mvn -B verify')], '', SETUP_JAVA)])
        tambah.append(['.gitignore', 'text', GI['java']])
        run = ('mvn spring-boot:run          # butuh PostgreSQL; atau docker compose up\n' if sb else 'mvn -q compile exec:java -Dexec.mainClass=Main\n') + 'mvn spotless:apply           # rapikan format\nmvn verify                   # test + pemeriksaan'
    elif prof == 'flutter':
        if 'pubspec.yaml' not in ada:
            dep = ''.join(f'  {k}: {v}\n' for k, v in [('flutter_riverpod', '^2.6.1'), ('go_router', '^14.6.0'), ('dio', '^5.7.0'), ('flutter_bloc', '^8.1.6'),
                                                      ('shared_preferences', '^2.3.3'), ('drift', '^2.21.0'), ('web_socket_channel', '^3.0.1'), ('intl', '^0.19.0')] if k.split('_')[0] in code or k in code)
            tambah.append(['pubspec.yaml', 'yaml', f'''name: {nama.replace('-', '_')}
description: Kode final proyek Ruang Kode.
publish_to: none
version: 1.0.0+1

environment:
  sdk: ^3.5.0

dependencies:
  flutter:
    sdk: flutter
{dep}
dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^5.0.0
  mocktail: ^1.0.4

flutter:
  uses-material-design: true
'''])
        tambah.append(['analysis_options.yaml', 'yaml', '''include: package:flutter_lints/flutter.yaml

analyzer:
  language:
    strict-casts: true
    strict-inference: true
    strict-raw-types: true

linter:
  rules:
    - prefer_const_constructors
    - prefer_final_locals
    - require_trailing_commas
    - avoid_print
    - use_build_context_synchronously
'''])
        if '.github/workflows/mobile.yml' not in ada:
            tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('flutter', [('Format', 'dart format --output=none --set-exit-if-changed .'), ('Analyze', 'flutter analyze'),
                                                                             ('Test', 'flutter test --coverage')], '', SETUP_FLUTTER)])
        tambah.append(['.gitignore', 'text', GI['flutter']])
        run = 'flutter create . --platforms=android,ios   # sekali, membuat folder platform\nflutter pub get\nflutter run\ndart format .\nflutter analyze\nflutter test'
    elif prof in ('android', 'kmp'):
        if 'gradle/libs.versions.toml' not in ada:
            tambah.append(['gradle/libs.versions.toml', 'toml', '''[versions]
agp = "8.7.2"
kotlin = "2.0.21"
compose-bom = "2024.10.01"
lifecycle = "2.8.7"
coroutines = "1.9.0"
detekt = "1.23.7"

[libraries]
compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }
compose-material3 = { group = "androidx.compose.material3", name = "material3" }
lifecycle-viewmodel-compose = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-compose", version.ref = "lifecycle" }
coroutines-test = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-test", version.ref = "coroutines" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-multiplatform = { id = "org.jetbrains.kotlin.multiplatform", version.ref = "kotlin" }
compose-compiler = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
detekt = { id = "io.gitlab.arturbosch.detekt", version.ref = "detekt" }
'''])
        tambah.append(['config/detekt.yml', 'yaml', '''build:
  maxIssues: 0
complexity:
  LongMethod:
    threshold: 60          # composable boleh sedikit lebih panjang
  LongParameterList:
    functionThreshold: 8
naming:
  FunctionNaming:
    ignoreAnnotated: ['Composable']
style:
  MagicNumber:
    ignorePropertyDeclaration: true
'''])
        tambah.append(['.editorconfig', 'conf', '[*.{kt,kts}]\nindent_size = 4\nmax_line_length = 120\nktlint_code_style = android_studio\nktlint_function_naming_ignore_when_annotated_with = Composable\n'])
        tugas = './gradlew detekt lint testDebugUnitTest' if prof == 'android' else './gradlew detekt allTests'
        tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('android', [('Lint + test', tugas), ('Build', './gradlew assembleDebug' if prof == 'android' else './gradlew :shared:build')], '', SETUP_GRADLE)])
        tambah.append(['.gitignore', 'text', GI['gradle']])
        run = ('./gradlew installDebug       # pasang ke emulator/HP\n' if prof == 'android' else './gradlew :androidApp:installDebug\nopen iosApp/iosApp.xcodeproj   # jalankan dari Xcode untuk iOS\n') + tugas
    elif prof == 'sql':
        tambah.append(['.sqlfluff', 'conf', '[sqlfluff]\ndialect = postgres\ntemplater = raw\nmax_line_length = 120\n\n[sqlfluff:rules:capitalisation.keywords]\ncapitalisation_policy = upper\n'])
        sqls = [f[0] for f in files if f[0].endswith('.sql')]
        if out is not None:
            tambah.append(['tests/keluaran_contoh.txt', 'text', out.rstrip() + '\n'])
        tambah.append(['docker-compose.yml', 'yaml', '''services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: app
    ports: ["5432:5432"]
    volumes:
      - ./db:/docker-entrypoint-initdb.d:ro   # berkas .sql dijalankan otomatis saat pertama kali
'''])
        jalan = ' && '.join(f'psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f {p}' for p in sqls) or 'echo "tidak ada berkas SQL"'
        tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('sql', [('Lint SQL', 'pipx run sqlfluff lint .'), ('Jalankan skrip di PostgreSQL 16', jalan)], PG)])
        tambah.append(['.gitignore', 'text', GI['umum']])
        run = 'docker compose up -d          # PostgreSQL 16 lokal\n' + '\n'.join(f'psql postgresql://postgres:postgres@localhost:5432/app -v ON_ERROR_STOP=1 -f {p}' for p in sqls) + '\npipx run sqlfluff lint .'
    elif prof == 'terraform':
        tambah.append(['.tflint.hcl', 'hcl', 'plugin "terraform" {\n  enabled = true\n  preset  = "recommended"\n}\n\nplugin "google" {\n  enabled = true\n  version = "0.30.0"\n  source  = "github.com/terraform-linters/tflint-ruleset-google"\n}\n'])
        if '.github/workflows/data-ci.yml' not in ada:
            tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('terraform', [('Format', 'terraform fmt -check -recursive'), ('Validate', 'cd infra/terraform && terraform init -backend=false && terraform validate'),
                                                                                ('Keamanan', 'pipx run checkov -d infra')], '', '      - uses: hashicorp/setup-terraform@v3\n')])
        tambah.append(['.gitignore', 'text', GI['terraform']])
        run = 'cd infra/terraform\nterraform init\nterraform fmt -recursive && terraform validate\ntflint --init && tflint\nterraform plan -out rencana.tfplan\nterraform apply rencana.tfplan'
    elif prof == 'infra':
        tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('validasi', [('Lint YAML', 'pipx run yamllint .'), ('Skema Kubernetes', 'docker run --rm -v "$PWD:/w" ghcr.io/yannh/kubeconform:latest -strict -ignore-missing-schemas -summary /w'),
                                                                            ('Keamanan', 'pipx run checkov -d .')])])
        tambah.append(['.yamllint.yml', 'yaml', 'extends: default\nrules:\n  line-length: { max: 140 }\n  document-start: disable\n'])
        tambah.append(['.gitignore', 'text', GI['umum']])
        run = 'kubectl apply --dry-run=server -f ' + utama + '\nkubectl apply -f ' + utama + '\nkubectl get pods -w'
    else:  # docs
        tambah.append(['.github/workflows/ci.yml', 'yaml', _ci('dokumen', [('Lint Markdown', 'npx --yes markdownlint-cli2 "**/*.md"'), ('Cek tautan', 'npx --yes markdown-link-check README.md')])])
        tambah.append(['.gitignore', 'text', GI['umum']])
        run = 'npx markdownlint-cli2 "**/*.md"'
    return [t for t in tambah if t and t[0] not in ada], run


def _tree(nama, paths):
    pohon = {}
    for p in sorted(paths, key=lambda x: (x.count('/') == 0, x)):
        n = pohon
        for b in p.split('/'):
            n = n.setdefault(b, {})
    baris = [nama + '/']

    def jalan(n, awal):
        kunci = sorted(n, key=lambda k: (not n[k], k.lower()))
        for i, k in enumerate(kunci):
            akhir = i == len(kunci) - 1
            baris.append(awal + ('└── ' if akhir else '├── ') + k + ('/' if n[k] else ''))
            jalan(n[k], awal + ('    ' if akhir else '│   '))
    jalan(pohon, '')
    return '\n'.join(baris)


def paket(jenis, judul, masalah, wajib, langkah, code, lang, out=None, stack='', standar=None, arsitektur=None):
    """Kembalikan dict `fin` untuk komponen kode final."""
    files = pecah(code, lang)
    prof = profil(lang, stack, files)
    nama = _slug(judul)
    tambah, run = _kerangka(prof, nama, lang, files, code, out, stack)
    env = _env(code)
    if env:
        tambah.append(['.env.example', 'conf', '# Salin menjadi .env lalu isi. Jangan commit berkas .env.\n' + ''.join(f'{n}=\n' for n in env)])
    semua = files + tambah
    std = polos(standar) if standar else ''
    readme = (f'# {polos(judul)}\n\n## Masalah\n{polos(masalah)}\n\n## Fitur wajib\n' + ''.join(f'- [x] {polos(w)}\n' for w in wajib)
              + (f'\n## Stack\n{polos(stack)}\n' if stack else '')
              + ('\n## Arsitektur\n| Bagian | Isi |\n|---|---|\n' + ''.join(f'| {polos(a)} | {polos(b)} |\n' for a, b in arsitektur) if arsitektur else '')
              + f'\n## Menjalankan\n```bash\n{run}\n```\n'
              + ('\n## Keluaran contoh\n```\n' + out.rstrip() + '\n```\n' if out else '')
              + '\n## Keputusan teknis\n' + ''.join(f'{i + 1}. {polos(s)}\n' for i, s in enumerate(langkah))
              + (f'\n## Standar yang dipenuhi\n{std}\n' if std else '')
              + ('\n## Variabel lingkungan\nSalin `.env.example` menjadi `.env`, isi nilainya. Rahasia tidak pernah di-commit.\n' if env else ''))
    if 'README.md' not in {f[0] for f in semua}:
        semua.append(['README.md', 'text', readme])
    cek = [[f'Fitur wajib {i + 1}', polos(w)] for i, w in enumerate(wajib)] + CEK_PROFIL.get(prof, []) + CEK_UMUM
    if std:
        cek.insert(len(wajib), ['Standar proyek', std])
    cek = [[a, polos(b)] for a, b in cek]
    if jenis == 'mini':
        n = ('Ini penyelesaian lengkap proyek mini, ditata seperti repositori tim industri: kode dipisah per berkas, ada uji otomatis, lint/format, CI GitHub Actions, dan README. '
             'Bandingkan dengan kodemu memakai checklist di bawah; perbedaan nama atau gaya boleh, perbedaan perilaku dan standar tidak.')
    else:
        n = ('Ini penyelesaian proyek besar dalam bentuk repositori industri: berkas inti setiap fitur wajib (yang paling sering salah dikerjakan), konfigurasi proyek, uji, CI, dan README dengan keputusan teknis. '
             'Bagian yang berulang (misalnya halaman atau endpoint lain yang polanya sama) tidak ditulis ulang; ikuti pola berkas inti. Pakai checklist untuk code review kodemu.')
    return {'n': n, 'tree': _tree(nama, [f[0] for f in semua]), 'files': semua, 'run': run, 'cek': cek}
