class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return 
        
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    cur.append(s[i:j + 1])
                    backtrack(j + 1, cur)
                    cur.pop()

        backtrack(0, [])
        return res
                

    # helper to check whether the s is palindrome
    def isPali(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # Time complexity: O(n * 2^n)
    # Space complexity: O(n)