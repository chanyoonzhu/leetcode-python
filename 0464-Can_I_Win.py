"""
- dynamic programming (top-down)
"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        pool = [x for x in range(1, maxChoosableInteger + 1)]
        mem = {} # only need to serialize the pool of integers since the remaining total can be derived from it
        
        if sum(pool) < desiredTotal:
            return False
        
        def helper(pool, remain):
            if len(pool) == 0:
                return False
            state = tuple(pool)
            if state not in mem:
                mem[state] = False
                if remain - pool[-1] <= 0: # greedily test the largest number
                    mem[state] = True
                else:
                    for x in pool:
                        new_pool = [y for y in pool if x != y]
                        if not helper(new_pool, remain - x): # there exist an x that make the opponent lose
                            mem[state] = True
                            break
            return mem[state]
        
        return helper(pool, desiredTotal)
        
"""
- todo: bitmask
"""
class Solution:
    
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        bit = 2 ** maxChoosableInteger - 1
        
        @lru_cache(None)
        def dp(bitmask, total):
            for pick in range(maxChoosableInteger, 0, -1):
                if bitmask & (1 << (pick - 1)): # picked number still available
                    if pick >= total or not dp(bitmask ^ (1 << (pick - 1)), total - pick):
                        return True
            return False

        # easy to miss: if all number added is still smaller
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False   
        
        return dp(bit, desiredTotal)