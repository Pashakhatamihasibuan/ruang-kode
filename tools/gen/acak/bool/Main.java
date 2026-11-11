public class Main {
    public static void main(String[] args) {
        // 1. Hasil perbandingan selalu boolean: true atau false
        int nilai = 82, hadir = 70;
        boolean nilaiCukup = nilai >= 75;
        boolean hadirCukup = hadir >= 80;
        System.out.println("nilaiCukup = " + nilaiCukup);
        System.out.println("hadirCukup = " + hadirCukup);

        // 2. AND (&&), OR (||), NOT (!)
        System.out.println("AND: lulus = " + (nilaiCukup && hadirCukup));
        System.out.println("OR : remedial = " + (!nilaiCukup || !hadirCukup));
        System.out.println("NOT: !hadirCukup = " + !hadirCukup);

        // 3. Tabel kebenaran semua kombinasi p dan q
        boolean[] tf = {true, false};
        System.out.println("p     q     AND   OR    XOR");
        for (boolean p : tf) {
            for (boolean q : tf) {
                System.out.printf("%-6s%-6s%-6s%-6s%s%n", p, q, p && q, p || q, p ^ q);
            }
        }

        // 4. Hukum De Morgan, dicek untuk semua kombinasi
        boolean hukum1 = true, hukum2 = true;
        for (boolean p : tf) {
            for (boolean q : tf) {
                if (!(p && q) != (!p || !q)) hukum1 = false;
                if (!(p || q) != (!p && !q)) hukum2 = false;
            }
        }
        System.out.println("De Morgan 1: !(p && q) == !p || !q -> " + hukum1);
        System.out.println("De Morgan 2: !(p || q) == !p && !q -> " + hukum2);

        // 5. Urutan: ! dulu, lalu &&, baru ||
        System.out.println("true || false && false = " + (true || false && false));

        // 6. Short-circuit: sisi kanan tidak dihitung jika hasil sudah pasti
        int pembagi = 0;
        if (pembagi != 0 && 10 / pembagi > 1) {
            System.out.println("hasil bagi besar");
        } else {
            System.out.println("short-circuit: 10 / 0 tidak pernah dihitung");
        }
    }
}
