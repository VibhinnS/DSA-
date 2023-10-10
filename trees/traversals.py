class BST:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            return
        
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
                
    def search(self, data):
        if self.key == data:
            print("Node Present")
            return
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print("No Node Present")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("No Node Present")
                
    def delete(self, data):
        if self.key is None:
            print("Delete Impossible")
            return
        if data < self.key:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("Node Unavailable")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("Node Unavailable")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
        node = self.right
        while node.left:
            node = node.left
            
            
            
             
                
    def preorder(self):
        #root - left - right
        #pehle root print, fir left subtree fir right subtree
        print(self.key, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        #left - root - right
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        #left - right - root
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end=" ")
            
list1 = [20, 4, 30, 4, 1, 5, 6] 
root = BST(list1[0])
for i in range(1, len(list1)):
    root.insert(list1[i])
root.preorder()
print("\n")
root.inorder()
print("\n")
root.postorder()
