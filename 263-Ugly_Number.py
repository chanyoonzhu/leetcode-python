"""
- 
- O(logN), O(1)
- TLE
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: # easy to miss: has to be positive integer
            return False
        for p in 2, 3, 5:
            while n % p == 0:
                n /= p
        return n == 1