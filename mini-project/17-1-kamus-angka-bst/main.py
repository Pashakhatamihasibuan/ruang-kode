class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add(node, v):
    if node is None: return TreeNode(v)
    if v < node.data: node.left = add(node.left, v)
    else: node.right = add(node.right, v)
    return node

def contains(node, v):
    if node is None: return False
    if v == node.data: return True
    if v < node.data: return contains(node.left, v)
    return contains(node.right, v)

def height(node):
    if node is None: return 0
    return 1 + max(height(node.left), height(node.right))

root = None
for v in [8, 3, 10, 1, 6, 14]:
    root = add(root, v)
print("ada 6?", contains(root, 6))
print("ada 9?", contains(root, 9))
print("tinggi =", height(root))
