"""
- math: add (iterative)
- O(n), O(n)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        a, b = list(a), list(b)
        while a or b or carry:
            if a:
                carry += (1 if a.pop() == "1" else 0)
            if b:
                carry += (1 if b.pop() == "1" else 0)
            res.insert(0, str(carry % 2))
            carry = carry // 2
        return ''.join(res)