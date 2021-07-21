# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

"""
- dfs (map grid) + bfs (find shortest path)
- O(m * n), O(m * n)
- https://tinyurl.com/26nv4tbs
"""
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        back = {"U": "D", "D": "U", "L": "R", "R": "L"}
        isValid = {}
        isValid[(0, 0)] = master.isTarget()
        
        def dfs(r, c):
            for d in dirs:
                nr, nc = r + dirs[d][0], c + dirs[d][1]
                if (nr, nc) not in isValid and master.canMove(d):
                    master.move(d)
                    isValid[(nr, nc)] = master.isTarget()
                    dfs(nr, nc)
                    master.move(back[d]) # move back
            
        dfs(0, 0)
        
        q = [(0, 0, 0)]
        visited = set((0, 0))
        while q:
            r, c, dist = q.pop(0)
            if isValid[(r, c)]:
                return dist
            for d in dirs:
                nr, nc = r + dirs[d][0], c + dirs[d][1]
                if (nr, nc) not in visited and (nr, nc) in isValid:
                    q.append((nr, nc, dist + 1))
                    visited.add((nr, nc))
        return -1