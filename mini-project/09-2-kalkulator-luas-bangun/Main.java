public class Main {
    public static void main(String[] args) {
        Bentuk[] daftar = {new Persegi(4), new PersegiPanjang(3, 5), new Segitiga(6, 4)};
        int total = 0;
        for (Bentuk b : daftar) {
            System.out.println(b.getClass().getSimpleName() + ": " + b.luas());
            total += b.luas();
        }
        System.out.println("Total: " + total);
    }
}

interface Bentuk {
    int luas();
}

class Persegi implements Bentuk {
    int s;
    Persegi(int s) { this.s = s; }
    public int luas() { return s * s; }
}

class PersegiPanjang implements Bentuk {
    int p, l;
    PersegiPanjang(int p, int l) { this.p = p; this.l = l; }
    public int luas() { return p * l; }
}

class Segitiga implements Bentuk {
    int a, t;
    Segitiga(int a, int t) { this.a = a; this.t = t; }
    public int luas() { return a * t / 2; }
}
