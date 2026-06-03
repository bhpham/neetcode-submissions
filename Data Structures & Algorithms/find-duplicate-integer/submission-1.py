class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        newSlow = 0
        while slow:
            newSlow = nums[newSlow]
            slow = nums[slow]
            if newSlow == slow:
                return slow