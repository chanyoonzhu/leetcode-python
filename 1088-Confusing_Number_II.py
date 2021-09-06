"""
- backtracking
"""
class Solution:
    def confusingNumberII(self, n: int) -> int:
        inverts = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        result = 0
        
        def backtrack(x, rotation, digits):
            nonlocal result
            if x != rotation: 
                result += 1
            for k in inverts.keys():
                next_x = x * 10 + k
                if 0 < next_x <= n: # easy to miss: > 0
                    backtrack(next_x, inverts[k] * 10 ** digits + rotation, digits + 1)
        
        backtrack(0, 0, 0)
        
        return result