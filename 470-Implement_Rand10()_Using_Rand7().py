# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

"""
- intuition: get a random number 0-39, then % 10 + 1
- O(1), O(1)
"""
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = 40
        while result >= 40: 
            result = 7 * (rand7() - 1) + (rand7() - 1) #  get a random number 0 - 48
        return result % 10 + 1