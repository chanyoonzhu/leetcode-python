"""
Instacart

Input: [
  ["3234.html", "xys.html", "7hsaa.html"], // user1
  ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
]
Output:
["xys.html", "7hsaa.html"]
"""
class Solution:
    def longestCommonSubsequence(self, l1: list, l2: list) -> list:
        
        max_len = 0
        res = []
        n1, n2 = len(l1), len(l2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)] # dp[i][j] - max length of common subarray ending at l1[i] and at l2[j]
        
        for i in range(n1):
            for j in range(n2):
                if l1[i] == l2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    if dp[i+1][j+1] > max_len:
                        max_len = max(max_len, dp[i+1][j+1])
                        res = l2[j-max_len+1:j+1]
                    
        return res
        