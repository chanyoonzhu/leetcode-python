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
- caveat: why cannot use visited hashset? because need to consider number of stops:
 path that uses fewer price may need more stops, visited eliminates other paths that use more price but with less stops
- O(V^2*logV), O(V^2)
- TLE
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

"""
- Dijkstra's Algorithm (bfs + queue) - optimized
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(set)
        for from_, to, p in flights:
            graph[from_].add((to, p))
            
        min_dists = [float("inf")] * n
        min_stops = [float("inf")] * n
        h = [(0, 0, src)] # total_price, stops, node
        res = float("inf")
        while h:
            total, stops, node = heapq.heappop(h)
            min_dists[node] = min(min_dists[node], total)
            min_stops[node] = min(min_stops[node], stops)
            if node == dst:
                return total
            if stops <= k:
                for nei, p in graph[node]:
                    if total + p < min_dists[nei] or stops + 1 < min_stops[nei]: # only push when price is smaller or stops are fewer
                        heapq.heappush(h, (total + p, stops + 1, nei))
        return -1 if res == float("inf") else res