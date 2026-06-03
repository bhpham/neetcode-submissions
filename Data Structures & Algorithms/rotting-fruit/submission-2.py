class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and
                        grid[r][c] == 1):
                        fresh -= 1
                        grid[r][c] = 0
                        q.append((r, c))
            time += 1
        
        return time if fresh == 0 else -1
        
        # Time complexity: O(m * n)
        # Space complexity: O(m * n)