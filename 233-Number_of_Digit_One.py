"""
- math
- consider number of 1 at one's, ten's, ... position respectively, then sum up
- https://leetcode.com/problems/number-of-digit-one/discuss/64382/JavaPython-one-pass-solution-easy-to-understand
"""
class Solution:
    def countDigitOne(self, n):
        """
        if n = xyzdabc， and we are considering the occurrence of one on thousand's position, it should be:
        (1) xyz * 1000                     if d == 0
        (2) xyz * 1000 + abc + 1           if d == 1
        (3) xyz * 1000 + 1000              if d > 1
        """
        if n <= 0:
            return 0
        q, x, ans = n, 1, 0
        while q > 0:
            digit = q % 10
            q //= 10
            q_times_x = q * x
            if digit == 0:
                ans += q_times_x
            elif digit == 1:
                ans += q_times_x + n % x + 1
            elif digit > 1:
                ans += q_times_x + x
            x *= 10
        return ans