"""
- dfs
- O(n^n+ElogE) E:the length of times; O(N+E)
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        dists = [0] + [float("inf")] * n
        
        def dfs(node, dist):
            if dist >= dists[node]: return
            dists[node] = dist
            for w, v in sorted(graph[node]):
                dfs(v, dist + w)
        
        dfs(k, 0)
        result = max(dists)
        return result if result < float("inf") else -1

"""
- bfs (Dijkstra's Algorithm) + queue
- O(ElogE) E:the length of times; O(N+E)
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = [0] + [float("inf")] * n
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        while heap:
            dist, node = heapq.heappop(heap)
            if dist < dists[node]:
                dists[node] = dist
                for v, w in graph[node]:
                    heapq.heappush(heap, (dist + w, v))
        result = max(dists)
        return result if result < float("inf") else -1