'''
stones = [-6, -4, -3, -2, -2]
pop()
pop()
y = 6, 2
x = 4, 

heap =[-3, -2, -2, -2]
pop()
pop()
y = 3, 1
x = 2

heap = [-2, -2, -1]
pop()
pop()
y = 2
x = 2 
heap =[-1]
-> 1 as res
TC: O(n * log(n)) where n is the number of stones in input list


'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first, second = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if first < second:
                heapq.heappush(maxHeap, first - second)
        
        return -maxHeap[0] if maxHeap else 0

