"""
- sliding window
- O(maxUnique*n), O(maxUnique)
- intuition: fix the number of unique chars, and solve like 159.
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def longestSubstringWithMUnique(s, k, unique_num_target):
            l = unique_num = num_no_less_than_k = max_len = 0
            counter = collections.Counter()
            for r, c in enumerate(s):
                if counter[c] == 0:
                    unique_num += 1
                counter[c] += 1
                if counter[c] == k:
                    num_no_less_than_k += 1
                
                while unique_num > unique_num_target:
                    if counter[s[l]] == k:
                        num_no_less_than_k -= 1
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        unique_num -= 1
                        
                    l += 1
                # now s[l:r+1] contains targeted unique chars

                if unique_num == num_no_less_than_k: max_len = max(max_len, r - l + 1)
            return max_len

        result = 0
        for i in range(1, len(collections.Counter(s)) + 1):
            result = max(result, longestSubstringWithMUnique(s, k, i))
        return result

"""
- todo: divide and conquer
"""
    