"""
- dfs
- TLE: can visit a cell multiple times
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(grid), len(grid[0])
        
        cost = [[float("inf")] * N for _ in range(M)]
        cost[0][0] = 0
        
        def dfs(r, c):
            prev_cost = cost[r][c]
            for i, j in DIR:
                rr, cc = r + i, c + j
                if 0 <= rr < M and 0 <= cc < N:
                    if (i, j) == DIR[grid[r][c]-1]:
                        if prev_cost < cost[rr][cc]: # no need to turn
                            cost[rr][cc] = prev_cost
                            dfs(rr, cc)
                    else: # need to turn
                        if prev_cost + 1 < cost[rr][cc]:
                            cost[rr][cc] = prev_cost + 1
                            dfs(rr, cc)
        
        dfs(0, 0)
        return cost[M-1][N-1]

"""
- bfs + heap (dijkstra)
- a cell still can be visited multiple times
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        pq = [(0, 0, 0)]
        visited = set((0, 0))
        
        while pq:
            cost, r, c = heapq.heappop(pq)
            if (r, c) == (M - 1, N - 1): return cost
			
            if (r, c) in visited:
                continue
            visited.add((r, c))
			
            for d, (i, j) in enumerate(DIR, 1):
                nr, nc = r + i, c + j
                if 0 <= nr < M and 0 <= nc < N and (nr, nc) not in visited:
                    if d == grid[r][c]:
                        heapq.heappush(pq, (cost, nr, nc))
                    else:
                        heapq.heappush(pq, (cost + 1, nr, nc))

"""
- bfs
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