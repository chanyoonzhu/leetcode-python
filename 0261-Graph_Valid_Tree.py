import collections

"""
- dfs
- O(V+E), O(V+E)
"""
class Solution(object):
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for v, u in edges:
            graph[v].add(u)
            graph[u].add(v)
            
        visited = set()
        
        # check cycle
        if not self.hasNoCycle(0, -1, visited, graph):
            return False

        # check not connect
        return len(visited) == n
    
    # return False if cycle
    def hasNoCycle(self, v, prev_v, visited, graph):
        if v in visited:
            return False
        visited.add(v)
        for nei in graph[v]:
            if nei != prev_v and not self.hasNoCycle(nei, v, visited, graph): # easy to miss: need to exclude prev node (don't go back)
                return False
        return True

"""
- union find
- O(n), O(n)
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        parents = [i for i in range(n)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            pa, py = find(x), find(y)
            if pa == py:
                return True
            parents[pa] = py
            return False
        
        # test cycle
        for u, v in edges:
            if union(u, v):
                return False
        
        # test all connected
        # can use "if len(edges) != n - 1: return False" to replace the following block
        prev_p = find(0)
        for p in parents:
            if find(p) != prev_p:
                return False
            
        return True
            
        
        

sl = Solution()
print(sl.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))