class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    def solve(root, targetSum, path):
        if root is None:
            return None
        targetSum -= root.val
        path.append(root.val)

        if root.left is None and root.right is None:
            if targetSum == 0:
                ans.append(path.copy())
        else:
            solve(root.left, targetSum, path)
            solve(root.right, targetSum, path)
        path.pop()

    ans = []
    solve(root, targetSum, [])
    return ans


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    root.right.right.left = TreeNode(5)

    print(hasPathSum(root, 22))
