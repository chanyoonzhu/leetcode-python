from collections import defaultdict

class Solution(object):
    """
    - sliding window: initial solution
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_to_index = defaultdict(list)
        left = right = 0
        longest = 0
        chars = set()
        while right < len(s):
            while right < len(s):
                char = s[right]
                char_to_index[char].append(right)
                if char in chars:
                    longest = max(longest, len(chars))
                    dup_prev_pos = char_to_index[char][-2]
                    for i in range(left, dup_prev_pos):
                        chars.remove(s[i])
                    left = dup_prev_pos + 1
                    break
                else:
                    chars.add(char)
                right += 1
            right += 1
            longest = max(longest, len(chars))
            
        return longest