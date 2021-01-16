# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """


"""
- Clarification questions:
Q: What should be returned if there's not a single 1?
A: return -1
"""
class Solution(object):
    """
    - Binary search
    - O(mlogn), O(1)
    """
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        leftmost = float("inf")
        for i in range(m):
            leftmost = min(leftmost, self.find_one_first_index(binaryMatrix, i, 0, n-1))
        return leftmost if leftmost < n else -1
    
    def find_one_first_index(self, matrix, row, left, right):
        if left == right:
            return right + 1 if matrix.get(row, right) == 0 else right # "else" handles row has no 0 situation
        mid = (left + right + 1) // 2
        if matrix.get(row, mid) == 1:
            return self.find_one_first_index(matrix, row, left, mid-1)
        else:
            return self.find_one_first_index(matrix, row, mid, right)

    """
    - Greedy: Start at Top Right, Move Only Left and Down
    - O(m + n), O(1)
    """
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        i, j = 0, n - 1
        while True:
            if j < 0 or i >= m:
                return j + 1 if j < n - 1 else -1
            while j >= 0 and binaryMatrix.get(i, j) == 1:
                j -= 1
            while j >= 0 and i < m and binaryMatrix.get(i, j) == 0:
                i += 1
        
        
        