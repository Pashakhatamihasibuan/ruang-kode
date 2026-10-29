import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> belanja = new ArrayList<>();
        belanja.add("beras");
        belanja.add("telur");
        belanja.add("susu");
        System.out.println(belanja);
        belanja.add(1, "gula");
        System.out.println(belanja);
        belanja.remove("telur");
        System.out.println(belanja);
        belanja.set(belanja.indexOf("susu"), "teh");
        System.out.println(belanja);
    }
}
