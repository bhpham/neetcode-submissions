class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l, r = 0, N - 1
        res = [0] * N
        res_idx = N - 1

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[res_idx] = nums[r] * nums[r]
                r -= 1
            else:
                res[res_idx] = nums[l] * nums[l]
                l += 1
            res_idx -= 1
        
        return res