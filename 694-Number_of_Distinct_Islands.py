class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        """
        - O(mn), -O(mn)
        - store each of the island's positions (relative to its start position) in sets
        - count length of sets
        """
        islands = []
        
        def destroy(grid, i, j, islandMap):
            if len(islandMap) == 0:
                islandMap.append((i, j))
            else:
                islandMap.append((i-islandMap[0][0], j-islandMap[0][1])) # record relative position to start point
            grid[i][j] = 0
            if i-1 >= 0 and grid[i-1][j] == 1:
                destroy(grid, i-1, j, islandMap)
            if i+1 < len(grid) and grid[i+1][j] == 1:
                destroy(grid, i+1, j, islandMap)
            if j-1 >= 0 and grid[i][j-1] == 1:
                destroy(grid, i, j-1, islandMap)
            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                destroy(grid, i, j+1, islandMap)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandMap = []
                    destroy(grid, i, j, islandMap)
                    islands.append(islandMap)
                    
        distinctIslands = set([tuple(i[1:]) for i in islands]) # i[1:] for removing the start pos
        return len(distinctIslands)
        
        
        