def reverse_list(self,head):
    prev = None
    curr = head
    while curr is not None:
        new_node = curr.next
        curr.next = prev
        prev = curr
        curr = new_node
    return prev
