"""
- Union Find
"""
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        time_to_meetings = defaultdict(set)
        for x, y, time in meetings:
            time_to_meetings[time].add((x, y))
        
        uf = UnionFind(n)
        res = [0]
        uf.union(0, firstPerson) # easy to miss
        
        for time in sorted(time_to_meetings.keys()): # handle smaller time first
            for x, y in time_to_meetings[time]:
                uf.union(x, y)
            uf.trimOther(0) # easy to miss: reset parent to itself if not connected to 0
        
        for i in range(1, n):
            if uf.find(i) == 0:
                res.append(i)
                
        return res

class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        
    def find(self, n):
        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if px < py:
                self.parents[py] = px
            else:
                self.parents[px] = py
    
    def trimOther(self, x):
        for i in range(len(self.parents)):
            if self.find(i) != self.find(x):
                self.parents[i] = i
        
        