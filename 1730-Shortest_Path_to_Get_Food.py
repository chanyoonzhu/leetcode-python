"""
- bfs
- O(mn), O(mn)
"""
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        M, N = len(grid), len(grid[0])
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        visited = set()
        # find start pos
        start_pos = None
        for r in range(M):
            for c in range(N):
                if grid[r][c] == "*":
                    q.append((r, c, 0))
                    visited.add((r, c))
                    break
            if q:
                break
        
        while q:
            r, c, step = q.popleft()
            if grid[r][c] == "#":
                return step
            for i, j in DIR:
                rr, cc = r + i, c + j
                if 0 <= rr < M and 0 <= cc < N and (rr, cc) not in visited and grid[rr][cc] in ["O", "#"]:
                    q.append((rr, cc, step + 1))
                    visited.add((rr, cc))
        return -1