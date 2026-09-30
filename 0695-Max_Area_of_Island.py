class Solution:
    def maxAreaOfIsland(self, grid):
        
        """
        - depth-first search, mark visited in place
        - O(n), O(1)
        """
    
        def helper(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 'X':
                return 0
            if grid[x][y] == 1:
                grid[x][y] = 'X'
                return 1 + helper(x - 1, y) + helper(x + 1, y) + helper(x, y + 1) + helper(x, y - 1)
            else:
                grid[x][y] = 'X'
                return 0
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, helper(i, j)) 
        return max_area

        """
        - depth-first search, recursive, mark visited in a set
        - O(n), O(n)
        """
        
        visited = set() # can use global variable instead of passing into stack
        
        def helper(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in visited:
                return 0
            visited.add((x, y))
            if grid[x][y] == 1:
                return 1 + helper(x - 1, y) + helper(x + 1, y) + helper(x, y + 1) + helper(x, y - 1)
            else:
                return 0
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, helper(i, j)) 
        return max_area

        """
        - depth-first search, iterative, mark visited in a set
        - O(n), O(n)
        """
        max_area = 0
        visited = set()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                area = 0
                n = grid[i][j]
                stack = [(i, j)] # use stack to track all neighbors (all need to be searched) 
                while stack:
                    x, y = stack.pop()
                    if 0 <= x < row and 0 <= y < col and (x, y) not in visited:
                        visited.add((x, y))
                        if grid[x][y] == 1:
                            area += 1
                            stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                max_area = max(max_area, area)
        return max_area

s = Solution()
# print(s.maxAreaOfIsland([[1]]))
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
