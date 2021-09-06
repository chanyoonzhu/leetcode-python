"""
- 2D array
- O(mn), O(n) 
"""
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        result = []
        for j in range(N):
            can_end = True
            cur_j = j
            for i in range(M):
                j_pair = cur_j - 1 if grid[i][cur_j] == -1 else cur_j + 1
                if j_pair < 0 or j_pair == N or grid[i][j_pair] != grid[i][cur_j]: # a wall or a "V" is found
                    can_end = False
                    break
                cur_j = j_pair
            result.append(cur_j if can_end else -1)
        return result