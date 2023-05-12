class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = [0]
        f(root, good, root.val)
        return good[0]


def f(root, cnt, curMax):
    if root:
        if root.val >= curMax:
            cnt[0] += 1
            curMax = root.val
        f(root.left, cnt, curMax)
        f(root.right, cnt, curMax)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    a = Solution()
    print(a.goodNodes(root))
