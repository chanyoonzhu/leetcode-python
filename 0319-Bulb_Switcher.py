"""
- Math logic
- intuition: light bulbs that are left on are switched odd number of times. Divisors come in pairs 12 = 2 * 6 = 3 * 4, only exception is when n is a square number like 16 = 4 * 4 (one single divisor).
    So only square numbers will be on at the end. Find all square numbers equal to or less than n.
- O(1), O(1)
"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))