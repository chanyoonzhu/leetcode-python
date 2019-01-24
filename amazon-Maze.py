# class Solution:

def maze(grid):

    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    i = j = 0
    visited = [[0] * len(row) for row in grid]

    def dfs(x, y):
        
        if (x < 0 or x >= len(grid) or 
            y < 0 or y >= len(grid[0]) 
            or visited[x][y]):
            return 0
        else:
            visited[x][y] = 1
            if grid[x][y] == 1:
                return 0
            elif grid[x][y] == 9:
                return 1
            else:
                return dfs(x-1, y) or dfs(x+1, y) or dfs(x, y+1) or dfs(x, y-1)
    
    return dfs(i, j)

def mazeDistance(grid, i, j):

    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return -1

    minDistance = float('inf')
    visited = [[0] * len(row) for row in grid]
    
    def expand(prev, x, y):
        start = prev[0]
        distance = prev[1]
        next = [start[0] + x, start[1] + y]
        if (next[0] >= 0 and next[0] < len(grid) 
            and next[1] >= 0 and next[1] < len(grid) 
            and grid[next[0]][next[1]] != 1 
            and not visited[next[0]][next[1]]) :
            visited[next[0]][next[1]] = 1
            q.append([next, distance + 1])
           
    q = [([i,j], 0)]
    while q:
        point = q[0]
        currStart = point[0]
        steps = point[1]
        
        if grid[currStart[0]][currStart[1]] == 9:
            minDistance = steps
            break

        expand(point, 1, 0)
        expand(point, -1, 0)
        expand(point, 0, 1)
        expand(point, 0, -1)

        del q[0]

    if minDistance != float('inf'):
        return minDistance
    else:
        return -1
    

# solution = new Solution()
grid = [[0,1,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,1,1,1],[0,0,0,0,9]]
grid2 = [[],[],[],[],[]]
grid3 = []
grid4 = None
grid5 = [[0,0,0,1],[0,1,1,1],[0,1,0,1],[0,0,0,9]]
# print(maze(grid))
print(mazeDistance(grid, 0, 0))
            
            
            
                        
        