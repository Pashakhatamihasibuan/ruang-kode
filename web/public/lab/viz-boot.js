/* Jembatan halaman pelajaran <-> visual lama. Berjalan di iframe sandbox tanpa akses ke situs induk. */
(function () {
  var host = document.getElementById("host");
  var last = 0;
  function size() {
    var h = Math.ceil(document.documentElement.scrollHeight);
    if (h !== last) { last = h; parent.postMessage({ rkViz: 1, h: h }, "*"); }
  }
  if (window.ResizeObserver) new ResizeObserver(size).observe(document.body);
  addEventListener("message", function (e) {
    if (e.source !== parent) return;
    var d = e.data || {};
    if (d.theme) {
      if (d.theme === "auto") delete document.documentElement.dataset.theme;
      else document.documentElement.dataset.theme = d.theme;
    }
    if (d.v3 && window.V3D) {
      host.innerHTML = "";
      host.className = "vizhost v3host";
      try { window.V3D(host, d.v3, d.v3p || null); }
      catch (err) { host.textContent = "Visual tidak bisa dimuat: " + err.message; }
      size();
    }
    if (d.viz && window.VIZ2 && window.VIZ2[d.viz]) {
      host.innerHTML = "";
      try { VLANG = d.lang || null; } catch (err) {}
      try { window.VIZ2[d.viz](host, { lang: d.lang, lesson: d.lesson || {} }); }
      catch (err) { host.textContent = "Visual tidak bisa dimuat: " + err.message; }
      size();
    }
  });
  parent.postMessage({ rkViz: 1, ready: 1 }, "*");
})();
