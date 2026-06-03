class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
            
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                return self.check_remaining(s, l + 1, r) or self.check_remaining(s, l, r - 1)
            
        return True


    def check_remaining(self, s, l, r) -> bool:
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        
        return True