class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    rev = reverse_list(head)
    print(rev.val, rev.next.val, rev.next.next.val)
