import collections

"""
- dfs
- O(n^2), O(n)
"""
class Solution(object):
    def validTree(self, n, edges):

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        visited = set()
        
        def has_cycle(x, prev):
            visited.add(x)
            for nei in graph[x]:
                if nei != prev: # easy to miss
                    if nei in visited:
                        return False
                    else:
                        has_cycle(nei, x)
            return True
        
                
        if not has_cycle(0, -1): # test no cycle
            return sum(visited) == n
        return False

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