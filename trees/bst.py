class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def inOrderPrint(root):
    if root is None:
        return -1
    else:
        inOrderPrint(root.left)
        print(root.data)
        inOrderPrint(root.right)


if __name__ == '__main__':
    arr = [5,2,10,7,15,12]
    root = Node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    inOrderPrint(root)
