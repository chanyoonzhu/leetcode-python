"""
- bfs + bitmask serialization
- caveat: 1 <= m, n <= 3, so storing all states of mat is not impossible
"""
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        bitmask = [1 << i for i in range(len(mat[0]))]
        M, N = len(mat), len(mat[0])
        q = collections.deque()
        q.append((mat, 0))
        visited = set()
        visited.add(self.serialize(mat, M, N, bitmask))
        
        while q:
            cur_mat, steps = q.popleft()
            if sum([sum(row) for row in cur_mat]) == 0:
                return steps
            for r in range(M):
                for c in range(N):
                    next_mat = [row[:] for row in cur_mat]
                    for rr, cc in [(r, c), (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if 0 <= rr < M and 0 <= cc < N:
                            next_mat[rr][cc] = 1 - next_mat[rr][cc]
                    serialized_mat = self.serialize(next_mat, M, N, bitmask)
                    if serialized_mat not in visited:
                        q.append((next_mat, steps + 1))
                        visited.add(serialized_mat)
        return -1
    
    def serialize(self, mat, M, N, bitmask):
        serialized = []
        for i in range(M):
            serialized_row = 0
            for j in range(N):
                if mat[i][j]:
                    serialized_row |= bitmask[j]
            serialized.append(serialized_row)
        return tuple(serialized)