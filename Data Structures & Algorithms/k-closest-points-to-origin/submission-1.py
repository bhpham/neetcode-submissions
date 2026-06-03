class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            distance = x ** 2 + y ** 2
            minHeap.append((distance, x, y))
        
        heapq.heapify(minHeap)
        
        while minHeap and k > 0:
            _, x, y = heapq.heappop(minHeap)
            k -= 1
            res.append((x, y))
        
        return res

        