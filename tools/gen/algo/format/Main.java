public class Main {
    public static void main(String[] args) {
        String nama = "Rina";
        int umur = 20;
        double ipk = 3.4567;
        // %s teks, %d bilangan bulat, %.2f desimal 2 angka, %n baris baru
        System.out.printf("Nama: %s, umur %d, IPK %.2f%n", nama, umur, ipk);

        // lebar kolom: angka positif = rata kanan, tanda minus = rata kiri
        System.out.printf("[%8s] [%-8s] [%5d] [%05d]%n", nama, nama, umur, umur);

        // pemisah ribuan, persen, basis lain, notasi ilmiah, boolean, karakter
        System.out.printf("Gaji %,d | diskon 15%% | hex %x | oktal %o%n", 7500000, 255, 8);
        System.out.printf("%.3e | %b | %c%n", 123456.789, umur > 17, 'A');

        // String.format menghasilkan teks, tidak langsung mencetak
        String kode = String.format("INV-%04d", 7);
        System.out.println(kode);

        // struk belanja: format di dalam loop membuat kolom rapi
        String[] barang = {"Kopi susu", "Roti bakar", "Air mineral"};
        int[] harga = {18000, 22500, 5000};
        int total = 0;
        System.out.printf("%-12s %10s%n", "Barang", "Harga");
        for (int i = 0; i < barang.length; i++) {
            System.out.printf("%-12s %,10d%n", barang[i], harga[i]);
            total += harga[i];
        }
        System.out.printf("%-12s %,10d%n", "TOTAL", total);
    }
}
