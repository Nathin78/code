# Level order (BFS) traversal of binary tree
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val; self.left = None; self.right = None

def level_order(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

root = TreeNode(3); root.left = TreeNode(9); root.right = TreeNode(20)
root.right.left = TreeNode(15); root.right.right = TreeNode(7)
print(level_order(root))  # [[3],[9,20],[15,7]]
