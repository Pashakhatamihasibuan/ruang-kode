public class Main {
    public static void main(String[] args) {
        int saldo = 100000;
        int tahun = 0;
        while (saldo < 200000) {
            saldo += saldo / 10;
            tahun++;
            System.out.println("Tahun " + tahun + ": " + saldo);
        }
        System.out.println("Butuh " + tahun + " tahun");
    }
}
