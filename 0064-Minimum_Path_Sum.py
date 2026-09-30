"""
- dynamic programming (2D top-down)
- O(mn), O(mn)
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
        
        def dfs(r, c):
            nonlocal m, n
            if dp[r][c] == float("inf"):
                dp[r][c] = grid[r][c] + min([dfs(rr, cc) for rr, cc in [(r + 1, c), (r, c + 1)] if 0 <= rr < m and 0 <= cc < n], default=0)
            return dp[r][c]
        
        return dfs(0, 0)  

"""
- dynamic programming (2D bottom-up)
- O(mn), O(mn)
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
    
        for r in range(m-2, -1, -1):
            dp[r][n-1] = grid[r][n-1] + dp[r+1][n-1]
        for c in range(n-2, -1, -1):
            dp[m-1][c] = grid[m-1][c] + dp[m-1][c+1]
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = min(dp[r+1][c] , dp[r][c+1]) + grid[r][c]
        return dp[0][0] 

"""
- dynamic programming (2D bottom-up, space optimized)
- O(mn), O(m)
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        prev_dp = [float("inf")] * m
        prev_dp[m-1] = grid[m-1][n-1]
    
        for r in range(m-2, -1, -1):
            prev_dp[r] = grid[r][n-1] + prev_dp[r+1]
        for c in range(n-2, -1, -1):
            dp = [float("inf")] * m
            for r in range(m-1, -1, -1):
                if r < m - 1:
                    dp[r] = dp[r + 1]
                dp[r] = min(dp[r], prev_dp[r]) + grid[r][c]
            prev_dp = dp
        return prev_dp[0]         