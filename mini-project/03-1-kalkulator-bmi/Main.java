public class Main {
    public static void main(String[] args) {
        System.out.println("Andi: " + bmi(60, 170));
        System.out.println("Bela: " + bmi(48, 155));
    }

    public static double bmi(int berat, int tinggiCm) {
        double m = tinggiCm / 100.0;
        double hasil = berat / (m * m);
        return Math.round(hasil * 10) / 10.0;
    }
}
