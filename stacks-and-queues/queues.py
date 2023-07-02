class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
       
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
         
            
    def dequeue(self):
        if self.front == None:
            return -1
        else:
            self.front = self.front.next
            
    
    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data, end = " ")
            temp = temp.next
            
    
    def is_empty(self):
        return self.front == None
    
    
    def size(self):
        temp = self.front
        size = 0
        while temp != None:
            size += 1
            temp = temp.next
        return size
    
    
    def front_item(self):
        if self.front == None:
            return -1
        else:
            return self.front.data
        
    
    def rear_item(self):
        if self.front == None:
            return -1
        else:
            return self.rear.data
        

    
            
            
    
q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.traverse()
print("\n")
q.dequeue()
q.traverse()