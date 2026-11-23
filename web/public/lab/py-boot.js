/* Menjalankan Python (Pyodide) di iframe sandbox. Halaman induk hanya menerima teks keluaran dan SVG grafik. */
(function () {
  var PY = null;
  var BASE = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
  function post(m) { parent.postMessage(Object.assign({ rkPy: 1 }, m), "*"); }
  function loadPy() {
    if (PY) return PY;
    PY = new Promise(function (res, rej) {
      var s = document.createElement("script");
      s.src = BASE + "pyodide.js";
      var to = setTimeout(function () { rej(new Error("waktu habis")); }, 60000);
      s.onload = function () { loadPyodide({ indexURL: BASE }).then(function (p) { clearTimeout(to); res(p); }, rej); };
      s.onerror = function () { rej(new Error("Pyodide tidak bisa diunduh")); };
      document.head.appendChild(s);
    });
    PY.catch(function () { PY = null; });
    return PY;
  }
  async function run(id, code) {
    var out = "";
    var push = function (s) { out += s + "\n"; post({ id: id, out: out }); };
    var py;
    try { post({ id: id, status: "Memuat Python di browser (sekali saja, sekitar 10 MB)…" }); py = await loadPy(); }
    catch (e) { post({ id: id, done: 1, err: 1, out: "Python di browser tidak bisa dimuat: " + e.message + ". Periksa koneksi internet lalu coba lagi." }); return; }
    py.setStdout({ batched: push }); py.setStderr({ batched: push });
    var bad = [];
    await py.loadPackagesFromImports(code, {
      messageCallback: function (m) { if (/^Loading /.test(m)) post({ id: id, status: "Memuat paket " + m.slice(8) + "…" }); },
      errorCallback: function (m) { bad.push(m); }
    });
    if (bad.length) { post({ id: id, done: 1, err: 1, out: "Paket yang dibutuhkan gagal diunduh. Periksa koneksi lalu jalankan lagi." }); return; }
    out = "";
    var g = py.globals.get("dict")();
    var figs = [], err = 0;
    if (/matplotlib|pyplot/.test(code)) py.runPython("import os\nos.environ['MPLBACKEND']='Agg'");
    try { await py.runPythonAsync(code, { globals: g }); }
    catch (e) {
      err = 1;
      var m = String(e.message || e).trim().split("\n"), i = m.findIndex(function (s) { return /^\s*File "<exec>"/.test(s); });
      push(i >= 0 ? ["Traceback (most recent call last):"].concat(m.slice(i)).join("\n") : m.slice(-2).join("\n"));
    } finally { g.destroy && g.destroy(); }
    if (/matplotlib|pyplot/.test(code)) {
      try {
        var r = py.runPython("import sys,io\n_rk=[]\nif 'matplotlib.pyplot' in sys.modules:\n  import matplotlib.pyplot as _p\n  for _n in _p.get_fignums():\n    _b=io.StringIO();_p.figure(_n).savefig(_b,format='svg',bbox_inches='tight');_rk.append(_b.getvalue())\n  _p.close('all')\n_rk");
        figs = r.toJs(); r.destroy && r.destroy();
      } catch (e) { figs = []; }
    }
    post({ id: id, done: 1, err: err, out: out, figs: figs });
  }
  addEventListener("message", function (e) {
    if (e.source !== parent) return;
    var d = e.data || {};
    if (typeof d.run === "string" && d.id) run(d.id, d.run);
  });
  post({ ready: 1 });
})();
