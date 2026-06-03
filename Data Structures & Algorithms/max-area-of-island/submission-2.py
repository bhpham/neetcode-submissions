class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] != 1):
                return 0
            
            visit.add((r, c))
            res = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea