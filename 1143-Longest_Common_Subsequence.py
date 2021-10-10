"""
- an exellent intro for dp problems: https://leetcode.com/problems/longest-common-subsequence/solution/
"""

"""
- dp (top-down) dfs(i1, i2) calculates the longest common subsequence in arrays text1[:i1 + 1] and text2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def dp(i1, i2):
            if i1 == -1 or i2 == -1:
                return 0
            if (i1, i2) not in memo:
                if text1[i1] == text2[i2]: # 1. first chars equal, then consume first chars
                    longest = 1 + dp(i1 - 1, i2 - 1)
                else: # 2. first char not equal, then skip current char in either string
                    longest = max(dp(i1, i2 - 1), dp(i1 - 1, i2))
                memo[i1, i2] = longest
            return memo[i1, i2]
        
        return dp(len(text1) - 1, len(text2) - 1)

"""
- dp (bottom-up): since L40 and L42 show that rows and cols with higher indexes need to be calculated first, we need to start from the higher indexes in the loops
- O(mn), O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        
        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]


