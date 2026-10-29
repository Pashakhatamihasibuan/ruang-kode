public class Main {
    public static void main(String[] args) {
        Buku a = new Buku("Laskar Pelangi", 529);
        Buku b = new Buku("Bumi", 440);
        System.out.println(a.info());
        System.out.println(b.info());
    }
}

class Buku {
    private String judul;
    private int halaman;

    public Buku(String judul, int halaman) {
        this.judul = judul;
        this.halaman = halaman;
    }

    public String info() {
        return judul + " (" + halaman + " hlm)";
    }
}
