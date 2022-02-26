"""
- dynamic programming
- similar: increasing subsequence with largest sum
- intuition: any compatible chain of cuboids can be transformed into another chain with the same cuboids, but each cuboid has its largest edge as the height w/o violating compatibility
"""
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        
        cubes = sorted(map(sorted, cuboids)) # rotate by sort
        N = len(cubes)
        
        @lru_cache(None)
        def dp(i):
            if i == N:
                return 0
            height = cubes[i][2]
            for j in range(i+1, N):
                if all(cubes[j][k] >= cubes[i][k] for k in range(3)):
                    height = max(height, cubes[i][2] + dp(j)) # greedily use largest side as height
            return height
        
        return max(dp(i) for i in range(N))