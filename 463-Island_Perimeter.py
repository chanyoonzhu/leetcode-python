"""
- dfs
- O(mn), O(1)
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.res = 0
        M, N = len(grid), len(grid[0])
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def isBoundary(neighbor_r, neighbor_c):
            if neighbor_r < 0 or neighbor_r >= M or neighbor_c < 0 or neighbor_c >= N:
                return True
            if grid[neighbor_r][neighbor_c] == 0:
                return True
            return False
        
        def dfs(r, c):
            if grid[r][c] != 1:
                return
            grid[r][c] = 2
            for i, j in DIR:
                nr, nc = r + i, c + j
                if isBoundary(nr, nc):
                    self.res += 1
                else:
                    dfs(nr, nc)
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return self.res

"""
- array iteration (2D)
- O(mn)， O(1)
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        
        return result
        