"""
- similar: 53-Maximum Subarray
"""
"""
- greedy
- O(n), O(1)
"""
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        prev_square = prev_no_square = 0
        result = 0
        
        for num in nums:
            no_square = max(num, prev_no_square + num)
            square = max(num * num, num * num + prev_no_square, num + prev_square)
            result = max(result, square)
            prev_square, prev_no_square = square, no_square
        return result

"""
- todo: dynamic programming
"""