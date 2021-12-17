"""
- dynamic programming 
- O(mn), O(mn)
"""
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        dp_left_up = [[(0, 0)] * N for _ in range(M)] # (left_sum, up_sum)
        dp_right_down = [[(0, 0)] * N for _ in range(M)] # (right_sum, down_sum)
        
        for i in range(M):
            for j in range(N):
                # lu_r: leftup_row, lu_c: leftup_col, rd_r: rightdown_row, rd_c: rightdown_col
                lu_r, lu_c, rd_r, rd_c = i, j, M - 1 - i, N - 1 - j
                if grid[lu_r][lu_c] != 'W':
                    left_sum, up_sum = dp_left_up[lu_r][lu_c-1][0] if lu_c > 0 else 0, dp_left_up[lu_r-1][lu_c][1] if lu_r > 0 else 0
                    if grid[lu_r][lu_c] == 'E':
                        dp_left_up[lu_r][lu_c] = (left_sum + 1, up_sum + 1)
                    elif grid[lu_r][lu_c] == '0':
                        dp_left_up[lu_r][lu_c] = (left_sum, up_sum)
                if grid[rd_r][rd_c] != 'W':
                    right_sum, down_sum = dp_right_down[rd_r][rd_c+1][0] if rd_c+1 < N else 0, dp_right_down[rd_r+1][rd_c][1] if rd_r+1 < M else 0
                    if grid[rd_r][rd_c] == 'E':
                        dp_right_down[rd_r][rd_c] = (right_sum + 1, down_sum + 1)
                    elif grid[rd_r][rd_c] == '0':
                        dp_right_down[rd_r][rd_c] = (right_sum, down_sum)
        
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "0":
                    res = max(res, sum(dp_left_up[i][j]) + sum(dp_right_down[i][j]))
        return res