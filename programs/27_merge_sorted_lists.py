# Merge two sorted linked lists
class Node:
    def __init__(self, val):
        self.val = val; self.next = None

def merge_lists(l1, l2):
    dummy = Node(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1; l1 = l1.next
        else:
            cur.next = l2; l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

def to_list(node):
    r = []
    while node: r.append(node.val); node = node.next
    return r

l1 = Node(1); l1.next = Node(3); l1.next.next = Node(5)
l2 = Node(2); l2.next = Node(4); l2.next.next = Node(6)
print(to_list(merge_lists(l1, l2)))  # [1,2,3,4,5,6]
