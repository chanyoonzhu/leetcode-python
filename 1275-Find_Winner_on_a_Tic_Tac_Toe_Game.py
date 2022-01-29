"""
- Array 2D
- O(moves), O(1)
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * 3, [0] * 3
        diags = [0] * 2 
        
        weight = 1 # 1 for player 1, -1 for player 2
        for x, y in moves:
            rows[x] += weight
            cols[y] += weight
            if x == y:
                diags[0] += weight
            if x + y == n - 1:
                diags[1] += weight
            if any(abs(sum_) == n for sum_ in (rows[x], cols[y], diags[0], diags[1])): # check if reaches 3 or -3
                return "A" if weight == 1 else "B"
            weight *= -1
            
        return "Draw" if len(moves) == n ** 2 else "Pending"