# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        - O(n^2), O(1)
        - time limit exceeded
        - brute force
        
        celebrity = -1
        
        for i in range(n):
            dontKnowOthers = True
            for j in range(n):
                if knows(i, j) and i != j:
                    dontKnowOthers = False
            if dontKnowOthers:
                allOthersKnow = True
                for k in range(n):
                    if not knows(k, i):
                        allOthersKnow = False
                if allOthersKnow:
                    celebrity = i
                
        
        return celebrity
        """
        
        """
        - O(n^2), O(2n)
        - row and col flags (slight improve)
        - exceed time limit
        
        celebrity = -1
        
        row = [1] * n # change to 0 if i knows someone
        col = [0] * n # change to 1 if someone doesn't know i
        
        for i in range(n):
            for j in range(n):
                if i != j and knows(i, j):
                    row[i] = 0
                if i != j and not knows(i, j):
                    col[j] = 1
        
        for i in range(n):
            if row[i] and not col[i]:
                celebrity = i
                
        return celebrity
        """
        
        """
        - O(n), O(1)
        - knows(i,j) = 1 - # i can't be a celebrity, change i to j 
            knows(i,j) = 0 - # j can't be a celebrity, increase j 
        """
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        
        for i in range(n):
            if (knows(celebrity, i) and celebrity != i) or not knows(i, celebrity):
                celebrity = -1
                break
                
        return celebrity