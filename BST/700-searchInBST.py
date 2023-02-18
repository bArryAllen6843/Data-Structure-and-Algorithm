class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val: int):
        def f(root, ans):
            if root.val == val:
                return printTree(root, ans)
            elif val < root.val:
                f(root.left, ans)
                if len(ans)>0:
                    return ans
            else:
                f(root.right, ans)
                if len(ans)>0:
                    return ans

        ans = f(root, [])
        return ans


def printTree(root, ans):
    if root:
        ans.append(root.val)
        printTree(root.left, ans)
        printTree(root.right, ans)
    return ans


if __name__ == '__main__':

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    a = Solution()
    b = a.searchBST(root, 2)
    print(b)
