public class Main {
    public static void main(String[] args) {
        Hewan[] kebun = {new Kucing("Oyen"), new Anjing("Doggo"), new Hewan("Ikan")};
        for (Hewan h : kebun) {
            System.out.println(h.nama + ": " + h.suara());
        }
    }
}

class Hewan {
    String nama;
    Hewan(String nama) { this.nama = nama; }
    String suara() { return "..."; }
}

class Kucing extends Hewan {
    Kucing(String nama) { super(nama); }
    @Override
    String suara() { return "Meong"; }
}

class Anjing extends Hewan {
    Anjing(String nama) { super(nama); }
    @Override
    String suara() { return "Guk guk"; }
}
