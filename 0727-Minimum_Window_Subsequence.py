"""
- dynamic programming (top-down)
- O(mn), O(mn)
"""
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        @lru_cache(None)
        def dp(i1, i2): # dp(i1, i2) -> length of minimum window of s2[:i2+1] being a subsequence of s1[:i1+1]
            if i2 < 0: # s2 fully matched
                return 0
            if i1 < 0: # s2 not fully matched when s1 exhausted
                return float("inf")
            if s1[i1] == s2[i2]:
                return 1 + dp(i1-1, i2-1) # greedily match as we see equal
            else:
                return 1 + dp(i1-1, i2) # match next in s1
            
        min_len = float("inf")
        for i in range(len(s1)):
            min_len = min(min_len, dp(i, len(s2)-1))
                
        if min_len == float("inf"): return ""
        for i in range(len(s1)):
            if dp(i, len(s2)-1) == min_len:
                return s1[i-min_len+1:i+1]

"""
- dynamic programming
- O(mn), O(mn)
"""
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        N1, N2 = len(s1), len(s2)
        dp = [[float("inf")] * (N1 + 1) for _ in range(N2 + 1)] # dp[i][j] length of minimum window subsequence of s1[:j+1] and s2[:i+1] endint at letter s1[j]
        
        for i in range(N2 + 1):
            for j in range(N1 + 1):
                if i == 0:
                    dp[i][j] = 0
                else:
                    if s1[j-1] == s2[i-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = dp[i][j-1] + 1
                        
        min_len = min(dp[-1])
        if min_len == float("inf"): return ""
        for j in range(1, N1 + 1):
            if dp[-1][j] == min_len:
                return s1[j-min_len:j]
        
        