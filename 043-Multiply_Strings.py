"""
- Math
- O(mn), O(1)
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i in range(len(num2) - 1, -1, -1):
            n2 = ord(num2[i]) - ord("0")
            res += self.multiply_single(num1, n2, len(num2) - 1 - i)
        return str(res)
        
    def multiply_single(self, num: str, n: int, shift: int) -> int:
        carry, digit, pos = 0, 0, 0
        res = 0
        for i in range(len(num) - 1, -1, -1):
            cur = (ord(num[i]) - ord("0")) * n + carry
            carry, digit = divmod(cur, 10)
            res = res + digit * (10 ** pos)
            pos += 1
        res = res + carry * (10 ** pos)
        return res * (10 ** shift)