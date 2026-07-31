# Reverse a singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head = Node(1); head.next = Node(2); head.next.next = Node(3)
print(to_list(reverse_list(head)))  # [3, 2, 1]
