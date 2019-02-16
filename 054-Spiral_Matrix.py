class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        res = []
        currDic = 0
        n, s, w, e = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while n <= s and w <= e:
            # four directions
            if currDic == 0:
                for j in range(w, e + 1):
                    res.append(matrix[n][j])
                n += 1
            elif currDic == 1:
                for i in range(n, s + 1):
                    res.append(matrix[i][e])
                e -= 1
            elif currDic == 2:
                for j in range(e, w-1, -1):
                    res.append(matrix[s][j])
                s -= 1
            elif currDic == 3:
                for i in range(s, n-1, -1):
                    res.append(matrix[i][w])
                w += 1 
            currDic = (currDic + 1) % 4
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sl = Solution()
print(sl.spiralOrder(matrix))
