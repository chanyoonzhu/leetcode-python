"""
- counter
- O(n), O(1)
"""
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        result = 0
        cur_count = [0] * 5 # marks where each currently active frogs are at. 
        mapping = {
            'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4
        }
        for char in croakOfFrogs:
            if char not in mapping: return -1
            prev_char_idx = mapping[char] - 1
            if cur_count[prev_char_idx]:
                cur_count[prev_char_idx] -= 1 # greedily moves current active frog forward (instead adding a new frog)
            elif prev_char_idx != -1: # invalid string
                return -1
            cur_count[mapping[char]] += 1
            if char == 'k':
                result = max(result, sum(cur_count))
                cur_count[mapping[char]] -= 1
        return result if not sum(cur_count) else -1