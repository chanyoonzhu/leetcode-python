"""
- union find
"""
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        
        M = max(nums)
        parents = [n for n in range(M + 1)]
        
        def find(n):
            if parents[n] != n:
                parents[n] = find(parents[n])
            return parents[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                parents[p1] = p2
        
        all_nums = set(nums)
        sieve = [1] * (M + 1) # sieve[i] == 1 if i is a prime
        sieve[0] = sieve[1] = 0
        for n in range(M // 2 + 1):
            if sieve[n] == 1: # if n is prime
                for m in range(2 * n, M + 1, n): # m can divide n, so not a prime
                    sieve[m] = 0
                    if m in all_nums: union(m, n)
        
        return all([find(n) == find(m) for n, m in zip(nums, sorted(nums))]) # can be sorted if original number in each pos can swap with sorted number in that pos (in the same unioned group)