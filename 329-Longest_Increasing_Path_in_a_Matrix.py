"""
- dfs with memoization
- note: path is strictly increasing -> no loop -> DAG -> can use dfs
- O(mn), O(mn)
"""
class Solution:
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(x, y, longest):
            for i, j in move:
                x_next = x + i
                y_next = y + j
                if 0 <= x_next < n and 0 <= y_next < m and matrix[x_next][y_next] > matrix[x][y]:
                    next_longest_path = longest_paths[x_next][y_next] if (x_next, y_next) in visited else dfs(x_next, y_next, 1)
                    longest = max(longest, next_longest_path + 1)
            visited.add((x, y))
            longest_paths[x][y] = longest
            return longest
            
        
        n, m = len(matrix), len(matrix[0])
        longest_paths = [[1] * m for _ in range(n)]
        visited = set()
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = 0
        
        for i in range(n):
            for j in range(m):
                result = max(result, dfs(i, j, 1))
        return result
    
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