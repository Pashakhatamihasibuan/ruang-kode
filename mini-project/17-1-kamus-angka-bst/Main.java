public class Main {
    public static void main(String[] args) {
        TreeNode root = null;
        for (int v : new int[]{8, 3, 10, 1, 6, 14}) {
            root = add(root, v);
        }
        System.out.println("ada 6? " + contains(root, 6));
        System.out.println("ada 9? " + contains(root, 9));
        System.out.println("tinggi = " + height(root));
    }

    static TreeNode add(TreeNode node, int v) {
        if (node == null) return new TreeNode(v);
        if (v < node.data) node.left = add(node.left, v);
        else node.right = add(node.right, v);
        return node;
    }

    static boolean contains(TreeNode node, int v) {
        if (node == null) return false;
        if (v == node.data) return true;
        if (v < node.data) return contains(node.left, v);
        return contains(node.right, v);
    }

    static int height(TreeNode node) {
        if (node == null) return 0;
        return 1 + Math.max(height(node.left), height(node.right));
    }
}

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int data) { this.data = data; }
}
