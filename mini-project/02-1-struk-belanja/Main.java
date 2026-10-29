public class Main {
    public static void main(String[] args) {
        int hargaBuku = 12500;
        int jumlahBuku = 3;
        int hargaPulpen = 4000;
        int jumlahPulpen = 2;

        int subBuku = hargaBuku * jumlahBuku;
        int subPulpen = hargaPulpen * jumlahPulpen;
        int total = subBuku + subPulpen;

        System.out.println("Buku   : " + subBuku);
        System.out.println("Pulpen : " + subPulpen);
        System.out.println("Total  : " + total);
    }
}
