from __future__ import annotations


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


new = Node(10)
new.left = Node(20)
new.right = Node(30)
new.right.left = Node(40)
new.right.right = Node(50)
new.right.right.right = Node(80)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


def size_of_tree(root):
    if not root:
        return 0
    else:
        left = size_of_tree(root.left)
        right = size_of_tree(root.right)
        return left + right + 1


def max_element_of_tree(root):
    if root is None:
        return float('-inf')
    else:
        left = max_element_of_tree(root.left)
        right = max_element_of_tree(root.right)
        return max(left, right, root.data)


# print(max_element_of_tree(new))


def search_in_tree(root, key):
    if not root:
        return False
    elif root.data == key:
        return True
    elif search_in_tree(root.left, key):
        return True
    else:
        return search_in_tree(root.right, key)


# print(search_in_tree(new, 50))


def height_of_tree(root, height=0):
    if not root:
        return 0
    else:
        height += 1
        left = height_of_tree(root.left, height)
        right = height_of_tree(root.right, height)
        return max(left + 1, right + 1)
        # or return max(left, right) + 1


"""Shorter Implementation

def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1"""


# print(height_of_tree(new))

# iterative inorder traversal

def iterative_inorder_traversal(root):
    if root is None:
        return
    st = []
    curr = root
    while curr is not None:
        st.append(curr)
        curr = curr.left
    while len(st) > 0:
        curr = st.pop()
        print(curr.data)
        curr = curr.right
        while curr is not None:
            st.append(curr)
            curr = curr.left


print(iterative_inorder_traversal(new))
