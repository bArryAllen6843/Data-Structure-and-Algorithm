class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isUnivalTree(root) -> bool:
    # method-1
    # def dfs(node):
    #     return not node or node.val == root.val and dfs(node.left) and dfs(node.right)
    #
    # return dfs(root)

    # method-2
    if not root:
        return True

    if root.left:
        if root.val != root.left.val:
            return False

    if root.right:
        if root.val != root.right.val:
            return False

    return isUnivalTree(root.left) and isUnivalTree(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(isUnivalTree(root))
