"""
- array
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        while n > 1:
            res.append(n)
            res.append(-n)
            n -= 2
        if n:
            res.append(0)
        return res

"""
- more concise version
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1 - n, n, 2)