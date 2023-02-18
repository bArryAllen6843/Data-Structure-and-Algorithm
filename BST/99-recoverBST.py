class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recover(root):
    res = []
    lastnode = None
    startnode = None
    prev = None

    def dfs(root):
        if root == None: return
        nonlocal res, lastnode, startnode, prev
        dfs(root.left)
        if prev and prev.val > root.val:
            if not startnode:
                startnode = prev
            lastnode = root
        prev = root

        dfs(root.right)

    dfs(root)
    if startnode and lastnode:
        startnode.val, lastnode.val = lastnode.val, startnode.val


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    recover(root)