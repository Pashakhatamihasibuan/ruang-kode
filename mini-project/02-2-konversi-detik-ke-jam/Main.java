public class Main {
    public static void main(String[] args) {
        int total = 3725;
        int jam = total / 3600;
        int sisa = total % 3600;
        int menit = sisa / 60;
        int detik = sisa % 60;
        System.out.println(jam + " jam " + menit + " menit " + detik + " detik");
    }
}
