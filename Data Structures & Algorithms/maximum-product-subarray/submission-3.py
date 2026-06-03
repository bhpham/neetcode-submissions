class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minSub, maxSub = 1, 1

        for n in nums:
            # if n == 0:
            #     minSub, maxSub = 1, 1
            #     continue

            tmp = maxSub * n
            maxSub = max(maxSub * n, minSub * n, n)
            minSub = min(minSub * n, tmp, n)    
            res = max(res, maxSub)
        
        return res

        # Time complexity: O(n)
        # Space complexity: O(1)