# iterative solution
def reverse_list(self, head):
    prev = None
    curr = head
    while curr is not None:
        forward = curr.next
        curr.next = prev
        prev = curr
        curr = forward
    return prev


# recursive solution
def reverse(self, head, curr, prev):
    if curr is None:
        head = prev
        return

    forward = curr.next
    curr.next = prev
    self.reverse(head, forward, curr)
    return head


def reverseList(self, head):
    if head is None:
        return None

    new_head = None
    curr = head
    prev = None

    while curr is not None:
        forward = curr.next
        curr.next = prev
        prev = curr
        curr = forward

    head = prev
    return head
