'''
s = 'neetcode'
wordDict = ['neet', 'code']

dp[8] = True
dp[7] = False
dp[6] = False
dp[5] = False
dp[4] = True
dp[3] = False
dp[2] = False
dp[1] = False
dp[0] = True
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i >= 0 and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]