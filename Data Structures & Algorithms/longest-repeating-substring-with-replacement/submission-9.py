#TC: O(n) where n is the size of input string s
#SC: O(n) as we used hashMap for additional memory space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf, l, r, res = 0, 0, 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)

        return res