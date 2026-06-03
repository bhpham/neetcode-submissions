class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        q = deque([(0, 0, 1)])      # (row, col, length)
        visited = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                      [1, 1], [1, -1], [-1, -1], [-1, 1]]
        
        while q:
            r, c, length = q.popleft()
            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (0 <= row < N and 0 <= col < N and
                    (row, col) not in visited and grid[row][col] == 0):
                    visited.add((row, col))
                    q.append((row, col, length + 1))
        
        return -1
