class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum: int) -> bool:
    sum = 0
    lstSum = []
    if root is None:
        return False

    pS(root, targetSum, sum, lstSum)

    return lstSum[0] if len(lstSum) > 0 else False


def pS(root, targetSum, sum, lstSum):
    sum += root.val
    if root.left:
        pS(root.left, targetSum, sum, lstSum)
    if root.right:
        pS(root.right, targetSum, sum, lstSum)
    if root.left is None and root.right is None:
        if sum == targetSum:
            lstSum.append(True)


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

    print(hasPathSum(root, 22))
