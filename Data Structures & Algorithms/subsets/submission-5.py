class Solution:
    #TC: O(n * 2^n) where n the number of elements in input list
    #SC: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return res
            
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()
            backtrack(i + 1, cur)

        
        backtrack(0, [])
        return res