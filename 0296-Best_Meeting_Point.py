"""
- Math: start thinking from 1D, the target that has minimal dist is the median of all target
- O(mn), O(mn)
"""
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        homes_x = []
        homes_y = []
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    homes_x.append(i)
                    homes_y.append(j)
                    
        homes_x.sort()
        homes_y.sort()
        
        homes_count = len(homes_x)
        median_x = homes_x[homes_count//2]
        median_y = homes_y[homes_count//2]
        
        result = 0
        for x in homes_x:
            result += abs(x - median_x)
        for y in homes_y:
            result += abs(y - median_y)
        return result