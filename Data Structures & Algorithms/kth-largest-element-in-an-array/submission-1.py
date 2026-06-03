class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        while maxHeap and k > 0:
            num = -heapq.heappop(maxHeap)
            k -= 1
            if k == 0:
                return num
        


