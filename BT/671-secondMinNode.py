class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root):
        res = [float('inf')]

        def traverse(node):
            if not node: return
            if root.val < node.val < res[0]:
                res[0] = node.val
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return -1 if res[0] == float('inf') else res[0]


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    a = Solution()
    print(a.findSecondMinimumValue(root))
