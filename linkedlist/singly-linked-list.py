class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c

class LinkedList:
    def __init__(self):
        # empty linked list = 0 nodes
        # head = None (linkedList is empty)
        self.head = None  # condition of empty linked list
        self.n = 0

    def __len__(self):
        return self.n
        # number of nodes in the linked list is called len()

    def insertHead(self, value):
        # new Node
        newNode = Node(value)
        # create connection
        newNode.next = self.head
        # reassign head
        self.head = newNode
        # increment n
        self.n += 1

    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result = result + str(current.data) + '->'
            current = current.next
        return result[:-2]

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):
        new_node = Node(value)
        current = self.head
        while current is not None:
            if current.data == after:
                break
            current = current.next

        if current is not None:
            new_node.next = current.next
            current.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty LL'

        self.head = self.head.next
        self.n -= 1

    def pop(self):
        if self.head is None:
            return 'Empty LL'

        current = self.head

        if current.next is None:
            return self.delete_head()

        while current.next.next is not None:
            current = current.next

        current.next = None
        self.n -= 1

    def removeDuplicates(head):
        curr = head
        while curr is not None:
            if curr == curr.next:
                curr.next = curr.next.next
            curr = curr.next
        return head


    def deleteDuplicates(head):
        curr = head
        while curr.next is not None:
            if curr == curr.next:
                curr.next = curr.next.next
                curr = curr.next
            else:
                curr = curr.next
        return head


L = LinkedList()
L.append(1)
L.append(1)
L.append(2)
print(L)
L.removeDuplicates(L)

# print(L.compute(12))
