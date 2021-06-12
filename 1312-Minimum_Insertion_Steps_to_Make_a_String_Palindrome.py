"""
- dp (top-down), dp[i][j] - the minimum insertions needed for making s[i:j + 1] a palindrom
- O(mn), O(mn)
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if -1 <= j - i <= 0: return 0
            _min = min(dp(i + 1, j), dp(i, j - 1)) + 1
            if s[i] == s[j]:
                _min = min(_min, dp(i + 1, j - 1))     
            return _min
                
        return dp(0, len(s) - 1)

"""
- dp (bottom-up), dp[i][j] - the minimum insertions needed for making s[i:j + 1] a palindrom
- O(mn), O(mn)
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])
        return dp[0][-1]