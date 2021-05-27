"""
- greedy
- O(n), O(1)
- intuition: 
    if current accumulative product is positive, the start of subarray should be the first non-zero element
    if current accumulative product is negative, the start of subarray should be the one after the first negative element
    reset when 0 is seen
"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        POS, NEG = 1, -1
        first_after_neg = first_non_zero = 0
        result = 0
        prev = POS
        for i, num in enumerate(nums):
            if num == 0:
                first_non_zero = i + 1
                first_after_neg = 0
                prev = POS
                continue
            if num < 0:
                if not first_after_neg:
                    first_after_neg = i + 1
            prev = POS if prev * num > 0 else NEG
            if prev == POS:
                result = max(result, i - first_non_zero + 1)
            else:
                result = max(result, i - first_after_neg + 1)
                
        return result