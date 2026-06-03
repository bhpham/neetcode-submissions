class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # either solve it using monotonic stack 
        # or more optimal with Greedy
        # Let's solve it using Greedy Algorithm

        res = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[res[-1]]:
                res.append(i)     
        res.reverse()
        return res