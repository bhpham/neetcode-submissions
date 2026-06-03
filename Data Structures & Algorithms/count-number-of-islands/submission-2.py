class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        island =0

        def bfs(r, c):
            q.append((r, c))
            while q:
                r, c = q.popleft()
                directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or 
                        (nr, nc) in visit or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        
        return island