"""
- hard part: bricks connected to hit brick may still be able to stick if connected to other stable bricks
"""

"""
- dfs (reversely add bricks back)
- O(m*n*h), O(m*n)
- https://tinyurl.com/ftsuv54k
"""
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # 2 - has brick after all hits, 1 - has brick before all hits, 0 - no brick, -1 - no brick and got hit
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            ret = 1
            grid[i][j] = 2
            ret += sum(dfs(x, y) for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
            return ret
        
        # check whether (i, j) is connected bricks still exist after all hits
        def is_connected(i, j):
            return i == 0 or any([0 <= x < m and 0 <= y < n and grid[x][y] == 2 for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]])
        
        # get grid after all hits
        for i, j in hits: grid[i][j] -= 1
        for j in range(n): dfs(0, j)

        # Reversely add the block of each hits and get count of newly add bricks
        result = [0] * len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                result[k] = dfs(i, j) - 1
        return result

"""
- todo: union find
"""
                        
                
            
            
            