class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        visit = set()
        q = collections.deque()

        def bfs(r, c):
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.pop()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(ROWS) and c in range(COLS) and 
                        (r, c) not in visit and grid[r][c] == "1"):
                        q.append((r, c))
                        visit.add((r, c))
  
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        
        return island 