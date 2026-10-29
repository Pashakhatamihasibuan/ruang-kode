public class Main {
    public static void main(String[] args) {
        int[] daftar = {1900, 2000, 2024, 2025};
        for (int t : daftar) {
            boolean kabisat = (t % 4 == 0 && t % 100 != 0) || t % 400 == 0;
            System.out.println(t + " kabisat? " + kabisat);
        }
    }
}
