"""
- greedy + hashmap
- key: greedily add shortest subarray (with sum equal to target) to result
- O(n), O(n)
"""
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix = {0: -1}
        sum_ = 0
        result = 0
        left = -1 
        for i, x in enumerate(nums):
            sum_ += x
            if sum_ - target in prefix:
                if prefix[sum_ - target] >= left: # easy to miss: check left boundary
                    result += 1
                    left = i
                del prefix[sum_ - target]    
            prefix[sum_] = i
        return result