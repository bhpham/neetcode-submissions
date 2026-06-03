class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # optimal way
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return res
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return 
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res

        # Time complexity: O(t / 2m) where t is target and m is minimum value in nums
        # Space complexity: O(t / m)