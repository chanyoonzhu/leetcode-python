"""
- dfs
- O(mn), -O(mn)
- store each of the island's positions (relative to its start position) in sets
- count length of sets
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c, r0, c0, points):
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= rr < M and 0 <= cc < N and grid[rr][cc] == 1 and (rr, cc) not in visited:
                    points.append((rr - r0, cc - c0)) # stores pos relative to the start pos
                    visited.add((rr, cc))
                    dfs(rr, cc, r0, c0, points)
                    
            
        islands = set()
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1 and (r, c) not in visited:
                    points = []
                    dfs(r, c, r, c, points)
                    islands.add(tuple(points)) # use tuple to "serialize" list
        return len(islands)
        
        
        