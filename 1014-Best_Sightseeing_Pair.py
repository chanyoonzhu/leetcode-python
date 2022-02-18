"""
- Array
- O(n), O(1)
- similar: 121-Best Time to Buy and Sell Stock (+ dist penalty); 1937-Maximum Number of Points with Cost
"""
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        value_i_with_dist_penalty = res = 0 # value_i_with_dist_penalty - max value[k] + i - j of (k from 0...i)
        for value in values:
            res = max(res, value + value_i_with_dist_penalty)
            value_i_with_dist_penalty = max(value_i_with_dist_penalty, value) - 1 # each move add dist penalty 1
        return res