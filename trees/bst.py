class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node
    
#Driver Code
tree = Tree() 
arr = [5,2,10,7,15,12]
root = tree.createNode(arr[0])

