"""
- an exellent intro for dp problems: https://leetcode.com/problems/longest-common-subsequence/solution/
"""

"""
- dp (top-down) dfs(i1, i2) calculates the longest common subsequence in arrays text1[:i1 + 1] and text2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1, n2 = len(text1), len(text2)
      
        @lru_cache(None)
        def dp(i1, i2):
            if i1 == n1 or i2 == n2:
                return 0
            if text1[i1] == text2[i2]:
                return 1 + dp(i1 + 1, i2 + 1)
            else:
                return max(dp(i1, i2 + 1), dp(i1 + 1, i2))
            
        return dp(0, 0)

"""
- dp (bottom-up):
- O(mn), O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[-1][-1]


