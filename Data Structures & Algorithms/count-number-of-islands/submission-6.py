class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # base case
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == "0"):
                return 
            
            grid[r][c] = "0"
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        island = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island += 1
        
        return island

    #TC: O(m * n) Where m is number of rows and n is the number of columns in grid
    #SC: O(m * n) for recursive backtrack to every cells in the matrix
