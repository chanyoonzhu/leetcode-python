"""
- topological sort
"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = collections.defaultdict(set)
        indegrees = [0] * numCourses
        pres = [set() for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            graph[pre].add(course)
            indegrees[course] += 1
            pres[course].add(pre)
        
        q = [i for i, ind in enumerate(indegrees) if not ind]
        while q:
            pre = q.pop(0)
            for course in graph[pre]:
                pres[course] |= pres[pre] # progressively add prereqs into sets
                indegrees[course] -= 1
                if indegrees[course] == 0: q.append(course)
        
        return [pre in pres[course] for pre, course in queries]

"""
- dfs
- O(E * n ^ 2)?, O(n ^ 2)
"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = collections.defaultdict(set)
        for pre, course in prerequisites:
            graph[pre].add(course)

        @lru_cache(None)
        def dfs(c1, c2):
            if c1 == c2 or c1 not in graph: return False
            if c1 < 0 or c1 >= numCourses or c2 < 0 or c2 >= numCourses: return False
            for n in graph[c1]:
                if n == c2 or dfs(n, c2): return True
            return False
        
        return [dfs(pre, course) for pre, course in queries]