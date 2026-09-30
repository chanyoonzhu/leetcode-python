"""
- backtracking
- O(k) - number of valid permutations
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        return self.backtracking(set([i for i in range(1, n + 1)]), n)
        
    def backtracking(self, remain, n):
        if not remain:
            return 1
        idx = n - len(remain) + 1
        arrangement_count = 0
        for x in remain:
            if x % idx == 0 or idx % x == 0:
                arrangement_count += self.backtracking(remain - set([x]), n)
        return arrangement_count

"""
- backtracking (with bitmasking)
- O(k) - number of valid permutations
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        
        @lru_cache(None)
        def backtracking(bitmask, i):
            if i == 0:
                return 1
            count = 0
            for k in range(n):
                if bitmask & (1 << k) and (i % (k + 1) == 0 or (k + 1) % i  == 0): # check availability of number k: bitmask & (1 << k)
                    count += backtracking(bitmask ^ (1 << k), i - 1) # turn off availability of number k: bitmask ^ (1 << k)
            return count
        
        bitmask = 2 ** (n) - 1 # all 111...11 (all available)
        return backtracking(bitmask, n)