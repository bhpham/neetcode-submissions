class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                v1 = stack.pop()
                v2 = stack.pop() 
                stack.append(int(float(v2) / v1))    
            else:
                stack.append(int(t))

        return stack[-1]    