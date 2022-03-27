"""
- bfs (each house to empty spaces)
- key: mark visited empty space by the house no. of last visited house
- O(n^2*m^2), O(nm)
"""
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        dp = [[0] * N for _ in range(M)]
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def calc_dist(r, c, iid):
            empty_mark = 0 if iid == 3 else iid - 1
            q = deque([(r, c, 0)])
            while q:
                i, j, dist = q.popleft()
                for ii, jj in DIR:
                    ni, nj = i + ii, j + jj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == empty_mark: # easy to miss, only visited empty spaces that are reachable to all previously traversed houses
                        dp[ni][nj] += dist + 1
                        grid[ni][nj] = iid
                        q.append((ni, nj, dist + 1))
        
        iid = 3 # building id starts at 3
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    calc_dist(i, j, iid)
                    iid += 1
        
        res = float("inf")
        for i in range(M):
            for j in range(N):
                if grid[i][j] == iid - 1: # must equal to last id
                    res = min(res, dp[i][j])
                    
        return res if res < float("inf") else -1