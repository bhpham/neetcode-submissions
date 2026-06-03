class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}  # diff -> idx

        for i, a in enumerate(nums):
            diff = target - a
            if diff in numMap:
                return [numMap[diff], i]
            numMap[a] = i
    