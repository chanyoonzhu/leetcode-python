"""
- greedy
- O(n), O(1)
"""
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        average, mod = divmod(sum(machines), len(machines))
        if mod != 0:
            return -1
        
        res = 0
        accumulated_move = 0
        for count in machines:
            move = count - average
            accumulated_move += move
            res = max(res, abs(accumulated_move), move)
        return res