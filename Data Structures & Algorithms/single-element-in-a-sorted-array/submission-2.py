class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]) or (i < len(nums) - 1 and nums[i] == nums[i + 1]):
                continue
            return nums[i]
            
