class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        """
        - O(2^n)
        - O(n)
        - only 2^n states possible, find how many iterations reach the same state to avoid executing duplicate steps
        """
        def copy(arrA, arrB, l):
            for i in range(l):
                arrA[i] = arrB[i]
        
        prevState = cells[:]
        temp = [0] * len(cells)
        seen = {}
        
        while N > 0:
            if tuple(prevState) in seen:
                N %= seen[tuple(prevState)] - N
            seen[tuple(prevState)] = N
            
            if N > 0:
                for i in range(1, len(cells)-1):
                    if prevState[i-1] == prevState[i+1]:
                        temp[i] = 1
                    else:
                        temp[i] = 0
                N -= 1
                
            copy(prevState, temp, 8)
        return temp
            
            
sl = Solution()
print(sl.prisonAfterNDays([0, 0, 1, 1, 0, 0, 1, 1], 4))
            
                