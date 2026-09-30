class Solution:

    """
    - dp (3D) dp[i][j] = [vertical line length, horizontal line length, diagnal line length, anti-diagonal line length]
    - O(mn), O(mn)
    """
    def longestLine(self, M: List[List[int]]) -> int:
        
        if not M or not M[0]:
            return 0
        
        max_length = 0
        m, n = len(M), len(M[0])
        dp = [[[0] * 4 for _ in range(n + 2)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    dp[i + 1][j + 1] = [dp[i][j + 1][0] + 1,dp[i + 1][j][1] + 1, dp[i][j][2] + 1, dp[i][j + 2][3] + 1]
                    max_length = max(max_length, max(dp[i + 1][j + 1]))
        return max_length
    
    """
    - dp (2D) - only need to keep track of prev line status to calculate current line status
    - O(mn), O(n)
    """
    def longestLine(self, M: List[List[int]]) -> int:
        
        if not M or not M[0]:
            return 0
        
        max_length = 0
        m, n = len(M), len(M[0])
        prev = [[0] * 4 for _ in range(n + 2)]
        for i in range(m):
            curr = [[0] * 4 for _ in range(n + 2)]
            for j in range(n):
                if M[i][j] == 1:
                    curr[j + 1] = [prev[j + 1][0] + 1, curr[j][1] + 1, prev[j][2] + 1, prev[j + 2][3] + 1]
                    max_length = max(max_length, max(curr[j + 1]))
            prev = curr
        return max_length