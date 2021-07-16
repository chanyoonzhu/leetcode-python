"""
- dfs
- O(V^2⋅K), O(V⋅K+V^2)
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapest = float("inf")
        
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        
        @lru_cache(None)
        def dfs(s, k):
            if k < 0: return float("inf")
            if s == dst: return 0
            cost = float("inf")
            for neighbor, p in graph[s]:
                cost = min(cost, p + dfs(neighbor, k - 1))
            return cost
        
        cheapest = dfs(src, k + 1)
        
        return cheapest if cheapest < float("inf") else -1

"""
- Dijkstra's Algorithm (bfs + queue)
- O(V^2*logV), O(V^2)
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = collections.defaultdict(dict)
        for s, d, p in flights:
            graph[s][d] = p
        
        q = [(0, src, k + 1)]
        while q:
            p, loc, k = heapq.heappop(q)
            if loc == dst: return p
            if k > 0:
                for i in graph[loc]:
                    heapq.heappush(q, (p + graph[loc][i], i, k - 1))
        
        return -1