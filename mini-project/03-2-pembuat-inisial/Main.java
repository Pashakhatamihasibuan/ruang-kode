public class Main {
    public static void main(String[] args) {
        String nama = "Budi Santoso";
        int spasi = nama.indexOf(" ");
        String inisial = nama.charAt(0) + "." + nama.charAt(spasi + 1) + ".";
        System.out.println("Inisial: " + inisial);
        System.out.println("Jumlah huruf: " + (nama.length() - 1));
    }
}
