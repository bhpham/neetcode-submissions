class Solution:
    #TC: O(n * 2^n)
    #SC: O(2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, cur):
            res.append(cur[:])
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                cur.append(nums[j])
                backtrack(j + 1, cur)
                cur.pop()
                
        
        backtrack(0, [])
        return res