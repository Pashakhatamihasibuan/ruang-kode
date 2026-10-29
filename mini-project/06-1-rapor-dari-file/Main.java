import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("nilai.txt"));
        while (input.hasNextLine()) {
            String[] t = input.nextLine().split(" ");
            int a = Integer.parseInt(t[1]);
            int b = Integer.parseInt(t[2]);
            System.out.println(t[0] + ": " + (a + b) / 2);
        }
    }
}
