"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    #TC: O(nlogn) for Timsort aka mergeSort where n is the number of intervals
    #SC: O(n) where n is the number of intervals
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        s, e = 0, 0
        count, res = 0, 0

        while s < len(intervals):   
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)
        
        return res

''' dry run
start = {0, 5, 15}
end = {10, 20, 40}
s = 3
e = 1
count = 2
res = 2

'''