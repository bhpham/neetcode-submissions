# Approach: Thinking to use the MinHeap to store the tuple of (dist, x, y)
# We can track smallest/closest distance based on `dist` value

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(minHeap, (dist, x, y))

        heapq.heapify(minHeap)

        while minHeap and k > 0:
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
            k -= 1

        return res
