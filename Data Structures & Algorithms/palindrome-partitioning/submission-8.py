''''
s = "aab"
i = 0, 1, 2
j = 1, 2
if s[i] == s[j]:
    found palindrome


return a list of every substring is palindrome

Constraints:
1/ what is the length of string s? 50 is max length
2/ Are we only given lowercase english characters? Yes

My straight forward approach is using DFS (backtracking algorithm)
base case is: return it when lenngth of string s == 1

TC: O(2^n * n)
SC: O(n) for auxiliary space result
'''


class Solution:
    #TC: O(2^n * n) where n is the characters in string s
    #SC: O(n) for auxiliary space
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

    # helper
    def isPali(self, s, l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True




