class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        """
        - O(mn), O(mn)
        - straight-forward solution
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        
        zeros = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
                    
        for zero in zeros:
            matrix[zero[0]] = [0] * len(matrix[0])
            for i in range(len(matrix)):
                matrix[i][zero[1]] = 0
        """
                
        """
        - O(mn), O(m+n)
        - use set to store row and column
        
        row, col = set(), set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0
        """
        
        
                    
        """
        O(mn) O(1)
        - use 1st row and 1st col as flag marking if that row/col should be set to 0
        - use matrix[0][0] to mark if first row should be all set to 0
        - use an additional space to mark if first col should be all set to 0
        """
        
        firstColZero = False
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstColZero = True

        if 0 in matrix[0]:
            matrix[0][0] = 0
                
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
            
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if firstColZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
            
        
sl = Solution()
matrix = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
sl.setZeroes(matrix)
print(matrix)
                
        
                