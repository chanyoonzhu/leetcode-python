class NumMatrix:

    """
    - Fenwick tree (binary index tree)
    - create: O(mn), O(mn); update: O(logm * logn), O(1), rangeRegion: O(logm * logn), O(1)
    - similar question: 307 (1D version) 
    """

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.sums = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
        
    def update(self, row: int, col: int, val: int) -> None:
        diff, self.matrix[row][col] = val - self.matrix[row][col], val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.sums[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumCorner(row2, col2) - self.sumCorner(row2, col1 - 1) - self.sumCorner(row1 - 1, col2) + self.sumCorner(row1 - 1, col1 - 1)
        
    def sumCorner(self, row, col):
        res, i = 0, row + 1
        while i:
            j = col + 1
            while j:
                res += self.sums[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)