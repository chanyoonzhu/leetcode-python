"""
- prefix sum
- O(mn), O(mn)
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sums = self._getPrefixSums(matrix)
        
    def _getPrefixSums(self, matrix):
        M, N = len(matrix), len(matrix[0])
        prefix_sums = [[0] * (N + 1) for _ in range(M + 1)]
        for r in range(1, M + 1):
            for c in range(1, N + 1):
                prefix_sums[r][c] = prefix_sums[r-1][c] + prefix_sums[r][c-1] - prefix_sums[r-1][c-1] + matrix[r-1][c-1]
        return prefix_sums
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sums[row2+1][col2+1] - self.prefix_sums[row1][col2+1] - self.prefix_sums[row2+1][col1] + self.prefix_sums[row1][col1]