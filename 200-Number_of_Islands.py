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
        
        result = 0
        M, N = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r, c):
            nonlocal M, N
            q = collections.deque()
            q.append((r, c))
            while q:
                i, j = q.popleft()
                for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ii < M and 0 <= jj < N and (ii, jj) not in visited and grid[ii][jj] == "1":
                        visited.add((ii, jj))
                        q.append((ii, jj))
        
        for r in range(M):
            for c in range(N):
                if (r, c) not in visited and grid[r][c] == "1":
                    result += 1
                    visited.add((r, c))
                    bfs(r, c)
        return result