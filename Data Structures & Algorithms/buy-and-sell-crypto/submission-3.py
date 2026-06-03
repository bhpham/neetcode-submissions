class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                res = max(res, prices[r] - prices[l])
                r += 1
            else:
                l = r
        
        return res