"""
- intuition: At each digit, if there is a larger digit that occurs later, we want the swap it with the largest such digit that occurs the latest.
- O(n), O(n)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))
        n_to_idx = {x: i for i, x in enumerate(digits)} # idx of last n
        for i, x in enumerate(digits):
            for d in range(9, x, -1): # find the largest
                if n_to_idx.get(d, -1) > i: # need to come after x
                    digits[i], digits[n_to_idx[d]] = digits[n_to_idx[d]], digits[i]
                    return int("".join(map(str, digits)))
        return num