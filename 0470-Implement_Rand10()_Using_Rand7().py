# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

"""
- intuition: rand7() -> rand(49) - 1 -> rand(40), then rand(40) % 10 + 1
- O(1), O(1)
- https://leetcode.com/problems/implement-rand10-using-rand7/discuss/150301/Three-line-Java-solution-the-idea-can-be-generalized-to-%22Implement-RandM()-Using-RandN()%22
"""
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = 40
        while result >= 40: 
            result = 7 * (rand7() - 1) + (rand7() - 1) #  get a uniform random number 0 - 48, note: rand7() * rand7() is not uniform 
        return result % 10 + 1