class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Get the count of each task
        #Define the maxHeap by the value of count
        #Define empty
        #Initilize result time to be 0
        # check where the maxHeap or q is not empty, then increase curren time by 1.
        # then check if maxHeap is not null, then pop the left most cnt of the maxHeap
        # then added by 1, after that appending to the queue [(cnt, time)]
        # if q is not empty and current time == idle time (n), pop the 1st value which is cnt then adding it back to maxHeap

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

