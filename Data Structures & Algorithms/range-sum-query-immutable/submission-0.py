class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        curSum = 0

        for n in nums:
            curSum += n
            self.prefixSum.append(curSum)
        
    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefixSum[right]
        preLeft = self.prefixSum[left - 1] if left > 0 else 0
        return preRight - preLeft


'''
[-2, 0, 3, -5, 2, -1]
prefixSum = [-2, -2, 1, -4, -2, -3]

[0, 2] = 1 - 0 = 1
[2, 5] = -3 - (-2) = -1
[0, 5] = -3 - 0 = -3

'''
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)