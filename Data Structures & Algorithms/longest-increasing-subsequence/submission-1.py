class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [1, 2, 4, 3]
        # LIS[3] = 1
        # LIS[2] = max(1 + LIS[3]) = 2
        # LIS[1] = max(1 + LIS[2], 1 + LIS[3]) = 3

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)