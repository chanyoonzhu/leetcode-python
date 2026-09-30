"""
- similar problem: 198-house robber
"""
"""
- dynamic programming (bottom-up)
- intuition: [2,2,3,3,3,4] transformed to house robber problem is [0, 0, 2, 3, 1], which is its Counter
- O(max(n, max-min))
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counters = collections.Counter(nums)
        minimum, maximum = min(nums), max(nums)

        prev = 0
        curr = 0
        for i in range(minimum, maximum + 1):
            prev, curr = curr, max(prev + counters[i] * i, curr)
        return curr