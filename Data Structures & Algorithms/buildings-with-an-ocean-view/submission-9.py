class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > heights[res[-1]]:
                res.append(i)
        
        return res[::-1]

    #TC: O(n) as we only scan to the input array once
    #SC: O(n) as we count auxiliary result space