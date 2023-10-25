class BST:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def insert(self, new_data):
        if new_data == self.data:
            return
        if new_data < self.data:
            if self.left_child is None:
                self.left_child = BST(new_data)
            else:
                self.left_child.insert(new_data)
        else:
            if self.right_child is None:
                self.right_child = BST(new_data)
            else:
                self.right_child.insert(new_data)
       
    def search(self, key):
        if self.data == key:
            print(True)
            return
        if key < self.data:
            if not self.left_child:
                print(False)
            else:
                self.left_child.search(key)
        else:
            if not self.right_child:
                print(False)
            else:
                self.right_child.search(key)




    def preorder(self):
        print(self.data)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
    
    
    
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.data, end=" ")
        if self.right_child:
            self.right_child.inorder()
    
    
    
    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()        
        print(self.data, end = " ")
        
        
    
    def delete(self,key):
        if self.data is None:
            return
        if key < self.data:
            if self.left_child:
                self.left_child = self.left_child.delete(key)
            else:
                print(None)
        else:
            if self.right_child:
                self.right_child = self.right_child.delete(key)
            else:
                print(None)
        
        

        
root = BST(20)
list = [6,3,1,6,98,3,7]
for element in list:
    root.insert(element)

root.preorder()
root.inorder()