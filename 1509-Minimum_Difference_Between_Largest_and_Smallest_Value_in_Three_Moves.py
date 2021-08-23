"""
- sliding window + quick sort
- greedily removes smallest or largest items of a total count of three
- O(nlogn), O(logn)
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)        
        if n <= 4:
            return 0
        nums.sort() # todo: no need to sort, only need the smallest/largest 4 numbers: O(n), O(1)
        result = float("inf")
        for i in range(4):
            result = min(result, nums[n - 1 - i] - nums[3 - i])
        # faster: return min(b - a for a, b in zip(nums[:4], nums[-4:]))
        return result
    