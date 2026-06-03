# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # optimize O(n) time complexity with Stack
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

        
        #Brute force
        # arr = []

        # def dfs(node):
        #     if not node:
        #         return None
            
        #     arr.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        #     return 
        
        # dfs(root)
        # arr.sort()
        # return arr[k - 1]

        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        