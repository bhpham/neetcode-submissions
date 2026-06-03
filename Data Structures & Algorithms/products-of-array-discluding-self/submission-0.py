class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, posfix = 1, 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for j in range(len(nums) -1, -1, -1):
            res[j] *= posfix
            posfix *= nums[j]
        
        return res