class Solution:
    #TC: O(m + n * 2^n) where n is the length of string s
    # and m is the sum of the lengths of the strings in wordDict
    #SC: O(m + 2^n)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]

            res = []
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w not in wordDict:
                    continue
                
                string = backtrack(j + 1)
                if not string:
                    continue
                for substr in string:
                    sentence = w 
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
            
            cache[i] = res
            return res
        
        return backtrack(0)

