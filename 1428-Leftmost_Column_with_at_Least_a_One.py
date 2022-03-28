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
- Greedy: Start at bottom right, Move only left and up
- O(m + n), O(1)
"""
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1]
        r, c = M - 1, N - 1
        res = N
        while r >= 0:
            while c >= 0 and binaryMatrix.get(r, c) == 1: # greedily check the first one in this column
                c -= 1
                res = min(res, c)
            r -= 1 # move up
        return res + 1 if res < N else -1
        
        
        