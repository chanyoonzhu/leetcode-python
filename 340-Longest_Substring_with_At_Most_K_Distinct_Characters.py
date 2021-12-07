"""
- sliding window
- O(n), O(k)
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
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

"""
- sliding window
- O(n), O(k)
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        distinct_count = 0
        l = 0
        res = 0
        for r, c in enumerate(s):
            if counter[c] == 0:
                distinct_count += 1
            counter[c] += 1
            while l < len(s) and distinct_count > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    distinct_count -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
        