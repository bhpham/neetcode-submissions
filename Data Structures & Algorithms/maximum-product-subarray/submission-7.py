class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minSub, maxSub = 1, 1
        
        for n in nums:
            if n == 0:
                maxSub, minSub = 1, 1
                continue

            tmp = maxSub * n
            maxSub = max(maxSub * n, minSub * n, n)
            minSub = min(minSub * n, tmp, n)
            res = max(res, maxSub)
        
        return res