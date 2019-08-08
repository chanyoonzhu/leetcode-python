class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        tl, br = (0,0), (len(matrix)-1,len(matrix[0])-1)
        return self.helper(matrix, tl, br, target)
        
    def helper(self, matrix, tl, br, target):
        if tl == br and matrix[tl[0]][tl[1]] == target:
            return True
        if matrix[tl[0]][tl[1]] > target or matrix[br[0]][br[1]] < target:
            return False
        br1 = (math.floor((tl[0]+br[0])/2), math.floor((tl[1]+br[1])/2))
        tl4 = (math.ceil((tl[0]+br[0])/2), math.ceil((tl[1]+br[1])/2))
        tl2, br2 = (tl[0], tl4[1]), (br1[0], br[1])
        tl3, br3 = (tl4[0], tl[1]), (br[0],br1[1])
        return (self.helper(matrix, tl, br1, target) or
                self.helper(matrix, tl2, br2, target) or
                self.helper(matrix, tl3, br3, target) or
                self.helper(matrix, tl4, br, target))
        
        
        """
        if not matrix: return False
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and 0 <= j:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1      
        return False
        """
        
        
        