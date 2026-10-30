"""Membuat src/js/bugs.js: latihan "perbaiki kode yang error" untuk setiap pelajaran berkode.

Dari contoh kode yang benar, skrip ini membuat satu kesalahan yang khas pemula (titik dua hilang,
titik koma hilang, salah ketik nama variabel, kurung tidak ditutup, kata kunci salah eja),
lalu MENJALANKAN kode rusak itu dan menyimpan pesan error aslinya. Kesalahan yang ternyata tidak
memicu error dilewati. Jalankan dari akar repo: python3 tools/gen/bugs.py
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tips import J_PRE, ROOT, HERE  # noqa: E402

JOFF = J_PRE.count("\n")
CONST_LANG = {"JAVA_MODULES": "java", "PY_MODULES": "python", "TS_MODULES": "ts", "FE0_MODULES": "js", "FE_MODULES": "js",
              "PDA_MODULES": "python", "DA_MODULES": "python", "DE_MODULES": "python", "BI_MODULES": "sql", "SQL_MODULES": "sql"}
CONST_KEY = {"JAVA_MODULES": "java", "PY_MODULES": "python", "TS_MODULES": "ts", "FE0_MODULES": "fe0", "FE_MODULES": "fe",
             "PDA_MODULES": "pda", "DA_MODULES": "da", "DE_MODULES": "de", "BI_MODULES": "bi", "SQL_MODULES": "sql"}

DUMP = r"""
const fs=require('fs'),vm=require('vm');global.document={addEventListener(){}};
for(const f of process.argv.slice(1))vm.runInThisContext(fs.readFileSync(f,'utf8').replace(/^const /gm,'var ').replace(/^let /gm,'var '));
const out=[];for(const c of %s)global[c].forEach(m=>m.lessons.forEach(l=>{if(l.k==='c'&&l.code&&l.out!=null&&l.run!==false)out.push({c,t:l.t,lang:l.lang||null,code:l.code})}));
process.stdout.write(JSON.stringify(out));
"""


def lessons():
    src = ROOT / "src/js"
    files = ["data.js", "util.js", "gl.js"] + [f for f in re.findall(r'"(track-[\w-]+\.js)"', (ROOT / "build.py").read_text())]
    r = subprocess.run(["node", "-e", DUMP % json.dumps(list(CONST_LANG)), *[str(src / f) for f in files]],
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


# ---------------------------------------------------------------- menjalankan kode rusak
def err_py(code):
    with tempfile.TemporaryDirectory() as d:
        Path(d, "main.py").write_text(code)
        r = subprocess.run(["python3", "main.py"], cwd=d, capture_output=True, text=True, timeout=30)
        if r.returncode == 0:
            return None
        lines = r.stderr.strip().splitlines()
        i = next((k for k, s in enumerate(lines) if s.strip().startswith('File "') and "main.py" in s), None)
        last = [s for s in lines[i:] if not s.strip().startswith(("^", "~"))] if i is not None else lines[-1:]
        return "\n".join(s.replace(d + "/", "") for s in last).strip()


def err_java(code):
    """Pelajaran Java berisi program utuh (public class ...); potongan tanpa kelas dibungkus dulu."""
    m = re.search(r"public\s+class\s+(\w+)", code)
    name, src, off = (m.group(1), code, 0) if m else ("Main", J_PRE + code + "\n  }\n}\n", JOFF)
    with tempfile.TemporaryDirectory() as d:
        Path(d, name + ".java").write_text(src)
        c = subprocess.run(["javac", name + ".java"], cwd=d, capture_output=True, text=True)
        if c.returncode == 0:
            r = subprocess.run(["java", name], cwd=d, capture_output=True, text=True, timeout=30)
            if r.returncode == 0:
                return None
            return "\n".join(x for x in r.stderr.splitlines() if not x.startswith(("\tat ", "Picked up")) and x.strip())
        msg = [x for x in c.stderr.splitlines() if not x.startswith("Picked up")]
        first = next(k for k, x in enumerate(msg) if re.match(re.escape(name) + r"\.java:\d+: error", x))
        out = msg[first:first + 3]
        out[0] = re.sub(re.escape(name) + r"\.java:(\d+)", lambda g: f"{name}.java:{int(g.group(1)) - off}", out[0])
        return "\n".join(out)


def err_ts(code):
    with tempfile.TemporaryDirectory() as d:
        Path(d, "main.ts").write_text(code)
        c = subprocess.run(["tsc", "--strict", "--noEmit", "--target", "es2022", "--module", "commonjs", "main.ts"], cwd=d, capture_output=True, text=True)
        if c.returncode == 0:
            return None
        return c.stdout.strip().splitlines()[0]


def err_js(code):
    with tempfile.TemporaryDirectory() as d:
        Path(d, "main.js").write_text(code)
        r = subprocess.run(["node", "main.js"], cwd=d, capture_output=True, text=True, timeout=30)
        if r.returncode == 0:
            return None
        keep = [x for x in r.stderr.splitlines() if not x.startswith("    at ") and not x.startswith("Node.js v") and x.strip()]
        return "\n".join(x.replace(d + "/", "") for x in keep).strip()


def err_sql(code, db):
    r = subprocess.run(["node", str(HERE / "sqlrun.js")], input=json.dumps({"db": db, "sql": code}), capture_output=True, text=True)
    if r.returncode == 0:
        return None
    m = re.search(r"SqlError: (.*)", r.stderr) or re.search(r"Error: (.*)", r.stderr)
    return m.group(1).strip() if m else r.stderr.strip().splitlines()[-1]


def sql_db(code):
    for db in ("toko", "bi"):
        if err_sql(code, db) is None:
            return db
    return None


# ---------------------------------------------------------------- jenis kesalahan
def mask(line, com):
    """Isi teks dan komentar diganti spasi, agar kesalahan tidak dibuat di dalamnya."""
    out, q, i = [], None, 0
    while i < len(line):
        c = line[i]
        if q:
            out.append(" ")
            if c == "\\":
                out.append(" ")
                i += 1
            elif c == q:
                q = None
        elif line.startswith(com, i):
            out.append(" " * (len(line) - i))
            break
        elif c in "\"'`":
            q = c
            out.append(" ")
        else:
            out.append(c)
        i += 1
    return "".join(out)


def typo(name):
    """Salah ketik yang wajar: satu huruf vokal di tengah hilang, atau dua huruf tertukar."""
    for i in range(len(name) - 2, 0, -1):
        if name[i] in "aiueo":
            return name[:i] + name[i + 1:]
    return name[:-2] + name[-1] + name[-2] if len(name) > 2 else name + name[-1]


def m_colon(lines, lang):
    for i, s in enumerate(lines):
        if re.match(r"\s*(def|for|if|while|class|elif|with)\b.*:\s*$", mask(s, "#")):
            return i, s.rstrip()[:-1], "colon"


def m_semicolon(lines, lang):
    for i, s in enumerate(lines):
        mk = mask(s, "//").rstrip()
        if mk.endswith(";") and not mk.strip().startswith("for") and i > 0:
            return i, s.rstrip()[:-1], "semicolon"


def m_typo(lines, lang):
    com = {"python": "#", "sql": "--"}.get(lang, "//")
    decl = {"python": r"^\s*([a-z_][a-z0-9_]{3,})\s*=[^=]",
            "java": r"^\s*(?:final\s+)?(?:int|double|long|String|boolean|var|char)(?:\[\])?\s+([a-z][A-Za-z0-9]{3,})\s*=",
            "js": r"^\s*(?:const|let|var)\s+([a-z][A-Za-z0-9]{3,})\s*=",
            "ts": r"^\s*(?:const|let)\s+([a-z][A-Za-z0-9]{3,})\s*(?::[^=]+)?=",
            "sql": None}[lang]
    if not decl:
        return None
    for i, s in enumerate(lines):
        m = re.match(decl, mask(s, com))
        if not m:
            continue
        name = m.group(1)
        for j in range(i + 1, len(lines)):
            mk = mask(lines[j], com)
            u = re.search(r"(?<![\w.])" + re.escape(name) + r"(?![\w])", mk)
            if u and not re.match(r"^\s*" + re.escape(name) + r"\s*=[^=]", mk):
                bad = lines[j][:u.start()] + typo(name) + lines[j][u.end():]
                return j, bad, "typo:" + name
    return None


def m_paren(lines, lang):
    com = {"python": "#"}.get(lang, "//")
    call = {"python": "print(", "java": "System.out.println(", "js": "console.log(", "ts": "console.log("}[lang]
    for i, s in enumerate(lines):
        mk = mask(s, com).rstrip()
        if mk.lstrip().startswith(call):
            end = mk.rfind(")")
            if end > 0 and mk.count("(") == mk.count(")"):
                return i, s[:end] + s[end + 1:], "paren"


def m_sqlkw(lines, lang):
    for i, s in enumerate(lines):
        mk = mask(s, "--")
        for kw, bad in (("FROM", "FORM"), ("GROUP BY", "GROUP"), ("SELECT", "SELET"), ("WHERE", "WHER")):
            u = re.search(r"\b" + kw + r"\b", mk)
            if u:
                return i, s[:u.start()] + bad + s[u.end():], "sqlkw:" + kw


ORDER = {"python": [m_colon, m_typo, m_paren], "java": [m_semicolon, m_typo, m_paren], "js": [m_typo, m_paren],
         "ts": [m_typo, m_paren], "sql": [m_sqlkw]}

WHY = {"colon": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua.",
       "semicolon": "Setiap statement Java diakhiri titik koma.",
       "paren": "Setiap kurung buka harus punya pasangan kurung tutup.",
       "typo": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil.",
       "sqlkw": "Kata kunci SQL harus dieja dengan benar."}


def make(L, idx):
    lang = L["lang"]
    code = L["code"]
    lines = code.split("\n")
    db = sql_db(code) if lang == "sql" else None
    if lang == "sql" and not db:
        return None
    fns = ORDER[lang]
    fns = fns[idx % len(fns):] + fns[:idx % len(fns)]
    for fn in fns:
        r = fn(lines, lang)
        if not r:
            continue
        i, bad, kind = r
        new = lines[:]
        new[i] = bad
        bcode = "\n".join(new)
        err = {"python": err_py, "java": err_java, "ts": err_ts, "js": err_js}[lang](bcode) if lang != "sql" else err_sql(bcode, db)
        if not err:
            continue
        base = kind.split(":")[0]
        return {"code": bcode, "err": err, "line": i + 1, "kind": base, "why": WHY[base]}
    return None


def main():
    out = {}
    for n, L in enumerate(lessons()):
        L["lang"] = L["lang"] or CONST_LANG[L["c"]]
        if L["lang"] not in ORDER:
            continue
        b = make(L, n)
        key = CONST_KEY[L["c"]] + ":" + L["t"]
        print(("✓" if b else "·"), key, "|", b and b["kind"])
        if b:
            out[key] = b
    tpl = (HERE / "bugs.tpl.js").read_text()
    (ROOT / "src/js/bugs.js").write_text(tpl.replace("%BUGS%", json.dumps(out, ensure_ascii=False, indent=0)))
    print(len(out), "latihan ditulis ke src/js/bugs.js")


if __name__ == "__main__":
    main()
