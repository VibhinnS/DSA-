class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None
    

class DLL:
    def __init__(self):
        self.head = None
        self.n = 0
    
    
    def __len__(self):
        return self.n


    def insertHead(self, value):
        new_node = Node(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.n += 1
        
        
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result += '<-' + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    
    def append(self,value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.n += 1
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
        self.n += 1

       
DLL = DLL()
DLL.insertHead(5)
DLL.insertHead(4)
DLL.insertHead(3)
DLL.insertHead(2)
DLL.append(6)

print(DLL)
print(len(DLL))