"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p_start: 'Node', q_start: 'Node') -> 'Node':
        p, q = p_start, q_start

        while p != q:
            if p.parent is not None:
                p = p.parent
            else:
                p = q_start
            
            if q.parent is not None:
                q = q.parent
            else:
                q = p_start

        return p

        # TC: O(n)
        # SC: O(1)