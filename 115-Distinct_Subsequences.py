"""
- dynamic programming (top-down)
- O(s*t), O(s*t)
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        M, N = len(s), len(t)
        
        @lru_cache(None)
        def dp(si, ti):
            nonlocal M, N
            if ti == -1: return 1  # Case t = "", there is a valid subsequence which is empty string.
            if si == ti: return 0 # optimize: use "si < ti: return 0" for early pruning
            ways = dp(si - 1, ti) # choose not match
            if s[si] == t[ti]:
                ways += dp(si - 1, ti - 1) # choose match
            return ways
        
        return dp(len(s) - 1, len(t) - 1)

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