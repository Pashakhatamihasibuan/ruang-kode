"""Pendalaman jalur Vue: istilah dunia kerja, Single File Component siap pakai, dan logika reaktivitas yang dijalankan dengan Node."""
K = 'vue'


def V(t, code, b=None, lang='html'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def J(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang='js')


D = {
'Mengenal Vue dan membuat proyek': dict(
  ist=[('Progressive framework', 'Bisa dipakai sebagian di halaman lama atau penuh sebagai SPA.'),
       ('SFC (.vue)', 'Single File Component: <template>, <script setup>, dan <style scoped> dalam satu file.'),
       ('Composition API', 'Gaya modern Vue 3 dengan ref, computed, dan composable.'),
       ('Options API', 'Gaya lama (data, methods, computed); masih banyak di proyek warisan.'),
       ('create-vue', 'Perintah resmi membuat proyek Vue + Vite.')],
  cx=[V('Membuat proyek dan komponen pertama', r'''
npm create vue@latest toko-vue      # pilih: TypeScript, Router, Pinia, Vitest, ESLint
cd toko-vue && npm install && npm run dev

<!-- src/components/SapaPengguna.vue -->
<script setup lang="ts">
import { ref } from "vue";
const props = defineProps<{ nama: string }>();
const jumlahKlik = ref(0);
</script>

<template>
  <section class="sapa">
    <h2>Halo, {{ props.nama }}!</h2>
    <button @click="jumlahKlik++">Diklik {{ jumlahKlik }} kali</button>
  </section>
</template>

<style scoped>
.sapa { padding: 1rem; border-radius: 12px; background: #ecfdf5; }
</style>'''),
      V('Options API vs Composition API (komponen yang sama)', r'''
<!-- Options API (Vue 2 / proyek lama) -->
<script>
export default {
  data() { return { qty: 1 } },
  computed: { total() { return this.qty * this.harga } },
  props: ["harga"],
  methods: { tambah() { this.qty++ } },
}
</script>

<!-- Composition API (Vue 3, direkomendasikan) -->
<script setup lang="ts">
import { ref, computed } from "vue";
const props = defineProps<{ harga: number }>();
const qty = ref(1);
const total = computed(() => qty.value * props.harga);
const tambah = () => qty.value++;
</script>''')]),

'Template syntax dan direktif': dict(
  ist=[('Interpolation {{ }}', 'Menampilkan nilai JavaScript sebagai teks (otomatis di-escape).'),
       ('v-bind (:)', 'Mengikat atribut ke data: :src, :class, :disabled.'),
       ('v-on (@)', 'Memasang event: @click, @submit.prevent, @keyup.enter.'),
       ('v-if / v-show', 'v-if menghapus dari DOM; v-show hanya menyembunyikan dengan CSS.'),
       ('v-for + :key', 'Merender daftar; key wajib unik dan stabil.')],
  cx=[V('Daftar produk dengan filter dan kelas dinamis', r'''
<script setup lang="ts">
import { ref, computed } from "vue";
type Produk = { id: number; nama: string; harga: number; stok: number };
const produk = ref<Produk[]>([
  { id: 1, nama: "Kopi Gayo", harga: 65000, stok: 4 },
  { id: 2, nama: "Teh Melati", harga: 18000, stok: 0 },
  { id: 3, nama: "Kopi Toraja", harga: 72000, stok: 12 },
]);
const hanyaTersedia = ref(false);
const tampil = computed(() => produk.value.filter((p) => !hanyaTersedia.value || p.stok > 0));
const rp = (n: number) => "Rp" + n.toLocaleString("id-ID");
</script>

<template>
  <label><input type="checkbox" v-model="hanyaTersedia" /> Hanya yang tersedia</label>
  <p v-if="tampil.length === 0">Tidak ada produk.</p>
  <ul v-else>
    <li v-for="p in tampil" :key="p.id" :class="{ habis: p.stok === 0, menipis: p.stok > 0 && p.stok < 5 }">
      {{ p.nama }} - {{ rp(p.harga) }}
      <small v-show="p.stok > 0 && p.stok < 5">Sisa {{ p.stok }}!</small>
      <button :disabled="p.stok === 0" @click="$emit('tambah', p)">Tambah</button>
    </li>
  </ul>
</template>'''),
      J('Compiler template mini: dari {{ }} ke string', r'''
function kompilasi(templat) {
  return (ctx) => templat.replace(/\{\{\s*([^}]+?)\s*\}\}/g, (_, ekspr) => {
    const nilai = new Function(...Object.keys(ctx), `return (${ekspr});`)(...Object.values(ctx));
    return String(nilai).replace(/[<>&]/g, (c) => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;" })[c]);
  });
}
const render = kompilasi("<h2>Halo, {{ nama }}!</h2><p>Total: {{ (qty * harga).toLocaleString('id-ID') }}</p><p>{{ catatan }}</p>");
console.log(render({ nama: "Rina", qty: 3, harga: 45000, catatan: "<script>alert(1)</script>" }));
''', 'Interpolasi Vue selalu meng-escape HTML. Hanya v-html yang menyisipkan HTML mentah, jadi jangan pernah mengisinya dengan data pengguna.')]),

'Form dan v-model': dict(
  ist=[('v-model', 'Two-way binding: nilai input dan state selalu sinkron.'),
       ('Modifier', '.trim, .number, .lazy untuk mengolah nilai otomatis.'),
       ('defineModel', 'Makro Vue 3.4+ agar komponen kustom mendukung v-model dengan mudah.'),
       ('VeeValidate + Zod', 'Kombinasi populer untuk validasi form di Vue.')],
  cx=[V('Form pendaftaran kursus dengan validasi', r'''
<script setup lang="ts">
import { reactive, computed } from "vue";
const form = reactive({ nama: "", email: "", umur: null as number | null, kelas: "frontend", setuju: false });
const error = computed(() => ({
  nama: form.nama.length < 3 ? "Nama minimal 3 huruf" : "",
  email: /^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(form.email) ? "" : "Format email belum benar",
  umur: form.umur && form.umur >= 15 ? "" : "Umur minimal 15 tahun",
  setuju: form.setuju ? "" : "Centang persetujuan",
}));
const valid = computed(() => Object.values(error.value).every((e) => !e));
</script>

<template>
  <form @submit.prevent="valid && kirim(form)" novalidate>
    <input v-model.trim="form.nama" placeholder="Nama lengkap" />
    <small>{{ error.nama }}</small>
    <input v-model.trim="form.email" type="email" />
    <small>{{ error.email }}</small>
    <input v-model.number="form.umur" type="number" min="10" />
    <select v-model="form.kelas">
      <option value="frontend">Frontend</option>
      <option value="backend">Backend</option>
    </select>
    <label><input type="checkbox" v-model="form.setuju" /> Saya setuju data dipakai untuk pendaftaran</label>
    <button :disabled="!valid">Daftar</button>
  </form>
</template>'''),
      V('Komponen input kustom dengan defineModel', r'''
<!-- InputRupiah.vue -->
<script setup lang="ts">
const nilai = defineModel<number>({ default: 0 });
const tampil = (n: number) => n.toLocaleString("id-ID");
const ubah = (e: Event) => { nilai.value = Number((e.target as HTMLInputElement).value.replace(/\D/g, "")) || 0; };
</script>
<template>
  <label class="rupiah">Rp <input :value="tampil(nilai)" @input="ubah" inputmode="numeric" /></label>
</template>

<!-- Pemakaian -->
<InputRupiah v-model="harga" />''')]),

'ref, reactive, computed, dan watch': dict(
  ist=[('ref()', 'Membungkus nilai apa pun menjadi reaktif; diakses lewat .value di script.'),
       ('reactive()', 'Membuat objek reaktif (berbasis Proxy); tidak untuk primitif.'),
       ('computed()', 'Nilai turunan yang di-cache dan dihitung ulang hanya saat dependensi berubah.'),
       ('watch / watchEffect', 'Menjalankan efek samping saat data berubah (simpan, fetch, log).'),
       ('Dependency tracking', 'Vue mencatat state apa yang dibaca efek, lalu menjalankannya ulang saat state itu berubah.')],
  cx=[J('Membangun reaktivitas ala Vue dengan Proxy', r'''
let efekAktif = null;
const peta = new WeakMap();
function track(obj, k) { if (!efekAktif) return; let m = peta.get(obj); if (!m) peta.set(obj, (m = new Map())); if (!m.has(k)) m.set(k, new Set()); m.get(k).add(efekAktif); }
function trigger(obj, k) { peta.get(obj)?.get(k)?.forEach((e) => e()); }
function reactive(obj) {
  return new Proxy(obj, {
    get(t, k) { track(t, k); return t[k]; },
    set(t, k, v) { if (t[k] === v) return true; t[k] = v; trigger(t, k); return true; },
  });
}
function effect(fn) { const e = () => { efekAktif = e; fn(); efekAktif = null; }; e(); }
function computed(fn) {
  let cache, kotor = true, hitung = 0;
  const c = { get value() { if (kotor) { cache = fn(); kotor = false; hitung++; } return cache; }, get hitung() { return hitung; } };
  effect(() => { fn(); kotor = true; });
  return c;
}

const keranjang = reactive({ qty: 2, harga: 45000, kupon: "" });
const total = computed(() => keranjang.qty * keranjang.harga);
effect(() => console.log(`[render] ${keranjang.qty} x ${keranjang.harga} = ${keranjang.qty * keranjang.harga}`));
keranjang.qty = 3;                  // memicu render
keranjang.kupon = "HEMAT10";        // tidak dibaca efek: tidak render
console.log("total:", total.value, total.value, "| fungsi computed dihitung", total.hitung, "kali");
''', 'Inilah inti reaktivitas Vue 3: Proxy mencatat siapa membaca properti apa (track), lalu menjalankan ulang hanya pembaca itu saat nilainya berubah (trigger).'),
      V('watch untuk autosave dan watchEffect untuk fetch', r'''
<script setup lang="ts">
import { ref, watch, watchEffect } from "vue";
const draf = ref(localStorage.getItem("draf") ?? "");
watch(draf, (baru) => localStorage.setItem("draf", baru), { debounce: 500 } as any);

const kategori = ref("kopi");
const produk = ref([]);
watchEffect(async (onCleanup) => {
  const ctrl = new AbortController();
  onCleanup(() => ctrl.abort());              // batalkan request lama
  produk.value = await fetch(`/api/produk?kat=${kategori.value}`, { signal: ctrl.signal }).then((r) => r.json());
});
</script>''')]),

'Props, emit, dan slot': dict(
  ist=[('defineProps', 'Mendeklarasikan props dengan tipe TypeScript.'),
       ('defineEmits', 'Mendeklarasikan event yang dikirim komponen ke induknya.'),
       ('Slot', 'Tempat induk menyisipkan konten; default slot dan named slot.'),
       ('Scoped slot', 'Slot yang menerima data dari anak (mirip render props di React).'),
       ('provide / inject', 'Mengirim data ke cucu tanpa prop drilling.')],
  cx=[V('Kartu dengan named slot dan tabel dengan scoped slot', r'''
<!-- KartuProduk.vue -->
<script setup lang="ts">
const props = withDefaults(defineProps<{ nama: string; harga: number; stok?: number }>(), { stok: 0 });
const emit = defineEmits<{ tambah: [qty: number]; favorit: [] }>();
</script>
<template>
  <article class="kartu">
    <slot name="gambar"><img src="/placeholder.svg" alt="" /></slot>
    <h3>{{ props.nama }}</h3>
    <slot />                                  <!-- default slot -->
    <footer>
      <button @click="emit('tambah', 1)" :disabled="props.stok === 0">Tambah</button>
      <button @click="emit('favorit')" aria-label="Favorit">♡</button>
    </footer>
  </article>
</template>

<!-- TabelData.vue (scoped slot) -->
<script setup lang="ts" generic="T extends { id: number }">
defineProps<{ baris: T[]; kolom: (keyof T)[] }>();
</script>
<template>
  <table>
    <tr v-for="b in baris" :key="b.id">
      <td v-for="k in kolom" :key="String(k)"><slot :name="k" :nilai="b[k]" :baris="b">{{ b[k] }}</slot></td>
    </tr>
  </table>
</template>

<!-- Pemakaian -->
<KartuProduk nama="Kopi Gayo" :harga="65000" :stok="4" @tambah="(q) => keranjang.tambah(q)">
  <template #gambar><img src="/gayo.webp" alt="Kopi Gayo" /></template>
  <p>Arabika, sangrai medium</p>
</KartuProduk>
<TabelData :baris="pesanan" :kolom="['id', 'total', 'status']">
  <template #status="{ nilai }"><span :class="`badge-${nilai}`">{{ nilai }}</span></template>
</TabelData>''')]),

'Lifecycle hooks dan composable': dict(
  ist=[('onMounted / onUnmounted', 'Dijalankan setelah komponen masuk DOM dan sebelum dilepas.'),
       ('onUpdated / onBeforeUnmount', 'Hook lain untuk siklus render dan pembersihan.'),
       ('Composable', 'Fungsi useXxx yang membungkus state + logika agar dapat dipakai ulang.'),
       ('VueUse', 'Koleksi 200+ composable siap pakai (useStorage, useFetch, useDark).')],
  cx=[V('Composable useJendela dan useFetch', r'''
// composables/useJendela.ts
import { ref, onMounted, onUnmounted } from "vue";
export function useJendela() {
  const lebar = ref(window.innerWidth);
  const ubah = () => (lebar.value = window.innerWidth);
  onMounted(() => window.addEventListener("resize", ubah, { passive: true }));
  onUnmounted(() => window.removeEventListener("resize", ubah));
  return { lebar, mobile: computed(() => lebar.value < 640) };
}

// composables/useFetch.ts
import { ref, watchEffect, toValue, type MaybeRefOrGetter } from "vue";
export function useFetch<T>(url: MaybeRefOrGetter<string>) {
  const data = ref<T | null>(null), error = ref<string | null>(null), memuat = ref(false);
  watchEffect(async () => {
    memuat.value = true; error.value = null;
    try { const r = await fetch(toValue(url)); if (!r.ok) throw new Error(`HTTP ${r.status}`); data.value = await r.json(); }
    catch (e) { error.value = (e as Error).message; }
    finally { memuat.value = false; }
  });
  return { data, error, memuat };
}

// Pemakaian di komponen
const { mobile } = useJendela();
const { data: produk, memuat, error } = useFetch<Produk[]>(() => `/api/produk?kat=${kategori.value}`);''', lang='ts'),
      J('Urutan lifecycle induk dan anak', r'''
const log = [];
function komponen(nama, anak = []) {
  return {
    mount() { log.push(`${nama}: setup`); log.push(`${nama}: onBeforeMount`); anak.forEach((a) => a.mount()); log.push(`${nama}: onMounted`); },
    unmount() { log.push(`${nama}: onBeforeUnmount`); anak.forEach((a) => a.unmount()); log.push(`${nama}: onUnmounted`); },
  };
}
const app = komponen("App", [komponen("Header"), komponen("DaftarProduk", [komponen("KartuProduk")])]);
app.mount(); log.push("--- halaman ditutup ---"); app.unmount();
console.log(log.join("\n"));
''', 'onMounted anak selalu selesai sebelum onMounted induk, karena induk baru dianggap terpasang setelah semua anaknya terpasang.')]),

'Vue Router': dict(
  ist=[('createRouter', 'Membuat router dengan daftar rute dan mode history.'),
       ('<RouterLink> / <RouterView>', 'Tautan navigasi dan tempat komponen rute dirender.'),
       ('Dynamic route /:id', 'Parameter dibaca lewat useRoute().params.'),
       ('Navigation guard', 'beforeEach untuk cek login atau izin sebelum pindah halaman.'),
       ('Lazy-loaded route', 'component: () => import(...) agar tiap halaman jadi bundle terpisah.')],
  cx=[V('Router dengan guard login dan lazy loading', r'''
// router/index.ts
import { createRouter, createWebHistory } from "vue-router";
import { useAuth } from "@/stores/auth";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: () => import("@/views/Beranda.vue") },
    { path: "/produk/:slug", component: () => import("@/views/DetailProduk.vue"), props: true },
    { path: "/akun", component: () => import("@/views/Akun.vue"), meta: { wajibLogin: true } },
    { path: "/masuk", component: () => import("@/views/Masuk.vue") },
    { path: "/:pathMatch(.*)*", component: () => import("@/views/Halaman404.vue") },
  ],
  scrollBehavior: (_to, _from, simpan) => simpan ?? { top: 0 },
});

router.beforeEach((to) => {
  const auth = useAuth();
  if (to.meta.wajibLogin && !auth.user) return { path: "/masuk", query: { lanjut: to.fullPath } };
});
export default router;

<!-- App.vue -->
<template>
  <nav><RouterLink to="/">Beranda</RouterLink> <RouterLink to="/akun">Akun</RouterLink></nav>
  <RouterView v-slot="{ Component }"><Transition name="pudar" mode="out-in"><component :is="Component" /></Transition></RouterView>
</template>''', lang='ts'),
      J('Simulasi navigation guard', r'''
const rute = [{ path: "/" }, { path: "/akun", meta: { wajibLogin: true } }, { path: "/admin", meta: { wajibLogin: true, peran: "admin" } }];
function navigasi(ke, user) {
  const r = rute.find((x) => x.path === ke);
  if (!r) return "404";
  if (r.meta?.wajibLogin && !user) return `redirect /masuk?lanjut=${encodeURIComponent(ke)}`;
  if (r.meta?.peran && user?.peran !== r.meta.peran) return "redirect / (tidak berwenang)";
  return `tampilkan ${ke}`;
}
for (const [ke, user] of [["/", null], ["/akun", null], ["/akun", { peran: "user" }], ["/admin", { peran: "user" }], ["/admin", { peran: "admin" }], ["/promo", null]])
  console.log(`${ke.padEnd(7)} ${(user?.peran ?? "tamu").padEnd(6)} -> ${navigasi(ke, user)}`);
''')]),

'Pinia untuk state bersama': dict(
  ist=[('Store', 'Wadah state global; satu file per domain (auth, keranjang, tema).'),
       ('Setup store', 'Store yang ditulis seperti composable: ref = state, computed = getters, function = actions.'),
       ('storeToRefs', 'Mengambil state dari store tanpa kehilangan reaktivitas.'),
       ('Pinia Devtools', 'Melihat dan mengubah state serta riwayat action di Vue Devtools.'),
       ('pinia-plugin-persistedstate', 'Menyimpan store ke localStorage otomatis.')],
  cx=[V('Store keranjang dengan Pinia', r'''
// stores/keranjang.ts
import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useKeranjang = defineStore("keranjang", () => {
  const item = ref<{ sku: string; nama: string; harga: number; qty: number }[]>([]);
  const kupon = ref<string | null>(null);

  const subtotal = computed(() => item.value.reduce((t, i) => t + i.harga * i.qty, 0));
  const diskon = computed(() => (kupon.value === "HEMAT10" ? Math.min(subtotal.value * 0.1, 15000) : 0));
  const total = computed(() => subtotal.value - diskon.value);

  function tambah(p: { sku: string; nama: string; harga: number }) {
    const ada = item.value.find((i) => i.sku === p.sku);
    ada ? ada.qty++ : item.value.push({ ...p, qty: 1 });
  }
  function hapus(sku: string) { item.value = item.value.filter((i) => i.sku !== sku); }
  return { item, kupon, subtotal, diskon, total, tambah, hapus };
}, { persist: true });

// Komponen
import { storeToRefs } from "pinia";
const keranjang = useKeranjang();
const { total, item } = storeToRefs(keranjang);   // tetap reaktif
keranjang.tambah({ sku: "KP", nama: "Kopi", harga: 45000 });''', lang='ts'),
      J('Logika store yang sama diuji di Node', r'''
function buatKeranjang() {
  const s = { item: [], kupon: null };
  const subtotal = () => s.item.reduce((t, i) => t + i.harga * i.qty, 0);
  const diskon = () => (s.kupon === "HEMAT10" ? Math.min(subtotal() * 0.1, 15000) : 0);
  return {
    s, subtotal, diskon, total: () => subtotal() - diskon(),
    tambah(p) { const a = s.item.find((i) => i.sku === p.sku); a ? a.qty++ : s.item.push({ ...p, qty: 1 }); },
  };
}
const k = buatKeranjang();
k.tambah({ sku: "KP", nama: "Kopi", harga: 45000 }); k.tambah({ sku: "KP", nama: "Kopi", harga: 45000 });
k.tambah({ sku: "FP", nama: "French Press", harga: 185000 });
k.s.kupon = "HEMAT10";
const rp = (n) => "Rp" + n.toLocaleString("id-ID");
console.log(k.s.item.map((i) => `${i.nama} x${i.qty}`).join(", "));
console.log(`subtotal ${rp(k.subtotal())} | diskon ${rp(k.diskon())} (maks Rp15.000) | total ${rp(k.total())}`);
''')]),

'Mengambil data dari API dan menangani status': dict(
  ist=[('Async state', 'Tiga nilai yang selalu berjalan bersama: data, error, memuat.'),
       ('Retry with backoff', 'Mencoba ulang dengan jeda yang makin panjang saat server sibuk.'),
       ('TanStack Query untuk Vue', 'Cache server state, refetch, dan pagination untuk Vue.'),
       ('Suspense (Vue)', 'Komponen <Suspense> untuk menunggu komponen async (masih eksperimental).')],
  cx=[V('Halaman pesanan dengan empat keadaan', r'''
<script setup lang="ts">
import { useFetch } from "@/composables/useFetch";
const { data: pesanan, error, memuat, muatUlang } = useFetch<Pesanan[]>("/api/pesanan");
</script>

<template>
  <div v-if="memuat" class="skeleton-list" aria-busy="true"><div v-for="i in 4" :key="i" class="skeleton h-16" /></div>
  <div v-else-if="error" role="alert">
    <p>Gagal memuat pesanan ({{ error }}).</p>
    <button @click="muatUlang">Coba lagi</button>
  </div>
  <div v-else-if="!pesanan?.length" class="kosong">
    <p>Belum ada pesanan.</p>
    <RouterLink to="/produk" class="btn">Mulai belanja</RouterLink>
  </div>
  <ul v-else>
    <li v-for="p in pesanan" :key="p.id">{{ p.id }} - {{ p.status }}</li>
  </ul>
</template>'''),
      J('fetch dengan retry dan exponential backoff', r'''
let percobaanServer = 0;
async function fetchPalsu() {
  percobaanServer++;
  if (percobaanServer < 3) { const e = new Error("503 Service Unavailable"); e.status = 503; throw e; }
  return [{ id: "INV-001", status: "dikirim" }];
}
async function denganRetry(fn, { maks = 4, dasarMs = 20 } = {}) {
  for (let i = 1; ; i++) {
    try { const r = await fn(); console.log(`percobaan ${i}: berhasil`); return r; }
    catch (e) {
      if (i >= maks || e.status < 500) throw e;
      const jeda = dasarMs * 2 ** (i - 1);
      console.log(`percobaan ${i}: ${e.message}, coba lagi dalam ${jeda} ms`);
      await new Promise((r) => setTimeout(r, jeda));
    }
  }
}
const data = await denganRetry(fetchPalsu);
console.log("data:", JSON.stringify(data));
''', 'Retry hanya untuk error sementara (5xx, timeout). Error 4xx seperti 401 atau 404 tidak akan sembuh dengan mencoba ulang.')]),

'Menguji komponen dengan Vitest': dict(
  ist=[('Vitest', 'Test runner berbasis Vite; cepat dan memakai konfigurasi yang sama.'),
       ('@vue/test-utils', 'mount, find, trigger, setValue untuk menguji komponen Vue.'),
       ('Testing Library for Vue', 'Alternatif yang menguji lewat role dan teks seperti pengguna.'),
       ('Snapshot test', 'Membandingkan keluaran render dengan versi tersimpan; pakai seperlunya.')],
  cx=[V('Tes komponen keranjang', r'''
// KeranjangItem.spec.ts
import { mount } from "@vue/test-utils";
import { createTestingPinia } from "@pinia/testing";
import { describe, it, expect } from "vitest";
import KeranjangItem from "./KeranjangItem.vue";

describe("KeranjangItem", () => {
  it("menampilkan nama dan subtotal", () => {
    const w = mount(KeranjangItem, { props: { nama: "Kopi", harga: 45000, qty: 2 } });
    expect(w.text()).toContain("Kopi");
    expect(w.get("[data-test=subtotal]").text()).toBe("Rp90.000");
  });

  it("mengirim event ubah saat tombol + ditekan", async () => {
    const w = mount(KeranjangItem, { props: { nama: "Kopi", harga: 45000, qty: 1 }, global: { plugins: [createTestingPinia()] } });
    await w.get("button[aria-label='Tambah']").trigger("click");
    expect(w.emitted("ubah")?.[0]).toEqual([2]);
  });
});

// npx vitest --coverage''', lang='ts'),
      J('Menulis tes untuk fungsi format', r'''
import assert from "node:assert/strict";
const rp = (n) => "Rp" + Math.round(n).toLocaleString("id-ID");
const kasus = [[90000, "Rp90.000"], [0, "Rp0"], [1250000.4, "Rp1.250.000"], [-5000, "-Rp5.000"]];
let lulus = 0;
for (const [masuk, harap] of kasus) {
  try { assert.equal(rp(masuk), harap); lulus++; console.log("✓", masuk, "->", harap); }
  catch { console.log("✗", masuk, "-> dapat", rp(masuk), "harap", harap); }
}
console.log(`${lulus}/${kasus.length} lulus`);
''', 'Satu tes gagal karena tanda minus: inilah gunanya tes, menemukan kasus tepi sebelum pengguna. Perbaikan: tulis tanda di depan "Rp".')]),

'Nuxt untuk SSR dan SEO': dict(
  ist=[('Nuxt', 'Meta-framework Vue: routing berbasis file, SSR, SSG, dan API server (Nitro).'),
       ('Auto-import', 'Komponen, composable, dan fungsi Vue dipakai tanpa baris import.'),
       ('useFetch / useAsyncData', 'Mengambil data di server lalu dikirim ke klien tanpa fetch ulang.'),
       ('useSeoMeta', 'Mengatur title, description, dan Open Graph per halaman.'),
       ('Hybrid rendering (routeRules)', 'Strategi render berbeda per rute: prerender, ISR, SPA.')],
  cx=[V('Halaman produk Nuxt dengan SEO dan route rules', r'''
<!-- pages/produk/[slug].vue -->
<script setup lang="ts">
const route = useRoute();
const { data: p, error } = await useFetch(`/api/produk/${route.params.slug}`);
if (error.value) throw createError({ statusCode: 404, statusMessage: "Produk tidak ditemukan" });

useSeoMeta({
  title: () => `${p.value?.nama} | Toko Kopi`,
  description: () => p.value?.ringkasan,
  ogImage: () => p.value?.gambar,
});
</script>
<template>
  <article>
    <NuxtImg :src="p!.gambar" width="600" height="600" format="webp" :alt="p!.nama" />
    <h1>{{ p!.nama }}</h1>
  </article>
</template>

// server/api/produk/[slug].get.ts  (Nitro)
export default defineEventHandler(async (e) => {
  const slug = getRouterParam(e, "slug");
  return await db.produk.findFirst({ where: { slug } });
});

// nuxt.config.ts
export default defineNuxtConfig({
  routeRules: {
    "/": { prerender: true },
    "/produk/**": { isr: 600 },          // statis, diperbarui tiap 10 menit
    "/akun/**": { ssr: false },          // SPA, data pribadi
  },
});''', lang='ts')]),

'Build dan deploy': dict(
  ist=[('vite build', 'Menghasilkan folder dist/ berisi file statis ber-hash.'),
       ('SPA fallback', 'Server harus mengembalikan index.html untuk semua rute agar refresh tidak 404.'),
       ('Environment variable (VITE_)', 'Hanya variabel berawalan VITE_ yang masuk ke bundle klien.'),
       ('CI/CD', 'GitHub Actions menjalankan tes lalu deploy otomatis ke Netlify, Vercel, atau Cloudflare Pages.'),
       ('Bundle analysis', 'rollup-plugin-visualizer untuk melihat pustaka mana yang membuat bundle besar.')],
  cx=[V('Konfigurasi deploy yang umum', r'''
# .env.production
VITE_API_URL=https://api.toko.id

# Netlify: public/_redirects  (SPA fallback)
/*  /index.html  200

# Nginx
location / { try_files $uri $uri/ /index.html; }
location /assets/ { add_header Cache-Control "public, max-age=31536000, immutable"; }

# .github/workflows/deploy.yml
name: deploy
on: { push: { branches: [main] } }
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run type-check && npm run test:unit -- --run
      - run: npm run build
      - uses: cloudflare/wrangler-action@v3
        with: { apiToken: "${{ secrets.CF_TOKEN }}", command: "pages deploy dist --project-name=toko-vue" }''', lang='yaml'),
      J('Memeriksa anggaran ukuran bundle', r'''
const hasilBuild = [
  ["assets/index-a1b2c3.js", 182_400], ["assets/vendor-vue-d4e5f6.js", 98_300],
  ["assets/Grafik-7a8b9c.js", 214_900], ["assets/index-0f1e2d.css", 24_100],
];
const gzipRasio = 0.32, anggaranKbGzip = { js: 170, css: 30 };
const total = { js: 0, css: 0 };
for (const [f, b] of hasilBuild) {
  const jenis = f.endsWith(".css") ? "css" : "js", gz = (b * gzipRasio) / 1024;
  if (!f.includes("Grafik")) total[jenis] += gz;             // Grafik dimuat lazy, tidak di halaman awal
  console.log(`${f.padEnd(30)} ${(b / 1024).toFixed(1).padStart(6)} KB  gzip ~${gz.toFixed(1).padStart(5)} KB${f.includes("Grafik") ? "  (lazy)" : ""}`);
}
for (const j of ["js", "css"]) console.log(`${j.toUpperCase()} awal ~${total[j].toFixed(1)} KB / anggaran ${anggaranKbGzip[j]} KB -> ${total[j] <= anggaranKbGzip[j] ? "LULUS" : "GAGAL, pecah bundle"}`);
''')]),
}
