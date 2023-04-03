class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, target):
        self.result = 0
        cache = {0: 1}
        self.dfs(root, target, 0, cache)
        return self.result

    def dfs(self, root, target, currentPathSum, cache):
        if not root: return

        currentPathSum += root.val
        oldPathSum = currentPathSum - target
        # checks if the oldPathSum exists in the cache. If it does, it adds the count of the oldPathSum
        # to the result variable. If it doesn't, it adds 0 to the result variable.
        self.result += cache.get(oldPathSum, 0)
        # updates the cache by adding the currentPathSum to it. If currentPathSum already exists in the cache,it
        # increments its count by 1. This is done to keep track of the number of times a path sum has been seen so far.
        cache[currentPathSum] = cache.get(currentPathSum, 0) + 1

        self.dfs(root.left, target, currentPathSum, cache)
        self.dfs(root.right, target, currentPathSum, cache)
        # updates the cache by decrementing the count of currentPathSum by 1. This is done to remove the currentPathSum
        # from the cache once the recursion is done with the current node and its children.
        cache[currentPathSum] -= 1


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    a = Solution()
    print(a.pathSum(root, 8))
