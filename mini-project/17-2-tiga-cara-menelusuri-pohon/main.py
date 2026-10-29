class TreeNode:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None

def add(n, v):
    if n is None: return TreeNode(v)
    if v < n.data: n.left = add(n.left, v)
    else: n.right = add(n.right, v)
    return n

def pre(n):
    if n: print(n.data, end=" "); pre(n.left); pre(n.right)

def ino(n):
    if n: ino(n.left); print(n.data, end=" "); ino(n.right)

def post(n):
    if n: post(n.left); post(n.right); print(n.data, end=" ")

root = None
for v in [8, 3, 10, 1, 6]:
    root = add(root, v)
print("pre : ", end=""); pre(root); print()
print("in  : ", end=""); ino(root); print()
print("post: ", end=""); post(root); print()
