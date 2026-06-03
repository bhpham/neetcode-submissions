class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        op = "+"
        s = s.replace(' ', '')

        for i, c in enumerate(s):
            if c.isdigit():
                cur = cur * 10 + int(c)
            
            if not c.isdigit() or i == len(s) - 1:
                if op == "+":
                    stack.append(cur)
                elif op == "-":
                    stack.append(-cur)
                elif op == "*":
                    stack.append(stack.pop() * cur)
                elif op == "/":
                    prev = stack.pop()
                    stack.append(int(prev / cur))
                cur = 0
                op = c
        
        return sum(stack)

