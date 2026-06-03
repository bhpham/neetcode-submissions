class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {')': '(', ']':'[', '}': '{'}
        stack = []

        for c in s:
            if c in closedToOpen:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack