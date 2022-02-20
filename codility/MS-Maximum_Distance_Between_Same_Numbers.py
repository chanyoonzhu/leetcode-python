"""
计算一个list中两个相等的数字的最大index之差
"""
from re import L


class Solution:
    def getDist(self, nums: list) -> int:
        num_to_first_idx = {}
        res = 0
        for i, x in enumerate(nums):
            if x in num_to_first_idx:
                res = max(res, i - num_to_first_idx[x])
            else:
                num_to_first_idx[x] = i
        return res

s = Solution()
print(s.getDist([]))
print(s.getDist([1,1]))
print(s.getDist([1, 2, 1]))
print(s.getDist([1]))
print(s.getDist([1, 2, 1, 3, 4, 5, 2]))
print(s.getDist([1, 2, 1, 3, 4, 5, 6, 1]))