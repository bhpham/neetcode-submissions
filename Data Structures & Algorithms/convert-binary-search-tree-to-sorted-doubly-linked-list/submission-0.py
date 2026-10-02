"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
'''
Tree traversal: LCR (inorder)

head = 1 <-> 2 <-> 3 <-> 4 <-> 5 -> 1

TC: O(n) where n is number of nodes in the binary tree
SC: O(h) where h is the height of the binary tree
'''

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.head = None    # head of DLL
        self.prev = None    # tail of DLL

        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)

            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.head = node
            
            self.prev = node    # update prev to current

            dfs(node.right)
        
        dfs(root)

        # make circular: connect head and tail
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head
        
        
            





        