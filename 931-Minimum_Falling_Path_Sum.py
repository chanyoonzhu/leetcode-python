"""
- similar: 1937. Maximum Number of Points with Cost(hard)
"""
"""
- dynamic problem (bottom-up)
- O(m*n), O(n)
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        if not matrix or not matrix[0]: return 0
        
        M, N = len(matrix), len(matrix[0])
        
        prev_dp = matrix[0]
        
        for r in range(1, M):
            dp = [-101] * N
            for c in range(N):
                dp[c] = min(prev_dp[c], prev_dp[c-1] if c > 0 else float("inf"), prev_dp[c+1] if c < N - 1 else float("inf")) + matrix[r][c]
            prev_dp = dp
        return min(prev_dp)