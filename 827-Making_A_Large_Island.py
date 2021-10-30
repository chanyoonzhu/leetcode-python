"""
- dfs
- steps:
    1. Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map. Note the grid elements are updated with their corresponding island index. Since the grid has elements 0 or 1. The island index is initialized with 2
    2. Loop every cell == 0, check its connected island index and calculate total islands area. The possible connected island index is stored in a set to remove duplicate index.
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        index_to_area = {} # island index start at 2
        result = 0
        
        def dfs(r, c, index):
            grid[r][c] = index
            area = 1
            for i, j in DIR:
                nr, nc = r + i, c + j
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == 1:
                    area += dfs(nr, nc, index)
            return area
        
        index = 2
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    area = dfs(r, c, index)
                    index_to_area[index] = area
                    result = max(result, area) # easy to miss
                    index += 1
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0:
                    connected_index_to_area = {} # easy to miss: avoid repetitive counts if both neighbors belong to a same island
                    for i, j in DIR:
                        nr, nc = r + i, c + j
                        if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] > 1:
                            connected_index_to_area[grid[nr][nc]] = index_to_area[grid[nr][nc]]
                    result = max(result, sum(connected_index_to_area.values()) + 1)
        
        return result