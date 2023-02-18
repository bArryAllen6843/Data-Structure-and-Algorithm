class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def binaryTreePaths(root):
#     return bt(root, [], '')
#
#
# def bt(root, ans, s):
#     if root is None:
#         return None
#     s += str(root.val)
#     s += '->'
#
#     if not root.left and not root.right:
#         s = s[:-2]
#         ans.append(s)
#     else:
#         bt(root.left, ans, s)
#         bt(root.right, ans, s)
#     return ans

class Solution:
    def invertTree(self, root):
        if root==None:return None

        else:
            temp=root
            self.invertTree(root.left)
            self.invertTree(root.right)

            temp=root.left
            root.left=root.right
            root.right=temp
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    a=Solution()
    print(a.invertTree(root))
