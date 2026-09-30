"""
- dfs
- O(V + E), O(V + E)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visited = {}
        
        for c, pre in prerequisites:
            graph[pre].append(c)
            
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = False # for detecting cycles
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visited[node] = True
            return True
        
        return all(dfs(c) for c in range(numCourses))
        
"""
- topological sort with BFS
- O(V + E), O(V + E)
- intuition: the start node has to have 0 incoming. remove start node from graph (all its neighbors' incoming nodes -1) and do it recursively
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        taken = 0
        
        graph = defaultdict(set)
        for c, pre in prerequisites:
            graph[pre].add(c)
            indegree[c] += 1
            
        q = [c for c in range(numCourses) if indegree[c] == 0]
        while q:
            c = q.pop(0)
            taken += 1
            for nei_c in graph[c]:
                if indegree[nei_c]: # skip if already taken
                    indegree[nei_c] -= 1
                    if indegree[nei_c] == 0:
                        q.append(nei_c)
        
        return taken == numCourses

sl = Solution()
print(sl.canFinish(3, [[1,0],[1,2],[0,1]]))