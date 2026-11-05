'''
Constraints:
1/ No duplicates in the sequence

20 -> 
10 -> 
2 -> 3 -> 4 -> 5

return len(res) = 4
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)  # O(1) lookup

        for n in numSet:
            if (n - 1) not in numSet:
                nextNum = n + 1
                while nextNum in numSet:
                    nextNum += 1
                longest = max(longest, nextNum - n)
        
        return longest