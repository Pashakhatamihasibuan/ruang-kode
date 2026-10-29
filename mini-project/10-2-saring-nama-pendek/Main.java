import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> nama = new ArrayList<>(List.of("Ani", "Budi", "Eko", "Ida", "Sari", "Tono"));
        for (int i = nama.size() - 1; i >= 0; i--) {
            if (nama.get(i).length() < 4) {
                nama.remove(i);
            }
        }
        System.out.println(nama);
    }
}
