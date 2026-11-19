"""Pembantu jalur roadmap baru. P() membuat pelajaran Python yang bisa dijalankan;
keluarannya dihitung saat generate dengan menjalankan kodenya, jadi selalu cocok."""
import io, contextlib
from mobile_lib import C, M, q
from mobile_dart_x import S


def jalan(code):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(code, '<pelajaran>', 'exec'), {'__name__': '__main__'})
    return buf.getvalue().rstrip('\n')


def P(t, b, code, tb=None, pts=None, qs=None, so=None, nodes=None, viz=None):
    d = C(t, b, code, None, 'python', tb, pts, qs, so, nodes, viz)
    d['out'] = jalan(code)
    return d


def SP(soal, petunjuk, jawab):
    """Soal Python: jawaban dijalankan untuk mendapatkan keluaran."""
    return S(soal, petunjuk, jawab, jalan(jawab), lang='python')


def X(soal, petunjuk, jawab, lang, out=None):
    return S(soal, petunjuk, jawab, out, lang=lang)


def jalan_plot(code):
    """Jalankan kode yang memakai Matplotlib; kembalikan (keluaran teks, [svg tiap gambar])."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt, re as _re
    plt.close('all')
    plt.rcParams.update({'svg.fonttype': 'none', 'svg.hashsalt': 'rk', 'figure.dpi': 100})
    teks = jalan(code)
    svgs = []
    for n in plt.get_fignums():
        b = io.StringIO()
        plt.figure(n).savefig(b, format='svg', bbox_inches='tight', metadata={'Date': None, 'Creator': None})
        s = b.getvalue()
        s = s[s.index('<svg'):]
        s = _re.sub(r'<metadata>.*?</metadata>', '', s, flags=_re.S)
        s = _re.sub(r'>\s+<', '><', s)
        s = _re.sub(r'(\d+\.\d{2})\d+', r'\1', s)
        svgs.append(s)
    plt.close('all')
    return teks, svgs


def PF(t, b, code, tb=None, pts=None, qs=None, so=None, nodes=None, viz=None):
    """Pelajaran Python yang menghasilkan grafik: gambar disimpan sebagai SVG di l.fig."""
    d = C(t, b, code, None, 'python', tb, pts, qs, so, nodes, viz)
    d['out'], figs = jalan_plot(code)
    if figs: d['fig'] = figs
    return d


def T(t, b, code, lang='text', tb=None, pts=None, qs=None, so=None, nodes=None, out=None):
    """Pelajaran konsep dengan contoh yang tidak dijalankan (perintah terminal, Dockerfile, dsb.)."""
    return C(t, b, code, out, lang, tb, pts, qs, so, nodes)
