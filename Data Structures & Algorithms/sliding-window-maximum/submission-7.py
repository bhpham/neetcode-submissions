'''
Questions:
1. What is the size of nums input?
2. What is the range of values of nums? 
3. What is length size?

1/ Naive brute-force approach: 2 nested loops with kth window; TC: O(n^2)
2/ Optimize it with sliding window approach with the monotonically decreasing queue

nums = [1,2,1,0,4,2,6], k = 3
queue = [4,1,0,]
res = [2,2]
l = 1
r = 1

'''

# Monotonically decreasing queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []
        l = r = 0 

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
        
            if l > q[0]:
                q.popleft()

            # check window size
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output


