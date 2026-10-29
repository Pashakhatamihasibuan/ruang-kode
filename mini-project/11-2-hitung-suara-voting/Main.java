import java.util.Map;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) {
        String[] suara = {"Ani", "Budi", "Ani", "Cici", "Budi", "Ani"};
        Map<String, Integer> hitung = new TreeMap<>();
        for (String s : suara) {
            hitung.put(s, hitung.getOrDefault(s, 0) + 1);
        }
        System.out.println(hitung);
        String juara = "";
        int maks = 0;
        for (String nama : hitung.keySet()) {
            if (hitung.get(nama) > maks) {
                maks = hitung.get(nama);
                juara = nama;
            }
        }
        System.out.println("Pemenang: " + juara + " (" + maks + " suara)");
    }
}
