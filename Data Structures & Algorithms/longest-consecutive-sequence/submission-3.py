class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in nums:
            if (n - 1) not in numSet:
                nextNum = n + 1
                while nextNum in numSet:
                    nextNum += 1
                longest = max(longest, nextNum - n)
        
        return longest