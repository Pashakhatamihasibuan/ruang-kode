/* Pratinjau kode HTML/CSS/JS siswa. Iframe ini sandbox (asal data buram), jadi kode siswa
   tidak bisa membaca cookie, localStorage, atau DOM situs induk. */
(function () {
  addEventListener("message", function f(e) {
    if (e.source !== parent) return;
    var d = e.data || {};
    if (typeof d.doc !== "string") return;
    removeEventListener("message", f);
    document.open();
    document.write(d.doc);
    document.close();
  });
  parent.postMessage({ rkWeb: 1, ready: 1 }, "*");
})();
