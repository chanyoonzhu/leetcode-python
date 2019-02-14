class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        """
        - O(n^2), O(n^2)
        - dfs with visited
        
        if not grid or len(grid) == 0:
            return 0
        
        visited = [[0] * len(grid[0]) for _ in grid]
        totalIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    totalIslands += 1
                    self.dfs(grid, i, j, visited)
                            
        return totalIslands
    
    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] != '1':
            return
        visited[i][j] = 1
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i, j-1, visited)
        self.dfs(grid, i, j+1, visited)
        """
        
        """
        - O(n^2), O(1)
        - dfs with grid modification
        
        totalIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    totalIslands += 1
                    self.dfs(grid, i, j)
                    
        return totalIslands
    
    def dfs(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
            if grid[i][j] == '1':
                grid[i][j] = '#'
                self.dfs(grid, i-1, j)
                self.dfs(grid, i+1, j)
                self.dfs(grid, i, j-1)
                self.dfs(grid, i, j+1)
            else:
                grid[i][j] = '#'
        """
        
        """
        - O(n^2), O(n^2)
        - bfs with visited
        
        totalIslands = 0
        visited = [[0] * len(grid[0]) for _ in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = 1
                    totalIslands += 1
                    q = [(i, j)]
                    while q:
                        r, c = q.pop(0)
                        if r - 1 >= 0 and grid[r-1][c] == '1' and not visited[r-1][c]: 
                            q.append((r-1, c))
                            visited[r-1][c] = 1
                        if r + 1 < len(grid) and grid[r+1][c] == '1' and not visited[r+1][c]: 
                            q.append((r+1, c))
                            visited[r+1][c] = 1
                        if c - 1 >= 0 and grid[r][c-1] == '1' and not visited[r][c-1]: 
                            q.append((r, c-1))
                            visited[r][c-1] = 1
                        if c + 1 < len(grid[0]) and grid[r][c+1] == '1' and not visited[r][c+1]: 
                            q.append((r, c+1))
                            visited[r][c+1] = 1
                    
                    
        return totalIslands
        """
        
        """
        - union find?
        """
        

print(Solution().numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]])
