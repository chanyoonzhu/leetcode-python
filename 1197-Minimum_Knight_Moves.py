"""
- BFS
- O(max(abs(x)^2, abs(y)^2)), O(max(abs(x)^2, abs(y)^2))
"""
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque()
        q.append((0, 0, 0)) # x, y, step
        visited = set()
        visited.add((0, 0))
        DIR = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        while q:
            i, j, step = q.popleft()
            if (i, j) == (x, y):
                return step
            for inc_i, inc_j in DIR:
                ni, nj = i + inc_i, j + inc_j
                if (ni, nj) not in visited:
                    q.append((ni, nj, step + 1))
                    visited.add((ni, nj))

"""
- bidirectional BFS
- O(max(abs(x)^2, abs(y)^2)), O(max(abs(x)^2, abs(y)^2))
"""
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0
        pos1, pos2 = set(), set() # pos from target, pos from origin
        step = 0
        pos2.add((x, y))
        pos1.add((0, 0))
        visited = set()
        visited.add((0, 0))
        visited.add((x, y))
        DIR = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        
        while True:
            if len(pos2) < len(pos1): # search from smaller set
                pos1, pos2 = pos2, pos1
            new_pos1 = set()
            while pos1:
                r, c = pos1.pop()
                for i, j in DIR:
                    nr, nc = r + i, c + j
                    if (nr, nc) in pos2:
                        return step + 1
                    if (nr, nc) not in visited:                            
                        new_pos1.add((nr, nc))
                        visited.add((nr, nc))
            step += 1
            pos1 = new_pos1
        
        
            
        
        