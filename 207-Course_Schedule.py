"""
- dfs
- O(V + E), O(V + E)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        can_take = {}
        graph = collections.defaultdict(list)
        for c, pre in prerequisites:
            graph[c].append(pre)
            
        def dfs(c):
            if c in can_take:
                return can_take[c]
            can_take[c] = False
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            can_take[c] = True
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True
        # return all(dfs(i) for i in range(numCourses))
        
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