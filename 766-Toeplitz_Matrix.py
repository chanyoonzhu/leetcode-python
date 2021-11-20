"""
- 2D array
"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        for r in range(M):
            for c in range(N):
                if r > 0 and c > 0:
                    if matrix[r][c] != matrix[r-1][c-1]: # compare with the upper-left element
                        return False
        return True