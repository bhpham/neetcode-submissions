class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            return (
                backtrack(i + 1, cur_sum + nums[i]) +
                backtrack(i + 1, cur_sum - nums[i])
            )
        
        return backtrack(0, 0)