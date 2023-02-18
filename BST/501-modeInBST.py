class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = None
    ans = []
    max_count = 0
    curr_count = 0

    def findMode(self, root):
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)

        self.curr_count = 1 if root.val != self.prev else self.curr_count + 1

        if self.curr_count == self.max_count:
            self.ans.append(root.val)
        elif self.curr_count > self.max_count:
            self.ans = [root.val]
            self.max_count = self.curr_count

        self.prev = root.val
        self.dfs(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(2)

    mode = Solution()
    print(mode.findMode(root))
