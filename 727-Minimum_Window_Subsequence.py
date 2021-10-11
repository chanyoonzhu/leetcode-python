"""
- dynamic programming
- O(mn), O(mn)
"""
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
    
        M, N = len(s1), len(s2)
        dp = [[float("inf")] * (M + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            for j in range(M + 1):
                if i == 0:
                    dp[i][j] = 0
                else:
                    if s1[j-1] == s2[i-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = dp[i][j-1] + 1
                        
        res = min(dp[-1])
        if res == float('inf'): return ''
        for j in range(1, M + 1):
            if dp[-1][j] == res:
                return s1[j - res:j]