class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        maxHeight = heights[len(heights) - 1]
        res.append(len(heights) - 1)
        
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxHeight:
                res.append(i)
                maxHeight = heights[i]
        
        return res[::-1]