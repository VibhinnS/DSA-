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
