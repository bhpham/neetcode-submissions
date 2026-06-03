class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nums = [1, 2, 3]
        # [1,2,3], [2,3,1], [1,3,2], [3,2,1], [3,1 2], [2,1,3]
        # pop nums[0] => [2, 3], [3, 2]
        # Doing permutations => [2], [3] , [3] , [2]
        
        res = []        
        if len(nums) <= 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        
        return res
        
