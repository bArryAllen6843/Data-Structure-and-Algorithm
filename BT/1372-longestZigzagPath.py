class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root):
        def dfs(root):
            if not root:
                return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]

        return dfs(root)[-1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right.left = TreeNode(1)
    root.right.right.right = TreeNode(1)
    root.right.right.left.right = TreeNode(1)
    root.right.right.left.right.right = TreeNode(1)

    a = Solution()
    print(a.longestZigZag(root))
