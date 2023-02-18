class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def averageOfLevels(self, root):
        queue = deque([root])
        ans = []
        while queue:
            level_len = count = len(queue)
            level_sum = 0
            while count:
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count -= 1

            ans.append(level_sum / level_len)
        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    a = Solution()
    print(a.averageOfLevels(root))
