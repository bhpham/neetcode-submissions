class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        
        return False

    #TC: O(n) where n is the size of input array nums
    #SC: O(n) as we used an additional hashSet in the memory space
