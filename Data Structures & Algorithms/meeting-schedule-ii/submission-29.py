"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
s = 3       // out of bound when s = 3
e = 1
count = 2
res = max(count, res) = 2
start = [0, 5, 15]  // sorted
end = [10, 20, 40]  // sorted

'''

class Solution:
    #TC: O(nlog(n)) due to sorting where n is number of intervals
    #SC: O(n)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = e = 0 
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        count = res = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        
        return res
