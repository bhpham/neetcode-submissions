'''
Question:
1/ Are we only given uppercase english letters?

My straight forward approach:
1/ Naive approach: iterate into every cell and run DFS to form the new word
2/ using backtracking(have options to undo from the tree)
TC: O(r * c * L) where r and c is number of rows and cols in board and L is max(len(word))
SC: O(r * c + S) where S is sum length of the word
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

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





