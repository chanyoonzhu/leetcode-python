"""
- array
- O(n), O(1)
"""
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        is_neg = False
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                is_neg = not is_neg
        return -1 if is_neg else 1