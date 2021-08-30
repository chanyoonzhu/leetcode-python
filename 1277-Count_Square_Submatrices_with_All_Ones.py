"""
- dynamic programming: dp[i][j] - the side length of the largest square that use matrix[i][j] as its bottom right corner
- O(mn), O(mn) - can be optimized to O(m)
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        result = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    result += dp[i + 1][j + 1]
        return result