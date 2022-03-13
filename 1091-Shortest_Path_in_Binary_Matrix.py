"""
- BFS
- O(n), O(n)
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        M, N = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[M-1][N-1]: return -1 # easy to miss
        q = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        
        while q:
            r, c, step = q.popleft()
            if r == M-1 and c == N-1:
                return step
            for i, j in DIR:
                rn, cn = r + i, c + j
                if self.canVisit(grid, rn, cn, visited, M, N):
                    q.append((rn, cn, step + 1))
                    visited.add((rn, cn))
        return -1
            
                
    def canVisit(self, grid, r, c, visited, m, n):
        return 0 <= r < m and 0 <= c < n and (r, c) not in visited and grid[r][c] == 0