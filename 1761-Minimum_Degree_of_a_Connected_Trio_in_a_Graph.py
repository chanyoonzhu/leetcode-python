"""
- hashmap
- O(v^3), O(v + e)
"""
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list) # single-direction graph (smaller as key, larger as value)
        bi_graph = defaultdict(set) # bi-direction graph
        for u, v in edges:
            if u > v:
                u, v = v, u
            graph[u].append(v)
            bi_graph[u].add(v)
            bi_graph[v].add(u)
            
        min_degree = float("inf")
        
        def calc_degree(v1, v2, v3):
            return len(bi_graph[v1]) + len(bi_graph[v2]) + len(bi_graph[v3]) - 3 * 2
        
        for i in range(n):
            graph[i] = sorted(graph[i]) # faster
            for j in range(len(graph[i])):
                for k in range(j+1, len(graph[i])):
                    u, v = graph[i][j], graph[i][k]
                    if v in bi_graph[u]:
                        min_degree = min(min_degree, calc_degree(i, u, v))
        return min_degree if min_degree < float("inf") else -1                   
                        
        