public class Main {
    public static void main(String[] args) {
        int[] nilai = {95, 82, 74, 50};
        for (int n : nilai) {
            System.out.println(n + " -> " + huruf(n));
        }
    }

    public static String huruf(int n) {
        if (n >= 90) {
            return "A";
        } else if (n >= 80) {
            return "B";
        } else if (n >= 70) {
            return "C";
        } else {
            return "D";
        }
    }
}
