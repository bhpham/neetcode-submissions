# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if root and subRoot and self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    #helper
    def isSameTree(self, r, s):
        if not r and not s:
            return True
        if not r or not s:
            return False
        if r and s and r.val == s.val:
            return self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right)
        else:
            return False