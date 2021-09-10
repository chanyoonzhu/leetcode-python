"""
- union find
"""
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        primesToNums = collections.defaultdict(list)
        
        parents = [i for i in range(len(nums))]
        
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        
        def union(i1, i2):
            p1, p2 = find(i1), find(i2)
            if p1 != p2:
                parents[p1] = p2
                
        def getPrimes(n): # smart recursion
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return getPrimes(n // i) | set([i])
            return set([n]) 
                    
        for i, n in enumerate(nums):
            primes = getPrimes(n)
            for p in primes:
                primesToNums[p].append(i)
            
        for _, indexes in primesToNums.items():
            for i in range(1, len(indexes)):
                union(indexes[i - 1], indexes[i])
                
        return max(collections.Counter([find(i) for i in range(len(parents))]).values())