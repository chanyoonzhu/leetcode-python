"""
- dfs
- O(V + E), O(V + E)
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use DFS to parse the course structure
        graph = collections.defaultdict(list) # a graph for all courses
        res = []
        
        for c, pre in prerequisites:
            graph[c].append(pre) 
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = False
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visited[node] = True
            res.append(node)
            return True
        
        for x in range(numCourses):
            if not dfs(x):
                return []
        return res

"""
- topological sort with BFS
- O(V + E), O(V + E)
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        result = []
        
        for c, pre in prerequisites:
            graph[pre].append(c)
            indegree[c] += 1
            
        q = [c for c, degree in enumerate(indegree) if degree == 0]
        while q:
            c = q.pop(0)
            result.append(c)
            for next_c in graph[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    q.append(next_c)
        
        return result if len(result) == numCourses else []

print(Solution().findOrder(2, [[1,0]] ))