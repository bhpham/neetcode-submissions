class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            #base case
            if total == target:
                res.append(cur.copy())
                return res
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            #cleanup
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res
