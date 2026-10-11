# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                res.append(lvl)
        
        return res

''' dry run
lvl = [1], [2,3], [4]
res = [[1], [2,3], [4, 5,6,7]]
TC: O(n) where n is the number of nodes in binary tree
SC: O(l) where l is the level in binary tree
'''