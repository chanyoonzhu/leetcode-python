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
        
        visited = set()
        graph = defaultdict(set)
        for u, v, t in times:
            graph[u].add((v, t))
        
        h = [(0, k)] # time, node
        while h:
            # bfs
            accumulative_time, v = heapq.heappop(h) # greedily pop the smallest time(accumulated)
            visited.add(v)
            if len(visited) == n:
                return accumulative_time
            for nei, time in graph[v]:
                if nei not in visited:
                    heapq.heappush(h, (accumulative_time + time, nei))
            
        return -1