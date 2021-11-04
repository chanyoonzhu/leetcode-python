"""
- dynamic programming (bottom-up)
- O(mn), O(mn)
"""
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxx = [[0] * n for _ in range(m)]
        minn = [[0] * n for _ in range(m)]
        maxx[0][0] = grid[0][0]
        minn[0][0] = grid[0][0]
        for j in range(1, n):
            maxx[0][j] = maxx[0][j - 1] * grid[0][j]
            minn[0][j] = minn[0][j - 1] * grid[0][j]
        for i in range(1, m):
            maxx[i][0] = maxx[i - 1][0] * grid[i][0]
            minn[i][0] = minn[i - 1][0] * grid[i][0]
            
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    maxx[i][j] = max(maxx[i - 1][j], maxx[i][j - 1]) * grid[i][j]
                    minn[i][j] = min(minn[i - 1][j], minn[i][j - 1]) * grid[i][j]
                else:
                    maxx[i][j] = min(minn[i - 1][j], minn[i][j - 1]) * grid[i][j]
                    minn[i][j] = max(maxx[i - 1][j], maxx[i][j - 1]) * grid[i][j]
        return maxx[-1][-1] % (10 ** 9 + 7) if maxx[-1][-1] >= 0 else -1