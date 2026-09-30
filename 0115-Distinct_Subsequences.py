"""
- dynamic programming (top-down)
- O(s*t), O(s*t)
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
                
        @lru_cache(None)
        def dp(si, ti):
            if ti == -1: return 1  # Case t = "", there is a valid subsequence which is empty string.
            if si == ti: return 0 # optimize: use "si < ti: return 0" for early pruning
            ways = dp(si - 1, ti) # choose not match
            if s[si] == t[ti]:
                ways += dp(si - 1, ti - 1) # choose match
            return ways
        
        return dp(len(s) - 1, len(t) - 1)
"""
- dynamic programming (bottom-up)
- O(s*t), O(s*t)
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    
        M, N = len(t), len(s)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = 1
        
        for i in range(M + 1):
            for j in range(1, N + 1):
                if i == 0: 
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1]
                    if s[j-1] == t[i-1]:
                        dp[i][j] += dp[i-1][j-1]
        return dp[M][N]

"""
- dynamic programming (bottom-up)
- O(s*t), O(t)
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        M, N = len(s), len(t)
        prev_dp = [1] + [0] * N
            
        for i in range(1, M + 1):
            dp = [1] + [0] * N
            for j in range(1, N + 1):
                dp[j] = prev_dp[j]
                if s[i-1] == t[j-1]:
                    dp[j] += prev_dp[j-1]
            prev_dp = dp
        return prev_dp[N]