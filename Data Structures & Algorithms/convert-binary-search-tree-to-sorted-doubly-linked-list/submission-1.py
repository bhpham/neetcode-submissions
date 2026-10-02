"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        self.head = None        # head of DLL
        self.prev = None        # tail of DLL

        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)

            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.head = node
            
            self.prev = node
            dfs(node.right)

        dfs(root)

        # make circular: head <-> tail 
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head
    


            





        