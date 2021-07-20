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
        edges = collections.defaultdict(list)
        degrees = [0] * numCourses
        for c, pre in prerequisites:
            edges[pre].append(c)
            degrees[c] += 1

        q = [course for course, degree in enumerate(degrees) if not degree]
        while q:
            course = q.pop(0)
            for next_course in edges[course]:
                degrees[next_course] -= 1
                if not degrees[next_course]:
                    q.append(next_course)

        return not sum(degrees)

sl = Solution()
print(sl.canFinish(3, [[1,0],[1,2],[0,1]]))