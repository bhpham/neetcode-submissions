'''
s = "racecariscar"
wordDict = ["racecar, "race", "car", "is"]

Constraints:
1/ Are we given only lowercase english characters? Yes
2/ What is length of string s? 20

My straightforward approach is using DFS with backtracking
to find all possible substring that make up to the composition in wordDict

TC: O(s * w) = O(n^2)
SC: O(n) where n is size of characters to store in the hashset
'''

class Solution:
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
                strings = backtrack(j + 1)
                if not strings:
                    continue
                for substr in strings:
                    sentence = w
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
            
            cache[i] = res
            return res
        
        return backtrack(0)

                




