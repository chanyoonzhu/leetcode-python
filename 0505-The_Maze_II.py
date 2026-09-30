"""
- bfs
- O(mn), O(mn)
"""
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        M, N = len(maze), len(maze[0])
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = collections.deque()
        visited = set()
        start_x, start_y = start
        for direction in range(4):
            q.append((start_x, start_y, direction, 0)) # one state for each direction
            visited.add((start_x, start_y, direction))
            
        def isWall(x, y):
            if x < 0 or x >= M:
                return True
            if y < 0 or y >= N:
                return True
            if maze[x][y] == 1:
                return True
            return False
        
        def canVisit(x, y, prev_d, d):
            nonlocal M, N
            next_x, next_y = x + DIRECTIONS[prev_d][0], y + DIRECTIONS[prev_d][1]
            if isWall(next_x, next_y): # should make a turn if following previous direction ends up in a wall
                if d == prev_d:
                    return False
                else:
                    return canVisit(x, y, d, d) # made a turn
            else: # should follow previous direction
                return prev_d == d and not isWall(next_x, next_y) and (next_x, next_y, d) not in visited
        
        while q:
            x, y, prev_d, step = q.popleft()
            if [x, y] == destination and isWall(x + DIRECTIONS[prev_d][0], y + DIRECTIONS[prev_d][1]): # must stop at destination
                return step
            for d in range(4):
                if canVisit(x, y, prev_d, d):
                    xx, yy = x + DIRECTIONS[d][0], y + DIRECTIONS[d][1]
                    visited.add((xx, yy, d))
                    q.append((xx, yy, d, step + 1))
        return -1

"""
- todo: Dijkstra's Algorithm
"""