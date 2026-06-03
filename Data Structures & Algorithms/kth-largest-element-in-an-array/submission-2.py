class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        val = 0
        while maxHeap and k > 0:
            val = -heapq.heappop(maxHeap)
            k -= 1
        
        return val