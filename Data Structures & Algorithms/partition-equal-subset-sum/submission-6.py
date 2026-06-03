class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check odd length
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        
        return False

    #TC: O(n * target)
    #SC: O(target)