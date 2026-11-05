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
