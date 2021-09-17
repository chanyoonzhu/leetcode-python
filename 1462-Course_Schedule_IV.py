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