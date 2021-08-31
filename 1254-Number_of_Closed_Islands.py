"""
- dfs
- O(mn), O(mn)
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        result = 0
        M, N = len(grid), len(grid[0])
        
        def is_closed(r, c):
            nonlocal M, N
            closed = True
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if rr == -1 or rr == M or cc == -1 or cc == N: 
                    closed = False # note: cannot return False immediately, need to mark all adjacent as traversed
                    continue
                if (rr, cc) not in visited and grid[rr][cc] == 0:
                    visited.add((rr, cc))
                    if not is_closed(rr, cc):
                        closed = False
            return closed
                    
        
        for r in range(M):
            for c in range(N):
                if (r, c) not in visited and grid[r][c] == 0 and is_closed(r, c):
                    visited.add((r, c))
                    result += 1
        return result