"""
- 2D array (simulation)
"""
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        GO_UP = True
        start_r, start_c = 0, 0 # start pos of each traversal
        direction = GO_UP
        
        M, N = len(mat), len(mat[0])
        res = []
        
        def isValid(r, c):
            return 0 <= r < M and 0 <= c < N
        
        def findNextStart(r, c):
            if c == N - 1:
                return r + 1, c
            elif r == 0 or r == M - 1:
                return r, c + 1
            elif c == 0:
                return r + 1, c
        
        while isValid(start_r, start_c):
            # traverse through diagonal
            res.append(mat[start_r][start_c])
            i, j = (-1, 1) if direction == GO_UP else (1, -1)
            next_r, next_c = start_r + i, start_c + j
            while isValid(next_r, next_c):
                res.append(mat[next_r][next_c])
                next_r += i
                next_c += j
            # update the next start and the direction
            start_r, start_c = findNextStart(next_r - i, next_c - j)
            direction = not direction
        return res

"""
- hashmap (index sum: i + j as key)
- O(mn), O(mn)
"""
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        sum_to_cells = defaultdict(list)
        M, N = len(mat), len(mat[0])
        direction = True
        for r in range(M):
            for c in range(N):
                sum_to_cells[r+c].append(mat[r][c])
        
        res = []
        for sum_ in range(M + N - 1):
            if direction == True:
                res.extend(sum_to_cells[sum_][::-1])
            else:
                res.extend(sum_to_cells[sum_])
            direction = not direction
        return res