class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        n = len(startTime)
        cache = {}

        # Binary search
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
