public class Main {
    public static void main(String[] args) {
        TreeNode root = null;
        for (int v : new int[]{8, 3, 10, 1, 6}) root = add(root, v);
        System.out.print("pre : "); pre(root); System.out.println();
        System.out.print("in  : "); in(root); System.out.println();
        System.out.print("post: "); post(root); System.out.println();
    }

    static TreeNode add(TreeNode n, int v) {
        if (n == null) return new TreeNode(v);
        if (v < n.data) n.left = add(n.left, v); else n.right = add(n.right, v);
        return n;
    }

    static void pre(TreeNode n)  { if (n != null) { System.out.print(n.data + " "); pre(n.left); pre(n.right); } }
    static void in(TreeNode n)   { if (n != null) { in(n.left); System.out.print(n.data + " "); in(n.right); } }
    static void post(TreeNode n) { if (n != null) { post(n.left); post(n.right); System.out.print(n.data + " "); } }
}

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int data) { this.data = data; }
}
