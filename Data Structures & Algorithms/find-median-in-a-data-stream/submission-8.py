class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []     # small=maxHeap, large=minHeap        

    #TC: O(log(n)) 
    #SC: O(n) where n is the auxiliary space of small/large heaps
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and 
            -1 * self.small[0] > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
        
        # what if diff length?
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        

    #TC: O(1)
    #SC: O(n)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2

''' Dry run
arr = [1, 3]
small = [-2, -1]
large = [3]
addNum(1)
findMedian
addnum(3)
findMedian: 2.0
AddNum(2)
findMedian: 2.0

'''
        