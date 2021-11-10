"""
- backtracking
- TLE
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        M, N = len(bikes), len(workers)
        
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)
        
        bikes_used = [0] * M
        
        def backtrack(i):
            if i == N:
                return 0
            min_dist = float("inf")
            for j in range(M):
                if not bikes_used[j]:
                    bikes_used[j] = 1
                    min_dist = min(min_dist, dist(workers[i], bikes[j]) + backtrack(i + 1))
                    bikes_used[j] = 0
            return min_dist
        
        return backtrack(0)

"""
- backtracking with pruning
- TLE
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        M, N = len(bikes), len(workers)
        min_dist_sum = float("inf")
        
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)
        
        bikes_used = [0] * M
        
        def backtrack(i, cur_sum):
            nonlocal min_dist_sum
            if i == N:
                min_dist_sum = min(min_dist_sum, cur_sum)
                return
            if cur_sum >= min_dist_sum: # return if current_sum is larger than the minimal sum previously found
                return
            for j in range(M):
                if not bikes_used[j]:
                    bikes_used[j] = 1
                    backtrack(i + 1, cur_sum + dist(workers[i], bikes[j]))
                    bikes_used[j] = 0
        
        backtrack(0, 0)
        return min_dist_sum

"""
- dp + bitmasking
- further improvement: cache worker to bike dist in a m*n array
- (2^m*mn)
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        M, N = len(bikes), len(workers)
        
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)
                
        @lru_cache
        def dp(i, bit_state):
            if i == N:
                return 0
            min_dist = float("inf")
            for j, bike in enumerate(bikes):
                if bit_state & (1<<j): # 1 - bike can be picked
                    min_dist = min(min_dist, dist(workers[i], bike) + dp(i + 1, bit_state ^ (1<<j)))
            return min_dist
                        
        return dp(0, (1<<M) - 1)

# todo: Dijkstra