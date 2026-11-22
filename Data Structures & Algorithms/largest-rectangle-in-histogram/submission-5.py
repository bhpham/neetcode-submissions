'''
heights = [7,1,7,2,2,4]
index = 4
stack = [   ]

pop: (1, 7)
pop: (1, 1)
pop: (3, 7)
pop: (5, 4)

maxArea = 7
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackIdx, stackH = stack.pop()
                maxArea = max(maxArea, stackH * (i - stackIdx))
                start = stackIdx
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

