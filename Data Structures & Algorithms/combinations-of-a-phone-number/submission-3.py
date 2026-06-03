class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }       # mapping digit -> chars

        res = []
        def dfs(i, cur):
            # base case 
            if i == len(digits):
                res.append(cur[:])
                return res
            
            for nei in digitToChar[digits[i]]:
                dfs(i + 1, cur + nei)
        
        if digits:
            dfs(0, "")
        
        return res 