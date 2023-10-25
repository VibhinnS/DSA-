class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        # similar to head se insertion
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
        
    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if self.isempty():
            return -1
        else:
            return self.top.data

    def pop(self):
        if self.isempty():
            return -1
        else:
            self.top = self.top.next


s = Stack()
s.push(3)
s.push(4)
s.push(5)
print(s.isempty())
# s.traverse()