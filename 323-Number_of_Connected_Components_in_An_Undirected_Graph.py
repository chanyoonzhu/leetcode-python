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
        uf = UnionFind(n)
        for v1, v2 in edges:
            uf.union(v1, v2)
        
        return len({uf.find(v) for v in range(n)})
            
    
class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if px < py:
                self.parents[py] = px
            else:
                self.parents[px] = py

print(Solution().countComponents(4,
[[0,1],[2,3],[1,2]]))