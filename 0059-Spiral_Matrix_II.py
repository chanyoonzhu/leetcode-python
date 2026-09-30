"""
- Array (2D)
- O(n^2), O(1)
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        LIMITS = [n-1, n-1, 0, 1] # limit of 4 sides: right, down, left, up (note: up side needs to be set to 1, not 0)
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_i = 0
        res = [[0] * n for _ in range(n)]
        r = c = 0
        x = 1
        
        while x <= n ** 2:
            res[r][c] = x
            if LIMITS[dir_i] == (c if dir_i % 2 == 0 else r): # need to make a turn
                LIMITS[dir_i] += (1 if dir_i > 1 else -1)
                dir_i = (dir_i + 1) % 4
            r += DIRS[dir_i][0]
            c += DIRS[dir_i][1]
            x += 1
            
        return res