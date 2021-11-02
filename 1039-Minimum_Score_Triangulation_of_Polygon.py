"""
- similar: 312 burst ballons
"""
"""
- dp (top-down)
- dfs(i, j) calculates the minimum score to triangulate A[i] ~ A[j]
    dfs(i, j) = min(dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j]))
- O(n^3), O(n^2)
"""
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        
        def dfs(i, j):
            if (i, j) not in memo:
                mini = float("inf")
                for k in range(i + 1, j):
                    mini = min(mini, dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j])
                memo[i, j] = mini if mini != float("inf") else 0
                """simplified L13-15
                memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
                """
                return memo[i, j] 
        return dfs(0, len(values) - 1)

"""
- dp (bottom-up)
- dp[i][j] is the minimum score to triangulate A[i] ~ A[j]
    dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]))
- to calculate dp[i1][j1], must guarantee that dp[i2][j2] has already been calculated where j2 - i2 < j1 - i1
- O(n^3), O(n^2)
"""
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        N = len(values)
        dp = [[0] * N for _ in range(N)]
        
        for diff in range(2, N):
            for l in range(N - diff):
                if diff == 2:
                    dp[l][l+2] = values[l] * values[l+1] * values[l+2]
                else:
                    r = l + diff
                    dp[l][r] = float("inf")
                    for k in range(l+1, r):
                        dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] + values[l] * values[k] * values[r])
        
        return dp[0][N-1]