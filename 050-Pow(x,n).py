"""
- Math - my solution
- O（logn), O(n)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {0: 1}
        res = 1
        if n < 0:
            n = -n
            x = 1.0 / x
        while n:
            degree = 1
            while n >= degree:
                if degree not in memo:
                    memo[degree] = x * memo[degree-1]
                res *= memo[degree]
                n -= degree
                degree += 1
        return res