import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        for (String s : new String[]{"(a[b]{c})", "(]", "((x)"}) {
            System.out.println(s + " -> " + seimbang(s));
        }
    }

    static boolean seimbang(String s) {
        Stack<Character> st = new Stack<>();
        for (char c : s.toCharArray()) {
            if ("([{".indexOf(c) >= 0) {
                st.push(c);
            } else if (")]}".indexOf(c) >= 0) {
                if (st.isEmpty()) return false;
                char buka = st.pop();
                if ("([{".indexOf(buka) != ")]}".indexOf(c)) return false;
            }
        }
        return st.isEmpty();
    }
}
