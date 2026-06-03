class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        1. Find the valley (first decreasing element from right)
        2. If no valley found, input is the highest permutation
        3. Find the "next_higher" number to the right of the valley
        4. Swap the valley and next_higher
        5. Reverse the tail after the valley
        '''
        valley = None
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                valley = i - 1
                break
            
        if valley == None:
            nums.reverse()
            return
        
        next_higher = len(nums) - 1
        while nums[next_higher] <= nums[valley]:
            next_higher -= 1
        
        nums[valley], nums[next_higher] = nums[next_higher], nums[valley]
        
        left = valley + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1