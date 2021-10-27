"""
- dfs
- O(n^2), O(n)
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        self.graph = defaultdict(list)
        for u, v in edges:
            self.visited = set()
            if self.is_connected(u, v):
                return [u, v]
            self.graph[u].append(v)
            self.graph[v].append(u)
            
    def is_connected(self, u, v):
        if u == v:
            return True
        for nei in self.graph[u]:
            if nei not in self.visited:
                self.visited.add(nei)
                if self.is_connected(nei, v):
                    return True
        return False

"""
- union find
- O(n), O(n)
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [i for i in range(len(edges) + 1)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return True # already connected
            parents[px] = py
            return False
        
        for u, v in edges:
                        
            if union(u, v):
                return [u, v]