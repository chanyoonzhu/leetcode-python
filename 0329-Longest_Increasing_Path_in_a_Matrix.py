"""
- dfs with memoization
- note: path is strictly increasing -> no loop -> DAG -> can use dfs
- O(mn), O(mn)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.res = 0
        for r in range(self.m):
            for c in range(self.n):
                self.dfs(r, c)
        return self.res
        
    @lru_cache(None)
    def dfs(self, r, c):
        connected = 0
        for i, j in self.dir:
            nr, nc = r + i, c + j
            if 0 <= nr < self.m and 0 <= nc < self.n and self.matrix[nr][nc] > self.matrix[r][c]:
                connected = max(connected, self.dfs(nr, nc))
        connected += 1 # itself
        self.res = max(self.res, connected)
        return connected
    
"""
- topological sorting
- O(mn), O(mn)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        indegrees = [[0] * N for _ in range(M)]
        
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(M):
            for c in range(N):
                for i, j in DIR:
                    nr, nc = r + i, c + j
                    if 0 <= nr < M and 0 <= nc < N and matrix[nr][nc] > matrix[r][c]:
                        indegrees[r][c] += 1
        
        q = deque()
        for r in range(M):
            for c in range(N):
                if indegrees[r][c] == 0:
                    q.append((r, c))
        
        steps = 0
        while q:
            new_q = deque()
            while q:
                r, c = q.popleft()
                for i, j in DIR:
                    nr, nc = r + i, c + j
                    if 0 <= nr < M and 0 <= nc < N and matrix[nr][nc] < matrix[r][c]:
                        indegrees[nr][nc] -= 1
                        if indegrees[nr][nc] == 0:
                            new_q.append((nr, nc))
            q = new_q
            steps += 1
        return steps