"""
- Hashmap + prefix sum
- O(n), O(1)
"""
class Solution:
    def numSplits(self, s: str) -> int:
        result = 0
        counter_right = collections.Counter(s)
        counter_left = collections.Counter()
        for c in s:
            counter_left[c] += 1
            counter_right[c] -= 1
            if not counter_right[c]: del counter_right[c]
            if len(counter_left) == len(counter_right):
                result += 1
        return result