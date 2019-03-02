class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
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