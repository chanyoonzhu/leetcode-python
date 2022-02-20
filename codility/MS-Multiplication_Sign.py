"""
计算一个list里所有数字相乘之后的符号是什么，1/-1/0.
"""

class Solution:
    def getSign(self, nums: list) -> int:
        is_positive = True
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                is_positive = not is_positive
        return 1 if is_positive else -1

s = Solution()
print(s.getSign([1, 2, 3]))
print(s.getSign([-1, 2, 3]))
print(s.getSign([-1, -1, 2]))
print(s.getSign([-1, -1, 0, 2]))
print(s.getSign([-1, -1, -1, 2]))
