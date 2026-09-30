"""
- dp (bottom-up)
- O(mn), O(mn)
- caveat: need to break into two directions: left-up and right-down, or will be infinite loop
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float("inf")] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0: 
                    dp[r][c] = 0
                    continue
                if r - 1 >= 0:
                    dp[r][c] = min(dp[r][c], 1 + dp[r-1][c])
                if c - 1 >= 0:
                    dp[r][c] = min(dp[r][c], 1 + dp[r][c-1])
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1 , -1, -1):
                if r + 1 < m:
                    dp[r][c] = min(dp[r][c], 1 + dp[r+1][c])
                if c + 1 < n:
                    dp[r][c] = min(dp[r][c], 1 + dp[r][c+1])
        return dp

"""
- bfs
- O(mn), O(mn)
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float("inf")] * n for _ in range(m)]
        q = []
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0: 
                    dp[r][c] = 0 
                    q.append((r, c, 0))
        
        while q:
            r, c, dist = q.pop(0)
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rr, cc = r + i, c + j
                if 0 <= rr < m and 0 <= cc < n and dp[rr][cc] == float("inf"):
                    q.append((rr, cc, dist + 1))
                    dp[rr][cc] = dist + 1
        return dp