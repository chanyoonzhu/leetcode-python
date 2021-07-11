"""
- sliding window
- O(n), O(k)
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        l = 0
        result = 0
        for r, c in enumerate(s):
            counter[c] += 1
            while len(counter) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            result = max(result, r - l + 1)
        return result
            
        