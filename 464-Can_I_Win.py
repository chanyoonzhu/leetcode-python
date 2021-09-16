"""
- dynamic programming (top-down)
"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        pool = [x for x in range(1, maxChoosableInteger + 1)]
        mem = {}
        
        if sum(pool) < desiredTotal:
            return False
        
        def helper(pool, remain):
            if len(pool) == 0:
                return False
            state = tuple(pool)
            if state not in mem:
                mem[state] = False
                if remain - pool[-1] <= 0:
                    mem[state] = True
                else:
                    for x in pool:
                        new_pool = [y for y in pool if x != y]
                        if not helper(new_pool, remain - x): # there exist an x that make the opponent lose
                            mem[state] = True
                            break
            return mem[state]
        
        return helper(pool, desiredTotal)