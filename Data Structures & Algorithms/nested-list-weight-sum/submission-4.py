'''
Analysis
nestedList = [[1, 1], 2, [1, 1]] , depth = 1
    sum = 2 * 1 = 2 + 8 = 10
nestedList = [1, 1], [1, 1], depth = 2
    sum = 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 = 8

'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    #TC: O(N) where N is size of nestedList
    #SC: O(D) where D is the depth of call stack recursive function
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
       # using BFS

        q = deque(nestedList)
        total = 0
        level = 1

        while q:
            for _ in range(len(q)):
                nested = q.popleft()
                if nested.isInteger():
                    total += nested.getInteger() * level
                else:
                    q.extend(nested.getList())      # Add individual elements
            level += 1
        
        return total




        