"""
- union find
"""
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        
        parents = [i for i in range(n + 1)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parents[px] = py
        
        sieve = [1] * (n + 1) # mark number that already unioned using "sieve of eratosthenes"
        
        for x in range(threshold + 1, n // 2 + 1):
            if sieve[x]:
                for y in range(2 * x, n + 1, x):
                    sieve[y] = 0
                    union(x, y)
        
        result = []
        for x, y in queries:
            result.append(find(x) == find(y))
        return result