class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

temp = [0]
def nnode(root, m):
    if not root:
        return
    if temp[0] <= m[0]:
        nnode(root.left, m)
        nnode(root.right, m)
        temp[0] += 1
        if temp[0] == m[0]:
            print(root.data)

root = Node(30)
root.left = Node(27)
root.right = Node(24)
root.left.left = Node(23)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(19)

m = [4]
nnode(root,m)