"""
- bfs + bitmask serialization
- caveat: 1 <= m, n <= 3, so storing all states of mat is not impossible
"""
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        ser = self.serialize(mat, M, N)
        q = deque([(ser, 0)]) # serialized mat, steps
        visited = set(ser)
        
        while q:
            ser, steps = q.popleft()
            if sum(ser) == 0:
                return steps
            for r in range(M):
                for c in range(N):
                    new_ser = list(ser)
                    for i, j in [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]: # easy to miss: also need to flip itself
                        nr, nc = r + i, c + j
                        if 0 <= nr < M and 0 <= nc < N:
                            self.flip(new_ser, nr, nc)
                    if tuple(new_ser) not in visited:
                        q.append((new_ser, steps + 1))
                        visited.add(tuple(new_ser))
        return -1
    
    def flip(self, ser_list, r, c):
        ser_list[r] ^= (1 << c)
        
    def serialize(self, mat, m, n):
        ser = [0] * m
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    ser[i] |= (1 << j)
        return ser