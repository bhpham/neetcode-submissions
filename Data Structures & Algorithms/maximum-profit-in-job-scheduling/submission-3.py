'''
startTime = [4,2,4,8,2] -> [2,2,4,4,8]
endTime = [5,5,5,10,8] -> [5,5,5,8,10]
profit = [1,2,8,10,4] -> [1,2,4,8,10]

Constraints:
1/ Are given startTime & endTime & profit sorted in order?
2/ Can profit value be negative? 
3/ Does startTime has to be smaller than endTime?

Approach: sort inputs, then brute force with bactracking and perhaps apply memoization to optimize


'''
import bisect 
class Solution:
    # Optimize with a cache
    # TC: O(n * log(n))
    # SC: O(n)
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit)) # O(nlogn)
        cache = {}      # Add a cache
        n = len(startTime)

        def next(l, end):
                r = n 
                while l < r:
                    mid = (l + r) // 2
                    if intervals[mid][0] < end:
                        l = mid + 1
                    else:
                        r = mid
                return l

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            # dont include
            res = dfs(i + 1)

            # include
            cache[i] = res = max(res, intervals[i][2] + dfs(next(i + 1, intervals[i][1])))
            return res
        
        return dfs(0)
        
