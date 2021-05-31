"""
- similar: 1371
"""
class Solution:
    def longestAwesome(self, s: str) -> int:
        memo = dict({0: -1})
        state = 0
        result = 0
        for i, c in enumerate(s):
            state ^= 1 << ord(c) - ord('0')
            if state not in memo:
                memo[state] = i
            else:
                result = max(result, i - memo[state]) # all even
            for j in range(10):
                temp_state = state ^ (1 << j)  # only one is odd (only one bit flipped)
                if temp_state in memo:
                    result = max(result, i - memo[temp_state]) 
        return result