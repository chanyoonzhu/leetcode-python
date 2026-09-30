"""
- 2D Array
- O(mn), O(mn)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        u, d, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        direction = 0
        
        res = []
        while l <= r and u <= d:
            if direction == 0: # to right:
                for j in range(l, r + 1):
                    res.append(matrix[u][j])
                u += 1
            elif direction == 1:
                for i in range(u, d + 1): # to down
                    res.append(matrix[i][r])
                r -= 1
            elif direction == 2: # to left:
                for j in range(r, l-1, -1):
                    res.append(matrix[d][j])
                d -= 1
            elif direction == 3: # to up
                for i in range(d, u-1, -1):
                    res.append(matrix[i][l])
                l += 1
            direction = (direction + 1) % 4
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sl = Solution()
print(sl.spiralOrder(matrix))
