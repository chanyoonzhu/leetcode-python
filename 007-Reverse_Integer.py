"""
- Math division
- O(logX), O(logX)
"""
class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            is_neg = True
            x = -x
        converted = 0
        while x:
            div, mod = divmod(x, 10)
            converted = converted * 10 + mod
            x = div
        if converted > 2 ** 31 - 1:
            return 0
        return converted if not is_neg else -converted