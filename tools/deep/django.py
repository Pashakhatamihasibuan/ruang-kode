"""Pendalaman jalur Django: istilah dunia kerja, kode Django siap pakai, dan konsep inti yang dijalankan dengan Python standar."""
K = 'django'


def D_(t, code, b=None, lang='python'):
    """Kode Django (butuh proyek Django), ditampilkan tanpa dijalankan."""
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


def P(t, code, b=None):
    """Konsep yang sama ditiru dengan Python standar agar keluarannya bisa dijalankan."""
    return dict(t=t, b=b, code=code.strip('\n'), lang='python')


D = {
'Django dan pola MTV': dict(
  ist=[('MTV', 'Model (data), Template (tampilan), View (logika); versi Django dari pola MVC.'),
       ('Batteries included', 'Django membawa ORM, admin, autentikasi, form, migrasi, dan keamanan bawaan.'),
       ('Request/response cycle', 'URL dicocokkan ke view, view memakai model, lalu merender template menjadi HttpResponse.'),
       ('WSGI / ASGI', 'Antarmuka antara server web dan aplikasi Python; ASGI mendukung async dan WebSocket.'),
       ('Middleware', 'Lapisan yang memproses setiap request/response: sesi, CSRF, autentikasi, keamanan.')],
  cx=[P('Siklus request Django dalam 40 baris Python', r'''
import re

# Model: data
PRODUK = [{"id": 1, "nama": "Kopi Gayo", "harga": 65000}, {"id": 2, "nama": "Teh Melati", "harga": 18000}]

# Template
def render(templat, ctx):
    return re.sub(r"\{\{\s*(\w+)\s*\}\}", lambda m: str(ctx[m.group(1)]), templat)

# View
def daftar_produk(request):
    baris = "".join(f"<li>{p['nama']} Rp{p['harga']:,}</li>".replace(",", ".") for p in PRODUK)
    return 200, render("<h1>{{ judul }}</h1><ul>{{ isi }}</ul>", {"judul": "Katalog", "isi": baris})

def detail_produk(request, pk):
    p = next((x for x in PRODUK if x["id"] == int(pk)), None)
    return (404, "Tidak ditemukan") if p is None else (200, render("<h1>{{ nama }}</h1>", p))

# URLconf
urlpatterns = [(r"^produk/$", daftar_produk), (r"^produk/(?P<pk>\d+)/$", detail_produk)]

# Middleware sederhana: mencatat setiap request
def middleware_log(handler):
    def bungkus(path):
        status, isi = handler(path)
        print(f"[log] GET /{path} -> {status}")
        return status, isi
    return bungkus

@middleware_log
def handler(path):
    for pola, view in urlpatterns:
        m = re.match(pola, path)
        if m:
            return view({"path": path}, **m.groupdict())
    return 404, "Halaman tidak ditemukan"

for p in ["produk/", "produk/2/", "produk/9/", "keranjang/"]:
    print("   ", handler(p)[1])
''', 'Django melakukan hal yang sama dengan jauh lebih lengkap: URLconf memilih view, view mengambil data dari model, template merender HTML, dan middleware membungkus semuanya.')]),

'Membuat proyek dan aplikasi': dict(
  ist=[('Project vs app', 'Project = satu situs (settings, urls utama); app = modul fitur yang dapat dipakai ulang (katalog, pesanan).'),
       ('manage.py', 'Perintah administrasi: runserver, makemigrations, migrate, createsuperuser, shell.'),
       ('INSTALLED_APPS', 'Daftar app yang aktif; app baru wajib didaftarkan di sini.'),
       ('Virtual environment', 'Lingkungan Python terisolasi per proyek (venv, uv, poetry).'),
       ('uv', 'Pengelola paket Python sangat cepat yang populer di 2026.')],
  cx=[D_('Membuat proyek toko dengan dua app', r'''
# 1. lingkungan dan paket
uv venv && source .venv/bin/activate          # Windows: .venv\Scripts\activate
uv pip install "django>=5.2" djangorestframework python-dotenv

# 2. proyek dan app
django-admin startproject config .            # folder config/ berisi settings & urls
python manage.py startapp katalog
python manage.py startapp pesanan

# 3. daftarkan di config/settings.py
INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "rest_framework",
    "katalog", "pesanan",
]

# 4. jalankan
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver                    # http://127.0.0.1:8000

# Struktur
toko/
├── manage.py
├── config/   (settings.py, urls.py, wsgi.py, asgi.py)
├── katalog/  (models.py, views.py, urls.py, admin.py, tests.py, migrations/)
└── pesanan/''', lang='bash')]),

'Settings penting dan variabel lingkungan': dict(
  ist=[('SECRET_KEY', 'Kunci untuk tanda tangan sesi, CSRF, dan reset password; wajib rahasia.'),
       ('DEBUG', 'Wajib False di produksi; True membocorkan detail error dan kode.'),
       ('ALLOWED_HOSTS', 'Daftar domain yang dilayani; mencegah serangan Host header.'),
       ('12-factor app', 'Konfigurasi dari environment variable, bukan dari kode.'),
       ('check --deploy', 'python manage.py check --deploy memeriksa setelan keamanan produksi.')],
  cx=[D_('settings.py yang membaca environment', r'''
# config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]                      # gagal cepat jika tidak ada
DEBUG = os.getenv("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost").split(",")
CSRF_TRUSTED_ORIGINS = [f"https://{h}" for h in ALLOWED_HOSTS if h != "localhost"]

DATABASES = {"default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.getenv("DB_NAME", "toko"), "USER": os.getenv("DB_USER", "toko"),
    "PASSWORD": os.getenv("DB_PASSWORD", ""), "HOST": os.getenv("DB_HOST", "localhost"),
    "CONN_MAX_AGE": 60,
}}
LANGUAGE_CODE = "id"
TIME_ZONE = "Asia/Jakarta"
USE_TZ = True

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000

# .env (jangan di-commit)
# DJANGO_SECRET_KEY=ganti-dengan-50-karakter-acak
# DJANGO_DEBUG=1
# DB_PASSWORD=rahasia'''),
      P('Validasi environment seperti check --deploy', r'''
import secrets

def cek_produksi(env):
    masalah = []
    if env.get("DJANGO_DEBUG") == "1":
        masalah.append("DEBUG aktif: halaman error akan menampilkan kode dan variabel")
    kunci = env.get("DJANGO_SECRET_KEY", "")
    if len(kunci) < 50 or kunci.startswith("django-insecure"):
        masalah.append("SECRET_KEY terlalu pendek atau masih bawaan startproject")
    hosts = env.get("DJANGO_ALLOWED_HOSTS", "")
    if not hosts or "*" in hosts.split(","):
        masalah.append("ALLOWED_HOSTS kosong atau '*'")
    return masalah

env_salah = {"DJANGO_DEBUG": "1", "DJANGO_SECRET_KEY": "django-insecure-abc", "DJANGO_ALLOWED_HOSTS": "*"}
env_benar = {"DJANGO_DEBUG": "0", "DJANGO_SECRET_KEY": secrets.token_urlsafe(50), "DJANGO_ALLOWED_HOSTS": "toko.example.id"}
for nama, env in [("env_salah", env_salah), ("env_benar", env_benar)]:
    hasil = cek_produksi(env)
    print(f"{nama}: {'LULUS' if not hasil else str(len(hasil)) + ' masalah'}")
    for m in hasil:
        print("  -", m)
print("contoh SECRET_KEY baru panjangnya", len(env_benar["DJANGO_SECRET_KEY"]), "karakter")
''')]),

'Model, field, dan relasi': dict(
  ist=[('Model', 'Kelas Python yang dipetakan ke tabel database.'),
       ('Field type', 'CharField, DecimalField, DateTimeField, BooleanField, JSONField, dan lainnya.'),
       ('ForeignKey (many-to-one)', 'Banyak pesanan milik satu pelanggan; on_delete menentukan perilaku saat induk dihapus.'),
       ('ManyToManyField', 'Relasi banyak-ke-banyak, misalnya produk dan tag.'),
       ('Meta options', 'ordering, indexes, constraints, verbose_name.')],
  cx=[D_('Model toko: kategori, produk, pesanan', r'''
# katalog/models.py
from django.db import models
from django.conf import settings

class Kategori(models.Model):
    nama = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self): return self.nama

class Produk(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.PROTECT, related_name="produk")
    nama = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    harga = models.DecimalField(max_digits=12, decimal_places=0)
    stok = models.PositiveIntegerField(default=0)
    aktif = models.BooleanField(default=True)
    tag = models.ManyToManyField("Tag", blank=True)
    dibuat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-dibuat"]
        indexes = [models.Index(fields=["kategori", "aktif"])]
        constraints = [models.CheckConstraint(condition=models.Q(harga__gte=0), name="harga_tidak_negatif")]

class Tag(models.Model):
    nama = models.CharField(max_length=30, unique=True)

# pesanan/models.py
class Pesanan(models.Model):
    class Status(models.TextChoices):
        BARU = "baru", "Baru"; DIBAYAR = "dibayar", "Dibayar"; DIKIRIM = "dikirim", "Dikirim"
    pelanggan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pesanan")
    status = models.CharField(max_length=10, choices=Status, default=Status.BARU)
    dibuat = models.DateTimeField(auto_now_add=True)

class ItemPesanan(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE, related_name="item")
    produk = models.ForeignKey(Produk, on_delete=models.PROTECT)
    qty = models.PositiveSmallIntegerField()
    harga_saat_beli = models.DecimalField(max_digits=12, decimal_places=0)   # harga dikunci saat checkout'''),
      P('SQL yang dihasilkan model tersebut (dijalankan di SQLite)', r'''
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript("""
CREATE TABLE katalog_kategori (id INTEGER PRIMARY KEY, nama VARCHAR(60) UNIQUE NOT NULL, slug VARCHAR(50) UNIQUE NOT NULL);
CREATE TABLE katalog_produk (
  id INTEGER PRIMARY KEY, nama VARCHAR(120) NOT NULL, slug VARCHAR(50) UNIQUE NOT NULL,
  harga DECIMAL NOT NULL CHECK (harga >= 0), stok INTEGER NOT NULL DEFAULT 0 CHECK (stok >= 0),
  aktif BOOL NOT NULL DEFAULT 1,
  kategori_id INTEGER NOT NULL REFERENCES katalog_kategori(id) ON DELETE RESTRICT);
CREATE INDEX katalog_pro_kategor_idx ON katalog_produk (kategori_id, aktif);
""")
db.execute("INSERT INTO katalog_kategori VALUES (1, 'Kopi', 'kopi')")
db.execute("INSERT INTO katalog_produk (nama, slug, harga, kategori_id) VALUES ('Kopi Gayo', 'kopi-gayo', 65000, 1)")
for sql, alasan in [
    ("INSERT INTO katalog_produk (nama, slug, harga, kategori_id) VALUES ('X', 'x', -5, 1)", "CheckConstraint harga"),
    ("INSERT INTO katalog_produk (nama, slug, harga, kategori_id) VALUES ('Y', 'kopi-gayo', 5, 1)", "slug unique"),
    ("DELETE FROM katalog_kategori WHERE id = 1", "on_delete=PROTECT"),
]:
    try:
        db.execute(sql); print("lolos?!", alasan)
    except sqlite3.IntegrityError as e:
        print(f"ditolak ({alasan}): {e}")
''')]),

'Migrasi dan QuerySet': dict(
  ist=[('Migration', 'File Python yang mencatat perubahan skema; dibuat makemigrations, diterapkan migrate.'),
       ('Data migration', 'Migrasi berisi RunPython untuk mengubah isi data, bukan hanya struktur.'),
       ('QuerySet', 'Kueri yang lazy: baru dieksekusi saat dievaluasi (iterasi, list(), len()).'),
       ('Lookup', 'filter(harga__gte=50000, nama__icontains="kopi") memakai dua garis bawah.'),
       ('F & Q expressions', 'F merujuk kolom lain di database; Q untuk kondisi OR/NOT.')],
  cx=[D_('Perintah migrasi dan kueri yang sering dipakai', r'''
python manage.py makemigrations katalog       # membuat 0002_produk_stok.py
python manage.py sqlmigrate katalog 0002      # melihat SQL-nya
python manage.py migrate                       # menerapkan
python manage.py showmigrations

# Kueri di python manage.py shell
from django.db.models import F, Q, Sum, Count, Avg
from katalog.models import Produk

Produk.objects.filter(aktif=True, harga__lte=70000).order_by("harga")[:10]
Produk.objects.filter(Q(nama__icontains="kopi") | Q(tag__nama="best-seller")).distinct()
Produk.objects.exclude(stok=0).count()
Produk.objects.filter(pk=1).update(stok=F("stok") - 1)               # atomik di database
Produk.objects.values("kategori__nama").annotate(jumlah=Count("id"), rata=Avg("harga"))
Pesanan.objects.filter(status="dibayar", dibuat__date__gte="2026-11-01") \
    .aggregate(omzet=Sum(F("item__qty") * F("item__harga_saat_beli")))''', lang='bash'),
      P('QuerySet lazy dan chaining, ditiru dengan Python', r'''
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, harga INT, stok INT)")
db.executemany("INSERT INTO produk (nama, harga, stok) VALUES (?, ?, ?)",
               [("Kopi Gayo", 65000, 4), ("Kopi Toraja", 72000, 0), ("Teh Melati", 18000, 20), ("Kopi Bali", 58000, 9)])
JUMLAH_QUERY = 0

class QuerySet:
    OPS = {"": "=", "gte": ">=", "lte": "<=", "icontains": "LIKE"}
    def __init__(self, where=(), order=None, limit=None):
        self.where, self.order, self.limit, self._cache = list(where), order, limit, None
    def filter(self, **kw):
        w = self.where[:]
        for k, v in kw.items():
            kol, _, op = k.partition("__")
            w.append((f"{kol} {self.OPS[op]} ?", f"%{v}%" if op == "icontains" else v))
        return QuerySet(w, self.order, self.limit)              # QuerySet baru, belum ke DB
    def order_by(self, kol):
        return QuerySet(self.where, kol.lstrip("-") + (" DESC" if kol.startswith("-") else ""), self.limit)
    def __getitem__(self, s):
        return QuerySet(self.where, self.order, s.stop)
    def sql(self):
        q = "SELECT nama, harga FROM produk"
        if self.where: q += " WHERE " + " AND ".join(w for w, _ in self.where)
        if self.order: q += f" ORDER BY {self.order}"
        if self.limit: q += f" LIMIT {self.limit}"
        return q
    def __iter__(self):
        global JUMLAH_QUERY
        if self._cache is None:
            JUMLAH_QUERY += 1
            self._cache = db.execute(self.sql(), [v for _, v in self.where]).fetchall()
        return iter(self._cache)

qs = QuerySet().filter(nama__icontains="kopi").filter(stok__gte=1).order_by("-harga")[:5]
print("SQL:", qs.sql())
print("query sebelum dievaluasi:", JUMLAH_QUERY)
for nama, harga in qs:
    print(f"  {nama:<10} Rp{harga:,}".replace(",", "."))
list(qs)
print("query setelah dua kali iterasi:", JUMLAH_QUERY, "(hasil di-cache)")
''')]),

'Panel admin dan masalah N+1': dict(
  ist=[('Django admin', 'Antarmuka CRUD otomatis untuk staf; dikustomisasi dengan ModelAdmin.'),
       ('N+1 query', 'Satu query untuk daftar, lalu satu query lagi untuk setiap baris; lambat saat data banyak.'),
       ('select_related', 'JOIN untuk ForeignKey/OneToOne dalam satu query.'),
       ('prefetch_related', 'Query kedua untuk ManyToMany/relasi balik, lalu digabung di Python.'),
       ('django-debug-toolbar', 'Menampilkan jumlah dan durasi query di setiap halaman saat development.')],
  cx=[D_('ModelAdmin yang rapi dan efisien', r'''
# katalog/admin.py
from django.contrib import admin
from .models import Produk, Kategori

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ("nama", "kategori", "harga", "stok", "aktif")
    list_filter = ("aktif", "kategori")
    search_fields = ("nama", "slug")
    list_editable = ("harga", "stok", "aktif")
    prepopulated_fields = {"slug": ("nama",)}
    list_select_related = ("kategori",)         # hindari N+1 di daftar admin
    autocomplete_fields = ("kategori",)
    actions = ["nonaktifkan"]

    @admin.action(description="Nonaktifkan produk terpilih")
    def nonaktifkan(self, request, queryset):
        n = queryset.update(aktif=False)
        self.message_user(request, f"{n} produk dinonaktifkan.")

# Di view:
Produk.objects.select_related("kategori").prefetch_related("tag")'''),
      P('Menghitung query: N+1 vs JOIN vs prefetch', r'''
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE kategori (id INTEGER PRIMARY KEY, nama TEXT);
CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, kategori_id INT);
CREATE TABLE tag (id INTEGER PRIMARY KEY, produk_id INT, nama TEXT);
""")
db.executemany("INSERT INTO kategori VALUES (?, ?)", [(1, "Kopi"), (2, "Teh"), (3, "Alat")])
db.executemany("INSERT INTO produk (nama, kategori_id) VALUES (?, ?)", [(f"Produk {i}", i % 3 + 1) for i in range(1, 51)])
db.executemany("INSERT INTO tag (produk_id, nama) VALUES (?, ?)", [(i, "promo") for i in range(1, 51, 5)])

hitung = 0
def q(sql, *a):
    global hitung
    hitung += 1
    return db.execute(sql, a).fetchall()

hitung = 0
for pid, nama, kid in q("SELECT * FROM produk"):
    q("SELECT nama FROM kategori WHERE id = ?", kid)
print(f"tanpa optimasi        : {hitung} query")

hitung = 0
q("SELECT p.nama, k.nama FROM produk p JOIN kategori k ON k.id = p.kategori_id")
print(f"select_related        : {hitung} query")

hitung = 0
produk = q("SELECT p.id, p.nama, k.nama FROM produk p JOIN kategori k ON k.id = p.kategori_id")
ids = [p[0] for p in produk]
tags = q(f"SELECT produk_id, nama FROM tag WHERE produk_id IN ({','.join('?' * len(ids))})", *ids)
peta = {}
for pid, t in tags:
    peta.setdefault(pid, []).append(t)
print(f"+ prefetch_related tag: {hitung} query, {len(peta)} produk punya tag")
''', 'Untuk 50 produk, versi naif butuh 51 query. Dengan 10.000 produk menjadi 10.001 query, sedangkan versi teroptimasi tetap 1 atau 2.')]),

'View dan URL': dict(
  ist=[('Function-based view (FBV)', 'View berupa fungsi; eksplisit dan mudah dibaca.'),
       ('Class-based view (CBV)', 'ListView, DetailView, CreateView; mengurangi kode berulang.'),
       ('path() & converter', 'path("produk/<slug:slug>/", ...) dengan converter int, slug, uuid.'),
       ('Named URL & reverse', 'name="detail" lalu reverse("katalog:detail", args=[...]) atau {% url %} di template.'),
       ('get_object_or_404', 'Mengambil objek atau otomatis mengembalikan 404.')],
  cx=[D_('FBV, CBV, dan URLconf', r'''
# katalog/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Produk

def detail(request, slug):
    produk = get_object_or_404(Produk.objects.select_related("kategori"), slug=slug, aktif=True)
    return render(request, "katalog/detail.html", {"produk": produk})

class DaftarProduk(ListView):
    template_name = "katalog/daftar.html"
    context_object_name = "produk"
    paginate_by = 24
    def get_queryset(self):
        qs = Produk.objects.filter(aktif=True).select_related("kategori")
        if q := self.request.GET.get("q"):
            qs = qs.filter(nama__icontains=q)
        return qs

# katalog/urls.py
from django.urls import path
from . import views
app_name = "katalog"
urlpatterns = [
    path("", views.DaftarProduk.as_view(), name="daftar"),
    path("<slug:slug>/", views.detail, name="detail"),
]

# config/urls.py
from django.urls import include, path
urlpatterns = [path("admin/", admin.site.urls), path("produk/", include("katalog.urls"))]'''),
      P('Converter path dan reverse() buatan sendiri', r'''
import re
CONVERTER = {"int": r"[0-9]+", "slug": r"[-a-zA-Z0-9_]+", "str": r"[^/]+"}

def path(pola, view, name):
    regex = "^" + re.sub(r"<(\w+):(\w+)>", lambda m: f"(?P<{m.group(2)}>{CONVERTER[m.group(1)]})", pola) + "$"
    return {"regex": re.compile(regex), "pola": pola, "view": view, "name": name}

urls = [path("produk/", "DaftarProduk", "daftar"),
        path("produk/<slug:slug>/", "detail", "detail"),
        path("pesanan/<int:pk>/", "detail_pesanan", "pesanan")]

def resolve(url):
    for u in urls:
        if m := u["regex"].match(url):
            return u["view"], m.groupdict()
    return "404", {}

def reverse(name, **kw):
    u = next(x for x in urls if x["name"] == name)
    return "/" + re.sub(r"<\w+:(\w+)>", lambda m: str(kw[m.group(1)]), u["pola"])

for url in ["produk/", "produk/kopi-gayo/", "pesanan/42/", "pesanan/abc/"]:
    print(f"{url:<20} -> {resolve(url)}")
print("reverse('detail', slug='teh-melati') =", reverse("detail", slug="teh-melati"))
''')]),

'Template dan inheritance': dict(
  ist=[('Django Template Language (DTL)', '{{ variabel }}, {% tag %}, dan |filter.'),
       ('Template inheritance', '{% extends "base.html" %} dan {% block %} untuk kerangka bersama.'),
       ('{% include %}', 'Menyisipkan potongan template (partial) seperti kartu produk.'),
       ('Auto-escaping', 'Semua variabel di-escape otomatis; |safe hanya untuk HTML tepercaya.'),
       ('Custom template filter', 'Filter sendiri, misalnya |rupiah, di templatetags/.')],
  cx=[D_('base.html, halaman daftar, dan filter rupiah', r'''
{# templates/base.html #}
<!doctype html>
<html lang="id">
<head><meta charset="utf-8"><title>{% block judul %}Toko Kopi{% endblock %}</title></head>
<body>
  {% include "partials/navbar.html" %}
  {% if messages %}{% for m in messages %}<div class="alert {{ m.tags }}">{{ m }}</div>{% endfor %}{% endif %}
  <main>{% block isi %}{% endblock %}</main>
</body>
</html>

{# templates/katalog/daftar.html #}
{% extends "base.html" %}
{% load toko_filters %}
{% block judul %}Katalog | {{ block.super }}{% endblock %}
{% block isi %}
  <h1>Katalog</h1>
  {% for p in produk %}
    <a href="{% url 'katalog:detail' p.slug %}">{{ p.nama }} - {{ p.harga|rupiah }}</a>
  {% empty %}
    <p>Belum ada produk.</p>
  {% endfor %}
  {% if is_paginated %}Halaman {{ page_obj.number }} dari {{ page_obj.paginator.num_pages }}{% endif %}
{% endblock %}

# katalog/templatetags/toko_filters.py
from django import template
register = template.Library()
@register.filter
def rupiah(n):
    return "Rp" + f"{int(n):,}".replace(",", ".")''', lang='django'),
      P('Inheritance dan auto-escaping ditiru dengan Python', r'''
import html, re

BASE = "<title>{% block judul %}Toko{% endblock %}</title><main>{% block isi %}{% endblock %}</main>"
ANAK = {"judul": "Katalog | Toko", "isi": "<h1>Katalog</h1><p>{{ ulasan }}</p><p>{{ harga|rupiah }}</p>"}

def rupiah(n):
    return "Rp" + f"{int(n):,}".replace(",", ".")

FILTER = {"rupiah": rupiah}

def render(base, blok, ctx):
    hasil = re.sub(r"\{% block (\w+) %\}.*?\{% endblock %\}", lambda m: blok.get(m.group(1), ""), base)
    def var(m):
        nama, _, f = m.group(1).partition("|")
        nilai = ctx[nama.strip()]
        nilai = FILTER[f.strip()](nilai) if f else nilai
        return html.escape(str(nilai))                     # auto-escaping
    return re.sub(r"\{\{\s*(.+?)\s*\}\}", var, hasil)

print(render(BASE, ANAK, {"ulasan": "<script>alert('xss')</script> enak!", "harga": 65000}))
''')]),

'Form, ModelForm, dan validasi': dict(
  ist=[('Form', 'Kelas yang mendefinisikan field, validasi, dan render HTML.'),
       ('ModelForm', 'Form yang dibuat otomatis dari model.'),
       ('clean_<field>() & clean()', 'Validasi per field dan validasi antar-field.'),
       ('cleaned_data', 'Data yang sudah divalidasi dan dikonversi ke tipe Python.'),
       ('PRG pattern', 'Post/Redirect/Get: setelah POST sukses, redirect agar refresh tidak mengirim ulang.')],
  cx=[D_('Form checkout dan view dengan PRG', r'''
# pesanan/forms.py
import re
from django import forms

class CheckoutForm(forms.Form):
    nama = forms.CharField(max_length=80, min_length=3)
    hp = forms.CharField(max_length=15)
    kode_pos = forms.CharField(max_length=5)
    kupon = forms.CharField(required=False)

    def clean_hp(self):
        hp = re.sub(r"[\s-]", "", self.cleaned_data["hp"])
        if not re.fullmatch(r"(\+62|0)8\d{8,11}", hp):
            raise forms.ValidationError("Nomor HP diawali 08 atau +628.")
        return "+62" + hp.removeprefix("+62").removeprefix("0")

    def clean(self):
        data = super().clean()
        if data.get("kupon") == "ONGKIR0" and not data.get("kode_pos", "").startswith("1"):
            self.add_error("kupon", "Kupon ONGKIR0 hanya untuk wilayah Jakarta.")
        return data

# pesanan/views.py
def checkout(request):
    form = CheckoutForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        pesanan = buat_pesanan(request.user, **form.cleaned_data)
        messages.success(request, "Pesanan dibuat.")
        return redirect("pesanan:detail", pk=pesanan.pk)          # PRG
    return render(request, "pesanan/checkout.html", {"form": form})'''),
      P('Alur validasi form Django ditiru dengan Python', r'''
import re

class ValidationError(Exception):
    pass

class CheckoutForm:
    def __init__(self, data):
        self.data, self.errors, self.cleaned_data = data, {}, {}

    def clean_nama(self, v):
        if len(v.strip()) < 3: raise ValidationError("Minimal 3 huruf.")
        return v.strip().title()
    def clean_hp(self, v):
        hp = re.sub(r"[\s-]", "", v)
        if not re.fullmatch(r"(\+62|0)8\d{8,11}", hp): raise ValidationError("Nomor HP diawali 08 atau +628.")
        return "+62" + hp.removeprefix("+62").removeprefix("0")
    def clean_kode_pos(self, v):
        if not re.fullmatch(r"\d{5}", v): raise ValidationError("Kode pos 5 digit.")
        return v
    def clean(self):
        if self.cleaned_data.get("kupon") == "ONGKIR0" and not self.cleaned_data.get("kode_pos", "").startswith("1"):
            self.errors["kupon"] = "Kupon ONGKIR0 hanya untuk wilayah Jakarta."

    def is_valid(self):
        for f in ["nama", "hp", "kode_pos", "kupon"]:
            nilai = self.data.get(f, "")
            try:
                self.cleaned_data[f] = getattr(self, f"clean_{f}", lambda v: v)(nilai)
            except ValidationError as e:
                self.errors[f] = str(e)
        self.clean()
        return not self.errors

for data in [{"nama": "al", "hp": "0812-3456", "kode_pos": "4011", "kupon": ""},
             {"nama": "rina wijaya", "hp": "0812 3456 7890", "kode_pos": "40115", "kupon": "ONGKIR0"},
             {"nama": "rina wijaya", "hp": "0812 3456 7890", "kode_pos": "12950", "kupon": "ONGKIR0"}]:
    f = CheckoutForm(data)
    print("valid " if f.is_valid() else "error ", f.cleaned_data if not f.errors else f.errors)
''')]),

'Autentikasi dan izin akses': dict(
  ist=[('django.contrib.auth', 'Model User, login/logout, hashing password, dan permission bawaan.'),
       ('Custom user model', 'AUTH_USER_MODEL kustom sejak awal proyek agar mudah menambah field (misalnya login dengan email).'),
       ('@login_required / LoginRequiredMixin', 'Membatasi view hanya untuk pengguna yang masuk.'),
       ('Permission & group', 'Hak granular (add/change/delete/view) yang dikelompokkan per peran.'),
       ('Object-level permission', 'Hak atas objek tertentu, misalnya hanya pemilik pesanan yang boleh melihatnya.')],
  cx=[D_('Custom user, login wajib, dan cek kepemilikan', r'''
# akun/models.py (buat sebelum migrate pertama!)
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)
    no_hp = models.CharField(max_length=15, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

# settings.py
AUTH_USER_MODEL = "akun.User"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "beranda"

# pesanan/views.py
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required
def pesanan_saya(request):
    return render(request, "pesanan/saya.html", {"pesanan": request.user.pesanan.all()})

@login_required
def detail_pesanan(request, pk):
    pesanan = get_object_or_404(Pesanan, pk=pk, pelanggan=request.user)    # bukan milik sendiri -> 404
    return render(request, "pesanan/detail.html", {"p": pesanan})

@permission_required("katalog.change_produk", raise_exception=True)
def ubah_harga(request, pk): ...

# config/urls.py
path("akun/", include("django.contrib.auth.urls")),   # login, logout, password_reset, ...'''),
      P('Cara Django menyimpan password: PBKDF2 dengan salt', r'''
import base64, hashlib, hmac, secrets

ITERASI = 1_000_000          # nilai bawaan Django 5.x

def make_password(raw, salt=None, iterasi=ITERASI):
    salt = salt or secrets.token_urlsafe(16)
    h = hashlib.pbkdf2_hmac("sha256", raw.encode(), salt.encode(), iterasi)
    return f"pbkdf2_sha256${iterasi}${salt}${base64.b64encode(h).decode()}"

def check_password(raw, disimpan):
    algo, iterasi, salt, _ = disimpan.split("$")
    return hmac.compare_digest(make_password(raw, salt, int(iterasi)), disimpan)

a = make_password("kopi-pagi-2026", salt="garamAcak01", iterasi=20_000)
b = make_password("kopi-pagi-2026", salt="garamAcak02", iterasi=20_000)
print(a[:60] + "...")
print("password sama, hash beda karena salt beda:", a != b)
print("login benar :", check_password("kopi-pagi-2026", a))
print("login salah :", check_password("kopi-pagi-2025", a))
''', 'Iterasi dikurangi agar contoh cepat. Django otomatis menaikkan iterasi hash lama saat pengguna login berikutnya.')]),

'API dengan Django REST Framework': dict(
  ist=[('Serializer', 'Mengubah model menjadi JSON dan memvalidasi input JSON.'),
       ('ViewSet & Router', 'Satu kelas untuk list/retrieve/create/update/delete, URL dibuat router.'),
       ('Permission class', 'IsAuthenticated, IsAdminUser, atau kelas sendiri seperti IsOwner.'),
       ('Pagination & filtering', 'PageNumberPagination, django-filter, SearchFilter, OrderingFilter.'),
       ('Throttling', 'Membatasi jumlah request per pengguna/IP.'),
       ('OpenAPI (drf-spectacular)', 'Dokumentasi API otomatis dengan Swagger UI.')],
  cx=[D_('API produk dan pesanan', r'''
# katalog/serializers.py
from rest_framework import serializers
class ProdukSerializer(serializers.ModelSerializer):
    kategori = serializers.CharField(source="kategori.nama", read_only=True)
    class Meta:
        model = Produk
        fields = ["id", "nama", "slug", "harga", "stok", "kategori"]

class ItemSerializer(serializers.Serializer):
    produk_id = serializers.IntegerField()
    qty = serializers.IntegerField(min_value=1, max_value=20)

class BuatPesananSerializer(serializers.Serializer):
    item = ItemSerializer(many=True)
    def validate_item(self, item):
        if not item: raise serializers.ValidationError("Keranjang kosong.")
        return item

# katalog/api.py
from rest_framework import viewsets, permissions, filters
class ProdukViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Produk.objects.filter(aktif=True).select_related("kategori")
    serializer_class = ProdukSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nama"]
    ordering_fields = ["harga", "dibuat"]

class IsPemilik(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.pelanggan_id == request.user.id

# config/urls.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("produk", ProdukViewSet)
urlpatterns += [path("api/", include(router.urls))]

# settings.py
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination", "PAGE_SIZE": 20,
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.UserRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"user": "120/minute"},
}'''),
      P('Serializer: validasi input dan bentuk respons', r'''
import json

class Serializer:
    fields = {}
    def __init__(self, data):
        self.data_in, self.errors, self.validated = data, {}, {}
    def is_valid(self):
        for nama, (tipe, aturan) in self.fields.items():
            v = self.data_in.get(nama)
            if v is None:
                self.errors[nama] = ["Field ini wajib diisi."]; continue
            if not isinstance(v, tipe):
                self.errors[nama] = [f"Harus bertipe {tipe.__name__}."]; continue
            for cek, pesan in aturan:
                if not cek(v):
                    self.errors.setdefault(nama, []).append(pesan)
            self.validated[nama] = v
        return not self.errors

class ItemSerializer(Serializer):
    fields = {"produk_id": (int, []), "qty": (int, [(lambda q: 1 <= q <= 20, "Pastikan nilai antara 1 dan 20.")])}

for body in ['{"produk_id": 3, "qty": 2}', '{"produk_id": "3", "qty": 50}', '{"qty": 0}']:
    s = ItemSerializer(json.loads(body))
    status = 201 if s.is_valid() else 400
    print(status, json.dumps(s.validated if status == 201 else s.errors, ensure_ascii=False))
''')]),

'Keamanan bawaan Django': dict(
  ist=[('CSRF protection', 'Token rahasia di form POST mencegah situs lain mengirim request atas nama pengguna.'),
       ('SQL injection protection', 'ORM memakai parameterized query; hati-hati dengan raw() dan extra().'),
       ('XSS protection', 'Template auto-escape; hindari |safe dan mark_safe pada data pengguna.'),
       ('Clickjacking protection', 'X-Frame-Options: DENY lewat XFrameOptionsMiddleware.'),
       ('SecurityMiddleware', 'HSTS, redirect HTTPS, nosniff, Referrer-Policy.')],
  cx=[D_('Pola aman dan tidak aman', r'''
# AMAN: ORM dan parameter
Produk.objects.filter(nama__icontains=q)
Produk.objects.raw("SELECT * FROM katalog_produk WHERE nama ILIKE %s", [f"%{q}%"])

# TIDAK AMAN: string formatting ke SQL
Produk.objects.raw(f"SELECT * FROM katalog_produk WHERE nama LIKE '%{q}%'")      # SQL injection

# Form wajib {% csrf_token %}
<form method="post">{% csrf_token %} ... </form>

# fetch dari JavaScript: kirim header X-CSRFToken
fetch("/keranjang/tambah/", { method: "POST", headers: { "X-CSRFToken": getCookie("csrftoken") }, body })

# Jangan:
@csrf_exempt                       # hanya untuk webhook yang diverifikasi signature
{{ ulasan|safe }}                  # XSS bila ulasan dari pengguna

# settings.py produksi
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_HTTPONLY = True'''),
      P('SQL injection: string formatting vs parameter', r'''
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, harga_modal INT)")
db.executemany("INSERT INTO produk (nama, harga_modal) VALUES (?, ?)", [("Kopi Gayo", 41000), ("Teh Melati", 9000)])
db.execute("CREATE TABLE auth_user (username TEXT, password TEXT)")
db.execute("INSERT INTO auth_user VALUES ('admin', 'pbkdf2_sha256$...rahasia')")

masukan = "x' UNION SELECT username, password, 0 FROM auth_user --"

tidak_aman = f"SELECT id, nama, 0 FROM produk WHERE nama LIKE '%{masukan}%'"
print("f-string    :", db.execute(tidak_aman).fetchall())

aman = "SELECT id, nama, 0 FROM produk WHERE nama LIKE ?"
print("parameter   :", db.execute(aman, (f"%{masukan}%",)).fetchall())
''', 'Dengan f-string, penyerang membaca tabel pengguna. Dengan parameter, masukan diperlakukan sebagai teks biasa sehingga hasilnya kosong.'),
      P('Cara token CSRF menolak request dari situs lain', r'''
import hmac, hashlib, secrets

SECRET_KEY = b"rahasia-server"
def buat_token(sesi_id):
    return hmac.new(SECRET_KEY, sesi_id.encode(), hashlib.sha256).hexdigest()[:32]

def proses_post(sesi_id, token_form):
    return "200 diproses" if hmac.compare_digest(buat_token(sesi_id), token_form or "") else "403 CSRF verification failed"

sesi = secrets.token_hex(8)
token_di_form = buat_token(sesi)                         # disisipkan {% csrf_token %} di halaman kita
print("form dari situs kita     :", proses_post(sesi, token_di_form))
print("form dari situs-jahat.id :", proses_post(sesi, None), "(cookie sesi ikut terkirim, token tidak)")
print("token tebakan            :", proses_post(sesi, "0" * 32))
''')]),

'Menulis tes di Django': dict(
  ist=[('TestCase', 'Setiap tes berjalan dalam transaksi yang di-rollback; database tes terpisah.'),
       ('Client', 'self.client.get/post untuk mensimulasikan request tanpa server.'),
       ('Fixture & factory', 'Data awal tes; factory_boy membuat objek tes dengan ringkas.'),
       ('assertNumQueries', 'Memastikan jumlah query tidak membengkak (mencegah N+1 kembali).'),
       ('pytest-django', 'Alternatif populer: fixture pytest, kode tes lebih ringkas.')],
  cx=[D_('Tes model, view, izin, dan jumlah query', r'''
# pesanan/tests.py
from django.test import TestCase
from django.urls import reverse

class PesananTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rina = User.objects.create_user(username="rina", email="rina@contoh.id", password="x")
        cls.budi = User.objects.create_user(username="budi", email="budi@contoh.id", password="x")
        kat = Kategori.objects.create(nama="Kopi", slug="kopi")
        cls.kopi = Produk.objects.create(kategori=kat, nama="Kopi Gayo", slug="gayo", harga=65000, stok=5)
        cls.p = Pesanan.objects.create(pelanggan=cls.rina)

    def test_harus_login(self):
        r = self.client.get(reverse("pesanan:detail", args=[self.p.pk]))
        self.assertRedirects(r, f"/akun/login/?next=/pesanan/{self.p.pk}/")

    def test_orang_lain_dapat_404(self):
        self.client.force_login(self.budi)
        self.assertEqual(self.client.get(reverse("pesanan:detail", args=[self.p.pk])).status_code, 404)

    def test_stok_berkurang_saat_checkout(self):
        self.client.force_login(self.rina)
        self.client.post(reverse("pesanan:checkout"), {"produk": self.kopi.pk, "qty": 2, "nama": "Rina", "hp": "081234567890", "kode_pos": "40115"})
        self.kopi.refresh_from_db()
        self.assertEqual(self.kopi.stok, 3)

    def test_daftar_produk_tanpa_n_plus_1(self):
        with self.assertNumQueries(2):            # 1 count untuk paginasi + 1 data
            self.client.get(reverse("katalog:daftar"))

# python manage.py test        atau    pytest -q --cov'''),
      P('Prinsip yang sama dengan unittest standar', r'''
import io, unittest

def kurangi_stok(stok, qty):
    if qty <= 0: raise ValueError("qty harus positif")
    if qty > stok: raise ValueError(f"stok tidak cukup (sisa {stok})")
    return stok - qty

def total_pesanan(item, kupon=None):
    sub = sum(h * q for h, q in item)
    diskon = min(sub * 10 // 100, 15000) if kupon == "HEMAT10" else 0
    return sub - diskon

class TesToko(unittest.TestCase):
    def test_stok_berkurang(self): self.assertEqual(kurangi_stok(5, 2), 3)
    def test_stok_kurang(self):
        with self.assertRaisesRegex(ValueError, "sisa 1"): kurangi_stok(1, 2)
    def test_qty_nol(self):
        with self.assertRaises(ValueError): kurangi_stok(5, 0)
    def test_diskon_dibatasi(self): self.assertEqual(total_pesanan([(65000, 3)], "HEMAT10"), 180000)
    def test_tanpa_kupon(self): self.assertEqual(total_pesanan([(45000, 2)]), 90000)

hasil = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(unittest.defaultTestLoader.loadTestsFromTestCase(TesToko))
print(f"{hasil.testsRun} tes, {len(hasil.failures)} gagal, {len(hasil.errors)} error -> {'OK' if hasil.wasSuccessful() else 'FAILED'}")
''')]),

'Caching dan tugas latar dengan Celery': dict(
  ist=[('Cache framework', 'Backend Redis/Memcached; cache_page, cache per fragmen template, atau cache.get/set.'),
       ('Cache invalidation', 'Menghapus cache saat data berubah; salah satu masalah tersulit.'),
       ('Celery', 'Antrean tugas latar: kirim email, buat laporan, proses gambar, di luar siklus request.'),
       ('Broker', 'Redis atau RabbitMQ sebagai penampung pesan tugas.'),
       ('Celery Beat', 'Penjadwal tugas berkala (cron) seperti laporan harian.'),
       ('Idempotent task', 'Tugas yang aman dijalankan ulang tanpa efek ganda.')],
  cx=[D_('Cache Redis dan tugas Celery', r'''
# settings.py
CACHES = {"default": {"BACKEND": "django.core.cache.backends.redis.RedisCache", "LOCATION": "redis://localhost:6379/1"}}
CELERY_BROKER_URL = "redis://localhost:6379/0"

# katalog/views.py
from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def beranda(request): ...

def produk_terlaris():
    return cache.get_or_set("terlaris", lambda: list(Produk.objects.order_by("-terjual")[:10]), timeout=600)

# hapus cache saat produk berubah
from django.db.models.signals import post_save
@receiver(post_save, sender=Produk)
def hapus_cache(sender, **kw): cache.delete("terlaris")

# config/celery.py
from celery import Celery
app = Celery("config"); app.config_from_object("django.conf:settings", namespace="CELERY"); app.autodiscover_tasks()

# pesanan/tasks.py
from celery import shared_task
@shared_task(bind=True, autoretry_for=(ConnectionError,), retry_backoff=True, max_retries=5)
def kirim_invoice(self, pesanan_id):
    p = Pesanan.objects.get(pk=pesanan_id)
    if p.invoice_terkirim: return "sudah"          # idempoten
    kirim_email(p); p.invoice_terkirim = True; p.save(update_fields=["invoice_terkirim"])

# di view: jangan tunggu email selesai
kirim_invoice.delay(pesanan.pk)

# celery -A config worker -l info      dan    celery -A config beat'''),
      P('Cache dengan TTL dan antrean tugas latar', r'''
import queue, threading, time

class Cache:
    def __init__(self): self.d = {}
    def get_or_set(self, k, fn, ttl, now):
        if k in self.d and self.d[k][1] > now: return self.d[k][0], "HIT"
        v = fn(); self.d[k] = (v, now + ttl); return v, "MISS"
    def delete(self, k): self.d.pop(k, None)

panggilan_db = 0
def query_terlaris():
    global panggilan_db
    panggilan_db += 1
    return ["Kopi Gayo", "Kopi Toraja", "Teh Melati"]

c = Cache()
for t, aksi in [(0, "get"), (30, "get"), (120, "get"), (130, "ubah produk"), (131, "get"), (700, "get")]:
    if aksi == "ubah produk":
        c.delete("terlaris"); print(f"t={t:>3}s admin mengubah produk -> cache dihapus"); continue
    _, s = c.get_or_set("terlaris", query_terlaris, ttl=600, now=t)
    print(f"t={t:>3}s {s}")
print("query DB:", panggilan_db, "dari 5 permintaan")

antre, terkirim = queue.Queue(), []
def worker():
    while (pid := antre.get()) is not None:
        time.sleep(0.01); terkirim.append(pid); antre.task_done()
w = threading.Thread(target=worker); w.start()
for pid in [101, 102, 103]: antre.put(pid)           # seperti kirim_invoice.delay(pid)
print("view langsung membalas 'Pesanan dibuat' tanpa menunggu 3 email selesai")
antre.join(); antre.put(None); w.join()
print("invoice terkirim di latar:", terkirim)
''')]),

'Deployment: Gunicorn, Nginx, dan Docker': dict(
  ist=[('Gunicorn / Uvicorn', 'Server aplikasi WSGI/ASGI yang menjalankan beberapa worker Django.'),
       ('Nginx (reverse proxy)', 'Menerima request, melayani file statis, TLS, lalu meneruskan ke Gunicorn.'),
       ('collectstatic & WhiteNoise', 'Mengumpulkan file statis; WhiteNoise melayani langsung dari Django.'),
       ('Docker Compose', 'Menjalankan web, database, Redis, dan worker bersama.'),
       ('Health check & zero-downtime', 'Endpoint /health dan migrasi yang kompatibel mundur saat rilis bertahap.')],
  cx=[D_('Dockerfile, compose, dan Nginx', r'''
# Dockerfile
FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
RUN useradd -m app && chown -R app /app
USER app
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "30"]

# compose.yaml
services:
  web:
    build: .
    env_file: .env
    depends_on: { db: { condition: service_healthy }, redis: { condition: service_started } }
    command: sh -c "python manage.py migrate --noinput && gunicorn config.wsgi -b 0.0.0.0:8000 -w 3"
  worker: { build: ., env_file: .env, command: celery -A config worker -l info }
  db:
    image: postgres:17
    environment: { POSTGRES_DB: toko, POSTGRES_USER: toko, POSTGRES_PASSWORD: "${DB_PASSWORD}" }
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck: { test: ["CMD", "pg_isready", "-U", "toko"], interval: 5s }
  redis: { image: redis:7-alpine }
  nginx:
    image: nginx:1.27-alpine
    ports: ["80:80", "443:443"]
    volumes: ["./nginx.conf:/etc/nginx/conf.d/default.conf", "./staticfiles:/static"]
volumes: { pgdata: {} }

# nginx.conf
server {
  listen 80;
  server_name toko.example.id;
  client_max_body_size 10M;
  location /static/ { alias /static/; expires 30d; add_header Cache-Control "public, immutable"; }
  location / {
    proxy_pass http://web:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}''', lang='yaml'),
      P('Menghitung jumlah worker Gunicorn dan kapasitas', r'''
def rekomendasi(cpu, ram_gb, ram_per_worker_mb=180, latensi_ms=120):
    worker_cpu = 2 * cpu + 1                                 # rumus umum Gunicorn
    worker_ram = int((ram_gb * 1024 * 0.7) // ram_per_worker_mb)   # sisakan 30% untuk OS, Postgres, Redis
    w = min(worker_cpu, worker_ram)
    rps = w * (1000 / latensi_ms)
    return w, worker_cpu, worker_ram, rps

print(f"{'server':<14}{'worker':>7}{'batas CPU':>11}{'batas RAM':>11}{'~req/detik':>12}")
for nama, cpu, ram in [("VPS 1 vCPU/1GB", 1, 1), ("VPS 2 vCPU/4GB", 2, 4), ("VPS 4 vCPU/8GB", 4, 8)]:
    w, wc, wr, rps = rekomendasi(cpu, ram)
    print(f"{nama:<14}{w:>7}{wc:>11}{wr:>11}{rps:>12.0f}")
puncak = 150
_, _, _, rps4 = rekomendasi(4, 8)
_, _, _, rps4c = rekomendasi(4, 8, latensi_ms=40)
print(f"Puncak flash sale ~{puncak} req/detik: 1 server 4 vCPU hanya ~{rps4:.0f}.")
print(f"Pilihan: {-(-puncak // int(rps4))} server di belakang load balancer, atau cache agar latensi 40 ms (~{rps4c:.0f} req/detik per server).")
''')]),
}
