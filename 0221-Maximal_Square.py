"""
- dynamic programming (bottom-up)
dp[i][j] = max_square_side_length
- O(mn), O(mn)
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]
        
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == '0':
                    continue
                up_len = dp[r-1][c] if r > 0 else 0
                left_len = dp[r][c-1] if c > 0 else 0
                up_left_len = dp[r-1][c-1] if r > 0 and c > 0 else 0
                dp[r][c] = min(up_len, left_len, up_left_len) + 1
                result = max(result, dp[r][c])
        return result ** 2

"""
- dynamic programming (bottom-up, space optimized)
dp[i][j] = max_square_side_length
- O(mn), O(n)
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        M, N = len(matrix), len(matrix[0])
        prev_dp = [0] * N
        
        for r in range(M):
            dp = [0] * N
            for c in range(N):
                if matrix[r][c] == '0':
                    continue
                up_len = prev_dp[c]
                left_len = dp[c-1] if c > 0 else 0
                up_left_len = prev_dp[c-1] if c > 0 else 0
                dp[c] = min(up_len, left_len, up_left_len) + 1
                result = max(result, dp[c])
            prev_dp = dp
        return result ** 2
        