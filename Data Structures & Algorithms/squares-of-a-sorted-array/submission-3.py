class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, len(nums) - 1
        res_idx = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[res_idx] = nums[l] * nums[l]
                l += 1
            else:
                res[res_idx] = nums[r] * nums[r]
                r -= 1
            res_idx -= 1
        
        return res