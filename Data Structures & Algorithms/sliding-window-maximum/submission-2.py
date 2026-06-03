'''
Monotonically decreasing queue
nums = [1,2,1,0,4,2,6] , k = 3

q = [6]
output = [2,2,4,4,6]
TC: O(n) 
SC: O(n) as we used extra space for queue data structure
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = r = 0 
        output = []

        while r < len(nums):
            # pop smaller value from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left from q
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output