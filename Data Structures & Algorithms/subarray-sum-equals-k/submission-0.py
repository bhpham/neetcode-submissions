class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums = [2, -1, 1, 2] , k = 2
        # curSum = 4
        # res = 4
        # prefixSum = { 0:1, 1:1, 2:2, 4:1 }

        prefixSum = { 0:1 }
        curSum = 0
        res = 0

        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        
        return res

        # TC: O(n) where n is the size of nums input array
        # SC: O(n) where n could go up to the size of prefixSum hashMap