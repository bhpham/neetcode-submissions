import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        res = 0
        while maxHeap and k > 0:
            res = -heapq.heappop(maxHeap)
            k -= 1
        return res