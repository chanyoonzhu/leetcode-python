"""
- dynamic programming
- challenge: each '1' can be corner of multiple rectangles, any of them can be the largest (unlike problem 221 with only squares)
- O(m^2*n), O(mn)
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)] # number of 1's on left side (including self)
        res = 0
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == '1':
                    dp[r][c] = (dp[r][c-1] + 1) if c > 0 else 1
                    temp_r, height, width = r, 0, dp[r][c]
                    while temp_r >= 0 and dp[temp_r][c]: # going up one row at a time to check which rectangle is largest
                        width = min(width, dp[temp_r][c])
                        height += 1
                        res = max(res, width * height)
                        temp_r -= 1
        return res

"""
- m lines of largest histogram (problem 84)
- O(m*n), O(n)
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        M, N = len(matrix), len(matrix[0])
        prev_dp = [0] * (N + 1) # number of 1's on top of it (including self)
        res = 0
        for r in range(M):
            dp = [0] * (N + 1)
            stack = []
            for c in range(N + 1):
                if c < N and matrix[r][c] == '1':
                    dp[c] = (prev_dp[c] + 1) if r > 0 else 1
                while stack and dp[stack[-1]] > dp[c]:
                    rec_h = dp[stack.pop()]
                    rec_w = c - (stack[-1] if stack else -1) - 1
                    res = max(res, rec_h * rec_w)
                stack.append(c)
            prev_dp = dp
        return res