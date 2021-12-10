"""
- dfs
- O(VE), O(VE)
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        def findHeight(v, visited):
            if v in visited:
                return 0
            visited.add(v)
            height = 0
            for nv in graph[v]:
                height = max(height, findHeight(nv, visited))
            return 1 + height
            
        heights = [0] * n
        for v in range(n):
            heights[v] = findHeight(v, set())
        
        return [i for i, height in enumerate(heights) if height == min(heights)]

"""
- topological sort
- O(v), O(v)
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        
        graph = defaultdict(set)
        indegrees = [-1] * n
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            indegrees[v1] += 1
            indegrees[v2] += 1
            
        leaves = [v for v in range(n) if not indegrees[v]]
        
        nodes_remain = n
        while nodes_remain > 0:
            nodes_remain -= len(leaves)
            newLeaves = []
            for v in leaves:
                for nv in graph[v]:
                    indegrees[nv] -= 1
                    if indegrees[nv] == 0:
                        newLeaves.append(nv)
            prev_leaves = leaves
            leaves = newLeaves
        return prev_leaves