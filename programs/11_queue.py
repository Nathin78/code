# Queue implementation using collections.deque
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue("a"); q.enqueue("b"); q.enqueue("c")
print(q.dequeue())  # a
print(q.dequeue())  # b
