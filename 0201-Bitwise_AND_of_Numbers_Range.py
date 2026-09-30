"""
- bitwise and
- TLE
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        sum_ = left
        for x in range(left + 1, right + 1):
            sum_ &= x
        return sum_

"""
- bit shift
- intuition: as long as there is one bit of zero value, then the result of AND operation on this series of bits would be zero.
    after the AND operation on all the numbers, the remaining part of bit strings is the common "1" prefix of all these bit strings
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right: 
            # getting rid of lower bits, getting closer to common prefix
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
        