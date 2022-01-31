"""
- graph
- O(n^2)
- optimization: find city with max and second max roads (caveat: may have many pairs, some pair have connections)
"""
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for v, u in roads:
            graph[v].add(u)
            graph[u].add(v)
        
        res = 0
        for v in graph:
            for u in graph:
                if v != u:
                    rank = len(graph[v]) + len(graph[u])
                    if u in graph[v]:
                        rank -= 1
                    res = max(res, rank)
        return res