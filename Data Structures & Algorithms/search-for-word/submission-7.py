''''
Constraints:
1/ what is length of the board? 1 <= 5
2/ what is length of the word? 1 <= 10
3/ Are these only lowercase or uppercase english letters? Yes

My staright forward approach is using DFS or BFS
I will use DFS
'''

class Solution:
    #TC: O(m * 4^n) where m is the number of words and n is the number of characters in the board)
    #SC: O(m * n) where m is the number of cells and n is the number of words
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()       # keep track of visited nodes

        def dfs(r, c, i) -> bool:
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or board[r][c] != word[i]):
                return False
            
            visit.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            visit.remove((r, c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False


