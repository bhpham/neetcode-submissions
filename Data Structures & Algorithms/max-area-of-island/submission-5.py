class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #BFS
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        max_island_area = 0

        def bfs(r, c):
            q.append((r, c))
            visited.add((r, c))
            area = 0

            while q:
                row, col = q.popleft()
                area += 1
                directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr >= 0 and nr < ROWS and
                        nc >= 0 and nc < COLS and
                        (nr, nc) not in visited and grid[nr][nc] == 1):

                        visited.add((nr, nc))
                        q.append((nr, nc))
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_island_area = max(max_island_area, bfs(r, c))
        
        return max_island_area