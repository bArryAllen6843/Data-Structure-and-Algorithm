from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root):
        # dfs recursive approach
        def dfs(root, curr):
            if not root: return 0
            curr = curr * 10 + root.val
            if not root.left and not root.right: return curr

            return dfs(root.left, curr) + dfs(root.right, curr)

        return dfs(root, 0)

    # dfs iterative approach
    def sumNumbers1(self, root):
        s, tot_sum = deque([(root, 0)]), 0
        while (len(s)):
            root, cur = s.pop()
            cur = cur * 10 + root.val
            if not root.left and not root.right:
                tot_sum += cur
            if root.right:
                s.append((root.right, cur))
            if root.left:
                s.append((root.left, cur))
        return tot_sum

    # morris traversal
    def sumNumbers2(self, root):
        tot_sum, cur, depth = 0, 0, 0
        while root:
            if root.left:
                pre, depth = root.left, 1
                while pre.right and pre.right != root:
                    pre, depth = pre.right, depth + 1
                if not pre.right:
                    pre.right = root
                    cur = cur * 10 + root.val
                    root = root.left
                else:
                    pre.right = None
                    if not pre.left: tot_sum += cur
                    cur //= 10 ** depth
                    root = root.right
            else:
                cur = cur * 10 + root.val
                if not root.right: tot_sum += cur
                root = root.right
        return tot_sum


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    a = Solution()
    print(a.sumNumbers2(root))
