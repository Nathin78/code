class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None

if __name__ == "__main__":
    p, q = TreeNode(2), TreeNode(8)
    root = TreeNode(6, p, q)
    print(lowest_common_ancestor(root, p, q).val)
