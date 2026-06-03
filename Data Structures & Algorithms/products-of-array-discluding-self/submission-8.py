'''
nums = [1, 2, 4, 6]
output = [48, 24, 12, 8]

nums    = [1,2,4,6]
prefix  = [1,1,2,8]
postfix = [48,24,6,1]
res     = [48,24,12,8]

#1st scan:
res = [1,1,2,8]
prefix = [1,2,8]

#2nd scan:
res = [48,24,12,8]
postfix = 1,6,24,48,48
TC: O(n) + O(n) = O(n) where n is the length of the input array
SC: O(n) if we count the auxiliary space 
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = postfix = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
    
        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * postfix
            postfix = postfix * nums[j]

        return res
            