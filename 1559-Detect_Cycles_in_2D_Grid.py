"""
- dfs
- O(mn), O(mn)
"""
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        M, N = len(grid), len(grid[0])
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = defaultdict(set) # a global set() also works
        
        def dfs(r, c, prev_r, prev_c):
            val = grid[r][c]
            has_loop = False
            for i, j in DIR:
                nr, nc = r + i, c + j
                if (nr, nc) == (prev_r, prev_c) or nr < 0 or nr >= M or nc < 0 or nc >= N or grid[nr][nc] != val:
                    continue
                if (nr, nc) in visited[val]:
                    return True
                visited[val].add((nr, nc))
                if dfs(nr, nc, r, c):
                    has_loop = True
            return has_loop
        
        for r in range(M):
            for c in range(N):
                val = grid[r][c]
                if (r, c) not in visited[val]:
                    visited[val].add((r, c))
                    if dfs(r, c, -1, -1):
                        return True
        return False