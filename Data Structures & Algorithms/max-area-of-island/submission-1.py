class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #bfs
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        maxArea = 0

        def bfs(r, c):
            area = 0
            q.append((r, c))
            visit.add((r, c))
            area += 1

            while q:
                row, col = q.popleft()
                directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and
                        (r, c) not in visit and grid[r][c] == 1):
                        q.append((r, c))
                        visit.add((r, c))
                        area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea
        