"""
- dynamic programming (bottom-up)
- O(n^2), O(n)
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_dp = triangle[0]
        
        for i in range(1, len(triangle)):
            dp = triangle[i]
            width = len(dp)
            for c in range(width):
                dp[c] += min(prev_dp[c] if c < width - 1 else float("inf"), prev_dp[c-1] if c > 0 else float("inf"))
            prev_dp = dp
        
        return min(prev_dp)


"""
- better solution: from bottom row to top row (avoids edge case handling)
- O(n^2), O(1)
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(len(triangle)-2, -1, -1):
            for c in range(len(triangle[i])):
                triangle[i][c] += min(triangle[i+1][c], triangle[i+1][c+1])
        
        return triangle[0][0]
        