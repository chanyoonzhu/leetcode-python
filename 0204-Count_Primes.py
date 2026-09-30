"""
- array
- Sieve of Eratosthenes
- O(nloglogn)), O(n)
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        
        sieves = [1] * n
        sieves[0] = sieves[1] = 0
        for l in range(2, int(sqrt(n)) + 1):
            if sieves[l]:
                for k in range(l*2, n, l):
                    sieves[k] = 0
        return sum(sieves)