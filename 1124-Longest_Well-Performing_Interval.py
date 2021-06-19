"""
- prefix sum + hashmap
- O(n), O(n)
"""
class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        result = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                result = i + 1
            elif score - 1 in seen: # intuition: sum(hours[seen[score - 1]: i + 1]) = 1
                result = max(result, i - seen[score - 1])
            if score not in seen: # only store first occurrence to get the smallest index for a score
                seen[score] = i
        return result

"""
- monotonically increasing/decreasing stack
- todo
"""