"""
- key: the numbers left are actually base 9 number, so the question translates to "get the nth 9-base number"
- O(logn), O(1)
"""
class Solution:
    def newInteger(self, n: int) -> int:
        
        res = ''
        while n:
            div, mod = divmod(n, 9)
            res = str(mod) + res
            n = div
        return int(res)