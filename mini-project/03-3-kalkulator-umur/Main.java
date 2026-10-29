import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Tahun lahir: ");
        int tahun = console.nextInt();
        int umur = 2026 - tahun;
        System.out.println("Umurmu " + umur + " tahun");
    }
}
