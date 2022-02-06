"""
- dfs
- O(mn), O(mn): space can be optimized by mutating the original grid (changing "1" to "#" after visiting)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        M, N = len(grid), len(grid[0])
        
        def dfs(r, c):
            nonlocal M, N
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rr, cc = r + i, c + j
                if 0 <= rr < M and 0 <= cc < N and (rr, cc) not in visited and grid[r][c] == "1":
                    visited.add((rr, cc))
                    dfs(rr, cc)
        
        for r in range(M):
            for c in range(N):
                if (r, c) not in visited and grid[r][c] == "1":
                    visited.add(r, c)
                    count += 1
                    dfs(r, c)
        return count

"""
- bfs
- O(mn), O(mn): space can be optimized by mutating the original grid (changing "1" to "#" after visiting)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        M, N = len(grid), len(grid[0])
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def traverse(r, c):
            grid[r][c] = "X"
            for i, j in DIR:
                nr, nc = r + i, c + j
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == "1":
                    traverse(nr, nc)
            
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    res += 1
                    traverse(i, j)
        return res