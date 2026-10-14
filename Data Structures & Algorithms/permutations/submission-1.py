'''
nums = [1,2,3]
        1     2     3
    2     3. 1
output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Constraints:
1/ unique integers

'''
#TC: O(n * n!)
#SC: O(n * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def swap(a, b) -> None:
            nums[a], nums[b] = nums[b], nums[a]

        def backtrack(i):
            if i == len(nums):
                res.append(nums.copy())
                return 

            for j in range(i, len(nums)):
                swap(i, j)  
                backtrack(i + 1)
                swap(i, j)

        backtrack(0)
        return res
