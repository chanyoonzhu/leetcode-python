"""
- binary search
- O(log(mn), O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        def getRowCol(i):
            return divmod(i, N) 
        
        l, r = 0, M * N - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = getRowCol(mid)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        