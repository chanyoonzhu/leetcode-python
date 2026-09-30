"""
- bfs
- search from gates
- O(mn), O(mn)
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        M, N = len(rooms), len(rooms[0])
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c):
            q = deque([(r, c, 0)])# r, c, step
            while q:
                x, y, step = q.popleft()
                for i, j in DIR:
                    nx, ny = x + i, y + j
                    if 0 <= nx < M and 0 <= ny < N and rooms[nx][ny] > step + 1:
                        rooms[nx][ny] = step + 1
                        q.append((nx, ny, step + 1))
            
    
        for r in range(M):
            for c in range(N):
                if rooms[r][c] == 0:
                    bfs(r, c)
            
        