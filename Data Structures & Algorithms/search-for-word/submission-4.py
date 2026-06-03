class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        
        def dfs(i, r, c):
            # base case
            if i == len(word):
                return True
            # base case 2
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or board[r][c] != word[i]):
                return
            
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

        # Time complexity: O(m * 4^n) Where m is number of cells and n is length of word
        # Space complexity: O(n)
