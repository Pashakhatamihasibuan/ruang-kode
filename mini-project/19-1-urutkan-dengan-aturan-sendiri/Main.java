import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> nama = new ArrayList<>(List.of("Siti", "Al", "Budiman", "Eka"));
        nama.sort((a, b) -> a.length() - b.length());
        System.out.println(nama);
        nama.forEach(s -> System.out.println(s.toUpperCase()));
    }
}
