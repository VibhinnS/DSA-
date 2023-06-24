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
def reverse(head,curr,prev):
    if curr is None:
        head = prev
        return

    forward = curr.next
    reverse(head,forward, curr)
    curr.next = prev


def reverse_recursion(head):
    curr = head
    prev = None
    reverse(head,curr,prev)
    return head
