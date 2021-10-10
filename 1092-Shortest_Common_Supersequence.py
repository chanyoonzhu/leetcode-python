"""
- dynamic programming （top-down)
- dp[i][j] is the shortest common subsequence for str1[:i+1] and str2[:j+1]
- O(mn), O(mn)
- MLE (stores strings in dp array)
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        memo = {}
        
        def dp(i, j):
            if i == -1 and j == -1: return ""
            if i == -1: return str2[:j + 1]
            if j == -1: return str1[:i + 1]
            
            if (i, j) not in memo:
                if str1[i] == str2[j]:
                    memo[(i, j)] = dp(i - 1, j - 1) + str1[i]
                else:
                    prev_i, prev_j = dp(i - 1, j), dp(i, j - 1)
                    if len(prev_i) < len(prev_j):
                        memo[(i, j)] = prev_i + str1[i]
                    else:
                        memo[(i, j)] = prev_j + str2[j]
            return memo[(i, j)]
    
        return dp(len(str1) - 1, len(str2) - 1)

"""
- dynamic programming
- store length only then trace path
- dp[i][j] is the length of the shortest common subsequence for str1[:i+1] and str2[:j+1]
- O(mn), O(mn)
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        N1, N2 = len(str1), len(str2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        dp[0] = [0] + [j for j in range(1, N2 + 1)]
        
        # dp stores the length of the Shortest Common Supersequence
        for i in range(N1 + 1):
            for j in range(N2 + 1):
                if i == 0: 
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if str1[i-1] == str2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                        
        result = []
        i, j = N1, N2
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] < dp[i][j-1]:
                    result.append(str1[i-1])
                    i -= 1
                else:
                    result.append(str2[j-1])
                    j -= 1
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        return ''.join(result[::-1])