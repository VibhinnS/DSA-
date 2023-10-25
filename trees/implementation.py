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
                
                
root = BST(20)
list = [6,3,1,6,98,3,7]
for element in list:
    root.insert(element)

root.search(69)
