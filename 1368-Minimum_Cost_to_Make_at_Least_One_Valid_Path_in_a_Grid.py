"""
- dynamic programming + dfs
- TLE: can visit a cell multiple times
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(grid), len(grid[0])
        
        dp = [[float("inf")] * N for _ in range(M)]
        dp[0][0] = 0
        
        def dfs(r, c):
            prev_cost = dp[r][c]
            for i, j in DIR:
                rr, cc = r + i, c + j
                if 0 <= rr < M and 0 <= cc < N:
                    if (i, j) == DIR[grid[r][c]-1]:
                        if prev_cost < dp[rr][cc]: # no need to turn
                            dp[rr][cc] = prev_cost
                            dfs(rr, cc)
                    else: # need to turn
                        if prev_cost + 1 < dp[rr][cc]:
                            dp[rr][cc] = prev_cost + 1
                            dfs(rr, cc)
        
        dfs(0, 0)
        return dp[M-1][N-1]

"""
- bfs + heap (dijkstra)
- a cell still can be visited multiple times
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(grid), len(grid[0])
        
        h = []
        h.append((0, 0, 0)) # cost, i, j
        visited = {}
        visited[(0, 0)] = 0
        
        while h:
            cost, r, c = heapq.heappop(h)
            if (r, c) == (M-1, N-1): return cost
            for i, j in DIR:
                rr, cc, next_cost = r + i, c + j, cost
                if (i, j) != DIR[grid[r][c] - 1]: next_cost += 1 
                if 0 <= rr < M and 0 <= cc < N and ((rr, cc) not in visited or visited[(rr, cc)] > next_cost):
                    heapq.heappush(h, (next_cost, rr, cc))
                    visited[(rr, cc)] = next_cost

"""
- bfs + dfs
- O(mn), O(mn)
- a cell is only visited one time
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(grid), len(grid[0])
        
        cells = [] # stores cells can be visited with current cost
        visited = {}
        
        def dfs(r, c, cost, cells): # greedily populate the cost of all cells can be reached without turning a sign
            if 0 <= r < M and 0 <= c < N and (r, c) not in visited:
                visited[(r, c)] = cost
                cells.append((r, c))
                i, j = DIR[grid[r][c]-1]
                dfs(r + i, c + j, cost, cells)
        
        cost = 0
        dfs(0, 0, cost, cells)
        while cells:
            cells, prev_cells = [], cells
            cost += 1
            for r, c in prev_cells:
                for i, j in DIR:
                    rr, cc = r + i, c + j
                    if 0 <= rr < M and 0 <= cc < N and (rr, cc) not in visited: 
                        dfs(rr, cc, cost, cells)
        
        return visited[(M-1, N-1)]