from __future__ import annotations
import collections
class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


new: Node = Node(1)
new.left = Node(2)
new.right = Node(5)
new.left.left = Node(3)
new.left.right = Node(4)
new.right.right = Node(6)

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

# preorder(new)

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


# print(iterative_inorder_traversal(new))


def level_order_traversal(root: Node) -> list[list[int]]:
    if not root:
        return []
    
    result: list[list[int]] = []
    queue: list[Node] = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        result.append(current_level)
    return result
# print(level_order_traversal(new))

def rightSideView(root: Node) -> list[int]:
    result = []  # Initialize an empty list to store the rightmost values
    q = collections.deque([root])  # Initialize a deque with the root node
    
    # Perform BFS traversal
    while q:
        rightMost = None  # Initialize a variable to track the rightmost node at each level
        n = len(q)  # Get the number of nodes at the current level
        
        # Iterate through each node at the current level
        for i in range(n):
            node = q.popleft()  # Dequeue a node from the left of the deque
            if node:
                rightMost = node  # Update the rightmost node
                q.append(node.left)  # Enqueue the left child
                q.append(node.right)  # Enqueue the right child
        
        # If a rightmost node was encountered at the current level, append its value to the result
        if rightMost:
            result.append(rightMost.data)
    
    return result  # Return the list containing the rightmost values

def leftSideView(root: Node) -> list[int]:
    result = []  # Initialize an empty list to store the rightmost values
    q = collections.deque([root])  # Initialize a deque with the root node
    
    # Perform BFS traversal
    while q:
        leftMost = None  # Initialize a variable to track the rightmost node at each level
        n = len(q)  # Get the number of nodes at the current level
        
        # Iterate through each node at the current level
        for i in range(n):
            node = q.popleft()  # Dequeue a node from the left of the deque
            if node:
                leftMost = node  # Update the rightmost node
                q.append(node.right)  # Enqueue the right child
                q.append(node.left)  # Enqueue the left child
        
        # If a rightmost node was encountered at the current level, append its value to the result
        if leftMost:
            result.append(leftMost.data)
    
    return result  # Return the list containing
# print(leftSideView(new))

def isSymmetric(root) -> list[list[int]]:
    if not root:
        return False

    levels: list[list[int]] = []
    queue: list[int] = [root]

    while queue:
        size: int = len(queue)
        current_level: list[int] = []

        for _ in range(size):
            node = queue.pop(0)
            if node.left:
                current_level.append(node.left.data)
            if node.right:
                current_level.append(node.right.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(current_level)
    return levels

# print(isSymmetric(new))
