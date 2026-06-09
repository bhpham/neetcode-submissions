class Solution:
    #TC: O(m * 4^n) where m is number of cells in grid and n is character length of input word
    #SC: O(n) where n is recursive call stack
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        #DFS
        def dfs(i, r, c):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or board[r][c] != word[i]):
                return False
            
            visit.add((r, c))
            res = (dfs(i + 1, r + 1, c) or
                    dfs(i + 1, r - 1, c) or
                    dfs(i + 1, r, c + 1) or
                    dfs(i + 1, r, c - 1))
            visit.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        
        return False

    