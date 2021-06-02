"""
- binary search + greedy
- O(log(maxSum)), O(1)
- intuition for greedy: from index, let the next numbers decrease by one to created min sum, use Gauss sum formula to calculate the sum
"""
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low, high = 0, maxSum
        self.r_count = n - index - 1
        self.l_count = index
        
        def can_construct(x):
            total = x
            # caveat: all nums have to be positive
            r_1_counts = max(self.r_count - x + 1, 0) # number of repetitive ones on the right
            l_1_counts = max(self.l_count - x + 1, 0) # number of repetitive ones on the left
            total += (max(x - self.r_count, 1) + x - 1) * (self.r_count - r_1_counts) // 2 + r_1_counts # Gauss sums
            total += (max(x - self.l_count, 1) + x - 1) * (self.l_count - l_1_counts) // 2 + l_1_counts
            return total <= maxSum
            
        while low < high:
            mid = low + (high - low + 1) // 2
            if can_construct(mid):
                low = mid
            else:
                high = mid - 1
        return low