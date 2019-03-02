class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        """
        - O(n), O(n)
        - calculate left distance and right distance separately

        size = len(seats)
        maxDist = 0
        
        left, right = [0] * size, [0] * size
        left[0] = right[size-1] = float('inf')
        leftPtr, rightPtr = 0, size-1
        
        for i in range(1, size):
            if seats[i] == 1:
                leftPtr = i
            left[i] = i - leftPtr
        
        for i in range(size-2, -1, -1):
            if seats[i] == 1:
                rightPtr = i
            right[i] = rightPtr - i
        
        for i in range(0, size):
            maxDist = max(maxDist, min(left[i], right[i]))
        
        return maxDist
        """

        """
        - O(n), O(1)
        - group zeros
        """
        
        
        maxZeros = 0
        
        i = 0
        while i < len(seats):
            end = False
            currZeros = 0
            if seats[i] != 1:
                while i < len(seats) and seats[i] != 1:
                    if i == 0 or i == len(seats)-1:
                        end = True
                    currZeros += 1
                    i += 1
                if end:
                    currZeros *= 2
                maxZeros = max(maxZeros, currZeros)
            else:
                i += 1
                
        return (maxZeros + 1) // 2