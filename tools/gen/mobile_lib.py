"""Pembantu kecil untuk menulis pelajaran jalur mobile dan framework CSS."""


def q(question, opts, ans, why):
    return [question, opts, ans, why]


def C(t, b, code=None, out=None, lang=None, tb=None, pts=None, qs=None, so=None, nodes=None, viz=None):
    d = {'k': 'c', 't': t, 'nodes': nodes or [], 'b': b}
    if lang: d['lang'] = lang
    if code is not None: d['code'] = code
    if out is not None:
        d['out'] = out
        d['run'] = False  # keluaran contoh: kode Dart/Kotlin tidak dijalankan di browser
    if tb: d['tb'] = tb
    if viz: d['viz'] = viz
    if so: d['so'] = so
    if pts: d['pts'] = pts
    if qs: d['q'] = qs
    return d


def W(t, b, html, css=None, js=None, fw=None, task=None, pts=None, qs=None, nodes=None):
    d = {'k': 'w', 't': t, 'nodes': nodes or [], 'b': b, 'html': html}
    if css is not None: d['css'] = css
    if js is not None: d['js'] = js
    if fw: d[fw] = True
    if task: d['task'] = task
    if pts: d['pts'] = pts
    if qs: d['q'] = qs
    return d


def M(t, lvl, d, nodes, lessons):
    return {'t': t, 'lvl': lvl, 'd': d, 'nodes': nodes, 'lessons': lessons}
