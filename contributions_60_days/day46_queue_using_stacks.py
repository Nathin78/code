class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None: self.s1.append(x)
    def pop(self) -> int: self._move(); return self.s2.pop()
    def peek(self) -> int: self._move(); return self.s2[-1]
    def empty(self) -> bool: return not self.s1 and not self.s2
    def _move(self):
        if not self.s2:
            while self.s1: self.s2.append(self.s1.pop())

if __name__ == "__main__":
    q = MyQueue(); q.push(1); print(q.peek())
