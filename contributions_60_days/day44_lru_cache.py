class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity; self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _add(self, node):
        n = self.head.next
        self.head.next = node
        node.prev, node.next = self.head, n
        n.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node); self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node; self._add(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru); del self.cache[lru.key]

if __name__ == "__main__":
    lru = LRUCache(2); lru.put(1, 1); print(lru.get(1))
