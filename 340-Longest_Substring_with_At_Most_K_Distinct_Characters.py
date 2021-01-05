"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""


"""
Questions to ask:
Q: length of s, length of k
A: 1 <= s.length <= 5 * 104; 0 <= k <= 50
Q: special chars: paces and tabs and \n
A: handled as normal chars
"""
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        - sliding window - initial solution
        - O(n), O(k)
        """
        left, longest = 0, 0
        char_to_rightmost_idx = dict()
        for right in range(len(s)):
            char_to_rightmost_idx[s[right]] = right
            if len(char_to_rightmost_idx.keys()) > k:
                char_leftmost, char_leftmost_pos = sorted(char_to_rightmost_idx.items(), key = lambda x: x[1])[0]
                del char_to_rightmost_idx[char_leftmost]
                left = char_leftmost_pos + 1
            longest = max(longest, right - left + 1)
        return longest

        """
        - sliding window - simpler solution, use min() instead of sorted()
        - O(n), O(k)
        """
        def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, longest = 0, 0
        char_to_rightmost_idx = dict()
        for right in range(len(s)):
            char_to_rightmost_idx[s[right]] = right
            if len(char_to_rightmost_idx.keys()) > k:
                char_leftmost_pos = min(char_to_rightmost_idx.values())
                del char_to_rightmost_idx[s[char_leftmost_pos]]
                left = char_leftmost_pos + 1
            longest = max(longest, right - left + 1)
        return longest
            
        