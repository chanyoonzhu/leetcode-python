"""
- bfs (each house to empty spaces)
- key: mark visited empty space by the house no. of last visited house
- O(n^2*m^2), O(nm)
"""
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        house_no = 2
        dists = [[0] * N for _ in range(M)]
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c, i):
            q = deque()
            q.append((r, c, 0))
            while q:
                rr, cc, dist = q.popleft()
                for di, dj in DIR:
                    nr, nc = rr + di, cc + dj
                    if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == (i - 1 if i > 3 else 0): # easy to miss, only visited empty spaces that are reachable to all previously traversed houses
                        grid[nr][nc] = i
                        dists[nr][nc] += (dist + 1)
                        q.append((nr, nc, dist + 1))
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    house_no += 1 # starts from 3
                    bfs(r, c, house_no)
        
        result = float("inf")
        for r in range(M):
            for c in range(N):
                if grid[r][c] == house_no:
                    result = min(result, dists[r][c])
        return result if result < float("inf") else -1