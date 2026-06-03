'''
stack = []  (index, temperature)
[5, 40]

stack = [1, 38]

res = [1,4 ,1, 2,1 ,0, 0]

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []      # (index, temperature)
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackIdx, stackT = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append((idx, temp))
        
        return res