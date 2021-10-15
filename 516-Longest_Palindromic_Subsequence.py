"""
- dynamic programming (top-down)
- O(n^2), O(n^2)
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
        
        return dp(0, len(s) - 1)

"""
- dynamic programming (bottom-up)
- O(n^2), O(n^2)
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for diff in range(N):
            for i in range(N - diff):
                if diff == 0: 
                    dp[i][i] = 1
                else:
                    j = i + diff
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][N-1]
