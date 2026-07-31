# Singly Linked List implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node; return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

ll = LinkedList()
for v in [1, 2, 3, 4, 5]:
    ll.append(v)
ll.display()
