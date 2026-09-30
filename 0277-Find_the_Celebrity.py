"""
- Math Logic
- O(n), O(1)
- knows(i,j) = 1 - # i can't be a celebrity, change i to j 
  knows(i,j) = 0 - # j can't be a celebrity, increase j 
"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i
        for i in range(n):
            if i != celebrity_candidate and (knows(celebrity_candidate, i) or not knows(i, celebrity_candidate)):
                return -1
        return celebrity_candidate