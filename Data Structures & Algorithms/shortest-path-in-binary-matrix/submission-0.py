class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        q = deque([(0, 0, 1)])      # (row, col, length)
        visit = set((0, 0))         # (row, col)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                      (1, 1), (-1, 1), (-1, -1), (-1, 1)]

        while q:
            r, c, length = q.popleft()
            if r == N - 1 and c == N - 1:
                return length 

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr >= 0 and nr < N and nc >= 0 and nc < N and
                    grid[nr][nc] == 0 and (nr, nc) not in visit):
                    q.append((nr, nc, length + 1))
                    visit.add((nr, nc))
        
        return -1