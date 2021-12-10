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
        
        indegrees = [0] * numCourses
        graph = defaultdict(set)
        for c, pre in prerequisites:
            graph[pre].add(c)
            indegrees[c] += 1
        
        q = [c for c in range(numCourses) if not indegrees[c]]
        while q:
            c = q.pop(0)
            for nc in graph[c]:
                indegrees[nc] -= 1
                if indegrees[nc] == 0:
                    q.append(nc)
        
        return not any(indegrees)

sl = Solution()
print(sl.canFinish(3, [[1,0],[1,2],[0,1]]))