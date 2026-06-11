class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    res = []
    def helper(node):
        if not node: return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    helper(root)
    return res

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(inorder_traversal(root))
