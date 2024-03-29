"""
- https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b:
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry
        
        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        return a