public class Main {
    public static void main(String[] args) {
        String[] data = {"12", "abc", "7", "3x", "20"};
        int total = 0;
        for (String s : data) {
            try {
                total += Integer.parseInt(s);
            } catch (NumberFormatException e) {
                System.out.println("Lewati: " + s);
            }
        }
        System.out.println("Total: " + total);
    }
}
