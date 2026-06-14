class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

if __name__ == "__main__":
    n1, n2, n3 = ListNode(3), ListNode(2), ListNode(0)
    n1.next, n2.next, n3.next = n2, n3, n2
    print(has_cycle(n1))
