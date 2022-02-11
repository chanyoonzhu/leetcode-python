"""
- Array
- O(n), O(1)
"""
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = res = 0 # cur - cur max (with decrements considered)
        for value in values:
            res = max(res, cur + value)
            cur = max(cur, value) - 1
        return res