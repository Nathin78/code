import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next
    def __lt__(self, other):
        return self.val < other.val

def merge_k_lists(lists):
    heap = []
    for l in lists:
        if l: heapq.heappush(heap, l)
    dummy = ListNode()
    curr = dummy
    while heap:
        node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next: heapq.heappush(heap, node.next)
    return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(4))
    l2 = ListNode(2, ListNode(3))
    print(merge_k_lists([l1, l2]).val)
