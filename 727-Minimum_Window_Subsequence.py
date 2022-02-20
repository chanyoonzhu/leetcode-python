"""
- dynamic programming
- O(mn), O(mn)
"""
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        N1, N2 = len(s1), len(s2)
        dp = [[float("inf")] * (N1 + 1) for _ in range(N2 + 1)]
        
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
        
        