"""
- todo: bfs, dfs
"""

"""
- union find
- time: O(E⋅α(n)) E = Number of edges, V = Number of vertices. Iterating over every edge requires O(E) operations, and for every operation, we are performing the combine method which is O(α(n)), where α(n) is the inverse Ackermann function.
    space: O(V)
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y): # union by rank
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] > rank[ry]:
                parents[ry] = rx
            elif rank[rx] < rank[ry]:
                parents[rx] = ry
            else:
                parents[rx] = ry
                rank[ry] += 1
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})

print(Solution().countComponents(4,
[[0,1],[2,3],[1,2]]))