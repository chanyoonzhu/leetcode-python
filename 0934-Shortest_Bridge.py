"""
- dfs + bfs
- dfs to map one island, bfs to find the shortest path to the second island
- O(mn), O(mn)
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        island1 = set()
        
        def dfs(r, c):
            nonlocal M, N
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= rr < M and 0 <= cc < N and (rr, cc) not in island1 and grid[rr][cc] == 1:
                    island1.add((rr, cc))
                    dfs(rr, cc)
        
        found_island1 = False
        for r in range(M):
            for c in range(N):
                if (r, c) not in island1 and grid[r][c] == 1:
                    found_island1 = True
                    island1.add((r, c))
                    dfs(r, c)
                    break # note: only need to map one island, remember to break when one is found
            if found_island1: break
        
        q = [(r, c, 0) for r, c in island1]
        visited = set([(r, c) for r, c in island1])
        while q:
            r, c, dist = q.pop(0)
            if (r, c) not in island1 and grid[r][c] == 1:
                return dist - 1
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= rr < M and 0 <= cc < N and (rr, cc) not in visited and (rr, cc) not in island1:
                    visited.add((rr, cc))
                    q.append((rr, cc, dist + 1))
        return -1