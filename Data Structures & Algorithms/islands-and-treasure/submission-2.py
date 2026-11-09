class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addGrid(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == -1):
                return 
            q.append((r, c))
            visit.add((r, c))

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addGrid(row + 1, col)
                addGrid(row - 1, col)
                addGrid(row, col + 1)
                addGrid(row, col - 1)
            dist += 1
                    
                
    