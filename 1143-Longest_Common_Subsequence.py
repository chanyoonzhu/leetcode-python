"""
- an exellent intro for dp problems: https://leetcode.com/problems/longest-common-subsequence/solution/
"""

"""
- dp (top-down) dfs(i1, i2) calculates the longest common subsequence in arrays text1[i1:] and text2[i2:]
- O(mn), O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        
        def dp(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if (i1, i2) not in memo:
                if text1[i1] == text2[i2]: # 1. first chars equal, then consume first chars
                    longest = 1 + dp(i1 + 1, i2 + 1)
                else: # 2. first char not equal, then skip first char in either string
                    longest = max(dp(i1, i2 + 1), dp(i1 + 1, i2))
                memo[i1, i2] = longest
            return memo[i1, i2]
        
        return dp(0, 0)

"""
- dp (bottom-up): since L40 and L42 show that rows and cols with higher indexes need to be calculated first, we need to start from the higher indexes in the loops
- O(mn), O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i1 in range(n1 - 1, -1, -1):
            for i2 in range(n2 - 1, -1, -1):
                if text1[i1] == text2[i2]:
                    dp[i1][i2] = 1 + dp[i1 + 1][i2 + 1]  # rows and cols with higher indexes need to be calculated first
                else:
                    dp[i1][i2] = max(dp[i1 + 1][i2], dp[i1][i2 + 1]) # rows and cols with higher indexes need to be calculated first
        
        return dp[0][0]


