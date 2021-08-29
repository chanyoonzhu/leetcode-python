"""
- bfs
- O(mnk), O(mn)
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque()
        q.append((0, 0, 0, 0))
        visited = {}
        visited[(0, 0)] = 0 # need to stores eliminated as value
        M, N = len(grid), len(grid[0])
        while q:
            r, c, step, eliminated = q.popleft()
            if r == M - 1 and c == N - 1 and eliminated <= k:
                return step
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rr, cc = r + i, c + j
                if 0 <= rr < M and 0 <= cc < N:
                    eliminated_next = eliminated + (grid[rr][cc] == 1)
                    if eliminated_next <= k and ((rr, cc) not in visited or eliminated_next < visited[(rr, cc)]): # only traverse if eliminated is smaller than previous traversal
                        q.append((rr, cc, step + 1, eliminated_next))
                        visited[(rr, cc)] = eliminated_next
        return -1