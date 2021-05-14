"""
- greedy
- O(n), O(1)
- intuition: start from the dish with the largest satisfaction, insert if do not bring down overall value
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        result = _sum = 0
        for s in satisfaction:
            if _sum + s > 0:
                result += s + _sum
                _sum = _sum + s
            else:
                break # optimizes speed - no need to continue with dishes with even smaller satisfaction rate
        return result