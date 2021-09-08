"""
- Union Find
- Key observation: If (0, 1) is exchangeable and (0, 2) is exchangeable, then any pair in (0, 1, 2) can be exchangeble
"""
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        n = len(source)
        parents = [i for i in range(n)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            if parents[x] != parents[y]:
                parents[find(x)] = find(y)
        
        for x, y in allowedSwaps: # connect swappable parts
            union(x, y)
        m = collections.defaultdict(set) # store each swappable part as a set in a map
        for i in range(n):
            m[find(i)].add(i)
        result = 0
        for indices in m.values(): # compute the Hamming distance of each swappable parts
            A = [source[i] for i in indices]
            B = [target[i] for i in indices]
            result += sum((Counter(A) - Counter(B)).values())
        return result
        