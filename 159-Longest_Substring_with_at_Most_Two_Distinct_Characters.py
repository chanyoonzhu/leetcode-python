"""
- Brute force
- O(n^2), O(n^2)
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        result = 0
        n = len(s)
        
        for l in range(n):
            chars = set()
            for r in range(l, n):
                chars.add(s[r])
                if len(chars) > 2:
                    break
                result = max(result, r - l + 1)
        return result
    
"""
- Sliding window
- O(n), O(n)
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = collections.defaultdict(int)
        result = 0
        l = 0
        for r, c in enumerate(s):
            counter[c] += 1
            while len(counter) > 2:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            result = max(result, r - l + 1)
        return result
        

sl = Solution()
print(sl.lengthOfLongestSubstringTwoDistinct("bacc"))