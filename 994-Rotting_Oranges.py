"""
- bfs
- O(mn), O(mn)
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        M, N = len(grid), len(grid[0])
        total_orange = rotten_orange = 0
        q = deque()
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    total_orange += 1
                elif grid[r][c] == 1:
                    total_orange += 1
        
        time = 0
        while q:
            r, c, time = q.popleft()
            rotten_orange += 1
            for i, j in DIR:
                nr, nc = r + i, c + j
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, time + 1))
        
        if rotten_orange == total_orange:
            return time
        return -1
        