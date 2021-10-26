"""
- DFS
- O(n^2), O(n^2)
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int: 

        def dfs(i, j, t):
            if i == self.n - 1 and j == self.n - 1:
                return t
            result = float("inf")
            for i_inc, j_inc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i_next = i + i_inc
                j_next = j + j_inc
                if 0 <= i_next < self.n and 0 <= j_next < self.n:
                    next_t = max(grid[i_next][j_next], t)
                    if (i_next, j_next) not in visited or visited[(i_next, j_next)] > next_t:
                        visited[(i_next, j_next)] = next_t
                        result = min(result, dfs(i_next, j_next, next_t))
            return result
        
        visited = {(0, 0): grid[0][0]}
        self.n = len(grid)
        return dfs(0, 0, grid[0][0])

"""
- greedy with bst and heap (bst, but pop the position with lowest elevation always)
- O(n^2, n^2)
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        
        pq = [(grid[0][0], 0, 0)] # height, i, j
        visited = set()
        visited.add((0, 0))
        
        while pq:
            h, i, j = heapq.heappop(pq)
            if (i, j) == (M - 1, N - 1):
                return h
            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ii < M and 0 <= jj < N and (ii, jj) not in visited:
                    heapq.heappush(pq, (max(h, grid[ii][jj]), ii, jj))
                    visited.add((ii, jj))

"""
- binary search and dfs
- O(n^2logn, n^2)
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        def can_arrive(t):
            q = [(0, 0)]
            visited = {(0, 0)}
            while q:
                i, j = q.pop(0)
                if i == j == n - 1:
                    return True
                for i_next, j_next in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= i_next < n and 0 <= j_next < n and (i_next, j_next) not in visited and grid[i_next][j_next] <= t:
                        q.append((i_next, j_next))
                        visited.add((i_next, j_next))
            return False

        n = len(grid)
        lo, hi = grid[0][0], n * n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_arrive(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

"""
- todo: union-find
"""