import collections
from collections import defaultdict


# chars in t can be the same! So can't store in set, has to use dic

"""
Questions to ask:
Q: Can t have duplicates? - very important question, easy to miss
A: Yes, in that case, the substring must have enough number of chars to cover the duplicates
Q: Are capital letters the same as lower letters?
A: No, case has to match

Pseudo code:
1. We start with two pointers, leftleft and rightright initially pointing to the first element of the string SS.
2. We use the rightright pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of TT.
3. Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.
4. If the window is not desirable any more, we repeat step \; 2step2 onwards.

Follow up question:
Q: Can it be optimized for when the length of s is far greater than the length of t?
A: Yes, filter s once with t to avoid traverse all elements of s twice (with left and right pointers)
"""
class Solution(object):
    """
    - sliding window: initial answer (wrong, did not cover cases where there're duplicates in t)
    """
    def minWindow_initial_answer(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        left = 0
        longest = float("inf")
        left_longest = right_longest = 0
        char_to_rightmost_pos = dict()
        for right in range(len(s)):
            char = s[right]
            if char in t:
                if char in char_to_rightmost_pos:
                    prev_pos = char_to_rightmost_pos[char]
                    del char_to_rightmost_pos[char]
                    left = min(char_to_rightmost_pos.values())
                char_to_rightmost_pos[char] = right
                if len(char_to_rightmost_pos.keys()) == len(t):
                    left = min(char_to_rightmost_pos.values())
                    if right - left + 1 < longest:
                        left_longest, right_longest = left, right
                        longest = right - left + 1
        return s[left_longest:right_longest+1] if longest != float("inf") else ""

    """
    - sliding window: correct answer
    - O(n+k), O(k)
    """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        longest = float("inf")
        left_longest = right_longest = 0
        char_counts = defaultdict(lambda: (0,0)) # (needed, current)
        for char in t:
            char_counts[char] = (char_counts[char][0] + 1, char_counts[char][1])
            
        
        for right in range(len(s)):
            char_right = s[right]
            if char_right in t:
                char_counts[char_right] = (char_counts[char_right][0], char_counts[char_right][1] + 1)
                if self.has_all_in_t(char_counts):
                    while left <= right:
                        char_left = s[left]
                        left += 1
                        if char_left in char_counts:
                            char_counts[char_left] = (char_counts[char_left][0], char_counts[char_left][1] - 1)
                            if char_counts[char_left][1] < char_counts[char_left][0]:
                                break
                    if right - left + 2 < longest:
                        longest = right - left + 2
                        left_longest, right_longest = left - 1, right
        return s[left_longest:right_longest+1] if longest != float("inf") else ""
    
    def has_all_in_t(self, char_counts):
        return all([expected <= actual for expected, actual in char_counts.values()])
    
    """
    - sliding window: performance improved - keep the count of matched chars in a variable
    - O(n+k), O(k)
    """
    def minWindow_performance_improved(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        left = 0
        longest = float("inf")
        left_longest = right_longest = 0
        char_needed = defaultdict(int)
        char_window = defaultdict(int)
        matched = 0
        for char in t:
            char_needed[char] += 1
            
        
        for right in range(len(s)): # move right pointer to the right until window satisfies condition
            char_right = s[right]
            if char_right in t:
                char_window[char_right] += 1
                if char_window[char_right] == char_needed[char_right]:
                    matched += 1
                while matched == len(char_needed) and left <= right: # move left pointer to the right until window not satisfy condition
                    char_left = s[left]
                    left += 1
                    if char_left in char_window:
                        char_window[char_left] -= 1
                        if char_window[char_left] < char_needed[char_left]:
                            matched -= 1
                    if right - left + 2 < longest:
                        longest = right - left + 2
                        left_longest, right_longest = left - 1, right
        return s[left_longest:right_longest+1] if longest != float("inf") else ""

    """
    - sliding window: performance improved when length of s far greater than t - filter s to avoid traverse all elements of s twice (right and left pointer)
    - O(n+k), O(k)
    """
    def minWindow_optimized_for_s_length_far_greater_than_t(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        left_ptr = 0
        longest = float("inf")
        left_longest = right_longest = 0
        char_needed = defaultdict(int)
        filtered_s = []
        char_window = defaultdict(int)
        matched = 0
        for char in t:
            char_needed[char] += 1
        for i, char in enumerate(s):
            if char in t:
                filtered_s.append((char, i))
        
        for right_ptr in range(len(filtered_s)):
            char_right, right = filtered_s[right_ptr]
            char_window[char_right] += 1
            if char_window[char_right] == char_needed[char_right]:
                matched += 1
            while matched == len(char_needed) and left_ptr <= right_ptr:
                char_left, left = filtered_s[left_ptr]
                left_ptr += 1
                if char_left in char_window:
                    char_window[char_left] -= 1
                    if char_window[char_left] < char_needed[char_left]:
                        matched -= 1
                if right - left + 1 < longest:
                    longest = right - left + 1
                    left_longest, right_longest = left, right
        return s[left_longest:right_longest+1] if longest != float("inf") else ""

sl = Solution()
print(sl.minWindow("ADOBECODEBANC", "ABC"))
print(sl.minWindow("aa", "aa"))

