# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.res

# Dry running
'''
root = 1
self.res = 3
dfs(1):
    left: dfs(null)
    right: dfs(2)
        left: dfs(3):
            left: dfs(5)
        right: dfs(4)

'''